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

**Draft status:** Sections 0–2 combine the team's supplied project description with revised wording and proposed objectives. Sections 3–7 retain the original repository template. The team must review the draft, resolve **TO CONFIRM** fields, add actual issue links, and verify references before submission.

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

> Describe your proposed approach to solve the problem, specifying how you
> will achieve the stated goals. List some possible strategies.

〈Your approach — **clear and concise**. State the strategy you chose, the
alternatives you considered, and the reasoning that decided between them.
Think of this as the argument, not the manual: a reader should finish this
section understanding *what* you will do and *why that* rather than the
alternatives.〉

**Keep the details out of this section.** Tooling, platforms, frameworks,
DBMS choices, environment setup, diagrams, and the work breakdown all belong
in §4 (Required Environment, Resources, and Planned Activities). If a
sentence here names a version number, a library, or a configuration, it
probably belongs in §4 — leave a pointer instead ("the implementation stack
is detailed in §4").

〈A few paragraphs, or a short list of candidate strategies with one line of
trade-off each. If it runs past a page, you are writing §4.〉

## 4. Required Environment, Resources, and Planned Activities

> Review the required and available resources and environment to complete
> your project. For example, server, platform, software tools, operating
> systems, DBMS, or any required skills.
>
> Describe the expected activities to achieve the stated goals, e.g.,
> software development process.

〈Your environment, resources, and planned activities.〉

**Diagrams belong in this section.** Include at minimum a high-level
architecture diagram and a system (context) diagram; add the ER/EER model and
a data-flow diagram where they help the reader understand what you are
building and what it depends on. Draw them with any graphical tool
(Lucidchart, draw.io, Miro, Mermaid, ERDPlus, Figma), keep the authoritative
copies in `docs/design/` with both editable source and exported image, and
reference them here.

〈Number every figure, caption it, and point at it from the prose — "Figure 1
shows the three deployment tiers and the trust boundary between them." A
figure the text never mentions is decoration. See `docs/design/DIAGRAMS.md`
for tools, conventions, and the rule that every box and arrow must be
verified against reality.〉

### Specification and design documents

**Every specification and design document the team writes is listed here**
with the objective it serves. This section is the index of the project's
technical detail: §3 holds the argument, §4 holds the documents that make it
buildable. CI gate G9 fails if a document exists in `docs/specs/` or
`docs/design/` that this section does not link.

| Document | Kind | Covers | Issues |
|---|---|---|---|
| 〈docs/specs/account-management.md〉 | specification | 〈account management requirements〉 | 〈#n, #n〉 |
| 〈docs/design/architecture.md〉 | design | 〈system architecture + data model〉 | 〈#n〉 |

〈The scaffold ships `docs/specs/example-spec.md` and
`docs/design/example-design.md` as worked examples — read them, then delete
them once you have your own, and list yours here.〉

〈Replace these rows with your own. Each document names its epic and stories
in its own first lines too (gate G2), so the trail runs both ways.〉

### Planned activities — the work items

The goals and objectives are listed in §2 as epics and user stories. The following table links supporting work items.

| Issue | Type | Activity | Parent | Owner | Sprint |
|---|---|---|---|---|---|
| [#11](https://github.com/sopper75/CPSC490-G19-TitanSecurity/issues/11) | task | Update proposal sections 0–2 | Standalone | 23jdo5 | Sprint 1 |

〈Replace these rows with your own, and keep the table current as you file new
issues — with §2 it gives a reader every planned activity in one place, each
traceable to the objective it serves.〉

## 5. Project Outcomes

> Describe the outcomes or deliverables, e.g., final project report, user
> manuals, source code, data or database files, etc.
>
> Note: the deliverables always include the team GitHub repository, which
> must already contain prototype v0 (a thin end-to-end proof-of-concept,
> however small, running when this proposal is submitted). Briefly describe
> what your v0 demonstrates and how to run it.

〈**One or two paragraphs** explaining the project outcome overall — what will
exist when the project is finished, and what it will let someone do. Keep it
prose, not a checklist; name the deliverables inside the paragraphs, and say
briefly what prototype v0 demonstrates today and how to run it.〉

## 6. Project Timeline

> Identifies tasks (project objectives) to be performed, milestones to be
> met, and the estimated number of hours for each task.

〈**This is the plan for CPSC 491 next semester — the implementation timeline,
not this semester's proposal work.** Identify the tasks (your objectives from
§2), the milestones, and the estimated hours for each, in the order they will
be built. State the assumptions it rests on (sponsor availability, data
access, hardware).〉

| Task (objective) | Milestone | Owner | Est. hours | Spring phase |
|---|---|---|---|---|
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |

〈Do **not** put this fall's four proposal sprints here — those live on the
project board and in `docs/sprint-reviews/`. This section answers "how does
the system actually get built next semester?"〉

## 7. AI Usage

> Per the course AI policy (see the syllabus, Use of AI Tools), disclose the
> AI tools used in preparing this proposal and the prototype: which tools,
> for what tasks (e.g., code generation, test writing, debugging,
> diagramming), and approximately what fraction of each artifact was
> AI-assisted.
>
> Reminder: the prose of this proposal must be your own writing. You remain
> fully responsible for the correctness of all AI-assisted work, including
> the prototype code.

〈Your disclosure. Naming the tool is not disclosure — name what it drafted,
what fraction of each artifact was AI-assisted, and how you verified it.〉

## 8. References

The following references are retained from the team's supplied draft. Their bibliographic details and support for the statements above require team verification; inclusion here does not certify that they have been independently checked.

[1] Halperin, D., Hu, W., Sheth, A., and Wetherall, D. “Tool Release: Gathering 802.11n Traces with Channel State Information.” *ACM SIGCOMM Computer Communication Review*, 41(1), p. 53, 2011. https://doi.org/10.1145/1925861.1925870

[2] Geng, J. *Dense Human Pose Estimation From WiFi*. Master's thesis, Carnegie Mellon University, Technical Report CMU-RI-TR-22-59, 2022. https://publications.ri.cmu.edu/dense-human-pose-estimation-from-wifi

[3] Geng, J., Huang, D., and De la Torre, F. *DensePose From WiFi*. arXiv:2301.00250. https://arxiv.org/abs/2301.00250. **TO CONFIRM: publication year; the supplied draft lists 2022.**

[4] Todt, J., Morsbach, F., and Strufe, T. “BFId: Identity Inference Attacks Utilizing Beamforming Feedback Information.” *Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security*, pp. 2399–2413, 2025. https://doi.org/10.1145/3719027.3765062

[5] Mengdu. “ESP-CSI: DIY WiFi Human Presence Detection.” *Hackster.io*, January 15, 2026. https://www.hackster.io/limengdu0117/esp-csi-diy-wifi-human-presence-detection-f80508. Accessed October 4, 2026, as recorded in the team's draft.
