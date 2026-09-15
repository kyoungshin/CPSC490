# CPSC 490 — Group Repository Setup Guide

> **This repository is itself the example.** It is laid out exactly the way
> your group repository should be — browse the folders, the issue templates,
> the labels, the `Sprint 1`–`Sprint 4` milestones, the sample issues (#1–#4),
> and the [CPSC490 project board](https://github.com/users/kyoungshin/projects/1)
> (Sprint Board + Sprint Plan table views; Status / Sprint / Story Points
> fields) — then build yours the same way. Your team README starts from
> [`README_TEMPLATE.md`](README_TEMPLATE.md). Start with §1 below.

**Fall 2026 · Prof. Kyoung Shin · Department of Computer Science, CSUF**

Every group runs its capstone like a real software project starting now.
CPSC 490 has **two deliverables that grow together all semester**: the
**project proposal** (with its specification and design documents) and a
**working prototype** — proof-of-concept code that de-risks the proposal
and evolves after every feedback round. Your team's GitHub repository holds
both, plus the issue board that shows who did what, when. In CPSC 491
(spring) the same repository carries you into full implementation, so set
it up right once.

> **Why this matters for your grade:** at each sprint checkpoint I review
> your repository directly — issues, board, documents, and pull requests —
> and score the team on five metrics (§7). A repo that makes your work
> visible is a repo that earns points.

---

## 1. Create the repository (leader, once — ~15 minutes)

1. Every member creates a **GitHub account** (free) with a recognizable
   username. Add your name to your GitHub profile.
2. The **group leader** creates ONE repository:
   - Name: `CPSC490-G<number>-<groupname>` (e.g. `CPSC490-G03-California`)
     — use your group number and name from the course group list.
   - Visibility: **Private**, unless the whole team prefers public.
   - Check "Add a README file".
3. Leader adds every member AND the instructor as collaborators:
   *Settings → Collaborators → Add people* — add each teammate's username
   and **`kyoungshin`** (instructor; required so I can grade).
4. Fill in the README (team contract, §2).
5. One member posts the repository URL where the course announces it
   (this was your HW#2 "Team GitHub repository URL" — keep it current if
   the repo moves).

**Every member must commit at least once in every sprint.** GitHub's
contributor graph is part of how individual participation is seen.

---

## 2. Repository layout

```
CPSC490-G03-California/
├── README.md               ← team + project one-pager (below)
├── proposal/
│   └── proposal.md         ← THE proposal, template §3 (single source of truth)
├── docs/
│   ├── specs/              ← specification documents (one .md per epic)
│   └── design/             ← design documents (architecture, UI, data, APIs)
│   └── sprint-reviews/     ← one file per sprint boundary (§6 ritual)
├── prototype/              ← prototype v0: running proof-of-concept (due Sep 27)
│   └── README.md           ← how to build/run it
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── epic.md         ← §5
    │   ├── user-story.md   ← §5
    │   ├── task.md         ← §5
    │   └── bug.md          ← §5
    └── PULL_REQUEST_TEMPLATE.md
```

**README.md** must contain: project title · sponsor code (e.g. RTX-3) if
sponsored · member table (name, GitHub username, role) · leader/contact ·
link to `proposal/proposal.md` · link to your Project board. **Start from
[`README_TEMPLATE.md`](README_TEMPLATE.md) in the example repository** —
copy it to your repo as `README.md` and fill in the 〈brackets〉.

---

## 3. The proposal (`proposal/proposal.md`)

Write the proposal in Markdown using **exactly the section headings of the
course template** (CPSC 490 Project Proposal Template Fall 2026):

1. Abstract
2. Introduction
3. Related Work
4. Problem Statements
5. **Goals and Objectives** ← this section drives your issue board (§4)
6. Proposed Approaches
7. Required Environment, Resources, and Planned Activities
8. Project Outcomes
9. Project Timeline
10. AI Usage
11. References

Two sections get special treatment:

- **Goals and Objectives** — write each *goal* as an **Epic** and each
  *objective* under it as a **User Story** (§4). In the proposal, list them
  with their issue numbers once created, e.g.
  `Goal 1: Secure account management (#1)` /
  `— Objective 1.1: As a user, I can register and log in (#2)`.
- **Project Timeline** — present the four 2-week sprints (§6) as a table:
  sprint, dates, the epics/stories planned in it.

The proposal you submit to Canvas (HW#4, the Word document following the
template) and `proposal.md` must say the same thing — the repo copy is the
living version you keep improving all semester; the Preview and Final
Project Proposal Papers grow out of it.

---

## 4. Epics and user stories on the issue board

CPSC 490 uses **GitHub Issues + one GitHub Projects board** (no Jira
needed; 491 teams may move to Jira later — the discipline is identical).

**Epic = a Goal.** One issue per goal from *Goals and Objectives*.
Label `epic`. An epic's body lists its user stories as a task list
(`- [ ] #12`) so progress is visible automatically.

**User story = an Objective.** One issue per objective, written in the
standard form: *"As a 〈who〉, I want 〈what〉, so that 〈why〉."*
Label `user-story`. Every story must have, from the moment it enters a
sprint:

| Field | How | Values |
|---|---|---|
| **Owner** | GitHub **Assignee** (exactly one) | a team member |
| **Sprint** | **Milestone** on the issue + the board's **Sprint iteration field** (keep both set — the milestone is what grading queries; the iteration drives the board's sprint view) | `Sprint 1` … `Sprint 4` |
| **Priority** | label | `priority: high / medium / low` |
| **Level of effort** | label | `loe: S / M / L` (≤½ day / ~1–2 days / needs splitting) |
| **Story points** | Projects board field (or `sp: n` label) | 1, 2, 3, 5, 8 |
| **Acceptance criteria** | issue body checklist | what "done" means, checkable |

**The full agile work-item taxonomy.** Epics and user stories are the two
types this course *requires*; the rest of the standard agile categories are
there when your work needs them (the labels exist in the example repo):

| Type label | What it is | Typical CPSC 490 use |
|---|---|---|
| `epic` | A **goal** — container of user stories | one per Goal in the proposal |
| `user-story` | An **objective** — user-visible value ("As a …") | one per Objective |
| `feature` | A new capability that delivers (part of) a story | prototype capabilities |
| `enhancement` | Improvement to something that already works | polish after check feedback |
| `bug` | Defect — built behavior ≠ spec | prototype defects |
| `task` | Concrete unit of work under a story/feature | "draft spec §3", "set up repo CI" |
| `sub-task` | Breakdown of a task — smallest tracked unit | child checklist items |

Hierarchy: **epic ⊃ user story ⊃ task ⊃ sub-task**, while
feature / enhancement / bug describe *what kind* of work an item is (an
item can carry both, e.g. `task` + `bug`). Every non-epic item, whatever
its type, still gets the fields above (owner, sprint, priority, LOE,
points). In CPSC 490 most of your board is epics, stories, and tasks;
bugs and enhancements become the daily vocabulary in CPSC 491.

**Board:** create one Project (*Projects → New project → Board*) with
columns **Backlog → Sprint To-Do → In Progress → In Review → Done**. Add
every epic and story to it, plus two custom fields:
- a **Story Points** number field, so per-sprint totals (planned vs.
  completed) can be read off at the sprint review — that ratio is your
  team's velocity;
- a **Sprint iteration field** (*field type: Iteration*, four 2-week
  iterations `Sprint 1`–`Sprint 4` matching §6's dates) — this is GitHub's
  native sprint mechanism: group or slice the board by it to get a
  per-sprint view, and it must agree with each issue's milestone.

**What "done" means in CPSC 490:** stories come in two kinds and both are
first-class. *Document stories* deliver a section of the proposal or a
spec/design document; *prototype stories* deliver working proof-of-concept
code in `prototype/` (a feature spike, an integration with the sponsor's
data, a demo path for the in-class check). Either kind is Done when its
change is **merged through a reviewed pull request** and its acceptance
criteria are checked off. What waits for CPSC 491 is production-depth
implementation — not coding itself.

---

## 5. Traceability: issues ↔ documents ↔ pull requests

The single habit that most affects your sprint grade:

1. **Every spec/design document names its issues.** Top of each file in
   `docs/`:
   `> Epic: #1 · Stories: #2, #3, #5`
2. **Every story links its document.** In the issue body:
   `Deliverable: docs/specs/account-management.md §2`
3. **Every change lands by pull request**, and the PR body says
   `Closes #12` so the story closes automatically on merge.
4. **Author ≠ reviewer.** A different team member approves each PR before
   merge. Rotate reviewers; don't let one person approve everything.

Issue templates live in `.github/ISSUE_TEMPLATE/`. The example repository
ships four ready to copy — `epic.md`, `user-story.md`, `task.md`, `bug.md`
— plus `PULL_REQUEST_TEMPLATE.md`. The two required ones are:

`epic.md`
```markdown
---
name: Epic (Goal)
about: One project goal from Goals & Objectives
labels: epic
---
## Goal
<one sentence — copy the goal from the proposal>

## User stories (objectives)
- [ ] #
- [ ] #

## Success measure
<how we know this goal is achieved>
```

`user-story.md`
```markdown
---
name: User story (Objective)
about: One objective under a goal
labels: user-story
---
## Story
As a <who>, I want <what>, so that <why>.

## Epic
#<epic number>

## Deliverable
docs/<specs|design>/<file>.md

## Acceptance criteria
- [ ]
- [ ]
```

`PULL_REQUEST_TEMPLATE.md`
```markdown
Closes #<story>

## What changed
-

## Checklist
- [ ] Acceptance criteria of the linked story are met
- [ ] Reviewed by a teammate who is not the author
```

---

## 6. The four sprints

Four 2-week sprints between the proposal submission and the Preview Paper
(dates may be adjusted in class — Canvas announcements win):

| Sprint | Dates (planned) | Focus | Syllabus anchor |
|---|---|---|---|
| **Sprint 1** | Sep 28 – Oct 11 | Epics + stories filed from Goals & Objectives; board running; specs started; **prototype v0 → v1 demo path** for the in-class check | ends right before the **Week-8 in-class prototype check** (Oct 13 §01 / Oct 15 §05) |
| **Sprint 2** | Oct 12 – Oct 25 | Specification documents per epic; proposed approach firmed; **prototype reworked from check feedback** | — |
| **Sprint 3** | Oct 26 – Nov 8 | Design documents (architecture, data, UI/API sketches); **prototype proves the riskiest design choice**; timeline validated | **report draft #1 due Nov 1** (mid-sprint) |
| **Sprint 4** | Nov 9 – Nov 22 | Integration: proposal/report polished end-to-end; **prototype stable + demoable, README run instructions verified** | **report draft #2 due Nov 29** (the sprint's output) |

Plan a healthy mix each sprint — document stories AND prototype stories.
A sprint that is all writing or all code is usually a planning smell.

Before Sprint 1 begins, two things are already due **Sep 27** per the
syllabus: the **project proposal** (HW#4) and **prototype v0 — a running
proof-of-concept committed to this repository**. Keep prototype code in a
`prototype/` folder with a README that says how to run it; prototype work
is issue-tracked like everything else.

Sprint ritual (30 minutes at each boundary, leader drives) — **write it down
in `docs/sprint-reviews/sprint-N.md`** (template in the example repo):
- **Close out:** move finished stories to Done (via merged PRs — not by
  dragging cards); carry over or re-scope what didn't finish, with a
  one-line note on why.
- **Plan:** pull next stories from Backlog into the new sprint's milestone;
  every pulled story gets owner, priority, LOE, and story points *at
  planning time*, not retroactively.
- Points planned vs. completed per sprint = your velocity; I look at the
  trend, not the absolute number.

---

## 7. Working with an LLM: AIDLC, human-in-the-loop

You may use any LLM (Claude, ChatGPT, Copilot, Gemini) for any part of this
project — that is encouraged, and it is what the AIDLC lectures are about.
The discipline is **human-in-the-loop**: the assistant drafts, *you* verify,
and a *second human* approves. Nothing reaches `main` otherwise.

Three things make that real in your repository, and all three are in the
example repo ready to copy:

1. **[`CLAUDE.md`](CLAUDE.md) — standardized context.** One file naming the
   project, conventions, what the assistant may draft, and what only a human
   decides. Every teammate's session starts from the same facts, so you stop
   getting five different answers about your own project. (Copilot reads
   `.github/copilot-instructions.md`, Cursor reads `.cursor/rules/` — keep
   one real file and copy it.)
2. **[`docs/aidlc/prompt-library.md`](docs/aidlc/prompt-library.md) —
   standardized prompts** for the jobs you actually do: draft a spec section
   from a story, write code from acceptance criteria, review a diff, write
   tests, survey related work. Each template ends by requiring the model to
   separate what it verified from what it could not.
3. **[`docs/aidlc/hitl-gates.md`](docs/aidlc/hitl-gates.md) — the seven
   gates.** Read this one carefully. It names the six ways LLMs fail
   (fabrication, plausible-but-wrong, requirement drift, scope creep,
   unverified claims, check-gaming) and, gate by gate, what catches each:
   framing criteria before prompting → your own verification → the CI
   harness (G1–G6) → peer review → protected merge → sprint review.

4. **[`docs/aidlc/loop-engineering.md`](docs/aidlc/loop-engineering.md) —
   the harness and the loop.** What a harness is (guides that steer before,
   sensors that detect after), which checks to build first for the best
   payoff, test-first with a committed failing test, the two-correction
   stopping rule, how to tell the *spec* is at fault rather than the prompt,
   how to stop a check from being gamed, and a ten-minute review protocol.
   Teams keep a [harness log](docs/aidlc/harness-log.md) where every rule
   names the failure that caused it — bring it to the sprint review.

**The harness** is the automated half — run it in one second before you push:

```bash
python .github/scripts/check_repo.py
```

It checks template structure, document↔issue traceability, that cited issue
numbers really exist, that links resolve, that no secrets are committed, and
flags leftover placeholders. GitHub Actions runs the same script on every
pull request, plus your prototype's tests and a check that your PR links a
story, discloses AI use, and says what you verified.

**Loop engineering** in one line: frame the criteria, prompt once, verify
against the harness, iterate — two failed corrections mean start a clean
session, three failed attempts mean the specification is the problem, not
the prompt. Keep the local command and the CI command identical, and
disclose AI-assisted commits with an `Assisted-by:` trailer.

**Git workflow and CI/CD:** standard Gitflow
(`main` / `develop` / `feature/*` / `release/*` / `hotfix/*`), branch
protection requiring green CI plus one non-author approval, releases tagged
on `main` — all in
[`docs/git-workflow.md`](docs/git-workflow.md).

**Course AIDLC materials** are in the repository so everything lives in one
place: [`docs/aidlc/lectures/`](docs/aidlc/lectures/) (Lecture 1 From SDLC to
AIDLC / HITL vs HOTL · Lecture 2 Prompt Engineering · Lecture 3 Harness Loop
Engineering · Lecture 4 Benchmarks, Quality and ROI) and the
[AIDLC Field Guide](docs/aidlc/AIDLC-Field-Guide.html).

## 8. How sprint performance is measured

At each sprint checkpoint the repository is reviewed against five metrics
(the same rubric continues into CPSC 491's implementation sprints):

| Metric | What I look for in YOUR repo |
|---|---|
| **Accountability** | Every story has exactly one assignee; every member owns stories and has commits/PRs each sprint |
| **Traceability** | Story ↔ document ↔ PR links resolve both ways (§5); epics' task lists reflect reality |
| **Transparency** | Board matches the truth — statuses current, carry-overs annotated, no "Done" without a merged PR |
| **Separation of duties** | PRs reviewed by a non-author; review rotation; work distribution isn't one person's repo |
| **Relevance** | Sprint work maps to the proposal's Goals & Objectives — no orphan busywork, no goals with zero movement |

Red flags that cost points: unassigned or field-less issues, documents with
no linked issue, one member with all the commits, a board updated only the
night before review, "Done" columns full of unmerged work.

---

## 9. Quick-start checklist (do in week one of Sprint 1)

- [ ] Repo created with course naming; all members + `kyoungshin` added
- [ ] README filled in from `README_TEMPLATE.md` (team table, project title, links)
- [ ] `proposal/proposal.md` skeleton committed with all 11 template headings
- [ ] Issue templates + PR template committed
- [ ] Labels created: `epic`, `user-story`, `priority: high/medium/low`, `loe: S/M/L`
- [ ] Milestones created: `Sprint 1`–`Sprint 4` with dates
- [ ] Project board created (5 columns + Story Points number field + Sprint iteration field), linked in README
- [ ] Every goal filed as an epic; every objective as a user story under it
- [ ] Sprint 1 stories pulled into the `Sprint 1` milestone with owner/priority/LOE/points — including prototype stories, not only writing
- [ ] Prototype v0 committed under `prototype/` with run instructions in its README
- [ ] `develop` branch created; branch protection on `main` + `develop` (green CI + 1 approval)
- [ ] `CLAUDE.md` copied and filled in; team agreed to read `docs/aidlc/hitl-gates.md`
- [ ] CI green on a first real pull request, reviewed by a non-author

---

## 10. AI usage

AI tools (Claude, Copilot, ChatGPT, …) are **encouraged** for drafting,
reviewing, and organizing — and their use must be disclosed in the
proposal's **AI Usage** section (what tools, for what, and how you verified
the output). AI-assisted work is your work; unverified AI output submitted
as fact is not.

---

*Questions or a blocker with GitHub setup? Post in the course channel or
bring it to the project meeting — do not lose sprint days to tooling.*
