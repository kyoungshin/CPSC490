# Group repository status: proposal vs. issue board

> [!IMPORTANT]
> **New (Oct 11): one card per group, ahead of the Sprint 1 reviews.**
> Scroll to **Your group**. Your card combines everything this page checks into one numbered list, in the order to fix it: *Unblock → Document → Board / Scope → Link → Plan → Workflow*. Work through it before your Sprint 1 review: **G01–G05 Tue Oct 13 · G11–G15 Thu Oct 15 · G06–G10 Tue Oct 20 · G16–G20 Thu Oct 22**, and bring the card to the meeting.
>
> The section **Why teams are stuck** explains the patterns behind most cards. Most teams are one merged pull request away from a much better card: §2 of your proposal, merged into `develop`.

> [!CAUTION]
> **HW#5 check (Oct 12): 11 groups' epics and user stories do not match the Goals and Objectives they submitted in HW#5 (§2).**
> 🔴 **Not reflected / wrong numbers:** [**G05**](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses/issues/7) · [**G06**](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/15) · [**G12**](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/82) · [**G14**](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/21) · [**G15**](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/23) · [**G17**](https://github.com/vibhorbh/CPSC490-G17-SonicScape/issues/13)
> 🟠 **Extra, duplicate or misnumbered items:** [**G07**](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/33) · [**G08**](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/48) · [**G13**](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/50) · [**G18**](https://github.com/austin2578/CPSC490-G18-ProStrats/issues/43) · [**G20**](https://github.com/muntay89/CPSC490-G20-Solos/issues/31)
>
> Each of these groups has an instructor issue in its repository listing its HW#5 goals and objectives, our evaluation, and a fix checklist. **Sprint 2 is planned from exactly the §2 set**, and mismatches are reviewed in the Sprint 1 evaluation. Fix them before your Sprint 1 review.

**CPSC 490 · Fall 2026 · swept 2026-10-11 04:00 UTC.** The previous edition (2026-10-09) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. **Find your group below: your card lists everything still open for your team, in the order to fix it.** The rules and the full tables are at the end.

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ⚠️](#g02) | [**G03** ⚠️](#g03) | [**G04** ⚠️](#g04) | [**G05** ❌](#g05) | [**G06** ⚠️](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ⚠️](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ⚠️](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ❌](#g17) | [**G18** ⚠️](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

**New to git or the board? Start with [First Steps](https://kyoungshin.github.io/CPSC490/first-steps.html)**: HW#4/HW#5 to the Sprint Board, every command listed.

## Sprint review: what to bring

Each sprint ends with a review in class. Bring:

1. **Story points for the sprint just ended:** the total committed at its start and the total done at its end. `scripts/sprint_report.py` counts both from the `sp:` labels and `Sprint N` milestones: run the *Sprint report* workflow in your repository's Actions tab, or locally `GITHUB_REPOSITORY=owner/repo GITHUB_TOKEN=$(gh auth token) python scripts/sprint_report.py --sprint N --markdown`.
2. **The Sprint Board** showing every issue for the next sprint, each with one assignee, a `Sprint N` milestone and `sp:`.
3. **Progress aligned three ways:** the board, `proposal/proposal.md` and the prototype code tell the same story. Every closed issue is cited in the proposal, and its change is merged into `develop` or `main`.
4. **Your card below, worked through.** Anything still on it, say why and when it'll be done.

| Groups | Sprint 1 | Sprint 1 review | Sprint 2 | Sprint 2 review | Sprint 3 | Sprint 4 |
|---|---|---|---|---|---|---|
| G01–G05 | Sep 29 – Oct 12 | Tue Oct 13 | Oct 13 – 26 | Tue Oct 27 | Oct 27 – Nov 9 | Nov 10 – 23 |
| G06–G10 | Oct 6 – 19 | Tue Oct 20 | Oct 20 – Nov 2 | Tue Nov 3 | Nov 3 – 16 | Nov 17 – 30 |
| G11–G15 | Oct 1 – 14 | Thu Oct 15 | Oct 15 – 28 | Thu Oct 29 | Oct 29 – Nov 11 | Nov 12 – 25 |
| G16–G20 | Oct 8 – 21 | Thu Oct 22 | Oct 22 – Nov 4 | Thu Nov 5 | Nov 5 – 18 | Nov 19 – Dec 2 |

## Why teams are stuck, and how to get unstuck

Across the 20 repositories, the same few things hold most teams back. They're listed in the order to fix them: each step unblocks the next. The rules on this page also grew during Sprint 1; your card already includes every rule, so you don't have to cross-check the tables.

**1. The proposal hasn't reached `proposal/proposal.md` yet** (13 groups: G02, G03, G04, G05, G06, G08, G09, G10, G11, G14, G15, G17, G18). §2 *Goals and Objectives* is still the template on both `main` and `develop`. Every other check on this page starts from that file, so until §2 is merged the page shows *0 issues linked*, even for groups that already have user stories on their board (G02, G06, G08, G09, G15, G18). **Do this first:** copy §2 from your HW#4/HW#5 draft into `proposal/proposal.md`, open one pull request into `develop`, and merge it this week.

**2. Finished work is sitting in branches and open pull requests** (11 groups: G01, G02, G03, G04, G07, G08, G09, G13, G14, G16, G19). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**3. Course files are now self-service.** The instructor's course-file pull requests were closed on Oct 11 in every repository, so there is nothing to merge. **Do this:** run the course-update command (see **Course-update command** under *The rules this page checks*) whenever this page says the course files changed. It updates only the course files you haven't edited, and commits them on a `course-update-YYYY-MM-DD` branch for you to open a pull request from.

**4. The board is a list, not a plan yet.** In 11 groups (G02, G03, G06, G07, G08, G09, G10, G13, G14, G19, G20) at least half the open issues have no assignee, and 15 groups (G01, G02, G03, G04, G06, G08, G09, G10, G11, G13, G14, G15, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 8 groups: G01, G06, G07, G10, G15, G16, G17, G19). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (19 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

**7. Goals haven't become epics and stories yet** (8 groups: G03, G04, G05, G10, G11, G12, G14, G17). Without them, Sprint 2 has nothing to point at. **Do this:** one epic per §2 goal and one user story per objective, titled with the objective's exact words (course README §4).

## Class at a glance

- ✅ **Aligned:** 8 (G01, G07, G08, G09, G13, G16, G19, G20)
- ⚠️ **Partial:** 6 (G02, G06, G10, G11, G12, G15)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 3 (G03, G04, G18)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 2 (G05, G17)
- Team-filed issues: **287** across 18 groups (18 new since 2026-10-09).

### What changed since 2026-10-09

- **G09 moved from process-only to aligned.** Epics #27/#28 and ten user stories (#29–#38) now track the project's features. They still need `sp:` on the work items not under a story, and links from `proposal.md`.
- **G19 is the first group to use typed references.** §2 of `proposal.md` now links 11 typed refs (13 of 14 issues linked). The remaining gap is direct commits to main.
- **G02** closed tasks #36 and #40, merged PRs #44 and #35, and put every open issue on its Sprint board. The §2 draft is still on an unmerged branch.
- **G01** merged develop into main (#46); the main README now carries the real title and sponsor. Links in `proposal.md` are still bare `#N`, and the Sprint board is still empty.
- **G13** added Sprint 1 process tasks (#34, #35, #43) and merged its Sprint 1 report (#37). `proposal.md` still links none of its 25 issues.
- **G03, G06, G10, G12** made small process changes (merged PRs, meeting and advisor-notes tasks, one new epic), and their verdicts are unchanged. Eleven groups had no changes since the last edition.
- **Instructor housekeeping:** the instructor's own Word-export and sprint-report issues closed in G01, G02, G03 and G10, now that their fixes are merged on main.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ⚠️](#g02) | [**G03** ⚠️](#g03) | [**G04** ⚠️](#g04) | [**G05** ❌](#g05) | [**G06** ⚠️](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ⚠️](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ⚠️](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ❌](#g17) | [**G18** ⚠️](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 21 issues (16 open) · Sprint 1 milestone: 2 open, 1 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge open PRs #34/#35/#36 into develop, convert the 18 bare #N links in proposal.md to typed `[epic:#N]` links, and add every open issue to the Sprint board (0 items now).

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull requests #36, #35, #34. Work in an open PR doesn't count yet.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Link.* Cite 3 of 21 issues in `proposal.md` (epics and stories in §2, the rest in §4): #41–#43.
5. *Link.* Rewrite 18 bare `#N` references as typed links, e.g. `[[story:#33]](https://github.com/LeDuy23/CPSC490-G01-BGAF/issues/33)`.
6. *Plan.* Link your Sprint Board to the repository (the repository's *Projects* tab → *Link a project*).
7. *Plan.* Add a **board-layout view** to your project (*New view → Board*).
8. *Plan.* Add 15 open issues to the board: #13, #20–#28, #32, #33, #41–#43.
9. *Plan.* Give #9–#14, #32, #41–#43 their own `sp:` label and a `Sprint N` milestone.
10. *Plan.* Assign 6 of 16 open issues to one person each.
11. *Workflow.* Stop pushing straight to `main`/`develop` (7 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
12. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (11 of 17 PRs closed no issue).

*Since 2026-10-09:* Issue set unchanged (21) and proposal main still links 18 bare/0 typed; main README now has real title and sponsor and 'Develop' PR #46 merged into main, but #34/#35/#36 are still unmerged and the Sprint board is still empty.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

⚠️ **Partial** · chain ❌ Broken · 23 issues (13 open) · Sprint 1 milestone: 6 open, 8 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge the §2 draft (branch feature/2_GoalsObjectives; task #40 is already closed) into develop, then file epics and stories for capture, fingerprinting, location and dashboard (#41) and fix the #16/#17 parent loop.

Everything still open, in the order to fix it:

1. *Unblock.* 1 branch holds work that isn't in `develop`: `feature/2_GoalsObjectives`. Open a pull request for each, or delete the branch.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: multi-node distribution and sync; Bluetooth capture; device fingerprinting; localization; dashboard; active-recording detection.
5. *Link.* Cite all 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15–#18, #20–#25, #36–#41.
6. *Plan.* Give #6, #15 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 12 of 13 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 13 PRs closed no issue).

*Since 2026-10-09:* Tasks #36 (Related Work) and #40 (§2 draft) closed and PRs #44/#35 merged into main, and the Sprint board now holds all open issues with a board view; but proposal.md still links no issues and only Wi-Fi among the project features is planned.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

⚠️ **Process only** · chain ❌ Broken · 10 issues (5 open) · Sprint 1 milestone: 2 open, 4 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Write §2 (#17) with 2-3 goals and measurable objectives, file one epic per goal and stories for the three AI stages (recognize, generate code, verify), and create/share a readable Sprint board.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull requests #26, #23. Work in an open PR doesn't count yet.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
6. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: all five core elements; no feature issues, epics or stories exist.
7. *Link.* Cite all 10 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #2, #4, #5, #13, #15–#17, #20, #24.
8. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.
9. *Plan.* Give #1, #2, #15, #17, #20, #24 their own `sp:` label and a `Sprint N` milestone.
10. *Plan.* Assign 4 of 5 open issues to one person each.
11. *Workflow.* Stop pushing straight to `main`/`develop` (1 direct commit so far): branch → pull request → review → merge. Turn on branch protection.
12. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 10 PRs closed no issue).

*Since 2026-10-09:* Related Work/problem-statement PRs merged (#25) and #16 closed and a Meeting #2 issue added, but still no epics/stories or feature issues, proposal.md links nothing, and the board link is still unreadable.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polygon Prediction Market PNL and Trader Profitability Analytics

⚠️ **Process only** · chain ❌ Broken · 7 issues (0 open) · Sprint 1 milestone: 0 open, 7 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Use the kickoff-notes scope (phase 1 proxy-wallet PNL, phase 2 EOA linking, client dashboard) to write §2 goals and objectives, file 2-3 epics with sp: stories in Sprint 2, and merge #21 so proposal.md replaces the template.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull request #21. Work in an open PR doesn't count yet.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
6. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Trade parsing; Resolution matching; PNL computation; Trader ranking and edge analysis; Dashboard.
7. *Link.* Cite all 7 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #3, #10–#13, #20.
8. *Plan.* Give #1, #3, #12, #13, #20 their own `sp:` label and a `Sprint N` milestone.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 8 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS

❌ **No issues** · chain ❌ Broken · 0 issues (0 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Your repository has **no epics or user stories**. HW#5 §2 lists 2 goals and 10 objectives, citing Epic #1 and Epic #2, but #1 is an instructor issue and #2 does not exist.
> See [the instructor issue](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses/issues/7) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Run the bootstrap to create the missing epic/user-story/sp:/task labels, commit the real proposal into proposal/proposal.md and the team README, and file Sprint 1 tasks with sp: for each proposal section.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
4. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
5. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · Forecast Market Analytics: GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking

⚠️ **Partial** · chain ❌ Broken · 5 issues (5 open) · Sprint 1 milestone: 3 open, 0 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** HW#5 §2 has **3 goals and 14 objectives**, but the repository has only Goal 1 (epic #13) with one story (#14, Objective 1.1). Epics #3 *Home Page* and #4 *Create LLM prototype* and stories #5 and #6 are not in HW#5.
> See [the instructor issue](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/15) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** File the missing story issues (1.3, 1.4, 2.1-2.3 plus a weak-spot tracker story), finish epic #4's unfinished goal sentence, and give every story an sp: label in Sprint 1.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Answer checking and per-concept mastery tracker has no story issue; assignment notifications; baseline evaluation; flashcards/summaries.
5. *Link.* Cite all 5 issues in `proposal.md` (epics and stories in §2, the rest in §4): #3–#6, #10.
6. *Plan.* Give #5, #6 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 4 of 5 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (12 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-09:* PR #9 merged into develop and the board gained an item; issue set and proposal.md links unchanged (5 issues, 0 linked), stories still lack sp:.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Material Database

✅ **Aligned** · chain ⚠️ Gaps · 24 issues (21 open) · Sprint 1 milestone: 7 open, 3 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 match, but the **issue numbers in HW#5 §2 are off by one from Goal 3 on**, and the repository has items HW#5 does not.
> See [the instructor issue](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/33) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Merge #30 so develop has the goals, convert the 16 links in proposal.md to typed references, add #28/#4/#1 or close them, and replace the course-template README with the project README.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull request #30. Work in an open PR doesn't count yet.
3. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Link.* Cite 8 of 24 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #4–#7, #27–#29.
6. *Link.* Rewrite 16 bare `#N` references as typed links, e.g. `[[story:#26]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/26)`.
7. *Plan.* Add a **board-layout view** to your project (*New view → Board*).
8. *Plan.* Add 1 open issue to the board: #29.
9. *Plan.* Assign 19 of 21 open issues to one person each.
10. *Workflow.* Stop pushing straight to `main`/`develop` (19 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
11. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 2 PRs closed no issue).

*Since 2026-10-09:* PR #30 is now open to sync develop with main (#29) and a Sprint board exists (no board-layout view, #29 not on it); issue structure, 16 bare links and 17 direct commits to main unchanged.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

✅ **Aligned** · chain ⚠️ Gaps · 33 issues (32 open) · Sprint 1 milestone: 12 open, 1 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals and objectives match HW#5 §2, but the repository has **extra and duplicate items**.
> See [the instructor issue](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/48) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Add sp: labels to every story and unparented task in a Sprint milestone, close junk epics #6/#7, and fill the template placeholders in task bodies.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* 2 branches hold work that isn't in `develop`: `proposal-abstract`, `proposal-goal-3`. Open a pull request for each, or delete the branch.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Link.* Cite 26 of 33 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6–#13, #17–#24, #27, #29–#36, #42.
6. *Link.* Rewrite 7 bare `#N` references as typed links, e.g. `[[story:#28]](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/28)`.
7. *Plan.* Add 2 open issues to the board: #6, #7.
8. *Plan.* Give #4, #5, #13, #15, #16, #21, #22, #28, #42 their own `sp:` label and a `Sprint N` milestone.
9. *Plan.* Assign 25 of 32 open issues to one person each.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 5 PRs closed no issue).

*Since 2026-10-09:* README task #42 closed via merged PR #41 (main README now the real Crime Busters one) and stray abstract PR #39 closed; issues, 7 bare proposal links and clean PR flow otherwise unchanged.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

✅ **Aligned** (was Process only) · chain ❌ Broken · 27 issues (25 open) · Sprint 1 milestone: 10 open, 2 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Merge PRs #21/#22/#25/#26 into develop, put sp: and a Sprint milestone on stories #29-#38 (all missing), and fill proposal.md §2/§4 with typed links.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull requests #26, #25, #22, #21. Work in an open PR doesn't count yet.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Abstract extras: automatic mileage tracking, DIY logs, parts finder, climate-based recommendations (not in the goals; fine if deliberately cut); receipt/paper-record scanning (import is data-only).
6. *Link.* Cite all 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #5–#19, #27–#38.
7. *Plan.* Give #29–#38 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 16 of 25 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (1 direct commit so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 5 PRs closed no issue).

*Since 2026-10-09:* Epics #27/#28 and ten user stories (#29-#38) filed since last edition, so the project is now tracked as features; PRs #21/#22 still open with two more (#25/#26) added, and proposal.md still links 0 of 25 issues.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: On-Chain Stablecoin Flow and Wash Trading Detection

⚠️ **Partial** · chain ❌ Broken · 10 issues (2 open) · Sprint 1 milestone: 1 open, 7 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** File epics for Goals 2 and 3 and one user-story issue per objective 1.1-3.3 (title = section 2 text verbatim, own sp: in Sprint 1/2), then link them from proposal.md section 2.

Everything still open, in the order to fix it:

1. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Board.* Create one **user story** per objective, titled with the objective's exact words.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Goal 2 epic and objectives 2.1-2.3; Goal 3 epic and objectives 3.1-3.3; Story issues for objectives 1.1-1.3; Validation strategy.
5. *Link.* Cite all 10 issues in `proposal.md` (epics and stories in §2, the rest in §4): #3–#9, #13, #15, #18.
6. *Plan.* Give #3, #6, #13 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 1 of 2 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (18 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 3 PRs closed no issue).

*Since 2026-10-09:* New process task #18 (advisor notes, closed) and PR #19 merged into main; still one epic with no stories, proposal.md still links 0 issues, direct pushes to main continue (14).

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

⚠️ **Partial** · chain ❌ Broken · 11 issues (7 open) · Sprint 1 milestone: 6 open, 5 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Decide the core (individual GPS+ML analysis per the proposal, or live event tracking per epic #4 and meeting notes), then write Goal 1 objectives in proposal §2 and file one story per objective.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Board.* Create one **user story** per objective, titled with the objective's exact words.
6. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: ML analysis against public marathon data; Storing/reviewing run logs; Display route on map and calculate distance/elapsed/pace objectives (Goal 1 objectives have no stories); Goals 2-3 not yet written.
7. *Link.* Cite 9 of 11 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1–#3, #6–#9, #17, #20.
8. *Link.* Rewrite 2 bare `#N` references as typed links, e.g. `[[story:#13]](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys/issues/13)`.
9. *Plan.* Link your Sprint Board to the repository (the repository's *Projects* tab → *Link a project*).
10. *Plan.* Add 1 open issue to the board: #6.
11. *Plan.* Give #1–#3, #6, #13 their own `sp:` label and a `Sprint N` milestone.
12. *Plan.* Assign 2 of 7 open issues to one person each.
13. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
14. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

⚠️ **Partial** · chain ⚠️ Gaps · 18 issues (6 open) · Sprint 1 milestone: 5 open, 20 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The stories match, but **HW#5 §2 cites placeholder numbers** ([Epic:#1]–[Epic:#5], [Story#1]/[Story#2]) instead of the real issues, and two epic titles differ from §2.
> See [the instructor issue](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/82) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write section 2 Goals and Objectives, finish epic #57 (real goal text) and add epics/stories for parameter estimation, classifier baselines, GUI/CLI and explanation; fill the README (title still TBD, summary template).

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Board.* Create one **user story** per objective, titled with the objective's exact words.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Parameter estimation and classifier implementation; GUI/CLI and interface control document; Explainability layer and abstain behavior; Robustness evaluation across channel conditions; No section 2 Goals/Objectives in proposal, so no stories.
4. *Link.* Cite 8 of 18 issues in `proposal.md` (epics and stories in §2, the rest in §4): #27–#32, #36, #57.
5. *Link.* Rewrite 10 bare `#N` references as typed links, e.g. `[[story:#48]](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/48)`.
6. *Plan.* Assign 1 of 6 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 13 PRs closed no issue).

*Since 2026-10-09:* One new epic (#57, peak picking) but it is still template text and has no stories or section 2 link; otherwise unchanged (10 of 18 issues linked, all bare, README still TBD template).

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ❌ Broken · 25 issues (24 open) · Sprint 1 milestone: 9 open, 1 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 and their objectives match, but the repository has a **Goal 0 epic (#30) with stories #31–#33** that HW#5 §2 does not have, and §2 cites no issue numbers.
> See [the instructor issue](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/50) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Make each story title the section 2 objective verbatim (drop the 'Objective n.n:' prefix), fill the placeholder bodies, give each story its own sp: and a Sprint milestone, and reconcile the platform (desktop vs web vs mobile).

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull requests #40, #36, #4. Work in an open PR doesn't count yet.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Platform inconsistent: abstract/section 3 say Windows desktop with Windows notifications, section 4/5 say Python+JS web app, README says mobile app; #12/#13 assume web.
4. *Link.* Cite all 25 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15–#27, #30–#35, #43.
5. *Plan.* Add 3 open issues to the board: #8, #12, #13.
6. *Plan.* Give #8, #10–#13, #15, #19–#27, #31–#33 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 21 of 24 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (1 direct commit so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 11 PRs closed no issue).

*Since 2026-10-09:* Process epic #30 now has tasks #34, #35 and #43 (Sprint 1), PR #37 sprint-1-report merged and #40 timeline opened; proposal.md still links 0 of 25 issues and 12 stories still lack sp:.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Rogue-Lite Cyber Sandbox

❌ **Mismatch** · chain ❌ Broken · 4 issues (4 open) · Sprint 1 milestone: 2 open, 2 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2 at all**: it has one epic, #8 *Create web scanner*, and no stories. HW#5 §2 has 2 goals and 10 objectives for a cybersecurity training sandbox.
> See [the instructor issue](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/21) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Agree on one project (the proposal is the Cyber Sandbox), commit the proposal text into proposal.md, write §2 goals, and replace the web scanner epic with epics and stories for the sandbox.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* Review and merge (or close) your open pull requests #12, #9. Work in an open PR doesn't count yet.
3. *Document.* Your board or README describes a **different project** than your proposal. Make them match, or tell the instructor the project changed.
4. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
5. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
6. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
7. *Board.* Create one **user story** per objective, titled with the objective's exact words.
8. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Every core element; §2 Goals and Objectives is unwritten, so there are no stories to file.
9. *Link.* Cite all 4 issues in `proposal.md` (epics and stories in §2, the rest in §4): #4, #6, #8, #13.
10. *Plan.* Add 1 open issue to the board: #13.
11. *Plan.* Give #13 its own `sp:` label and a `Sprint N` milestone.
12. *Plan.* Assign 2 of 4 open issues to one person each.
13. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
14. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 7 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Low End Hardware ECS Game Engine with Game

⚠️ **Partial** · chain ❌ Broken · 6 issues (4 open) · Sprint 1 milestone: 2 open, 0 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2**: it has one epic, #6 *Setting up*, with one story, #9 *Window and Renderer*. HW#5 §2 has 2 goals (*Game Demo*, *Game Engine*) and 8 objectives.
> See [the instructor issue](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/23) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write §2 goals and objectives (rendering, ECS, game creation, benchmarking), then retitle #6 and #9 to match, file stories for the missing objectives, and stop committing directly to main (4 direct commits).

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: ECS implementation; Game-creation interface / showcase game; Benchmarking and performance evaluation; Memory management; Story for closing the window (listed in epic #6, no issue).
6. *Link.* Cite all 6 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #9–#12, #16.
7. *Plan.* Add 3 open issues to the board: #6, #9, #10.
8. *Plan.* Give #12, #16 their own `sp:` label and a `Sprint N` milestone.
9. *Workflow.* Stop pushing straight to `main`/`develop` (8 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 8 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ⚠️ Gaps · 21 issues (17 open) · Sprint 1 milestone: 6 open, 3 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Convert the 21 bare issue links in proposal.md to typed references (`[epic:#11]`, `[story:#14]`, `[task:#27]`), then fix the Sprint board (README link is not readable) so every open issue is on it.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Unblock.* 1 branch holds work that isn't in `develop`: `feature/5-bridgewatch-prototype`. Open a pull request for each, or delete the branch.
3. *Link.* Rewrite 21 bare `#N` references as typed links, e.g. `[[story:#39]](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic/issues/39)`.
4. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.
5. *Plan.* Assign 3 of 17 open issues to one person each.
6. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 16 PRs closed no issue).

*Since 2026-10-09:* Big jump: proposal.md is now the real proposal on develop with all 21 issues linked (was 0 of 19), README describes BridgeWatch, prototype v0 (#36) merged via PR, tasks #34/#39 filed; remaining gaps are untyped links and an unreadable board.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: SonicScape

❌ **No issues** · chain ❌ Broken · 0 issues (0 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Your repository has **no epics or user stories**. HW#5 §2 lists 2 goals and 5 objectives with placeholder numbers (#〈1〉, #〈2〉).
> See [the instructor issue](https://github.com/vibhorbh/CPSC490-G17-SonicScape/issues/13) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Copy the abstract and introduction into proposal/proposal.md, write section 2, file Sprint 1 tasks with sp: for the five core systems (and open a Sprint board), link each from proposal.md as typed references, and open PRs into develop that close them.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
4. *Workflow.* Stop pushing straight to `main`/`develop` (9 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 4 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue

⚠️ **Process only** · chain ❌ Broken · 12 issues (4 open) · Sprint 1 milestone: 1 open, 7 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 match (epics #29–#31, stories #32–#41), but the repository has **two extra epics not in HW#5 §2**: #17 (*playable and extensible prototype*, story #18) and #19 (*capstone proposal*, story #20).
> See [the instructor issue](https://github.com/austin2578/CPSC490-G18-ProStrats/issues/43) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write proposal §2 with one objective per core system (classes, weapon Mastery, attributes/boons, branching rooms, combat, playtest measures), file each as a story under an epic titled verbatim from §2 with its own sp: and Sprint milestone, and link every issue from proposal.md as typed references.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Class system; Weapon replacement / Mastery / affixes; Attributes, boons, respec; Branching route map and handcrafted rooms; Core combat and platforming; Playtest plan for build variety / meaningful decisions.
5. *Link.* Cite all 12 issues in `proposal.md` (epics and stories in §2, the rest in §4): #2, #5–#9, #13, #15, #17–#20.
6. *Plan.* Add 1 open issue to the board: #13.
7. *Plan.* Give #2, #6–#9, #13, #18, #20 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 1 of 4 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-09:* Board now exists (Sprint Board/Current Sprint/Sprint Plan views) and all 7 PRs close issues, but still 0 of 12 issues linked from the skeleton proposal.md and stories/tasks have no sp:.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi

✅ **Aligned** · chain ⚠️ Gaps · 14 issues (14 open) · Sprint 1 milestone: 12 open, 1 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Retype #11 and #20 as [task:#N] in proposal section 4 (still skeleton), type the epic/story links, merge develop to main by PR, and assign the stories.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #24, #22. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Hardware selection/test-environment setup beyond #8; proposal section 4 and related work not yet tracked.
4. *Link.* Cite 1 of 14 issues in `proposal.md` (epics and stories in §2, the rest in §4): #23.
5. *Link.* Rewrite 2 bare `#N` references as typed links, e.g. `[[story:#20]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/20)`.
6. *Plan.* Add 1 open issue to the board: #23.
7. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 12 of 14 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 5 PRs closed no issue).

*Since 2026-10-09:* Proposal section 2 now links 11 typed refs (13 of 14 issues linked, was 12 bare); new tasks #20 and #23; PR #21 merged; direct commits to main and the skeleton on main remain.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia

✅ **Aligned** · chain ⚠️ Gaps · 16 issues (16 open) · Sprint 1 milestone: 5 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals and objectives match HW#5 §2, but the **story numbering differs**: the repository uses *Objective 12.1, 17.1, 21.1* (issue numbers) where §2 uses 1.1, 2.1, 3.1.
> See [the instructor issue](https://github.com/muntay89/CPSC490-G20-Solos/issues/31) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write §2 in proposal.md with each goal and objective verbatim, cite all 8 stories there as typed references and the 5 tasks in §4, give the 8 stories sp: plus a Sprint 1 milestone, and add the project title to the proposal.

Everything still open, in the order to fix it:

1. *Unblock.* Run the course-update command (see **Course-update command** under *The rules this page checks*) to pull the latest course files. The instructor's course-file pull requests were closed on Oct 11; you no longer merge them.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Unpredictable monster placement/encounters (only distinct behaviors are tracked, not varied placement).
4. *Link.* Cite 13 of 16 issues in `proposal.md` (epics and stories in §2, the rest in §4): #11, #13–#15, #18–#20, #22–#24, #26–#28.
5. *Link.* Rewrite 3 bare `#N` references as typed links, e.g. `[[story:#21]](https://github.com/muntay89/CPSC490-G20-Solos/issues/21)`.
6. *Plan.* Give #13–#15, #18–#20, #22, #23 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 11 of 16 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 3 PRs closed no issue).

*Since 2026-10-09:* From zero issues to 16: three epics, eight stories, five Sprint 1 tasks, a Sprint board with every open issue, README rewritten as Insomnia on develop, and two PRs merged that close issues; only 3 epics are linked from proposal.md and stories lack sp:.

[↑ Back to all groups](#groups)

## The rules this page checks

1. **Document first, then workflow, then code.** Every issue is cited in `proposal/proposal.md`, and every change lands through a pull request that closes one of those issues. No pushing straight to `main` or `develop`.
2. **Merge your work into `develop` or `main`.** This page reads only those two branches; work left on a feature branch doesn't count yet.
3. **Typed issue references**, each linked to its issue, at the end of the paragraph it belongs to: `[[epic:#12]](https://github.com/OWNER/REPO/issues/12)` (double brackets, so GitHub shows `[epic:#12]`), and likewise `[story:#N]`, `[feature:#N]`, `[enhancement:#N]`, `[bug:#N]`, `[task:#N]`, `[sub-task:#N]`, with the type matching the issue's own.
4. **Epics and stories are cited in §2 *Goals and Objectives* only.** Every other issue is cited anywhere in §4: environment, a specification or design document, a diagram's caption, or planned activities.
5. **Story points:** an issue **under a user story has no `sp:`** (the story carries the points). Every issue **not under a story** (the story itself, or a parentless feature, task, bug …) carries its **own `sp:` in a `Sprint N` milestone**. Epics carry no points. In Sprint 1, until epics and stories exist, every issue is a task with `sp:` in Sprint 1.
6. **One Sprint Board** (GitHub Projects, board layout), linked to the repository, with every open issue on it.

**Course-update command.** From inside your repository (Git Bash or a terminal): `git switch develop && git pull`, then `curl -fsSL https://raw.githubusercontent.com/kyoungshin/CPSC490/main/scripts/update-course-files.sh | bash`. It updates only course files you haven't edited and commits them on a new `course-update-YYYY-MM-DD` branch; open a pull request into `develop` for it like any other change. Details: [Getting the latest course files](https://github.com/kyoungshin/CPSC490#getting-the-latest-course-files).

**Word for Canvas: one command.** Install pandoc once (`winget install pandoc`; macOS `brew install pandoc`), then from the repository root:

```
pandoc proposal/proposal.md -o proposal/proposal.docx --reference-doc=proposal/reference.docx --lua-filter=proposal/to-word.lua --resource-path=proposal
```

This produces the course template's cover page filled from your header block, the Abstract on its own page, Word-numbered headings, Times New Roman 11 pt with 1.5 spacing and 1.0-inch margins, and every issue tag such as `[epic:#12]` linked to *Appendix A. Issue References*, which lists the full URLs. See [`proposal/example-proposal.md`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/example-proposal.md) and the [Word file it produces](https://github.com/kyoungshin/CPSC490/blob/main/proposal/example-proposal.docx).

### How to get to *Aligned*

Follow the course README, [§4 Epics and user stories on the issue board](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board). In short:

1. Each **goal** in your proposal §2 *Goals and Objectives* is one **epic** issue (label `epic`). Its body lists its user stories as a task list (`- [ ] #12`).
2. Each **objective** under a goal is one **user story** issue (label `user-story`), **titled with the objective itself, in the exact words of proposal §2**: an action word plus what gets completed, with a number wherever possible. Not a feature name, and not a paraphrase. A user-story sentence goes in the issue body only when the objective has a real user, and it is optional.
3. Every story in a sprint has exactly one assignee, a `Sprint N` milestone, a `priority:` label and an `sp: N` label (1, 2, 3, 5, 8; `sp: 8` means split it). Points go on the objective only, never on the epic or the tasks under it. A writing task with no objective above it carries its own points.
4. Link every epic and story from proposal §2, and every other work item from §4, each as a typed reference linked to its issue. Make the README on `main` say what the proposal says: title, sponsor code, and a one-paragraph summary.
5. Change the repository only through pull requests from a feature branch into `develop`, each closing an issue that proposal.md links.

## Appendix: the full tables

The same facts as the cards, one rule at a time, for comparing groups.

### Progress on `main` and `develop`

What `proposal/proposal.md` says on each branch (rule 2), and feature branches holding work that is in neither yet.

| Group | `main` | `develop` | Not merged yet |
|---|---|---|---|
| G01 | §2 9 links · §4 skeleton · 18 issues cited · 0 typed · 37 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | 18-abstract-intro (3 commits not in develop); 43-update-goals-and-objectives (20 commits not in develop); Damon (2 commits not in develop) |
| G02 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 57 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | feature/2_GoalsObjectives (1 commit not in develop) |
| G03 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 70 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | Elizabeth-7-7-patch-1 (4 commits not in develop); Sehaj36-patch-1 (6 commits not in develop); feature/15-related-work-section (3 commits not in develop); johnkyohannan-patch-1 (1 commit not in develop) |
| G04 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | patch-1-proposal.md (2 commits not in develop) |
| G05 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G06 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 82 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 82 〈placeholders〉 | none |
| G07 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | proposal-abstract (1 commit not in develop); proposal-goal-3 (1 commit not in develop) |
| G09 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | feature/5-proposal-goals-objectives (3 commits not in develop); feature/6-Related-Work-Table-and-9-AI-Usage-+-References (2 commits not in develop); feature/8-proposal-cleanup (5 commits not in develop); feature/10-header-fields-sprint-list (2 commits not in develop); feature/11-update-readme (3 commits not in develop); proposal-draft (3 commits not in develop) |
| G10 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G11 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 2 issues cited · 0 typed · 70 〈placeholders〉 | none |
| G12 | §2 0 links · §4 10 links · 10 issues cited · 0 typed | §2 0 links · §4 10 links · 10 issues cited · 0 typed | none |
| G13 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 0 links · §4 0 links · 0 issues cited · 0 typed | UnreadableCode1-patch-1 (1 commit not in develop); UnreadableCode1-patch-2 (8 commits not in develop); UnreadableCode1-patch-3 (1 commit not in develop) |
| G14 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | jvillacorte-patch-3 (1 commit not in develop) |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 74 〈placeholders〉 | none |
| G16 | §2 12 links · §4 9 links · 20 issues cited · 0 typed | §2 12 links · §4 10 links · 21 issues cited · 0 typed | feature/5-bridgewatch-prototype (1 commit not in develop) |
| G17 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 77 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | none |
| G19 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 80 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 11 typed · 26 〈placeholders〉 | course-update-2026-10-09 (2 commits not in develop); revert-1-23jdo5-patch-1 (11 commits not in develop) |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 63 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 9 links / skeleton | 18 of 21 | 0 of 18 | 5 / 5 of 18 | 11 of 17 | 4 / 3 | ⚠️ Gaps |
| G02 | skeleton / skeleton | 0 of 23 | 0 of 0 | 0 / 0 of 0 | 4 of 13 | 1 / 1 | ❌ Broken |
| G03 | skeleton / skeleton | 0 of 10 | 0 of 0 | 0 / 0 of 0 | 3 of 10 | 1 / 0 | ❌ Broken |
| G04 | skeleton / skeleton | 0 of 7 | 0 of 0 | 0 / 0 of 0 | 1 of 8 | 0 / 0 | ❌ Broken |
| G05 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 0 of 0 | 0 / 0 | ❌ Broken |
| G06 | skeleton / skeleton | 0 of 5 | 0 of 0 | 0 / 0 of 0 | 0 of 1 | 12 / 0 | ❌ Broken |
| G07 | 16 links / skeleton | 16 of 24 | 0 of 16 | 0 / 0 of 16 | 1 of 2 | 17 / 2 | ⚠️ Gaps |
| G08 | skeleton / skeleton | 7 of 33 | 0 of 7 | 0 / 5 of 7 | 1 of 5 | 0 / 0 | ⚠️ Gaps |
| G09 | skeleton / skeleton | 0 of 27 | 0 of 0 | 0 / 0 of 0 | 1 of 5 | 1 / 0 | ❌ Broken |
| G10 | skeleton / skeleton | 0 of 10 | 0 of 0 | 0 / 0 of 0 | 1 of 3 | 14 / 4 | ❌ Broken |
| G11 | skeleton / skeleton | 2 of 11 | 0 of 2 | 0 / 1 of 2 | 0 of 7 | 1 / 1 | ❌ Broken |
| G12 | 0 links / 10 links | 10 of 18 | 0 of 10 | 5 / 4 of 10 | 3 of 13 | 1 / 1 | ⚠️ Gaps |
| G13 | 0 links / 0 links | 0 of 25 | 0 of 0 | 0 / 0 of 0 | 2 of 11 | 1 / 0 | ❌ Broken |
| G14 | skeleton / skeleton | 0 of 4 | 0 of 0 | 0 / 0 of 0 | 2 of 7 | 1 / 1 | ❌ Broken |
| G15 | skeleton / skeleton | 0 of 6 | 0 of 0 | 0 / 0 of 0 | 3 of 8 | 4 / 4 | ❌ Broken |
| G16 | 12 links / 10 links | 21 of 21 | 0 of 21 | 4 / 6 of 21 | 5 of 16 | 3 / 3 | ⚠️ Gaps |
| G17 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 4 of 4 | 8 / 1 | ❌ Broken |
| G18 | skeleton / skeleton | 0 of 12 | 0 of 0 | 0 / 0 of 0 | 0 of 7 | 1 / 1 | ❌ Broken |
| G19 | 11 links / skeleton | 13 of 14 | 11 of 13 | 0 / 2 of 13 | 2 of 5 | 36 / 28 | ⚠️ Gaps |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 3 | 1 / 1 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [CPSC490-01-BGAF](https://github.com/users/LeDuy23/projects/2) ⚠️ not linked to the repo | 0 of 16 | ❌ View 1 (table) | 10 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 13 of 13 | ✅ | 2 | none | none |
| G03 | ❌ none (README links github.com/users/eccortes4/projects/1 but it isn't readable (private, or wrong URL)) | – | – | 9 (Sprint 1 rule) | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 0 of 0 | ✅ | 5 | none | none |
| G05 | ❌ none | – | – | none | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 5 of 5 | ✅ | 2 | none | none |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 20 of 21 | ❌ View 1 (table) | none | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 30 of 32 | ✅ | 9 | none | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 25 of 25 | ✅ | 10 | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 2 of 2 | ✅ | 3 | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/Card1n/projects/1) ⚠️ not linked to the repo | 6 of 7 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 6 of 6 | ✅ | none | none | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 21 of 24 | ✅ | 18 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 3 of 4 | ✅ | 1 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 1 of 4 | ✅ | 2 | none | none |
| G16 | ❌ none (README links github.com/users/garybs16/projects/2 but it isn't readable (private, or wrong URL)) | – | – | none | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 0 of 0 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 3 of 4 | ✅ | 8 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 13 of 14 | ✅ | 1 | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 21 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 23 issues; epics, stories, points, Sprint 1 | matches | ⚠️ **Partial** |
| G03 California | Three AIs and Literate Programming | 10 issues (1 new); points, Sprint 1 | matches | ⚠️ **Process only** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 7 issues; points, Sprint 1 | matches | ⚠️ **Process only** |
| G05 Fighting Mongooses | WILS | 0 issues; no epics or stories | not yet | ❌ **No issues** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 5 issues; epics, stories, Sprint 1 | matches | ⚠️ **Partial** |
| G07 Mighty Morphin | Online Material Database | 24 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 33 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 27 issues (12 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | On-Chain Stablecoin Flow and Wash Trading Detection | 10 issues (1 new); epics, points, Sprint 1 | matches | ⚠️ **Partial** |
| G11 5 Guys | Marathon Tracker | 11 issues; epics, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G12 ACJMM | Explainable 6G Waveform Classification | 18 issues (1 new); epics, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 25 issues (1 new); epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 4 issues; epics, points, Sprint 1 | not yet | ❌ **Mismatch** |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 6 issues; epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 21 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | SonicScape | 0 issues; no epics or stories | matches | ❌ **No issues** |
| G18 Team ProStrats | Project Rogue | 12 issues; epics, stories, Sprint 1 | matches | ⚠️ **Process only** |
| G19 Titan Security | Radar over WiFi | 14 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia | 16 issues; epics, stories | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
