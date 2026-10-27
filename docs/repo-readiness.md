# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-10-27 19:47 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G01](#g01) BGAF | Tue Oct 27 | ⚠️ | ✅ | ✅ | ⚠️ | ✅ |
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) EpicEngineers | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G07](#g07) Mighty Morphins | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G11](#g11) 5 Guys | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G13](#g13) BYKX | Thu Oct 29 | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G16](#g16) G16 | Thu Nov 5 | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G17](#g17) SonicScape (EchoSphere) | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 7 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G08, G13, G16).
- **Design and diagrams:** 10 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G07, G08, G10, G16, G18).
- **Environment:** 15 of 20 have written their environment choices into the repository (G01, G02, G03, G04, G05, G06, G07, G08, G10, G12, G13, G14, G16, G18, G19).
- **Prototype wiring:** 8 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G03, G05, G06, G08, G12, G16, G18).
- **Waiting in a branch or open pull request:** G01, G02, G04, G06, G12, G13, G16, G19, G20. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting (SNX-4)

*Rebuild Hyperliquid order books from SonarX data, validate them, and backtest strategies on validated days.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Rewrite proposal §4 Environment and resources so it matches what the prototype and `docs/design/database.md` already chose (DuckDB, React/Vite).

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 epics #20-22 plus Sprint 2 epics #71-74, #89, #90; stories use objective wording; 71 of 73 issues linked; Goal stories #23-28 still open. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1 (#20, stories #23, #24); FR, acceptance, open questions; `docs/specs/validation.md` (main) — Goal 2 (#21, #25, #26); names dated market events; `docs/specs/backtest.md` (main) — Goal 3 (#22, #27, #28); fill model, costs, metrics |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: multi-step data pipeline; er: stored events, snapshots, results; uml: market-day critical flow; ui_flow: research workspace front end. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (stale) + README + design docs. Language: Python 3.12 (pipeline), TypeScript (front end); Framework: React + Vite front end; pytest; Platform: team laptops; GitHub Actions CI; Node 20.19+/22.12+; Data: Parquet + DuckDB (`duckdb==2.0.0`), per `docs/design/database.md`; Hosting/hardware: none; local laptops, 1 market x 1 week; Sponsor resources: SonarX requester-pays S3 buckets, Hyperliquid archive, AWS account + CLI; Tools: GitHub Actions, npm, oxlint, pytest, Mermaid. |
| 5. Prototype wiring | ✅ done | `prototype/src/bgaf_pipeline/` six step modules mirror the architecture; `prototype/requirements.txt` pins pytest and duckdb; `pyproject.toml` present; `prototype/frontend/` Vite React skeleton with package-lock.json; `prototype/README.md` setup, test, front-end run commands; PR #139 DuckDB load |

