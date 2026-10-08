# Project Proposal — Radar over WiFi

**Department of Computer Science**  
**CPSC 490 Undergraduate Seminar in Computer Science — Proposal for Capstone Project**

**Group G19 — Titan Security** · Sponsor: **TO CONFIRM: sponsor code**  
Authors: Jonathan Do, Delvin Cao, Zachary Headley, Alex Le, Chase Sisavath  
GitHub usernames: **TO CONFIRM for each author**  
Semester: Fall 2026  
Original proposal date: October 4, 2026  
Draft revision date: October 8, 2026  
Repository: https://github.com/sopper75/CPSC490-G19-TitanSecurity

**Draft status:** This document combines the team's supplied project description with proposed wording for unfinished sections. The team must review the proposed methods and estimates, resolve all **TO CONFIRM** fields, add actual issue/document links, and verify references before submission. Proposed work is not a claim of completed implementation.

## 0. Abstract

Accessible Wi-Fi equipment may offer a way to investigate short-range drone sensing without deploying a dedicated radar system. Wi-Fi signals change as objects move through the surrounding environment. Channel State Information (CSI) records properties of the wireless channel that can support analysis of these changes [1]. However, observing a change does not establish that a drone caused it: human movement, environmental variation, and interference can also affect measurements.

Radar over WiFi will investigate whether a prototype using CSI can distinguish drone activity from non-drone conditions in controlled experiments. The project will establish a CSI capture and recording platform, collect labeled measurements, develop a detection classifier, and investigate estimates of drone position and movement. Evaluation will address detection accuracy, missed detections, false detections, and performance at different distances. The team will also document equipment cost, portability, and setup effort and compare these with available published information about selected conventional radar systems.

The expected contribution is a reproducible prototype and an evidence-based assessment of its capabilities and limitations. Human-sensing research motivates the investigation but does not establish that the proposed hardware will detect or locate drones successfully. The project therefore treats performance as an experimental question. This proposal describes the relevant background, research problems, goals, proposed approach, required resources, deliverables, and implementation timeline.

## 1. Introduction

Radar detects objects by transmitting radio waves and analyzing reflected signals. Wi-Fi also uses radio waves, primarily to exchange data between devices. Signals can reach a receiver along multiple paths after reflecting from surrounding objects. Movement can change these paths and the measured wireless channel. CSI provides measurements that researchers can use to investigate these changes [1].

Radar over WiFi will examine whether accessible Wi-Fi equipment can provide useful information about nearby drone activity. A central challenge is distinguishing drone-related changes from changes caused by people, interference, or ordinary background variation. Detecting motion alone would not satisfy the project's drone-detection objective.

The project is motivated by affordability, portability, and setup effort. These benefits will be evaluated rather than assumed. The initial scope is a controlled experimental prototype; results will describe the equipment, environments, and conditions actually tested. They will not establish suitability for operational security or field deployment.

### 1.1 Related Work

Halperin et al. describe a tool for collecting CSI, providing a foundation for experimental wireless-channel measurements [1]. Geng's thesis and the related DensePose From WiFi paper investigate estimating human pose from Wi-Fi measurements [2], [3]. These works motivate the use of wireless measurements for sensing, but their human-sensing results do not establish drone-detection performance.

The team's supplied literature review also identifies BFId, which investigates identity inference using Wi-Fi beamforming feedback [4]. Its relevance is that wireless measurements may reveal information beyond their original communication purpose. It addresses a different measurement source and task from the proposed drone classifier. The ESP-CSI project provides a practical example of human-presence sensing with ESP32 equipment [5]. As a project account, it offers implementation context rather than direct evidence of performance for this project's target.

| Existing approach | Contribution relevant to this project | Strength | Limitation for our project | How Radar over WiFi differs |
|---|---|---|---|---|
| CSI collection tool [1] | Collection of wireless-channel measurements | Provides a basis for reproducible measurement work | Collection alone does not identify drones; equipment compatibility must be checked | Adds labeled drone experiments and detection evaluation |
| Human-pose estimation [2], [3] | Learning relationships between Wi-Fi measurements and physical activity | Investigates richer outputs than presence alone | Human-pose results do not demonstrate drone sensing or transfer to our equipment | Evaluates drone presence and investigates position and movement |
| BFId [4] | Identity inference from beamforming feedback | Highlights information exposed by wireless measurements | Uses a different task and measurement approach | Focuses on drone-versus-non-drone conditions |
| ESP-CSI presence project [5] | Practical sensing with accessible hardware | Offers prototype and deployment context | Human-presence results are not drone-detection results | Measures drone detection, confounding conditions, and range |

