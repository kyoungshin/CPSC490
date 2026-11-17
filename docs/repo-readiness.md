# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.
>
> **Sprint 4 (G01–G05 and G11–G15, now in Sprint 4):** Sprint 4 asks for the same three rules, taken to the finish. **Finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages** without the Appendix, and **complete the prototype so it is fully functional**. You run Sprint 4 on the board as usual, and I grade it on the same five rubric lenses. Your card shows the Sprint 4 bar and your page count so far. G06–G10 and G16–G20: your card still shows the Sprint 3 review bar.

**CPSC 490 · Fall 2026 · swept 2026-11-17 20:36 UTC.** Earlier editions are kept in this file's git history.

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
| G01–G05 | Oct 27 – Nov 9 | **Tue Nov 10** | Nov 10 – 23 |
| G11–G15 | Oct 29 – Nov 11 | **Thu Nov 12** | Nov 12 – 25 |
| G06–G10 | Nov 3 – 16 | **Tue Nov 17** | Nov 17 – 30 |
| G16–G20 | Nov 5 – 18 | **Thu Nov 19** | Nov 19 – Dec 2 |

## Class at a glance

✅ done · ⚠️ partial · ❌ not there yet. **Pages so far** is a rough estimate (words outside the Appendix ÷ 500) to set against the 50-page final; tables and figures add a little more.

