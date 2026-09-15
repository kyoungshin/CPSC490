# Project Proposal — 〈Project Title〉

**CPSC 490 Undergraduate Seminar in Computer Science — Proposal for Capstone Project**
Department of Computer Science, California State University, Fullerton

**Group 〈N〉 — 〈Group Name〉** · Sponsor: 〈RTX-3 / EL-1 / SNX-n / independent〉
Authors: 〈Last, First (GitHub username)〉, 〈…〉
Date: 〈YYYY-MM-DD〉

> **This file is the proposal document, not a README.** Section numbers and
> titles below match the course Word template exactly, so it converts
> cleanly for Canvas submission. Write continuous academic prose — no task
> lists, no emoji, no repo jargon. Keep figures numbered and referenced.
> Delete this note and every 〈bracket〉 before submitting.
>
> **Converting to the Word template** (keeps the template's styles):
>
> ```bash
> pandoc proposal/proposal.md -o proposal.docx \
>   --reference-doc="CPSC 490 Project Proposal Template Fall 2026.docx"
> ```
>
> Then open it in Word, check the heading numbering and figure placement,
> and submit that file. If your team would rather write in Word directly,
> commit the `.docx` here as well — but keep this Markdown copy current,
> because it is what review and CI can actually read.

---

## 0. Abstract

〈150–250 words: the problem, your approach, and the expected outcome. Written
last, read first.〉

## 1. Introduction

〈Context and motivation. What is the setting, who has this problem, and why
does solving it matter? End with a short roadmap of the document.〉

### 1.1 Related Work

〈Survey existing solutions, products, and published work, and say what gap
remains for your project. Cite with bracketed numbers matching §7 — every
reference must be a source your team has actually read.〉

### 1.2 Problem Statements

〈State the problem this project solves, precisely enough to be falsifiable.
One paragraph per distinct problem; number them P1, P2, … if there are
several so later sections can refer back.〉

### 1.3 Goals and Objectives

Each **goal** is tracked as an **Epic** issue and each **objective** under it
as a **User Story** issue in the team repository (see the repository README
§4). Reference the issue numbers so the document and the board stay in step.

- **Goal 1: Secure account management** (Epic #1)
  - Objective 1.1: As a member, I want to register and log in, so that my
    data is private. (#2)
  - Objective 1.2: As a reviewer, I want a runnable login prototype, so that
    the riskiest flow is proven early. (#3)
  - Objective 1.3: As a developer, I want a documented architecture, so that
    implementation in CPSC 491 is unambiguous. (#4)
- **Goal 2: 〈your second goal〉** (Epic #〈n〉)
  - Objective 2.1: 〈As a …, I want …, so that …〉 (#〈n〉)

〈Goal 1 above is the live example in this repository — issues #1–#4 and the
project board show exactly these items with owner, sprint, priority, level of
effort, and story points. Replace it with your own goals and objectives.〉

## 2. Proposed Approaches

〈The candidate approaches you considered, the trade-offs between them, and
the direction you chose with the reasoning that decided it. Where a choice is
still open, say so and say when it will be closed.〉

## 3. Required Environment, Resources, and Planned Activities

〈Development process, languages and frameworks, datasets, hardware, cloud
services, sponsor-provided resources and access, and the activities that will
achieve the stated goals.〉

**Diagrams belong in this section.** At minimum include a high-level
architecture diagram and a system (context) diagram; add the ER/EER model and
a data-flow diagram where they help the reader understand what you are
building and what it depends on. Draw them with any graphical tool
(Lucidchart, draw.io, Miro, Mermaid, ERDPlus, Figma), keep the authoritative
copies in `docs/design/` with both editable source and exported image, and
reference them here.

〈Number every figure, caption it, and point at it from the prose — "Figure 1
shows the three deployment tiers and the trust boundary between them." A
figure the text never mentions is decoration. See `docs/design/DIAGRAMS.md`
for tools, file conventions, and the rule that every box and arrow must be
verified against reality.〉

## 4. Project Outcomes

〈What will exist at the end: concrete deliverables and the measurable
criteria by which each is judged complete. Distinguish what this semester
produces (proposal, specifications, designs, prototype) from what the
implementation semester produces.〉

## 5. Project Timeline

〈**This is the plan for CPSC 491 next semester — the implementation
timeline, not this semester's proposal work.** Lay out the spring schedule:
what gets built in each phase, in what order, with which dependencies and
milestones, and who owns each area. Show it as a table or a Gantt chart, and
state the assumptions it rests on (sponsor availability, data access,
hardware).〉

| Phase / Sprint (Spring) | Dates | Planned work | Deliverable |
|---|---|---|---|
| 〈Sprint 1〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈Sprint 2〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈Sprint 3〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈Sprint 4〉 | 〈…〉 | 〈…〉 | 〈…〉 |

〈Do **not** put this fall's four proposal sprints here — those live on the
project board and in `docs/sprint-reviews/`. This section answers "how will
the project actually be built next semester?"〉

## 6. AI Usage

〈Which AI tools the team used, for what parts of this proposal and the
prototype, and how the output was verified. Be specific and honest: naming
the tool is not disclosure — naming what it drafted and what you checked is.
The course requires human-in-the-loop practice, so describe the verification,
not just the generation.〉

## 7. References

〈Number references in the order first cited; cite them in the text as [1],
[2]. Every entry must be a source a team member has actually read and can
produce on request.〉

[1] 〈Author(s), "Title," Venue/Publisher, Year.〉
[2] 〈Author(s), "Title," Venue/Publisher, Year. DOI or URL.〉
[3] 〈For a web source: Author/Organization, "Title," URL, accessed YYYY-MM-DD.〉