These approaches differ in their measurements, targets, and outputs. The proposed contribution is not that Wi-Fi sensing is new, but that the team will evaluate a specific accessible setup for drone sensing and document its practical limitations. Hardware selection and testing must establish which lessons transfer to this project.

**TO CONFIRM:** Team members must verify the comparison against the sources they have read. Select and cite the conventional radar systems used for the later cost and deployment comparison; none have been identified yet.

### 1.2 Problem Statements

**P1. Reproducible measurements:** The project needs a repeatable way to obtain and preserve usable wireless-channel measurements so experiments can be compared and checked.

**P2. Target discrimination and estimation:** Changes in wireless measurements are not unique to drones. It remains uncertain whether the selected equipment can distinguish drone activity from human movement and interference and support useful estimates of position and movement.

**P3. Performance and practicality:** The detection range, error rates, cost, portability, and setup effort of the proposed system have not been established. Without these measurements, its usefulness and trade-offs relative to conventional radar cannot be assessed.

| Problem | Addressed by |
|---|---|
| P1 | Goal 1; Objectives 1.1–1.2 |
| P2 | Goal 2; Objectives 2.1–2.3 |
| P3 | Goal 3; Objectives 3.1–3.3 |

## 2. Goals and Objectives

### Goal 1: Build a Wi-Fi CSI sensing platform

**Epic link: TO CONFIRM.**

**Objective 1.1: Set up a Wi-Fi transmitter and receiver pair and demonstrate CSI frame capture.**  
Document the equipment and configuration needed to reproduce the setup, and verify that the receiver captures CSI frames during a test recording. **Story link: TO CONFIRM.**

**Objective 1.2: Save CSI measurements to timestamped files and verify their data quality.**  
Implement a recording process and check the saved measurements for missing or malformed records and timestamp consistency. Document the checks and their results. **Story link: TO CONFIRM.**

### Goal 2: Detect drones and estimate their position and movement using Wi-Fi CSI

**Epic link: TO CONFIRM.**

**Objective 2.1: Collect labeled CSI datasets for drone activity, empty background, human movement, and interference conditions.**  
Record the condition and equipment arrangement for each recording. Document the amount of data collected for each condition and separate training and evaluation recordings. **Story link: TO CONFIRM.**

**Objective 2.2: Train and evaluate a classifier that distinguishes drone presence from non-drone conditions.**  
Use the labeled datasets to develop the classifier and evaluate it on recordings excluded from training. Report its predictions for drone activity, empty background, human movement, and interference conditions. **Story link: TO CONFIRM.**

**Objective 2.3: Implement and evaluate estimates of drone position and movement in a controlled test area.**  
Compare the estimates with recorded reference positions and movements. Report position error and how consistently the system identifies movement, including conditions where estimation fails. **Story link: TO CONFIRM.**

### Goal 3: Evaluate detection performance and practical trade-offs against conventional radar

**Epic link: TO CONFIRM.**

**Objective 3.1: Measure drone-detection accuracy, missed detections, and false detections on held-out test recordings.**  
Report the evaluation results and define how each metric is calculated. Present results separately for the tested conditions so that the effects of human movement and interference are visible. **Story link: TO CONFIRM.**

**Objective 3.2: Measure drone-detection performance at multiple distances to determine the effective detection range.**  
Define the distance reference, test arrangement, and criterion for successful detection before conducting the evaluation. Repeat trials at each tested distance and report the farthest tested distance that meets the criterion under those conditions. **Story link: TO CONFIRM.**

**Objective 3.3: Compare prototype cost, portability, and setup effort with selected conventional radar systems using documented evidence.**  
Record the prototype's equipment cost, physical size, weight, and setup time. Compare these measurements with available published information for the selected radar systems, identifying unavailable data and differences in capabilities or testing conditions. **Story link: TO CONFIRM.**

The proposed radar comparison is literature-based rather than a commitment to obtain radar equipment. The team must confirm this scope. Performance thresholds, trial counts, and test distances will be specified before final evaluation. Surrogate targets, if used during development, will be identified separately and will not be presented as evidence of actual drone detection.

## 3. Proposed Approaches

The proposed approach begins with reliable measurement collection. The team will establish a repeatable transmitter–receiver arrangement, record CSI, and check the integrity of saved data before developing a classifier. This separates collection problems from detection problems and creates recordings that can be reused for analysis.

The team will then collect labeled sessions representing drone activity and non-drone conditions. Labels will describe observed conditions rather than model predictions. Entire recording sessions will be assigned to training or evaluation sets to reduce the risk of closely related samples appearing in both. Data preparation choices and model selection will use training data, with a separate validation process where needed; final evaluation recordings will remain excluded from model selection.

