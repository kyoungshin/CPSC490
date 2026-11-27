# Group repository status: Sprint 4 readiness (the whole paper, §0–§8, and a fully functional prototype)

## Word export check (Nov 27): fix these in `proposal.md`

You submit the Preview (Sun Nov 29) and the Final (Sun Dec 20) as Word files made from `proposal/proposal.md`. I converted every group's `proposal.md` (both `main` and `develop`) with pandoc and the course converter, using the command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). All 20 convert without errors. The table below lists what still comes out wrong in Word, on the branch with your fuller proposal.

**Everyone: copy the updated converter first. As of Nov 27, four groups have it: G03, G06, G09 and G16.** Since Nov 18, [`proposal/to-word.lua`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/to-word.lua) scales every picture to fit the page: at most 6.5 in wide and 8.5 in tall, aspect ratio kept. With an older copy, a tall diagram runs off the bottom of the page. Copy it, and [`proposal/reference.docx`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/reference.docx), into your `proposal/` folder, replacing your old copies. Then run the README command again.

**〈placeholders〉:** the converter warns about any 〈…〉 left outside the guidance quotes, and Word prints it as typed. Sprint 4 finishes the whole paper, so none may remain: draft §5–§8 for the Preview and clear every one before the Final.

| Group | Branch | Converter in your repo | What comes out wrong in Word |
|---|---|---|---|
| G01 | `main` | Old copy: replace it | Clean. |
| G02 | `develop` | Old copy: replace it | 〈…〉 in §5 and §7. |
| G03 | `develop` | Current, but `reference.docx` is missing: add it | 〈…〉 in §1, §4 and §5–§8. |
| G04 | `develop` | Old copy: replace it | 〈…〉 in §5–§7. |
| G05 | `develop` | Old copy: replace it | The header block still has 〈…〉 in the sponsor and the date, so the cover page leaves them blank. 〈…〉 in §0, §3, §4 and §5–§7. |
| G06 | `develop` | Current | Clean. |
| G07 | `main` | Old copy: replace it | The header block's date is still in 〈…〉, so the cover page leaves it blank. 〈…〉 in §5–§7. |
| G08 | `develop` | Old copy: replace it | Clean. |
| G09 | `develop` | Current | 〈…〉 in §5 and §6. |
| G10 | `develop` | Old copy: replace it | The header block wraps your real values in 〈…〉 (title, group, team, sponsor, authors, date). The converter treats them as unfilled, so **the cover page comes out blank**: remove the brackets and keep the values. |
| G11 | `main` | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §1 and §4–§8. |
| G12 | `develop` | Old copy: replace it | Clean. |
| G13 | `main` (same as `develop`) | Old copy: replace it | Clean. |
| G14 | `develop` | Old copy: replace it | 〈…〉 in §5–§7. |
| G15 | `main` (same as `develop`) | Old copy: replace it | **25 references are plain text, `[story:https://…/issues/26]`, not links,** so the full URLs stay in your paragraphs and Appendix A is nearly empty. Write each one as a typed link: `[[story:#26]](https://github.com/…/issues/26)`. Two links are untyped, `[#25](https://…/issues/25)`; type them too (`[[feature:#25]](https://…/issues/25)`). 〈…〉 in §5–§7. |
| G16 | `develop` | Current | Clean. |
| G17 | `main` | Old copy: replace it | 〈…〉 in §5–§8. |
| G18 | `develop` | Old copy: replace it | Two diagrams are `.svg`. pandoc needs `rsvg-convert` to embed them for older Word versions and warns without it; export them as `.png` instead. 〈…〉 in §6–§8. |
| G19 | `develop` | Old copy: replace it | 〈…〉 in §4–§7. |
| G20 | `main` (same as `develop`) | Missing: add `to-word.lua` and `reference.docx` | 〈…〉 in §3, §5–§8 and in the References block above §8. |

> [!IMPORTANT]
> **New (Nov 20): this page now checks Sprint 4 readiness.** Every group has had its Sprint 3 review and is in Sprint 4. Sprint 4 asks for the same three rules of thumb, taken to the finish: **finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages** without the Appendix, and **complete the prototype so it is fully functional**. You run Sprint 4 on the board as usual, and I grade it on the same five rubric lenses; this page is a readiness check, not your sprint grade. Find your group's card below: it says what's missing and what to do, in order.
>
> **The marks now measure against the Sprint 4 bar.** Rule 2 used to ask for §0–§4 and now asks for the whole paper; rule 3 used to ask for one working slice and now asks for the complete prototype. A mark can read lower than in the last edition with nothing in your repository having gone backwards.

