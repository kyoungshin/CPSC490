# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-10-28 21:24 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) Epic Engineers | Tue Oct 27 | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G07](#g07) Mighty Morphins | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G13](#g13) BYKX | Thu Oct 29 | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ❌ | ✅ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G16](#g16) neuroprosthetic | Thu Nov 5 | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| [G17](#g17) SonicScape (EchoSphere) | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 9 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G08, G12, G13, G14, G16).
- **Design and diagrams:** 10 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G08, G10, G12, G16, G18).
- **Environment:** 15 of 20 have written their environment choices into the repository (G01, G02, G03, G04, G05, G06, G07, G08, G10, G12, G13, G14, G16, G18, G19).
- **Prototype wiring:** 8 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G03, G05, G06, G08, G12, G16, G18).
- **Waiting in a branch or open pull request:** G01, G02, G04, G05, G06, G07, G12, G13, G14, G15, G16, G19, G20. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting (SNX-4)

*Rebuild Hyperliquid order books from SonarX data, validate them, then backtest strategies on validated days.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge PR #179 and sync develop with main so one branch holds the current proposal, then add the ER and wireframe figures to §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 (#20-22) with objectives #23-28 on main, objective-titled; Sprint 2 stories closed. Open #142-148 features have no milestone; develop lags main; #179 restating §2 is unmerged. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1 (#20, stories #23/#24); traced requirements, open questions; `docs/specs/validation.md` (main) — Goal 2 (#21, #25/#26); match rate, gate, dated events; `docs/specs/backtest.md` (main) — Goal 3 (#22, #27/#28); fill model, costs, metrics |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: pipeline stages move data; er: stored events and results; uml: market-day sequence is the critical flow; ui_flow: front-end screens exist. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main). Language: Python 3.12 (pipeline); TypeScript (front end); Framework: React + Vite skeleton (prototype/frontend); pytest; framework choice still marked open in design doc; Platform: team laptops; GitHub Actions CI; Data: DuckDB (pinned in requirements.txt, PR #139); SonarX S3 buckets; Hosting/hardware: local only; AWS account for requester-pays S3; Sponsor resources: SonarX L2 snapshots and order-level data via S3; access still open (#82, #155); Tools: hftbacktest trial (#169, open); GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | `prototype/src/bgaf_pipeline/` one module per pipeline step, docstrings only; `prototype/pyproject.toml` and pinned `requirements.txt` incl. duckdb; `prototype/frontend/` Vite React TypeScript skeleton with package-lock; `prototype/tests/test_package.py` layout tests; README setup and test commands; `login.py` and `test_login.py` scaffold still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #179 (open, 171-three-goals) — restates §2 as three goals and regenerates §4 work items; develop — 9 §2 links vs 24 on main; sync main into develop; branches 58-cite-dropped-objective-main, 18-abstract-intro, 43-update-goals-and-objectives — stale, close or merge.

**To do before your Sprint 2 review:**

1. Merge PR #179 into main, then merge main into develop so both carry the same proposal and docs.
2. Add proposal §4 figures for the ER diagram (`docs/design/database.md`) and the wireframes (`docs/design/ui-wireframe.png`) with numbered captions.
3. Update §4 Environment and resources with DuckDB, React/Vite, Node, backtest library and a reason each.
4. Add the open issues #169-#185 and #142-#148 to the Sprint board, with Sprint 3 milestone and sp: where missing.
5. Add a README smoke run for loading one SonarX sample into DuckDB; remove `prototype/login.py` and `prototype/tests/test_login.py`.
6. Mark `docs/design/frontend-architecture.md` §6.5 framework decision as settled (React) and add .env.example.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: distributed signal capture for multi-node device detection (RTX-4)

