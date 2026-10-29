# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-10-29 19:45 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G01](#g01) BGAF | Tue Oct 27 | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ |
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) Epic Engineers | Tue Oct 27 | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G07](#g07) Mighty Morphin | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G13](#g13) BYKX | Thu Oct 29 | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ✅ | ❌ |
| [G15](#g15) HIBBI | Thu Oct 29 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G16](#g16) G16 | Thu Nov 5 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| [G17](#g17) SonicScape (EchoSphere) | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 10 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G08, G11, G12, G13, G14, G16).
- **Design and diagrams:** 13 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G08, G10, G11, G12, G13, G14, G16, G18).
- **Environment:** 16 of 20 have written their environment choices into the repository (G01, G03, G04, G05, G06, G07, G08, G10, G11, G12, G13, G14, G15, G16, G18, G19).
- **Prototype wiring:** 11 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G02, G03, G05, G06, G08, G11, G12, G15, G16, G18).
- **Waiting in a branch or open pull request:** G01, G02, G04, G05, G06, G07, G09, G12, G13, G14, G15, G16, G19, G20. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting (SonarX)

*Rebuild Hyperliquid order books from SonarX data, validate them, then backtest strategies on validated days only.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge #179 and sync develop with main, then rewrite §4 Environment so it matches the DuckDB and React/Vite prototype.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 (#20-#22) with objective-titled stories #23-#28; Sprint 2 stories #113-#119 and #128 closed. Tasks #171-#185 and features #142-#169 are not in proposal main; many have no milestone. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1 (#20, #23/#24); scope, FR/NFR, acceptance, open questions; `docs/specs/validation.md` (main) — Goal 2 (#21, #25/#26); match rate, gate, dated events; `docs/specs/backtest.md` (main) — Goal 3 (#22, #27/#28); fill model, costs, metrics |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: pipeline stages move data; er: stored events and results; uml: market-day sequence is the critical flow; ui_flow: front-end screens exist. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main), out of date. Language: Python 3.12 (pipeline); TypeScript (front end); Framework: React + Vite skeleton in prototype/frontend; pytest; Platform: team laptops; GitHub Actions CI; Node 20.19+ for Vite; Data: DuckDB (pinned in requirements.txt); SonarX S3 files; Hosting/hardware: local only; AWS account for requester-pays S3; Sponsor resources: SonarX L2 snapshots and order-level data via S3; access still open (#155); Tools: pytest, oxlint, GitHub Actions, AWS CLI. |
| 5. Prototype wiring | ⚠️ started | `prototype/src/bgaf_pipeline/` one module per pipeline step, mirrors architecture; `prototype/pyproject.toml`, `requirements.txt` pin pytest and duckdb; `prototype/frontend/` Vite React TypeScript skeleton with lockfile and run steps; `prototype/tests/test_package.py` layout tests; README setup and test commands; `prototype/login.py` and `tests/test_login.py` scaffold still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #179 (open, into main) — restates §2 as three goals and regenerates §4 work items; PR #186 (open, into main) — cleaning-pipeline design skeleton for #176; develop — far behind main (9 vs 24 §2 links, §4 skeleton); sync main into develop; branches 171-three-goals, 176-cleaning-pipeline-design, older 58/18/43 branches — merge or delete.

**To do before your Sprint 2 review:**

1. Merge #179 and #186, then sync develop with main so one branch carries the current proposal.
2. Rewrite proposal §4 Environment to match the prototype: DuckDB, React + Vite, Node version, AWS CLI, with a reason per choice.
3. Add the ER diagram and wireframe figure to proposal §4 Diagrams with numbered captions, and update the database.md row.
4. Add the DuckDB sample-load smoke run, `.env.example` and a frontend CI build; remove `login.py` and `test_login.py`.
5. Give #142-#148 and #157-#169 a milestone and assignee, and put the 20 open issues missing from the board on it.
6. Do #181-#184: context and architecture update, L0/L1 DFD, front-end component and state diagrams.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis (RTX)

