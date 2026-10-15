# Group repository status: proposal vs. issue board

> [!IMPORTANT]
> **New (Oct 11): one card per group, ahead of the Sprint 1 reviews.**
> Scroll to **Your group**. Your card combines everything this page checks into one numbered list, in the order to fix it: *Unblock → Document → Board / Scope → Link → Plan → Workflow*. Work through it before your Sprint 1 review: **G01–G05 Tue Oct 13 · G11–G15 Thu Oct 15 · G06–G10 Tue Oct 20 · G16–G20 Thu Oct 22**, and bring the card to the meeting.
>
> The section **Why teams are stuck** explains the patterns behind most cards. Most teams are one merged pull request away from a much better card: §2 of your proposal, merged into `develop`.

> [!CAUTION]
> **HW#5 check (Oct 12): 10 groups' epics and user stories do not match the Goals and Objectives they submitted in HW#5 (§2).**
> 🔴 **Not reflected / wrong numbers:** [**G06**](https://github.com/Joshbolus/CPSC490-G06-GapWise/issues/15) · [**G12**](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/82) · [**G14**](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/21) · [**G15**](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/23) · [**G17**](https://github.com/vibhorbh/CPSC490-G17-SonicScape/issues/13)
> 🟠 **Extra, duplicate or misnumbered items:** [**G07**](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/33) · [**G08**](https://github.com/miketruong91/CPSC490-G08-Crime-Busters/issues/48) · [**G13**](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/50) · [**G18**](https://github.com/austin2578/CPSC490-G18-ProStrats/issues/43) · [**G20**](https://github.com/muntay89/CPSC490-G20-Solos/issues/31)
>
> Each of these groups has an instructor issue in its repository listing its HW#5 goals and objectives, our evaluation, and a fix checklist. **Sprint 2 is planned from exactly the §2 set**, and mismatches are reviewed in the Sprint 1 evaluation. Fix them before your Sprint 1 review.

**CPSC 490 · Fall 2026 · swept 2026-10-15 21:21 UTC.** The previous edition (2026-10-13) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. **Find your group below: your card lists everything still open for your team, in the order to fix it.** The rules and the full tables are at the end.

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ⚠️](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ⚠️](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

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

**1. The proposal hasn't reached `proposal/proposal.md` yet** (6 groups: G06, G08, G09, G11, G14, G15). §2 *Goals and Objectives* is still the template on both `main` and `develop`. Every other check on this page starts from that file, so until §2 is merged the page shows *0 issues linked*, even for groups that already have user stories on their board (G06, G08, G09, G11, G15). **Do this first:** copy §2 from your HW#4/HW#5 draft into `proposal/proposal.md`, open one pull request into `develop`, and merge it this week.

**2. Finished work is sitting in branches and open pull requests** (10 groups: G01, G03, G05, G06, G09, G11, G13, G14, G16, G19). This page, the harness and the sprint report read only `develop` and `main`, so a section drafted on a branch doesn't count yet. **Do this:** give every pull request a reviewer the day it opens, and merge (or close) it within two days. Delete branches you've abandoned.

**4. The board is a list, not a plan yet.** In 13 groups (G02, G03, G04, G05, G06, G07, G09, G10, G12, G13, G17, G19, G20) at least half the open issues have no assignee, and 18 groups (G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G18, G19, G20) have work items without their own `sp:` and `Sprint N` milestone. The sprint report can only count what's labeled. **Do this at your Sprint 1 review:** every card you commit to Sprint 2 gets one assignee, `sp:`, a `priority:` and the `Sprint 2` milestone before the meeting ends.

**5. Changes skip the pull-request step** (3 or more direct pushes in 8 groups: G01, G06, G07, G10, G15, G16, G17, G19). A direct push closes no issue and leaves nothing to review. **Do this:** turn on branch protection (*Settings → Branches → Add rule* for `main` and `develop`: *Require a pull request before merging*), so the repository enforces it for you.

**6. Pull-request descriptions are still the template** (20 groups). Write two lines: what changed and `Closes #N`. That one line is what moves the card on your board to *Done*.

**7. Goals haven't become epics and stories yet** (2 groups: G14, G17). Without them, Sprint 2 has nothing to point at. **Do this:** one epic per §2 goal and one user story per objective, titled with the objective's exact words (course README §4).

## Class at a glance

- ✅ **Aligned:** 15 (G01, G02, G04, G05, G06, G07, G08, G09, G10, G12, G13, G16, G18, G19, G20)
- ⚠️ **Partial:** 4 (G03, G11, G15, G17)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 0 (none)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 0 (none)
- Team-filed issues: **484** across 20 groups (67 new since 2026-10-13).

### What changed since 2026-10-13

- **G05 went from No issues to ✅ Aligned.** It now has 19 issues (2 epics, and 9 stories with `sp:` in Sprint 2), proposal §1–2 filled with 11 links on main, 8 PRs and a Sprint board. Develop still carries bare §2 links until PR #34 (main → develop) merges.
- **G17 went from No issues to ⚠️ Partial.** It filed its first issue (epic #15), and §2 Goals and Objectives are now written in proposal.md (PR #14 merged into develop). Goal 2 and four objectives still have no issues.
- **G01 and G13 grew their Sprint 2 backlogs** (G01 +31 issues, G13 +13). The new issues are not yet cited in proposal.md, so link coverage fell. Cite each new issue in §4 as a typed reference.
- **G14 removed the off-proposal web-scanner epic (#8),** but proposal.md is still the unfilled template and the README still describes a different project.
- **G11 rebuilt its board** around three goal epics and six objective stories. The PRs that link them from §2 (#35/#36) are still open, so develop's §2 is still a skeleton.
- **G15 and G19 started on links:** G15 added epics #24/#25 and a Sprint board; G19 opened PR #35 to fill §4, but it targets main instead of develop.
- **G16 opened PR #46** to switch its 21 proposal links to typed references (not merged yet).
- **No change:** G06, G08, G09, G10, G18 and G20 (evaluations carried over), plus G04, G07 and G12.

<a name="groups" id="groups"></a>

## Your group

**Jump to your group:**

| [**G01** ✅](#g01) | [**G02** ✅](#g02) | [**G03** ⚠️](#g03) | [**G04** ✅](#g04) | [**G05** ✅](#g05) | [**G06** ✅](#g06) | [**G07** ✅](#g07) | [**G08** ✅](#g08) | [**G09** ✅](#g09) | [**G10** ✅](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11** ⚠️](#g11) | [**G12** ✅](#g12) | [**G13** ✅](#g13) | [**G14** ❌](#g14) | [**G15** ⚠️](#g15) | [**G16** ✅](#g16) | [**G17** ⚠️](#g17) | [**G18** ✅](#g18) | [**G19** ✅](#g19) | [**G20** ✅](#g20) |

*Status* is how well the board matches the proposal. *Chain* is the document-first path: `proposal.md` → issue → pull request. *Start here* is the reviewer's one most useful next action; the numbered list is everything else, in order.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting

✅ **Aligned** · chain ⚠️ Gaps · 56 issues (41 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge #70 and #61 into develop (and release to main), fill the README project summary and contact, then put sp: and a Sprint 2 milestone on the Sprint 2 tasks (#76-#88, #91-#94) and on stories #23-#28.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #75, #70, #62, #61. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Link.* Cite 30 of 56 issues in `proposal.md` (epics and stories in §2, the rest in §4): #58, #64–#69, #71–#74, #76–#94.
4. *Plan.* Give #9–#14, #18, #23–#28, #32, #33, #43, #47, #49, #51, #53, #55, #58, #64–#67, #76–#88, #91–#94 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Remove `sp:` from epics #71–#74, #89, #90.
6. *Plan.* Assign 18 of 41 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (14 of 29 PRs closed no issue).

*Since 2026-10-13:* Filed 31 Sprint 2 issues (#64-#94: four design epics, a backtesting research epic, prototype v0 features, spec and research tasks), but only 26 of 56 issues are linked from proposal.md; the linking PRs (#70, #61) are still open and most new tasks lack sp:, while epics now carry sp: wrongly.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

✅ **Aligned** · chain ⚠️ Gaps · 40 issues (23 open) · Sprint 1 milestone: 0 open, 14 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Sync develop with main, then fill proposal §4 with typed links to every non-story issue (#17, #18, #23-#25, #36-#41 and the Sprint 1 tasks) and give the leftover Sprint 1 tasks an sp:.

Everything still open, in the order to fix it:

1. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
2. *Link.* Cite 22 of 40 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #8–#13, #15, #17, #18, #20–#25, #36–#41.
3. *Plan.* Give #6, #8–#13, #15, #36–#41 their own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign all 23 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 18 PRs closed no issue).

*Since 2026-10-13:* Prototype/data/frontend stories (#45-#61) are unchanged but all five Sprint 1 proposal tasks closed and 14 PRs (#62-#66) merged, goal 0 was removed from §2, so 18 of 40 issues are linked (down from 24); §4 is still a skeleton and develop is stale.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

⚠️ **Partial** · chain ⚠️ Gaps · 21 issues (13 open) · Sprint 1 milestone: 0 open, 6 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Add stories under epic #28 for equation-to-code generation and the literate-notebook output (and handwriting recognition), give every story an sp: and a Sprint 2 milestone, then link them as typed references in §2.

Everything still open, in the order to fix it:

1. *Unblock.* 3 branches hold work that isn't in `develop`: `Elizabeth-7-7-patch-1`, `Sehaj36-patch-1`, `eccortes4-proposal-epic-issues`. Open a pull request for each, or delete the branch.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: AI 2: equation-to-code generation; Literate-programming/notebook documentation output; End-to-end pipeline integration and computation of results; Handwriting recognition itself (stories only collect and sort inputs).
4. *Link.* Cite 11 of 21 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #2, #4, #5, #13, #15–#17, #20, #24, #39.
5. *Link.* Rewrite 10 bare `#N` references as typed links, e.g. `[[story:#37]](https://github.com/eccortes4/CPSC490-G03-California/issues/37)`.
6. *Plan.* Add 5 open issues to the board: #1, #20, #24, #27, #28.
7. *Plan.* Give #1, #2, #20, #24, #30–#37, #39 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign all 13 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (4 of 13 PRs closed no issue).

*Since 2026-10-13:* One new Sprint 2 task (#39, closed by merged PR #40 straight into main); still 10 of 21 issues linked and all as bare, untyped references, stories still lack sp:/Sprint, and §4 remains a skeleton.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polygon Prediction Market PNL and Trader Profitability Analytics

✅ **Aligned** · chain ⚠️ Gaps · 24 issues (15 open) · Sprint 1 milestone: 0 open, 9 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Add sp: points and a Sprint 2 (or later) milestone to the 12 stories #25-#28, #30-#32, #34-#38, then start the prototype with a PR for Objective 1.1.

Everything still open, in the order to fix it:

1. *Plan.* Give #12, #13, #25–#28, #30–#32, #34–#38 their own `sp:` label and a `Sprint N` milestone.
2. *Plan.* Assign all 15 open issues to one person each.
3. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (1 of 16 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS: Whale Identification/Location System

✅ **Aligned** (was No issues) · chain ⚠️ Gaps · 19 issues (14 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Tue Oct 13**, Sprint 2 review Tue Oct 27

**Start here:** Merge PR #34 so develop gets the typed §2 links, then add the remaining issues (#20, #23, #26, #29, #31, #33) to proposal §4 and give #20, #24, #25 a Sprint milestone.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #34, #32. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Identifying individual whales (only species-level identification is tracked); Microphone/hydrophone array setup or simulated array data (no issue for the hardware/data-collection side).
4. *Link.* Cite 8 of 19 issues in `proposal.md` (epics and stories in §2, the rest in §4): #20, #23–#26, #29, #31, #33.
5. *Link.* Rewrite 11 bare `#N` references as typed links, e.g. `[[story:#18]](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses/issues/18)`.
6. *Plan.* Give #20, #23–#25 their own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 7 of 14 open issues to one person each.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-13:* Large change: last edition found zero issues and an unmodified template; now 19 issues (2 epics, 9 stories with sp: in Sprint 2, writing tasks), proposal §1-2 filled with 11 linked items on main, 8 PRs (6 merged) and a Sprint board with a view.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · Forecast Market Analytics: GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking

✅ **Aligned** · chain ❌ Broken · 23 issues (22 open) · Sprint 1 milestone: 7 open, 1 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

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

*Since 2026-10-13:* Filed the new Goal 1-3 epics and 14 stories (#13-#31) with sp: and Sprints 1-3 in the last two days; still 0 issues linked from proposal.md, 18 direct commits on main and 1 of 2 PRs still open into main.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Online Material Database

✅ **Aligned** · chain ⚠️ Gaps · 25 issues (22 open) · Sprint 1 milestone: 7 open, 3 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 match, but the **issue numbers in HW#5 §2 are off by one from Goal 3 on**, and the repository has items HW#5 does not.
> See [the instructor issue](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/33) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Make the README describe the Online Material Database (it is still the course setup guide), then start Sprint 1 stories #12-#16 through PRs into develop that say Closes #N.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 9 of 25 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1, #4–#7, #27–#29, #34.
4. *Link.* Rewrite 16 bare `#N` references as typed links, e.g. `[[story:#26]](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin/issues/26)`.
5. *Plan.* Add 1 open issue to the board: #29.
6. *Plan.* Give #34 its own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 18 of 22 open issues to one person each.
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

*Since 2026-10-13:* Three duplicate objective issues (#45-#47) were created 10-12 (#46 already closed); proposal.md still links only 7 of 36 issues, all bare, and PR flow is otherwise unchanged.

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

*Since 2026-10-13:* Chain improved from BROKEN: 12 of 27 issues now linked from proposal.md on main (bare, not typed), 4 issues closed and 8 tied to PRs (3 merged); stories #29-#38 still lack sp: and Sprint milestones.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: On-Chain Stablecoin Flow and Wash Trading Detection

✅ **Aligned** · chain ❌ Broken · 22 issues (12 open) · Sprint 1 milestone: 3 open, 9 closed · **Sprint 1 review Tue Oct 20**, Sprint 2 review Tue Nov 3

**Start here:** Link epics #15/#23/#24 and stories #25-#33 from proposal.md §2 and the tasks from §4 as typed references, fix epics #23/#24 whose bodies hold unrelated text ('Members' data is private...'), and stop committing straight to main.

Everything still open, in the order to fix it:

1. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Validation strategy (synthetic ring injection, known case studies, manual precision review) described in Proposed Approaches has no objective or issue; Address-label enrichment (exchanges, bridges, routers) used to control false positives.
2. *Link.* Cite all 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #3–#9, #13, #15, #18, #20, #23–#33.
3. *Plan.* Give #3, #6, #13 their own `sp:` label and a `Sprint N` milestone.
4. *Plan.* Assign all 12 open issues to one person each.
5. *Workflow.* Stop pushing straight to `main`/`develop` (28 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 6 PRs closed no issue).

*Since 2026-10-13:* Epics #23/#24 and stories #25-#33 now exist (verdict moves from PARTIAL to ALIGNED), board has 5 views, but proposal.md still links 0 of 22 issues and 14 direct commits to main remain.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

⚠️ **Partial** · chain ❌ Broken · 21 issues (12 open) · Sprint 1 milestone: 2 open, 9 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

**Start here:** Merge PR #36 (§2 goals) and #35, then reconcile the proposal: say whether the product is runner analytics with ML or live event tracking plus posts, and make the README describe it (it is still the setup guide).

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #36, #35. Work in an open PR doesn't count yet.
2. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
3. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
4. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
5. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Use of publicly available marathon datasets as a baseline; Recommending more efficient running patterns/routes (only finish-time prediction is tracked); Storing runs/performance history for the individual runner (not an explicit objective).
6. *Link.* Cite 19 of 21 issues in `proposal.md` (epics and stories in §2, the rest in §4): #1–#3, #6–#9, #17, #20, #26–#34, #37.
7. *Link.* Rewrite 2 bare `#N` references as typed links, e.g. `[[story:#13]](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys/issues/13)`.
8. *Plan.* Link your Sprint Board to the repository (the repository's *Projects* tab → *Link a project*).
9. *Plan.* Add 1 open issue to the board: #37.
10. *Plan.* Give #1, #2, #6, #13, #34, #37 their own `sp:` label and a `Sprint N` milestone.
11. *Plan.* Assign 3 of 12 open issues to one person each.
12. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
13. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N`.

*Since 2026-10-13:* Large board change: epics #26/#27 and objectives #28-#33 (live tracking, shareable posts, race-time prediction) plus #37 were added, and PRs #35/#36 are open, but proposal.md still links only 2 of 21 issues and the epics now diverge from the submitted proposal's ML analysis focus.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

✅ **Aligned** · chain ⚠️ Gaps · 34 issues (16 open) · Sprint 1 milestone: 1 open, 34 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The stories match, but **HW#5 §2 cites placeholder numbers** ([Epic:#1]–[Epic:#5], [Story#1]/[Story#2]) instead of the real issues, and two epic titles differ from §2.
> See [the instructor issue](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/82) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Give stories #62-#71 a Sprint milestone and add issues for baud/carrier estimation and robustness evaluation, then rewrite the README, which still says Project title TBD.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Baud-rate and carrier-frequency estimation; Evaluation of robustness across SNR, multipath and Doppler with common data partitions; Simulated 6G data generation; Modular design / interface control document between components.
3. *Link.* Cite 7 of 34 issues in `proposal.md` (epics and stories in §2, the rest in §4): #27–#32, #36.
4. *Link.* Rewrite 27 bare `#N` references as typed links, e.g. `[[story:#76]](https://github.com/CharlesSinde/CPSC490-G12-ACJMM/issues/76)`.
5. *Plan.* Give #62–#71 their own `sp:` label and a `Sprint N` milestone.
6. *Plan.* Assign 15 of 16 open issues to one person each.
7. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
8. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 21 PRs closed no issue).

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: Assignment Motivation Initiative Year-Round Assistant

✅ **Aligned** · chain ⚠️ Gaps · 40 issues (25 open) · Sprint 1 milestone: 0 open, 11 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!WARNING]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Goals 1–3 and their objectives match, but the repository has a **Goal 0 epic (#30) with stories #31–#33** that HW#5 §2 does not have, and §2 cites no issue numbers.
> See [the instructor issue](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/50) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Settle the platform (abstract/§3 say Windows desktop, §4/§5 say Python+JS web app) and update §4, then add sp: and Sprint milestones to the stories and all tasks.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #52. Work in an open PR doesn't count yet.
2. *Link.* Cite 28 of 40 issues in `proposal.md` (epics and stories in §2, the rest in §4): #8, #10–#13, #15, #30–#35, #43, #44, #47, #53–#65.
3. *Link.* Rewrite 12 bare `#N` references as typed links, e.g. `[[story:#27]](https://github.com/ktnwin/CPSC490-G13-BYKX/issues/27)`.
4. *Plan.* Give #8, #10–#13, #15, #19–#27, #31–#34 their own `sp:` label and a `Sprint N` milestone.
5. *Plan.* Assign all 25 open issues to one person each.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 17 PRs closed no issue).

*Since 2026-10-13:* Backlog grew from 27 to 40 issues with features #53-#54/#59-#60/#65 and tasks #55-#58/#61-#64 under stories #22-#24, all in Sprint 2; proposal.md still links only 12 and §4 is still a placeholder.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Rogue-Lite Cyber Sandbox

❌ **Mismatch** · chain ❌ Broken · 3 issues (3 open) · Sprint 1 milestone: 2 open, 2 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2 at all**: it has one epic, #8 *Create web scanner*, and no stories. HW#5 §2 has 2 goals and 10 objectives for a cybersecurity training sandbox.
> See [the instructor issue](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad/issues/21) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Decide the project (README says AI Assisted Security Operations Platform, proposal says Rogue-Lite Cyber Sandbox), move the submitted proposal into proposal.md, write §2, then file epics and stories for the chosen project.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #12, #9. Work in an open PR doesn't count yet.
2. *Document.* Your board or README describes a **different project** than your proposal. Make them match, or tell the instructor the project changed.
3. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
4. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop` (a draft may already be in one of the branches above).
5. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
6. *Board.* Create one **epic** per §2 goal and one **user story** per objective, titled with the objective's exact words.
7. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: All core elements: no epics, stories or feature issues exist; proposal/proposal.md still the unfilled template (§0-§4 skeleton, 83 placeholders).
8. *Link.* Cite all 3 issues in `proposal.md` (epics and stories in §2, the rest in §4): #4, #6, #13.
9. *Plan.* Add 1 open issue to the board: #13.
10. *Plan.* Give #13 their own `sp:` label and a `Sprint N` milestone.
11. *Plan.* Assign 1 of 3 open issues to one person each.
12. *Workflow.* Stop pushing straight to `main`/`develop` (2 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
13. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 7 PRs closed no issue).

*Since 2026-10-13:* Issue #8 (web scanner) is gone and only 3 process issues remain (#13 Update README, #6, #4); proposal.md still an unfilled template and the README (AI-assisted SOC platform) still disagrees with the sandbox proposal.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Low End Hardware ECS Game Engine with Game

⚠️ **Partial** · chain ❌ Broken · 8 issues (5 open) · Sprint 1 milestone: 2 open, 0 closed · **Sprint 1 review Thu Oct 15**, Sprint 2 review Thu Oct 29

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** The repository **does not reflect HW#5 §2**: it has one epic, #6 *Setting up*, with one story, #9 *Window and Renderer*. HW#5 §2 has 2 goals (*Game Demo*, *Game Engine*) and 8 objectives.
> See [the instructor issue](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01/issues/23) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Write §2 goals and objectives, add the ECS and benchmarking objectives, fill the blank story lists in epics #24 and #25 with real stories (objective text verbatim, sp: in a Sprint milestone), link all in proposal.md as typed references, and replace the template README.

Everything still open, in the order to fix it:

1. *Document.* Make `README.md` on `main` describe your project: title, sponsor code (if any), one-paragraph summary, Sprint Board link.
2. *Document.* Write **§2 Goals and Objectives** into `proposal/proposal.md` and merge it into `develop`.
3. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
4. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: ECS implementation (no issue; not named in any epic); Benchmarking and performance evaluation (the proposal's central goal); Memory management; Stories under #24 and #25 (both still list blank '#' placeholders); Story for closing the window (listed in epic #6, no issue).
5. *Link.* Cite all 8 issues in `proposal.md` (epics and stories in §2, the rest in §4): #6, #9–#12, #16, #24, #25.
6. *Plan.* Add 2 open issues to the board: #9, #10.
7. *Plan.* Give #12, #16 their own `sp:` label and a `Sprint N` milestone.
8. *Plan.* Assign 2 of 5 open issues to one person each.
9. *Workflow.* Stop pushing straight to `main`/`develop` (8 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
10. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (3 of 8 PRs closed no issue).

*Since 2026-10-13:* Two new epics (#24 Game Engine, #25 Game Demo) filed 10-15 with goals but blank story lists, and the Sprint board now exists (10 items, still missing #9 and #10); still 0 of 8 issues linked from proposal.md, §2/§4 still skeletons, 4 direct commits on main, #10/#11 still open after merged PRs.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits

✅ **Aligned** · chain ⚠️ Gaps · 22 issues (18 open) · Sprint 1 milestone: 7 open, 3 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Merge PR #46 so the 21 bare issue links in proposal.md become typed references ([epic:#11], [story:#14], [task:#27]), make the Sprint board (users/garybs16/projects/2, now linked in README) publicly readable with every open issue on it, and merge release PR #48 so main matches develop.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull requests #48, #47, #46, #44. Work in an open PR doesn't count yet.
2. *Link.* Cite 1 of 22 issues in `proposal.md` (epics and stories in §2, the rest in §4): #45.
3. *Link.* Rewrite 21 bare `#N` references as typed links, e.g. `[[story:#39]](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic/issues/39)`.
4. *Plan.* Create the **Sprint Board** (*Projects → New project → Board*) and link it from the repository's Projects tab and the README.
5. *Workflow.* Stop pushing straight to `main`/`develop` (6 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
6. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 20 PRs closed no issue).

*Since 2026-10-13:* Task #45 filed and PR #46 opened to convert the 21 bare links to typed references (not merged yet), README now links the Sprint board (still unreadable), more open PRs (#44, #46-#48) pending; 21 of 22 issues linked, 0 typed, still no direct-push growth.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · Sonic Scape: SonicScape / EchoSphere

⚠️ **Partial** (was No issues) · chain ❌ Broken · 1 issues (1 open) · Sprint 1 milestone: 0 open, 0 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

> [!CAUTION]
> **HW#5 check (Oct 12): your epics and user stories do not match your HW#5 §2 Goals and Objectives.** Your repository has **no epics or user stories**. HW#5 §2 lists 2 goals and 5 objectives with placeholder numbers (#〈1〉, #〈2〉).
> See [the instructor issue](https://github.com/vibhorbh/CPSC490-G17-SonicScape/issues/13) for your goals and objectives as submitted, our evaluation and the fix checklist.

**Start here:** Create the real issues now: epic Goal 2, stories for Objectives 1.1, 1.2, 2.1 and 2.2 (objective text verbatim, sp: points, Sprint 1 or 2 milestone), plus tasks for the proposal sections, put them on the Sprint board, then replace the made-up #1-#4 numbers in proposal.md with typed references to the real issue numbers.

Everything still open, in the order to fix it:

1. *Board.* Create one **user story** per objective, titled with the objective's exact words.
2. *Scope.* Reviewer's notes on proposal elements with no issue yet, or that don't agree: Goal 2 (find new artists and music) and its objectives 2.1 (Music class / Last.fm API) and 2.2 (LLM taste learning): no epic or stories; Objectives 1.1 (exoplanet API parser) and 1.2 (solar-system UI): no stories; Swipe feedback, playback/playlists/search; Any tasks, e.g. writing tasks for §1 to §4.
3. *Link.* Cite all 1 issues in `proposal.md` (epics and stories in §2, the rest in §4): #15.
4. *Plan.* Add 1 open issue to the board: #15.
5. *Plan.* Assign all 1 open issues to one person each.
6. *Workflow.* Stop pushing straight to `main`/`develop` (4 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
7. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (5 of 5 PRs closed no issue).

*Since 2026-10-13:* First team issue filed (#15 epic 'Goal 1', created 10-15, blank story list, no milestone, not on the board), §2 goals and objectives now written in proposal.md with placeholder issue numbers, and a develop PR (#14) merged; still 1 issue total, 0 linked, §4 skeleton, no sp:, no Sprint 1 milestone usage.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · Team ProStrats: Project Rogue

✅ **Aligned** · chain ⚠️ Gaps · 27 issues (19 open) · Sprint 1 milestone: 15 open, 7 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

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

*Since 2026-10-13:* Epics #29-#31 and 10 stories (#32-#41) added, §2 links 13 typed refs on develop (was 0 of 12 linked), but §4 is still a skeleton, 14 issues are unlinked, and main still has the skeleton.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over Wi-Fi (ROW) drone detection

✅ **Aligned** · chain ⚠️ Gaps · 19 issues (19 open) · Sprint 1 milestone: 17 open, 4 closed · **Sprint 1 review Thu Oct 22**, Sprint 2 review Thu Nov 5

**Start here:** Merge #35 (retarget to develop) so §4 lists the remaining tasks, convert the 10 bare refs in §2 to typed refs, close the finished writing tasks, and release develop to main so the proposal and a real team README land there.

Everything still open, in the order to fix it:

1. *Unblock.* Review and merge (or close) your open pull request #35. Work in an open PR doesn't count yet.
2. *Document.* Fill in **§4**: list your other work items (tasks, features, documents) there.
3. *Link.* Cite 6 of 19 issues in `proposal.md` (epics and stories in §2, the rest in §4): #23, #26–#29, #34.
4. *Link.* Rewrite 10 bare `#N` references as typed links, e.g. `[[story:#20]](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/20)`.
5. *Plan.* Add 2 open issues to the board: #23, #34.
6. *Plan.* Give #23 its own `sp:` label and a `Sprint N` milestone.
7. *Plan.* Assign 12 of 19 open issues to one person each.
8. *Workflow.* Stop pushing straight to `main`/`develop` (64 direct commits so far): branch → pull request → review → merge. Turn on branch protection.
9. *Workflow.* In every pull request, replace the template text with what changed, and add `Closes #N` (2 of 10 PRs closed no issue).

*Since 2026-10-13:* Task #34 and PR #35 (adds §4 links) opened, but the PR is unmerged into main, not develop; linked issues still 13 of 19 (68%, was 13 of 18) with 3 typed refs, §4 still a skeleton, Sprint 1 now 17 open and 4 closed, board holds 23 items but misses #34 and #23.

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

*Since 2026-10-13:* From zero issues to 16: three epics, eight stories, five Sprint 1 tasks, a Sprint board with every open issue, README rewritten as Insomnia on develop, and two PRs merged that close issues; only 3 epics are linked from proposal.md and stories lack sp:.

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
| G01 | §2 9 links · §4 17 links · 26 issues cited · 38 typed · 17 〈placeholders〉 | §2 9 links · §4 17 links · 26 issues cited · 36 typed · 17 〈placeholders〉 | 18-abstract-intro (2 commits not in develop); 43-update-goals-and-objectives (2 commits not in develop); 55-hw5-proposal (1 commit not in develop); 67-link-sprint2-items (5 commits not in develop); Damon (1 commit not in develop) |
| G02 | §2 18 links · §4 skeleton · 18 issues cited · 18 typed · 40 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | none |
| G03 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 42 〈placeholders〉 | §2 10 links · §4 skeleton · 10 issues cited · 0 typed · 45 〈placeholders〉 | Elizabeth-7-7-patch-1 (1 commit not in develop); Sehaj36-patch-1 (1 commit not in develop); eccortes4-proposal-epic-issues (1 commit not in develop) |
| G04 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | §2 15 links · §4 9 links · 24 issues cited · 24 typed · 17 〈placeholders〉 | none |
| G05 | §2 11 links · §4 skeleton · 11 issues cited · 11 typed · 43 〈placeholders〉 | §2 11 links · §4 skeleton · 11 issues cited · 0 typed · 43 〈placeholders〉 | feature/31-sprint1-meetings (1 commit not in develop) |
| G06 | §2 0 links · §4 skeleton · 0 issues cited · 0 typed · 47 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 82 〈placeholders〉 | feature/14-document-upload (18 commits not in develop) |
| G07 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | none |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | none |
| G09 | §2 skeleton · §4 skeleton · 12 issues cited · 0 typed · 62 〈placeholders〉 | §2 12 links · §4 skeleton · 12 issues cited · 0 typed · 53 〈placeholders〉 | feature/6-Related-Work-Table-and-9-AI-Usage-+-References (6 commits not in develop); feature/7-problem-statements (2 commits not in develop); feature/8-proposal-cleanup (10 commits not in develop); feature/11-update-readme (5 commits not in develop); feature/19-archive-hw4-draft (1 commit not in develop); proposal-draft (3 commits not in develop) |
| G10 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | none |
| G11 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 67 〈placeholders〉 | §2 skeleton · §4 skeleton · 2 issues cited · 0 typed · 70 〈placeholders〉 | 1-2-problem-statements (1 commit not in develop); feature/3-goals-objectives (3 commits not in develop) |
| G12 | §2 15 links · §4 12 links · 27 issues cited · 0 typed | §2 15 links · §4 12 links · 27 issues cited · 0 typed | none |
| G13 | §2 12 links · §4 12 links · 12 issues cited · 0 typed | §2 12 links · §4 12 links · 12 issues cited · 0 typed | feature/32-project-proposal (6 commits not in develop); sprint1-patch-1 (1 commit not in develop); updated-proposal (3 commits not in develop) |
| G14 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | jvillacorte-patch-3 (1 commit not in develop) |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 74 〈placeholders〉 | none |
| G16 | §2 12 links · §4 9 links · 20 issues cited · 0 typed | §2 12 links · §4 10 links · 21 issues cited · 0 typed | 30-sprint-1-review (1 commit not in develop); 42-course-update (1 commit not in develop); 45-proposal-typed-refs (1 commit not in develop) |
| G17 | §2 4 links · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | §2 4 links · §4 skeleton · 0 issues cited · 0 typed · 66 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 13 links · §4 skeleton · 13 issues cited · 18 typed (5 misplaced) · 40 〈placeholders〉 | none |
| G19 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 80 〈placeholders〉 | §2 11 links · §4 skeleton · 13 issues cited · 3 typed · 26 〈placeholders〉 | feature/34-section4-links (2 commits not in develop) |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 63 〈placeholders〉 | none |

### Document first: proposal.md → issue → pull request

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain |
|---|---|---|---|---|---|---|---|
| G01 | 9 links / 17 links | 26 of 56 | 26 of 26 | 14 / 11 of 26 | 14 of 29 | 3 / 3 | ⚠️ Gaps |
| G02 | 18 links / skeleton | 18 of 40 | 18 of 18 | 0 / 0 of 18 | 4 of 18 | 1 / 1 | ⚠️ Gaps |
| G03 | 10 links / skeleton | 10 of 21 | 0 of 10 | 0 / 0 of 10 | 4 of 13 | 1 / 1 | ⚠️ Gaps |
| G04 | 15 links / 9 links | 24 of 24 | 24 of 24 | 9 / 6 of 24 | 1 of 16 | 0 / 0 | ⚠️ Gaps |
| G05 | 11 links / skeleton | 11 of 19 | 0 of 11 | 0 / 0 of 11 | 0 of 8 | 0 / 0 | ⚠️ Gaps |
| G06 | skeleton / skeleton | 0 of 23 | 0 of 0 | 0 / 0 of 0 | 0 of 2 | 18 / 0 | ❌ Broken |
| G07 | 16 links / skeleton | 16 of 25 | 0 of 16 | 0 / 0 of 16 | 1 of 2 | 2 / 2 | ⚠️ Gaps |
| G08 | skeleton / skeleton | 7 of 36 | 0 of 7 | 0 / 5 of 7 | 1 of 5 | 0 / 0 | ⚠️ Gaps |
| G09 | skeleton / skeleton | 12 of 27 | 0 of 12 | 4 / 8 of 12 | 1 of 8 | 0 / 0 | ⚠️ Gaps |
| G10 | 0 links / 0 links | 0 of 22 | 0 of 0 | 0 / 0 of 0 | 3 of 6 | 14 / 14 | ❌ Broken |
| G11 | skeleton / skeleton | 2 of 21 | 0 of 2 | 1 / 1 of 2 | 0 of 10 | 1 / 1 | ❌ Broken |
| G12 | 15 links / 12 links | 27 of 34 | 0 of 27 | 11 / 6 of 27 | 3 of 21 | 1 / 1 | ⚠️ Gaps |
| G13 | 12 links / 12 links | 12 of 40 | 0 of 12 | 0 / 0 of 12 | 2 of 17 | 0 / 0 | ⚠️ Gaps |
| G14 | skeleton / skeleton | 0 of 3 | 0 of 0 | 0 / 0 of 0 | 2 of 7 | 1 / 1 | ❌ Broken |
| G15 | skeleton / skeleton | 0 of 8 | 0 of 0 | 0 / 0 of 0 | 3 of 8 | 4 / 4 | ❌ Broken |
| G16 | 12 links / 10 links | 21 of 22 | 0 of 21 | 4 / 7 of 21 | 5 of 20 | 3 / 3 | ⚠️ Gaps |
| G17 | 4 links / skeleton | 0 of 1 | 0 of 0 | 0 / 0 of 0 | 5 of 5 | 2 / 2 | ❌ Broken |
| G18 | 13 links / skeleton | 13 of 27 | 13 of 13; 5 in the wrong section | 0 / 0 of 13 | 0 of 9 | 1 / 1 | ⚠️ Gaps |
| G19 | 11 links / skeleton | 13 of 19 | 3 of 13 | 0 / 2 of 13 | 2 of 10 | 36 / 28 | ⚠️ Gaps |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 3 | 1 / 1 | ⚠️ Gaps |

### Sprint board and story points

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [BGAF Sprint Board](https://github.com/users/LeDuy23/projects/3) | 41 of 41 | ✅ | 43 | none | 6 |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 23 of 23 | ✅ | 14 | none | none |
| G03 | ✅ [CPSC-490-G03-California](https://github.com/users/eccortes4/projects/1) | 8 of 13 | ✅ | 13 | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 15 of 15 | ✅ | 14 | none | none |
| G05 | ✅ [WILS](https://github.com/users/M-Kwatcher/projects/2) | 14 of 14 | ✅ | 4 | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 18 of 22 | ✅ | 2 | 1 | 3 |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 21 of 22 | ✅ | 1 | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 30 of 34 | ✅ | 4 | 1 | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 23 of 23 | ✅ | 10 | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 12 of 12 | ✅ | 3 | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/Card1n/projects/1) ⚠️ not linked to the repo | 11 of 12 | ✅ | 6 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 16 of 16 | ✅ | 10 | none | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 25 of 25 | ✅ | 19 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 2 of 3 | ✅ | 2 (Sprint 1 rule) | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 3 of 5 | ✅ | 2 | none | none |
| G16 | ❌ none (README links github.com/users/garybs16/projects/2 but it isn't readable (private, or wrong URL)) | – | – | none | none | none |
| G17 | ✅ [G17-SonicScape-Sprint-Board](https://github.com/users/vibhorbh/projects/2) | 0 of 1 | ✅ | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 17 of 19 | ✅ | 10 | none | none |
| G19 | ✅ [CPSC490-G19-TitanSecurity](https://github.com/users/sopper75/projects/1) | 17 of 19 | ✅ | 1 | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

### Every group, by number

| Group | Project | Board | README | Status |
|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 56 issues (29 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 40 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G03 California | Three AIs and Literate Programming | 21 issues; epics, stories, Sprint 1 | matches | ⚠️ **Partial** |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 24 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G05 Fighting Mongooses | WILS: Whale Identification/Location System | 19 issues (19 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 23 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G07 Mighty Morphin | Online Material Database | 25 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G08 Crime Busters | Interactive Crime Map and Database | 36 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G09 Sigma Squad | Vehicle Maintenance Logger | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G10 Team Jiddak | On-Chain Stablecoin Flow and Wash Trading Detection | 22 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G11 5 Guys | Marathon Tracker | 21 issues (1 new); epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G12 ACJMM | Explainable 6G Waveform Classification | 34 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 40 issues (13 new); epics, stories, Sprint 1 | matches | ✅ **Aligned** |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 3 issues; points, Sprint 1 | not yet | ❌ **Mismatch** |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 8 issues (2 new); epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 22 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G17 Sonic Scape | SonicScape / EchoSphere | 1 issues (1 new); epics | matches | ⚠️ **Partial** |
| G18 Team ProStrats | Project Rogue | 27 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G19 Titan Security | Radar over Wi-Fi (ROW) drone detection | 19 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** |
| G20 Solos | Insomnia | 16 issues; epics, stories | matches | ✅ **Aligned** |

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
