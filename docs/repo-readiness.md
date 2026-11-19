# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

## Word export check (Nov 19): fix these in `proposal.md`

I converted every group's `proposal/proposal.md` (both `main` and `develop`) with pandoc and the course converter, using the command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). All 20 convert without errors. The table below lists what still comes out wrong in Word, on the branch with your fuller proposal.

**Everyone: copy the updated converter first.** Since Nov 18, [`proposal/to-word.lua`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/to-word.lua) scales every picture to fit the page: at most 6.5 in wide and 8.5 in tall, aspect ratio kept. Before this, a tall diagram ran off the bottom of the page. Copy it, and [`proposal/reference.docx`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/reference.docx), into your `proposal/` folder, replacing your old copies. Then run the README command again.

**〈placeholders〉:** the converter warns about any 〈…〉 left outside the guidance quotes, and Word prints it as typed. Template text still in §5–§8 is expected until you write those sections, but none may remain in the final paper (due Sun Dec 20).

| Group | Branch | What comes out wrong in Word |
|---|---|---|
| G01 | `main` | Your `proposal/to-word.lua` is an edited copy; replace it with the course one. Otherwise clean. |
| G02 | `develop` | 〈…〉 in §5 and §7. |
| G03 | `develop` | No `proposal/to-word.lua` or `reference.docx`: add both. 〈…〉 in §1, §4, §5, §6, §7 and §8. One picture is taller than the page (fixed by the new converter). |
| G04 | `main` | 〈…〉 in §5–§7. Three pictures are taller than the page (fixed by the new converter). |
| G05 | `develop` | The header block still has 〈…〉 in the sponsor and the date, so the cover page leaves them blank. 〈…〉 in §0, §3, §4 and §5–§7. |
| G06 | `develop` | No `proposal/to-word.lua` or `reference.docx`: add both. 〈…〉 in §5–§7. |
| G07 | `main` | The header block's date is still in 〈…〉, so the cover page leaves it blank. 〈…〉 in §5–§7. One picture is 20 in tall (fixed by the new converter). |
| G08 | `develop` | Clean. |
| G09 | `develop` | No `proposal/to-word.lua` or `reference.docx`: add both. 〈…〉 in §5 and §6. |
| G10 | `develop` | The header block wraps your real values in 〈…〉 (title, group, team, sponsor, authors, date). The converter treats them as unfilled, so **the cover page comes out blank**: remove the brackets and keep the values. One picture is taller than the page (fixed by the new converter). |
| G11 | `main` | No `proposal/to-word.lua` or `reference.docx`: add both. 〈…〉 in §1 and §4–§8. |
| G12 | `develop` | 〈…〉 in §4, including a reference written `task:#〈n〉`: put the real issue number in. |
| G13 | `develop` | Clean. |
| G14 | `develop` | 〈…〉 in §5–§7. One picture is 16 in tall (fixed by the new converter). |
| G15 | `develop` | **25 references are plain text, `[story:https://…/issues/26]`, not links,** so the full URLs stay in your paragraphs and Appendix A is nearly empty. Write each one as a typed link: `[[story:#26]](https://github.com/…/issues/26)`. The table in §1 uses untyped `[#25](https://…/issues/25)` links; type them too (`[[feature:#25]](https://…/issues/25)`). 〈…〉 in §5–§7. |
| G16 | `develop` | Clean. |
| G17 | `main` | 〈…〉 in §5–§8. One picture is taller than the page (fixed by the new converter). |
| G18 | `develop` | Two diagrams are `.svg`. pandoc needs `rsvg-convert` to embed them for older Word versions and warns without it; export them as `.png` instead. 〈…〉 in §6–§8. |
| G19 | `develop` | 〈…〉 in §4–§7. One picture is taller than the page (fixed by the new converter). |
| G20 | `develop` | No `proposal/to-word.lua` or `reference.docx`: add both. 〈…〉 in §3, §5–§8 and in the References block above §8. One picture is taller than the page (fixed by the new converter). |

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.
>
> **Sprint 4 (G01–G05 and G11–G15 and G06–G10, now in Sprint 4):** Sprint 4 asks for the same three rules, taken to the finish. **Finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages** without the Appendix, and **complete the prototype so it is fully functional**. You run Sprint 4 on the board as usual, and I grade it on the same five rubric lenses. Your card shows the Sprint 4 bar and your page count so far. G16–G20: your card still shows the Sprint 3 review bar.

**CPSC 490 · Fall 2026 · swept 2026-11-19 20:47 UTC.** Earlier editions are kept in this file's git history.

**Jump to your group:**