**CPSC 490 · Fall 2026 · swept Nov 27, 12:13 PM PST.** Earlier editions are kept in this file's git history.

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
| [G01](#g01) BGAF | Mon Nov 30 | ⚠️ | ⚠️ | ✅ ≈ 106 | ⚠️ | ⚠️ | ⚠️ |
| [G02](#g02) Linux Larpers | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 16 | ⚠️ | ⚠️ | ❌ |
| [G03](#g03) California | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 10 | ⚠️ | ⚠️ | ❌ |
| [G04](#g04) Epic Engineers | Mon Nov 30 | ✅ | ⚠️ | ≈ 33 | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Mon Nov 30 | ⚠️ | ⚠️ | ≈ 5 | ⚠️ | ⚠️ | ❌ |
| [G06](#g06) GapWise | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 7 | ⚠️ | ✅ | ⚠️ |
| [G07](#g07) Mighty Morphins | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 17 | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 13 | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 11 | ⚠️ | ⚠️ | ⚠️ |
| [G10](#g10) Team Jiddak | Mon Dec 7 | ⚠️ | ⚠️ | ≈ 22 | ⚠️ | ⚠️ | ⚠️ |
| [G11](#g11) 5 Guys | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ❌ |
| [G12](#g12) ACJMM | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 20 | ⚠️ | ⚠️ | ❌ |
| [G13](#g13) BYKX | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 8 | ⚠️ | ⚠️ | ❌ |
| [G14](#g14) G14 | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 11 | ⚠️ | ⚠️ | ❌ |
| [G15](#g15) HIBBI-01 | Wed Dec 2 | ⚠️ | ⚠️ | ≈ 6 | ⚠️ | ⚠️ | ❌ |
| [G16](#g16) G16 | Wed Dec 9 | ⚠️ | ✅ | ≈ 27 | ⚠️ | ✅ | ⚠️ |
| [G17](#g17) G17 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 15 | ⚠️ | ⚠️ | ❌ |
| [G18](#g18) G18 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 9 | ⚠️ | ⚠️ | ⚠️ |
| [G19](#g19) G19 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 8 | ⚠️ | ⚠️ | ❌ |
| [G20](#g20) G20 | Wed Dec 9 | ⚠️ | ⚠️ | ≈ 12 | ⚠️ | ⚠️ | ⚠️ |

- **Rule 1 met:** 1 of 20 (G04).
- **Epic or story links outside §2:** 10 of 20 (G01 9, G02 33, G05 16, G06 14, G07 44, G08 4, G10 3, G14 2, G18 6, G19 7). Epics and stories are cited in §2 only. Each card lists them.
- **Issues under no story that carry no `sp:`:** 17 of 20 (G01 2, G02 12, G03 14, G05 15, G06 3, G07 11, G08 13, G10 3, G11 1, G12 10, G13 32, G14 7, G15 24, G16 2, G17 3, G18 5, G19 6). An issue can stand without a story, but then it carries its own points. Each card lists them.
- **Issues under no epic that `proposal.md` doesn't link anywhere:** 15 of 20 (G01 1, G02 2, G03 14, G05 14, G07 1, G08 1, G09 3, G11 7, G12 2, G13 4, G14 1, G15 11, G17 2, G18 9, G19 3). Each card lists them.
- **Whole paper §0–§8 complete:** 1 of 20 (G16).
- **Past 50 pages:** 1 of 20 (G01).
- **Template text 〈…〉 still in the paper:** 14 of 20 (G02, G03, G04, G05, G07, G09, G10, G11, G14, G15, G17, G18, G19, G20).
- **Prototype complete, working and tested:** 0 of 20 (none).
- **Ready to present both today:** 0 of 20 (none).

**What changed since the last edition:**

- **The Preview paper is due this Sunday, Nov 29.** Every section drafted, §0–§4 complete, one Word file per group. Each card's to-do list says what to finish first.
- **17 of 20 repositories changed since Nov 24.** Three did not (G13, G19, G20): no commit on `main` or `develop`, no issue or PR activity. Their cards are the Nov 24 cards.
- **One overall mark moved: G16, rule 2, from ⚠️ to ✅.** On `develop`, §5, §6 and §7 are now full sections (PR #132), so every section §0–§8 is written. It is the first paper with no thin or missing section. Two things remain for G16: `main` still has the old §5–§7 text, so release `develop` to `main`; and the paper is still short of 50 pages.
- **Paper sections that moved up:** G06 (§5, §6 and §7 written, PRs #78 and #80: all three ✅, and every 〈…〉 is cleared), G07 (§4 environment and design are now ✅: alternatives, the data model and the validation sequence are explained), G12 (§1.1 Related Work has its comparison table, and §4 implementation and planned activities are prose now: all three ✅), G03 (§4 environment and planned activities started, PR #93), G18 (§4 implementation and §7 started).
- **Merged since Nov 24:** G01 (22 PRs on `main`, #349, #372, #373 and #393–#413), G03 (PRs #90 and #93 into `develop`), G05 (PR #82 into `develop`), G06 (PRs #78 and #80), G08 (PR #98: the prototype now covers several cities, with four new test files), G10 (PRs #102 and #105: Objective 2.1 and Objective 1.4 written up in §4), G12 (PR #171), G15 (PR #95), G16 (PR #132), G18 (PR #85).
- **Open, not merged yet, so it does not count yet:** G02 (PRs #141 and #142), G03 (#92 and #95), G04 (#150, #158 and #161–#163), G05 (#83), G06 (#84), G07 (#183 and #184), G09 (#128 and #130), G11 (#98), G14 (#178–#181: the §6 timeline, the §1.1 comparison and the §4 narrative), G18 (#92). Get these reviewed and merged before you convert the paper for the Preview.
- **CI:** G01 `main` is green again. G10 `develop` is green and its `main` is still red at the `Repository harness` job; the release from `develop` should fix it.
- **Word export:** G03, G06 and G09 now have the Nov 18 converter, joining G16; G03 still needs `reference.docx`. G06 now converts clean. The other 16 groups still need the current converter before they make the Preview file (see the top of this page).

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules and the Word export, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting (SNX-4)

*Pipeline that rebuilds Hyperliquid order books from SNX-4 data, validates them, and backtests strategies behind a gate.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 106), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Add estimated hours per task and an assumptions paragraph to §6 for the Preview (Sun Nov 29); it is the one section still thin.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58 is dropped and has none). 42 open child issues have no Sprint milestone (#302-#324, #364, #287, #147, #142-#169 ...); stories #23-#28 and #58 have none either; 24 typed refs sit in §1 or §6 instead of §2/§4, 9 of them epic and story refs in §6; `[task:#255]` is cited twice but #255 is a sub-task; #414 is not in the proposal (PR #416 links it); #302 and #312 (one clean week, known market events) are still open with no PR after #362, #363 and #374 were closed unmerged; Old PRs without `Closes #N` (#126, #57, #38, #37, #29) and three early direct commits on main; every recent PR has one. |
| 2. Paper §0–§8 (`main`, ≈ 106 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ✅ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Link tables in place of prose: The §2 objective status table and the §5 deliverables table are maps beside real prose; they do not replace it. |
| 3. Prototype complete | ⚠️ partial | DuckDB storage, cleaning, `gate.py`, report metrics, look-ahead refusal; front end shows L1-L4 views, depth chart, filters, replay, backtest and API review tabs on synthetic order data. Not built or not tested yet: In-memory book and replay (#24), validation (#25), a book rebuilt from real data, strategies and results (#28) moved to CPSC 491; front end runs on fixtures only. CI: Main run 11/25 21:12 PST green: Repository harness and Prototype job (Python install and pytest; Node skipped there). The front end has its own `frontend.yml`, not in my data. Tests: `tests/test_*.py` for storage, cleaning, gate, report, backtest, package; front-end `*.test.ts(x)` for book, depth, cost of size, filters, replay, workspace. |
| 4. Word export (`main`) | ⚠️ partial | 809 issue citation(s) become small in-text tags; 234 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ⚠️ partial | Paper is whole except §6 hours and assumptions and §7 fractions; main CI is green and the front end demos on synthetic data, but no book is rebuilt from real data. |

**Epic and story links outside §2:** 9 on `main`: `[story:#23]` in §6, `[story:#24]` in §6, `[story:#25]` in §6, `[story:#26]` in §6, `[story:#27]` in §6, `[story:#28]` in §6, `[epic:#20]` in §6, `[epic:#21]` in §6, `[epic:#22]` in §6. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 2: #58, #89. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 77 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 1 of them aren't linked anywhere yet: #414. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §6 Project Timeline gives order of build, milestones, critical path and a figure for CPSC 491, but no estimated hours per task and no assumptions list; add both; §7 AI Usage is detailed per artifact but gives no rough fraction of each artifact that was AI-assisted; add one per artifact; §4 is now about 40,000 words; remove repeated passages across specs, design and backtest design before the final paper (Sun Dec 20); PRs #415 (Sprint 4 review, link #414), #416 (README demo steps) and #417 (Dec 1 slides) are open on main; merge them before your presentation (Tue Dec 1).

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #415 (open, main): Sprint 4 review and link #414 in proposal §4; PR #416 (open, main): prototype README demo steps brought up to date (#414); PR #417 (open, main): Dec 1 presentation slides (#276).

**To do in Sprint 4:**

1. Add estimated hours per task and an assumptions paragraph to §6 for the Preview (Sun Nov 29).
2. Merge #415 and #416 so #414 is linked and the README shows one clean-then-gate command, before your presentation (Tue Dec 1).
3. Decide whether #302 and #312 move to CPSC 491 with a named milestone or return to Sprint 4; give every other open child the Sprint 4 milestone.
4. Fix `[task:#255]`, and move the epic and story refs in §6 and the work-item refs in §1 to §2 and §4.
5. Add a rough AI-assisted fraction per artifact to §7 for the Preview (Sun Nov 29).
6. Cut repeated passages in §4 and recheck the Word export length before the final paper (Sun Dec 20).

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 16, about 34 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §4 Implementation details; it is the one §4 subsection still absent, and §5 depends on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 15 stories have child issues (#16, #45, #46, #48, #49, #57); 9 stories (#51-#55, #58-#61) have none. Nine of 15 user stories have no child issues; break each into feature, task, sub-task on the board; 21 tasks carry `sp:` under a story (double counting): #95, #92, #91, #86, #84, #81, #77, #69, #68, #41 ; Child issues #18, #17 and new #136 have no assignee; six meeting issues (#101, #80, #79, #72, #70, #6) have no type label; #130, #99 and new tasks #136, #138-#140 are not linked from the proposal; epic and story refs sit in §3; Eight direct commits on develop and one on main; PRs #3, #4, #5, #14 lack `Closes #N`; PRs #137, #133, #127, #141, #142 open. |
| 2. Paper §0–§8 (`develop`, ≈ 16 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities · ⚠️ §5 Outcomes · ✅ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §7 (2). Link tables in place of prose: §4 'Specification and design documents' is now a 4-row document table, but two prose paragraphs summarize the specs and the design; §2 uses bullets with refs. |
| 3. Prototype complete | ⚠️ partial | FastAPI `/health`, `/health/db`, POST/GET `/observations` on PostgreSQL via Compose; Angular starter page; ESP32 `main.cpp` is a skeleton with no capture. Not built or not tested yet: Wi-Fi and Bluetooth capture (1.1, 1.2), identification, location, dashboard display and real-time updates (Goal 3); no ESP32 observation reaches the dashboard. PR #142 adds scanner models, still open. CI: Develop run 11/24 12:38 PST green; Prototype job ran Python install and pytest on the backend. Angular and ESP32 projects are not built in CI; main run is older. Tests: `test_main.py`, `test_observations.py`, `test_observation_model.py` (in-memory SQLite); Angular `app.spec.ts` is not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 141 issue citation(s) become small in-text tags; 75 issue(s) fill 5 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 2 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Implementation, AI usage and §5 are unwritten, and the demo would show only API storage; no capture or dashboard data yet. |

**Epic and story links outside §2:** 33 on `develop`: `[epic:#47]` in §3, `[story:#16]` in §3, `[story:#45]` in §3, `[story:#49]` in §3, `[story:#46]` in §3, `[story:#48]` in §3, `[epic:#50]` in §3, `[story:#51]` in §3, `[story:#52]` in §3, `[story:#53]` in §3, `[story:#54]` in §3, `[story:#55]` in §3, and more. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 12: #25, #117, #132, #136, #75, #99, #101, #102, #104, #105, #119, #130. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 19 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 2 of them aren't linked anywhere yet: #99, #130. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §4 Implementation details is absent; describe the backend API, PostgreSQL tables, ESP32 firmware and dashboard as built, ending in task refs; §5 still holds a 〈Update this sentence…〉 placeholder; say what Prototype v0 does and how to run it; §7 AI Usage is the unfilled template; PR #137 and `feature/25-finalize-proposal` are open: name tools, tasks, fractions and verification, then merge; §4 summaries of the three specs and `docs/design/system-design.md` are one paragraph each; add each epic's scope, key FRs and NFRs in prose; §1.2 Problem Statements is about 215 words with bullets, and main still holds the unfilled §3 and §4 template: merge develop (#133).

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop: §3, §4 environment, specs, design and planned activities, observation API; merge into main; PR #133 (open, main): develop-to-main merge; get it reviewed and merged; PR #137 (open, develop): adds §7 to the proposal and cleans stale parts; PR #141 (open, develop): adds the development OS to §4 environment; PR #142 (open, develop): scanner and session models and endpoints (#138); PR #127 (open, develop): restart-persistence check; review and merge or close; Branches feature/25-finalize-proposal, feature/117-dev-os, feature/138-scanners-sessions: commits not in develop.

**To do in Sprint 4:**

1. Write §4 Implementation details from `prototype/backend`, the PostgreSQL tables and the firmware skeleton, ending each paragraph with task refs, for the Preview (Sun Nov 29).
2. Fill the §5 placeholder and the §7 AI disclosure (tools, tasks, fractions, verification), then merge #137, for the Preview (Sun Nov 29).
3. Expand the §4 spec summaries with each epic's scope, functional and non-functional requirements and open questions in prose.
4. Get one ESP32 observation onto the dashboard through the API, with a test per acceptance criterion, before your presentation.
5. Create child issues for stories #51-#55 and #58-#61, remove `sp:` from the 21 tasks, and assign #18, #17 and #136.
6. Link #130, #99 and #136-#140 from the proposal, merge #141 and #142, and merge develop into main (#133) so paper and code are on main.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 10, about 40 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Replace the template text in §5, §6 and §7 for the Preview (Sun Nov 29); merge #95 once the §5 draft has no 〈…〉 text.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 13 stories have child issues; 8 stories (#30, #31, #33, #35, #36, #37, #45, #47) have none. Eight of 13 user stories have no child issues; break each into feature, task, sub-task on the board; 16 issues created since Sprint 2 are not in the proposal (#94, #91, #89, #85 ...); 21 issues carry no type label; 16 issues lack `sp:` or a Sprint milestone; Open #89, #85, #75, #71, #68, #53 have no assignee; #89, #85, #75, #68, #53 and story #45 have no Sprint milestone; #65 sits under epic #28; PRs #81 and #77 lack `Closes #N`; PRs #92 and #95 are open on develop; one direct commit on main and develop; Six epic and story refs in §2 are bare, and `[story:#31]` points at issue #30. |
| 2. Paper §0–§8 (`develop`, ≈ 10 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in §1, §4, §5, §6, §7, §8 (17). Link tables in place of prose: §2 is a bullet list with refs; §4 'Specification and design documents' and 'Planned activities' (6 task rows, no prose) are tables, not prose. |
| 3. Prototype complete | ⚠️ partial | Transcriber with recognizer and verifier, dataset generation, storage and display, PyTorch training (two-variable equations merged), plotting and plot test data, and a pipeline notebook. Not built or not tested yet: Code generation and round-trip check (no objective yet), relational database (#84), raw human text input (#86), workbook output (Goal 4); #87 open; notebook viewer #92 is an open PR. CI: Develop run 11/25 22:43 PST green: harness and Prototype job ran Python install and pytest on team code. Main run 10/27 is older and green. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train and plot_equation tests; none for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 28 issue citation(s) become small in-text tags; 27 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 17 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §4 is partly written and §5 to §7 are template; the README now runs the transcriber pipeline, but Goals 2 to 4 are incomplete and tests skip dataset code. |

**Issues under no story, without points:** 14: #1, #20, #24, #42, #53, #68, #75, #85, #89, #2, #39, #55, #60, #65. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 15 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 14 of them aren't linked anywhere yet: #42, #53, #68, #71, #75, #85, #89, #94, #39, #41, #55, #60, #72, #91. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §4 Required Environment (develop, #93) lists install steps only; add why Jupyter, Python, SQLite and Mathpix were chosen, hosting and the sponsor's requirement. The §4 lead still has its template prompt; §4 Planned activities is a 6-row table; write the remaining work items as prose ending in refs. Specs `docs/specs/*.md` and `docs/design/architecture.md` get one paragraph each; summarize with FRs, NFRs, criteria; §4 has no Implementation section and no data model or decisions with rejected alternatives; describe the built transcriber, trainer and notebook; §5, §6 and §7 are the unfilled template (PR #95 drafts §5, unmerged); §6 needs CPSC 491 tasks with hours and assumptions, §7 tools, tasks, fractions and verification; §1.2 is a two-row table with a 〈…〉 placeholder; §1 is about 300 words; §8 lists 21 sources but ends with the template note and has no in-text [n] cites.

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop: transcriber, recognizer, training, plotting, notebook, specs, README steps, §4 Required Environment; merge into main; PR #95 (open, develop): draft of §5 Project Outcomes (#94); remove template text, then merge; PR #92 (open, develop): Jupyter notebook to view a part of the dataset (Objective 2.5).

**To do in Sprint 4:**

1. Write §6 (CPSC 491 tasks, hours, assumptions) and §7 (tools, tasks, fractions, verification), and merge #95 once §5 has no 〈…〉 text, for the Preview (Sun Nov 29).
2. Extend §4 Required Environment with the reason for each tool, and write Implementation and Planned activities in prose with typed refs; link #94, #91, #84, #86, #87.
3. Summarize the three specs and `docs/design/architecture.md` in §4 with scope, FRs, NFRs and criteria, and fill §1.2; remove all 〈…〉 text.
4. Delete the `login.py` template text at the end of `prototype/README.md` and merge #92, before your presentation (Tue Dec 1).
5. Create child issues for the eight stories without breakdown with one assignee and a Sprint 4 milestone; type every issue.
6. Add tests for dataset generate, store and display and `plot_data.py`, and merge develop into main so the paper and code are on main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and trader profitability analytics

*Compute profit and loss per Polymarket wallet from SonarX Polygon data, rank traders, and show them on a dashboard.* · **Sprint 4: Nov 10 – 30** · presentation Tue Dec 1 · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 33, about 17 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Finish and merge #150 so §5, §6 and §7 stop being template text; these three sections are the largest gap for the Preview.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 12 of 12 stories have child issues (feature, task, sub-task); 11 stories still open. Five PRs (#150, #158, #161, #162, #163) are open against develop; their issues cannot close until they merge; Eight feature branches (#55, #58, #59, #96, #105, #116, #117, #149) have commits not in develop; PR #4 (Sprint 1 team README) has no `Closes #N`; no recent PR lacks one. |
| 2. Paper §0–§8 (`main`, ≈ 33 of 50+ pages) | ⚠️ partial | ⚠️ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §1.2 is a 6-row table with no prose; §1.1 is one paragraph plus a 6-row table. Specs, design and planned activities are prose with typed refs. |
| 3. Prototype complete | ⚠️ partial | Settings loader, Snowflake client, smoke query, FIFO position builder and resolution matching checked against the spec's worked example; no live-data run, ranking or dashboard. Not built or not tested yet: Read-only SQL extract (#105, PR #158), trader ranking (Goal 2, PRs #161, #162) unmerged; dashboard (Goal 3) unbuilt; no end-to-end run on real rows. CI: Latest main run 11/9 15:28 PST green; develop run 11/23 11:33 PST green. Prototype job ran Python install and pytest; the live-Snowflake integration test is skipped without credentials. Tests: `tests/unit/` positions, resolutions, settings, snowflake_client; `tests/integration/test_smoke_query.py` (skipped); worked-example fixture. |
| 4. Word export (`main`) | ⚠️ partial | 119 issue citation(s) become small in-text tags; 105 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §7 are template and the prototype on develop shows tested PNL logic on fixtures only; ranking sits in open PRs, no live data or dashboard. |

**Paper, what to write:** §5, §6 and §7 on main are still the unfilled template with 〈…〉 prompts; PR #150 and branch `149-proposal-sections-5-7` hold a draft that has not merged; §6 must plan CPSC 491: the Goal 1 to Goal 3 objectives as tasks with milestones, estimated hours, build order and assumptions; §4 Environment and resources is one paragraph; dashboard framework and result storage are not chosen. Add a subsection per tool with reasons; §0 Abstract is 148 words; §1.1 needs prose arguing what differs from each compared tool; §1.2 needs a paragraph per problem; §7 AI Usage must name tools, tasks, rough fraction of each artifact AI-assisted, and how the team verified it.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #158 (open, develop): read-only SQL extract module and tests; PR #150 (open, develop): proposal §5 to §7 draft and stale §4 fixes; PR #161, #162 (open, develop): PNL ranking and ROI ranking with tests; #161 also edits architecture and proposal; PR #163 (open, develop): links feature #96 (dashboard spec) in proposal §4; Branch develop: Goal 3 dashboard spec and dashboard questions (#156, #159); merge into main at the end of Sprint 4.

**To do in Sprint 4:**

1. Merge #150 with §5 to §7 written in prose, and fill every 〈…〉 prompt, for the Preview (Sun Nov 29).
2. Write §6 as the CPSC 491 plan: objectives as tasks, milestones, hours per task, build order, assumptions.
3. Merge #158, then run the position builder on real SonarX rows end to end and demo one wallet's PNL at the presentation (Tue Dec 1).
4. Merge #161 and #162 for the Goal 2 ranking, then build one dashboard page (Goal 3) from the merged spec, with a test per acceptance criterion.
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
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 9 stories have child issues; #10-#13, #15, #16, #18 have none (tasks hang off epics #8 and #14). Seven of nine user stories have no child issues; tasks attach to epics #8 and #14 instead of stories; 17 tasks are not linked from the proposal (#84, #81, #73, #71, #70, #69 ...); 15 standalone tasks carry no `sp:`; Open tasks #84, #68, #67, #61, #57, #56 have no assignee; #84, #71, #68, #61, #57 have no Sprint milestone; Epic and story citations sit in §4 instead of §2 only; PRs #72 and #62 are open against develop and #83 against main; every merged PR has `Closes #N`. |
| 2. Paper §0–§8 (`develop`, ≈ 5 of 50+ pages) | ⚠️ partial | ❌ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ❌ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in the header block, §0, §3, §4, §5, §6, §7 (26). Link tables in place of prose: §4 'Planned activities' is an 18-row link table with about 224 words around it and no prose; the spec and design index is a table with a 〈template〉 row left. |
| 3. Prototype complete | ⚠️ partial | Locator: TDOA direction and distance from simulated hydrophones, 20-scenario direction check, interactive demo, call saving; detector train and detect scripts. Not built or not tested yet: Detector is not tested or tied to the locator; no database link or end-to-end run from recording to detected call to location; boat-noise story #12 and #11 open. CI: Develop run 11/25 10:44 PST green: harness and Prototype job (Python install and pytest). Main run 11/8 16:01 PST red: the Repository harness 'Run gates' step failed. Tests: `tests/` test_tdoa, test_locate, test_save_call, test_speed_of_sound, test_scenarios (20 scenarios, 80% pass); `ai-detector/` scripts untested. |
| 4. Word export (`develop`) | ⚠️ partial | 48 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 26 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | The proposal still has a placeholder abstract and template §3, §4 and §5 to §7; the locator demo runs, the detector is untested and unconnected. |

**Epic and story links outside §2:** 16 on `develop`: `[epic:#14]` in §4, `[story:#15]` in §4, `[story:#16]` in §4, `[story:#17]` in §4, `[story:#18]` in §4, `[epic:#8]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 15: #57, #58, #61, #63, #66, #67, #68, #71, #81, #84, #23, #47, #65, #69, #70. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 22 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 14 of them aren't linked anywhere yet: #57, #58, #61, #66, #67, #68, #71, #81, #84, #23, #47, #65, #69, #70. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §0 Abstract is a one-line placeholder on develop (PR #83 holds the draft, open on main); the front matter still has template placeholders; §3 Proposed Approaches and §4 Environment are the template prompts (task #84 is open for Environment); state strategy, alternatives, and each tool, dataset and hosting choice with its reason; §4 summarizes only the locator spec and design; summarize `goal-1-detector.md` and `ai-detector-design.md`, delete the placeholder row, add captioned diagrams and Implementation; §5, §6, §7 are the unfilled template; §6 needs the CPSC 491 plan with hours and assumptions, §7 tools, tasks, fractions and verification; §8 lists 2 sources, but §1.1 cites [1], [2], [3] with [2] and [3] being web pages that §8 does not hold; list every source, numbered in order cited.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #72 (open, develop): fills proposal §4, branch `fill-section-4-proposal.md`, 3 commits; PR #62 (open, develop): remerge main into develop (schema and ER diagram); PR #83 (open, main): §0 abstract for #81, design docs and scenario tests; 4 commits; Branch develop: scenario tests, direction demo, detector and locator design docs; main CI red.

**To do in Sprint 4:**

1. Merge PR #72 and #62, then merge develop into main and fix the failing harness gate so main CI is green.
2. Write §0 Abstract (merge PR #83, #81) and §3 Proposed Approaches, and fill the front-matter placeholders, for the Preview (Sun Nov 29).
3. Write §4 Environment (#84), summarize the detector spec and design, add captioned diagrams, and describe the built prototype in prose with issue refs.
4. Fill §5, §6 (CPSC 491 tasks, hours, assumptions) and §7 (tools, tasks, fractions, verification); rebuild §8 to match every citation.
5. Create child issues under stories #10-#13, #15, #16, #18; link the 17 unlinked tasks, #84 and #81 included, in §4.
6. Give #84, #68, #67, #61, #57, #56 an assignee and #84, #71, #68, #61, #57 a Sprint 4 milestone; add `sp:` to standalone tasks.
7. Remove the `python login.py` line from `prototype/README.md`, add detector tests, and connect detector output to the locator before your presentation (Tue Dec 1).

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Turns a student's notes into practice questions and tracks per-concept mastery and forgetting to target weak spots.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 7, about 43 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #84 and write the §4 specs, design and implementation prose on develop: the Preview (Sun Nov 29) needs §0-§4 complete.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 17 stories have child issues; #14, #18, #19, #21, #29, #31 have none (#5, #6 are old closed leftovers). Feature PRs close stories directly (#39 for #21, #53 for #18, #54 for #19, #56 for #29); no feature, task or sub-task between; Twelve issues created since Oct 20 are not linked in the proposal: #43, #49, #51, #58, #60, #74-#77, #81-#83; Story refs `[story:#16]`, `#18`, `#21`-`#24`, `#26`, `#28`-`#31` sit in the §6 table; `[epic:#13]`, `#20`, `#27` sit in §4. Epics and stories belong in §2; §4 Planned activities uses bare `#10`, `#36`, `#41` instead of typed refs; new task #81 (under #28) has no assignee; Stories #5 and #6 have no assignee; Sprint 3 still has 3 open issues past due (#24, #26, #48); the six stories above have no child issue. |
| 2. Paper §0–§8 (`develop`, ≈ 7 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ✅ §5 Outcomes · ✅ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Link tables in place of prose: §4 Environment is an 8-row table with reasons of a few words; Planned activities is a 10-row table of mostly finished items; specs are a list of links; Components, Data Model and Key Decisions are bullet lists. |
| 3. Prototype complete | ⚠️ partial | `run_demo.py` takes a notes file through document processing, concept extraction and question generation (template mode, no API key); other modules are not wired in. Not built or not tested yet: Flask web app, accounts, SQLite storage, mastery/selector/grader in the demo, live LLM mode, reminders UI, #31 user study, response-time check in practice. CI: develop run 11/24 22:04 PST green; Prototype job ran Install and test (Python) on team tests. main run 11/15 15:15 PST green but holds fewer modules. Tests: 11 team pytest files on develop (processor, concepts, questions, selector, mastery, forgetting, grader, override, summary, timer, exam calendar, demo); JS flashcards test not in CI. |
| 4. Word export (`develop`) | ✅ done | 40 issue citation(s) become small in-text tags; 26 issue(s) fill 4 table(s) in Appendix A. |
| Ready to present | ⚠️ partial | A command-line demo runs from a fresh clone on develop and §5-§7 are now drafted, but §4 is thin, the specs are not carried, and the web app in the stories does not exist. |

**Epic and story links outside §2:** 14 on `develop`: `[epic:#13]` in §4, `[epic:#20]` in §4, `[epic:#27]` in §4, `[story:#28]` in §6, `[story:#16]` in §6, `[story:#18]` in §6, `[story:#21]` in §6, `[story:#22]` in §6, `[story:#23]` in §6, `[story:#24]` in §6, `[story:#26]` in §6, `[story:#29]` in §6, and more. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 3: #48, #5, #6. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Paper, what to write:** §7 table ends with a row saying three teammates' own work and Figures 1 and 2 are "being confirmed"; finish it with tool, share and verification; §5 names the web app, code, tests and report; name the repository too, and say what the demo shows at your presentation; §4 specs: `docs/specs/specs-epic-1.md` to `-3.md` are only linked; summarize each in §4 and extend them (open PR #84 rewrites §4); §4 design is bullets (about 430 words); `docs/design/gapwise-design.md` is not carried; write paragraphs with a rejected alternative per decision; No §4 implementation section: describe each prototype module, how it was tested, and what is not built (Flask app, SQLite, accounts, reminders); §1 (375 words), §1.2 (72 words) and §3 (165 words) are short for a 50-page paper; the two figures are hotlinked images; §8 has 3 sources.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #84 (open, develop): rewrites §4 as paragraphs with typed refs, closes #83; branch develop: holds §5-§7, specs, design doc and newest features; main stopped at merge #63 on 11/15; branches 73-fill-proposal-5-6-7, 71-link-specs, feature/21-mastery-tracking: commits not in develop; merge or delete; about 19 unmerged branches (flashcards, question-selector, assignment tracker): merge into develop or delete.

**To do in Sprint 4:**

1. Merge PR #84 and finish §4 in proposal.md for the Preview (Sun Nov 29): summarize `docs/specs/specs-epic-1.md` to `-3.md` and `docs/design/gapwise-design.md`, with a rejected alternative per decision.
2. Finish §7 for the Preview (Sun Nov 29): complete the last table row, add fractions for Figures 1 and 2; name the repository in §5.
3. Add a §4 implementation section for the Preview (Sun Nov 29), then expand §1, §1.2 and §3 as paragraphs and add sources to §8.
4. Move the story and epic refs out of the §6 table and §4; link #43, #49, #51, #58, #60, #74-#77, #81-#83 in §4; assign #81.
5. Create child issues under stories #14, #18, #19, #21, #29, #31, each with one assignee and a Sprint 4 milestone.
6. Build the Flask and SQLite parts and wire `mastery_tracker`, `question_selector` and `grader` into the demo, with a test per acceptance criterion, before your presentation (Tue Dec 8).
7. Merge develop into main by PR with `Closes #N` and update `prototype/README.md`, which still says the modules are not connected.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (EL-1)

*Extracts material data from vendor certificates and test reports, stores it after human review, and supports analysis.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 17, about 33 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §5, §6 and §7 in proposal.md now: they are still template text and the Preview (Sun Nov 29) needs every section drafted.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 16 of 16 stories have child issues; all stories have an assignee and a Sprint milestone. Features #151-#167 and tasks #147-#149 (20 open issues) have no assignee; §4 cites 44 epic and story refs outside §2, 3 bare refs (#5-#7), wrong kinds (`[task:#63]`, `[bug:#117]`, `[task:#134]`-`[task:#136]`), and a broken `[[task:#146]]` URL; Task #38 carries `sp: 3` under story #48; eleven standalone issues have no `sp:` (#28, #63, #67, #137-#139, #147-#149, #177, #178); PRs #174 (closed) and #180 (open) have no `Closes #N`; a fourth direct commit reached main (`Add analysis prototype`); Task #178 is not linked in the proposal; four Sprint 3 issues (#43, #94, #95, #114) are still open past due. |
| 2. Paper §0–§8 (`main`, ≈ 17 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in the header block, §5, §6, §7 (15). Link tables in place of prose: §4 Planned activities is a 100-row link table (98 issue-link rows) with one paragraph; the 15-row document table stands in for specification writing. |
| 3. Prototype complete | ⚠️ partial | Static HTML mock-ups plus a page-5 analysis screen (`ui-tabs/analysis.html`, `analysis.js`) on synthetic records; no back end, OCR or database on main. Not built or not tested yet: Upload, Snowflake storage, extraction/OCR, authentication and review: page 2 and page 3 prototypes (#183, #184) are open PRs; search is a mock-up. CI: Main run 11/25 16:54 PST green, both jobs. The Prototype job ran Python install and pytest on the course `tests/test_login.py` only; Node steps were skipped, so `analysis.test.js` is not run. Tests: `prototype/ui-tabs/analysis.test.js` (node --test, not in CI); CI runs only the course `test_login.py`; PR #184 adds backend tests. |
| 4. Word export (`main`) | ⚠️ partial | 253 issue citation(s) become small in-text tags; 134 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 15 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only a static search page and the page-5 screen can be shown; §5-§7 are template text, §4 specs are links, and CI runs no team test. |

**Epic and story links outside §2:** 44 on `main`: `[epic:#4]` in §4, `[epic:#45]` in §4, `[story:#49]` in §4, `[epic:#1]` in §4, `[story:#12]` in §4, `[story:#16]` in §4, `[story:#24]` in §4, `[story:#27]` in §4, `[story:#13]` in §4, `[story:#14]` in §4, `[story:#15]` in §4, `[story:#18]` in §4, and more. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 11: #147, #148, #149, #177, #28, #63, #67, #137, #138, #139, #178. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 32 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 1 of them aren't linked anywhere yet: #178. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5, §6 and §7 are still the template prompts with 〈…〉 placeholders (#147-#149 open); §6 must be the CPSC 491 plan with hours, not this fall's sprints; §4 specs: the three goal specs in `docs/specs/` (5,600-6,400 characters each) are only linked; summarize each in §4 (PR #145 is open); §4 diagrams: Figures 1 (use case) and 4 (data flow) have no explaining prose and Figure 2 has a one-line caption; add a paragraph and caption each; No §4 implementation section; describe the prototype pages (PRs #183, #184 open) and replace the 98-row planned-activities table with prose; §4 environment reasons now exist for most tools; add FastAPI and Figma, and fix the typos. §1 (259 words) and §8 (4 sources) are short.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #184 (open, main): page 3 validation prototype with backend and tests, closes #88; PR #183 (open, main): page 2 processing and review queue prototype; PR #145 (open, main): goal specification summaries added to the proposal; PR #185 and #180 (open, main): normalize typed links; fix wireframe reference (no Closes line on #180); PR #102 (open, main): page-5 analysis sequence diagram; nine branches unmerged.

**To do in Sprint 4:**

1. Write §5, §6 and §7 in proposal.md for the Preview (Sun Nov 29): outcomes, a CPSC 491 plan with hours per §2 objective, an AI disclosure with fractions and verification (#147-#149).
2. Merge PR #145 and summarize each goal specification in §4 as prose; add a paragraph for Figures 1 and 4 for the Preview (Sun Nov 29).
3. Merge PRs #183 and #184, then write the §4 implementation section and replace the 100-row planned-activities table with paragraphs ending in typed refs.
4. Replace `login.py`, `test_login.py` and the template text in `prototype/README.md`, and make CI run the team tests, before your presentation (Tue Dec 8).
5. Assign #151-#167 and #147-#149; fix the `[[task:#146]]` URL and wrong ref kinds; move epic and story refs out of §4; remove `sp:` from #38; add `sp:` to #28, #63, #67, #137-#139, #177, #178.
6. Give PR #180 a `Closes #N` line and stop committing straight to main; every change goes through a PR.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: interactive crime map and database

*Normalizes public Costa Mesa crime-call data into SQLite and shows it on a filterable Leaflet map.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 13, about 37 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build radius selection (#33, #34) into the Leaflet page with tests, so the demo shows the stories rather than only the marker map.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child tasks. Closed legacy issues #45-#47 (labelled duplicate), #6 and #7 have no Sprint milestone; Task #97 (Anaheim and Fullerton sources, merged by PR #98) is not linked in the proposal; Standalone tasks #49, #62, #79, #80, #83, #89, #95, #97 carry no `sp:`; Goal 1 text in §4 on develop cites `[epic:#3]`, `[story:#4]`, `[story:#5]` and `[story:#28]`; epics and stories belong in §2 only; Sprint 1 PRs #37, #39, #40 lack `Closes #N`; every later PR has one. #27 is still open under past-due Sprint 3. |
| 2. Paper §0–§8 (`develop`, ≈ 13 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ✅ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ✅ §8 References. Link tables in place of prose: none; §4 is prose with typed refs at the end of each part. |
| 3. Prototype complete | ⚠️ partial | Flask map of 353 mapped records from Costa Mesa, Fullerton and Anaheim: city and crime-type filters, grouped markers, popups; standalone `multi-city-map.html`. Not built or not tested yet: Radius selection (#33, #34), marker selection #27, summaries and charts (#19, #20) are open and not in the page; no tests for them. CI: develop run 11/24 21:22 PST green, harness green; Prototype job ran Install and test (Python) on team tests. main run 11/17 19:49 PST green. Tests: Nine team test files: normalize, load_db, area_filter, crime_frequency, app routes, normalize_city, multi_city_map, geocoding. |
| 4. Word export (`develop`) | ⚠️ partial | 57 issue citation(s) become small in-text tags; 48 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ⚠️ partial | The Flask and Leaflet map runs from a fresh clone with tests, but radius search, summaries and §6-§7 are unfinished, and the paper is far short of 50 pages. |

**Epic and story links outside §2:** 4 on `develop`: `[epic:#3]` in §4, `[story:#4]` in §4, `[story:#5]` in §4, `[story:#28]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 13: #6, #7, #45, #46, #47, #49, #62, #79, #80, #83, #89, #95, #97. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 12 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 1 of them aren't linked anywhere yet: #97. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §6 is one paragraph with no tasks per objective, no hours and no dates ("pending team planning"); write the CPSC 491 plan: tasks #13-#22, milestones, hours, assumptions; §7 is a per-change log of ChatGPT drafting at about 100% with the template blockquote left in; state tools, fractions per artifact, and how you verified; §1.1 (369 words) is a table plus two paragraphs; argue more fully what this project does differently, add sources to §8 (4 now). §1 and §1.2 are short; Goal 1 §4 is a full section (about 2,000 words); Goals 2 and 3 are about 200 words each; bring them to the same depth; §4 Implemented modules and §5 (one 83-word paragraph, no run commands) describe only the Costa Mesa slice; add the Fullerton and Anaheim sources (#97); The paper is still far short of 50 pages, so every section must grow.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is three PRs ahead of main: #94 (route tests), #96 (Goal 1 §4), #98 (city sources); branch 83-update-prototype-readme: 4 commits not in develop; merge or delete.

**To do in Sprint 4:**

1. Build radius selection (#33, #34) and the frequency summaries (#19, #20) into the map page, with a test per acceptance criterion, before your presentation (Tue Dec 8).
2. Finish #27 marker selection and the combined filters (#29-#31) so the page matches the stories.
3. Write §6 as the CPSC 491 plan with tasks, milestones, hours and assumptions, and rewrite §7 as a verified disclosure, for the Preview (Sun Nov 29).
4. Update §4 Implemented modules and §5 for the multi-city data, link #97, expand §1, §1.1 (what Crime Busters does differently), §1.2; give Goals 2 and 3 Goal 1's depth.
5. Move `[epic:#3]`, `[story:#4]`, `[story:#5]`, `[story:#28]` out of §4 and add `sp:` to the standalone tasks.
6. Release `develop` to main by PR with `Closes #N`; close legacy #45-#47, #6, #7; delete branch 83-update-prototype-readme.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11, about 39 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge release PR #110 so main shows the working prototype, then build the dashboard alerts list (#117) the demo needs.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 10 of 10 stories have child issues (#37 has #117, #118; #38 has #119). `sp:` sits under pointed parents on #129, #122, #120, #115, #112, #111, #101 and #57 (double counting); #80 no longer carries it; Six issues are not linked in proposal §4: #106, #115, #122, #125, #126, #129; PRs #116, #123, #127, #130 are open; #106 is closed with no Sprint milestone; #59 hangs off epic #28, not a story; Release PR #110 is still open, so main is scaffold; PR #20 (old draft) has no Closes line; every Sprint 3-4 PR has one. |
| 2. Paper §0–§8 (`develop`, ≈ 11 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6 (13). Link tables in place of prose: §4 Specification and design documents is a table that indexes eight docs without summarizing them; Planned activities is a 53-row issue-link table with one intro paragraph. |
| 3. Prototype complete | ⚠️ partial | Vehicle selection, service-record API and CRUD, manual entry and CSV import forms, dashboard with edit/delete, mileage entry, status-label recommendations for three service types. Not built or not tested yet: Dashboard alerts Due Soon/Due Now (#117, #37), mileage window (#118), five-scenario end-to-end tests (#119, #38), nickname editing (#125, criterion 7 of #32), typed UI tests (#91). CI: develop 11/25 17:12 PST green: the Prototype job ran Install and test for Node and Python, so API and UI tests executed. main 10/22 green but scaffold only. Tests: Seven pytest files (vehicle and service-record APIs, label, engine, interval) and seven `tests/ui/*.test.js` page tests; `smoke_test.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 63 issue citation(s) become small in-text tags; 63 issue(s) fill 3 table(s) in Appendix A; 13 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | The develop prototype runs with green CI and real tests, but alerts for #37 and the end-to-end suite for #38 are unbuilt, §5-§6 are template, and §4 is index-only. |

**Issues outside your epics, not linked yet:** 19 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 3 of them aren't linked anywhere yet: #122, #126, #106. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5 and §6 are still template prompts with 〈…〉 placeholders (13 left); write §6 as the CPSC 491 plan with hours per objective, not this fall's sprints; Eight specs and design docs in `docs/specs/` and `docs/design/` (2,000-9,000 characters each) are only indexed; summarize scope, requirements, acceptance criteria, open questions in §4; §3 is about 190 words: add alternatives beyond rules versus AI (Flask versus other stacks, SQLite versus hosted, React) with reasons; §1.2 is 103 words; No §4 implementation prose: describe the service-record API, entry and import forms, dashboard, label rule and tests, ending in task refs; §7 is a real disclosure but gives one overall figure (10%); add fractions for the prototype code. The paper is about 7,000 words, far from 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #110 (open, develop to main): release of Sprint 2 and 3 work; main is still scaffold; PR #130 (open, develop): §3 and §4 prose from the specs and design docs, closes #122; PR #128 (open, develop): five-scenario end-to-end validation for the engine (#119); PR #116, #123, #124, #127 (open): four-label sync, files #122, Sprint 3 facts, double-bracket refs; branches feature/98-sprint-3-review (8 commits), feature/59-four-labels and five more: not in develop.

**To do in Sprint 4:**

1. Merge release PR #110 with CI green on main so the default branch shows the prototype and proposal.
2. Merge PR #128 and build the dashboard alerts (#117), the mileage window (#118) and nickname editing (#125), then finish #91, before your presentation (Tue Dec 8).
3. Write §5 and §6 for the Preview (Sun Nov 29): outcomes naming repository, prototype and paper, and a CPSC 491 plan with hours per objective.
4. Merge PR #130, then check §4 carries the five specs and `docs/design/architecture.md` as prose, with an implementation subsection and rejected alternatives.
5. Remove sp: from #129, #122, #120, #115, #112, #111, #101, #57; link #106, #115, #122, #125, #126, #129 in §4; give #106 a Sprint milestone.
6. Expand §3 alternatives and §1.2 as paragraphs, replace the work-item table with prose, and add code fractions to §7.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · **Sprint 4: Nov 17 – Dec 7** · presentation Tue Dec 8 · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 22, about 28 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Replace the 〈…〉 front matter and write §5-§7 in proposal.md, then build the first dashboard story (#28) so Goal 3 exists for the demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 12 of 14 stories have child issues; #30 and #55 (Epic #24) have none; #28 and #29 have only §4 writing tasks #103, #104. Stories #30 and #55 have no child issue; #28 and #29 have only §4 writing tasks (#103, #104); #88 (feature) carries sp: 4 under story #33, and #33 itself hangs off task #46; #56 carries sp: under pointed task #13; Eight issues are not linked in the proposal: #83, #88, #91, #92, #94, #100, #103, #104; #90 is a bare link, not a typed ref; `[task:#3]` is untyped and `[task:#69]` points to an epic; #69 is linked outside §2; `[epic:#15]`, `[epic:#23]` and `[story:#25]` are cited in §4 (epics and stories belong in §2 only); #38 is closed with no assignee; #73 and #74 (closed) have no Sprint milestone; 14 direct commits on main from before the last review; none since; all 42 PRs close an issue. |
| 2. Paper §0–§8 (`develop`, ≈ 22 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in the header block (6). Link tables in place of prose: §4 Planned Activities (5 bullets) and Tracked Task Issues (about 30 bullets with one-line descriptions) are lists; Environment is bullets plus one paragraph; §5 is a bullet list. |
| 3. Prototype complete | ⚠️ partial | Goal 1 network model plus Goal 2 detection: six rules, features, anomaly model, risk score with evidence, injected-ring validation and reports via `demo.py` and `validate.py` on synthetic data. Not built or not tested yet: Goal 3 dashboard (#28-#30, #55), search and tracing; no UI; stories #38 and #39 still open. CI: develop 11/25 17:29 PST green (43211b5); Prototype job ran Install and test (Python) on team code. main 11/17 14:24 PST still red on Repository harness (Run gates). Tests: Goal 1: 33 tests in two files; Goal 2: seven `test_goal2_*.py` files (features, heuristics, scoring, models, ground truth, review, integration); plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 60 issue citation(s) become small in-text tags; 53 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 6 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | Goals 1 and 2 run from the command line with tests, but Goal 3 and any UI are unbuilt, and front matter, §5-§7 still carry template or thin text. |

**Epic and story links outside §2:** 3 on `develop`: `[epic:#15]` in §4, `[epic:#23]` in §4, `[story:#25]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 3: #6, #67, #77. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Paper, what to write:** Front matter still holds 〈StableScope〉, 〈10〉, 〈Jiddak〉, 〈SNX-3〉 and a 〈2026-05-17〉 date; replace them before the Preview; §6 is this fall's sprints 1-6 (weeks 5-16): thin. Replace with the CPSC 491 plan: tasks = §2 objectives, milestones, hours, assumptions, in build order; §5 is a deliverables bullet list plus a stale "Prototype (starting Sprint 2)" section; write prose on what Goals 1 and 2 demonstrate and how to run them; §4: Objective 2.1 now has a prose write-up with three captioned diagrams, but Epic #23 and #24 specs still lack requirements and acceptance criteria; no implementation section; §7 is two table rows plus one verification sentence; §1 and §1.1 (a table, few citations) are short; the ER text still says nothing is implemented. About 10,000 words, far from 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is ahead of main: Goal 2 prototype and §4 prose are not on main; main CI is red; branch feat/69-goal1-network-model-prototype: 2 unmerged commits not in develop.

**To do in Sprint 4:**

1. Replace every 〈…〉 in the front matter, then rewrite §5, §6 and §7 as prose for the Preview (Sun Nov 29); §6 is the CPSC 491 plan with hours.
2. Build a minimal dashboard (#28, then #29 and #30) with a test per acceptance criterion before your presentation (Tue Dec 8).
3. Fix the Run gates failure on main and release develop to main by PR at sprint end (Dec 7); keep direct commits off main.
4. Write a §4 Implementation section for `stablescope/`, `stablescope_detection/` and their tests; add requirements and acceptance criteria to the Epic #23 and #24 specs.
5. Create child issues under #30 and #55; assign #38; drop sp: from #88 and #56; link #83, #88, #91-#94, #100, #103, #104 as typed refs in §4; keep epic and story refs in §2.
6. Expand §1, §1.1 and §7 (verification method, AI fractions for the prototype code) for the Preview (Sun Nov 29).

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

*Phone app records a marathon runner's GPS to Firebase; spectators follow on a web page; pace and finish-time prediction.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build the spectator view (#69) so a phone's GPS position shows on a web page through Firestore; the demo needs it and three stories wait on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33); 49 of 56 issues linked from the proposal. Not linked from `proposal/proposal.md` §4: #89, #90 (11/19) and new #93, #94, #95, #96, #97 (11/26); #93 is a standalone task with no `sp:`; #94-#97 carry their own `sp:`; PR #98 (closes #93) is open against `main`, not `develop`; #93 is not in the proposal; Open stories #28, #29, #30, #31, #33 and features #63, #68, #69, #71, #74 have no merged PR yet; `develop` exists but is stale (login scaffold); PRs #87, #92 merged straight into `main`; #91 closed unmerged; One old direct commit (`.github` scaffold) on main and develop; every PR closes an issue. |
| 2. Paper §0–§8 (`main`, ≈ 9 of 50+ pages) | ⚠️ partial | ⚠️ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in the header block, §1, §5, §6, §7, §8 (17). Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; only Goal 3 is summarized in prose. §2 is a bullet list of goals and objectives. |
| 3. Prototype complete | ⚠️ partial | Expo app with Firebase client, runner GPS tracking (`runner-app/tracking.js`), Firestore smoke test, pace calculation (`prediction/pace.py`). No spectator view, posts or route map. Not built or not tested yet: Spectator view (#69), posts (#63, #74), route map (#71), finish-time prediction (#68); stories #28-#31 and #33 not complete. CI: main CI green 11/19 (1658566); Prototype job ran Node install and test (jest) and Python install and test. develop green but only the login scaffold. Tests: 3 test files: `__tests__/App.test.js`, `__tests__/tracking.test.js` (jest), `prediction/test_pace.py`; no tests for posts or spectator. |
| 4. Word export (`main`) | ⚠️ partial | 55 issue citation(s) become small in-text tags; 50 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 17 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only the phone-GPS-to-Firestore and pace slice runs; spectator view, posts and prediction are unbuilt, and §5-§7 are template text. |

**Issues under no story, without points:** 1: #93. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 16 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 7 of them aren't linked anywhere yet: #89, #90, #93, #94, #95, #96, #97. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §0 Abstract describes an ML performance-analysis app; the goals are live tracking, posts and a spectator page. Rewrite it to match §2; §1 and §1.1 still hold template quote blocks and a 〈Your survey〉 placeholder; fix the duplicated table cell and typos; §5 Outcomes, §6 Timeline and §7 AI Usage are still template text and 〈…〉 placeholders. Write the CPSC 491 plan with hours per objective; §4 specs and design: only Goal 3 is in prose; carry Goals 1 and 2 specs, data model, decisions with rejected alternatives from `docs/`; §4 tech stack gives reasons but is not a titled Environment section; the Firebase setup text is a first-person how-to. The paper is about 4,600 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #98 (open, base main) - §4 GPS implementation write-up, closes #93; branch 93-gps-implementation-writeup; branch develop - stale login scaffold only; bring up to date with main (#89) or retire.

**To do in Sprint 4:**

1. Build the spectator view (#69) in `prototype/spectator-view/` so a runner position reaches a web page through Firestore, with a test per acceptance criterion, before your presentation (Thu Dec 3).
2. Build posts (#63, #74), route map (#71) and finish-time prediction (#68); close each story with a merged PR that says `Closes #N`.
3. For the Preview (Sun Nov 29) write §5 Outcomes, §6 Timeline for CPSC 491 with hours per objective, and §7 AI Usage naming tools, tasks and fractions (#97).
4. Rewrite §0 to match Goals 1-3 and expand §1 and §2 (#94, #95); remove every quote block and 〈…〉 placeholder in §0-§8.
5. Carry the Goal 1 and Goal 2 specs, data model and architecture decisions with rejected alternatives from `docs/` into §4 prose; link #70 and #73.
6. Link #89, #90 and #93-#97 as typed refs in §4, add `sp:` to #93, merge PR #98, settle the `develop`/`main` stream, and refresh `prototype/README.md`.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Python app that finds signal peaks in 6G captures, classifies waveform and modulation, and explains the decision.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 20, about 30 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Finish the waveform family gate (#142) and CLI integration (#161), because the demo needs one working end-to-end path; then rewrite §6.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 10 of 16 stories have child issues; #67, #69, #70, #71, #84, #95 have none. Stories #67, #69, #70, #71, #84, #95 have no child feature, task or sub-task; Eight issues created since Sprint 2 are not in the proposal on develop: #172, #165, #163, #158, #157, #147, #103, #95; Stories #70 and #71 have no assignee or Sprint milestone; #103 is untyped with no assignee, milestone or `sp:`; Tasks #172 (under epic #60) and #163 (under epic #58) hang straight under an epic and carry sp:1; Wrong-kind refs: `[task:#67]` (twice) is a story, `[task:#169]` and `[task:#164]` are sub-tasks, `[task:#88]` and `[task:#97]` are features; Standalone tasks with no `sp:`: #168, #162, #161, #152, #150, #147, #112, #100, #85. |
| 2. Paper §0–§8 (`develop`, ≈ 20 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. |
| 3. Prototype complete | ⚠️ partial | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, Captum attribution, transformer AMC module. Not built or not tested yet: Waveform family gate (#142, #143), CLI wired to the full pipeline (#161), re-classifier stories #70, #71; channelizer not called by any entry point. CI: develop 11/26 00:47 PST green (7df3d5f); Repository harness green and Prototype job ran Install and test (Python) on team code. main is the 10-16 login scaffold, also green. Tests: 14 test files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, pipeline gate, OFDM, training, transformer. |
| 4. Word export (`develop`) | ⚠️ partial | 115 issue citation(s) become small in-text tags; 64 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ❌ not ready | Peak-picker and XAI demo runs from develop, but waveform identification and pipeline integration are unbuilt, and §5, §6 and the specs are not paper quality. |

**Issues under no story, without points:** 10: #150, #152, #161, #162, #85, #100, #103, #112, #147, #168. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 10 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 2 of them aren't linked anywhere yet: #95, #103. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §6 is now a three-phase CPSC 491 plan in prose, but has no hours per task, milestone dates or assumptions; add them: thin; §5 is a future-tense deliverables paragraph; say what exists at the end, what the prototype demonstrates and how to run it; §4 opens with the old MATLAB paragraph; Environment and resources names Python libraries without reasons. Add why MATLAB, PyTorch, Captum, h5py and where data lives; §4 specs exist for the application architecture and waveform family; Goals 1, 4, 5 get a sentence each. Add requirements and acceptance criteria per epic; §1.2 P2 and P3 are one sentence each. §4 implementation now covers peak pickers and channelizer; add the waveform-family gate and `modulation_classification/`. About 10,500 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #173 (open, develop) - fixes XAI figure cross-references in §3.3, closes #172; branch develop - real prototype and §4 work; main is the scaffold, release it at sprint end; branches Application-Structure, docs/team-documentation - commits not in develop.

**To do in Sprint 4:**

1. Build the waveform family gate (#142, #143) and integrate the CLI with the analysis pipeline (#161); add one test per acceptance criterion before your presentation (Thu Dec 3).
2. For the Preview (Sun Nov 29) add hours per task, milestone dates and assumptions to §6, and rewrite §5 as outcome prose with run steps.
3. Add a reason per tool to §4 Environment, replace its opening MATLAB paragraph, and describe the waveform-family gate and `modulation_classification/` in Implementation.
4. Add per-epic specs for Goals 1, 4, 5 (requirements, acceptance criteria, open questions); expand §1.2 so P2 and P3 are paragraphs.
5. Link #172, #165, #163, #158, #157, #147, #103, #95 in §4 as typed refs, add children for stories #67, #69, #70, #71, #84, #95, and assign #70, #71 a milestone.
6. Merge PR #173, then open the sprint-end develop-to-main PR so main carries the real prototype.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8, about 42 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge the five open feature PRs, then rewrite `prototype/README.md` and rename the test file so CI exercises the app.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#19-#27 via features #53-#102 and tasks #55-#106). Only 8 of 84 linked issues are closed; tasks #56, #57, #61, #62 and feature #53 have open PRs #144, #145, #147, #148, #153; #93, #94, #124 and #47 have no Sprint milestone; #13 has no assignee or milestone; #139, #125 (3 assignees), #126, #124, #123, #122 (2), #111 and #107 (4) break one-assignee-per-issue; 4 issues are not in proposal.md (#131, #124, #113, #107); refs like `taskL#127`, `[task:#139]` and #119's wrong URL are malformed; Merged PR #150 has no Closes; older PRs #1, #3, #4, #9, #36, #117 lack issues. |
| 2. Paper §0–§8 (`develop`, ≈ 8 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ⚠️ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Link tables in place of prose: §4 Planned Activities is a 17-row issue table (16 link rows) with no prose; below it are 40 one-line task sentences, each just a ref. §1.1 is a table only. |
| 3. Prototype complete | ⚠️ partial | `A.M.I.Y.A.core/` has app, database, models, assignment and deadline services; the Electron/Vite UI has a task modal. Form, storage and edit PRs are unmerged. Not built or not tested yet: Nearly all of Goals 1-3: form validation, storage, edit/delete, suggested deadline UI, override, extension, progress slider, reminders (#53-#106 open). CI: develop green 11/16 (8be40c7), main green 11/14 (3c0d601); Prototype job ran only the Python step; the UI `package.json` is in a subfolder, so Node was skipped. Tests: One file, `A.M.I.Y.A.core/tests/TestAssignments.py`; its name does not match pytest discovery, so CI likely does not run it. |
| 4. Word export (`develop`) | ⚠️ partial | 102 issue citation(s) become small in-text tags; 84 issue(s) fill 5 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it. |
| Ready to present | ❌ not ready | Prototype runs a thin core and UI shell; most stories are open, no run steps exist, and §6, §7 and §4 implementation are not written. |

**Issues under no story, without points:** 32: #122, #123, #125, #126, #127, #129, #130, #136, #137, #142, #8, #10, #11, #12, #13, #15, #31, #32, #33, #34, and more. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 22 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 4 of them aren't linked anywhere yet: #107, #113, #124, #131. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §6 Timeline lists this fall's four sprints, which is the wrong content. Write the CPSC 491 plan: objectives as tasks, hours, build order, assumptions; §7 AI Usage says "None as of this moment." Disclose tools, tasks, fraction per artifact and how the team verified output; §1.1 has a pros-and-cons table but no prose on what A.M.I.Y.A. does differently; §1.2 is 68 words; only four references; §4 Environment gives no reason per tool and no data store; specs are three one-paragraph summaries linking `docs/specs/specs-G1.md` to `specs-G3.md`; §4 design is wireframes only: add system context, components, data model (`docs/design/ER_DIAGRAMS.md`), data flow, decisions; no Implementation section; §5 omits how to run.

**Merge first** (it doesn't count until it's in `develop` or `main`): PRs #144, #145, #147, #148 (open): form validation, local data, edit/delete, confirmation; PR #153 (open): assignment UI feature #53; branches task/111-specification-details, task/122-high-level-architecture-diagram: unmerged commits; PRs #134, #135 closed; branches task/136-related-work-format, task/141-planned-activities: unmerged §1.1 and §4 writing; open PRs.

**To do in Sprint 4:**

1. Merge PRs #144, #145, #147, #148, #153 with `Closes #N`, then build storage, suggested deadline, progress slider and reminders, one story at a time.
2. Rewrite `prototype/README.md` with install, run and test commands for the core and the UI before your presentation.
3. Rename `TestAssignments.py` to `test_assignments.py` and add one test per acceptance criterion in `docs/specs/specs-G1.md` through `specs-G3.md`.
4. For the Preview (Sun Nov 29) rewrite §6 as the CPSC 491 plan and §7 as a real AI disclosure; merge the §1.1 and Planned Activities branches and expand §1.2 into prose.
5. Write §4 Environment with a reason per tool, an Implementation section, and carry specs and ER design into §4 prose.
6. Add Sprint milestones to #93, #94, #124, one assignee per issue, and fix the malformed refs in the Planned Activities table.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · G14: Cyber Sandbox (Cyber Squad)

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11, about 39 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PRs #179-#181 and write §5 and §7 in `proposal/proposal.md` for the Sun Nov 29 Preview, since both are still template text.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 18 of 18 stories have child issues (feature, task, sub-task); epics #22 and #23 sit above them. About 40 Sprint 4 children (#136-#175, minus #140) plus #114, #115 have no Sprint milestone; `sp:` remains on #99, a task under story #25; points belong on the story only; #88 and #92 have no assignee; #79, #80, #81, #44 and #45 have several; Sprint 4 meeting #177 is not in the proposal and has no assignee; #91 and #92 are cited as plain links, not typed refs; Of the Sprint 4 children #136-#175 none is closed; only #126, #129, #130 (PRs #127, #131) are done, and #115 is still open; PR #50 (Goal 2 spec) has no issue; §4 cites story #24 and §1 cites task #113. |
| 2. Paper §0–§8 (`develop`, ≈ 11 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ✅ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §4 "Specification and design documents" opens with an 11-row link table, but each document then gets a prose summary; planned activities are prose paragraphs with refs. |
| 3. Prototype complete | ⚠️ partial | PySide6 start menu loads a sample or JSON scenario validated by Pydantic; user browses, creates and deletes simulated files in memory; optional Ollama generator script. Not built or not tested yet: Process manager, log and network viewers, malware behaviors, response and lifecycle controls, scenario configuration, NRP.ai integration, action log, report, hints (#139-#175). CI: main green 11/12 (ec16018), develop green 11/12 (2a0c3b8); Prototype job ran Install and test (Python) on team code, and CI fails if no tests are collected. Tests: 5 test files in `prototype/tests/`: scenario model, loader, simulation engine, scenario generator, UI (Qt offscreen); none for unbuilt stories. |
| 4. Word export (`develop`) | ⚠️ partial | 176 issue citation(s) become small in-text tags; 119 issue(s) fill 6 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | Only the file view and JSON loader work; most of the 18 stories are unbuilt and §5-§7 are template text, so neither paper nor prototype is complete. |

**Epic and story links outside §2:** 2 on `develop`: `[story:#24]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 7: #140, #177, #13, #88, #91, #92, #134. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 12 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 1 of them aren't linked anywhere yet: #177. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5 Outcomes is still the template quote and 〈…〉 placeholder. Write two paragraphs naming repository, prototype and paper, what it demonstrates and how to run it; §6 Timeline is template text and an empty 〈…〉 table. Write the CPSC 491 plan: objectives as tasks, hours, milestones, build order, assumptions; §7 AI Usage is the template placeholder. Disclose tools, tasks, fraction per artifact (proposal, diagrams, code) and how you verified output; §3 still says 'Sprint 2 priorities'; rewrite it to match the prototype. §1.2 has spelling errors; §2 is a 20-line bullet list; §4 implementation covers `ui/`, `sim/`, `scenario/`; extend as process, log and network views and AI generation land. §8 has five sources, all competitor sites.

**Merge first** (it doesn't count until it's in `develop` or `main`): PRs #179, #180, #181 (open, develop) - §6 spring timeline, §1.1 simulator comparison, §4 requirements and design narrative; PR #178 (open, develop) - file information on inspect, #25 AC2, with tests and README; branch develop - holds the fuller proposal (57k characters vs 50k on main); release it to main at sprint end.

**To do in Sprint 4:**

1. Merge PRs #179, #180, #181 into develop for the Preview (Sun Nov 29), then write §5 Outcomes and §7 AI Usage; check §6 has hours per objective, milestones and assumptions.
2. Merge PR #178 and build the simulated process manager, log viewer and network viewer (#139, #143, #105 design) with a test per acceptance criterion before your presentation (Thu Dec 3).
3. Implement malware behaviors, response controls and scenario lifecycle (#146, #149, #152), then scenario configuration, NRP.ai adapter, action log and report (#155-#167).
4. Add a Sprint milestone to the Sprint 4 children (#136-#175) and #114, #115; give #88 and #92 one owner; remove `sp:` from #99.
5. Rewrite §3 (still 'Sprint 2 priorities') to match the prototype; proofread §1.2; turn §2 bullets into sentences.
6. Link #177 as a typed ref in §4, then release develop to main at sprint end (Dec 2).

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · **Sprint 4: Nov 12 – Dec 2** · presentation Thu Dec 3 · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 6, about 44 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Build a first playable slice of the game demo (enemies, #26) in `prototype/`, since the demo and four stories have no code yet.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 8 stories have child issues (#30, #31, #32, #33); #26-#29 have none. Stories #26, #27, #28, #29 (game demo) still have no child feature, task or sub-task; `proposal/proposal.md` has 0 typed refs: bare `#N` cells and untyped `[story:https://...]` parents in the §4 table; #46 is under story #32 yet still carries `sp: 2`; Sixteen issues are not in the proposal: #43, #76, #78, #82, #84, #86-#94, #96, #97; #86-#88 and #94 are untyped; Standalone issues #86-#91, #94, #96 and nine older ones have no `sp:`; #43 has no milestone, #44 no assignee; Stories #26-#30, #32, #33 each have 2 assignees; one assignee per issue. |
| 2. Paper §0–§8 (`main`, ≈ 6 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in §5, §6, §7 (14). Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; "Planned activities" is a 38-row table with no prose; §1.2 and §2 are a table and a bullet list. |
| 3. Prototype complete | ⚠️ partial | CMake project (SDL3, Assimp, ImGui, GLM) with ECS core, transform and mesh components, renderer and model loader, mesh manipulation (#84); README now has Windows setup. Not built or not tested yet: Game demo stories #26-#29 (headers only, no gameplay), multiplatform proof (#31), renderer camera, lighting, texture (#92, #93, #97), editor beyond mesh manipulation (#33). CI: main green 11/12 PST (43fce39); develop b100494 green 11/25 16:10 PST. Prototype job detected CMake, installed graphics libraries, configured, built C++ and ran Tests (CMake). Tests: README names target `test_engine_components` (basic ECS checks); test sources not visible in the sweep's file list. |
| 4. Word export (`main`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 25 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | The engine builds and a basic ECS test passes, but no game demo exists, and §4 design, implementation and §5-§7 are unwritten. |

**Issues under no story, without points:** 24: #86, #87, #88, #89, #90, #91, #96, #43, #44, #47, #48, #49, #50, #54, #57, #58, #61, #64, #70, #74, and more. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 28 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 11 of them aren't linked anywhere yet: #86, #87, #88, #89, #90, #91, #96, #43, #76, #78, #94. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5 Outcomes, §6 Timeline and §7 AI Usage are still the template quote blocks and 〈…〉 placeholders; write all three, with the CPSC 491 plan and hours; §4 specs: summarize `docs/specs/game-engine.md` and `game-demo.md` in prose (scope, FR/NFR, acceptance criteria, open questions); today only file names appear; §4 design: write components, ECS data model, data flow, decisions with rejected alternatives, undesigned parts from `docs/design/architecture.md`; §4 environment is one line per tool; Figures 1 and 2 have captions but no paragraph explaining them; no implementation section for `include/engine/` and `demo/`; §8 has four bare URLs with no author or title, and the [2]-[4] numbers in §1.1 do not match the table. The paper is about 2,900 words.

**Merge first** (it doesn't count until it's in `develop` or `main`): branch 33-objective-24-implement-visual-editor-...: 1 commit not in develop; branch 64/Environment-Folder-Organization: 1 commit not in develop; develop is ahead of main by PRs #85 and #95; release it at sprint end (Wed Dec 2).

**To do in Sprint 4:**

1. Build the game demo stories #26-#29 (3 enemies, gameplay loop, input, building) in `prototype/include/demo/`, with a test per acceptance criterion before your presentation (Thu Dec 3).
2. For the Preview (Sun Nov 29) write §5 Outcomes, §6 Timeline for CPSC 491 (objectives, hours, milestones, assumptions) and §7 AI Usage with tools, tasks and fractions.
3. Write §4 Specifications and Design as prose from `docs/specs/game-engine.md`, `game-demo.md` and `docs/design/architecture.md`, with decisions and rejected alternatives (#87).
4. Add a §4 Implementation section on what the CMake prototype builds and tests, citing #63, #66, #67, #82, #84; explain Figures 1 and 2 in prose (#89, #90).
5. Create child issues under stories #26-#29, remove `sp:` from #46, and rewrite the §4 table with typed refs including #76, #78, #82, #84, #86-#94, #96, #97.
6. Merge the #33 branch with `Closes #N`; fix the 〈…〉 title in `prototype/README.md`, complete the four §8 entries, and release develop to main.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Monitors cross-chain bridge vaults, learns normal outflow, and alerts on drains with measured false alarms.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 27, about 23 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Release develop to main so the Preview (Sun Nov 29) shows the new §5-§7, then run the false-alarm count on the SonarX Jul-Oct window (#123).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 7 of 9 stories have child issues; all five open stories (#14, #17-#21) do; closed #5 and #16 have none. Closed stories #5 and #16 have no child issues; #117 and #126 are standalone tasks with no `sp:`; PRs #75 and #35 have no `Closes #N`, both closed and old; recent PRs #129-#132 close an issue. |
| 2. Paper §0–§8 (`develop`, ≈ 27 of 50+ pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities · ✅ §5 Outcomes · ✅ §6 Timeline (CPSC 491) · ✅ §7 AI usage · ✅ §8 References. Link tables in place of prose: Table 9 indexes the specs and design doc and Table 11 is the CPSC 491 schedule; each is backed by prose, so no section depends on a table alone. |
| 3. Prototype complete | ⚠️ partial | Detector, SQLite store, Ethereum poller, SonarX Snowflake-share source (#124, in release 0.4), five-hack replay, false-alarm evaluation, Slack notifier, FastAPI API, dashboard, demo mode. Not built or not tested yet: No live SonarX stream; false alarms on the SonarX window (#123), user test (#21: #121 script in open PR #133, #122) and stretch #19 not done; replay met target on 3 of 5. CI: develop 65c9839 green 11/26 22:52 PST; main fd41921 green 11/26 00:59 PST; Prototype job ran Install and test (Python), so team tests executed. Tests: Four files in `prototype/tests/` (detector, live loop, baseline, data pipeline); PR #129 added dashboard FR-1, FR-2, FR-4 criteria; proposal reports sixty tests. |
| 4. Word export (`develop`) | ✅ done | 86 issue citation(s) become small in-text tags; 57 issue(s) fill 4 table(s) in Appendix A. |
| Ready to present | ⚠️ partial | Paper has every section drafted on develop and the prototype runs in four modes on green CI, but the user test and SonarX false-alarm count are unfinished. |

**Issues under no story, without points:** 2: #117, #126. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Paper, what to write:** Whole paper is about 13,900 words, §4 about 7,900; well short of 50 pages, so expand §1, §3 and the results as Sprint 4 lands; `main` still has the old §5 ("does not use SonarX yet"), §6 and a §7 without fractions; release develop to main; §7 fractions are a `git blame` upper bound (97-99% for §0-§3); add which parts the team rewrote by hand and who verified each; §4 Planned activities and §5 need results for #123 (SonarX false alarms) and #121-#122 (user test) once done; Check §8 against any new citations added for Sprint 4, and keep every [N] in §1.1 matching its entry.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #133 - Objective 3.2 user-test session script (#121), open against develop; branch 93-cpsc491-timeline: 13 commits not in develop; §6 already merged, so merge by PR or delete; develop to main - §5-§7 update and cover; main proposal still has the old text.

**To do in Sprint 4:**

1. Write a test in `prototype/tests/` for each acceptance criterion of Objectives 2.2, 2.3 and 3.1, and fix the Harmony and Ronin replay misses (#97).
2. Finish #123 (false alarms on the SonarX window), merge #133 and run the four sessions of #122 before your presentation (Thu Dec 10); add results to §4 and §5.
3. Add `--sonarx` run steps and the share's window to `prototype/README.md`, which still treats SonarX as a future source class.
4. For the Preview (Sun Nov 29) extend §1, §3 and §4 toward 50 pages and release develop to main so the old §5-§6 text is gone.
5. Add `sp:` to #117 and #126, merge or delete `93-cpsc491-timeline`, and keep develop to main as one release at the end of Sprint 4 (Wed Dec 9).

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 15, about 35 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Replace the template text in §5 to §8 of `proposal/proposal.md` with real content, starting with §6 hours per objective for CPSC 491, for the Preview (Sun Nov 29).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 6 stories have child issues (#25, #27, #29, #30); #26 and #28 have none (tasks #46, #47, #53 hang off epic #21). `sp:` on 11 tasks under a story or under pointed tasks (#41-#43, #49, #51, #55, #57-#59, #65, #68); Eleven issues are not in the proposal: #41, #49, #51, #55, #57-#59, #62-#64, #76; 9 of 18 linked refs are untyped; #49 and #55 have no assignee; #74 has two and #76 three; #64 has no type label; Tasks hang off epics or other tasks: #46, #47, #53, #62 under epics; #51, #58, #59, #74, #76 under tasks; Standalone #62, #63, #64, #74 and #76 carry no `sp:`; 18 merged PRs lack `Closes #N`, including recent #75 and #67; main has 32 direct commits; Stories #29 and #30 are still open although login PRs #69 and #70 merged. |
| 2. Paper §0–§8 (`main`, ≈ 15 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ❌ §8 References. Template text 〈…〉 still in §5, §6, §7, §8 (15). Link tables in place of prose: §1.1 and §1.2 are tables, §2 is nine bullets, the spec and design index is a link table, and Planned activities is a 7-row table with no prose. |
| 3. Prototype complete | ⚠️ partial | Arcade login and preferences screens (#62), swipe on the main screen (#72), SQLite `db.py` and `schema.sql` (#64), Last.fm client; not shown wired end to end. Not built or not tested yet: Galaxy map, recommendations (#26, #28), persisted swipe history and restore on sign-in (#30); no test for any acceptance criterion. CI: main c2f301d (11/18 PST) green; Prototype job ran Install and test (Python), but no `prototype/tests/` exists, so CI tests no team code. No develop branch. Tests: none; no `prototype/tests/` folder although the README claims four tests. |
| 4. Word export (`main`) | ⚠️ partial | 16 issue citation(s) become small in-text tags; 16 issue(s) fill 3 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 15 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §8 are template text, the paper is far from 50 pages, and the prototype has screens and a database but no end-to-end flow or tests. |

**Issues under no story, without points:** 3: #62, #63, #64. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 2 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 2 of them aren't linked anywhere yet: #63, #64. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5 Project Outcomes, §6 Project Timeline, §7 AI Usage and §8 References still hold the template text; write all four, with CPSC 491 hours in §6; §1.1 is a four-row table with no prose and no citations; §8 has only the template examples. Add paragraphs arguing the difference, cited [1] onward; §1.2 is a table and §2 is bullets; write the problem statements and each epic and story as paragraphs ending in typed refs; §4 has no implementation details; describe `prototype/src/sonicscape` (screens, swipe, `db.py`, `lastfm.py`) with task refs; Whole paper is about 7,500 words; far short of 50 pages. Planned activities needs Sprint 3 and 4 work in prose.

**To do in Sprint 4:**

1. Write §5 Outcomes, §6 CPSC 491 Timeline with hours, §7 AI Usage with fractions and §8 References for the Preview (Sun Nov 29).
2. Rewrite §1.1, §1.2 and §2 as prose ending in typed refs, and cite sources numbered from [1] in §8.
3. Build the galaxy map and recommendations (#26, #28), then connect login, map, swipe and `db.py` so one run works end to end.
4. Add `prototype/tests/` with a test per acceptance criterion and fix the README run and test sections.
5. Remove `sp:` from child tasks, assign #49 and #55, link the eleven unlinked issues (#41, #49, #51, #55, #57-#59, #62-#64, #76) in §4 as typed refs, and give standalone tasks their own `sp:`.
6. Add Implementation details and Sprint 3 and 4 planned activities in prose to §4, and export the Mermaid figures as images.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: Project Rogue, 2D action roguelite with flexible builds (Unity)

*A Unity 2D action roguelite where builds develop through weapons, attributes and branching three-Act runs.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9, about 41 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Write §6 and §8 of `proposal/proposal.md` on develop and replace the template prompt in §7, so the Preview (Sun Nov 29) has every section drafted.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32 via #72, #35 via #64, #41 via #48); #33, #34, #36-#40 have none. #64 (under story #35) carries `sp:`; #65, #56, #53 sit directly under an epic; #20, #18, #15, #5 under tasks; #74 and #58 have no Sprint milestone; #26 and #13 are untyped with no milestone; #87 has two assignees; Fifteen issues are not linked from proposal.md: #86-#91, #76, #74, #72, #65, #64, #61, #58, #56, #53; Epics #29-#31 are cited in §1 and story #41 in §4; epics and stories belong in §2 only; Two proposal refs call #79 a task but the issue has no type label; #76, #74, #61, #26, #13 have no `sp:`. |
| 2. Paper §0–§8 (`develop`, ≈ 9 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities · ⚠️ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ⚠️ §7 AI usage · ❌ §8 References. Template text 〈…〉 still in the header block, §6, §8 (14). Link tables in place of prose: §4 Specification and design documents is a 5-row link table; Planned activities is a 28-row issue table with only four short paragraphs. |
| 3. Prototype complete | ⚠️ partial | Unity 6 project on develop: title screen, pause, retry and a one-room arena with three temporary enemies and an exit (#79); classes (#81), rooms (#83), run progression (#84). Not built or not tested yet: Enemies and encounters (#38), branching three-Act map (#39), playtests (#41), boons (#64); arena is one room, not a run; no automated tests. CI: develop c9d67ca green 11/24 15:09 PST and main d6e8c9a green 11/4 PST; Prototype job ran only Install and test (Python) on the scaffold, so no Unity code was compiled or tested. Tests: No automated tests; Editor scripts `ClassVerification.cs`, `ProgressionVerification.cs`, `MenuFlowVerification.cs` and the `Test_Combat` scene serve as manual checks. |
| 4. Word export (`develop`) | ⚠️ partial | 56 issue citation(s) become small in-text tags; 48 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 14 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ⚠️ partial | Title screen, arena, classes, rooms and progression run from develop, but §6 and §8 are template, §4 lacks specs and design prose, and the map is unbuilt. |

**Epic and story links outside §2:** 6 on `develop`: `[epic:#29]` in §1, `[epic:#30]` in §1, `[epic:#31]` in §1, `[story:#41]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 5: #13, #26, #61, #74, #76. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 15 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 9 of them aren't linked anywhere yet: #86, #87, #88, #89, #90, #91, #58, #74, #76. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §6 Project Timeline and §8 References are template text on both branches; write the CPSC 491 plan with hours and the cited sources; §7 AI Usage has only a task #79 disclosure above the template prompt; add all tools, tasks, fractions per artifact and verification, then delete the prompt; §4 Specifications: summarize the three goal specs in `docs/specs/` per epic with requirements and acceptance criteria; §4 Design: carry `system-overview.md` in; §4 Implementation covers only the title, pause and retry arena (#79); add classes (#81), rooms (#83), run progression (#84), combat and traversal; §5 still cites only PRs #44 and #45 and says no complete run; update it for the playable arena. Paper is about 5,100 words; main has template §3 and §4.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #92 - prototype menu implementation text for §4 (#86), open against develop; branch feature/40-node-reward-run-progression: 2 commits not in develop after #84; check and delete; branch feature/86-proposal-menu: 1 commit not in develop (PR #92); develop to main - §3 text, classes, rooms, run progression and arena; main last changed 11/4 PST.

**To do in Sprint 4:**

1. Write §6 CPSC 491 Timeline with hours per objective, finish §7 AI Usage with fractions and §8 References for the Preview (Sun Nov 29).
2. Build enemies and encounters (#38) and the branching three-Act map (#39), and connect the arena to rooms and progression, so a full run plays before your presentation (Thu Dec 10).
3. Add edit-mode tests for the resolver, classes and progression, and a CI step that runs them; record manual results in `prototype/README.md`.
4. Summarize the three goal specs per epic and `system-overview.md` in §4, embed the missing diagrams, and widen the Implementation subsection beyond #79 (#87).
5. Update §5 for the playable arena, #81, #83, #84; align §2 and §3 on classes versus weapon-and-element builds.
6. Create sub-issues for #33, #34, #36-#40, remove `sp:` from #64, milestone #74 and #58, link the fifteen unlinked issues, and merge develop into main at the end of Sprint 4 (Wed Dec 9).

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · G19: Titan Security, Radar over WiFi drone detection (RTX-2)

*Detect small drones and estimate position and movement from Wi-Fi CSI, compared against conventional radar.* · **Sprint 4: Nov 19 – Dec 9** · presentation Thu Dec 10 · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Sprint 4 bar:** the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8, about 42 to go), and a fully functional prototype with a test per acceptance criterion.

**Start here:** Merge PR #104, then write §5, §6 and §7 in `proposal/proposal.md` on develop, replacing every 〈…〉 block, for the Preview (Sun Nov 29).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 13 of 13 stories have child issues, but 8 children (#77-#84) have no type, assignee or Sprint milestone. #77-#84 are untyped, have no assignee or Sprint milestone, and none is linked from proposal.md; #99 is labelled user-story and task, carries `sp:` under story #97, and is cited as a task; 18 issues are not linked from §4, including #101, #98, #93, #75, #71, #53 and #43; #93 has no Sprint milestone; story #73 has no `sp:`; The §4 work-item table cites stories #6, #7, #13-#17; stories belong in §2 only; Sprint 3 (due 11/18) has 8 open and 4 closed issues; PR #104 is open. |
| 2. Paper §0–§8 (`develop`, ≈ 8 of 50+ pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities · ❌ §5 Outcomes · ❌ §6 Timeline (CPSC 491) · ❌ §7 AI usage · ⚠️ §8 References. Template text 〈…〉 still in §4, §5, §6, §7 (20). Link tables in place of prose: §4.3 is a link table with a leftover template placeholder block and no per-epic spec summaries; §4.4 is a 15-row table, with the prose in §4.5. |
| 3. Prototype complete | ⚠️ partial | CSI capture and quality-check scripts with a sample recording, preliminary feature extraction and event analysis (`features.py`, `event_analysis.py`, PR #102); scaffold `login.py` remains. Not built or not tested yet: Labeled datasets (#14), drone classifier (#15), distance tests (#16), radar comparison (#17); no detection slice and no tests for them. CI: develop 484bafe (11/18 PST) green; Install and test (Python) ran, but the only test is the course `test_login.py`, so no team code is tested. main 7fca571 (11/5 PST) is older. Tests: Only the course `prototype/tests/test_login.py`; nothing tests capture, quality check, features or event analysis. |
| 4. Word export (`develop`) | ⚠️ partial | 46 issue citation(s) become small in-text tags; 37 issue(s) fill 4 table(s) in Appendix A; your `proposal/to-word.lua` is not the current course version (Nov 18: it fits every picture to the page): replace it; 20 〈placeholder〉(s) are still in the text and would print in Word. |
| Ready to present | ❌ not ready | §5 to §7 are template, §4 lacks specs and implementation prose, and the prototype has capture and offline analysis but no detector and no team tests. |

**Epic and story links outside §2:** 7 on `develop`: `[story:#13]` in §4, `[story:#14]` in §4, `[story:#15]` in §4, `[story:#7]` in §4, `[story:#6]` in §4, `[story:#16]` in §4, `[story:#17]` in §4. Your goals (epics) and objectives (stories) are cited in §2 only. Take these links out of the other sections.

**Issues under no story, without points:** 6: #91, #37, #38, #51, #73, #93. An issue can exist without a story, but then it carries its own `sp:`. Give each of these its points.

**Issues outside your epics, not linked yet:** 5 issue(s) sit under no epic. That's fine as long as each carries its own `sp:`: your goals and objectives were set earlier, and such an issue can be linked from any place in `proposal.md`, the Appendix included. 3 of them aren't linked anywhere yet: #37, #38, #43. Link each one where the paper talks about that work, or list it in the Appendix. Issues created before Sprint 2, before your goals and objectives were final, don't need to be in the proposal and are not counted.

**Paper, what to write:** §5 Project Outcomes, §6 Project Timeline and §7 AI Usage are template text; write all three, with CPSC 491 hours per objective in §6; §8 carries a "retained from the draft, requires verification" banner and a TO CONFIRM line; verify each source and remove both; §4.3: delete the two placeholder rows, summarize `wifi-csi-sensing.md`, `drone-detection.md`, `evaluation.md` per epic (PR #104 open); §4: add the data model, key decisions with rejected alternatives, and what is not designed; add an Implementation section for `capture.py`, `features.py`, `event_analysis.py`; Resolve the draft-status banner and the TO CONFIRM in §1.1 (name the conventional radar systems); paper is about 3,700 words, far short of 50 pages.

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #104 - epic spec summaries and design narrative for #97, open against develop; develop to main - main last changed 11/5 PST and lacks all Sprint 3 work; branch feature/97-Documentation_for_project_proposal_enviornment: 1 commit not in develop.

**To do in Sprint 4:**

1. Merge PR #104 and write §5 Outcomes, §6 CPSC 491 Timeline with hours, and §7 AI Usage with fractions for the Preview (Sun Nov 29).
2. Collect labeled datasets (#14) and train the drone classifier (#15), then add pytest tests for capture, quality check, features and detection.
3. Replace `login.py` and `test_login.py`, and rewrite `prototype/README.md` run steps and the Sprint 3 row.
4. Type, assign and milestone #77-#84, link every child in §4 as a typed ref, fix #99.
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
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child issues (#13, #14, #15, #18, #19, #20, #22, #23). Only 11 refs are typed; 39 of 51 issue refs are bare `#N` or `Task `[#N]` links, mostly in §4; Sprint 3 (due 11/18) has 19 open and 17 closed issues; stories #14, #15, #18-#20, #22, #23 are open; Epics #12, #17, #21 sit in Sprint 4 while their stories sit in Sprint 3; The §4 table lists #41 under Type 'Task' but cites it as 'Feature'; fix the Type column. |
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
5. Move unfinished Sprint 3 issues to Sprint 4.
6. Delete the §3, §4 and §1.2 template text, align §1.1 with the maze concept, and add requirements per epic to the specs.

[↑ Back to all groups](#groups)

## About this page

This page checked Sprint 3 readiness (proposal §0–§4 and one working slice) from Nov 8 to Nov 19; those editions, and the Sprint 2 cards before them, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
