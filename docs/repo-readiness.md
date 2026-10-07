# Group repository status: proposal vs. issue board

**CPSC 490 · Fall 2026 · swept 2026-10-07 05:44 UTC.** The previous edition (2026-10-07) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. Every goal in your proposal §2 should be an epic, and every objective a user story titled with the objective's own words.

### Class at a glance

- ✅ **Aligned:** 4 (G01, G07, G08, G13)
- ⚠️ **Partial:** 6 (G02, G06, G11, G15, G16, G19)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 5 (G03, G04, G10, G12, G18)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 4 (G05, G09, G17, G20)
- Team-filed issues: **195** across 16 groups (19 new since 2026-10-07).
- Using epics: G01, G02, G06, G07, G08, G11, G13, G14, G15, G18, G19. User stories: G01, G02, G06, G07, G08, G13, G15, G16, G18, G19. Story points: G01, G03, G04, G07, G10, G11, G12, G14, G15, G16.
- README doesn't describe the proposal's project yet: G05, G07, G11, G12, G14, G15, G16, G20.

### What changed since 2026-10-07

- **New this edition: the *Document first* check** (table below). Every issue should be linked from `proposal/proposal.md`, and every change should land by a pull request that closes one of those issues. Right now **17 of 20 groups still have the template skeleton in proposal.md §2 and §4**, so almost no issue on any board is linked from the document. Only G01, G07 and G08 have started.
- **Direct pushes:** several groups commit straight to `main` or `develop` instead of opening a pull request. Worst: G19 (36 on `main`, 28 on `develop`), G07 (17 on `main`), G06 (12 on `main`) and G10 (6 and 4).
- **G07** moves from **Process only** to **Aligned**: 3 goal epics and 16 objective stories with `sp:` points and Sprint milestones, and its proposal §2 links 16 of them. It is the model to copy. Next: stop pushing to `main` and link the remaining 6 issues.
- **G19** retitled its stories with real objectives, added a *CSI Capture* story (#8) and named the project and sponsor in its README. Still **Partial**.
- **G06** removed the template brackets from its story titles. Still **Partial**.

### Sprint calendar (per group; 14 days from your sprint meeting)

| Groups | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| G01–G05 | Sep 29 – Oct 12 | Oct 13 – 26 | Oct 27 – Nov 9 | Nov 10 – 23 |
| G06–G10 | Oct 6 – 19 | Oct 20 – Nov 2 | Nov 3 – 16 | Nov 17 – 30 |
| G11–G15 | Oct 1 – 14 | Oct 15 – 28 | Oct 29 – Nov 11 | Nov 12 – 25 |
| G16–G20 | Oct 8 – 21 | Oct 22 – Nov 4 | Nov 5 – 18 | Nov 19 – Dec 2 |

### Fix first

- **G14 (Cyber Squad):** the README or issue board describes a different project than the proposal. Make the board match the proposal, or tell the instructor the project changed.
- **Merge the instructor's open PRs.** Still open in 14 repositories: G01 #31; G03 #19; G05 #4, #2; G06 #8, #2; G07 #10; G08 #26; G09 #4, #2; G11 #22; G13 #39, #29; G14 #18, #16; G15 #20, #8; G16 #10, #8; G18 #23; G20 #9, #7.
- **Pull requests: fill in the template and link the issue** (`Closes #N`), and open feature PRs into `develop`, not `main`. Seen this edition in G01, G02, G03, G04, G05, G07, G08, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20.

## Document first: proposal.md → issue → pull request

**The rule: document first, then workflow, then code.**
- Every issue is linked from `proposal/proposal.md`: epics and user stories in §2, every other work item in §4.
- Every code change lands through a pull request that closes one of those issues. No pushing straight to `main` or `develop`.
- A feature, enhancement, bug, task or sub-task that isn't under a user story carries its **own `sp:` points in a Sprint milestone**.
- **Sprint 1, until you have epics and stories:** file every issue as a **task** with `sp:` points in the **Sprint 1** milestone.

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Items missing own sp:/Sprint | PRs with no issue | Direct pushes (main / develop) | Chain | Fix first |
|---|---|---|---|---|---|---|---|
| G01 | 9 links / skeleton | 9 of 16 | 5 | 6 of 9 | 4 / 3 | ⚠️ Gaps | Link the 7 unlinked work issues (#9-#14, #18) from proposal.md section 4 (9 of 16 are linked via section 2), and stop direct commits to main/develop: open PRs that close an issue. |
| G02 | skeleton / skeleton | 0 of 17 | 1 | 4 of 12 | 1 / 1 | ❌ Broken | Write proposal.md sections 2 and 4 (still skeletons) and link epics/stories #20-#25 and #16-#18 from them; 0 of 17 issues are linked today. |
| G03 | skeleton / skeleton | 0 of 9 | 5 (Sprint 1 rule) | 3 of 7 | 1 / 0 | ❌ Broken | Replace the template proposal.md on develop with the real proposal text (it still has placeholders), then link #4/#5/#13/#15/#16/#17 from sections 2 and 4 and make them typed tasks with sp: in Sprint 1. |
| G04 | skeleton / skeleton | 0 of 7 | 2 | 1 of 7 | 0 / 0 | ❌ Broken | Replace the template proposal.md on develop with the real proposal and link #11-#13 plus new epics/stories from sections 2 and 4; 0 of 7 issues are linked. |
| G05 | skeleton / skeleton | 0 of 0 | none | 0 of 0 | 0 / 0 | ❌ Broken | Write the proposal into proposal/proposal.md (still the template) and file Sprint 1 tasks with sp: for every proposal section; there are 0 issues, 0 PRs and 0 team commits. |
| G06 | skeleton / skeleton | 0 of 4 | none | 0 of 0 | 12 / 0 | ❌ Broken | Fill proposal/proposal.md section 2 and 4 (still the template skeleton on develop) and link epics #3/#4 and stories #5/#6 plus new stories for the checklist-only objectives; route proposal/README edits through PRs instead of direct pushes to main (12 so far). |
| G07 | 16 links / skeleton | 16 of 22 | none | 1 of 1 | 17 / 2 | ⚠️ Gaps | Link #27 and writing tasks #4-#7 from proposal.md section 2/4 (16 of 22 linked) and move proposal edits (17 direct commits on main) into PRs that close issues. |
| G08 | skeleton / skeleton | 7 of 33 | none | 1 of 5 | 0 / 0 | ⚠️ Gaps | Link #3-#36 from proposal/proposal.md section 2 (epics/stories) and 4 (tasks): develop's proposal is still a skeleton so only 7 of 33 issues are linked; also give tasks sp: and Sprint milestones. |
| G09 | skeleton / skeleton | 0 of 0 | none | 0 of 0 | 1 / 0 | ❌ Broken | Create the issues: file the proposal's goals as epics and objectives as stories (or tasks with sp: in Sprint 1), list them in proposal.md section 2/4, and open PRs into develop that close them. |
| G10 | skeleton / skeleton | 0 of 8 | 2 (Sprint 1 rule) | 1 of 1 | 6 / 4 | ❌ Broken | Create the three epics and nine objective stories from proposal section 2 and link them (and writing tasks #4-#9) from proposal.md; today 0 of 8 issues are linked and 10 commits landed directly on main/develop. |
| G11 | skeleton / skeleton | 2 of 11 | 2 | 0 of 7 | 1 / 1 | ❌ Broken | Fill proposal section 2 and 4 and link epic #4 plus tasks #3, #7, #8, #9, #13, #17, #20 from them (2 of 11 issues linked now); give #3 and #13 sp:. |
| G12 | 0 links / 0 links | 0 of 15 | none | 3 of 7 | 1 / 1 | ❌ Broken | Write proposal section 2/4 and link all 15 issues from them (0 linked now); close duplicate setup issues #28-#31 and stop PRs #1/#2/#44 landing on main without an issue. |
| G13 | 0 links / 0 links | 0 of 24 | 6 | 2 of 10 | 1 / 0 | ❌ Broken | Link epics #16-#18 and stories #19-#27 from proposal section 2 and tasks #8, #10-#13, #15, #34, #35 from section 4 (0 of 24 linked now); give the six unpointed tasks sp:. |
| G14 | skeleton / skeleton | 0 of 4 | 1 | 2 of 7 | 1 / 1 | ❌ Broken | Replace epic #8 with epics for the sandbox goals, write proposal section 2/4, and link all issues from them (0 of 4 linked). |
| G15 | skeleton / skeleton | 0 of 6 | 2 | 3 of 8 | 4 / 4 | ❌ Broken | Stop direct pushes to main/develop (4 commits incl. proposal and prototype) and link all 6 issues from proposal section 2/4 (0 linked now). |
| G16 | skeleton / skeleton | 0 of 1 | none | 4 of 5 | 5 / 3 | ❌ Broken | Replace the template skeleton in proposal/proposal.md with the real proposal (section 2 goals and objectives) and link #5 plus new epic/story issues from sections 2/4. |
| G17 | skeleton / skeleton | 0 of 0 | none | 4 of 4 | 4 / 1 | ❌ Broken | File the first issues (Sprint 1 tasks with sp: until epics/stories exist), link them from proposal.md sections 2/4, and stop merging PRs and commits straight into main without an issue. |
| G18 | skeleton / skeleton | 0 of 12 | 1 | 0 of 7 | 1 / 1 | ❌ Broken | Write proposal.md sections 2/4 and link #17-#20, #15 and the HW#4 writing tasks from it, then file the game-system stories (with sp: and Sprint) under #17; PRs already close issues, keep that. |
| G19 | skeleton / skeleton | 0 of 6 | none | 1 of 1 | 36 / 28 | ❌ Broken | Stop committing directly to main (36 direct commits): work on feature branches, open PRs into develop that close issues, and link #2-#8 from proposal.md sections 2/4. |
| G20 | skeleton / skeleton | 0 of 0 | none | 1 of 1 | 1 / 1 | ❌ Broken | Fill proposal/proposal.md (title, abstract, section 2) and file the first issues as Sprint 1 tasks with sp: linked from section 4; no work items exist yet. |

## Every group, by number

| Group | Project | Board | README | Status | Not tracked yet | Next step |
|---|---|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 16 issues; epics, stories, points, Sprint 1 | matches | ✅ **Aligned** | none | Before the next deadline, add sp: labels and a Sprint milestone to open writing tasks #13/#10 (and #12/#9/#14 if reopened), file #9-#14/#18 under proposal.md section 4, and open feature branches into develop instead of committing README edits directly. |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 17 issues; epics, stories, Sprint 1 | matches | ⚠️ **Partial** | Bluetooth capture and multi-node distribution; Backend collection and fingerprinting; Location estimation; Dashboard; Recording-state detection | Fill proposal section 2 with 3-4 goals and objectives (capture, fingerprint, locate/dashboard, recording detection), file a matching epic plus sp: story each in Sprint 2, and fix #16's parent so it points to its epic. |
| G03 California | Three AIs and Literate Programming | 9 issues; points, Sprint 1 | matches | ⚠️ **Process only** | All five technical elements (handwriting recognition, code generation, computation/verification, pipeline integration, generated documentation) | Finish section 2 (#17) with 2-3 goals, file one epic per goal and one sp: story per objective in Sprint 1/2, and type the writing issues as tasks. |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 7 issues; points, Sprint 1 | matches | ⚠️ **Process only** | Trade parsing; Resolution matching; PNL computation; Trader ranking/edge analysis; Dashboard | Turn the kickoff notes into section 2 goals and objectives, file 2-3 epics and sp: stories (ingestion, PNL, ranking, dashboard) in Sprint 2, and write the Problem Statements. |
| G05 Fighting Mongooses | WILS | 0 issues; no epics or stories | not yet | ❌ **No issues** | All core elements (no issues exist) | Create the missing labels with the bootstrap, commit the real proposal into proposal/proposal.md, and file Sprint 1 tasks with sp: for each proposal section, then epics and stories for the goals. |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 4 issues; epics, stories, Sprint 1 | matches | ⚠️ **Partial** | Answer grading + recording missed concepts; Summaries/flashcards; Adaptive vs non-adaptive evaluation; Core LLM objectives 1.3, 1.4, 2.1-2.3 exist only as checklist lines in epics #3/#4, with no story issues | Before Sun Oct 11, fill proposal section 2 and 4 with the core loop (upload notes, generate questions, grade and record misses, weak-spot tracker, adaptive vs non-adaptive comparison), file each objective as a story issue titled verbatim, add sp: labels, and link every issue from the proposal. |
| G07 Mighty Morphin | Online Material Database | 22 issues (17 new); epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** | none | Replace the course-guide README with the project one-pager, close #1, add #27 and the writing tasks #4-#7 to proposal section 2/4, and stop pushing proposal edits straight to main. |
| G08 Crime Busters | Interactive Crime Map and Database | 33 issues (1 new); epics, stories, Sprint 1 | matches | ✅ **Aligned** | none | Before Sun Oct 11, add sp: labels and Sprint milestones to stories/tasks missing them (#14-#20, #23-#34), delete stray epics #6/#7, and write proposal section 2/4 linking the epics, stories and tasks. |
| G09 Sigma Squad | Vehicle Maintenance Logger | 0 issues; no epics or stories | n/a | ❌ **No issues** | All core elements: the repo has zero issues | Before Sun Oct 11, write proposal section 2 goals and objectives, then create epics/stories (or Sprint 1 tasks with sp:) and link them from proposal.md; replace develop's template README. |
| G10 Team Jiddak | Stablecoin Wash-Trading and Suspicious Transaction Detection | 8 issues; points, Sprint 1 | matches | ⚠️ **Process only** | Goals 1-3 and all nine objectives (no epics or stories exist) | Before Sun Oct 11, do #13: file three goal epics and nine objective stories (titles verbatim from proposal section 2) with sp: in Sprint 1, set #13's milestone, and link them from proposal.md section 2. |
| G11 5 Guys | Marathon Tracker | 11 issues; epics, points, Sprint 1 | not yet | ⚠️ **Partial** | ML analysis of runs vs public marathon data; Storing performance data; Runner/supporter connection hub; Goals 2-3 and all objectives are not yet in proposal section 2 | Write the remaining objectives in proposal section 2 (GPS recording, route map, distance/pace, ML analysis), file one user story per objective under epic #4, and replace the course-guide README on main with the team README. |
| G12 ACJMM | Explainable 6G Waveform Classification | 15 issues; points, Sprint 1 | not yet | ⚠️ **Process only** | Peak detection; Parameter estimation; GUI/CLI and ICD; Explanation layer; Evaluation across noise/channel conditions; Proposal has no section 2 goals either | Add proposal section 2 goals/objectives (peak picking, parameter estimation, classification, GUI/CLI, explanation), file an epic per goal with user-story objectives, and replace the README 'TBD' title and sponsor placeholders. |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 24 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** | none | Add sp: labels to all stories and the unpointed tasks, put stories #25-#27 into a Sprint milestone, and reconcile proposal section 4 (web app) with the abstract and section 3 (Windows app). |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 4 issues; epics, points, Sprint 1 | not yet | ❌ **Mismatch** | Every core element; Proposal section 2 goals are still template text | Decide which project is real, then write proposal section 2 goals/objectives and make the README, epic and issues describe that same project (sandbox vs web scanner). |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 6 issues; epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** | ECS implementation; Game-creation tooling; Demo game; Performance measurement; Proposal section 2 goals not written | Write proposal section 2 goals/objectives (rendering, ECS, game tooling, benchmarking), file one epic per goal with stories, and fill the README title/team placeholders (still '3D Game'). |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 1 issues; stories, points, Sprint 1 | not yet | ⚠️ **Partial** | Goals 1-3 as epic issues; Obj 2.1 alert rules; Obj 2.2 hack replay; Obj 2.3 false-alarm tuning as its own story; Obj 3.1 dashboard and Slack alerts; Obj 3.2 user test; Obj 2.4 stretch accounting check | Copy the real proposal text into proposal/proposal.md, write section 2 with Goals 1-3 and Objectives 1.1-3.2, link epics/stories from it, and file them (sp: + Sprint milestone) with #5 re-parented under the Goal 2 epic; also fix the README (still 'Phenoscope' with placeholders) and merge or close PRs #1-#4. |
| G17 Sonic Scape | SonicScape | 0 issues; no epics or stories | matches | ❌ **No issues** | Space-themed navigation UI; NASA API ingestion/parser; Music playback and music data source; Swipe rating; Preference profile / recommendation engine | Fill proposal/proposal.md section 2 (Goals/Objectives, e.g. navigation UI, NASA ingestion, swipe profile), then file epics/stories (or Sprint 1 tasks with sp:) and link them from sections 2/4; open PRs into develop that close those issues; sync develop's placeholder README and settle on one project name. |
| G18 Team ProStrats | Project Rogue | 12 issues; epics, stories, Sprint 1 | matches | ⚠️ **Process only** | Class system; Weapon replacement / Mastery / affixes; Attributes, boons, respec; Branching route map and handcrafted rooms; Core combat and platforming; Playtest plan for build variety / meaningful decisions | Write proposal section 2 with one objective per core system (classes, weapon Mastery, attributes/boons, branching rooms, combat, playtest measures), file each as a story under epic #17 titled verbatim from section 2 with sp: and a Sprint milestone, and link them from the proposal. |
| G19 Titan Security | Radar over WiFi | 6 issues (1 new); epics, stories | matches | ⚠️ **Partial** | Effective-range measurement; Drone vs person/interference separation; Cost, portability and setup-effort comparison; Detection story under epic #3 (only position story #7) | Fill proposal section 2 with the real goals/objectives, make story titles match it verbatim, replace the template bodies in #2-#8, add stories for range and drone-vs-person separation, and give every issue sp: and a Sprint 1 milestone. |
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
