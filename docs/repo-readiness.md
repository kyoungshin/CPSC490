# Group repository status: Sprint 2 (specification, design, environment)

> [!IMPORTANT]
> **New (Oct 26): this page now checks Sprint 2.** Sprint 2 is about *documents and environment, not features*: a specification per epic, a high-level design with diagrams, your environment and resource choices written down, and those choices wired into `prototype/` as a project skeleton that installs and starts. **You do not need to start coding features yet.** Find your group's card below: it lists what's done and what to do, in order, before your Sprint 2 review.

**CPSC 490 · Fall 2026 · swept 2026-10-26 15:04 UTC.** Earlier editions (proposal vs. issue board) are kept in git history.

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
| [G01](#g01) BGAF | Tue Oct 27 | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ |
| [G02](#g02) Linux Larpers | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G03](#g03) California | Tue Oct 27 | ⚠️ | ⚠️ | ❌ | ❌ | ⚠️ |
| [G04](#g04) Epic Engineers | Tue Oct 27 | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ |
| [G05](#g05) Fighting Mongooses | Tue Oct 27 | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ |
| [G06](#g06) GapWise | Tue Nov 3 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G07](#g07) MightyMorphin | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G08](#g08) Crime Busters | Tue Nov 3 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| [G09](#g09) Sigma Squad | Tue Nov 3 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G10](#g10) Team Jiddak | Tue Nov 3 | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| [G11](#g11) 5 Guys | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G12](#g12) ACJMM (RTX-1) | Thu Oct 29 | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ |
| [G13](#g13) BYKX | Thu Oct 29 | ✅ | ⚠️ | ❌ | ⚠️ | ❌ |
| [G14](#g14) Cyber Squad | Thu Oct 29 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G15](#g15) HIBBI-01 | Thu Oct 29 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G16](#g16) Neuroprosthetic | Thu Nov 5 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| [G17](#g17) SonicScape (EchoSphere) | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| [G18](#g18) ProStrats | Thu Nov 5 | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| [G19](#g19) Titan Security | Thu Nov 5 | ⚠️ | ❌ | ❌ | ⚠️ | ❌ |
| [G20](#g20) Solos | Thu Nov 5 | ⚠️ | ❌ | ❌ | ❌ | ❌ |

- **Specs:** 6 of 20 groups have written specifications, in proposal.md or a separate doc (G01, G03, G04, G08, G13, G16).
- **Design and diagrams:** 9 of 20 have started their design, as diagrams or design write-ups (G01, G02, G04, G05, G07, G08, G10, G16, G18).
- **Environment:** 13 of 20 have written their environment choices into the repository (G01, G02, G04, G06, G07, G08, G10, G12, G13, G14, G16, G18, G19).
- **Prototype wiring:** 8 of 20 have their own skeleton in `prototype/` or a merged project folder (G01, G03, G05, G06, G08, G12, G16, G18).
- **Waiting in a branch or open pull request:** G01, G03, G04, G05, G06, G12, G13, G16, G19, G20. Merge it, or it doesn't count.

<a name="groups" id="groups"></a>

## Your group

Each card shows the five Sprint 2 items, what I found in your repository (both `main` and `develop`), and a numbered to-do list in the order to do it.

<a name="g01" id="g01"></a>

### G01 · BGAF: Hyperliquid order-book reconstruction and backtesting (SNX-4)

*Pipeline that cleans SonarX Hyperliquid data, rebuilds and validates order books, and backtests strategies, with a React front end.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/LeDuy23/CPSC490-G01-BGAF)

**Start here:** Write the three epic specs (requirements and acceptance criteria for Goals #20, #21, #22); #64 and #65 are closed but no spec text exists anywhere.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals #20-#22 with stories #23-#28 plus Sprint 2 epics #71-#74 and stories #113-#119 filed; 68 of 70 issues linked in proposal on main. Stories #24, #26, #27 lack assignee; many tasks lack sp:. |
| 2. Specs | ⚠️ started | proposal/proposal.md §3 (main) — five design decisions, validation and replay approach; reasoning, not requirements; docs/design/backtesting-research.md (main, linked §4) — feeds backtest spec; research not requirements Missing: Epic #20 Goal 1: requirements and acceptance criteria; Epic #21 Goal 2: requirements and acceptance criteria; Epic #22 Goal 3: requirements and acceptance criteria. |
| 3. Design & diagrams | ✅ done | ✅ architecture · ✅ context · ✅ data flow · ▫️ ER · ✅ UML · ✅ page flow. Needed for this project: er: events and snapshots need stored schema (#79 open); uml: sequence of replay then validate then backtest. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 Environment and resources (main; develop copy is shorter). Language: Python 3.12+ (pipeline); TypeScript (front end); Framework: React + Vite front end; data libraries undecided; Platform: team laptops; GitHub Actions CI; Data: SonarX S3 (L2 snapshots, order-level); storage format undecided (#80/#81); Hosting/hardware: none stated; ~100 GB/day node logs scoped to one market, one week; Sponsor resources: SNX-4: SonarX requester-pays S3 buckets, AWS account and CLI; Tools: Mermaid, pytest, oxlint, GitHub Projects. |
| 5. Prototype wiring | ⚠️ started | prototype/src/bgaf_pipeline/ six step modules (clean, replay, validate, gate, backtest, report): docstring stubs; prototype/pyproject.toml, requirements.txt (pytest only), tests/test_package.py; prototype/frontend/ Vite React TS skeleton with package.json; prototype/login.py and tests/test_login.py still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #133 — front-end tool comparisons and decision (frontend-architecture.md); open, base main; Branch 87-document-why-our-front-end-architecture-differs... — same content as #133; develop is 34 commits behind main: sync or retire; open stale branches 58-cite-dropped-objective-main, sync-main-into-develop.

**To do before your Sprint 2 review:**

1. Write the three epic specs (Goals #20, #21, #22): scope, FR/NFR traced to #23-#28, acceptance criteria, open questions. Put detail in docs/specs/ (recommended) with a summary and link in §4.
2. Complete the ER diagram and data model in docs/design/database.md (#79); embed it in proposal §4 Diagrams with a caption and record the #80 storage decision.
3. Add a sequence diagram of one market-day run (download, clean, replay, validate, gate, backtest) to §4 Diagrams.
4. Implement #81/#82: add .env.example, S3 access notes, and a smoke run that parses one SonarX sample file.
5. Remove prototype/login.py and tests/test_login.py; update prototype/README.md Status table and front-end run commands.
6. Merge PR #133, assign stories #24, #26, #27, add sp: to open tasks, and link #58 and #112 in proposal §4.

[↑ Back to all groups](#groups)

<a name="g02" id="g02"></a>

### G02 · Linux Larpers: Distributed Signal Capture for Multi-Node Analysis

*ESP32 nodes capture Wi-Fi/Bluetooth metadata; a backend fingerprints nearby recording devices and a dashboard shows them.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eliThomass/CPSC490-G02-Linux-Larpers)

**Start here:** Merge PRs #87, #88, #89 into develop, then rewrite proposal §4 with the environment choices from #79 and the architecture and ER figures.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Goals 1-3 filed as epics (#47, #50, #56) with 15 objective stories, titles prefixed 'Objective N.M (Role):'. Sprint 2 stories #16, #45, #46, #48, #49 have sp but no assignee. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #47 Goal 1: Collect wireless signal metadata; Epic #50 Goal 2: Identify selected recording devices; Epic #56 Goal 3: Present observations through a dashboard. |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: signals flow node to backend to dashboard; er: Postgres stores observations and devices; uml: sequence for capture-to-detection flow; ui_flow: Angular dashboard screens. |
| 4. Environment | ⚠️ partial | Stated in: HW#4 only (decisions in meeting issue #79; Lightsail in open PR #87); proposal §4 is a skeleton. Language: C/C++ firmware (ESP32); Python for backend; Framework: FastAPI; Angular (undecided); Platform: ESP32 capture nodes; Data: PostgreSQL; Hosting/hardware: AWS Lightsail + SSH tunnels (proposed, pending sponsor approval, PR #87); 2 ESP32 + 1 kit on order list; Sponsor resources: RTX-4 (Flock camera data dropped per #70); Tools: draw.io, GitHub Projects. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py and tests/test_login.py: unchanged course example; prototype/requirements.txt: scaffold copy, no FastAPI/Postgres deps; No firmware, API, or DB files anywhere in repo |

**Merge first** (not counted until it's in `develop` or `main`): PR #89 — ER diagram drawio + png and proposal edit; targets main, should go to develop; PR #87 — Lightsail/SSH-tunnel §4 text; base is a feature branch; PR #88 — §5/§6 outcomes and timeline into develop; PR #83 — ESP32 wording in §0/§1; targets main; PR #78 — remove README.old.md (develop).

**To do before your Sprint 2 review:**

1. Incorporate docs/design/diagrams/architecture.drawio.png (develop) into proposal §4: add a Diagrams subsection with caption, summary and link; merged PR #85 never touched proposal.md.
2. Rewrite proposal §4: environment choices with reasons, diagram figures with captions, and spec/design index; link #77, #82, #84, #86 as typed refs.
3. Write docs/specs one spec per epic #47, #50, #56 with first line naming epic and stories.
4. Add docs/design/architecture.md and system context diagram (#80); merge via develop.
5. Redo DFD L0/L1 (#77 was closed with no file on any branch) and retarget PR #89 to develop.
6. Create PlatformIO ESP32 project and FastAPI skeleton in prototype/; delete login.py and test_login.py.
7. Add .env.example and a smoke run: ESP32 Wi-Fi scan printed over serial, FastAPI /health, Postgres connect.

[↑ Back to all groups](#groups)

<a name="g03" id="g03"></a>

### G03 · California: Three AIs and Literate Programming

*Pipeline turning a handwritten equation into verified LaTeX, generated training data, a trained model and a documented report.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/eccortes4/CPSC490-G03-California)

**Start here:** Write proposal §4 Environment and resources: pick the recognizer and ML library, state Python/Jupyter versions, and give a reason for each.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Four epics (#28, #27, #43, #44) and 15 objective-titled stories filed and linked in §2. Only #30 and #33 carry the Sprint 2 milestone; most stories lack milestone; #31/#32 duplicate objective 2.4. |
| 2. Specs | ⚠️ started | docs/specs/transcription.md (develop; linked in §4 table) — Epic #28; only #33 filled, solid FR/NFR Missing: Epic #27 Goal 2: Generate a training data set; Epic #43 Goal 3: Train a model; Epic #44 Goal 4: Output steps, code and plots in the proposal. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: architecture and context: required for every project; dfd: equation to LaTeX to code to dataset to model; uml: sequence of transcribe, verify, accept hand-off; er: only if datasets get a stored schema; ui_flow: notebook review step, only if widgets added. |
| 4. Environment | ❌ not started | Stated in: nowhere (§4 is a skeleton; spec mentions Jupyter and a vision-LLM recognizer, undecided). Language: Python (inferred from prototype/*.py); Framework: Jupyter notebook; recognizer undecided (vision LLM suggested in spec); Data: CSV/other datasets (Goal 2 stories); Sponsor resources: RTX-3: sponsor tools/accounts not stated; Tools: pytest, GitHub Actions CI. |
| 5. Prototype wiring | ⚠️ started | prototype/transcriber.py and verifier.py on develop: real Goal 1 modules; prototype/tests/test_verifier.py: tests for verifier FRs; prototype/requirements.txt and README.md still unchanged course scaffold; prototype/train.py only in open PR #58 |

**Merge first** (not counted until it's in `develop` or `main`): PR #58 — prototype/train.py for loss-curve plotting, into develop; Branch loss-curve-train — same commit as PR #58; main is behind develop: promote Sprint 2 work after merging.

**To do before your Sprint 2 review:**

1. Write §4 Environment and resources and §3 approach in proposal.md; every choice gets a reason; fill the Planned activities table.
2. Finish docs/specs/transcription.md for #30 and #50, then write specs for epics #27, #43 and #44.
3. Add diagrams directly to proposal §4 (Mermaid or PNG with captions): architecture, system context, DFD; detail may go in docs/design/ (recommended).
4. Create docs/design/ architecture and system context diagrams (Mermaid or draw.io plus PNG); add DFD and a sequence diagram; delete example-design.md.
5. Rewrite prototype/README.md and requirements.txt for the real stack; add .env.example and a smoke run that loads the sample images.
6. Merge PR #58 after adding it to a tracked task; remove prototype/login.py leftovers and login mentions in README.
7. Move Sprint 2 stories onto the Sprint 2 milestone with sp: and assignee; close duplicate #32; link new issues in §4.

[↑ Back to all groups](#groups)

<a name="g04" id="g04"></a>

### G04 · Epic Engineers: Polymarket PNL and top-trader dashboard (SNX-1)

*Compute per-wallet Polymarket profit and loss from SonarX Snowflake data, rank traders, and serve a client dashboard.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/Bryancostco/CPSC490-G04-EpicEngineers)

**Start here:** Decide the stack this week and record it in proposal §4 (#52); the skeleton in #62 and the architecture doc in #56 both wait on it.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ✅ done | Three epics (#24, #29, #33), 15 stories titled 'Objective N.M: ...' linked in §2. Sprint 2 tasks #49-#65 filed, assigned, on the Sprint 2 milestone; #62, #54, #55 lack sp:. |
| 2. Specs | ⚠️ started | docs/specs/pnl-calculation.md (open PR #67 only, not on develop) — Epic #24 Goal 1 Missing: Epic #24 Goal 1 (spec unmerged); Epic #29 Goal 2: top traders and drivers (#54 open); Epic #33 Goal 3: client dashboard. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ✅ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: er: PNL results and wallet data stored; uml: sequence of a PNL run (#59); ui_flow: leaderboard and wallet lookup pages (#60). |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 names Snowflake only; stack explicitly 'not chosen yet' (#52 open). Language: not chosen; Framework: not chosen; Platform: not chosen; Data: SonarX Snowflake (Polygon/Polymarket tables); own storage undecided; Hosting/hardware: not chosen; Sponsor resources: SNX-1: SonarX Snowflake access, credentials via Slack pending; Tools: GitHub Projects, Mermaid. |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, tests/test_login.py: course example unchanged; prototype/README.md and requirements.txt: unchanged scaffold; #62 (skeleton + Snowflake connection) open, no branch |

**Merge first** (not counted until it's in `develop` or `main`): PR #67 — PNL calculation spec for Goal 1; base develop; PR #68 — DFD L0/L1 mmd+png and design doc; base is spec branch, retarget develop; PR #66 — cite Sprint 2 work items in proposal §4; PR #69 — proposal references [1]-[7]; PR #70, #71, #72, #64 — context doc, dev plan, Sprint 2 review draft, sync main into develop.

**To do before your Sprint 2 review:**

1. Hold the stack decision meeting, file notes as an issue, and close #52 by writing the choices and reasons into proposal §4 and CLAUDE.md.
2. Merge PRs #64, #66, #67, #68 into develop (retarget #68), then link all merged docs in §4.
3. Write docs/design/architecture.md (#56) with architecture and system-context diagrams as Mermaid plus PNG.
4. Write the ER (#57), sequence (#59) and dashboard flow (#60) design docs; each first line names epic and stories.
5. Write docs/specs/trader-ranking.md (#54) and a dashboard spec for epic #33.
6. Implement #62: replace login example with the chosen skeleton, .env.example, and Snowflake smoke query; note row count in the PR.
7. After PRs #67 and #68 merge, add their summary, diagrams and links to proposal §4 (currently says no spec or design documents exist).

[↑ Back to all groups](#groups)

<a name="g05" id="g05"></a>

### G05 · Fighting Mongooses: WILS passive whale locator and identifier

*Hydrophone array locates whale calls by time difference of arrival; an AI classifies species and a database stores detections.* · Sprint 2: Oct 13 – 26 · **Sprint 2 review Tue Oct 27** · [repository](https://github.com/M-Kwatcher/CPSC490-G05-Fighting-Mongooses)

**Start here:** File Sprint 2 tasks for specs, diagrams and environment, then write proposal §4 stating language, ML framework, database and hardware with reasons.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | Two epics (#8, #14), 9 stories titled 'Objective N.M:' linked in §2, all on Sprint 2 with assignee and sp:. Goal 3 or any data/UI epic absent; no tasks for specs, design, environment. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #8 Goal 1: Build an AI recognizing whale calls; Epic #14 Goal 2: Create a locator for sound distance. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ✅ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: hydrophone audio to detection to location to storage; uml: sequence of call detected, located, saved; er: whale-call database stores clips with timestamp and hydrophone ID. |
| 4. Environment | ❌ not started | Stated in: nowhere (§4 skeleton; Python/numpy/scipy visible only in prototype). Language: Python (inferred from prototype/); Framework: numpy, scipy, matplotlib; AI framework undecided; Data: SQL database (db/init/schema.sql in open PR #39); Hosting/hardware: hydrophone array; hardware unstated; Tools: pytest, GitHub Actions CI. |
| 5. Prototype wiring | ⚠️ started | prototype/locator/ (tdoa.py, simulate.py, config.py, demo_delay.py) on develop: working direction estimate #15; prototype/tests/test_tdoa.py; requirements.txt pins numpy/scipy/matplotlib; prototype/login.py and tests/test_login.py still present; README header still scaffold |

**Merge first** (not counted until it's in `develop` or `main`): PR #38 — distance estimate locate.py with tests, into develop (story #16); PR #39 — db/init/schema.sql and ER diagram png; targets main, retarget develop; Branch issue#9 — 4 commits not in develop (database for #9).

**To do before your Sprint 2 review:**

1. Write proposal §3 and §4: Python, ML framework, DBMS, hydrophone hardware or simulation, dataset source, each with a reason.
2. Create docs/specs/ files for epics #8 and #14 with first-line epic/story headers; delete example-spec.md.
3. Add architecture and system-context diagrams to docs/design/ plus a DFD and detection sequence diagram; export images and list in §4.
4. Incorporate the ER diagram into proposal §4 with caption and link once PR #39 merges.
5. Retarget and merge PR #39 into develop; add editable ER source; merge PR #38 after review.
6. Clean prototype/: remove login files, rewrite README with fresh-machine setup, add .env.example and a smoke run.
7. File tasks for each of these with parent, sp: and Sprint 2, and link them in §4.

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

### G07 · MightyMorphin: materials database for Edwards (EL-1)

*Internal web app extracting material data from CoC and test-report PDFs into a verified relational database.* · Sprint 2: Oct 20 – Nov 2 · **Sprint 2 review Tue Nov 3** · [repository](https://github.com/CPSC490-Team-Proj/CPSC490-G07-MightyMorphin)

**Start here:** Finish #47 (tech stack and AWS services) first: the DB and framework choice drives the ER diagram, specs and prototype skeleton.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 product epics (#11,#17,#22), 16 objective stories, none with Sprint milestone or assignee. Goal 0 (#42) holds spec/design tasks. Process epics #1,#4,#28,#45 clutter. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: Epic #11 Goal 1 Extraction and verification; Epic #17 Goal 2 Storage and management; Epic #22 Goal 3 Access and analysis. |
| 3. Design & diagrams | ⚠️ started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: PDF ingest, OCR/extract, verify, store pipeline; er: materials, vendors, lots, documents tables; uml: sequence upload, extract, review, approve; ui_flow: upload, review queue, search, compare screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 and §3 (main); develop §4 still skeleton; #47 open. Language: Python; Framework: TBD backend and frontend; Platform: internal web app; AWS (Objective 2.2); Data: relational DB, engine TBD; Snowflake option under evaluation; Hosting/hardware: AWS-hosted; team laptops; Sponsor resources: Edwards CoC and test-report PDFs; sponsor Snowflake platform (unconfirmed); Tools: VS Code, Git/GitHub; document-processing library TBD. |
| 5. Prototype wiring | ❌ example files only | prototype/ holds only course login.py, test_login.py, README, requirements.txt (unchanged) |

**Merge first** (not counted until it's in `develop` or `main`): develop out of sync: main holds proposal §3/§4/§2 content, develop still skeleton; issue #67: port typed-link fix between develop and main (no PR yet).

**To do before your Sprint 2 review:**

1. Assign #46, #58, #59 and write the three goal specs (scope, FR/NFR traced to stories, acceptance criteria, open questions) in proposal §4 or docs/specs/ files linked from §4.
2. Draw architecture, system context, DFD, ER, extraction sequence and review-queue wireframes (#36-#41); embed as Mermaid or PNG in proposal §4 and fill the four empty figure links.
3. Finish #47: choose DB, backend, frontend, OCR library, AWS services; replace TBD cells in §4 with reasons tied to §3.
4. Create prototype skeleton with manifest, .env.example, README setup and run, smoke run on one sample PDF; replace login scaffold.
5. Fix §4: document index links, #58 URL; add #28 and #67; sync develop and main by PR; give product stories a sprint and owner.
6. Recommended: keep summaries and diagrams in proposal.md but put full spec and design detail in docs/specs/ and docs/design/, linked from §4.

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

### G12 · ACJMM (RTX-1): Explainable 6G Waveform Classification

*App that finds signal peaks, classifies waveform/modulation, and explains results with confidence and Unknown labels.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/CharlesSinde/CPSC490-G12-ACJMM)

**Start here:** Open the PR for branch Application-Structure into develop and write prototype/README.md and requirements.txt so the existing classifier code has a documented, runnable setup.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 5 epics (#57-#61), ~13 stories, several titled as tasks not objectives. Sprint 2 stories #63, #67, #68, #70, #71 lack milestone/assignee; 0 typed refs; #95-#98 unlinked. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #57 Signal Detection & Preprocessing; epic #58 Application interface and cross functional integration; epic #59 Waveform Identification & Receiver Processing; epic #60 Modulation, Decision & Explainable AI; epic #61 Modulation type re-classifier. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: .iq input through peaks, classifier, XAI report; er: only if runs/results are stored; uml: sequence for classify-one-snapshot flow; ui_flow: CLI first, then GUI screens. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (prose only, on main and develop). Language: MATLAB, possibly Python; Framework: MATLAB 6G Simulink library; ML/CV methods; Captum (#64); Platform: desktop CLI and GUI over one core engine; Data: signal data from sponsor mentors (.iq files, #97); Hosting/hardware: local machines; not stated; Sponsor resources: RTX-1 mentor-provided simulated 6G waveforms; Tools: GitHub board; Python test tooling in develop. |
| 5. Prototype wiring | ⚠️ started | develop: prototype/modulation_classifier.py + tests/test_modulation_classifier.py; develop: prototype/xai/calibration.py, decision_fusion.py + tests/test_calibration.py; develop: prototype/data/raw/.gitkeep; main still has only login.py scaffold; prototype/README.md and requirements.txt still scaffold copies; login.py still present |

**Merge first** (not counted until it's in `develop` or `main`): PR #99 (develop, merged): XAI calibration/Unknown abstention in prototype/xai; not yet on main; Branch Application-Structure: 5 commits not in develop; open a PR; Branch docs/team-documentation: 3 commits not in develop; open a PR; Merge develop into main so Sprint 2 work reaches main.

**To do before your Sprint 2 review:**

1. Write five specs in proposal §4 (or docs/specs/, linked from §4) (one per epic #57-#61) naming epic and stories first, requirements traced to stories, acceptance criteria.
2. Create architecture and system-context diagrams in proposal §4 as Mermaid or images; add DFD L1 and a classify-flow sequence diagram; list all in proposal §4 Diagrams.
3. Fill proposal §4 Environment: MATLAB vs Python split, ML libraries, GUI toolkit, data source, with reasons; link specs under Specification and design documents.
4. Recommended once §4 has the summaries: move full spec/design detail into docs/specs/<epic>.md and docs/design/, linking each from §4.
5. Fix prototype/README.md, requirements.txt, .env.example, add a smoke run on a sample .iq file; delete login.py and test_login.py.
6. Open PRs for Application-Structure and docs/team-documentation into develop, then merge develop into main.
7. Retitle stories to objective wording, add Sprint 2 milestone/assignee to #63, #67, #68, #70, #71, use typed refs, link #95-#98.

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

### G15 · HIBBI-01: Constrained-hardware ECS game engine with demo game

*Small ECS game engine for low-end hardware with cross-platform builds, renderer, editor, and a demo game.* · Sprint 2: Oct 15 – 28 · **Sprint 2 review Thu Oct 29** · [repository](https://github.com/Isaiah714/CPSC490-G15-HIBBI-01)

**Start here:** Do #46: add prototype/CMakeLists.txt with a window-and-cube build that compiles on a fresh machine, then record language and graphics API choices in §4.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 2 epics (#24, #25), 8 stories (#26-#33) objective-titled but no sp:/milestone/assignee; stray epic #6; §2 skeleton; refs untyped; #46 parent points to itself. |
| 2. Specs | ❌ not started | No specification in proposal.md or `docs/specs/` yet. Missing: epic #24 Game Engine; epic #25 Game Demo. |
| 3. Design & diagrams | ❌ not started | ▫️ architecture · ▫️ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: input to ECS systems to renderer; uml: sequence for frame loop; class for ECS; er: only if levels/assets serialized; ui_flow: editor (#33) and game screens. |
| 4. Environment | ❌ not started | Stated in: nowhere (§4 skeleton; HW#4 names no language or graphics API; only #46 mentions CMake). Language: not stated (CMake implies C/C++); Framework: custom ECS engine; graphics API not stated; Platform: Windows, Mac, Linux (story #31); constrained older hardware; Data: not stated; Hosting/hardware: low-end target hardware not specified; Sponsor resources: none stated; Tools: CMake (#46). |
| 5. Prototype wiring | ❌ example files only | prototype/login.py, tests/test_login.py: course example unchanged; No manifest and no CMakeLists.txt in prototype/ (requirements.txt absent); prototype/README.md: template text |

**To do before your Sprint 2 review:**

1. Fix #46 parent self-reference, set Sprint 2/sp:/assignee on #24-#33, and use typed refs in §2 and §4.
2. Write §3 approach and §4 environment (language, graphics API, window library, CMake, target OSes, test hardware) with reasons.
3. Write specs for epics #24 and #25 (#49) in proposal §4 with requirements traced to stories and acceptance criteria.
4. Recommended once §4 has the summaries: move full spec/design detail into docs/specs/<epic>.md and docs/design/, linking each from §4.
5. Draw architecture (#48) and system-context (#47) diagrams in proposal §4 as Mermaid or images with images; add ECS class and frame-loop sequence diagrams.
6. Add prototype/CMakeLists.txt skeleton and window-plus-cube smoke run (#46, #9); replace README; delete login.py and test_login.py.
7. Open PRs into develop for each Sprint 2 issue, link all in §4, and merge develop into main.

[↑ Back to all groups](#groups)

<a name="g16" id="g16"></a>

### G16 · Neuroprosthetic: BridgeWatch, real-time cross-chain bridge exploit detection (SNX-3)

*Alarm system that learns normal bridge-vault outflow and alerts operators on exploits, with a dashboard.* · Sprint 2: Oct 22 – Nov 4 · **Sprint 2 review Thu Nov 5** · [repository](https://github.com/garybs16/CPSC490-G16-Neuroprosthetic)

**Start here:** Start task #62: create docs/design/architecture.md with editable Mermaid for the existing Figure 1 and 2, and add the SQLite ER diagram.

| Item | Status | What I found |
|---|---|---|
| 1. Epics & stories | ⚠️ gaps | 3 epics (#11-#13) and 11 objective-titled stories; Sprint 2 stories #14, #15 and tasks #61-#66 are assigned with sp and milestone. Task #69 is not linked in proposal §4; #67 is untyped. |
| 2. Specs | ⚠️ started | docs/specs/goal-2-detection.md (develop) — Epic #12, stories #5,#16-#19; FR/NFR, EARS, rule tables, acceptance criteria; docs/specs/goal-3-dashboard.md (main, develop) — Epic #13, stories #20,#21; problem, scope, requirements, criteria Missing: Epic #11 Goal 1: Learn what normal bridge activity looks like (task #61 open). |
| 3. Design & diagrams | ⚠️ started | ✅ architecture · ✅ context · ▫️ data flow · ▫️ ER · ▫️ UML · ▫️ page flow. Needed for this project: dfd: ingest, store, baseline, detector, alerts pipeline; er: SQLite store holds transfers, alerts, cursor; uml: sequence for live loop to alert to webhook; ui_flow: operator dashboard, mark-as-seen flow. |
| 4. Environment | ⚠️ partial | Stated in: proposal §4 (Table 6), README in prototype/. Language: Python 3.12; Framework: FastAPI + uvicorn; single-page web dashboard (prototype/web/bridgewatch.html); Platform: Docker image (prototype/Dockerfile.bridgewatch); OS not stated; public Ethereum JSON-RPC nodes; Data: SQLite store; saved hack datasets as JSON under prototype/bridgewatch/data; Hosting/hardware: Docker packaging; host not chosen (Table 6 says 'Not decided'); Sponsor resources: SonarX stream, prices and balances still 'To request'; SNX-3 mentor questions in #28; Tools: pytest, GitHub Actions CI, Slack webhook alerts. |
| 5. Prototype wiring | ✅ done | prototype/requirements.txt pins fastapi, uvicorn, httpx; requirements-dev.txt pins pytest; prototype/bridgewatch/ modules mirror architecture: source, detector, store, live, notify, app; prototype/README.md: install, run, test commands; 48 offline tests; prototype/Dockerfile.bridgewatch and run_bridgewatch.py (demo and live smoke run); prototype/bridgewatch/config.py reads BRIDGEWATCH_* variables; web/bridgewatch.html dashboard |

**Merge first** (not counted until it's in `develop` or `main`): PR #70 (open, develop) — ingest lag in minutes and degrade past five minutes; closes #69; branch 15-baseline-check — 1 commit not in develop, no PR; open one for #15 or drop; develop to main release PR due by Nov 3 (task #64); develop has goal-2 spec and sprint-2-start.

**To do before your Sprint 2 review:**

1. Write docs/specs/goal-1-baseline.md for #11 stories #14 and #15 (task #61), with a first line naming the epic and stories.
2. Add editable sources for Figures 1 and 2 and the store ER, live-loop sequence and dashboard wireframe (task #62); show them in proposal §4.
3. Update proposal §4 Table 9 to list goal-1, goal-2, goal-3 specs and any design doc with issue refs; add #69 and the Sprint 2 tasks.
4. Recommended: put the full design detail in docs/design/architecture.md and keep the summary and Figures 1 and 2 in proposal §4.
5. Add prototype/.env.example and a SonarX source stub, and state in README which commands prove the toolchain on a fresh machine.
6. Review and merge PR #70, then decide on branch 15-baseline-check; keep every PR tied to an issue.
7. Open the develop to main release PR by Nov 3 and write docs/sprint-reviews/sprint-2.md (#64).

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
