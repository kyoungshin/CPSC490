# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-11-03 20:31 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G01](#g01) BGAF | Tue Oct 27 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [G02](#g02) LinuxLarpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ⚠️ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) EpicEngineers | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ |
| [G05](#g05) WILS | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ✅ | ⚠️ |
| [G07](#g07) Mighty Morphins | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ❌ | ⚠️ | ⚠️ | ✅ |
| [G13](#g13) BYKX | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G16](#g16) Neuroprosthetic | Thu Nov 5 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [G17](#g17) EchoSphere (SonicScape) | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ⚠️ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 15 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G07, G08, G09, G10, G11, G13, G14, G15, G16, G17, G19).
- **Design and diagrams:** 17 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G07, G08, G09, G11, G12, G13, G14, G15, G16, G17, G18, G19).
- **Environment:** 17 of 20 have written their environment choices into the repository (G01, G02, G03, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G18, G19).
- **Prototype wiring:** 14 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G02, G03, G05, G06, G08, G09, G11, G12, G13, G15, G16, G18, G19).
- **Waiting in a branch or open pull request:** G02, G03, G05, G06, G07, G08, G10, G12, G13, G14, G19. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting pipeline

*Rebuilds Hyperliquid order books from SonarX data, measures accuracy, and backtests strategies only on validated market-days.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Resolve the conflicts on PR #189 (issue #218) and merge it, then merge PR #193; both are finished documentation still outside main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | 3 goal epics (#20-22) and 16 objective-titled stories; 7 Sprint 2 stories closed with assignee, sp and milestone; all 138 issues linked in proposal §2/§4 as typed refs. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1; requirements traced to stories, open questions listed; `docs/specs/validation.md` (main) — Goal 2; match rate, gate threshold, dated market events; `docs/specs/backtest.md` (main) — Goal 3; fill model, costs, strategies, metrics |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: data cleaning and storage pipeline; er: five stored entities in DuckDB; uml: sequence for the market-day flow; ui_flow: React research workspace. |
| 4. Environment | ✅ done | Stated in: proposal §4. Language: Python 3.12 (CI version), decimal for exact prices; TypeScript for front end; Framework: React + Vite front end; one `bgaf_pipeline` package; pytest 8.3.5; Platform: Team laptops and GitHub Actions Linux runners; Node 20.19+/22.12+; Data: DuckDB 2.0.0 with DECIMAL(38,18); Parquet per market-day recommended; Hosting/hardware: Nothing hosted yet; front-end hosting open in `docs/design/frontend-architecture.md` §6.5; Sponsor resources: SonarX L2/L4 data via requester-pays S3 and Snowflake trial share; AWS accounts in `prototype/.env`; Tools: GitHub, Actions CI, Mermaid diagrams, pandoc Word export, Claude Code. |
| 5. Prototype wiring | ✅ done | `prototype/src/bgaf_pipeline/` — one module per pipeline step, mirrors architecture; `prototype/requirements.txt`, `pyproject.toml`, `.env.example` — manifests, no secrets; `prototype/tests/test_storage.py` — DuckDB schema and one SonarX sample load; `prototype/frontend/` — Vite React TypeScript skeleton with package.json; `prototype/README.md` — setup, smoke run and test commands; login.py removed (PR #198) |

**Merge first** (not counted until it's in `develop` or `main`): PR #193 — extends the data model to an EER diagram in `docs/design/database.md` (#175); PR #189 — front-end architecture in `docs/design/frontend-architecture.md` and proposal §4 (#187); has conflicts (#218).

**To do before your Sprint 2 review:**

1. Fix PR #189 per #218 (conflicts, two issue links) and merge it so the front-end architecture reaches proposal §4.
2. Review and merge PR #193 so the EER diagram replaces the plain ER figure in proposal §4.
3. Add the wireframe and front-end screen-flow figure, with a caption, to proposal §4 Diagrams.
4. Add the Sprint 3 issues #205-#219 to the board and give sub-tasks #212-#217 an sp: label.
5. Move the [[task:#195]] reference from §7 to §4 so work items stay in one section.
6. Close or accept each open question in the three specs before building starts in Sprint 3.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · LinuxLarpers: Distributed Signal Capture for Multi-Node Analysis

*ESP32 nodes capture Wi-Fi and Bluetooth metadata of nearby recording devices; a backend identifies them and a dashboard shows them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Write proposal §4 (#105) with the environment choices and the design-document table, and merge develop into main so the diagrams and the FastAPI skeleton reach main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#47, #50, #56) and 16 objective stories exist, but only 18 of 65 issues are linked from the proposal, and Sprint 2 board work is tasks only. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Goal 1 (#47): collect wireless signal metadata; Goal 2 (#50): identify selected recording devices; Goal 3 (#56): present observations on a dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence for capture, upload, identify flow; ui_flow: dashboard screens in Goal 3; er: PostgreSQL stores (diagram exists); dfd: data moves ESP32 to server (exists). |
| 4. Environment | ⚠️ partial | Stated in: issues #79/#91 and `docs/design/system-context.md`; proposal §4 is still a skeleton. Language: Python 3.12 backend; C/C++ firmware; TypeScript for Angular (inferred from issues); Framework: FastAPI backend, Angular dashboard, ESP32 firmware (issue #91); Platform: ESP32 capture nodes, laptop or Raspberry Pi per HW#4; Data: PostgreSQL with six stores (DFD Level 1); Hosting/hardware: ESP32 order list; own server under discussion after Lightsail was ruled out (#102); Sponsor resources: RTX sponsor guidance: free or open-source tooling, demoable real-time data (#101); Tools: GitHub, Gitflow, draw.io, uv/pip. |
| 5. Prototype wiring | ⚠️ started | `prototype/backend/main.py` (develop) — FastAPI app with /health endpoint; `prototype/backend/pyproject.toml`, `requirements.txt`, `uv.lock` (develop) — dependency manifests; `prototype/backend/test_main.py` (develop) — smoke test for the backend; `prototype/README.md` (develop) — backend setup, run and test commands; main still has course `prototype/login.py` and `tests/test_login.py` |

**Merge first** (not counted until it's in `develop` or `main`): develop (PRs #85, #90, #96, #98) — architecture, DFD, context diagram, FastAPI scaffold; not yet in main; PR #103 — syncs main into develop; open; branch `feature/23-approach-environment` — 10 commits incl. §4 Lightsail text, not in develop; branch `feature/86-lightsail-hosting` — 2 commits, not in develop.

**To do before your Sprint 2 review:**

1. Write the three specs in `docs/specs/` (Goal 1 #47, Goal 2 #50, Goal 3 #56) and link them in proposal §4.
2. Write proposal §4 (#105): environment table with reasons, the Specification and design documents table, and the figures with captions.
3. Add `docs/design/architecture.md`, a sequence diagram of capture to dashboard, and dashboard wireframes; update system-context for #102.
4. Finish #92, #93 and #94 so `prototype/esp32/`, `prototype/database/` and `prototype/dashboard/` exist with smoke runs, then add `.env.example`.
5. Link the 47 unlinked issues in proposal §4, and add sp: to unpointed tasks #97, #99, #102, #104, #105.
6. Merge develop into main through a reviewed PR so the architecture, DFD and backend skeleton count.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: equation-to-model Jupyter notebook pipeline

*A Jupyter notebook that transcribes an equation from image, LaTeX or code, generates data, trains a PyTorch model and plots results.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Fix `prototype/requirements.txt` and `prototype/README.md` for the real PyTorch and Jupyter stack with a smoke run, since both are still the course template.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 4 goal epics (#28, #27, #43, #44) and objective-titled stories; Sprint 2 stories assigned with sp. Stories #45, #47 lack a milestone; 18 of 41 issues are linked from the proposal. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (main) — Epic #28 Goal 1; stories listed, draft; `docs/specs/data-generation.md` (main) — Epic #27 Goal 2; five stories, owners partly unconfirmed Missing: Epic #43 Goal 3: Train a model; Epic #44 Goal 4: Output in a Jupyter notebook. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: ui_flow: notebook cell flow and where users enter input; er: only if dataset store is a relational database. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 and HW#4 only; §4 Environment and resources still a placeholder. Language: Python (code in prototype/); Framework: PyTorch for training, chosen over TensorFlow (§3); Platform: Jupyter notebook as the only UI, required by the sponsor (§3); Data: CSV or relational database, undecided (story #34); Hosting/hardware: Local run for training; no hosting stated; Sponsor resources: External AI for transcription and data parameters (Mathpix named in HW#4); RTX approved outside APIs on Oct 21; Tools: GitHub, Mermaid, CI workflows. |
| 5. Prototype wiring | ⚠️ started | `prototype/verifier.py` and `tests/test_verifier.py` — real verifier code and test; `prototype/transcriber.py`, `generate_dataset.py`, `train.py` — pipeline step modules exist; `prototype/README.md` — still the course template (login.py text); `prototype/requirements.txt` — unchanged course scaffold, no dependencies listed; No `.env.example` and no notebook file in `prototype/` |

**Merge first** (not counted until it's in `develop` or `main`): develop — PRs #61, #62, #63, #64, #67 (specs, diagrams, CSV data) ahead of main; main has Release v0.2 (#66); branch `feature/46-plot-equation` — 1 commit, plotting, not in develop; branch `feature/50-transcriber` — 2 commits, transcriber work, not in develop.

**To do before your Sprint 2 review:**

1. Write the Goal 3 and Goal 4 specs (#71, #72) in `docs/specs/` and add them to the proposal §4 document table with working links.
2. Write proposal §4 Environment and resources: language, PyTorch, Jupyter, recognizer and LLM services, data store, with reasons.
3. Rewrite `prototype/README.md` and `requirements.txt` for the real stack, add `.env.example`, and run a smoke test that imports torch and runs `verifier.py`.
4. Add a notebook-flow diagram showing user input cells and outputs, and surface it in proposal §4 Diagrams.
5. Link every remaining issue (#65, #69, #70, #71, #72, #60) in proposal §4 and give #45 and #47 a milestone.
6. Merge `feature/46-plot-equation` and `feature/50-transcriber` into develop through reviewed PRs, then release to main.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · EpicEngineers: Polymarket wallet PNL and trader-ranking dashboard (SNX-1)

*Computes profit and loss for Polymarket proxy wallets from SonarX Snowflake data, ranks traders, and serves a dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Hold a team decision on the prototype stack (#52) and record it in proposal §4; it blocks the architecture update, the implementation plan and the prototype skeleton.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#24, #29, #33) and 15 objective-titled stories with assignees and sp; Sprint 2 stories #25, #34 on board. Only 40 of 94 issues are linked from the proposal. |
| 2. Specs | ⚠️ started | `docs/specs/pnl-calculation.md` (main) — Epic #24 Goal 1; FIFO and PNL formulas, worked example; `docs/specs/trader-ranking.md` (develop) — Epic #29 Goal 2; ranking, win rate, behavior metrics, not in main Missing: Epic #33 Goal 3: client dashboard (draft in open PR #73, `docs/specs/dashboard-questions.md`). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: Snowflake to PNL to ranking to dashboard; er: positions, lots, wallet PNL tables; uml: sequence for one PNL run (#59); ui_flow: leaderboard and wallet pages (#60). |
| 4. Environment | ❌ not started | Stated in: nowhere beyond Snowflake; stack decision #52 is open. Platform: Snowflake warehouse (confirmed with sponsor); Data: SonarX Polygon data in Snowflake; own tables for positions, lots, PNL; Sponsor resources: SonarX Snowflake access, credentials pending; open-source tools allowed; Tools: GitHub, Mermaid, CLAUDE.md. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` — unchanged course example on main and develop; `prototype/requirements.txt` and `README.md` — course scaffold, no team content; `docs/design/implementation.md` (main) — proposed prototype layout, blocked on #52 |

**Merge first** (not counted until it's in `develop` or `main`): PR #135 — Sprint 3 repo fixes: architecture, DFD L0/L1 diagrams, implementation, proposal; PR #81 — revised architecture and system context diagrams; PR #79 — dashboard flow design and diagram (#60); PR #73 — dashboard questions spec for Goal 3 (#34); PR #72 — Sprint 2 review draft; develop (trader-ranking spec, §3) not yet in main.

**To do before your Sprint 2 review:**

1. Decide the stack in #52 (language, dashboard framework, Snowflake connector, hosting) and write proposal §4 Environment and resources with a reason for each.
2. Merge PRs #135, #81, #79 and #73, resolving conflicts, so DFD, architecture, dashboard flow and the Goal 3 spec reach develop.
3. Write `docs/design/data-model.md` with an ER diagram (#57) and `docs/design/pnl-pipeline.md` with a sequence diagram (#59).
4. Replace login.py with the chosen skeleton in `prototype/` (#62): manifest, `.env.example`, README commands, and a Snowflake smoke run.
5. Fix the first line of `docs/design/architecture.md` to name stories by number and show every figure with a caption in proposal §4 Diagrams.
6. Release develop to main through a reviewed PR and link the unlinked issues (#126-#134 and others) in proposal §4.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · WILS: Whale Identification/Location System

*Detects whale calls in hydrophone audio and estimates call direction and distance from time differences.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge PRs #54, #55 and #48, then write `docs/specs/goal-1-detector.md` for epic #8 (stories #9-#13) using the Goal 2 spec as the model.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 goal epics (#8, #14) and 9 objective stories; Sprint 2 stories have assignee, sp and milestone. Only 11 of 31 issues are linked from proposal §4; #57, #58, #47 lack sprint and sp. |
| 2. Specs | ⚠️ started | `docs/specs/goal-2-locator.md` (develop) — Goal 2 epic #14, stories #15-#18; FR table, scope, strong Missing: epic #8 Goal 1: whale-call recognizer (stories #9-#13). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: audio flows detector to locator to store; er: whale-call database (schema.sql exists); uml: sequence for detect-then-locate flow. |
| 4. Environment | ⚠️ partial | Stated in: README / repo files only; proposal §4 is still the template skeleton. Language: Python; Framework: torch, librosa, scipy, numpy (`prototype/requirements.txt` on develop); Platform: local venv; Windows and Mac/Linux commands in README; Data: PostgreSQL via `docker_compose.yaml`, `db/init/schema.sql`, `seed.sql` (main); Hosting/hardware: local machine and Docker; not stated in proposal; Sponsor resources: hydrophone recordings and whale-call data sources not stated; Tools: pytest, GitHub Actions CI, Docker. |
| 5. Prototype wiring | ✅ done | `prototype/locator/` TDOA package with `smoke.py` end-to-end run (develop); `prototype/ai-detector/` whale, boat, ambient converters and detector (develop); `prototype/requirements.txt` pinned numpy, scipy, torch, librosa; `.env.example` present (develop); `prototype/tests/test_tdoa.py`, `test_locate.py`, `test_save_call.py` (develop); `docker_compose.yaml` and `db/init/schema.sql` on main only |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 (open, develop to main) — Goal 2 spec, locator, ai-detector, README, `.env.example`; PR #55 (open, develop) — `docs/design/locator-design.md` plus proposal edits (#49); PR #54 (open, develop) — lists all work items in proposal §4 (#53); develop lacks `db/` and `docker_compose.yaml` from main; sync both branches.

**To do before your Sprint 2 review:**

1. Merge PR #54, #55, then #48; verify main ends with spec, design doc, locator, detector and `docker_compose.yaml`.
2. Write `docs/specs/goal-1-detector.md` for epic #8 (stories #9-#13) using the Goal 2 spec as the model, and link it in §4.
3. Draw system context, architecture and DFD in `docs/design/` with editable source; export the ER diagram from `schema.sql` and link all four in §4 Diagrams.
4. Replace the template text in proposal §3 and §4 Environment and resources with real choices and reasons.
5. Fix README: drop `login.py`, add Postgres/Docker start and a DB smoke check, correct `requirements.txt` header.
6. Add sp: and a Sprint milestone to #57, #58; type #47 and #23; keep the board current.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Generates practice questions from a student's own course materials and targets the concepts they keep missing.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write the Goal 2 spec (`docs/specs/weak-spot-tracking.md`, epic #20, stories #21-#26), since the mastery, forgetting and selection code already gives you the requirements.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#13, #20, #27) and objective-titled stories exist; stale closed epics #3/#4 remain. Sprint 2 stories #21-#26 are on the Sprint 2 milestone, but #24, #25 and #26 have no assignee. #25 has no sp. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #13 Goal 1 (generate, grade, summarize); epic #20 Goal 2 (weak-spot tracking); epic #27 Goal 3 (web app, reminders, user study). |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: documents flow through extraction, questions and mastery; er: SQLite stores per-student mastery data; uml: sequence for the generate-grade-update loop; ui_flow: web app with dashboard and practice view. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop). Language: Python 3; Framework: Flask; Platform: Web app (browser); Data: SQLite (per-student mastery data); Hosting/hardware: Render free tier, deploys from GitHub; Sponsor resources: Anthropic Claude API (Python SDK); Tools: GitHub issues/PRs/Actions CI, pytest. |
| 5. Prototype wiring | ⚠️ started | `prototype/document_processor.py` + `concept_extractor.py` (develop) — real extraction code with tests; `prototype/forgetting.py`, `question_selector.py`, `question_generator.py` — logic modules, each with a test file; `prototype/requirements.txt` lists pypdf, python-docx, python-pptx, pytest only; `prototype/README.md` is still the course login text; `login.py` remains; no `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #39 (open, base main) — mastery tracking for #21; retarget to develop and merge; feature/question-generator, feature/question-selector — 2 commits each not in develop; feature/14-document-upload, feature/proposal-environment — 1 commit each not in develop; develop to main release — main lacks §4 content and all prototype modules.

**To do before your Sprint 2 review:**

1. Write `docs/specs/` documents for epics #13, #20 and #27, naming the epic and stories in the first lines, and link them from proposal §4.
2. Draw architecture and system context diagrams in `docs/design/` (Mermaid plus PNG) and add them as captioned figures in proposal §4 Diagrams.
3. Add ER and sequence diagrams for the SQLite mastery model and the question-generate/grade/update loop; add a DFD and page flow if the UI is planned.
4. Retarget PR #39 to develop and merge it; merge or close the four unmerged feature branches.
5. Replace the scaffold README and `login.py`; add Flask, anthropic and `.env.example`; add a smoke run to the README.
6. Assign #24, #25, #26, add sp: to #25, close #41 now that PR #42 merged, and restore typed refs (`[[task:#41]]`) in develop proposal §2 and §4.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphins: Online Materials Database (EL-1)

*Extract data from material CoC and test-report PDFs into a verified, searchable relational database with a web UI.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Merge PRs #72, #74 and #75 together so main has architecture, wireframes and the AWS tech stack, then fix the empty figure and spec links in proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #11, #17, #22 with objective-titled stories #12-#27, plus Goal 0 epic #42 (stories #48, #49). Stories #12-#27 have no milestone or assignee. #67 and #63 lack sp. Develop proposal is a skeleton. |
| 2. Specs | ⚠️ started | `docs/specs/data-extraction-spec.md` (main) — Goal 1 (#11); scope, 5 FR, 2 NFR, criteria, questions; header cites epic #42 and task #46, not #11 and #12-#16 Missing: epic #17 Goal 2 (centralized storage); #58 open, §4 link is empty; epic #22 Goal 3 (access and analysis); #59 open, §4 link is empty. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence for upload, extract, verify, store; ui_flow: web app for upload, review queue and search; dfd and er: both present on main. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main); AWS stack only in open PR #75. Language: Python; Framework: TBD (backend and frontend); Platform: Internal web application; Data: Relational DB on AWS; DBMS TBD; Hosting/hardware: AWS (services named only in PR #75); Sponsor resources: EL-1 CoCs and material test reports (PDF); sample documents pending; Tools: VS Code, Git/GitHub; OCR and PDF library TBD. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `tests/test_login.py` — unchanged course example; `prototype/requirements.txt` — unchanged scaffold copy; `prototype/README.md` — still course login text, no project setup or run |

**Merge first** (not counted until it's in `develop` or `main`): PR #72 (open, main) — system architecture diagram + PNG for #39; PR #74 (open, main) — UI wireframes (SVG/PNG/Figma export) for #41; PR #75 (open, main) — tech stack and AWS services for §4, #47; PR #73 (open, main) — fixes proposal issue links (#67); develop is a skeleton; all team work is on main.

**To do before your Sprint 2 review:**

1. Merge PRs #72, #74, #73 and #75 into main; fix the empty `[System Architecture]` image and the two empty spec links in proposal §4.
2. Write the Goal 2 (#58) and Goal 3 (#59) specs in `docs/specs/`, each with FR/NFR traced to stories, criteria and open questions.
3. Add a system context diagram and a UML sequence diagram for upload, extract, verify and store; list both in proposal §4.
4. Decide the TBD items (DBMS, frameworks, OCR/PDF library) in §4 with reasons tied to §3; record how sample EL-1 documents will be handled.
5. Replace the scaffold prototype: pinned `requirements.txt`, `.env.example`, folders for extraction, API and DB, README setup and a smoke run on a sample PDF.
6. Give stories #12-#27 an owner and sprint (or state Sprint 3 start), add sp: to #67 and #63, and use typed refs `[[task:#N]]` for the 21 bare links.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: public crime data explorer with interactive map

*Collect public crime records, standardize them in a database, and explore them on a map with radius search.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Merge PR #71, then open the develop to main release so the specs, diagrams and §4 text reach the default branch.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #3, #14, #12 with objective-titled stories. Duplicate untyped copies #45, #46, #47 (no type label) sit beside #13, #21, #22. #69/#70 open and not in §4. Main proposal is a skeleton. |
| 2. Specs | ⚠️ started | `docs/specs/crime-map.md` (develop) — Goal 3 (#12); scope, FR/NFR, criteria; stories #13, #21, #22; `docs/crime-data-format.md`, `docs/crime-data-sources.md` (develop) — Goal 1 content, not in `docs/specs/`; `docs/crime-pattern-analysis.md` (develop) — Goal 2 content, prototype analysis only Missing: epic #3 Goal 1 needs a spec with FR/NFR traced to #4, #5, #28; epic #14 Goal 2 needs a spec traced to #15, #16. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ▫️ page flow. Needed for this project: dfd: import and normalize, then query pipeline; er: SQLite stores incident records; uml: radius-search sequence for the critical flow; ui_flow: interactive map with filters and radius. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop). Language: Python, JavaScript; Framework: Flask; Leaflet.js; HTML/CSS/JS; Platform: Localhost, modern browser; Data: SQLite file; Hosting/hardware: None planned; localhost prototype; Sponsor resources: Public crime data (Costa Mesa layer under evaluation); basemap provider unresolved; Tools: GitHub, Python 3.12 CI, virtualenv. |
| 5. Prototype wiring | ⚠️ started | `prototype/schema.sql`, `load_db.py`, `normalize.py` — SQLite schema, normalizer and loader with tests; `prototype/area_filter.py`, `crime_frequency.py` — standalone logic with synthetic-data tests; `prototype/requirements.txt` — unchanged scaffold; no Flask or Leaflet; `prototype/README.md` is still course login text; no Flask app or `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #71 (open, base develop) — data flow and radius-search sequence diagrams; branch docs/sprint2-diagrams — 9 commits not in develop (same work); develop to main release — main has no team spec, design or prototype work.

**To do before your Sprint 2 review:**

1. Merge PR #71, then list data-flow, sequence and ER documents with figures in proposal §4 and correct the 'ER not delivered' sentence.
2. Write Goal 1 and Goal 2 specs in `docs/specs/`, reusing `docs/crime-data-format.md` and `docs/crime-pattern-analysis.md` for scope and requirements.
3. Draw a map-screen flow or wireframe for the filter, radius and marker-detail interaction and add it to §4 Diagrams.
4. Replace the scaffold `requirements.txt`, README and `login.py`; add Flask, `app.py`, a Leaflet page, and a smoke run reading the SQLite file.
5. Close #45-#47 as duplicates, add #58, #69, #70 to §4 with typed refs, and open the develop to main release PR.
6. Choose the final data source and basemap provider in §4 with a reason tied to §3.

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

### G10 · Team Jiddak: StableScope

*Graph analysis and explainable wash-trading detection on stablecoin transactions, with an investigator dashboard (SNX-3).* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Create `docs/design/architecture.md` with a Mermaid pipeline diagram (SonarX, graph, detection, dashboard) and link it from proposal §4, because design is entirely missing.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#15, #23, #24) and 15 objective stories, titled "Objective N.N: ...". Only #31 is in Sprint 2; #59 has no sp:, #56 has no milestone; 8 issues not linked in proposal. |
| 2. Specs | ⚠️ started | `docs/specs/Epic-23-spec.md` (develop, main) — epic #23 detection; FR/NFR table traced to stories; [N] placeholders remain; `docs/specs/Epic-24-spec.md` (develop, main) — epic #24 dashboard; requirements traced; still draft; `docs/specs/Epic-15-spec.md` (PR #63, open) — epic #15 network model; not on develop yet Missing: epic #15 Goal 1: Network Model (spec only in open PR #63). |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: pipeline from SonarX through graph to scores; er: Parquet/DuckDB and graph tables; uml: sequence for ingest-detect-score flow; ui_flow: investigator dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 and §4. Language: Python (pipeline, detection, ML); Framework: Streamlit/Dash or React+FastAPI undecided; scikit-learn for Isolation Forest/LOF; Platform: Laptops/desktops; Company machine for heavy compute; Data: SonarX warehouse SQL; Parquet + DuckDB; optional Neo4j; Hosting/hardware: Team laptops, warehouse machine; Sponsor resources: SonarX stablecoin transaction logs (SNX-3), USDT/USDC on Ethereum; Tools: GitHub branches/PRs, Discord. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` still the course example; `prototype/README.md` describes `network.py`, but that file is not on main or develop; `prototype/requirements.txt` lists only pytest==8.3.4; no .env.example |

**Merge first** (not counted until it's in `develop` or `main`): PR #63 — renames Goal 1 spec to `docs/specs/Epic-15-spec.md` and updates proposal.md; Branch docs/N-rename-epic-15-spec — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #63 so the epic #15 spec reaches develop, then fix the 'Account management' title in all three specs.
2. Create the architecture and system-context diagrams in `docs/design/` (Mermaid) and surface them with captions in proposal §4.
3. Add DFD, ER and dashboard wireframe diagrams, since the project stores graph data and has a UI.
4. Replace login.py/test_login.py with the network.py prototype from README; pin the real dependencies in requirements.txt.
5. Add a 'Specification and design documents' subsection in proposal §4 linking `docs/specs/Epic-15/23/24-spec.md` and the design docs.
6. Fill the [N]/[K] placeholders and open-questions table in Epic-23 and Epic-24 specs.
7. Link #59, #56, #51, #50, #46, #45, #42, #5 in proposal §4 and fix their sp:/milestone labels.

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

### G12 · ACJMM: Explainable 6G Waveform Classification

*Detect signal peaks, classify 6G waveforms and modulation, and explain each decision with Captum (RTX-1).* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Write `docs/specs/epic-60-spec.md` (Modulation, Decision & Explainable AI), the epic with the most built, then repeat for the other four epics.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 5 epics (#57-#61) and about 15 stories, all linked; Sprint 2 stories mostly closed. Stories #63, #67, #68, #70, #71 lack a milestone; 10 issues not linked from proposal. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #57 Signal Detection & Preprocessing; epic #58 Application interface and cross functional integration; epic #59 Waveform Identification & Receiver Processing; epic #60 Modulation, Decision & Explainable AI; epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: IQ file to peaks to classifier to XAI; uml: sequence for the CLI/GUI-over-core-engine flow; ui_flow: CLI first, then GUI screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (short prose) and README. Language: MATLAB plus Python (code is Python); Framework: PyTorch, Captum, SciPy, NumPy, h5py; 6G Simulink library; Platform: Local Python; CI runs pytest; Data: Mentor-provided .iq captures and labeled dataset kept local (git-ignored); HDF5 bursts; Hosting/hardware: Not stated; Sponsor resources: RTX-1 mentor-script dataset and .iq files; Tools: GitHub Actions CI, pytest, matplotlib. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` pins numpy, scipy, h5py, torch, captum, pytest; `prototype/README.md` fresh-clone smoke run: `scripts/analyze_iq.py` on bundled sample .iq; `prototype/waveform_identification/` and `prototype/xai/` mirror pipeline components; 44 tests; login.py scaffold replaced via PR #109; code merged to develop only |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — main still has login scaffold; 29 prototype files only on develop; branch Application-Structure — 5 commits not in develop; branch docs/team-documentation — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Write `docs/specs/epic-57-spec.md` through epic-61 specs: scope, FR/NFR traced to stories, acceptance criteria, open questions; link them in proposal §4.
2. Create architecture and system-context Mermaid diagrams in `docs/design/` showing core engine, CLI, GUI, XAI; add captions in proposal §4 Diagrams.
3. Add a pipeline DFD (IQ in, peaks, classifier, Captum) and a CLI/GUI screen-flow sketch; link the existing calibration flow PNG.
4. Expand proposal §4 Environment with reasons: Python vs MATLAB roles, PyTorch/Captum, data from mentors, hardware.
5. Merge develop into main via PR; decide on Application-Structure and docs/team-documentation branches (merge or close).
6. Link the 10 unlinked issues in §4 and add milestones to stories #63, #67, #68, #70, #71.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A.

*Offline Windows desktop app that suggests assignment deadlines, tracks progress and sends reminders.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Close PR #117, then open a PR rewriting `prototype/README.md` with real setup and run commands for the core and UI, and delete login.py.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#16-#18) and 9 objective-titled stories, all linked. Stale Sprint 1 epic #30 'Tasks' with Objective 0.2/0.3 stories remains; #25-#27 lack a milestone; #8, #12, #13 unassigned or unscheduled. |
| 2. Specs | ✅ done | `docs/specs/specs-G1.md` (develop) — epic #16 CRUD and layout; FR/NFR, criteria, open question; `docs/specs/specs-G2.md` (develop) — epic #17 deadline algorithm and progress; traced to #19-#21; `docs/specs/specs-G3.md` (develop) — epic #18 notifications; shortest, still Draft |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: architecture: Python core plus JS/Electron UI via IPC; context: user, Windows notifications, local storage; er: assignment/course records stored locally; uml: sequence for create-assignment and reminder flows. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (develop). Language: Python backend; JavaScript frontend; Framework: Electron + Vite + React (in prototype only, not in proposal); Platform: Windows desktop, offline; Data: Local SQLite or JSON, undecided; Hosting/hardware: Local Windows machine, no hosting; Sponsor resources: None stated; Tools: GitHub, CI pytest, Mermaid. |
| 5. Prototype wiring | ⚠️ started | `prototype/A.M.I.Y.A.core/` has App.py, Database.py, services/, tests/ (develop); `prototype/A.M.I.Y.A.ui/` has Electron main.js, Vite config, React components (develop); `prototype/README.md` and `requirements.txt` are still the course scaffold; login.py remains; No `.env.example`; `Package.json`, `Requirements.txt`, `scr/` casing and spelling break on Linux CI |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — PR #118 skeleton, #112/#114/#115 specs and wireframes are not on main; PR #117 (open) — reverts #115 proposal spec/wireframe integration; close it; branch feature/34-project-proposal — 28 commits not in develop; branch updated-proposal — 6 commits not in develop.

**To do before your Sprint 2 review:**

1. Close PR #117 so the proposal §4 wireframes and spec links from #115 stay on develop; then merge develop into main via PR.
2. Add `docs/design/architecture.md` and `context.md` (Mermaid) and an ER diagram for the assignment model; caption them in proposal §4.
3. Replace the scaffold `prototype/README.md` and `requirements.txt` with real setup and run commands for core and UI; delete login.py.
4. Fix filename casing and spelling (`Package.json`, `Requirements.txt`, `scr/`) so installs work on a clean machine.
5. Close #116 (PR #118 closed #107 by mistake) and fix proposal links for #107 and #116.
6. Update proposal §4 Environment to include Electron, React, Vite, IPC and the SQLite vs JSON decision with reasons.
7. Close or retitle epic #30 and stories #32/#33; add milestones to #25-#27.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox Incident-Response Training Simulator

*In-memory PySide6 desktop simulator with LLM-generated, validated malware scenarios for beginner incident-response training.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Create `prototype/start_simulation.py` (PySide6 window) and add pyside6 and pydantic to `prototype/requirements.txt` so the README run command works.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 goal epics (#22, #23) and 18 objective-titled stories (#24-#41), all linked. Stories #24-#41 have no Sprint milestone; §4 cites epic/story refs (43 misplaced); #88, #84, #82 unassigned or unscheduled. |
| 2. Specs | ✅ done | `docs/specs/training-environment.md` (main, develop) — epic #22; scope, FR, NFR, acceptance criteria; `docs/specs/ai-scenarios.md` (main, develop) — epic #23; scope and FR, NFR/acceptance sections thinner |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: scenario generation and validation flow; er: scenario schema and action logs; uml: sequence for scenario generation flow; ui_flow: desktop screens and game loop. |
| 4. Environment | ✅ done | Stated in: proposal §4 'Environment and resources' table with reasons. Language: Python 3.x; Framework: PySide6 UI, Pydantic validation; Platform: Windows/macOS/Linux local desktop; Data: In-memory state; optional file fixtures; Hosting/hardware: Local machine; Dockerfile planned for the engine; Sponsor resources: None; independent project; Tools: NRP.ai LLM endpoint via env vars, GitHub, Discord. |
| 5. Prototype wiring | ❌ example files only | `prototype/README.md` (develop) rewritten, but run command `start_simulation.py` does not exist; `prototype/Dockerfile` is one TODO line; `prototype/requirements.txt` still the course scaffold; no PySide6 or Pydantic; main still has login.py and test_login.py; PR #89 open |

**Merge first** (not counted until it's in `develop` or `main`): PR #89 — develop to main: context, sequence, DFD/ERD updates, specs, prototype README; branch copilot/create-requirements-list-for-goal-2-47 — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Add pyside6 and pydantic to `prototype/requirements.txt` and create `prototype/start_simulation.py` plus a test so the README run command works (#60).
2. Create ui/, simulation/, ai/ folders and a Pydantic scenario model mirroring `docs/design/architecture.md`; add `.env.example` for the NRP.ai key.
3. Fix `docs/design/system-context.md` heading and embed Figures 2 and 5 (context, sequence) in proposal §4 Diagrams; close #54.
4. Merge PR #89 into main, then delete login.py and tests/test_login.py from main.
5. Add Sprint milestones to stories #24-#41 and remove the epic/story refs from proposal §4.
6. Add Open questions tables to both specs and finish NFR and acceptance sections in `docs/specs/ai-scenarios.md`.
7. Implement the Dockerfile for the engine or drop it from the prototype.

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

### G17 · EchoSphere (SonicScape): galaxy-map music discovery with swipe feedback

*A space-themed music map where genres, artists and songs are navigated and tuned by swipes.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Decide the tech stack and write it into proposal §4 Environment and resources; every other wiring step depends on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Live epics #21-#23 and stories #25-#30 use objective wording, but five closed duplicate epics (#15, #17-#20, #24) remain. Stories #25-#28 are still open on the past-due Sprint 1 milestone. |
| 2. Specs | ⚠️ started | `docs/specs/specs_goal1.md` (main) - epic #21, stories #25, #26; owner left as placeholder; `docs/specs/specs_goal2.md` (main) - epic #22; cites stories 2.1, 2.2 not #27, #28; Sprint TBD; not linked in §4; `docs/specs/specs_goal3.md` (main, develop) - epic #23, stories #29, #30; scope, FR, acceptance; linked in §4 |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: music dataset and API data into map generation. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Data: local database, technology undecided (goal3-database.md); Sponsor resources: independent; Spotify API drawn in context diagram; NASA API in HW#4. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `prototype/tests/test_login.py` - course example, unchanged; `prototype/requirements.txt` - unchanged scaffold copy; `prototype/README.md` - still the course login text |

**Merge first** (not counted until it's in `develop` or `main`): develop is behind main (49 vs 55 files); sync main into develop so specs and diagrams are on both; Open issues #42, #43, #47 are still open although their PRs (#44, #48) merged; close them.

**To do before your Sprint 2 review:**

1. Write the §4 environment section naming language, frontend, backend, database, APIs and hosting with reasons tied to §3.
2. Replace `prototype/login.py` and its test with a created project skeleton, a manifest, `.env.example` and README commands; run it once as a smoke test.
3. Fix the Epic: #1 headers in `docs/design/architecture.md`, `system_context.md` and `goal2-design.md`; link all design docs and figures in proposal §4.
4. Add a data-flow diagram of dataset and API ingestion to map generation, and link it in §4.
5. Fix `specs_goal2.md` (story numbers, owner, sprint) and link it in §4.
6. Delete duplicate epics #17-#20 and fix the #21/#22 checklists; put carried stories #25-#28 on Sprint 2.
7. Remove the leftover placeholder rows and angle brackets from proposal §4.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · ProStrats: Project Rogue, a 2D action roguelike with build variety

*A Unity 2D action roguelike testing whether weapon, element and route choices produce distinct builds.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Write the first spec file in `docs/specs/` for epic #30 (action gameplay) from the draft text already in issue #30, then repeat for #29 and #31.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #29-#31 and stories #32-#41 carry the objective wording. Spec tasks #53, #54, #56 are Sprint 2 but not on the board or linked in §4; #61 duplicates #56 and #58 has no milestone. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #29 Flexible character progression; epic #30 Action gameplay; epic #31 Replayable run structure. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: combat class diagram (#60) and attack sequence; state/flow: run, room and reward flow (#58); ui_flow: map and menu screens; er: only if a save file is stored (format undecided). |
| 4. Environment | ✅ done | Stated in: proposal §4 'Development environment and resources' (develop). Language: C#; Framework: Unity 6000.3.25f1, Universal 2D, URP, Input System, 2D physics; Platform: downloadable Windows game; Data: no DBMS; save-file format undecided; Hosting/hardware: developer PC with Windows; player minimum to be set by build tests; Sponsor resources: independent, none; Tools: Git/GitHub, C# editor; CI does not build Unity. |
| 5. Prototype wiring | ⚠️ started | `prototype/ProjectRogue/ProjectSettings/ProjectVersion.txt` - Unity 6000.3.25f1; `prototype/ProjectRogue/Packages/manifest.json` - Input System and URP listed; `prototype/ProjectRogue/Assets/Movement/` and `Assets/Scripts/Combat/` - movement and combat scripts, scenes (develop); `prototype/README.md` and `requirements.txt` - unchanged course scaffold |

**Merge first** (not counted until it's in `develop` or `main`): develop to main - system overview, proposal §4, movement/combat PRs #44 and #45 are only on develop; main holds only the Unity foundation (PR #16).

**To do before your Sprint 2 review:**

1. Write the three specs under `docs/specs/` for epics #29-#31 (#53, #54, #56) and link them in proposal §4.
2. Rewrite `prototype/README.md` with Unity version, open, run and Windows-build steps (#59); delete the scaffold requirements file.
3. Close #61 as duplicate of #56; add #53, #54, #56, #58, #59, #60 to the board and §4 as typed refs.
4. Draw the combat class diagram (#60) and run/room/reward flow (#58); add them to `docs/design/` and §4.
5. Move the [epic:#29-#31] refs out of §1 into §2, and set a milestone on #58 and the epics.
6. Run a Windows standalone build once and record it as the smoke run.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi (ROW) drone detection with Wi-Fi CSI (RTX-2)

*Detect and track small drones from Wi-Fi channel state information instead of radar, then compare with radar.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Write the proposal §4 environment (hardware plus capture software, OS and ML tools); it unblocks the architecture diagram and the prototype skeleton.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #2-#4 and stories #6-#17 use objective wording. Spec tasks #49-#51 have no milestone and #45, #47, #49-#51 are not in main's §4; #50 is mislabeled epic #4. |
| 2. Specs | ⚠️ started | `docs/specs/wifi-csi-sensing.md` (develop) - epic #2, stories #8, #13; scope, FR traced to stories, NFR, hardware; `docs/specs/drone-detection.md` (open PR #52) - epic #3, not merged Missing: epic #3 Drone Detection (PR #52 open); epic #4 Evaluation (#50 not started). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence of capture, record, validate, classify; dfd: detection pipeline L1 (epic #3); er: only if datasets go in a database. |
| 4. Environment | ⚠️ partial | Stated in: spec `docs/specs/wifi-csi-sensing.md` §6 (develop); proposal §4 is still a placeholder. Language: not stated; Framework: not stated (classifier tooling unchosen); Platform: host computer and OS for CSI capture not stated in §4; Data: timestamped CSI files; format not stated; Hosting/hardware: GL.iNet GL-MT3000 transmitter, ALFA AWUS036AXM receiver (#39), Seeed XIAO microcontroller; Sponsor resources: RTX-2 mentor guidance; sponsor data not stated; Tools: not stated. |
| 5. Prototype wiring | ⚠️ started | `prototype/csi-setup.md` - equipment roles and compatibility notes (PR #40, main); `prototype/csi-capture.md` - CSI frame capture procedure (PR #41, main); `prototype/README.md`, `login.py`, `requirements.txt` - unchanged course scaffold; no capture script, dependency manifest or smoke run of CSI frames |

**Merge first** (not counted until it's in `develop` or `main`): PR #52 (open) - drone detection specification into develop; branch feature/49-drone-detection-specification - 1 commit not in develop; develop to main - wifi-csi-sensing spec, DFDs and proposal §4 are only on develop.

**To do before your Sprint 2 review:**

1. Merge PR #52 and write the Evaluation spec for epic #4 (#50) under `docs/specs/`.
2. Add architecture and system context diagrams to `docs/design/` and proposal §4.
3. Write the §4 environment: language, capture software, host OS, drivers, ML tools and data storage, each with a reason.
4. Replace `prototype/login.py`, its test and requirements with a capture script, manifest and README, and run it once to produce CSI frames (#8).
5. Link #45, #47, #49-#51 as typed refs in proposal §4 and add milestones; fix #50's title.
6. Open a develop to main release PR so main carries the specs and diagrams.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia first-person horror maze game

*First-person horror maze game in Unreal Engine with adaptive monsters, dynamic encounters and responsive audio.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Pick the Unreal version and Blueprints versus C++, write it in proposal §4 with reasons, then create the project skeleton in prototype/.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #12, #17, #21 and 8 objective stories (#13-#15, #18-#20, #22-#23) are in place with assignees and sp:, but all stories sit in Sprint 1; tasks #39-#52 have no milestone, assignee or parent. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #12 Goal 1: exploration experience; Epic #17 Goal 2: suspense; Epic #21 Goal 3: immersion. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: state machine for monster behavior and director; uml: sequence for player noise to monster response; ui_flow: menu, objective HUD, game-over screens; dfd: game state to AI director to NPC. |
| 4. Environment | ❌ not started | Stated in: HW#4 only (Unreal Engine named); §4 environment is a placeholder. Framework: Unreal Engine (version not stated). |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `tests/test_login.py` — unchanged course example; `prototype/requirements.txt` — unchanged scaffold copy; `prototype/README.md` — course template, not team text |

**Merge first** (not counted until it's in `develop` or `main`): PR #53 — §4 work task chart from develop, open against main.

**To do before your Sprint 2 review:**

1. Write §3 Proposed Approaches and the §4 'Environment and resources' list (Unreal version, Blueprints/C++, OS, tools), each choice with a reason.
2. Create one spec per epic (#12, #17, #21) in `docs/specs/`, finishing #28, and add them to the §4 document index.
3. Add architecture and context diagrams in `docs/design/` (Mermaid plus export) and a monster state diagram; embed in §4 with captions.
4. Create the Unreal project skeleton in `prototype/`, remove login.py, add `.gitignore`/LFS, README setup and a map that opens on a fresh machine.
5. Fix the §4 task table: replace placeholders with real parent, owner and sprint, link the 9 missing issues, and merge PR #53 after review.
6. Assign #39-#52 to a Sprint 2 milestone with owners and parent stories; close duplicates #33 and #35.

[↑ Back to all groups](#groups)

## What this page no longer checks

Sprint 1 is graded and closed, so its checks are gone from this page: the Sprint 1 milestone counts, the HW#5 Goals & Objectives comparison, instructor pull requests, the Word export, and the per-issue story-point and assignee lists. The rules behind them still hold (see [README §4–§6](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board)), and the harness in your Actions tab still checks them on every pull request. The proposal-vs-board editions are in this file's git history.