A simple change-detection baseline will provide a comparison for the proposed learned classifier. A threshold-based approach may be easier to inspect but may respond to non-drone movement. A trained classifier may better distinguish patterns, but requires representative labeled recordings. The team will choose a model based on available data and validation results rather than assume that a more complex model will perform better.

Position and movement estimation will be investigated using recordings with known reference positions and movements. The team will determine whether the selected sensing arrangement supports the intended spatial output. If additional sensing locations or a narrower estimation scope are needed, the change will be documented and agreed before revising the objective.

Final experiments will measure detection errors and performance across tested distances and conditions. Practical comparisons will use measured prototype characteristics and documented radar information. Differences in test conditions and capabilities will be stated explicitly; a cost comparison alone will not establish equivalent performance.

## 4. Required Environment, Resources, and Planned Activities

The project requires CSI-capable Wi-Fi equipment, a computer for capture and analysis, storage for labeled recordings, and access to a drone and controlled test area. Ordinary Wi-Fi connectivity alone does not confirm that a device exposes the measurements needed for the project. Equipment compatibility must therefore be established before committing to a collection platform.

| Resource | Intended use | Selection or availability |
|---|---|---|
| Wi-Fi transmitter and CSI-capable receiver | Generate traffic and collect channel measurements | TO CONFIRM: models, antennas, firmware, and CSI support |
| Capture and analysis computer | Record, prepare, and analyze data | TO CONFIRM: computer and operating system |
| Capture and analysis software | Log data, train models, and generate results | TO CONFIRM after hardware selection |
| Drone and test area | Collect labeled drone and background sessions | TO CONFIRM: access and test arrangement |
| Position and distance reference | Check range and spatial estimates | TO CONFIRM: measurement method |
| Data storage | Preserve raw data, labels, and experiment metadata | TO CONFIRM: location, capacity, and backup method |

Planned activities include hardware validation, recording-tool development, data-quality checks, labeled collection, classifier development, position-estimation experiments, and final evaluation. Each recording will preserve its condition label, timestamp information, and relevant setup metadata. Raw recordings will remain distinguishable from processed data so that analysis can be repeated.

The proposed high-level architecture is a Wi-Fi transmitter and receiver feeding a capture/logger component, followed by timestamped storage, data preparation, detection and estimation, and evaluation outputs. In the proposed system context, a team operator configures and labels experiments; drone activity and background conditions affect the sensing environment; and the prototype produces measurements and analysis results. These descriptions are design proposals, not verified implementation diagrams.

**TO CONFIRM:** Create and verify the required architecture and system-context diagrams against the selected setup. Save editable sources and exported images under `docs/design/`, then insert numbered figures, captions, and links here.

### Specification and design documents

The following documents are proposed work products, not files confirmed to exist. Their actual links and issue references must be added when created.

| Planned document | Kind | Objectives served | File and issue links |
|---|---|---|---|
| CSI capture and recording specification | Specification | 1.1, 1.2 | TO CONFIRM |
| Dataset and labeling protocol | Specification | 2.1, 2.2 | TO CONFIRM |
| Architecture and system-context design | Design | 1.1–2.3 | TO CONFIRM |
| Evaluation protocol | Specification | 2.3, 3.1–3.3 | TO CONFIRM |

### Planned activities — the work items

Goal epics and objective stories belong in §2. The table below identifies supporting activities for the team to reconcile with its actual issues. It does not assign existing issue numbers, owners, or sprint commitments.

| Issue link | Type | Activity | Parent or purpose | Owner | Sprint |
|---|---|---|---|---|---|
| TO CONFIRM | Task | Update proposal and reconcile issue links | Standalone proposal work | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Check hardware and capture compatibility | Objective 1.1 | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Document recording format and quality checks | Objective 1.2 | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Prepare labeling and experiment protocol | Objective 2.1 | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Create and verify architecture/context diagrams | Goals 1 and 2 | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Define evaluation measures and range-test criteria | Objectives 3.1 and 3.2 | TO CONFIRM | TO CONFIRM |
| TO CONFIRM | Task | Select and document radar comparison sources | Objective 3.3 | TO CONFIRM | TO CONFIRM |

Repository changes will use feature branches and pull requests into `develop`, with each pull request closing an issue linked from this document. Sprint stories will have one assignee, a sprint milestone, a priority label, and story points. Epics and tasks beneath a pointed story will not receive separate points; standalone work items will carry their own points and sprint milestone.

## 5. Project Outcomes

The planned outcome is an experimental Wi-Fi CSI sensing prototype accompanied by source code, configuration instructions, a recording procedure, labeled datasets where distribution is appropriate, and reproducible analysis. The team will deliver detection results, position and movement estimation results, an effective-range assessment, and a comparison of equipment cost, portability, and setup effort. The final report will explain both successful results and limitations, including conditions in which the system fails to distinguish drone activity reliably.

