# Group repository status: proposal vs. issue board

**CPSC 490 · Fall 2026 · swept 2026-10-08 03:29 UTC.** The previous edition (2026-10-07) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. Every goal in your proposal §2 should be an epic, and every objective a user story titled with the objective's own words.

### Class at a glance

- ✅ **Aligned:** 5 (G01, G07, G08, G13, G16)
- ⚠️ **Partial:** 6 (G02, G06, G11, G12, G15, G19)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 5 (G03, G04, G09, G10, G18)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 3 (G05, G17, G20)
- Team-filed issues: **235** across 17 groups (40 new since 2026-10-07).
- Using epics: G01, G02, G06, G07, G08, G11, G13, G14, G15, G16, G18, G19. User stories: G01, G02, G06, G07, G08, G13, G15, G16, G18, G19. Story points: G01, G02, G03, G04, G07, G09, G10, G11, G12, G14, G15, G16.
- README doesn't describe the proposal's project yet: G05, G07, G11, G12, G14, G15, G16, G20.

### What changed since 2026-10-07

- **G16** moves from **Partial** to **Aligned**: 3 goal epics and 9 stories now cover every §2 objective. Next: merge PRs #24/#25 so `proposal.md` and the README stop showing the template, and link the 14 issues from the proposal.
- **G12** moves from **Process only** to **Partial**, and its *Document first* status from **Broken** to **Gaps**: the submitted proposal is now in `proposal.md`, and §4 links 9 of 16 issues through PRs that close them. Still missing: issues for the pipeline features (peak finding, parameter estimation, explanation, GUI/CLI).
- **G09** moves from **No issues** to **Process only**: 15 proposal-writing tasks with `sp:` points and Sprint milestones. No feature issues yet, and `proposal.md` §2/§4 are still the skeleton.
- **G01** added its epics and stories (#20–#28); `proposal.md` now links 18 of 20 issues (was 9). Its merged PRs still don't say `Closes #N`.
- **G02** grew to 23 issues, but only Wi-Fi scanning is tracked, and `proposal.md` links none of them.
- **G10:** the instructor PRs are merged and the main README now has the real project summary. The §2 epics and stories still don't exist, and there are 11 direct commits to main/develop.
- **G07** still pushes proposal edits straight to `main` (17 commits vs 1 PR). That is now its biggest gap.
- **G12 #42** (the instructor's writing-task fix) is closed now that the fix is merged.

### Sprint calendar (per group; 14 days from your sprint meeting)

| Groups | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| G01–G05 | Sep 29 – Oct 12 | Oct 13 – 26 | Oct 27 – Nov 9 | Nov 10 – 23 |
| G06–G10 | Oct 6 – 19 | Oct 20 – Nov 2 | Nov 3 – 16 | Nov 17 – 30 |
| G11–G15 | Oct 1 – 14 | Oct 15 – 28 | Oct 29 – Nov 11 | Nov 12 – 25 |
| G16–G20 | Oct 8 – 21 | Oct 22 – Nov 4 | Nov 5 – 18 | Nov 19 – Dec 2 |

### Fix first

- **G14 (Cyber Squad):** the README or issue board describes a different project than the proposal. Make the board match the proposal, or tell the instructor the project changed.
- **Merge the instructor's open PRs.** Still open in 14 repositories: G01 #31; G05 #4, #2; G06 #8, #2; G07 #10; G08 #26; G09 #4, #2; G11 #22; G13 #39, #29; G14 #18, #16; G15 #20, #8; G16 #10, #8; G18 #23; G19 #10; G20 #9, #7.
- **Pull requests: fill in the template and link the issue** (`Closes #N`), and open feature PRs into `develop`, not `main`. Seen this edition in G01, G02, G03, G04, G05, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20.

## Document first: proposal.md → issue → pull request

**The rule: document first, then workflow, then code.**
- Every issue is linked from `proposal/proposal.md`: epics and user stories in §2, every other work item in §4.
- Every code change lands through a pull request that closes one of those issues. No pushing straight to `main` or `develop`.
- A feature, enhancement, bug, task or sub-task that isn't under a user story carries its **own `sp:` points in a Sprint milestone**.
- **Sprint 1, until you have epics and stories:** file every issue as a **task** with `sp:` points in the **Sprint 1** milestone.

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Items missing own sp:/Sprint | PRs with no issue | Direct pushes (main / develop) | Chain | Fix first |
|---|---|---|---|---|---|---|---|
| G01 | 9 links / skeleton | 18 of 20 | 6 | 10 of 16 | 4 / 3 | ⚠️ Gaps | Open every doc change as a PR from a feature branch into develop that closes a #N issue (ten merged PRs went to main with no issue); also link sponsor questions #41/#42 from proposal.md section 4. |
| G02 | skeleton / skeleton | 0 of 23 | 1 | 4 of 12 | 1 / 1 | ❌ Broken | Fill proposal.md sections 2 and 4 and link #16-#25 and #36-#41 from them (currently 0 of 23 linked), then file the project epics and stories there first. |
| G03 | skeleton / skeleton | 0 of 9 | 5 (Sprint 1 rule) | 3 of 7 | 1 / 0 | ❌ Broken | Make #15, #16, #17, #5, #4 typed tasks with sp: in Sprint 1, add sp:/milestone to #1/#20, and link all of them from proposal.md section 4 (0 of 9 linked). |
| G04 | skeleton / skeleton | 0 of 7 | 2 | 1 of 7 | 0 / 0 | ❌ Broken | Replace the template proposal.md on develop with the real proposal and link #11-#13 plus new epics/stories from sections 2 and 4; 0 of 7 issues are linked. |
| G05 | skeleton / skeleton | 0 of 0 | none | 0 of 0 | 0 / 0 | ❌ Broken | Write the proposal into proposal/proposal.md (still the template) and file Sprint 1 tasks with sp: for every proposal section; there are 0 issues, 0 PRs and 0 team commits. |
| G06 | skeleton / skeleton | 0 of 4 | none | 0 of 0 | 12 / 0 | ❌ Broken | Fill proposal/proposal.md section 2 and 4 (still the template skeleton on develop) and link epics #3/#4 and stories #5/#6 plus new stories for the checklist-only objectives; route proposal/README edits through PRs instead of direct pushes to main (12 so far). |
| G07 | 16 links / skeleton | 16 of 23 | none | 1 of 1 | 17 / 2 | ⚠️ Gaps | Stop pushing to main: open PRs from feature branches into develop that close issues (17 direct commits on main vs 1 PR). |
| G08 | skeleton / skeleton | 7 of 33 | none | 1 of 5 | 0 / 0 | ⚠️ Gaps | Link #3-#36 from proposal/proposal.md section 2 (epics/stories) and 4 (tasks): develop's proposal is still a skeleton so only 7 of 33 issues are linked; also give tasks sp: and Sprint milestones. |
| G09 | skeleton / skeleton | 0 of 15 | 3 (Sprint 1 rule) | 1 of 1 | 1 / 0 | ❌ Broken | Link #5-#19 from proposal.md section 4 (it is still a skeleton) and add feature issues for the logger itself; stop pushing to main and open PRs into develop that close issues. |
| G10 | skeleton / skeleton | 0 of 8 | 2 (Sprint 1 rule) | 1 of 1 | 7 / 4 | ❌ Broken | Create the three epics and nine objective stories from section 2 (this closes #13), link them and #4-#9 from proposal.md, and stop pushing directly to main/develop (11 direct commits). |
| G11 | skeleton / skeleton | 2 of 11 | 2 | 0 of 7 | 1 / 1 | ❌ Broken | Fill proposal section 2 and 4 and link epic #4 plus tasks #3, #7, #8, #9, #13, #17, #20 from them (2 of 11 issues linked now); give #3 and #13 sp:. |
| G12 | 0 links / 9 links | 9 of 16 | none | 3 of 8 | 1 / 1 | ⚠️ Gaps | Write section 2 goals and open epics/stories for the actual pipeline features, link them plus #27, #36 and #28-#32 (or close the duplicates) from proposal.md so every issue is listed. |
| G13 | 0 links / 0 links | 0 of 24 | 6 | 2 of 10 | 1 / 0 | ❌ Broken | Link epics #16-#18 and stories #19-#27 from proposal section 2 and tasks #8, #10-#13, #15, #34, #35 from section 4 (0 of 24 linked now); give the six unpointed tasks sp:. |
| G14 | skeleton / skeleton | 0 of 4 | 1 | 2 of 7 | 1 / 1 | ❌ Broken | Replace epic #8 with epics for the sandbox goals, write proposal section 2/4, and link all issues from them (0 of 4 linked). |
| G15 | skeleton / skeleton | 0 of 6 | 2 | 3 of 8 | 4 / 4 | ❌ Broken | Stop direct pushes to main/develop (4 commits incl. proposal and prototype) and link all 6 issues from proposal section 2/4 (0 linked now). |
| G16 | skeleton / skeleton | 0 of 14 | none | 4 of 7 | 5 / 3 | ❌ Broken | Merge PR #24 so proposal.md carries the submitted proposal and link epics #11-#13 from section 2 and stories #5, #14-#21 plus tasks #22-#23 from section 4; today 0 of 14 issues are linked. |
| G17 | skeleton / skeleton | 0 of 0 | none | 4 of 4 | 4 / 1 | ❌ Broken | File the first issues (Sprint 1 tasks with sp: until epics/stories exist), link them from proposal.md sections 2/4, and stop merging PRs and commits straight into main without an issue. |
| G18 | skeleton / skeleton | 0 of 12 | 1 | 0 of 7 | 1 / 1 | ❌ Broken | Write proposal.md sections 2/4 and link #17-#20, #15 and the HW#4 writing tasks from it, then file the game-system stories (with sp: and Sprint) under #17; PRs already close issues, keep that. |
| G19 | skeleton / skeleton | 0 of 6 | none | 1 of 1 | 36 / 28 | ❌ Broken | Stop committing directly to main (36 direct commits): work on feature branches, open PRs into develop that close issues, and link #2-#8 from proposal.md sections 2/4. |
| G20 | skeleton / skeleton | 0 of 0 | none | 1 of 1 | 1 / 1 | ❌ Broken | Fill proposal/proposal.md (title, abstract, section 2) and file the first issues as Sprint 1 tasks with sp: linked from section 4; no work items exist yet. |

## Every group, by number

| Group | Project | Board | README | Status | Not tracked yet | Next step |
|---|---|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 20 issues (4 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** | none | Merge the open PRs #35/#36 into develop and close #32, then add sp: and a Sprint milestone to the writing tasks #10, #12, #13, #14, #9; stop merging doc PRs straight into main. |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 23 issues (6 new); epics, stories, points, Sprint 1 | matches | ⚠️ **Partial** | multi-node distribution and sync; Bluetooth capture; fingerprinting; localization; dashboard; active-recording detection | Write section 2 with goals and objectives for capture, fingerprinting, location and dashboard, then file one epic per goal and sp: stories in Sprint 2 and fix the #16/#17 parent loop. |
| G03 California | Three AIs and Literate Programming | 9 issues; points, Sprint 1 | matches | ⚠️ **Process only** | all five core elements; no feature issues exist | Write section 2 (#17), then type the writing issues as tasks and file one epic per goal with sp: stories for the three AI stages in Sprint 2. |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 7 issues; points, Sprint 1 | matches | ⚠️ **Process only** | Trade parsing; Resolution matching; PNL computation; Trader ranking/edge analysis; Dashboard | Turn the kickoff notes into section 2 goals and objectives, file 2-3 epics and sp: stories (ingestion, PNL, ranking, dashboard) in Sprint 2, and write the Problem Statements. |
| G05 Fighting Mongooses | WILS | 0 issues; no epics or stories | not yet | ❌ **No issues** | All core elements (no issues exist) | Create the missing labels with the bootstrap, commit the real proposal into proposal/proposal.md, and file Sprint 1 tasks with sp: for each proposal section, then epics and stories for the goals. |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 4 issues; epics, stories, Sprint 1 | matches | ⚠️ **Partial** | Answer grading + recording missed concepts; Summaries/flashcards; Adaptive vs non-adaptive evaluation; Core LLM objectives 1.3, 1.4, 2.1-2.3 exist only as checklist lines in epics #3/#4, with no story issues | Before Sun Oct 11, fill proposal section 2 and 4 with the core loop (upload notes, generate questions, grade and record misses, weak-spot tracker, adaptive vs non-adaptive comparison), file each objective as a story issue titled verbatim, add sp: labels, and link every issue from the proposal. |
| G07 Mighty Morphin | Online Material Database | 23 issues (1 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** | none | Replace the course-guide README on main and develop with the project one-pager, close superseded epic #1, and link #4-#7, #27 and #28 from proposal.md. |
| G08 Crime Busters | Interactive Crime Map and Database | 33 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** | none | Before Sun Oct 11, add sp: labels and Sprint milestones to stories/tasks missing them (#14-#20, #23-#34), delete stray epics #6/#7, and write proposal section 2/4 linking the epics, stories and tasks. |
| G09 Sigma Squad | Vehicle Maintenance Logger | 15 issues (15 new); points, Sprint 1 | n/a | ⚠️ **Process only** | Vehicle/service-history input and recommendation engine; Paper-record bulk ingestion; Reminders and urgency labelling; Mileage tracking, DIY logs, parts finder, climate recommendations | Turn the section 2 goals into epics and objectives into user stories (or Sprint 1 tasks with sp:) for the logger's features, and list them in proposal.md sections 2 and 4. |
| G10 Team Jiddak | Stablecoin Wash-Trading and Suspicious Transaction Detection | 8 issues; points, Sprint 1 | matches | ⚠️ **Process only** | Goal 1 graph pipeline (no epic or stories); Goal 2 detection engine (no epic or stories); Goal 3 dashboard (no epic or stories); All nine objectives 1.1-3.3 | Do what #13 says: create the three epics and nine objective stories (titles verbatim from section 2, sp: on stories, Sprint 1), then list them in proposal.md sections 2 and 4. |
| G11 5 Guys | Marathon Tracker | 11 issues; epics, points, Sprint 1 | not yet | ⚠️ **Partial** | ML analysis of runs vs public marathon data; Storing performance data; Runner/supporter connection hub; Goals 2-3 and all objectives are not yet in proposal section 2 | Write the remaining objectives in proposal section 2 (GPS recording, route map, distance/pace, ML analysis), file one user story per objective under epic #4, and replace the course-guide README on main with the team README. |
| G12 ACJMM | Explainable 6G Waveform Classification | 16 issues (1 new); points, Sprint 1 | not yet | ⚠️ **Partial** | Peak detection and parallel processing; Parameter estimation (baud rate, carrier frequency); Explainability layer and abstention; GUI, CLI and interface control document; Evaluation across SNR/channel conditions | Add section 2 Goals and Objectives to proposal.md, then file epics and objective stories (explicit titles, sp:) for peak finding, parameter estimation, classification, explanation and GUI/CLI; fill the README (title still TBD). |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 24 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** | none | Add sp: labels to all stories and the unpointed tasks, put stories #25-#27 into a Sprint milestone, and reconcile proposal section 4 (web app) with the abstract and section 3 (Windows app). |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 4 issues; epics, points, Sprint 1 | not yet | ❌ **Mismatch** | Every core element; Proposal section 2 goals are still template text | Decide which project is real, then write proposal section 2 goals/objectives and make the README, epic and issues describe that same project (sandbox vs web scanner). |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 6 issues; epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** | ECS implementation; Game-creation tooling; Demo game; Performance measurement; Proposal section 2 goals not written | Write proposal section 2 goals/objectives (rendering, ECS, game tooling, benchmarking), file one epic per goal with stories, and fill the README title/team placeholders (still '3D Game'). |
| G16 Neuroprosthetic | BridgeWatch: cross-chain bridge exploit detection | 14 issues (13 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** | none | Merge #24 and #25 into develop so proposal.md and README show BridgeWatch (both still say Phenoscope/template), then put Sprint 1 work on the board and write real PR bodies. |
| G17 Sonic Scape | SonicScape | 0 issues; no epics or stories | matches | ❌ **No issues** | Space-themed navigation UI; NASA API ingestion/parser; Music playback and music data source; Swipe rating; Preference profile / recommendation engine | Fill proposal/proposal.md section 2 (Goals/Objectives, e.g. navigation UI, NASA ingestion, swipe profile), then file epics/stories (or Sprint 1 tasks with sp:) and link them from sections 2/4; open PRs into develop that close those issues; sync develop's placeholder README and settle on one project name. |
| G18 Team ProStrats | Project Rogue | 12 issues; epics, stories, Sprint 1 | matches | ⚠️ **Process only** | Class system; Weapon replacement / Mastery / affixes; Attributes, boons, respec; Branching route map and handcrafted rooms; Core combat and platforming; Playtest plan for build variety / meaningful decisions | Write proposal section 2 with one objective per core system (classes, weapon Mastery, attributes/boons, branching rooms, combat, playtest measures), file each as a story under epic #17 titled verbatim from section 2 with sp: and a Sprint milestone, and link them from the proposal. |
| G19 Titan Security | Radar over WiFi | 6 issues; epics, stories | matches | ⚠️ **Partial** | Effective-range measurement; Drone vs person/interference separation; Cost, portability and setup-effort comparison; Detection story under epic #3 (only position story #7) | Fill proposal section 2 with the real goals/objectives, make story titles match it verbatim, replace the template bodies in #2-#8, add stories for range and drone-vs-person separation, and give every issue sp: and a Sprint 1 milestone. |
| G20 Solos | Untitled first-person horror maze game | 0 issues; no epics or stories | not yet | ❌ **No issues** | Maze level design; Monster AI behaviors; Lighting/sound atmosphere; Encounter unpredictability; Core player loop | Move the abstract/introduction into proposal/proposal.md with a project title, write section 2, then file Sprint 1 tasks with sp: (maze level, monster AI, lighting/audio, player loop) and replace the README, which still reads 'CPSC490-G20-California'. |

## How to get to *Aligned*

Follow the course README, [§4 Epics and user stories on the issue board](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board). In short:

1. Each **goal** in your proposal §2 *Goals and Objectives* is one **epic** issue (label `epic`). Its body lists its user stories as a task list (`- [ ] #12`).
2. Each **objective** under a goal is one **user story** issue (label `user-story`), **titled with the objective itself, in the exact words of proposal §2**: an action word plus what gets completed, with a number wherever possible. Not a feature name, and not a paraphrase. A user-story sentence goes in the issue body only when the objective has a real user, and it is optional.
3. Every story in a sprint has exactly one assignee, a `Sprint N` milestone, a `priority:` label and an `sp: N` label (1, 2, 3, 5, 8; `sp: 8` means split it). Points go on the objective only, never on the epic or the tasks under it. A writing task with no objective above it carries its own points.
4. Link every epic and story from proposal §2, and every other work item (feature, enhancement, bug, task, sub-task) from §4. Make the README on `main` say what the proposal says: title, sponsor code, and a one-paragraph summary.
5. A work item that isn't under a user story carries its own `sp:` points in a Sprint milestone. In Sprint 1, until your epics and stories exist, every issue is a task with `sp:` in Sprint 1.
6. Change the repository only through pull requests from a feature branch into `develop`, each closing an issue that proposal.md links. Document first, then workflow, then code.

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
