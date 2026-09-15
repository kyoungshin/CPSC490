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
