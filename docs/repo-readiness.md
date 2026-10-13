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

**CPSC 490 · Fall 2026 · swept 2026-10-13 19:21 UTC.** The previous edition (2026-10-11) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. **Find your group below: your card lists everything still open for your team, in the order to fix it.** The rules and the full tables are at the end.

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ⚠️](#g03) | [**G04** ✅](#g04) | [**G05** ❌](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ❌](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

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

**1. The proposal hasn't reached `proposal/proposal.md` yet** (8 groups: G05, G06, G08, G09, G11, G14, G15, G17). §2 *Goals and Objectives* is still the template on both `main` and `develop`. Every other check on this page starts from that file, so until §2 is merged the page shows *0 issues linked*, even for groups that already have user stories on their board (G06, G08, G09, G11, G15). **Do this first:** copy §2 from your HW#4/HW#5 draft into `proposal/proposal.md`, open one pull request into `develop`, and merge it this week.

**2. Finished work is sitting in branches and open pull requests** (9 groups: G01, G02, G03, G06, G09, G11, G13, G14, G16). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**4. The board is a list, not a plan yet.** In 12 groups (G02, G03, G04, G06, G07, G09, G10, G12, G13, G14, G19, G20) at least half the open issues have no assignee, and 17 groups (G01, G02, G03, G04, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 8 groups: G01, G06, G07, G10, G15, G16, G17, G19). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (19 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

**7. Goals haven't become epics and stories yet** (3 groups: G05, G14, G17). Without them, Sprint 2 has nothing to point at. **Do this:** one epic per §2 goal and one user story per objective, titled with the objective's exact words (course README §4).

## Class at a glance

- ✅ **Aligned:** 14 (G01, G02, G04, G06, G07, G08, G09, G10, G12, G13, G16, G18, G19, G20)
- ⚠️ **Partial:** 3 (G03, G11, G15)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 0 (none)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 2 (G05, G17)
- Team-filed issues: **418** across 18 groups (131 new since 2026-10-11).

### What changed since 2026-10-11

- Seven teams moved up to ALIGNED on the proposal: G02, G04, G06, G10, G12 and G18 now have epics and user stories that cover their §2 goals. G03 went from PROCESS_ONLY to PARTIAL.
- Six teams moved their document-first chain from BROKEN to GAPS: G02, G03, G04, G09, G13 and G18. Their issues are now linked from `proposal.md`. The remaining gaps are mostly untyped links (`#N` instead of `story:#N`) and stories with no `sp:` or Sprint.
- G06 and G10 are ALIGNED, but their chains are still BROKEN. Neither links any issue from `proposal.md`, and both still commit directly to main.
- G05 and G17 still have no issues, and G14 still has a proposal-to-board MISMATCH. These three teams need help first.
- New since the last edition: G08 opened duplicate stories (#45–#47) on 10-12. G01's research PRs #59/#60 target main instead of develop.
- No repos were renamed and no new course repos appeared. G05, G14, G15, G16 and G20 had no board or proposal changes, so their notes carry over from the last edition.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ⚠️](#g03) | [**G04** ✅](#g04) | [**G05** ❌](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ❌](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (15 open) · Sprint 1 milestone: 4 open, 11 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill the README project summary and contact, give #9/#12/#14 a real parent, and open #59/#60 into develop with Closes #10 and a tracking issue for L1/L2 research.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #60, #59. Work in an open PR doesn't count yet.
2. *Link.* Cite 1 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #58.
3. *Plan.* Give #58 its own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign 6 of 15 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (14 of 25 PRs closed no issue).

*Since 2026-10-11:* Added #58 (story 1.3 for L1/L2 views) and open research PRs #59/#60 into main, and merged the HW5 proposal PRs; 26 of 27 issues are now linked with typed references and the Sprint board has a board view.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

✅ **Aligned** (was Partial) · chain ⚠️ Gaps · 40 issues (26 open) · Sprint 1 milestone: 2 open, 12 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge main back into develop so both carry the §2 links, then link the 16 unlinked work items (#17/#18 and the proposal tasks) in §4 as typed references.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #65. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 16 of 40 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15, #17, #18, #36–#41.
4. *Plan.* Give #6, #15 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Assign all 26 open issues to one person each.
6. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 17 PRs closed no issue).

*Since 2026-10-11:* Filed 3 epics and 15 prototype/data/frontend stories (#45-#61) with sp: and Sprints 2-4 and linked 24 in §2 on main; 24 of 40 issues now linked, up from none, but §4 is still a skeleton and develop is stale.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

⚠️ **Partial** (was Process only) · chain ⚠️ Gaps · 21 issues (14 open) · Sprint 1 milestone: 0 open, 6 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill the epic checklists with the real story numbers, add an epic for the 3-AI pipeline and literate notebook output, and give every story its own sp: and Sprint milestone.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #40. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Integrating the three AIs into one end-to-end pipeline; Literate-programming/notebook documentation output; Code-generation AI as its own goal (epic #28 is framed around input sources, objectives 1.1-1.3 are about sorting inputs, not transcribing them).
4. *Link.* Cite 11 of 21 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #2, #4, #5, #13, #15–#17, #20, #24, #39.
5. *Link.* Rewrite 10 bare `#N` references as typed links, e.g. `[[story:#37]](https://github.com/eccortes4/CPSC490-G03-California/issues/37)`.
6. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.
7. *Plan.* Give #1, #2, #20, #24, #30–#37, #39 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 13 of 14 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 13 PRs closed no issue).

*Since 2026-10-11:* Filed epics #27/#28 and stories #30-#37 and linked them in §2 (all bare, not typed), plus a new open fix PR #40; Sprint 1 is 6 closed, but the Sprint board is still unreadable.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polygon Prediction Market PNL and Trader Profitability Analytics

✅ **Aligned** (was Process only) · chain ⚠️ Gaps · 24 issues (15 open) · Sprint 1 milestone: 0 open, 9 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Give all 12 stories their own sp: label and Sprint 2-4 milestone, and add sp: to sub-tasks #12/#13.

Everything still open, in the order to fix it:

1. *Plan.* Give #12, #13, #25–#28, #30–#32, #34–#38 their own `sp:` label and a `Sprint N` milestone.
2. *Plan.* Assign all 15 open issues to one person each.
3. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 15 PRs closed no issue).

*Since 2026-10-11:* Filed 3 epics and 15 stories mirroring the §2 goals, linked all 24 issues as typed references in §2/§4 on main and develop; chain moved from no links to 24 of 24, with no direct commits.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS

❌ **No issues** · chain ❌ Broken · 0 issues (0 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Your repository has **no epics or user stories**. HW#5 §2 lists 2 goals and 10 objectives, citing Epic #1 and Epic #2, but #1 is an instructor issue and #2 does not exist.
> See [the instructor issue](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses/issues/7) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Run the bootstrap to create the missing epic/user-story/sp:/task labels, commit the real proposal into proposal/proposal.md and the team README, and file Sprint 1 tasks with sp: for each proposal section.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
4. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · Forecast Market Analytics: GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking

✅ **Aligned** (was Partial) · chain ❌ Broken · 23 issues (22 open) · Sprint 1 milestone: 7 open, 1 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** HW#5 §2 has **3 goals and 14 objectives**, but the repository has only Goal 1 (epic #13) with one story (#14, Objective 1.1). Epics #3 *Home Page* and #4 *Create LLM prototype* and stories #5 and #6 are not in HW#5.
> See [the instructor issue](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/15) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Close or re-scope the old epics #3/#4 and stories #5/#6, link every epic and story from proposal §2 as typed references, and retarget PR #32 to develop.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #32. Work in an open PR doesn't count yet.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Link.* Cite all 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #3–#6, #10, #13, #14, #16–#31.
5. *Plan.* Add 4 open issues to the board: #3–#6.
6. *Plan.* Give #5, #6 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Remove `sp:` from #25: they're under a user story, which carries the points.
8. *Plan.* Remove `sp:` from epics #13, #20, #27.
9. *Plan.* Assign 17 of 22 open issues to one person each.
10. *Workflow.* Stop pushing straight to `main`/`develop` (18 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
11. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-11:* Filed the new Goal 1-3 epics and 14 stories (#13-#31) with sp: and Sprints 1-3 in the last two days; still 0 issues linked from proposal.md, 18 direct commits on main and 1 of 2 PRs still open into main.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Material Database

✅ **Aligned** · chain ⚠️ Gaps · 25 issues (22 open) · Sprint 1 milestone: 7 open, 3 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 match, but the **issue numbers in HW#5 §2 are off by one from Goal 3 on**, and the repository has items HW#5 does not.
> See [the instructor issue](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/33) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Convert the 16 bare #N links in proposal.md §2 to typed [epic:#N]/[story:#N] references, fill §4 with typed task links, and replace the placeholder epic #1; then open feature PRs into develop that close the Sprint 1 stories.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 9 of 25 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #4–#7, #27–#29, #34.
4. *Link.* Rewrite 16 bare `#N` references as typed links, e.g. `[[story:#26]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/26)`.
5. *Plan.* Add 1 open issue to the board: #29.
6. *Plan.* Give #34 its own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 19 of 22 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 2 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

✅ **Aligned** · chain ⚠️ Gaps · 36 issues (34 open) · Sprint 1 milestone: 12 open, 1 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals and objectives match HW#5 §2, but the repository has **extra and duplicate items**.
> See [the instructor issue](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/48) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Close duplicate stories #45/#46/#47 and stray epics #6/#7, remove sp: from task #36 (it sits under story #28), then add typed links for all remaining issues to proposal.md §2/§4.

Everything still open, in the order to fix it:

1. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 29 of 36 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6–#13, #17–#24, #27, #29–#36, #42, #45–#47.
4. *Link.* Rewrite 7 bare `#N` references as typed links, e.g. `[[story:#28]](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/28)`.
5. *Plan.* Add 4 open issues to the board: #6, #7, #45, #47.
6. *Plan.* Give #42, #45–#47 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Remove `sp:` from #36: they're under a user story, which carries the points.
8. *Plan.* Assign 14 of 34 open issues to one person each.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 5 PRs closed no issue).

*Since 2026-10-11:* Three duplicate objective issues (#45-#47) were created 10-12 (#46 already closed); proposal.md still links only 7 of 36 issues, all bare, and PR flow is otherwise unchanged.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (23 open) · Sprint 1 milestone: 8 open, 4 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Give each of stories #29-#38 an sp: label and a Sprint milestone, and merge the open PRs (#21, #25, #39, #41) into develop so §2 (already written on develop) reaches main.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #41, #39, #25, #21. Work in an open PR doesn't count yet.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Bulk ingestion of old mixed-format paper records (only structured import #31 exists); Stretch features named in the abstract: automatic mileage tracking, DIY maintenance help, parts finder, climate-based recommendations (likely intentional cut; the proposal should say so).
5. *Link.* Cite 15 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #16–#18, #27–#38.
6. *Link.* Rewrite 12 bare `#N` references as typed links, e.g. `[[story:#19]](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad/issues/19)`.
7. *Plan.* Give #29–#38 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 16 of 23 open issues to one person each.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 8 PRs closed no issue).

*Since 2026-10-11:* Chain improved from BROKEN: 12 of 27 issues now linked from proposal.md on main (bare, not typed), 4 issues closed and 8 tied to PRs (3 merged); stories #29-#38 still lack sp: and Sprint milestones.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: On-Chain Stablecoin Flow and Wash Trading Detection

✅ **Aligned** (was Partial) · chain ❌ Broken · 22 issues (12 open) · Sprint 1 milestone: 3 open, 9 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Link epics #15/#23/#24 and stories #25-#33 from proposal.md §2 and the tasks from §4 as typed references, fix epics #23/#24 whose bodies hold unrelated text ('Members' data is private...'), and stop committing straight to main.

Everything still open, in the order to fix it:

1. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Validation strategy (synthetic ring injection, known case studies, manual precision review) described in Proposed Approaches has no objective or issue; Address-label enrichment (exchanges, bridges, routers) used to control false positives.
2. *Link.* Cite all 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #3–#9, #13, #15, #18, #20, #23–#33.
3. *Plan.* Give #3, #6, #13 their own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign all 12 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (28 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 6 PRs closed no issue).

*Since 2026-10-11:* Epics #23/#24 and stories #25-#33 now exist (verdict moves from PARTIAL to ALIGNED), board has 5 views, but proposal.md still links 0 of 22 issues and 14 direct commits to main remain.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

⚠️ **Partial** · chain ❌ Broken · 20 issues (11 open) · Sprint 1 milestone: 2 open, 9 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Rewrite proposal §2 so Goals 1-3 match epics #4/#26/#27 with their objectives verbatim, then add stories for run recording/storage and for the public marathon-data baseline that the abstract promises.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #35. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Use of publicly available marathon routes and times as the analysis baseline (central to the Abstract); Recording and storing distance, elapsed time and pace per run (proposal Goal 1 objectives); Recommending more efficient running patterns or routes; Low-cost, no-special-equipment accessibility claim (no acceptance criteria).
6. *Link.* Cite 18 of 20 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1–#3, #6–#9, #17, #20, #26–#34.
7. *Link.* Rewrite 2 bare `#N` references as typed links, e.g. `[[story:#13]](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys/issues/13)`.
8. *Plan.* Link your Sprint Board to the repository (the repository's *Projects* tab → *Link a project*).
9. *Plan.* Give #1, #2, #6, #13, #34 their own `sp:` label and a `Sprint N` milestone.
10. *Plan.* Assign 3 of 11 open issues to one person each.
11. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
12. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 9 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

✅ **Aligned** (was Partial) · chain ⚠️ Gaps · 34 issues (18 open) · Sprint 1 milestone: 3 open, 32 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The stories match, but **HW#5 §2 cites placeholder numbers** ([Epic:#1]–[Epic:#5], [Story#1]/[Story#2]) instead of the real issues, and two epic titles differ from §2.
> See [the instructor issue](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/82) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Fill the README (title and project summary are still the course template on develop and main), put the 10 stories into a Sprint milestone, and add stories for parameter estimation and SNR/channel evaluation.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Parameter estimation (baud rate, carrier frequency) has no story; Evaluation across SNR, channel model and observation length, with per-condition metrics, has no story; Modular design for swapping algorithms is not an objective.
3. *Link.* Cite 7 of 34 issues in `proposal.md` (epics and stories in §2, the rest in §4): #27–#32, #36.
4. *Link.* Rewrite 27 bare `#N` references as typed links, e.g. `[[story:#76]](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/76)`.
5. *Plan.* Give #62–#71 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 15 of 18 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 21 PRs closed no issue).

*Since 2026-10-11:* Epics #57-#61 now have 10 stories (#62-#71) and §2 plus §4 link 27 of 34 issues (was 10 of 18), still all bare refs; README still the template and stories have no Sprint milestone.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (26 open) · Sprint 1 milestone: 10 open, 1 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 and their objectives match, but the repository has a **Goal 0 epic (#30) with stories #31–#33** that HW#5 §2 does not have, and §2 cites no issue numbers.
> See [the instructor issue](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/50) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Add sp: to all 9 stories and the tasks, put every issue on a Sprint milestone, and fill the issue bodies (replace placeholder text and the #1.1-style checklist refs with real #N).

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #51, #46. Work in an open PR doesn't count yet.
2. *Link.* Cite 14 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15, #31–#35, #43, #44, #47.
3. *Link.* Rewrite 13 bare `#N` references as typed links, e.g. `[[story:#30]](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/30)`.
4. *Plan.* Add 6 open issues to the board: #8, #12, #13, #30, #32, #33.
5. *Plan.* Give #8, #10–#13, #15, #19–#27, #31–#34 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 19 of 26 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 16 PRs closed no issue).

*Since 2026-10-11:* Stories #19-#27 and epics #16-#18 now exist with real titles and proposal develop links 13 of 27 issues (was 0 of 25), but all bare, epics/stories sit in §4 not §2, and 19 stories/tasks have no sp:.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Rogue-Lite Cyber Sandbox

❌ **Mismatch** · chain ❌ Broken · 4 issues (4 open) · Sprint 1 milestone: 2 open, 2 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2 at all**: it has one epic, #8 *Create web scanner*, and no stories. HW#5 §2 has 2 goals and 10 objectives for a cybersecurity training sandbox.
> See [the instructor issue](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/21) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Agree on one project (the proposal is the Cyber Sandbox), commit the proposal text into proposal.md, write §2 goals, and replace the web scanner epic with epics and stories for the sandbox.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #12, #9. Work in an open PR doesn't count yet.
2. *Document.* Your board or README describes a **different project** than your proposal. Make them match, or tell the instructor the project changed.
3. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
4. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
5. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
6. *Board.* Create one **user story** per objective, titled with the objective's exact words.
7. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Every core element; §2 Goals and Objectives is unwritten, so there are no stories to file.
8. *Link.* Cite all 4 issues in `proposal.md` (epics and stories in §2, the rest in §4): #4, #6, #8, #13.
9. *Plan.* Add 1 open issue to the board: #13.
10. *Plan.* Give #13 its own `sp:` label and a `Sprint N` milestone.
11. *Plan.* Assign 2 of 4 open issues to one person each.
12. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
13. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 7 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Low End Hardware ECS Game Engine with Game

⚠️ **Partial** · chain ❌ Broken · 6 issues (4 open) · Sprint 1 milestone: 2 open, 0 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2**: it has one epic, #6 *Setting up*, with one story, #9 *Window and Renderer*. HW#5 §2 has 2 goals (*Game Demo*, *Game Engine*) and 8 objectives.
> See [the instructor issue](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/23) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write §2 goals and objectives (rendering, ECS, game creation, benchmarking), then retitle #6 and #9 to match, file stories for the missing objectives, and stop committing directly to main (4 direct commits).

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: ECS implementation; Game-creation interface / showcase game; Benchmarking and performance evaluation; Memory management; Story for closing the window (listed in epic #6, no issue).
5. *Link.* Cite all 6 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #9–#12, #16.
6. *Plan.* Add 3 open issues to the board: #6, #9, #10.
7. *Plan.* Give #12, #16 their own `sp:` label and a `Sprint N` milestone.
8. *Workflow.* Stop pushing straight to `main`/`develop` (8 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 8 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ⚠️ Gaps · 21 issues (17 open) · Sprint 1 milestone: 6 open, 3 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Convert the 21 bare issue links in proposal.md to typed references (`[epic:#11]`, `[story:#14]`, `[task:#27]`), then fix the Sprint board (README link is not readable) so every open issue is on it.

Everything still open, in the order to fix it:

1. *Unblock.* 1 branch holds work that isn't in `develop`: `feature/5-bridgewatch-prototype`. Open a pull request for each, or delete the branch.
2. *Link.* Rewrite 21 bare `#N` references as typed links, e.g. `[[story:#39]](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic/issues/39)`.
3. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.
4. *Plan.* Assign 3 of 17 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 16 PRs closed no issue).

*Since 2026-10-11:* Big jump: proposal.md is now the real proposal on develop with all 21 issues linked (was 0 of 19), README describes BridgeWatch, prototype v0 (#36) merged via PR, tasks #34/#39 filed; remaining gaps are untyped links and an unreadable board.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: SonicScape / EchoSphere

❌ **No issues** · chain ❌ Broken · 0 issues (0 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Your repository has **no epics or user stories**. HW#5 §2 lists 2 goals and 5 objectives with placeholder numbers (#〈1〉, #〈2〉).
> See [the instructor issue](https://github.com/vibhorbh/CPSC490-G17-SonicScape/issues/13) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Create the Sprint 1 issues now: one epic per goal with its stories, plus tasks with sp: in the Sprint 1 milestone (due 10-21), then link them from proposal.md §2/§4; also settle on one name (SonicScape vs EchoSphere).

Everything still open, in the order to fix it:

1. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
2. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
3. *Workflow.* Stop pushing straight to `main`/`develop` (11 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
4. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 4 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue

✅ **Aligned** (was Process only) · chain ⚠️ Gaps · 27 issues (19 open) · Sprint 1 milestone: 15 open, 7 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 match (epics #29–#31, stories #32–#41), but the repository has **two extra epics not in HW#5 §2**: #17 (*playable and extensible prototype*, story #18) and #19 (*capstone proposal*, story #20).
> See [the instructor issue](https://github.com/austin2578/CPSC490-G18-ProStrats/issues/43) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Merge develop into main so the filled §2 appears there, add §4 typed links for tasks, and close or retype the untyped HW#4 issues (#5-#9, #13, #26).

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 14 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #2, #5–#9, #13, #15, #17–#20, #26, #28.
3. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
4. *Plan.* Add 2 open issues to the board: #13, #26.
5. *Plan.* Give #2, #6–#9, #13, #18, #20, #26, #41 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 9 of 19 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-11:* Epics #29-#31 and 10 stories (#32-#41) added, §2 links 13 typed refs on develop (was 0 of 12 linked), but §4 is still a skeleton, 14 issues are unlinked, and main still has the skeleton.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over Wi-Fi (ROW) drone detection

✅ **Aligned** · chain ⚠️ Gaps · 18 issues (18 open) · Sprint 1 milestone: 16 open, 4 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Link §4 (still a skeleton) with typed refs for #11, #20, #26-#29, convert the bare epic/story refs to typed form, and replace develop's README with the team README.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 5 of 18 issues in `proposal.md` (epics and stories in §2, the rest in §4): #23, #26–#29.
3. *Link.* Rewrite 10 bare `#N` references as typed links, e.g. `[[story:#20]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/20)`.
4. *Plan.* Add 1 open issue to the board: #23.
5. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 12 of 18 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 9 PRs closed no issue).

*Since 2026-10-11:* Task issues #26-#29 added and PRs #30-#33 merged closing them, but linked issues stayed 13 of 18 (72%, was 13 of 14) with only 3 typed refs, §4 still a skeleton, and main still carries the skeleton.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia

✅ **Aligned** · chain ⚠️ Gaps · 16 issues (16 open) · Sprint 1 milestone: 5 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals and objectives match HW#5 §2, but the **story numbering differs**: the repository uses *Objective 12.1, 17.1, 21.1* (issue numbers) where §2 uses 1.1, 2.1, 3.1.
> See [the instructor issue](https://github.com/muntay89/CPSC490-G20-Solos/issues/31) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write §2 in proposal.md with each goal and objective verbatim, cite all 8 stories there as typed references and the 5 tasks in §4, give the 8 stories sp: plus a Sprint 1 milestone, and add the project title to the proposal.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Unpredictable monster placement/encounters (only distinct behaviors are tracked, not varied placement).
3. *Link.* Cite 13 of 16 issues in `proposal.md` (epics and stories in §2, the rest in §4): #11, #13–#15, #18–#20, #22–#24, #26–#28.
4. *Link.* Rewrite 3 bare `#N` references as typed links, e.g. `[[story:#21]](https://github.com/muntay89/CPSC490-G20-Solos/issues/21)`.
5. *Plan.* Give #13–#15, #18–#20, #22, #23 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 11 of 16 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 3 PRs closed no issue).

*Since 2026-10-11:* From zero issues to 16: three epics, eight stories, five Sprint 1 tasks, a Sprint board with every open issue, README rewritten as Insomnia on develop, and two PRs merged that close issues; only 3 epics are linked from proposal.md and stories lack sp:.

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
| G01 | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 17 〈placeholders〉 | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 17 〈placeholders〉 | 10-L3-orderbook-research (5 commits not in develop); 18-abstract-intro (2 commits not in develop); 43-update-goals-and-objectives (2 commits not in develop); Damon (1 commit not in develop); L1-L2_Orderbook_Research (3 commits not in develop) |
| G02 | §2 24 links · §4 skeleton · 24 issues cited · 24 typed · 44 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | 39-proofread-v2 (21 commits not in develop) |
| G03 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 45 〈placeholders〉 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 45 〈placeholders〉 | Elizabeth-7-7-patch-1 (1 commit not in develop); Sehaj36-patch-1 (1 commit not in develop); eccortes4-proposal-epic-issues (1 commit not in develop); hotfix/doc-formatting (2 commits not in develop) |
| G04 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | none |
| G05 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G06 | §2 0 links · §4 skeleton · 0 issues cited · 0 typed · 47 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 82 〈placeholders〉 | feature/14-document-upload (18 commits not in develop) |
| G07 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | none |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | none |
| G09 | §2 skeleton · §4 skeleton · 12 issues cited · 0 typed · 62 〈placeholders〉 | §2 12 links · §4 skeleton · 12 issues cited · 0 typed · 53 〈placeholders〉 | feature/6-Related-Work-Table-and-9-AI-Usage-+-References (6 commits not in develop); feature/7-problem-statements (2 commits not in develop); feature/8-proposal-cleanup (10 commits not in develop); feature/11-update-readme (5 commits not in develop); feature/19-archive-hw4-draft (1 commit not in develop); proposal-draft (3 commits not in develop) |
| G10 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | none |
| G11 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 67 〈placeholders〉 | §2 skeleton · §4 skeleton · 2 issues cited · 0 typed · 70 〈placeholders〉 | 1-2-problem-statements (1 commit not in develop); feature/3-goals-objectives (1 commit not in develop) |
| G12 | §2 15 links · §4 12 links · 27 issues cited · 0 typed | §2 15 links · §4 12 links · 27 issues cited · 0 typed | none |
| G13 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 0 links · §4 13 links · 13 issues cited · 0 typed | feature/32-project-proposal (6 commits not in develop); proposal-patch-1 (1 commit not in develop); sprint1-patch-1 (1 commit not in develop) |
| G14 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | jvillacorte-patch-3 (1 commit not in develop) |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 74 〈placeholders〉 | none |
| G16 | §2 12 links · §4 9 links · 20 issues cited · 0 typed | §2 12 links · §4 10 links · 21 issues cited · 0 typed | feature/5-bridgewatch-prototype (1 commit not in develop) |
| G17 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 81 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 13 links · §4 skeleton · 13 issues cited · 18 typed (5 misplaced) · 40 〈placeholders〉 | none |
| G19 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 80 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 3 typed · 26 〈placeholders〉 | none |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 63 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 9 links / 17 links | 26 of 27 | 26 of 26 | 11 / 10 of 26 | 14 of 25 | 3 / 3 | ⚠️ Gaps |
| G02 | 24 links / skeleton | 24 of 40 | 24 of 24 | 1 / 1 of 24 | 4 of 17 | 1 / 1 | ⚠️ Gaps |
| G03 | 10 links / skeleton | 10 of 21 | 0 of 10 | 0 / 0 of 10 | 4 of 13 | 1 / 1 | ⚠️ Gaps |
| G04 | 15 links / 9 links | 24 of 24 | 24 of 24 | 9 / 6 of 24 | 1 of 15 | 0 / 0 | ⚠️ Gaps |
| G05 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 0 of 0 | 0 / 0 | ❌ Broken |
| G06 | skeleton / skeleton | 0 of 23 | 0 of 0 | 0 / 0 of 0 | 0 of 2 | 18 / 0 | ❌ Broken |
| G07 | 16 links / skeleton | 16 of 25 | 0 of 16 | 0 / 0 of 16 | 1 of 2 | 2 / 2 | ⚠️ Gaps |
| G08 | skeleton / skeleton | 7 of 36 | 0 of 7 | 0 / 5 of 7 | 1 of 5 | 0 / 0 | ⚠️ Gaps |
| G09 | skeleton / skeleton | 12 of 27 | 0 of 12 | 4 / 8 of 12 | 1 of 8 | 0 / 0 | ⚠️ Gaps |
| G10 | 0 links / 0 links | 0 of 22 | 0 of 0 | 0 / 0 of 0 | 3 of 6 | 14 / 14 | ❌ Broken |
| G11 | skeleton / skeleton | 2 of 20 | 0 of 2 | 1 / 1 of 2 | 1 of 9 | 1 / 1 | ❌ Broken |
| G12 | 15 links / 12 links | 27 of 34 | 0 of 27 | 9 / 6 of 27 | 3 of 21 | 1 / 1 | ⚠️ Gaps |
| G13 | 0 links / 13 links | 13 of 27 | 0 of 13 | 0 / 0 of 13 | 2 of 16 | 0 / 0 | ⚠️ Gaps |
| G14 | skeleton / skeleton | 0 of 4 | 0 of 0 | 0 / 0 of 0 | 2 of 7 | 1 / 1 | ❌ Broken |
| G15 | skeleton / skeleton | 0 of 6 | 0 of 0 | 0 / 0 of 0 | 3 of 8 | 4 / 4 | ❌ Broken |
| G16 | 12 links / 10 links | 21 of 21 | 0 of 21 | 4 / 6 of 21 | 5 of 16 | 3 / 3 | ⚠️ Gaps |
| G17 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 4 of 4 | 10 / 1 | ❌ Broken |
| G18 | 13 links / skeleton | 13 of 27 | 13 of 13; 5 in the wrong section | 0 / 0 of 13 | 0 of 9 | 1 / 1 | ⚠️ Gaps |
| G19 | 11 links / skeleton | 13 of 18 | 3 of 13 | 0 / 2 of 13 | 2 of 9 | 36 / 28 | ⚠️ Gaps |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 3 | 1 / 1 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [Sprint 1](https://github.com/users/LeDuy23/projects/3) | 15 of 15 | ✅ | 1 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 26 of 26 | ✅ | 2 | none | none |
| G03 | ❌ none (README links github.com/users/eccortes4/projects/1 but it isn't readable (private, or wrong URL)) | – | – | 13 | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 15 of 15 | ✅ | 14 | none | none |
| G05 | ❌ none | – | – | none | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 18 of 22 | ✅ | 2 | 1 | 3 |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 21 of 22 | ✅ | 1 | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 30 of 34 | ✅ | 4 | 1 | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 23 of 23 | ✅ | 10 | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 12 of 12 | ✅ | 3 | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/Card1n/projects/1) ⚠️ not linked to the repo | 11 of 11 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 18 of 18 | ✅ | 10 | none | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 20 of 26 | ✅ | 19 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 3 of 4 | ✅ | 1 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 1 of 4 | ✅ | 2 | none | none |
| G16 | ❌ none (README links github.com/users/garybs16/projects/2 but it isn't readable (private, or wrong URL)) | – | – | none | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 0 of 0 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 17 of 19 | ✅ | 10 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 17 of 18 | ✅ | 1 | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 27 issues (6 new); epics, stories, points, Sprint 1 | n/a | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 40 issues (17 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G03 California | Three AIs and Literate Programming | 21 issues (11 new); epics, stories, points, Sprint 1 | matches | ⚠️ **Partial** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 24 issues (17 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G05 Fighting Mongooses | WILS | 0 issues; no epics or stories | not yet | ❌ **No issues** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 23 issues (18 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G07 Mighty Morphin | Online Material Database | 25 issues (1 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 36 issues (3 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | On-Chain Stablecoin Flow and Wash Trading Detection | 22 issues (12 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G11 5 Guys | Marathon Tracker | 20 issues (9 new); epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G12 ACJMM | Explainable 6G Waveform Classification | 34 issues (16 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 27 issues (2 new); epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 4 issues; epics, points, Sprint 1 | not yet | ❌ **Mismatch** |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 6 issues; epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 21 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | SonicScape / EchoSphere | 0 issues; no epics or stories | n/a | ❌ **No issues** |
| G18 Team ProStrats | Project Rogue | 27 issues (15 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G19 Titan Security | Radar over Wi-Fi (ROW) drone detection | 18 issues (4 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia | 16 issues; epics, stories | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
