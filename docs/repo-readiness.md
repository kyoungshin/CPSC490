# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.

**CPSC 490 · Fall 2026 · swept 2026-11-10 20:22 UTC.** Earlier editions are kept in this file's git history.

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
3. **The code under `prototype/` must always work, never be broken.** Whatever is in it has to install, run and pass CI (the *Prototype build & tests* job). For Sprint 3, build the slice your design depends on most, write a test for each of its acceptance criteria, and demo it at your review. The folders mirror your architecture diagram, and `prototype/README.md` has run commands that work from a clean clone ([CI gate](https://github.com/kyoungshin/CPSC490/blob/main/.github/workflows/ci.yml)).

4. **Your proposal converts to Word.** I convert each group's `proposal/proposal.md` with pandoc and the course converter, using the one command in [README §3](https://github.com/kyoungshin/CPSC490#3-the-proposal-proposalproposalmd). **Updated Nov 8:** the converter (`proposal/to-word.lua` in the course repo) now pulls every GitHub issue link out of the text and lists it in *Appendix A. Issue References*, as tables grouped by type (epics, stories, features, tasks, sub-tasks). In the text, each link becomes a small citation such as `[task:#23]` that jumps to its row. Copy the new `proposal/to-word.lua` into your repository. To fill in the Title column, first export your issue titles with `gh issue list --state all --limit 1000 --json number,title > proposal/issues.json`. A reference only moves to the appendix if it's written as a link: `[task:#23](https://github.com/OWNER/REPO/issues/23)`.

As before, it only counts once it's **merged into `develop` or `main`**. Work left in a branch or an open pull request doesn't count yet.

| Groups | Sprint 3 | Sprint 3 review (start of Sprint 4) |
|---|---|---|
| G01–G05 | Oct 27 – Nov 9 | **Tue Nov 10** |
| G11–G15 | Oct 29 – Nov 11 | **Thu Nov 12** |
| G06–G10 | Nov 3 – 16 | **Tue Nov 17** |
| G16–G20 | Nov 5 – 18 | **Thu Nov 19** |

## Class at a glance

✅ done · ⚠️ partial · ❌ not there yet. **Pages so far** is a rough estimate (words outside the Appendix ÷ 500) to set against the 50-page final; tables and figures add a little more.

| Group | Sprint 3 review | 1. PRs ↔ issues ↔ proposal | 2. Proposal §0–§4 | 3. Prototype works | 4. Word export | Demo-ready | Pages so far |
|---|---|---|---|---|---|---|---|
| [G01](#g01) BGAF | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 82 |
| [G02](#g02) Linux Larpers | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 15 |
| [G03](#g03) G03 California | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Tue Nov 10 | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 33 |
| [G05](#g05) Fighting Mongooses | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G06](#g06) GapWise | Tue Nov 17 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G07](#g07) Mighty Morphins | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 8 |
| [G08](#g08) Crime Busters | Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 7 |
| [G09](#g09) Sigma Squad | Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 10 |
| [G10](#g10) Team Jiddak | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 5 |
| [G11](#g11) 5 Guys | Thu Nov 12 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 6 |
| [G12](#g12) ACJMM | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 7 |
| [G13](#g13) G13 BYKX | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 7 |
| [G14](#g14) Cyber Squad | Thu Nov 12 | ❌ | ⚠️ | ❌ | ✅ | ❌ | ≈ 6 |
| [G15](#g15) HIBBI-01 | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) G16 | Thu Nov 19 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 14 |
| [G17](#g17) G17 | Thu Nov 19 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | ≈ 5 |
| [G18](#g18) G18 | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) Titan Security | Thu Nov 19 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G20](#g20) Solos | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |

- **Rule 1 met:** 1 of 20 (G04).
- **Proposal §0–§4 complete:** 0 of 20 (none).
- **Prototype working, with a real slice and tests:** 8 of 20 (G01, G02, G03, G04, G05, G09, G12, G16).
- **Ready to demo both today:** 0 of 20 (none).

**What changed since the Nov 5 edition:**

- **Prototypes moved on `develop` for three groups since Nov 8:** G02 (observation model and API, with Angular and ESP32 scaffolds), G03 (transcriber, recognizer and plotting with five test files) and G11 (a Firebase smoke test, plus the §4 tech stack and three goal specs). Their rule 3 mark went up.
- **G04 now passes rule 1:** every story is broken down and the chain is complete. It is the first group with a ✅ on the chain.
- **Proposal §4 grew** for G01 (back-end module design), G05 (spec and design summaries), G10 (two epic specs and diagrams), G12, G13, G15 and G16. No group has §0–§4 complete yet, so rule 2 is still open for all 20.
- **No change since Nov 8:** G06, G09, G17, G19 and G20. G18 changed very little.
- **Finished work still sits on `develop` only** for many groups (G02, G03, G05, G06, G09, G12, G13, G15, G16, G18, G20). Merge it to `main` before your review: I read the best of both branches here, but your Word export and final submission come from `main`.
- **Check what your CI really tests.** For several groups the prototype job is green without building or testing team code (G13, G15, G18, G20), and two READMEs describe files that aren't in the repository (G10, G14). A green check only counts when it runs your code.
- **Review dates:** G01–G05 Tue Nov 10, G11–G15 Thu Nov 12, G06–G10 Tue Nov 17, G16–G20 Thu Nov 19.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and strategy backtesting

*Pipeline that cleans SonarX Hyperliquid data, rebuilds order books, validates them, and gates backtests of trading strategies.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Run the `prototype/README.md` smoke load and the 14 tests on a fresh clone and rehearse the §4 walkthrough for tonight's review (#272).

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 13 of 14 stories have child issues (#58, a dropped objective, has none); stories #24, #26, #27 are open. Eleven tasks carry `sp:` under a story or pointed task: #195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134.; 93 epic/story citations sit in §4 instead of §2 only; #278 is open; #151 is cited as a task but is a sub-task.; Sprint 4 features #144, #145, #148, #157-#159, #163-#167, #169 and tasks #94, #147 have no assignee; #202, #187 have 2-3.; 33 tasks have no parent (#271, #264, #249, #232, #231, #206 ...); stories #24, #26, #27 have no assignee.; PR #126 and early PRs have no `Closes #N`; three direct commits on main (README and docs).. |
| 2. Proposal §0–§4 (`main`, ≈ 82 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: None in place of prose; §4 is paragraphs ending in refs. A small link table remains in the specification index only.. |
| 3. Prototype works | ✅ done | DuckDB schema and a SonarX L2 snapshot loader; replay, validate, gate and backtest modules are docstring stubs; front end is the Vite starter page. CI: main run green; Prototype job ran Python install and the 14 pytest tests; Node steps skipped, so the Vite front end is not built in CI. Tests: `prototype/tests/test_package.py` (layout, step order) and `test_storage.py` (schema, load, exact decimals, repeat load). |
| 4. Word export (`main`) | ✅ done | 665 issue citation(s) become small in-text tags; 164 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The paper is demo-ready, but the prototype only loads one snapshot file into DuckDB; replay engine and everything after it are not built. |

**Proposal, what to write:** §1.2 Problem Statements is 233 words and a two-row table; expand into full paragraphs for P1 and P2 with the evidence behind each.; Dedicated validation-and-gate and replay-engine designs (#260-#262, open) are not in §4; the module design only summarizes them at contract level.; §4 holds about 16,000 words of spec and design prose, but 93 epic/story links belong in §2; move them (#278).; Planned activities mix old and new work; mark what is done, in progress and left so the remaining work is clear..

**Merge first** (it doesn't count until it's in `develop` or `main`): `develop` (43K characters, 15 placeholders) is far behind main; sync it or state main is the integration branch (#274); Branches 18-abstract-intro, 43-update-goals-and-objectives, 58-cite-dropped-objective(-main) are unmerged; merge or delete.

**To do before your Sprint 3 review:**

1. Rehearse the demo from `prototype/README.md` on a fresh clone: the smoke load into DuckDB plus the 14 tests, then walk §4 (#272).
2. Write the validation-and-gate design with diagrams and summarize it and the replay design in §4 (#260, #261, #262).
3. Build the in-memory order book and replay engine core (#144, #145) in `prototype/src/bgaf_pipeline/replay.py`, one test per acceptance criterion.
4. Finish #278: move epic and story citations from §4 to §2, and change the four `[task:#151]` refs to `[sub-task:#151]`.
5. Remove `sp:` from #195, #187, #184, #183, #181, #180, #175, #174, #173, #172 and #134; keep points on the story or standalone task.
6. Assign one owner to each Sprint 4 feature and to stories #24, #26, #27; reduce #202 and #187 to one assignee.
7. Expand §1.2 into two full problem paragraphs and add a Node build step so CI exercises `prototype/frontend`.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

*ESP32 nodes passively capture Wi-Fi/Bluetooth metadata; FastAPI and PostgreSQL store it for device identification on a dashboard.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Write the Goal 1 spec in `docs/specs/` and its §4 summary, since the Sprint 3 slice implements Goal 1 and §4 has no specification.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); #49, #51-#55, #58-#61 have none. Ten stories have no child issues: #49, #51-#55, #58-#61; Goals 2 and 3 are not broken down on the board.; Tasks #95, #92, #91 carry `sp:` under stories #16 and #45; 18 older tasks double-count under pointed tasks #21, #22, #23, #70, #79.; #130, #99, #20 are not cited in the proposal; #101, #80, #79, #72, #70, #6 are untyped or bare; 27 epic/story cites sit outside §2.; Open PRs #126, #127, #131 on develop; eight direct commits on develop and one on main; old PRs #3-#5 lack `Closes`.. |
| 2. Proposal §0–§4 (`develop`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: Specification and design index is a 2-row table with a template comment; no spec or design prose in §4.. |
| 3. Prototype works | ✅ done | FastAPI backend with /health, /health/db, POST and GET /observations on PostgreSQL via Compose; Angular starter page; ESP32 firmware prints a skeleton string, no capture yet. CI: develop run green; Prototype job ran Python install and tests for the backend only; Angular and ESP32 projects are not built in CI. Tests: `prototype/backend/test_main.py` (health) and `test_observations.py` (observation model and API); `dashboard/src/app/app.spec.ts` not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 122 issue citation(s) become small in-text tags; 74 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Backend and database can be demoed from develop, but §4 lacks specs and implementation, main is still a skeleton, and no ESP32 capture exists. |

**Proposal, what to write:** No `docs/specs/` file exists; write the Goal 1 spec (scope, functional and non-functional requirements, acceptance criteria, open questions) and summarize it in §4.; `docs/design/architecture.md` exists on develop but is not in the §4 index; carry components, data model and key decisions into §4 prose.; §4 has no Prototype implementation section; describe the observation model, API routes, Compose database, Angular and ESP32 scaffolds, citing #107-#114.; main still holds the §3-§4 template with 34 placeholders; the real text is on develop only. §1.2 is one paragraph and a table..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #126 (develop) — observation model tests, closes #109; PR #127 (develop) — observations persist after backend restart (#114); PR #131 (develop) — Sprint 3 review (#130); develop to main — main still has the template §3-§4 and health-only backend.

**To do before your Sprint 3 review:**

1. Write `docs/specs/goal-1-capture.md` with scope, requirements, acceptance criteria and open questions; add its summary and issue refs to §4.
2. List `docs/design/architecture.md` in the §4 index and write components, data model and rejected alternatives into §4 prose.
3. Add a §4 Prototype implementation section: observation model, routes, Compose database, Angular and ESP32 scaffolds, with #107-#114 refs.
4. Rehearse the review demo: start Compose, run `fastapi dev`, POST then GET an observation, restart and show it persists (#114), run `pytest`.
5. Merge PRs #126, #127, #131 with `Closes #N`, then release develop to main so main carries the real §3-§4.
6. File features and tasks under stories #49, #51-#55, #58-#61; remove `sp:` from #95, #92, #91; cite #130, #99, #20 in §4.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · G03 California: Three AIs and Literate Programming (RTX-3)

*Jupyter pipeline that transcribes an equation, generates noisy data, trains a PyTorch model and plots results.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Write the §4 Environment and resources section, since it is still the template prompt and everything else in §4 hangs off it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 13 stories have child issues (#50 has #69, #70; #46 has #78). Eleven stories have no child issues (#30-#37, #45, #47, #48), though dataset, storage and plot code is already built.; 25 issues are absent from the proposal: #78, #70, #69, #65, #60, #51, #41 plus 18 untyped meeting and document issues.; No Sprint milestone on #75, #68, #55, #53, #47, #45, #42, #41, #24, #20; #75, #71, #68, #53 have no assignee.; PRs #77 and #81 target feature branches and, with #8, #9, #11, #29, lack `Closes`; ref `[story:#31]` links issue 30.; Eighteen issues are untyped (no feature, task or sub-task label) and the single direct commit sits on main.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a one-row link table plus a template placeholder; the spec index is a table of three rows.. |
| 3. Prototype works | ✅ done | Transcriber router and recognizer, verifier with accept record, dataset generation, storage and display, PyTorch training with loss curve, equation plot, pipeline notebook. CI: develop run green; Prototype job installed and ran pytest in Python on team tests. main last ran Oct 27 and lacks the new work. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train, plot_equation tests; none named for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The develop prototype and notebook can be shown, but §4 environment, implementation and activities are placeholders and the README run steps are the course template. |

**Proposal, what to write:** §4 opens with the template prompt and a 〈placeholder〉; write Environment and resources with a reason per tool (Jupyter, PyTorch, recognizer and code-generation AIs).; Three specs and `architecture.md` are only indexed; carry them into §4 in full or as summaries, and list `docs/specs/workbook-generation.md`.; No Prototype implementation or Planned activities prose; describe transcriber, verifier, dataset, training and plotting and the remaining work, citing #69, #70, #78.; §1.2 is a table with unfilled 〈Goal 2 (#n)〉 and 'Goal 4 (#)'; §1 Introduction is one paragraph. Proposal text is identical on main and develop..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main — transcriber, recognizer, plot, notebook and tests are not on main; PR #83 (develop) — open; merge with `Closes #N`; feature/47-plot-test-data — 3 commits not in develop.

**To do before your Sprint 3 review:**

1. Write §4 Environment and resources: each tool, hosting, data store and AI service with the reason chosen; remove the template prompt and placeholder.
2. Rewrite `prototype/README.md`: drop login.py, give fresh-clone setup, run, test and notebook steps, then rehearse the review demo from it.
3. Carry the specs and `docs/design/architecture.md` into §4 as summaries with issue refs; add `docs/specs/workbook-generation.md` to the index.
4. Write §4 Prototype implementation and Planned activities as prose, citing #69, #70, #78 and the remaining Goal 3 and Goal 4 work.
5. File feature and task children under stories #30-#37, #45, #47, #48; set a Sprint milestone on #45 and #47 and one assignee each.
6. Type and cite #69-#72, #78, #51, #60, #65 in §4; fix `[story:#31]` to link issue 31; fill the §1.2 placeholders.
7. Release develop to main through a `Closes #N` PR and add tests for generate_dataset, store_datatype and display_dataset.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket trader PNL and ranking dashboard (SNX-1)

*Computes Polymarket wallet profit and loss from SonarX Polygon data in Snowflake, ranks traders, and feeds a dashboard.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Get Snowflake credentials (#153) and run the PNL code on real SonarX trades so the review demo shows live output, not only fixtures.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 12 of 12 stories have child issues (feature, task, sub-task). 22 tasks have no parent story (#155, #154, #152, #149, #142, #141 ...); all are standalone pointed writing or release tasks, which is allowed.; Open Sprint 3 items past the milestone: #149, #152, #153, #154, #155, #125, #105; close or carry them to Sprint 4.; Sprint 1 PR #4 has no `Closes`; every later PR links an issue; no direct commits; no `sp:` under any story.; Issue #20 (kickoff notes) has no assignee.. |
| 2. Proposal §0–§4 (`main`, ≈ 33 pages) | ⚠️ partial | ⚠️ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: None in §4; planned activities are prose by goal. §1.1 is a table whose 'Why ours differs' cells are placeholders.. |
| 3. Prototype works | ✅ done | Settings loader, Snowflake client, smoke query, FIFO position builder and resolution matching checked against the spec's worked example; no live data, ranking or dashboard. CI: main run green; Prototype job installed and ran pytest on team code (positions, resolutions, settings, Snowflake client); live smoke test skips without credentials. Tests: `tests/unit/` positions, resolutions, settings, snowflake_client; `tests/integration/test_smoke_query.py` skipped without credentials; worked-example fixture. |
| 4. Word export (`main`) | ✅ done | 119 issue citation(s) become small in-text tags; 105 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Unit tests and §4 specs and designs are demoable; a live Snowflake run needs credentials (#153) and no ranking or dashboard code exists yet. |

**Proposal, what to write:** §1.1 'Why ours differs' cell reads 'Will discover after meeting with mentor' for every tool; write the comparative prose and cite §8.; §0 Abstract is 148 words in future tense; state the problem, approach and what the prototype already computes.; §4 Environment and resources is one paragraph; add Snowflake, Python, CI, results store and dashboard framework with reasons, and settle the two undecided choices.; §1.2 is 90 words; write two problem paragraphs with issue refs. §5-§7 still hold template text (not required yet)..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #158 (main) — read-only SQL queries and fixture tests (#105); PR #159 (main) — Goal 3 dashboard specification (#125); PRs #150, #156, #160 (develop) — §5-§7, dashboard questions, Sprint 3 review numbers; Eight branches, e.g. 59-pnl-pipeline and 125-dashboard, hold commits not in develop; merge or delete.

**To do before your Sprint 3 review:**

1. Rehearse the demo: run `python -m pytest -q` in `prototype/`, then show the worked example against `docs/specs/pnl-calculation.md`.
2. Get Snowflake credentials for all members (#153) and run `smoke_query.py` plus the #105 queries on real trades so the demo shows live output.
3. Merge PRs #158, #159, #150, #156, #160 and release develop to main (#154); delete or merge the eight stale branches.
4. Replace 'Will discover after meeting with mentor' in §1.1 with a prose argument per tool, and expand §0 and §1.2.
5. Expand §4 Environment and resources with a reason per tool, and decide the results store and dashboard framework.
6. Start Sprint 4 with the ranking slice (Goal 2) in `prototype/src/services/`, one test per acceptance criterion.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, Whale Identification/Location System

*Passive acoustic system: AI detects whale calls, a hydrophone-delay locator estimates direction and distance.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge PRs #62 and #72 into develop, then write §0 and §3 so the proposal stops reading as template prompts.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 9 stories have child issues; #10-#13, #15, #16, #18 have none (tasks hang off epics #8 and #14). Seven stories (#10-#13, #15, #16, #18) have no child issues; Sprint 3 design tasks attach to epics or nothing.; 15 issues are absent from the proposal (#56-#58, #61, #63, #65-#71, #73, #47, #23); 16 epic/story cites sit in §4.; No Sprint milestone on #71, #68, #61, #57, #47; no assignee on #69, #68, #67, #61, #57, #56.; Open PRs #62 and #72 on develop; branch fill-section-4-proposal.md has three commits not in develop.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ❌ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ❌ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a 20-row issue-link table with one intro paragraph; no prose per work item.. |
| 3. Prototype works | ✅ done | Locator: TDOA direction and distance from simulated hydrophones, 20-scenario check, interactive demo, call saving; detector train and detect scripts. CI: develop run green; Prototype job installed and ran pytest on team tests. main's latest run is red at the harness gates (prototype job green). Tests: `tests/` tdoa, locate, save_call, speed_of_sound, scenarios (20 scenarios, 80% pass); ai-detector scripts untested. |
| 4. Word export (`develop`) | ⚠️ partial | 48 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Locator and detector can be demoed from the README commands and pytest, but §0, §3 and most of §4 are template text and main CI is red. |

**Proposal, what to write:** §0 Abstract is still the template prompt; write the background, problem, approach and expected result in one or two paragraphs.; §3 Proposed Approaches is the template prompt; state strategy, alternatives and reasoning for detector and locator.; §4 has two good summaries (Goal 2 spec and locator design) but no detector spec or design summary, no environment, no implementation section.; Diagrams: `docs/design/diagrams/ai-design.png` and the ER diagram are not in the proposal; add them with captions and explaining prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #62 (develop) — remerge main into develop; `db/init/` schema, seed and ER diagram are on main only; PR #72 (develop) — fills §4 of the proposal; develop to main — design docs and scenario work; main CI harness gates are failing.

**To do before your Sprint 3 review:**

1. Merge PRs #62 and #72 into develop so the database schema, seed and ER diagram are back and §4 text lands.
2. Write §0 Abstract and §3 Proposed Approaches over the template prompts, with strategy, alternatives and reasons.
3. Write §4 Environment and resources and a Prototype implementation section (detector, locator, database) with a reason per tool.
4. Summarize the Goal 1 detector spec and `docs/design/ai-detector-design.md` in §4 and add the diagrams with captions and prose.
5. Rewrite the Planned activities table as prose by goal; cite #56-#58, #63, #65-#71, #73 with typed refs.
6. Create child issues under stories #10-#13, #15, #16, #18; set a milestone on #71, #68, #61, #57 and an owner on #69, #68, #67, #61, #57, #56.
7. Rehearse the demo: `python -m locator.smoke`, `locator.scenarios`, `pytest tests`; fix the main CI gate failure before release.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant that tracks and targets weak spots

*Web app that generates questions from course material, tracks per-concept mastery and schedules practice on weak spots.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Merge develop into main, then rewrite `prototype/README.md` so the modules that already work can be run and shown.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 16 stories have child issues; only 26 issues exist in total. 13 stories have no child features or tasks: #16, #18, #19, #21, #22, #26, #28, #29, #30, #31 and others.; Six issues are not linked from the proposal: #43, #25, #6, #5, #4, #3.; Proposal §2 and §4 refs are bare links on develop (0 typed refs); main has only 17 typed refs and an empty §4.; #43 and #36 carry `sp:` under a story; #5 and #6 are stories with no `sp:`.; PR #40 has no issue; PRs #44, #46 and #34 close issues the proposal does not cite.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ❌ skeleton | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 3-row status table; the environment is a 6-row table with reasons but no prose.. |
| 3. Prototype works | ⚠️ partial | On develop: document processing, concept extraction, forgetting curve, question generator and selector modules; no web app or storage yet; mastery tracker is in open PR #39. CI: Develop 11-03 run green with Install and test (Python) executed; main's latest push run (10-20) failed in Run gates, while its prototype job passed. Tests: Develop has tests for document processor, concept extractor, forgetting, question generator, selector, plus scaffold `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 17 issue citation(s) become small in-text tags; 17 issue(s) fill 1 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | Proposal §3-§4 are placeholders and the working modules sit on develop with no runnable end-to-end flow or accurate README. |

**Proposal, what to write:** §4 has no specification per epic; write scope, functional and non-functional requirements and acceptance criteria for each of the three goals.; No design documents or diagrams: add system context, components, data model and data flow with captions and prose (diagram PR #46 is open).; §3 is 165 words; state the chosen strategy, alternatives considered and the reasoning.; §4 lacks implementation details of the prototype and planned-activity prose with issue refs.; Front matter still holds template placeholders (group, title, authors) and §5-§7 are template text..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch `develop` — five prototype modules with tests; not on main; PR #39 — per-concept mastery tracking and tests; PR #46 — §4 environment diagram; Branches `feature/question-generator`, `feature/question-selector` — 2 commits each not in develop.

**To do before your Sprint 3 review:**

1. Merge develop into main (and PRs #39, #46) so the working modules are on the integration branch and CI is green there.
2. Rewrite `prototype/README.md` with real setup, run and test steps and add a thin end-to-end path from document to questions.
3. File child issues under each of the 13 childless stories, assign one owner and a Sprint 3 or 4 milestone, and put `sp:` on stories only.
4. Write §4 specs per epic and design sections (context, components, data model, data flow, decisions) as prose with typed issue refs.
5. Link #3, #4, #5, #6, #25, #43 in the proposal; convert bare links to typed refs in §2 and §4.
6. Expand §3 with strategy, alternatives and reasoning; fill the front matter placeholders and remove `sp:` from #36 and #43.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (sponsor EL-1)

*Web app that extracts CoC and test-report PDF data into a structured, searchable material database.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Merge one working prototype slice (upload plus PDF extraction, with a test) so the Nov 17 review has running code instead of the login scaffold.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 16 stories have child issues (#12, #16, #24, #27, #48, #49); 63 issues in total. Stories #13-#15, #18-#21, #23, #25, #26 have no child issues; #12-#27 have no assignee or Sprint milestone.; Features #78, #85-#95 carry `sp: 3` under stories #12, #16, #24, #27, #48: double counting.; 13 issues are not linked from the proposal, including #84-#95 (Sprint 3 features) and #91.; Most §4 planned-activities rows use bare `#N` links instead of typed refs.; 2 early direct commits sit on main and develop; no recent PR lacks `Closes`.. |
| 2. Proposal §0–§4 (`main`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 spec/design index (7 rows) and the 30-row planned-activities table stand in for prose; spec and design documents are linked, not carried.. |
| 3. Prototype works | ❌ skeleton | Nothing from the project: `prototype/` holds the course `login.py`, its test and the placeholder README; no extraction, storage or UI. CI: main run 11-06 green; prototype job ran Install and test (Python), but the only test is the course `test_login.py`. Tests: Only `prototype/tests/test_login.py` (course scaffold). |
| 4. Word export (`main`) | ⚠️ partial | 90 issue citation(s) become small in-text tags; 55 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | Design documents exist, but the prototype is the course scaffold and §4 does not carry specs or explain diagrams. |

**Proposal, what to write:** §4 Specifications: the three `docs/specs/` files (Goals 1-3) are linked only; bring scope, requirements and acceptance criteria into the proposal.; §4 Diagrams: five figures have captions but no explaining paragraphs; write what each shows and the decision behind it.; §4 Environment lists PostgreSQL on Amazon RDS while `docs/design/system-architecture-diagram.md` shows Snowflake; §3 says undecided. Reconcile (#78).; §1 Introduction is about 260 words; no implementation section describes the prototype, which is still scaffold.; Planned activities should be prose per epic, including the Sprint 3 prototype-page features (#85-#95)..

**To do before your Sprint 3 review:**

1. Build and merge the first prototype slice from #86 and #93 (upload, then PDF extraction) with tests, so there is something to run on Nov 17.
2. Replace `prototype/README.md` and delete `login.py` and `test_login.py` once real code and tests are in.
3. Write §4 spec summaries for Goals 1-3 and a paragraph per diagram, then a design section (decisions, rejected alternatives, undesigned parts).
4. Resolve the Snowflake versus PostgreSQL/RDS conflict in §3, §4 and the architecture doc, and state the outcome (#78).
5. Remove `sp:` from #78 and #85-#95, and give stories #12-#27 an assignee and a Sprint milestone.
6. Link #84-#95 in §4 as typed refs and break stories #13-#15, #18-#21, #23, #25, #26 into child issues.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

*Localhost Flask/SQLite/Leaflet app that loads public crime records and supports radius search with filters and summaries.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Add the first Flask endpoint over the SQLite loader and fix `prototype/README.md`, so the Nov 17 demo is a running request rather than pytest output.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child tasks; 49 issues in total. Tasks #27, #29, #30, #31, #33 and #34 have no assignee.; #79 (specs task) is not in the proposal; #79 and #80 have no parent story.; Untyped leftovers #6, #7, #45-#47 and open #62 have no Sprint milestone.; 19 story refs sit in §4's Parent column; the chain check wants stories in §2 only.; PR #78 closes #79, which the proposal does not cite.. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 specification index (9 rows) and a 26-row planned-activities table carry most of the work; spec content is not in the proposal.. |
| 3. Prototype works | ⚠️ partial | Standalone modules: Costa Mesa normalizer, SQLite schema and loader, circular area filter, frequency counts; no Flask, map or integrated run. CI: develop run 11-09 green, both jobs; the Python install-and-test step ran, so root-level `test_*.py` files should be collected (job log not in the data). Tests: `test_normalize`, `test_load_db`, `test_area_filter`, `test_crime_frequency` on synthetic data; `tests/test_login.py` is scaffold. |
| 4. Word export (`develop`) | ⚠️ partial | 65 issue citation(s) become small in-text tags; 43 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The proposal is nearly complete on develop, but the demo is pytest output only; no running app and the README shows the login example. |

**Proposal, what to write:** §4 Specifications: only the Goal 3 spec is summarized (one paragraph); write scope, requirements and acceptance criteria for Goals 1 and 2.; §4 Diagrams: the data-flow diagram and radius-search sequence are only linked, and the text still says they are pending in PR #71, now merged.; §4 Design: add key decisions with rejected alternatives and what is not yet designed; §3 holds only the snapshot-versus-live choice.; §4 Implementation: one paragraph covers `area_filter.py` and `crime_frequency.py`; add the normalizer, loader and schema from PR #73.; Figure numbers skip Figure 4; planned activities are a table, not prose per epic..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch `develop` — wireframe, three specs, schema/loader/normalizer; main lacks PRs #73, #78, #81.

**To do before your Sprint 3 review:**

1. Merge develop into main so the reviewed proposal, specs and prototype modules are the same on both branches.
2. Add a Flask route plus a minimal page that returns radius-filtered incidents from SQLite, with a test, and demo it on Nov 17.
3. Rewrite `prototype/README.md` with run and test commands that work from a fresh clone; pin Flask in `requirements.txt`.
4. Write §4 spec prose for Goals 1 and 2, and add the data-flow and radius-search figures with captions and explaining paragraphs.
5. Add a key-decisions and not-yet-designed subsection to §4; delete the stale 'pending in PR #71' sentence.
6. Assign tasks #27, #29, #30, #31, #33 and #34; link #79 and #62 in §4 as typed refs.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*Web app that stores a vehicle's service history and recommends next services with urgent or convenient labels.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Merge develop into main, then build the recommendation engine (story #34), so the Nov 17 demo shows vehicle selection feeding a next-service result.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 1 of 10 stories has a child issue (#29 has #63); 40 issues in total. Stories #30-#38 have no child features or tasks; the build work is not broken down.; Tasks #49-#54 (specs, diagrams, prototype skeleton) have no parent story.; Open stories #31-#38 have assignees but no child tasks, so Sprint 3 PRs cannot trace to a task.; #59 is a task attached directly to epic #28 rather than to a story.; PR #20 (early draft) has no `Closes`.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 spec and design index (7 rows) and a 30-row planned-activities table; spec documents are linked, not carried.. |
| 3. Prototype works | ✅ done | Vehicle selection: Flask API, SQLite schema and seed, page to pick make/model/year/trim and save a vehicle for a seeded user. CI: develop run 11-03 green; Install and test ran for both Python and Node, so pytest and the jsdom page test executed. Tests: `test_vehicle_api.py`, `smoke_test.py`, `tests/ui/vehicle-select.test.js` (jsdom); course `test_login.py` still present. |
| 4. Word export (`develop`) | ⚠️ partial | 40 issue citation(s) become small in-text tags; 40 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | Develop can demo vehicle selection with tests and a full §4, but main shows the skeleton and the recommendation engine is not built. |

**Proposal, what to write:** §4 Specifications: the four `docs/specs/` files are indexed only; summarize scope, requirements, acceptance criteria and open questions per epic.; §4 Implementation: no section describes the Flask API, SQLite schema or page already built; write it with refs to #29, #30, #63.; §3 is about 190 words; add alternatives for the data store, import path and status labels with reasons.; §1.2 is 103 words plus a table; each problem needs a paragraph.; main still holds the Sprint 1 skeleton, so a review from main shows the older §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch `develop` — full §4, diagrams, specs, Flask/React prototype and tests; main has the Sprint 1 skeleton.

**To do before your Sprint 3 review:**

1. Merge develop into main so the reviewed branch carries the proposal and the prototype.
2. Build the recommendation-engine slice (story #34) with a test per acceptance criterion, and demo vehicle selection plus a next-service result on Nov 17.
3. Add §4 implementation prose and per-epic spec summaries (scope, requirements, acceptance criteria, open questions) with typed refs.
4. File child tasks under #30-#38 and parent #49-#54 to their stories.
5. Expand §3 with alternatives for data store, import and label rules, and write §1.2 as paragraphs.
6. Delete `prototype/login.py` and `tests/test_login.py` as the README says.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph model of USDT/USDC transfers with heuristic and ML wash-trading detection and an investigation dashboard.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Push `prototype/network.py` with its tests so the README run steps work; the Nov 17 demo needs the Goal 1 graph slice running.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 14 stories have child issues; 37 issues in total. No story (#25-#33, #38, #39, #53-#55) has child issues; tasks #46 and #50 hang from epics instead.; Nine issues are not linked from the proposal: #67, #64, #59, #56, #51, #46, #45, #42, #5.; #3 (meeting notes) is cited as `task:` but has no type; #56 has no Sprint milestone.; Stories #53-#55 have no assignee.; 14 direct commits sit on main and develop; PR #14 closes #12, which the proposal does not cite.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Tracked Task Issues is a bullet list of links and §4 Planned Activities is five one-line bullets; spec files are linked, not carried.. |
| 3. Prototype works | ❌ skeleton | Nothing from the project: `prototype/` holds `login.py`; its README describes `network.py` and 5 tests that are not on either branch. CI: develop run 11-10 green; Install and test (Python) ran, but only the course `test_login.py` exists. main's latest run (11-03) failed Repository harness gates. Tests: Only `prototype/tests/test_login.py` (course scaffold). |
| 4. Word export (`develop`) | ⚠️ partial | 30 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | The README promises a graph slice that is not in the repo, so nothing runs; §1.1, §1.2 and §4 are thin. |

**Proposal, what to write:** §1.1 Related Work is one sentence naming one vendor; write a comparative pros-and-cons table across several tools with citations matching §8.; §1.2 Problem Statements is one sentence; write each problem as a paragraph tied to Goals 1-3.; §4 Environment is bullets without reasons; explain why SonarX SQL, scikit-learn and each hardware choice were picked.; §2 still has placeholders `[N]`, `[M]`, `[K]` and `[metric]` in objectives 2.2, 2.4-2.6 and 3.1.; §4 Specifications: `Epic-23-spec.md` and `Epic-24-spec.md` are titled 'Account management'; fix them and summarize all three in the proposal..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch `develop` — Epic specs, five design diagrams, architecture doc; main lags and its CI failed.

**To do before your Sprint 3 review:**

1. Push `prototype/network.py` and its 5 tests to develop so the README run steps work, then demo the Goal 1 graph on Nov 17.
2. Write §1.1 as a comparative table plus prose with citations from §8, and §1.2 as a paragraph per problem.
3. Rewrite §4 environment with reasons for each tool, and add per-epic spec summaries and implementation prose for the graph slice.
4. Fix the 'Account management' titles in `docs/specs/Epic-23-spec.md` and `Epic-24-spec.md`; replace the `[N]`, `[M]`, `[K]` placeholders in §2.
5. File child issues under all 14 stories, assign #53-#55, and link #67, #64, #59, #56, #51, #46, #45, #42, #5 in §4.
6. Merge develop into main so CI is green there; open PRs for further changes instead of direct commits.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker (live runner tracking, posts, race-time prediction)

*React Native app streams runner GPS to Firebase for a spectator web page, plus race-time prediction.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Write §3 Proposed Approaches and the §4 environment reasoning in full prose, since both are still template prompts and the review is Thursday.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33). 31 of 48 issues are not linked from the proposal on main, including all Sprint 3 items #58-#74 and #59, #61, #62, #64.; PR #76 (closes #58) would add the citations but is still open and unmerged.; Parentless tasks: #72, #65, #60, #58, #48, #42; each should sit under a story or epic.; #1, #2 and #6 are untyped meeting issues; #1 and #6 have no assignee.; Direct commit cdf9bde (.github scaffold) on main and develop; Sprint 3 milestone has 18 open issues due 11/11.. |
| 2. Proposal §0–§4 (`main`, ≈ 6 pages) | ❌ skeleton | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ❌ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 specs index is a table mixing unfilled 〈…〉 template rows with real rows; §2 objectives are bullet lines with refs, not paragraphs.. |
| 3. Prototype works | ⚠️ partial | Expo app skeleton with a Firebase client and a Firestore smoke test script; README says no tracking feature is implemented yet. CI: main CI green on 11/10 (c6d92b9); Prototype job ran Node install and test, but `npm test` only syntax-checks `index.js` and reads the Expo config. Tests: none beyond `prototype/firestore-smoke-test.mjs` (needs live Firebase); `npm test` is a syntax check only |
| 4. Word export (`main`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 17 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | No GPS tracking, posting or prediction runs yet, and §3 and §4 are still template prompts; only a Firebase connection check exists. |

**Proposal, what to write:** §3 is still the template prompt with two 〈…〉 placeholders; write the strategy, alternatives considered and the reason for Firebase and Expo.; §4 opens with a template placeholder; the tech stack is a pipe-delimited list with no per-choice reasoning paragraphs.; §4 figures are named only; no caption or prose explains Figures 1-3. The specs in `docs/specs/` are listed, not summarized in §4.; No §4 implementation-details prose: the Firebase connection and smoke test (#61, PR #75) are not described.; §0 abstract describes ML analysis of routes, but §2 goals are live tracking, posts and prediction; align the abstract with the goals..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #76 — cites every work item in §4 (closes #58), still open; branch feature/58-cite-issues — 43 commits not in develop.

**To do before your Sprint 3 review:**

1. Merge PR #76, then link the remaining unlinked issues (#59-#74 and Sprint 1-2 tasks) as typed refs in §4 before Thursday's review.
2. Write §3 Proposed Approaches (strategy, alternatives, reasoning) and delete the template prompt and 〈…〉 text in §3 and §4.
3. Keep environment files out of git: commit only `prototype/.env.example` and confirm `.gitignore` covers `.env`.
4. Finish #59: record runner GPS to Firestore every 5 seconds, so the review can show a live position.
5. Finish #69: spectator view reads the runner position from Firestore; demo the two together on Thursday.
6. Add real tests for pace and GPS logic so `npm test` exercises team code (#64); document them in §4 implementation.
7. Caption and explain Figures 1-3 and summarize each `docs/specs/` file inside §4 with its epic and story refs.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Pipeline that detects signal bursts, classifies waveforms and modulations, and explains decisions with attribution heatmaps.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Merge develop into main today, then write the §4 specs and design from the existing `docs/` guides so the proposal matches the working prototype.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of about 19 stories have child issues (#66, #68, #135). Most stories (#67, #83, #84, #62, #64, #65, #114-#116) have no child feature, task or sub-task issues.; sp: carried below a story: #123 and #98 under #66, #88 under #68; points belong on the story only.; No assignee or Sprint milestone: #63, #70, #71 (stories), #126 (no milestone), #108 (no milestone), #103 untyped.; #135, #95, #103 and Sprint 1 setup tasks (#27-#32, #36) are not linked from the proposal on develop.; PRs #1 and #2 on main lack an issue; direct commit 0ae479e on main.. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §2 objectives and §4 planned activities are bullet lists of issue refs with no prose; 24 task bullets stand in for the activities narrative.. |
| 3. Prototype works | ✅ done | IQ capture to peak picking (baseline v1.4 and CV model), channelizer, calibrated classifier, Captum attribution, XAI CLI and a GUI under `prototype/GUI`. CI: develop CI green 11/9 (d7e90ac); Prototype job ran Install and test (Python) on the team code. main CI is from 10/16 and main still has the login scaffold. Tests: Ten files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, classifier, pipeline gate, stand-in training; none for the GUI |
| 4. Word export (`develop`) | ✅ done | 46 issue citation(s) become small in-text tags; 46 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The prototype demo from develop is strong with a sample-file command, but §4 has no specs, design or diagrams and main still shows the scaffold. |

**Proposal, what to write:** §4 has one short environment paragraph naming MATLAB and Python with no reasons per tool, and no mention of Captum, HDF5 or the GUI toolkit.; No per-epic specification in §4 (scope, requirements, acceptance criteria, open questions) for Goals 1-5; `docs/specs/` still holds only the example.; No design document or diagram in §4: write context, components, data model and data flow for the peak picker, classifier and XAI path.; The method guides in `docs/` (`captum-attribution.md`, `confidence-calibration.md`, `channelization.md`) are not summarized or linked from §4.; §1.2 gives three one-sentence problems; §2 objectives are bullets with no paragraph explaining each goal..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop — whole prototype, §3.1 and §2 updates; main is stale since 10/16; branch Application-Structure — 5 commits not in develop; branch docs/team-documentation — 1 commit not in develop.

**To do before your Sprint 3 review:**

1. Merge develop into main before Thursday's review so the default branch carries the prototype and the proposal.
2. Write §4 environment with a reason for each tool: MATLAB, Python, Captum, HDF5, the GUI toolkit, mentor data and where it is stored.
3. Write one spec per epic in `docs/specs/` and summarize each in §4: scope, requirements, acceptance criteria, open questions, refs to #57-#61.
4. Write a design document with architecture, data flow and decisions; add captioned diagrams to §4 with explaining paragraphs.
5. Decompose stories #67, #62, #64, #65, #114-#116 into child issues; remove sp: from #123, #98, #88; assign #63, #70, #71 and set milestones.
6. Add §4 implementation-details prose for the peak picker, channelizer, calibration and XAI CLI, citing the closed issues and PRs.
7. Rehearse the sample command `python scripts/analyze_iq.py data/sample/peak_picker_smoke.iq --sample-rate 1000000` and one GUI run for the demo.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · G13 BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Offline Windows desktop app (Python core, Electron UI) that suggests deadlines, tracks progress and sends reminders.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Fix the prototype README and rename the test file so CI exercises team code, then merge develop to main and demo the running Electron UI on Thursday.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#53-#106). 30 of 96 issues are not linked from the proposal on develop: diagram tasks #122-#130, #131, #119, #120, #116, #113.; Sprint 3.x subtree has no Sprint milestone: stories #25-#27, features #89-#102 and tasks #97-#106, #92-#94.; No assignee: epics #16-#18, #119 and #120 (Sprint reports), plus closed #30, #32, #33.; PRs #4, #9, #36, #117 closed without an issue; Sprint 3 milestone holds 54 open issues, 0 closed.; Two unmerged branches carry work: feature/34-project-proposal (28 commits) and feature/47-sprint-reports (18).. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned Activities is a 38-row issue table with no prose; §1.1 is a four-row comparison table with no argument paragraphs after it.. |
| 3. Prototype works | ⚠️ partial | Python core (Models, Database, Assignment and Deadline services) plus an Electron/Vite UI with form, list and progress components, none shown running. CI: develop CI green but from 10/31 (522b783); main last ran 10/16 and failed Run gates. Prototype job ran only the Python step, which cannot collect `TestAssignments.py`. Tests: One file, `prototype/A.M.I.Y.A.core/tests/TestAssignments.py`; name misses pytest discovery; nothing tests the UI |
| 4. Word export (`develop`) | ⚠️ partial | 84 issue citation(s) become small in-text tags; 66 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | Goals, specs and wireframes are written, but §4 lacks architecture, the README is scaffold, and a demo depends on code CI has not exercised. |

**Proposal, what to write:** §4 has no system context, components, data model, data flow or decisions-with-rejected-alternatives; issues #122-#131 are only open tasks.; §4 Diagrams holds six wireframes only; add architecture, context, ER and sequence diagrams, each with a caption and explaining paragraph.; The three specs in `docs/specs/specs-G1.md` to `specs-G3.md` are summarized in one sentence each; carry scope, requirements, acceptance criteria and open questions into §4.; §4 Environment names Python and JavaScript but not Electron, Vite, SQLite or Windows notification APIs, nor why each was chosen.; No §4 implementation-details section for the Python core and React components that exist on develop..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop — wireframes, specs, prototype code; main last updated 10/16; branch feature/34-project-proposal — 28 commits not in develop; branch feature/47-sprint-reports — 18 commits not in develop.

**To do before your Sprint 3 review:**

1. Replace the scaffold `prototype/README.md` with real install, run and test steps, then verify them from a fresh clone before Thursday's review.
2. Rename `TestAssignments.py` to `test_assignments.py`, add tests for deadline suggestion and progress logic, and make the CI Python step collect them.
3. Draw the architecture, context, ER and sequence diagrams (#122-#131) and add each to §4 with a caption and a paragraph.
4. Write a §4 design narrative: components, data model, IPC data flow, and decisions with rejected alternatives such as cloud storage.
5. Fold the key requirements and acceptance criteria from `docs/specs/specs-G1.md` through `specs-G3.md` into §4, one block per epic.
6. Set Sprint milestones and assignees on #25-#27, #89-#106, #119 and #120; link #113-#131 in §4; merge develop into main.
7. Expand §1.1 with paragraphs arguing the difference after the table, and add reasons per tool to the §4 environment.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox incident-response training simulator

*Sandboxed desktop simulator for investigating fake malware incidents, with LLM-generated, schema-validated scenarios.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Get one runnable PySide6 window with a passing test merged to develop and main before Thursday, so the review has something to demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ❌ not started | 0 of 18 stories have child issues; tasks #53-#94 hang off epics #22 and #23. No story #24-#41 has a feature, task or sub-task child; the Sprint 3 tasks #79-#94 sit under epics.; 16 of 53 issues are not linked from the proposal: #79-#94, #88, #13, #6, #4.; Epics and stories (#22, #24-#41) are cited in §4 tables, where only §2 should carry them.; Stories #24-#41 and tasks #44-#47, #88 have no Sprint milestone; #88, #84, #82, #92 have no assignee.; 9 direct commits on main and 10 on develop; PR #50 lacks an issue, and #91 and #92 are untyped.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 specs and design index and the planned-activities list are tables of issue refs; §2 objectives are 20 bullet lines; §1.1 is a table with one paragraph.. |
| 3. Prototype works | ❌ skeleton | Nothing runs: develop has a Dockerfile containing a TODO and a README; login.py was deleted, and main still holds the scaffold login. CI: develop CI green 10/31 (af3eb7e); Python step ran but no tests exist, so it exercised nothing. main CI green 10/29 on the course `login.py` scaffold. Tests: none on develop; only course `test_login.py` on main |
| 4. Word export (`develop`) | ✅ done | 111 issue citation(s) become small in-text tags; 54 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | No runnable prototype: README names `start_simulation.py`, which does not exist, and the Dockerfile is a TODO; §4 lacks implementation prose. |

**Proposal, what to write:** §4 carries no implementation-details section; nothing says what the prototype does, because the prototype is not built yet.; §4 Diagrams embeds three figures with captions; Figures 2, 4 and 5 (context, ER, sequence) are one-line list items, not embedded or explained.; Spec content stays in `docs/specs/*.md`; §4 gives one summary paragraph each, without requirements, acceptance criteria or open questions.; No design narrative in §4: write components, data model, decisions with rejected alternatives and what is not designed yet.; §1 Introduction is 130 words; §1.1 is a table plus one paragraph; add prose arguing how this differs from existing training simulators..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop — design docs, Dockerfile TODO, README; main still carries the login scaffold; branch copilot/create-requirements-list-for-goal-2-47 — 1 commit not in develop.

**To do before your Sprint 3 review:**

1. Build a runnable slice before Thursday: a PySide6 start menu that loads one in-memory scenario, and `prototype/start_simulation.py` the README can run.
2. Add pytest tests for Pydantic scenario validation and host isolation (#30, #36); make the CI Python step collect them.
3. Create child issues under stories #24-#41 (feature, task, sub-task), assign owners and Sprint milestones, and reparent #79-#94.
4. Remove epic and story refs from §4 tables, link #79-#94 as typed refs in §4 prose, and stop direct commits to main.
5. Embed Figures 2, 4 and 5 in §4 with captions and one paragraph each; explain how the diagrams fit together.
6. Write a §4 implementation-details section describing the prototype once it runs, with the Dockerfile either implemented (#79) or removed.
7. Summarize spec requirements and acceptance criteria from `docs/specs/training-environment.md` and `ai-scenarios.md` inside §4.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo for constrained hardware

*Lightweight OpenGL 3.3 C++ game engine with ECS architecture, scene editor, and a demo game.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Add a CMake build and test step to CI, then fix the README so the engine's build and run steps are proven before Thursday's demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 8 stories have child issues (#32 via #9, #33 via #67). 23 of 35 issues are not linked from the proposal on develop, including #63, #66, #67, #9, #46 and the §4 tasks #47-#49.; Child tasks #63 and #66 hang off epic #24, not a story; stories #26-#31 have no children.; No typed refs on develop: refs are written `[epic:https://…]` instead of `[story:#N]` form.; #46 carries sp: while it is a task; #44 has no assignee; #57, #43 and #16 have no Sprint milestone.; Nine untyped issues (#43, #44, #47-#50, #54, #61, #64); 4 direct commits on main; PRs #3, #4, #5, #41 lack an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §1.2 is a two-row table with no prose; §2 objectives are bullet lines; the §4 specs index and work-item table hold only 〈…〉 template rows.. |
| 3. Prototype works | ⚠️ partial | CMake C++26 project fetching SDL3 and assimp with vendored glad and glm, GLSL shaders; `src/` is not visible in the sweep (120 of 439 files listed). CI: develop CI green 11/9 (b9e3776) but the prototype job skipped Node and Python install and test; it never built the C++ code. Tests: none; README test section is still the course `test_login.py` text |
| 4. Word export (`develop`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 11 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | README gives dependency, build and run commands and the engine skeleton exists, but §4 is mostly template and CI has never built or tested it. |

**Proposal, what to write:** §4 specs index still lists `docs/specs/game-engine.md` and `game-demo.md` as 〈…〉 placeholders; summarize each epic's scope, requirements and acceptance criteria in §4.; §4 planned activities is one template row; list every work item in prose with typed refs, including #63, #66, #67 and #9.; No design writing in §4: `docs/design/architecture.md` and the system context are not carried; add components, data model, data flow and decisions.; §4 template guidance and 〈…〉 diagram prompts are still present; the system-context figure is missing and Figure 1 has no explaining prose.; §4 environment lists tools with one-line reasons; add why SDL3, assimp and C++26 over alternatives, and hosting or hardware targets..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop — full proposal §0-§4 progress, prototype, specs; main still the template; branch 33-objective-24-implement-visual-editor… — 3 commits not in develop.

**To do before your Sprint 3 review:**

1. Merge develop into main so the default branch carries the proposal and prototype before Thursday's review.
2. Replace the 〈…〉 rows in the §4 specs index and write a summary of `docs/specs/game-engine.md` and `game-demo.md` with typed refs.
3. Add a CI C++ build and ctest step so the prototype job builds the engine, and add a test per acceptance criterion for the ECS core.
4. Rewrite `prototype/README.md` test and status sections for the real engine; check the setup, build and run steps on a fresh clone.
5. Write §4 design from `docs/design/architecture.md` and the system context: components, data flow and decisions; delete the template diagram prompts.
6. Reparent #63, #66 under their stories, file children for stories #26-#31, and link every issue in §4 with typed refs.
7. Expand §1.2 and §2 into prose paragraphs ending in refs, and decide what you will demo on Thursday (window, renderer, ECS entities).

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Monitors cross-chain bridge vaults, learns normal outflow, and alerts on drains with measured false alarms.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Move the three goal specs' scope, requirements and acceptance criteria into proposal §4 as prose, since specs are the largest missing §4 block before Nov 19.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#14, #15, #17, #18, #20); #5, #16, #19, #21 have none. #97 and #98 (Sprint 3 tasks under #17 and #18) have no assignee and are not linked from the proposal.; PR #44 closes #42, which the proposal does not cite.; About 20 tasks (#90-#95, #72, #67 and others) have no parent story; they carry their own sp:.; PRs #75 and #35 have no `Closes #N`; three direct commits on main (`docs:` team details).; #19 and #21 (Sprint 4 stories) and #5, #16 have no child tasks on the board.. |
| 2. Proposal §0–§4 (`develop`, ≈ 14 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: Table 9 lists the three specs and the design doc as file paths with issue refs only; the D1-D6 diagram list links out to `docs/design/architecture.md`.. |
| 3. Prototype works | ✅ done | Detector, SQLite store, live Ethereum poller, replay of five past hacks, false-alarm evaluation, Slack notifier, FastAPI API, web dashboard, demo mode, Dockerfile. CI: develop 927e722 (Nov 9) green; Prototype job ran 'Install and test (Python)', so team tests executed. main run Nov 3 also green. Tests: Four files in `prototype/tests/`: detector, live loop, baseline check, data pipeline, including the mark-as-seen API test. |
| 4. Word export (`develop`) | ✅ done | 46 issue citation(s) become small in-text tags; 41 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The prototype runs in live, demo and replay modes and could be shown; proposal §4 still lacks spec, design and implementation prose. |

**Proposal, what to write:** §4 specs: `docs/specs/goal-1-baseline.md`, `goal-2-detection.md`, `goal-3-dashboard.md` are only listed in Table 9; summarize scope, FR/NFR, acceptance criteria, open questions per epic.; §4 design: carry the six design elements from `docs/design/architecture.md` (context, components, data model, flow, decisions with rejected alternatives, undesigned parts) into the proposal in prose.; §4 diagrams D1-D6 get one-line captions but no explaining prose in proposal.md; Figures 1 and 2 are the planned design, not the built one.; §4 has no implementation-details section: describe detector, store, live poller, notifier, API and dashboard as built, with refs to merged tasks.; §4 planned activities for Sprints 3-4 (#90-#98) are one paragraph; add the replay and false-alarm work under Objectives 2.2 and 2.3..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: D1-D6 diagram list, Sprint 3 tasks and later prototype work are not on main.

**To do before your Sprint 3 review:**

1. Summarize each epic's spec in §4 (scope, requirements, acceptance criteria, open questions) from the three `docs/specs/` files before the Nov 19 review.
2. Write the design subsection in §4 from `docs/design/architecture.md` with prose for D1-D6 and the rejected alternatives.
3. Add an Implementation details subsection to §4 describing each `prototype/bridgewatch/` module as built, citing merged tasks.
4. Assign #97 and #98, add them to §4, then finish the replay and false-alarm results for Objectives 2.2 and 2.3.
5. Add child tasks under stories #14, #17, #18, #20 and parent the standalone doc tasks.
6. Release develop to main and rehearse the live, demo and replay modes for the Nov 19 demo.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Get one runnable end-to-end slice into `prototype/src/sonicscape/` with tests, because nothing runs today and the review on Nov 19 needs a live demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 6 stories have child issues (#25, #29, #30); #26, #27, #28 have none; #46, #47, #53 hang under epic #21. `sp: 2` on tasks #41, #42, #43, #49, #55 under stories (double counting); #51 under pointed task #47.; #41, #49, #51, #55 are not linked from the proposal; PRs #40, #50, #52, #56 close them.; #49 and #55 have no assignee; Sprint 3 milestone has no issues at all.; Sixteen merged PRs (#5-#45 range) have no `Closes #N`; main has 30 direct commits.; Tasks #46, #47, #53 are parented to epic #21, not to stories #25/#26.. |
| 2. Proposal §0–§4 (`main`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1, §1.2, the §4 environment table, the spec/design document table and 'Planned activities' (5 rows) are tables; no prose carries the issue refs.. |
| 3. Prototype works | ❌ skeleton | Empty module skeleton: `backend/lastfm.py`, `database/db.py`, `schema.sql`, `main.py`; README says there is no current code to run. CI: main 12278fb (Nov 6): run failed on Repository harness 'Run gates'; Prototype job green but no team tests exist. develop run green (Nov 2). Tests: none; no `prototype/tests/` folder, although the README claims four tests |
| 4. Word export (`main`) | ✅ done | 14 issue citation(s) become small in-text tags; 14 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | There is no running prototype to demo, main CI is red on the harness gate, and §4 has no specs, design or implementation prose. |

**Proposal, what to write:** §1.1 is a four-row table with no prose; add paragraphs arguing what SonicScape does differently, with citations matching §8.; §1.2 is a three-row table and §2 has no prose; write the problem statements and explain each epic and story in full paragraphs ending in refs.; §4 specs: `docs/specs/specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` are only listed; summarize scope, requirements, acceptance criteria, open questions per epic.; §4 diagrams are bare Mermaid blocks or images with no explaining prose; the system-context and architecture figures lack numbers and real captions; write a paragraph for each.; §4 has no implementation details and 'Planned activities' lists only five Sprint 2 rows; describe the first end-to-end slice and Sprint 3-4 work..

**To do before your Sprint 3 review:**

1. Build the first runnable slice in `prototype/src/sonicscape/` before Nov 19: load Last.fm data, show the galaxy, record a swipe in SQLite.
2. Add `prototype/tests/` with a test per acceptance criterion and make the README run and test steps work from a fresh clone.
3. Fix the Repository harness 'Run gates' failure on main so CI is fully green.
4. File Sprint 3 child issues under stories #26, #27, #28 (Sprint 3 milestone, one assignee each, no `sp:`) and link them in §4.
5. Write §1.1 and §1.2 as prose, and give §2 explanatory paragraphs with refs.
6. Summarize the three specs and the design documents in §4, add captions and prose to every diagram, and add an Implementation details subsection.
7. Remove `sp:` from tasks #41, #42, #43, #49, #55 and assign #49 and #55.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: Project Rogue, 2D action roguelite with flexible builds (Unity)

*A Unity 2D action roguelite where builds develop through weapons, attributes and branching three-Act runs.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Reconcile main and develop so one branch holds the movement and boon/effects code, then add Unity tests and a CI step; the review needs one playable build.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32, #35, #41); #33, #34, #36-#40 have none. Eight issues are not linked from the proposal: #53, #56, #58, #61, #64, #65, #72, #74; PRs #66, #68-#71 close them.; `sp: 2` on #64 under story #35; old tasks #15, #18, #20, #5 are pointed tasks under pointed tasks.; #74 and #58 have no Sprint milestone; #26 and #13 are untyped with no assignee or milestone.; Spec tasks #53, #56, #61, #65 hang under epics #29-#31 instead of stories.; Six refs sit in the wrong §4 spot; branch `feature/33-attributes-resources-respec` has 2 unmerged commits.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ⚠️ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Planned activities' is a long table of issue links; the spec and design table lists documents with status only. Main still has template placeholders.. |
| 3. Prototype works | ⚠️ partial | Unity 6 project: combat scene (resolver, abilities, loadouts, target dummy) and traversal room with class movement; main has boons/effects, develop has movement, not both. CI: develop f4f6a49 (Nov 5) green, but the Prototype job only ran the Python step; Unity code was not compiled or tested. Tests: none automated; `Editor/ProgressionVerification.cs` and the `Test_Combat` scene serve as manual checks |
| 4. Word export (`develop`) | ✅ done | 54 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The Unity combat and traversal demos can be shown from develop; proposal §4 lacks spec, design and implementation prose and CI does not run the game. |

**Proposal, what to write:** §1.2 still contains the template instruction paragraph; delete it and write the three problems as full paragraphs with refs.; §4 specs: `docs/specs/goal-2-action-gameplay-spec.md`, `replayable-run-structure.md` and the Goal 1 folder are not in the §4 table; summarize scope, requirements, acceptance criteria, open questions per epic.; §4 design is two overview figures; add data model (save file, progression), data flow, key decisions with rejected alternatives, and what is not designed yet.; `combat-class-diagram.svg` and `run-room-reward-flowchart.svg` exist but are not embedded in §4 with captions and prose.; §4 has no implementation-details subsection for the combat resolver, movement, traversal room and loadout panel; §3 still says class-based wording needs alignment..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: §3-§4 text, diagrams, traversal and movement work are not on main; branch feature/33-attributes-resources-respec: 2 commits not in develop; branch austin2578-patch-1: 1 commit not in develop.

**To do before your Sprint 3 review:**

1. Merge develop into main, then bring main's boon/effects code and develop's movement code onto one branch so a single build shows both.
2. Add Unity EditMode tests (or a CI build step) covering each acceptance criterion of #36, #37 and #32, and tell the README how to run them.
3. Summarize the Goal 1, Goal 2 and Goal 3 specs in §4 and list all three in the document table.
4. Embed the combat class and run/room/reward diagrams in §4 with captions and prose, and add an Implementation details subsection.
5. Delete the template paragraph in §1.2 and replace the §4 activities table with prose that ends in typed refs, including #53, #56, #58, #61, #64, #65, #72, #74.
6. File child tasks under stories #33, #34, #36-#40 with one assignee and a Sprint 3 milestone, and remove `sp:` from #64.
7. Rehearse the combat and traversal demo from a fresh clone before Nov 19.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi drone detection (RTX-AST)

*Detect small drones and estimate position and movement from Wi-Fi CSI, compared against conventional radar.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Write the §4 environment and resources section to replace the template prompt, then merge the pending section-4 branch.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 12 stories have child issues (#8 has 3; #56, #69, #73 have 1); 8 have none. Stories #6, #7, #13-#17, #67 have no children; Sprint 3 and 4 stories not broken down.; sp: on children #71, #53, #47, #45, #39 under stories (double counting).; #38, #43 untyped; #51, #53, #65, #71, #75 and others not linked from §4.; 3 open issues have no Sprint milestone; 15 tasks have no parent story.. |
| 2. Proposal §0–§4 (`main`, ≈ 5 pages) | ❌ skeleton | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 10-row link table; spec/design section is an index table with template placeholders.. |
| 3. Prototype works | ⚠️ partial | Capture and quality-check stubs (capture.py, quality_check.py) with a sample recording; README keeps scaffold text and a placeholder row. CI: main and develop 11-06 green; Python install-and-test ran, but the only test is course test_login, so team code is untested. Tests: Only course tests/test_login.py; no test for capture or quality check. |
| 4. Word export (`main`) | ⚠️ partial | 30 issue citation(s) become small in-text tags; 29 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | §4 is largely template and the prototype is stubs with no tests; a CSI capture could be shown but not a detection slice. |

**Proposal, what to write:** §4 opening is still the template prompt plus a placeholder; write environment: CSI hardware, receiver, OS, language, ML libraries and why.; Only one design (CSI data flow) is in §4; add architecture, system context and capture-to-detection diagrams with prose.; Specs for CSI sensing, drone detection and evaluation exist in docs/specs but are only indexed; summarize each in §4.; §1 is 148 words and §3 about 200; expand with background and rejected alternatives.; No implementation or planned-activities prose; §4 has 6 placeholders..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch feature/#51-section4-update - drone detection and evaluation spec additions to §4, not in develop.

**To do before your Sprint 3 review:**

1. Replace the template text in §4 with a real environment/resources section (hardware, OS, language, ML tools, reasons).
2. Merge feature/#51-section4-update and summarize the three specs and every design doc in §4.
3. Add architecture, system context and capture-to-detection diagrams with captions and prose to §4.
4. Write real capture and quality-check code with tests for each acceptance criterion; remove login.py and update README.
5. Remove sp: from #39, #45, #47, #53, #71; create child issues under open stories #6-#7, #13-#17.
6. Link #51, #53, #65, #71, #75 in §4 and write the planned activities as prose.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia, first-person horror maze game in Unreal Engine

*Unreal Engine 5 first-person horror maze game with adaptive monsters, encounter director and responsive atmosphere.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Write the §4 design document with embedded diagrams, since the monster state-machine and context diagrams already exist on main.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 8 stories have child tasks (#14, #15, #23 have none). 11 tasks under stories (#39, #40, #43-#52) carry sp:; points belong on the story only.; Goals #12, #17, #21 are epics but cited as [story:#N] in §2.; 12 issues not in §4 (#24-#28, #33-#35, #37, #54, #55, #57); tasks #39-#52 linked as bare refs.; #33 has no assignee or milestone; #12, #17, #21 have 2-3 assignees.; PR #5 has no Closes; 1 early direct commit; design diagrams (#54) never reached proposal.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned-activities is a 16-row link table with one paragraph; spec index mixes template rows with real ones.. |
| 3. Prototype works | ⚠️ partial | Unreal Engine 5 first-person starter project (Config, Content, Insomnia.uproject); only starter-level movement, manual smoke test. CI: main and develop green but prototype job ran only 'Nothing to build'; Unreal project not exercised by CI. Tests: None; README records a manual smoke test only. |
| 4. Word export (`develop`) | ⚠️ partial | 25 issue citation(s) become small in-text tags; 25 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Starter level runs per README, but no team gameplay yet; §4 design and diagrams are not in the proposal. |

**Proposal, what to write:** §1.1 Related Work lacks a pros-and-cons table; add one across Visage, MADiSON, Phasmophobia and tie citations to §8.; §4 spec index keeps two 〈…〉 template rows; three specs exist in `docs/specs/` but are not summarized in prose.; No design documents: `docs/design/` holds only scaffold, plus `.mmd` diagram sources on main only, none in the proposal.; Develop §3 is real prose but main still has the template §3; merge so the best branch is main.; §4 lacks prose on what the prototype implements and on remaining work; write per-goal planned activities..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: main §3 is template and trails develop; PR #62 diagrams are on main only; bring `docs/design/*.mmd` to develop and into the proposal.

**To do before your Sprint 3 review:**

1. Remove sp: from tasks #39, #40, #43-#52; keep points on stories #13-#23.
2. Fix §2 refs: #12, #17, #21 as [epic:#N]; link tasks in §4 with typed refs and add #24-#37, #54-#57.
3. Write §4 design: context, components (monster AI, director, audio), state model, decisions with rejected alternatives; embed diagrams with captions.
4. Add a pros-and-cons related-work table and tie references to §8.
5. Build the first playable slice (maze, patrol monster) with a test per acceptance criterion in each spec.
6. Create child tasks under stories #14, #15, #23; give #33 an owner and Sprint.
7. Delete 〈…〉 rows in §4 and merge develop to main.

[↑ Back to all groups](#groups)

## About this page

The Sprint 2 checklist (specs, design, environment, prototype wiring) is now folded into rule 2 (§4) and rule 3. The earlier editions, including the Sprint 2 cards, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