*ESP32 nodes capture nearby Wi-Fi/Bluetooth metadata; a backend fingerprints devices and a dashboard maps them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Merge feature/23-approach-environment into develop and then main so the stack choices and hosting reasons are in proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 0-3 (#20, #47, #50, #56) with objective-titled stories #16, #45-#61 (sp, Sprint 3/4). Sprint 2 tasks exist, but only 18 issues are linked; #91-#99 and #101 are not in the proposal. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #47 Goal 1: Collect wireless signal metadata; epic #50 Goal 2: Identify selected recording devices; epic #56 Goal 3: Present device observations through a dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence for node to backend to dashboard flow; ui_flow: Angular dashboard screens exist; er: PostgreSQL stores observations. |
| 4. Environment | ❌ not started | Stated in: HW#4 only (the merged-to-main proposal §4 is still a skeleton; the Lightsail text is on an unmerged branch). Language: Python (backend), TypeScript (Angular), ESP32 firmware (language not stated); Framework: FastAPI; Angular; ESP32 firmware project; Platform: ESP32 capture nodes; Linux; Data: PostgreSQL; Hosting/hardware: AWS Lightsail with SSH-tunnel development (branch feature/23-approach-environment); Sponsor resources: RTX sponsor: demo expectations from sponsor meetings #70, #101; Tools: uv, pytest, GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | `prototype/backend/main.py` FastAPI app with a `/health` route (develop only); `prototype/backend/pyproject.toml`, `uv.lock`, `requirements.txt` (develop); `prototype/README.md` setup, run and test steps for backend (develop); main still has only the scaffold `prototype/login.py` and `tests/test_login.py`; No Angular, ESP32 or PostgreSQL folders yet (#92-#94 open) |

**Merge first** (not counted until it's in `develop` or `main`): branch feature/23-approach-environment — 8 commits incl. Lightsail §4 (PR #87 merged into it, not develop); branch feature/86-lightsail-hosting — 2 commits not in develop; develop — FastAPI scaffold (PR #96) and diagrams (#85, #90, #98); not yet in main.

**To do before your Sprint 2 review:**

1. Merge `feature/23-approach-environment` into develop, then develop into main, so §3 and §4 environment text lands.
2. Write one spec per epic (#47, #50, #56) in `docs/specs/` with traced FR/NFR and acceptance criteria; link them from §4.
3. Embed architecture, context and DFD figures in §4 Diagrams with captions; add the design docs to the §4 table.
4. Add a sequence diagram of capture, upload, fingerprint and display, and low-fidelity dashboard wireframes.
5. Finish #92-#94: ESP32 firmware project, Angular app, PostgreSQL setup, then a smoke run end to end.
6. Link #91-#99 and #101 in §4 and assign #92 and #93.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: equation-to-code literate programming pipeline in a Jupyter notebook (RTX-3)

*Turn a handwritten or typeset equation into verified LaTeX, Python, a training dataset and a trained model.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Rewrite `prototype/README.md` and `requirements.txt` for the real stack (torch, notebook, API client) with a verifier smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics Goal 1-4 (#28, #27, #43, #44) with objective stories; Sprint 2 stories on board. #32, #45, #47 lack milestone; #51, #60, #65 and meetings not linked in §4. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (develop, main) — Goal 1 (#28); covers only #33, other stories pending; `docs/specs/data-generation.md` (develop, main) — Goal 2 (#27); five stories, owners TBC Missing: epic #43 Goal 3: train a model; epic #44 Goal 4: Jupyter notebook output. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er: dataset store (CSV or relational) is chosen by user; ui_flow: notebook cell flow is the whole UI. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 (decisions); §4 Environment still placeholder. Language: Python; Framework: Jupyter notebook UI (sponsor requirement); PyTorch for training; Platform: user's local machine for training; external AI calls for transcription and data generation; Data: CSV or relational store chosen by user; accepted.json hand-off; Hosting/hardware: local only; Sponsor resources: RTX-3 sponsor requires notebook UI; recognizer and code AI service not yet named (marked open); Tools: pytest; GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | `prototype/verifier.py`, `transcriber.py`, `train.py`, `generate_dataset.py` exist; `prototype/tests/test_verifier.py` and input images in `prototype/tests/inputs/`; `prototype/requirements.txt` and README still unchanged course scaffold; no notebook or .env.example in prototype/ |

**To do before your Sprint 2 review:**

1. Replace `prototype/requirements.txt` and `prototype/README.md` scaffold with real dependencies, setup and run commands, and a smoke run.
2. Fill proposal §4 Environment and resources: Python, Jupyter, PyTorch, recognizer API, code AI, reasons tied to §3.
3. Write specs for Goal 3 (#43) and Goal 4 (#44) in `docs/specs/`; extend transcription.md beyond #33.
4. Add the Jupyter notebook cell-flow diagram to `docs/design/` and §4 with a caption.
5. Link #51, #60, #65 and remaining tasks in the §4 work-items table; set milestones on #32, #45, #47.
6. Add `prototype/.env.example` and an empty notebook skeleton that loads accepted.json.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL accounting and top-trader dashboard (SNX-1)

*Compute per-wallet PNL from SonarX Polygon data in Snowflake, rank traders, and show them on a dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Record the stack decision (#52) in proposal §4 and merge PRs #73, #79, #81 so main and develop agree.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Epics #24, #29, #33 with 11 objective-titled stories (#25-#38) on the board; Sprint 2 stories #25 and #34 assigned; 40 of 41 issues linked in proposal. #80, #12, #13 lack sp:. |
| 2. Specs | ⚠️ started | `docs/specs/pnl-calculation.md` (main, develop) — Goal 1 (#24); FIFO, formulas, worked example; `docs/specs/trader-ranking.md` (develop) — Goal 2 (#29); PNL and ROI ranking, worked example Missing: epic #33 Goal 3: dashboard (PR #73 open, `dashboard-questions.md`). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: dfd: trades flow to PNL to ranking; er: results tables stored in Snowflake; uml: sequence of one PNL run; ui_flow: leaderboard and wallet pages. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (Snowflake only); implementation.md. Language: not chosen; Framework: not chosen (blocked on #52); Platform: not chosen; Data: Snowflake warehouse holding SonarX Polygon data; Hosting/hardware: not stated; Sponsor resources: SNX-1 Snowflake access and open-source tools permitted; credentials via env vars; Tools: GitHub Actions; CLAUDE.md. |
| 5. Prototype wiring | ❌ example files only | `prototype/` holds only login.py, test_login.py, scaffold README and requirements.txt; `docs/design/implementation.md` (main) proposes layout and .env.example but nothing created; #62 skeleton and Snowflake connection is open |

**Merge first** (not counted until it's in `develop` or `main`): PR #79 (open, develop) — dashboard flow doc and diagram; PR #81 (open, main) — revised architecture and context diagrams, proposal.md; PR #73 (open, develop) — dashboard questions spec for Goal 3; PR #72 (open) — Sprint 2 review draft; main and develop diverged: architecture.md and implementation.md only on main, trader-ranking.md only on develop.

**To do before your Sprint 2 review:**

1. Decide the language and dashboard framework (#52), record them in proposal §4 Environment and resources with reasons.
2. Merge PRs #73, #79 and #81; sync main and develop so specs, designs and §4 links are on one branch.
3. Draw the ER (#57), Level 0/1 data flow (#58) and PNL sequence (#59) diagrams; add them to §4 with captions.
4. Create the prototype skeleton (#62): folders, manifest, `.env.example`, README setup, and a Snowflake connection smoke run.
5. Link `docs/design/implementation.md`, architecture and dashboard docs in proposal §4; link #80 and add sp:.
6. Remove `prototype/login.py` and `prototype/tests/test_login.py` once the real skeleton exists.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS, Whale Identification/Location System

*Detects whale calls in hydrophone audio and estimates the call's direction and distance.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Fill proposal §4 on develop: environment table, spec/design index linking docs/specs/goal-2-locator.md, and the task table, then merge via PR #48.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 goal epics (#8, #14), 9 objective-titled stories, all Sprint 2 with assignee and sp. But 12 non-story issues are not linked in §4; #23 and #47 are untyped. |
| 2. Specs | ⚠️ started | docs/specs/goal-2-locator.md (develop) — epic #14, stories #15-#18; scope, FR/NFR, criteria, open questions Missing: Epic #8 Goal 1 Build an AI capable of recognizing whale calls. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: audio to detector to locator to saved calls; er: calls and hydrophones are stored in Postgres; uml: sequence of detect, save call, locate. |
| 4. Environment | ⚠️ partial | Stated in: README / HW#4 only. Language: Python (prototype/requirements.txt); Framework: numpy, scipy, torch, librosa, soundfile, matplotlib; Platform: local venv, pytest in CI; Data: Postgres via docker_compose.yaml and db/init/*.sql (main only); Hosting/hardware: local; hydrophone array simulated; Sponsor resources: independent; public whale-call datasets; Tools: GitHub Actions CI, pytest, Docker. |
| 5. Prototype wiring | ✅ done | prototype/requirements.txt (develop): pinned numpy, scipy, torch, librosa; prototype/.env.example: DB and CALLS_DIR settings, no secrets; prototype/locator/smoke.py: documented smoke run for the locator; prototype/tests/: 4 test files covering locator and save_call; prototype/ai-detector/: detector and converter scripts with pipeline.sh |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 develop to main (open) — Goal 2 spec, locator, detector, README, .env.example; main-only files (docker_compose.yaml, db/init/*.sql, ER png via PR #39) are absent from develop; bring them into develop.

**To do before your Sprint 2 review:**

1. Fill proposal §4: environment table with reasons, spec and design document index, and a Planned activities table linking every non-story issue (#41, #42, #35 and others).
2. Write docs/specs/goal-1-detector.md for epic #8 and stories #9-#13; first lines name the epic and stories; link it from §4.
3. Draw architecture, system context and DFD diagrams in docs/design/ (source plus image) and embed them in proposal §4 with captions.
4. Copy the ER diagram and db/init/ schema into develop, add editable source, and link the ER from §4.
5. Edit prototype/README.md: delete the login.py line, add the docker compose command, and add a detector smoke run.
6. Merge PR #48 only after §4 is filled, then confirm main shows the spec and prototype.
7. Retype #23 and #47, add sp: and a Sprint 2 milestone, and decide whether open stories #10-#12 and #17 carry to Sprint 3.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Web app that generates and grades practice questions from uploaded course notes and tracks per-concept weak spots.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write docs/specs/goal2-weak-spot-tracker.md for epic #20 (Sprint 2 stories #21-#26): scope, FR/NFR traced to stories, acceptance criteria, open questions.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#13,#20,#27), 15 objective-titled stories; Sprint 2 stories #21-#26 have sp and milestone but no assignee. Stale #3-#6 remain; #25, #36 unlinked. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #13 Goal 1 Generate, grade, summarize; Epic #20 Goal 2 Track weak spots; Epic #27 Goal 3 Usable web app and reminders. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: upload, extract, question, grade, tracker flow; er: subjects, materials, concepts, mastery, answers stored; uml: sequence of practice session, grading, mastery update; ui_flow: accounts, workspaces, practice view, reminders. |
| 4. Environment | ⚠️ partial | Stated in: nowhere in proposal (§3/§4 skeletons); only implied by prototype/requirements.txt. Language: Python (prototype/*.py); Framework: not chosen (web framework, LLM API); Platform: web app (HW#4 only); Data: not chosen (accounts, mastery store); Hosting/hardware: not chosen; Sponsor resources: none (own project); Tools: pytest, pypdf, python-docx, python-pptx; GitHub CI. |
| 5. Prototype wiring | ⚠️ started | prototype/document_processor.py + test: PDF/DOCX/text extraction (main, develop); prototype/concept_extractor.py, question_generator.py + tests (develop); prototype/requirements.txt lists pypdf, python-docx, python-pptx, pytest; prototype/README.md still course login scaffold; login.py remains |

**Merge first** (not counted until it's in `develop` or `main`): develop ahead of main: #37 question builder, #38 concept extraction not on main; branch feature/question-generator: 2 commits not in develop; matches open task #36.

**To do before your Sprint 2 review:**

1. Write the three goal specs (#13, #20, #27): scope, FR/NFR traced to stories, acceptance criteria, open questions, in proposal §4 or docs/specs/ files linked from §4.
2. Draw architecture, system context, DFD, ER and practice-session sequence as Mermaid in proposal §4 (or docs/design/ plus PNG); caption each in §4 Diagrams.
3. Fill proposal §3 and §4 Environment: web framework, LLM API, database, hosting, each with a reason; commit to one stack.
4. Replace prototype/README.md and login scaffold with setup, run, test steps, a smoke run and .env.example.
5. Assign owners to #21-#26 and #36; close stale #3-#6; add #25 and #36 to §4 tasks table; keep typed refs on develop.
6. Open PRs for feature/question-generator and develop to main so the work counts.
7. Recommended: once specs exist in proposal.md, move the full detail to docs/specs/ and docs/design/ and keep summaries and diagrams in proposal.md.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Edwards materials database from CoCs and test reports (EL)

*Web app that extracts material data from certificates and test-report PDFs into a verified, searchable database.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Close #47: pick DBMS, backend, frontend and extraction approach with reasons in proposal §4; every diagram and the skeleton depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 (#11, #17, #22) with objective-titled stories #12-#27; Goal 0 (#42) holds Sprint 2 stories #48, #49 and tasks #36-#41, #46, #47. Tasks lack `sp:`; §4 links are untyped. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #11 Goal 1: Automated Material Data Extraction and Verification; epic #17 Goal 2: Centralized Material Data Storage; epic #22 Goal 3: Material Data Access and Analysis. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: architecture and context: required; er: relational materials database; dfd: PDF ingestion to storage pipeline; uml: sequence for upload, extract, verify; ui_flow: web app with review queue. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main). Language: Python; Framework: TBD backend and frontend frameworks; Platform: internal web application on AWS; Data: relational database, DBMS still TBD; Hosting/hardware: AWS-hosted (services not yet chosen, #47); Sponsor resources: EL sample CoCs and test reports not yet received; Tools: VS Code, Git and GitHub. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` unchanged course scaffold; `prototype/requirements.txt` unchanged scaffold copy; `prototype/README.md` still has the 〈project title〉 placeholder |

**Merge first** (not counted until it's in `develop` or `main`): PR #68 task/36-use-case-diagram (open to main) — use-case.md and png; branch has 39 commits not in develop; #67 — port the typed-link fix from develop into main; main §4 is real, develop §4 is a skeleton.

**To do before your Sprint 2 review:**

1. Close #47: choose DBMS, backend, frontend, extraction approach and AWS services with reasons; write them into proposal §4.
2. Write the three goal specs (#46, #58, #59) in `docs/specs/` and point the empty §4 table links at them.
3. Merge #68, then draw architecture, ER, data flow and wireframes (#38-#41) and embed them in §4 with captions.
4. Create the prototype skeleton for the chosen stack with manifest, `.env.example`, README run steps and a smoke run; remove `login.py`.
5. Add `sp:` to the Sprint 2 tasks, switch §4 links to typed refs, and reconcile develop with main (#67).

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: crime-incident map and pattern analysis

*Web app mapping public crime incidents and analyzing patterns within a user-selected radius.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Hold one stack decision (DBMS, map library, framework, hosting) and record it in §3 and §4; diagrams, ER and skeleton all depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#3,#12,#14) with objective-titled stories; Sprint 2 stories #4,#5,#13,#28 have sp and assignee; tasks lack sp. Stray #6,#7,#45-#47 unlinked; stories cited in §4. |
| 2. Specs | ⚠️ started | docs/crime-pattern-analysis.md (develop) — Goal 2 filtering/frequency; linked from §4; docs/crime-data-format.md (develop) — Goal 1 format; not linked from proposal; docs/crime-data-sources.md (develop) — Goal 1 sources; notes, not linked Missing: Epic #3 Goal 1 spec in docs/specs/; Epic #14 Goal 2 spec in docs/specs/; Epic #12 Goal 3 spec in docs/specs/. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: import, normalize, store, filter, map; er: incident table (#32 schema); uml: sequence of radius search to map markers; ui_flow: map, filter controls, radius screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (develop); §3 still skeleton; main still skeleton. Language: Python 3 (stdlib, unittest); Framework: not selected (app framework, mapping library); Platform: browser map UI; OS target not selected; Data: public crime dataset not chosen; DBMS not selected; Hosting/hardware: none for prototype; hosting TBD; Sponsor resources: none (own project); Tools: GitHub, unittest. |
| 5. Prototype wiring | ⚠️ started | prototype/area_filter.py + test_area_filter.py: radius filtering (develop, #55); prototype/crime_frequency.py + test (develop, #61); prototype/README.md and requirements.txt still scaffold; login.py remains; tests sit beside code, not in prototype/tests |

**Merge first** (not counted until it's in `develop` or `main`): develop ahead of main: proposal §2/§4, filter and frequency prototypes, three data docs not on main.

**To do before your Sprint 2 review:**

1. Incorporate docs/crime-data-format.md and docs/crime-data-sources.md into proposal §4 (summary and link); add a Goal 3 map spec; trace requirements to stories.
2. Draw architecture and system-context diagrams promised as Figures 1-2 (Mermaid in §4 or docs/design/ plus PNG), then ER for #32, DFD, sequence, map wireframe.
3. Decide DBMS, map library, web framework, hosting; write §3 Proposed Approaches (still skeleton) and fill §4 with reasons.
4. Replace prototype/README.md, requirements.txt and login scaffold; organize prototype/ by component; add smoke run and .env.example.
5. Clean issues: close #6,#7,#45-#47; add sp to Sprint 2 tasks; link #58,#60,#62; keep stories out of §4.
6. Open a PR develop to main so Sprint 2 content lands on both branches.
7. Recommended: move full spec detail to docs/specs/ per goal, keeping summary and diagrams in proposal.md.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: Vehicle maintenance logger

*Web app that tracks vehicle service history and recommends next maintenance with urgency alerts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Agree the stack in one meeting and write it, with a reason per choice, into proposal §3 and §4 (#16, #17); everything else depends on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-2 (#27, #28) with 10 objective-titled stories #29-#38 (sp, assignee; #29-#31 in Sprint 2). Tasks #13, #16, #17 exist; none for specs, diagrams or prototype wiring. §1 cites epics #27 and #28. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #27 Goal 1: Centralized Vehicle Data & Maintenance Tracking; epic #28 Goal 2: Scheduled Maintenance Recommendations & Alerts. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required; er: vehicles and service history stored; uml: sequence for next-service calculation; ui_flow: dashboard and entry screens. |
| 4. Environment | ❌ not started | Stated in: nowhere (proposal §3 and §4 are still skeletons; HW#4 names no stack). Platform: web app (per project summary); Data: a vehicle database (PR #48 adds a schema, store not stated); Sponsor resources: none (own project). |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` unchanged scaffold; `prototype/requirements.txt` unchanged scaffold copy; PR #48 (open) adds `prototype/db/schema.sql` and `init_db.py` only |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 (open, into develop) — vehicle database schema and seed script for #29; develop to main — nothing Sprint 2 is merged yet.

**To do before your Sprint 2 review:**

1. Hold one meeting and fix the stack; write it with reasons into §3 and §4 (#16, #17).
2. File and assign Sprint 2 tasks for two specs, the design diagrams and the prototype skeleton, each with `sp:` and the Sprint 2 milestone.
3. Write `docs/specs/` for epics #27 and #28 tied to stories #29-#38; link them in §4.
4. Draw architecture, context, ER and screen flow in `docs/design/`; embed in §4 with captions.
5. Review and merge #48, then replace `login.py` with the real skeleton, `.env.example`, README and smoke run.
6. Link #46 in §4 and remove the epic references from §1.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope stablecoin wash-trading detector (SNX-2)

*Graph analytics and risk scoring to detect wash trading in stablecoin transfers, with an investigator dashboard.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Write docs/specs/goal1-network-model.md for epic #15 (Sprint 2 stories #31-#33, #38), grounded in a confirmed sample SonarX extract.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#15,#23,#24), 11 objective-titled stories with sp and sprint, 0 assignees. 24 of 26 issues linked; #3 untyped. No Sprint 2 doc or wiring tasks. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #15 Goal 1 Model and analyze transaction networks; Epic #23 Goal 2 Detect wash trading; Epic #24 Goal 3 Investigation dashboard. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: SonarX to graph to detection to score pipeline; er: wallets, transfers, labels, risk scores stored; uml: sequence of wallet search to evidence profile; ui_flow: search, graph explorer, wallet summary screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 and §3 (main and develop). Language: Python (pipeline, detection, ML); Framework: scikit-learn; dashboard undecided (Streamlit/Dash or React+FastAPI); Platform: laptops; company machine for heavy compute; Data: SQL in SonarX; Parquet and DuckDB; Neo4j optional; Hosting/hardware: team machines; no hosting named; Sponsor resources: SNX-2: SonarX stablecoin data and SQL warehouse; Tools: GitHub, Discord. |
| 5. Prototype wiring | ❌ example files only | prototype/ holds course login.py, test_login.py, scaffold README; requirements.txt unchanged; root requirements.txt empty; root login.py and course files are copies, not team work |

**To do before your Sprint 2 review:**

1. Write per-epic specs (#15, #23, #24) tracing requirements to stories, in proposal §4 or docs/specs/ files linked from §4.
2. Draw architecture, context, DFD, ER, wallet-search sequence and dashboard wireframe as Mermaid or PNG in proposal §4; caption each.
3. Confirm SonarX access and a sample extract; decide graph store and dashboard stack; record each with a reason in §4.
4. Build prototype skeleton: manifest, component folders, .env.example, README, smoke run on a sample transfers file; remove login scaffold.
5. Assign #31-#33 and #38; add Sprint 2 tasks for specs, diagrams, wiring; fix #3 type; link #5 and #42.
6. Land all work by PR to develop (14 direct commits so far); remove copied course files from repo root.
7. Recommended: keep summary and diagrams in proposal.md, put full spec and design detail in docs/specs/ and docs/design/.

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

### G12 · ACJMM: Explainable 6G waveform classification

*Application that finds signal peaks, classifies simulated 6G waveforms and explains each result with calibrated confidence.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Write the first spec in docs/specs/ for epic #59 or #60, using docs/confidence-calibration.md as the base, and link it from §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #57-#61 plus new #103; stories linked in §2. Several stories (#63, #67, #68, #70, #71, #95) lack Sprint milestone or assignee; #96, #103, #107 not in §4; main has 0 typed refs. |
| 2. Specs | ⚠️ started | docs/confidence-calibration.md (develop) — story #65 handoff; not in docs/specs, not linked in §4; docs/baseline-peak-picker.md (develop) — story #66 baseline method and results; handoff, not spec Missing: Epic #57 Signal Detection & Preprocessing; Epic #58 Application interface and cross functional integration; Epic #59 Waveform Identification & Receiver Processing; Epic #60 Modulation, Decision & Explainable AI (only story #65 covered); Epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: signal to peaks to classes to explanation; uml sequence: snapshot through to explained result; ui_flow: GUI and CLI both planned; er: only if results or labeled data are stored. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (short paragraph), prototype/README. Language: Python (prototype), MATLAB for EDA; Framework: numpy/scipy/h5py; Captum planned for XAI; GUI framework not chosen; Platform: Local machine, pytest in CI; Data: Sponsor RTX .iq captures kept in git-ignored .local-data; simulated MATLAB 5G NR data; Hosting/hardware: not stated; Sponsor resources: RTX mentor I/Q files and MATLAB 6G Simulink library; Tools: GitHub Actions CI, pytest. |
| 5. Prototype wiring | ✅ done | prototype/requirements.txt — pinned numpy, scipy, h5py, pytest; prototype/README.md — setup, sample-capture smoke run, test commands; prototype/data/sample/peak_picker_smoke.iq — sample capture; login scaffold removed (PR #109); prototype/waveform_identification/ and prototype/xai/ — packages mirroring components |

**Merge first** (not counted until it's in `develop` or `main`): PR #110 — Captum integrated gradients (story #64), open against develop; develop to main — main still has login.py scaffold and 0 typed refs; branch Application-Structure — 5 commits not in develop; branch docs/team-documentation — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Write docs/specs/<epic>.md for each of epics #57-#61 with FR/NFR traced to stories, acceptance criteria and open questions; first lines name epic and stories.
2. Add a §4 Specification and design documents table linking every spec and design doc, including docs/confidence-calibration.md.
3. Draw architecture and system context diagrams in docs/design/ with editable source and image; embed them in §4 Diagrams with captions.
4. Add a DFD, a sequence diagram for snapshot to explanation, and GUI/CLI wireframes; reuse docs/images/confidence-calibration-flow.png as the XAI flow.
5. Convert the §4 environment paragraph into a table with a reason per choice, including GUI toolkit, data store and sponsor data handling.
6. Link #96, #103, #107 in §4; give open stories a Sprint milestone and assignee; merge PR #110 and release develop to main.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. assignment manager

*Windows desktop app that manages assignments, suggests deadlines from difficulty, tracks progress and sends reminders.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Pick the desktop shell and storage, then generate the prototype skeleton and replace login.py with a smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Epics #16-#18 with 9 objective-titled stories; Sprint 2 stories #22-#24 assigned with sp:. Features and tasks filed under stories with typed refs on develop; main has 0 typed refs. |
| 2. Specs | ✅ done | docs/specs/specs-G1.md (develop) — epic #16, stories #22-#24; scope, FR/NFR, criteria, questions; docs/specs/specs-G2.md (develop) — epic #17, stories #19-#21; same structure; docs/specs/specs-G3.md (develop) — epic #18, stories #25-#27; same structure |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: er: assignments stored locally; dfd: UI to Python to storage to notifier; uml sequence: create assignment and deadline suggestion; architecture and context: both required. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4. Language: Python backend, JavaScript frontend; Framework: UI-to-Python bridge planned, desktop shell not named; Platform: Windows desktop, native toast notifications; Data: local JSON or SQLite, undecided; Hosting/hardware: local only, offline; Sponsor resources: none stated; Tools: not stated. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and tests/test_login.py — course example still present; prototype/requirements.txt — unchanged scaffold; prototype/README.md — unchanged scaffold; no project skeleton |

**Merge first** (not counted until it's in `develop` or `main`): PR #115 — spec and wireframe links into proposal §4, open against develop; develop to main — main lacks specs, wireframes and typed refs; branch feature/111-spec-links — 3 commits not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #115 so §4 Specification and design documents lists specs-G1/G2/G3 and the six wireframes.
2. Draw architecture and system context diagrams in docs/design/ with source plus image; embed in §4 Diagrams.
3. Add an ER diagram for the assignment record and a sequence diagram for create assignment through deadline suggestion.
4. Fill §4 Environment and resources as a table naming the desktop shell, storage, notification library and test tools with reasons.
5. Create the prototype skeleton for the chosen stack, delete prototype/login.py and tests/test_login.py, and add a README smoke run.
6. Add sp: to #113 and link #113, #111, #44, #47 in §4; merge develop into main.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox

*Desktop in-memory cybersecurity training simulator with LLM-generated, schema-validated incident scenarios.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Create the PySide6 plus Pydantic prototype skeleton for #60 and replace login.py with a smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #22, #23 with 18 objective-titled stories (#24-#41) but no Sprint milestone on them, though the specs are Sprint 2. §4 spec table cites epics and stories; #4, #6, #13 not linked. |
| 2. Specs | ✅ done | docs/specs/training-environment.md (main, develop) — epic #22, stories #24-#32; scope, FR/NFR, criteria; docs/specs/ai-scenarios.md (main, develop) — epic #23, stories #33-#41; scope and requirements |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ▫️ context · ✅ data flow · ✅ ER · ▫️ UML · ✅ page flow. Needed for this project: uml sequence: configure, generate, validate, load, report; context diagram: required, PR #75 unmerged. |
| 4. Environment | ✅ done | Stated in: proposal §4 Environment and resources. Language: Python 3.x; Framework: PySide6, Pydantic; Platform: Windows, macOS, Linux local desktop; Data: in-memory state, optional file fixtures; Hosting/hardware: local machine, no hosting; Sponsor resources: independent; NRP.ai LLM endpoint and API key via env vars; Tools: GitHub Actions, pytest, check_repo.py. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and tests/test_login.py — course example still present; prototype/requirements.txt — unchanged scaffold; no PySide6 or Pydantic; prototype/README.md — scaffold text with placeholder title; Issue #60 prototype skeleton still open |

**Merge first** (not counted until it's in `develop` or `main`): PR #75 — system context diagram and doc, open against develop; branch feature/54-System-context-diagram-for-Cyber-Sandbox — 1 commit not in develop; branch copilot/create-requirements-list-for-goal-2-47 — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Build the prototype skeleton (#60): PySide6 window, Pydantic scenario model, requirements.txt, .env.example, README smoke run; remove login.py and test_login.py.
2. Merge PR #75 so docs/design/system-context.md and its image land; verify the §4 link.
3. Write the sequence diagram (#57) as docs/design/scenario-sequence.md, or remove the dead §4 link until it exists.
4. Set Sprint 2 milestone on stories #24-#41; add #13, #6, #4 to §4.
5. Finish #70, #72 and #73 aligning data model, data flow and spec open questions with the architecture decisions.
6. Release develop to main once PR #75 and the prototype PR are merged.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI: C++ ECS game engine

*Lightweight data-oriented game engine on OpenGL 3.3 with ECS, built for a game demo.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Add src/main.cpp so the CMake build produces a window and the README smoke run actually works.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #24, #25 and 8 objective-titled stories, but stories have no milestone or assignee; #43-#50 untyped; #6 'Setting up' epic is not a goal; §4 table is template placeholders, 0 typed refs. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #24 Game Engine; Epic #25 Game Demo. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: input to ECS systems to render; uml: ECS entity/component/system classes; ui_flow: editor (Objective 2.4) screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (bare list), prototype/README. Language: C++26; Framework: OpenGL 3.3, SDL3, GLM, Glad, Assimp, stb_image; Platform: Windows 11, Ubuntu 26.04, Arch Linux; Data: asset files via Assimp; no database; Hosting/hardware: local desktop, older GPUs; Sponsor resources: independent project; Tools: CMake 4.0.0, GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | prototype/CMakeLists.txt — C++26, SDL3, assimp, glm, executable run; prototype/lib/include/ — vendored glm and glad headers; prototype/README.md — setup, build, run steps for Linux and Windows; No src/main.cpp or setup scripts on develop; test section still scaffold pytest |

**Merge first** (not counted until it's in `develop` or `main`): PR #51 — system context diagram, open against develop; branch documentation/47-architecture-diagram — 2 commits not in develop; develop to main — main still has login.py and skeleton §2/§4.

**To do before your Sprint 2 review:**

1. Add prototype/src/main.cpp and glad.c so cmake -B build works and a window opens; commit the setup.sh and setup.ps1 the README references.
2. Merge PR #51 and the architecture-diagram branch; embed both in §4 Diagrams with captions.
3. Write specs in docs/specs/ for epics #24 and #25 (#49), and a design doc with ECS class and data-flow diagrams.
4. Replace the §4 template tables with real rows: typed refs for #43-#50 and tasks, and a spec/design document index.
5. Add a reason per choice to the §4 environment list; fill dev tools and benchmark hardware.
6. Give Sprint 2 stories an assignee, milestone and sp:; type #43-#50; release develop to main.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch cross-chain bridge exploit detection

*Detector that learns normal bridge outflows, alerts on exploits and shows operators a dashboard, using SonarX data.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Write docs/design/architecture.md (#62) with the architecture and context diagrams plus data-flow and ER, and add it to Table 9.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Epics #11-#13 with objective-titled stories #14-#21, assigned with sp: and sprints; all 33 issues linked from proposal with typed refs. Sprint 2 stories #14, #15 on board. |
| 2. Specs | ✅ done | docs/specs/goal-1-baseline.md (develop) — epic #11, stories #14, #15; problem, scope, requirements; docs/specs/goal-2-detection.md (develop) — epic #12; alert rules, replays, false alarms; docs/specs/goal-3-dashboard.md (main, develop) — epic #13; dashboard and user test |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: source to detector to store to alerts; er: SQLite transfers, alerts, cursor; uml sequence: live ingest to alert; ui_flow: operator dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 Table 6, prototype/.env.example and README. Language: Python 3.12; Framework: FastAPI; Platform: Windows 11 and Ubuntu CI, Docker packaging; Data: SQLite; SonarX data pending, public Ethereum nodes meanwhile; Hosting/hardware: host not chosen, Docker image; Sponsor resources: SNX data and real-time stream, requested, no reply; Tools: GitHub Actions, pytest, Slack webhook. |
| 5. Prototype wiring | ✅ done | prototype/requirements.txt, requirements-dev.txt — pinned dependencies; prototype/.env.example — every setting with default (develop); prototype/bridgewatch/ — source, detector, store, live, notify, app modules; prototype/README.md — run modes and tests; Dockerfile.bridgewatch present; prototype/tests/test_bridgewatch.py — automated tests; login scaffold gone |

**Merge first** (not counted until it's in `develop` or `main`): PR #78 — Table 6 reasons tied to §3, open against develop; develop to main — main lacks Goal 1/2 specs and .env.example (release due Nov 3, #64); branch 15-baseline-check — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Write docs/design/architecture.md (#62) with Figures 1 and 2 as editable source plus image, and link it from Table 9.
2. Add data-flow, ER (from store.py schema) and sequence diagrams for the live ingest to alert path.
3. Add dashboard wireframes or a screen-flow diagram for Goal 3 (#20).
4. Merge PR #78, then close #72.
5. Release develop to main (#64) so specs, .env.example and typed refs reach main.
6. Add a captioned Diagrams list in §4 pointing at each file in docs/design/.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · SonicScape (EchoSphere): galaxy-style music discovery app (independent)

*Space-themed music map: swipe to like genres, artists, songs; preferences persist per user.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Hold a 30-minute stack decision, then write it into proposal §3 and §4 so specs, design and the prototype skeleton can follow.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Open epics #21-#23 with stories #25-#30 titled with the objective wording. All six stories sit in Sprint 1 (past due); Sprint 2 milestone is empty; six duplicate closed epics remain; no tasks filed. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #21 Goal 1: Galaxy Navigation with Discovery-Focused Recommendations; Epic #22 Goal 2: Swipe Feedback; Epic #23 Goal 3: Personalized Map with a Persistent User Profile. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: swipe feedback flows to recommendations; er: users, preferences, swipe history in local database; uml: sequence for swipe then map update; ui_flow: sign-in, genre picks, galaxy map screens. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Language: not stated; Framework: not stated (3D galaxy/map rendering implied); Platform: not stated; Data: local database named in Objective 3.2; engine not chosen; Hosting/hardware: not stated; Sponsor resources: independent; NASA free API keys and a music database named in HW#4 only; Tools: not stated. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and prototype/tests/test_login.py are the course example; prototype/README.md and requirements.txt are unchanged course scaffold; no .env.example, no framework project, no manifest for the chosen stack |

**Merge first** (not counted until it's in `develop` or `main`): develop is behind main: proposal/proposal.md has 4 §2 links on develop versus 9 on main; sync develop from main.

**To do before your Sprint 2 review:**

1. Pick the stack in a team meeting, record language, framework, database and music/NASA data sources in proposal §3 and §4 with reasons.
2. Close duplicate epics #15, #17-#20, #24; move #25-#30 to Sprint 2 and file Sprint 2 tasks with assignee, sp and milestone.
3. Write three specs (epics #21-#23), inline in proposal §4 or in docs/specs/ linked from §4, with requirements traced to stories and acceptance criteria.
4. Add Mermaid architecture and context diagrams to proposal §4, then ER, swipe sequence and screen flow; recommended: full detail in docs/design/architecture.md.
5. Create the prototype skeleton in prototype/ with the chosen tool, replace login.py, add .env.example and a README smoke run.
6. Fill §4 Specification and design documents and Planned activities, linking every task as typed refs; merge anything unique from root proposal.md into proposal/proposal.md (the file the harness reads), then delete the root copy and proposal/~$oposal.docx.
7. Open PRs into develop that close each issue, then merge develop into main.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · ProStrats: Project Rogue, 2D action roguelite platformer in Unity (independent)

*Playable Unity 2D roguelite prototype with flexible builds, weapon combat and branching run structure.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Rewrite prototype/README.md with Unity Hub setup and a Test_Combat smoke run; it is the smallest change that makes the existing project count as wiring.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#29-#31) and 10 stories (#32-#41), all assigned and pointed; Sprint 2 stories #32-#38 on board. Story titles are short labels (bodies empty), and #13, #26 are untyped; §1 cites epics. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #29 Goal 1: Flexible character progression; Epic #30 Goal 2: Action gameplay; Epic #31 Goal 3: Replayable run structure. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: class diagram of combat classes (CombatResolver, AbilityData, AttributeSet); uml: state or sequence for run, room, reward flow; ui_flow: loadout panel, route map, HUD screens. |
| 4. Environment | ✅ done | Stated in: proposal §4 (develop), §3 pointer; main still skeleton. Language: C#; Framework: Unity 6000.3.25f1, Universal 2D, URP, Input System, 2D physics; Platform: Local Windows standalone build; Data: none; no server or DBMS needed (ScriptableObjects for ability data); Hosting/hardware: Developer PC for Editor; player hardware minimum to be set by build testing; Sponsor resources: independent; placeholder art with CREDITS.txt; Tools: Git/GitHub, C# editor, Sprint Board; CI does not compile Unity. |
| 5. Prototype wiring | ⚠️ started | prototype/ProjectRogue/ is a real Unity 6000.3 project (Packages/manifest.json, ProjectVersion.txt); prototype/ProjectRogue/Assets/Scripts/Combat/ and Assets/Movement/ hold merged feature code (#44, #45); Scenes: Test_Combat.unity, TraversalRoom.unity, MovementFoundation.unity; prototype/README.md and requirements.txt are still the course scaffold |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release PR: main has only the Unity foundation (#16); develop has movement, combat, design docs, proposal §3-§4.

**To do before your Sprint 2 review:**

1. Rewrite prototype/README.md for Unity: editor version, how to open prototype/ProjectRogue, which scene to Play, what a successful smoke run shows; remove login.py scaffold.
2. Write one spec per epic in docs/specs/ (#29, #30, #31), requirements traced to stories #32-#41, and list them in proposal §4.
3. Add a class diagram of Scripts/Combat and a run/room state diagram to docs/design/, plus wireframes for the loadout panel and route map.
4. Retitle #32-#41 with the exact §2 objective wording, fill bodies, and fix the class versus weapon/element mismatch in §2.
5. Close #13 and #26 or give them types, sp and Sprint 2; replace [epic:] refs in §1 with plain text.
6. Open a develop to main PR so §3, §4, design docs and the Unity work are on main; land #48 playtest protocol.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · Titan Security: Radar over WiFi, drone detection from Wi-Fi CSI (RTX-2)

*Detect small drones from Wi-Fi channel state information using inexpensive off-the-shelf equipment.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Fix PR #44 so the equipment notes reach main, then write the three epic specs using the findings in prototype/csi-setup.md.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#2-#4) and 9 objective-titled stories (#6-#8, #13-#17). Only #8 is in Sprint 2; Sprint 1 still holds 9 open issues; #3 and #4 unassigned; #37, #38, #43 untyped or unlinked. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #2 Wi-Fi CSI sensing; Epic #3 Drone Detection; Epic #4 Evaluation. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: CSI capture, files, quality check, classifier, position; uml: sequence for capture-to-detection run; er: skip; use a file and record schema table instead. |
| 4. Environment | ⚠️ partial | Stated in: prototype/csi-setup.md on develop (not incorporated into proposal §4, which has no environment text). Language: not stated; Framework: not stated (CSI capture tool and classifier library open); Platform: host OS and drivers documented in csi-setup.md per #39; not in proposal; Data: timestamped CSI recording files (Objective 1.2); format not stated; Hosting/hardware: ALFA AWUS036AXM adapter and GL.iNet GL-MT3000 router plus a host computer (#39); Sponsor resources: RTX-2: equipment and test-area access not stated; Tools: not stated. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, test_login.py, README.md, requirements.txt are course scaffold; prototype/csi-setup.md and csi-capture.md exist on develop only (PRs #40, #41): notes, not a skeleton; no code or manifest for CSI capture |

**Merge first** (not counted until it's in `develop` or `main`): PR #44 (open, base main, head develop-merge-conflict) — csi-setup.md and csi-capture.md; branch has 15 commits not in develop; develop has the equipment notes; main does not.

**To do before your Sprint 2 review:**

1. Resolve PR #44: re-merge develop into main cleanly so csi-setup.md and csi-capture.md land, or retarget to develop.
2. Write three epic specs (#2, #3, #4), inline in proposal §4 or docs/specs/ linked from §4, traced to stories #6-#17, with open questions on range targets.
3. Add architecture, context and CSI data-flow diagrams to proposal §4 (Mermaid); recommended: full detail in docs/design/architecture.md linked from §4.
4. Fill §3 and §4 environment: summarize prototype/csi-setup.md (equipment, OS, capture tool, language, ML library, RTX-2 resources) with reasons and link it.
5. Build the prototype skeleton in prototype/ (capture module, sample recording, quality checks, .env.example, README smoke run) for story #8.
6. Move or close the open Sprint 1 issues (#26-#28, #37, #38, #43), assign #3 and #4, and link #37, #39, #43 in §4.

[↑ Back to all groups](#groups)

<a name="g20" id="g20"></a>

### G20 · Solos: Insomnia, first-person horror maze game in Unreal Engine (independent)

*First-person horror maze game with adaptive monsters, reactive environment and audio, built in Unreal Engine.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/muntay89/CPSC490-G20-Solos)

**Start here:** Create the Unreal First Person project in prototype/ with a .gitignore, commit it through an issue and PR, and write the README with the Play-in-Editor smoke run.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#12, #17, #21) and 8 objective-titled stories; 14 tasks (#39-#52) filed but have no milestone or assignee. Sprint 2 milestone is empty; §2 cites epics as [story:]; task refs are bare. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #12 Goal 1: engaging, replayable horror exploration; Epic #17 Goal 2: suspense through player-responsive threats; Epic #21 Goal 3: psychological immersion, audiovisual storytelling. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: state diagram for monster behavior (patrol, chase, kill); uml: sequence for horror director to NPC; ui_flow: menu, HUD, objective tracking screens. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Language: not stated (C++ or Blueprints); Framework: Unreal Engine named in HW#4; version not stated; Platform: not stated; Data: none stated; Hosting/hardware: not stated; Sponsor resources: independent; Tools: not stated. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, test_login.py, README.md, requirements.txt are course scaffold; no Unreal project or .uproject anywhere in the repo |

**Merge first** (not counted until it's in `develop` or `main`): PR #53 (open, base main) — §4 work task chart in proposal.md; retarget to develop; develop to main release: main §2 and §4 are skeleton while develop has 11 §2 links.

**To do before your Sprint 2 review:**

1. Decide Unreal version and C++ versus Blueprints; write it into §3 and §4 with reasons, and finish the §4 task chart (#35, PR #53 retargeted to develop).
2. Create the Unreal project in prototype/ with .gitignore and a README that opens it and runs Play-in-Editor on a fresh machine.
3. Assign #39-#52 to owners and put them in Sprint 2; move stories #13-#23 to Sprint 2; add priority to #22 and #23.
4. Write three epic specs (#12, #17, #21), inline in proposal §4 or docs/specs/ linked from §4; recommended: summary in §4, detail in docs/specs/.
5. Add architecture and context Mermaid diagrams, a monster state diagram and a HUD/menu flow to proposal §4; recommended: detail in docs/design/architecture.md.
6. Fix §2 refs: use [epic:] for #12, #17, #21 and typed [[task:#n]] refs for #39-#52; release develop to main.

[↑ Back to all groups](#groups)

## What this page no longer checks

Sprint 1 is graded and closed, so its checks are gone from this page: the Sprint 1 milestone counts, the HW#5 Goals & Objectives comparison, instructor pull requests, the Word export, and the per-issue story-point and assignee lists. The rules behind them still hold (see [README §4–§6](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board)), and the harness in your Actions tab still checks them on every pull request. The proposal-vs-board editions are in this file's git history.
