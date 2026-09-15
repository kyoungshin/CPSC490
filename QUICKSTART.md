# Quick start — one hour, start to finished setup

**Read this page first.** It is the whole setup, in order, as commands and
clicks. Everything else in this repository is reference material you read
when you need it (map at the bottom).

Do steps 1–4 together as a team in one sitting. One person drives; everyone
watches, because everyone has to work in this repo.

---

## 1. Leader: create the repository (5 min)

1. GitHub → **New repository**
2. Name: `CPSC490-G<number>-<groupname>` — e.g. `CPSC490-G03-California`
3. **Private**, and check **Add a README file**
4. Create it.

## 2. Leader: add your team and the instructor (2 min)

**Settings → Collaborators → Add people** — add every teammate's GitHub
username, then add **`kyoungshin`** (required, so your work can be graded).

## 3. Leader: copy the scaffolding from this example repo (10 min)

Download this example repo (green **Code** button → **Download ZIP**) and
copy these into your new repository, then commit:

| Copy this | To | What it is |
|---|---|---|
| `README_TEMPLATE.md` | your `README.md` | your team's front page — fill in the 〈brackets〉 |
| `CLAUDE.md` | `CLAUDE.md` | shared AI context — fill in the 〈brackets〉 |
| `proposal/proposal.md` | `proposal/proposal.md` | the proposal skeleton (already matches the Word template) |
| `.github/` (whole folder) | `.github/` | issue + PR templates, CI workflow, the harness script |
| `docs/` (whole folder) | `docs/` | reference docs, diagram guide, sprint-review template |
| `prototype/` | `prototype/` | the runnable starter — replace the code with yours |

```bash
git add -A && git commit -m "chore: course scaffolding" && git push
```

## 4. Leader: set up branches, labels, milestones, board (20 min)

**Branches** — create `develop` and protect both:

```bash
git switch -c develop && git push -u origin develop
```

Then **Settings → Branches → Add branch ruleset**, once for `main` and once
for `develop`:
- Require a pull request before merging
- Require approvals: **1**
- Dismiss stale approvals when new commits are pushed
- Require status checks: `Repository harness (G1–G6)`, `Prototype build & tests`, `PR links an issue and discloses AI use`
- Require branches to be up to date before merging
- Block force pushes

**Labels** — Issues → Labels → New label. Create exactly these:

```
epic  user-story  feature  enhancement  bug  task  sub-task
priority: high   priority: medium   priority: low
loe: S   loe: M   loe: L
sp: 1   sp: 2   sp: 3   sp: 5   sp: 8
```

**Milestones** — Issues → Milestones → New milestone: `Sprint 1` … `Sprint 4`
with the due dates from the setup guide §6.

**Board** — Projects → New project → **Board**:
- Status column values: `Backlog`, `Sprint To-Do`, `In Progress`, `In Review`, `Done`
- add a **number** field named `Story Points`
- add an **iteration** field named `Sprint` with four 2-week iterations
- paste the board URL into your README

## 5. Everyone: file your goals and objectives as issues (30 min)

From your proposal's *Goals and Objectives*:

- one **epic** issue per goal (label `epic`)
- one **user-story** issue per objective (label `user-story`), each with
  **assignee, milestone, `priority:`, `loe:`, story points, and acceptance
  criteria** — filled in when the story enters a sprint, not later
- list the story numbers in the epic body as `- [ ] #12` so progress shows
- link every epic and story from proposal §2, and every task/bug/feature
  from proposal §4

## 6. Everyone: make your first real pull request (15 min)

```bash
git switch develop && git pull
git switch -c feature/<issue-number>-<short-slug>
# ...do the work...
python .github/scripts/check_repo.py        # the harness — must be green
git push -u origin HEAD
```

Open the PR against `develop`, fill in the template (link the story, say
what you verified, disclose AI use), and have **a teammate who is not the
author** approve it. Green CI + one approval → squash merge.

That is the loop you will repeat all semester.

---

## What to read, and when

| When | Read |
|---|---|
| Before Sprint 1, everyone | [`docs/aidlc/hitl-gates.md`](docs/aidlc/hitl-gates.md) — the seven gates and the LLM failure each one catches |
| Before you first use an LLM on this project | [`docs/aidlc/prompt-library.md`](docs/aidlc/prompt-library.md) — the standard prompts |
| Before your first PR | [`docs/git-workflow.md`](docs/git-workflow.md) — Gitflow, CI, releases |
| When writing the proposal | [`README.md`](README.md) §3 and the skeleton in `proposal/proposal.md` |
| When you start design work | [`docs/design/DIAGRAMS.md`](docs/design/DIAGRAMS.md) — which diagram, which tool, where it lives |
| When something keeps going wrong | [`docs/aidlc/loop-engineering.md`](docs/aidlc/loop-engineering.md) — harness building and the stopping rules |
| At every sprint boundary | [`docs/sprint-reviews/sprint-1.md`](docs/sprint-reviews/sprint-1.md) — copy it for the new sprint |
| The full reference | [`README.md`](README.md) — the complete setup guide |

Stuck on tooling for more than 20 minutes? Ask in the course channel or at
the project meeting. Do not lose sprint days to setup.
