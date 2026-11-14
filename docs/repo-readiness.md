# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.

**CPSC 490 · Fall 2026 · swept 2026-11-14 20:16 UTC.** Earlier editions are kept in this file's git history.

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
| [G01](#g01) BGAF | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 84 |
| [G02](#g02) Linux Larpers | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 15 |
| [G03](#g03) California | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Tue Nov 10 | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 33 |
| [G05](#g05) Fighting Mongooses | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G06](#g06) GapWise | Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G07](#g07) Mighty Morphins | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 8 |
| [G08](#g08) Crime Busters | Tue Nov 17 | ✅ | ✅ | ✅ | ⚠️ | ✅ | ≈ 8 |
| [G09](#g09) Sigma Squad | Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 10 |
| [G10](#g10) Team Jiddak | Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 5 |
| [G11](#g11) 5 Guys | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G12](#g12) ACJMM | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G13](#g13) BYKX | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G14](#g14) Cyber Squad | Thu Nov 12 | ⚠️ | ✅ | ✅ | ✅ | ✅ | ≈ 11 |
| [G15](#g15) HIBBI-01 | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) G16 | Thu Nov 19 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 17 |
| [G17](#g17) G17 | Thu Nov 19 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | ≈ 5 |
| [G18](#g18) G18 | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) Titan Security | Thu Nov 19 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G20](#g20) Solos | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |

- **Rule 1 met:** 2 of 20 (G04, G08).
- **Proposal §0–§4 complete:** 2 of 20 (G08, G14).
- **Prototype working, with a real slice and tests:** 13 of 20 (G01, G02, G03, G04, G05, G06, G08, G09, G11, G12, G14, G15, G16).
- **Ready to demo both today:** 2 of 20 (G08, G14).

**What changed since the Nov 5 edition:**

- **G08 is the first group with a ✅ on all three rules.** Since Nov 12 its unassigned tasks were fixed and the last unlinked issue was added to the proposal, and `develop` now runs a map demo from a fresh clone with a current README. Release PR #86 into `main` is still open: merge it.
- **G14's proposal now passes rule 2.** On `develop`, §4 gained design decisions with the rejected alternatives, implementation details by layer, and a pros-and-cons table in §1.1. All 18 stories now have child issues (5 on Nov 12); 40 of the new children still need a Sprint milestone.
- **Three prototypes moved up on rule 3.** G06 (`develop`: an end-to-end command-line demo, a rewritten README and seven team test files, CI green) and G15 (CI now builds the CMake project and runs the tests) are ✅. G10 went from skeleton to partial: a Goal 1 prototype with 31 tests is on `develop`, but its README is stale and the harness gate there is red.
- **Story breakdown improved:** G12 now has child issues under 12 of 18 stories (3 on Nov 12) and removed the story points it had under stories. G01 merged the PR that links its 47 Sprint 4 issues from the proposal.
- **Also moved:** G07 (unlinked issues down from 6 to 4), G13 (the merge-conflict markers in §4 are resolved; the Planned Activities issue table and some malformed references remain), G20 (sprint and crouch movement merged to `develop`).
- **No change since Nov 12:** G02, G03, G04, G05, G09, G11, G16, G17, G18 and G19. G02, G03, G09 and G17 have new issues or open PRs, but nothing merged into the proposal or the prototype.
- **Check before your review:** G09 has five feature PRs open and G17 has two; work in an open PR does not count until it merges. G10 and G17 have a red harness gate. Several groups still keep finished work on `develop` only: merge it to `main`.
- **Review dates:** G06–G10 Tue Nov 17, G16–G20 Thu Nov 19. G01–G05 had theirs on Tue Nov 10 and G11–G15 on Thu Nov 12.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and strategy backtesting

*Rebuild Hyperliquid's order book from SonarX data, validate it, and backtest strategies only on validated days.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Get the replay engine (#144, #145) running with tests on one market-day, since validation, gate and backtest all depend on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58, closed, has none); 7 stories (#23-#28, #279) are still open. Eleven tasks carry `sp:` under a story or pointed task (double counting): #195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134.; Twenty child issues lack exactly one assignee (#187, #169, #167, #166, #165, #164, #163, #159, #158, #157 ...); stories #24, #26, #27 are unassigned.; 33 tasks have no parent story or feature (#271, #264, #249, #247, #232, #231, #206 ...).; `[task:#151]` is cited four times but #151 is a sub-task; epic/story citations also sit in §4 rather than §2 only.; Many early PRs (#126, #123, #62, #40, #38, #29) lack `Closes #N`; three direct commits on main; PR #334 open.. |
| 2. Proposal §0–§4 (`main`, ≈ 84 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: None in place of prose; §4 is paragraphs ending in refs. A small link table remains in the specification index only.. |
| 3. Prototype works | ✅ done | DuckDB schema and a SonarX L2 snapshot loader (`storage.py`); replay, validate, gate, backtest and report modules are docstring stubs; front end is the Vite starter. CI: Latest main run green; Prototype job ran Python install and pytest. Node steps skipped, so the Vite front end in `prototype/frontend` is never built in CI. Tests: `prototype/tests/test_package.py` (step layout) and `test_storage.py` (schema, load, exact decimals, repeat load). |
| 4. Word export (`main`) | ✅ done | 719 issue citation(s) become small in-text tags; 218 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | §0-§4 can be presented now; the prototype only loads one snapshot file into DuckDB, with replay, validation and backtest not yet built. |

**Proposal, what to write:** §1.2 Problem Statements is a short table plus a few sentences; write full paragraphs for P1 and P2 with the evidence behind each.; Validation-and-gate and replay-engine designs (#260-#262, open) are not in §4; the module design only gives contract-level summaries.; §4 carries about 16,000 words of spec and design prose, but epic/story citations belong in §2; move them (#278).; Planned activities mix old and new work; mark what is done, in progress and remaining, including the new Sprint 4 front-end tasks (#327-#333)..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #334 (open, main) — new change awaiting review and merge into main; Branches 18-abstract-intro, 43-update-goals-and-objectives and similar old branches — merge or delete; develop holds an old 43,786-character proposal; sync it with main or retire it.

**To do before your Sprint 3 review:**

1. Build the replay engine (#144, #145) in `prototype/` with a test per acceptance criterion in the replay spec, and show it on one day of data.
2. Remove `sp:` from tasks #195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134.
3. Give each open child issue exactly one assignee and attach the 33 parentless tasks (#271, #264, #249 ...) to a story or feature.
4. Rewrite §1.2 as full paragraphs and write the gate and replay designs with diagrams (#260-#262).
5. Move epic and story citations out of §4 into §2 (#278); retype the #151 refs as sub-task.
6. Add a Node build and test job for `prototype/frontend` to the CI workflow.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

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

**To do before your Sprint 3 review:**

1. Write one spec per epic (Goals 1-3) in `docs/specs/` and summarize each in §4 with FRs, NFRs, acceptance criteria and open questions.
2. Add a §4 design narrative from `docs/design/*.md`: data model, decisions with rejected alternatives, what is not designed yet.
3. Add a §4 Implementation subsection describing the backend API, tables, firmware and dashboard, ending in task refs.
4. Create child issues for stories #49, #51-#55, #58-#61 and remove `sp:` from the 21 tasks (#95, #92, #91 ...).
5. Get one ESP32 observation into the dashboard via the API and add a CI build for `prototype/dashboard`.
6. Link #132, #130, #99 and #20 from the proposal and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

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

**To do before your Sprint 3 review:**

1. Rewrite `prototype/README.md` with working install, run and test commands; remove the course `login.py` references.
2. Replace the §4 template prompt with Environment prose: each tool, platform and hosting choice with its reason.
3. Summarize `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` in §4 with FRs, NFRs and acceptance criteria.
4. Expand the §4 design section from `docs/design/architecture.md`: data model, decisions and rejected alternatives, undesigned parts.
5. Create child issues for the ten stories without breakdown, with one assignee and a Sprint milestone each; link them all in §2/§4.
6. Add `Closes #N` to PRs and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and trader profitability analytics

*Compute profit and loss per Polymarket wallet from SonarX Polygon data, rank traders, and show them on a dashboard.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

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

**To do before your Sprint 3 review:**

1. Merge PRs #158, #159, #156, #150 and #160 so the specs, tests and review are on develop and main.
2. Expand §4 Environment and resources: one subsection per tool or platform, with the reason, including the dashboard framework decision.
3. Rewrite §0 Abstract, §1.1 Related Work and §1.2 Problem Statements as full paragraphs, with citations matching §8.
4. Run the position builder on real SonarX data end to end and demo one wallet's PNL.
5. Assign #20 and give each standalone task a parent story or label it a writing task.
6. Delete the eight stale feature branches once merged.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, whale identification and location system

*Detect whale calls with an AI model and locate them from hydrophone recordings.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

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

**To do before your Sprint 3 review:**

1. Merge PR #72 and PR #62, then merge develop into main and fix the failing harness gate so main CI is green.
2. Write §0 Abstract and fill the sponsor and date in the front matter.
3. Replace the §3 template prompt with strategy, alternatives and reasoning.
4. Write §4 Environment and resources, summarize the detector spec and design, add the architecture diagram with a caption, and describe the built prototype.
5. Create child issues under stories #10-#13, #15, #16, #18; give #69, #68, #67, #61, #57, #56 an assignee and Sprint milestone.
6. Fix the `prototype/README.md` run commands and add tests for `ai-detector/`.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant that tracks and targets weak spots

*A study assistant that generates questions from a student's notes and aims practice at tracked weak concepts.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write the Goal 1 spec (#13) into §4; the prototype tests already map to it, and design text follows from it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 17 stories have child issues (#17, #23, #24, #48); #5 and #6 are old closed leftovers. Stories #14, #16, #18, #19, #21, #22, #26, #28-#31 have no child feature/task issues.; #41 and #10 carry sp: under story #48; points belong on the story only.; Story #26 has no assignee (closed #5, #6 also none).; Tasks #25, #43, #49, #51 are not linked from the proposal; §4 planned activities use bare #N, not typed refs.; PR #40 has no Closes line; PRs #53 and #55 are open against main, not develop.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Environment is a 6-row table and Planned activities a 3-row issue table; Specification and design documents only says docs will be linked later.. |
| 3. Prototype works | ✅ done | `run_demo.py` takes a notes file through document processing, concept extraction, question generation and weak-spot selection, with a mastery tracker and forgetting; no web app yet. CI: develop latest run green: harness and Prototype build & tests both ran Install and test (Python) on team code. main's latest run failed Run gates; its prototype job passed. Tests: Seven team test files on develop: document processor, concept extractor, question generator, selector, forgetting, mastery tracker, run_demo; plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 19 issue citation(s) become small in-text tags; 19 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A command-line end-to-end demo and accurate README exist on develop; §4 still has no specs or design, and no web app. |

**Proposal, what to write:** §1.1 table cells still carry 〈…〉 brackets; remove them and cite [1]-[4] consistently with §8.; §1.2 is under 100 words plus a table of goal links; write each problem as a paragraph ending in issue refs.; §4 has no specs: write scope, FRs, NFRs, acceptance criteria and open questions per epic (#13, #20, #27).; §4 has two figures with a one-sentence description each; add captions and prose explaining components and data flow, plus a data model and key decisions.; §4 Implementation is absent; describe the five tested modules and `run_demo.py` with task refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prose, prototype demo and green CI; main still has the skeleton; PR #53 (open, main) — answer grader; retarget to develop; PR #55 (open, main) — flashcard system; retarget to develop; PR #54 (open, develop) — study summary feature; review and merge.

**To do before your Sprint 3 review:**

1. Merge develop into main so the green CI, README, demo and prose are the graded branch; fix main's failing Run gates step.
2. Write one spec per epic (#13, #20, #27) in §4: scope, FRs, NFRs, acceptance criteria, open questions.
3. Write the six-part design in §4 and add captions plus prose under Figures 1 and 2.
4. Create child issues for stories #14, #16, #18, #19, #21, #22, #26, #28-#31; remove sp: from #41 and #10.
5. Retarget PRs #53 and #55 to develop; add Closes lines; link #25, #43, #49, #51 as typed refs.
6. Turn the §4 Environment and Planned activities tables into prose and clear the 〈…〉 cells in §1.1.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (sponsor EL-1)

*Extract material data from vendor certificates into a searchable database with a review web app.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Build the page 1 upload-and-extract slice (#86) with tests in `prototype/`; without it there is nothing to demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 16 stories have child issues (#12, #16, #24, #27, #48, #49); 10 stories (#13-#15, #18-#21, #23, #25, #26) have none. Stories #12-#27 have no assignee and no Sprint milestone; ten stories have no children.; Features #86, #88, #90, #93, #95 and tasks #85, #87, #89, #92, #94, #78 carry sp: under a story.; #49 and epics #45, #28, #4 are not linked from proposal.md; one issue sits in the wrong section.; Three direct commits on main and two on develop; PRs #81, #50 and #8 have no Closes line.; Sixteen child issues lack exactly one assignee; #91, #84 and #7 have no parent; PRs #96, #99, #100 open on main.. |
| 2. Proposal §0–§4 (`main`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a long issue table with no prose; Specification and design documents is a link table with short summaries.. |
| 3. Prototype works | ❌ skeleton | Only the course login example; the five prototype-page features (#86, #88, #90, #93, #95) are open. CI: main latest run green: Install and test (Python) ran, but only the course `test_login.py` was exercised. develop also green. Tests: Only the course `test_login.py`; no team tests. |
| 4. Word export (`main`) | ⚠️ partial | 77 issue citation(s) become small in-text tags; 60 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | Proposal and diagrams are substantial, but there is no prototype beyond the course login example to demo. |

**Proposal, what to write:** §1 Introduction is one 259-word block; add motivation, scope and a reading guide.; §4 Environment is a tool-and-purpose table (now Snowflake, AWS, FastAPI); add the reason each was chosen over alternatives, and say what is still undecided.; Specs for Goals 1-3 exist in `docs/specs/` but §4 only lists them; summarize requirements and acceptance criteria in proposal.md.; Five figures carry captions only; add prose under each, and design text with rejected alternatives and 'not designed yet'.; No §4 implementation text: the prototype is still the login example. Describe what pages 1-5 will implement, then planned work in paragraphs..

**Merge first** (it doesn't count until it's in `develop` or `main`): PRs #96, #99, #100 (open, main) — review and merge or close; branch sprint-2-review — many commits not in develop; develop is behind main (no specs, figures or §4 text); sync it.

**To do before your Sprint 3 review:**

1. Implement page 1 (upload and extract, #86) in `prototype/` with tests per Goal 1 acceptance criterion; update the README run steps.
2. Add children to stories #13-#15, #18-#21, #23, #25, #26 and give every story an assignee and Sprint milestone.
3. Strip sp: from features #86, #88, #90, #93, #95 and tasks #85, #87, #89, #92, #94, #78.
4. Write §4 spec summaries for Goals 1-3 from `docs/specs/`, and prose under each of the five figures.
5. Add the reason for each §4 tool choice and a design narrative with rejected alternatives and undesigned parts.
6. Link #49 and epics #45, #28, #4 from the proposal; add Closes lines; stop direct pushes to main.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

*A localhost Flask and Leaflet web map of crime incidents, backed by SQLite, with radius search and statistics planned.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Merge release PR #86 so main carries the working map demo, then add tests for `app.py` routes.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ✅ done | 8 of 8 stories have child tasks (#4, #5, #13, #15, #16, #21, #22, #28). Legacy issues #6, #7, #45-#47 have no type label and are not in proposal.md; #45-#47 lack a Sprint milestone.; PRs #37, #39 and #40 (Sprint 2) have no Closes line; Sprint 3 PRs #84, #85, #87 all close an issue.; Release PR #86 (develop to main) carries no Closes line, which is normal for a release.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ✅ done | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. |
| 3. Prototype works | ✅ done | Normalize and load Costa Mesa calls into SQLite; Flask `app.py` serves a Leaflet page and `/api/incidents`; markers highlight when selected. CI: develop 11-14 green (db0cc5c); Install and test (Python) ran, so the team pytest files were collected. main 11-04 green but behind. Tests: Four team test files (normalize, load_db, area_filter, crime_frequency), about 51 tests; none yet for `app.py` routes. |
| 4. Word export (`develop`) | ⚠️ partial | 45 issue citation(s) become small in-text tags; 45 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ✅ ready | Develop runs a map demo from a fresh clone and §0-§4 are written; only main still lags until release PR #86 merges. |

**Proposal, what to write:** §1 Introduction (253 words) and §1.1 (369 words) are short; add per-competitor comparison prose citing matching §8 entries.; §1.2 is 157 words; give each problem its own paragraph tied to a goal.; §4 Design decisions (168 words): name the rejected alternatives, for example SQLite versus a server database.; §4 Implemented modules now covers Goals 1-3, but route and browser tests for filters and radius are still listed as unwritten..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #86 (open, develop to main): Sprint 3 release with the map demo and §4 text; branch 83-update-prototype-readme: 4 commits not in develop.

**To do before your Sprint 3 review:**

1. Merge release PR #86 so main shows the runnable prototype and the finished proposal.
2. Add pytest route tests for `/api/incidents` and `/` in `prototype/` so `app.py` is covered by CI.
3. Build radius selection and filters (#23, #27, #33, #34) with one test per Goal 3 acceptance criterion.
4. Expand §1 and §1.1 with comparison prose on each competitor, citing matching §8 entries.
5. Add rejected alternatives to §4 Design decisions, such as SQLite versus a server database.
6. Close or relabel legacy issues #6, #7 and #45-#47, and decide whether branch 83-update-prototype-readme is still needed.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Merge PR #82 and the feature PRs that already have CI green, then open the develop-to-main release PR.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 7 of 10 stories have child issues (#29-#32, #34-#36); #33, #37, #38 have none yet. Sprint 3 tasks #72-#81, #83, #85-#87 and new #91 are not linked in proposal.md on develop; PR #82 would add them.; #80 carries sp: 1 under story #32; #57 carries sp: 1 under pointed task #55.; Stories #33, #37, #38 have no child issues; #59 hangs off epic #28, not a story.; Six open PRs (#88-#93, #82) and seven unmerged branches hold the Sprint 3 work; nothing merged since 11-03.; PR #20 (old draft) has no Closes line.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a short index of docs, and Planned activities is a long issue table; neither summarizes content.. |
| 3. Prototype works | ✅ done | Vehicle selection: Flask JSON API with SQLite seed data, React/Vite page to pick make, model, year and trim and save a vehicle. CI: develop 11-03 green (f4c1e41): Install and test ran for Node and Python, so API and UI tests executed. main 10-22 green but scaffold. Tests: `prototype/tests/test_vehicle_api.py`, `smoke_test.py` and `tests/ui/vehicle-select.test.js`, plus course `test_login.py` on main. |
| 4. Word export (`develop`) | ⚠️ partial | 40 issue citation(s) become small in-text tags; 40 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | The vehicle-selection prototype runs on develop, but §4 specs and design are index-only, five feature PRs are unmerged, and main is scaffold. |

**Proposal, what to write:** §3 is about 190 words in two short paragraphs; compare alternatives such as Flask versus other stacks, with reasons.; Four specs in `docs/specs/` are only indexed; summarize scope, requirements and acceptance criteria per epic in §4.; Design lacks decisions with rejected alternatives and a not-designed-yet list; `docs/design/architecture.md` is not carried by proposal.md.; No §4 implementation prose: describe the vehicle-selection slice (Flask API, SQLite, React page) and its tests.; §1.2 is 103 words plus a table; write each problem as a paragraph ending in refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prototype and §3-§4; main is still scaffold; PR #82: links Sprint 3 tasks and the vehicle-data spec in §4; PRs #88, #89, #90, #92, #93: service entry form, records API, dashboard, edit/delete, label rule; PR #84 and branch feature/83-claude-md-board-reminder: board reminder in CLAUDE.md.

**To do before your Sprint 3 review:**

1. Review and merge PR #82, then the feature PRs #89, #88, #90, #92, #93, each with CI green.
2. Open the develop-to-main release PR so main shows the prototype and proposal.
3. Remove sp: from #80 and #57; add child issues for stories #33, #37, #38; link #91 in §4.
4. Add §4 implementation prose for the vehicle slice and its tests, ending in typed refs.
5. Summarize the four specs and `docs/design/architecture.md` in §4: requirements, acceptance criteria, decisions, open questions.
6. Expand §3 alternatives and write §1.2 problems as paragraphs.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Fix the failing Run gates job on develop and rewrite `prototype/README.md`, then release develop to main.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 14 stories have child issues; all tasks hang off epics or the proposal task. None of stories #25-#33, #38, #39, #53-#55 has child feature or task issues.; Tasks #56, #9, #8, #7, #5, #4 carry sp: under a pointed parent.; Stories #53, #54, #55 have no assignee; #56 has no Sprint milestone.; #3 is untyped; #71, #67, #64, #59, #56, #51, #46, #45, #42, #5 are not linked in proposal.md; #69 (epic) is cited outside §2.; 14 direct commits on main and develop, including repo restructuring.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Software, Planned Activities and Tracked Task Issues are bullet lists; Specification and Design Documents is a short list of links.. |
| 3. Prototype works | ⚠️ partial | Goal 1 network model on develop: transfer CSV to wallet graph, cycles, metrics and reconciliation checks via `demo.py` on a synthetic sample. CI: develop 11-13 red on Repository harness (Run gates); Prototype build & tests passed with Install and test (Python). main 11-03 red the same way. Tests: 31 team tests in `prototype/goal1-network-model-prototype/tests/` (acceptance and per-requirement); CI collection from `prototype/` unconfirmed. |
| 4. Word export (`develop`) | ⚠️ partial | 31 issue citation(s) become small in-text tags; 30 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A tested Goal 1 demo runs on develop, but §1.1-§1.2 are one sentence, specs and design are only linked, and main has no prototype. |

**Proposal, what to write:** §1.1 is 28 words naming one vendor; write a pros-and-cons table of existing wash-trading detectors plus prose, citing §8.; §1.2 is one 19-word sentence; write each problem statement as a paragraph.; §4 Environment is bullets without reasons; say why Python, scikit-learn and SonarX SQL were chosen over alternatives.; Epic specs and `docs/design/architecture.md` are only linked; summarize them in §4 with decisions and rejected alternatives.; No §4 implementation prose for the new `prototype/goal1-network-model-prototype/`; describe modules and tests..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prototype, Epic 15 spec, design doc and diagrams; main has none and its CI is red; branch feat/69-goal1-network-model-prototype: 2 commits not in develop.

**To do before your Sprint 3 review:**

1. Fix the Run gates failure on develop, then open a develop-to-main PR so main shows the prototype.
2. Rewrite `prototype/README.md` with run and test commands that match `prototype/goal1-network-model-prototype/`.
3. Create child issues under each story (start with #31, #32, #25-#27), each with one assignee and a Sprint milestone.
4. Remove sp: from tasks under #6, #13 and from #56; assign #53-#55; link #71, #67, #64 and the other unlinked tasks in §4.
5. Write §1.1 as a comparison table plus prose and §1.2 as problem paragraphs; cite sources in §8.
6. Carry spec, design and implementation summaries into §4 as paragraphs; stop direct commits to main and develop.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5 Guys: Marathon Tracker

*Phone app records a marathon runner's GPS to Firebase; spectators follow on a web page; pace and finish-time prediction.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Build the spectator view (#69) so the review demo shows a phone's GPS position reaching a web page through Firestore.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 6 stories have child issues (#28-#33); 45 of 48 issues linked from the proposal. #62 (task under story #28) carries `sp: 3`; points belong on the story only, so story #28 is double counted.; PR #39 closes #21, which `proposal/proposal.md` does not link.; Open stories #28, #29, #30, #31, #33 and all Sprint 4 features have no merged PR yet; the Sprint 3 milestone is past due (11/11).; #1, #2, #6 are untyped and not in the proposal; #1 and #6 have no assignee (old Sprint 1 leftovers).; Tasks #58, #60, #65, #72 hang off no story; fine as process tasks, but #62 and #64 are the only prototype tasks under #28.. |
| 2. Proposal §0–§4 (`main`, ≈ 9 pages) | ⚠️ partial | ⚠️ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ⚠️ §2 Goals · ⚠️ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; the specs and design docs stay in `docs/` and the proposal carries only one Goal 3 paragraph.. |
| 3. Prototype works | ✅ done | Expo app with Firebase client, runner GPS tracking module (`runner-app/tracking.js`), Firestore smoke test, and pace calculation (`prediction/pace.py`). Spectator view is only a README placeholder. CI: main CI green 11/12 (720486b); Prototype job ran Node install and test (jest) and Python install and test; "Nothing to build" was skipped. develop is stale, still the login scaffold. Tests: 3 test files: `__tests__/App.test.js`, `__tests__/tracking.test.js` (jest) and `prediction/test_pace.py` (pace maths); all run in CI. |
| 4. Word export (`main`) | ⚠️ partial | 50 issue citation(s) become small in-text tags; 45 issue(s) fill 4 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A phone-GPS-to-Firestore demo and pace test can run, but §4 is incomplete and the spectator view (#69) that ties it together is not built. |

**Proposal, what to write:** §0 Abstract describes an ML performance-analysis app; the goals are live tracking, posts and a spectator page. Rewrite it to match §2.; §1 and §1.1 still hold template quote blocks and a stray 〈Your survey〉 placeholder; §1.1 ends mid-sentence ("our") and has a duplicated table cell.; §4 has no Environment and resources section: tech-stack reasons (Expo, Firebase, Mapbox, Python) appear only as one paragraph under Planned activities (#48, #72).; §4 specs: only Goal 3 is summarized; add scope, requirements, acceptance criteria and open questions for Goals 1 and 2 (#70, #73) from `docs/specs/`.; §4 design: carry the components, data model, key decisions with rejected alternatives and 'not designed yet' from `docs/design/architecture.md` and `data-model.md` into the proposal.; §4 implementation reads as a setup tutorial and says "we plan to use" for GPS and spectator code that already exists; describe what `tracking.js` and `pace.py` do..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - stale, holds only the login scaffold; later PRs targeting it never reached main's prototype.

**To do before your Sprint 3 review:**

1. Build the spectator view (#69) in `prototype/spectator-view/` so the demo shows a runner position on a page end to end.
2. Add an Environment and resources subsection to §4 with one reason per tool (Expo, Firebase Firestore, Mapbox, Python); cite #48 and #72.
3. Summarize the Goal 1 and Goal 2 specs in §4 and complete the Goal 3 summary; finish #70, then link each spec's acceptance criteria to a test.
4. Move the data model, architecture and key decisions (with rejected alternatives) from `docs/design/` into §4 prose, each paragraph ending with issue refs.
5. Rewrite §0 Abstract so it matches Goals 1-3; fix §1.1 ending, remove 〈…〉 placeholders and template quote blocks in §0-§4.
6. Remove `sp: 3` from #62, close or type #1, #2, #6, and refresh `prototype/README.md` run steps.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Python app that finds signal peaks in 6G captures, classifies waveform and modulation, and explains the decision.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Merge develop into main today so the review shows the real prototype and proposal from the default branch.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 12 of 18 stories have child issues; #63, #67, #69, #70, #71, #84 have none. Stories #63, #67, #69, #70, #71, #84 have no child feature, task or sub-task.; 21 issues are not in proposal.md on develop, including new tasks #147-#162 and #95, #103.; Stories #63, #70, #71 have no assignee or Sprint milestone; #103 is untyped.; §4 still cites stories (#66, #68, #84, #111, #126) that belong only in §2; 14 misplaced refs.; One direct commit on develop; PRs #1, #2 (old) have no issue.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. |
| 3. Prototype works | ✅ done | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, Captum attribution and a new transformer AMC module. CI: develop 11-13 green (2719a5c); Prototype job ran Install and test (Python) on team code. main is 10-16 scaffold. Tests: 14 test files in `prototype/tests/`: peak pickers, channelizer, calibration, attribution, CLI, pipeline gate, OFDM, training, transformer. |
| 4. Word export (`develop`) | ⚠️ partial | 70 issue citation(s) become small in-text tags; 54 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The peak-picker and classifier demo runs from develop, but §4 lacks Environment detail and Implementation, and main still shows the scaffold. |

**Proposal, what to write:** §4 Environment and resources is 28 words with template placeholders; give each tool (MATLAB, Python, Captum, dataset) and the reason it was chosen.; Only two specs (application architecture, waveform family) for five epics; Goals 1, 4 and 5 need scope, requirements, acceptance criteria and open questions.; No §4 implementation section for `waveform_identification/`, `xai/`, `GUI/` and `modulation_classification/`; add paragraphs ending in task refs.; §1.1 has four prose subsections but no pros-and-cons table or prose on what this project does differently.; §1.2 states P1-P3 in about 50 words; explain why each matters and tie it to a goal. No planned-activities prose exists..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop: holds the real prototype and §4 work; main is the login scaffold, promote it; PRs #151, #153 (open): Sprint 2 review notes and Word export converter; branches Application-Structure, docs/team-documentation, docs/150-sprint-2-review, docs/152-word-export: commits not in develop.

**To do before your Sprint 3 review:**

1. Open and merge a develop-to-main PR so `prototype/` and `proposal/proposal.md` on main are current; keep main CI green.
2. Link #147-#162 and #95 in §4 as typed refs, and move story refs out of §4 into §2.
3. Create child issues for stories #63, #67, #69, #70, #71, #84; assign one person and a Sprint milestone to each.
4. Replace the §4 Environment placeholder with each tool and why it was chosen, ending paragraphs with task refs.
5. Write a §4 Implementation section for the four prototype packages and planned-activities prose for the remaining work.
6. Add short specs for Goals 1, 4 and 5, and a §1.1 pros-and-cons table with prose on what differs.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Merge release PR #140, then rewrite `prototype/README.md` and rename the test file so CI exercises the app.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#19-#27 via features #53-#102 and tasks #55-#106). Only 22 of 101 issues are closed; tasks #56, #57, #61, #62 have open PRs (#144, #145, #147, #148) not yet merged.; Tasks #91-#106 and stories #25-#27 have no Sprint milestone.; #139, #125 (3 assignees), #126, #123, #122, #61 (2), #111 (4) break one-assignee-per-issue.; 21 issues are not in proposal.md, including #141, #142, #131, #124, #113, #107; refs like `taskL#127` and empty links are malformed.; PR #117 closed without Closes; older PRs #1, #3, #4, #9, #36 lack issues.. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned Activities is a 17-row issue table (12 link rows) plus short per-item lines; it carries no explanatory prose of its own.. |
| 3. Prototype works | ⚠️ partial | `A.M.I.Y.A.core/` has app, database, models and assignment and deadline services; the Electron/Vite UI now has a task modal and GUI (#143). CI: develop 11-14 green (bc61f02), but the Prototype job ran only the Python step and cannot collect `TestAssignments.py`; the UI `package.json` sits in a subfolder, so Node was skipped. Tests: One file, `A.M.I.Y.A.core/tests/TestAssignments.py`; its name does not match pytest discovery, so CI does not run it. |
| 4. Word export (`develop`) | ✅ done | 99 issue citation(s) become small in-text tags; 80 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Wireframes and specs are showable, but `prototype/README.md` is still the login scaffold, there are no run steps, and CI proves nothing about the app. |

**Proposal, what to write:** Merge-conflict markers are gone from `proposal/proposal.md`; the Planned Activities table still has malformed refs such as `taskL#127` and empty links.; §1.1 has a pros-and-cons table but no prose arguing what A.M.I.Y.A. does differently; add it, citing §8.; §4 Environment describes Python and JavaScript but gives no reason per tool and names no data store or hosting.; §4 specs are short summaries linking `docs/specs/specs-G1.md`; carry scope, requirements, acceptance criteria and open questions into the proposal.; §4 design is wireframes only (Diagrams section); add system context, components, data model, data flow and decisions with rejected alternatives..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #140 (open, develop to main): release of the proposal and prototype to main; PRs #144, #145, #147, #148 (open): form validation, local data, edit/delete, confirmation; branches task/111-specification-details, task/122-high-level-architecture-diagram: unmerged commits.

**To do before your Sprint 3 review:**

1. Merge PR #140 so main carries the current proposal and prototype, and keep main CI green.
2. Rewrite `prototype/README.md` with install, run and test commands for the core and the UI.
3. Rename `TestAssignments.py` to `test_assignments.py` and add tests for deadline suggestion and CRUD, one per acceptance criterion in `docs/specs/specs-G1.md`.
4. Merge task PRs #144, #145, #147, #148 with `Closes #N` and close the issues the prototype already implements.
5. Add Sprint milestones to #91-#106, one assignee per issue, and fix malformed refs in the Planned Activities table.
6. Write §4 Environment with a reason per tool, an Implementation section, and carry specs and the ER design into §4 prose.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Add Sprint milestones to the 40 new Sprint 4 child issues (#136-#175) so every child has one assignee and a milestone.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 18 of 18 stories have child issues (feature, task, sub-task); epics #22 and #23 sit above them. Forty Sprint 4 children #136-#175 have no Sprint milestone; #114, #115, #44-#47 also lack one.; `sp:` remains on #99, a task under story #25; points belong on the story only.; #112, #113, #88 have no assignee; #79, #80, #81, #44, #45 have several.; 9 direct commits each on main and develop (e.g. 118e0ed adding Sprint 3 tasks); use a branch and PR with `Closes #N`.; PR #50 (Goal 2 spec) has no issue; #91 and #92 are cited as plain links, not typed refs.; §4 cites story #24 and §1 cites task #113; stories belong in §2 only, work items in §4.. |
| 2. Proposal §0–§4 (`develop`, ≈ 11 pages) | ✅ done | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" opens with an 11-row link table, but each document then gets a prose summary; planned activities are prose paragraphs with refs.. |
| 3. Prototype works | ✅ done | PySide6 start menu loads a sample or JSON scenario validated by Pydantic; user browses, creates and deletes simulated files in memory; optional Ollama generator script. CI: main green 11/12 (ec16018), develop green 11/12 (2a0c3b8); Prototype job ran Install and test (Python) on team code, and CI fails if no tests are collected. Tests: 5 test files in `prototype/tests/`: scenario model, loader, simulation engine, scenario generator, UI (Qt offscreen). |
| 4. Word export (`develop`) | ✅ done | 176 issue citation(s) become small in-text tags; 119 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ✅ ready | Proposal §0-§4 is written on develop and the PySide6 slice runs from a clean clone with README steps and green CI. |

**Proposal, what to write:** §3 still says 'Sprint 2 priorities' and 'prototype skeleton'; rewrite it to describe what the prototype implements now and what Sprint 4 adds.; §4 spec summaries name requirements and acceptance criteria but give few figures; state the main FR and NFR for Goals 1 and 2 explicitly.; §1.2 has spelling errors ("Acceess", "exercuses", "witht he"); proofread, and write §2 objectives as sentences, not a 20-line bullet list.; §4 implementation covers `ui/`, `sim/`, `scenario/`; add a sentence per layer on tests and on what each acceptance criterion checks..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - holds the fuller proposal (57k chars vs 50k on main) and 40 new issues; promote it to main.

**To do before your Sprint 3 review:**

1. Add a Sprint milestone to #136-#175, #114 and #115, and assign #112, #113 and #88 one owner each.
2. Remove `sp:` from #99 and move the points to story #25 if needed; keep points on stories only.
3. Stop direct commits to main and develop: open a branch and PR with `Closes #N` for every proposal edit, including Sprint 4 task additions.
4. Rewrite §3 (still 'Sprint 2 priorities') to match the PySide6 prototype and Sprint 4 plan.
5. Add explicit FR, NFR and acceptance-criteria sentences to the §4 summaries of `training-environment.md` and `ai-scenarios.md`.
6. Build the process, log and network views (#139, #143, #105) with a test per acceptance criterion before the review.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Write the §4 Design subsection from `docs/design/architecture.md`; it is the largest missing piece and the diagram and CMake build already exist.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 8 stories have child issues (#30, #31, #32, #33); #26-#29 have none. Stories #26, #27, #28, #29 (game demo) have no child feature, task or sub-task.; `proposal/proposal.md` has 0 typed refs: 36 bare `#N` cells and malformed `[story:https://...]` parents in the §4 table.; #46 is parented to story #32 yet carries `sp: 2`; #46's table row names itself as its own parent.; #76, #78, #82, #43 and epic #6 are not in the proposal; #43 has no milestone; #44 has no assignee.; Stories #26-#33 each have 2 assignees; one assignee per issue.; 4 early direct commits on main; PRs #3, #4, #5, #41 have no issue (old).. |
| 2. Proposal §0–§4 (`main`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 4-row link table; "Planned activities" is a 38-row table of issues, owners and sprints with no prose; §1.2 sits in a table.. |
| 3. Prototype works | ✅ done | CMake project (SDL3, Assimp, ImGui, GLM) with ECS core, transform and mesh components, renderer and model loader headers, shaders; README gives build, run and test commands. CI: main green 11/13 (43fce39) and develop green 11/14 (c80ac06); Prototype job detected CMake, installed graphics libraries, configured, built C++ and ran Tests (CMake). Tests: README names target `test_engine_components` (basic ECS checks); test sources not visible in the sweep's file list. |
| 4. Word export (`main`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 25 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | CMake build and ECS test run green in CI, but §4 is tables and links with no design or implementation prose, so the proposal half is not ready. |

**Proposal, what to write:** §4 specs: summarize `docs/specs/game-engine.md` and `game-demo.md` in prose (scope, FR/NFR, acceptance criteria, open questions); today only the file names appear.; §4 design: write components, data model (entities, components, systems), data flow and key decisions with rejected alternatives from `docs/design/architecture.md`.; §4 diagrams: Figures 1 and 2 have captions but no paragraph explaining them; add one per figure.; §4 environment is one line per tool; explain why SDL3, Assimp, ImGui and C++26 suit old hardware, and name the test machines.; §4 has no implementation section: describe `prototype/include/engine/` and `demo/` and what runs, citing #63, #66, #67, #82..

**To do before your Sprint 3 review:**

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

**Start here:** Write the Goal 2 spec summary in §4 from `docs/specs/goal-2-detection.md`, ending with its issue refs; then repeat for Goal 3 and the design.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 9 stories have child issues (#14, #15, #17, #18, #20); #5, #16, #19, #21 have none. About 22 tasks (#22-#95, #101) have no parent story; most carry their own sp:, so story points are counted outside any story.; #19 and #21 (Sprint 4 stories) and #16 have no child tasks; #14 has three, #17 and #18 one each.; PRs #75 and #35 have no `Closes #N`; PR #44 closes #42, which the proposal does not cite.; Three direct `docs:` commits on main and develop (team details), outside any PR.; #28 (first questions to the SonarX mentor) is still open in Sprint 3 and has no parent.. |
| 2. Proposal §0–§4 (`develop`, ≈ 17 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: Table 9 lists the three specs and the design doc as file paths with issue refs; the D1-D6 list links out to `docs/design/architecture.md` with one- or two-line captions.. |
| 3. Prototype works | ✅ done | Detector, SQLite store, live Ethereum poller, replay of five past hacks, false-alarm evaluation, Slack notifier, FastAPI API, web dashboard, demo mode, Dockerfile. CI: develop 60745cb (Nov 11) green; Prototype job ran 'Install and test (Python)', so team tests executed. main run Nov 3 also green. Tests: Four files in `prototype/tests/`: detector, live loop, baseline check, data pipeline; proposal reports sixty tests. |
| 4. Word export (`develop`) | ✅ done | 59 issue citation(s) become small in-text tags; 46 issue(s) fill 4 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | The prototype runs in live, demo and replay modes and could be shown; §4 lacks Goal 2 and 3 spec summaries and design prose. |

**Proposal, what to write:** §4 specs: only the Goal 1 spec is summarized in prose (requirements, acceptance criteria, open questions); add the same for Goals 2 and 3 from `docs/specs/`.; §4 design: `docs/design/architecture.md` is not carried; write context, components, data model, data flow, key decisions with rejected alternatives, and undesigned parts in prose.; §4 diagrams D1-D6 get a short caption each but no explaining paragraph; Figures 1 and 2 are the planned design, not the built one.; The implementation-details subsection is now real prose for each module; add the replay and false-alarm results once #97 and #98 are done..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #103 — proposes the hosting target in Table 6 (develop); develop to main — implementation details, Goal 1 spec summary and Sprint 3 tasks are not on main.

**To do before your Sprint 3 review:**

1. Summarize the Goal 2 and Goal 3 specs in §4 (scope, requirements, acceptance criteria, open questions) from `docs/specs/goal-2-detection.md` and `goal-3-dashboard.md`.
2. Write the design subsection in §4 from `docs/design/architecture.md`, including rejected alternatives and what is not designed yet.
3. Add a paragraph after each of D1-D6 explaining the diagram, and label Figures 1 and 2 as planned versus built.
4. Run the five-hack replay and false-alarm weeks (#97, #98) and write the numbers into §4 against Objectives 2.2 and 2.3.
5. Parent the standalone doc tasks to a story and add child tasks under #19 and #21 before Sprint 4.
6. Merge PR #103 and release develop to main so the graded branch holds the current paper and prototype.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape, galaxy-style music discovery map with swipe feedback

*A game-like map of genres, artists and songs where swipes steer personalized music discovery.* · Sprint 3: Nov 5 – 18 · **Sprint 3 review Thu Nov 19** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Open the failing 'Run gates' step on main, fix it, then build one running slice in `prototype/` with a test; that unlocks a demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 6 stories have child issues (#25, #29, #30); #26, #27, #28 have none. `sp:` on tasks #41, #42, #43, #49, #55, #57 under stories, and on #51 under pointed task #47.; #41, #49, #51, #55, #57, #58, #59 are not linked from the proposal.; #49 and #55 have no assignee.; 16 merged PRs (e.g. #31-#39, #45) have no `Closes #N`; main has 30 direct commits.; Tasks #46, #47, #53 hang under epic #21, not a story; open PRs #60 and #61 are not merged.. |
| 2. Proposal §0–§4 (`main`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1, §1.2, the §4 environment table, the spec and design document table and 'Planned activities' (7 rows) are tables; no prose carries the issue refs.. |
| 3. Prototype works | ❌ skeleton | Empty module skeleton: `backend/lastfm.py`, `database/db.py`, `schema.sql`, `main.py`; README says there is no current code to run. CI: main (11/6, 12278fb) red: Repository harness failed at 'Run gates'; Prototype job green but no team tests exist. develop green 11/2. Tests: none; no `prototype/tests/` folder although the README claims four tests |
| 4. Word export (`main`) | ✅ done | 14 issue citation(s) become small in-text tags; 14 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | No running prototype exists, main CI is red on the harness gate, and §4 has no spec, design or implementation prose. |

**Proposal, what to write:** §1.1 is a six-row table with no prose; add paragraphs on what SonicScape does differently, with citations matching §8.; §1.2 is a table and §2 is nine bullets; write problem statements and explain each epic and story in paragraphs ending in refs.; §4 specs: summarize `docs/specs/specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` (scope, FR/NFR, acceptance criteria, open questions).; §4 diagram sections hold 5 to 84 words each; the data flow and screen flow diagrams have no explaining prose.; §4 has no implementation details; planned activities list seven Sprint 2 rows, with no Sprint 3 or 4 work..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #60 - §4 environment table description, open, closes its task; PR #61 - data flow diagram description for §4, open, closes its task; develop branch - stale scaffold with a different title; align it with main or retire it.

**To do before your Sprint 3 review:**

1. Open the failing 'Run gates' step on main, fix what it names, and get CI green.
2. Build the first end-to-end slice in `prototype/` (Last.fm into SQLite, one galaxy view, one swipe) with a test per acceptance criterion in `prototype/tests/`.
3. Replace the README run line with commands that work from a fresh clone, and drop the claim of four tests until they exist.
4. Merge PRs #60 and #61, then write §1.1 and §1.2 as prose and add a paragraph per goal and objective in §2 ending with typed refs.
5. Summarize `specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` in §4, then add a caption and paragraph for each diagram.
6. Link #41, #49, #51, #55, #57-#59 in §4, remove `sp:` from child tasks, and create Sprint 3 child issues under #26-#28.

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

**Start here:** Write the §4 design document with embedded diagrams (task #64); the context and monster state diagrams already exist on main.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 8 stories have child issues (#13, #18, #19, #20, #22); #14, #15, #23 have none. Goals #12, #17, #21 are epics but cited as [story:#N] in §2; PR #70 (open) would fix this.; 16 issues not in §4: #11, #24-#28, #34, #35, #37, #54, #55, #57, #64-#68.; Features #39-#52 appear as bare `Task [#N]`, not typed refs; 14 bare refs in total.; Tasks #28, #41, #54, #55, #64 carry `sp:` but hang under epic #12, not a story; #54 and #55 have two assignees.; PR #5 has no `Closes #N`; one scaffold direct commit on main.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 16-row link table with no prose; the spec table keeps template rows beside the three real specs.. |
| 3. Prototype works | ⚠️ partial | Unreal Engine 5 first-person starter project (`Config/`, `Content/`, `Insomnia.uproject`); PR #69 adds sprint and crouch movement on develop (binary assets, not verifiable here). CI: main green 11/6 (4235cfb) and develop green 11/13 (a88a416), but the Prototype job ran only 'Nothing to build'; CI does not exercise the Unreal project. Tests: none; README describes a manual smoke test only |
| 4. Word export (`develop`) | ⚠️ partial | 25 issue citation(s) become small in-text tags; 25 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The starter level with sprint and crouch should run per the README, but there is no monster or maze yet, and §4 design and diagrams are not in the proposal. |

**Proposal, what to write:** §1.1 has prose on three games but no pros-and-cons table; add one across Visage, MADiSON and Phasmophobia (task #68).; §4 specs: three files in `docs/specs/` are indexed but only briefly summarized; give scope, requirements, acceptance criteria and open questions per epic.; §4 design is absent: write context, components (monster AI, director, audio), data flow, decisions with rejected alternatives and undesigned parts (task #64).; Diagram sources `docs/design/*.mmd` exist on main only and are not in the proposal; embed each with a caption and prose.; §4 has no implementation details and no prose on remaining work; describe the starter project and each Sprint 3 feature group..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #70 - corrects epic refs in §2, open against develop; branch feature/67-cite-epics - 1 commit not in develop; develop to main - main §3 is still the template and trails develop; docs/design/*.mmd diagrams are on main only; bring to develop and into the proposal.

**To do before your Sprint 3 review:**

1. Write the §4 design subsection from task #64: context, components, state model, decisions with rejected alternatives; embed `docs/design/*.mmd` diagrams with captions.
2. Merge PR #70, make #39-#52 typed refs, and add #11, #24-#28, #34, #35, #37, #54, #55, #57, #64-#68 to §4.
3. Add a pros-and-cons related-work table across the three games (task #68) and tie it to the references.
4. Build the first playable slice (maze, patrol monster) with one test per acceptance criterion in each spec.
5. Create child issues under #14, #15, #23; hang tasks #28, #41, #54, #55, #64 under stories and remove `sp:`.
6. Delete the 〈…〉 template rows in §4 and merge develop into main.

[↑ Back to all groups](#groups)

## About this page

The Sprint 2 checklist (specs, design, environment, prototype wiring) is now folded into rule 2 (§4) and rule 3. The earlier editions, including the Sprint 2 cards, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