*ESP32 scanners capture Wi-Fi and Bluetooth metadata to identify nearby recording devices on a dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Merge PRs #96 and #100 and the feature/23 branch into develop so proposal §3/§4, diagrams and the FastAPI scaffold are all on one merged branch.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #47, #50, #56 with 15 objective-titled stories, all Sprint 3-4 and unassigned. Sprint 2 tasks #92-94 unassigned; #82, #75, #97 lack sp:; most tasks not in §4. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #47 Goal 1: collect wireless signal metadata; epic #50 Goal 2: identify devices; epic #56 Goal 3: dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: signals flow ESP32 to server to dashboard; er: PostgreSQL stores observations; uml: sequence of scan, upload, identify; ui_flow: Angular dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: design docs only; proposal §3/§4 still skeleton on develop and main. Language: C/C++ firmware; Python backend; TypeScript dashboard; Framework: FastAPI backend; Angular dashboard (architecture diagram lists dashboard TBD); Platform: ESP32 capture nodes; server; Data: PostgreSQL (six stores in the DFD and ER); Hosting/hardware: AWS Lightsail proposed (~$168 for 8 months, #101) in unmerged branch feature/23; ESP32 order list due; Sponsor resources: RTX-4 sponsor approval for Lightsail and order list; Tools: uv for backend (PR #96). |
| 5. Prototype wiring | ❌ example files only | develop `prototype/` holds only login.py, tests/test_login.py, scaffold requirements.txt; PR #96 (open) adds `prototype/backend/main.py`, pyproject.toml, uv.lock, test_main.py; no ESP32, Angular or PostgreSQL project in any merged branch |

