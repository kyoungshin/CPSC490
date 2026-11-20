# Group repository status: Sprint 4 readiness (the whole paper, §0–§8, and a fully functional prototype)

## Word export check (Nov 20): fix these in `proposal.md`

You submit the Preview (Sun Nov 29) and the Final (Sun Dec 20) as Word files made from `proposal/proposal.md`. I converted every group's `proposal.md` (both `main` and `develop`) with pandoc and the course converter, using the command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). All 20 convert without errors. The table below lists what still comes out wrong in Word, on the branch with your fuller proposal.

**Everyone: copy the updated converter first. As of Nov 20, no group has it.** Since Nov 18, [`proposal/to-word.lua`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/to-word.lua) scales every picture to fit the page: at most 6.5 in wide and 8.5 in tall, aspect ratio kept. With an older copy, a tall diagram runs off the bottom of the page. Copy it, and [`proposal/reference.docx`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/reference.docx), into your `proposal/` folder, replacing your old copies. Then run the README command again.

**〈placeholders〉:** the converter warns about any 〈…〉 left outside the guidance quotes, and Word prints it as typed. Sprint 4 finishes the whole paper, so none may remain: draft §5–§8 for the Preview and clear every one before the Final.

| Group | Branch | Converter in your repo | What comes out wrong in Word |
|---|---|---|---|
| G01 | `main` | Old copy: replace it | Clean. |
| G02 | `develop` | Old copy: replace it | 〈…〉 in §5 and §7. |
| G03 | `main` (same as `develop`) | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §1, §4 and §5–§8. |
| G04 | `main` | Old copy: replace it | 〈…〉 in §5–§7. |
| G05 | `develop` | Old copy: replace it | The header block still has 〈…〉 in the sponsor and the date, so the cover page leaves them blank. 〈…〉 in §0, §3, §4 and §5–§7. |
| G06 | `develop` | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §5–§7. |
| G07 | `main` | Old copy: replace it | The header block's date is still in 〈…〉, so the cover page leaves it blank. 〈…〉 in §5–§7. |
| G08 | `develop` | Old copy: replace it | Clean. |
| G09 | `develop` | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §5 and §6. |
| G10 | `develop` | Old copy: replace it | The header block wraps your real values in 〈…〉 (title, group, team, sponsor, authors, date). The converter treats them as unfilled, so **the cover page comes out blank**: remove the brackets and keep the values. |
| G11 | `main` | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §1 and §4–§8. |
| G12 | `develop` | Old copy: replace it | 〈…〉 in §4, including a reference written `task:#〈n〉`: put the real issue number in. |
| G13 | `main` (same as `develop`) | Old copy: replace it | Clean. |
| G14 | `develop` | Old copy: replace it | 〈…〉 in §5–§7. |
| G15 | `main` (same as `develop`) | Old copy: replace it | **25 references are plain text, `[story:https://…/issues/26]`, not links,** so the full URLs stay in your paragraphs and Appendix A is nearly empty. Write each one as a typed link: `[[story:#26]](https://github.com/…/issues/26)`. Two links are untyped, `[#25](https://…/issues/25)`; type them too (`[[feature:#25]](https://…/issues/25)`). 〈…〉 in §5–§7. |
| G16 | `main` (same as `develop`) | Old copy: replace it | Clean. |
| G17 | `main` | Old copy: replace it | 〈…〉 in §5–§8. |
| G18 | `develop` | Old copy: replace it | Two diagrams are `.svg`. pandoc needs `rsvg-convert` to embed them for older Word versions and warns without it; export them as `.png` instead. 〈…〉 in §6–§8. |
| G19 | `develop` | Old copy: replace it | 〈…〉 in §4–§7. |
| G20 | `main` (same as `develop`) | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §3, §5–§8 and in the References block above §8. |

> [!IMPORTANT]
> **New (Nov 20): this page now checks Sprint 4 readiness.** Every group has had its Sprint 3 review and is in Sprint 4. Sprint 4 asks for the same three rules of thumb, taken to the finish: **finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages** without the Appendix, and **complete the prototype so it is fully functional**. You run Sprint 4 on the board as usual, and I grade it on the same five rubric lenses; this page is a readiness check, not your sprint grade. Find your group's card below: it says what's missing and what to do, in order.
>
> **The marks now measure against the Sprint 4 bar.** Rule 2 used to ask for §0–§4 and now asks for the whole paper; rule 3 used to ask for one working slice and now asks for the complete prototype. A mark can read lower than in the last edition with nothing in your repository having gone backwards.

**CPSC 490 · Fall 2026 · swept Nov 20, 10:36 AM PST.** Earlier editions are kept in this file's git history.

**Jump to your group:**

