# Group repository status: proposal vs. issue board

> [!IMPORTANT]
> **New (Oct 11): one card per group, ahead of the Sprint 1 reviews.**
> Scroll to **Your group**. Your card combines everything this page checks into one numbered list, in the order to fix it: *Unblock → Document → Board / Scope → Link → Plan → Workflow*. Work through it before your Sprint 1 review: **G01–G05 Tue Oct 13 · G11–G15 Thu Oct 15 · G06–G10 Tue Oct 20 · G16–G20 Thu Oct 22**, and bring the card to the meeting.
>
> The section **Why teams are stuck** explains the patterns behind most cards. Most teams are one merged pull request away from a much better card: §2 of your proposal, merged into `develop`.

**CPSC 490 · Fall 2026 · swept 2026-10-24 19:36 UTC.** The previous edition (2026-10-22) is kept in git history.

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

**2. Finished work is sitting in branches and open pull requests** (10 groups: G01, G02, G03, G05, G06, G12, G13, G16, G19, G20). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**4. The board is a list, not a plan yet.** In 10 groups (G02, G03, G04, G06, G07, G10, G12, G14, G15, G20) at least half the open issues have no assignee, and 17 groups (G01, G02, G03, G04, G05, G06, G07, G08, G11, G12, G13, G14, G15, G16, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 8 groups: G01, G07, G10, G15, G16, G17, G19, G20). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (20 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

## Class at a glance

- ✅ **Aligned:** 20 (G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20)
- ⚠️ **Partial:** 0 (none)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 0 (none)
- ❌ **Mismatch** (board or README about a different project): 0 (none)
- ❌ **No issues yet:** 0 (none)
- Team-filed issues: **707** across 20 groups (39 new since 2026-10-22).

### What changed since 2026-10-22

- G17's revised §2 and its board now agree: proposal.md on main cites epics #21–#23 and stories #25–#30. The chain is still broken, because no PR closes an issue and most PRs merged straight into main.
- G16 closed out Sprint 1 (0 open, was 7) and merged its release PR into main. The chain stays complete (CHAIN_OK).
- G18 merged its movement and combat PRs and its Sprint 1 review. G19 merged its first work toward Objective 1.1 (setup notes and capture procedure).
- G20 filled its §4 work chart with 14 new task issues. They still need a Sprint milestone or a parent story, and main still holds the skeleton proposal.
- G01 now links 66 of 68 issues, all typed. G07's main now links 47 of 49 issues, though 24 links are still bare.
- G02 and G13 added issues without linking them from proposal §4, so their linked share fell or stayed flat. Link new work items as you create them.
- G04–G06, G08–G12, G14 and G15 had no changes since the last edition.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ✅](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ✅](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ✅](#g14) | [**G15** ✅](#g15) | [**G16** ✅](#g16) | [**G17** ✅](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 68 issues (32 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge or close #123 and open all new work as feature-branch PRs into develop with Closes #N; start the Sprint 2 code stories (#23, #24, #68, #69) so the prototype issues get PRs; replace the README placeholders.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #123. Work in an open PR doesn't count yet.
2. *Link.* Cite 2 of 68 issues in `proposal.md` (epics and stories in §2, the rest in §4): #58, #112.
3. *Plan.* Give #58 its own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign 11 of 32 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (16 of 49 PRs closed no issue).

*Since 2026-10-22:* Sprint 2 stories and tasks are now linked from proposal.md on main (66 of 68 issues, up from 55 of 67; #121 merged) and the Sprint 2 spec and research tasks closed, but PRs still go straight to main and open #123 and merged #126 have no Closes line.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

✅ **Aligned** · chain ⚠️ Gaps · 52 issues (28 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Fill proposal §4 with typed task/sub-task links for the 34 unlinked issues, open the first prototype PRs into develop closing #16/#17/#18, and add a story for the multi-node collector.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #83, #78. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Multi-node coordination (several nodes feeding one central collector) has no story of its own; Objective 1.4 covers storage only.
4. *Link.* Cite 34 of 52 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15, #17, #18, #20–#25, #36–#41, #67–#70, #72, #73, #75, #77, #79–#82.
5. *Plan.* Give #6, #8–#13, #15, #36–#41, #75, #82 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 21 of 28 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 23 PRs closed no issue).

*Since 2026-10-22:* Sprint 2 work was added (#80 meeting, #81/#82 proposal tasks, #83 ESP32 PR into main) without links, so linked share fell to 18 of 52 issues; no prototype code PR yet.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

✅ **Aligned** · chain ⚠️ Gaps · 32 issues (22 open) · Sprint 1 milestone: 0 open, 6 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge develop into main so proposal.md carries the revised §2, fix the story parents (#35 and #37 under the wrong goal, close duplicate #31/#32), add stories for equation-to-code generation and model training under Goal 3, and give stories a Sprint milestone.

Everything still open, in the order to fix it:

1. *Unblock.* 3 branches hold work that isn't in `develop`: `Elizabeth-7-7-patch-1`, `Sehaj36-patch-1`, `eccortes4-proposal-epic-issues`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Equation-to-code generation (the proposal's second AI) has no story; Objective 1.2 only converts between representations; Goal 3 has no Objective 3.1 (model training itself) and no child stories under #43.
4. *Link.* Cite 15 of 32 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #2, #4, #5, #13, #15–#17, #20, #24, #39, #41, #42, #51, #53.
5. *Link.* Rewrite 5 bare `#N` references as typed links, e.g. `[[story:#44]](https://github.com/eccortes4/CPSC490-G03-California/issues/44)`.
6. *Plan.* Add 6 open issues to the board: #1, #20, #24, #27, #42, #53.
7. *Plan.* Give #1, #2, #20, #24, #31, #32, #34–#37, #39, #41, #42, #45–#48, #50, #53 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 13 of 22 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 15 PRs closed no issue).

*Since 2026-10-22:* Goal 1 was split into transcriber/verifier objectives (#50, PR #52 merged into develop) and #51 closed; main still lacks the revised §2, 17 of 32 issues linked, stories mostly without a Sprint.

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

*Since 2026-10-22:* Nine new Sprint 2 tasks #55-#63 (spec drafts, prototype v0 Snowflake wiring, project-context doc) were added, so linked share fell from 24 of 30 to 24 of 39 and 9 open issues are missing from the board; still no prototype code merged.

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

*Since 2026-10-22:* All 11 section 2 links are now typed and develop is synced with main; the board is otherwise unchanged and section 4 is still a skeleton.

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

*Since 2026-10-22:* Code now lands: question-prompt builder and concept-extraction PRs #37 and #38 merged into develop and #36 was added (with sp: under story #17), while develop's links are still 0 typed, stale #3-#6 and #25 remain, and Sprint 1 still has 6 open past its 10-19 due date.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Materials Database

✅ **Aligned** · chain ⚠️ Gaps · 49 issues (37 open) · Sprint 1 milestone: 3 open, 11 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Convert the 24 bare links in proposal.md (#5-#54 work items) to typed refs, give Objectives #12-#27 a Sprint milestone, and put #57 (README) and #51 through to closed.

Everything still open, in the order to fix it:

1. *Link.* Cite 2 of 49 issues in `proposal.md` (epics and stories in §2, the rest in §4): #28, #67.
2. *Link.* Rewrite 24 bare `#N` references as typed links, e.g. `[[story:#63]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/63)`.
3. *Plan.* Give #12–#16, #18–#21, #23–#27, #63 their own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign 24 of 37 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 11 PRs closed no issue).

*Since 2026-10-22:* Proposal.md on main now links 47 of 49 issues (was 24 bare links on develop) after PRs #62-#66 merged to main, but only 23 are typed, stories still lack a Sprint, and #67 for the typed-link fix is open.

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

*Since 2026-10-22:* Sprint 1 closed out (0 open): proposal.md on develop now has 34 typed refs, 10 PRs merged with code (incident filtering #55, frequency analysis #61), data-format and README PRs merged, but §4 cites stories 19 times and #60/#62 are unlinked with no milestone.

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

*Since 2026-10-22:* Sprint 1 closed 13/13 and was released to main via #47 (README, typed-link PR #45, sprint review merged); board scope is unchanged at 2 epics and 10 objectives, with §3-§6 still to write in Sprint 2-3.

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

*Since 2026-10-22:* Objectives 1.4 and 2.4 added (#38, #39) and all 24 linked issues now use typed refs (25 typed, 0 misplaced) after PRs #43/#44, but 14 direct commits and merges into main persist and the proposal header still reads SNX-3 and a May date.

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

*Since 2026-10-22:* README now rewritten for Marathon Tracker and develop merged to main (PRs #39, #41); epics #26/#27 and Objectives 1.1-3.2 (#28-#33) are on the board in Sprint 2 and linked from section 2 (9 typed refs), but #13 is still bare and 13 of 23 issues remain unlinked.

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

*Since 2026-10-22:* Four new issues (#95-#98) added; PRs #92/#94 landed the glossary and feature #88 link, but all 31 links remain bare, #98 and #88 carry points under a story, 6 stories lack a Sprint, and README is still the template.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ⚠️ Gaps · 84 issues (68 open) · Sprint 1 milestone: 0 open, 12 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Fix the README to say Windows desktop app, start the Sprint 2 implementation (#22-#24) with feature PRs into develop that close the feature issues, and give #25-#27 a Sprint.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #112. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Link.* Cite 18 of 84 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15, #30–#35, #43, #44, #47, #107, #111, #113.
4. *Link.* Rewrite 66 bare `#N` references as typed links, e.g. `[[story:#106]](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/106)`.
5. *Plan.* Give #8, #10–#13, #15, #25–#27, #31–#34, #44, #47, #113 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 3 of 68 open issues to one person each.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 21 PRs closed no issue).

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

*Since 2026-10-22:* From 3 process issues to 23 (epics #22/#23 and 18 measurable objective stories #24-#41); proposal.md section 2 now links all 20 epics/stories and the README names the same project, but no story has sp: or a Sprint milestone and links are untyped.

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

*Since 2026-10-22:* Stories #26-#33 filled in under epics #24/#25 (ECS, renderer, editor, game loop), the develop README now describes the project, and 11 of 22 issues are linked from proposal.md on develop, but links are bare, section 2 is still skeleton, main has none, and benchmarking remains untracked.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ✅ OK · 32 issues (20 open) · Sprint 1 milestone: 0 open, 13 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Sprint 2 (due Nov 4) holds 11 open issues: move on the 'collect from SonarX stream' and 'normal range' stories (#14, #15) with feature PRs into develop that say Closes #N, link task #69 from proposal §4, and release develop to main before the boundary.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #70. Work in an open PR doesn't count yet.
2. *Link.* Cite 2 of 32 issues in `proposal.md` (epics and stories in §2, the rest in §4): #67, #69.
3. *Plan.* Give #67 its own `sp:` label and a `Sprint N` milestone.
4. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 31 PRs closed no issue).

*Since 2026-10-22:* Sprint 1 closed out (0 open, 13 closed; was 7 open) with release PR #59 merged to main, Goal 2 and Goal 3 specs started, Sprint 2 task issues #61-#66 and #69 added and 30 of 32 issues now linked; objectives 1.1, 1.2, 2.2, 2.3 still unbuilt.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: EchoSphere (team SonicScape): galaxy-style music discovery app

✅ **Aligned** · chain ❌ Broken · 15 issues (9 open) · Sprint 1 milestone: 6 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Sprint 1 is past due with all six stories open and no code: either start the map prototype (#25) on a feature branch with a PR into develop that says Closes #25, or re-plan the stories into Sprint 2+; also file task issues for the proposal edits and fill §4 with typed links.

Everything still open, in the order to fix it:

1. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Music playback / catalog source: §1.1 table says SonicScape 'plays music as users explore', but no §2 objective or issue covers playback or where songs come from; NASA data parsing and a separate AI profile model still appear in the §1 introduction but not in revised §2 or on the board (acceptable under the revision, but §1 should be updated to match).
2. *Link.* Cite 6 of 15 issues in `proposal.md` (epics and stories in §2, the rest in §4): #15, #17–#20, #24.
3. *Plan.* Assign 3 of 9 open issues to one person each.
4. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
5. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (13 of 13 PRs closed no issue).

*Since 2026-10-22:* Revised §1.1/§1.2/§2 are now in proposal.md on main and the board matches them: epics #21-#23 and stories #25-#30 are cited in §2 (9 typed links, was still citing #1-#6), all 9 open issues are on the board, old epics closed; still 0 of 6 stories started, no PR closes an issue, and develop lags main.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue (team ProStrats): 2D action roguelite platformer

✅ **Aligned** · chain ⚠️ Gaps · 29 issues (14 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Merge develop's proposal.md into main (main §2 and §4 are still the skeleton), cite the 16 unlinked issues (#47, #48, #28, #18, #15 and others) as typed [task:#N] in §4, and give each story a measurable objective title with a deliverable.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 16 of 29 issues in `proposal.md` (epics and stories in §2, the rest in §4): #2, #5–#9, #13, #15, #17–#20, #26, #28, #47, #48.
3. *Link.* Move  to the right section (epics and stories in §2 only, everything else in §4).
4. *Plan.* Add 2 open issues to the board: #13, #26.
5. *Plan.* Give #13, #26 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 2 of 14 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-22:* Shared-movement PR #44 and combat PR #45 merged (stories #36 and #37 closed), Sprint 1 review PR #46 merged (Sprint 1 now 14 closed, 0 open), new playtest task #48 added; 13 of 29 issues linked, §1 still cites epics and main still holds the skeleton proposal.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi: Wi-Fi CSI Drone Detection

✅ **Aligned** · chain ⚠️ Gaps · 22 issues (18 open) · Sprint 1 milestone: 7 open, 10 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Sprint 1 is past due with 7 open writing/README tasks: close the ones already merged (#26-#28), remove sp: from #39 (it sits under story #8), add sp: to #37/#38 or close them, merge main and develop together so proposal.md matches, and fill in the README summary; then start Obj 1.1 (#8) with a PR that says Closes #8.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #42. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 3 of 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #37–#39.
4. *Plan.* Give #37, #38 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Remove `sp:` from #39: they're under a user story, which carries the points.
6. *Plan.* Assign 2 of 18 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-22:* First work toward Obj 1.1: PRs #40 and #41 merged (CSI equipment setup notes, capture procedure) closing new task #39; 22 issues now (3 new: #37-#39), Sprint 1 at 10 closed/7 open, develop lags main on typed links (3 vs 19), proposal and README still match.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia (team Solos): first-person horror maze game

✅ **Aligned** · chain ⚠️ Gaps · 34 issues (27 open) · Sprint 1 milestone: 10 open, 6 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Retag #12, #17, #21 as [epic:#N] (they are cited as [story:]) and the 14 bare task refs as [task:#N], give tasks #39-#52 a Sprint milestone and a parent story, merge develop into main, and start the first story with a PR that says Closes #N.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #53. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 9 of 34 issues in `proposal.md` (epics and stories in §2, the rest in §4): #11, #24, #26–#28, #33–#35, #37.
4. *Link.* Rewrite 14 bare `#N` references as typed links, e.g. `[[story:#52]](https://github.com/muntay89/CPSC490-G20-Solos/issues/52)`.
5. *Link.* Fix the type on : the tag must match the issue's own type.
6. *Plan.* Give #33, #39–#52 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 14 of 27 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (3 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 7 PRs closed no issue).

*Since 2026-10-22:* §4 work-task chart filled with 14 new task issues (#39-#52), 34 issues now (was 16) with 25 linked, develop §2 cites 3 epics and 8 stories (tagged [story:] throughout), Sprint 1 at 6 closed/10 open; main is still the skeleton and PR #53 into main is open.

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
| G01 | §2 22 links · §4 44 links · 66 issues cited · 89 typed | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 15 〈placeholders〉 | 18-abstract-intro (2 commits not in develop); 43-update-goals-and-objectives (2 commits not in develop); 58-cite-dropped-objective (1 commit not in develop); 58-cite-dropped-objective-main (34 commits not in develop); Damon (1 commit not in develop); sync-main-into-develop (34 commits not in develop) |
| G02 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | feature/23-approach-environment (1 commit not in develop); feature/24-outcomes-timeline (1 commit not in develop); feature/73-remove-readme-old (1 commit not in develop); feature/81-esp32-hardware (1 commit not in develop) |
| G03 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 42 〈placeholders〉 | §2 17 links · §4 skeleton · 17 issues cited · 13 typed · 41 〈placeholders〉 | Elizabeth-7-7-patch-1 (1 commit not in develop); Sehaj36-patch-1 (1 commit not in develop); eccortes4-proposal-epic-issues (1 commit not in develop) |
| G04 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | none |
| G05 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | feature/15-direction-estimate (4 commits not in develop) |
| G06 | §2 17 links · §4 skeleton · 17 issues cited · 17 typed · 47 〈placeholders〉 | §2 17 links · §4 skeleton · 22 issues cited · 0 typed · 82 〈placeholders〉 | feature/question-generator (2 commits not in develop) |
| G07 | §2 23 links · §4 30 links · 47 issues cited · 23 typed · 15 〈placeholders〉 | §2 24 links · §4 skeleton · 24 issues cited · 16 typed · 40 〈placeholders〉 | none |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 11 links · §4 31 links · 34 issues cited · 61 typed (19 misplaced) · 21 〈placeholders〉 | none |
| G09 | §2 12 links · §4 skeleton · 28 issues cited · 30 typed (2 misplaced) · 25 〈placeholders〉 | §2 12 links · §4 skeleton · 28 issues cited · 30 typed (2 misplaced) · 25 〈placeholders〉 | none |
| G10 | §2 14 links · §4 11 links · 24 issues cited · 25 typed · 6 〈placeholders〉 | §2 14 links · §4 11 links · 24 issues cited · 25 typed · 6 〈placeholders〉 | none |
| G11 | §2 9 links · §4 skeleton · 10 issues cited · 9 typed · 42 〈placeholders〉 | §2 9 links · §4 skeleton · 10 issues cited · 9 typed · 58 〈placeholders〉 | none |
| G12 | §2 17 links · §4 14 links · 31 issues cited · 0 typed | §2 17 links · §4 14 links · 31 issues cited · 0 typed | Application-Structure (5 commits not in develop); docs/team-documentation (3 commits not in develop); feature/65-confidence-calibration-unknown-label (1 commit not in develop) |
| G13 | §2 12 links · §4 48 links · 52 issues cited · 0 typed | §2 12 links · §4 54 links · 66 issues cited · 0 typed | documentation/111-spec-and-development-plan (4 commits not in develop); feature/34-project-proposal (28 commits not in develop); sprint1-patch-1 (1 commit not in develop); updated-proposal (6 commits not in develop) |
| G14 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | §2 20 links · §4 skeleton · 20 issues cited · 0 typed · 39 〈placeholders〉 | none |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 11 issues cited · 0 typed · 35 〈placeholders〉 | none |
| G16 | §2 12 links · §4 12 links · 24 issues cited · 25 typed | §2 12 links · §4 18 links · 30 issues cited · 31 typed | 15-baseline-check (1 commit not in develop); 69-ingest-lag-minutes (1 commit not in develop) |
| G17 | §2 9 links · §4 skeleton · 9 issues cited · 9 typed · 41 〈placeholders〉 | §2 4 links · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 13 links · §4 skeleton · 13 issues cited · 18 typed (5 misplaced) · 40 〈placeholders〉 | none |
| G19 | §2 11 links · §4 skeleton · 19 issues cited · 19 typed · 26 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 3 typed · 26 〈placeholders〉 | feature/update-readme-team (1 commit not in develop) |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | §2 11 links · §4 skeleton · 25 issues cited · 11 typed · 75 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 22 links / 44 links | 66 of 68 | 66 of 66 | 34 / 25 of 66 | 16 of 49 | 3 / 3 | ⚠️ Gaps |
| G02 | 18 links / skeleton | 18 of 52 | 18 of 18 | 0 / 0 of 18 | 4 of 23 | 1 / 1 | ⚠️ Gaps |
| G03 | 17 links / skeleton | 17 of 32 | 12 of 17; 1 bad link | 0 / 0 of 17 | 4 of 15 | 1 / 1 | ⚠️ Gaps |
| G04 | 15 links / 9 links | 24 of 39 | 24 of 24 | 9 / 6 of 24 | 1 of 16 | 0 / 0 | ⚠️ Gaps |
| G05 | 11 links / skeleton | 11 of 20 | 11 of 11 | 0 / 0 of 11 | 0 of 9 | 0 / 0 | ⚠️ Gaps |
| G06 | 17 links / skeleton | 22 of 24 | 0 of 22 | 2 / 3 of 22 | 0 of 7 | 0 / 0 | ⚠️ Gaps |
| G07 | 23 links / 30 links | 47 of 49 | 23 of 47 | 11 / 9 of 47 | 2 of 11 | 2 / 2 | ⚠️ Gaps |
| G08 | 11 links / 31 links | 34 of 42 | 34 of 34; 19 in the wrong section | 6 / 10 of 34 | 3 of 15 | 0 / 0 | ✅ OK |
| G09 | 12 links / skeleton | 28 of 29 | 28 of 28; 2 in the wrong section | 12 / 10 of 28 | 1 of 12 | 0 / 0 | ✅ OK |
| G10 | 14 links / 11 links | 24 of 26 | 25 of 24; 1 wrong type | 10 / 6 of 24 | 0 of 12 | 14 / 14 | ⚠️ Gaps |
| G11 | 9 links / skeleton | 10 of 23 | 9 of 10 | 1 / 1 of 10 | 0 of 12 | 1 / 1 | ⚠️ Gaps |
| G12 | 17 links / 14 links | 31 of 42 | 0 of 31 | 13 / 10 of 31 | 3 of 29 | 1 / 1 | ⚠️ Gaps |
| G13 | 12 links / 54 links | 66 of 84 | 0 of 66 | 0 / 0 of 66 | 5 of 21 | 0 / 0 | ⚠️ Gaps |
| G14 | 20 links / skeleton | 20 of 23 | 0 of 20 | 0 / 0 of 20 | 2 of 9 | 1 / 1 | ⚠️ Gaps |
| G15 | skeleton / skeleton | 11 of 22 | 0 of 11 | 0 / 0 of 11 | 4 of 14 | 4 / 4 | ⚠️ Gaps |
| G16 | 12 links / 18 links | 30 of 32 | 30 of 30 | 12 / 15 of 30 | 5 of 31 | 3 / 3 | ✅ OK |
| G17 | 9 links / skeleton | 9 of 15 | 9 of 9 | 0 / 0 of 9 | 13 of 13 | 2 / 2 | ❌ Broken |
| G18 | 13 links / skeleton | 13 of 29 | 13 of 13; 5 in the wrong section | 2 / 2 of 13 | 0 of 12 | 1 / 1 | ⚠️ Gaps |
| G19 | 11 links / skeleton | 19 of 22 | 19 of 19 | 3 / 8 of 19 | 0 of 14 | 36 / 28 | ⚠️ Gaps |
| G20 | 11 links / skeleton | 25 of 34 | 11 of 25; 3 wrong type | 0 / 2 of 25 | 2 of 7 | 1 / 2 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [BGAF Sprint Board](https://github.com/users/LeDuy23/projects/3) | 32 of 32 | ✅ | 1 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 28 of 28 | ✅ | 16 | none | none |
| G03 | ✅ [CPSC-490-G03-California](https://github.com/users/eccortes4/projects/1) | 16 of 22 | ✅ | 19 | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 21 of 30 | ✅ | 12 | none | none |
| G05 | ✅ [WILS](https://github.com/users/M-Kwatcher/projects/2) | 11 of 11 | ✅ | 1 | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 18 of 22 | ✅ | 2 | 1 | none |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 37 of 37 | ✅ | 15 | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 28 of 30 | ✅ | 6 | 1 | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 16 of 16 | ✅ | none | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 14 of 14 | ✅ | none | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/markachavez2003-lab/projects/1) | 9 of 9 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 21 of 22 | ✅ | 9 | 2 | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 68 of 68 | ✅ | 16 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 20 of 21 | ✅ | 19 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 11 of 11 | ✅ | 11 | none | none |
| G16 | ✅ [Sprint Board](https://github.com/users/garybs16/projects/2) | 20 of 20 | ✅ | 1 | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 9 of 9 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 12 of 14 | ✅ | 2 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 18 of 18 | ✅ | 2 | 1 | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 27 of 27 | ✅ | 15 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 68 issues (1 new); epics, stories, points, Sprint 1 | n/a | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 52 issues (4 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G03 California | Three AIs and Literate Programming | 32 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 39 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G05 Fighting Mongooses | WILS: Whale Identification/Location System | 20 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 24 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G07 Mighty Morphin | Online Materials Database | 49 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 42 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 29 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | Stablecoin Wash-Trading and Suspicious Transaction Detection | 26 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G11 5 Guys | Marathon Tracker | 23 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G12 ACJMM | Explainable 6G Waveform Classification | 42 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 84 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 23 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G15 HIBBI-01 | Low End Hardware/ECS Architecture Game Engine with Game | 22 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 32 issues (8 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | EchoSphere (team SonicScape): galaxy-style music discovery app | 15 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G18 Team ProStrats | Project Rogue (team ProStrats): 2D action roguelite platformer | 29 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G19 Titan Security | Radar over WiFi: Wi-Fi CSI Drone Detection | 22 issues (3 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia (team Solos): first-person horror maze game | 34 issues (18 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