**Merge first** (not counted until it's in `develop` or `main`): PR #96 (open) — FastAPI scaffold with tests and uv.lock into develop; PR #100 (open, into main) — diagrams, design docs and proposal.md updates; feature/23-approach-environment — 8 commits incl. Lightsail §4, not in develop; feature/86-lightsail-hosting — 2 commits not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #96, PR #100 and feature/23-approach-environment into develop, then release to main.
2. Write one spec per epic in `docs/specs/` (#47, #50, #56), first lines naming epic and stories; link each in proposal §4.
3. Fill proposal §4 Environment and resources with language, framework, ESP32 hardware, PostgreSQL, Lightsail and reasons tied to §3.
4. Add a sequence diagram (scan, upload, identify) and dashboard screen flow to `docs/design/`; add all diagrams to §4 with captions.
5. Scaffold ESP32 firmware (#92), Angular dashboard (#94) and PostgreSQL (#93) in `prototype/`; assign owners.
6. List every task (#67-#101) in the §4 work-items table and add sp: to #75, #82, #97.

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

### G07 · Mighty Morphins: Online Materials Database

*Web app that extracts material data from vendor CoC and test-report PDFs into a searchable AWS database.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Close #47: choose the DBMS, backend, frontend, extraction method and AWS services with reasons, and write them into proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #11, #17, #22 with 15 objective-titled stories (#12-#27) have no milestone or assignee. Sprint 2 work (#48, #49, tasks) is on the board. Develop and main disagree on typed refs. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #11 Goal 1 Automated Material Data Extraction and Verification; Epic #17 Goal 2 Centralized Material Data Storage and Management; Epic #22 Goal 3 Material Data Access and Analysis. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: PDF upload, extract, verify, store flow; er: material records, vendors, source documents stored; uml: sequence of upload, extraction, verification, storage; ui_flow: search, filter and display screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (main only; develop §4 is a skeleton). Language: Python (backend, extraction); Framework: TBD backend and frontend; document processing TBD; Platform: AWS services (undetermined); Data: relational DB on AWS (story #19); DBMS 'TDB'; Hosting/hardware: AWS; Sponsor resources: EL-1: vendor CoC and internal test-report PDFs; Tools: VS Code, Git and GitHub. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and tests/test_login.py: unchanged course example; prototype/requirements.txt: unchanged scaffold copy; prototype/README.md: template text, project title placeholder |

**Merge first** (not counted until it's in `develop` or `main`): PR #68 task/36-use-case-diagram (open to main) — use-case.md and png; branch has 39 commits not in develop; #67 — port the typed-link fix from develop into main; main §4 is real, develop §4 is a skeleton.

**To do before your Sprint 2 review:**

1. Decide the stack in #47 (DBMS, backend, frontend, extraction/OCR, named AWS services) and write each with a reason into proposal §4 on main.
2. Merge PR #68, then draw architecture and system context diagrams, the DFD (#40), ER (#38) and wireframe (#41) into docs/design/ with captions.
3. Fill the empty image and document links in proposal §4 on main; no link may point at a missing file.
4. Assign #46, #58, #59 and write docs/specs/ specs naming each epic and its stories in the first lines; link them from §4.
5. Replace prototype/login.py and tests with a skeleton for your stack, a requirements.txt, .env.example, and README commands.
6. Sync main and develop (#67) so both carry the same §2 and §4 with typed refs; do the work on develop and release to main.
7. Add sp: to #36-#41, #47, #46, #58, #59 and #63.

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

### G09 · Sigma Squad: Vehicle Maintenance Logger

*Web app tracking vehicle service history and recommending next maintenance with urgency alerts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Do #16 and #17 first: agree the stack in one meeting and write it, with reasons, into §3 and §4; every other Sprint 2 item depends on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 goal epics (#27,#28), 10 objective-titled stories with sp, assignee, sprints; Sprint 2 stories #29-#31. 28 of 29 issues linked, typed. No tasks for specs, design or wiring. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #27 Goal 1 Vehicle data and maintenance tracking; Epic #28 Goal 2 Scheduled recommendations and alerts. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: vehicles, service history, rules, users stored; uml: sequence of due-mileage calculation and alert; ui_flow: vehicle select, history entry, dashboard; dfd: service-history import into recommendation engine. |
| 4. Environment | ❌ not started | Stated in: nowhere (§3/§4 skeletons; HW#4 only says web and/or mobile app). Platform: web app (mobile undecided); Data: database plus REST API (Objective 1.2); vehicle data source undecided; Sponsor resources: none (independent); Tools: GitHub, CI. |
| 5. Prototype wiring | ❌ example files only | prototype/ holds only course login.py, test_login.py, README, requirements.txt, unchanged |

**To do before your Sprint 2 review:**

1. Finish #16 and #17: choose language, framework, DB, hosting, vehicle data source; write §3 and §4 with reasons.
2. Add Sprint 2 tasks for specs, design and wiring with assignee and sp; list them in §4 work-items table.
3. Write specs for epics #27 and #28 tracing FR/NFR to stories #29-#38, in proposal §4 or docs/specs/ files linked from §4.
4. Draw architecture, context, ER, recommendation sequence and dashboard wireframe as Mermaid or PNG in proposal §4; caption each.
5. Create prototype skeleton for the chosen stack with manifest, .env.example, README run steps, smoke run; delete login.py.
6. Remove epic refs from §1 and link #46 in §4.
7. Recommended: put full spec and design detail in docs/specs/ and docs/design/, keeping summary and diagrams in proposal.md.

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

*Mobile app that tracks runners live, shares posts to web pages and predicts race finish times.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Do #48 first: write the environment and tech stack in proposal §4 with a reason per choice, since the spec, diagrams and skeleton all depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#4, #26, #27), 6 objective-titled stories (#28-#33), all Sprint 2 with assignee and sp. Sprint 2 tasks #42-#49 are on the board but missing from §4. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #4 Goal 1 Live Runner Tracking; Epic #26 Goal 2 Posts and Shareable Web Page; Epic #27 Goal 3 Race Time Prediction. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: GPS data to tracker to posts to predictor; er: runs, routes, posts, race data stored; uml: sequence of live tracking update every 5 seconds; ui_flow: mobile tracking screens and the public post page. |
| 4. Environment | ❌ not started | Stated in: nowhere. Platform: mobile app plus a public web page (HW#4); Data: public marathon routes and times (HW#4); Hosting/hardware: smartphone GPS; Sponsor resources: independent; Tools: GitHub, GitHub Actions CI. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and tests/test_login.py: unchanged course example; prototype/requirements.txt: unchanged scaffold copy; prototype/README.md: template text with placeholders |

**To do before your Sprint 2 review:**

1. Do #48: write the stack (language, mobile/web framework, backend, data store, GPS/map API, ML tooling) with reasons into proposal §3 and §4.
2. Do #43-#45: write one spec per goal naming the epic and stories first, with scope, FR/NFR, acceptance criteria, open questions; link from §4.
3. Do #46 and #47: draw architecture, context, sequence, DFD, ER and screen flow in docs/design/ and embed them in proposal §4 with captions.
4. Do #49: replace prototype/login.py with a skeleton built with the chosen framework, a manifest, .env.example and a README smoke run.
5. Do #42: link every Sprint 2 task in §4 as typed refs and move #13 from §2 to §4; add sp: to #43-#47 and #49.
6. Get every Sprint 2 change merged into develop through PRs; the Sprint 2 milestone is due today.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Explainable 6G Waveform Classification

*Application that finds signal peaks, classifies simulated 6G waveforms and explains each result with calibrated confidence.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Write the spec for epic #57 (peak picking) from docs/baseline-peak-picker.md into docs/specs/, then link it from proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 5 goal epics (#57-#61) plus #103; objective-titled stories mostly on board, but #63, #67, #68, #70, #71, #95 lack milestone or assignee. 18 of 34 §4 links typed on develop, 0 on main. |
| 2. Specs | ⚠️ started | docs/confidence-calibration.md (develop) — story #65 only; handoff doc, not in docs/specs; docs/baseline-peak-picker.md (develop) — story #66 baseline method and results; not a spec Missing: Epic #57 Signal Detection & Preprocessing; Epic #58 Application interface and cross functional integration; Epic #59 Waveform Identification & Receiver Processing; Epic #60 Modulation, Decision & Explainable AI (only story #65 covered); Epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: .iq file to peaks to classifier to explanation; uml: sequence of CLI/GUI calling the shared engine; ui_flow: GUI screens (story #63, #84). |
| 4. Environment | ⚠️ partial | Stated in: proposal §4. Language: MATLAB and Python; Framework: MATLAB 6G Simulink library; numpy, scipy, h5py; Captum planned (#64); Platform: local desktop; pytest in CI; Data: mentor-provided .iq captures; generated labeled datasets; Hosting/hardware: local; no hosting stated; Sponsor resources: RTX-1 mentor data; Tools: GitHub Actions CI, pytest. |
| 5. Prototype wiring | ⚠️ started | prototype/requirements.txt: pinned numpy, scipy, h5py only; prototype/README.md: setup, analyze_iq.py run, pytest commands; prototype/waveform_identification/ and prototype/xai/: layout following the architecture; prototype/tests/: 41 tests per README; login test still present; prototype/data/raw/.gitkeep: no sample capture to run on |

**Merge first** (not counted until it's in `develop` or `main`): PR #106 feature/69-model-selection to develop (open) — proposal §3.1 model selection; branches Application-Structure (5 commits) and docs/team-documentation (1 commit) not in develop; develop to main — peak picker, XAI code and calibration docs are on develop only.

**To do before your Sprint 2 review:**

1. Write docs/specs/ specs for epics #57-#61, naming epic and stories in the first lines; link them from proposal §4 with summaries.
2. Draw architecture, system context, pipeline DFD, GUI wireframe and sequence diagrams in docs/design/ and embed them with captions in §4 Diagrams.
3. Link docs/baseline-peak-picker.md and docs/confidence-calibration.md from §4, or fold their requirements into the specs.
4. Rewrite §4 Environment as a table of language, ML framework, CLI/GUI toolkit, data and tools with reasons tied to §3.
5. Remove prototype/login.py and its test; update requirements.txt and add a smoke run on a tiny sample capture.
6. Merge PR #106 and the Application-Structure branch through PRs, then release develop to main.
7. Fix the typed refs on main and develop; link #96, #103; assign and set Sprint 2 for #63, #67, #68, #70, #71.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. assignment manager

*Windows desktop app for assignments with difficulty-based deadlines, progress tracking, and native toast reminders.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Link specs-G1/G2/G3 in proposal §4 and merge develop into main, then pick the desktop shell so prototype wiring can start.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | 3 epics (#16-#18), 9 objective-titled stories (#19-#27), about 50 features/tasks with parents; Sprint 2 items assigned. Develop has typed refs, main has none. #25-#27 lack milestone. |
| 2. Specs | ⚠️ started | docs/specs/specs-G1.md (develop) — epic #16, stories #22-#24; scope, FR/NFR, ACs, questions; docs/specs/specs-G2.md (develop) — epic #17, stories #19-#21; FR table, NFRs; docs/specs/specs-G3.md (develop) — epic #18, stories #25-#27; only 4 FRs, 1 NFR |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: UI to Python core to local store; er: assignments stored locally (task #13); uml: sequence for create assignment over IPC bridge; ui_flow: dashboard, creation form, edit, alert panels. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (develop); prose only, no per-choice reasons. Language: Python backend, JavaScript frontend; Framework: desktop shell not named; IPC bridge between JS UI and Python core; Platform: Windows desktop, offline; Data: local JSON or SQLite (undecided, specs-G1); Hosting/hardware: local Windows machine; no hosting; Sponsor resources: none stated; Tools: Windows script host / native toast bindings; no tool list. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, tests/test_login.py: course example unchanged on both branches; prototype/requirements.txt: scaffold copy; README is template text; No package.json or desktop-shell project anywhere |

**Merge first** (not counted until it's in `develop` or `main`): develop (not main): specs-G1/G2/G3, sprint-2 review (PR #112), typed-ref proposal §4; merge develop into main; Branches feature/34-project-proposal (28 commits), updated-proposal (6), sprint1-patch-1 (1) not in develop; review or close.

**To do before your Sprint 2 review:**

1. Incorporate specs-G1/G2/G3 into proposal.md §4: one summary per epic (#16-#18) plus a link, in the Specification and design documents table with issue numbers.
2. Merge develop into main so the proposal §4 (typed refs, 54 work-item links) and the specs reach main.
3. Add architecture, system-context, ER and create-assignment sequence diagrams to proposal.md §4 as Mermaid or figures, captioned; covers #13 and #44.
4. Recommended: keep detailed design in docs/design/ and full specs in docs/specs/, with summaries and diagrams in proposal.md.
5. Decide desktop shell and storage (JSON vs SQLite), add reasons per choice to §4 Environment, and resolve the encryption question in specs-G1.
6. Replace prototype/login.py with the skeleton: package.json/requirements.txt, ui/ core/ storage/ notifier/, .env.example, README, and a smoke run saving one record via the IPC bridge (#58).
7. Set sp:/milestone on #25-#27, #111, #113; link #107, #111, #113 in §4; triage the three stale branches.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: Cyber Sandbox

*AI-assisted cybersecurity training sandbox: simulated desktop VM where users investigate and contain malware incidents.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Write `docs/design/architecture.md` and `system-context.md` (#53, #54): §4 already cites them but they exist on no branch.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 epics (#22, #23), 18 objective stories (#24-#41), all linked. Stories have no assignee or Sprint 2 milestone; epics/stories also cited in §4 (39 misplaced refs); #44, #45 untyped. |
| 2. Specs | ✅ done | `docs/specs/training-environment.md` (main, develop) — Goal 1 epic #22, stories #24-#32; scope, FR, NFR, acceptance; `docs/specs/ai-scenarios.md` (main, develop) — Goal 2 epic #23, stories #33-#41; scope and FRs; no NFR/open-questions headings seen |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: scenario data moves through LLM, validation, loader; er: scenario schema and action logs are persisted; uml: sequence for configure-generate-validate-load-report; ui_flow: PySide6 desktop screens and transitions. |
| 4. Environment | ✅ done | Stated in: proposal §4. Language: Python 3.x; Framework: PySide6 (desktop UI), Pydantic (schema validation); Platform: Local desktop on Windows/macOS/Linux; Data: In-memory state; optional file fixtures; Hosting/hardware: Local machine only, no hosting; Sponsor resources: Independent; NRP.ai-compatible LLM endpoint (account and API key via env vars); Tools: GitHub Issues/Projects/Actions, pytest, .env + .env.example. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `prototype/tests/test_login.py` still the course example; `prototype/README.md` still says 〈project title〉 and describes the login example; `prototype/requirements.txt` unchanged course copy; no `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #64 (docs/issue-55-dfd -> main) — DFD source, image, §4 reference; open; branch copilot/create-requirements-list-for-goal-2-47 — 1 commit not in develop; merge or delete.

**To do before your Sprint 2 review:**

1. Create `docs/design/architecture.md` and `system-context.md` with Mermaid diagrams (#53, #54); proposal §4 cites them but they exist on no branch.
2. Merge PR #64 for the DFD, then add `data-model.md` (#56), `scenario-sequence.md` (#57), `user-flow.md` (#58).
3. Replace the scaffold prototype (#60): remove login files, create the PySide6 skeleton, `requirements.txt`, `.env.example`, README setup/run, and a smoke run.
4. Write proposal §3 (#61) with approach, alternatives and rationale, then remove the placeholder text still in the proposal.
5. Backfill stories #24-#41 (#62): assignee, Sprint 2 milestone where in scope; cite epics/stories only in §2.
6. Add acceptance criteria and open questions to `docs/specs/ai-scenarios.md`.
7. Type or close #44 and #45 and link them from §4.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Constrained-hardware ECS game engine

*Lightweight ECS game engine for older OpenGL hardware, with a top-down 3D bullet-heaven demo game.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Fill proposal §4 Environment and resources (language, OpenGL version, CMake, libraries, OS targets): wiring and design depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 epics (#24 Game Engine, #25 Game Demo), 8 objective stories (#26-#33), none assigned or on Sprint 2. §2/§4 on develop use bare #n, 0 typed refs; §4 still skeleton. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #24 Game Engine; epic #25 Game Demo. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: ECS component/system classes and game loop; ui_flow: editor and demo screens. |
| 4. Environment | ❌ not started | Stated in: nowhere. Platform: Windows, Linux, possibly Mac (README); Hosting/hardware: Older/low-end hardware, older OpenGL (abstract); Sponsor resources: Independent; Tools: CMake (task #46). |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `prototype/tests/test_login.py`, README still the course example; no dependency manifest and no CMake files on either branch; tasks #46 (CMake) and #9 (window + cube) open |

**Merge first** (not counted until it's in `develop` or `main`): PR #51 (develop) — draft §4 System Context Diagram (#47); open; branch documentation/50-Revise-Sprint-1-from-Feedback — 5 commits not in develop; main lags develop: proposal on main is still template.

**To do before your Sprint 2 review:**

1. Write proposal §3 and §4 Environment and resources; both are still template text (§4 has 35 placeholders on develop).
2. Write `docs/specs/game-engine.md` and `game-demo.md` (#49) and link both from §4 with typed issue refs.
3. Merge PR #51 for the system context diagram; add the architecture diagram (#48) with figure numbers and captions.
4. Do CMake setup (#46) and window + cube (#9) in `prototype/`; remove the login scaffold; document build and run.
5. Convert §2/§4 refs to typed form; assign stories and set Sprint 2 milestone and `sp:`; add §4 rows for #46-#50.
6. Merge branch documentation/50 and develop into main so current work is graded.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · neuroprosthetic: BridgeWatch (SNX-3)

*Real-time detection of cross-chain bridge exploits with baselines, alert rules and an operator dashboard (SNX-3).* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Create `docs/design/architecture.md` (#62) with editable Mermaid architecture and context diagrams; the proposal already promises it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | 3 epics (#11-#13), 9 objective stories (#5, #14-#21) with assignee, sp: and sprint; all 33 issues linked with typed refs; Sprint 2 tasks on board. |
| 2. Specs | ✅ done | `docs/specs/goal-1-baseline.md` (develop) — epic #11; FR/NFR; no acceptance or open-questions heading seen; `docs/specs/goal-2-detection.md` (develop) — epic #12; rules, FR/NFR, acceptance; no open questions; `docs/specs/goal-3-dashboard.md` (main, develop) — epic #13; scope, FR/NFR, acceptance, open questions |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: transfers flow source, detector, store, alerts; er: SQLite transfers, alerts, cursor tables; uml: sequence for live ingest-detect-notify loop; ui_flow: dashboard parts (status, flow, alerts). |
| 4. Environment | ✅ done | Stated in: proposal §4 (Table 6) and `prototype/README.md`. Language: Python 3.12; Framework: FastAPI, uvicorn, httpx; web dashboard page; Platform: Windows 11 and Ubuntu (CI); Data: SQLite; SonarX data requested, no reply yet; Hosting/hardware: Docker packaged; host not chosen; Sponsor resources: SNX-3: SonarX transfer/balance/price data and real-time stream; public Ethereum nodes; Chainlink fallback; Tools: GitHub Actions CI, pytest, Slack webhook. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` pinned, `requirements-dev.txt`, `.env.example` (develop); `prototype/bridgewatch/` modules mirror source/detector/store/notify/app architecture; `prototype/README.md` run commands; `run_bridgewatch.py`, tests, `Dockerfile.bridgewatch` |

**Merge first** (not counted until it's in `develop` or `main`): PR #77 (develop) — marks Goal 1 spec as written in Table 9; open; branch 61-table-9-row — same change, 1 commit not in develop; develop -> main release: goal-1/goal-2 specs, `.env.example`, SonarX stub are not on main.

**To do before your Sprint 2 review:**

1. Write `docs/design/architecture.md` (#62) with Mermaid architecture and system-context diagrams replacing the image-only Figures 1 and 2; list it in Table 9.
2. Add data flow, an ER diagram from `prototype/bridgewatch/store.py`, and a live-loop sequence diagram, each captioned in proposal §4.
3. Add acceptance criteria and open questions to `docs/specs/goal-1-baseline.md`; open questions to goal-2.
4. Merge PR #77, then open the develop-to-main release PR so the specs and `.env.example` reach main.
5. Finish #72: confirm the fresh-machine smoke run is in `prototype/README.md`, then close it; send the SonarX questions (#28).
6. Add a reason per Table 6 row tied to §3.

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
