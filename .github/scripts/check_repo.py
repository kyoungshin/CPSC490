#!/usr/bin/env python3
"""CPSC 490 repository harness — the automated gates that check AI (and human)
output before a pull request can merge.

Each gate below exists because of a specific, observed LLM failure mode. Read
`docs/aidlc/hitl-gates.md` for the why; this file is the what.

    python .github/scripts/check_repo.py            # run all gates
    python .github/scripts/check_repo.py --strict   # warnings fail too

Standard library only, so it runs anywhere with Python 3.9+ and needs no
install step. GITHUB_TOKEN (provided automatically in Actions) enables the
issue-existence check; without it that gate is skipped, not failed.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# The 11 headings of the CPSC 490 proposal template, in order.
REQUIRED_PROPOSAL_HEADINGS = [
    "Abstract",
    "Introduction",
    "Related Work",
    "Problem Statements",
    "Goals and Objectives",
    "Proposed Approaches",
    "Required Environment, Resources, and Planned Activities",
    "Project Outcomes",
    "Project Timeline",
    "AI Usage",
    "References",
]

# Files that are meant to contain 〈placeholders〉 — templates and examples.
TEMPLATE_GLOBS = [
    "README_TEMPLATE.md",
    "CLAUDE.md",                     # copy-and-edit template
    ".github/**/*.md",
    "docs/aidlc/*.md",               # course reference material
    "docs/**/example-*.md",
    "docs/sprint-reviews/sprint-*.md",
    "proposal/proposal.md",
]

SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub personal access token"),
    (r"github_pat_[A-Za-z0-9_]{50,}", "GitHub fine-grained token"),
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style secret key"),
    (r"sk-ant-[A-Za-z0-9\-_]{20,}", "Anthropic API key"),
    (r"AIza[0-9A-Za-z\-_]{35}", "Google API key"),
    (r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----", "private key block"),
    (r"(?i)(password|passwd|secret|api[_-]?key)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]", "hardcoded credential"),
]

PLACEHOLDER_PATTERNS = [r"〈[^〉]{0,80}〉", r"\bTODO\b", r"\bFIXME\b", r"(?i)lorem ipsum"]

failures: list[str] = []
warnings: list[str] = []


def fail(gate: str, msg: str) -> None:
    failures.append(f"{gate}: {msg}")


def warn(gate: str, msg: str) -> None:
    warnings.append(f"{gate}: {msg}")


def md_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith((".git/", "node_modules/")):
            continue
        out.append(p)
    return sorted(out)


def is_template(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(rel.match(g) or rel.as_posix().startswith(g.split("**")[0].rstrip("/") + "/")
               and rel.match(g) for g in TEMPLATE_GLOBS) or any(rel.match(g) for g in TEMPLATE_GLOBS)


# ---------------------------------------------------------------- gate 1
def gate_proposal_structure() -> None:
    """G1 — the proposal still follows the course template.

    Catches: the assistant helpfully 'improving' the structure — renaming,
    merging, or dropping template sections. The template is the requirement.
    """
    g = "G1 template-structure"
    p = ROOT / "proposal" / "proposal.md"
    if not p.exists():
        fail(g, "proposal/proposal.md is missing")
        return
    text = p.read_text(encoding="utf-8", errors="replace")
    headings = [re.sub(r"\s+", " ", m.group(1)).strip()
                for m in re.finditer(r"^#{1,3}\s+(.+?)\s*$", text, re.M)]
    lowered = [h.lower() for h in headings]
    missing = [h for h in REQUIRED_PROPOSAL_HEADINGS if h.lower() not in lowered]
    if missing:
        fail(g, "proposal is missing required section(s): " + ", ".join(missing))
    # order check on the ones that are present
    present = [h for h in REQUIRED_PROPOSAL_HEADINGS if h.lower() in lowered]
    positions = [lowered.index(h.lower()) for h in present]
    if positions != sorted(positions):
        warn(g, "proposal sections are out of template order")
    if not failures:
        print(f"  {g}: all {len(REQUIRED_PROPOSAL_HEADINGS)} template sections present")


# ---------------------------------------------------------------- gate 2
def gate_traceability() -> None:
    """G2 — every spec/design document names the issue(s) it serves.

    Catches: orphan documents. An assistant asked to 'write the design doc'
    will happily produce work nobody planned, which then counts for nothing
    at the sprint review.
    """
    g = "G2 traceability"
    docs = [p for p in (ROOT / "docs").rglob("*.md")
            if p.parent.name in ("specs", "design")] if (ROOT / "docs").exists() else []
    if not docs:
        warn(g, "no documents in docs/specs or docs/design yet")
        return
    for p in docs:
        head = "\n".join(p.read_text(encoding="utf-8", errors="replace").splitlines()[:8])
        if not re.search(r"#\d+", head):
            fail(g, f"{p.relative_to(ROOT).as_posix()} does not name an issue in its first 8 lines "
                    f"(expected a line like '> Epic: #1 · Stories: #2, #3')")
    print(f"  {g}: checked {len(docs)} document(s)")


# ---------------------------------------------------------------- gate 3
def gate_issue_refs_exist() -> None:
    """G3 — issue numbers cited in documents actually exist.

    Catches: invented issue numbers. Models produce plausible-looking
    references (#42) with no hesitation; a citation that resolves to nothing
    is worse than no citation.
    """
    g = "G3 issue-refs"
    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")
    if not (repo and token):
        print(f"  {g}: skipped (no GITHUB_REPOSITORY/GITHUB_TOKEN — runs in CI)")
        return
    refs: dict[int, set[str]] = {}
    for p in md_files():
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(".github/") or rel in ("README.md", "README_TEMPLATE.md", "CLAUDE.md"):
            continue
        for m in re.finditer(r"(?<![\w/])#(\d{1,5})\b", p.read_text(encoding="utf-8", errors="replace")):
            refs.setdefault(int(m.group(1)), set()).add(rel)
    if not refs:
        print(f"  {g}: no issue references found")
        return
    bad: list[str] = []
    for num, where in sorted(refs.items()):
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/issues/{num}",
            headers={"Authorization": f"Bearer {token}", "User-Agent": "cpsc490-harness",
                     "Accept": "application/vnd.github+json"})
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                bad.append(f"#{num} (cited in {', '.join(sorted(where))})")
            else:
                warn(g, f"could not verify #{num}: HTTP {e.code}")
        except Exception as e:  # network trouble must not fail the build
            warn(g, f"could not verify #{num}: {e}")
    for b in bad:
        fail(g, f"cited issue does not exist: {b}")
    print(f"  {g}: verified {len(refs)} distinct issue reference(s)")


# ---------------------------------------------------------------- gate 4
def gate_links() -> None:
    """G4 — relative links point at files that exist.

    Catches: confident references to files the assistant never created, and
    paths that drifted after a rename.
    """
    g = "G4 links"
    broken = 0
    for p in md_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = m.group(1).strip()
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = (p.parent / target.split("#")[0]).resolve()
            if not str(path).startswith(str(ROOT)):
                continue
            if not path.exists():
                fail(g, f"{p.relative_to(ROOT).as_posix()} links to missing '{target}'")
                broken += 1
    if not broken:
        print(f"  {g}: all relative links resolve")


# ---------------------------------------------------------------- gate 5
def gate_secrets() -> None:
    """G5 — no credentials committed.

    Catches: the assistant pasting a working key into an example, and the
    classic 'just hardcode it for now'.
    """
    g = "G5 secrets"
    hits = 0
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if not p.is_file() or rel.startswith((".git/", "node_modules/")):
            continue
        if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".pptx", ".docx", ".xlsx", ".zip"):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern, label in SECRET_PATTERNS:
            for m in re.finditer(pattern, text):
                if "check_repo.py" in rel:  # this file lists the patterns
                    continue
                fail(g, f"possible {label} in {rel} (line {text[:m.start()].count(chr(10)) + 1})")
                hits += 1
    if not hits:
        print(f"  {g}: no credential patterns found")


# ---------------------------------------------------------------- gate 6
def gate_placeholders() -> None:
    """G6 — unfilled placeholders (warning).

    Not a hard failure: templates and examples are supposed to have them.
    But a document you claim is finished should not still say 〈…〉 or TODO,
    and reviewers use this list at the review gate.
    """
    g = "G6 placeholders"
    total = 0
    for p in md_files():
        if is_template(p):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        n = sum(len(re.findall(pat, text)) for pat in PLACEHOLDER_PATTERNS)
        if n:
            warn(g, f"{p.relative_to(ROOT).as_posix()} has {n} unfilled placeholder(s)/TODO(s)")
            total += n
    if not total:
        print(f"  {g}: no stray placeholders outside templates")


def main() -> int:
    strict = "--strict" in sys.argv
    print("CPSC 490 repository harness\n" + "=" * 34)
    for gate in (gate_proposal_structure, gate_traceability, gate_issue_refs_exist,
                 gate_links, gate_secrets, gate_placeholders):
        gate()
    print()
    for w in warnings:
        print(f"WARN  {w}")
    for f in failures:
        print(f"FAIL  {f}")
    print()
    if failures or (strict and warnings):
        print(f"HARNESS RED — {len(failures)} failure(s), {len(warnings)} warning(s).")
        print("Fix the cause, re-run, and say in your PR what you verified.")
        return 1
    print(f"HARNESS GREEN — 0 failures, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
