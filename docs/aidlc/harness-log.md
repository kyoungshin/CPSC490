# Harness log — every rule earns its place

One row per rule in our harness (CI check, `CLAUDE.md` line, issue-template
field, review habit), naming **the failure that caused it**. The rule is the
ratchet: once something goes wrong, we make it impossible to go wrong the
same way again.

A rule with no failure behind it is superstition — delete it. A failure with
no rule behind it will happen again — add one.

Bring this file to the sprint review. It is the cleanest evidence that the
team learned something, not just shipped something.

| Date | What went wrong (the failure) | Rule added | Where it lives | Added by |
|---|---|---|---|---|
| 2026-09-15 | *(example)* A design document cited issue `#42`, which never existed — the number was invented and nobody noticed for two days | Cited issue numbers are verified against the real issue list | CI gate G3 (`.github/scripts/check_repo.py`) | course scaffold |
| 2026-09-15 | **Real:** G3 failed in CI on `#12`/`#42`/`#123` cited inside the course reference docs that *explain* issue numbers — the gate was scoped too widely | Content gates (G3, G6) only inspect team deliverables (`proposal/`, `docs/specs/`, `docs/design/`, `docs/sprint-reviews/`) | `is_deliverable()` in the harness | course scaffold |
| 2026-09-15 | **Real:** the setup script's create paths had never been executed - only its skip paths - and a full run on a fresh private repo showed branch protection failing outright (GitHub forbids it on private repos on the free plan), which would have left every team's merge rule unenforced on day one | Test setup automation on a throwaway repo before handing it out; document the visibility/plan decision in QUICKSTART and git-workflow, and make the script say plainly that protection did not apply | `scripts/bootstrap.sh`, `QUICKSTART.md`, `docs/git-workflow.md` | course scaffold |
| 2026-09-15 | **Real:** CI reported "Prototype build & tests: success" while never running the tests — the glob `ls tests test_*.py **/test_*.py` failed because one pattern did not match, so the step silently skipped to the warning branch | Ask the tool, never a glob: run pytest and treat exit code 5 (no tests collected) as the only "nothing to run" case; check `package.json` scripts with node. **A gate that silently passes is worse than no gate.** | `.github/workflows/ci.yml` | course scaffold |
| 2026-09-15 | **Real:** re-running the setup script replaced the board's Status options, which assigns new option ids and silently cleared the Status of every card on the board | `bootstrap.sh` compares the existing Status options first and only replaces them when they differ; if it must replace them it warns that cards need re-setting | `scripts/bootstrap.sh` | course scaffold |
| 2026-09-15 | **Real:** G5 flagged a fake password in a prototype test as a committed credential | Secret scan honours an explicit `# pragma: allowlist secret` marker; every exemption is greppable for review | `gate_secrets()` in the harness | course scaffold |
| 2026-09-15 | **Real:** G4 reported a dead link that was a documented *example* inside a fenced code block | The link gate strips fenced code before scanning | `FENCE_RE` in the harness | course scaffold |
| 2026-09-15 | *(example)* A spec was written that no story asked for, and it scored nothing at the sprint review | Every spec/design doc must name its epic and stories in its first lines | CI gate G2 | course scaffold |
| | | | | |

## How to add a row

1. Something breaks, or review catches something that *almost* broke.
2. Ask: **what check would have caught this in under a minute?**
3. Prefer a deterministic check (CI, template field, type) over a prompt
   instruction — prompts are advisory, gates are enforced.
4. Add the check, add the row, and say in your PR which row it implements.

## Rules we considered and rejected

Keep this too — knowing what you decided *not* to gate is part of the
design, and it stops the harness from growing into something nobody runs.

| Rule considered | Why we rejected it |
|---|---|
| *(example)* Fail CI on any leftover `TODO` | Too noisy this early; kept it as a warning (G6) that reviewers read instead |
| | |