**Merge first** (not counted until it's in `develop` or `main`): Branch `Damon` — 1 commit not in develop; `develop` is 34 commits behind main — sync main into develop or retire develop.

**To do before your Sprint 2 review:**

1. Update proposal §4 Environment on main: Python 3.12, DuckDB/Parquet, React/Vite, Node, AWS CLI and requester-pays S3, each with its reason from §3.
2. Add the ER diagram (`docs/design/database.md`) and the wireframe as numbered figures with captions in proposal §4 Diagrams.
3. Add `prototype/.env.example` and fill README status rows; remove the course `login.py` and `tests/test_login.py` in their own PR.
4. Link #58 and #140 in proposal; give #94 and #82 sp: and a Sprint milestone; assign #24, #26, #27, #69.
5. Resolve the README contradiction: front-end framework 'still open' (#114) yet the skeleton exists; record the decision in `docs/design/frontend-architecture.md`.
6. Mark the three specs reviewed once open questions (gate threshold, SonarX gaps) get answers; keep SonarX questions #41, #42 moving.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: distributed signal capture for nearby recording devices (RTX-4)

*ESP32 nodes capture Wi-Fi/Bluetooth metadata; a backend identifies recording devices and a dashboard shows them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Merge `feature/23-approach-environment` and PR #96 into develop, then release develop to main so the environment choices and diagrams are on the record.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #47, #50, #56 with 15 'Objective n.m' stories; Sprint 2 work is tasks; only 18 of 60 issues linked from proposal; §4 is a skeleton. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Goal 1 #47 Collect wireless metadata; Goal 2 #50 Identify recording devices; Goal 3 #56 Dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: ESP32-to-server upload sequence; ui_flow: Angular dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: issue titles #91-#95, #86 and unmerged branch `feature/23-approach-environment`; proposal §4 is a skeleton. Language: C/C++ (ESP32 firmware), Python (backend), TypeScript (Angular); Framework: FastAPI backend, Angular dashboard; Platform: ESP32 capture nodes; SSH-tunnel development; Data: PostgreSQL (#93); Hosting/hardware: ESP32 boards; AWS Lightsail proposed (#86); Sponsor resources: RTX-4 guidance: passive capture only; no Flock camera data; Tools: draw.io, Mermaid, GitHub Actions. |
| 5. Prototype wiring | ❌ example files only | develop `prototype/` holds only `login.py`, `tests/test_login.py`, scaffold README and requirements; Open PR #96 adds `prototype/backend/` FastAPI, pyproject, uv.lock, test_main.py; No ESP32 firmware, Angular app, or PostgreSQL setup in any merged branch |

**Merge first** (not counted until it's in `develop` or `main`): PR #96 — FastAPI scaffold in prototype/backend (open into develop); Branch `feature/23-approach-environment` — §3/§4 and Lightsail hosting; 6 commits not in develop; Branch `feature/86-lightsail-hosting` — 2 commits not in develop; develop to main — diagrams #77, #84, #97 exist only on develop.

**To do before your Sprint 2 review:**

1. Merge PR #96 and the `feature/23-approach-environment` branch, then fill proposal §4 Environment with ESP32, FastAPI, PostgreSQL, Angular, Lightsail and reasons.
2. Write three specs in `docs/specs/` (one per goal epic #47, #50, #56) and link them in proposal §4 'Specification and design documents'.
3. Add captioned figures for architecture, context, DFD and ER to proposal §4 Diagrams and link `data-flow.md`, `system-context.md`; add an architecture doc.
4. Scaffold the ESP32 (#92), Angular (#94) and PostgreSQL (#93) projects in `prototype/` with `.env.example` and a smoke run; assign owners.
5. Add a sequence diagram (ESP32 upload to backend) and dashboard wireframes for Goal 3.
6. Link every Sprint 2 task in proposal §4; add sp: to #75, #82, #97; replace untyped meeting issues #79, #80 with typed ones.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: equation transcription, data generation and model training notebook (RTX-3)

*Jupyter notebook that transcribes an equation, generates training data, trains a model and plots results.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Merge PR #66, then write proposal §4 Environment naming the exact AI services, PyTorch/Jupyter versions, and how API keys are supplied.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-4 epics #28, #27, #43, #44; stories use objective wording; several stories lack a Sprint milestone; 14 untyped issues; 18 of 36 not in proposal. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (develop) — Goal 1 (#28); only #33 written, #30, #50 TBD; `docs/specs/data-generation.md` (develop) — Goal 2 (#27); #36, #35, #48 done; #34, #31 TBD Missing: epic #43 Goal 3 train a model; epic #44 Goal 4 notebook output. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er: only if datasets get a stored schema; ui_flow: notebook cell flow where user input is needed. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 only; §4 Environment is still a placeholder. Language: Python; Framework: Jupyter notebook (sponsor-required UI); PyTorch for training; Platform: user's local machine for training; Data: CSV / .npy datasets (spec); Hosting/hardware: none stated; Sponsor resources: external AI services for transcription and dataset generation; models not yet named; Tools: Mermaid, GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | develop `prototype/transcriber.py`, `verifier.py`, `generate_dataset.py`, `train.py` exist; `prototype/tests/test_verifier.py` is the only test file; `prototype/requirements.txt` and README are still unchanged course scaffold; No notebook `.ipynb` and no `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #66 — Release 0.2: develop to main with specs, diagrams, prototype code.

**To do before your Sprint 2 review:**

1. Merge PR #66 so specs, diagrams and prototype reach main.
2. Write proposal §4 Environment: Python/PyTorch versions, Jupyter, the named AI services, API-key handling, local compute, each with its reason.
3. Pin real dependencies in `prototype/requirements.txt`, add `.env.example`, replace the scaffold README with working setup and run commands.
4. Create the starter notebook in `prototype/` that runs transcribe, verify, generate on one equation as a smoke run.
5. Complete TBD sections in both specs and add specs for Goals 3 and 4 (#43, #44).
6. Clean the board: type or delete untyped meeting issues, add Sprint milestone and assignees to stories, link #51, #60, #65 in §4.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · EpicEngineers: Polymarket wallet PNL and trader profitability dashboard (SNX-1)

*Compute PNL for Polymarket proxy wallets from SonarX Snowflake data, rank traders, and show a dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Settle the stack decision in #52 and write it into proposal §4; the prototype skeleton and Snowflake smoke run (#62) cannot start until then.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #24, #29, #33 with 15 'Objective' stories; 40 of 41 issues linked; Sprint 2 has 17 open tasks; only #25 and #34 stories are in Sprint 2. |
| 2. Specs | ⚠️ started | `docs/specs/pnl-calculation.md` (main, develop) — Goal 1 (#24); worked example, FIFO; `docs/specs/trader-ranking.md` (develop) — Goal 2 (#29); ranking and behavior metrics Missing: epic #33 Goal 3 dashboard (draft in open PR #73). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: dfd: query-to-dashboard data pipeline; er: derived PNL and ranking tables; uml: sequence for a PNL run (#59); ui_flow: dashboard leaderboard and wallet pages. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (Snowflake only); `docs/design/implementation.md` on main. Language: not chosen; Framework: not chosen (#52 open); Platform: not chosen; Data: Snowflake (SonarX Polygon warehouse); Hosting/hardware: not stated; Sponsor resources: SonarX Snowflake access; open-source tools allowed; Tools: Predicts.guru / Polymarket Analytics for validation. |
| 5. Prototype wiring | ❌ example files only | `prototype/` holds only course `login.py`, `test_login.py`, scaffold README and requirements; `docs/design/implementation.md` proposes a layout with `.env.example` but nothing is created; Issue #62 (skeleton + Snowflake connection) is open |

**Merge first** (not counted until it's in `develop` or `main`): PR #81 — revised architecture and context diagrams into main; PR #79 — dashboard flow doc and diagram into develop; PR #73 — dashboard questions spec (#34) into develop; PR #72 — Sprint 2 review draft into develop; Branches `55-pnl-calculation-spec`, `58-data-flow-diagrams` — DFD L0/L1 not in develop.

**To do before your Sprint 2 review:**

1. Decide and record the prototype stack (#52) in proposal §4 and `CLAUDE.md`; replace 'not chosen yet' with language, framework, hosting.
2. Merge open PRs #73, #79, #81 and the DFD branch; sync main and develop, which have diverged.
3. Link `docs/design/architecture.md` and all new diagrams in proposal §4 with numbered captions.
4. Write the ER (`data-model.md`, #57) and PNL-run sequence (`pnl-pipeline.md`, #59).
5. Create the prototype skeleton and Snowflake connection smoke run (#62) with `.env.example` and README.
6. Replace the small architecture sketch with real components; give #80 sp: and an assignee.

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: Whale Identification/Location System (own project, no sponsor)

*AI that detects and identifies whale calls in hydrophone audio, then locates the source by time difference.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge PR #48, then draw the architecture and system context diagrams in `docs/design/` and embed them in proposal §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #8, #14; 9 objective stories (1.1-1.5, 2.1-2.4) in Sprint 2 with assignees; 12 other issues not linked in proposal §4. |
| 2. Specs | ⚠️ started | `docs/specs/goal-2-locator.md` (develop) — Goal 2 (#14, #15-#18); scope, FR/NFR, criteria, open questions Missing: epic #8 Goal 1 whale-call recognizer. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for any project; dfd: audio to detector to locator pipeline; er: whale database schema exists (`db/init/schema.sql`); uml: sequence for detect then locate. |
| 4. Environment | ⚠️ partial | Stated in: prototype README and requirements.txt only; proposal §4 is a skeleton. Language: Python; Framework: PyTorch, librosa, scipy, numpy; Platform: local machines, venv; Windows and Mac/Linux commands; Data: PostgreSQL via `docker_compose.yaml` and `db/init/schema.sql`; whale audio datasets; Hosting/hardware: none; simulated hydrophone recordings; Sponsor resources: none (own project); public whale call datasets; Tools: GitHub Actions, pytest, docker compose. |
| 5. Prototype wiring | ✅ done | develop `prototype/locator/` and `ai-detector/` mirror Goals 2 and 1; `prototype/requirements.txt` pins numpy, scipy, torch, librosa; `prototype/.env.example` and README setup/run/test; `python -m locator.smoke`; Tests: `tests/test_tdoa.py`, `test_locate.py`, `test_save_call.py` |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 — develop to main: locator, detector, spec, .env.example, README; develop holds all Sprint 2 work; main has only the ER image and DB init.

**To do before your Sprint 2 review:**

1. Merge PR #48 so the spec, prototype and README reach main.
2. Draw high-level architecture and system context diagrams in `docs/design/` with source and PNG; add a DFD for audio to detector to locator.
3. Embed the ER diagram and new figures in proposal §4 Diagrams with captions; export an editable ER source.
4. Write proposal §4 Environment (Python, PyTorch, librosa, PostgreSQL via docker, datasets) with reasons tied to §3.
5. Write `docs/specs/goal-1-recognizer.md` for epic #8 and stories #9-#13, then link it in the §4 table.
6. Link all non-story issues (#20-#42) in proposal §4 and fix README commands that no longer exist.

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

*Web app that extracts material data from CoC and test-report PDFs into a verified, searchable relational database.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Close #47 (tech stack and AWS services): the DBMS and framework choice drives the ER diagram, three specs and the prototype skeleton.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #11,#17,#22,#42,#45 and stories titled as objectives, all linked in proposal. Sprint 2 stories #48,#49 and design tasks #36-#41 are assigned, but spec tasks #46,#58,#59 have no assignee. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Goal 1 Automated Material Data Extraction and Verification (#11, task #46); Goal 2 Centralized Material Data Storage and Management (#17, task #58); Goal 3 Material Data Access and Analysis (#22, task #59). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: PDF ingest, OCR, extract, verify, store pipeline; er: relational records with source-document links; uml: sequence for upload to verified record; ui_flow: internal search/compare web pages; context: Edwards users, PDFs, AWS services. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (table, with TBD rows) and §3. Language: Python (backend, extraction, processing); Framework: TBD backend and frontend; Platform: web application; AWS-hosted per Objective 2.2; Data: relational database, product TBD (typo TDB); Hosting/hardware: AWS, services not yet named (#47 open); Sponsor resources: CoCs and internal test-report PDFs from EL-1; not listed in section 4; Tools: VS Code, Git/GitHub. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` are the course example; `prototype/README.md` still has the template text and placeholders; No team manifest or `.env.example` |

**Merge first** (not counted until it's in `develop` or `main`): PR #68 (task/36-use-case-diagram) — use-case diagram `docs/design/use-case.md` and PNG; 28 commits not in develop, rebase first.

**To do before your Sprint 2 review:**

1. Close #47: pick DBMS, backend and frontend framework, OCR/extraction tool and AWS services; write them in the proposal section 4 table with reasons.
2. Assign #46, #58, #59 and write the three specs in `docs/specs/`, each naming its epic and stories in the first lines.
3. Finish #38, #39, #40 as Mermaid or exported images in `docs/design/`; add the missing context diagram and #41 wireframe.
4. Fill the empty diagram and document links in proposal section 4 (`[...]` and `[...]`), and add captions.
5. Rebase and merge PR #68 into main; bring main's proposal content back into develop (develop section 4 is still a skeleton).
6. Replace `prototype/login.py` with a skeleton for the chosen stack, a manifest, `.env.example` and README commands.

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

### G11 · 5 Guys: Marathon Tracker App

*Phone GPS app showing a runner's live position, posts, and predicted finish time to spectators.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/markachavez2003-lab/CPSC490-G11-5Guys)

**Start here:** Pick and write down the stack in proposal §4 (mobile framework, backend, database, map service); every spec, diagram, and the prototype depends on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#4, #26, #27), 6 stories (#28-#33) titled with objective wording; stories on Sprint 2 with assignee and sp:3. No typed refs; #13 bare; #42 missing from board. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #4 Goal 1: Live Runner Tracking; epic #26 Goal 2: Posts and Shareable Web Page; epic #27 Goal 3: Race Time Prediction. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: GPS to server to spectator page; er: runners, posts, locations, past runs stored; uml: sequence for live position update; ui_flow: runner app and spectator web page. |
| 4. Environment | ❌ not started | Stated in: nowhere (§3 and §4 still skeleton; HW#4 only mentions smartphone GPS, ML, public marathon data). Platform: smartphone app plus public spectator web page (HW#4 only); Data: database implied by Goal 1 success measure; not chosen; Sponsor resources: independent; public marathon route/results data (HW#4). |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, tests/test_login.py: unchanged course example on main and develop; prototype/requirements.txt: unchanged scaffold copy; prototype/README.md: still the template text |

**To do before your Sprint 2 review:**

1. Decide and write the tech stack in §3/§4 (mobile framework, backend, DB, map API, hosting), one reason each, tied to Goals 1-3.
2. Write three specs in proposal.md §4 (summary per epic), one per epic #4, #26, #27, tracing FRs to stories #28-#33 with acceptance criteria.
3. Draw architecture and system-context diagrams in proposal §4 as Mermaid or images, add exported images, and caption them in §4.
4. Recommended once §4 has the summaries: move full spec/design detail into docs/specs/<epic>.md and docs/design/, linking each from §4.
5. Add DFD, ER diagram, and a sequence diagram for the position-update flow; add screen flow for runner and spectator views.
6. Replace prototype/login.py with the framework skeleton, manifest, .env.example, working README, and a smoke run.
7. File Sprint 2 task issues with assignee, sp:, Sprint 2 and link them in §4 as typed refs; link #42 and fix the bare #13 ref.

[↑ Back to all groups](#groups)

<a name="g12" id="g12"></a>

### G12 · ACJMM: Waveform identification and modulation classifier with explainable AI

*Detects signal peaks, identifies 6G waveforms and modulation, with confidence, Unknown abstention and CLI/GUI.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Merge PR #102 with a real `prototype/README.md` and `requirements.txt`, so the peak picker and XAI code have documented, runnable setup.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Five epics #57-#61, stories titled as objectives, Sprint 2 stories assigned. Develop links 17 typed refs; main has none. #95-#98 not in proposal; #95-#97 have no milestone. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #57 Signal Detection & Preprocessing; Epic #58 Application interface and cross functional integration; Epic #59 Waveform Identification & Receiver Processing; Epic #60 Modulation, Decision & Explainable AI; Epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: IQ samples to peaks to classifier to explanation; uml: sequence for classify with Unknown abstention; ui_flow: GUI screens mirroring CLI inputs and outputs; er: only if results or retraining cases are stored. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose only). Language: MATLAB, possibly Python (develop code is Python); Framework: MATLAB 6G Simulink library; Captum planned in issues; Platform: not stated (desktop CLI and GUI); Data: IQ data from mentors; no store named; Hosting/hardware: not stated; Sponsor resources: mentor-provided signal data (RTX-1); Tools: not listed beyond MATLAB/Python. |
| 5. Prototype wiring | ⚠️ started | develop `prototype/xai/calibration.py`, `decision_fusion.py` with tests (PR #99 merged); develop `prototype/modulation_classifier.py` stand-in classifier; `prototype/README.md` and `requirements.txt` still course scaffold on develop; Open PR #102: `waveform_identification/` package, scripts, README, requirements |

**Merge first** (not counted until it's in `develop` or `main`): PR #102 (feature/98-baseline-peak-picking) — baseline peak picker, scripts, README, requirements; open; Branch Application-Structure — 5 commits not in develop; open a PR or drop; Branch docs/team-documentation — 1 commit not in develop; develop to main — typed refs, goals format (#101), prototype code not on main.

**To do before your Sprint 2 review:**

1. Merge PR #102 after replacing the scaffold `prototype/README.md` and `requirements.txt` with real setup and run commands.
2. Write specs in `docs/specs/` for epics #57-#61, each opening with epic and stories; link in section 4.
3. Draw architecture, system context, DFD and GUI wireframe; put them with captions in proposal section 4.
4. Expand section 4 environment into a table with a reason per choice; resolve MATLAB versus Python.
5. Link #95-#98 in section 4; assign Sprint and parent to #95-#97; merge duplicate stories #70/#71.
6. Open a PR for Application-Structure; merge develop into main.

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

### G14 · Cyber Squad: Rogue-Lite Cyber Sandbox

*AI-assisted simulated-desktop malware incident-response trainer; LLM generates scenarios, Pydantic validates them.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Fill proposal §4 environment (PySide6, Pydantic, NRP.ai) from your HW#4 text, then create the PySide6 prototype skeleton that opens a window.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 epics (#22, #23), 18 stories (#24-#41) titled with objective wording, linked in §2. No story has sp:, Sprint milestone, or assignee; refs untyped; no Sprint 2 tasks. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #22 Goal 1: interactive and secure cybersecurity training environment; epic #23 Goal 2: Integrate AI-assisted mechanics. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: parameters to LLM to validated scenario to UI; er: scenario schema (files, processes, logs, network); uml: sequence for scenario generate-validate-load; ui_flow: simulated desktop, config screen, after-action report. |
| 4. Environment | ⚠️ partial | Stated in: HW#4 only (§3 and §4 in repo are still skeleton). Language: Python (HW#4); Framework: PySide6 tentative; Pydantic for validation; Platform: desktop app, simulated OS entirely inside the app; Data: in-memory virtual file system; scenario JSON; store not chosen; Hosting/hardware: local run; LLM hosted by NRP.ai; Sponsor resources: none stated; NRP.ai LLM access; Tools: GitHub board, CODEOWNERS; pytest in CI. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, tests/test_login.py: course example unchanged; prototype/requirements.txt: scaffold copy; prototype/README.md: template text |

**To do before your Sprint 2 review:**

1. Write §3 approach and §4 environment (PySide6, Pydantic, NRP.ai client, storage) with reasons; convert §2/§4 refs to typed form.
2. Write the two epic specs in proposal.md §4 (summary per epic) covering stories #24-#41, with host isolation (#30) and schema validation (#36) as NFR/acceptance items.
3. Draw architecture and system-context diagrams in docs/design/ (Mermaid + images) and list them with captions in §4.
4. Recommended once §4 has the summaries: move full spec/design detail into docs/specs/<epic>.md and docs/design/, linking each from §4.
5. Add DFD for scenario generation, ER/class diagram for the scenario schema (#34), a sequence diagram, and desktop wireframes.
6. Replace login.py with a PySide6 skeleton: requirements.txt, .env.example, README run steps, smoke run opening a window.
7. Add sp:, assignee, Sprint 2 milestone to stories; file Sprint 2 tasks for specs/design/env/prototype and link #4, #6, #13 in §4.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: ECS game engine for constrained hardware with demo game

*Lightweight ECS-based game engine for older hardware, with a top-down 3D bullet-heaven demo game.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Do #46: add `prototype/CMakeLists.txt` with a window build that compiles on a fresh machine, then record language and OpenGL choices in §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #24 Game Engine, #25 Game Demo with eight objective-titled stories (#26-#33), none in Sprint 2. Sprint 2 tasks #46-#50, #9 assigned but untyped or without sp:; §2 and §4 links are bare, none typed. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #24 Game Engine; Epic #25 Game Demo. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: input to ECS systems to renderer per frame; uml: class diagram of entity, component, system; ui_flow: editor screens for objective 2.4; er: only if scenes or assets are stored. |
| 4. Environment | ❌ not started | Stated in: HW#4 only (plus README platforms and issue #46). Language: not stated (CMake in #46 implies C/C++); Framework: custom ECS engine; legacy OpenGL per HW#4; Platform: Windows, Linux, maybe Mac (README); Data: not stated; Hosting/hardware: older or constrained hardware; target spec not stated; Sponsor resources: none (own project); Tools: CMake (#46). |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` are course example; `prototype/README.md` still template text; No CMakeLists.txt or manifest |

**Merge first** (not counted until it's in `develop` or `main`): PR #51 (documentation/47-System-Context-Diagram) — §4 system context diagram draft; open; develop to main — develop has README and §2 work; main proposal is still a skeleton.

**To do before your Sprint 2 review:**

1. Do #46: add `prototype/CMakeLists.txt` and a window-and-triangle build that compiles on a fresh machine; replace `login.py`.
2. Write the environment table in proposal §4 with language, OpenGL version, libraries, compilers, platforms, tools and reasons.
3. Merge PR #51 and finish #48 architecture diagram; add ECS class diagram and DFD with captions in §4.
4. Write `docs/specs/` for both epics (#49) and list them in §4 with issue numbers.
5. Add typed refs for every issue in §2 and §4; label #47-#50 as task; add sp: and Sprint 2 milestone to stories being worked.
6. Merge develop into main so main's proposal has the real §0-§2.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch cross-chain bridge exploit detection

*Learns normal bridge outflow, raises alerts on hacks with few false alarms, and shows them on a dashboard.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Do #62: create `docs/design/architecture.md` with editable Mermaid for Figures 1 and 2, and add the SQLite ER diagram.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Epics #11-#13 and stories titled with objectives; Sprint 2 stories #14,#15 and tasks assigned with sp:, milestone. Proposal links 30 of 33 issues as typed refs. |
| 2. Specs | ⚠️ started | `docs/specs/goal-3-dashboard.md` (main, develop) — Goal 3 draft, epic #13, stories #20,#21; `docs/specs/goal-2-detection.md` (develop only) — Goal 2 draft, epic #12; merge to main Missing: Epic #11 Goal 1 Learn what normal bridge activity looks like (task #61). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: SQLite transfers, alerts and cursor tables; uml: sequence for live loop and alert notify; ui_flow: dashboard screens and alert states; dfd: only if architecture figure lacks flows. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (Table 6) and prototype README. Language: Python 3.12; Framework: FastAPI, uvicorn, httpx; Platform: web dashboard, Docker packaging; OS not stated; Data: SQLite; SonarX stream and public Ethereum nodes, Chainlink feed; Hosting/hardware: Docker; host not chosen; Sponsor resources: SonarX data (SNX-3), still to request from mentor; Tools: pytest, GitHub CI, Slack webhook alerts. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` pinned fastapi, uvicorn, httpx; `requirements-dev.txt` pytest; `prototype/bridgewatch/` modules mirror source, detector, store, live, notify, app; `prototype/README.md` run and test commands; `run_bridgewatch.py`, `Dockerfile.bridgewatch`; `prototype/tests/` 48 offline tests; saved hack datasets and results |

**Merge first** (not counted until it's in `develop` or `main`): PR #73 (72-environment) — environment write-up, `.env.example`, SonarX source stub; open; PR #74 (65-table-9-docs) — Table 9 lists every spec and design document; open; PR #70 (69-ingest-lag-minutes) — ingest lag in minutes, degrade past five minutes (Objective 1.1); open; Branch 15-baseline-check — 1 commit not in develop, no PR; develop to main — goal-2 spec and Sprint 2 work not on main.

**To do before your Sprint 2 review:**

1. Merge PRs #73, #74 and #70 into develop after review; release develop to main.
2. Do #61: write `docs/specs/goal-1-baseline.md` with epic #11, stories #14,#15 in the first lines.
3. Do #62: create `docs/design/architecture.md` with Mermaid for Figures 1 and 2, plus SQLite ER and live-loop sequence diagrams.
4. Add a dashboard wireframe or screen-flow for Objective 3.1 to the design doc and proposal section 4.
5. Link #67, #69, #72 in proposal section 4 and update Table 6 statuses and hosting choice.
6. Open a PR for 15-baseline-check or drop the branch (#15).

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
