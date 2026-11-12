# Group repository status: Sprint 3 readiness (proposal §0–§4 and a working prototype)

> [!IMPORTANT]
> **New (Nov 8): this page now checks Sprint 3 readiness.** At your Sprint 3 review, which is the meeting that starts Sprint 4, I expect two things: **your proposal complete from the beginning through §4**, and **a working prototype you can demo**. This page checks your repository against the three rules of thumb from my Oct 31 email. It is a readiness check, not your sprint grade; the five rubric lenses are graded separately. Find your group's card below: it says what's missing and what to do, in order.

**CPSC 490 · Fall 2026 · swept 2026-11-12 20:22 UTC.** Earlier editions are kept in this file's git history.

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
| [G03](#g03) California | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G04](#g04) Epic Engineers | Tue Nov 10 | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 33 |
| [G05](#g05) Fighting Mongooses | Tue Nov 10 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 5 |
| [G06](#g06) GapWise | Tue Nov 17 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G07](#g07) Mighty Morphins | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 8 |
| [G08](#g08) Crime Busters | Tue Nov 17 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ≈ 8 |
| [G09](#g09) Sigma Squad | Tue Nov 17 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 10 |
| [G10](#g10) Team Jiddak | Tue Nov 17 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ | ≈ 5 |
| [G11](#g11) 5 Guys | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G12](#g12) ACJMM | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ≈ 9 |
| [G13](#g13) BYKX | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 9 |
| [G14](#g14) Cyber Squad | Thu Nov 12 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ≈ 10 |
| [G15](#g15) HIBBI-01 | Thu Nov 12 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |
| [G16](#g16) G16 | Thu Nov 19 | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ≈ 17 |
| [G17](#g17) G17 | Thu Nov 19 | ⚠️ | ⚠️ | ❌ | ✅ | ❌ | ≈ 5 |
| [G18](#g18) G18 | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ≈ 8 |
| [G19](#g19) Titan Security | Thu Nov 19 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ | ≈ 5 |
| [G20](#g20) Solos | Thu Nov 19 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ≈ 6 |

- **Rule 1 met:** 1 of 20 (G04).
- **Proposal §0–§4 complete:** 1 of 20 (G08).
- **Prototype working, with a real slice and tests:** 10 of 20 (G01, G02, G03, G04, G05, G09, G11, G12, G14, G16).
- **Ready to demo both today:** 1 of 20 (G14).

**What changed since the Nov 5 edition:**

- **G14 is the first group I would call demo-ready.** Since Nov 10 it went from no broken-down stories and a skeleton prototype to five stories with child issues, a running desktop slice with five test files that CI runs, and a §4 with eleven figures. Its rule 3 mark is now ✅.
- **G11's prototype now passes rule 3:** CI on `main` runs the team's own tests, and §4 gained diagrams and planned-activities prose. The spectator view is still open, so the demo has no end-to-end path yet.
- **Proposal writing moved for G06 and G08.** G06's `develop` now has rewritten §0–§3 and an environment table (rule 2 went from skeleton to partial). G08's §4 now carries per-goal requirements, implemented modules, design decisions and five figures, and it is the first group with a ✅ on rule 2.
- **More groups are breaking stories down:** G09 (7 of 10 stories), G14 (5 of 18), G15 (4), and G20 listed its features in §4. Only G04 has the whole chain complete.
- **Also moved:** G07 (three spec documents and five figures on `main`), G10 (a spec, a design document and five diagrams on `develop`), G12 (four captioned figures and a waveform-family spec and design), G13 (three goal specs, wireframes and ER diagrams on `develop`), G16 (a Goal 1 spec summary and implementation details in §4).
- **No change since Nov 10:** G03, G04, G05, G18 and G19. G01 and G17 filed new issues but the proposal and prototype did not move.
- **Check before your review:** G13's `proposal/proposal.md` on `develop` has unresolved merge-conflict markers in §4. For G13, G15 and G20 the prototype job is green without building or testing team code. Several groups (G02, G05, G06, G09, G12, G13, G15, G16, G20) still keep finished work on `develop` only: merge it to `main`.
- **Review dates:** G11–G15 Thu Nov 12, G06–G10 Tue Nov 17, G16–G20 Thu Nov 19. G01–G05 had theirs on Tue Nov 10.

<a name="groups" id="groups"></a>

## Your group

Each card covers the three rules, using the best of `main` and `develop` (the branch is named), and ends with a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and strategy backtesting

*Rebuild Hyperliquid's order book from SonarX data, validate it, and backtest strategies only on validated days.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Build the replay engine (#144, #145) in `prototype/src/bgaf_pipeline/replay.py` with tests; it is the slice every later step and the demo depend on.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 14 of 15 stories have child issues (#58, closed, has none); 7 stories (#23-#28, #279) are still open. Eleven tasks carry `sp:` under a story or pointed task (double counting): #195, #187, #184, #183, #181, #180, #175, #174, #173, #172, #134.; 47 issues (#279-#325, the Sprint 4 plan and prototype tasks) are not linked from the proposal; PR #326 is open to add them.; 93 epic/story citations sit in §4 instead of §2 only; #151 is cited as a task but is a sub-task.; 23 child issues lack exactly one assignee (#202, #187, #169, #167, #166, #165, #164, #163, #159, #158, #157, #151, #148, #147, #145, #144 ...).; 33 tasks have no parent (#271, #264, #249, #232, #231, #206 ...); PR #126 and early PRs lack `Closes #N`; three direct commits on main.. |
| 2. Proposal §0–§4 (`main`, ≈ 82 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ✅ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: None in place of prose; §4 is paragraphs ending in refs. A small link table remains in the specification index only.. |
| 3. Prototype works | ✅ done | DuckDB schema and a SonarX L2 snapshot loader (`storage.py`); replay, validate, gate, backtest and report modules are docstring stubs; front end is the Vite starter. CI: Latest main run green; Prototype job ran Python install and pytest. Node steps skipped, so the Vite front end in `prototype/frontend` is not built in CI. Tests: `prototype/tests/test_package.py` (step layout) and `test_storage.py` (schema, load, exact decimals, repeat load). |
| 4. Word export (`main`) | ✅ done | 665 issue citation(s) become small in-text tags; 164 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | §0-§4 can be presented now; the prototype only loads one snapshot file into DuckDB, with replay, validation and backtest not yet built. |

**Proposal, what to write:** §1.2 Problem Statements is 233 words and a two-row table; expand into full paragraphs for P1 and P2 with the evidence behind each.; Dedicated validation-and-gate and replay-engine designs (#260-#262, open) are not in §4; the module design only summarizes them at contract level.; §4 holds about 16,000 words of spec and design prose, but 93 epic/story links belong in §2; move them (#278).; Planned activities mix old and new work; mark what is done, in progress and left so the remaining work is clear..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #326 — links Objective 2.6 and the Nov 10 prototype tasks in the proposal; Branch 58-cite-dropped-objective-main — 34 commits not in develop; merge or delete; Branches 18-abstract-intro, 43-update-goals-and-objectives — stale, delete.

**To do before your Sprint 3 review:**

1. Merge PR #326 so #279-#325 are cited in §4, with prose paragraphs rather than a list.
2. Remove `sp:` from #195, #187, #184, #183, #181, #180, #175, #174, #173, #172 and #134; points stay on the user story only.
3. Assign exactly one person to #202, #187, #169, #167-#163, #159-#157, #151, #148, #147, #145, #144.
4. Implement the replay engine (#144, #145) and the Sprint 4 backtest tasks #311-#325 with one test per acceptance criterion.
5. Add a CI step that installs and builds `prototype/frontend` so the front end is exercised.
6. Expand §1.2 into a paragraph per problem statement ending in issue refs.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, stored and shown on a dashboard to identify recording devices.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Write the Goal 1 specification (scope, requirements, acceptance criteria, open questions) in `docs/specs/` and summarize it in §4; specs are the biggest missing piece.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 15 stories have child issues (#16, #45, #46, #48, #57); 10 stories (#49, #51-#55, #58-#61) have none. Ten of 15 user stories have no child issues; break each into feature, task, sub-task on the board.; 21 children carry `sp:` under a story (double counting): #95, #92, #91, #86, #84, #81, #77, #69, #68, #41 ...; 18 child issues lack exactly one assignee (#101, #72, #70, #68, #67, #41, #39, #38, #36, #25 ...); five meeting issues have no type label.; #130 and #99 (sprint reviews) and epic #20 are not linked from the proposal; some epic/story refs sit in §3.; Eight direct commits on develop and one on main; PRs #3, #4, #5, #14 lack `Closes #N`; #127 and #131 still open.. |
| 2. Proposal §0–§4 (`develop`, ≈ 15 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §2 uses bullets with refs; §4 'Specification and design documents' is still a template comment plus a 4-row table with no spec or design prose.. |
| 3. Prototype works | ✅ done | FastAPI `/health`, `/health/db`, POST/GET `/observations` on PostgreSQL via Compose; Angular starter page; ESP32 firmware is a skeleton with no capture yet. CI: Latest develop run green; Prototype job ran Python install and pytest on the backend. Angular and ESP32 projects are not built in CI; main run is also green but older. Tests: `test_main.py`, `test_observations.py`, `test_observation_model.py` (19 cases, in-memory SQLite); Angular `app.spec.ts` not run in CI. |
| 4. Word export (`develop`) | ⚠️ partial | 122 issue citation(s) become small in-text tags; 74 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | Backend ingest and query can be demoed; no live ESP32 capture or dashboard data, and §4 specs, design and implementation are not written. |

**Proposal, what to write:** §4 Specifications: no spec per epic exists; `docs/specs/` holds only the scaffold example. Write scope, FRs, NFRs, acceptance criteria and open questions for Goals 1-3.; §4 Design: `docs/design/architecture.md`, `data-flow.md`, `system-context.md` exist but §4 carries only figures; summarize components, data model, decisions with rejected alternatives, and what is undesigned.; §4 Implementation details is absent; describe the backend API, PostgreSQL tables, ESP32 firmware and dashboard as built, with task refs.; §1.1 is one table plus a short paragraph; §1.2 is 215 words. Main still holds the unfilled template for §3 and §4..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — §3, §4 environment and planned activities, observation API; merge into main; PR #127 — restart-persistence test for stored observations; PR #131 — Sprint 3 review (#130).

**To do before your Sprint 3 review:**

1. Write one spec per epic (#47, #50, #56) in `docs/specs/` and summarize each in §4 with scope, FRs, NFRs, acceptance criteria, open questions.
2. Summarize `docs/design/architecture.md`, `data-flow.md` and `system-context.md` in §4 with decisions, rejected alternatives and undesigned parts.
3. Add a §4 'Implementation' subsection describing the backend, database, firmware and dashboard as built, ending each paragraph in task refs.
4. Create child issues under stories #49, #51-#55, #58-#61; remove `sp:` from the 21 listed children.
5. Merge PRs #127 and #131, then merge develop into main so main matches the work.
6. Connect the ESP32 to POST `/observations` and render it in the dashboard for the demo.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Transcribe a handwritten equation, generate code and a training dataset, and train a model in a notebook.* · Sprint 3: Oct 27 – Nov 9 · **Sprint 3 review Tue Nov 10** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Rewrite `prototype/README.md` so a fresh clone can run the pipeline and tests; then fill the §4 environment section.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 2 of 13 stories have child issues (#50 has #69, #70; #46 has #78); 11 stories, 9 still open, have none. Eleven of 13 user stories have no child issues; break each into feature, task, sub-task on the board.; 25 issues are not in the proposal (#78, #72, #71, #70, #69, #65, #60, #51, #41 ...); 18 issues carry no type label (meetings, writing tasks).; Eight issues have no assignee and ten have no Sprint milestone (#75, #68, #55, #53, #42, #41, #24, #20, #2, #1).; PRs #81 and #77 (Sprint 3) have no `Closes #N`; PR #83 is open; one direct commit on main and develop.; Six refs are bare or point at the wrong issue number (story #31 links to issue 30); only 12 of 18 refs are typed.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ❌ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ❌ §4 Planned activities. Link tables in place of prose: §2 is a bullet list with refs; §4 'Specification and design documents' and 'Planned activities' are small tables, not prose; §4 opens with the unfilled template prompt.. |
| 3. Prototype works | ✅ done | Transcriber router and recognizer, verifier, dataset generation, storage and display, PyTorch training, equation plotting, and a pipeline notebook. CI: Latest develop run green; Prototype job ran Python install and pytest on team code. Main CI is green but from Oct 27, before most of the prototype landed. Tests: `tests/` has transcriber, recognize, verifier, pipeline, train and plot_equation tests; none named for dataset generate, store or display. |
| 4. Word export (`develop`) | ⚠️ partial | 18 issue citation(s) become small in-text tags; 18 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The prototype pipeline is demoable from develop, but §4 is mostly missing and the README run steps do not work. |

**Proposal, what to write:** §4 Environment and resources is still the template prompt; name each tool, platform, hosting and the sponsor's notebook requirement with the reason.; §4 Specifications: `docs/specs/transcription.md`, `data-generation.md`, `workbook-generation.md` exist but are only indexed; summarize each with FRs, NFRs, acceptance criteria.; §4 Design: `docs/design/architecture.md` gets one paragraph; add data model, key decisions with rejected alternatives, and what is undesigned.; §4 Implementation and Planned activities hold a 3-row table; describe the built transcriber, verifier, trainer and the remaining work in prose with refs.; §1 Introduction is 307 words and §1.2 is 49 words with a placeholder; both need real paragraphs..

**Merge first** (it doesn't count until it's in `develop` or `main`): Branch develop — transcriber, recognizer, training, plotting, notebook, spec drafts; main still at Oct 27; PR #83 — plotting test data (feature/47-plot-test-data).

**To do before your Sprint 3 review:**

1. Merge develop into main so the CI-checked prototype and proposal are on the default branch.
2. Rewrite `prototype/README.md` with the real run and test commands; remove the `login.py` text.
3. Fill §4 Environment and resources with each tool, API, hosting choice and the reason.
4. Carry the three specs and the architecture design into §4 as full prose, then add Implementation and Planned activities.
5. Add child issues under stories #31, #32, #34-#37, #45, #47, #48; add assignee and Sprint milestone to #75, #68, #55, #53, #42.
6. Expand §1 Introduction and §1.2 Problem Statements; fix the story #31 link.

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

**Start here:** Write the Goal 1 spec (#13) and design section in §4 of proposal.md; it is the largest missing block and everything else hangs on it.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 15 open stories have child issues (#17, #23, #24, #48); #5 and #6 are old closed leftovers. Stories #14, #16, #18, #19, #21, #22, #26, #28-#31 have no child feature/task issues yet.; #41 and #10 carry sp: under story #48; points belong on the story only.; Stories #26, #28, #29, #30, #31 have no assignee.; develop §2 and §4 links are plain links, not typed refs like [task:#36]; #25, #43, #47, #48 are not linked at all.; PR #40 has no Closes line; PRs #39 and #46 are open against main, not develop.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ❌ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a 3-row issue table; §4 Specification and design documents only says docs will be linked later.. |
| 3. Prototype works | ⚠️ partial | Python modules for document extraction, concept extraction, question generation, question selection and forgetting; no web app or single runnable entry point yet. CI: develop 11-03 green: harness and Prototype build & tests ran Install and test (Python). main's latest run 10-20 failed Run gates; its prototype job passed. Tests: Five team test files on develop (document processor, concept extractor, question generator, question selector, forgetting) plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 17 issue citation(s) become small in-text tags; 17 issue(s) fill 1 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | §4 has no specs, design or diagrams, and the prototype has tested modules but no runnable demo or accurate README. |

**Proposal, what to write:** §1.1 table still has 〈…〉 brackets in every cell; remove them and cite [1]-[4] consistently with §8.; §1.2 is 72 words plus a table of goal links; write each problem as a paragraph ending in its issue refs.; §4 has no specs: write scope, functional and non-functional requirements, acceptance criteria and open questions per epic (#13, #20, #27).; §4 has no design text or figures; 'diagrams will be added' is a promise. Draw and explain context, architecture, ER and data flow.; §4 Environment is a 6-row table; add prose on LLM provider, SQLite and Render choices, and describe the implemented modules..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prose, prototype modules and green CI; main still has the skeleton; PR #39 (open, main) — mastery tracker and tests; retarget to develop; PR #46 (open, main) — §4 environment diagram; retarget to develop; branches feature/question-generator, feature/question-selector, feature/14-document-upload — unmerged commits.

**To do before your Sprint 3 review:**

1. Create child issues under each Sprint 3 story, one assignee and Sprint milestone each; remove sp: from #41 and #10.
2. Type every issue link in §2 and §4 and add #25, #43, #47, #48 to proposal.md.
3. Write one spec per epic (#13, #20, #27) in §4 following docs/specs/example-spec.md, then summarize in proposal.md.
4. Write the design (context, components, data model, data flow, decisions, undesigned parts) and add five captioned diagrams in §4.
5. Rewrite `prototype/README.md` and add a runnable entry point; merge PR #39 so mastery tracking is demoable.
6. Clean the 〈…〉 brackets from §1.1 and expand §1.2 into paragraphs; merge develop into main.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Material Database (sponsor EL-1)

*Extract material data from vendor certificates into a searchable database with a review web app.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Build and merge the page 1 upload-and-extract slice (#86) with a test, so there is something running to demo at the review.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 6 of 16 stories have child issues (#12, #16, #24, #27, #48, #49). Stories #12-#27 have no assignee and no Sprint milestone; #13-#15, #18-#21, #23, #25, #26 have no children.; Features #86, #88, #90, #93, #95 and tasks #85, #87, #89, #92, #94, #78 carry sp: under a story.; #48, #49 and epics #42, #45, #28, #4 are not linked from proposal.md; #1 sits in the wrong section.; Three direct commits on main, including 'Update proposal with Sprint 3 work items'.; PRs #81, #50 and #8 have no Closes line.. |
| 2. Proposal §0–§4 (`main`, ≈ 8 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ✅ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Planned activities is a 42-row issue table with no prose; Specification and design documents is a link table with one-line summaries.. |
| 3. Prototype works | ❌ skeleton | Only the course login example; the five prototype-page features (#86, #88, #90, #93, #95) are open. CI: main 11-12 green: Install and test (Python) ran, but only the course `test_login.py` was exercised. develop 10-22 also green. Tests: Only the course `test_login.py`; no team tests. |
| 4. Word export (`main`) | ⚠️ partial | 74 issue citation(s) become small in-text tags; 57 issue(s) fill 5 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | Proposal and diagrams are substantial, but there is no prototype beyond the course login example to demo. |

**Proposal, what to write:** §1 Introduction is one 259-word block; add motivation, scope and a reading guide.; §4 Environment is a table of tool and purpose; add the reason for choosing AWS, FastAPI, PostgreSQL and Textract over alternatives.; Specs for Goals 1-3 exist in `docs/specs/` but §4 only lists them; summarize requirements and acceptance criteria in proposal.md.; Design docs lack rejected alternatives and 'not designed yet'; the five figures carry captions only, so add explaining prose for each.; No §4 implementation text: the prototype is still the login example. Describe what pages 1-5 will implement, then the planned work in paragraphs..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #98 (open, main) — reconciles diagrams and tech stack (#78); branch sprint-2-review — 133 commits not in develop; develop is behind main (no specs, figures or §4 text); sync it.

**To do before your Sprint 3 review:**

1. Implement page 1 (upload and extract, #86) in `prototype/` with tests per Goal 1 acceptance criterion; update the README run steps.
2. Add children to stories #13-#15, #18-#21, #23, #25, #26 and give every story an assignee and Sprint milestone.
3. Remove sp: from features #86-#95 and tasks #85-#94; keep points on stories only.
4. Merge PR #98 and rewrite §4 Environment with the reason for each technology choice.
5. Summarize each spec's requirements and acceptance criteria in §4; add prose under Figures 1-5 and a design-decisions paragraph.
6. Replace the 42-row work-item table with paragraphs ending in typed refs; link #48, #49, #42, #45.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: Interactive Crime Map and Database

*A localhost Flask and Leaflet web map of crime incidents with radius search, filters and statistics.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Rewrite `prototype/README.md` (#83) with commands that work from a fresh clone, then add the Flask and Leaflet map slice.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 8 of 8 stories have child tasks (#4, #5, #13, #15, #16, #21, #22, #28). Open tasks #27, #29, #30, #31, #33, #34 have no assignee.; #83 and the standalone tasks #62, #79, #80 are not linked in proposal.md on develop.; Tasks #66, #68, #69, #70 hang off epics rather than a story.; Legacy #6, #7, #45-#47 have no type label; #45-#47 also lack a Sprint milestone.; PRs #37, #39 and #40 have no Closes line (older Sprint 2 work).. |
| 2. Proposal §0–§4 (`develop`, ≈ 8 pages) | ✅ done | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. |
| 3. Prototype works | ⚠️ partial | Data pipeline modules: normalize crime records, load SQLite schema, area filter and crime frequency functions. No Flask app or map page yet. CI: develop 11-12 green and main 11-04 green; Install and test (Python) ran. The log is not in the data, so whether root-level `test_*.py` files were collected is unconfirmed. Tests: Four team tests in `prototype/`: normalize, load_db, area_filter, crime_frequency, plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 44 issue citation(s) become small in-text tags; 44 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The proposal is demoable on develop; the prototype shows tested data modules but no running map, and the README is still the course example. |

**Proposal, what to write:** §4 Implemented modules is 124 words; describe each module (normalizer, loader, area filter, frequency) and how its tests map to acceptance criteria.; §1 Introduction (253 words) and §1.1 (369 words) are short; add comparison prose on each competitor and cite matching §8 entries.; §1.2 is 157 words; state each problem as its own paragraph tied to a goal.; §4 Design decisions: add rejected alternatives (for example SQLite versus a server database) beside the open interfaces..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the §4 specs, five figures and prose; main is behind with link tables and placeholders.

**To do before your Sprint 3 review:**

1. Open a release PR from develop to main so the finished §0-§4 is on main.
2. Build the Flask and Leaflet slice (#23, #27) with a test per Goal 3 acceptance criterion.
3. Finish #83: rewrite `prototype/README.md` with commands that work from a fresh clone; remove `login.py`.
4. Assign #27, #29-#31, #33, #34 and link #83, #62, #79, #80 in §4 as typed refs.
5. Expand §4 Implemented modules and §1/§1.1 prose; cite sources matching §8.
6. Close or label legacy issues #6, #7, #45-#47.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*A web app that records vehicle service history and recommends next service by mileage rules.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Merge PR #82 and open the develop-to-main release PR so the prototype and proposal are on main for the review.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 7 of 10 stories have child issues (#29-#32, #34-#36); #33, #37, #38 have none yet. Sprint 3 child tasks #72-#79, #81, #85-#87 are not linked in proposal.md on develop; PR #82 would add them.; #80 carries sp: 1 under story #32; #57 carries sp: 1 under pointed task #55.; Stories #33, #37, #38 have no child issues; #59 hangs off epic #28, not a story.; Unmerged branches feature/80-section4-sprint3-rows and feature/83-claude-md-board-reminder.; PR #20 (old draft) has no Closes line.. |
| 2. Proposal §0–§4 (`develop`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Specification and design documents is a 7-row index and Planned activities a 30-row issue table; neither summarizes the content.. |
| 3. Prototype works | ✅ done | Vehicle selection: Flask JSON API with SQLite seed data, React/Vite page to pick make, model, year and trim and save a vehicle. CI: develop 11-03 green: Install and test ran for both Node and Python, so pytest API tests and the jsdom page test executed. main 10-22 green but still scaffold. Tests: `prototype/tests/test_vehicle_api.py`, `smoke_test.py` and `tests/ui/vehicle-select.test.js`, plus course `test_login.py`. |
| 4. Word export (`develop`) | ⚠️ partial | 40 issue citation(s) become small in-text tags; 40 issue(s) fill 3 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | A running vehicle-selection prototype is ready on develop, but §4 specs and design are index-only and main still holds the skeleton. |

**Proposal, what to write:** §3 is two short paragraphs (about 190 words); add the reasoning against alternatives beyond rule-based versus AI, for example Flask versus other stacks.; Four specs in `docs/specs/` are only indexed; summarize scope, requirements and acceptance criteria per epic in §4.; Design lacks a decisions-with-rejected-alternatives and 'not designed yet' summary; `docs/design/architecture.md` is not carried by proposal.md.; No §4 implementation prose: describe the vehicle-selection slice (Flask API, SQLite, React page) and its tests.; §1.2 is 103 words plus a table; write each problem P1, P2 as a paragraph ending in refs..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the prototype, specs, figures and §3-§4; main is still scaffold; PR #82 (open, develop) — links Sprint 3 tasks and vehicle-data spec in §4; branch feature/83-claude-md-board-reminder — one commit not in develop.

**To do before your Sprint 3 review:**

1. Merge PR #82, then release develop into main before the review so main shows the prototype.
2. Remove sp: from #80 and #57; add children for stories #33, #37, #38.
3. Add §4 implementation prose for the vehicle-selection slice and its tests, ending in typed refs.
4. Summarize the four specs and `docs/design/architecture.md` in §4: requirements, acceptance criteria, decisions, open questions.
5. Expand §3 alternatives and §1.2 problem paragraphs.
6. Build the service-record CRUD (#81) and entry form (#85) so the demo covers history, not only selection.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope, stablecoin wash-trading detection (sponsor SNX-3)

*Graph and anomaly-detection pipeline that flags wash trading in stablecoin transfers, with an investigation dashboard.* · Sprint 3: Nov 3 – 16 · **Sprint 3 review Tue Nov 17** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Write and test the Goal 1 graph-building code in `prototype/` (#31, #32); right now there is nothing to demo.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 0 of 14 stories have child issues; all tasks hang off epics or the proposal task. None of stories #25-#33, #38, #39, #53-#55 has child feature or task issues.; Tasks #56, #9, #8, #7, #5, #4 carry sp: under a pointed parent; #46, #50, #51 carry sp: under epics.; Stories #53, #54, #55 have no assignee; #56 has no Sprint milestone.; #3 (meeting note) is cited as [task:#3]; #67, #64, #59, #56, #51, #46, #45, #42, #5 are not linked in proposal.md.; 14 direct commits on main and develop, including recent repo restructuring.. |
| 2. Proposal §0–§4 (`develop`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 Software, Planned Activities and Tracked Task Issues are bullet lists; Specification and Design Documents is a list of links to epic specs.. |
| 3. Prototype works | ❌ skeleton | None: `prototype/` still holds only the course login example, though its README describes a Goal 1 network model slice. CI: develop 11-10 green: Install and test (Python) ran but only the course `test_login.py` exists. main 11-03 failed Repository harness; its prototype job passed. Tests: Only the course `test_login.py`; no team tests. |
| 4. Word export (`develop`) | ⚠️ partial | 30 issue citation(s) become small in-text tags; 29 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ❌ not ready | §1.1-§1.2 are one sentence each, specs and design are only linked, and the prototype contains no team code to run. |

**Proposal, what to write:** §1.1 is 28 words naming one vendor; write a comparative table of existing wash-trading detectors with pros, cons, citations from §8.; §1.2 is a single 19-word sentence; write each problem statement as a paragraph.; §4 Environment is bullets without reasons; say why Python, scikit-learn and SonarX SQL were chosen over alternatives.; Specs (`docs/specs/Epic-15-spec.md` and the Epic-23 and Epic-24 specs) and `docs/design/architecture.md` are only linked; summarize them in proposal.md.; §4 has five captioned figures but one line of explanation each; add prose on decisions, rejected alternatives and what is undesigned..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop vs main: develop holds the Epic 15 spec, design doc and diagrams; main lacks them and its CI is red.

**To do before your Sprint 3 review:**

1. Build the Goal 1 network model (#31, #32) in `prototype/` with tests, and fix the README so its commands and file references exist.
2. Create child issues under each story (start with #31, #32, #25-#27) with one assignee and Sprint milestone each.
3. Remove sp: from tasks under #6, #13, #15, #23 and from #56; assign #53-#55.
4. Write §1.1 as a comparison table plus prose and §1.2 as problem paragraphs; cite sources in §8.
5. Carry spec and design summaries into §4 as paragraphs with decisions and rejected alternatives; link #67, #64, #59, #56, #51, #46, #45, #42, #5.
6. Merge develop into main and stop direct commits.

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
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 19 stories have child issues (#66, #68, #135); 16 stories have none. Stories #62, #63, #64, #65, #67, #69, #83, #84, #111, #114, #115, #116, #126, #70, #71 have no child feature, task or sub-task.; #98 and #123 (tasks under story #66) carry `sp:`; points belong on the story only.; Stories #62, #63, #64, #65 are listed in §2 only by title, while §4 cites stories (#66, #68, #84, #111, #126) 14 times; stories belong in §2 only.; #145 is not in `proposal/proposal.md` on develop (open PR #146 adds it); #88 and #97 are cited as tasks but are features.; #108 (task under #66) has no Sprint milestone; #103 is untyped, unassigned, no milestone; stories #63, #70, #71 have no milestone or assignee.; PRs #1, #2 have no issue (old); #88 and #95 sit under an epic or nothing rather than under a story.. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ✅ §4 Design · ✅ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 "Planned activities" is a 28-line bullet list of issue links with no prose; the old Sprint 1 tasks are listed alongside the open work.. |
| 3. Prototype works | ✅ done | CLI and GUI run peak picking (baseline v1.4, CV model), channelizer, calibration with Unknown abstention, and Captum attribution; family gate (#142) not built yet. CI: develop CI green 11/12 (af07900); Prototype job ran Install and test (Python) on the team code. main CI is from 10/16 and main still holds the login scaffold. Tests: 10 test files in `prototype/tests/` covering peak picker, CV picker, channelizer, calibration, attribution, CLI, classifier, pipeline gate. |
| 4. Word export (`develop`) | ⚠️ partial | 66 issue citation(s) become small in-text tags; 50 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | A CLI or GUI peak-picker demo on the sample file runs now, but §4 lacks Environment and Implementation and main still shows the scaffold. |

**Proposal, what to write:** §4 "Environment and resources" still holds the template placeholder; the tool list is in one lead paragraph without a reason per tool (MATLAB, Python, Captum, data store).; §4 has 2 specs (application architecture, waveform family) for 5 epics; Goals 1, 4 and 5 need scope, requirements, acceptance criteria and open questions in the proposal.; §4 has no implementation section: describe what `prototype/waveform_identification/`, `xai/` and `GUI/` implement, each paragraph ending with task refs.; §1.1 has four prose subsections but no pros-and-cons table, and no prose saying what this project does differently.; §1.2 states P1-P3 in one line each; explain why each matters and tie each to a Goal.; §4 "Planned activities" should describe the remaining work (family gate #142, #143, re-classifier #70, #71, CLI/GUI join) in prose..

**Merge first** (it doesn't count until it's in `develop` or `main`): branch develop - holds the real prototype and §4 work; main is the login scaffold, promote it; PR #146 - links AMC transformer tasks #135-#137 in the proposal; closes #145; branches Application-Structure, feature/136-self-attention-amc - unmerged commits not in develop.

**To do before your Sprint 3 review:**

1. Open and merge a develop-to-main PR so `prototype/` and `proposal/proposal.md` on main are the current versions; keep main CI green.
2. Create child issues under each story that did work (#62, #64, #65, #83, #111, #114-#116, #126), assign one person and a Sprint milestone each, and cite them in §4.
3. Replace the §4 Environment placeholder with each tool and why you chose it (MATLAB, Python, Captum, mentor dataset), ending paragraphs with task refs.
4. Write a §4 Implementation section for `waveform_identification/`, `xai/` and `GUI/`, then convert the Planned activities bullet list into prose paragraphs.
5. Add short specs for Goals 1, 4 and 5 (scope, requirements, acceptance criteria, open questions) in §4, and a pros-and-cons table plus 'what this project does differently' prose in §1.1.
6. Remove `sp:` from #98 and #123; give #108, #63, #70, #71 a milestone and assignee; type #103 or close it.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. Assignment Motivation Assistant

*Windows desktop app (Python core, JavaScript UI) for assignments, suggested deadlines, progress and reminders.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Resolve the merge-conflict markers in `proposal/proposal.md` on develop and rewrite `prototype/README.md` so the review shows a document that reads cleanly and an app that runs.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 9 of 9 stories have child features and tasks (#19-#27 via features #53-#102 and tasks #55-#106). Only 6 of 72 linked issues are closed and 54 sit open in Sprint 3 (due 11/11); no feature (#53-#102) has a merged PR.; Merged PRs #108-#118 close #107, #111, #113 (documents), not the feature or task they implement; `prototype/` code exists but those issues stay open.; Tasks #91-#94, #97-#100, #104, #106 (stories 3.1-3.3) have no Sprint milestone; stories #25-#27 also lack one.; #122-#125 have 2 assignees, #107 and #111 have 4, #119 and #120 none; one assignee per issue.; Not in `proposal/proposal.md`: #113, #116, #119, #120, #122-#131 (diagram, environment and report tasks); #30-#35 use bare refs.; #111 (task, `sp: 3`) and #107 (`sp: 2`) carry points without a story parent; PRs #1, #3, #4, #9, #36 had no issue (old).. |
| 2. Proposal §0–§4 (`develop`, ≈ 9 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ⚠️ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 "Planned Activities" is a 74-row issue table (36 issue rows) with no prose; it also contains unresolved merge markers (`<<<<<<<`, `>>>>>>>`) at lines around §4 headings and in §5-§6.. |
| 3. Prototype works | ⚠️ partial | `prototype/A.M.I.Y.A.core/` has Flask-style app, database, models and assignment/deadline services; `A.M.I.Y.A.ui/` has an Electron/React assignment list and form. CI: develop CI green 11/12 (58904f4), but the Prototype job ran only the Python step and cannot collect `TestAssignments.py`; the UI `Package.json` sits in a subfolder, so Node was skipped. main last ran 10/16 and failed Run gates. Tests: 1 file, `A.M.I.Y.A.core/tests/TestAssignments.py`; name does not match pytest discovery, so CI does not run it. |
| 4. Word export (`develop`) | ⚠️ partial | 124 issue citation(s) become small in-text tags; 100 issue(s) fill 5 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo. |
| Demo-ready | ⚠️ partial | Wireframes and specs are showable, but `prototype/README.md` is still the login scaffold, no run steps exist, and CI proves nothing about the app. |

**Proposal, what to write:** `proposal/proposal.md` on develop contains merge-conflict markers in §4 (twice before and inside the Planned Activities table); resolve them, it reads as broken.; §1.1 has a 4-row pros-and-cons table but no prose arguing what A.M.I.Y.A. does differently; add it, with citations matching §8.; §4 intro describes Python + JavaScript but gives no reason per tool (Electron, Vite, SQLite or JSON) and lists no data store or hosting; #131 is open.; §4 specs are one-paragraph summaries linking `docs/specs/specs-G1-G3.md`; carry scope, requirements, acceptance criteria and open questions into the proposal.; §4 design has only UI wireframes; add system context, components, data model (`docs/design/ER_DIAGRAMS.md`), data flow and key decisions with rejected alternatives.; §3 never compares alternatives (desktop vs web vs mobile); README says 'mobile application' while the proposal says Windows desktop..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #135 - high-level architecture diagram and doc (closes #122), open into develop; PR #121 - Sprint reports and README update (closes #119), open; branch develop - holds all real work; main is stale and failed gates 10/16; branches feature/34-project-proposal, feature/47-sprint-reports - unmerged commits, 23 and 19.

**To do before your Sprint 3 review:**

1. Resolve the merge-conflict markers in `proposal/proposal.md` on develop, then merge PR #135 and #121 and promote develop to main.
2. Rewrite `prototype/README.md` with install, run and test commands for the core and the UI; rename folders and files to match what CI and the README expect.
3. Add `test_*.py` tests for deadline suggestion and assignment CRUD (one per acceptance criterion in `docs/specs/specs-G1.md`) so CI exercises team code.
4. Open one PR per feature or task (#53-#58 first) with `Closes #N`, and close the issues the prototype already implements.
5. Write §4 Environment with a reason per tool and an Implementation section, then carry specs G1-G3 and the ER design into §4 prose.
6. Fix issue hygiene: Sprint milestone on #91-#106, one assignee each, link #113-#131 in §4, and replace bare refs for #30-#35.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox

*Offline PySide6 desktop sandbox where beginners investigate and contain simulated malware, with AI-generated scenarios.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Create child issues under the 13 stories that have none, starting with #24, #26 and #27 for the next prototype slices.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 18 stories have child issues (#25, #28, #30, #36, #37); 13 stories have none. Stories #24, #26, #27, #29, #31-#35, #38-#41 have no child feature, task or sub-task; many tasks still hang directly off epics #22 and #23.; `sp:` appears on tasks #114, #115 (under stories #36, #30) and #99 (under story #25); points belong on the story only.; 9 direct commits to main and develop in Sprint 3 (e.g. adding task #70 to the architecture doc); use a branch and PR with `Closes #N`.; #79, #80, #81 have 5 assignees each; #114, #115, #84, #82 have none; #112, #113, #88 and stories #24-#41 have no Sprint milestone.; PR #50 (Goal 2 spec) has no issue; PRs #49 and #43 close #12, which is not in the proposal; #91, #92 untyped.; #113 is cited in §1 and story #24 in §4; work items go in §4 and stories in §2 only.. |
| 2. Proposal §0–§4 (`main`, ≈ 10 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ✅ §4 Specs · ⚠️ §4 Design · ✅ §4 Diagrams · ⚠️ §4 Implementation · ✅ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" opens with an 11-row link table, but each document then gets a prose summary paragraph; planned activities are prose with refs.. |
| 3. Prototype works | ✅ done | PySide6 start menu loads a sample or JSON scenario, validated by Pydantic; user browses, creates and deletes simulated files in memory; optional Ollama scenario generator. CI: main CI green 11/12 (ec16018) and develop green; Prototype job ran Install and test (Python) on team code, and CI fails if no tests are collected. Tests: 5 test files in `prototype/tests/`: scenario model, loader, simulation engine, scenario generator, and UI (Qt offscreen). |
| 4. Word export (`main`) | ✅ done | 127 issue citation(s) become small in-text tags; 79 issue(s) fill 6 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ✅ ready | Proposal §0-§4 is written and the PySide6 prototype runs from a clean clone with README steps and green CI; the demo covers file actions and scenario loading. |

**Proposal, what to write:** §4 design: only the network viewer (#105) shows key decisions with rejected alternatives; add decisions and 'not designed yet' for architecture, data model and data flow.; §4 "Prototype implementation details" is one 129-word paragraph; split into front-end (`ui/`), simulation (`sim/`), scenario and data store (`scenario/`) with task refs.; §4 specs: carry scope, FR/NFR and acceptance criteria for Goal 1 and Goal 2 into the proposal, not only the summary paragraphs; the Tkinter spec contradicts the PySide6 prototype.; §1.1 table has emphasis and difference columns but no pros and cons per platform; add both.; §3 still says 'Sprint 2 priorities' and 'not high-risk runtime behavior'; update it to what the prototype now implements..

**To do before your Sprint 3 review:**

1. Create child feature, task and sub-task issues under the 13 stories without children (start with #24, #26, #27, #29), each with one assignee and a Sprint milestone.
2. Remove `sp:` from #99, #114 and #115; assign #114, #115, #84 and #82; add milestones to #112, #113 and #88.
3. Stop direct commits to main and develop: open a branch and PR with `Closes #N` for each change, including proposal edits.
4. Expand §4 "Prototype implementation details" by layer (`ui/`, `sim/`, `scenario/`), each paragraph ending with task refs.
5. Add key decisions, rejected alternatives and 'not designed yet' summaries for architecture, data model and data flow in §4 design.
6. Add pros and cons columns to the §1.1 table and reconcile `docs/specs/desktop-interface.md` (Tkinter) with the PySide6 prototype.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine and game demo

*C++ OpenGL 3.3 entity-component-system engine plus a game demo to measure performance on old hardware.* · Sprint 3: Oct 29 – Nov 11 · **Sprint 3 review Thu Nov 12** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Merge PR #77 and get "Prototype build & tests" to compile the CMake project in CI, so the review can show a green build of the engine.

| Rule | Status | What I found |
|---|---|---|
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 4 of 8 stories have child issues (#30, #31, #32, #33); #26-#29 have none. Stories #26, #27, #28, #29 (Goal 1, game demo) have no child feature, task or sub-task.; `proposal/proposal.md` on develop has 0 typed refs: the planned-activities table uses bare `#N` and malformed `[story:https://...]` parent cells; use `[task:#N]`.; #46 names itself as parent and carries `sp: 2`; re-parent under story #32 and drop the points.; Stories #30, #32, #33, #26-#29 have 2 assignees and epic #6 has 5; one assignee per issue. #43 has no milestone; #44 has no assignee.; #76, #43 and epic #6 are not in the proposal; #44, #47-#50, #54, #61 have no type; PR #77 closes #76.; main still holds the Sprint 1 scaffold: 4 direct commits, 83 placeholders; PRs #3, #4, #5, #41 have no issue (old).. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ✅ §1.1 Related work · ⚠️ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ⚠️ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 "Specification and design documents" is a 3-row link table and "Planned activities" is a 37-row table of issues, owners and sprints with no prose; §1.2 problems sit in a table.. |
| 3. Prototype works | ⚠️ partial | CMake project (SDL3, Assimp, ImGui, GLM) with engine, renderer, ECS, platform and demo header trees plus GLSL shaders; no run is shown in CI. CI: develop CI green 11/11 (f2ea0f3) but the Prototype job ran only "Nothing to build"; Node and Python steps skipped, so the C++ code was never compiled or tested. main last ran 10/2. Tests: none on develop; open PR #77 adds `tests/test.cpp`, and `tests/test_login.py` is only on main. |
| 4. Word export (`develop`) | ⚠️ partial | 2 issue citation(s) become small in-text tags; 2 issue(s) fill 1 table(s) in Appendix A; 25 issue URL(s) stay in the text because they aren't written as links (use `[task:#N](https://github.com/OWNER/REPO/issues/N)`); replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ⚠️ partial | Proposal §0-§3 reads well, but §4 is tables and links, CI never built the C++ code, and the window and ECS demo work sits in unmerged PR #77 and branches. |

**Proposal, what to write:** §4 has no specs in the proposal: summarize `docs/specs/game-engine.md` and `game-demo.md` (scope, FR/NFR, acceptance criteria, open questions) in prose.; §4 design is only a link to `docs/design/architecture.md`; add components, data model (entities, components, systems), data flow and key decisions with rejected alternatives.; §4 diagrams: Figures 1 and 2 have captions but no explaining paragraph; add one per figure.; §4 environment gives a one-line reason per tool; add why SDL3, Assimp, ImGui and C++26 fit the old-hardware target, and the build and test machines.; §4 has no implementation section: describe the headers under `prototype/include/engine/` and `demo/` and what runs today, ending with #63, #66, #67.; §4 planned activities: replace the table with paragraphs on the remaining work (editor #33, renderer #32, enemies and gameplay #26-#29)..

**Merge first** (it doesn't count until it's in `develop` or `main`): PR #77 - CMake plus `src/main.cpp` and `tests/test.cpp` for multiplatform build (closes #76), open; branch develop - the real proposal and prototype; main is the Sprint 1 scaffold, promote it; branch 31/Objective-2.2-Demonstrate-multiplatform-compilation - 3 commits not in develop; branch 33-objective-24-implement-visual-editor... - 7 commits not in develop.

**To do before your Sprint 3 review:**

1. Merge PR #77, then fix CI (#76) so "Prototype build & tests" runs CMake build and a C++ test; show a green build before the review.
2. Rewrite `prototype/README.md`: delete the login text, add a working "How to test" and "What it proves" for the ECS slice.
3. Open PR from develop into main so main carries the current proposal, prototype and CI.
4. Add child issues under stories #26-#29, fix #46's parent, and give each issue one assignee and a Sprint milestone.
5. In §4 write Specifications, Design (components, data model, data flow, decisions) and Implementation as prose, carried from `docs/specs/` and `docs/design/`.
6. Replace the planned-activities table with paragraphs and typed refs like `[task:#63]`; explain Figures 1 and 2 in text.

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
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 3 of 6 stories have child issues (#25, #29, #30); #26, #27, #28 have none; #46, #47, #53 hang under epic #21. `sp: 2` on tasks #41, #42, #43, #49, #55 and `sp: 1` on new #57 under stories; #51 under pointed task #47 (double counting).; #41, #49, #51, #55, #57, #58, #59 are not linked from the proposal; PRs #40, #50, #52, #56 close some of them.; #49 and #55 have no assignee.; Sixteen merged PRs (#5-#45 range) have no `Closes #N`; main has 30 direct commits.; Tasks #46, #47, #53 are parented to epic #21, not to a story; #26, #27, #28 still have no children.. |
| 2. Proposal §0–§4 (`main`, ≈ 5 pages) | ⚠️ partial | ✅ §0 Abstract · ⚠️ §1 Intro · ⚠️ §1.1 Related work · ⚠️ §1.2 Problem · ⚠️ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ❌ §4 Specs · ⚠️ §4 Design · ⚠️ §4 Diagrams · ❌ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §1.1, §1.2, the §4 environment table, the spec/design document table and 'Planned activities' (5 rows) are tables; no prose carries the issue refs.. |
| 3. Prototype works | ❌ skeleton | Empty module skeleton: `backend/lastfm.py`, `database/db.py`, `schema.sql`, `main.py`; README says there is no current code to run. CI: main 12278fb (Nov 6): run failed on Repository harness 'Run gates'; Prototype job green but no team tests exist. develop run green (Nov 2). Tests: none; no `prototype/tests/` folder, although the README claims four tests |
| 4. Word export (`main`) | ✅ done | 14 issue citation(s) become small in-text tags; 14 issue(s) fill 3 table(s) in Appendix A; replace your `proposal/to-word.lua` with the Nov 8 course version to get the issue tables. |
| Demo-ready | ❌ not ready | There is no running prototype to demo, main CI is red on the harness gate, and §4 has no spec, design or implementation prose. |

**Proposal, what to write:** §1.1 is a four-row table with no prose; add paragraphs arguing what SonicScape does differently, with citations matching §8.; §1.2 is a three-row table and §2 has no prose; write the problem statements and explain each epic and story in paragraphs ending in refs.; §4 specs: `docs/specs/specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` are only listed; summarize scope, requirements, acceptance criteria, open questions per epic.; §4 diagrams are bare Mermaid blocks or images with no explaining prose; the system-context diagram has no caption; write a paragraph for each.; §4 has no implementation details and 'Planned activities' lists only five Sprint 2 rows; describe the first end-to-end slice and Sprint 3-4 work..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop branch — stale scaffold with a different title; align it with main or retire it.

**To do before your Sprint 3 review:**

1. Fix the failing Repository harness gate on main so CI is green again; read the 'Run gates' log and correct what it names.
2. Build the first end-to-end slice in `prototype/` (Last.fm into SQLite, one galaxy view, one swipe) and add `prototype/tests/` with one test per acceptance criterion.
3. Replace the README run line with commands that work from a fresh clone, and drop the claim of four tests until they exist.
4. Write §1.1 and §1.2 as prose, and add a paragraph after each goal and objective in §2 ending with typed refs.
5. Summarize `specs_goal1.md`, `specs_goal2.md`, `specs_goal3.md` in §4, then add a paragraph and caption for every diagram.
6. Link #41, #49, #51, #55, #57-#59 in §4 and remove `sp:` from child tasks; add Sprint 3 child issues under #26-#28.

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
| 1. PRs ↔ issues ↔ proposal | ⚠️ gaps | 5 of 8 stories have child issues (#13, #18, #19, #20, #22); #14, #15, #23 have none. Goals #12, #17, #21 are epics but cited as [story:#N] in §2; features #39-#52 appear as bare `Task [#N]`, not typed refs.; 12 issues not in §4: #11, #24-#28, #34, #35, #37, #54, #55, #57, #64.; §4 Parent column disagrees with the board parent for #41, #42, #44, #45, #49, #51, #52.; `sp:` on tasks #28, #41, #54, #55, #64, parented to epic #12 rather than a story; #54 and #55 have two assignees.; PR #5 has no `Closes #N`; one early direct commit on main.. |
| 2. Proposal §0–§4 (`develop`, ≈ 6 pages) | ⚠️ partial | ✅ §0 Abstract · ✅ §1 Intro · ⚠️ §1.1 Related work · ✅ §1.2 Problem · ✅ §2 Goals · ✅ §3 Approaches · ✅ §4 Environment · ⚠️ §4 Specs · ❌ §4 Design · ❌ §4 Diagrams · ⚠️ §4 Implementation · ⚠️ §4 Planned activities. Link tables in place of prose: §4 planned activities is a 14-row link table with no prose; the spec index keeps two 〈…〉 template rows beside three real ones.. |
| 3. Prototype works | ⚠️ partial | Unreal Engine 5 first-person starter project (`Config/`, `Content/`, `Insomnia.uproject`); starter-level movement only, no team gameplay. CI: main (Nov 6) and develop (Nov 6) green, but the Prototype job ran only 'Nothing to build'; the Unreal project is not exercised by CI. Tests: none; README describes a manual smoke test only |
| 4. Word export (`develop`) | ⚠️ partial | 25 issue citation(s) become small in-text tags; 25 issue(s) fill 2 table(s) in Appendix A; `proposal/to-word.lua` or `proposal/reference.docx` is missing from your repository: copy both from the course repo; 〈placeholders〉 are still in the text and would print in Word. |
| Demo-ready | ⚠️ partial | The starter level runs per the README, but there is no team gameplay yet, and §4 design and diagrams are not in the proposal. |

**Proposal, what to write:** §1.1 has good prose on three games but no pros-and-cons table; add one across Visage, MADiSON, Phasmophobia and state what Insomnia does differently.; §4 specs: three files in `docs/specs/` are indexed but not summarized; add scope, requirements, acceptance criteria and open questions per epic, and delete template rows.; §4 design is absent: write context, components (monster AI, director, audio), data flow, decisions with rejected alternatives, and what is undesigned (#64).; Diagram sources `docs/design/*.mmd` exist on main only and are not in the proposal; embed each with a caption and prose.; §4 has no implementation details and no prose on remaining work; describe the starter project and each Sprint 3 feature group..

**Merge first** (it doesn't count until it's in `develop` or `main`): develop to main — main §3 is still the template and trails develop; docs/design/*.mmd diagrams (PR #62) are on main only; bring to develop and into the proposal.

**To do before your Sprint 3 review:**

1. Write the §4 design subsection from task #64: context, components, state model, decisions with rejected alternatives; embed `docs/design/*.mmd` diagrams with captions.
2. Fix the §2 refs for #12, #17, #21 to [epic:#N]; make #39-#52 typed refs and add #11, #24-#28, #34, #35, #37, #54, #55, #57, #64 to §4.
3. Align the §4 Parent column with the board for #41, #42, #44, #45, #49, #51, #52; remove `sp:` from tasks under epics.
4. Add a pros-and-cons related-work table across the three games and tie it to the references.
5. Build the first playable slice (maze, patrol monster) with one test per acceptance criterion in each spec.
6. Create child issues under #14, #15, #23; delete the 〈…〉 rows in §4 and merge develop into main.

[↑ Back to all groups](#groups)

## About this page

The Sprint 2 checklist (specs, design, environment, prototype wiring) is now folded into rule 2 (§4) and rule 3. The earlier editions, including the Sprint 2 cards, are in this file's git history. The harness in your Actions tab still checks the repository rules on every pull request.
