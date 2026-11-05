# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-11-05 20:47 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

**Jump to your group:**

| [**G01**](#g01) | [**G02**](#g02) | [**G03**](#g03) | [**G04**](#g04) | [**G05**](#g05) | [**G06**](#g06) | [**G07**](#g07) | [**G08**](#g08) | [**G09**](#g09) | [**G10**](#g10) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [**G11**](#g11) | [**G12**](#g12) | [**G13**](#g13) | [**G14**](#g14) | [**G15**](#g15) | [**G16**](#g16) | [**G17**](#g17) | [**G18**](#g18) | [**G19**](#g19) | [**G20**](#g20) |

## What Sprint 2 must cover

Each item lands the usual way: an issue on your board, cited in `proposal/proposal.md`, done in a pull request that says `Closes #N`, and **merged into `develop` or `main` before your review**. Work left in a branch or an open pull request doesn't count yet.

**Where it goes: `proposal/proposal.md` must carry all of it.** Your specifications, design and diagrams count as long as they're incorporated into `proposal.md` (§3 and §4). **I recommend** that `proposal.md` holds the summary and the diagrams, and that the full detail lives in its own document in the repository: one `docs/specs/<epic>.md` per epic and one `docs/design/<topic>.md` per design topic, each linked from §4. The proposal stays readable, the detail stays reviewable, and CPSC 491 starts from documents you can extend.

1. **Epics and stories, kept current.** Every goal in §2 is an epic and every objective a story titled with the objective's own words ([README §4](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board)). Every Sprint 2 card on the board has one assignee, `sp:` and the `Sprint 2` milestone, and every issue is cited in `proposal.md` (epics and stories in §2, everything else in §4).
2. **A specification per epic**, summarized in proposal §4 (recommended: full detail in `docs/specs/<epic>.md`): scope (in and out), functional and non-functional requirements traced to your stories, acceptance criteria someone else can check, and open questions. The first lines name the epic and its stories. Model: [example-spec.md](https://github.com/kyoungshin/CPSC490/blob/main/docs/specs/example-spec.md).
3. **A high-level design with diagrams**, shown in proposal §4 *Diagrams* with captions (recommended: full detail in `docs/design/<topic>.md`). Every project needs a **high-level architecture** diagram (the major pieces and how they connect) and a **system context** diagram (what's inside your system, and who and what is outside it). Add the ones your project needs: a **data flow diagram** (how data moves and is transformed), an **ER/EER diagram** (anything you store), **UML** (a sequence diagram for your critical flow; class or state diagrams where they're real), and a **page/screen flow or wireframes** (anything with a UI). Commit the editable source and an exported image, or use Mermaid in the `.md`. Model: [example-design.md](https://github.com/kyoungshin/CPSC490/blob/main/docs/design/example-design.md); tools and conventions: [DIAGRAMS.md](https://github.com/kyoungshin/CPSC490/blob/main/docs/design/DIAGRAMS.md).
4. **Your environment and resource choices, written down** in proposal §4 *Environment and resources*: language(s), framework or engine, platform and OS, data store, hosting or hardware, sponsor data, APIs and accounts, and dev tools. Give each a one-line reason tied to §3 *Proposed Approaches*. List every separate spec and design document under §4 *Specification and design documents*, with a one-paragraph summary each.
5. **Wire those choices into `prototype/`, no features yet.** Create the project skeleton with your chosen stack: the framework's own starter (or the Unity/Godot project, the Python environment, the firmware project), a dependency file (`requirements.txt`, `package.json`, …), folders that mirror the components in your architecture diagram, a `.env.example` for keys and connection strings (never the real secrets), and a `prototype/README.md` with setup and run commands that work on a teammate's fresh laptop. Prove the toolchain with one smoke run: the app or server starts, the database or sponsor API connects, the board flashes, the notebook loads sample data. Delete the course's example `login.py` and its test once yours replaces them.
6. **Demo at your Sprint 2 review:** walk through the diagrams, then run the skeleton from a clean clone by following your README. Bring the story points committed and done (*Sprint report* workflow in your Actions tab).

> [!NOTE]
> **New from Sprint 2: I look at *when* work moved, for each member's sprint score.** Move your own cards as the work happens: **In Progress** when you start (open a branch or a draft pull request), **In Review** when your pull request is ready and a teammate is reviewing it, and **Done** when it merges. The board records the time of every status change, and pull requests record first commit, review and merge. Work that spends real time in progress and in review counts. Cards that jump straight to Done, or a batch of cards moved and closed in one burst at the end of the sprint, don't show that work happened during the sprint.

**Not required in Sprint 2:** feature code, a working end-to-end slice, or a polished UI. Those start in Sprint 3, when the prototype proves your riskiest design choice.

| Groups | Sprint 2 | Sprint 2 review and demo | Sprint 3 |
|---|---|---|---|
| G01–G05 | Oct 13 – 26 | **Tue Oct 27** | Oct 27 – Nov 9 |
| G11–G15 | Oct 15 – 28 | **Thu Oct 29** | Oct 29 – Nov 11 |
| G06–G10 | Oct 20 – Nov 2 | **Tue Nov 3** | Nov 3 – 16 |
| G16–G20 | Oct 22 – Nov 4 | **Thu Nov 5** | Nov 5 – 18 |

## Class at a glance

✅ done · ⚠️ started, not complete · ❌ not started, or only the course's example files. Each column is one item from the list above; the card below each group says exactly what's missing.

| Group | Sprint 2 review | 1. Epics & stories | 2. Specs | 3. Design & diagrams | 4. Environment | 5. Prototype wiring |
|---|---|---|---|---|---|---|
| [G01](#g01) BGAF | Tue Oct 27 | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ⚠️ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) Epic Engineers | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ✅ | ⚠️ |
| [G07](#g07) MightyMorphin | Tue Nov 3 | ⚠️ | ⚠️ | ✅ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [G10](#g10) Team Jiddak StableScope | Tue Nov 3 | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G13](#g13) BYKX | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G16](#g16) Neuroprosthetic | Thu Nov 5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [G17](#g17) SonicScape | Thu Nov 5 | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ⚠️ | ❌ | ⚠️ | ✅ |

- **Specs:** 18 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20).
- **Design and diagrams:** 18 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19).
- **Environment:** 20 of 20 have written their environment choices into the repository (G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20).
- **Prototype wiring:** 15 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G02, G03, G05, G06, G08, G09, G11, G12, G13, G15, G16, G17, G18, G20).
- **Waiting in a branch or open pull request:** G02, G03, G06, G07, G10, G12, G13, G14, G17. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting pipeline

*Cleans SonarX Hyperliquid data, rebuilds order books, validates them, and backtests strategies behind a React research workspace.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge PRs #252, #221 and #189 (resolving #218's conflicts) so proposal §4 carries the ER, front-end and wireframe figures.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#20-#22) and objective-titled stories exist, all 146 issues linked from proposal.md. But epics/stories are also cited in §4, and about 25 open issues are not on the board. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1 cleaning and rebuild; scope, FR, criteria; `docs/specs/validation.md` (main) — Goal 2 validation and gating; `docs/specs/backtest.md` (main) — Goal 3 backtesting |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: data cleaning pipeline; er: DuckDB stored data; uml: sequence for market-day run; ui_flow: React workspace. |
| 4. Environment | ✅ done | Stated in: proposal §4 (main). Language: Python 3.12; TypeScript; Framework: React + Vite front end; one `bgaf_pipeline` package; Platform: Laptops and GitHub Actions Linux runners; Node 20.19+; Data: DuckDB 2.0.0 with DECIMAL(38,18) prices; Parquet proposed; Hosting/hardware: Local only; hosting undecided; Sponsor resources: SonarX L2/L4 data, requester-pays S3, Snowflake trial share; Tools: GitHub Actions CI, pytest, Mermaid, oxlint. |
| 5. Prototype wiring | ✅ done | `prototype/src/bgaf_pipeline/` one module per pipeline step, mirrors architecture; `prototype/requirements.txt` and `pyproject.toml` pin duckdb and pytest; `prototype/.env.example` AWS settings; README has setup and run steps; `prototype/tests/test_storage.py` loads a SonarX snapshot into DuckDB; `prototype/frontend/` Vite React TypeScript skeleton with package.json |

**Merge first** (not counted until it's in `develop` or `main`): PR #252 — EER data model summary and er-model diagram into proposal §4; PR #221 — proposal §5 Project Outcomes; PR #189 — front-end architecture doc and proposal summary (needs conflict fix, #218); `develop` — holds only scaffold; all team work is on `main`.

**To do before your Sprint 2 review:**

1. Merge PRs #252, #221 and #189 into the branch you use, after fixing the conflicts listed in #218.
2. Close #206-#216 by adding the screen-flow, wireframe, component and state-diagram figures with captions to proposal §4 Diagrams.
3. Move epic and story citations out of §4 into §2 and keep only work items in §4.
4. Add the open issues missing from the board (#242-#246, #206-#216) with assignee, `sp:` and milestone.
5. Sync `develop` with `main`, or choose one integration branch and state it in the README.
6. Recommend: keep the summaries and diagrams in proposal.md and the full detail in `docs/specs/` and `docs/design/`, as you already do.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: distributed signal capture for multi-node analysis (RTX)

*ESP32 nodes capture Wi-Fi and Bluetooth metadata, a backend identifies recording devices, and a dashboard shows them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Merge feature/23-approach-environment and finish §4 so the environment choices (ESP32, FastAPI, Postgres, Angular) are in proposal.md with reasons.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 4 epics (#20, #47, #50, #56) and objective-titled stories exist, but only 18 of 73 issues are linked from proposal.md, and most Sprint 3 stories have no assignee. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #47 Goal 1: collect wireless signal metadata; Epic #50 Goal 2: identify selected recording devices; Epic #56 Goal 3: dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence for node-to-backend upload; ui_flow: dashboard screens; er: Postgres observations (done). |
| 4. Environment | ⚠️ partial | Stated in: HW#4 only; unmerged branch feature/23-approach-environment; proposal §4 is a skeleton. Language: Python 3.12 (backend); ESP32 firmware language not stated; Framework: FastAPI backend, Angular dashboard; Platform: ESP32 nodes over Wi-Fi; Data: PostgreSQL (PR #115); Hosting/hardware: ESP32 capture nodes; AWS Lightsail proposed then being removed (#102); Sponsor resources: RTX project sponsor meetings; no data feed named; Tools: uv, pytest, GitHub Actions, drawio. |
| 5. Prototype wiring | ⚠️ started | `prototype/backend/main.py` FastAPI app with /health; `test_main.py` tests it; `prototype/backend/pyproject.toml` and `requirements.txt` from uv; `prototype/README.md` has setup, run and test steps for backend only; PR #115 adds Postgres compose, `db.py` and `.env.example` (not merged) |

**Merge first** (not counted until it's in `develop` or `main`): PR #115 — Postgres compose, db.py, .env.example; open against develop; branch feature/23-approach-environment — §3/§4 environment text, 10 commits unmerged; branch feature/86-lightsail-hosting — hosting proposal, being superseded by #102; branch feature/93-postgres-database — same content as PR #115.

**To do before your Sprint 2 review:**

1. Merge the §3/§4 branch feature/23-approach-environment and finish §4 Environment and resources (#105).
2. Write three specs in `docs/specs/` for epics #47, #50, #56, each opening with the epic and stories lines.
3. Write `docs/design/architecture.md` and list all design docs in the proposal §4 table, replacing the placeholder rows.
4. Embed architecture, context and DFD figures in proposal §4 with captions, not only the ER image.
5. Scaffold the Angular dashboard (#94) and ESP32 firmware (#92) in `prototype/` and update the README.
6. Link the 55 unlinked issues from §4 and assign #92, #67, #102, #105.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: equation transcription, data generation and model training notebook

*A Jupyter notebook that transcribes an equation, generates a noisy dataset, trains a PyTorch model and plots results.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Replace the scaffold `prototype/README.md` and `requirements.txt` so a fresh machine can install and run the verifier and dataset generator.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 4 epics (#27, #28, #43, #44) and objective-titled stories exist. Epics and stories #43-#47 have no milestone, and §2 has bare or bad-URL refs for #27, #28, #31, #43, #44. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (main, develop) — Goal 1; only #33 section complete; `docs/specs/data-generation.md` (main, develop) — Goal 2; partial, two stories unowned Missing: Epic #43 Goal 3 train a model (issue #71); Epic #44 Goal 4 notebook output (issue #72). |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er: stored dataset files need a schema (CSV columns); ui_flow: notebook steps and user-input points. |
| 4. Environment | ⚠️ partial | Stated in: §3 (design decisions); §4 Environment still a placeholder. Language: Python (not stated); Framework: Jupyter notebook (sponsor requirement); PyTorch; Platform: User's local machine for training; Data: CSV or relational via notebook; store not final; Hosting/hardware: None; local notebook; Sponsor resources: External AI APIs for transcription and data generation, model not named; Tools: GitHub Actions CI, Mermaid. |
| 5. Prototype wiring | ⚠️ started | `prototype/verifier.py`, `transcriber.py`, `generate_dataset.py`, `train.py` exist; `prototype/tests/test_verifier.py` tests the verifier; `prototype/requirements.txt` is still the unchanged course scaffold; `prototype/README.md` still describes login.py |

**Merge first** (not counted until it's in `develop` or `main`): PR #74 — train.py for Objective 3.1; open against develop; PR #73 — live loss curve in train.py; open against main; branches feature/50-transcriber and feature/46-plot-equation — unmerged; develop — ahead of main with csv_file.py, train.py and datasets.

**To do before your Sprint 2 review:**

1. Rewrite `prototype/README.md` and `requirements.txt` for the notebook, PyTorch and the AI client, with a smoke run.
2. Add `prototype/.env.example` for the AI API key and keep the key out of git.
3. Fill proposal §4 Environment and resources, naming the AI services and versions.
4. Write specs for Goals 3 and 4 (#71, #72) and finish the missing story sections in the two existing specs.
5. Merge PRs #73 and #74 and branches feature/50-transcriber and feature/46-plot-equation, then promote develop to main.
6. Fix §2 refs and add milestones and assignees to #43-#47; link #60-#72 in §4.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket trader PNL and ranking dashboard (SNX)

*Computes profit and loss for Polymarket wallets from SonarX Snowflake data, ranks traders, and serves a dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Merge PR #137 and PR #138 so the chosen stack and the prototype skeleton are on the integration branch.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#24, #29, #33) and objective-titled stories (#25-#38) exist, all linked from §2/§4. But every story is on Sprint 3 or 4, none on Sprint 2, and #80 is cited as a task though it is a sub-task. |
| 2. Specs | ⚠️ started | `docs/specs/pnl-calculation.md` (main, develop) — Epic #24; scope, FR, worked example; `docs/specs/trader-ranking.md` (develop) — Epic #29; ranking and behavior metrics; `docs/specs/dashboard-questions.md` (PR #73, open) — Epic #33 question list Missing: Epic #33 dashboard spec (`docs/specs/dashboard.md`, #125; `data-sources.md`, #104). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ✅ page flow. Needed for this project: dfd: pipeline from Snowflake to results; er: stored results tables; uml: sequence for a PNL run (#59); ui_flow: leaderboard and wallet pages. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (Snowflake only); stack decision in PR #137 and #52 unmerged. Language: Python (only in unmerged PRs #138-#140); Framework: Dashboard framework not chosen on main; Platform: Not stated; Data: SonarX Snowflake, Polygon Polymarket tables; Hosting/hardware: Not stated; Sponsor resources: SonarX read-only Snowflake access (SNX); Tools: GitHub Actions, pytest, Mermaid. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` still the course example; `prototype/requirements.txt` and `README.md` unchanged scaffold; PR #138 adds `src/` skeleton, Snowflake client, `.env.example`; open |

**Merge first** (not counted until it's in `develop` or `main`): PR #138 — prototype skeleton and Snowflake client (#62); PR #137 — records the prototype stack in proposal §4 (#52); PRs #136, #135, #79, #143 — data-flow, ER, dashboard-flow diagrams and proposal copies; PRs #139, #140 — position builder and resolution matching code; PR #73 — dashboard questions spec.

**To do before your Sprint 2 review:**

1. Merge PR #137 and #138 first: the stack record and the skeleton unblock the rest.
2. Merge diagram PRs #136, #79, #135, then #143 after rebasing; resolve the overlapping `docs/design/architecture.md` edits.
3. Write `docs/specs/dashboard.md` (#125) and `docs/specs/data-sources.md` (#104).
4. Write `docs/design/pnl-pipeline.md` with the sequence diagram (#59).
5. Delete `prototype/login.py` and its test, then add a Snowflake smoke run to `prototype/README.md`.
6. Confirm one integration branch (develop or main) and merge the Sprint 2 PRs there.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS whale identification and location system

*Detects whale calls in hydrophone audio with a trained AI and locates the source from time differences.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge PR #48 and the open design PRs, then draw the missing architecture and system context diagrams (#57) into proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 epics (#8, #14) and objective-titled stories (#9-#18) are linked in §2 and on the board. Only 11 of 32 issues are linked; Sprint 3 items and #56-#58 are missing from §4. |
| 2. Specs | ⚠️ started | `docs/specs/goal-2-locator.md` (develop) — Epic #14 locator; scope, FR, criteria Missing: Epic #8 Goal 1 whale-call recognition (AI detector). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for every project; er: whale-call database exists; dfd: audio to detection to location; uml: sequence for detect then locate. |
| 4. Environment | ⚠️ partial | Stated in: README and requirements (develop); proposal §4 skeleton. Language: Python; Framework: PyTorch, librosa, scipy, numpy; Platform: Local machine, Windows or Mac/Linux; Data: SQL database from `db/init/schema.sql`, `docker_compose.yaml`; Hosting/hardware: Local; simulated hydrophone array; Sponsor resources: Hydrophone recordings; source of audio not stated; Tools: GitHub Actions, pytest, Docker. |
| 5. Prototype wiring | ✅ done | `prototype/locator/` and `ai-detector/` mirror the two goals (develop); `prototype/requirements.txt` pins numpy, scipy, torch, librosa; `prototype/.env.example` exists; README has setup, run, test; `python -m locator.smoke` smoke run; 4 test files in `prototype/tests/`; `db/init/schema.sql` and `docker_compose.yaml` on main for the database |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 — develop to main: locator, AI detector, README, requirements; PR #55 — locator design doc (#49) and proposal edits; PR #60 — AI design diagram (#58); PR #54 — work items listed in proposal §4 (#53); PR #62 — remerge main into develop (schema, ER diagram).

**To do before your Sprint 2 review:**

1. Merge PRs #48, #54, #55, #60 and #62 so main and develop agree.
2. Write `docs/specs/goal-1-detector.md` for epic #8 and link both specs from proposal §4.
3. Draw architecture and system context diagrams (#57) as Mermaid plus PNG and embed them in §4.
4. Add a DFD and a sequence diagram for detect then locate, plus the ER diagram, with captions in §4.
5. Fill §4 Environment and resources from the README choices, with reasons tied to §3.
6. Remove the course `login.py` line from `prototype/README.md` and add the database start step.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Web study assistant that generates questions from student materials and targets each student's weak concepts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write docs/specs/ for epic #20 (stories #21-#26 are already underway) and link it in proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #13, #20, #27 with objective-titled stories; Sprint 2 stories #21-#26 on board. Stale epics #3/#4 and stories #5/#6 remain; develop §2 has links but no typed refs. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #13 Goal 1 generate/grade/summarize; epic #20 Goal 2 weak-spot tracking; epic #27 Goal 3 web app and study. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for every project; dfd: upload, extract, generate, grade loop; er: SQLite stores mastery and concepts; uml sequence: question generation then grading; ui_flow: student web app screens. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop); main still a skeleton. Language: Python 3; Framework: Flask; Platform: Python web app on localhost/Render; Data: SQLite; Hosting/hardware: Render free tier; Sponsor resources: none (no sponsor); Tools: GitHub Issues/PRs/Actions, pytest, Anthropic Claude API. |
| 5. Prototype wiring | ⚠️ started | `prototype/requirements.txt` lists pypdf, python-docx, python-pptx, pytest; `prototype/question_selector.py`, `forgetting.py`, `concept_extractor.py` with tests on develop; `prototype/README.md` is still the login scaffold; `login.py` not replaced; No Flask, anthropic or sqlite code; no `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #46 (open, main) — §4 environment diagram, proposal.md only; PR #39 (open, main) — per-concept mastery tracker and tests (#21); develop to main release — forgetting, selector, question generator, §3/§4 only on develop; branches feature/question-generator, feature/question-selector, feature/21-mastery-tracking not in develop.

**To do before your Sprint 2 review:**

1. Write one spec per epic in docs/specs/ for #13, #20, #27 and link them in proposal §4 'Specification and design documents'.
2. Create docs/design/architecture.md and system-context.md with Mermaid diagrams, and add them with captions to proposal §4 Diagrams.
3. Add an ER diagram for SQLite mastery data and a sequence diagram for generate-then-grade; list them in §4.
4. Rewrite prototype/README.md for GapWise with working setup, run and test commands; remove login.py and test_login.py.
5. Add a Flask skeleton with /health, SQLite init and a stubbed Claude call, plus .env.example, as the smoke run.
6. Merge PR #39 and #46, then promote develop to main; convert §2/§4 links to typed refs like [[task:#41]](url).

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · MightyMorphin: material certificate data extraction and database (EL)

*Internal web app that extracts material test data from CoC PDFs, stores it, and supports search and comparison.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Merge the two open spec PRs (#76, #79) so all three epics have a spec on main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #11, #17, #22 with objective stories #12-#27; design epic #42 with #48/#49 on Sprint 2. Some issues lack sp:/Sprint, story #48 cited in §4, #28 is an epic-typed task. |
| 2. Specs | ⚠️ started | `docs/specs/data-extraction-spec.md` (main) — Goal 1; all sections, but names epic #42 not #11 Missing: epic #17 Goal 2 storage (PR #76 open); epic #22 Goal 3 analysis (PR #79 open). |
| 3. Design & diagrams | ✅ done | ✅ architecture · ▫️ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: uml sequence: upload, extract, review, approve flow; separate system context: architecture shows externals only. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main). Language: Python; Framework: FastAPI backend; React/Vue frontend (undecided); Platform: AWS; Data: PostgreSQL on RDS in §4; Snowflake in architecture diagram; Hosting/hardware: AWS, S3 for PDFs; Sponsor resources: EL CoC and test-report PDFs (not yet received), SSO; Tools: VS Code, Git/GitHub, Figma, Textract/Tesseract. |
| 5. Prototype wiring | ❌ example files only | `prototype/` holds only course `login.py` and `tests/test_login.py`; `prototype/requirements.txt` unchanged scaffold; README is the course example; Only other code is wireframe build scripts under `docs/design/ui-wireframe/` |

**Merge first** (not counted until it's in `develop` or `main`): PR #76 (open, main) — Goal 2 storage spec and proposal links; PR #79 (open, main) — Goal 3 analysis spec and proposal links; branches task/58-goal-2-spec-doc, task/59-goal-3-spec-doc sit behind those PRs.

**To do before your Sprint 2 review:**

1. Merge PRs #76 and #79 so all three epics have a spec on main; Sprint 2 is the spec deadline, so move #58 and #59 out of Sprint 3.
2. Fix the first line of docs/specs/data-extraction-spec.md to epic #11 and the stories it covers.
3. Close #78: choose Postgres RDS or Snowflake and update §4, architecture and ER diagrams together.
4. Add a system-context diagram and a sequence diagram for upload-extract-review-approve under docs/design/.
5. Create the FastAPI prototype skeleton with /health, .env.example and README run steps; delete login.py.
6. Remove [[story:#48]] from §4 and cite it in §2; add sp: to #63 and #67.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: public crime data map and pattern analysis

*Localhost web app that loads public crime records into SQLite and shows them on a filterable radius-search map.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Open the develop to main release PR so the three specs and all design diagrams are on main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #3, #14, #12 with objective-titled stories and tasks; Sprint 2 work assigned with sp:. Stray epics #6/#7, untyped #45-#47, and 19 story refs misplaced in §4. |
| 2. Specs | ✅ done | `docs/specs/crime-data-foundation.md` (develop) — epic #3, all sections, evidence-based; `docs/specs/crime-map.md` (main, develop) — epic #12, all sections; `docs/specs/crime-pattern-analysis.md` (develop) — epic #14, all sections |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ▫️ page flow. Needed for this project: ui_flow: map page with filter controls and detail panel; dfd L1: only one DFD level present. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop). Language: Python plus HTML/CSS/JavaScript; Framework: Flask, Leaflet.js; Platform: localhost, Python 3.12 in CI; Data: SQLite from a reviewed Costa Mesa snapshot; Hosting/hardware: team laptops; no hosted server; Sponsor resources: none; public open data; Tools: GitHub, venv, pytest CI. |
| 5. Prototype wiring | ⚠️ started | `prototype/schema.sql`, `normalize.py`, `load_db.py` with tests; `prototype/area_filter.py`, `crime_frequency.py` with tests; `prototype/README.md` is still the login scaffold; `prototype/requirements.txt` unchanged scaffold; no Flask |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release PR — two more specs, design docs, schema and loader sit on develop.

**To do before your Sprint 2 review:**

1. Open a develop to main release PR and merge it so specs, diagrams and prototype modules are on main.
2. Rewrite prototype/README.md and requirements.txt for your real stack and delete login.py and test_login.py.
3. Add a Flask app with /health and a Leaflet page as the toolchain smoke run, with install steps tested on a clean machine.
4. Draw a UI wireframe or page flow for the map and filters and add it to proposal §4 Diagrams.
5. Close #69 and #70, and clean the stray issues #6, #7, #45-#47.
6. Fix §4 so stories are cited only in §2; keep typed task refs there.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle Maintenance Logger

*Web app that tracks each vehicle's service history and recommends next services with due-soon alerts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Link `docs/specs/vehicle-data-and-tracking.md` in proposal §4, then open the develop to main release PR (#56).

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Two goal epics (#27, #28) with objective-titled stories #29-#38, all assigned with sp:. Sprint 2 stories and tasks are on the milestone, and 40 issues are typed-linked in the develop proposal. |
| 2. Specs | ✅ done | `docs/specs/vehicle-data-and-tracking.md` (develop) — epic #27; names stories #29-#33; `docs/specs/vehicle-selection.md` (develop) — story #29; overview and requirements; `docs/specs/vehicle-service-api.md` (develop) — story #30; REST CRUD and schema; `docs/specs/recommendations-and-alerts.md` (develop) — epic #28; stories #34-#38, four status labels |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ▫️ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: optional, import of service history; er, uml and ui_flow: all present; keep ER current as the proposed tables are built. |
| 4. Environment | ✅ done | Stated in: proposal §4.1-4.2 (develop). Language: Python, TypeScript; Framework: Flask; React, Tailwind CSS, Vite; Platform: Web app, desktop and mobile browsers; Data: SQLite (prototype); Hosting/hardware: To be determined; Sponsor resources: None; maintenance intervals from owner's manuals and dealer specs; Tools: GitHub Actions CI, VS Code, Node/npm, pytest, draw.io. |
| 5. Prototype wiring | ✅ done | `prototype/app.py` Flask API + `db/schema.sql`, `init_db.py` — vehicle API and seeded SQLite; `prototype/requirements.txt` pinned Flask/pytest; `package.json`; `web/` Vite+React; `prototype/.env.example`, `tests/smoke_test.py`, `tests/test_vehicle_api.py` — config template and smoke/API tests; `prototype/README.md` has Windows and Linux setup/run; still lists scaffold `login.py` |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release (task #56 open) — main lacks specs, diagrams, §4 and prototype; no open team PRs or unmerged branches; all Sprint 2 PRs (#58-#71) merged to develop.

**To do before your Sprint 2 review:**

1. Open and merge the develop to main release PR (#56) so main carries the specs, diagrams, §4 and prototype.
2. Add `docs/specs/vehicle-data-and-tracking.md` to the proposal §4 specification index, then close #49.
3. Resolve #59: update §3 (two labels) or the spec (four labels) so they agree, and close the issue.
4. Remove `prototype/login.py` and `tests/test_login.py`; document the smoke run and `.env.example` in `prototype/README.md`.
5. State the hosting choice (or localhost-only) in §4.1 with a reason, and decide whether a DFD for service-history import is worth adding.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak StableScope: stablecoin wash-trading detection (SNX)

*Builds transaction graphs from stablecoin data, flags wash trading with heuristics and ML, shows results in a dashboard.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Merge develop into main, then commit the prototype code (network.py and tests) that the README already describes.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #15, #23, #24 with objective-titled stories; only #31 is on Sprint 2. Nine task issues missing from proposal, #3 untyped, #67 and #59 lack sp:, #56 lacks milestone. |
| 2. Specs | ✅ done | `docs/specs/Epic-15-spec.md` (develop) — Goal 1, full sections; `docs/specs/Epic-23-spec.md` (main, develop) — Goal 2, all sections; `docs/specs/Epic-24-spec.md` (main, develop) — Goal 3, all sections |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml sequence: ingest, score, explain a wallet; ui_flow: investigation dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 and §4 (develop). Language: Python; Framework: dashboard undecided: Streamlit/Dash or React+FastAPI; Platform: laptops plus company warehouse; Data: SonarX SQL warehouse; Parquet/DuckDB, optional Neo4j (§3 only); Hosting/hardware: team laptops and sponsor machine; Sponsor resources: SNX-n SonarX data access and address labels; Tools: scikit-learn, GitHub, Discord. |
| 5. Prototype wiring | ❌ example files only | `prototype/README.md` describes network.py and 5 tests, but neither is in the file list; `prototype/login.py`, `tests/test_login.py` still present; `prototype/requirements.txt` only pins pytest; root `requirements.txt` is empty |

**Merge first** (not counted until it's in `develop` or `main`): PR #66 (open, develop) — proposal link changes for epic 23/24 specs; branch 50-spec_23_and24 — 1 commit not in develop; develop to main — Epic-15 spec, all design diagrams, prototype README.

**To do before your Sprint 2 review:**

1. Commit the prototype code the README describes (network.py and tests), or correct the README to match what exists.
2. Merge develop into main so the Epic-15 spec, five diagrams and sprint review land on main.
3. Choose the dashboard framework and local data store in §4, with a reason for each tied to §3.
4. Add a sequence diagram and a dashboard wireframe to docs/design/ and embed them in proposal §4.
5. Retitle the Epic-23 and Epic-24 specs and add the missing task issues to proposal §4 as typed refs.
6. Close #64 and #67 since PRs #65 and #68 merged, and add sp: to #59 and #67.

[↑ Back to all groups](#groups)

<a name="g11" id="g11"></a>

### G11 · 5Guys: Marathon Tracker App

*Mobile app that tracks marathon runners live, hosts shareable post pages and predicts finish times.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Merge develop into main so the architecture, context and sequence diagrams land, then embed them in proposal §4 Diagrams.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 (#4, #26, #27) with 6 objective-titled stories #28-#33 (sp, assignee). Sprint 2 tasks #42-#49 are linked. Sprint 1 tasks #3, #7-#9, #13, #17, #20, #34, #37, #38, #40 and three untyped meeting issues are not linked from §4. |
| 2. Specs | ✅ done | `docs/specs/live-runner-tracking.md` (main) — Goal 1 (#4, #28/#29); EARS FRs, NFRs, acceptance; `docs/specs/posts-and-shareable-page.md` (main) — Goal 2 (#26, #30/#31); scope and requirements, thin acceptance; `docs/specs/race-time-prediction.md` (main) — Goal 3 (#27, #32/#33); 5 percent accuracy target |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: GPS and posts move through Firebase; er: Firestore stores runs and posts; uml: live position update sequence; ui_flow: runner and spectator screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main); §3 is still a skeleton. Language: JavaScript/TypeScript (app, web); Python (race prediction); Framework: React Native with Expo; React for spectator page; Platform: Android and iOS via Expo; web; Data: Firebase Firestore, Firebase Auth, Cloud Storage; Hosting/hardware: Firebase Hosting; Sponsor resources: none (own project); Mapbox API key; Tools: VS Code, GitHub, Android Studio, Google Colab. |
| 5. Prototype wiring | ⚠️ started | `prototype/package.json` and lockfile: Expo, React Native; `prototype/.env.example` holds Firebase and Mapbox keys without secrets; `prototype/README.md` install, run, test; npm test only checks the config; `prototype/App.js` is a starter screen; no folders for runner app, spectator page, prediction; `prototype/requirements.txt` still scaffold copy |

**Merge first** (not counted until it's in `develop` or `main`): develop — PR #55 architecture, context and sequence diagrams (#46) not yet in main; develop is behind main on the proposal (§4 skeleton, 54 placeholders); sync main into develop.

**To do before your Sprint 2 review:**

1. Merge develop into main so `docs/design/architecture.md` (context, architecture, sequence) is on main, then close #46.
2. Embed the context, architecture, DFD, ER, sequence and screen-flow figures in §4 Diagrams with numbered captions.
3. Write §3 Proposed Approaches and tie each §4 stack choice to it; fix the `techstack.png` path.
4. Add the posts spec row to the §4 table and strengthen its acceptance criteria; remove the leftover scaffold rows.
5. Create the architecture-mirroring folders, init Firebase from `.env`, and add a smoke run that reads one Firestore document.
6. Link the unlinked Sprint 1 tasks in §4 as typed refs.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: 6G waveform and modulation identification with explainable AI

*Python tool that finds signal peaks in radio captures, classifies waveform/modulation, and explains decisions with Captum.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Draw the architecture and system-context diagrams for #126 and embed them in proposal §4; they are the largest missing Sprint 2 piece.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Five epics (#57-#61) with stories; Sprint 2 stories mostly closed and 45 typed refs in the develop proposal. Several stories lack a Sprint milestone or assignee; #126 has no milestone. |
| 2. Specs | ⚠️ started | `docs/baseline-peak-picker.md` (develop) — story #66; method and results, not a spec; `docs/captum-attribution.md` (develop) — story #64; handoff note, no FR/NFR; `docs/confidence-calibration.md` (develop) — story #65; handoff note; `docs/labeled-signal-dataset.md` (develop) — dataset contract for #66 Missing: epic #57 Signal Detection & Preprocessing; epic #58 Application interface and cross functional integration; epic #59 Waveform Identification & Receiver Processing; epic #60 Modulation, Decision & Explainable AI; epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: architecture and context: always required; dfd: signal to peaks to classifier to report; uml sequence: CLI, engine, classifier, explanation; ui_flow: CLI and GUI both planned; er: only if the labeled-dataset manifest is stored. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose, develop). Language: MATLAB and possibly Python stated in §4; Python in prototype; Framework: NumPy, SciPy, h5py, PyTorch, Captum, matplotlib (requirements.txt); Platform: Local desktop CLI; GUI toolkit not chosen; Data: Mentor-provided I/Q and HDF5 files plus a synthetic labeled set; Hosting/hardware: Not stated; Sponsor resources: Mentor scripts and dataset; MATLAB 6G Simulink library mentioned; Tools: pytest, GitHub Actions. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` pins numpy, scipy, h5py, torch, captum, pytest; `prototype/waveform_identification/` and `prototype/xai/` mirror the pipeline components; `prototype/data/sample/peak_picker_smoke.iq` with `scripts/analyze_iq.py` is the smoke run; `prototype/tests/` has four test files; login scaffold removed (PR #109); `prototype/README.md` has setup and run commands |

**Merge first** (not counted until it's in `develop` or `main`): branch `Application-Structure` — 5 commits not in develop; open a PR or drop it; branch `feature/114-captum-real-weights-h5` — 2 commits for #114, not in develop; branch `docs/team-documentation` — 1 commit not in develop; develop to main — Sprint 2 and 3 work sits on develop only.

**To do before your Sprint 2 review:**

1. Write one spec per epic in `docs/specs/` for #57-#61, naming epic and stories in the first lines, with FR/NFR, acceptance criteria and open questions.
2. Finish #126: draw architecture, system context and a DFD in `docs/design/` as Mermaid plus PNG, and embed them in proposal §4 Diagrams.
3. Add a sequence diagram for the CLI to peak picker to classifier to Captum flow, and a screen flow for the planned GUI (#63).
4. Rewrite proposal §4 environment as a reasoned table; resolve MATLAB versus Python and pick the GUI technology.
5. Add Sprint 3 milestone, assignee and sp: to #126, #63, #67, #68; link #126, #95, #96 from proposal §4.
6. Open PRs for `Application-Structure` and `feature/114-captum-real-weights-h5`, then merge develop into main.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. assignment manager

*Offline Windows desktop app that suggests deadlines by difficulty, tracks progress and sends native reminder notifications.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Add the architecture and system-context diagrams to `docs/design/` and proposal §4; specs and wireframes are already solid.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Three goal epics (#16-#18), objective-titled stories #19-#27, and 60+ feature/task issues, all typed-linked in the develop proposal. Several Sprint 2 items still open; #25-#27 have no milestone. |
| 2. Specs | ✅ done | `docs/specs/specs-G1.md` (develop) — epic #16, stories #22-#24; scope, FR, NFR, AC, questions; `docs/specs/specs-G2.md` (develop) — epic #17, stories #19-#21; same structure; `docs/specs/specs-G3.md` (develop) — epic #18, stories #25-#27; same structure |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: architecture and context: required, missing; er: local assignment storage; uml sequence: UI to IPC to Python core to storage; dfd: deadline and reminder data flow. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop). Language: Python core, JavaScript UI; Framework: Electron with Vite/React UI (prototype); Platform: Windows desktop, offline; Data: Local JSON or SQLite file storage; Hosting/hardware: Local machine, no hosting; Sponsor resources: None stated; Tools: GitHub Actions, pytest. |
| 5. Prototype wiring | ⚠️ started | `prototype/A.M.I.Y.A.core/` App.py, Database.py, services/, tests/TestAssignments.py; `prototype/A.M.I.Y.A.ui/` Electron main.js, React components, vite.config.js; `prototype/README.md` is still the unchanged course scaffold; `Package.json`, `Requirements.txt` capitalised and `scr/` misspelled; no `.env.example` or smoke run |

**Merge first** (not counted until it's in `develop` or `main`): PR #121 `feature/47-sprint-reports` — sprint reports; touches proposal and prototype README; branch `updated-proposal` — 6 commits not in develop; branch `feature/34-project-proposal` — 28 commits not in develop; likely stale; develop to main — specs, wireframes and prototype live only on develop.

**To do before your Sprint 2 review:**

1. Create `docs/design/architecture.md` and `system-context.md` with Mermaid diagrams and exported PNGs; list them in proposal §4 Diagrams.
2. Add an ER diagram for the assignment store and a sequence diagram for create-assignment; link from #13 and §4.
3. Rewrite `prototype/README.md` for A.M.I.Y.A.: setup, run and test commands that work on a fresh Windows machine.
4. Fix prototype casing (`package.json`, `requirements.txt`, `src/`) and add a smoke run proving the Python core starts and the UI loads.
5. Remove scaffold files `docs/specs/example-spec.md`, `docs/design/example-design.md`, `prototype/requirements.txt`; confirm CI passes.
6. Merge #121, then open a develop to main PR so the work lands on the default branch.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: AI-assisted incident-response training simulator

*Sandboxed desktop simulator for investigating fake malware incidents; an LLM generates validated scenarios and after-action reports.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Replace the scaffold prototype: PySide6/pydantic requirements plus a start_simulation.py window that runs (#60), then merge PR #89.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Two epics (#22, #23), 18 objective-titled stories #24-#41; Sprint 2 tasks assigned with sp:. Stories have no milestone, 14 placeholders remain, and story refs are cited in §4 instead of §2. |
| 2. Specs | ✅ done | `docs/specs/training-environment.md` (main, develop) — epic #22, stories #24-#32; scope, FR, NFR, AC; `docs/specs/ai-scenarios.md` (main, develop) — epic #23, stories #33-#41; capture shows scope and FR only |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: all six present; context diagram needs cleanup; keep ER current as the schema evolves. |
| 4. Environment | ✅ done | Stated in: proposal §4 'Environment and resources' table (main and develop). Language: Python 3.x; Framework: PySide6, Pydantic; Platform: Windows/macOS/Linux local desktop; Data: In-memory state; file fixtures; Hosting/hardware: Local machine only; Sponsor resources: None; NRP.ai LLM account and key; Tools: GitHub Actions, pytest, check_repo.py. |
| 5. Prototype wiring | ❌ example files only | `prototype/requirements.txt` unchanged course scaffold; no PySide6 or pydantic; `prototype/Dockerfile` (develop) contains only a TODO comment; `prototype/README.md` (develop) names `start_simulation.py`, which does not exist; main still has scaffold `login.py` and `tests/test_login.py` |

**Merge first** (not counted until it's in `develop` or `main`): PR #89 develop into main — carries sequence, context, README, Dockerfile that main lacks; branch `copilot/create-requirements-list-for-goal-2-47` — 1 commit not in develop; issue #88 (merge develop into main) — open; PR #89 would close it.

**To do before your Sprint 2 review:**

1. Replace `prototype/requirements.txt`, delete `login.py` and `tests/test_login.py`, and add PySide6, pydantic and pytest (#60).
2. Write `start_simulation.py` that opens a PySide6 window plus `tests/test_smoke.py`, and fix the README run and test commands.
3. Add `prototype/.env.example` with the NRP.ai key variable and no secret; implement or delete the TODO Dockerfile.
4. Correct `docs/design/system-context.md` (title, issue #54) and embed its exported image in proposal §4 Figure 2; close #54.
5. Merge PR #89 into main after CI passes so main carries every Sprint 2 document.
6. Remove the 14 template placeholders and move epic/story refs from §4 to §2 in proposal.md.
7. Add open-questions sections to both specs and link #79, #80, #84 in §4.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Constrained-hardware ECS game engine + game demo

*A lightweight C++/OpenGL ECS game engine for low-end hardware, with a game demo and scene editor.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Commit `prototype/src/main.cpp` and `src/glad.c` so the CMake build in `prototype/README.md` actually produces a window, then document the smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #24 Game Engine, #25 Game Demo, #6 Setting up; stories #26-#33 use objective wording. Stories all sit in Sprint 3 and no Sprint 2 story is on the board. |
| 2. Specs | ✅ done | `docs/specs/game-engine.md` (develop) - epic #24, stories #30-#33; scope, FR, NFR, acceptance, open questions; `docs/specs/game-demo.md` (develop) - epic #25, stories #26-#29; scope, FR traced to stories, NFR |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: asset load to render data flow; uml: sequence of one frame (input, ECS update, render); ui_flow: scene editor screens (Objective 2.4). |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (develop), still wrapped in placeholder text. Language: C++26; Framework: OpenGL 3.3 with SDL3, GLM, Glad, Assimp, stb_image; Platform: Windows and Linux builds (README); target low-end hardware not yet defined; Data: none stated (scene files saved by editor, format undecided); Hosting/hardware: not stated; 'resource-constrained hardware' has no spec; Sponsor resources: independent, none; Tools: CMake (proposal says 3.3-4.0, CMakeLists needs 3.30). |
| 5. Prototype wiring | ⚠️ started | `prototype/CMakeLists.txt` - find_package SDL3, assimp, glm; builds target run; `prototype/README.md` - Linux and Windows build and run commands; `prototype/lib/include/` - vendored glm, glad.h, stb_image headers; CMakeLists names `src/main.cpp` and `src/glad.c`; neither is on develop; README cites setup.sh/setup.ps1 (absent); test and status sections are still the login scaffold |

**Merge first** (not counted until it's in `develop` or `main`): develop to main - all Sprint 2 specs, diagrams and CMake wiring exist only on develop; main is still the scaffold.

**To do before your Sprint 2 review:**

1. Add `prototype/src/main.cpp` and `src/glad.c` so cmake -B build and the run target work; record the clean-machine smoke run in the README.
2. Add the missing setup.sh and setup.ps1 (or vcpkg.json) that the README cites, and delete the login test/status text.
3. Fix `docs/design/System Context Diagram.md`: real diagram, correct epic and story numbers, drop the login ER; add the figure to proposal §4.
4. Add a data-flow diagram and a frame-loop sequence diagram under `docs/design/` and surface both in proposal §4 with captions.
5. Convert proposal §4 and §2 refs to typed form like [[task:#9]](url) for all 19 unlinked issues (#46, #47, #48, #49, #61 and others); remove the angle brackets.
6. Move the Sprint 2 stories to the Sprint 2 milestone with assignees, and fix #28's body and #46's parent.
7. Open a develop to main release PR once the above merge.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Detects cross-chain bridge exploits from vault outflows against a learned baseline, with Slack alerts and a dashboard.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Resolve #28: get SonarX data access confirmed, because the live-stream source is the one box still drawn dashed in every diagram.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Three epics #11-#13 and stories in the objective's exact words; Sprint 2 work on board with assignee and sp; all 35 issues typed-linked from proposal §2 and §4. |
| 2. Specs | ✅ done | `docs/specs/goal-1-baseline.md` (main, develop) - epic #11, stories #14, #15; ingest lag and baseline measurement; `docs/specs/goal-2-detection.md` (main, develop) - epic #12, stories #5, #16-#19; three rules, acceptance per objective; `docs/specs/goal-3-dashboard.md` (main, develop) - epic #13, stories #20, #21; FR, NFR, open questions |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: done (D4); er: done (D3); uml: done (D5); ui_flow: done (D6). |
| 4. Environment | ✅ done | Stated in: proposal §4 Table 6, plus prototype README and .env.example. Language: Python 3.12; Framework: FastAPI; web dashboard page; Platform: Windows 11 verified, Ubuntu in CI; Data: SQLite; saved hack datasets as JSON; Hosting/hardware: Docker packaging; host not decided; Sponsor resources: SNX-3 SonarX data and real-time stream (requested, no reply); public Ethereum nodes meanwhile; Tools: pytest, GitHub Actions CI, Slack webhook, Chainlink feed fallback. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` and `requirements-dev.txt` - dependency manifests; `prototype/.env.example` - every BRIDGEWATCH_* setting with defaults, no secrets; `prototype/README.md` - fresh-machine commands, run modes, tests; `prototype/bridgewatch/` - source, detector, store, notifier, API mirror the architecture; `prototype/tests/` - four offline test files run in CI; `Dockerfile.bridgewatch` present |

**To do before your Sprint 2 review:**

1. Follow up the SonarX mentor on #28 and record the answer in proposal §4 Table 6 and the context diagram.
2. Decide a hosting target (the Docker image is built) and state it in Table 6.
3. Export D1-D6 from `docs/design/architecture.md` as images next to the Mermaid source.
4. Update proposal Figure 1 to match the prototype, or label it as the planned design.
5. Assign a Sprint milestone to epics #11-#13.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · SonicScape: galaxy-style music discovery map

*Python/Arcade app mapping genres, artists and songs as galaxies, with swipe feedback and SQLite user profiles.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Make the prototype run: one smoke command that opens the Arcade window, creates the SQLite file and calls Last.fm, with a test for it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Three goal epics (#21-#23) and objective-titled stories #25-#30, all with sp:; Sprint 2 tasks closed. Five §4 refs are bare, and the develop proposal has no typed refs. |
| 2. Specs | ✅ done | `docs/specs/specs_goal1.md` (main) — epic #21, stories #25-#26; all required sections; `docs/specs/specs_goal2.md` (main) — epic #22, stories #27-#28; all required sections; `docs/specs/specs_goal3.md` (main, develop) — epic #23, stories #29-#30; all required sections |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: all present; architecture needs more detail: Arcade, Last.fm, SQLite. |
| 4. Environment | ✅ done | Stated in: proposal §4 'Environment and Resources' table (main). Language: Python 3.10+; Framework: Arcade 2D; Platform: Desktop, local; Data: SQLite; Last.fm and NASA APIs; Hosting/hardware: Local machine (not stated explicitly); Sponsor resources: None; Last.fm API key and NASA open APIs; Tools: pytest, GitHub Actions, Mermaid. |
| 5. Prototype wiring | ⚠️ started | `prototype/src/sonicscape/` backend/lastfm.py, database/db.py, frontend/, recommender/ mirror the architecture; `prototype/.env.example` has LASTFM_API_KEY and DATABASE_PATH; `prototype/requirements.txt` arcade, requests, python-dotenv, pytest (unpinned); `prototype/README.md` says no code yet; `schema.sql` is empty; no tests |

**Merge first** (not counted until it's in `develop` or `main`): branch `develop` is stale (scaffold prototype, 66 placeholders); main holds all work, so sync or delete develop.

**To do before your Sprint 2 review:**

1. Make `prototype/src/sonicscape/main.py` run: open an Arcade window, create SQLite from `schema.sql`, and call Last.fm with the key from `.env`.
2. Add `prototype/tests/test_smoke.py`, fix the README run and test commands, and remove the leftover scaffold wording.
3. Fill `schema.sql` from `docs/design/goal3-er-diagram.mmd` and pin versions in `requirements.txt`.
4. Correct `docs/design/system_context.md` (Spotify versus Last.fm/NASA) and expand `architecture.md` to the real components.
5. Clean proposal §4: delete the template quote and 〈〉 notes, fix Goal 2 relative links, use typed refs for #42, #43, #46, #47, #53.
6. Replace 'Epic: #1' in design docs with #21-#23; sync or retire `develop`.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · ProStrats: Project Rogue

*2D action roguelite in Unity with weapon-and-element builds, shared combat and movement, and branching replayable runs.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Rename the Goal 1 spec to `.md` and add all three specs to the proposal §4 index table, then merge develop into main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Three goal epics (#29-#31), ten objective-titled stories (#32-#41), all assigned with sp:. Sprint 2 stories are on the milestone, but nine tasks (#53-#56, #58, #61, #64-#65, #72) are not linked in the proposal. |
| 2. Specs | ⚠️ started | `docs/specs/goal-2-action-gameplay-spec.md` (develop) — epic #30; scope, FR, NFR, acceptance, open questions; `docs/specs/replayable-run-structure.md` (develop) — epic #31; same section set, names stories #39-#41; `docs/specs/goal1-flexible-player-progression` (develop) — epic #29 from PR #69; file has no .md extension |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: uml class: present for combat classes; run/room/reward flowchart: present (run-room-reward-flowchart.svg); er: only if save files are adopted; ui_flow: only once menus/HUD are planned. |
| 4. Environment | ✅ done | Stated in: proposal §4 'Development environment and resources' (develop). Language: C#; Framework: Unity 6000.3.25f1, Universal 2D / URP, Input System, 2D physics; Platform: Downloadable Windows game; Data: None; no server or DBMS needed (save format undecided); Hosting/hardware: Developer PCs capable of the Editor; Windows build testing; Sponsor resources: None; placeholder art with credits; Tools: GitHub, Git workflow, C# editor, repo harness; Unity not covered by CI. |
| 5. Prototype wiring | ✅ done | `prototype/ProjectRogue/` Unity project with pinned `Packages/manifest.json`; `prototype/README.md` setup, run and test steps per scene; `Assets/Scenes/Test_Combat.unity` and `MovementFoundation.unity` as smoke scenes; `Assets/Scripts/Combat` and `Assets/Movement` folders mirror architecture boxes |

**Merge first** (not counted until it's in `develop` or `main`): feature/33-attributes-resources-respec — 2 commits not in develop; open a PR for #33; develop to main — main still has the skeleton §4, no specs, no design docs, no diagrams.

**To do before your Sprint 2 review:**

1. Rename `docs/specs/goal1-flexible-player-progression` to `.md` and link all three specs in the proposal §4 index with issues #53, #65, #61.
2. Add the unlinked issues (#53-#56, #58, #61, #64-#65, #72) to the §4 work-item table as typed refs.
3. Close duplicate tasks #54 and #56 (specs merged under #65 and #61), and set sp: on #61 and Sprint 2 on #58.
4. Resolve the §2 class wording versus the weapon-and-element direction in §3, and update #32 and #38 titles to match.
5. Surface the class diagram and run-room-reward flowchart as captioned figures in §4 Diagrams.
6. Open the PR for feature/33 into develop, then promote develop to main so the graded branch has the work.
7. Remove the scaffold `prototype/requirements.txt` and verify `.gitignore` covers Unity Library and Temp.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi

*Detect small drones and estimate position and movement from Wi-Fi CSI, evaluated against conventional radar (RTX-AST sponsor).* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Decide the capture stack and receiver, write it in proposal §4 Environment, then replace the login scaffold in `prototype/` with a capture smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Four epics (#2, #3, #4, #55) and stories titled as objectives. Epics #3 and #4 have no assignee, and seven issues (#37, #38, #39, #43, #51, #53, #65) are missing from the proposal. |
| 2. Specs | ✅ done | `docs/specs/wifi-csi-sensing.md` (develop, main) — epic #2; FR traced to stories, NFR, acceptance; `docs/specs/drone-detection.md` (develop, main) — epic #3; scope in/out, FR/NFR, acceptance criteria; `docs/specs/evaluation.md` (develop, main) — epic #4; metrics, evaluation design, acceptance criteria Missing: epic #55 Team Process & Documentation has no spec (non-technical; optional). |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er or dataset-layout sketch: timestamped recordings and labeled datasets; ui_flow: not needed; no user interface; dfd for classifier and evaluation flow: only capture L0/L1 exist. |
| 4. Environment | ⚠️ partial | Stated in: spec §6 and DFD text; proposal §4 environment is still a skeleton. Language: not stated; Framework: not stated (ML library, CSI tool unnamed); Platform: not stated (receiver OS, capture firmware unconfirmed); Data: Timestamped CSI files in a documented format (format not chosen); Hosting/hardware: GL.iNet GL-MT3000 transmitter, Seeed XIAO microcontroller, receiver unconfirmed; Sponsor resources: RTX-AST sponsor; drone and radar comparison access not stated; Tools: GitHub, Mermaid. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `prototype/tests/test_login.py` still the course example; `prototype/requirements.txt` is the unchanged course scaffold copy; `prototype/.env.example` has only CAPTURE_INTERFACE, SAMPLE_RATE, OUTPUT_DIR; `prototype/README.md` keeps scaffold text and the login table row |

**Merge first** (not counted until it's in `develop` or `main`): feature/#51-section4-update — 2 commits not in develop; its goal is already met, merge or close; develop to main — main lacks the architecture, context and sequence images.

**To do before your Sprint 2 review:**

1. Complete proposal §3 and §4 environment: language, capture firmware, receiver, OS, ML stack, test site, drone source, each with a reason tied to §3.
2. Replace `prototype/login.py`, `prototype/tests/test_login.py` and the scaffold `requirements.txt` with a CSI capture smoke run and real dependencies.
3. Rewrite `prototype/README.md` with fresh-machine setup, run steps and a smoke test of one captured frame.
4. Add the architecture, context and sequence figures with captions to proposal §4 Diagrams, and extend the DFD to classification and evaluation.
5. Close #51 (specs are in the §4 index), delete the placeholder rows, and link #39, #53, #65 in the work-item table.
6. Assign epics #3 and #4, add sp: to #37, #38, #51, and merge develop into main.
7. Add a dataset layout or ER sketch for recordings, labels and quality reports under `docs/design/`.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia

*First-person Unreal Engine 5 horror maze game with adaptive monsters driven by an AI horror director.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Finish issue #54: draw the architecture and system context diagrams in Mermaid, export them to `docs/design/`, and add them to proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Three goal epics (#12, #17, #21) with objective-titled stories #13-#15, #18-#20, #22-#23, all assigned with sp:. Epics and stories sit on Sprint 4, tasks on Sprint 3, and 12 issues are missing from the proposal. |
| 2. Specs | ⚠️ started | `docs/specs/exploration-experience.md` (develop, main) — epic #12; objectives 1.1-1.3, testable requirements; `docs/specs/suspense-threats.md` (develop, main) — epic #17; two monster types, encounters, evasion; `docs/specs/immersion-environment.md` (develop, main) — epic #21; visibility and audio, short |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for any project; uml state: monster states and horror director; dfd: director reads game state, drives NPCs; ui_flow: menu, HUD, game over screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 'Environment and Resources' (develop). Language: Blueprints (visual scripting); C++ not mentioned; Framework: Unreal Engine 5 (5.8.3 per README); Platform: Windows 10/11; Data: None stated (save or progression data undecided); Hosting/hardware: Developer PCs able to run UE5; Git LFS for assets; Sponsor resources: None; Tools: VS Code, Git/GitHub, Git LFS, Tripo, Blender. |
| 5. Prototype wiring | ✅ done | `prototype/Insomnia.uproject` with `Config/` and `Content/` UE5 first-person template (develop); `prototype/README.md` requirements, install and run steps with Git LFS; README smoke test: project opens, starter level loads, movement works; no secrets involved; `.env.example` not required |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — main holds only specs and the §4 table; UE5 skeleton (PR #60) and §4 environment (PR #61) are on develop only.

**To do before your Sprint 2 review:**

1. Create architecture, system context and monster state diagrams with Mermaid source and images in `docs/design/` (issue #54) and caption them in proposal §4.
2. Write proposal §3 Proposed Approaches: AI horror director, maze variation and audio, with alternatives and reasons (issue #55).
3. Link the 12 missing issues in §4 and convert the bare refs for #39-#52 to typed refs.
4. Strengthen the three specs: scope in/out, non-functional requirements, story traceability and open questions; correct the 'Story' labels on epics.
5. Put the remaining Sprint 2 work on the board with sp: and the Sprint 2 milestone; all tasks sit on Sprint 3 and epics on Sprint 4.
6. Add a data-flow or sequence diagram for the horror director and NPC behaviour.
7. Merge develop into main, and confirm the prototype folder has no leftover scaffold files.

[↑ Back to all groups](#groups)

## What this page no longer checks

Sprint 1 is graded and closed, so its checks are gone from this page: the Sprint 1 milestone counts, the HW#5 Goals & Objectives comparison, instructor pull requests, the Word export, and the per-issue story-point and assignee lists. The rules behind them still hold (see [README §4–§6](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board)), and the harness in your Actions tab still checks them on every pull request. The proposal-vs-board editions are in this file's git history.
