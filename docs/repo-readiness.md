# Group repository status: proposal vs. issue board

> [!IMPORTANT]
> **New (Oct 11): one card per group, ahead of the Sprint 1 reviews.**
> Scroll to **Your group**. Your card combines everything this page checks into one numbered list, in the order to fix it: *Unblock → Document → Board / Scope → Link → Plan → Workflow*. Work through it before your Sprint 1 review: **G01–G05 Tue Oct 13 · G11–G15 Thu Oct 15 · G06–G10 Tue Oct 20 · G16–G20 Thu Oct 22**, and bring the card to the meeting.
>
> The section **Why teams are stuck** explains the patterns behind most cards. Most teams are one merged pull request away from a much better card: §2 of your proposal, merged into `develop`.

**CPSC 490 · Fall 2026 · swept 2026-10-22 19:58 UTC.** The previous edition (2026-10-21) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. **Find your group below: your card lists everything still open for your team, in the order to fix it.** The rules and the full tables are at the end.

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ✅](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ✅](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ✅](#g14) | [**G15** ✅](#g15) | [**G16** ✅](#g16) | [**G17** ✅](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

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

**2. Finished work is sitting in branches and open pull requests** (10 groups: G01, G02, G03, G05, G06, G07, G12, G13, G16, G18). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**4. The board is a list, not a plan yet.** In 10 groups (G02, G03, G04, G06, G07, G10, G12, G14, G15, G19) at least half the open issues have no assignee, and 16 groups (G01, G02, G03, G04, G05, G06, G07, G08, G11, G12, G13, G14, G15, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 7 groups: G01, G07, G10, G15, G16, G17, G19). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (20 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

## Class at a glance

- ✅ **Aligned:** 20 (G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20)
- ⚠️ **Partial:** 0 (none)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 0 (none)
- ❌ **Mismatch** (board or README about a different project): 0 (none)
- ❌ **No issues yet:** 0 (none)
- Team-filed issues: **668** across 20 groups (48 new since 2026-10-21).

### What changed since 2026-10-21

- G17 moved Partial → Aligned: the board was rebuilt with 3 epics and 6 stories that match the revised proposal §2. The chain is still broken, because §2 still cites the old issue numbers (#1–#6) instead of the new epics and stories.
- G08 and G09 reached a complete document-first chain (CHAIN_OK). Both closed all of their Sprint 1 issues. G09 also merged its proposal, README and sprint review into main.
- G10 now uses typed references for every linked issue (25 typed refs). It still has direct commits on main/develop and feature PRs merged straight into main.
- G19 now links all 19 issues as typed refs on main, and G16 now links 24 of 24.
- G11 linked its epics and objectives in §2 and merged develop into main. G20 merged its first feature PR, and G06 merged two code PRs.
- Most groups added Sprint 2 tasks without linking them from proposal §4 (G01, G02, G04), so their linked share fell. Link new work items as you create them.
- G03, G05, G14 and G15 had no changes since the last edition.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ✅](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ✅](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ✅](#g14) | [**G15** ✅](#g15) | [**G16** ✅](#g16) | [**G17** ✅](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 67 issues (47 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Cite epics #71-#74, #89, #90 and stories #113-#119 in proposal §2 and tasks #106, #109, #112, #120 in §4 (merge #121), and decide whether front-end work belongs in §2 goals.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #121, #111, #110, #107, #102, #101, #100, #99. Work in an open PR doesn't count yet.
2. *Link.* Cite 12 of 67 issues in `proposal.md` (epics and stories in §2, the rest in §4): #58, #106, #109, #112–#120.
3. *Plan.* Give #58 its own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign 14 of 47 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (14 of 45 PRs closed no issue).

*Since 2026-10-21:* Added Sprint 2 stories #113-#119 under epics #71-#74/#89/#90 with tasks re-parented, Slack epic closed, PRs #98-#121 opened (backtesting research, architecture, §3 to main); 12 of 67 issues are now unlinked from proposal.md (55 linked, 82%) and #121 to fix that is open.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

✅ **Aligned** · chain ⚠️ Gaps · 48 issues (25 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill proposal §4 with typed task links for the 30 issues not yet cited, and add a story for multi-node capture (nodes plus central collector).

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #78. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Multi-node distribution: no objective for running several capture nodes and merging their data (the project's title idea); the README mentions ESP32 firmware but no issue covers node hardware; Raspberry Pi / ESP32 node build is not tracked by any story.
4. *Link.* Cite 30 of 48 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15, #17, #18, #20–#25, #36–#41, #67–#70, #72, #73, #75, #77.
5. *Plan.* Add 1 open issue to the board: #77.
6. *Plan.* Give #6, #8–#13, #15, #36–#41, #70, #72, #75 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 22 of 25 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 22 PRs closed no issue).

*Since 2026-10-21:* Task #77 (data flow diagrams) and README cleanup PR #78 were added after PREV; linked share fell to 18 of 48 issues, §4 is still a skeleton and #77 is parented to stale Goal 0 task #23.

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

*Since 2026-10-21:* No material change: still 31 issues with 17 linked from develop's proposal.md, duplicate story #31/#32, no Sprint milestone on any story, revised section 2 not yet on main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polygon Prediction Market PNL and Trader Profitability Analytics

✅ **Aligned** · chain ⚠️ Gaps · 39 issues (30 open) · Sprint 1 milestone: 0 open, 9 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Give stories #26-#28, #30-#32, #35-#38 a Sprint milestone (they are Sprint 2-4 work) and cite tasks #49-#63 in proposal §4 so the 15 unlinked issues appear.

Everything still open, in the order to fix it:

1. *Link.* Cite 15 of 39 issues in `proposal.md` (epics and stories in §2, the rest in §4): #49–#63.
2. *Plan.* Add 9 open issues to the board: #55–#63.
3. *Plan.* Give #12, #13, #26–#28, #30–#32, #35–#38 their own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign all 30 open issues to one person each.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 16 PRs closed no issue).

*Since 2026-10-21:* Nine new Sprint 2 tasks #55-#63 (spec drafts, prototype v0 Snowflake wiring, project-context doc) were added, so linked share fell from 24 of 30 to 24 of 39 and 9 open issues are missing from the board; still no prototype code merged.

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

*Since 2026-10-21:* All 11 section 2 links are now typed and develop is synced with main; the board is otherwise unchanged and section 4 is still a skeleton.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · Forecast Market Analytics: GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking

✅ **Aligned** · chain ⚠️ Gaps · 24 issues (22 open) · Sprint 1 milestone: 6 open, 2 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Close or re-parent stale #3-#6 and duplicate #25, and rewrite develop's proposal §2 links as typed refs and cite #36 and the Sprint 2 tasks in §4 (still a skeleton).

Everything still open, in the order to fix it:

1. *Unblock.* 1 branch holds work that isn't in `develop`: `feature/question-generator`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 2 of 24 issues in `proposal.md` (epics and stories in §2, the rest in §4): #25, #36.
4. *Link.* Rewrite 22 bare `#N` references as typed links, e.g. `[[story:#31]](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/31)`.
5. *Plan.* Add 4 open issues to the board: #3–#6.
6. *Plan.* Give #5, #6 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Remove `sp:` from #36: they're under a user story, which carries the points.
8. *Plan.* Assign 17 of 22 open issues to one person each.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-21:* Code now lands: question-prompt builder and concept-extraction PRs #37 and #38 merged into develop and #36 was added (with sp: under story #17), while develop's links are still 0 typed, stale #3-#6 and #25 remain, and Sprint 1 still has 6 open past its 10-19 due date.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Materials Database

✅ **Aligned** · chain ⚠️ Gaps · 47 issues (39 open) · Sprint 1 milestone: 6 open, 7 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Merge #56 and the README branch (#57), retarget #60 to develop, and give Objectives #12-#27 a Sprint milestone.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #60, #56. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Link.* Cite 23 of 47 issues in `proposal.md` (epics and stories in §2, the rest in §4): #28, #29, #34, #36, #38–#41, #43–#49, #51–#55, #57–#59.
5. *Link.* Rewrite 24 bare `#N` references as typed links, e.g. `[[story:#42]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/42)`.
6. *Plan.* Give #12–#16, #18–#21, #23–#27 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 23 of 39 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 6 PRs closed no issue).

*Since 2026-10-21:* Spec tasks #58/#59 added and feature PR #60 (§4 environment) opened into main, but #56 is still unmerged, proposal.md still has 0 typed refs, README is still the course template, and Objectives #12-#27 still have no Sprint milestone.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

✅ **Aligned** · chain ✅ OK · 42 issues (30 open) · Sprint 1 milestone: 0 open, 7 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Fix §4 citations (stories belong in §2 only), type and link #60/#62 in proposal.md, and give #62/#60 sp: and a Sprint milestone.

Everything still open, in the order to fix it:

1. *Link.* Cite 8 of 42 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #7, #45–#47, #58, #60, #62.
2. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
3. *Plan.* Add 2 open issues to the board: #60, #62.
4. *Plan.* Give #45–#47, #49, #60, #62 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Remove `sp:` from #36: they're under a user story, which carries the points.
6. *Plan.* Assign 9 of 30 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 15 PRs closed no issue).

*Since 2026-10-21:* Sprint 1 closed out (0 open): proposal.md on develop now has 34 typed refs, 10 PRs merged with code (incident filtering #55, frequency analysis #61), data-format and README PRs merged, but §4 cites stories 19 times and #60/#62 are unlinked with no milestone.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

✅ **Aligned** · chain ✅ OK · 29 issues (16 open) · Sprint 1 milestone: 0 open, 13 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Write §3 and §4 of proposal.md (#16/#17, Sprint 2) and state which HW#4 extras (mileage tracking, parts finder, climate, receipt ingestion) are out of scope.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: HW#4 abstract features automatic mileage tracking, DIY maintenance help, parts finder, climate-based recommendations, and bulk ingestion of mixed-format paper records have no issues (board scopes to Goals 1-2; state in proposal.md that these are deferred).
3. *Link.* Cite 1 of 29 issues in `proposal.md` (epics and stories in §2, the rest in §4): #46.
4. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 12 PRs closed no issue).

*Since 2026-10-21:* Sprint 1 closed 13/13 and was released to main via #47 (README, typed-link PR #45, sprint review merged); board scope is unchanged at 2 epics and 10 objectives, with §3-§6 still to write in Sprint 2-3.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: Stablecoin Wash-Trading and Suspicious Transaction Detection

✅ **Aligned** · chain ⚠️ Gaps · 26 issues (14 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Put the board URL and roles in the README, retarget feature PRs to develop, and fix the proposal header (title, SNX-2 vs SNX-3, date) and #3's type.

Everything still open, in the order to fix it:

1. *Link.* Cite 2 of 26 issues in `proposal.md` (epics and stories in §2, the rest in §4): #5, #42.
2. *Link.* Fix the type on : the tag must match the issue's own type.
3. *Plan.* Assign all 14 open issues to one person each.
4. *Workflow.* Stop pushing straight to `main`/`develop` (28 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-21:* Objectives 1.4 and 2.4 added (#38, #39) and all 24 linked issues now use typed refs (25 typed, 0 misplaced) after PRs #43/#44, but 14 direct commits and merges into main persist and the proposal header still reads SNX-3 and a May date.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

✅ **Aligned** · chain ⚠️ Gaps · 23 issues (9 open) · Sprint 1 milestone: 0 open, 11 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Add concrete acceptance criteria to stories #28-#33 (still the generated placeholder), start a prototype PR for Objective 1.1, and link #37, #34, #20 and the other task issues in proposal.md section 4.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Spectator/group-event features raised in the first meeting notes (multi-runner events, login/security) have no issues and are not in the revised goals; No tasks or features yet under the objectives (all 6 stories are still generated placeholders in Sprint 2).
3. *Link.* Cite 13 of 23 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1–#3, #6–#9, #17, #20, #34, #37, #38, #40.
4. *Link.* Rewrite 1 bare `#N` reference as typed links, e.g. `[[story:#13]](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys/issues/13)`.
5. *Plan.* Give #1, #2, #6, #13, #34 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 2 of 9 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-21:* README now rewritten for Marathon Tracker and develop merged to main (PRs #39, #41); epics #26/#27 and Objectives 1.1-3.2 (#28-#33) are on the board in Sprint 2 and linked from section 2 (9 typed refs), but #13 is still bare and 13 of 23 issues remain unlinked.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

✅ **Aligned** · chain ⚠️ Gaps · 42 issues (22 open) · Sprint 1 milestone: 0 open, 41 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Replace the setup-guide README with the real project title, RTX-1 sponsor and summary, and convert the 31 bare issue links in proposal.md into typed refs.

Everything still open, in the order to fix it:

1. *Unblock.* 3 branches hold work that isn't in `develop`: `Application-Structure`, `docs/team-documentation`, `feature/65-confidence-calibration-unknown-label`. Open a pull request for each, or delete the branch.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Parameter estimation (baud rate, carrier frequency) has no explicit story; Interface control document and robustness across SNR/channel conditions (evaluation plan) have no issues.
4. *Link.* Cite 11 of 42 issues in `proposal.md` (epics and stories in §2, the rest in §4): #27–#32, #36, #95–#98.
5. *Link.* Rewrite 31 bare `#N` references as typed links, e.g. `[[story:#88]](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/88)`.
6. *Plan.* Add 1 open issue to the board: #96.
7. *Plan.* Give #63, #67, #68, #70, #71, #85, #95–#97 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Remove `sp:` from #88, #98: they're under a user story, which carries the points.
9. *Plan.* Assign 14 of 22 open issues to one person each.
10. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
11. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 29 PRs closed no issue).

*Since 2026-10-21:* Four new issues (#95-#98) added; PRs #92/#94 landed the glossary and feature #88 link, but all 31 links remain bare, #98 and #88 carry points under a story, 6 stories lack a Sprint, and README is still the template.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ⚠️ Gaps · 84 issues (68 open) · Sprint 1 milestone: 0 open, 12 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Start implementing the Sprint 2 objectives (#22-#24) with PRs that close the feature issues, and fix the README to say Windows desktop app.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #112. Work in an open PR doesn't count yet.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: No implementation started: 0 linked issues closed by a PR, all work items for Goals 1-3 still open; Platform inconsistency is not tracked (proposal says Windows desktop, README says mobile app).
3. *Link.* Cite 18 of 84 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15, #30–#35, #43, #44, #47, #107, #111, #113.
4. *Link.* Rewrite 66 bare `#N` references as typed links, e.g. `[[story:#106]](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/106)`.
5. *Plan.* Give #8, #10–#13, #15, #25–#27, #31–#34, #44, #47, #113 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 21 of 68 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 21 PRs closed no issue).

*Since 2026-10-21:* No new work items since 10-21 (still 84 issues, 66 linked and 0 typed); PR #112 for the spec/development plan remains open, and objectives #25-#27 still lack a Sprint.

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

*Since 2026-10-21:* From 3 process issues to 23 (epics #22/#23 and 18 measurable objective stories #24-#41); proposal.md section 2 now links all 20 epics/stories and the README names the same project, but no story has sp: or a Sprint milestone and links are untyped.

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

*Since 2026-10-21:* Stories #26-#33 filled in under epics #24/#25 (ECS, renderer, editor, game loop), the develop README now describes the project, and 11 of 22 issues are linked from proposal.md on develop, but links are bare, section 2 is still skeleton, main has none, and benchmarking remains untracked.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ✅ OK · 24 issues (17 open) · Sprint 1 milestone: 7 open, 8 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Close out Sprint 1 (past due 10-21 with 7 open issues: #16, #27, #28, #30, #34, #50, #56) by merging release PR #59 and moving unfinished items to Sprint 2.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #59. Work in an open PR doesn't count yet.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: None; every objective has a story, though Objectives 1.1, 1.2, 2.2 and 2.3 are not yet started.
3. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
4. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 28 PRs closed no issue).

*Since 2026-10-21:* Task #56 is now linked in proposal.md (24 of 24 issues typed-linked, up from 23 of 24); Sprint 1 due date passed with 7 open issues and release PR #59 is still open.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: SonicScape / EchoSphere

✅ **Aligned** (was Partial) · chain ❌ Broken · 15 issues (9 open) · Sprint 1 milestone: 6 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Update proposal.md §2 so epics point to #21/#22/#23 and stories to #25-#30 (it still cites #1-#6), add all six stories to the Sprint board, and decide whether the space-exploration UI is still in scope.

Everything still open, in the order to fix it:

1. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: HW#4 core idea of exploring genres/artists/songs as galaxies, star systems and planets with swipe feedback is absent from revised §2 and the board; NASA API parsing and AI/recommendation profile (Abstract and Introduction) have no epic or story.
2. *Link.* Cite all 15 issues in `proposal.md` (epics and stories in §2, the rest in §4): #15, #17–#30.
3. *Plan.* Add 6 open issues to the board: #25–#30.
4. *Plan.* Assign 3 of 9 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (6 of 6 PRs closed no issue).

*Since 2026-10-21:* Board rebuilt on 10-22: six stories #25-#30 under epics #21-#23 now match revised §2 (was only old epic #15), but proposal.md still links none of them, 6 stories are not all on the board, and no PR closes an issue.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (18 open) · Sprint 1 milestone: 14 open, 8 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Retire or re-parent the older epics #17/#19 and stories #18/#20 against the §2 tree, give #41, #18 and #20 correct sp:, and merge develop proposal.md (with §2 links) into main.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #44. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 14 of 27 issues in `proposal.md` (epics and stories in §2, the rest in §4): #2, #5–#9, #13, #15, #17–#20, #26, #28.
4. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
5. *Plan.* Add 2 open issues to the board: #13, #26.
6. *Plan.* Give #2, #6–#9, #13, #18, #20, #26, #41 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 7 of 18 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-21:* Combat-pipeline PR #45 merged (closes #37) and shared-movement PR #44 is open; 13 of 27 issues are still linked and main still holds the skeleton proposal.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over Wi-Fi

✅ **Aligned** · chain ⚠️ Gaps · 19 issues (18 open) · Sprint 1 milestone: 14 open, 7 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Start building: no story is closed or has code yet. Open a feature branch for Obj 1.1 (CSI capture) with a PR into develop that says Closes #8.

Everything still open, in the order to fix it:

1. *Link.* Fix the type on : the tag must match the issue's own type.
2. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
3. *Plan.* Assign 12 of 18 open issues to one person each.
4. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 10 PRs closed no issue).

*Since 2026-10-21:* Typed refs on main now cover all 19 issues (develop lags: 13 linked, 3 typed); README and proposal match; still only 1 of 19 issues closed and no PR touches a story.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia

✅ **Aligned** · chain ⚠️ Gaps · 16 issues (16 open) · Sprint 1 milestone: 5 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Put the eight stories in the Sprint 1 milestone, link them as typed refs in proposal.md §2, and merge develop into main.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 13 of 16 issues in `proposal.md` (epics and stories in §2, the rest in §4): #11, #13–#15, #18–#20, #22–#24, #26–#28.
3. *Link.* Rewrite 3 bare `#N` references as typed links, e.g. `[[story:#21]](https://github.com/muntay89/CPSC490-G20-Solos/issues/21)`.
4. *Plan.* Give #13–#15, #18–#20, #22, #23 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Assign 3 of 16 open issues to one person each.
6. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 4 PRs closed no issue).

*Since 2026-10-21:* First feature PR #32 (maze variations and atmosphere, closes #14/#22) merged into develop; otherwise still 3 of 16 issues linked as bare refs and stories lack a Sprint milestone.

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
| G01 | §2 15 links · §4 40 links · 55 issues cited · 67 typed | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 15 〈placeholders〉 | 18-abstract-intro (2 commits not in develop); 43-update-goals-and-objectives (2 commits not in develop); 58-cite-dropped-objective (1 commit not in develop); 58-cite-dropped-objective-main (34 commits not in develop); 66-sprint1-review (36 commits not in develop); 80-storage-choice (34 commits not in develop); 84-pipeline-dfd (34 commits not in develop); 88-backend-why-ours-differs (34 commits not in develop); 91-backtesting-research (36 commits not in develop); 106-section3-to-main (36 commits not in develop); 120-link-sprint2-stories (35 commits not in develop); Damon (1 commit not in develop); Sp2_Doc_Damon (23 commits not in develop); sync-main-into-develop (34 commits not in develop) |
| G02 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | feature/24-outcomes-timeline (1 commit not in develop); feature/73-remove-readme-old (1 commit not in develop) |
| G03 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 42 〈placeholders〉 | §2 17 links · §4 skeleton · 17 issues cited · 13 typed · 41 〈placeholders〉 | Elizabeth-7-7-patch-1 (1 commit not in develop); Sehaj36-patch-1 (1 commit not in develop); eccortes4-proposal-epic-issues (1 commit not in develop) |
| G04 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | none |
| G05 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | feature/15-direction-estimate (4 commits not in develop) |
| G06 | §2 17 links · §4 skeleton · 17 issues cited · 17 typed · 47 〈placeholders〉 | §2 17 links · §4 skeleton · 22 issues cited · 0 typed · 82 〈placeholders〉 | feature/question-generator (2 commits not in develop) |
| G07 | §2 24 links · §4 skeleton · 24 issues cited · 0 typed · 40 〈placeholders〉 | §2 24 links · §4 skeleton · 24 issues cited · 0 typed · 40 〈placeholders〉 | 51-typed-proposal-issue-links (1 commit not in develop); 55-sprint-1-review (1 commit not in develop); 57-project-readme (1 commit not in develop); feature/-53-environment-resources-activities (3 commits not in develop) |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 11 links · §4 31 links · 34 issues cited · 61 typed (19 misplaced) · 21 〈placeholders〉 | none |
| G09 | §2 12 links · §4 skeleton · 28 issues cited · 30 typed (2 misplaced) · 25 〈placeholders〉 | §2 12 links · §4 skeleton · 28 issues cited · 30 typed (2 misplaced) · 25 〈placeholders〉 | none |
| G10 | §2 14 links · §4 11 links · 24 issues cited · 25 typed · 6 〈placeholders〉 | §2 14 links · §4 11 links · 24 issues cited · 25 typed · 6 〈placeholders〉 | none |
| G11 | §2 9 links · §4 skeleton · 10 issues cited · 9 typed · 42 〈placeholders〉 | §2 9 links · §4 skeleton · 10 issues cited · 9 typed · 58 〈placeholders〉 | none |
| G12 | §2 17 links · §4 14 links · 31 issues cited · 0 typed | §2 17 links · §4 14 links · 31 issues cited · 0 typed | Application-Structure (5 commits not in develop); docs/team-documentation (3 commits not in develop); feature/65-confidence-calibration-unknown-label (1 commit not in develop) |
| G13 | §2 12 links · §4 48 links · 52 issues cited · 0 typed | §2 12 links · §4 54 links · 66 issues cited · 0 typed | documentation/111-spec-and-development-plan (4 commits not in develop); feature/34-project-proposal (28 commits not in develop); sprint1-patch-1 (1 commit not in develop); updated-proposal (6 commits not in develop) |
| G14 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | none |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 11 issues cited · 0 typed · 35 〈placeholders〉 | none |
| G16 | §2 12 links · §4 10 links · 22 issues cited · 22 typed | §2 12 links · §4 12 links · 24 issues cited · 25 typed | release/0.1 (4 commits not in develop) |
| G17 | §2 6 links · §4 skeleton · 0 issues cited · 0 typed · 41 〈placeholders〉 | §2 4 links · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 13 links · §4 skeleton · 13 issues cited · 18 typed (5 misplaced) · 40 〈placeholders〉 | feature/36-shared-movement (1 commit not in develop) |
| G19 | §2 11 links · §4 skeleton · 19 issues cited · 19 typed · 26 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 3 typed · 26 〈placeholders〉 | none |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 61 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 15 links / 40 links | 55 of 67 | 55 of 55 | 17 / 22 of 55 | 14 of 45 | 3 / 3 | ⚠️ Gaps |
| G02 | 18 links / skeleton | 18 of 48 | 18 of 18 | 0 / 0 of 18 | 4 of 22 | 1 / 1 | ⚠️ Gaps |
| G03 | 17 links / skeleton | 17 of 31 | 12 of 17; 1 bad link | 0 / 0 of 17 | 4 of 15 | 1 / 1 | ⚠️ Gaps |
| G04 | 15 links / 9 links | 24 of 39 | 24 of 24 | 9 / 6 of 24 | 1 of 16 | 0 / 0 | ⚠️ Gaps |
| G05 | 11 links / skeleton | 11 of 20 | 11 of 11 | 0 / 0 of 11 | 0 of 9 | 0 / 0 | ⚠️ Gaps |
| G06 | 17 links / skeleton | 22 of 24 | 0 of 22 | 2 / 3 of 22 | 0 of 7 | 0 / 0 | ⚠️ Gaps |
| G07 | 24 links / skeleton | 24 of 47 | 0 of 24 | 5 / 0 of 24 | 2 of 6 | 2 / 2 | ⚠️ Gaps |
| G08 | 11 links / 31 links | 34 of 42 | 34 of 34; 19 in the wrong section | 6 / 10 of 34 | 3 of 15 | 0 / 0 | ✅ OK |
| G09 | 12 links / skeleton | 28 of 29 | 28 of 28; 2 in the wrong section | 12 / 10 of 28 | 1 of 12 | 0 / 0 | ✅ OK |
| G10 | 14 links / 11 links | 24 of 26 | 25 of 24; 1 wrong type | 10 / 6 of 24 | 0 of 12 | 14 / 14 | ⚠️ Gaps |
| G11 | 9 links / skeleton | 10 of 23 | 9 of 10 | 1 / 1 of 10 | 0 of 12 | 1 / 1 | ⚠️ Gaps |
| G12 | 17 links / 14 links | 31 of 42 | 0 of 31 | 13 / 10 of 31 | 3 of 29 | 1 / 1 | ⚠️ Gaps |
| G13 | 12 links / 54 links | 66 of 84 | 0 of 66 | 0 / 0 of 66 | 5 of 21 | 0 / 0 | ⚠️ Gaps |
| G14 | 20 links / skeleton | 20 of 23 | 0 of 20 | 0 / 0 of 20 | 2 of 9 | 1 / 1 | ⚠️ Gaps |
| G15 | skeleton / skeleton | 11 of 22 | 0 of 11 | 0 / 0 of 11 | 4 of 14 | 4 / 4 | ⚠️ Gaps |
| G16 | 12 links / 12 links | 24 of 24 | 24 of 24 | 7 / 13 of 24 | 5 of 28 | 3 / 3 | ✅ OK |
| G17 | 6 links / skeleton | 0 of 15 | 0 of 0 | 0 / 0 of 0 | 6 of 6 | 2 / 2 | ❌ Broken |
| G18 | 13 links / skeleton | 13 of 27 | 13 of 13; 5 in the wrong section | 1 / 2 of 13 | 0 of 11 | 1 / 1 | ⚠️ Gaps |
| G19 | 11 links / skeleton | 19 of 19 | 19 of 19; 1 wrong type | 1 / 7 of 19 | 2 of 10 | 36 / 28 | ⚠️ Gaps |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 4 | 1 / 1 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [BGAF Sprint Board](https://github.com/users/LeDuy23/projects/3) | 47 of 47 | ✅ | 1 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 24 of 25 | ✅ | 17 | none | none |
| G03 | ✅ [CPSC-490-G03-California](https://github.com/users/eccortes4/projects/1) | 16 of 21 | ✅ | 18 | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 21 of 30 | ✅ | 12 | none | none |
| G05 | ✅ [WILS](https://github.com/users/M-Kwatcher/projects/2) | 11 of 11 | ✅ | 1 | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 18 of 22 | ✅ | 2 | 1 | none |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 39 of 39 | ✅ | 14 | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 28 of 30 | ✅ | 6 | 1 | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 16 of 16 | ✅ | none | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 14 of 14 | ✅ | none | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/markachavez2003-lab/projects/1) | 9 of 9 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 21 of 22 | ✅ | 9 | 2 | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 68 of 68 | ✅ | 16 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 20 of 21 | ✅ | 19 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 11 of 11 | ✅ | 11 | none | none |
| G16 | ✅ [Sprint Board](https://github.com/users/garybs16/projects/2) | 17 of 17 | ✅ | none | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 3 of 9 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 16 of 18 | ✅ | 10 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 18 of 18 | ✅ | 1 | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 67 issues (10 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 48 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G03 California | Three AIs and Literate Programming | 31 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 39 issues (9 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G05 Fighting Mongooses | WILS: Whale Identification/Location System | 20 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 24 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G07 Mighty Morphin | Online Materials Database | 47 issues (2 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 42 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 29 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | Stablecoin Wash-Trading and Suspicious Transaction Detection | 26 issues (3 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G11 5 Guys | Marathon Tracker | 23 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G12 ACJMM | Explainable 6G Waveform Classification | 42 issues (4 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 84 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 23 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G15 HIBBI-01 | Low End Hardware/ECS Architecture Game Engine with Game | 22 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 24 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | SonicScape / EchoSphere | 15 issues (14 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G18 Team ProStrats | Project Rogue | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G19 Titan Security | Radar over Wi-Fi | 19 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia | 16 issues; epics, stories, points | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