The team repository will contain the implementation and documentation needed to reproduce the work. The proposed minimum end-to-end prototype will capture CSI, save a recording, load that recording for analysis, and produce an inspectable output. This milestone will establish a working data path without claiming validated drone detection. **TO CONFIRM: actual prototype v0 status, what it currently demonstrates, its location, and exact run instructions.** The supplied repository template requires a runnable v0 when the proposal is submitted; this draft does not claim that requirement has already been met.

## 6. Project Timeline

This is a proposed CPSC 491 implementation plan for the following semester, not the Fall 2026 proposal sprint schedule. Weeks are relative to the start of implementation. Estimates represent total team person-hours and are planning suggestions requiring team review. They assume that compatible hardware, a drone, and a suitable test area are available. Hardware delays or inadequate spatial information may require revised milestones.

| Task (objective) | Milestone | Owner | Proposed person-hours | Spring phase |
|---|---|---|---|---|
| 1.1 Establish CSI capture | Repeatable capture demonstration | TO CONFIRM | 30 | Weeks 1–2 |
| 1.2 Record and verify data | Timestamped recordings and quality report | TO CONFIRM | 25 | Weeks 2–3 |
| 2.1 Collect labeled datasets | Documented sessions and training/evaluation split | TO CONFIRM | 55 | Weeks 3–6 |
| 2.2 Develop detector | Baseline and classifier with validation results | TO CONFIRM | 55 | Weeks 5–8 |
| 2.3 Investigate spatial estimation | Position/movement estimates and error analysis | TO CONFIRM | 60 | Weeks 7–11 |
| 3.1 Evaluate detection | Held-out accuracy, miss, and false-detection results | TO CONFIRM | 30 | Weeks 10–12 |
| 3.2 Evaluate range | Repeated distance trials and range assessment | TO CONFIRM | 30 | Weeks 11–13 |
| 3.3 Compare practicality | Cost, portability, and setup comparison | TO CONFIRM | 20 | Weeks 12–13 |
| Integrate documentation and demonstration | Reproducible release and final report | TO CONFIRM | 45 | Weeks 14–15 |

The proposed total is 350 team person-hours. The team will revise estimates and assign owners before adopting this plan. Progress will be assessed through recorded demonstrations and documented results rather than time spent alone.

## 7. AI Usage

OpenAI's Codex assistant was used to reorganize team-supplied proposal material, edit wording, refine goals and measurable objectives, and draft missing sections, including problem statements, the proposed approach, resource planning, deliverables, and a suggested implementation timeline. AI assistance affected wording throughout this draft and supplied substantial new planning text. The generated plans and estimates have not yet been confirmed by the team.

**TO CONFIRM before submission:** Estimate the proportion of the final proposal that remains AI-assisted after team revision. Record which team members verified the claims, references, objectives, and feasibility, and describe the checks actually completed. Disclose any additional AI assistance to code, tests, or diagrams separately; its extent is not established by the supplied material. The team must revise the final prose in accordance with the course's own-writing requirement and remains responsible for the submitted work.

## 8. References

The following references are retained from the team's supplied draft. Their bibliographic details and support for the statements above require team verification; inclusion here does not certify that they have been independently checked.

[1] Halperin, D., Hu, W., Sheth, A., and Wetherall, D. “Tool Release: Gathering 802.11n Traces with Channel State Information.” *ACM SIGCOMM Computer Communication Review*, 41(1), p. 53, 2011. https://doi.org/10.1145/1925861.1925870

[2] Geng, J. *Dense Human Pose Estimation From WiFi*. Master's thesis, Carnegie Mellon University, Technical Report CMU-RI-TR-22-59, 2022. https://publications.ri.cmu.edu/dense-human-pose-estimation-from-wifi

[3] Geng, J., Huang, D., and De la Torre, F. *DensePose From WiFi*. arXiv:2301.00250. https://arxiv.org/abs/2301.00250. **TO CONFIRM: publication year; the supplied draft lists 2022.**

[4] Todt, J., Morsbach, F., and Strufe, T. “BFId: Identity Inference Attacks Utilizing Beamforming Feedback Information.” *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security*, pp. 2399–2413, 2025. https://doi.org/10.1145/3719027.3765062

[5] Mengdu. “ESP-CSI: DIY WiFi Human Presence Detection.” *Hackster.io*, January 15, 2026. https://www.hackster.io/limengdu0117/esp-csi-diy-wifi-human-presence-detection-f80508. Accessed October 4, 2026, as recorded in the team's draft.
