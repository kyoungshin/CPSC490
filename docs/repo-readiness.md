# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.

**CPSC 490 · Fall 2026 · swept 2026-11-09 01:40 UTC.** Earlier editions are kept in this file's git history.

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
| [G01](#g01) BGAF | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 74 |
| [G02](#g02) Linux Larpers | Tue Nov 10 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 15 |
| [G03](#g03) G03 California | Tue Nov 10 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 32 |
| [G05](#g05) Fighting Mongooses | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 4 |
| [G06](#g06) GapWise | Tue Nov 17 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G07](#g07) Mighty Morphins | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 8 |
| [G08](#g08) G08 Crime Busters | Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 7 |
| [G09](#g09) Sigma Squad | Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 10 |
| [G10](#g10) Team Jiddak | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 5 |
| [G11](#g11) 5 Guys | Thu Nov 12 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ | ≈ 6 |
| [G12](#g12) ACJMM | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 7 |
| [G13](#g13) G13 BYKX | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 7 |
| [G14](#g14) Cyber Squad | Thu Nov 12 | ❌ | ⚠️ | ❌ | ✅ | ❌ | ≈ 6 |
| [G15](#g15) HIBBI-01 | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) BridgeWatch | Thu Nov 19 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 13 |
| [G17](#g17) SonicScape | Thu Nov 19 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | ≈ 5 |
| [G18](#g18) G18 ProStrats | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) Titan Security | Thu Nov 19 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G20](#g20) Solos | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |

- **Rule 1 met:** 0 of 20 (none).
- **Proposal §0–§4 complete:** 0 of 20 (none).
- **Prototype working, with a real slice and tests:** 6 of 20 (G01, G04, G05, G09, G12, G16).
- **Ready to demo both today:** 0 of 20 (none).

**What changed since the Nov 5 edition:**

- **This page now checks Sprint 3 readiness** against the three rules of thumb, plus the Word export. The Sprint 2 checklist (specs, design, environment, wiring) is folded into rule 2 (§4) and rule 3.
- **Prototypes moved the most:** G04 (tested FIFO and PNL code), G09 (Flask, SQLite and React slice on `develop`), G12 (signal pipeline with 9 test files) and G16 (detector, replay and dashboard) now have working, tested prototypes.
- **Most of the finished work sits on `develop` only** (G02, G04, G05, G06, G09, G12, G13, G15, G18, G20). That's fine, but `main` is what the Word export and your final submission come from, so merge before your review.
- **Rule 1 is the class-wide gap.** Most stories have no sub-issues yet, many Sprint 3 issues aren't cited in §4, and several groups put `sp:` on tasks under a story, which counts the same work twice.
- **Course fix (instructor's, Nov 8):** the readiness sweep was asking sub-tasks under a pointed writing task for their own `sp:`. That was wrong: points go on the story, or on the standalone task, once. Those false flags are gone.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and strategy backtesting

*Pipeline that cleans SonarX Hyperliquid data, rebuilds order books, validates them, and gates backtests of trading strategies.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge PR #269, then write the replay and validation designs (#260-#262) into §4; these are the largest remaining §4 gaps.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 13 of 14 stories have child issues (#58, a dropped objective, has none). Nine tasks carry `sp:` under a story (double counting): #195, #187, #184, #183, #181, #175, #174, #173, #172.; 93 epic/story citations sit in §4 instead of §2 only; #278 is open to move them.; About 14 Sprint 4 features and tasks (#144-#169, #147, #94) have no assignee; #202 and #187 have 2-3 assignees.; About 33 tasks have no parent story (#271, #264, #249, #232, #231, #206 ...), so the story-to-task chain is broken for them.; PR #126 and merge PRs from develop have no `Closes #N`; three direct commits on main; #151 is cited as a task but is a sub-task.. |
| 2. Proposal §0–§4 (`main`, ≈ 74 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: Spec/design index has a 14-row issue link table beside the prose; §2 goals and objectives are bullet lines with typed refs; planned activities are prose.. |
| 3. Prototype works | ✅ done | DuckDB schema from `docs/design/database.md` and a SonarX L2 snapshot loader; five other pipeline modules are docstring stubs; Vite React skeleton. CI: Main 11-08 push run green; Prototype job ran Install and test (Python), so team tests ran. Node job skipped, so the front end is not built by CI. Tests: `prototype/tests/test_package.py` (layout, imports) and `test_storage.py` (schema, load, exact decimals, repeat load). |
| 4. Word export (`main`) | ✅ done | 589 issue citation(s) become small in-text tags; 164 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Proposal §0-§4 is largely demoable, but the prototype shows only the storage loader; cleaning, replay and validation are not running. |

**Proposal, what to write:** §4 design is missing the replay engine and validation/gate designs (#260-#262 open); write them with diagrams and summarize in §4.; Front-end screen flow, component and state design is only in open PR #269; merge it so §4 carries it.; §1.2 Problem Statements is 223 words plus a 4-row table; expand into prose arguing each problem.; `develop` is stale (proposal §4 has 17 links); main is the real integration branch, so say so in the README (#274).; Main proposal is about 269k characters, well above the page target; length is not the gap..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #269 — front-end screen flow, component and state summaries for §4; Branch `develop` — stale, far behind main; retire or sync.

**To do before your Sprint 3 review:**

1. Merge PR #269, then write the replay engine and validation/gate designs into proposal §4 (#260-#262) with captioned diagrams.
2. Implement the cleaning step and replay step in `prototype/src/bgaf_pipeline/` with one test per acceptance criterion of Objectives 1.1 and 1.2.
3. Add a Node job path so CI installs, lints and builds `prototype/frontend`; today the Node steps are skipped.
4. Remove `sp:` from the nine tasks under stories and assign every Sprint 4 feature and task a single assignee.
5. Give each of the 33 parentless tasks a story parent; finish #278 so §4 cites no epics or stories.
6. Expand §1.2 into prose and add `Closes #N` to every PR, including merges from develop.
7. Run the README steps on a fresh clone (#272) and rehearse the Dec 1 demo (#276).

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

*ESP32 nodes passively capture Wi-Fi/Bluetooth metadata; FastAPI and PostgreSQL store it for device identification on a dashboard.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Write the Goal 1 spec (Epic #47) in `docs/specs/` and add its summary to §4, since the Sprint 3 slice implements Goal 1.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); Goal 2 stories #51-#55 and most of Goal 3 have none. Stories #49, #51-#55, #58-#61 have no child feature/task issues; Tasks #91, #92, #94, #95 carry sp: under stories #16, #45, #57 (double counting); #17, #18, #92 and #109 have no assignee; #99 and #20 are not linked from proposal.md; #6, #70, #72, #79, #80, #101 are untyped refs; develop has 8 direct commits for the proposal; PRs #120 and #121 are open. |
| 2. Proposal §0–§4 (`develop`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §2 is bullets only (18 lines, no prose). The §4 spec/design table lists two docs; main's §3 and §4 are still template skeletons with placeholders.. |
| 3. Prototype works | ⚠️ partial | FastAPI backend with /health and /health/db against PostgreSQL in Docker Compose; no ESP32 firmware, observation model or API yet. CI: develop CI green (11/8 PST), 'Install and test (Python)' ran; main green. Only `test_main.py` exercises team code, so coverage is thin. Tests: One file, `prototype/backend/test_main.py`, covering the health endpoint scaffold. |
| 4. Word export (`develop`) | ⚠️ partial | 122 issue citation(s) become small in-text tags; 74 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | §0-§3 and environment prose are presentable; no specs or implementation section, and the prototype demo is only a health check. |

**Proposal, what to write:** §4 Specifications: no spec for Epics #47, #50, #56 (scope, FR, NFR, acceptance, open questions); `docs/specs/example-spec.md` is untouched; §4 Design documents: system-context and data-flow exist but lack decisions with rejected alternatives and a not-yet-designed list; add ER and architecture docs; §4 Implementation details: nothing describes the backend, database and observation API in the prototype; write it from #107-#114; §2 Goals and Objectives is a bullet list; add prose per epic explaining each goal and its stories; Merge develop into main: main §3 and §4 still hold template prompts.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: §3, §4 environment, diagrams, planned activities and Postgres setup; PR #120: open, targets develop; PR #121: architecture diagram update on `feature/84-architecture-diagram`.

**To do before your Sprint 3 review:**

1. Write one spec per epic (#47, #50, #56) in `docs/specs/` using `example-spec.md`, and summarize each in §4.
2. Expand `system-context.md` and `data-flow.md` into the six-part design shape; add ER and architecture design docs with decisions and rejected alternatives.
3. Add an 'Implementation details' subsection to §4 covering backend, database and observation API from #107-#114.
4. Create child issues for stories #49, #51-#55, #58-#61 with one assignee and Sprint milestone; remove sp: from #91, #92, #94, #95.
5. Rewrite §2 as prose per goal; give #17, #18, #92, #109 assignees.
6. Merge #120 and #121, then develop into main through a PR; stop direct commits to develop.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · G03 California: Three AIs and Literate Programming (RTX-3)

*Jupyter pipeline that transcribes an equation, generates noisy data, trains a PyTorch model and plots results.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Replace the §4 template placeholder with the environment and resources section, since everything else in §4 hangs off it and it is currently empty.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 13 stories have child issues (#50 has #51, #69, #70; #46 has #78). Only #50 and #46 have child issues; 11 other stories (#30, #33, #31, #34, #35, #36, #37, #45, #47, #48) have none.; Not linked in proposal §2/§4: #69, #70, #78 (tasks), #71, #72 (spec tasks), #65, #60, #51, #41 and meeting issues.; #71 has no assignee; #71 and #72 carry sp: 1 and have no parent story.; Epics #43, #44, #27, #28 use bare refs; the #31 link in §2 points to /issues/30.; PR #77 (open) and #29, #11, #9, #8 have no Closes #N; direct commit 85f6da8 on main/develop.; Stories #45 and #47 lack a Sprint milestone; #45 has no assignee; #47 is open on the board without one.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.2 is a two-row table with a placeholder and an empty Goal 4 ref; §4 planned activities is one table row (#59) plus a template placeholder.. |
| 3. Prototype works | ⚠️ partial | Dataset generation with range validation, datatype storage, dataset display, a PyTorch train script with loss curve, and a verifier; transcriber is a stub. CI: develop 11-05 green; main 10-27 green. Prototype job ran 'Install and test (Python)'; Node steps skipped, so team tests in tests/ did run. Tests: tests/test_verifier.py and tests/test_train.py on develop; none for generate_dataset, store_datatype or display_dataset; main has only test_verifier. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Dataset and training pieces run, but §4 is a placeholder, the transcriber is unmerged (PR #76) and the README does not describe running the pipeline. |

**Proposal, what to write:** §4 opening is still the template prompt plus a placeholder: write the environment/resources section (Jupyter, PyTorch, Mathpix/recognizer API, hosting) with the reason for each.; §1.2 has two problem rows and a placeholder; write full problem-statement paragraphs ending in typed refs, including Goals 2-4.; Specs are only indexed in §4, not carried: summarize docs/specs/transcription.md and data-generation.md in prose; specs for Goals 3 and 4 do not exist (#71, #72).; Design is Figures 1-4 with captions only; add data model, key decisions with rejected alternatives and 'not designed yet' prose from docs/design/architecture.md.; No implementation-details subsection: describe generate_dataset, store_datatype, display_dataset, train and verifier with task refs; planned activities list only #59.; §1 Introduction is four paragraphs with no issue refs; related work (§1.1) is strong and comparative..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #76 (feature/50-transcriber) — Mathpix recognizer, pipeline notebook, transcription tests, transcription spec; PR #74 (feature/32-train-model) — trains model on Goal 2 data, edits train.py; PR #77 into feature/46-plot-equation — plot_equation.py with tests; needs Closes #46 and a base of develop; Release develop to main: main CI is from 10-27 and lacks train tests and csv files.

**To do before your Sprint 3 review:**

1. Write §4 environment and resources: each tool, API and data store with the reason chosen, ending each paragraph with typed issue refs.
2. Create child issues under every story (e.g. #30, #33, #36, #35, #34, #31, #48, #37) with one assignee and a Sprint milestone; link each in §4.
3. Add Closes #N to PR #77, retarget it to develop, and merge PRs #74 and #76 after review.
4. Rewrite `prototype/README.md` with real setup, run and test steps for the notebook pipeline; remove login.py references.
5. Finish §1.2 for Goals 1-4 and fill every proposal link table gap (§2 #31 link, §4 table rows for #69, #70, #78).
6. Add tests for generate_dataset, store_datatype, display_dataset; write specs for Goals 3 and 4 (#71, #72) and carry spec summaries into §4.
7. Write §4 design prose: data model, key decisions with rejected alternatives, and what is not designed yet.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket trader PNL and ranking dashboard (SNX-1)

*Computes Polymarket wallet profit and loss from SonarX Polygon data in Snowflake, ranks traders, and feeds a dashboard.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Get Snowflake credentials (#153) and run the existing PNL code on real SonarX trades so the review demo shows live output.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 12 of 12 stories have child issues (3 to 12 each: feature, task, sub-task). #149, #152, #153, #154, #155 (and #142) are open Sprint 3 tasks not linked from proposal §4.; #4 (old team README PR) closed without Closes; all Sprint 3 PRs close an issue.; #13 and #12 are sub-tasks with no parent story; ~20 closed admin tasks (#1-#147) have no parent.; Epics #24, #29, #33 have no Sprint milestone (stories carry sp:, no points under any story).. |
| 2. Proposal §0–§4 (`develop`, ≈ 32 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: none; §4 planned activities are prose (2,300 words). §1.2 is a 4-row table with no prose.. |
| 3. Prototype works | ✅ done | Python core: settings, Snowflake client, FIFO position matching and resolution handling, checked against the specs' worked example; no live data or dashboard yet. CI: develop 11-08 and main 11-07 green; 'Install and test (Python)' ran pytest on team code, Node steps skipped correctly. Tests: Unit tests for positions, resolutions, settings, Snowflake client; live smoke integration test skipped without credentials. |
| 4. Word export (`develop`) | ✅ done | 114 issue citation(s) become small in-text tags; 100 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Proposal §0-§4 is close to demo quality, but the prototype is unit-tested logic with no live data or UI to show. |

**Proposal, what to write:** §1.1 table 'Why ours differs' column still reads 'Will discover after meeting with mentor' in every row; write the real contrast per tool.; §1.2 Problem Statements is only a table; add a paragraph per problem P1-P4 explaining evidence and impact.; §4 environment is one paragraph; storage for results and dashboard framework undecided. Add per-resource reasons (Snowflake, Python, pytest, dashboard, hosting).; Specs cover Goals 1 and 2 in full; Goal 3 has only a 700-word question list, not scope/NFR/acceptance criteria.; develop holds the sequence design and most inlined docs; main lags (release PR #154 pending)..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #150 - proposal §5-§7 draft, AI rules, stale §4 facts; PR #144 - Sprint 3 review doc (draft); PR #156 - updates dashboard-questions spec; Branch develop to main (#154) - sequence design, data model update.

**To do before your Sprint 3 review:**

1. Fill the 'Why ours differs' column in §1.1 and add comparative prose naming what the project adds over each tool.
2. Expand §1.2 into a paragraph per problem with evidence; link each to its goal.
3. Rewrite §4 environment as a per-resource list with reasons; record results storage and dashboard framework choices (#52).
4. Write a Goal 3 spec (scope, FR, NFR, acceptance, open questions) in docs/specs and inline it in §4.
5. Obtain Snowflake credentials (#153) and run the pipeline on real wallets; capture a demo.
6. Link #149, #152-#155, #142 in §4 and merge develop to main (#154) before the review.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, Whale Identification/Location System

*Passive acoustic system: AI detects whale calls, a hydrophone-delay locator estimates direction and distance.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge the three unmerged design branches into develop, then write §0 and §3 so the proposal reads as a paper.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 9 stories have child issues (tasks hang off epics #8 and #14 instead). 14 of 40 issues not in proposal §4: design tasks #56-#71, #47, #61 (all Sprint 3).; #56, #57, #61, #67, #68, #69 have no assignee; #57, #61, #68, #71 have no Sprint milestone.; Tasks #49, #50, #51 under epic #14 carry sp:, while stories #15-#18 hold the points.; [epic:#8]/[epic:#14] refs appear in the §4 table; epics belong in §2 only (7 misplaced).; Design work sits in 4 unmerged branches (#49, #58, #70 and fill-section-4-proposal.md).. |
| 2. Proposal §0–§4 (`develop`, ≈ 4 pages) | ⚠️ partial | ❌ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ❌ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Planned activities' is a 15-row issue-link table with one intro paragraph and no prose; the spec index lists one spec plus a template placeholder row.. |
| 3. Prototype works | ✅ done | Locator: TDOA direction and distance from simulated hydrophones, call saving with timestamp; AI detector scripts (whale vs ambient/boat) and DB schema/seed. CI: develop push CI green incl. 'Install and test (Python)' on team code; main latest run failed only the Repository harness 'Run gates' step, prototype job passed. Tests: 4 files in `prototype/tests` (tdoa, locate, save_call, speed_of_sound); detector scripts untested. |
| 4. Word export (`develop`) | ⚠️ partial | 33 issue citation(s) become small in-text tags; 26 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Locator and detector can be demoed from the README, but §0, §3 and §4 are template text and no diagrams exist. |

**Proposal, what to write:** §0 Abstract is still the template placeholder; write the one-page abstract.; §3 Proposed Approaches is the unfilled template prompt; write strategy, alternatives (other detectors, other TDOA methods) and reasoning.; §4 opening still holds template text and 〈…〉 markers: no tools, hosting, dataset or Postgres/PyTorch rationale written.; No design documents or diagrams in the proposal; `docs/design/` is empty and `docs/specs/goal-1-detector.md` is not indexed in §4.; Only `docs/specs/goal-2-locator.md` is indexed; add the Goal 1 spec and summarize both in prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branches feature/49-locator-design, task/58-ai-design, task/70-detector-design: design docs and diagrams not in develop; Branch fill-section-4-proposal.md: §4 content not in develop; develop to main: main's CI harness is red and main trails develop.

**To do before your Sprint 3 review:**

1. Write §0 Abstract and §3 Proposed Approaches in full paragraphs, each ending with issue refs.
2. Merge the three design branches, then embed the context, architecture, ER and data-flow diagrams in §4 with captions and explaining prose.
3. Rewrite §4 environment: Python, PyTorch, librosa, Postgres/Docker, dataset sources, each with the reason chosen.
4. Index `docs/specs/goal-1-detector.md` in §4 and summarize both specs; add refs for #56-#71 and assign owners.
5. Create child issues under each story (#9-#18) so story to task to sub-task is visible; keep sp: on stories only.
6. Fix prototype README commands and add tests for `ai-detector/` before the demo.
7. Open a develop-to-main PR with `Closes #N` once the harness gate passes.

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

### G07 · Mighty Morphins: Online Material Database

*Web app that extracts CoC and test-report PDF data into a structured, searchable material database.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Replace the login scaffold in `prototype/` with the smallest PDF-to-database extraction slice and a passing test, then demo it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 17 stories have child issues (#48, #49); the 15 Goal 1-3 stories #12-#27 have none. Stories #12-#16, #18-#21, #23-#27 have no child issues and no Sprint milestone; #84 and #28 are not linked from proposal.md; #28 is epic-typed but is a task; #38 and #78 carry sp: under story #48 (double counting); 24 of 50 proposal links are bare #N, not typed refs; #83, #82, #80 close issues not in proposal; PRs #81 and #50 have no Closes; Goal 0 epic #42 has no sp: or stories under it for design. |
| 2. Proposal §0–§4 (`main`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 30-row issue table with no prose; the environment and spec/design sections are tables.. |
| 3. Prototype works | ❌ skeleton | Nothing: `prototype/` still holds the course `login.py` example and its README placeholders; no extraction, storage or UI code. CI: main CI green (11/5 PST); 'Install and test (Python)' ran but only exercises the course `test_login.py`, so no team code is tested. Tests: Only the course `prototype/tests/test_login.py`. |
| 4. Word export (`main`) | ⚠️ partial | 90 issue citation(s) become small in-text tags; 55 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | Proposal text and design diagrams exist, but there is no working prototype; a demo would show only slides and docs. |

**Proposal, what to write:** §4 Environment: table gives one-line purposes; write why each tool was chosen and resolve React/Vue and Snowflake versus RDS PostgreSQL; §4 Diagrams: five figures have captions only; add a paragraph explaining each and what it implies for the design; §4 Specs/Designs: three specs and five design docs are only linked; summarize each in prose, with decisions and rejected alternatives; §4 Implementation details missing; planned activities should describe remaining work in prose, ending each paragraph with its refs; §1 Introduction is about 260 words; expand motivation, scope and sponsor context.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is behind main and holds no unique work; use main as base.

**To do before your Sprint 3 review:**

1. Choose the Sprint 3 slice (PDF upload to extraction to stored record) and file feature/task children under stories #12, #13 and #18.
2. Replace `prototype/login.py` and `tests/test_login.py` with team code, tests per acceptance criterion, and a real README.
3. Rewrite §4 tables as prose: tool rationale, a paragraph per diagram, a paragraph per spec/design doc, and remaining work.
4. Add an Implementation details subsection to §4 describing the prototype modules, tied to task issues.
5. Add children, assignees and Sprint milestones for all Goal 1-3 stories; remove sp: from #38 and #78; retype #28.
6. Convert bare #N refs in §4 to typed refs and link #84 and #28.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · G08 Crime Busters: Interactive Crime Map and Database

*Localhost Flask/SQLite/Leaflet app that loads public crime records and supports radius search with filters and summaries.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Write the §4 per-epic specification prose (functional and non-functional requirements, acceptance criteria, open questions) from the three docs/specs files, since the proposal currently only indexes them.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child issues (#4, #5, #28, #13, #15, #16, #21, #22). sp: carried by tasks under stories: #36, #35, #32 (under #28), #23 (#13), #11 (#5), #9 (#4); double counting.; No assignee on tasks #27, #29, #30, #31, #33, #34.; Story #13 has no sp:; #45, #46, #47 are closed duplicate stories (untyped, no milestone) not in proposal.; #79 (task) not linked in proposal §4; #62 has no Sprint milestone.; PR #40 merged without Closes #N; direct pushes none.; §4 cites story refs such as #4, #5, #28, #13 (stories belong in §2 only); #68 is a bare ref.. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Specification and design documents' (11 rows) and 'Planned activities' (26 link rows, 664 words) are tables; specs are only indexed there.. |
| 3. Prototype works | ⚠️ partial | Standalone modules: normalize Costa Mesa records, SQLite schema/loader, selected-area filtering, frequency counts. No Flask, map or integrated run yet. CI: develop 11-09 green, main 11-04 green. Python step ran; no Node. Team tests are at prototype root, README still points at tests/ and login.py, so discovery unconfirmed. Tests: test_normalize, test_load_db, test_area_filter, test_crime_frequency on synthetic data; tests/test_login.py is scaffold. |
| 4. Word export (`develop`) | ⚠️ partial | 65 issue citation(s) become small in-text tags; 43 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | §0-§3 and environment are solid and data-layer modules are tested, but there is no running app, §4 specs/design are tables, README is scaffold. |

**Proposal, what to write:** Specs for Goals 1-3 exist in docs/specs/ but §4 carries only an index table; add per-epic scope, functional/non-functional requirements, acceptance criteria and open questions in prose.; Design is split: architecture and context have captions plus prose, but the data-flow and radius-search sequence diagrams are only linked bullets; embed them with explanatory paragraphs.; No data model, key-decision or 'not designed yet' prose in §4: write them from docs/design/crime-database-er.md and architecture.md with rejected alternatives.; Planned activities is mostly a 26-row issue table; replace with prose per goal, ending with typed refs.; Implementation details: describe area_filter, crime_frequency, normalize, load_db and schema.sql in a subsection with task refs (#17, #18, #10, #11, #35, #36).; §2 goals are short bullets with no explanatory prose; §3 is concise and reasoned, with alternatives..

**Merge first** (it doesn't count until it's in `develop` or `main`): None open: develop is ahead of main only by Sprint 3 docs; release develop to main when README is fixed.

**To do before your Sprint 3 review:**

1. Write §4 specification prose per epic (Goals 1-3) from docs/specs/crime-data-foundation.md, crime-pattern-analysis.md and crime-map.md, ending with typed task refs.
2. Embed the data-flow and radius-search sequence diagrams in §4 with captions and paragraphs; add data-model, key decisions and not-yet-designed prose.
3. Remove sp: from tasks #36, #35, #32, #23, #11, #9; set sp on story #13; assign tasks #27, #29, #30, #31, #33, #34.
4. Rewrite `prototype/README.md` and delete `prototype/login.py` and its test; document how to run each module and the pytest command.
5. Build the Flask plus Leaflet slice (#23, #24) on the SQLite data so the review can show a map; add tests for each acceptance criterion.
6. Replace the planned-activities table with prose and add an implementation-details subsection for merged modules; link #79 and use task refs in §4.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*Web app that stores a vehicle's service history and recommends next services with urgent or convenient labels.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Merge develop into main so the working prototype and full §4 are what the review sees.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 1 of 10 stories has a child issue (#29 has #63); the other 9 have none. Stories #30-#38 have no feature/task children; breakdown on the issue board is missing.; 27 tasks (#16-#59) have no parent story; Sprint 3 and 4 work is not yet broken down.; #49 (spec) is open though its PR merged; #59 and #56 still open in Sprint 2.; PR #20 (old initial draft) lacks Closes; Sprint 2-3 PRs all close an issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 28-row issue-link table; spec/design section is an index table.. |
| 3. Prototype works | ✅ done | Vehicle selection: Flask API, SQLite schema and seed, React/Vite page to pick make/model/year/trim and save a vehicle. CI: develop 11-03 green; Node and Python install-and-test steps both ran. main last CI 10-22 still holds only the course login example. Tests: pytest API and smoke tests plus a jsdom page test for vehicle select; course test_login still present. |
| 4. Word export (`develop`) | ⚠️ partial | 40 issue citation(s) become small in-text tags; 40 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | Prototype slice runs from develop and is demoable; proposal §4 on main is skeleton and develop's §4 lacks spec and implementation prose. |

**Proposal, what to write:** §1.2 still has the template quote 'Briefly state the problem'; write fuller problem paragraphs.; §3 is about 190 words (one approach, one alternative); add reasoning and more decisions with rejected options.; Five spec docs and two design docs exist but §4 only indexes them; summarize each (scope, FR, NFR, acceptance) in §4.; Add an 'Implementation details' section describing the vehicle-selection API, SQLite schema and React page as built.; Replace the §4 work-item table with prose per goal ending in issue refs; main §4 is still skeleton..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop to main - full §4, specs, diagrams, working prototype (main is still skeleton).

**To do before your Sprint 3 review:**

1. Merge develop into main now; main still has the scaffold prototype and skeleton §4.
2. Create child issues under stories #30-#38 (feature, task) with one assignee and Sprint milestone; link them in §4.
3. Write §1.2 prose for P1-P2 and expand §3 to cover each key decision with rejected alternatives.
4. Summarize each of the five specs and design docs in §4; add an 'Implementation details' subsection for the built slice.
5. Replace the planned-activities table with per-goal prose ending in typed refs.
6. Close #49, decide #59, and build the recommendations/alerts slice for the review.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection

*Graph model of USDT/USDC transfers with heuristic and ML wash-trading detection and an investigation dashboard.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Push the working `prototype/network.py` and its tests so the README run steps work, then demo it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 14 stories have child issues (tasks hang under epics and #6/#46 only). 14 direct commits on main/develop (e.g. moving `development-plan.md`); use PRs that close issues.; #3 is cited as [task:#3] but has no issue type.; Stories #53, #54, #55 have no assignee; #42, #64, #6 have several assignees.; #64 (Sprint 2) and #31 (Sprint 2) still open; #56 has no Sprint milestone.; §4 tracked-task list omits #45, #46, #51, #56, #59, #64, #67 and #5 (9 issues missing).. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Tracked Task Issues' and 'Planned Activities' are bullet lists of Sprint 1 tasks and five one-line items, not prose.. |
| 3. Prototype works | ❌ skeleton | Nothing from the project: `prototype/` holds only the course `login.py` and its test; no graph or ingestion code. CI: develop green incl. Python install/test; main latest run failed Repository harness 'Run gates'. Prototype job only ran the course `test_login.py`. Tests: Only `prototype/tests/test_login.py` (course scaffold). |
| 4. Word export (`develop`) | ⚠️ partial | 29 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | README describes `network.py` and 5 tests that are not in the repo; only the course login example runs. |

**Proposal, what to write:** §1.1 Related Work is one sentence on one vendor; add a pros-and-cons table of 3-4 tools plus prose on how StableScope differs.; §1.2 Problem Statements is a single sentence; write P1..Pn with why each is hard.; §2 keeps unfilled [N]/[M]/[K] targets in objectives 2.2, 2.4, 2.6, 3.1; set measurable numbers.; §4 environment is four bullets with no reasons; justify SonarX, DuckDB, scikit-learn, dashboard choice.; Diagrams carry one-line captions only; summarize `docs/design/architecture.md` decisions in §4 prose; Epic-23/24 specs keep 'Account management' titles..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch 50-spec_23_and24: spec update not in develop; develop to main: main lacks the §4 diagrams, design doc and specs; main CI red.

**To do before your Sprint 3 review:**

1. Commit the Goal 1 prototype slice (`prototype/network.py` plus tests) that the README already describes; remove `login.py`.
2. Add child feature/task issues under every story (#25-#33, #38, #39) with one assignee and a Sprint milestone each.
3. Rewrite §1.1 as a comparative table of existing detectors plus prose, and expand §1.2 to P1..Pn.
4. Replace [N]/[M]/[K] in §2 and expand §4 environment with the reason for each tool.
5. Retitle the Epic-23/24 specs, and summarize spec and design content in §4 prose with issue refs.
6. Link #45, #46, #51, #56, #59, #64, #67 in §4; fix #3 type.
7. Open a develop-to-main PR with `Closes #N` after gates pass.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker (live runner tracking, posts, race-time prediction)

*React Native app streams runner GPS to Firebase for a spectator web page, plus race-time prediction.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Build the live GPS tracking slice in `prototype/` with tests; the current prototype is an unmodified starter and cannot be demoed.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues. 14 of 31 issues are not linked from the proposal on main: #40, #38, #37, #34, #20, #17, #13, #9 and more.; #1, #2 and #6 are meeting issues with no type label and no parent.; Several tasks have no parent story: #48, #42, #40, #38, #34, #17, #9, #8, #7.; #34, #20, #6 and #1 have no assignee; one direct commit on main.; Only one issue is open for Sprint 3, so Sprint 3 work is not on the board.. |
| 2. Proposal §0–§4 (`main`, ≈ 6 pages) | ❌ skeleton | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 specs index is a table with unfilled template rows beside two real rows; §2 objectives are bullet lines.. |
| 3. Prototype works | ❌ skeleton | Expo starter app (`App.js`, `index.js`); README states no marathon tracking features are implemented. CI: Main 10-29 push run green; Node job ran npm ci and npm test, which is only `node --check index.js` and `expo config`, so no team code is tested. Tests: none |
| 4. Word export (`main`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 17 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | §3-§4 are largely template and the prototype is an unmodified Expo starter with no tracking feature or tests. |

**Proposal, what to write:** §3 is still the template prompt plus two placeholders; write strategy, alternatives and reasoning in paragraphs.; §4 opens with the template text; the tech stack is terse fragments; give a reason for each tool and resource in prose.; Specs `docs/specs/live-runner-tracking.md` and `race-time-prediction.md` are only linked; summarize scope, requirements and acceptance criteria in §4.; Data model design and Figures 1-3 are referenced but images are not in the proposal; embed them with captions and explain each.; No implementation-details section; template placeholders remain in §3, §4 and §5-§8..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch `develop` — 3 §4 figures in proposal but otherwise behind main; sync or retire.

**To do before your Sprint 3 review:**

1. Replace §3 and the §4 template text with prose: strategy, alternatives, reasoning, and a reason for each tool and resource.
2. Build the riskiest slice, runner GPS recording to Firebase with a spectator view, in `prototype/` with a test per acceptance criterion.
3. Embed the data-flow, data-model and screen-flow diagrams in §4 with captions and prose; summarize both specs there.
4. Replace the `node --check` test script with real tests so CI exercises team code.
5. Link the 14 unlinked issues in §4 as typed refs and give each task a story parent and one assignee.
6. File Sprint 3 and Sprint 4 child issues under every story, each with an owner and milestone.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Pipeline that detects signal bursts, classifies waveforms/modulations and explains decisions with attribution heatmaps.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Merge develop into main so the working prototype and its CI-tested modules are what the review sees.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of about 17 stories have child issues (#66, #68, #135); epics have story children. Stories #62-#65, #67, #69-#71, #111, #114-#116 have no child issues; 13 issues not in proposal.md: #135, #126, #95, #137, #136, #103, #36, #27-#32; #123, #98, #88 carry sp: under stories #66 and #68; #63, #68, #70, #71, #126 have no Sprint milestone; #103 untyped and unscheduled; #108 has no milestone; 3 old PRs without Closes (#1, #2, #44); PR #134 open. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 24-line bullet list of issue links; §2 is bullets.. |
| 3. Prototype works | ✅ done | IQ capture to peak picking (baseline v1.4, CV model), channelizer, calibrated classifier with Captum attribution; CLI via `scripts/analyze_iq.py`. CI: develop CI green (11/8 PST); 'Install and test (Python)' ran. main CI green but still the login scaffold, since develop is unmerged. Tests: Nine files under `prototype/tests/`: peak pickers, channelizer, calibration, attribution, classifier, pipeline gate, stand-in training. |
| 4. Word export (`develop`) | ✅ done | 45 issue citation(s) become small in-text tags; 45 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Prototype demo from develop is strong; proposal §4 has no specs, design or diagrams, and main still shows the scaffold. |

**Proposal, what to write:** §4 has one tool paragraph and a bullet list; add per-tool reasons (MATLAB vs Python, PyTorch, Captum, data hosting); §4 Specifications: none per epic (#57-#61); `docs/specs/` holds only the example; fold the `docs/*.md` handoff notes into specs; §4 Design and Diagrams: no context, component, data model or flow diagrams; `docs/images` figures are not in the proposal; §4 Implementation details missing though the prototype has peak picking, channelizer and XAI modules; write them with task refs; §1.2 Problem Statements is 53 words; expand each problem into a paragraph.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: peak picker, channelizer, XAI modules, 9 test files, proposal §3.1; PR #134: Peak-Picker GUI (`prototype/GUI/`), not merged; `Application-Structure` and `docs/team-documentation` branches, unmerged.

**To do before your Sprint 3 review:**

1. Open a PR from develop to main so the working prototype and §3.1 are on main.
2. Write a spec per epic (#57-#61) in `docs/specs/` and summarize each in §4.
3. Draw and caption system context, component and data-flow diagrams; write design prose with decisions and rejected alternatives (#126).
4. Add an Implementation details subsection to §4 summarizing peak picking, channelizer, calibration and attribution with task refs.
5. Rewrite the §4 bullet list as prose paragraphs; add #135-#137, #126, #95 refs.
6. Add children under stories #62-#65, #67, #69-#71; remove sp: from #88, #98, #123; add Sprint milestones to #63, #68, #70, #71.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · G13 BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Offline Windows desktop app (Python core, Electron UI) that suggests deadlines, tracks progress and sends reminders.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Rewrite `prototype/README.md` and rename the tests so CI runs them, so the review can show one verified create-assignment slice from a fresh clone.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features with tasks (#19-#27). Goal 3 features and tasks (#89-#102, #104, #106) and stories #25, #26, #27 have no Sprint milestone.; No assignee on #119, #120 (under #47), #8, #12, #13, #30, #32, #33.; Not linked in proposal: #120, #119, #116, #113, #111, #47, #44, #43, #35, #34, #33, #32, #31, #30, #15, #13, #12, #11, #10, #8.; #116 (prototype folder structure) and #113 are not under a story or feature, so they sit outside the chain.; Closed PRs #117, #36 and merged #4, #1 have no Closes #N; no linked issue is closed yet.; Stories #32, #33 and epic #30 are leftover process issues, untyped in the proposal.. |
| 2. Proposal §0–§4 (`develop`, ≈ 7 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Planned Activities' is a 38-row issue table with no prose; §1.1 is a table with no comparative prose after it.. |
| 3. Prototype works | ⚠️ partial | Develop has a Python core (Models, Database, Assignment and Deadline services) and an Electron/Vite UI with form, list and progress components; main is still the login scaffold. CI: develop 10-31 green and main 10-16 red (harness). Prototype job ran only 'Install and test (Python)'; Node skipped, so the Electron UI is untested and develop's CI predates the code. Tests: One file, A.M.I.Y.A.core/tests/TestAssignments.py; name does not match pytest discovery and nothing tests the UI. |
| 4. Word export (`develop`) | ⚠️ partial | 84 issue citation(s) become small in-text tags; 66 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | Goals and wireframes are written, but §4 lacks architecture, README is scaffold, CI is stale, and no feature issue is closed; a demo depends on unverified code. |

**Proposal, what to write:** §1.1 Related Work is a four-row table only; add paragraphs arguing what A.M.I.Y.A. does differently and tie citations to §8.; §1.2 has three one-sentence problems with no issue refs; expand into paragraphs ending with typed refs to Goals 1-3.; Specs in docs/specs/specs-G1..G3.md are only summarized in one or two sentences each; carry scope, requirements, acceptance criteria and open questions into §4.; No architecture, system context, data model or data flow design: write them (Python core, Electron UI, local storage) with decisions and rejected alternatives.; §4 diagrams are six UI wireframes; add component and data-flow diagrams with captions and prose, plus an implementation-details subsection for the prototype.; Planned activities is a 38-row table: write prose per goal and sprint, ending with typed refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #121 — Sprint reports, edits proposal.md and prototype README; closes #119; Branch feature/34-project-proposal — 28 commits not in develop; Branch updated-proposal — 6 commits not in develop; Release develop to main: main still has only the login scaffold and a red CI.

**To do before your Sprint 3 review:**

1. Rewrite `prototype/README.md` with real setup, run and test steps for A.M.I.Y.A.core and A.M.I.Y.A.ui; delete the login scaffold on main.
2. Rename `TestAssignments.py` to test_*.py, add tests per acceptance criterion in specs-G1/G2, and make CI run the Node package too.
3. Write §4 architecture, system context, data model and data-flow design with decisions and rejected alternatives; embed the three specs' key content.
4. Replace the Planned Activities table with prose per goal; add §1.1 comparative prose and expand §1.2 with typed refs.
5. Give every open child issue a Sprint milestone and assignee; link or close #8, #12, #13, #30-#35, #119, #120 and parent #116, #113.
6. Close Goal 1 features through reviewed PRs with Closes #N and demo create, edit, delete and local storage.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox incident-response training simulator

*Sandboxed desktop simulator for investigating fake malware incidents, with LLM-generated, schema-validated scenarios.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Build the smallest runnable PySide6 window with one tested simulated-file feature so the review has something to demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ❌ not started | 0 of 18 stories have child issues; none of #24-#41 is decomposed. No story #24-#41 has feature/task children; board has no breakdown below story.; 21 open issues have no Sprint milestone, including all 18 stories and epics.; #92, #91 untyped; 16 issues (#79-#94) not linked from proposal; story/epic refs cited in §4.; 9 direct commits on main; PRs #50, #2, #1 closed without Closes; #79-#84, #88 unassigned.. |
| 2. Proposal §0–§4 (`main`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 19-row issue-link table; spec/design section is a link table plus short summaries.. |
| 3. Prototype works | ❌ skeleton | Nothing runs: develop prototype has a Dockerfile TODO and README; login.py removed on develop, still on main. CI: develop 10-31 and main 10-29 green, but 'Install and test (Python)' ran against unchanged scaffold requirements; no team code or tests to exercise. Tests: none (only course test_login on main) |
| 4. Word export (`main`) | ✅ done | 111 issue citation(s) become small in-text tags; 54 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | No runnable prototype; README names a start_simulation.py that does not exist, and §4 lacks implementation and planned-work prose. |

**Proposal, what to write:** §1 Introduction is about 130 words; add background, motivation and scope.; §3 is about 170 words; justify the in-memory design and LLM choice with more alternatives.; Planned activities is a table; #94 rewrites it as prose, finish it per goal.; Design docs are only summarized; add data model, component and key-decision prose (decisions with rejected options).; No implementation section: nothing is built yet. Environment table is solid but diagrams need fuller captions..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #89 - develop to main: aligned design docs, diagrams, prototype README; Branch copilot/create-requirements-list-for-goal-2-47 - unreviewed, unmerged spec work.

**To do before your Sprint 3 review:**

1. Build a runnable prototype slice (simulated desktop window or file system) in prototype/ with pytest tests; fix README to match.
2. Create child issues under every story #24-#41, each with one assignee and a Sprint milestone; give the stories Sprint milestones.
3. Link #79-#94 in §4, type #91/#92, and keep epic/story refs in §2 only.
4. Rewrite planned activities (#94) as prose per goal and expand §1 and §3 to full paragraphs.
5. Add decisions, data model and component prose to §4 design; merge PR #89 so main matches develop.
6. Stop committing straight to main; use issue branches and PRs with Closes.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo for constrained hardware

*Lightweight OpenGL 3.3 C++ game engine with ECS architecture, scene editor, and a demo game.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Merge develop into main by PR, then fill the §4 spec index and work-item table with real links.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 8 stories have child issues (#9, #46, #63 attach to epics or loosely). 21 issues not in proposal: #6, #10-#12, #16, #34-#36, #40, #43-#50, #54, #57, #58, #61, #63, #64.; §2 refs are bare `[epic:https://…]` text, not linked typed refs (0 typed).; Seven stories (#26-#30, #32, #33) have two assignees; #44 has no assignee, #57 no Sprint.; #46 lists itself as parent; #63 typed user-story but is a task; #9 closed with no PR.; Old PRs #3-#5, #41 lack Closes; 4 early direct commits on main; main proposal is still the template.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §1.2 is a two-row table; §4 spec index and planned-activities tables are template rows with 〈…〉 and one placeholder issue row.. |
| 3. Prototype works | ⚠️ partial | CMake C++26 project linking SDL3, assimp, glm, with vendored glad/glm and GLSL shaders; contents of `src/` not verifiable in the sweep. CI: develop CI green but prototype job ran only 'Nothing to build'; CMake/C++ was not built or tested. Main has the course login scaffold. Tests: README test section still the course `test_login.py` flow; no C++ tests visible. |
| 4. Word export (`develop`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 11 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | README gives setup/build/run steps and an engine skeleton exists, but proposal §4 is mostly template and CI never built it. |

**Proposal, what to write:** §4 spec index lists 〈docs/specs/game-engine.md〉 and game-demo.md as placeholders; two specs exist but are not linked or summarized.; §4 has one architecture figure; no system context, data model or data flow, and no prose from `docs/design/architecture.md`.; §4 environment gives one-line reasons per tool; template guidance and 〈…〉 prompts remain; add hosting, platforms and test hardware.; §1.2 Problem Statements are table cells only; write prose on each problem and why it is hard.; §4 work-item table has one placeholder row; list all tasks and describe implemented and remaining work in prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main: main has template proposal and scaffold prototype; develop has everything; Branch 33-objective-24-implement-visual-editor...: 1 commit, editor work not in develop.

**To do before your Sprint 3 review:**

1. Open a develop-to-main PR with `Closes #N` so main shows the real proposal and prototype.
2. Convert §2 refs to `[story:#N]`/`[epic:#N]` and link all 21 missing issues in the §4 table.
3. Link and summarize `docs/specs/game-engine.md` and `game-demo.md` in §4; delete the 〈…〉 rows and template prompts.
4. Add system context and data-flow diagrams and carry architecture.md prose into §4 with figure captions.
5. Create task children under each story, one assignee and Sprint each; keep sp: on stories only.
6. Make CI build the CMake target and add ECS unit tests; fix README test steps.
7. Expand §1.2 into prose and finish §4 planned activities.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · BridgeWatch: real-time detection of cross-chain bridge exploits (SNX-3)

*Hour-of-day baseline and alert rules watch bridge vaults, replay past hacks, and feed a Slack and web dashboard.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Merge PR #96, then carry the Goal 1-3 specs and `docs/design/architecture.md` into proposal §4 as prose with embedded diagrams.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#21 and #19 open and childless; #16 and #5 closed). Eight Sprint 3 tasks #90-#98 are not linked from the proposal.; #97 and #98 have no assignee.; About 20 tasks have no parent story (#95, #94, #93, #92, #91, #90, #72, #67 ...); Sprint 1 tasks keep their own points.; PRs #75, #35 and four early typo PRs have no `Closes #N`; three direct commits on main.; PR #96 (Sprint 3 plan) is open and closes #90, which the proposal does not cite.. |
| 2. Proposal §0–§4 (`main`, ≈ 13 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: Specs and design are listed in a 4-row table (Table 9); diagrams D1-D6 are a bullet list of links; planned tasks stop at Sprint 2.. |
| 3. Prototype works | ✅ done | Working detector, SQLite store, live Ethereum poller, hack replay on five past bridges, false-alarm evaluation, Slack notifier, FastAPI and web dashboard, Docker file. CI: Main 11-03 push run green; Prototype job ran Install and test (Python), so the BridgeWatch tests ran. Develop also green. Tests: `test_bridgewatch.py`, `test_bridgewatch_live.py`, `test_baseline_check.py`, `test_data_pipeline.py`: detector, live loop, baseline, data loading. |
| 4. Word export (`main`) | ✅ done | 40 issue citation(s) become small in-text tags; 35 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The prototype can be demoed (demo mode, replay, dashboard), but §4 does not yet carry the specs, design documents and implementation detail. |

**Proposal, what to write:** Specs `docs/specs/goal-1-baseline.md`, `goal-2-detection.md`, `goal-3-dashboard.md` are only linked; summarize scope, requirements and acceptance criteria in §4.; `docs/design/architecture.md` (D1-D6) is not carried in the proposal; add the six design elements and embed the diagrams with prose.; No implementation-details section: describe detector, store, live loop, notifier, API and dashboard as built.; Planned activities say later tasks come as filed; describe Sprint 3 and 4 work (#90-#98) in prose with refs.; §1.1 Related Work is 346 words; argue in prose what BridgeWatch does differently, with citations matching §8..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #96 — Sprint 3 plan, §4 citations, Goal 1 spec and architecture design; Branch `90-sprint-3-plan` — 14 commits not in develop.

**To do before your Sprint 3 review:**

1. Merge PR #96, then link #90-#98 as typed refs in §4 and assign #97 and #98.
2. Carry the three goal specs into §4: scope, functional and non-functional requirements, acceptance criteria, open questions.
3. Carry `docs/design/architecture.md` into §4: context, components, data model, data flow, decisions with rejected alternatives, undesigned items; embed D1-D6.
4. Add a prototype implementation section in §4 covering the live loop, detector, store, notifier, API and dashboard.
5. File child issues under stories #19 and #21 and parent the loose tasks to stories.
6. Rewrite the planned-activities prose for Sprints 3 and 4 and expand §1.1 into a comparative argument.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · SonicScape: Galaxy-style Music Discovery App

*Desktop music-discovery app mapping genres, artists and songs as galaxies and planets, with swipe feedback and profiles.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Fix the failing 'Run gates' step on main, then replace the empty prototype skeleton with one tested Last.fm-to-SQLite slice.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 6 stories have child issues (#25, #29, #30); #26, #27, #28 have none. 16 PRs merged without Closes #N, incl. #31-#39 and #45; main has 30 direct commits, mostly proposal and design edits; Tasks #41, #42, #43, #49, #55 carry sp: under stories (double counting); #41, #49, #51, #55 not linked in proposal.md; #42, #43, #46, #47, #53 are bare refs; #49 and #55 have no assignee; no Sprint 3 issues exist. |
| 2. Proposal §0–§4 (`main`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1 and §1.2 are tables; §4 environment, spec/design list and planned activities are tables; §2 is bullets.. |
| 3. Prototype works | ❌ skeleton | Empty module skeleton (`backend/lastfm.py`, `database/db.py`, `main.py`); README says 'no current code' and the run step does nothing. CI: main CI red (11/5 PST): Repository harness 'Run gates' failed; Prototype job passed but ran no team tests (no `tests/` folder). Tests: none |
| 4. Word export (`main`) | ✅ done | 14 issue citation(s) become small in-text tags; 14 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | No runnable prototype and main CI is red; only documents and diagrams exist to show. |

**Proposal, what to write:** §4 Specs: three specs exist in `docs/specs/` but the proposal only lists them; add a prose summary per epic; §4 Diagrams: Mermaid code blocks will not convert to Word; export images, add captions and an explaining paragraph each; §4 Design docs: `dataflow.md`, `screenflow.md`, `system_context.md` are near empty; write the six-part design with decisions; §4 Implementation details missing; planned activities lists five rows only; describe prototype work and remaining work in prose; §1.1 comparative prose and §1.2 problem paragraphs missing; Goal 2 doc links in the §4 table use broken relative paths.

**Merge first** (it doesn't count until it's in `develop` or `main`): develop is behind main; its only unique work is bringing scaffold files; use main.

**To do before your Sprint 3 review:**

1. Read the failing 'Run gates' log on main and fix it so CI is green.
2. Create Sprint 3 feature/task issues under stories #25-#30 and implement the first slice with tests and a working README run step.
3. Export the Mermaid diagrams as images with captions and explaining paragraphs; fix broken relative links in the §4 spec/design table.
4. Write Implementation details and summarize each spec and design doc in §4 prose; expand `dataflow.md`, `screenflow.md`, `system_context.md`.
5. Convert §1.1, §1.2 and §4 tables into paragraphs and add typed refs for #41, #49, #51, #55, #42, #43, #46, #47, #53.
6. Work through develop and PRs with Closes #N; remove sp: from #41, #42, #43, #49, #55.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18 ProStrats: Project Rogue

*2D Unity action roguelite with weapon-and-element builds, shared combat and movement, and branching replayable runs.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Index and summarize the three docs/specs files in the §4 specification section, since they exist but the proposal never carries them.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 10 stories have child issues (#32 has #72, #35 has #64, #41 has #48). Seven stories (#33, #34, #36, #37, #38, #39, #40) have no child issues; spec and diagram tasks #53, #56, #61, #65 hang off epics instead.; #64 carries sp: 2 under story #35 (double counting); #58 and #74 have no Sprint milestone.; Not linked in proposal: #74, #72, #65, #64, #61, #58, #56, #53; #13 and #26 are untyped leftovers.; Proposal §1 cites epics #29-#31 and §4 cites story #41 (epics and stories belong in §2 only).; #56 has two assignees; #58 and #74 have no parent; direct scaffold commit c9af2ba on main/develop.; All 24 PRs reference an issue; develop proposal §4 status text is stale (#33, #34, #35, #37 listed open).. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 'Specification and design documents' (7 rows, no spec rows) and 'Planned activities' (28 rows, 639 words) are tables; specs are not in the index.. |
| 3. Prototype works | ⚠️ partial | Unity 6 project with a combat scene (resolver, abilities, loadouts, target dummy) and a traversal room with class movement; progression verification editor script. CI: develop 11-05 and main 11-04 green, but the prototype job ran only 'Install and test (Python)' on the scaffold requirements; the Unity project is not built or tested by CI. Tests: No automated Unity tests; Editor/ProgressionVerification.cs and Test_Combat scene serve as manual checks. |
| 4. Word export (`develop`) | ✅ done | 54 issue citation(s) become small in-text tags; 47 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Playable combat and traversal demos with a working README can be shown, but §4 specs/design are thin, run flow (Goal 3) is unbuilt, and CI proves nothing. |

**Proposal, what to write:** §4 specs: docs/specs has Goal 1, Goal 2 and Goal 3 specs but the proposal index omits them; summarize each epic's scope, requirements, acceptance criteria, open questions in prose.; Design is two figures with short prose: add data model (save file, progression state), data flow, key decisions with rejected alternatives and not-yet-designed items.; Run/room/reward flowchart and combat class diagram exist in docs/design/diagrams but are not embedded with captions in §4.; No implementation-details subsection: describe the combat resolver, movement, traversal room, loadout panel and progression verification with task refs.; Planned activities is a 28-row table that is stale; replace with prose per goal and sprint ending with typed refs.; §1.2 still contains the template instruction block ('Every problem here must connect...'); delete it. Main branch §3-§4 still holds placeholders..

**Merge first** (it doesn't count until it's in `develop` or `main`): Release develop to main: develop holds merged PRs #66-#73 (specs, weapons, attributes) that main lacks; Branch feature/33-attributes-resources-respec — 2 commits not in develop after PR #73; Branch patch-1 (personal patch branch) — 1 commit not in develop.

**To do before your Sprint 3 review:**

1. Add child issues under stories #33, #34, #36, #37, #38, #39, #40 with one assignee and Sprint milestone; remove sp: from #64; fix #58 and #74 milestones.
2. Update §4 'Specification and design documents' to index and summarize the Goal 1, 2 and 3 specs, with scope, requirements, acceptance criteria and open questions.
3. Embed the run/room/reward flowchart and combat class diagram in §4 with captions and prose; add data model, key decisions and rejected alternatives.
4. Write an implementation-details subsection for the combat, movement, traversal and progression code, and refresh the stale status column in planned activities.
5. Add Unity EditMode tests for combat, attributes, weapons and boons, and note how reviewers run them since CI cannot build Unity.
6. Link #53-#74 in §4, move epic and story refs out of §1 and §4, and delete the §1.2 template block.

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