| [**G01**](#g01) | [**G02**](#g02) | [**G03**](#g03) | [**G04**](#g04) | [**G05**](#g05) | [**G06**](#g06) | [**G07**](#g07) | [**G08**](#g08) | [**G09**](#g09) | [**G10**](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11**](#g11) | [**G12**](#g12) | [**G13**](#g13) | [**G14**](#g14) | [**G15**](#g15) | [**G16**](#g16) | [**G17**](#g17) | [**G18**](#g18) | [**G19**](#g19) | [**G20**](#g20) |

## What's due, and when

| Groups | Sprint 4 | Sprint 4 ends | Presentation and prototype demo (Zoom, 7 PM) |
|---|---|---|---|
| G01–G05 | Nov 10 – 30 | **Mon Nov 30** | Tue Dec 1 |
| G11–G15 | Nov 12 – Dec 2 | **Wed Dec 2** | Thu Dec 3 |
| G06–G10 | Nov 17 – Dec 7 | **Mon Dec 7** | Tue Dec 8 |
| G16–G20 | Nov 19 – Dec 9 | **Wed Dec 9** | Thu Dec 10 |

- **Sun Nov 29: Preview Project Proposal Paper.** Every section drafted, §0–§4 complete.
- **The day before your presentation: Sprint 4 ends.** Sprint 4 is one week longer for every group because of Thanksgiving week (updated Nov 19).
- **Your presentation: the prototype demo.** You demo the finished prototype there, and every member speaks.
- **Sun Dec 20: Final Project Proposal Paper.** §5–§8 complete, more than 50 pages without the Appendix, Preview feedback addressed. No late submissions.

The full calendar is on the [sprint schedule](https://github.com/kyoungshin/CPSC490/blob/main/docs/sprint-schedule.md).

## The three rules of thumb, at the Sprint 4 bar

1. **Every PR references its issue, and every issue is linked from `proposal/proposal.md`.** Each PR says `Closes #N`. Epics and stories are cited in §2; every feature, task and sub-task is cited in §4 as a typed reference such as `[feature:#23]`. Every user story is broken down on the board into sub-issues: story → feature (or enhancement or bug) → task → sub-task. **Story points go on the user story only, once**; don't point its features or tasks. Every child issue has one assignee and the Sprint milestone, and moves across the board as you work. If your group uses `main` and `develop`, keep the two streams apart: develop on `develop` during the sprint, and release from `develop` to `main` at the end of the sprint. Steps: [git-workflow.md](https://github.com/kyoungshin/CPSC490/blob/main/docs/git-workflow.md); worked example: [#1 → #3 → #6 → #5 → #7](https://github.com/kyoungshin/CPSC490/issues/1).
2. **The proposal is the whole paper, §0–§8, and it stands on its own.** The final paper runs more than 50 pages in Times New Roman 11 pt, 1.5 spacing. The Appendix doesn't count toward that, and issue links move into the Appendix when `proposal.md` is converted to Word, so a table of issue links adds no pages. Write full paragraphs that explain the work and end each one with its issue references. No template text or 〈placeholder〉 may remain.
   - §0 Abstract, §1 Introduction, §1.1 Related Work (a pros-and-cons table across existing work, then prose on what you do differently), §1.2 Problem Statements, §2 Goals and Objectives, §3 Proposed Approaches.
   - **§4, the largest section, where most of your pages come from:**
     - Environment and resources, with the reason for each choice.
     - One specification per epic: scope, functional and non-functional requirements, acceptance criteria and open questions ([model](https://github.com/kyoungshin/CPSC490/blob/main/docs/specs/example-spec.md)).
     - Design documents: context, components, data model, data flow, key decisions with the alternatives you rejected, and what isn't designed yet ([model](https://github.com/kyoungshin/CPSC490/blob/main/docs/design/example-design.md)).
     - Diagrams, each with prose that explains it.
     - Implementation details of what the prototype does.
     - The planned activities, written in prose.
   - Every spec, design section and diagram must be in `proposal.md`, either in full or summarized and linked from §4.
   - **§5 Project Outcomes:** one or two paragraphs on what exists when the project is finished, naming the deliverables, what the prototype demonstrates and how to run it.
   - **§6 Project Timeline:** your plan for CPSC 491 next semester, not this fall's sprints: the tasks (your §2 objectives), milestones, estimated hours and the assumptions behind them.
   - **§7 AI Usage:** which tools, for which tasks, about what fraction of each artifact, and how you verified the result. Naming a tool is not a disclosure.
   - **§8 References:** numbered in the order first cited, cited in the text as [1], [2]; every source in §1.1 appears here.
3. **The code under `prototype/` must always work, and by the end of Sprint 4 it is complete.** Whatever is in it has to install, run and pass CI (the *Prototype build & tests* job). Every story you put in scope works end to end, with a test for each of its acceptance criteria, ready to demo at your presentation. The folders mirror your architecture diagram, and `prototype/README.md` has run commands that work from a clean clone ([CI gate](https://github.com/kyoungshin/CPSC490/blob/main/.github/workflows/ci.yml)).

4. **Your proposal converts to Word.** You submit the Preview and the Final as Word files, so I convert each group's `proposal/proposal.md` with pandoc and the course converter, using the one command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). The converter (`proposal/to-word.lua` in the course repo) pulls every GitHub issue link out of the text and lists it in *Appendix A. Issue References*, as tables grouped by type. In the text, each link becomes a small citation such as `[task:#23]` that jumps to its row. To fill in the Title column, first export your issue titles with `gh issue list --state all --limit 1000 --json number,title > proposal/issues.json`. A reference only moves to the appendix if it's written as a link: `[task:#23](https://github.com/OWNER/REPO/issues/23)`. The Word export check at the top of this page lists what comes out wrong for your group.

As before, it only counts once it's **merged into `develop` or `main`**. Work left in a branch or an open pull request doesn't count yet.

## Class at a glance

✅ done · ⚠️ partial · ❌ not there yet. **Pages so far** is a rough estimate (words outside the Appendix ÷ 500) to set against the 50-page final; tables and figures add a little more. It carries a ✅ once it passes 50.

| Group | Sprint 4 ends | 1. PRs ↔ issues ↔ proposal | 2. Paper §0–§8 | Pages so far (target 50+) | 3. Prototype complete | 4. Word export | Ready to present |
|---|---|---|---|---|---|---|---|
| [G01](#g01) BGAF | Mon Nov 30 | ⚠️ | ⚠️ | ✅ ≈ 99 | ⚠️ | ⚠️ | ⚠️ |
| [G02](#g02) Linux Larpers | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 15 | ⚠️ | ⚠️ | ❌ |
| [G03](#g03) California | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ❌ |
| [G04](#g04) Epic Engineers | Mon Nov 30 | ✅ | ⚠️ | ≈ 33 | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 5 | ⚠️ | ⚠️ | ❌ |
| [G06](#g06) GapWise | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 6 | ⚠️ | ⚠️ | ⚠️ |
| [G07](#g07) Mighty Morphins | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Mon Dec 7 | ✅ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 11 | ⚠️ | ⚠️ | ⚠️ |
| [G10](#g10) Team Jiddak | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 11 | ⚠️ | ⚠️ | ⚠️ |
| [G11](#g11) 5 Guys | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ❌ |
| [G12](#g12) ACJMM | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ❌ |
| [G13](#g13) BYKX | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 8 | ⚠️ | ⚠️ | ❌ |
| [G14](#g14) G14 | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 11 | ⚠️ | ⚠️ | ❌ |
| [G15](#g15) HIBBI-01 | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 6 | ⚠️ | ⚠️ | ❌ |
| [G16](#g16) G16 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 25 | ⚠️ | ⚠️ | ⚠️ |
| [G17](#g17) G17 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 15 | ⚠️ | ⚠️ | ❌ |
| [G18](#g18) G18 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 8 | ⚠️ | ⚠️ | ⚠️ |
| [G19](#g19) G19 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 8 | ⚠️ | ⚠️ | ❌ |
| [G20](#g20) G20 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 12 | ⚠️ | ⚠️ | ⚠️ |

- **Rule 1 met:** 2 of 20 (G04, G08).
- **Whole paper §0–§8 complete:** 0 of 20 (none).
- **Past 50 pages:** 1 of 20 (G01).
- **Template text 〈…〉 still in the paper:** 16 of 20 (G02, G03, G04, G05, G06, G07, G09, G10, G11, G12, G14, G15, G17, G18, G19, G20).
- **Prototype complete, working and tested:** 0 of 20 (none).
- **Ready to present both today:** 0 of 20 (none).

**What changed since the last edition:**

- **The page moved to the Sprint 4 bar.** Rule 2 now covers the whole paper, §0–§8, and rule 3 the complete prototype. The four groups that had §0–§4 done on Nov 19 (G01, G08, G14, G16) keep those section marks; their rule 2 now reads partial because of §5–§8. Nothing in those repositories went backwards.
- **Length is the largest gap.** One paper (G01) is past 50 pages; 15 of the other 19 are at 12 pages or fewer. Most of the missing pages belong in §4: the specifications, the design sections and the implementation details, written as prose.
- **§5–§8 are the next gap.** 16 of 20 groups still have the template text in at least one of §5, §6 and §7. G01 and G08 are the furthest along: G01 has §5, §7 and §8 written and §6 needs hours and assumptions; G08 has §5 and §8 written and §6 and §7 are thin.
- **No prototype is complete yet.** Every group has a working slice or less; each card now names the stories that aren't built or tested.
- **Merged since Nov 19:** G01 (PRs #352, #367, #368, #370, #371, #378), G10 (PR #87, and `develop` CI is green), G11 (PR #92, which closed its open chain gap), G18 (PR #84).
- **New Sprint 4 work on the board:** G09 (issues #115, #117–#120, PRs #116 and #121 open). G03, G12 and G15 added a task or two. The other repositories did not change since the last edition.
- **Word export:** no group has the Nov 18 converter yet; see the check at the top of this page.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules and the Word export, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting (SNX-4)

*Pipeline that rebuilds Hyperliquid order books from SNX-4 data, validates them, and backtests strategies behind a gate.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 99), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge #376 and rewrite §1.2 as paragraphs, then add hours and assumptions to §6; these are the two thin sections for the Preview.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58 is dropped and has none). 29 open child issues have no Sprint milestone (#144, #145, #157, #158, #163, #164, #166, #287, #303-#324, #364); stories #23-#28 and #58 have none either; 88 typed refs sit in §1, §5 or §6 instead of §2/§4; `[task:#151]` is cited four times but #151 is a sub-task; About 33 tasks have no parent issue (recent: #271, #264, #249, #247, #232, #231); each belongs under a story; Ten PRs open on main (#356, #362, #363, #372-#377, #379): their issues stay open until merged; Old PRs without `Closes #N` (#126, #57, #38, #37, #29) and three early direct commits on main; every recent PR has one. |
| 2. Paper §0–§8 (`main`, ≈ 99 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ✅ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Link tables in place of prose: The §2 objective status table and the §5 deliverables table are maps beside real prose; they do not replace it. |
| 3. Prototype complete | ⚠️ partial | DuckDB storage, cleaning, `gate.py`, strategy metrics in `report.py`, a look-ahead refusal in `backtest.py`, and a React workspace shell. Replay and validation are stubs. Not built or not tested yet: Replay (#24), validation (#25), end-to-end run on a market-week, strategies and results (#28); the team moved this back-end work to CPSC 491 on Nov 18. CI: Main run 11/20 01:33 PST: green, both jobs. Prototype job ran Python install and pytest; Node steps skipped, so the front end is built only by `frontend.yml`. Tests: `test_storage.py`, `test_clean.py`, `test_gate.py`, `test_report.py`, `test_backtest.py`, `test_package.py`, plus `ResearchWorkspace.test.tsx` for the front end. |
| 4. Word export (`main`) | ⚠️ partial | 835 issue citation(s) become small in-text tags; 226 issue(s) fill 5 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ⚠️ partial | The paper is nearly whole but §1.2 and §6 are thin; the demo can show load, cleaning, gate and the workspace shell, not a rebuilt book. |

**Paper, what to write:** §1.2 Problem Statements on main is 223 words plus a table; PR #376 (why the problem is non-trivial) is open: merge it and write a paragraph per problem; §6 Project Timeline gives order of build and milestones for CPSC 491 but no estimated hours per task and no assumptions list; add both; §5 'What the prototype does today' still describes Nov 17 and a Vite starter page; PR #375 is open. Merge it after the demo path works; §7 AI Usage is detailed per artifact but gives no rough fraction of each artifact that was AI-assisted; add one per artifact; §4 is very long (about 35,000 words); remove repeated passages across specs, design and backtest design before the final paper.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #362, #363 (open, main): one clean week from S3; known market events check; PR #374, #375 (open, main): prototype README demo path; proposal §1.2, §4, §5 update; PR #376, #377 (open, main): why the problem is non-trivial; summary and conclusion of §6; PR #372, #373 (open, main): risks and lessons rewrite; evaluation plan and threats to validity; PR #356, #379 (open, main): timeline figure for §6; report load fixture.

**To do in Sprint 4:**

1. Merge #376 and rewrite §1.2 as one paragraph per problem, each ending with its issue refs, for the Preview (Sun Nov 29).
2. Add estimated hours per task and an assumptions paragraph to §6, and merge #356 and #377, for the Preview (Sun Nov 29).
3. Merge #362, #363 and #374, then make `prototype/README.md` show one command that cleans and gates the sample for the Dec 1 demo.
4. Update §5 'What the prototype does today' with merged #352, #368, #378 (PR #375) so it matches `main` before your presentation.
5. Put every child kept in Sprint 4 on the Sprint 4 milestone, give orphan tasks (#271, #264, #249, #247) a parent story, and fix `[task:#151]`.
6. Add a rough AI-assisted fraction per artifact to §7 and cut repeated passages in §4 before the final paper (Sun Dec 20).

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 15, about 35 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge #135 and write the Goal 1 spec (scope, FRs, NFRs, acceptance criteria, open questions) into §4; design and implementation text build on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); 10 stories (#49, #51-#55, #58-#61) have none. Ten of 15 user stories have no child issues; break each into feature, task, sub-task on the board; 21 tasks carry `sp:` under a story (double counting): #95, #92, #91, #86, #84, #81, #77, #69, #68, #41 ; Child issues #25, #18 and #17 have no assignee; six meeting issues (#101, #80, #79, #72, #70, #6) have no type label; #130, #99 and epic #20 are not linked from the proposal; epic and story refs sit in §3 and §4; Eight direct commits on develop and one on main; PRs #3, #4, #5, #14 lack `Closes #N`; PRs #135, #133, #127 open. |
| 2. Paper §0–§8 (`develop`, ≈ 15 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities · ⚠️ §5 Outcomes · ✅ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §7 (2). Link tables in place of prose: §2 uses bullets with refs; §4 'Specification and design documents' is a 3-row document table with no spec or design prose. |
| 3. Prototype complete | ⚠️ partial | FastAPI `/health`, `/health/db`, POST/GET `/observations` on PostgreSQL via Compose; Angular starter page; ESP32 `main.cpp` is a skeleton with no capture. Not built or not tested yet: Wi-Fi and Bluetooth capture (1.1, 1.2), identification, location, dashboard display and real-time updates (Goal 3); no ESP32 observation reaches the dashboard. CI: Develop run 11/17 18:41 PST green; Prototype job ran Python install and pytest on the backend. Angular and ESP32 projects are not built in CI; main run is older. Tests: `test_main.py`, `test_observations.py`, `test_observation_model.py` (in-memory SQLite); Angular `app.spec.ts` is not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 125 issue citation(s) become small in-text tags; 75 issue(s) fill 5 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 2 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Specs, implementation, AI usage and §5 are unwritten, and the demo would show only API storage; no capture or dashboard data yet. |

**Paper, what to write:** §4 Specifications: `docs/specs/` holds only the scaffold example. Write scope, FRs, NFRs, acceptance criteria and open questions for each of Goals 1-3 (PR #135 is open); §4 Design: `docs/design/architecture.md`, `data-flow.md`, `system-context.md` exist; add prose on components, data model, decisions, rejected alternatives, undesigned parts; §4 Implementation details is absent; describe the backend API, PostgreSQL tables, ESP32 firmware and dashboard as built, ending in task refs; §5 still holds a 〈Update this sentence…〉 placeholder; say what Prototype v0 does and how to run it. §7 AI Usage is the unfilled template; §1.2 Problem Statements is about 215 words with bullets; main still holds the unfilled §3 and §4 template, so merge develop (#133).

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop: §3, §4 environment and planned activities, observation API; merge into main; PR #133 (open, main): develop-to-main merge; get it reviewed and merged; PR #135 (open, develop): specs and design for issue #119; PR #127 (open, develop): restart-persistence check; review and merge or close; Branch feature/114-restart-persistence: 3 commits not in develop.

**To do in Sprint 4:**

1. Merge #135, then write one spec per epic in `docs/specs/` and summarize each in §4, for the Preview (Sun Nov 29).
2. Add §4 design prose from `docs/design/*.md`: data model, decisions with rejected alternatives, what is not designed yet, for the Preview (Sun Nov 29).
3. Write §4 Implementation details and fill the §5 placeholder and the §7 AI disclosure with tools, tasks, fractions and verification.
4. Get one ESP32 observation onto the dashboard through the API, with a test per acceptance criterion, before your presentation.
5. Create child issues for stories #49, #51-#55, #58-#61, remove `sp:` from the 21 tasks, and assign #25, #18, #17.
6. Link #130, #99 and #20 from the proposal and merge develop into main (#133) so the paper and code are on main.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Fix `prototype/README.md` so a fresh clone runs the transcriber-to-training pipeline; the demo on Dec 1 depends on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 13 stories have child issues; 8 stories (#30, #31, #33, #35, #36, #37, #45, #47) have none. Eight of 13 user stories have no child issues; break each into feature, task, sub-task on the board; 29 issues are not in the proposal (#87, #86, #84, #78, #72, #71, #70, #69 ...); 19 issues carry no type label; Open children #86, #85, #75, #71, #68, #53 have no assignee; #85, #75, #68, #53 and story #45 have no Sprint milestone; 22 non-story issues have no parent; PRs #81 and #77 lack `Closes #N`; PRs #88 and #83 are open; one direct commit on main and develop; Six epic and story refs in §2 are bare, and `[story:#31]` points at issue #30. |
| 2. Paper §0–§8 (`develop`, ≈ 9 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in the header block, §1, §4, §5, §6, §7, §8 (18). Link tables in place of prose: §2 is a bullet list with refs; §4 'Specification and design documents' and 'Planned activities' are small tables (one activity row), not prose. |
| 3. Prototype complete | ⚠️ partial | Transcriber with Mathpix recognizer and verifier, dataset generation, storage and display, PyTorch training, equation plotting, and a pipeline notebook. Not built or not tested yet: Code generation and round-trip check (no objective yet), relational database (#84), two-variable equations (#87, PR #88 open), raw human text input (#86), workbook output (Goal 4). CI: Develop run 11/9 21:27 PST green; Prototype job ran Python install and pytest on team code. Main run is older and green. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train and plot_equation tests; none for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 18 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §4 to §7 are template, and the README run steps do not work; the pipeline notebook runs from develop but Goals 2 to 4 are incomplete. |

**Paper, what to write:** §4 opens with the unfilled template prompt; write Environment and resources: each tool, platform, hosting and the sponsor's notebook requirement, with the reason; §4 Specifications: `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` are only indexed (the third is not listed); summarize each with FRs, NFRs, acceptance criteria; §4 Design and Implementation: one paragraph on `docs/design/architecture.md`; add data model, decisions with rejected alternatives, and the built transcriber, trainer and notebook; §5, §6 and §7 are the unfilled template; §6 needs CPSC 491 tasks with hours and assumptions, §7 tools, tasks, fractions and verification; §1.2 is a two-row table with a 〈…〉 placeholder; §1 is about 300 words; §8 lists 21 sources but still ends with the template note and has no in-text [n] cites.

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop: transcriber, recognizer, training, plotting, notebook, specs; merge into main; PR #83 (open, develop): plot test data, 3 commits; review and merge or close; PR #88 (open, develop): two-variable equations in training, 2 commits.

**To do in Sprint 4:**

1. Rewrite `prototype/README.md` with working install, run and test commands, and remove the course `login.py` text, before your presentation.
2. Replace the §4 template prompt with Environment prose, and summarize the three specs and `docs/design/architecture.md` in full, for the Preview (Sun Nov 29).
3. Write §4 Implementation and Planned activities in prose, ending each paragraph with typed issue refs; link #84, #86, #87 and the other 26 issues.
4. Fill §1.2, §5, §6 (CPSC 491 tasks, hours, assumptions) and §7 (tools, tasks, fractions, verification), and remove all 〈…〉 text.
5. Create child issues for the eight stories without breakdown with one assignee and a Sprint 4 milestone; type every issue.
6. Add tests for dataset generate, store and display, merge #83 and #88, and merge develop into main so the paper and code are on main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and trader profitability analytics

*Compute profit and loss per Polymarket wallet from SonarX Polygon data, rank traders, and show them on a dashboard.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 33, about 17 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Finish and merge #150 so §5, §6 and §7 stop being template text; these three sections are the largest gap for the Preview.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 12 of 12 stories have child issues (feature, task, sub-task); 11 stories still open. Five PRs (#150, #156, #158, #159, #160) are still open against develop; their issues cannot close until they merge; Eight feature branches (#55, #58, #59, #105, #125, #142, #149, dashboard-questions) have commits not in develop; 22 standalone writing and process tasks (#155, #154, #152, #149 ...) have no parent story; label them as writing tasks; PR #4 (Sprint 1 team README) has no `Closes #N`; no recent PR lacks one. |
| 2. Paper §0–§8 (`main`, ≈ 33 of 50+ pages) | ⚠️ partial | ⚠️ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §1.2 is a 6-row table with no prose; §1.1 is one paragraph plus a 6-row table. Specs, design and planned activities are prose with typed refs. |
| 3. Prototype complete | ⚠️ partial | Settings loader, Snowflake client, smoke query, FIFO position builder and resolution matching checked against the spec's worked example; no live-data run, ranking or dashboard. Not built or not tested yet: Read-only SQL extract (#105, PR #158 open), trader ranking and behavior (Goal 2), dashboard (Goal 3, spec PR #159 open); no end-to-end run on real rows. CI: Latest main run 11/9 15:28 PST green; Prototype job ran Python install and pytest. The live-Snowflake integration test is skipped without credentials. Tests: `tests/unit/` positions, resolutions, settings, snowflake_client; `tests/integration/test_smoke_query.py` (skipped); worked-example fixture. |
| 4. Word export (`main`) | ⚠️ partial | 119 issue citation(s) become small in-text tags; 105 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §7 are template and the prototype shows tested PNL logic on fixtures only: no live data, ranking or dashboard to demo. |

**Paper, what to write:** §5, §6 and §7 on main are still the unfilled template with 〈…〉 prompts; PR #150 and branch `149-proposal-sections-5-7` hold a draft that has not merged; §6 must plan CPSC 491: the Goal 1 to Goal 3 objectives as tasks with milestones, estimated hours, build order and assumptions; §4 Environment and resources is one paragraph; dashboard framework and result storage are not chosen. Add a subsection per tool with reasons; §0 Abstract is 148 words; §1.1 needs prose arguing what differs from each compared tool; §1.2 needs a paragraph per problem; §7 AI Usage must name tools, tasks, rough fraction of each artifact AI-assisted, and how the team verified it.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #158 (open, develop): read-only SQL extract module and tests; PR #159 (open, develop): Goal 3 dashboard specification; PR #156 (open, develop): dashboard questions update; PR #150 (open, develop): proposal §5 to §7 draft and stale §4 fixes; PR #160 (open, develop): final Sprint 3 review numbers.

**To do in Sprint 4:**

1. Merge #150 with §5 to §7 written in prose, and fill every 〈…〉 prompt, for the Preview (Sun Nov 29).
2. Write §6 as the CPSC 491 plan: objectives as tasks, milestones, hours per task, build order, assumptions.
3. Merge #158, then run the position builder on real SonarX rows end to end and demo one wallet's PNL at the presentation.
4. Build trader ranking (Goal 2) and one dashboard page (Goal 3) from the merged specs, with a test per acceptance criterion.
5. Expand §4 Environment into a subsection per tool with reasons, and rewrite §0, §1.1 and §1.2 as full paragraphs with citations matching §8.
6. Merge develop into main at the end of Sprint 4 (Mon Nov 30) and delete the eight stale feature branches.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, whale identification and location system

*Detect whale calls with an AI model and locate them from hydrophone recordings.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 5, about 45 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #72 and develop into main and fix the harness gate so main CI is green; then write §0 and §3.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 9 stories have child issues; #10-#13, #15, #16, #18 have none (tasks hang off epics #8 and #14). Seven of nine user stories have no child issues; tasks attach to epics instead of stories; 15 tasks are not linked from the proposal (#73, #71, #70, #69, #68, #67, #66, #65, #63, #61, #58, #57, #56, #47, #23); Open tasks #68, #67, #61, #57, #56 have no assignee; #71, #68, #61, #57 have no Sprint milestone; Epic and story citations sit in §4 instead of §2 only; 15 tasks have no parent issue; PRs #72 and #62 are open against develop; every merged PR has `Closes #N`. |
| 2. Paper §0–§8 (`develop`, ≈ 5 of 50+ pages) | ⚠️ partial | ❌ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ❌ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in the header block, §0, §3, §4, §5, §6, §7 (26). Link tables in place of prose: §4 'Planned activities' is an 18-row link table with about 224 words around it and no prose; the spec and design index is a table with a 〈template〉 row left. |
| 3. Prototype complete | ⚠️ partial | Locator: TDOA direction and distance from simulated hydrophones, 20-scenario direction check, interactive demo, call saving; detector train and detect scripts. Not built or not tested yet: Detector is not tested or tied to the locator; no database link or end-to-end run from recording to detected call to location; boat-noise story #12 and #11 open. CI: Develop run 11/9 23:51 PST green; Prototype job ran Python install and pytest. Main run 11/8 16:01 PST red: the Repository harness 'Run gates' step failed, though the prototype job passed. Tests: `tests/` test_tdoa, test_locate, test_save_call, test_speed_of_sound, test_scenarios (20 scenarios, 80% pass); `ai-detector/` scripts untested. |
| 4. Word export (`develop`) | ⚠️ partial | 48 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 26 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | The proposal still has a placeholder abstract and template §3, §4 and §5 to §7; the locator demo runs, the detector is untested and unconnected. |

**Paper, what to write:** §0 Abstract is a one-line placeholder; the front matter still has template placeholders for sponsor and date; §3 Proposed Approaches and §4 Environment are the template prompts; state strategy, alternatives, and each tool, dataset and hosting choice with its reason; §4 summarizes only the locator spec and design; summarize `goal-1-detector.md` and `ai-detector-design.md`, delete the placeholder row, add captioned diagrams and Implementation; §5, §6, §7 are the unfilled template; §6 needs the CPSC 491 plan with hours and assumptions, §7 tools, tasks, fractions and verification; §8 lists 2 sources, but §1.1 cites [1], [2], [3] with [2] and [3] being web pages that §8 does not hold; list every source, numbered in order cited.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #72 (open, develop): fills proposal §4, branch `fill-section-4-proposal.md`, 3 commits; PR #62 (open, develop): remerge main into develop (schema and ER diagram); Branch develop: scenario tests, direction demo, detector and locator design docs; main CI red.

**To do in Sprint 4:**

1. Merge PR #72 and #62, then merge develop into main and fix the failing harness gate so main CI is green.
2. Write §0 Abstract and §3 Proposed Approaches (strategy, alternatives, reasoning), and fill the front-matter placeholders, for the Preview (Sun Nov 29).
3. Write §4 Environment, summarize the detector spec and design, add captioned diagrams, and describe the built prototype in prose with issue refs.
4. Fill §5, §6 (CPSC 491 tasks, hours, assumptions) and §7 (tools, tasks, fractions, verification); rebuild §8 to match every citation.
5. Create child issues under stories #10-#13, #15, #16, #18; give #68, #67, #61, #57, #56 an assignee and Sprint 4 milestone; link the 15 tasks in §4.
6. Fix the `prototype/README.md` run commands, add detector tests, and connect detector output to the locator for the Dec 1 demo.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Turns a student's notes into practice questions and tracks per-concept mastery and forgetting to target weak spots.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 6, about 44 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §5, §6 and §7 in proposal.md on develop now: they are still template text, and the Preview on Sun Nov 29 needs every section drafted.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 17 stories have child issues; #14, #18, #19, #21, #28, #29, #31 have none (#5, #6 are old closed leftovers). Feature PRs close stories directly (#39 for #21, #53 for #18, #54 for #19, #56 for #29); no feature, task or sub-task between; Tasks #74-#77 (filed Nov 17) have no assignee and no Sprint milestone; none is linked in the proposal; Fourteen issues are not linked from the proposal, among them #43, #49, #51, #58, #60 and #73-#77; §4 Planned activities uses bare `#10`, `#36`, `#41` instead of typed refs; `[epic:#13]`, `#20`, `#27` are cited in §4; Stories #5 and #6 have no assignee; Sprint 3 milestone is past due with 6 issues still open. No Sprint 4 work is filed or merged yet. |
| 2. Paper §0–§8 (`develop`, ≈ 6 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §4 Environment is an 8-row table with reasons of a few words; Planned activities is an 8-row table of mostly finished items; specs are a list of links; Components, Data Model and Key Decisions are bullet lists. |
| 3. Prototype complete | ⚠️ partial | `run_demo.py` takes a notes file through document processing, concept extraction and question generation (template mode, no API key); other modules are not wired in. Not built or not tested yet: Flask web app, accounts, SQLite storage, mastery/selector/grader in the demo, live LLM mode, reminders UI, #31 user study, response-time check in practice. CI: develop run 11/16 19:48 PST green; Prototype job ran Install and test (Python) on team tests. main run 11/15 15:15 PST green but holds fewer modules. Tests: 11 team pytest files on develop (processor, concepts, questions, selector, mastery, forgetting, grader, override, summary, timer, exam calendar, demo); JS flashcards test not in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 27 issue citation(s) become small in-text tags; 24 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | A command-line demo runs from a fresh clone on develop, but §5-§7 are template text, §4 is thin, and the web app in the stories does not exist. |

**Paper, what to write:** §5, §6 and §7 still hold the template prompts and 〈…〉 placeholders (14 left); write all three, starting with §6 as the CPSC 491 plan with hours; §4 specs: `docs/specs/specs-epic-1.md` to `-3.md` (about 1,100-1,600 characters each) are only linked; summarize each in §4 and extend them; §4 design is bullets (about 430 words); `docs/design/gapwise-design.md` (8,800 characters) is not carried; write paragraphs with a rejected alternative per decision; No §4 implementation section: describe each prototype module, how it was tested, and what is not built (Flask app, SQLite, accounts, reminders); §1 (375 words), §1.2 (72 words) and §3 (165 words) are short for a 50-page paper; the two figures are hotlinked images that may not survive Word export; §8 has 3 sources.

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop: holds specs, design doc, §4 sections and newest features; main stopped at merge #63 on 11/15; branch 73-fill-proposal-5-6-7: 1 commit not in develop, aimed at §5-§7 (#73); merge it; branch 71-link-specs and feature/21-mastery-tracking: commits not in develop; merge or close; about 18 unmerged feature branches (flashcards, question-selector, assignment tracker): merge into develop or delete.

**To do in Sprint 4:**

1. Write §5, §6 and §7 in proposal.md (#73): outcomes naming repository, prototype and paper; a CPSC 491 plan with hours per §2 objective; an AI disclosure with fractions, for the Preview (Sun Nov 29).
2. Rewrite §4 Components, Data Model, Data Flow and Key Decisions as paragraphs ending in typed refs; add a rejected alternative for every decision.
3. Summarize `docs/specs/specs-epic-1.md` to `-3.md` and `docs/design/gapwise-design.md` inside §4: scope, requirements, acceptance criteria, open questions.
4. Create child issues under stories #14, #18, #19, #21, #28, #29, #31; give #74-#77 an assignee and Sprint 4 milestone; link them in §4.
5. Build the Flask and SQLite parts and wire `mastery_tracker`, `question_selector` and `grader` into the demo, with a test per acceptance criterion, before your presentation (Tue Dec 8).
6. Merge develop into main by PR with `Closes #N`, then add §4 implementation prose and expand §1, §1.2 and §3.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (EL-1)

*Extracts material data from vendor certificates and test reports, stores it after human review, and supports analysis.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Start the prototype now: one tested upload-to-review slice in `prototype/` with a real README, since none of the §2 stories has code today.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 16 of 16 stories have child issues; all stories have an assignee and a Sprint milestone. Seventeen features #151-#167 (children of stories #12-#19) have no assignee and are not linked from the proposal; Thirty-one issues are bare refs in the proposal, not typed refs (#28-#59 among them); §2 writes `story#48` and `story#49` without a colon; Nineteen story refs sit in §4; epics #1, #4, #45 are cited outside §2; wrong ref types include `[task:#78]`, `[bug:#117]`, `[task:#134]`-`[task:#136]`; Task #38 carries `sp: 3` under story #48; #28 has no Sprint milestone; #146-#149 have no assignee; Three direct commits on main; PRs #168, #145, #143, #140, #102, #99 are still open and eight branches are unmerged. |
| 2. Paper §0–§8 (`main`, ≈ 9 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in the header block, §5, §6, §7 (15). Link tables in place of prose: §4 Planned activities is a 76-row table (48 issue links) with no prose; the 12-row document table stands in for specification and design writing; Environment is a table with short purposes. |
| 3. Prototype complete | ⚠️ partial | Static HTML mock-ups, `prototype/index.html` and `ui-tabs/search-view.html` (PR #101); no back end, extraction, OCR or database code. Not built or not tested yet: Every story in §2: upload, Snowflake storage, extraction/OCR, review and approval, search, authentication, analysis; none has code or a test. CI: Main run 11/17 14:29 PST green; Prototype job ran Install and test (Python), but the only test is the course `tests/test_login.py`, so no team code was exercised. Tests: none for team code; only the course `tests/test_login.py`. |
| 4. Word export (`main`) | ⚠️ partial | 129 issue citation(s) become small in-text tags; 96 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 15 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only a static search page can be shown; §5-§7 are template text, §4 is mostly links and tables, and no team code runs or is tested. |

**Paper, what to write:** §5, §6 and §7 are still the template prompts with 〈…〉 placeholders (#146-#149 are open); §6 must be the CPSC 491 plan with hours, not this fall's sprints; §4 specs: the three goal specs in `docs/specs/` (5,600-6,400 characters each) are only linked; summarize each in §4 (PR #145 is open); §4 design: five figures, only Figure 3 has explaining prose; add components, data model, data flow, key decisions with rejected alternatives, from `technology-stack-decision.md`; §4 Environment needs a paragraph per choice (Snowflake, AWS, FastAPI, OCR tool) with the reason and rejected option (PR #143 and #140 are open); No implementation section; replace the 76-row table with prose. §1 (259 words) and §8 (4 sources) are short for a 50-page paper.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #145 (open, main): goal specification summaries added to the proposal; PR #168 (open, main): Review 3 write-up, closes #150; PR #143 and #140 (open, main): data-flow update and environment table; PR #99 and #102 (open, main): search-view and page-5 sequence diagrams; Eight unmerged branches, among them `proposal-environment-reasoning`, `update-data-flow`, `task/124-proposal-goal-spec-summary`.

**To do in Sprint 4:**

1. Merge PRs #145, #143 and #140, then confirm §4 carries each goal specification and the environment reasoning as prose, not links to `docs/specs/`.
2. Write §5, §6 and §7 for the Preview (Sun Nov 29): outcomes, a CPSC 491 plan with hours per objective, and an AI disclosure with fractions and verification.
3. Build one working slice (upload, extraction, review, Snowflake storage) in `prototype/`, replace the course `login.py` and `test_login.py`, and rewrite `prototype/README.md`.
4. Assign one person to each of features #151-#167 and tasks #146-#149, and link them in §4 with the correct typed refs.
5. Write §4 design as paragraphs: context, components, data model, data flow, key decisions with rejected alternatives, what is not designed yet.
6. Replace the Planned activities table with paragraphs, convert the 31 bare refs, fix `story#48`, `story#49`, move story refs out of §4, remove `sp:` from #38.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: interactive crime map and database

*Normalizes public Costa Mesa crime-call data into SQLite and shows it on a filterable Leaflet map.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build radius selection (#33, #34) into the Leaflet page with tests, so the Dec 8 demo shows the stories rather than only the marker map.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 8 of 8 stories have child tasks. Closed legacy issues #45-#47 (labelled duplicate), #6 and #7 are not in the proposal and have no Sprint milestone; Sprint 1 PRs #37, #39, #40 lack `Closes #N`; every later PR, including #94, has one; #27 (marker display and selection) is still open under the past-due Sprint 3 milestone; No direct commits, no `sp:` under a story, every linked child has an assignee and milestone. |
| 2. Paper §0–§8 (`develop`, ≈ 9 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ✅ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ✅ §8 References. Link tables in place of prose: none; §4 is prose with typed refs at the end of each part. |
| 3. Prototype complete | ⚠️ partial | Normalizes a Costa Mesa snapshot into SQLite, serves `/api/incidents`; Leaflet map shows 19 calls at 13 locations with a crime-type filter and marker highlight. Not built or not tested yet: Radius selection (#33, #34), combined filters (#30), marker selection #27, frequency charts and summaries (#19, #20) in the page; no tests for those criteria. CI: develop run 11/18 22:07 PST green; main run 11/17 19:49 PST green; the Prototype job ran Install and test (Python) on the team test files. Tests: `test_normalize.py`, `test_load_db.py`, `test_area_filter.py`, `test_crime_frequency.py`, `test_app.py` (map and incidents routes). |
| 4. Word export (`develop`) | ⚠️ partial | 47 issue citation(s) become small in-text tags; 47 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ⚠️ partial | The Flask and Leaflet map runs from a fresh clone with tests, but radius search, summaries and §6-§7 are unfinished, and the paper is far short of 50 pages. |

**Paper, what to write:** §6 is one paragraph with no tasks per objective, no hours and no dates ("pending team planning"); write the CPSC 491 plan: tasks #13-#22, milestones, hours, assumptions; §7 is a per-change log of ChatGPT drafting at about 100% and says the team "must" still verify; state tools, fractions per artifact, and how you verified; §1.1 (369 words) is a table plus two paragraphs; argue more fully what this project does differently, add sources to §8 (4 now). §1 and §1.2 are short; §4 Figure 3 (the ER diagram) is still only a link; embed it with a caption and a paragraph on the tables. Goal 1-3 specs lack non-functional requirements and open questions; §5 is one 83-word paragraph without the run commands; the paper is about 6,600 words, so every section must grow for a 50-page paper.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is one PR ahead of main: PR #94 route tests and the §4 test paragraph are not on main; branch 83-update-prototype-readme: 4 commits not in develop; merge or delete.

**To do in Sprint 4:**

1. Build radius selection (#33, #34) and the frequency summaries (#19, #20) into the map page, with a test per acceptance criterion, before your presentation (Tue Dec 8).
2. Finish #27 marker selection and the combined filters (#29-#31); update `prototype/README.md` so Status and What it proves match.
3. Write §6 as the CPSC 491 plan with tasks, milestones, hours and assumptions, and rewrite §7 as a verified disclosure, for the Preview (Sun Nov 29).
4. Expand §1, §1.1 (what Crime Busters does differently from existing maps), §1.2 and §5; embed Figure 3 (ER diagram) with a caption and prose.
5. Add non-functional requirements and open questions to each Goal 1-3 specification in §4.
6. Release `develop` to main by PR with `Closes #N`; close legacy #45-#47, #6, #7; delete branch 83-update-prototype-readme.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11, about 39 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge release PR #110 so main shows the working prototype, then build the dashboard alerts list (#117) the demo needs.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 10 of 10 stories have child issues (#37 gained #117 and #118, #38 gained #119). #80 (child of story #32) and #120 carry sp:; #57, #101, #111, #112, #115 carry sp: under pointed tasks; New tasks #115, #117-#120 and #112 are not linked in proposal §4; PRs #116 and #121 are open; #106 is closed with no Sprint milestone and is not linked in §4; #59 hangs off epic #28, not a story; Release PR #110 is still open, so main is scaffold; PR #20 (old draft) has no Closes line; every Sprint 3-4 PR has one. |
| 2. Paper §0–§8 (`develop`, ≈ 11 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6 (13). Link tables in place of prose: §4 Specification and design documents is a table that indexes eight docs without summarizing them; Planned activities is a 46-row issue-link table with one intro paragraph. |
| 3. Prototype complete | ⚠️ partial | Vehicle selection, service-record API and CRUD, manual entry and CSV import forms, dashboard with edit/delete, mileage entry, status-label recommendations for three service types. Not built or not tested yet: Dashboard alerts list Due Soon/Due Now (#117, #37), mileage window and miles remaining (#118), five-scenario end-to-end tests (#119, #38), typed UI tests (#91); `login.py` scaffold remains. CI: develop 11/19 00:48 PST green: the Prototype job ran Install and test for Node and Python, so API and UI tests executed. main 10/22 green but scaffold only. Tests: Seven pytest files (vehicle and service-record APIs, label, engine, interval) and seven `tests/ui/*.test.js` page tests; `smoke_test.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 58 issue citation(s) become small in-text tags; 58 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 13 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | The develop prototype runs with green CI and real tests, but alerts for #37 and the end-to-end suite for #38 are unbuilt, §5-§6 are template, and §4 is index-only. |

**Paper, what to write:** §5 and §6 are still template prompts with 〈…〉 placeholders (13 left); write §6 as the CPSC 491 plan with hours per objective, not this fall's sprints; Eight specs and design docs in `docs/specs/` and `docs/design/` (2,000-9,000 characters each) are only indexed; summarize scope, requirements, acceptance criteria, open questions in §4; §3 is about 190 words: add alternatives beyond rules versus AI (Flask versus other stacks, SQLite versus hosted, React) with reasons; §1.2 is 103 words; No §4 implementation prose: describe the service-record API, entry and import forms, dashboard, label rule and tests, ending in task refs; §7 is a real disclosure but gives one overall figure (10%); add fractions for the prototype code. The paper is about 7,000 words, far from 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #110 (open, develop to main): release of Sprint 2 and 3 work; main is still scaffold; PR #116 (open, develop): four-label sync and acceptance criteria for #34, #37, #38, closes #59, #115; PR #121 (open, develop): child tasks for #37 and #38, closes #120; PR #114 (open): course files; branches feature/98-sprint-3-review (8 commits) and feature/106-list-epic-27-spec: not in develop.

**To do in Sprint 4:**

1. Merge release PR #110 with CI green on main so the default branch shows the prototype and proposal.
2. Build the dashboard alerts (#117), the mileage window (#118) and the five-scenario end-to-end tests (#119), then finish #91, before your presentation (Tue Dec 8).
3. Write §5 and §6 for the Preview (Sun Nov 29): outcomes naming repository, prototype and paper, and a CPSC 491 plan with hours per objective.
4. Write the §4 implementation prose and summarize the five specs and `docs/design/architecture.md` in §4: requirements, acceptance criteria, decisions with rejected alternatives.
5. Remove sp: from #80, #120, #57, #101, #111, #112, #115; link #106, #112, #115, #117-#120 in §4; give #106 a Sprint milestone.
6. Expand §3 alternatives and §1.2 as paragraphs, replace the work-item table with prose, and add code fractions to §7.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11, about 39 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Fix the front matter and §5-§7 placeholders in proposal.md and the failing Run gates job on main; both block a clean hand-in.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 14 stories have child issues (#31, #32); #25-#30, #33, #38, #39, #53-#55 have none. Twelve stories have no child feature, task or sub-task; #33 hangs off task #46 and carries sp: 4; #56 carries sp: under pointed task #13; #38 is open with no assignee; #73 and #74 have no Sprint milestone; #3 is untyped; #88 and #83 are not linked in the proposal; #82, #74, #73 are bare refs; `[epic:#15]` is cited in §4, `[task:#69]` points to an epic; About 25 task refs count as outside §4, probably because the pasted `# Goal 1: Network Model` heading splits the outline; 14 direct commits on main from before the last review, including repo restructuring; none since; all 35 PRs close an issue. |
| 2. Paper §0–§8 (`develop`, ≈ 11 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in the header block (6). Link tables in place of prose: §4 Planned Activities (5 bullets) and Tracked Task Issues (29 bullets) are lists; Environment is bullets with one paragraph; §5 is a bullet list of deliverables. |
| 3. Prototype complete | ⚠️ partial | Goal 1 network model: transfer CSV to wallet graph, derived views, time-respecting cycles, metrics and reconciliation checks via `demo.py` on a synthetic sample. Not built or not tested yet: Goal 2 (heuristic and ML detectors, risk score, validation) and Goal 3 (dashboard, search, tracing); stories #25-#30, #38, #39, #53-#55, and #33 metrics (#88) unfinished. CI: develop 11/19 22:15 PST green (Prototype job ran Install and test (Python)); main 11/17 14:24 PST red on Repository harness (Run gates), Prototype job green. Tests: 31 tests in `tests/test_requirements.py` and `tests/test_acceptance.py` in the nested folder; whether CI collects them is not shown; plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 47 issue citation(s) become small in-text tags; 46 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 6 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | A tested Goal 1 demo runs from the command line, but Goals 2 and 3 and any UI are unbuilt, run steps are wrong, and §5-§7 carry template text. |

**Paper, what to write:** Front matter still holds 〈StableScope〉, 〈10〉, 〈Jiddak〉, 〈SNX-3〉 and a 〈2026-05-17〉 date; §7 keeps `[e.g., GitHub Copilot / ChatGPT]` and `[tool]` rows; §6 is this fall's sprints 1-6 (weeks 5-16): thin. Replace with the CPSC 491 plan: tasks = §2 objectives, milestones, hours, assumptions, in build order; §5 is a deliverables bullet list plus a stale "Prototype (starting Sprint 2)" section; write prose and say what the Goal 1 prototype demonstrates and how to run it; §4: Goal 1 spec is prose (1,158 words with design terms); Epics #23 and #24 specs lack requirements and acceptance criteria; five diagrams have one-line captions only; no implementation section; §1 (155 words) and §1.1 (two vendors, one citation) are short; §7 names one tool at 10%. The paper is about 7,000 words, far from 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is ahead of main: the new §4 spec prose (PR #87) and references [18]-[19] are not on main; main CI is red; branch feat/69-goal1-network-model-prototype: 2 commits not in develop.

**To do in Sprint 4:**

1. Replace every 〈…〉 in the front matter and the `[e.g.…]` rows in §7, then rewrite §5, §6 and §7 as prose for the Preview (Sun Nov 29); §6 is the CPSC 491 plan.
2. Fix the Run gates failure on main, release develop to main by PR, and stop direct commits to main.
3. Rewrite `prototype/README.md` and the nested README so run and test commands work from `prototype/goal1-network-model-prototype/`.
4. Build the Goal 2 detectors (#25, #26) and a minimal dashboard (#28) with a test per acceptance criterion before your presentation (Tue Dec 8); finish #88.
5. Create child issues under each remaining story (start with #25-#30, #33), one assignee and Sprint 4 milestone each; drop sp: from #56 and #33; remove the stray `# Goal 1` heading.
6. Write a §4 Implementation section for `stablescope/` and the 31 tests; finish the Epic #23 and #24 specs and explain each diagram in prose with rejected alternatives.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

*Phone app records a marathon runner's GPS to Firebase; spectators follow on a web page; pace and finish-time prediction.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build the spectator view (#69) so a phone's GPS position shows on a web page through Firestore; the demo needs it and three stories wait on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33); 49 of 51 issues linked from the proposal. New tasks #89 and #90 are not linked from `proposal/proposal.md` §4 and have no parent; PR #92 merged: #21, #1, #2, #6 are now cited; chain gap from Sprint 3 is closed; Open stories #28, #29, #30, #31, #33 and features #63, #68, #69, #71, #74 have no merged PR yet; `develop` exists but is stale (login scaffold); PRs #87, #92 merged straight into `main`; #91 closed unmerged; One old direct commit (`.github` scaffold) on main and develop; every PR closes an issue. |
| 2. Paper §0–§8 (`main`, ≈ 9 of 50+ pages) | ⚠️ partial | ⚠️ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in the header block, §1, §5, §6, §7, §8 (17). Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; only Goal 3 is summarized in prose. §2 is a bullet list of goals and objectives. |
| 3. Prototype complete | ⚠️ partial | Expo app with Firebase client, runner GPS tracking (`runner-app/tracking.js`), Firestore smoke test, pace calculation (`prediction/pace.py`). No spectator view, posts or route map. Not built or not tested yet: Spectator view (#69), posts (#63, #74), route map (#71), finish-time prediction (#68); stories #28-#31 and #33 not complete. CI: main CI green 11/19 (1658566); Prototype job ran Node install and test (jest) and Python install and test. develop green but only the login scaffold. Tests: 3 test files: `__tests__/App.test.js`, `__tests__/tracking.test.js` (jest), `prediction/test_pace.py`; no tests for posts or spectator. |
| 4. Word export (`main`) | ⚠️ partial | 55 issue citation(s) become small in-text tags; 50 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 17 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only the phone-GPS-to-Firestore and pace slice runs; spectator view, posts and prediction are unbuilt, and §5-§7 are template text. |

**Paper, what to write:** §0 Abstract describes an ML performance-analysis app; the goals are live tracking, posts and a spectator page. Rewrite it to match §2; §1 and §1.1 still hold template quote blocks and a 〈Your survey〉 placeholder; fix the duplicated table cell and typos; §5 Outcomes, §6 Timeline and §7 AI Usage are still template text and 〈…〉 placeholders. Write the CPSC 491 plan with hours per objective; §4 specs and design: only Goal 3 is in prose; carry Goals 1 and 2 specs, data model, decisions with rejected alternatives from `docs/`; §4 tech stack gives reasons but is not a titled Environment section; the Firebase setup text is a first-person how-to. The paper is about 4,600 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - stale login scaffold only; bring up to date with main (#89) or retire.

**To do in Sprint 4:**

1. Build the spectator view (#69) in `prototype/spectator-view/` so a runner position reaches a web page through Firestore, with a test per acceptance criterion, before your presentation.
2. Build posts (#63, #74), route map (#71) and finish-time prediction (#68); close each story with a merged PR that says `Closes #N`.
3. For the Preview (Sun Nov 29) write §5 Outcomes, §6 Timeline for CPSC 491 with hours per objective, and §7 AI Usage naming tools, tasks and fractions.
4. Rewrite §0 to match Goals 1-3; remove every quote block and 〈…〉 placeholder in §0-§8.
5. Carry the Goal 1 and Goal 2 specs, data model and architecture decisions with rejected alternatives from `docs/` into §4 prose; link #70 and #73.
6. Link #89 and #90 in §4, settle the `develop`/`main` stream, and refresh `prototype/README.md`.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Python app that finds signal peaks in 6G captures, classifies waveform and modulation, and explains the decision.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #167, then finish the waveform family gate (#142) and CLI integration (#161), because the demo needs one working end-to-end path.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 11 of 17 stories have child issues; #67, #69, #70, #71, #84, #95 have none. Stories #67, #69, #70, #71, #84, #95 have no child feature, task or sub-task; 26 issues are not in `proposal/proposal.md` on develop: tasks #147-#165, #168, #169 and stories #95, #163; #70 and #71 have no assignee or Sprint milestone; #103 is untyped with no assignee; §4 still cites stories (#68, #84, #111, #126) that belong only in §2; 14 misplaced refs; New task #168 has no parent story; PR #167 (closes #163) is still open; PRs #1, #2 are old and have no issue. |
| 2. Paper §0–§8 (`develop`, ≈ 9 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in the header block (3). Link tables in place of prose: §4 "Planned activities" is a 31-item bullet list of task links with no prose; §2 is a bullet list. |
| 3. Prototype complete | ⚠️ partial | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, Captum attribution, transformer AMC module. Not built or not tested yet: Waveform family gate (#142, #143), CLI wired to the full pipeline (#161), re-classifier stories #70, #71; channelizer not called by any entry point. CI: develop green 11/19 (3b7ee1b); Prototype job ran Install and test (Python) on team code. main is the 10-16 login scaffold, also green. Tests: 14 test files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, pipeline gate, OFDM, training, transformer. |
| 4. Word export (`develop`) | ⚠️ partial | 70 issue citation(s) become small in-text tags; 54 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 3 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Peak-picker and XAI demo runs from develop, but waveform identification and pipeline integration are unbuilt, and §4 Environment, Implementation, §6 are missing. |

**Paper, what to write:** §4 Environment and resources is still the template 〈…〉 placeholder; the opening paragraph names MATLAB only generally. Give each tool and dataset with the reason chosen; §4 specs: only the application architecture and waveform family specs exist for five epics; add scope, requirements, acceptance criteria for Goals 1, 4, 5; §4 has no implementation text for `waveform_identification/`, `xai/`, `GUI/`, `modulation_classification/`; write what each does, ending in task refs; §6 Timeline points to `docs/sprint-schedule.md` (this fall's sprints). Write the CPSC 491 plan: tasks per objective, hours, milestones, assumptions; §5 is a future-tense list; §7 names no fractions and omits prototype code. §1.1 lacks a pros-and-cons table; §1.2 is three sentences. About 4,400 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #167 (open, develop) - merges diagrams and design docs into `proposal/proposal.md` (closes #163); branch develop - real prototype and §4 work; main is the scaffold, release it at sprint end; branches Application-Structure, docs/team-documentation - commits not in develop.

**To do in Sprint 4:**

1. Merge PR #167 and finish #164, #165 so the specs and design from `docs/` are carried inside `proposal/proposal.md`.
2. Build the waveform family gate (#142, #143) and integrate the CLI with the analysis pipeline (#161); add one test per acceptance criterion before your presentation.
3. For the Preview (Sun Nov 29) replace the §4 Environment placeholder with each tool and why, and write §4 implementation prose for the four prototype packages.
4. Rewrite §6 as the CPSC 491 plan (tasks = §2 objectives, hours, milestones, assumptions); expand §5 and §7 with run steps and AI fractions.
5. Link tasks #147-#169 in §4 as typed refs, add children for stories #67, #69, #70, #71, #84, #95, and assign #70, #71 with a milestone.
6. Add specs for Goals 1, 4, 5 and a §1.1 pros-and-cons table; open the sprint-end develop-to-main PR.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8, about 42 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge the five open feature PRs, then rewrite `prototype/README.md` and rename the test file so CI exercises the app.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#19-#27 via features #53-#102 and tasks #55-#106). Only 8 of 84 linked issues are closed; tasks #56, #57, #61, #62 and feature #53 have open PRs #144, #145, #147, #148, #153; #93, #94, #124 and #47 have no Sprint milestone; #13 has no assignee or milestone; #139, #125 (3 assignees), #126, #124, #123, #122 (2), #111 and #107 (4) break one-assignee-per-issue; 19 issues are not in proposal.md, including #131, #124, #113, #107; refs like `taskL#127`, `[task:#139]` and #119's wrong URL are malformed; Merged PR #150 has no Closes; older PRs #1, #3, #4, #9, #36, #117 lack issues. |
| 2. Paper §0–§8 (`develop`, ≈ 8 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Link tables in place of prose: §4 Planned Activities is a 17-row issue table (16 link rows) with no prose; below it are 40 one-line task sentences, each just a ref. §1.1 is a table only. |
| 3. Prototype complete | ⚠️ partial | `A.M.I.Y.A.core/` has app, database, models, assignment and deadline services; the Electron/Vite UI has a task modal. Form, storage and edit PRs are unmerged. Not built or not tested yet: Nearly all of Goals 1-3: form validation, storage, edit/delete, suggested deadline UI, override, extension, progress slider, reminders (#53-#106 open). CI: develop green 11/16 (8be40c7), main green 11/14 (3c0d601); Prototype job ran only the Python step; the UI `package.json` is in a subfolder, so Node was skipped. Tests: One file, `A.M.I.Y.A.core/tests/TestAssignments.py`; its name does not match pytest discovery, so CI likely does not run it. |
| 4. Word export (`develop`) | ⚠️ partial | 102 issue citation(s) become small in-text tags; 84 issue(s) fill 5 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ❌ not ready | Prototype runs a thin core and UI shell; most stories are open, no run steps exist, and §6, §7 and §4 implementation are not written. |

**Paper, what to write:** §6 Timeline lists this fall's four sprints, which is the wrong content. Write the CPSC 491 plan: objectives as tasks, hours, build order, assumptions; §7 AI Usage says "None as of this moment." Disclose tools, tasks, fraction per artifact and how the team verified output; §1.1 has a pros-and-cons table but no prose on what A.M.I.Y.A. does differently; §1.2 is 68 words; only four references; §4 Environment gives no reason per tool and no data store; specs are three one-paragraph summaries linking `docs/specs/specs-G1.md` to `specs-G3.md`; §4 design is wireframes only: add system context, components, data model (`docs/design/ER_DIAGRAMS.md`), data flow, decisions; no Implementation section; §5 omits how to run.

**Merge first** (it doesn't count until it's in `develop` or `main`): PRs #144, #145, #147, #148 (open): form validation, local data, edit/delete, confirmation; PR #153 (open): assignment UI feature #53; branches task/111-specification-details, task/122-high-level-architecture-diagram: unmerged commits; PRs #134, #135 closed.

**To do in Sprint 4:**

1. Merge PRs #144, #145, #147, #148, #153 with `Closes #N`, then build storage, suggested deadline, progress slider and reminders, one story at a time.
2. Rewrite `prototype/README.md` with install, run and test commands for the core and the UI before your presentation.
3. Rename `TestAssignments.py` to `test_assignments.py` and add one test per acceptance criterion in `docs/specs/specs-G1.md` through `specs-G3.md`.
4. For the Preview (Sun Nov 29) rewrite §6 as the CPSC 491 plan and §7 as a real AI disclosure; expand §1.1 and §1.2 into prose.
5. Write §4 Environment with a reason per tool, an Implementation section, and carry specs and ER design into §4 prose.
6. Add Sprint milestones to #93, #94, #124, one assignee per issue, and fix the malformed refs in the Planned Activities table.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · G14: Cyber Sandbox (Cyber Squad)

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11, about 39 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §5, §6 and §7 in `proposal/proposal.md` for the Sun Nov 29 Preview, since they are still template text.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 18 of 18 stories have child issues (feature, task, sub-task); epics #22 and #23 sit above them. About 40 Sprint 4 children (#136-#175, minus #140) plus #114, #115 have no Sprint milestone; `sp:` remains on #99, a task under story #25; points belong on the story only; #88 and #92 have no assignee; #79, #80, #81, #44 and #45 have several; New Sprint 4 meeting #177 is not in the proposal and has no assignee; #91 and #92 are cited as plain links, not typed refs; Of the Sprint 4 children #136-#175 none is closed; only #126, #129, #130 (PRs #127, #131) are done, and #115 is still open; PR #50 (Goal 2 spec) has no issue; §4 cites story #24 and §1 cites task #113. |
| 2. Paper §0–§8 (`develop`, ≈ 11 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §4 "Specification and design documents" opens with an 11-row link table, but each document then gets a prose summary; planned activities are prose paragraphs with refs. |
| 3. Prototype complete | ⚠️ partial | PySide6 start menu loads a sample or JSON scenario validated by Pydantic; user browses, creates and deletes simulated files in memory; optional Ollama generator script. Not built or not tested yet: Process manager, log and network viewers, malware behaviors, response and lifecycle controls, scenario configuration, NRP.ai integration, action log, report, hints (#139-#175). CI: main green 11/12 (ec16018), develop green 11/12 (2a0c3b8); Prototype job ran Install and test (Python) on team code, and CI fails if no tests are collected. Tests: 5 test files in `prototype/tests/`: scenario model, loader, simulation engine, scenario generator, UI (Qt offscreen); none for unbuilt stories. |
| 4. Word export (`develop`) | ⚠️ partial | 176 issue citation(s) become small in-text tags; 119 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only the file view and JSON loader work; most of the 18 stories are unbuilt and §5-§7 are template text, so neither paper nor prototype is complete. |

**Paper, what to write:** §5 Outcomes is still the template quote and 〈…〉 placeholder. Write two paragraphs naming repository, prototype and paper, what it demonstrates and how to run it; §6 Timeline is template text and an empty 〈…〉 table. Write the CPSC 491 plan: objectives as tasks, hours, milestones, build order, assumptions; §7 AI Usage is the template placeholder. Disclose tools, tasks, fraction per artifact (proposal, diagrams, code) and how you verified output; §3 still says 'Sprint 2 priorities'; rewrite it to match the prototype. §1.2 has spelling errors; §2 is a 20-line bullet list; §4 implementation covers `ui/`, `sim/`, `scenario/`; extend as process, log and network views and AI generation land. §8 has five sources, all competitor sites.

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - holds the fuller proposal (57k characters vs 50k on main); release it to main at sprint end.

**To do in Sprint 4:**

1. Build the simulated process manager, log viewer and network viewer (#139, #143, #105 design) with a test per acceptance criterion before your presentation.
2. Implement malware behaviors, response controls and scenario lifecycle (#146, #149, #152), then scenario configuration, NRP.ai adapter, action log and report (#155-#167).
3. For the Preview (Sun Nov 29) write §5 Outcomes, §6 Timeline for CPSC 491 with hours per objective, and §7 AI Usage with tools, tasks and fractions.
4. Add a Sprint milestone to the Sprint 4 children (#136-#175) and #114, #115; give #88 and #92 one owner; remove `sp:` from #99.
5. Rewrite §3 (still 'Sprint 2 priorities') to match the prototype; proofread §1.2; turn §2 bullets into sentences.
6. Link #177 as a typed ref in §4, and open a PR with `Closes #N` for every proposal edit.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 6, about 44 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build a first playable slice of the game demo (enemies, #26) in `prototype/`, since the demo and four stories have no code yet.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 8 stories have child issues (#30, #31, #32, #33); #26-#29 have none. Stories #26, #27, #28, #29 (game demo) have no child feature, task or sub-task; `proposal/proposal.md` has 0 typed refs: bare `#N` cells and untyped `[story:https://...]` parents in the §4 table; #46 is parented to story #32 yet carries `sp: 2`; its table row names itself as its own parent; #76, #78, #82, #84, #43 and epic #6 are not in the proposal; #43 has no milestone; #44 has no assignee; New task #84 has parent #83, a merged PR, not a story; PR #85 (develop) is open; Stories #26-#30, #32, #33 each have 2 assignees; one assignee per issue. |
| 2. Paper §0–§8 (`main`, ≈ 6 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; "Planned activities" is a 38-row table with no prose; §1.2 and §2 are a table and a bullet list. |
| 3. Prototype complete | ⚠️ partial | CMake project (SDL3, Assimp, ImGui, GLM) with ECS core, transform and mesh components, renderer and model loader headers, shaders; README gives build, run, test commands. Not built or not tested yet: Game demo stories #26-#29 (enemies, gameplay loop, input, building), multiplatform proof (#31), adaptable renderer (#32), editor beyond import (#33, #84). CI: main green 11/13 (43fce39), develop green 11/13 (c80ac06); Prototype job detected CMake, installed graphics libraries, configured, built C++ and ran Tests (CMake). Tests: README names target `test_engine_components` (basic ECS checks); test sources not visible in the sweep's file list. |
| 4. Word export (`main`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 25 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | The engine builds and a basic ECS test passes, but no game demo exists, and §4 design, implementation and §5-§7 are unwritten. |

**Paper, what to write:** §5 Outcomes, §6 Timeline and §7 AI Usage are still the template quote blocks and 〈…〉 placeholders; write all three, with the CPSC 491 plan and hours; §4 specs: summarize `docs/specs/game-engine.md` and `game-demo.md` in prose (scope, FR/NFR, acceptance criteria, open questions); today only file names appear; §4 design: write components, ECS data model, data flow, decisions with rejected alternatives, undesigned parts from `docs/design/architecture.md`; §4 environment is one line per tool; Figures 1 and 2 have captions but no paragraph explaining them; no implementation section for `include/engine/` and `demo/`; §8 has four bare URLs with no author or title, and the [2]-[4] numbers in §1.1 do not match the table. The paper is about 2,900 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #85 (open, develop) - target entity ID and manipulate menu for the editor (#84); branch 33-objective-24-implement-visual-editor-...: 2 commits not in develop; branch task/84-Mesh-Manipulation: 1 commit not in develop.

**To do in Sprint 4:**

1. Build the game demo stories #26-#29 (3 enemies, gameplay loop, input, building) in `prototype/include/demo/`, with a test per acceptance criterion before your presentation.
2. For the Preview (Sun Nov 29) write §5 Outcomes, §6 Timeline for CPSC 491 (objectives, hours, milestones, assumptions) and §7 AI Usage with tools, tasks and fractions.
3. Write §4 Specifications and Design as prose from `docs/specs/game-engine.md`, `game-demo.md` and `docs/design/architecture.md`, with decisions and rejected alternatives.
4. Add a §4 Implementation section on what the CMake prototype builds and tests, citing #63, #66, #67, #82; explain Figures 1 and 2 in prose.
5. Create child issues under stories #26-#29, remove `sp:` from #46, re-parent #84 to #33, and rewrite the §4 table with typed refs including #76, #78, #82, #84.
6. Merge PR #85 and the #33 and #84 branches with `Closes #N`; fix the 〈…〉 title and complete the four §8 entries.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Monitors cross-chain bridge vaults, learns normal outflow, and alerts on drains with measured false alarms.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 25, about 25 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write a test in `prototype/tests/` for each acceptance criterion of #17, #18 and #20, so the prototype is proven before the Dec 10 demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#14, #15, #17, #18, #20); #19, #21 (Sprint 4) and closed #5, #16 have none. Stories #19 and #21, both open in Sprint 4, have no child issues yet; Task #107 has no assignee and no parent story; task #28 has no parent story either; PRs #75 and #35 have no `Closes #N`, both closed and old; recent PRs all close an issue; Closed stories #5 and #16 have no child issues. |
| 2. Paper §0–§8 (`develop`, ≈ 25 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ❌ §8 References. Link tables in place of prose: Table 9 indexes the specs and design doc and Table 11 is the CPSC 491 schedule; each is backed by prose, so no section depends on a table alone. |
| 3. Prototype complete | ⚠️ partial | Detector, SQLite store, live Ethereum poller, five-hack replay, false-alarm evaluation, Slack notifier, FastAPI API, web dashboard, demo mode. Not built or not tested yet: SonarX source (#100, #14) not built; user test (#21) and stretch #19 not started; replay met target on 3 of 5 hacks. CI: main 93cd0c2 and develop 3463b50 green (11/18 PST); Prototype job ran Install and test (Python), so the team tests executed. Tests: Four files in `prototype/tests/` (detector, live loop, baseline check, data pipeline); proposal reports sixty tests. |
| 4. Word export (`develop`) | ⚠️ partial | 78 issue citation(s) become small in-text tags; 50 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ⚠️ partial | Prototype runs in demo, live and replay modes on green CI, but SonarX source and user test are unbuilt and §7 and paper length need work. |

**Paper, what to write:** §7 AI Usage names tasks and review but gives no approximate AI-assisted fraction per artifact; add one per paper section, prototype code, and docs; Whole paper is about 12,500 words, §4 about 7,500; well short of 50 pages, so expand §1, §3, §4 planned activities and results; §4 Planned activities should describe the Sprint 4 work (#100, #19, #21) in prose ending in typed refs; §5 should add the final results (replay misses for Harmony and Ronin, false-alarm rate) once Sprint 4 lands; §8 order of first citation needs a check.

**Merge first** (it doesn't count until it's in `develop` or `main`): branch 93-cpsc491-timeline: 13 commits not in develop; §6 already merged via #110, so merge by PR or delete.

**To do in Sprint 4:**

1. Create child tasks under stories #19 and #21 now, each with one assignee, a Sprint 4 milestone and no `sp:`.
2. Assign #107 and put #107 and #28 under a story so every issue sits in the chain.
3. Write a test in `prototype/tests/` for each acceptance criterion of Objectives 2.2, 2.3 and 3.1, and fix the Harmony and Ronin replay misses (#97).
4. Build the SonarX source (#100) or state in §5 and §6 that the demo runs on public Ethereum data.
5. Add AI-assisted fractions per artifact to §7, and extend §4 Planned activities, §1 and §3 for the Preview (Sun Nov 29).
6. Merge or delete `93-cpsc491-timeline`, and keep develop to main as one release at the end of Sprint 4 (Wed Dec 9).

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 15, about 35 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Replace the template text in §5 to §8 of `proposal/proposal.md` with real content, starting with §6 hours per objective for CPSC 491, for the Preview (Sun Nov 29).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 6 stories have child issues (#25, #27, #29, #30); #26 and #28 have none (tasks #46, #47, #53 hang off epic #21). `sp:` on 11 child tasks under stories or pointed tasks (#41-#43, #49, #51, #55, #57-#59, #65, #68); #41, #49, #51, #55, #57-#59, #62-#64 are not linked from the proposal; 9 of 18 linked refs are untyped; #49 and #55 have no assignee; #63 and #64 have no parent; #64 has no type label; 18 merged PRs lack `Closes #N`, including recent #75 and #67; main has 32 direct commits; Stories #29 and #30 are still open although login PRs #69 and #70 merged; Sprint 2 holds 2 open issues. |
| 2. Paper §0–§8 (`main`, ≈ 15 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ❌ §8 References. Template text 〈…〉 still in §5, §6, §7, §8 (15). Link tables in place of prose: §1.1 and §1.2 are tables, §2 is nine bullets, the spec and design index is a link table, and Planned activities is a 7-row table with no prose. |
| 3. Prototype complete | ⚠️ partial | Arcade login and preferences screens (#62), swipe on the main screen (#72), SQLite `db.py` and `schema.sql` (#64), Last.fm client; not shown wired end to end. Not built or not tested yet: Galaxy map, recommendations (#26, #28), persisted swipe history and restore on sign-in (#30); no test for any acceptance criterion. CI: main c2f301d (11/18 PST) green; Prototype job ran Install and test (Python), but no `prototype/tests/` exists, so CI tests no team code. No develop branch. Tests: none; no `prototype/tests/` folder although the README claims four tests. |
| 4. Word export (`main`) | ⚠️ partial | 16 issue citation(s) become small in-text tags; 16 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 15 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §8 are template text, the paper is far from 50 pages, and the prototype has screens and a database but no end-to-end flow or tests. |

**Paper, what to write:** §5 Project Outcomes, §6 Project Timeline, §7 AI Usage and §8 References still hold the template text; write all four, with CPSC 491 hours in §6; §1.1 is a four-row table with no prose and no citations; §8 has only the template examples. Add paragraphs arguing the difference, cited [1] onward; §1.2 is a table and §2 is bullets; write the problem statements and each epic and story as paragraphs ending in typed refs; §4 has no implementation details; describe `prototype/src/sonicscape` (screens, swipe, `db.py`, `lastfm.py`) with task refs; Whole paper is about 7,500 words; far short of 50 pages. Planned activities needs Sprint 3 and 4 work in prose.

**To do in Sprint 4:**

1. Write §5 Outcomes, §6 CPSC 491 Timeline with hours, §7 AI Usage with fractions and §8 References for the Preview (Sun Nov 29).
2. Rewrite §1.1, §1.2 and §2 as prose ending in typed refs, and cite sources numbered from [1] in §8.
3. Build the galaxy map and recommendations (#26, #28), then connect login, map, swipe and `db.py` so one run works end to end.
4. Add `prototype/tests/` with a test per acceptance criterion and fix the README run and test sections.
5. Remove `sp:` from child tasks, assign #49 and #55, link the ten unlinked issues in §4 as typed refs, parent #63 and #64.
6. Add Implementation details and Sprint 3 and 4 planned activities in prose to §4, and export the Mermaid figures as images.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: Project Rogue, 2D action roguelite with flexible builds (Unity)

*A Unity 2D action roguelite where builds develop through weapons, attributes and branching three-Act runs.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8, about 42 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #85, then write §6 to §8 of `proposal/proposal.md` on develop so the Preview (Sun Nov 29) has every section drafted.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32 via #72, #35 via #64, #41 via #48); #33, #34, #36-#40 have none. #64 (under story #35), #65, #56 and #53 carry `sp:`; points belong on the story only; #74 and #58 have no Sprint milestone; #26 and #13 are untyped with no milestone; #79, #76, #74, #72, #65, #64, #61, #58, #56, #53 are not linked from proposal.md; Epics #29-#31 are cited in §1 and story #41 in §4; epics and stories belong in §2 only; Tasks #79, #76, #74, #60, #59, #58, #51, #49, #47 have no parent; PR #85 for #79 still open. |
| 2. Paper §0–§8 (`develop`, ≈ 8 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ❌ §8 References. Template text 〈…〉 still in §6, §7, §8 (14). Link tables in place of prose: §4 Specification and design documents is a 5-row link table; Planned activities is a 28-row issue table with only four short paragraphs. |
| 3. Prototype complete | ⚠️ partial | Unity 6 project on develop: combat demo, movement and traversal room, starting classes (#81), five room scenes (#83), run/node/reward progression (#84); title and pause flow in open PR #85. Not built or not tested yet: Enemies and encounters (#38), branching three-Act map (#39), playtests (#41), title/pause/retry (#79, PR #85 open); no automated tests. CI: develop f612687 (11/19 PST) and main d6e8c9a (11/4 PST) green; Prototype job ran only Install and test (Python) on the scaffold, so no Unity code was compiled or tested. Tests: No automated tests; `Assets/Editor/ClassVerification.cs` and `ProgressionVerification.cs` and the `Test_Combat` scene serve as manual checks. |
| 4. Word export (`develop`) | ⚠️ partial | 54 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | Combat, classes, rooms and run progression run from develop, but §6 to §8 are template, §4 lacks specs and design prose, and enemies and map are unbuilt. |

**Paper, what to write:** §6 Project Timeline, §7 AI Usage and §8 References are template text on both branches; write the CPSC 491 plan with hours, a real disclosure, and the cited sources; §4 Specifications: summarize the three goal specs in `docs/specs/` per epic with requirements and acceptance criteria; §4 Design: carry `system-overview.md` in; §4 Implementation: describe what `prototype/ProjectRogue` implements (combat, classes, traversal, rooms, run progression) with task refs; §5 still cites only PRs #44 and #45; update it for classes (#81), rooms (#83) and run progression (#84); Paper is about 4,000 words on develop and main still has the template §3 and §4; far short of 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #85 - title, pause and retry flow for #79, open against develop; branch feature/40-node-reward-run-progression: 2 commits not in develop after #84; check and delete; develop to main - §3 text, classes, rooms and run progression; main last changed 11/4 PST.

**To do in Sprint 4:**

1. Write §6 CPSC 491 Timeline with hours per objective, §7 AI Usage with fractions and §8 References for the Preview (Sun Nov 29).
2. Merge PR #85, then build enemies and encounters (#38) and the branching three-Act map (#39) so a full run plays.
3. Add edit-mode tests for the resolver, classes and progression, and a CI step that runs them; record manual results in `prototype/README.md`.
4. Summarize the three goal specs per epic and `system-overview.md` in §4, embed the missing diagrams, and add an Implementation subsection.
5. Update §5 for #81, #83, #84; align §2 and §3 on classes versus weapon-and-element builds.
6. Create sub-issues for #33, #34, #36-#40, remove `sp:` from #64, #65, #56, #53, milestone #74 and #58, then merge develop into main at the end of Sprint 4.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · G19: Titan Security, Radar over WiFi drone detection (RTX-2)

*Detect small drones and estimate position and movement from Wi-Fi CSI, compared against conventional radar.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8, about 42 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #104, then write §5, §6 and §7 in `proposal/proposal.md` on develop, replacing every 〈…〉 block, for the Preview (Sun Nov 29).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 13 of 13 stories have child issues, but 8 children (#77-#84) have no type, assignee or Sprint milestone. #77-#84 are untyped, have no assignee or Sprint milestone, and none is linked from proposal.md; #99 is labelled user-story and task, carries `sp:` under story #97, and is cited as a task; 18 issues are not linked from §4, including #101, #98, #93, #75, #71, #53 and #43; #86 and #91 are tasks with no parent; #93 has no Sprint milestone; story #73 has no `sp:`; The §4 work-item table cites stories #6, #7, #13-#17; stories belong in §2 only; Sprint 3 (due 11/18) has 8 open and 4 closed issues; PR #104 is open. |
| 2. Paper §0–§8 (`develop`, ≈ 8 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in §4, §5, §6, §7 (20). Link tables in place of prose: §4.3 is a link table with a leftover template placeholder block and no per-epic spec summaries; §4.4 is a 15-row table, with the prose in §4.5. |
| 3. Prototype complete | ⚠️ partial | CSI capture and quality-check scripts with a sample recording, preliminary feature extraction and event analysis (`features.py`, `event_analysis.py`, PR #102); scaffold `login.py` remains. Not built or not tested yet: Labeled datasets (#14), drone classifier (#15), distance tests (#16), radar comparison (#17); no detection slice and no tests for them. CI: develop 484bafe (11/18 PST) green; Install and test (Python) ran, but the only test is the course `test_login.py`, so no team code is tested. main 7fca571 (11/5 PST) is older. Tests: Only the course `prototype/tests/test_login.py`; nothing tests capture, quality check, features or event analysis. |
| 4. Word export (`develop`) | ⚠️ partial | 46 issue citation(s) become small in-text tags; 37 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 20 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §7 are template, §4 lacks specs and implementation prose, and the prototype has capture and offline analysis but no detector and no team tests. |

**Paper, what to write:** §5 Project Outcomes, §6 Project Timeline and §7 AI Usage are template text; write all three, with CPSC 491 hours per objective in §6; §8 carries a "retained from the draft, requires verification" banner and a TO CONFIRM line; verify each source and remove both; §4.3: delete the two placeholder rows, summarize `wifi-csi-sensing.md`, `drone-detection.md`, `evaluation.md` per epic (PR #104 open); §4: add the data model, key decisions with rejected alternatives, and what is not designed; add an Implementation section for `capture.py`, `features.py`, `event_analysis.py`; Resolve the draft-status banner and the TO CONFIRM in §1.1 (name the conventional radar systems); paper is about 3,700 words, far short of 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #104 - epic spec summaries and design narrative for #97, open against develop; develop to main - main last changed 11/5 PST and lacks all Sprint 3 work; branch feature/97-Documentation_for_project_proposal_enviornment: 1 commit not in develop.

**To do in Sprint 4:**

1. Merge PR #104 and write §5 Outcomes, §6 CPSC 491 Timeline with hours, and §7 AI Usage with fractions for the Preview (Sun Nov 29).
2. Collect labeled datasets (#14) and train the drone classifier (#15), then add pytest tests for capture, quality check, features and detection.
3. Replace `login.py` and `test_login.py`, and rewrite `prototype/README.md` run steps and the Sprint 3 row.
4. Type, assign and milestone #77-#84, link every child in §4 as a typed ref, fix #99, parent #86 and #91.
5. Delete §4.3 placeholders and the draft banner, add data model, decisions and Implementation to §4, and verify §8 sources.
6. Release develop to main by one PR at the end of Sprint 4 (Wed Dec 9) and stop merging features into main.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · G20: Solos, Insomnia, first-person horror maze game in Unreal Engine

*Unreal Engine 5 first-person horror maze game with adaptive monsters, encounter director and responsive atmosphere.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 12, about 38 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §6 of `proposal/proposal.md` (hours per objective for CPSC 491), then §5, §7 and §8, replacing the template text, for the Preview (Sun Nov 29).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child issues (#13, #14, #15, #18, #19, #20, #22, #23). Only 11 refs are typed; 39 of 51 issue refs are bare `#N` or `Task `[#N]` links, mostly in §4; Tasks #64-#68, #76-#78 and #91 are standalone with `sp:` and no parent story or epic; Sprint 3 (due 11/18) has 19 open and 17 closed issues; stories #14, #15, #18-#20, #22, #23 are open; Epics #12, #17, #21 sit in Sprint 4 while their stories sit in Sprint 3; The §4 table lists #41 under Type 'Task' but cites it as 'Feature'; fix the Type column. |
| 2. Paper §0–§8 (`develop`, ≈ 12 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ❌ §8 References. Template text 〈…〉 still in §1, §3, §5, §6, §7, §8 (18). Link tables in place of prose: The spec and design index and the 41-row work-item table are tables, but each follows real prose; no section relies on a link table alone. |
| 3. Prototype complete | ⚠️ partial | Unreal Engine 5 project with sprint and crouch movement (#40), prototype maze (#71), objective tracker (#42), a chasing enemy (#48) and hide evasion (#73). Not built or not tested yet: Maze variation (#72), director and monster perception (#44, #45, #50-#52), game over (#49), flashlight (#39), reactive events (#74), audio (#75); nothing tested. CI: develop c686eb8 and main 8f44220 (11/18 PST) green, but the Prototype job ran only "Nothing to build", so CI did not exercise the Unreal project. Tests: None automated; manual tests are recorded in PR descriptions, and the README smoke test covers only the starter level. |
| 4. Word export (`develop`) | ⚠️ partial | 61 issue citation(s) become small in-text tags; 51 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 18 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | A maze with movement, objective and chasing enemy can be shown, but most stories are unbuilt, no tests exist, and §5 to §8 are template. |

**Paper, what to write:** §5 Project Outcomes, §6 Project Timeline, §7 AI Usage and §8 References are template or empty on both branches; write all four, with hours in §6; §1.1 compares three games in short pros and cons and calls Insomnia a haunted-house game while §0 and §2 describe a maze; align it, cite [1]-[3] in text, move them to §8; Template text remains: quote blocks and the "Keep the details out" note in §3, an empty table header in §4, and 〈〉 cells in the §1.2 table; §4 Specifications: each summary is one paragraph; add numbered functional and non-functional requirements and acceptance criteria per epic; Paper is about 6,800 words; far short of 50 pages. Expand §1, §1.1, §3 and the implementation and verification prose as features land.

**To do in Sprint 4:**

1. Write §5 Outcomes, §6 CPSC 491 Timeline with hours, §7 AI Usage with fractions and §8 References for the Preview (Sun Nov 29).
2. Build the open Sprint 3 features first: perception (#44, #45), director (#50, #51), game over (#49), maze variation (#72), then audio and events (#74, #75).
3. Update `prototype/README.md` for the maze level and controls, with a written manual test and result per acceptance criterion.
4. Rewrite the §4 work-item table and every `#N` in §4 prose as typed refs such as `feature:#40` and `task:#41`.
5. Parent #64-#68, #76-#78 and #91 under an epic or story, and move unfinished Sprint 3 issues to Sprint 4.
6. Delete the §3, §4 and §1.2 template text, align §1.1 with the maze concept, and add requirements per epic to the specs.

[↑ Back to all groups](#groups)

## About this page

This page checked Sprint 3 readiness (proposal §0–§4 and one working slice) from Nov 8 to Nov 19; those editions, and the Sprint 2 cards before them, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