| Group | Now | 1. PRs ↔ issues ↔ proposal | 2. Proposal §0–§4 | 3. Prototype works | 4. Word export | Demo-ready | Pages so far (target 50+) |
|---|---|---|---|---|---|---|---|
| [G01](#g01) BGAF | Sprint 4 (Nov 10 – 23) | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ≈ 87 |
| [G02](#g02) Linux Larpers | Sprint 4 (Nov 10 – 23) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 15 |
| [G03](#g03) California | Sprint 4 (Nov 10 – 23) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Sprint 4 (Nov 10 – 23) | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 33 |
| [G05](#g05) Fighting Mongooses | Sprint 4 (Nov 10 – 23) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G06](#g06) GapWise | Sprint 3 review Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 6 |
| [G07](#g07) Mighty Morphins | Sprint 3 review Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 9 |
| [G08](#g08) Crime Busters | Sprint 3 review Tue Nov 17 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ≈ 9 |
| [G09](#g09) Sigma Squad | Sprint 3 review Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 11 |
| [G10](#g10) Team Jiddak | Sprint 3 review Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 10 |
| [G11](#g11) 5 Guys | Sprint 4 (Nov 12 – 25) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G12](#g12) ACJMM | Sprint 4 (Nov 12 – 25) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G13](#g13) BYKX | Sprint 4 (Nov 12 – 25) | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G14](#g14) G14 | Sprint 4 (Nov 12 – 25) | ⚠️ | ✅ | ✅ | ✅ | ✅ | ≈ 11 |
| [G15](#g15) HIBBI-01 | Sprint 4 (Nov 12 – 25) | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) G16 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 21 |
| [G17](#g17) G17 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | ≈ 8 |
| [G18](#g18) G18 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) G19 | Sprint 3 review Thu Nov 19 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G20](#g20) G20 | Sprint 3 review Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 8 |

- **Rule 1 met:** 2 of 20 (G04, G08).
- **Proposal §0–§4 complete:** 3 of 20 (G01, G08, G14).
- **Prototype working, with a real slice and tests:** 13 of 20 (G01, G02, G03, G04, G05, G06, G08, G09, G11, G12, G14, G15, G16).
- **Ready to demo both today:** 2 of 20 (G08, G14).

**What changed since the last edition:**

- **G01–G05 and G11–G15 are now in Sprint 4.** Sprint 4 asks for the same three rules, taken to the finish: the whole paper in `proposal.md` (§0–§8, more than 50 pages without the Appendix) and a fully functional prototype, graded on the five rubric lenses as usual. Your card now shows the Sprint 4 bar and your page count.
- **G01's proposal now passes rule 2.** `main` gained the §4 summaries for the validation gate, the front end and the data model, and the gap finder (#334) merged. PRs #337, #338 and #343 are still open.
- **G07 moved up on rule 3 and on demo readiness.** A static search page merged, and all 16 stories now have child issues, with all 97 issues linked from the proposal. The only test is still the course's `test_login.py`, so write tests for your own code.
- **Big Sprint 3 merges:** G09 merged every Sprint 3 PR (#82–#109) into `develop`: service records, entry and import forms, the dashboard and recommendations. G06 doubled its stories with child issues (4 to 8) and added specs and a design doc on `develop`. G10's `develop` CI is green again and its proposal grew by about 70%. G16 explained its design diagrams in §4. G17's proposal grew from about 19k to 30k characters. G18 wrote §3 and the §4 environment and added three goal specs. G20 broke down all 8 stories into child issues.
- **G08 and G14 stay demo-ready.** G08 merged the crime-type filter (#90) and marker highlighting (#87); release PR #86 into `main` is still open. G14's proposal and prototype are unchanged.
- **No change since Nov 14:** G02, G03, G04, G05, G11 and G15. G12 and G13 changed only on the board or by merging `develop` into `main`.
- **Check before your review:** G17's CI is red on `main`. G13's test file is not named so pytest finds it (`test_*.py`). G18, G19 and G20 have green CI that never builds or tests their own code. Work in an open PR does not count until it merges.
- **Review dates:** G06–G10 Tue Nov 17 (tonight), G16–G20 Thu Nov 19.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting (SNX-4)

*Pipeline that rebuilds Hyperliquid order books from SNX-4 data, validates them, and backtests strategies behind a gate.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 23** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 87), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge PRs #337, #338 and #343 and refresh `prototype/README.md` so the demo shows cleaning and loading, not only a snapshot load.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58 is dropped and has none); 7 stories are still open. Eleven tasks carry `sp:` under a story (#195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134): double counting.; Eighteen child issues have no assignee, 14 still open (features #144, #145, #148, #157-#159, #163-#167, #169; tasks #94, #147).; Dropped story #58 has no Sprint milestone or points; #346, #347, #348 (filed today) are not yet linked in §4.; `[task:#151]` is cited four times but #151 is a sub-task; 79 typed refs sit in §5, §6 or §8 instead of §2/§4.; Three direct commits on main; old PRs #126, #123, #62, #40 lack `Closes #N` (every PR after #126 has one).. |
| 2. Proposal §0–§4 (`main`, ≈ 87 pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: The 15-row document table in §4 is a map only; it sits beside real prose for each document, so no prose is replaced.. |
| 3. Prototype works | ✅ done | DuckDB schema and snapshot loader (`storage.py`) plus `find_gap_ranges` in `clean.py`; replay, validate, gate, backtest, report are stubs; front end is the Vite starter. CI: main run 11/16 16:07 PST green; Prototype job ran Install and test (Python) with pytest. Node steps skipped, so `prototype/frontend` is never built in CI. Tests: `test_storage.py` (schema, load, exact decimals, repeat load), `test_clean.py` (gap ranges), `test_package.py` (imports). |
| 4. Word export (`main`) | ✅ done | 713 issue citation(s) become small in-text tags; 218 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Proposal §0-§4 on main is complete; the prototype demo is a sample load into DuckDB that needs a CSV kept out of git, with replay and validation not built. |

**Proposal, what to write:** §1.2 Problem Statements is 223 words plus a table; write each problem as a paragraph that names the goal it leads to.; §2 is a 19-line bullet list; merge PR #345, which adds the goal narratives.; §4 runs about 30,000 words with repeated material across specs, design and backtest sections; shorten as #346-#348 plan, keeping the six design parts.; §5 'What the prototype does today' says storage only; update it when #337, #338, #343 merge..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #337 (open, main): duplicate removal and UTC nanosecond timestamps in the cleaning step; PR #338 (open, main): event ordering by block height and position, with tests; PR #343 (open, main): load order-level tables into event and snapshot rows; PR #344 and #345 (open, main): validation-gate summary in §4; goal narratives in §2; branch develop: old proposal with 15 placeholders; retire it, main is the integration branch.

**To do in Sprint 4:**

1. Merge PRs #337, #338 and #343, then update `prototype/README.md` layout and test list and the §5 'What the prototype does today' paragraph to match.
2. Remove `sp:` from tasks #195, #187, #184, #183, #181, #180, #175, #174, #173, #172 and #134; points stay on the story only.
3. Assign one person to each open child without an assignee (#144-#169 features, #94, #147) and give #58 a closing note or milestone.
4. Link #346, #347, #348 in §4 and change the four `[task:#151]` refs to `[sub-task:#151]`; move work-item refs out of §5 and §6.
5. Rewrite §1.2 Problem Statements as paragraphs, merge #345, and shorten §4 where specs and design repeat each other.
6. Run `npm ci` and `npm run build` in `prototype/frontend` before your Sprint 4 review, since CI skips Node; stop committing directly to main.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 23** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 15), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Write the Goal 1 spec (scope, FRs, NFRs, acceptance criteria, open questions) into §4; it unblocks the design and implementation text and sets the prototype tests.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); 10 stories (#49, #51-#55, #58-#61) have none. Ten of 15 user stories have no child issues; break each into feature, task, sub-task on the board.; 21 tasks carry `sp:` under a story (double counting): #95, #92, #91, #86, #84, #81, #77, #69, #68, #41 ...; Thirteen child issues lack exactly one assignee (#68, #67, #41, #39, #38, #36, #25 ...); six meeting issues have no type label.; #132, #130, #99 and epic #20 are not linked from the proposal; some epic/story refs sit in §3.; Eight direct commits on develop and one on main; PRs #3, #4, #5, #14 lack `Closes #N`; PRs #127, #131, #133, #134 open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §2 uses bullets with refs; §4 'Specification and design documents' is a template comment plus a 4-row table with no spec or design prose.. |
| 3. Prototype works | ✅ done | FastAPI `/health`, `/health/db`, POST/GET `/observations` on PostgreSQL via Compose; Angular starter page; ESP32 firmware is a skeleton with no capture yet. CI: Latest develop run green; Prototype job ran Python install and pytest on the backend. Angular and ESP32 projects are not built in CI; main run is also green but older. Tests: `test_main.py`, `test_observations.py`, `test_observation_model.py` (in-memory SQLite); Angular `app.spec.ts` not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 122 issue citation(s) become small in-text tags; 74 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Backend ingest and query can be demoed; no live ESP32 capture or dashboard data, and §4 specs, design and implementation are not written. |

**Proposal, what to write:** §4 Specifications: no spec per epic exists; `docs/specs/` holds only the scaffold example. Write scope, FRs, NFRs, acceptance criteria and open questions for Goals 1-3.; §4 Design: `docs/design/architecture.md`, `data-flow.md`, `system-context.md` exist but §4 carries only figures; summarize components, data model, decisions, rejected alternatives and undesigned parts.; §4 Implementation details is absent; describe the backend API, PostgreSQL tables, ESP32 firmware and dashboard as built, with task refs.; §1.1 is one table plus a short paragraph and §1.2 is about 215 words; main still holds the unfilled template for §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — §3, §4 environment and planned activities, observation API; merge into main; PR #133 (open, main) — develop-to-main merge; get it reviewed and merged; PRs #127, #131, #134 (open, develop) — review and merge or close; Branches feature/114-restart-persistence, feature/130-sprint-3-review, feature/132-section4-links — unmerged commits.

**To do in Sprint 4:**

1. Write one spec per epic (Goals 1-3) in `docs/specs/` and summarize each in §4 with FRs, NFRs, acceptance criteria and open questions.
2. Add a §4 design narrative from `docs/design/*.md`: data model, decisions with rejected alternatives, what is not designed yet.
3. Add a §4 Implementation subsection describing the backend API, tables, firmware and dashboard, ending in task refs.
4. Create child issues for stories #49, #51-#55, #58-#61 and remove `sp:` from the 21 tasks (#95, #92, #91 ...).
5. Get one ESP32 observation into the dashboard via the API and add a CI build for `prototype/dashboard`.
6. Link #132, #130, #99 and #20 from the proposal and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 23** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Fix `prototype/README.md` so a fresh clone runs the transcriber-to-training pipeline; the demo depends on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 13 stories have child issues (#50, #46, #34); 10 stories, 8 still open, have none. Ten of 13 user stories have no child issues; break each into feature, task, sub-task on the board.; 27 issues are not in the proposal (#85, #84, #78, #72, #71, #70, #69 ...); 19 issues carry no type label (meetings, writing tasks).; 22 non-story issues have no parent; several have no Sprint milestone (#85, #75, #68, #55, #53, #45 ...).; PRs #81 and #77 (Sprint 3) have no `Closes #N`; PR #83 is open; one direct commit on main and on develop.; Six refs are bare or point at the wrong issue number; only 12 of 18 refs are typed.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §2 is a bullet list with refs; §4 'Specification and design documents' and 'Planned activities' are small tables, not prose; §4 opens with the unfilled template prompt.. |
| 3. Prototype works | ✅ done | Transcriber router and recognizer, verifier, dataset generation, storage and display, PyTorch training, equation plotting, and a pipeline notebook. CI: Latest develop run green; Prototype job ran Python install and pytest on team code. Main CI is green but older, before most of the prototype landed. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train and plot_equation tests; none named for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The prototype pipeline is demoable from develop, but §4 is mostly missing and the README run steps do not work. |

**Proposal, what to write:** §4 Environment and resources is still the template prompt; name each tool, platform, hosting and the sponsor's notebook requirement with the reason.; §4 Specifications: `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` exist but are only indexed; summarize each with FRs, NFRs, acceptance criteria.; §4 Design: `docs/design/architecture.md` gets one paragraph; add data model, key decisions with rejected alternatives, and what is undesigned.; §4 Implementation and Planned activities are a 3-row table; describe the built transcriber, verifier, trainer and remaining work in prose with refs.; §1 Introduction is about 300 words and §1.2 is about 50 words with a placeholder; both need real paragraphs..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — transcriber, recognizer, training, plotting, notebook, specs; merge into main; PR #83 (open, develop) — review and merge or close.

**To do in Sprint 4:**

1. Rewrite `prototype/README.md` with working install, run and test commands; remove the course `login.py` references.
2. Replace the §4 template prompt with Environment prose: each tool, platform and hosting choice with its reason.
3. Summarize `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` in §4 with FRs, NFRs and acceptance criteria.
4. Expand the §4 design section from `docs/design/architecture.md`: data model, decisions and rejected alternatives, undesigned parts.
5. Create child issues for the ten stories without breakdown, with one assignee and a Sprint milestone each; link them all in §2/§4.
6. Add `Closes #N` to PRs and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and trader profitability analytics

*Compute profit and loss per Polymarket wallet from SonarX Polygon data, rank traders, and show them on a dashboard.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 23** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

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

*Detect whale calls with an AI model and locate them from hydrophone recordings.* · Sprint 3 review held Tue Nov 10 · **Sprint 4: Nov 10 – 23** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

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

*Turns a student's notes into practice questions and tracks per-concept mastery and forgetting to target weak spots.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

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

**To do before your Sprint 3 review:**

1. Merge develop into main (reviewed PR with `Closes #N`) so the proposal, specs and demo are on one branch before the review.
2. Rewrite §4 Components, Data Model, Data Flow and Key Decisions as paragraphs, each ending with typed issue refs; add rejected alternatives for every decision.
3. Summarize `docs/specs/specs-epic-1.md` to `-3.md` inside §4: scope, functional and non-functional requirements, acceptance criteria, open questions.
4. Create child issues under stories #14, #18, #19, #21, #28, #29, #31; give #74-#77 an assignee and Sprint 4 milestone; link them in §4.
5. Add a §4 implementation section for the prototype modules and replace the Planned activities table with prose.
6. Wire `mastery_tracker`, `question_selector` and `grader` into `run_demo.py` and refresh `prototype/README.md`.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (EL-1)

*Extracts material data from vendor certificates and test reports, stores it after human review, and supports analysis.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Rewrite `prototype/README.md` for the real prototype and add one tested slice, then carry the three specs and the design documents into §4 as prose.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 16 of 16 stories have child issues; all stories have an assignee and a Sprint milestone. Thirty issues are cited as bare refs in the proposal, not typed refs (#28-#59, #63, #67, #77 among them).; Nineteen story refs sit in §4, where only work items belong; epics #1, #4, #45 and story #49 are cited untyped outside §2.; Wrong ref types: `[task:#78]` and `[task:#94]` are features, `[task:#103]` is a bug, `[bug:#117]` is a task.; Task #38 carries `sp: 3` under story #48 (double counting); #28 has no Sprint milestone.; Three direct commits on main, two on develop; PRs #145, #144, #143, #140, #102, #99 are open.. |
| 2. Proposal §0–§4 (`main`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a 76-row table (48 issue links) with no prose; the 12-row document table stands in for specification and design writing.. |
| 3. Prototype works | ⚠️ partial | Static HTML mock-ups, `prototype/index.html` and `ui-tabs/search-view.html` (PR #101); no back end, extraction or database code. CI: main run 11/16 22:31 PST green; Prototype job ran Install and test (Python), but the only test is the course `tests/test_login.py`. Tests: none for team code; only the course `tests/test_login.py`. |
| 4. Word export (`main`) | ⚠️ partial | 128 issue citation(s) become small in-text tags; 95 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A static search page can be shown, but §4 is mostly links and tables, the README is the course template, and no team code is tested or runs. |

**Proposal, what to write:** §4 specs: `docs/specs/data-extraction-spec.md`, `data-storage-spec.md`, `data-analysis-spec.md` are only linked; summarize each in §4 (scope, requirements, acceptance criteria, open questions).; §4 design: five figures, but only Figure 3 has explaining prose; add components, data model, data flow and key decisions with rejected alternatives, using `technology-stack-decision.md`.; §4 Environment is a table with short purposes; add a paragraph per choice (Snowflake, AWS, FastAPI, OCR tool) giving the reason and rejected option.; No implementation section: describe the static search view and what remains to be built; replace the 76-row table with prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #145 (open, main): goal specification summaries added to the proposal; PR #144 (open, main): §2 update with new goal specs under `docs/specs/`; PR #143 and #140 (open, main): data-flow update and environment table; PR #99 and #102 (open, main): search-view and page-5 sequence diagrams; branch develop: far behind main and holds an old skeleton; retire it.

**To do before your Sprint 3 review:**

1. Merge PR #145 and #144, then confirm §4 carries each goal specification as prose, not only a link to `docs/specs/`.
2. Write §4 design as paragraphs: system context, components, data model, data flow, key decisions with rejected alternatives, and what is not designed yet.
3. Replace the Planned activities table with paragraphs and convert the 30 bare issue refs to typed refs of the correct kind.
4. Rewrite `prototype/README.md` for the real prototype and add team tests; replace the course `login.py` and `test_login.py`.
5. Pick one slice (for example document upload, extraction and review) and implement it with a test per acceptance criterion before Sprint 4 ends.
6. Move story refs out of §4, type the epic refs #1, #4, #45 and story ref #49 in §2, and remove `sp:` from #38.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: interactive crime map and database

*Normalizes public Costa Mesa crime-call data into SQLite and shows it on a filterable Leaflet map.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Merge release PR #86 into main so the default branch carries the Sprint 3 prototype and proposal text.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 8 of 8 stories have child tasks. Closed legacy issues #45-#47 (untyped objectives), #6 and #7 are not in the proposal and have no Sprint milestone.; Release PR #86 (develop to main) is still open, so main lacks the Sprint 3 work; PR #88 lists `Closes #86` twice.; Sprint 1 PRs #37, #39, #40 lack `Closes #N`; every later PR has one. No direct commits, no `sp:` under a story.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ✅ done | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: none; §4 on develop is prose, each part ending with typed refs (the old link table was replaced).. |
| 3. Prototype works | ✅ done | Normalizes a Costa Mesa snapshot, loads and verifies SQLite, serves `/api/incidents`; Leaflet shows 19 calls at 13 locations, crime-type filter, selected marker highlight. CI: develop run 11/16 22:31 PST green; Prototype job ran Install and test (Python) and collected the team test files. main run 11/03 green but lacks the app. Tests: `test_normalize.py`, `test_load_db.py`, `test_area_filter.py`, `test_crime_frequency.py`; none for `app.py` or the page. |
| 4. Word export (`develop`) | ⚠️ partial | 46 issue citation(s) become small in-text tags; 46 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ✅ ready | On develop, §0-§4 are real prose and the Flask and Leaflet map runs from a fresh clone; demo from develop until #86 merges to main. |

**Proposal, what to write:** §4 Figure 3 (the ER diagram) is only a link; embed the image with a caption and walk through the entities.; §4 Goal 1-3 requirements are compact: add a separate non-functional requirements paragraph and an open-questions list per goal, as in `docs/specs/example-spec.md`.; §1.1 (369 words) needs prose arguing what this project does differently from the existing crime maps in the table; §1 and §1.2 are also short..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #86 (open, develop to main): Sprint 3 release with the map demo and §4 text; PR #91 (open, develop): map markers update with the crime-type filter; branch 83-update-prototype-readme: 4 commits not in develop; merge or delete; branch feature/map-filter-results: 3 commits not in develop, same work as PR #91.

**To do before your Sprint 3 review:**

1. Merge PR #86 into main after CI passes, so the review demo and §0-§4 are on the default branch.
2. Merge PR #91 and add a test for `/api/incidents` and for the filter's marker update in `prototype/`.
3. Embed Figure 3 (ER diagram) in §4 with a caption and one paragraph on the tables.
4. Add non-functional requirements and open questions to each Goal 1-3 specification summary in §4.
5. Expand §1.1 with prose on what Crime Busters does differently from the existing maps, and lengthen §1 and §1.2.
6. Close legacy issues #45-#47, #6, #7 or give them a type label and Sprint milestone.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Open the develop-to-main release PR today so the review demo and the default branch show the working prototype.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 7 of 10 stories have child issues (#29-#32, #34-#36); #33, #37, #38 have none. #80 carries sp: 1 under story #32, and #57 carries sp: 1 under pointed task #55.; #101 and #91 are open with no assignee, no Sprint milestone, and no link in proposal.md.; #106 and #98 are not linked in §4 of proposal.md on develop.; Stories #33, #37, #38 have no child issues; #59 hangs off epic #28, not a story.; PR #20 (old draft) has no Closes line; all Sprint 3 PRs #82-#109 close an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 11 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a table that indexes eight docs without summarizing them; Planned activities is a 42-row issue-link table with one intro paragraph.. |
| 3. Prototype works | ✅ done | Vehicle selection, service-record API and CRUD, manual entry and CSV import forms, dashboard with edit/delete, mileage entry, and status-label recommendation engine for three service types. CI: develop 11-17 green (4a0f895): Prototype job ran Install and test for both Node and Python, so API and UI tests executed. main 10-22 green but scaffold only. Tests: Seven pytest files (`test_vehicle_api.py`, `test_service_records_api.py`, label, engine, interval tests) and seven `tests/ui/*.test.js` page tests. |
| 4. Word export (`develop`) | ⚠️ partial | 54 issue citation(s) become small in-text tags; 54 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | The full Sprint 3 prototype runs from develop with green CI, but §4 specs and design are index-only, there is no implementation section, and main is scaffold. |

**Proposal, what to write:** §3 is about 190 words; add alternatives beyond rules versus AI (for example Flask versus other stacks, SQLite versus a hosted database) with reasons.; Five specs in `docs/specs/` are only indexed; summarize scope, requirements, acceptance criteria and open questions per epic in §4 prose.; Design lacks decisions with rejected alternatives and a not-yet-designed list; `docs/design/architecture.md` and `maintenance-dashboard.md` are not carried by proposal.md.; No §4 implementation prose: describe the service-record API, entry and import forms, dashboard, label rule and their tests, ending in task refs.; §1.2 is about 100 words plus a table; write each problem as a full paragraph ending in refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prototype, specs, design docs and diagrams; main is still the scaffold; branch feature/98-sprint-3-review: 8 commits not in develop (Sprint 3 review); branch feature/106-list-epic-27-spec: 2 commits not in develop; PR #107 closed unmerged.

**To do before your Sprint 3 review:**

1. Open and merge the develop-to-main release PR, with CI green on main, so the default branch shows the prototype and proposal.
2. Add §4 implementation prose for the vehicle, service-record, dashboard and recommendation code and its tests, ending in typed refs.
3. Summarize the five specs and `docs/design/architecture.md` in §4: requirements, acceptance criteria, decisions with rejected alternatives, open questions.
4. Remove sp: from #80 and #57; assign #91 and #101 with a Sprint milestone; link #91, #98, #101, #106 in §4.
5. Add child issues for stories #33, #37, #38, and re-parent #59 under a story.
6. Expand §3 alternatives and write §1.2 problems as paragraphs; replace the work-item table with prose.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Fix the failing Run gates job on main and merge PR #80, then rewrite `prototype/README.md` so the demo runs from a fresh clone.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 14 stories have child issues; #46 and #69 hang off epic #15, not a story. None of stories #25-#33, #38, #39, #53-#55 has child feature, task or sub-task issues.; #56 carries sp: under pointed task #13; #69 is labelled epic with sp: 5 and cited as a task.; #73 and #74 have no Sprint milestone; #3 is untyped; #6 has five assignees.; #79, #74, #73 are bare refs in §4, not typed refs.; 14 direct commits on main and develop, including repo restructuring; all 32 PRs close an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned Activities (5 bullets) and Tracked Task Issues (28 bullets) are lists; Specification and Design Documents is a link list followed by pasted doc text.. |
| 3. Prototype works | ⚠️ partial | Goal 1 network model: transfer CSV to wallet graph, derived views, time-respecting cycles, metrics and reconciliation checks via `demo.py` on a synthetic sample. CI: develop 11-17 green (525ffda): Install and test (Python) ran. main 11-15 red on Repository harness (Run gates); whether pytest collects the nested tests is unconfirmed. Tests: 31 tests in `tests/test_requirements.py` and `tests/test_acceptance.py` under the nested prototype folder; plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 44 issue citation(s) become small in-text tags; 44 issue(s) fill 4 table(s) in Appendix A; 1 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A tested Goal 1 demo runs on develop from the CLI, but there is no UI, run steps are wrong, specs and design are thin, and main has no prototype. |

**Proposal, what to write:** §1.1 now has a table and prose but compares only two vendors with one citation; add academic and open-source detectors and cite §8.; §1 Introduction is about 155 words; explain the domain, why wash trading matters and the sponsor context.; Epic #23 and #24 specs are summarized as scope paragraphs only; add requirements, acceptance criteria and open questions per epic.; Five diagrams have one-line captions; add prose per figure, decisions with rejected alternatives, and what is not designed yet.; No §4 implementation prose for `prototype/goal1-network-model-prototype/`; pasted `# Goal 1` headings sit inside §4 and need a place in the outline..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #80 (open, develop to main): releases the prototype, specs and diagrams to main; main CI is red; branch feat/69-goal1-network-model-prototype: 2 commits not in develop.

**To do before your Sprint 3 review:**

1. Fix the Run gates failure on main, then merge PR #80 so the default branch shows the prototype.
2. Rewrite `prototype/README.md` and the nested README so run and test commands work from `prototype/goal1-network-model-prototype/`.
3. Create child issues under each story (start with #31, #32, #25-#27), each with one assignee and a Sprint milestone; drop sp: from #56 and #69.
4. Write a §4 Implementation section for `stablescope/` modules and the 31 tests, ending in typed refs.
5. Summarize Epics #23 and #24 specs fully and explain each diagram in prose with decisions and rejected alternatives.
6. Expand §1 Introduction and §1.1 with more sources cited in §8; stop direct commits to main and develop.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

*Phone app records a marathon runner's GPS to Firebase; spectators follow on a web page; pace and finish-time prediction.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – 25** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Build the spectator view (#69) so the Sprint 4 review demo shows a phone's GPS position reaching a web page through Firestore.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33); 45 of 48 issues linked from the proposal. #62 (task under story #28) carries `sp: 3`; points belong on the story only, so story #28 is double counted.; PR #39 closes #21, which `proposal/proposal.md` does not link.; Open stories #28, #29, #30, #31, #33 and all Sprint 4 features have no merged PR yet; the Sprint 3 milestone is past due (11/11).; #1, #2, #6 are untyped and not in the proposal; #1 and #6 have no assignee (old Sprint 1 leftovers).; Tasks #58, #60, #65, #72 hang off no story; fine as process tasks, but #62 and #64 are the only prototype tasks under #28.. |
| 2. Proposal §0–§4 (`main`, ≈ 9 pages) | ⚠️ partial | ⚠️ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; the specs and design docs stay in `docs/` and the proposal carries only one Goal 3 paragraph.. |
| 3. Prototype works | ✅ done | Expo app with Firebase client, runner GPS tracking module (`runner-app/tracking.js`), Firestore smoke test, and pace calculation (`prediction/pace.py`). Spectator view is only a README placeholder. CI: main CI green 11/12 (720486b); Prototype job ran Node install and test (jest) and Python install and test; "Nothing to build" was skipped. develop is stale, still the login scaffold. Tests: 3 test files: `__tests__/App.test.js`, `__tests__/tracking.test.js` (jest) and `prediction/test_pace.py` (pace maths); all run in CI. |
| 4. Word export (`main`) | ⚠️ partial | 50 issue citation(s) become small in-text tags; 45 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A phone-GPS-to-Firestore demo and pace test can run, but §4 is incomplete and the spectator view (#69) that ties it together is not built. |

**Proposal, what to write:** §0 Abstract describes an ML performance-analysis app; the goals are live tracking, posts and a spectator page. Rewrite it to match §2.; §1 and §1.1 still hold template quote blocks and a stray 〈Your survey〉 placeholder; §1.1 ends mid-sentence ("our") and has a duplicated table cell.; §4 has no Environment and resources section: tech-stack reasons (Expo, Firebase, Mapbox, Python) appear only as one paragraph under Planned activities (#48, #72).; §4 specs: only Goal 3 is summarized; add scope, requirements, acceptance criteria and open questions for Goals 1 and 2 (#70, #73) from `docs/specs/`.; §4 design: carry the components, data model, key decisions with rejected alternatives and 'not designed yet' from `docs/design/architecture.md` and `data-model.md` into the proposal.; §4 implementation reads as a setup tutorial and says "we plan to use" for GPS and spectator code that already exists; describe what `tracking.js` and `pace.py` do..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - stale, holds only the login scaffold; later PRs targeting it never reached main's prototype.

**To do in Sprint 4:**

1. Build the spectator view (#69) in `prototype/spectator-view/` so the demo shows a runner position on a page end to end.
2. Add an Environment and resources subsection to §4 with one reason per tool (Expo, Firebase Firestore, Mapbox, Python); cite #48 and #72.
3. Summarize the Goal 1 and Goal 2 specs in §4 and complete the Goal 3 summary; finish #70, then link each spec's acceptance criteria to a test.
4. Move the data model, architecture and key decisions (with rejected alternatives) from `docs/design/` into §4 prose, each paragraph ending with issue refs.
5. Rewrite §0 Abstract so it matches Goals 1-3; fix §1.1 ending, remove 〈…〉 placeholders and template quote blocks in §0-§4.
6. Remove `sp: 3` from #62, close or type #1, #2, #6, and refresh `prototype/README.md` run steps.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Python app that finds signal peaks in 6G captures, classifies waveform and modulation, and explains the decision.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – 25** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 9), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge develop into main today so your Sprint 4 review shows the real prototype and proposal from the default branch.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 10 of 17 stories have child issues; #67, #69, #70, #71, #84, #95, #163 have none. Stories #67, #69, #70, #71, #84, #95, #163 have no child feature, task or sub-task.; 22 issues are not in proposal.md on develop, including tasks #154-#162, #147, #150, #152 and stories #95, #163.; #70 and #71 have no assignee or Sprint milestone; #103 is untyped with no assignee.; §4 still cites stories (#68, #84, #111, #126) that belong only in §2; 14 misplaced refs, one to deleted #63.; One direct commit on develop; PRs #1, #2 (old) have no issue; PRs #151, #153 still open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. |
| 3. Prototype works | ✅ done | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, Captum attribution and a transformer AMC module. CI: develop 11-13 green (2719a5c); Prototype job ran Install and test (Python) on team code. main is 10-16 scaffold. Tests: 14 test files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, pipeline gate, OFDM, training, transformer. |
| 4. Word export (`develop`) | ⚠️ partial | 70 issue citation(s) become small in-text tags; 54 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The peak-picker and classifier demo runs from develop, but §4 lacks Environment detail and Implementation, and main still shows the scaffold. |

**Proposal, what to write:** §4 Environment and resources is 28 words with template placeholders; give each tool (MATLAB, Python, Captum, dataset) and the reason it was chosen.; Only two specs (application architecture, waveform family) for five epics; Goals 1, 4 and 5 need scope, requirements, acceptance criteria and open questions.; No §4 implementation section for `waveform_identification/`, `xai/`, `GUI/` and `modulation_classification/`; add paragraphs ending in task refs.; §1.1 has four prose subsections but no pros-and-cons table or prose on what this project does differently.; §1.2 states P1-P3 in about 50 words; explain why each matters and tie it to a goal. No planned-activities prose exists..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop: holds the real prototype and §4 work; main is the login scaffold, promote it; PRs #151, #153 (open): Sprint 2 review notes and Word export converter; branches Application-Structure, docs/team-documentation, docs/150-sprint-2-review, docs/152-word-export: commits not in develop.

**To do in Sprint 4:**

1. Open and merge a develop-to-main PR so `prototype/` and `proposal/proposal.md` on main are current; keep main CI green.
2. Link #147-#162 and #95 in §4 as typed refs, and move story refs out of §4 into §2.
3. Create child issues for stories #67, #69, #70, #71, #84, #95, #163; assign one person and a Sprint milestone to each.
4. Replace the §4 Environment placeholder with each tool and why it was chosen, ending paragraphs with task refs.
5. Write a §4 Implementation section for the four prototype packages and planned-activities prose for the remaining work.
6. Add short specs for Goals 1, 4 and 5, and a §1.1 pros-and-cons table with prose on what differs.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – 25** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Sprint 4 bar:** finalize `proposal.md` as the whole paper, §0–§8, more than 50 pages without the Appendix (now ≈ 8), and complete the prototype so it is fully functional, with a test per acceptance criterion. The checks below still apply; finish every open item first.

**Start here:** Merge the open feature PRs, then rewrite `prototype/README.md` and rename the test file so CI exercises the app.

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
3. Rename `TestAssignments.py` to `test_assignments.py` and add tests for deadline suggestion and CRUD, one per acceptance criterion in `docs/specs/specs-G1.md`.
4. Merge the architecture diagram branch and add system context, data model and data flow diagrams with prose to §4.
5. Add Sprint milestones to #93, #94, #124, keep one assignee per issue, and fix malformed refs in the Planned Activities table.
6. Write §4 Environment with a reason per tool, an Implementation section, and carry specs and the ER design into §4 prose.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · G14: Cyber Sandbox (Cyber Squad)

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – 25** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

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

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · Sprint 3 review held Thu Nov 12 · **Sprint 4: Nov 12 – 25** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

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

**To do in Sprint 4:**

1. Write §4 Specifications as prose from `docs/specs/game-engine.md` and `game-demo.md`: scope, FR, NFR, acceptance criteria, open questions per epic.
2. Write §4 Design (components, ECS data model, data flow, decisions with rejected alternatives, undesigned parts) from `docs/design/architecture.md`.
3. Add a §4 Implementation section on what the CMake prototype builds and tests today, citing #63, #66, #67, #82.
4. Replace the 38-row planned-activities table with paragraphs and typed refs; add #76, #78, #82 and epic #6.
5. Create child issues under stories #26-#29; remove `sp:` from #46 and fix its parent.
6. Explain Figures 1 and 2 in prose, and fix the 〈…〉 title in `prototype/README.md`.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Monitors cross-chain bridge vaults, learns normal outflow, and alerts on drains with measured false alarms.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Merge PR #115, then write the decisions-and-rejected-alternatives and not-yet-designed paragraphs after D6 in §4 from `docs/design/architecture.md`.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#14, #15, #17, #18, #20); #5, #16, #19, #21 have none. Stories #19 and #21 (Sprint 4) and closed stories #5 and #16 have no child issues.; #113 and #114 (Goal 2 and 3 spec summaries) are not linked from the proposal; PR #115 that cites them is open.; PRs #75 and #35 have no `Closes #N`.; Three direct `docs:` commits on main and develop (team details), outside any PR.. |
| 2. Proposal §0–§4 (`develop`, ≈ 21 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: Table 9 lists the three specs and design doc as file paths with issue refs; apart from Goal 1, no spec has a prose summary behind it.. |
| 3. Prototype works | ✅ done | Detector, SQLite store, live Ethereum poller, replay of five past hacks, false-alarm evaluation on real normal days, Slack notifier, FastAPI API, web dashboard, demo mode. CI: develop b3da6c6 (11/17) green; Prototype job ran 'Install and test (Python)', so team tests executed. main last ran 11/3, also green. Tests: Four files in `prototype/tests/`: detector, live loop, baseline check, data pipeline; proposal reports sixty tests. |
| 4. Word export (`develop`) | ✅ done | 69 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The prototype runs in live, demo and replay modes and could be shown; §4 still lacks Goal 2 and 3 spec summaries and decisions prose. |

**Proposal, what to write:** §4 specs: only Goal 1 is summarized in prose; write Goals 2 and 3 (scope, requirements, acceptance criteria, open questions) and merge PR #115.; §4 design: context, architecture, data model and data flow are explained under D0-D6; key decisions with rejected alternatives and what is not designed yet are missing.; Figures 1 and 2 still sit at the end of §4 as the planned design; fold them into the D1-D2 prose or drop them.; main still holds the Nov 3 paper (47k characters vs 71k on develop); the graded branch must carry D0-D6 and the implementation details..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #115 - Goal 2 and Goal 3 spec summaries in §4 (develop); closes #113 and #114; PR #109 - counts 30 normal days per bridge for Objective 2.3 (develop); develop to main - D0-D6, implementation details and Sprint 3 tasks are not on main.

**To do before your Sprint 3 review:**

1. Merge PR #115 so the Goal 2 and Goal 3 spec summaries are in §4 with their issue refs, and check each states acceptance criteria and open questions.
2. Add to §4 after D6 a paragraph on the key design decisions with the rejected alternatives, and one on what is not designed yet.
3. Create child tasks under stories #19 and #21 before Sprint 4 starts, each with one assignee and a Sprint milestone.
4. Merge PR #109, then write the 30-day false-alarm numbers into §4 against Objective 2.3.
5. Fold Figures 1 and 2 into the D1 and D2 explanations, labelled planned versus built.
6. Release develop to main so the graded branch holds the current paper and prototype.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Fix the failing 'Run gates' step on main, then merge PR #70 and build one running slice in `prototype/` with a test; that unlocks a demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 6 stories have child issues (#25, #29, #30); #26, #27, #28 have none. `sp:` on child tasks #41, #42, #43, #49, #55, #57, #58, #59, #65, #68 and #51 under stories or pointed tasks.; #41, #49, #51, #55, #57, #58, #59, #62, #63, #64 are not linked from the proposal.; #49 and #55 have no assignee; #63 and #64 have no parent.; 17 merged PRs (e.g. #31-#39, #45, #67) have no `Closes #N`; main has 30 direct commits.; 7 of 16 proposal issue refs are bare links, not typed refs (e.g. #42, #43, #46, #47, #53).. |
| 2. Proposal §0–§4 (`main`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1 and §1.2 are tables, §2 is nine bullets, and the spec/design document table and 'Planned activities' (5 rows) stand in for prose; neither carries issue refs in sentences.. |
| 3. Prototype works | ❌ skeleton | Module skeleton plus a starting UI (`frontend/ScreenViews.py`, PR #69) and `backend/lastfm.py`; `db.py` and `schema.sql` are in open PR #70; README still says skeleton. CI: main 59bd5d6 (11/16 PST) red: Repository harness failed at 'Run gates'; Prototype job green but no team tests exist. develop is a stale scaffold. Tests: none on main; no `prototype/tests/` folder although the README claims four tests |
| 4. Word export (`main`) | ✅ done | 14 issue citation(s) become small in-text tags; 14 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | A starting UI exists but no tested slice, main CI is red on the harness gate, and §4 has no spec or implementation prose. |

**Proposal, what to write:** §1.1 is a four-row table with no prose and no citations to §8; add paragraphs on what SonicScape does differently.; §1.2 is a table and §2 is bullets; write problem statements and explain each epic and story in paragraphs ending in refs.; §4 specs: summarize `docs/specs/specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` (scope, FR/NFR, acceptance criteria, open questions) in prose.; §4 swipe sequence, architecture and system context diagrams are raw Mermaid with no explaining prose; data flow, screen flow and database design are real prose.; §4 has no implementation details; planned activities list only five Sprint 2 rows; §5-§8 still hold template text..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #70 - SQLite connections in `db.py` and `schema.sql` for Goal 3 login backend, open against main; develop branch - stale scaffold with a different title; align it with main or retire it.

**To do before your Sprint 3 review:**

1. Open the failing 'Run gates' step on main, fix what it names, and get CI green.
2. Merge PR #70, then build the first end-to-end slice in `prototype/` (Last.fm into SQLite, galaxy view, one swipe) with tests in `prototype/tests/` per acceptance criterion.
3. Replace the README run line (it reads 'cd cd') and the four-tests claim with commands and tests that work from a fresh clone.
4. Summarize `specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` in §4, then add a caption and paragraph for the swipe, architecture and context diagrams.
5. Rewrite §1.1, §1.2 and §2 as prose with citations matching §8; add an implementation-details subsection and Sprint 3-4 planned activities.
6. Remove `sp:` from child tasks, assign #49 and #55, link #41, #49, #51, #55, #57-#59, #62-#64 in §4, and add children under #26-#28.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: Project Rogue, 2D action roguelite with flexible builds (Unity)

*A Unity 2D action roguelite where builds develop through weapons, attributes and branching three-Act runs.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Write the §4 Implementation subsection from the existing combat and traversal code, then add one edit-mode test per acceptance criterion in the Goal 2 spec.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32 via #72, #35 via #64, #41 via #48); #33, #34, #36-#40 have none. #65, #64, #56, #53 carry sp: under a story or epic; points belong on the story only.; #76, #74, #58 have no Sprint milestone; #26 and #13 are untyped with no milestone.; #76, #74, #72, #65, #64, #61, #58, #56, #53 are not linked from proposal.md.; Epics #29-#31 are cited in §1 and story #41 in §4; epics and stories belong in §2 only.; #60, #59, #58, #51, #49, #47 are tasks with no parent story or epic.; Sprint 3 closes 11/18 with 6 issues open and none closed.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a 5-row link table; Planned activities is a 28-row issue table with only four short paragraphs.. |
| 3. Prototype works | ⚠️ partial | Unity 6 project with a combat demo (resolver, abilities, target dummy, loadouts) and a movement/traversal room; two demos, no run loop yet. CI: develop b5888ff (11/16 PST) and main d6e8c9a green; the Prototype job ran only 'Install and test (Python)' on the scaffold, so no Unity code was compiled or tested. Tests: No automated tests; `Assets/Editor/ProgressionVerification.cs` and the `Test_Combat` scene serve as manual checks. |
| 4. Word export (`develop`) | ✅ done | 54 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Combat and traversal demos can be shown from develop, but §4 lacks specification, design and implementation prose and CI does not run the game. |

**Proposal, what to write:** §4 Specifications: the three goal specs in `docs/specs/` are not summarized per epic with requirements and acceptance criteria.; §4 Design: `docs/design/system-overview.md` is only linked; carry context, components, data model, data flow, decisions and open items into the proposal.; §4 Diagrams: the class diagram and run/room/reward flowchart in `docs/design/diagrams/` are not embedded; the two embedded figures get one short paragraph each.; §4 Implementation: add a section describing what `prototype/ProjectRogue` implements (combat resolver, abilities, movement, traversal room, boons) with task refs.; §2 and §3 disagree on starting classes versus weapon-and-element builds; align them. main still has the template §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: §3-§4 text, diagrams, specs and the prototype's movement work are not on main.

**To do before your Sprint 3 review:**

1. Create child issues for stories #33, #34, #36-#40, each with one assignee and a Sprint milestone, and remove sp: from #65, #64, #56, #53.
2. Link #76, #74, #72, #65, #64, #61, #58, #56, #53 from §4 as typed refs and move epic refs out of §1 and story #41 out of §4.
3. Write a per-epic specification summary in §4 (scope, functional and non-functional requirements, acceptance criteria, open questions) from the `docs/specs/` files.
4. Carry the system overview and combat class diagram into §4 with context, components, data model, data flow, rejected alternatives and open items.
5. Add a §4 Implementation subsection naming what each folder under `prototype/ProjectRogue` does, with task refs.
6. Add edit-mode tests for combat and progression and run them in CI or record manual results.
7. Merge develop into main through a reviewed PR and keep main demo-ready.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · G19: Titan Security, Radar over WiFi drone detection (RTX-AST)

*Detect small drones and estimate position and movement from Wi-Fi CSI, compared against conventional radar.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Merge PR #87 so §4 has a real environment section, then replace the course `test_login.py` with tests for `capture.py` and `quality_check.py`.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 12 of 12 stories have child issues, but 8 of those children (#77-#84) have no assignee or Sprint milestone. #77-#84 are untyped, have no assignee and no Sprint milestone; none is linked from proposal.md.; #88, #71, #53, #47, #45, #39 carry sp: under a story; points belong on the story only.; #88, #86, #75, #71, #65, #53, #51, #39, #37, #38, #43 are not linked from §4.; §4 Planned activities lists only 8 Sprint 1 tasks; no Sprint 2 or Sprint 3 work item appears.; Open PRs #87 and #89 are unmerged; #85 was closed without merging.; Story #73 has no sp:; every story must carry its points once.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ❌ skeleton | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a link table plus template placeholder rows; Planned activities is an 8-row Sprint 1 issue table with one sentence of prose.. |
| 3. Prototype works | ⚠️ partial | CSI capture and recording quality-check stubs (`capture.py`, `quality_check.py`) with a sample recording; README keeps scaffold text and a placeholder row. CI: main 7fca571 and develop 55e7853 green (11/5 PST); 'Install and test (Python)' ran, but the only test is the course `test_login.py`, so team code is untested. Tests: Only the course `prototype/tests/test_login.py`; nothing tests capture or quality check. |
| 4. Word export (`develop`) | ⚠️ partial | 30 issue citation(s) become small in-text tags; 29 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | §4 is largely template and the prototype is stubs with no team tests; a CSI capture could be shown but not a detection slice. |

**Proposal, what to write:** §4 opens with a template placeholder; write each tool, device, host and data store with the reason for the choice (PR #87 holds a draft).; §4 Specifications: summarize the three specs in `docs/specs/` (CSI sensing, drone detection, evaluation) with requirements and acceptance criteria.; §4 Design: only the Level 0/1 data flow is in the proposal; add context, components, data model and decisions with rejected alternatives.; §4 Diagrams: `high-level-architecture.png`, `system-context.png` and `sequence-diagram.png` exist in `docs/design/diagrams/` but are not embedded.; §1 is 148 words and §3 is informal; expand both and add a Sprint 3 Implementation and planned-activities narrative..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #87 - §4 CSI experiment environment (#86), open against develop; PR #89 - classifier training and evaluation plan (#88), open against develop; Branch feature/#51-section4-update - drone detection and evaluation spec additions to §4, not in develop.

**To do before your Sprint 3 review:**

1. Merge PRs #87 and #89 after review, delete branch feature/#51-section4-update once its §4 text is in develop, and merge develop into main.
2. Assign and milestone #77-#84, type them, and add them and #86, #88 to §4 as typed refs.
3. Remove sp: from #88, #71, #53, #47, #45, #39; keep points on the stories only.
4. Write the §4 environment, three per-epic specification summaries and a design narrative, embedding `high-level-architecture.png` and `system-context.png` with captions.
5. Replace `login.py` and `tests/test_login.py` with capture and quality-check tests; fix the README run block and the Sprint 3 row.
6. Add Sprint 3 and 4 work items to the §4 Planned activities with prose describing the remaining work.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · G20: Solos, Insomnia, first-person horror maze game in Unreal Engine

*Unreal Engine 5 first-person horror maze game with adaptive monsters, encounter director and responsive atmosphere.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Merge the `.mmd` diagrams onto develop and embed them in §4 with captions and prose, closing #64 and #77.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child issues (#13, #14, #15, #18, #19, #20, #22, #23). Only 11 typed refs; 39 issues are cited as bare #N or untyped links, mostly in §4 Planned activities.; #41 carries sp: 3 under story #13; points belong on the story only.; #65-#68 and #76-#78 are standalone tasks with sp: and no parent story or epic.; Sprint 3 closes tomorrow with 34 open issues and 1 closed; PR #82 for #42 is still open.; Epics #12, #17, #21 sit in Sprint 4 while their stories sit in Sprint 3.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a link table still holding two template placeholder rows; the 41-row work-item table follows real workstream prose.. |
| 3. Prototype works | ⚠️ partial | Unreal Engine 5 first-person starter project with sprint and crouch movement (#40); no maze, monster or director yet. CI: develop c2776b9 (11/16 PST) and main 4235cfb (11/5 PST) green, but the Prototype job ran only 'Nothing to build'; CI does not exercise the Unreal project. Tests: None automated; the README describes a manual smoke test and records it as passed. |
| 4. Word export (`develop`) | ⚠️ partial | 50 issue citation(s) become small in-text tags; 50 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The starter level with movement should run per the README, but there is no monster or maze yet, and §4 design and diagrams are missing. |

**Proposal, what to write:** §1.1 compares three games in prose with short pros and cons, but has no comparison table; task #68 is open.; §4 Specifications: three spec files in `docs/specs/` are only listed; summarize scope, requirements and acceptance criteria per epic.; §4 Design and Diagrams: nothing is embedded; the `.mmd` diagrams are on main only, so bring them to develop with captions and prose.; §3 still ends with template text and §4 Environment still carries template diagram instructions; delete them.; §4 Implementation: describe what the starter project and movement work (#40) implement; add the architecture and monster-state design..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #82 - objective tracking UI for #42, open against develop; Branch issue-42-objective-tracking - 1 commit not in develop; develop to main - main §3 is still the template and §4 trails develop; docs/design/*.mmd diagrams are on main only; bring to develop and into the proposal.

**To do before your Sprint 3 review:**

1. Rewrite the issue refs in §4 Planned activities as typed refs, such as feature:#40 and task:#41, and remove sp: from #41.
2. Parent #65-#68 and #76-#78 under an epic or story and make sure each has one assignee and a Sprint milestone.
3. Merge the `.mmd` diagrams onto develop, export images, embed them in §4 with captions and explaining prose (#64, #79).
4. Summarize the three specs per epic in §4 and write the design documents: context, components, data flow, decisions, open items (#66).
5. Add the §1.1 comparison table (#68) and delete the template text left in §3 and §4.
6. Build the maze slice (#71) with a manual test per acceptance criterion, then merge develop into main (#77, #78).
7. Merge PR #82 and close the Sprint 3 issues that are done before the review.

[↑ Back to all groups](#groups)

## About this page

The Sprint 2 checklist (specs, design, environment, prototype wiring) is now folded into rule 2 (§4) and rule 3. The earlier editions, including the Sprint 2 cards, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
