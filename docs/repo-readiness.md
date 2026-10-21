# Group repository status: proposal vs. issue board

> [!IMPORTANT]
> **New (Oct 11): one card per group, ahead of the Sprint 1 reviews.**
> Scroll to **Your group**. Your card combines everything this page checks into one numbered list, in the order to fix it: *Unblock → Document → Board / Scope → Link → Plan → Workflow*. Work through it before your Sprint 1 review: **G01–G05 Tue Oct 13 · G11–G15 Thu Oct 15 · G06–G10 Tue Oct 20 · G16–G20 Thu Oct 22**, and bring the card to the meeting.
>
> The section **Why teams are stuck** explains the patterns behind most cards. Most teams are one merged pull request away from a much better card: §2 of your proposal, merged into `develop`.

**CPSC 490 · Fall 2026 · swept 2026-10-21 23:11 UTC.** The previous edition (2026-10-20) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. **Find your group below: your card lists everything still open for your team, in the order to fix it.** The rules and the full tables are at the end.

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ✅](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ✅](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ✅](#g14) | [**G15** ✅](#g15) | [**G16** ✅](#g16) | [**G17** ⚠️](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

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

**1. The proposal hasn't reached `proposal/proposal.md` yet** (1 groups: G15). §2 *Goals and Objectives* is still the template on both `main` and `develop`. Every other check on this page starts from that file, so until §2 is merged the page shows *0 issues linked*, even for groups that already have user stories on their board (G15). **Do this first:** copy §2 from your HW#4/HW#5 draft into `proposal/proposal.md`, open one pull request into `develop`, and merge it this week.

**2. Finished work is sitting in branches and open pull requests** (12 groups: G01, G02, G03, G05, G07, G08, G09, G11, G12, G13, G16, G18). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**4. The board is a list, not a plan yet.** In 11 groups (G02, G03, G04, G06, G07, G10, G12, G14, G15, G17, G19) at least half the open issues have no assignee, and 16 groups (G01, G02, G03, G04, G05, G06, G07, G08, G11, G12, G13, G14, G15, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 7 groups: G01, G07, G10, G15, G16, G17, G19). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (20 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

**7. Goals haven't become epics and stories yet** (1 groups: G17). Without them, Sprint 2 has nothing to point at. **Do this:** one epic per §2 goal and one user story per objective, titled with the objective's exact words (course README §4).

## Class at a glance

- ✅ **Aligned:** 19 (G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G18, G19, G20)
- ⚠️ **Partial:** 1 (G17)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 0 (none)
- ❌ **Mismatch** (board or README about a different project): 0 (none)
- ❌ **No issues yet:** 0 (none)
- Team-filed issues: **619** across 20 groups (31 new since 2026-10-20).

### What changed since 2026-10-20

- **G10 chain: broken → gaps.** proposal.md now links 15 of 23 issues (was 0) via PR #36 and Sprint 1 is closed. The links are plain `#N`, stories #26–#32 and #35 are unlinked, and feature PRs still go straight to `main`.
- **G08 and G19 switched to typed references.** G08 links 34 of 42 issues as `[story:#N]`-style refs on `develop` (was 7 plain); G19 links all 19 after PR #35. G08 still cites stories in §4, which belong only in §2.
- **G16 stays the only group with an unbroken chain**: prototype and Goal 3 spec merged (#53–#55); only new task #56 still needs a §4 link.
- **G01, G04, G12 and G13 added Sprint 2–4 work** (story points, milestones, new tasks), but G04's six new tasks #49–#54 and several G01/G12 stories have no link or no Sprint milestone yet.
- **Plain `#N` links remain the most common gap** (G06, G07, G09, G12, G13, G20 have 0 typed refs). Switch them to `[story:#N]` so the Word export lists them in Appendix A.
- **G17 is unchanged on the board:** §2 was revised (PR #16) but it cites #1–#6, which are PRs, not issues, and the board still has only epic #15.
- **Course harness (instructor's):** two instructor issues on G19's repo (#9 writing-task rule, #18 Word export) closed now that their fixes are on `main`.
- No repo was renamed. Five groups (G05, G11, G14, G15, G18) had no changes and carry their previous evaluation.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ✅](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ✅](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ✅](#g14) | [**G15** ✅](#g15) | [**G16** ✅](#g16) | [**G17** ⚠️](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 56 issues (38 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge the open develop PRs (#61, #70, #104), give #58 its replacement link, and retarget the open feature PRs (#99-#102) to develop with real PR descriptions.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #104, #102, #101, #100, #99, #70, #61. Work in an open PR doesn't count yet.
2. *Link.* Cite 1 of 56 issues in `proposal.md` (epics and stories in §2, the rest in §4): #58.
3. *Plan.* Give #58 its own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign 14 of 38 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (14 of 39 PRs closed no issue).

*Since 2026-10-20:* Epics lost their sp: and stories now carry sp: with a Sprint 2 milestone; Objective 1.3 (#58) was dropped and closed, new research and architecture tasks (#91-#94) and PRs #99-#102 were opened, and develop still lags main.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

✅ **Aligned** · chain ⚠️ Gaps · 46 issues (25 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill proposal section 4 with typed links for the 28 unlinked issues, give the closed Sprint 1 tasks sp: (or fold them under a story), and add a story for the multi-node architecture.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #74. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Multi-node distribution (several capture nodes feeding one backend, laptop/Raspberry Pi deployment) has no story of its own.
4. *Link.* Cite 28 of 46 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15, #17, #18, #20–#25, #36–#41, #67–#70, #72, #73.
5. *Plan.* Give #6, #8–#13, #15, #36–#41, #70, #72 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 23 of 25 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 20 PRs closed no issue).

*Since 2026-10-20:* One new process issue (#73, README.old.md cleanup) and PR #74 opened; links (18 of 46), the section 4 skeleton and the goal-to-story tree are otherwise unchanged.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

✅ **Aligned** · chain ⚠️ Gaps · 31 issues (21 open) · Sprint 1 milestone: 0 open, 6 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge develop into main, close duplicate #32, give stories a Sprint milestone, and add a Goal 3 objective for model training plus a story for equation-to-code generation.

Everything still open, in the order to fix it:

1. *Unblock.* 3 branches hold work that isn't in `develop`: `Elizabeth-7-7-patch-1`, `Sehaj36-patch-1`, `eccortes4-proposal-epic-issues`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Goal 3 has one story (#37 loss curve): no objective for the model training itself; No story for AI 2 equation-to-code generation as its own objective.
4. *Link.* Cite 14 of 31 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #2, #4, #5, #13, #15–#17, #20, #24, #39, #41, #42, #51.
5. *Link.* Rewrite 5 bare `#N` references as typed links, e.g. `[[story:#44]](https://github.com/eccortes4/CPSC490-G03-California/issues/44)`.
6. *Plan.* Add 5 open issues to the board: #1, #20, #24, #27, #42.
7. *Plan.* Give #1, #2, #20, #24, #31, #32, #34–#37, #39, #41, #42, #45–#48, #50 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 14 of 21 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 15 PRs closed no issue).

*Since 2026-10-20:* No material change: still 31 issues with 17 linked from develop's proposal.md, duplicate story #31/#32, no Sprint milestone on any story, revised section 2 not yet on main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polygon Prediction Market PNL and Trader Profitability Analytics

✅ **Aligned** · chain ⚠️ Gaps · 30 issues (21 open) · Sprint 1 milestone: 0 open, 9 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Give the 10 stories without a Sprint (#26-#28, #30-#32, #35-#38) a Sprint milestone, link the six Sprint 2 tasks #49-#54 from proposal section 4, and start the Sprint 2 prototype PRs.

Everything still open, in the order to fix it:

1. *Link.* Cite 6 of 30 issues in `proposal.md` (epics and stories in §2, the rest in §4): #49–#54.
2. *Plan.* Give #12, #13, #26–#28, #30–#32, #35–#38 their own `sp:` label and a `Sprint N` milestone.
3. *Plan.* Assign all 21 open issues to one person each.
4. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 16 PRs closed no issue).

*Since 2026-10-20:* Six new Sprint 2 documentation tasks (#49-#54) were added, so linked share fell from 24 of 24 to 24 of 30; stories #25 and #34 now sit in Sprint 2 and no prototype code or PR exists yet.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS: Whale Identification/Location System

✅ **Aligned** · chain ⚠️ Gaps · 20 issues (11 open) · Sprint 1 milestone: 0 open, 7 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill proposal section 4 with typed [task:#N] links for the 9 unlinked issues, assign the stories to Sprint milestones, and merge the feature/15-direction-estimate branch via a PR into develop.

Everything still open, in the order to fix it:

1. *Unblock.* 1 branch holds work that isn't in `develop`: `feature/15-direction-estimate`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 9 of 20 issues in `proposal.md` (epics and stories in §2, the rest in §4): #20, #23–#26, #29, #31, #33, #35.
4. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Assign 2 of 11 open issues to one person each.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-20:* All 11 section 2 links are now typed and develop is synced with main; the board is otherwise unchanged and section 4 is still a skeleton.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · Forecast Market Analytics: GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking

✅ **Aligned** · chain ⚠️ Gaps · 23 issues (21 open) · Sprint 1 milestone: 6 open, 2 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Close or re-parent stale #3-#6 and duplicate #25, convert develop's proposal.md links to typed epic/story links, and close or roll over the 6 open Sprint 1 issues (due 10-19).

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 1 of 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #25.
3. *Link.* Rewrite 22 bare `#N` references as typed links, e.g. `[[story:#31]](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/31)`.
4. *Plan.* Add 4 open issues to the board: #3–#6.
5. *Plan.* Give #5, #6 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 17 of 21 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-20:* No material change: develop's proposal.md still links 22 of 23 issues with none typed; stale #3-#6 and duplicate #25 remain, and Sprint 1 is past due with 6 open.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Materials Database

✅ **Aligned** · chain ⚠️ Gaps · 45 issues (37 open) · Sprint 1 milestone: 6 open, 7 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Replace the template README on main/develop with the project README (task #57), give stories #12-#27 a Sprint milestone, and merge #56 so proposal.md uses typed refs.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #56, #50. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Link.* Cite 21 of 45 issues in `proposal.md` (epics and stories in §2, the rest in §4): #28, #29, #34, #36, #38–#41, #43–#49, #51–#55, #57.
5. *Link.* Rewrite 24 bare `#N` references as typed links, e.g. `[[story:#42]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/42)`.
6. *Plan.* Give #12–#16, #18–#21, #23–#27 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 21 of 37 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 5 PRs closed no issue).

*Since 2026-10-20:* Goal 0 design epic with stories and diagram tasks (#36-#49), sponsor-forms epic and Sprint 1 writing tasks (#51-#57) added, board has 3 views and the typed-link fix PR #56 is open, but proposal.md still has 0 typed refs and the README is still the course template.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

✅ **Aligned** · chain ⚠️ Gaps · 42 issues (32 open) · Sprint 1 milestone: 0 open, 7 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Remove the duplicate/placeholder issues from the chain, replace the template Deliverable placeholders in tasks #23-#36, and merge develop into main after sprint review so main shows the real proposal.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #56. Work in an open PR doesn't count yet.
2. *Link.* Cite 8 of 42 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #7, #45–#47, #58, #60, #62.
3. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
4. *Plan.* Add 2 open issues to the board: #60, #62.
5. *Plan.* Give #45–#47, #49, #60, #62 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Remove `sp:` from #36: they're under a user story, which carries the points.
7. *Plan.* Assign 9 of 32 open issues to one person each.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 14 PRs closed no issue).

*Since 2026-10-20:* Big step forward: proposal.md on develop now links 34 of 42 issues as typed refs (was 7 bare), tasks 1.1.1-3.3.2 and Sprint 2-4 milestones exist, README names the project, and 8 PRs closed issues; but refs are misplaced in §4 and main is not synced.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (16 open) · Sprint 1 milestone: 0 open, 11 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Open a develop->main PR after sprint review, and write proposal §3/§4/§5-6 (#16-#18) in Sprint 2 with typed links, since §4 is still skeleton.

Everything still open, in the order to fix it:

1. *Unblock.* 1 branch holds work that isn't in `develop`: `proposal-draft`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Abstract features not carried into §2 objectives (automatic mileage tracking, parts finder, climate-based recommendations, DIY logs); acceptable if §2 deliberately narrowed scope, but say so in the proposal.
4. *Link.* Cite 3 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #16–#18.
5. *Link.* Rewrite 24 bare `#N` references as typed links, e.g. `[[story:#38]](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad/issues/38)`.
6. *Plan.* Assign 2 of 16 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 10 PRs closed no issue).

*Since 2026-10-20:* Sprint 1 closed out (11 of 11 closed, sprint-1 review PR #43 merged) and develop now links 24 of 27 issues from proposal.md with §2 written and README filled in, but all links are bare, §4 is skeleton and main is stale.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: Stablecoin Wash-Trading and Suspicious Transaction Detection

✅ **Aligned** · chain ⚠️ Gaps · 23 issues (12 open) · Sprint 1 milestone: 0 open, 11 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Link stories #26-#32 and #35 from proposal.md as typed refs, fix the leftover text in epics #23/#24, and open feature branches into develop instead of main.

Everything still open, in the order to fix it:

1. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Validation strategy and key risks (proposal sections) have no issue; acceptable until Sprint 3 if a task is added.
2. *Link.* Cite 8 of 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #26–#32, #35.
3. *Link.* Rewrite 15 bare `#N` references as typed links, e.g. `[[story:#33]](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak/issues/33)`.
4. *Plan.* Assign all 12 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (28 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 8 PRs closed no issue).

*Since 2026-10-20:* Proposal.md now links 15 of 23 issues (was 0) via PR #36, Sprint 1 is fully closed and the develop branch is merged into main, but links are bare, 7 stories are still unlinked and 14 direct commits remain.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

✅ **Aligned** · chain ⚠️ Gaps · 22 issues (12 open) · Sprint 1 milestone: 2 open, 8 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Merge PR #39 so main carries §2, replace the README (still the course setup guide on both branches) with the Marathon Tracker README, and add typed task links in §4.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #39. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Public marathon datasets as the ML baseline and recommending more efficient routes (Abstract/HW#4) have no objective; Low-cost/accessibility aim has no acceptance criterion.
5. *Link.* Cite 12 of 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1–#3, #6–#9, #17, #20, #34, #37, #38.
6. *Link.* Rewrite 1 bare `#N` reference as typed links, e.g. `[[story:#13]](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys/issues/13)`.
7. *Plan.* Give #1, #2, #6, #13, #34 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 2 of 12 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-20:* Little since 10-18: PR #39 (develop to main) is still open, README is still the setup guide, #34 and #13 are now closed, and develop still links 10 of 22 issues.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

✅ **Aligned** · chain ⚠️ Gaps · 38 issues (18 open) · Sprint 1 milestone: 0 open, 41 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Fill in the project README (title, sponsor RTX-1, summary, board link) on develop and main, re-parent stories #66-#71 to the right epics, and put them in a Sprint milestone.

Everything still open, in the order to fix it:

1. *Unblock.* 2 branches hold work that isn't in `develop`: `Application-Structure`, `docs/team-documentation`. Open a pull request for each, or delete the branch.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Evaluation under varied SNR/channel conditions and shortcut-avoidance (proposal's stated motivation) has no story; no interface control document item.
4. *Link.* Cite 7 of 38 issues in `proposal.md` (epics and stories in §2, the rest in §4): #27–#32, #36.
5. *Link.* Rewrite 31 bare `#N` references as typed links, e.g. `[[story:#88]](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/88)`.
6. *Plan.* Give #63, #66–#68, #70, #71, #85 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Remove `sp:` from #88: they're under a user story, which carries the points.
8. *Plan.* Assign 12 of 18 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 29 PRs closed no issue).

*Since 2026-10-20:* Epics and stories (#57-#71, #83, #84, #88) and Sprint 2 work are on the board and proposal.md links 31 of 38 issues; Sprint 1 is fully closed, but links remain bare, six stories have no Sprint, #88 has points under a story and the README is still the template.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ⚠️ Gaps · 84 issues (68 open) · Sprint 1 milestone: 0 open, 12 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Fix platform contradictions: proposal section 4/5 say a web app and the README says a mobile app, while the abstract and Objective 3.3 say a Windows desktop app; pick one and update all three, then start the first Sprint 2 feature PR (Objective 1.1, #22).

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #112. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Link.* Cite 18 of 84 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15, #30–#35, #43, #44, #47, #107, #111, #113.
4. *Link.* Rewrite 66 bare `#N` references as typed links, e.g. `[[story:#106]](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/106)`.
5. *Plan.* Give #8, #10–#13, #15, #25–#27, #31–#34, #44, #47, #113 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 30 of 68 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 21 PRs closed no issue).

*Since 2026-10-20:* New docs PR #112 open for the spec/development plan (issues #111, #113), objectives carry sp: with Sprints 2-4 assigned, but proposal links are still 66 of 84 and all bare (0 typed).

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Rogue-Lite Cyber Sandbox

✅ **Aligned** · chain ⚠️ Gaps · 23 issues (21 open) · Sprint 1 milestone: 0 open, 4 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Add sp: and a Sprint 2 milestone to all 18 stories (#24-#41; Sprint 2 is empty and ends 10-28), make #13 a parented task with sp:, and link all issues from proposal.md as typed refs.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Python/PySide6 technology setup (no setup task); Learner-outcome evaluation of the training value (no objective).
3. *Link.* Cite 3 of 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #4, #6, #13.
4. *Link.* Rewrite 20 bare `#N` references as typed links, e.g. `[[story:#41]](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/41)`.
5. *Plan.* Add 1 open issue to the board: #13.
6. *Plan.* Give #13, #24–#41 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign all 21 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 9 PRs closed no issue).

*Since 2026-10-20:* From 3 process issues to 23 (epics #22/#23 and 18 measurable objective stories #24-#41); proposal.md section 2 now links all 20 epics/stories and the README names the same project, but no story has sp: or a Sprint milestone and links are untyped.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Low End Hardware/ECS Architecture Game Engine with Game

✅ **Aligned** · chain ⚠️ Gaps · 22 issues (11 open) · Sprint 1 milestone: 0 open, 7 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Add a benchmarking objective (ECS vs a baseline under entity count) and a memory-management objective, put stories #26-#33 into Sprint 2 (they have sp: but no milestone), and fill the epic/story bodies still holding template text.

Everything still open, in the order to fix it:

1. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Benchmarking and performance evaluation (the proposal's central goal); Custom memory management; Legacy-OpenGL compatibility testing on old hardware.
4. *Link.* Cite 11 of 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #10–#12, #16, #34–#36, #40, #43, #44.
5. *Link.* Rewrite 11 bare `#N` references as typed links, e.g. `[[story:#33]](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/33)`.
6. *Plan.* Give #16, #26–#33, #43, #44 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 10 of 11 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (8 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 14 PRs closed no issue).

*Since 2026-10-20:* Stories #26-#33 filled in under epics #24/#25 (ECS, renderer, editor, game loop), the develop README now describes the project, and 11 of 22 issues are linked from proposal.md on develop, but links are bare, section 2 is still skeleton, main has none, and benchmarking remains untracked.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ✅ OK · 24 issues (17 open) · Sprint 1 milestone: 7 open, 8 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Link #56 from proposal.md section 4 as [task:#56], merge the Sprint 1 close-out PRs (#57, #59), and open the first Sprint 2 PR closing Objective 1.1 (#14) using real SonarX data.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #59, #57. Work in an open PR doesn't count yet.
2. *Link.* Cite 1 of 24 issues in `proposal.md` (epics and stories in §2, the rest in §4): #56.
3. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
4. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 28 PRs closed no issue).

*Since 2026-10-20:* Prototype and Goal 3 spec work merged (#53-#55), Sprint 1 close-out PRs #57/#59 opened, new task #56 not yet in proposal; 23 of 24 issues typed-linked.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: EchoSphere / SonicScape

⚠️ **Partial** · chain ❌ Broken · 1 issues (1 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Create the Goal 1-3 epics and the six objective stories that proposal.md section 2 describes (it cites #1-#6, which are PRs), reconcile section 2 with the space-UI idea in the abstract, and file Sprint 1 tasks with sp:.

Everything still open, in the order to fix it:

1. *Board.* Create one **user story** per objective, titled with the objective's exact words.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: proposal.md Goals 1-3 and all six objectives have no issues (section 2 cites #1-#6, which are PRs, not issues); space-map UI and NASA data parser from HW#4 have no stories; recommendation/preference learning has no issue; no process or writing tasks in Sprint 1.
3. *Link.* Cite all 1 issues in `proposal.md` (epics and stories in §2, the rest in §4): #15.
4. *Plan.* Assign all 1 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (6 of 6 PRs closed no issue).

*Since 2026-10-20:* Proposal.md section 2 was revised to account/preferences/persistence goals (PR #16), but the board still holds only epic #15 on the old space-UI idea; no new issues, no linked refs, all Sprint milestones empty.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (19 open) · Sprint 1 milestone: 15 open, 7 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Merge develop into main so §2 appears there, add §4 typed task links (§4 is still skeleton), move the [epic:#29-31] cites out of §1 into §2, and close stub #13 and retire old epics #17/#19.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #44. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 14 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #2, #5–#9, #13, #15, #17–#20, #26, #28.
4. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
5. *Plan.* Add 2 open issues to the board: #13, #26.
6. *Plan.* Give #2, #6–#9, #13, #18, #20, #26, #41 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 7 of 19 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-20:* Only change since 10-18 is PR #44 (shared movement) opened into develop; §4 is still skeleton, main still has the skeleton, and 13 of 27 issues remain linked.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi

✅ **Aligned** · chain ⚠️ Gaps · 19 issues (18 open) · Sprint 1 milestone: 16 open, 5 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Make #23 a typed task with sp: and a Sprint milestone, fill section 4 (still a skeleton) with the writing tasks, and begin Objective 1.1 (#8) with a PR into develop; no objective is closed yet.

Everything still open, in the order to fix it:

1. *Link.* Fix the type on : the tag must match the issue's own type.
2. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
3. *Plan.* Assign 12 of 18 open issues to one person each.
4. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 10 PRs closed no issue).

*Since 2026-10-20:* All 19 issues now linked as typed refs (was 13 of 19, 3 typed) after PR #35 merged and #34 closed; #23 still untyped, 1 of 21 Sprint 1 issues closed.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia

✅ **Aligned** · chain ⚠️ Gaps · 16 issues (16 open) · Sprint 1 milestone: 5 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Link all 16 issues from proposal.md as typed refs (stories under section 2, tasks #11, #24, #26-#28 under section 4), and give the 8 stories a Sprint milestone (they already carry sp:).

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 13 of 16 issues in `proposal.md` (epics and stories in §2, the rest in §4): #11, #13–#15, #18–#20, #22–#24, #26–#28.
3. *Link.* Rewrite 3 bare `#N` references as typed links, e.g. `[[story:#21]](https://github.com/muntay89/CPSC490-G20-Solos/issues/21)`.
4. *Plan.* Give #13–#15, #18–#20, #22, #23 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Assign 3 of 16 open issues to one person each.
6. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 3 PRs closed no issue).

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
| G01 | §2 15 links · §4 40 links · 55 issues cited · 67 typed | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 15 〈placeholders〉 | 18-abstract-intro (2 commits not in develop); 43-update-goals-and-objectives (2 commits not in develop); 58-cite-dropped-objective (1 commit not in develop); 80-storage-choice (34 commits not in develop); 84-pipeline-dfd (34 commits not in develop); 88-backend-why-ours-differs (34 commits not in develop); Damon (1 commit not in develop); Sp2_Doc_Damon (23 commits not in develop) |
| G02 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | task/69-readme-roles (28 commits not in develop) |
| G03 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 42 〈placeholders〉 | §2 17 links · §4 skeleton · 17 issues cited · 13 typed · 41 〈placeholders〉 | Elizabeth-7-7-patch-1 (1 commit not in develop); Sehaj36-patch-1 (1 commit not in develop); eccortes4-proposal-epic-issues (1 commit not in develop) |
| G04 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | none |
| G05 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | feature/15-direction-estimate (4 commits not in develop) |
| G06 | §2 17 links · §4 skeleton · 17 issues cited · 17 typed · 47 〈placeholders〉 | §2 17 links · §4 skeleton · 22 issues cited · 0 typed · 82 〈placeholders〉 | none |
| G07 | §2 24 links · §4 skeleton · 24 issues cited · 0 typed · 40 〈placeholders〉 | §2 24 links · §4 skeleton · 24 issues cited · 0 typed · 40 〈placeholders〉 | 51-typed-proposal-issue-links (1 commit not in develop); review (2 commits not in develop) |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 11 links · §4 31 links · 34 issues cited · 61 typed (19 misplaced) · 21 〈placeholders〉 | feature/8-document-crime-data-sources (3 commits not in develop) |
| G09 | §2 skeleton · §4 skeleton · 12 issues cited · 0 typed · 62 〈placeholders〉 | §2 12 links · §4 skeleton · 24 issues cited · 0 typed · 25 〈placeholders〉 | proposal-draft (3 commits not in develop) |
| G10 | §2 5 links · §4 10 links · 15 issues cited · 0 typed · 6 〈placeholders〉 | §2 5 links · §4 10 links · 15 issues cited · 0 typed · 6 〈placeholders〉 | none |
| G11 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 67 〈placeholders〉 | §2 9 links · §4 skeleton · 10 issues cited · 9 typed · 58 〈placeholders〉 | feature/38-merge-develop-into-main (5 commits not in develop) |
| G12 | §2 17 links · §4 14 links · 31 issues cited · 0 typed | §2 17 links · §4 14 links · 31 issues cited · 0 typed | Application-Structure (5 commits not in develop); docs/team-documentation (3 commits not in develop) |
| G13 | §2 12 links · §4 48 links · 52 issues cited · 0 typed | §2 12 links · §4 54 links · 66 issues cited · 0 typed | documentation/111-spec-and-development-plan (4 commits not in develop); feature/34-project-proposal (28 commits not in develop); sprint1-patch-1 (1 commit not in develop); updated-proposal (6 commits not in develop) |
| G14 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | none |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 11 issues cited · 0 typed · 35 〈placeholders〉 | none |
| G16 | §2 12 links · §4 10 links · 22 issues cited · 22 typed | §2 12 links · §4 11 links · 23 issues cited · 24 typed | 30-sprint-1-final (4 commits not in develop); release/0.1 (3 commits not in develop) |
| G17 | §2 6 links · §4 skeleton · 0 issues cited · 0 typed · 41 〈placeholders〉 | §2 4 links · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 13 links · §4 skeleton · 13 issues cited · 18 typed (5 misplaced) · 40 〈placeholders〉 | feature/36-shared-movement (1 commit not in develop) |
| G19 | §2 11 links · §4 skeleton · 19 issues cited · 19 typed · 26 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 3 typed · 26 〈placeholders〉 | none |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 63 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 15 links / 40 links | 55 of 56 | 55 of 55 | 17 / 18 of 55 | 14 of 39 | 3 / 3 | ⚠️ Gaps |
| G02 | 18 links / skeleton | 18 of 46 | 18 of 18 | 0 / 0 of 18 | 4 of 20 | 1 / 1 | ⚠️ Gaps |
| G03 | 17 links / skeleton | 17 of 31 | 12 of 17; 1 bad link | 0 / 0 of 17 | 4 of 15 | 1 / 1 | ⚠️ Gaps |
| G04 | 15 links / 9 links | 24 of 30 | 24 of 24 | 9 / 6 of 24 | 1 of 16 | 0 / 0 | ⚠️ Gaps |
| G05 | 11 links / skeleton | 11 of 20 | 11 of 11 | 0 / 0 of 11 | 0 of 9 | 0 / 0 | ⚠️ Gaps |
| G06 | 17 links / skeleton | 22 of 23 | 0 of 22 | 2 / 3 of 22 | 0 of 5 | 0 / 0 | ⚠️ Gaps |
| G07 | 24 links / skeleton | 24 of 45 | 0 of 24 | 5 / 0 of 24 | 2 of 5 | 2 / 2 | ⚠️ Gaps |
| G08 | 11 links / 31 links | 34 of 42 | 34 of 34; 19 in the wrong section | 4 / 8 of 34 | 3 of 14 | 0 / 0 | ⚠️ Gaps |
| G09 | 12 links / skeleton | 24 of 27 | 0 of 24 | 11 / 9 of 24 | 1 of 10 | 0 / 0 | ⚠️ Gaps |
| G10 | 5 links / 10 links | 15 of 23 | 0 of 15 | 10 / 2 of 15 | 3 of 8 | 14 / 14 | ⚠️ Gaps |
| G11 | 9 links / skeleton | 10 of 22 | 9 of 10 | 1 / 1 of 10 | 0 of 11 | 1 / 1 | ⚠️ Gaps |
| G12 | 17 links / 14 links | 31 of 38 | 0 of 31 | 13 / 10 of 31 | 3 of 29 | 1 / 1 | ⚠️ Gaps |
| G13 | 12 links / 54 links | 66 of 84 | 0 of 66 | 0 / 0 of 66 | 5 of 21 | 0 / 0 | ⚠️ Gaps |
| G14 | 20 links / skeleton | 20 of 23 | 0 of 20 | 0 / 0 of 20 | 2 of 9 | 1 / 1 | ⚠️ Gaps |
| G15 | skeleton / skeleton | 11 of 22 | 0 of 11 | 0 / 0 of 11 | 4 of 14 | 4 / 4 | ⚠️ Gaps |
| G16 | 12 links / 11 links | 23 of 24 | 23 of 23 | 7 / 12 of 23 | 5 of 28 | 3 / 3 | ✅ OK |
| G17 | 6 links / skeleton | 0 of 1 | 0 of 0 | 0 / 0 of 0 | 6 of 6 | 2 / 2 | ❌ Broken |
| G18 | 13 links / skeleton | 13 of 27 | 13 of 13; 5 in the wrong section | 0 / 1 of 13 | 0 of 10 | 1 / 1 | ⚠️ Gaps |
| G19 | 11 links / skeleton | 19 of 19 | 19 of 19; 1 wrong type | 1 / 7 of 19 | 2 of 10 | 36 / 28 | ⚠️ Gaps |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 3 | 1 / 1 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [BGAF Sprint Board](https://github.com/users/LeDuy23/projects/3) | 38 of 38 | ✅ | 1 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 25 of 25 | ✅ | 16 | none | none |
| G03 | ✅ [CPSC-490-G03-California](https://github.com/users/eccortes4/projects/1) | 16 of 21 | ✅ | 18 | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 21 of 21 | ✅ | 12 | none | none |
| G05 | ✅ [WILS](https://github.com/users/M-Kwatcher/projects/2) | 11 of 11 | ✅ | 1 | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 17 of 21 | ✅ | 2 | none | none |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 37 of 37 | ✅ | 14 | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 30 of 32 | ✅ | 6 | 1 | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 16 of 16 | ✅ | none | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 12 of 12 | ✅ | none | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/markachavez2003-lab/projects/1) | 12 of 12 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 18 of 18 | ✅ | 7 | 1 | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 68 of 68 | ✅ | 16 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 20 of 21 | ✅ | 19 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 11 of 11 | ✅ | 11 | none | none |
| G16 | ✅ [Sprint Board](https://github.com/users/garybs16/projects/2) | 17 of 17 | ✅ | none | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 1 of 1 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 17 of 19 | ✅ | 10 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 18 of 18 | ✅ | 1 | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 56 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 46 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G03 California | Three AIs and Literate Programming | 31 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 30 issues (6 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G05 Fighting Mongooses | WILS: Whale Identification/Location System | 20 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 23 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G07 Mighty Morphin | Online Materials Database | 45 issues (18 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 42 issues (4 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | Stablecoin Wash-Trading and Suspicious Transaction Detection | 23 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G11 5 Guys | Marathon Tracker | 22 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G12 ACJMM | Explainable 6G Waveform Classification | 38 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 84 issues (1 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 23 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G15 HIBBI-01 | Low End Hardware/ECS Architecture Game Engine with Game | 22 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 24 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | EchoSphere / SonicScape | 1 issues; epics | matches | ⚠️ **Partial** |
| G18 Team ProStrats | Project Rogue | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G19 Titan Security | Radar over WiFi | 19 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia | 16 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
