# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.
>
> **Features without code are fine.** If your stories break down into features, enhancements or tasks whose deliverable is a requirements, specification or design document, that is how I want them used: the issue type does not have to be `task`, and the issue does not need code. Link it from §4 and close it with a merged pull request that adds the document. If the Oct 24 edition of this page asked your group to open a code pull request (G13, G16, G17, G20), you can set that aside for Sprint 2.

**CPSC 490 · Fall 2026 · swept 2026-10-31 19:30 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G07](#g07) Mighty Morphin | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G11](#g11) 5Guys | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G12](#g12) ACJMM | Thu Oct 29 | ⚠️ | ❌ | ⚠️ | ⚠️ | ✅ |
| [G13](#g13) BYKX | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| [G16](#g16) G16 | Thu Nov 5 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| [G17](#g17) SonicScape | Thu Nov 5 | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 13 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G05, G08, G10, G11, G13, G14, G15, G16, G17, G19).
- **Design and diagrams:** 14 of 20 have started their design, as diagrams or design write-ups (G01, G02, G03, G04, G05, G08, G11, G12, G13, G14, G15, G16, G18, G19).
- **Environment:** 17 of 20 have written their environment choices into the repository (G01, G02, G03, G04, G05, G06, G07, G08, G10, G11, G12, G13, G14, G15, G16, G18, G19).
- **Prototype wiring:** 13 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G02, G03, G05, G06, G08, G11, G12, G13, G15, G16, G18, G19).
- **Waiting in a branch or open pull request:** G01, G02, G04, G05, G06, G07, G09, G12, G13, G14, G16. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order book reconstruction and backtesting pipeline (SNX)

*Rebuild Hyperliquid order books from SonarX data, validate the rebuild, then backtest strategies on validated market-days.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Merge PR #179, then add the DuckDB smoke run and `.env.example` to `prototype/` so a fresh machine can prove the toolchain end to end.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goal epics #20-#22 with objective-titled stories #23-#28; Sprint 2 stories closed. #171-#187 tasks and #142-#170 features are not linked in proposal on main; #23-#28 and many features lack a milestone; 15 open issues off the board. |
| 2. Specs | ✅ done | `docs/specs/reconstruction.md` (main) — epic #20, stories #23-#24; FR/NFR, acceptance, open questions; `docs/specs/validation.md` (main) — epic #21, stories #25-#26; names dated market events; `docs/specs/backtest.md` (main) — epic #22, stories #27-#28; fill model, costs, metrics |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ✅ ER · ✅ UML · ✅ page flow. Needed for this project: dfd: pipeline stages move data between steps; er: DuckDB stores events and results; uml: market-day sequence exists; add backtest order lifecycle; ui_flow: dashboard screens designed. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 Environment and resources (main). Language: Python 3.12 (pipeline); TypeScript (front end); Framework: bgaf_pipeline package; React + Vite skeleton in `prototype/frontend/`; Platform: team laptops; GitHub Actions CI; Data: DuckDB in `requirements.txt`, not yet stated in §4; Hosting/hardware: local only; one market, one week; Sponsor resources: SonarX L2 snapshots and order-level data via requester-pays S3 (SNX); Hyperliquid archive; Tools: pytest, AWS CLI, npm, oxlint. |
| 5. Prototype wiring | ⚠️ started | `prototype/src/bgaf_pipeline/` one module per pipeline step (clean, replay, validate, gate, backtest, report); `prototype/pyproject.toml`, `requirements.txt` pin pytest and duckdb; `prototype/frontend/` Vite React TypeScript skeleton, lockfile, run steps in README; `prototype/tests/test_package.py` layout tests; `login.py` and `test_login.py` still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #179 (open, into main) — restates §2 as three goals, regenerates §4 work items; PR #186 (open, into main) — `docs/design/cleaning-pipeline.md` skeleton for #176; develop — far behind main (57 vs 114 files); sync or retire it; branches 171-three-goals, 176-cleaning-pipeline-design, 58-cite-dropped-objective-main — unmerged commits.

**To do before your Sprint 2 review:**

1. Merge PR #179 and #186, then relink proposal §2 and §4 so #142-#187 appear as typed refs.
2. Add DuckDB, React/Vite and the AWS cost note to proposal §4 Environment and resources, each with a reason tied to §3.
3. Add a smoke run: load one SonarX sample file into DuckDB via `storage.py`; document it in `prototype/README.md` and add `.env.example`.
4. Delete `prototype/login.py` and `tests/test_login.py`; replace README Status placeholders; let CI build `prototype/frontend/`.
5. Give #23-#28 and #142-#169 a milestone and assignee; add the 15 open issues missing from the board.
6. Export PNGs for diagrams that only have `.mmd` source and caption them in §4 Diagrams.
7. Recommended: keep proposal.md as summaries plus diagrams and detail in `docs/specs/`, as already done.

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

### G03 · California: equation-to-code literate programming pipeline in a Jupyter notebook (RTX-3)

*Turn a handwritten or typeset equation into verified LaTeX, Python, a training dataset and a trained model.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Rewrite `prototype/requirements.txt` and `prototype/README.md` for torch, jupyter and the API client with a verifier smoke run, then merge to develop and main.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Four goal epics (#28,#27,#43,#44), objective-titled stories, Sprint 2 stories assigned with sp. #45 and #47 lack a milestone; §4 tasks table lists only #59; meeting issues untyped and off the board. |
| 2. Specs | ⚠️ started | `docs/specs/transcription.md` (develop, main) — epic #28; #33 in full, #30 and #50 pending; `docs/specs/data-generation.md` (develop, main) — epic #27; #36, #35, #48 full, #34 and #31 pending Missing: epic #43 Goal 3 train a model; epic #44 Goal 4 output steps, code and plots. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ▫️ page flow. Needed for this project: er: only if the data set store becomes relational; ui_flow: notebook cell flow is the whole UI. |
| 4. Environment | ⚠️ partial | Stated in: proposal §3 (reasoned decisions); §4 Environment still a placeholder; `docs/design/architecture.md` key decisions. Language: Python; Framework: Jupyter notebook UI (sponsor requirement); PyTorch for training; Platform: local machine for training; external AI calls for transcription and data generation; Data: CSV or relational store, still open; accepted.json hand-off; Hosting/hardware: local only; Sponsor resources: RTX-3 requires notebook UI; recognizer and code-AI service not yet named; Tools: pytest; GitHub Actions. |
| 5. Prototype wiring | ⚠️ started | `prototype/verifier.py`, `transcriber.py`, `train.py`, `generate_dataset.py` exist (develop); `prototype/tests/test_verifier.py` and `tests/inputs/*.png` present; `prototype/requirements.txt` and `prototype/README.md` still unchanged course scaffold; no notebook skeleton or `.env.example` in `prototype/` |

**Merge first** (not counted until it's in `develop` or `main`): develop is 2 commits ahead of main (#67 CSV files) — release to main again; no open PRs; prior diagrams, specs and #66 release are merged.

**To do before your Sprint 2 review:**

1. Rewrite `prototype/README.md` and `requirements.txt` for the real stack (torch, jupyter, API client) with a verifier smoke run that works on a fresh machine.
2. Fill proposal §4 Environment and resources: recognizer and code-generation AI, API keys, data store, versions, each with a reason tied to §3.
3. Write `docs/specs/` for epics #43 (train model) and #44 (notebook output), naming epic and stories in the first lines; link both from §4.
4. Finish the pending sections of `transcription.md` (#30, #50) and `data-generation.md` (#34, #31) and assign their owners.
5. Add every non-story issue (#51, #60, #65, #69, #70) to the §4 work-items table; add milestone to #45, #47; type the meeting issues.
6. Add `.env.example` and a `notebook.ipynb` skeleton, then draw the notebook cell flow diagram and add it to §4 Diagrams.
7. Recommended: keep summaries and diagrams in proposal.md and full detail in the `docs/` files, as you do now.

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

*Detects whale calls in hydrophone audio and estimates call direction and distance from time difference of arrival.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** Merge PR #54 and PR #55, then write `docs/specs/goal-1-detector.md` for epic #8 (stories #9-#13) using the Goal 2 spec as the model.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 goal epics (#8,#14), 11 objective-titled stories, all assigned with sp and milestone. Sprint 2 due 10-26 passed with #10, #11, #12, #17 open; 17 task issues not linked in §4. |
| 2. Specs | ⚠️ started | `docs/specs/goal-2-locator.md` (develop) — epic #14, stories #15-#18; scope, FR/NFR, acceptance, open questions Missing: Epic #8 Goal 1 Build an AI capable of recognizing whale calls. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: audio to detector to locator to saved calls; er: calls and hydrophones stored in Postgres; uml: sequence of detect, save call, locate. |
| 4. Environment | ⚠️ partial | Stated in: README / HW#4 only (proposal §4 still skeleton). Language: Python (`prototype/requirements.txt`); Framework: numpy, scipy, torch, librosa, soundfile, matplotlib; Platform: local venv; pytest in CI; Data: Postgres via `docker_compose.yaml` and `db/init/*.sql` (main only); Hosting/hardware: local; hydrophone array simulated; Sponsor resources: independent; public whale-call datasets; Tools: GitHub Actions CI, pytest, Docker. |
| 5. Prototype wiring | ✅ done | `prototype/locator/smoke.py` + `README.md` setup: `python -m locator.smoke` (develop); `prototype/requirements.txt` pinned numpy, scipy, torch, librosa; `.env.example` present (develop); `prototype/locator/`, `ai-detector/` mirror Goal 2 and Goal 1 components; README still tells reader to run `login.py` and an unverified `./ai-detector/pipeline` |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 (open, develop to main) — spec, locator, ai-detector, README, .env.example; PR #55 (open, develop) — `docs/design/locator-design.md` plus proposal edits (#49); PR #54 (open, develop) — lists all work items in proposal §4 (#53); branches feature/49-locator-design, feature/53-proposal-work-items — commits not in develop.

**To do before your Sprint 2 review:**

1. Merge PR #54 and #55 into develop, then PR #48 into main so spec, design and wiring count on both branches.
2. Write the Goal 1 spec for epic #8 in `docs/specs/` naming epic and stories #9-#13 in its first lines.
3. Fill proposal §4: Environment table with reasons, document table linking both specs and the design doc, Diagrams with captions.
4. Draw architecture, system context and DFD (Mermaid or draw.io plus PNG); bring the ER diagram onto develop with editable source.
5. Fix `prototype/README.md` run section (remove login.py, verify ai-detector commands) and merge Postgres/Docker files from main into develop.
6. Resolve overdue Sprint 2 stories #10, #11, #12, #17: finish, split, or move to Sprint 3 with a note.
7. Recommended: keep summaries and diagrams in proposal.md and full detail in `docs/specs/` and `docs/design/`, linked from §4.

[↑ Back to all groups](#groups)

<a name="g06" id="g06"></a>

### G06 · GapWise: LLM study assistant with adaptive weak-spot tracking

*Web app that generates and grades practice questions from uploaded course notes and tracks per-concept weak spots.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Joshbolus/CPSC490-G06-GapWise)

**Start here:** Write the spec for epic #20 (Sprint 2 stories #21-#26) in proposal §4 or `docs/specs/`: scope, FR/NFR traced to stories, acceptance criteria, open questions.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 goal epics (#13,#20,#27), 15 objective-titled stories. Sprint 2 stories #22-#26 still have no assignee; stale #3-#6 open and off the board; #25, #36 unlinked from §4. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #13 Goal 1 Generate, grade, summarize; Epic #20 Goal 2 Track weak spots; Epic #27 Goal 3 Usable web app and reminders. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: upload, extract, question, grade, tracker flow; er: subjects, materials, concepts, mastery, answers stored; uml: sequence of practice session, grading, mastery update; ui_flow: accounts, workspaces, practice view, reminders. |
| 4. Environment | ⚠️ partial | Stated in: nowhere in proposal (§3/§4 skeletons); only implied by prototype/requirements.txt and HW#4. Language: Python (prototype/*.py); Framework: not chosen (web framework, LLM API); Platform: web app (HW#4 only); Data: not chosen (accounts, mastery store); Hosting/hardware: not chosen; Sponsor resources: none (own project); Tools: pytest, pypdf, python-docx, python-pptx; GitHub CI. |
| 5. Prototype wiring | ⚠️ started | `prototype/document_processor.py` + test: PDF/DOCX/text extraction (main, develop); `prototype/concept_extractor.py`, `question_generator.py` + tests (develop); `prototype/requirements.txt` lists pypdf, python-docx, python-pptx, pytest; `prototype/README.md` is still the course login scaffold; `login.py` remains |

**Merge first** (not counted until it's in `develop` or `main`): PR #39 (open, base main) — `prototype/mastery_tracker.py` + tests for #21; develop ahead of main: #37 question builder and #38 concept extraction not on main; branches feature/question-generator, feature/14-document-upload, feature/21-mastery-tracking have commits not in develop.

**To do before your Sprint 2 review:**

1. Write the three goal specs (#13, #20, #27): scope, FR/NFR traced to stories, acceptance criteria, open questions, in proposal §4 or `docs/specs/` files linked from §4.
2. Draw architecture, system context, DFD, ER and practice-session sequence as Mermaid in proposal §4 (or `docs/design/` plus PNG); caption each in §4 Diagrams.
3. Fill proposal §3 and §4 Environment: web framework, LLM API, database, hosting, each with a reason; commit to one stack.
4. Replace `prototype/README.md` and the login scaffold with setup, run, test steps, a smoke run and `.env.example`.
5. Assign owners to #22-#26; close stale #3-#6; add #25 and #36 to the §4 tasks table; keep typed refs on develop.
6. Merge PR #39 and close #36 now that #37 is merged; retarget feature branches into develop so the work counts.
7. Recommended: once specs exist in proposal.md, move the full detail to `docs/specs/` and `docs/design/` and keep summaries and diagrams in proposal.md.

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

### G09 · Sigma Squad: Vehicle Maintenance Logger

*Web app that logs vehicle service history and recommends next maintenance with urgency labels and alerts.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/TylerWard741/CPSC490-G09-SigmaSquad)

**Start here:** Write proposal §4 Environment and resources (#17): pick language, framework and database with reasons. The schema PR, skeleton and diagrams all depend on that choice.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #27, #28 and 10 objective-titled stories #29-#38 with sp. Sprint 2 tasks #49-#56 are on the board with assignee, sp and milestone, but none is linked from proposal §4; §1 cites both epics. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #27 Goal 1: Centralized Vehicle Data & Maintenance Tracking (task #49); epic #28 Goal 2: Scheduled Maintenance Recommendations & Alerts (task #50). |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required; er: vehicles and service history are stored; uml: sequence for next-service calculation; ui_flow: dashboard and service-entry screens. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Platform: web app and/or mobile (HW#4 wording); Data: vehicle database; engine not named; Sponsor resources: independent, none; Tools: GitHub. |
| 5. Prototype wiring | ❌ example files only | `prototype/` holds only course login.py, test_login.py, scaffold README and requirements.txt; open PR #48 adds `prototype/db/schema.sql` and `init_db.py`, not merged |

**Merge first** (not counted until it's in `develop` or `main`): PR #48 (open, develop) — vehicle DB schema and seed script for story #29; branch feature/49-epic-1-specification — epic #27 spec commits not in develop; branch feature/29-vehicle-selection — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Fill proposal §3 and §4 (#16, #17) with the chosen stack, reasons and an Environment and resources table.
2. Merge the epic #27 spec from `feature/49-epic-1-specification` via PR; write the epic #28 spec (#50) in `docs/specs/`.
3. Draw architecture and system context (#51), ER and next-service sequence (#52), screen flow (#53) in `docs/design/` and caption them in §4.
4. Review and merge PR #48 after the stack is stated in §4 so the schema matches the chosen database.
5. Replace `prototype/login.py` and `test_login.py` with the real skeleton and smoke run (#54); link #46 and #49-#56 in §4; drop epic refs from §1.

[↑ Back to all groups](#groups)

<a name="g10" id="g10"></a>

### G10 · Team Jiddak: stablecoin wash-trading detector (SNX-2)

*Graph analytics and risk scoring to detect wash trading in stablecoin transfers, with an investigator dashboard.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/Alexander-Sanchez2/CPSC490-G10-Team_Jiddak)

**Start here:** Draw the architecture and system context diagrams in `docs/design/` and caption them in proposal §4. Neither required diagram exists yet.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #15, #23, #24 and 11 objective-titled stories with sp, all in §2. Task #46 (spec) is Sprint 2 but not linked in §4; #45 and #5 also unlinked. |
| 2. Specs | ⚠️ started | `docs/specs/goal1-network-model.md` (develop) — epic #15; scope, FR, NFR, AC, open questions; traced to #31-#33, #38 Missing: epic #23 Goal 2 Detect wash trading; epic #24 Goal 3 Investigation dashboard. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required; dfd: SonarX to graph to detection to score; er: wallets, transfers, labels, scores stored; uml: sequence for wallet search to evidence; ui_flow: search, graph explorer, wallet summary. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 / §3. Language: Python (pipeline, detection, ML); Framework: scikit-learn; dashboard stack undecided; Platform: team laptops; company machine for heavy compute; Data: SonarX SQL extract, Parquet + DuckDB; Neo4j optional; Hosting/hardware: local machines; no hosting named; Sponsor resources: SNX-2: SonarX stablecoin data and warehouse; Tools: GitHub, Discord. |
| 5. Prototype wiring | ❌ example files only | `prototype/` holds course login.py, test_login.py, scaffold README; `requirements.txt` at root is empty and `prototype/requirements.txt` is scaffold (#45) |

**To do before your Sprint 2 review:**

1. Link `docs/specs/goal1-network-model.md` from proposal §4 with a short summary, and link #5, #45, #46 as typed refs.
2. Write specs for epic #23 (detection) and epic #24 (dashboard) in `docs/specs/`, each traced to its stories.
3. Draw architecture and system context, then DFD, ER and sequence diagrams; commit source and image and add captions in §4.
4. Decide the dashboard stack and graph store; add a §4 table giving a reason for each choice.
5. Fix #45: pin real dependencies in `prototype/requirements.txt`, replace `login.py`, add README run commands and a smoke run on sample data.

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

### G12 · ACJMM: wireless waveform identification with explainable AI

*MATLAB/Python tool that detects signal peaks, classifies modulation and explains decisions with attribution heatmaps.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Write the first spec in `docs/specs/` for the epic with most built code (#60 Explainable AI), then repeat per epic and link all from §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #57-#61 and objective stories exist; Sprint 2/3 stories on board with sp and assignee. Epics have no assignee or milestone; #96, #95, #103 are unlinked or untyped; #111, #96, #62 are off the board. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #57 Signal Detection & Preprocessing; epic #58 Application interface and cross functional integration; epic #59 Waveform Identification & Receiver Processing; epic #60 Modulation, Decision & Explainable AI; epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required; dfd: IQ capture to peaks to classifier to attribution; uml: sequence for analyze-signal run; ui_flow: CLI then GUI screens (story #84). |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose) and README. Language: Python (prototype); MATLAB for EDA; Framework: NumPy/SciPy, PyTorch, Captum; GUI framework not named; Platform: local desktop; MATLAB 6G Simulink library; Data: mentor-provided .iq captures (float64 I/Q), HDF5 bursts; Hosting/hardware: team machines; no hosting; Sponsor resources: mentor IQ files and MATLAB 5G NR holdout; Tools: pytest, GitHub Actions CI. |
| 5. Prototype wiring | ✅ done | `prototype/requirements.txt` pins numpy, scipy, torch, captum, pytest; `prototype/README.md` has setup and run commands with bundled sample `.iq` smoke file; `prototype/waveform_identification/` and `xai/` mirror pipeline components; 44 pytest tests run in CI; PR #109 replaced the login scaffold on develop |

**Merge first** (not counted until it's in `develop` or `main`): develop to main release PR — wiring, XAI and proposal work exist only on develop; branch Application-Structure — 5 commits not in develop; branch docs/team-documentation — 1 commit not in develop.

**To do before your Sprint 2 review:**

1. Write a spec per epic #57-#61 in `docs/specs/`, with FR/NFR traced to stories, acceptance criteria and open questions; link them in §4.
2. Draw architecture and system context diagrams; add a pipeline DFD and a CLI/GUI flow (#84); store in `docs/design/` and caption in §4.
3. Link `docs/images/confidence-calibration-flow.png` and the handoff docs from proposal §4 as design references.
4. Convert §4 environment prose into a table with a reason per choice tied to §3.1; name the GUI framework.
5. Open the develop to main release PR; review `Application-Structure`; add #111, #96, #62 to the board and link #96, #103 in §4.

[↑ Back to all groups](#groups)

<a name="g13" id="g13"></a>

### G13 · BYKX: A.M.I.Y.A. desktop assignment manager

*Windows desktop app that manages assignments, suggests deadlines by difficulty and sends native reminders.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/ktnwin/CPSC490-G13-BYKX)

**Start here:** Close revert PR #117, then draw the architecture and system context diagrams. They are the only required design pieces missing.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #16-#18 and objective stories #22-#27 exist; features and tasks extend to #106. Epics have no assignee; #113, #116, #111, #107 are not linked from §4; #107 is untyped. |
| 2. Specs | ✅ done | `docs/specs/specs-G1.md` (develop) — epic #16 CRUD and storage; full template sections; `docs/specs/specs-G2.md` (develop) — epic #17 scheduling and progress; full template; `docs/specs/specs-G3.md` (develop) — epic #18 notifications; full template |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ✅ page flow. Needed for this project: architecture and context: required, none drawn; er: assignments stored locally; uml: sequence for deadline suggestion and reminder; dfd: UI to Python core to storage. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose). Language: Python core, JavaScript UI; Framework: Electron + React/Vite appear in open PR #118; not stated in §4; Platform: Windows desktop, offline; Data: local JSON or SQLite, undecided; Hosting/hardware: local only; Sponsor resources: none; Tools: not stated. |
| 5. Prototype wiring | ⚠️ started | open PR #118 adds `prototype/A.M.I.Y.A.core` Python app and `A.M.I.Y.A.ui` Electron/React; develop `prototype/` is still course login.py and scaffold README; PR #118 lists Requirements.txt and Package.json but no README or smoke run; folder `scr/` looks like a typo |

**Merge first** (not counted until it's in `develop` or `main`): PR #118 (open) — prototype folder structure, Python core and Electron UI; PR #117 (open) — reverts spec and wireframe links in proposal; close without merging; develop to main release — specs, wireframes and proposal links not on main.

**To do before your Sprint 2 review:**

1. Close PR #117 unmerged so proposal §4 keeps its spec and wireframe links.
2. Draw architecture and system context (Electron UI, Python core, storage, OS notifications) and an ER diagram as Mermaid in `docs/design/`; caption in §4.
3. Fix and merge PR #118: pin `requirements.txt` and `package.json`, README run commands, smoke run, delete `login.py`.
4. Add an environment table to §4 with a reason for each choice, including JSON vs SQLite and the shell.
5. Link #107, #111, #113, #116 in §4; then merge develop to main.

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

### G17 · SonicScape: galaxy-style music discovery map

*A music app where genres, artists and songs are galaxies, star systems and planets, with swipe feedback.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/vibhorbh/CPSC490-G17-SonicScape)

**Start here:** Decide the tech stack and write it in proposal §4 'Environment and resources' with reasons; every other Sprint 2 item depends on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #21-#23 and stories #25-#30 are objective-titled, but all stories are open in Sprint 1 (overdue); nothing in Sprint 2. Six closed duplicate epics (#15, #17-#20, #24) clutter the list. |
| 2. Specs | ⚠️ started | `docs/specs/specs_goal1.md` (main) — epic #21, stories #25-#26; EARS FR, NFR, criteria, open questions; `docs/specs/specs_goal2.md` (main) — expected epic #22; present, content not verified; `docs/specs/specs_goal3.md` (main) — expected epic #23; present, content not verified |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: stored user profile, swipe history, music dataset; uml: sequence for swipe feedback updating the map; ui_flow: galaxy to system to planet navigation screens; dfd: dataset and user data to generated map. |
| 4. Environment | ❌ not started | Stated in: HW#4 only. Data: stored music dataset plus per-user profile (store not chosen); Sponsor resources: NASA API (free key) for space names; external listening service TBD. |
| 5. Prototype wiring | ❌ example files only | `prototype/login.py`, `tests/test_login.py` — unchanged course example; `prototype/requirements.txt` — unchanged scaffold copy; `prototype/README.md` — course template, not team text |

**Merge first** (not counted until it's in `develop` or `main`): PR #40 — §3 proposed approaches from `feature/section-3-approaches`, open against main; develop is stale (4 §2 links vs 9 typed refs on main); work lands on main, so sync or retire develop.

**To do before your Sprint 2 review:**

1. Choose and write the tech stack in §4 'Environment and resources' with a reason per choice tied to §3; merge PR #40 so §3 exists.
2. Create `docs/design/architecture.md` with Mermaid architecture and context diagrams; embed both in §4 Diagrams with captions.
3. Add an ER diagram (users, swipes, genres/artists/songs) and a UI flow of map screens under `docs/design/`.
4. Verify `specs_goal2.md` and `specs_goal3.md` name epics #22 and #23 and stories; list all three specs in §4 'Specification and design documents'.
5. Create Sprint 2 tasks (spec, design, setup) with assignee, sp: and Sprint 2 milestone; move stories off the overdue Sprint 1 milestone; link them in §4.
6. Replace `prototype/login.py` with a framework skeleton, manifest, `.env.example` and README smoke run.

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

### G19 · Titan Security: Radar over WiFi drone detection (RTX-2)

*Detect and locate drones from Wi-Fi channel state information, compared against conventional radar.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/sopper75/CPSC490-G19-TitanSecurity)

**Start here:** Write the architecture and system context diagrams in docs/design/ and embed them in proposal §4; the DFDs are done, these two are the required gap.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Epics #2-#4 and stories #6-#8, #13-#17 are objective-titled with Sprint 2-4 milestones and assignees. Sprint 2 tasks #45, #47 open despite merged PRs; #37-#39, #43 not in §4; #43, #38 untyped. |
| 2. Specs | ⚠️ started | `docs/specs/wifi-csi-sensing.md` (develop) — epic #2, stories #8, #13; thorough FR/NFR, criteria Missing: Epic #3 Drone Detection; Epic #4 Evaluation. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: only if recordings go in a database; uml: sequence for capture to validated dataset; ui_flow: skip unless a dashboard exists. |
| 4. Environment | ⚠️ partial | Stated in: prototype notes (`prototype/csi-setup.md`) and spec; §4 environment text still a placeholder. Framework: CSI capture tool/firmware not yet confirmed; Platform: host OS and drivers documented in `prototype/csi-setup.md`; Data: timestamped CSI recordings in files (format per spec); Hosting/hardware: ALFA AWUS036AXM receiver adapter, GL.iNet GL-MT3000 transmitter; Sponsor resources: RTX-2 sponsor. |
| 5. Prototype wiring | ⚠️ started | `prototype/csi-setup.md` — equipment roles, compatibility findings, configuration; `prototype/csi-capture.md` — CSI frame capture procedure; `prototype/README.md`, `requirements.txt`, `login.py` — still unchanged scaffold; No capture script, dependency manifest or smoke run |

**Merge first** (not counted until it's in `develop` or `main`): develop to main — main lacks the spec, design docs and DFD images (PR #44 predates them).

**To do before your Sprint 2 review:**

1. Write §3 Proposed Approaches and the §4 'Environment and resources' list, each choice with a reason tied to §3.
2. Add a high-level architecture diagram and system context diagram to `docs/design/` and embed both in §4 with captions.
3. Write specs for epics #3 and #4 in `docs/specs/` naming epic and stories in the first lines; add to the §4 index.
4. Replace `prototype/README.md` and `login.py` with a CSI capture skeleton: manifest, config template, capture script, README smoke run.
5. Close #45 and #47; add typed refs for #37, #39, #43, #45, #47 to §4 on develop; add Sprint 2 tasks for the new work.
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
