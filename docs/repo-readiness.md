# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-11-02 21:51 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ⚠️ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G04](#g04) Epic Engineers | Tue Oct 27 | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) WILS | Tue Oct 27 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ⚠️ |
| [G07](#g07) Mighty Morphin | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G13](#g13) BYKX | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G16](#g16) G16 | Thu Nov 5 | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| [G17](#g17) G17 | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ |
| [G18](#g18) G18 | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) G19 | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 14 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G08, G10, G11, G12, G13, G14, G15, G16, G17, G19).
- **Design and diagrams:** 17 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G07, G08, G09, G11, G12, G13, G14, G15, G16, G17, G18, G19).
- **Environment:** 16 of 20 have written their environment choices into the repository (G01, G02, G03, G04, G05, G07, G08, G10, G11, G12, G13, G14, G15, G16, G18, G19).
- **Prototype wiring:** 14 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G02, G03, G05, G06, G08, G09, G11, G12, G13, G15, G16, G18, G19).
- **Waiting in a branch or open pull request:** G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G12, G13, G14, G17. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting pipeline (SNX)

*Python pipeline that cleans SonarX Hyperliquid data, rebuilds order books, validates them, then backtests strategies.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge PRs #193 and #189, then correct proposal §4 Environment and `prototype/README.md` so both match the DuckDB and React/Vite code already on main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#20-#22), 13 objective stories; Sprint 2 stories #113-#119, #128 closed with sp and milestone. 12 open Sprint 3 issues missing from the board. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — Goal 1 epic #20; FR traced to stories #23-#24; `docs/specs/validation.md` (main) — Goal 2 epic #21; dated market events named; `docs/specs/backtest.md` (main) — Goal 3 epic #22; fill model, costs, open questions |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: data cleaned and stored in stages; er: DuckDB event/snapshot/result tables; uml: market-day sequence for critical flow; ui_flow: report viewer screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4. Language: Python 3.12 (pipeline), TypeScript (front end); Framework: React + Vite front-end skeleton; front-end choice marked open in docs; Platform: team laptops; GitHub Actions CI; Data: DuckDB (in `requirements.txt`, `database.md`); proposal §4 still says standard library only; Hosting/hardware: local only; no hosting stated; Sponsor resources: SonarX requester-pays S3 buckets, Hyperliquid archive; AWS account needed; Tools: pytest, GitHub Actions, Node 20.19+/22.12+, oxlint. |
| 5. Prototype wiring | ⚠️ started | `prototype/src/bgaf_pipeline/` has clean, replay, validate, gate, backtest, report, storage modules; `prototype/pyproject.toml` and `requirements.txt` pin pytest and duckdb; `prototype/frontend/` Vite React skeleton with `package-lock.json`; `prototype/tests/test_package.py` layout test; CI runs pytest; `prototype/login.py` and `test_login.py` still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #193 (open, main) — EER diagram extending `docs/design/database.md` (#175); PR #189 (open, main) — front-end architecture written into proposal (#187); `develop` — 57 files vs 118 on main; sync or retire it; branch `175-eer-diagram` — 127 commits not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #193 and PR #189, then add the EER and front-end diagrams to proposal §4 Diagrams with captions.
2. Rewrite proposal §4 Environment so it matches the repo: DuckDB, React/Vite, and the AWS requester-pays access.
3. Update `prototype/README.md`: remove 〈placeholders〉, say DuckDB is chosen, and document the front-end framework decision (#114).
4. Add a pytest smoke test in `prototype/tests/` that creates the DuckDB schema and loads one sample (#81), plus `.env.example`.
5. Put the 12 open Sprint 3 issues (#172-#187) on the board and add sp: to #89, #112, #191.
6. Delete `prototype/login.py` and `prototype/tests/test_login.py` in their own PR.
7. Sync `develop` with main or retire it so one branch holds the truth.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed signal capture for multi-node analysis (RTX)

*ESP32 nodes capture nearby Wi-Fi/Bluetooth metadata; a backend fingerprints devices and a dashboard maps them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Write `docs/specs/goal-1-collection.md` for epic #47 (stories #16, #45-#49) with scope, FR/NFR, acceptance criteria and open questions, then repeat for #50 and #56.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 0-3 (#20,#47,#50,#56) with objective-titled stories #16, #45-#61 (sp, Sprint 3/4). Sprint 2 tasks #91-#99, #101, #102 not linked in §4; #92, #93 unassigned; meeting issues untyped. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #47 Goal 1 Collect wireless signal metadata; epic #50 Goal 2 Identify selected recording devices; epic #56 Goal 3 Present device observations through a dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: sequence for node to backend to dashboard flow; ui_flow: Angular dashboard screens planned; er: PostgreSQL stores observations. |
| 4. Environment | ⚠️ partial | Stated in: HW#4 only; proposal §3 and §4 Environment still skeleton on main and develop; Lightsail text sits on unmerged branch. Language: Python (backend), TypeScript (Angular), ESP32 firmware (language not stated); Framework: FastAPI; Angular; ESP32 firmware project; Platform: ESP32 capture nodes; Linux; Data: PostgreSQL; Hosting/hardware: AWS Lightsail with SSH-tunnel development (branch only; #102 now removes Lightsail); Sponsor resources: RTX sponsor: real-time demo expectations (sponsor meetings #70, #101); Tools: uv, pytest, GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | `prototype/backend/main.py` FastAPI app with `/health` and `test_main.py` (develop only); `prototype/backend/pyproject.toml`, `uv.lock`, `requirements.txt` (develop); `prototype/README.md` backend setup, run, test steps (develop); main still has scaffold `prototype/login.py` and `tests/test_login.py`; no Angular, ESP32 or PostgreSQL folders; #92-#94 open |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — FastAPI scaffold (#96) and diagrams (#85, #90, #98) not on main; no PR open; PR #103 (open, main to develop) — syncs proposal.md into develop; branch feature/23-approach-environment — 10 commits incl. §4 hosting text, not in develop; branch feature/86-lightsail-hosting — 2 commits not in develop.

**To do before your Sprint 2 review:**

1. Write one spec per epic (#47, #50, #56) in `docs/specs/` naming epic and stories in the first lines; list them in the §4 document table.
2. Resolve the Lightsail question (#101, #102), then merge `feature/23-approach-environment` into develop so §3 and §4 Environment carry each stack choice and reason.
3. Embed architecture, context and DFD figures in §4 Diagrams with captions; add the design docs to the §4 table; add a sequence diagram.
4. Finish #92-#94: ESP32 firmware project, Angular app, PostgreSQL via docker compose, plus `.env.example`; assign #92 and #93.
5. Link #91-#99, #101, #102 in §4 work-items as typed refs and type the meeting issues.
6. Open a develop to main PR so the FastAPI scaffold and diagrams count; delete scaffold `login.py`.
7. Recommended: keep summaries and diagrams in proposal.md; keep full detail in `docs/specs/` and `docs/design/`.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: equation-to-code literate programming pipeline (RTX-3)

*Jupyter notebook that transcribes an equation, generates data, trains a PyTorch model and plots results.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Fill the 〈placeholder〉 in proposal §4 Environment and resources with Jupyter, PyTorch, the named AI APIs and the CSV/DB choice, each with a reason tied to §3.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 4 goal epics (#27, #28, #43, #44) and 13 objective-titled stories; Sprint 2 stories on board with sp. Six Sprint 2 stories (#31, #34-#37, #48) still open; 12 issues have no milestone. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (main) — Goal 1 epic #28; only #33 written, #30/#50 pending; `docs/specs/data-generation.md` (main) — Goal 2 epic #27; covers #36, #35, #48 only Missing: epic #43 Goal 3: Train a model (issue #71 open); epic #44 Goal 4: Output notebook (issue #72 open). |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: dfd: data moves through transcribe, generate, train; er: datasets stored as CSV or relational DB; uml: sequence for transcribe-review-accept flow; ui_flow: notebook step order and user inputs. |
| 4. Environment | ⚠️ partial | Stated in: §3 (§4 Environment is still the 〈placeholder〉). Language: Python (notebook); Framework: PyTorch for the model, run locally; external AI calls for transcription and dataset generation; Platform: Jupyter notebook is the only interface (sponsor requirement); Data: CSV or relational database for generated data sets; Hosting/hardware: user's own machine for training; not stated otherwise; Sponsor resources: external image-recognizer and LLM API accounts not yet named; Tools: GitHub Actions CI, pytest. |
| 5. Prototype wiring | ⚠️ started | `prototype/verifier.py` and `tests/test_verifier.py` exist with test inputs; `prototype/transcriber.py`, `generate_dataset.py`, `store_datatype.py`, `train.py` are flat scripts; `prototype/requirements.txt` is the unchanged course copy; `prototype/README.md` is the course login example with 〈placeholders〉; No `.ipynb` notebook and no `.env.example`; `csv_file.py` only on develop |

**Merge first** (not counted until it's in `develop` or `main`): `develop` — 2 commits ahead of main (#67 CSV files, `csv_file.py`); release to main; branch `feature/46-plot-equation` — 1 commit not in develop; open a PR.

**To do before your Sprint 2 review:**

1. Fill proposal §4 Environment and resources: Python, Jupyter, PyTorch, the named recognizer and LLM APIs, CSV or DB, with reasons from §3.
2. Write `docs/specs/goal-3-training.md` (#71) and `docs/specs/goal-4-notebook.md` (#72) with FR/NFR traced to stories #32, #37, #45-#47.
3. Complete the #30/#50 sections in `docs/specs/transcription.md` and #34/#31 in `data-generation.md`; link all specs in proposal §4.
4. Rewrite `prototype/README.md` and `requirements.txt` for torch and jupyter, add `.env.example` and a smoke notebook run.
5. Fix proposal link format: type epics `[[epic:#27]]`, correct #31's URL, and link untyped issues #71, #72, #69, #70 in §4.
6. Add a DFD Level 0, a notebook step-flow diagram and a data-set schema diagram to `docs/design/`.
7. Release develop to main so `csv_file.py` reaches the default branch.

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

*Web app that generates and grades practice questions from course notes and tracks weak concepts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write the Goal 2 spec for epic #20 (stories #21-#26) in `docs/specs/goal-2-weak-spots.md` and link it from proposal §4, then repeat for Goals 1 and 3.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#13, #20, #27), objective-titled stories; Sprint 2 stories #21-#24, #26 on board with sp. #22, #24-#26 unassigned. develop has 0 typed refs; old items #3-#6 still in §2. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #13 Goal 1: generate, grade, summarize (stories #14-#19); epic #20 Goal 2: track weak spots (stories #21-#26); epic #27 Goal 3: web app, reminders, user study (stories #28-#31). |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for every project; dfd: documents flow to questions to mastery; er: per-student concept and answer records; uml: sequence for answer-grade-update loop; ui_flow: web app has accounts and practice view. |
| 4. Environment | ❌ not started | Stated in: nowhere on main or develop (PR #42 open); HW#4 only mentions a web app and an LLM. Language: Python (prototype); Framework: not stated; web framework undecided; Platform: web app (HW#4); Data: not stated; Hosting/hardware: not stated; Sponsor resources: LLM provider and API key not stated; Tools: pypdf, python-docx, python-pptx, pytest (`prototype/requirements.txt`). |
| 5. Prototype wiring | ⚠️ started | `prototype/document_processor.py` with `tests/test_document_processor.py` (main); `prototype/concept_extractor.py` and `question_generator.py` with tests (develop); `prototype/requirements.txt` lists 4 unpinned packages; `prototype/README.md` is the course login example, 〈placeholders〉; `prototype/login.py` and `tests/test_login.py` still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #39 (open, base main) — `prototype/mastery_tracker.py` + tests for #21; PR #44 (open, develop) — `prototype/question_selector.py` + tests (#43); PR #42 (open, develop) — fills proposal §3 and §4 environment; develop is ahead of main: `question_generator.py`, `concept_extractor.py` not on main; branches `feature/question-generator`, `feature/14-document-upload` — commits not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #42 once §4 Environment names language, web framework, LLM provider, database, hosting and tools, each with a reason from §3.
2. Write the Goal 2 spec (epic #20, stories #21-#26) in `docs/specs/goal-2-weak-spots.md`, then Goals 1 and 3; link all in proposal §4.
3. Draw architecture and system-context diagrams in `docs/design/` (Mermaid) plus a sequence for answer-grade-update and an ER sketch; embed in §4 Diagrams.
4. Create the chosen web skeleton in `prototype/`, pin `requirements.txt`, add `.env.example`, a README with run commands and a smoke test; remove `login.py`.
5. Merge PR #44, then PR #39 into develop, and release develop to main so main has all prototype code.
6. Assign #22, #24, #26; fix typed refs on develop and list #36, #41, #43 in §4 planned activities.

[↑ Back to all groups](#groups)

<a name="g07" id="g07"></a>

### G07 · Mighty Morphin: Edwards materials database from CoCs and test reports (EL)

*Web app that extracts material data from CoC and test-report PDFs into a searchable relational database.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Close #47: pick DBMS, backend, frontend and extraction approach with reasons in proposal §4; the diagrams, specs and the prototype skeleton all depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 epics (#11, #17, #22) plus Goal 0 design epic #42; 16 stories objective-titled. Goal 1-3 stories have no milestone; #58, #59, #42 unassigned; #48, #49 lack sp:. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #11 Goal 1 extraction (PR #71 `docs/specs/data-extraction-spec.md` open); epic #17 Goal 2 storage (#58); epic #22 Goal 3 access and analysis (#59). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ✅ UML · ▫️ page flow. Needed for this project: architecture and context: required for every project; dfd: PDF to extraction to database flow; uml: sequence for upload-extract-verify; ui_flow: internal web app search and display. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 table (main); stack still TBD. Language: Python; Framework: backend and frontend framework TBD; Platform: internal web application (Goal 3); Data: AWS-hosted relational database (story #19); DBMS TBD; Hosting/hardware: AWS (stories, #47); services not named; Sponsor resources: CoC and test-report PDFs from the sponsor (EL); sample documents pending; Tools: Visual Studio Code, Git and GitHub; OCR and document-processing tool TBD. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py` and `tests/test_login.py` are the course example; `prototype/requirements.txt` is the unchanged course copy; `prototype/README.md` still has 〈placeholders〉; no code, manifest or `.env.example` for any chosen stack |

**Merge first** (not counted until it's in `develop` or `main`): PR #73 (open, main) — fixes proposal issue links and activity references (#67); PR #72 (open, main) — system architecture diagram PNG and proposal edit; PR #71 (open, main) — Goal 1 spec `docs/specs/data-extraction-spec.md`; PR #69 (open, main) — data flow diagram; develop — behind main; port typed-link fix and sync.

**To do before your Sprint 2 review:**

1. Close #47: choose DBMS, backend and frontend frameworks, extraction/OCR library and AWS services; fill the TBD cells in §4 with reasons.
2. Merge PRs #73, #72, #71 and #69; make sure each diagram file is linked in §4 and images are not empty.
3. Write the Goal 2 (#58) and Goal 3 (#59) specs with FR/NFR traced to stories #18-#21 and #23-#27; link in §4.
4. Add a system-context diagram, an upload-extract-verify sequence and UI wireframes (#41) in `docs/design/`.
5. Create the `prototype/` skeleton for the chosen stack, with pinned deps, `.env.example`, README run steps and a smoke test; remove `login.py`.
6. Assign #42, #58, #59; add sp: to #48, #49; set Sprint 3 milestones on Goal 1-3 stories.
7. Sync develop with main so both branches match.

[↑ Back to all groups](#groups)

<a name="g08" id="g08"></a>

### G08 · Crime Busters: crime-incident map and pattern analysis

*Web app that maps public crime incidents and analyzes patterns inside a user-selected radius.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/miketruong91/CPSC490-G08-Crime-Busters)

**Start here:** Pick the DBMS, framework, map library and hosting this week and write them into §4; the ER diagram and skeleton cannot start without it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#3,#12,#14) with objective-titled stories; Sprint 2 stories #4,#5,#13,#28 have sp, assignee, milestone. Several Sprint 2 tasks lack sp or assignee; #60,#62,#65,#66 off board or unlinked. |
| 2. Specs | ⚠️ started | `docs/crime-pattern-analysis.md` (develop) — Goal 2 filtering/frequency; linked from §4, outside `docs/specs/`; `docs/crime-data-format.md` (develop) — Goal 1 format; not linked from proposal; `docs/crime-data-sources.md` (develop) — Goal 1 sources; not linked from proposal Missing: Epic #3 Goal 1 spec in `docs/specs/` (format and sources docs unlinked); Epic #12 Goal 3 map spec; Epic #14 Goal 2 spec (analysis doc exists, no requirements/AC). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: ingest, normalize, store, filter, map; er: incident table (#32 schema); uml: sequence for radius query from map click; ui_flow: map, filter controls, radius selection. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (develop). Language: Python 3 stdlib (prototype only); Framework: not chosen; Platform: not chosen; Data: DBMS not chosen; Hosting/hardware: laptops; hosting not chosen; Sponsor resources: public crime dataset not yet selected (#8 documented candidates); Tools: GitHub, unittest. |
| 5. Prototype wiring | ⚠️ started | `prototype/area_filter.py`, `prototype/crime_frequency.py` — real stdlib code from #17, #18; `prototype/test_area_filter.py`, `prototype/test_crime_frequency.py` — unittest checks; `prototype/README.md` and `prototype/requirements.txt` — still course scaffold; `login.py` remains |

**Merge first** (not counted until it's in `develop` or `main`): PR #67 (open, develop) — architecture and system-context diagrams plus §3/§4 draft; branch `feature/60-sprint2-proposal-design` — same work as PR #67.

**To do before your Sprint 2 review:**

1. Choose DBMS, web framework, map library and hosting; record in §3 and §4 with reasons (#60, #65).
2. Merge PR #67 and caption Figure 1 and 2 in §4; link `docs/design/architecture.md` and `docs/design/system-context.md`.
3. Link `docs/crime-data-format.md` and `docs/crime-data-sources.md` in §4, or move all specs to `docs/specs/`; write the Goal 3 map spec.
4. Draw ER from the #32 schema, then a DFD and a sequence diagram for the radius query.
5. Build the prototype skeleton for the chosen stack; replace `login.py`, README and `requirements.txt`.
6. Add sp and assignees to #9,#11,#23,#24,#27,#32,#35; add #60,#62,#65,#66 to the board and link them in §4.

[↑ Back to all groups](#groups)

<a name="g09" id="g09"></a>

### G09 · Sigma Squad: vehicle maintenance logger

*Web app tracking vehicle service history and recommending next services with dashboard alerts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Merge the open PRs in order: PR #65 (stack in §4), #60, #62, #67, then one skeleton PR. Nearly all Sprint 2 documentation sits unmerged.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Two epics (#27,#28), objective-titled stories #29-#38; Sprint 2 stories #29-#31 on board with sp and assignee. Tasks #59 and #63 not linked in proposal; epics cited in §1. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #27 spec (PR #60 `docs/specs/vehicle-data-and-tracking.md` open, unmerged); Epic #28 spec (#50, nothing started). |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: er: vehicles, trims, service history tables; uml: sequence for next-service calculation; dfd: service entry to recommendation to alerts. |
| 4. Environment | ❌ not started | Stated in: nowhere. Language: Python and TypeScript (seen in open PRs only); Framework: Vite web frontend (PR #66); Platform: web; Data: SQLite schema in `prototype/db/schema.sql`; Tools: GitHub. |
| 5. Prototype wiring | ⚠️ started | `prototype/db/schema.sql`, `prototype/db/init_db.py` (develop) — vehicle schema and seed; `prototype/requirements.txt` and `login.py` — still scaffold; PR #64 and #66 (open) — two competing app skeletons, no merged README |

**Merge first** (not counted until it's in `develop` or `main`): PR #60 (open) — epic #27 specification; PR #62 (open) — architecture and system-context diagrams; PR #67 (open) — ER model and next-service sequence diagram; PR #65 (open) — proposal §4; PR #66 (open) — frontend package skeleton; PR #64 (open) — vehicle selection API and page (#29).

**To do before your Sprint 2 review:**

1. Settle the stack in one decision and write it in §3 and §4 (#16, #17); merge PR #65 with it.
2. Merge PRs #60, #62, #67 once reviewed; link specs and captioned diagrams in §4.
3. Resolve PR #64 versus #66: keep one prototype layout with one frontend folder, then merge.
4. Write the epic #28 spec (#50) with FR/NFR traced to stories #34-#38.
5. Replace `prototype/login.py`, README and `requirements.txt`; add `.env.example` and a smoke run (#54).
6. Link #59 and #63 in §4; remove epic cites from §1.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: StableScope wash-trading detection

*Dashboard that detects wash trading in stablecoin transaction networks with explainable risk scores.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Draw the architecture and system-context diagrams in `docs/design/` and caption them in §4. Neither required diagram exists, and §3 already gives the boxes.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#15,#23,#24), objective stories #25-#39,#53-#55. Sprint 2 stories #53-#55 have no assignee; #53-#56 not linked in proposal (PR #57 open). |
| 2. Specs | ⚠️ started | `docs/goal1-network-model.md` (develop) — Goal 1 network model; outside `docs/specs/`, unlinked from §4 Missing: Epic #23 Goal 2 spec (#50); Epic #24 Goal 3 spec (#50); Epic #15 spec not in `docs/specs/` or linked from §4. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: ingest, graph build, detect, score; er: wallets, transfers, labels, scores; uml: sequence for wallet investigation flow; ui_flow: dashboard search, graph, wallet views. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 and §3. Language: Python; Framework: scikit-learn; dashboard Streamlit/Dash or React+FastAPI undecided; Platform: laptops, local run; Data: SonarX SQL, Parquet with DuckDB, optional Neo4j; Hosting/hardware: team laptops plus company machine for heavy jobs; Sponsor resources: SonarX stablecoin transaction data; Tools: GitHub, Discord. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `prototype/tests/test_login.py` — course example still present; `prototype/README.md` cites `network.py` and `docs/specs/goal1-network-model.md`; neither exists; duplicate course files at repo root (`requirements.txt`, `login.py`); PR #58 open to remove |

**Merge first** (not counted until it's in `develop` or `main`): PR #57 (open, develop) — §2 objectives split, new stories linked; PR #58 (open, main) — removes duplicate course files from repo root (#56).

**To do before your Sprint 2 review:**

1. Draw architecture and system-context diagrams in `docs/design/`; caption them in §4 (no diagram exists).
2. Move the Goal 1 spec into `docs/specs/`, link it in §4, and write Goal 2 and Goal 3 specs (#50).
3. Build the Goal 1 prototype named in the README: `prototype/network.py`, tests, sample CSV, pinned requirements.
4. Merge PR #57 and #58 to link #53-#56 and clean the repo root.
5. Assign #53-#55 and add sp to #51, #56; fix #3 type.
6. Add an ER and DFD once the graph schema is set.

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

### G12 · ACJMM: 6G waveform identification with explainable AI

*Tool that detects and classifies 6G radio waveforms with CLI/GUI and explainable confidence.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Write the first spec in `docs/specs/` for epic #60 (most built code), draw the architecture diagram, and link both from §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 5 epics (#57-#61) and objective-style stories; epics lack assignee and milestone. Stories #63,#67,#68,#70,#71 have no milestone or assignee; #96 and #103 not linked. |
| 2. Specs | ⚠️ started | `docs/baseline-peak-picker.md` (develop) — Epic #57 handoff; not a spec, unlinked; `docs/captum-attribution.md`, `docs/confidence-calibration.md` (develop) — Epic #60 handoffs; unlinked; `docs/labeled-signal-dataset.md` (develop) — dataset contract; unlinked Missing: Epic #57 spec in `docs/specs/`; Epic #58 spec; Epic #59 spec; Epic #60 spec; Epic #61 spec. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: IQ capture to peaks to classifier to report; uml: sequence for CLI/GUI calling the core engine; ui_flow: CLI and GUI screens (#62,#63). |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose). Language: MATLAB and Python (proposal); Python in prototype; Framework: NumPy, SciPy, PyTorch, Captum; GUI framework unnamed; Platform: local desktop/CLI; Data: mentor-provided .iq captures and labeled dataset; Hosting/hardware: laptops; no hosting; Sponsor resources: mentor 6G dataset and scripts; Tools: MATLAB 6G Simulink library, GitHub. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` — pinned numpy, scipy, h5py, torch, captum, pytest; `prototype/README.md` — setup plus a sample-data run command from a fresh clone; `prototype/waveform_identification/`, `prototype/xai/`, `prototype/tests/` — layout mirrors components |

**Merge first** (not counted until it's in `develop` or `main`): branch `Application-Structure` — 5 commits not in develop; branch `docs/team-documentation` — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Draw architecture and system-context diagrams; save source and image in `docs/design/` and caption in §4.
2. Write one spec per epic in `docs/specs/`, starting with #60; link them in a §4 documents table.
3. Link `docs/baseline-peak-picker.md`, `docs/captum-attribution.md`, `docs/confidence-calibration.md` in §4 until specs replace them.
4. Assign epics #57-#61; give #63,#67,#68,#70,#71 milestone, assignee, sp.
5. State the environment choices with reasons in §4; settle MATLAB or Python.
6. Review the two unmerged branches and merge or close them.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. assignment manager (Windows)

*Windows desktop app that manages assignments, suggests deadlines and sends native reminders.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Close revert PR #117, then draw the architecture and system-context diagrams. They are the two required design pieces still missing.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#16-#18), objective-titled stories #19-#27 with sp; epics lack assignee; #25-#27 lack milestone. Sprint 2 has 6 open items: #113,#116 lack sp; #116 still open though PR #118 merged. |
| 2. Specs | ✅ done | `docs/specs/specs-G1.md` (develop) — epic #16, FR/NFR, AC, questions; `docs/specs/specs-G2.md` (develop) — epic #17, same structure; `docs/specs/specs-G3.md` (develop) — epic #18, same structure |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: er: assignment record and local store; uml: sequence for UI to IPC to Python; dfd: assignment input to deadline calc to notification. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3/§4. Language: Python backend, JavaScript frontend; Framework: Electron, React and Vite appear in prototype only; Platform: Windows desktop; Data: local JSON or SQLite, undecided; Hosting/hardware: local, offline; Sponsor resources: none; Tools: GitHub. |
| 5. Prototype wiring | ⚠️ started | `prototype/A.M.I.Y.A.core/` — App.py, Database.py, services, tests; `prototype/A.M.I.Y.A.ui/` — Electron, Vite, React files; `prototype/README.md` and `prototype/requirements.txt` — course scaffold text |

**Merge first** (not counted until it's in `develop` or `main`): PR #117 (open) — reverts the merged specs and wireframes integration; close it.

**To do before your Sprint 2 review:**

1. Close revert PR #117 so spec and wireframe links stay in proposal §4.
2. Draw architecture and system-context diagrams (Mermaid in `docs/design/`) and caption them in §4.
3. Rename `Package.json` to `package.json`, `scr/` to `src/`; npm and CI fail on case-sensitive systems.
4. Rewrite `prototype/README.md` with setup, run, and smoke-test commands that work on a fresh Windows machine.
5. Add an ER diagram once storage is chosen (JSON or SQLite); state the choice in §4.
6. Assign epics #16-#18; add milestone to #25-#27; add sp to #113,#116 and close #116.

[↑ Back to all groups](#groups)

<a name="g14" id="g14"></a>

### G14 · Cyber Squad: incident-response training simulator

*PySide6 desktop sandbox where trainees investigate simulated malware, with LLM-generated scenarios validated by Pydantic.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/jvillacorte/CPSC490-G14-Cyber-Squad)

**Start here:** Make the README smoke run real: commit `prototype/start_simulation.py` plus a pinned requirements.txt with PySide6 and pydantic, then close #60.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #22, #23 and 18 objective-titled stories #24-#41 exist; Sprint 2 tasks closed. Stories and epics are cited 43 times in §4 (wrong section); #79-#88 and #13, #6, #4 are not linked from §4. |
| 2. Specs | ✅ done | `docs/specs/training-environment.md` (main, develop) — epic #22; scope, FR, NFR, AC; indexed in §4; `docs/specs/ai-scenarios.md` (main, develop) — epic #23; scope and FR; indexed in §4 |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: all six present; ER for scenario schema and logs; uml: sequence for configure-to-report flow; ui_flow: desktop screens. |
| 4. Environment | ✅ done | Stated in: proposal §4. Language: Python 3.x; Framework: PySide6, Pydantic; Platform: Windows/macOS/Linux local desktop; Data: in-memory state; optional file fixtures; Hosting/hardware: local machine; Dockerfile planned; Sponsor resources: independent; NRP.ai LLM endpoint via env vars; Tools: GitHub, Actions CI, pytest, `.env.example`. |
| 5. Prototype wiring | ❌ example files only | `prototype/README.md` run command `python start_simulation.py`, but that file does not exist; `prototype/Dockerfile` contains only a TODO line; `prototype/requirements.txt` is the unchanged course scaffold; no PySide6 or Pydantic; `login.py` and `test_login.py` removed on develop; no replacement code |

**Merge first** (not counted until it's in `develop` or `main`): PR #89 (open, develop to main) — system context, sequence, DFD/ER updates and prototype docs; branch copilot/create-requirements-list-for-goal-2-47 — 1 commit not in develop; review or delete.

**To do before your Sprint 2 review:**

1. Create `prototype/start_simulation.py` that launches a PySide6 window, so the README smoke run works (#60).
2. Pin `prototype/requirements.txt` with PySide6, pydantic, pytest; add `.env.example` and a pytest smoke test; implement or remove the Dockerfile TODO.
3. Fix `docs/design/system-context.md`: correct the title, expand actors and boundaries, and add Figure 2 image with a caption in §4 (#54 is still open).
4. Move epic and story refs out of §4 and link #79-#88 as typed tasks; add #88 to the board.
5. Merge PR #89 into main after review by a non-author; close #54 and #88.

[↑ Back to all groups](#groups)

<a name="g15" id="g15"></a>

### G15 · HIBBI-01: Constrained-hardware ECS game engine

*Lightweight data-oriented C++ game engine on OpenGL 3.3 with ECS, plus a game demo and scene editor.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Add prototype/src/main.cpp and glad.c so the CMake build produces a window and the README smoke run works.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #24, #25 and 8 objective-titled stories (#26-#33), but all are Sprint 3, unassigned. #6 'Setting up' is not a goal. #43-#50, #54 untyped; §4 task table has 0 typed refs. |
| 2. Specs | ✅ done | `docs/specs/game-engine.md` (develop) — epic #24, stories #30-#33; scope, FR/NFR, criteria; `docs/specs/game-demo.md` (develop) — epic #25, stories #26-#29; scope, FR/NFR, criteria |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: input to ECS systems to render; uml: ECS entity/component/system classes; ui_flow: scene editor (Objective 2.4) screens; er: skip, no database. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (bare list) + §3 rationale; reasons PR #59 still open. Language: C++26; Framework: OpenGL 3.3, SDL3, GLM, Glad, Assimp, stb_image; Platform: Windows 11, Ubuntu 26.04, Arch Linux; Data: asset files via Assimp; no database; Hosting/hardware: local desktop, older GPUs (2010-era); Sponsor resources: independent project; Tools: CMake 4.0.0, GitHub Actions CI. |
| 5. Prototype wiring | ⚠️ started | `prototype/CMakeLists.txt` — C++26, SDL3/assimp/glm, executable `run` from src/main.cpp; `prototype/README.md` — Linux/Windows setup, build, run steps; `prototype/lib/include/` — vendored glm and glad headers; No `prototype/src/main.cpp`, `glad.c` or setup scripts on develop; test section still pytest |

**Merge first** (not counted until it's in `develop` or `main`): PR #59 — reason per environment choice (issue #58), open against develop; develop to main — main still has login.py, skeleton §2/§4 and no specs or diagrams.

**To do before your Sprint 2 review:**

1. Add `prototype/src/main.cpp` and `src/glad.c` so `cmake -B build` builds and an SDL3 window opens; commit the `setup.sh` and `setup.ps1` the README references.
2. Merge PR #59, then replace the §4 spec/design index placeholder rows with links to `docs/specs/game-engine.md`, `game-demo.md`, `architecture.md` and the context doc.
3. Embed the context diagram in §4 Diagrams with a caption; fix the scaffold header and mermaid fence in `docs/design/System Context Diagram.md`.
4. Add a DFD (input to systems to render), an ECS class diagram and an editor screen flow to `docs/design/`, linked from §4.
5. Type #43-#50 and #54, add typed refs for #9 and #46-#58 in §4, and give the story/epic issues a consistent Sprint 2 or 3 milestone with assignees.
6. Replace the pytest section in `prototype/README.md` with a ctest smoke run, then open develop to main.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · G16: BridgeWatch cross-chain bridge exploit detection

*Detector that learns normal bridge outflows, alerts on exploits, and shows operators a dashboard, using SonarX data.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Open the develop to main release PR (#64) now; nothing else on main matches what develop already holds.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #11-#13 and stories #5, #14-#21 objective-titled, assigned, pointed; Sprint 2 tasks on board. #81 (Sprint 2) is not linked in §4 and carries sp: under story #20. |
| 2. Specs | ✅ done | `docs/specs/goal-1-baseline.md` (develop) — epic #11, stories #14, #15; scope, FR/NFR; `docs/specs/goal-2-detection.md` (develop) — epic #12, stories #5, #16-#19; alert rules, criteria; `docs/specs/goal-3-dashboard.md` (main, develop) — epic #13, stories #20, #21; complete |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: ingest to detector to alert path; er: SQLite store holds transfers, alerts, cursor; uml: sequence for live poll to alert; ui_flow: Goal 3 dashboard screens. |
| 4. Environment | ✅ done | Stated in: proposal §4 Table 6 (develop). Language: Python 3.12; Framework: FastAPI, uvicorn, httpx; pytest; Platform: Windows 11 verified; Ubuntu in CI; Data: SQLite single file; JSON replay datasets; Hosting/hardware: Docker image; host not chosen; Sponsor resources: SNX-3: SonarX real-time stream requested from mentor, no reply; public Ethereum RPC and Chainlink fallback; Tools: GitHub Actions CI, pytest, Slack-style webhook alerts. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt`, `requirements-dev.txt` — pinned fastapi, uvicorn, httpx, pytest; `prototype/.env.example` — every BRIDGEWATCH_* variable, no secrets; `prototype/README.md` — fresh-venv install, test, demo run and health-check commands; `prototype/Dockerfile.bridgewatch` and CI job — build and test on Ubuntu; `prototype/bridgewatch/` — modules mirror the architecture (source, detector, store, notify, app) |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release (#64) — develop holds Goal 1/2 specs, architecture.md, .env.example, Table 6 reasons; main lacks them; PR #75 closed unmerged; reopen as a fresh develop to main PR.

**To do before your Sprint 2 review:**

1. Open and merge the develop to main release PR (#64) so specs, architecture.md and .env.example are on main before the Nov 4 boundary.
2. Verify D3-D6 in `docs/design/architecture.md` give an ER diagram of the store and a data-flow diagram; add a live-poll-to-alert sequence diagram.
3. Add dashboard wireframes or a screen-flow diagram for Goal 3 (#20) to `docs/design/` and list them in §4.
4. Add #81 to §4 as a typed ref; close #14 and #15 or note what remains against their criteria.
5. Add a captioned Diagrams list in §4 pointing to each figure file under `docs/design/`.
6. Finish #64, #66, #67 and #28 (SonarX mentor follow-up) before Sprint 2 closes.

[↑ Back to all groups](#groups)

<a name="g17" id="g17"></a>

### G17 · G17: SonicScape galaxy-style music discovery map

*A music app where genres, artists and songs are galaxies, star systems and planets, with swipe feedback.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Decide the tech stack and write it in proposal §4 Environment and resources with reasons; the skeleton, diagrams and tasks all depend on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #21-#23 and stories #25-#30 are objective-titled, but all six stories sit in the Sprint 1 milestone (past due); only task #41 is in Sprint 2. Closed duplicate epics #15, #17-#20, #24 remain. |
| 2. Specs | ⚠️ started | `docs/specs/specs_goal1.md` (main) — epic #21, stories #25, #26; EARS FR, NFR, criteria; owners 〈name〉; `docs/specs/specs_goal2.md` (main) — epic #22; stories cited as 2.1, 2.2 not #27, #28; sprint TBD; `docs/specs/specs_goal3.md` (main) — epic #23 expected; file exists, text not captured |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er: user profile, swipe history, music dataset stored; dfd: dataset and user data to generated map; ui_flow: galaxy, star system, planet screens; uml: sequence for sign-in and profile restore. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Data: stored music dataset plus per-user profile; store not chosen; Sponsor resources: independent; NASA API (free key) for space names; external listening service TBD. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `tests/test_login.py` — unchanged course example; `prototype/requirements.txt` — unchanged scaffold copy; `prototype/README.md` — course template, not team text |

**Merge first** (not counted until it's in `develop` or `main`): PR #40 — §3 proposed approaches from `feature/section-3-approaches`, open against main; branch `feature/section-3-approaches` — 22 commits not in develop; develop is stale: no specs, no design docs, 4 §2 links; work goes to main, so retire or sync develop.

**To do before your Sprint 2 review:**

1. Choose the tech stack and write it in §4 Environment and resources with a reason per choice tied to §3; merge PR #40 so §3 exists.
2. Fix the first lines of `architecture.md`, `system_context.md`, `goal2-design.md`: name epic #21, #22 or #23 and the real story numbers.
3. Add ER and UI-flow diagrams to `docs/design/`; embed every figure in §4 Diagrams with captions and list all docs in §4 'Specification and design documents'.
4. Create Sprint 2 tasks (spec, design, setup) with assignee, sp: and milestone; move stories #25-#30 off the overdue Sprint 1 milestone; link them in §4.
5. Replace `prototype/login.py` with a framework skeleton, manifest, `.env.example` and README smoke run.
6. Work through issue-linked PRs into develop or main instead of direct commits to main.

[↑ Back to all groups](#groups)

<a name="g18" id="g18"></a>

### G18 · G18: ProStrats, Project Rogue 2D roguelite platformer in Unity

*Playable Unity 2D roguelite prototype with flexible builds, weapon combat and branching run structure.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/austin2578/CPSC490-G18-ProStrats)

**Start here:** Write the three epic specs (#53, #54, #56) in `docs/specs/`; they are the only Sprint 2 deliverable with nothing written.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #29-#31 and stories #32-#41 are objective-titled, assigned and pointed; Sprint 2 stories #32-#38 on board. Spec tasks #53, #54, #56 (Nov 2) are not on the board or in §4; #13, #26 untyped. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #29 Goal 1: Flexible character progression (task #53 filed, not written); Epic #30 Goal 2: Action gameplay (task #54 filed, not written); Epic #31 Goal 3: Replayable run structure (task #56 filed, not written). |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: uml: class diagram of Scripts/Combat classes; uml: state or sequence for run, room, reward flow; ui_flow: loadout panel, route map, HUD screens. |
| 4. Environment | ✅ done | Stated in: proposal §4 'Development environment and resources' (develop); main still skeleton. Language: C#; Framework: Unity 6000.3.25f1, Universal 2D, URP, Input System, 2D physics; Platform: Local Windows standalone build; Data: none; no server or DBMS (ScriptableObjects for ability data); Hosting/hardware: Developer PC for Editor; player minimum to be set by build testing; Sponsor resources: independent; placeholder art with CREDITS.txt; Tools: Git/GitHub, C# editor, Sprint Board; CI does not compile Unity. |
| 5. Prototype wiring | ⚠️ started | `prototype/ProjectRogue/` — real Unity 6000.3 project with `ProjectSettings/ProjectVersion.txt`; `prototype/ProjectRogue/Assets/Scripts/Combat/`, `Assets/Movement/` — merged feature code (#44, #45); Scenes `Test_Combat.unity`, `TraversalRoom.unity`, `MovementFoundation.unity` exist; `prototype/README.md`, `requirements.txt` — still unchanged course scaffold |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release PR — main has only the Unity foundation (#16); develop has §2-§4, diagrams, movement (#44), combat (#45); PR #55 — playtest protocol for Objective 3.3 (#48), open against develop.

**To do before your Sprint 2 review:**

1. Write the three specs (#53, #54, #56) in `docs/specs/` with epic and story lines, FR/NFR, acceptance criteria and open questions; link them in §4.
2. Rewrite `prototype/README.md` for Unity with setup, the scene to Play and the expected result; delete `requirements.txt`.
3. Add a combat class diagram and a run/room state diagram to `docs/design/system-overview.md`; add loadout and route-map wireframes; show them in §4.
4. Put #53, #54, #56 on the board and in §4; type or close #13 and #26; remove [epic:] refs from §1.
5. Merge PR #55, then open a develop to main release PR so §3, §4, diagrams and the Unity work are on main.

[↑ Back to all groups](#groups)

<a name="g19" id="g19"></a>

### G19 · G19: Titan Security, Radar over WiFi drone detection (RTX-2)

*Detect and locate drones from Wi-Fi channel state information, compared against conventional radar.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Draw the architecture and system context diagrams in `docs/design/` and embed them in §4; the DFDs exist, these two are the required gap.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #2-#4 and stories #6-#8, #13-#17 are objective-titled, with Sprint 2-4 milestones. Task #49 has no milestone; #37, #38, #43 lack type or sp:; develop §4 refs lack double brackets, so they are not typed refs. |
| 2. Specs | ⚠️ started | `docs/specs/wifi-csi-sensing.md` (develop) — epic #2, stories #8, #13; scope, FR/NFR, criteria; linked in §4 Missing: Epic #3 Drone Detection (task #49 filed, not written); Epic #4 Evaluation. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: only if recordings go in a database; uml: sequence for capture to validated dataset; ui_flow: skip unless a dashboard exists. |
| 4. Environment | ⚠️ partial | Stated in: README/prototype notes (`prototype/csi-setup.md`) and spec; §4 environment text still a placeholder. Framework: CSI capture tool or firmware not confirmed (spec says final receiver and method unconfirmed); Platform: host OS and drivers in `prototype/csi-setup.md`; Data: timestamped CSI recording files, format per spec; validated dataset and quality reports; Hosting/hardware: GL.iNet Wi-Fi transmitter; CSI-compatible receiver still to be confirmed; Sponsor resources: RTX-2 sponsor. |
| 5. Prototype wiring | ⚠️ started | `prototype/csi-setup.md` — equipment setup notes; `prototype/csi-capture.md` — CSI frame capture procedure; `prototype/README.md`, `requirements.txt`, `login.py`, `tests/test_login.py` — unchanged scaffold; No capture script, dependency manifest or smoke run |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — main lacks the spec, design doc and DFD images; PR #44 predates them.

**To do before your Sprint 2 review:**

1. Write §3 Proposed Approaches and the §4 environment list, each choice with a reason tied to §3.
2. Draw the architecture and system context diagrams in `docs/design/`; embed both in §4 with captions.
3. Write the Drone Detection spec (#49, give it Sprint 2) and an Evaluation spec; first lines name epic and stories; add both to the §4 index.
4. Replace `prototype/README.md` and `login.py` with a CSI capture skeleton: manifest, config template, capture script, smoke run.
5. Fix §4 refs on develop to `[[task:#N]](url)` and add #37, #39, #43, #45, #47, #49; type or close #38 and #43.
6. Open a PR merging develop into main once the above is in.

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