| [**G01**](#g01) | [**G02**](#g02) | [**G03**](#g03) | [**G04**](#g04) | [**G05**](#g05) | [**G06**](#g06) | [**G07**](#g07) | [**G08**](#g08) | [**G09**](#g09) | [**G10**](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11**](#g11) | [**G12**](#g12) | [**G13**](#g13) | [**G14**](#g14) | [**G15**](#g15) | [**G16**](#g16) | [**G17**](#g17) | [**G18**](#g18) | [**G19**](#g19) | [**G20**](#g20) |

## The three rules of thumb

1. **Every PR references its issue, and every issue is linked from `proposal/proposal.md`.** Each PR says `Closes #N`. Epics and stories are cited in §2; every feature, task and sub-task is cited in §4 as a typed reference such as `[feature:#23]`. Every user story is broken down on the board into sub-issues: story → feature (or enhancement or bug) → task → sub-task. Features don't have to be code: "Write the functional requirements for X" counts. **Story points go on the user story only, once**; don't point its features or tasks. Every child issue has one assignee and the Sprint milestone, and moves across the board as you work. Steps: [git-workflow.md](https://github.com/kyoungshin/CPSC490/blob/main/docs/git-workflow.md); worked example: [#1 → #3 → #6 → #5 → #7](https://github.com/kyoungshin/CPSC490/issues/1).
2. **The proposal stands on its own as a technical paper.** The final paper (due Sun Dec 20) runs more than 50 pages in Times New Roman 11 pt, 1.5 spacing. The Appendix doesn't count toward that, and issue links move into the Appendix when `proposal.md` is converted to Word, so a table of issue links adds no pages. Write full paragraphs that explain the work and end each one with its issue references. **By your Sprint 3 review, §0–§4 should be complete:**
   - §0 Abstract, §1 Introduction, §1.1 Related Work (a pros-and-cons table across existing work, then prose on what you do differently), §1.2 Problem Statements, §2 Goals and Objectives, §3 Proposed Approaches.
   - **§4, the largest section:**
     - Environment and resources, with the reason for each choice.
     - One specification per epic: scope, functional and non-functional requirements, acceptance criteria and open questions ([model](https://github.com/kyoungshin/CPSC490/blob/main/docs/specs/example-spec.md)).
     - Design documents: context, components, data model, data flow, key decisions with the alternatives you rejected, and what isn't designed yet ([model](https://github.com/kyoungshin/CPSC490/blob/main/docs/design/example-design.md)).
     - Diagrams, each with prose that explains it.
     - Implementation details of what the prototype does.
     - The planned activities, written in prose.
   - Every spec, design section and diagram must be in `proposal.md`, either in full or summarized and linked from §4.
   - **In Sprint 4, finish the whole paper:** §0–§4 at full length plus §5 Project Outcomes, §6 Project Timeline (CPSC 491), §7 AI Usage and §8 References, more than 50 pages without the Appendix.
3. **The code under `prototype/` must always work, never be broken.** Whatever is in it has to install, run and pass CI (the *Prototype build & tests* job). For Sprint 3, build the slice your design depends on most, write a test for each of its acceptance criteria, and demo it at your review. In Sprint 4, complete it: every story in scope works end to end, with its tests. The folders mirror your architecture diagram, and `prototype/README.md` has run commands that work from a clean clone ([CI gate](https://github.com/kyoungshin/CPSC490/blob/main/.github/workflows/ci.yml)).

4. **Your proposal converts to Word.** I convert each group's `proposal/proposal.md` with pandoc and the course converter, using the one command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). **Updated Nov 8:** the converter (`proposal/to-word.lua` in the course repo) now pulls every GitHub issue link out of the text and lists it in *Appendix A. Issue References*, as tables grouped by type (epics, stories, features, tasks, sub-tasks). In the text, each link becomes a small citation such as `[task:#23]` that jumps to its row. Copy the new `proposal/to-word.lua` into your repository. To fill in the Title column, first export your issue titles with `gh issue list --state all --limit 1000 --json number,title > proposal/issues.json`. A reference only moves to the appendix if it's written as a link: `[task:#23](https://github.com/OWNER/REPO/issues/23)`.

As before, it only counts once it's **merged into `develop` or `main`**. Work left in a branch or an open pull request doesn't count yet.

| Groups | Sprint 3 | Sprint 3 review (start of Sprint 4) | Sprint 4 |
|---|---|---|---|
| G01–G05 | Oct 27 – Nov 9 | **Tue Nov 10** | Nov 10 – 30 |
| G11–G15 | Oct 29 – Nov 11 | **Thu Nov 12** | Nov 12 – Dec 2 |
| G06–G10 | Nov 3 – 16 | **Tue Nov 17** | Nov 17 – Dec 7 |
| G16–G20 | Nov 5 – 18 | **Thu Nov 19** | Nov 19 – Dec 9 |

**Updated Nov 19: Sprint 4 is one week longer for every group, because of Thanksgiving week.** It now ends the day before your group's presentation: Mon Nov 30 (G01–G05), Wed Dec 2 (G11–G15), Mon Dec 7 (G06–G10) and Wed Dec 9 (G16–G20). The full calendar is on the [sprint schedule](https://github.com/kyoungshin/CPSC490/blob/main/docs/sprint-schedule.md).

## Class at a glance

✅ done · ⚠️ partial · ❌ not there yet. **Pages so far** is a rough estimate (words outside the Appendix ÷ 500) to set against the 50-page final; tables and figures add a little more.

| Group | Now | 1. PRs ↔ issues ↔ proposal | 2. Proposal §0–§4 | 3. Prototype works | 4. Word export | Demo-ready | Pages so far (target 50+) |
|---|---|---|---|---|---|---|---|
| [G01](#g01) BGAF | Sprint 4 (Nov 10 – 30) | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ≈ 97 |
| [G02](#g02) Linux Larpers | Sprint 4 (Nov 10 – 30) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 15 |
| [G03](#g03) California | Sprint 4 (Nov 10 – 30) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Sprint 4 (Nov 10 – 30) | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 33 |
| [G05](#g05) Fighting Mongooses | Sprint 4 (Nov 10 – 30) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G06](#g06) GapWise | Sprint 4 (Nov 17 – Dec 7) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 6 |
| [G07](#g07) Mighty Morphins | Sprint 4 (Nov 17 – Dec 7) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 9 |
| [G08](#g08) Crime Busters | Sprint 4 (Nov 17 – Dec 7) | ✅ | ✅ | ✅ | ⚠️ | ✅ | ≈ 9 |
| [G09](#g09) Sigma Squad | Sprint 4 (Nov 17 – Dec 7) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 11 |
| [G10](#g10) Team Jiddak | Sprint 4 (Nov 17 – Dec 7) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 10 |
| [G11](#g11) 5 Guys | Sprint 4 (Nov 12 – Dec 2) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G12](#g12) ACJMM | Sprint 4 (Nov 12 – Dec 2) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G13](#g13) BYKX | Sprint 4 (Nov 12 – Dec 2) | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G14](#g14) G14 | Sprint 4 (Nov 12 – Dec 2) | ⚠️ | ✅ | ✅ | ✅ | ✅ | ≈ 11 |
| [G15](#g15) HIBBI-01 | Sprint 4 (Nov 12 – Dec 2) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) G16 | Sprint 3 review Thu Nov 19 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ≈ 25 |
| [G17](#g17) G17 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 15 |
| [G18](#g18) G18 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) G19 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 8 |
| [G20](#g20) G20 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 12 |

- **Rule 1 met:** 2 of 20 (G04, G08).
- **Proposal §0–§4 complete:** 4 of 20 (G01, G08, G14, G16).
- **Prototype working, with a real slice and tests:** 13 of 20 (G01, G02, G03, G04, G05, G06, G08, G09, G11, G12, G14, G15, G16).
- **Ready to demo both today:** 3 of 20 (G08, G14, G16).

**What changed since the last edition:**

- **G06–G10 are now in Sprint 4**, with G01–G05 and G11–G15. Sprint 4 asks for the same three rules, taken to the finish: the whole paper in `proposal.md` (§0–§8, more than 50 pages without the Appendix) and a fully functional prototype, graded on the five rubric lenses as usual. **G16–G20 have their Sprint 3 review tonight (Thu Nov 19)** and start Sprint 4 after it.
- **G16's proposal now passes rule 2, and G16 is demo-ready.** PRs #115 and #118 merged the Goal 2 and Goal 3 specs and the key design decisions into §4, and `develop` was released to `main`. Stories #19 and #21 still have no child issues.
- **G17 moved up on rule 3 and on demo readiness.** The login and preferences screens, the swipe screen and the SQLite layer merged, CI on `main` is green again, and the proposal grew from about 30k to 51k characters. There are still no tests for the team's own code.
- **G19's proposal moved from skeleton to partial.** `develop` gained the §4 environment, five embedded diagrams and the remaining-work prose. The epic summaries and design narrative are still in open PR #104, so they do not count yet.
- **G20 merged `develop` into `main` (#94)** with six diagrams, spec summaries, implementation prose, a maze, an objective tracker and a chasing enemy. Template text is still in §1.2, §3 and §4, and CI does not build the Unreal project, so write a manual test per acceptance criterion.
- **G01** merged the goal narratives (#345), the validation gate and its tests; the *Repository harness* job now fails on `main`. **G08** stays ✅ on all three rules and merged its release (#86). **G10's** `main` now holds the prototype (#80), but the *Repository harness* job is still red there. **G18** added starting classes (#81) and room scenes (#83) on `develop`; its proposal is unchanged.
- **Word export:** I converted every proposal again today. G10 fixed its broken reference. G03, G06, G09, G11 and G20 still have no `proposal/to-word.lua` or `reference.docx`.
- **No change since Nov 17:** G04, G05, G06, G13 and G14. G02, G03, G11, G12 and G15 changed only on the board or by small merges.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting (SNX-4)

*Pipeline that rebuilds Hyperliquid order books from SNX-4 data, validates them, and backtests strategies behind a gate.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 30** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 97), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Open the failed Repository harness run on main, fix the failing gate, then merge #349, #362 and #363 so cleaning is demoable end to end.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58 is dropped and has none); 11 stories are still open. Eleven tasks carry `sp:` under a story (#195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134): double counting; unchanged since the last edition.; Fourteen open child issues have no assignee (features #144, #145, #148, #157-#159, #163-#167, #169; tasks #94, #280).; Stories #23-#28 and about 30 back-end children lost their Sprint milestone on Nov 18 when the work moved to CPSC 491; #58 has none either.; 88 typed refs sit in §5, §6 or §8 instead of §2/§4; `[task:#151]` is cited four times but #151 is a sub-task; #369 is not linked yet (PR #370 open).; Three direct commits on main; PRs #8, #5, #4, #1 and other old PRs lack `Closes #N` (every recent PR has one).. |
| 2. Proposal §0–§4 (`main`, ≈ 97 pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: The document table in §4 and the objective status table in §2 are maps beside real prose; they do not replace it.. |
| 3. Prototype works | ✅ done | DuckDB schema and loader (`storage.py`, now with order-level tables via #343), cleaning (duplicate removal, block-order sort, gap finder) and `gate.py` (#350). Replay, validate, backtest, report still stubs. CI: Main run 11/18 17:11 PST: Prototype job green (Install and test (Python), pytest); Repository harness failed at 'Run gates'. Node steps skipped, so `prototype/frontend` is never built. Tests: `test_storage.py`, `test_clean.py`, `test_gate.py` (new, with fixtures in `prototype/tests/fixtures/`), `test_package.py`. |
| 4. Word export (`main`) | ✅ done | 805 issue citation(s) become small in-text tags; 225 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Proposal §0-§4 can be shown; the prototype demo is sample load, cleaning and the gate, with no replay or validation yet, and a CSV kept out of git. |

**Proposal, what to write:** §1.2 Problem Statements is 223 words plus a table; write each problem as a paragraph that names the goal it leads to.; §4 is now about 35,000 words in total; the replay design (#355) added text while #357-#359 trimmed some; remove repeated passages across specs, design and backtest design.; §4 Planned activities and §6 still say moved back-end work happens in Sprint 4; merge PR #370 so the text matches the Nov 18 plan.; §5 'What the prototype does today' is 192 words and still says only storage runs; update it for cleaning and the gate..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #349, #362, #363 (open, main): twice-identical cleaning test, one clean week from S3, known-event check; PR #352, #368 (open, main): strategy metrics in `report.py`; refuse data after a decision time; PR #367 (open, main): front-end build, lint, typecheck and test; PR #370, #371 (open, main): proposal §4/§6 for the CPSC 491 move; replay design summary; PR #356 (open, main): timeline figure for §6.

**To do in Sprint 4:**

1. Find which gate failed in the Repository harness 'Run gates' step on main (run of Nov 18 17:11 PST) and fix it so main is green again in Sprint 4.
2. Merge #349, #362, #363, #368, #352 with a test per acceptance criterion, then update `prototype/README.md` layout, test list and the §5 prototype paragraph.
3. Remove `sp:` from tasks #195, #187, #184, #183, #181, #180, #175, #174, #173, #172 and #134; points stay on the story only.
4. Assign one person to each open child without an assignee (#144, #145, #148, #157-#159, #163-#167, #169, #94, #280) and give each child kept in Sprint 4 a milestone.
5. Merge #370, change the four `[task:#151]` refs to `[sub-task:#151]`, and move work-item refs out of §5, §6 and §8.
6. Rewrite §1.2 as paragraphs and shorten repeated passages in §4; run `npm ci` and `npm run build` in `prototype/frontend` before your Sprint 4 review.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 30** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 15), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Write the Goal 1 spec (scope, FRs, NFRs, acceptance criteria, open questions) into §4; it unblocks the design and implementation text and sets the prototype tests.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); 10 stories (#49, #51-#55, #58-#61) have none. Ten of 15 user stories have no child issues; break each into feature, task, sub-task on the board.; 21 tasks carry `sp:` under a story (double counting): #95, #92, #91, #86, #84, #81, #77, #69, #68, #41 ...; Thirteen child issues lack exactly one assignee (#68, #67, #41, #39, #38, #36, #25 ...); six meeting issues have no type label.; #130, #99 and epic #20 are not linked from the proposal; some epic/story refs sit in §3.; Eight direct commits on develop and one on main; PRs #3, #4, #5, #14 lack `Closes #N`; PRs #133 and #127 are open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §2 uses bullets with refs; §4 'Specification and design documents' is a template comment plus a 5-row table with no spec or design prose.. |
| 3. Prototype works | ✅ done | FastAPI `/health`, `/health/db`, POST/GET `/observations` on PostgreSQL via Compose; Angular starter page; ESP32 firmware is a skeleton with no capture yet. CI: Develop run 11/17 18:41 PST green; Prototype job ran Python install and pytest on the backend. Angular and ESP32 projects are not built in CI; main run is green but older. Tests: `test_main.py`, `test_observations.py`, `test_observation_model.py` (in-memory SQLite); Angular `app.spec.ts` not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 125 issue citation(s) become small in-text tags; 75 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Backend ingest and query can be demoed; no live ESP32 capture or dashboard data, and §4 specs, design and implementation are not written. |

**Proposal, what to write:** §4 Specifications: no spec per epic exists; `docs/specs/` holds only the scaffold example. Write scope, FRs, NFRs, acceptance criteria and open questions for Goals 1-3.; §4 Design: `docs/design/architecture.md`, `data-flow.md`, `system-context.md` exist but §4 carries only figures and a table row; summarize components, data model, decisions, rejected alternatives, undesigned parts.; §4 Implementation details is absent; describe the backend API, PostgreSQL tables, ESP32 firmware and dashboard as built, with task refs.; §1.1 is one table plus a short paragraph and §1.2 is about 215 words; main still holds the unfilled template for §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — §3, §4 environment and planned activities, observation API; merge into main; PR #133 (open, main) — develop-to-main merge; get it reviewed and merged; PR #127 (open, develop) — review and merge or close; Branch feature/114-restart-persistence — 3 commits not in develop.

**To do in Sprint 4:**

1. Write one spec per epic (Goals 1-3) in `docs/specs/` and summarize each in §4 with FRs, NFRs, acceptance criteria and open questions.
2. Add a §4 design narrative from `docs/design/*.md`: data model, decisions with rejected alternatives, what is not designed yet.
3. Add a §4 Implementation subsection describing the backend API, tables, firmware and dashboard, ending in task refs.
4. Create child issues for stories #49, #51-#55, #58-#61 and remove `sp:` from the 21 tasks (#95, #92, #91 ...).
5. Get one ESP32 observation into the dashboard via the API, with a test per acceptance criterion and a CI build for `prototype/dashboard`.
6. Link #130, #99 and #20 from the proposal and merge develop into main (#133).

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 30** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Fix `prototype/README.md` so a fresh clone runs the transcriber-to-training pipeline; the demo depends on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 13 stories have child issues; 9 stories have none. Nine of 13 user stories have no child issues; break each into feature, task, sub-task on the board.; 28 issues are not in the proposal (#86, #85, #84, #78, #72, #71, #70 ...); 19 issues carry no type label (meetings, writing tasks).; 22 non-story issues have no parent; #86 has no assignee and #45 no Sprint milestone; #85, #75, #68, #55, #53 are also unplaced.; PRs #81 and #77 (Sprint 3) have no `Closes #N`; PR #83 is open; one direct commit on main and on develop.; Six refs are bare or point at the wrong issue number; only 12 of 18 refs are typed.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §2 is a bullet list with refs; §4 'Specification and design documents' and 'Planned activities' are small tables, not prose; §4 opens with the unfilled template prompt.. |
| 3. Prototype works | ✅ done | Transcriber router and recognizer, verifier, dataset generation, storage and display, PyTorch training, equation plotting, and a pipeline notebook. CI: Latest develop run (11/9 21:27 PST) green; Prototype job ran Python install and pytest on team code. Main CI is green but older, before most of the prototype landed. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train and plot_equation tests; none named for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The prototype pipeline is demoable from develop, but §4 is mostly missing and the README run steps do not work. |

**Proposal, what to write:** §4 Environment and resources is still the template prompt; name each tool, platform, hosting and the sponsor's notebook requirement with the reason.; §4 Specifications: `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` exist but are only indexed; summarize each with FRs, NFRs, acceptance criteria.; §4 Design: `docs/design/architecture.md` gets one paragraph; add data model, key decisions with rejected alternatives, and what is undesigned.; §4 Implementation and Planned activities are a 3-row table; describe the built transcriber, verifier, trainer and remaining work in prose with refs.; §1 Introduction is about 300 words and §1.2 is about 50 words with a placeholder; both need real paragraphs..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — transcriber, recognizer, training, plotting, notebook, specs; merge into main; PR #83 (open, develop) — review and merge or close.

**To do in Sprint 4:**

1. Rewrite `prototype/README.md` with working install, run and test commands; remove the course `login.py` references.
2. Replace the §4 template prompt with Environment prose: each tool, platform and hosting choice with its reason.
3. Summarize `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` in §4 with FRs, NFRs and acceptance criteria.
4. Expand the §4 design section from `docs/design/architecture.md`: data model, decisions and rejected alternatives, undesigned parts.
5. Create child issues for the nine stories without breakdown, with one assignee and a Sprint milestone each; link them all in §2/§4, including #86.
6. Add a test per acceptance criterion (dataset generate, store, display), add `Closes #N` to PRs, and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and trader profitability analytics

*Compute profit and loss per Polymarket wallet from SonarX Polygon data, rank traders, and show them on a dashboard.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 30** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 33), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge the five open PRs (#150, #156, #158-#160), then expand §4 Environment and resources into one subsection per tool with reasons.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 12 of 12 stories have child issues (feature, task, sub-task); 11 stories still open. Five PRs (#150, #156, #158, #159, #160) open against develop, touching proposal, specs and tests; merge them.; Eight feature branches (#55, #58, #59, #105, #125, #142, #149, dashboard-questions) have commits not in develop.; #20 has no assignee; 22 standalone writing and process tasks (#155, #154, #152 ...) have no parent story.; PR #4 (Sprint 1 team README) has no `Closes #N`; no recent PR lacks one.. |
| 2. Proposal §0–§4 (`main`, ≈ 33 pages) | ⚠️ partial | ⚠️ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §1.2 is a 4-row table with no prose; §1.1 is one paragraph plus a 6-row table. Specs, design and planned activities are prose with typed refs.. |
| 3. Prototype works | ✅ done | Settings loader, Snowflake client, smoke query, FIFO position builder and resolution matching checked against the spec's worked example; no live data run, ranking or dashboard. CI: Latest main run green; Prototype job ran Python install and pytest. The live-Snowflake integration test is skipped without credentials. Tests: `tests/unit/` positions, resolutions, settings, snowflake_client; `tests/integration/test_smoke_query.py` (skipped); worked-example fixture. |
| 4. Word export (`main`) | ✅ done | 119 issue citation(s) become small in-text tags; 105 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Paper is largely demo-ready; the prototype shows tested PNL logic on fixtures, but no live data, ranking or dashboard yet. |

**Proposal, what to write:** §4 Environment and resources is one paragraph; it says dashboard framework and result storage are not chosen. Add a subsection per tool or platform with reasons.; §0 Abstract is 148 words in one paragraph; state problem, approach, method and expected results.; §1.1 Related Work: add prose arguing what this project does differently from each compared tool, with citations matching §8.; §1.2 Problem Statements: write a paragraph per problem (P1-P4) explaining why it matters, instead of table rows..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #158 — read-only SQL extract module and tests; PR #159 — Goal 3 dashboard specification; PR #156 — dashboard questions update; PR #150 — proposal §5 to §7 draft and stale §4 fixes; PR #160 — final Sprint 3 review numbers.

**To do in Sprint 4:**

1. Merge PRs #158, #159, #156, #150 and #160 so the specs, tests and review are on develop and main.
2. Expand §4 Environment and resources: one subsection per tool or platform, with the reason, including the dashboard framework decision.
3. Rewrite §0 Abstract, §1.1 Related Work and §1.2 Problem Statements as full paragraphs, with citations matching §8.
4. Run the position builder on real SonarX data end to end and demo one wallet's PNL.
5. Assign #20 and give each standalone task a parent story or label it a writing task.
6. Delete the eight stale feature branches once merged.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, whale identification and location system

*Detect whale calls with an AI model and locate them from hydrophone recordings.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 30** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 5), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge PR #72 and develop into main and fix the harness gate so main CI is green; then write §0 and §3.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 9 stories have child issues; #10-#13, #15, #16, #18 have none (tasks hang off epics #8 and #14). Seven of nine user stories have no child issues; tasks attach to epics instead of stories.; 15 tasks are not linked from the proposal (#47, #56-#58, #61, #63, #65-#71, #73, #23).; Seven issues have no assignee (#69, #68, #67, #61, #57, #56, #20); five have no Sprint milestone (#71, #68, #61, #57, #47).; Epic and story citations sit in §4 instead of §2 only; 15 tasks have no parent.; PR #72 and PR #62 are open against develop; every merged PR has `Closes #N`.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ❌ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ❌ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §2 is a bullet list; §4 'Planned activities' is an 18-row link table with 224 words of text and no prose; the spec and design index is a 5-row table with a template row left.. |
| 3. Prototype works | ✅ done | Locator: TDOA direction and distance from simulated hydrophones, 20-scenario check, interactive direction demo, call saving; detector train and detect scripts. CI: Latest develop run green; Prototype job ran Python install and pytest. Latest main run is red: the Repository harness gate failed, though the prototype job passed. Tests: `tests/` test_tdoa, test_locate, test_save_call, test_speed_of_sound, test_scenarios (20 scenarios, 80% pass); ai-detector scripts untested. |
| 4. Word export (`develop`) | ⚠️ partial | 48 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Locator demo and 20-scenario check run today; the proposal still has a placeholder abstract and template §3 and §4, and main CI is red. |

**Proposal, what to write:** §0 Abstract is a placeholder; sponsor and date in the front matter are still template text.; §3 Proposed Approaches is the template prompt; state the strategy, alternatives considered and reasoning for the detector and locator.; §4 Environment and resources is the template prompt; list each tool, dataset, hosting and sponsor resource with the reason.; §4 Specs and design: locator spec and design are summarized; summarize `goal-1-detector.md` and `ai-detector-design.md` too and delete the placeholder row.; §4 has no diagrams in proposal.md and no Implementation section; add captioned figures and describe the built code..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #72 — fills proposal §4 (branch fill-section-4-proposal.md, 3 commits); PR #62 — remerge main into develop (schema and ER diagram); Branch develop — scenario tests, direction demo, detector and locator design docs; main CI red.

**To do in Sprint 4:**

1. Merge PR #72 and PR #62, then merge develop into main and fix the failing harness gate so main CI is green.
2. Write §0 Abstract and fill the sponsor and date in the front matter.
3. Replace the §3 template prompt with strategy, alternatives and reasoning.
4. Write §4 Environment and resources, summarize the detector spec and design, add the architecture diagram with a caption, and describe the built prototype.
5. Create child issues under stories #10-#13, #15, #16, #18; give #69, #68, #67, #61, #57, #56 an assignee and Sprint milestone.
6. Fix the `prototype/README.md` run commands and add tests for `ai-detector/`.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Turns a student's notes into practice questions and tracks per-concept mastery and forgetting to target weak spots.* · Sprint 3 review held Tue Nov 17 · **Sprint 4: Nov 17 – Dec 7** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 6), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge develop into main, then rewrite §4 Components, Data Model and Key Decisions as paragraphs with typed refs and rejected alternatives.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 17 stories have child issues; #14, #18, #19, #21, #28, #29, #31 have none (#5, #6 are old closed leftovers). Feature PRs close stories directly (#39 for #21, #53 for #18, #54 for #19, #56 for #29); no feature, task or sub-task sits between.; Tasks #74-#77 (filed today) have no assignee, no Sprint milestone, and are not in the proposal.; Fourteen issues are not linked from the proposal, among them #43, #49, #51, #58, #60 and #73-#77.; §4 Planned activities uses bare `#10`, `#36`, `#41` instead of typed refs; stories #5 and #6 have no assignee.; Only #40 (closed) lacks `Closes #N`; no direct commits. About 18 feature branches are unmerged.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Environment is an 8-row table with reasons of a few words; Planned activities is an 8-row table of mostly finished items; specs are a list of links.. |
| 3. Prototype works | ✅ done | `run_demo.py` takes a notes file through document processing, concept extraction and question generation (template mode, no API key); mastery, forgetting, selector, grader are modules not yet wired in. CI: develop run 11/16 19:48 PST green; Prototype job ran Install and test (Python) with team tests. main run 11/15 green but holds fewer modules. Tests: 12 team test files on develop (document processor, concepts, questions, selector, mastery, forgetting, grader, override, summary, timer, demo); flashcards JS test is not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 27 issue citation(s) become small in-text tags; 24 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | The command-line demo runs from a fresh clone on develop, but §4 is thin, the specs and design sit only on develop, and no web app exists. |

**Proposal, what to write:** §4 specs: `docs/specs/specs-epic-1.md` to `-3.md` are only linked; summarize each in §4 with scope, functional and non-functional requirements, acceptance criteria, open questions.; §4 design is bullet lists (Components, Data Model, Key Decisions, about 430 words); write each as paragraphs and name the rejected alternative for every decision.; §4 has no implementation details: describe what the prototype modules do and how they were tested, with the task refs.; §3 (165 words) and §1 (375 words) are brief; the two figures are hotlinked images that may not survive Word export..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop: holds the specs, design doc, §4 sections and newest features; main stopped at merge #63 on 11/15; feature branches (feature/25-flashcard-system, feature/21-mastery-tracking and others): merge into develop or delete; branch 71-link-specs: 3 commits not in develop; merge or close.

**To do in Sprint 4:**

1. Merge develop into main (reviewed PR with `Closes #N`) so the proposal, specs and demo are on one branch before your Sprint 4 review.
2. Rewrite §4 Components, Data Model, Data Flow and Key Decisions as paragraphs, each ending with typed issue refs; add rejected alternatives for every decision.
3. Summarize `docs/specs/specs-epic-1.md` to `-3.md` inside §4: scope, functional and non-functional requirements, acceptance criteria, open questions.
4. Create child issues under stories #14, #18, #19, #21, #28, #29, #31; give #74-#77 an assignee and Sprint 4 milestone; link them in §4.
5. Add a §4 implementation section for the prototype modules and replace the Planned activities table with prose.
6. Wire `mastery_tracker`, `question_selector` and `grader` into `run_demo.py` and refresh `prototype/README.md`.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (EL-1)

*Extracts material data from vendor certificates and test reports, stores it after human review, and supports analysis.* · Sprint 3 review held Tue Nov 17 · **Sprint 4: Nov 17 – Dec 7** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Rewrite `prototype/README.md` for the real prototype and add one tested slice, then carry the three specs and the design documents into §4 as prose.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 16 of 16 stories have child issues; all stories have an assignee and a Sprint milestone. Seventeen new features #151-#167 (children of stories #12-#19) have no assignee and are not linked from the proposal.; Thirty-one issues are bare refs in the proposal, not typed refs (#28-#59 among them); §2 now writes `story#48` and `story#49` without a colon.; Nineteen story refs sit in §4; epics #1, #4, #45 are cited outside §2; wrong ref types: `[task:#78]`, `[task:#94]`, `[task:#103]`, `[bug:#117]`, `[task:#134]`-`[task:#136]`.; Task #38 carries `sp: 3` under story #48 (double counting); #28 has no Sprint milestone; #147-#149 have no assignee.; Three direct commits on main; PRs #168, #145, #143, #140, #102, #99 are open.. |
| 2. Proposal §0–§4 (`main`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a 76-row table (48 issue links) with no prose; the 12-row document table stands in for specification and design writing.. |
| 3. Prototype works | ⚠️ partial | Static HTML mock-ups, `prototype/index.html` and `ui-tabs/search-view.html` (PR #101); no back end, extraction or database code. CI: Main run 11/17 14:29 PST green; Prototype job ran Install and test (Python), but the only test is the course `tests/test_login.py`. Tests: none for team code; only the course `tests/test_login.py`. |
| 4. Word export (`main`) | ⚠️ partial | 129 issue citation(s) become small in-text tags; 96 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A static search page can be shown, but §4 is mostly links and tables, the README is the course template, and no team code is tested or runs. |

**Proposal, what to write:** §4 specs: the three goal specs in `docs/specs/` (renamed `goal-1-...`, `goal-2-...`, `goal-3-...`, each 5,600-6,400 characters) are only linked; summarize each in §4 (PR #145 is open).; §4 design: five figures, but only Figure 3 has explaining prose; add components, data model, data flow and key decisions with rejected alternatives, using `technology-stack-decision.md`.; §4 Environment is a table with short purposes; add a paragraph per choice (Snowflake, AWS, FastAPI, OCR tool) giving the reason and rejected option (PR #143 is open).; No implementation section: describe the static search view and what remains to be built; replace the 76-row table with prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #145 (open, main): goal specification summaries added to the proposal; PR #168 (open, main): Review 3 write-up, closes #150; PR #143 and #140 (open, main): data-flow update and environment table; PR #99 and #102 (open, main): page-5 and search-view sequence diagrams; Eight unmerged branches, among them `proposal-environment-reasoning` and `update-data-flow`.

**To do in Sprint 4:**

1. Merge PR #145 and #143, then confirm §4 carries each goal specification and the environment reasoning as prose, not only a link to `docs/specs/`.
2. Assign one person to each of features #151-#167 and tasks #147-#149, and link them in §4 with the correct typed refs.
3. Write §4 design as paragraphs: system context, components, data model, data flow, key decisions with rejected alternatives, and what is not designed yet.
4. Replace the Planned activities table with paragraphs, convert the 31 bare issue refs to typed refs, and fix `story#48`, `story#49` in §2.
5. Rewrite `prototype/README.md`, replace the course `login.py` and `test_login.py`, and implement one slice (upload, extraction, review) with a test per acceptance criterion.
6. Move story refs out of §4, type the epic refs #1, #4, #45, and remove `sp:` from #38.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: interactive crime map and database

*Normalizes public Costa Mesa crime-call data into SQLite and shows it on a filterable Leaflet map.* · Sprint 3 review held Tue Nov 17 · **Sprint 4: Nov 17 – Dec 7** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Finish #27 with a test per acceptance criterion, so the Sprint 4 prototype is complete rather than a map slice.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 8 of 8 stories have child tasks (new #93 under #13). Closed legacy issues #45-#47 (untyped objectives), #6 and #7 are not in the proposal and have no Sprint milestone.; Sprint 1 PRs #37, #39, #40 lack `Closes #N`; every later PR, including #94, has one.; #27 (marker display and selection) is still open under the Sprint 3 milestone, which is past due.; No direct commits, no `sp:` under a story, every linked child has an assignee and milestone.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ✅ done | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: none; §4 is prose with typed refs at the end of each part.. |
| 3. Prototype works | ✅ done | Normalizes a Costa Mesa snapshot into SQLite, serves `/api/incidents`; Leaflet map shows incidents with a crime-type filter, marker updates and highlight. CI: develop run 11/18 22:07 PST green and main run 11/17 19:49 PST green; the Prototype job ran Install and test (Python) on the team test files. Tests: `test_normalize.py`, `test_load_db.py`, `test_area_filter.py`, `test_crime_frequency.py`, and new `test_app.py` for the map and incidents routes. |
| 4. Word export (`develop`) | ⚠️ partial | 47 issue citation(s) become small in-text tags; 47 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ✅ ready | Release #86 is on main and develop adds route tests; §0-§4 are prose and the Flask and Leaflet map runs from a fresh clone. |

**Proposal, what to write:** §4 Figure 3 (the ER diagram) is still only a link; embed the image with a caption and walk through the entities.; §4 Goal 1-3 requirements are compact: add a non-functional requirements paragraph and an open-questions list per goal, as in `docs/specs/example-spec.md`.; §1.1 (369 words) needs prose arguing what this project does differently from the existing crime maps; §1 and §1.2 are also short.; The paper is about 6,500 words; the final paper needs more than 50 pages without the Appendix, so §5-§8 and every §0-§4 section must grow in Sprint 4..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is one PR ahead of main: PR #94 route tests and the §4 test paragraph are not on main; branch 83-update-prototype-readme: 4 commits not in develop; merge or delete.

**To do in Sprint 4:**

1. Release `develop` to main again so PR #94 (`prototype/test_app.py`) and the §4 test paragraph reach the default branch.
2. Finish #27 and write a test for each acceptance criterion of the marker selection and filter stories before your Sprint 4 review.
3. Embed Figure 3 (ER diagram) in §4 with a caption and one paragraph on the tables.
4. Add non-functional requirements and open questions to each Goal 1-3 specification in §4.
5. Expand §1, §1.1 (what Crime Busters does differently from existing maps) and §1.2, then write §5-§8 toward the 50-page paper.
6. Close legacy issues #45-#47, #6, #7 or give them a type label and Sprint milestone; delete branch 83-update-prototype-readme.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · Sprint 3 review held Tue Nov 17 · **Sprint 4: Nov 17 – Dec 7** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge release PR #110 so main shows the working prototype, then write the §4 implementation section.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 10 stories have child issues; #37 and #38 have none (#33 gained #91). #80 carries sp: 1 under story #32; #57, #101, #111 and #112 carry sp: under pointed tasks.; #106 is open with no Sprint milestone and is not linked in proposal §4; #112 (PR #114 open) is not linked yet.; Stories #37 and #38 have no child issues; #59 hangs off epic #28, not a story.; PR #20 (old draft) has no Closes line; all Sprint 3 and Sprint 4 PRs close an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 11 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a table that indexes eight docs without summarizing them; Planned activities is a 46-row issue-link table with one intro paragraph.. |
| 3. Prototype works | ✅ done | Vehicle selection, service-record API and CRUD, manual entry and CSV import forms, dashboard with edit/delete, mileage entry, and status-label recommendations for three service types. CI: develop 11/19 00:48 PST green: the Prototype job ran Install and test for Node and Python, so API and UI tests executed. main 10/22 green but scaffold only. Tests: Seven pytest files (vehicle and service-record APIs, label, engine, interval) and seven `tests/ui/*.test.js` page tests. |
| 4. Word export (`develop`) | ⚠️ partial | 58 issue citation(s) become small in-text tags; 58 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | The Sprint 3 prototype runs from develop with green CI, but §4 specs and design are index-only, no implementation section, and main is still scaffold until #110 merges. |

**Proposal, what to write:** §3 is about 190 words; add alternatives beyond rules versus AI (Flask versus other stacks, SQLite versus hosted database) with reasons.; Five specs in `docs/specs/` are only indexed; summarize scope, requirements, acceptance criteria and open questions per epic in §4 prose.; Design lacks decisions with rejected alternatives and a not-yet-designed list; `docs/design/architecture.md` and `maintenance-dashboard.md` are not carried by proposal.md.; No §4 implementation prose: describe the service-record API, entry and import forms, dashboard, label rule and their tests, ending in task refs.; The paper is about 6,500 words and §5-§8 are not written; the final paper needs more than 50 pages without the Appendix..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #110 (open, develop to main): release of Sprint 2 and 3 work; main is still scaffold; PR #114 (open, develop): update course files; branch feature/98-sprint-3-review: 8 commits not in develop; branch feature/106-list-epic-27-spec: 2 commits not in develop; PR #107 closed unmerged.

**To do in Sprint 4:**

1. Merge release PR #110 with CI green on main so the default branch shows the prototype and proposal.
2. Write the §4 implementation prose for the vehicle, service-record, dashboard and recommendation code and its tests, ending in typed refs.
3. Summarize the five specs and `docs/design/architecture.md` in §4: requirements, acceptance criteria, decisions with rejected alternatives, open questions.
4. Remove sp: from #80, #57, #101, #111, #112; give #106 a Sprint milestone and link #106 and #112 in §4.
5. Add child issues for stories #37 and #38 and re-parent #59 under a story; complete #91.
6. Expand §3 alternatives, write §1.2 as paragraphs, replace the work-item table with prose, then write §5-§8 toward 50 pages.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · Sprint 3 review held Tue Nov 17 · **Sprint 4: Nov 17 – Dec 7** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 10), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Fix the failing Run gates job on main, then rewrite `prototype/README.md` so the demo runs from a fresh clone.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 1 of 14 stories has child issues (#31 gained #82); #46 and #69 hang off epic #15, not a story. Stories #25-#30, #32, #33, #38, #39, #53-#55 have no child feature, task or sub-task issues.; #82 carries sp: 1 under story #31; #56 carries sp: under pointed task #13; #69 is labelled epic with sp: 5.; #33 and #38 are open with no assignee; #73 and #74 have no Sprint milestone; #3 is untyped.; #82, #74, #73 are bare refs in §4; #83 is not linked; `[epic:#15]` is cited in §4 instead of §2.; 14 direct commits on main, including repo restructuring; all 34 PRs close an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned Activities (5 bullets) and Tracked Task Issues (28 bullets) are lists; Specification and Design Documents is a link list followed by pasted doc text.. |
| 3. Prototype works | ⚠️ partial | Goal 1 network model: transfer CSV to wallet graph, derived views, time-respecting cycles, metrics and reconciliation checks via `demo.py` on a synthetic sample. CI: develop 11/18 20:57 PST green (Prototype job ran Install and test (Python)); main 11/17 14:24 PST red on Repository harness (Run gates), Prototype job green. Tests: 31 tests in `tests/test_requirements.py` and `tests/test_acceptance.py` in the nested prototype folder; plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 46 issue citation(s) become small in-text tags; 45 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A tested Goal 1 demo runs on develop from the CLI and PR #80 put it on main, but there is no UI, run steps are wrong, and specs and design are thin. |

**Proposal, what to write:** §1.1 compares only two vendors with one citation; add academic and open-source detectors and cite them in §8.; §1 Introduction is about 155 words; explain the domain, why wash trading matters and the sponsor context.; Goal 1 specification is now a prose paragraph on the graph model; add requirements, acceptance criteria and open questions, and finish Epic #24.; Five diagrams have one-line captions; add prose per figure, decisions with rejected alternatives, and what is not designed yet.; No §4 implementation prose for `prototype/goal1-network-model-prototype/`; pasted `# Goal 1` headings sit outside the outline. The paper is about 5,600 words; the final needs more than 50 pages..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is ahead of main: Goal 1 spec prose and reference [18] in proposal.md are not on main; branch feat/69-goal1-network-model-prototype: 2 commits not in develop.

**To do in Sprint 4:**

1. Fix the Run gates failure on main so the default branch is green, then release develop to main.
2. Rewrite `prototype/README.md` and the nested README so run and test commands work from `prototype/goal1-network-model-prototype/`.
3. Create child issues under each remaining story (start with #32, #25-#27), each with one assignee and a Sprint milestone; drop sp: from #82, #56, #69.
4. Write a §4 Implementation section for the `stablescope/` modules and the 31 tests, ending in typed refs; build the Goal 2 and Goal 3 slices with a test per acceptance criterion.
5. Summarize the Epic #23 and #24 specs fully and explain each diagram in prose with decisions and rejected alternatives.
6. Expand §1 and §1.1 with sources cited in §8, write §5-§8, and stop direct commits to main.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

*Phone app records a marathon runner's GPS to Firebase; spectators follow on a web page; pace and finish-time prediction.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – Dec 2** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Build the spectator view (#69) so your Sprint 4 demo shows a phone's GPS position reaching a web page through Firestore.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33); 45 of 49 issues linked from the proposal. `sp:` removed from #62; #1, #2, #6 are now typed and assigned, but still not linked from the proposal.; PR #39 closes #21, which `proposal/proposal.md` does not link; new task #88 (to fix this) has no parent and is not linked either.; Open stories #28, #29, #30, #31, #33 and all Sprint 4 features have no merged PR yet.; One direct commit (`.github` scaffold) on main and develop; every PR closes an issue.. |
| 2. Proposal §0–§4 (`main`, ≈ 9 pages) | ⚠️ partial | ⚠️ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; the specs and design docs stay in `docs/` and the proposal carries only one Goal 3 paragraph.. |
| 3. Prototype works | ✅ done | Expo app with Firebase client, runner GPS tracking module (`runner-app/tracking.js`), Firestore smoke test, and pace calculation (`prediction/pace.py`). Spectator view is only a README placeholder. CI: main CI green 11/12 (720486b); Prototype job ran Node install and test (jest) and Python install and test. develop green but still the login scaffold. Tests: 3 test files: `__tests__/App.test.js`, `__tests__/tracking.test.js` (jest) and `prediction/test_pace.py`; all run in CI. |
| 4. Word export (`main`) | ⚠️ partial | 50 issue citation(s) become small in-text tags; 45 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A phone-GPS-to-Firestore demo and pace test can run, but §4 is incomplete and the spectator view (#69) that ties it together is not built. |

**Proposal, what to write:** §0 Abstract describes an ML performance-analysis app; the goals are live tracking, posts and a spectator page. Rewrite it to match §2.; §1 and §1.1 still hold template quote blocks and a stray 〈Your survey〉 placeholder; §1.1 ends mid-sentence and has a duplicated table cell.; §4 has no Environment and resources section: tech-stack reasons (Expo, Firebase, Mapbox, Python) appear only under Planned activities (#48, #72).; §4 specs: only Goal 3 is summarized; add scope, requirements, acceptance criteria and open questions for Goals 1 and 2 (#70, #73) from `docs/specs/`.; §4 design and implementation: carry components, data model and decisions with rejected alternatives into the proposal; describe what `tracking.js` and `pace.py` do. The paper is about 5,600 words; the final needs more than 50 pages..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - stale, holds only the login scaffold; later PRs never reached main's prototype.

**To do in Sprint 4:**

1. Build the spectator view (#69) in `prototype/spectator-view/` so a runner position reaches a web page end to end, with a test per acceptance criterion.
2. Add an Environment and resources subsection to §4 with one reason per tool (Expo, Firebase Firestore, Mapbox, Python); cite #48 and #72.
3. Summarize the Goal 1 and Goal 2 specs in §4 and complete Goal 3; finish #70 and link each acceptance criterion to a test.
4. Move the data model, architecture and key decisions (with rejected alternatives) from `docs/design/` into §4 prose, each paragraph ending with issue refs.
5. Rewrite §0 to match Goals 1-3; fix §1.1, remove 〈…〉 placeholders and quote blocks, then write §5-§8 toward 50 pages.
6. Finish #88 (link #21, #1, #2, #6) and refresh `prototype/README.md` run steps.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Python app that finds signal peaks in 6G captures, classifies waveform and modulation, and explains the decision.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – Dec 2** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge PR #167 and promote develop to main so your Sprint 4 work builds on one proposal and one prototype on the default branch.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 11 of 17 stories have child issues; #67, #69, #70, #71, #84, #95 have none (#163 now has #164, #165). Stories #67, #69, #70, #71, #84, #95 have no child feature, task or sub-task.; 24 issues are not in proposal.md on develop, including tasks #147-#152, #154-#162, #164, #165 and stories #95, #163.; #70 and #71 have no assignee or Sprint milestone; #103 is untyped with no assignee.; §4 still cites stories (#68, #84, #111, #126) that belong only in §2; 14 misplaced refs, one to deleted #63.; One direct commit on develop and main; PRs #1, #2 (old) have no issue; PR #167 is open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. |
| 3. Prototype works | ✅ done | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, Captum attribution and a transformer AMC module. CI: develop 11-19 green (3b7ee1b), re-run on the same code; Prototype job ran Install and test (Python) on team code. main is the 10-16 scaffold. Tests: 14 test files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, pipeline gate, OFDM, training, transformer. |
| 4. Word export (`develop`) | ⚠️ partial | 70 issue citation(s) become small in-text tags; 54 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The peak-picker and classifier demo runs from develop, but §4 lacks Environment detail and Implementation, and main still shows the scaffold. |

**Proposal, what to write:** §4 Environment and resources is 28 words with template placeholders; give each tool (MATLAB, Python, Captum, dataset) and the reason it was chosen.; Only two specs (application architecture, waveform family) for five epics; Goals 1, 4 and 5 need scope, requirements, acceptance criteria and open questions.; No §4 implementation section for `waveform_identification/`, `xai/`, `GUI/` and `modulation_classification/`; add paragraphs ending in task refs.; §1.1 has four prose subsections but no pros-and-cons table or prose on what this project does differently.; §1.2 states P1-P3 in about 50 words; explain why each matters and tie it to a goal. No planned-activities prose exists..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #167 (open): merges diagrams and design docs into `proposal/proposal.md` (closes #163); branch develop: holds the real prototype and §4 work; main is the login scaffold, promote it; branches Application-Structure, docs/team-documentation: commits not in develop.

**To do in Sprint 4:**

1. Merge PR #167 and finish #164 and #165 so the specs and design in `docs/` are carried inside `proposal/proposal.md`.
2. Open and merge a develop-to-main PR so `prototype/` and `proposal/proposal.md` on main are current; keep main CI green.
3. Link #147-#165 in §4 as typed refs, and move story refs out of §4 into §2.
4. Create child issues for stories #67, #69, #70, #71, #84, #95; assign one person and a Sprint milestone to each.
5. Replace the §4 Environment placeholder with each tool and why it was chosen; write an Implementation section for the four prototype packages and planned-activities prose.
6. Add specs for Goals 1, 4 and 5 and a §1.1 pros-and-cons table, then draft §5 to §8 in Sprint 4.
7. Wire the CLI to the analysis pipeline (#161) and add one test per acceptance criterion in `prototype/tests/` for the full prototype.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – Dec 2** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge the open feature PRs, then rewrite `prototype/README.md` and rename the test file so CI exercises the app in Sprint 4.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#19-#27 via features #53-#102 and tasks #55-#106). Only 8 of 84 linked issues are closed; tasks #56, #57, #61, #62 and feature #53 have open PRs #144, #145, #147, #148, #153.; #93, #94, #124 and #47 have no Sprint milestone; #13 has no assignee or milestone.; #139, #125 (3 assignees), #126, #124, #123, #122 (2), #111 and #107 (4) break one-assignee-per-issue.; 19 issues are not in proposal.md, including #131, #124, #113, #107; refs like `taskL#127`, `[task:#139]` and #119's wrong URL are malformed.; Merged PR #150 has no Closes; older PRs #1, #3, #4, #9, #36, #117 lack issues.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned Activities is a 17-row issue table (16 link rows) plus short per-item lines; it carries no explanatory prose of its own.. |
| 3. Prototype works | ⚠️ partial | `A.M.I.Y.A.core/` has app, database, models, assignment and deadline services; the Electron/Vite UI has a task modal and GUI (#143). Form, storage and edit PRs are unmerged. CI: develop 11-16 green (8be40c7), main 11-14 green (3c0d601), but the Prototype job ran only the Python step; the UI `package.json` is in a subfolder, so Node was skipped. Tests: One file, `A.M.I.Y.A.core/tests/TestAssignments.py`; its name does not match pytest discovery, so CI likely does not run it. |
| 4. Word export (`develop`) | ✅ done | 102 issue citation(s) become small in-text tags; 84 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Wireframes and specs are showable, but `prototype/README.md` is still the login scaffold, there are no run steps, and CI proves little about the app. |

**Proposal, what to write:** §1.1 has a pros-and-cons table but no prose arguing what A.M.I.Y.A. does differently; add it, citing §8.; §1.2 is 68 words; write each problem as a paragraph tied to a goal and ending in refs.; §4 Environment describes Python and JavaScript but gives no reason per tool and names no data store or hosting.; §4 specs are short summaries linking `docs/specs/specs-G1.md` to `specs-G3.md`; carry scope, requirements, acceptance criteria and open questions into the proposal.; §4 design is six wireframes only; add system context, components, data model (`docs/design/ER_DIAGRAMS.md`), data flow and decisions with rejected alternatives..

**Merge first** (it doesn't count until it's in `develop` or `main`): PRs #144, #145, #147, #148 (open): form validation, local data, edit/delete, confirmation; PR #153 (open): assignment UI feature #53; branches task/111-specification-details, task/122-high-level-architecture-diagram: unmerged commits; architecture diagram PRs #134, #135 closed.

**To do in Sprint 4:**

1. Merge PRs #144, #145, #147, #148, #153 with `Closes #N` and close the issues the prototype already implements.
2. Rewrite `prototype/README.md` with install, run and test commands for the core and the UI.
3. Rename `TestAssignments.py` to `test_assignments.py` and add one test per acceptance criterion in `docs/specs/specs-G1.md` through `specs-G3.md`.
4. Merge the architecture diagram branch and add system context, data model and data flow diagrams with prose to §4.
5. Add Sprint milestones to #93, #94, #124, keep one assignee per issue, and fix malformed refs in the Planned Activities table.
6. Write §4 Environment with a reason per tool, an Implementation section, and carry specs and the ER design into §4 prose.
7. Start §5 to §8 in Sprint 4 so the whole paper reaches the 50-page target.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · G14: Cyber Sandbox (Cyber Squad)

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – Dec 2** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 11), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Add Sprint milestones to the Sprint 4 child issues (#136-#175) so every child has one assignee and a milestone.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 18 of 18 stories have child issues (feature, task, sub-task); epics #22 and #23 sit above them. About 40 Sprint 4 children (#136-#175, minus #140) plus #114, #115, #44-#47 have no Sprint milestone.; `sp:` remains on #99, a task under story #25; points belong on the story only.; #88 and #92 have no assignee; #79, #80, #81, #44 and #45 have several.; New Sprint 4 meeting #177 is not in the proposal; #91 and #92 are cited as plain links, not typed refs.; 9 direct commits each on main and develop (e.g. 118e0ed adding Sprint 3 tasks); use a branch and PR with `Closes #N`.; PR #50 (Goal 2 spec) has no issue; §4 cites story #24 and §1 cites task #113.. |
| 2. Proposal §0–§4 (`develop`, ≈ 11 pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" opens with an 11-row link table, but each document then gets a prose summary; planned activities are prose paragraphs with refs.. |
| 3. Prototype works | ✅ done | PySide6 start menu loads a sample or JSON scenario validated by Pydantic; user browses, creates and deletes simulated files in memory; optional Ollama generator script. CI: main green 11/12 (ec16018), develop green 11/12 (2a0c3b8); Prototype job ran Install and test (Python) on team code, and CI fails if no tests are collected. Tests: 5 test files in `prototype/tests/`: scenario model, loader, simulation engine, scenario generator, UI (Qt offscreen). |
| 4. Word export (`develop`) | ✅ done | 176 issue citation(s) become small in-text tags; 119 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ✅ ready | Proposal §0-§4 is written on develop and the PySide6 slice runs from a clean clone with README steps and green CI. |

**Proposal, what to write:** §3 still says 'Sprint 2 priorities' and 'prototype skeleton'; rewrite it to describe what the prototype implements now and what Sprint 4 adds.; §4 spec summaries name requirements and acceptance criteria but few figures; state the main FR and NFR for Goals 1 and 2 explicitly.; §1.2 has spelling errors; proofread it, and write §2 objectives as sentences, not a 20-line bullet list.; §4 implementation covers `ui/`, `sim/`, `scenario/`; add a sentence per layer on tests and on what each acceptance criterion checks..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - holds the fuller proposal (57k characters vs 50k on main); promote it to main.

**To do in Sprint 4:**

1. Add a Sprint milestone to the Sprint 4 children (#136-#175), #114, #115 and #44-#47, and give #88 and #92 one owner each.
2. Remove `sp:` from #99 and move the points to story #25 if needed; keep points on stories only.
3. Link #177 in §4 as a typed ref and convert #91 and #92 to typed refs.
4. Stop direct commits to main and develop: open a branch and PR with `Closes #N` for every proposal edit, including Sprint 4 task additions.
5. Rewrite §3 (still 'Sprint 2 priorities') to match the PySide6 prototype and the Sprint 4 plan.
6. Build the process, log and network views (#139, #143, #105) with a test per acceptance criterion before your Sprint 4 review.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – Dec 2** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 6), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Write the §4 Design subsection from `docs/design/architecture.md`; it is the largest missing piece and the diagram and CMake build already exist.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 8 stories have child issues (#30, #31, #32, #33); #26-#29 have none. Stories #26, #27, #28, #29 (game demo) have no child feature, task or sub-task.; `proposal/proposal.md` has 0 typed refs: 36 bare `#N` cells and malformed `[story:https://...]` parents in the §4 table.; #46 is parented to story #32 yet carries `sp: 2`; #46's table row names itself as its own parent.; #76, #78, #82, #43 and epic #6 are not in the proposal; #43 has no milestone; #44 has no assignee.; Stories #26-#33 each have 2 assignees; one assignee per issue.; 4 early direct commits on main; PRs #3, #4, #5, #41 have no issue (old).. |
| 2. Proposal §0–§4 (`main`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; "Planned activities" is a 38-row table of issues, owners and sprints with no prose; §1.2 sits in a table.. |
| 3. Prototype works | ✅ done | CMake project (SDL3, Assimp, ImGui, GLM) with ECS core, transform and mesh components, renderer and model loader headers, shaders; README gives build, run and test commands. CI: main green 11/13 (43fce39) and develop green 11/14 (c80ac06); Prototype job detected CMake, installed graphics libraries, configured, built C++ and ran Tests (CMake). Tests: README names target `test_engine_components` (basic ECS checks); test sources not visible in the sweep's file list. |
| 4. Word export (`main`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 25 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | CMake build and ECS test run green in CI, but §4 is tables and links with no design or implementation prose, so the proposal half is not ready. |

**Proposal, what to write:** §4 specs: summarize `docs/specs/game-engine.md` and `game-demo.md` in prose (scope, FR/NFR, acceptance criteria, open questions); today only the file names appear.; §4 design: write components, data model (entities, components, systems), data flow and key decisions with rejected alternatives from `docs/design/architecture.md`.; §4 diagrams: Figures 1 and 2 have captions but no paragraph explaining them; add one per figure.; §4 environment is one line per tool; explain why SDL3, Assimp, ImGui and C++26 suit old hardware, and name the test machines.; §4 has no implementation section: describe `prototype/include/engine/` and `demo/` and what runs, citing #63, #66, #67, #82..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch 33-objective-24-implement-visual-editor-to-import-models-create-objects-and-design-the-game-world: 2 commits not in develop.

**To do in Sprint 4:**

1. Write §4 Specifications as prose from `docs/specs/game-engine.md` and `game-demo.md`: scope, FR, NFR, acceptance criteria, open questions per epic.
2. Write §4 Design (components, ECS data model, data flow, decisions with rejected alternatives, undesigned parts) from `docs/design/architecture.md`.
3. Add a §4 Implementation section on what the CMake prototype builds and tests today, citing #63, #66, #67, #82.
4. Replace the 38-row planned-activities table with paragraphs and typed refs; add #76, #78, #82 and epic #6.
5. Create child issues under stories #26-#29; remove `sp:` from #46 and fix its parent.
6. Merge the #33 visual-editor branch by PR with `Closes #N`, and add a test per acceptance criterion for the engine and demo.
7. Explain Figures 1 and 2 in prose, fix the 〈…〉 title in `prototype/README.md`, and start §5 to §8 in Sprint 4.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Monitors cross-chain bridge vaults, learns normal outflow, and alerts on drains with measured false alarms.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Create child tasks under stories #19 and #21 with one assignee and a Sprint 4 milestone each, then tie each to a test.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#14, #15, #17, #18, #20); #5, #16, #19, #21 have none. Stories #19 and #21 (Sprint 4) and closed stories #5 and #16 have no child issues.; Tasks #28 and #107 have no parent story; #107 also has no assignee.; PRs #75 and #35 have no `Closes #N` (both closed, old).; Three direct `docs:` commits on main and develop (team details), outside any PR.. |
| 2. Proposal §0–§4 (`main`, ≈ 25 pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: Table 9 lists the specs and design doc as paths with issue refs, but prose summaries for Goals 1, 2 and 3 now sit behind it.. |
| 3. Prototype works | ✅ done | Detector, SQLite store, live Ethereum poller, replay of five past hacks, false-alarm evaluation on real normal days, Slack notifier, FastAPI API, web dashboard, demo mode. CI: main 93cd0c2 and develop 3463b50 both green on 11-18; Prototype job ran Install and test (Python), so team tests executed. Tests: Four files in `prototype/tests/`: detector, live loop, baseline check, data pipeline; proposal reports sixty tests. |
| 4. Word export (`main`) | ✅ done | 78 issue citation(s) become small in-text tags; 50 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ✅ ready | The prototype runs in live, demo and replay modes on green CI, and §0-§4 now carry specs, design decisions and implementation prose on both branches. |

**Proposal, what to write:** Goals 2 and 3 now have spec summaries in §4 (PR #115) and the Key design decisions and Not designed yet paragraphs exist (PR #118).; Figures 1 and 2 are labelled as the original plan beside D0 to D6; keep them marked planned versus built.; §4 Planned activities should be updated in Sprint 4 so the Sprint 4 tasks read as prose ending in refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch 93-cpsc491-timeline: 13 commits not in develop.

**To do before your Sprint 3 review:**

1. Create child tasks under stories #19 and #21 at the start of Sprint 4, each with one assignee and a Sprint milestone.
2. Give #107 an assignee and put #28 and #107 under a story, so every issue sits in the story chain.
3. Add a test per acceptance criterion for Objectives 2.2, 2.3 and the dashboard in `prototype/tests/`, and finish the prototype for Sprint 4.
4. Update §4 Planned activities with the Sprint 4 tasks and the 30-day false-alarm results for Objective 2.3.
5. Draft §5 to §8 in full so the whole paper moves toward the >50-page target.
6. Merge the `93-cpsc491-timeline` branch by PR with `Closes #N`, and stop direct commits to main.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Write one pytest per acceptance criterion of `docs/specs/specs_goal3.md` against `db.py` (account, salted hash, swipes survive restart) and run them in CI.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 6 stories have child issues (#25, #27, #29, #30); #26 and #28 have none (tasks #46, #47, #53 hang off epic #21). `sp:` on 11 child tasks under stories or pointed tasks (#41-#43, #49, #51, #55, #57-#59, #65, #68).; #41, #49, #51, #55, #57-#59, #62-#64 are not linked from the proposal; 9 of 18 linked refs are untyped.; #49 and #55 have no assignee; #63 and #64 have no parent; #64 has no type label.; 18 merged PRs lack `Closes #N`, including recent #75 and #67; main has 32 direct commits.; Stories #29 and #30 are still open although login PRs #69 and #70 merged; Sprint 2 holds 2 open issues.. |
| 2. Proposal §0–§4 (`main`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1 and §1.2 are tables, §2 is nine bullets, the spec and design index is a link table, and Planned activities is a 7-row table with no prose.. |
| 3. Prototype works | ⚠️ partial | Arcade login and preferences screens (#62, PR #69), swipe on the main screen (#72), SQLite `db.py` and `schema.sql` (#64), Last.fm client; not shown wired end to end. CI: main c2f301d (11/18 PST) green: harness passed and 'Install and test (Python)' ran, but no team tests exist, so CI verifies no team code. The develop branch no longer exists. Tests: none; no `prototype/tests/` folder although the README claims four tests |
| 4. Word export (`main`) | ✅ done | 16 issue citation(s) become small in-text tags; 16 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Login, preferences and a swipe screen can be shown from main and §4 now has specs and design prose, but there is no tested end-to-end slice. |

**Proposal, what to write:** §1.1 is a four-row table with no prose and no citations to §8; §8 still holds template references. Add paragraphs on what SonicScape does differently.; §1.2 is a table and §2 is bullets; write the problem statements and each epic and story as paragraphs ending in typed refs.; §4 has no implementation details; describe what `prototype/src/sonicscape` does (screens, swipe, `db.py`, `lastfm.py`) with task refs.; §4 figures 3 to 5 are raw Mermaid blocks, and figure numbers repeat (two Figure 1 labels, Figure 6 then 7); export images and renumber.; §4 Planned activities lists only 7 rows; describe Sprint 3 and 4 work in prose. §5-§8 are still template text..

**To do before your Sprint 3 review:**

1. Add `prototype/tests/` with a pytest per acceptance criterion in `docs/specs/specs_goal1.md`, `specs_goal2.md` and `specs_goal3.md` (login, salted hash, swipe saved, restart persistence) and run them in CI.
2. Wire one end-to-end slice: Last.fm data into SQLite, galaxy view, a swipe that saves a like; rewrite the README run and test steps so they work from a fresh clone.
3. Rewrite §1.1, §1.2 and §2 as prose with citations matching §8, and add an implementation-details subsection to §4.
4. Fill §5 to §8 and grow `proposal.md` past 50 pages without the Appendix; export the Mermaid figures and renumber them.
5. Add child issues under stories #26 and #28, remove `sp:` from child tasks, assign #49 and #55, link #41, #49, #51, #55, #57-#59, #62-#64 as typed refs.
6. Close stories #29 and #30 once their tests pass, and open every change through a PR with `Closes #N` instead of direct commits to main.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: Project Rogue, 2D action roguelite with flexible builds (Unity)

*A Unity 2D action roguelite where builds develop through weapons, attributes and branching three-Act runs.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Write the §4 Implementation subsection from the existing combat, class and traversal code, then add one edit-mode test per acceptance criterion in the Goal 2 spec.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32 via #72, #35 via #64, #41 via #48); #33, #34, #36-#40 have none. #64 (under story #35), #65, #56 and #53 carry `sp:`; points belong on the story only.; #74 and #58 have no Sprint milestone; #26 and #13 are untyped with no milestone.; #79, #76, #74, #72, #65, #64, #61, #58, #56, #53 are not linked from proposal.md.; Epics #29-#31 are cited in §1 and story #41 in §4; epics and stories belong in §2 only.; #79, #76, #74, #60, #59, #58, #51, #49, #47 are tasks with no parent story or epic.; PR #80 to main has no `Closes #N`; Sprint 3 closed 11/18 with 6 issues open and 2 closed.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a 5-row link table; Planned activities is a 28-row issue table with only four short paragraphs.. |
| 3. Prototype works | ⚠️ partial | Unity 6 project on develop: combat demo (resolver, abilities, target dummy), movement and traversal room, starting classes (#81), five room scenes with enemy placeholders (#83); no run loop merged. CI: develop 559632c (11/19 PST) and main d6e8c9a (11/4 PST) green; the Prototype job ran only 'Install and test (Python)' on the scaffold, so no Unity code was compiled or tested. Tests: No automated tests; `Assets/Editor/ClassVerification.cs`, `ProgressionVerification.cs` and the `Test_Combat` scene serve as manual checks. |
| 4. Word export (`develop`) | ✅ done | 54 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Combat, traversal and class demos run from develop, but §4 lacks specification, design and implementation prose and CI does not run the game. |

**Proposal, what to write:** §4 Specifications: the three goal specs in `docs/specs/` are not summarized per epic with requirements and acceptance criteria.; §4 Design: `docs/design/system-overview.md` is only linked; carry context, components, data model, data flow, decisions and open items into the proposal.; §4 Diagrams: the class diagram and run/room/reward flowchart in `docs/design/diagrams/` are not embedded; the two embedded figures get one short paragraph each.; §4 Implementation: add a section describing what `prototype/ProjectRogue` implements (combat resolver, abilities, movement, traversal room, boons, classes) with task refs.; §2 and §3 disagree on starting classes versus weapon-and-element builds; align them. main still has the template §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #84 - run, node and reward progression for #40, open against develop; PR #80 - title, pause and retry UI for #79, open against main with no `Closes`; develop to main - §3-§4 text, diagrams, specs and prototype work are not on main.

**To do before your Sprint 3 review:**

1. Write the §4 Implementation subsection naming what each folder under `prototype/ProjectRogue` does (combat, movement, classes, rooms, boons) with task refs.
2. Write a per-epic specification summary in §4 (scope, functional and non-functional requirements, acceptance criteria, open questions) from the `docs/specs/` files.
3. Carry the system overview and combat class diagram into §4 with context, components, data model, data flow, rejected alternatives and open items.
4. Add edit-mode tests, one per acceptance criterion in the three specs, and run them in CI; merge PR #84 and finish the run loop.
5. Create child issues for stories #33, #34, #36-#40 with one assignee and a Sprint milestone each, remove `sp:` from #64, #65, #56, #53, and link every issue in §4 as a typed ref.
6. Fill §5 to §8 and grow `proposal.md` past 50 pages without the Appendix; merge develop into main through a reviewed PR.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · G19: Titan Security, Radar over WiFi drone detection (RTX-2)

*Detect small drones and estimate position and movement from Wi-Fi CSI, compared against conventional radar.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Write pytest tests for `quality_check.py` and `event_analysis.py` against the sample recording, replace the course `test_login.py`, and run them in CI.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 13 of 13 stories have child issues, but 8 children (#77-#84) have no type, assignee or Sprint milestone. #77-#84 are untyped, have no assignee or Sprint milestone, and none is linked from proposal.md.; #99 is labelled user-story and task, carries `sp:` under story #97, and is cited as a task.; 18 issues are not linked from §4, including #101, #98, #93, #75, #71, #53 and #43.; #86 and #91 are tasks with no parent; #93 has no Sprint milestone; story #73 has no `sp:`.; The §4 work-item table cites stories #6, #7, #13-#17; stories belong in §2 only.; Sprint 3 (due 11/18) has 8 open and 4 closed issues; PR #104 is open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4.3 is a link table with a leftover template placeholder block and no per-epic spec summaries; §4.4 is a 15-row table, with the prose in §4.5.. |
| 3. Prototype works | ⚠️ partial | CSI capture and quality-check scripts with a sample recording, plus preliminary feature extraction and event analysis (`features.py`, `event_analysis.py`, PR #102); scaffold `login.py` remains. CI: develop 484bafe (11/18 PST) green and 'Install and test (Python)' ran, but the only test is the course `test_login.py`, so no team code is tested; main 7fca571 (11/5 PST) is older. Tests: Only the course `prototype/tests/test_login.py`; nothing tests capture, quality check, features or event analysis. |
| 4. Word export (`develop`) | ⚠️ partial | 46 issue citation(s) become small in-text tags; 37 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | §4 environment, diagrams and remaining-work prose are real and CSI capture plus offline event analysis can be shown, but there are no team tests or detection slice. |

**Proposal, what to write:** §4.3: delete the two placeholder rows and summarize `wifi-csi-sensing.md`, `drone-detection.md` and `evaluation.md` per epic; PR #104 is open for this.; §4 design: add the data model (recording and dataset formats), key decisions with rejected alternatives, and what is not designed yet.; §4 has no implementation section; describe what `capture.py`, `quality_check.py`, `features.py` and `event_analysis.py` do, with #101.; The draft-status banner under the title and the 'TO CONFIRM' lines in §1.1 and §8 remain; resolve them and name the conventional radar systems.; §1 is three short paragraphs and §3 is brief; expand the motivation, scope and the reasoning for the two-computer pipeline..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #104 - epic spec summaries and design narrative for #97, open against develop; develop to main - main last changed 11/5 PST and lacks all Sprint 3 work.

**To do before your Sprint 3 review:**

1. Merge PR #104, delete the placeholder rows in §4.3 and the draft banner, and merge develop into main.
2. Add tests for `capture.py`, `quality_check.py`, `features.py` and `event_analysis.py` per acceptance criterion in `docs/specs/wifi-csi-sensing.md`; replace `login.py` and its test; fix the README.
3. Add a §4 Implementation subsection and the design data model, decisions with rejected alternatives and open items, with task refs.
4. Type, assign and milestone #77-#84, fix #99, parent #86 and #91, and link all 18 unlinked issues as typed refs in §4.
5. Finish the Sprint 3 stories #13-#15 and #7 (labeled data, classifier, position estimates) with results written into the proposal.
6. Fill §5 to §8 and grow `proposal.md` past 50 pages without the Appendix; select the conventional radar systems in §1.1.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · G20: Solos, Insomnia, first-person horror maze game in Unreal Engine

*Unreal Engine 5 first-person horror maze game with adaptive monsters, encounter director and responsive atmosphere.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Rewrite the §4 work-item table and prose refs as typed refs, then update `prototype/README.md` to run the maze level with a manual test per acceptance criterion.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child issues (#13, #14, #15, #18, #19, #20, #22, #23). Only 11 refs are typed; 39 of 51 issue refs are bare `#N` or `Task `[#N]` links, mostly in §4.; Tasks #64-#68, #76-#78 and #91 are standalone with `sp:` and no parent story or epic.; Sprint 3 (due 11/18) has 19 open and 17 closed issues; stories #14, #15, #18-#20, #22, #23 are open.; Epics #12, #17, #21 sit in Sprint 4 while their stories sit in Sprint 3.; The §4 table lists #41 under Type 'Task' but cites it as 'Feature'; fix the Type column.. |
| 2. Proposal §0–§4 (`develop`, ≈ 12 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: The spec and design index and the 41-row work-item table are tables, but each follows real prose; no section relies on a link table alone.. |
| 3. Prototype works | ⚠️ partial | Unreal Engine 5 project with sprint and crouch movement (#40), a prototype maze (#71), objective tracker (#42), an enemy that chases and attacks (#48) and hide evasion (#73). CI: develop c686eb8 and main 8f44220 (11/18 PST) green, but the Prototype job ran only 'Nothing to build', so CI did not exercise the Unreal project; judged by README and PR notes. Tests: None automated; manual tests are recorded in PR descriptions, and the README smoke test covers only the starter level. |
| 4. Word export (`develop`) | ⚠️ partial | 61 issue citation(s) become small in-text tags; 51 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The prototype shows movement, a maze, an objective tracker and a chasing enemy, but it has no tests, and template text is still in §1.2, §3 and §4. |

**Proposal, what to write:** §1.1 compares three games in short pros and cons and calls Insomnia a haunted-house game while §0 and §2 describe a maze; align and cite [1]-[3] in §8.; §4 Specifications: each summary is one paragraph; add non-functional requirements and numbered functional requirements per epic.; Template text remains: the quote blocks and 'Keep the details out' note in §3, the quote block in §4, an empty table header, and 〈〉 cells in the §1.2 table.; §4 Design: add the data model or state explicitly that none exists, and describe the director and monster state data.; §4 Implementation is clear on status; add the Unreal Blueprint structure and the hide, line-of-sight and attack-timing work (#73)..

**To do before your Sprint 3 review:**

1. Rewrite the §4 work-item table and every `#N` in §4 prose as typed refs such as `feature:#40` and `task:#41`.
2. Parent #64-#68, #76-#78 and #91 under an epic or story, and move unfinished Sprint 3 issues to the Sprint 4 milestone.
3. Update `prototype/README.md` for the maze level and controls, with a manual test per acceptance criterion and recorded results.
4. Build the second monster type, the director (#50, #51) and adaptive audio (#75), each with a written test per acceptance criterion in the specs.
5. Delete the leftover template text in §1.2, §3 and §4, align §1.1 with the maze concept, and add non-functional requirements to the specs.
6. Fill §5 to §8 and grow `proposal.md` past 50 pages without the Appendix.

[↑ Back to all groups](#groups)

## About this page

The Sprint 2 checklist (specs, design, environment, prototype wiring) is now folded into rule 2 (§4) and rule 3. The earlier editions, including the Sprint 2 cards, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
