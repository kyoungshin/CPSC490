# Group repository status: proposal vs. issue board

**CPSC 490 · Fall 2026 · swept 2026-10-09 06:36 UTC.** The previous edition (2026-10-08) is kept in git history.

This page compares each team's **issue board** with what its **own proposal** says it will build. Every goal in your proposal §2 should be an epic, and every objective a user story titled with the objective's own words.

**New to git or the board? Start with [First Steps](https://kyoungshin.github.io/CPSC490/first-steps.html)**: HW#4/HW#5 to the Sprint Board, every command listed.

### The rules this page checks

1. **Document first, then workflow, then code.** Every issue is cited in `proposal/proposal.md`, and every change lands through a pull request that closes one of those issues. No pushing straight to `main` or `develop`.
2. **Merge your work into `develop` or `main`.** This page reads only those two branches; work left on a feature branch doesn't count yet. Both branches are scanned below.
3. **Typed issue references**, each linked to its issue, at the end of the paragraph it belongs to: `[epic:#12](https://github.com/OWNER/REPO/issues/12)`, and likewise `[story:#N]`, `[feature:#N]`, `[enhancement:#N]`, `[bug:#N]`, `[task:#N]`, `[sub-task:#N]`, with the type matching the issue's own.
4. **Epics and stories are cited in §2 *Goals and Objectives* only.** Every other issue is cited anywhere in §4: environment, a specification or design document, a diagram's caption, or planned activities.
5. **Story points:** an issue **under a user story has no `sp:`** (the story carries the points). Every issue **not under a story** (the story itself, or a parentless feature, task, bug …) carries its **own `sp:` in a `Sprint N` milestone**. Epics carry no points. In Sprint 1, until epics and stories exist, every issue is a task with `sp:` in Sprint 1.
6. **One Sprint Board** (GitHub Projects, board layout), linked to the repository, with every open issue on it.

**Word for Canvas: one command.** Install pandoc once (`winget install pandoc`; macOS `brew install pandoc`), then from the repository root:

```
pandoc proposal/proposal.md -o proposal/proposal.docx --reference-doc=proposal/reference.docx --lua-filter=proposal/to-word.lua --resource-path=proposal
```

This produces the course template's cover page filled from your header block, the Abstract on its own page, Word-numbered headings, Times New Roman 11 pt with 1.5 spacing and 1.0-inch margins, and every issue tag such as `[epic:#12]` linked to *Appendix A. Issue References*, which lists the full URLs. See [`proposal/example-proposal.md`](https://github.com/kyoungshin/CPSC490/blob/main/proposal/example-proposal.md) and the [Word file it produces](https://github.com/kyoungshin/CPSC490/blob/main/proposal/example-proposal.docx).

### Prepare for your next sprint meeting

1. **Story points for the previous sprint:** the total committed at its start and the total done at its end. `scripts/sprint_report.py` counts both, from the `sp:` labels and `Sprint N` milestones: run the *Sprint report* workflow in your repository's Actions tab, or locally `GITHUB_REPOSITORY=owner/repo GITHUB_TOKEN=$(gh auth token) python scripts/sprint_report.py --sprint N --markdown`.
2. **The Sprint Board** showing every to-do issue for the current sprint: assignee, `Sprint N` milestone and `sp:` on each card.
3. **Progress aligned three ways:** the board, `proposal/proposal.md` and the prototype code tell the same story. Every closed issue is cited in the proposal, and its change is merged into `develop` or `main`.

### Class at a glance

- ✅ **Aligned:** 7 (G01, G07, G08, G13, G16, G19, G20)
- ⚠️ **Partial:** 6 (G02, G06, G10, G11, G12, G15)
- ⚠️ **Process only** (writing, meeting and setup tasks; no project features): 4 (G03, G04, G09, G18)
- ❌ **Mismatch** (board or README about a different project): 1 (G14)
- ❌ **No issues yet:** 2 (G05, G17)
- Team-filed issues: **269** across 18 groups (22 new since 2026-10-08).
- Using epics: G01, G02, G06, G07, G08, G10, G11, G13, G14, G15, G16, G18, G19, G20. User stories: G01, G02, G06, G07, G08, G13, G15, G16, G18, G19, G20. Story points: G01, G02, G03, G04, G07, G09, G10, G11, G12, G14, G15, G16, G19.
- README doesn't describe the proposal's project yet: G05, G07, G11, G12, G14, G15, G19.

### What changed since 2026-10-08

- **G20** went from no issues to **Aligned**: 16 issues (3 epics, 8 stories, 5 tasks), a Sprint board, and a rewritten README on `develop`. Next: cite the stories and tasks in `proposal.md` (3 of 16 cited so far) and give the stories `sp:` and a Sprint milestone.
- **G10** moved from *Process only* to **Partial** with its first project epic, #15 (Goal 1). Its stories aren't filed yet.
- **G16** cites all 21 of its issues in `proposal.md` (none before), and **G19**'s `develop` copy cites 12 of 12 through a pull request. Both moved from ❌ to ⚠️ in the Document-first table. Next for both: write the citations as typed references.
- **New this edition (instructor):** the rules at the top of this page; typed issue references (`[epic:#N]` …), with epics and stories cited in §2 only and every other issue in §4; the story-point rule; the Sprint-board check; and progress read from **both `main` and `develop`**, plus feature branches not merged into either. No group uses typed references yet. That's expected: the rule is new, and nobody loses anything for it this week.
- **Instructor pull requests in every repository:** *"Instructor: one-command Word export of proposal.md"*, into `develop`. It adds `proposal/reference.docx` and `proposal/to-word.lua` (and two `.gitignore` lines) so the pandoc command above works in your repo. Merge it.
- **Sprint boards (first check):** 15 groups have one the course can read. Every open issue is on the board for G02, G06, G09, G10, G12 and G20. G03, G05, G16, G17 and G19 have no readable board; G03, G16 and G19 link one from their README that can't be opened, so it is probably private. Make it visible and link it to the repository from its Projects tab. G01 and G07 have no board-layout view yet.

### Sprint calendar (per group; 14 days from your sprint meeting)

| Groups | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| G01–G05 | Sep 29 – Oct 12 | Oct 13 – 26 | Oct 27 – Nov 9 | Nov 10 – 23 |
| G06–G10 | Oct 6 – 19 | Oct 20 – Nov 2 | Nov 3 – 16 | Nov 17 – 30 |
| G11–G15 | Oct 1 – 14 | Oct 15 – 28 | Oct 29 – Nov 11 | Nov 12 – 25 |
| G16–G20 | Oct 8 – 21 | Oct 22 – Nov 4 | Nov 5 – 18 | Nov 19 – Dec 2 |

### Fix first

- **G14 (Cyber Squad):** the README or issue board describes a different project than the proposal. Make the board match the proposal, or tell the instructor the project changed.
- **Create the Sprint Board** (*Projects → New project → Board*, then link it to the repository from its Projects tab and from the README). No readable board yet: G03, G05, G16, G17, G19.
- **Merge the instructor's open PRs.** Still open in 9 repositories: G01 #31; G05 #4, #2; G06 #8, #2; G07 #10; G08 #26; G11 #22; G13 #39, #29; G14 #18, #16; G15 #8.
- **Pull requests: fill in the template and link the issue** (`Closes #N`), and open feature PRs into `develop`, not `main`. Seen this edition in G01, G02, G03, G04, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20.

## Progress on `main` and `develop`

What `proposal/proposal.md` says on each branch (rule 2), and feature branches holding work that is in neither yet. The tables below use the branch whose proposal cites more issues.

| Group | `main` | `develop` | Not merged yet |
|---|---|---|---|
| G01 | §2 9 links · §4 skeleton · 18 issues cited · 0 typed · 37 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | 18-abstract-intro (3 commits not in develop); 43-update-goals-and-objectives (20 commits not in develop); Damon (2 commits not in develop) |
| G02 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 75 〈placeholders〉 | none |
| G03 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 74 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | Elizabeth-7-7-patch-1 (4 commits not in develop); Sehaj36-patch-1 (6 commits not in develop) |
| G04 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | patch-1-proposal.md (2 commits not in develop) |
| G05 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G06 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 82 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | Kaleb16-patch-1 (1 commit not in develop) |
| G07 | §2 16 links · §4 skeleton · 16 issues cited · 0 typed · 40 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G08 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | §2 skeleton · §4 skeleton · 7 issues cited · 0 typed · 73 〈placeholders〉 | proposal-abstract (1 commit not in develop); proposal-goal-3 (1 commit not in develop) |
| G09 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | feature/5-proposal-goals-objectives (1 commit not in develop); feature/11-update-readme (1 commit not in develop); proposal-draft (3 commits not in develop) |
| G10 | §2 0 links · §4 0 links · 0 issues cited · 0 typed · 6 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G11 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 2 issues cited · 0 typed · 70 〈placeholders〉 | none |
| G12 | §2 0 links · §4 9 links · 9 issues cited · 0 typed | §2 0 links · §4 10 links · 10 issues cited · 0 typed | none |
| G13 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 0 links · §4 0 links · 0 issues cited · 0 typed | UnreadableCode1-patch-1 (1 commit not in develop); UnreadableCode1-patch-2 (8 commits not in develop); UnreadableCode1-patch-3 (1 commit not in develop) |
| G14 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | jvillacorte-patch-3 (1 commit not in develop) |
| G15 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 74 〈placeholders〉 | none |
| G16 | §2 12 links · §4 9 links · 20 issues cited · 0 typed | §2 12 links · §4 10 links · 21 issues cited · 0 typed | feature/5-bridgewatch-prototype (1 commit not in develop) |
| G17 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 77 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | none |
| G18 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 55 〈placeholders〉 | none |
| G19 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 80 〈placeholders〉 | §2 11 links · §4 skeleton · 12 issues cited · 0 typed · 27 〈placeholders〉 | none |
| G20 | §2 skeleton · §4 skeleton · 0 issues cited · 0 typed · 83 〈placeholders〉 | §2 3 links · §4 skeleton · 3 issues cited · 0 typed · 63 〈placeholders〉 | none |

## Document first: proposal.md → issue → pull request

Rules 1, 3 and 4 above, per group.

| Group | proposal.md §2 / §4 | Issues linked from proposal.md | Typed references | Linked issues closed / with a PR | PRs with no issue | Direct pushes (main / develop) | Chain | Fix first |
|---|---|---|---|---|---|---|---|---|
| G01 | 9 links / skeleton | 18 of 21 | 0 of 18 | 5 / 5 of 18 | 10 of 16 | 4 / 3 | ⚠️ Gaps | Rewrite proposal.md references as typed links ([epic:#20](...), [story:#23](...), [task:#33](...); 0 of 18 are typed), put #41/#42/#43/#32 in §4, and add all 16 open issues to the Sprint board (currently 0 items, no board view); then stop direct pushes/PRs into main. |
| G02 | skeleton / skeleton | 0 of 23 | 0 of 0 | 0 / 0 of 0 | 4 of 12 | 1 / 1 | ❌ Broken | proposal.md §2 and §4 are still skeletons with 0 of 23 issues linked: link epic #20 and stories #21-#25, #16 in §2 and every other issue in §4 as typed refs (e.g. [task:#36](url)), then file real project epics/stories (capture, fingerprinting, location, dashboard). |
| G03 | skeleton / skeleton | 0 of 9 | 0 of 0 | 0 / 0 of 0 | 3 of 7 | 1 / 0 | ❌ Broken | proposal.md on main and develop is still the unfilled template (0 of 9 issues linked, §2/§4 skeletons): paste the written proposal in, link #15/#16/#17/#5/#4/#13/#2 as typed [task:#N](url) in §4, make them typed tasks with sp: in Sprint 1, and create the Sprint board (README link is unreadable). |
| G04 | skeleton / skeleton | 0 of 7 | 0 of 0 | 0 / 0 of 0 | 1 of 8 | 0 / 0 | ❌ Broken | Merge PR #21 (and the unmerged patch-1-proposal.md branch) so proposal.md is no longer the template, then link #10-#13 as typed refs in §4 and add epics/stories for ingestion, PNL, ranking and dashboard in §2; 0 of 7 issues are linked. |
| G05 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 0 of 0 | 0 / 0 | ❌ Broken | Write the proposal into proposal/proposal.md and the team README (both still the course template), then file Sprint 1 tasks with sp: for each proposal section and link them as typed refs in §4; there are 0 issues, 0 team PRs, no Sprint board and no sprint-labels (milestones exist but hold nothing). |
| G06 | skeleton / skeleton | 0 of 5 | 0 of 0 | 0 / 0 of 0 | 0 of 1 | 12 / 0 | ❌ Broken | Fill proposal.md (still the course skeleton on main and develop) and link #3-#6 in section 2 and #10 in section 4 as typed [epic:#N] / [story:#N] / [task:#N] references; merge PR #9 into develop. |
| G07 | 16 links / skeleton | 16 of 24 | 0 of 16 | 0 / 0 of 16 | 1 of 2 | 17 / 2 | ⚠️ Gaps | Rewrite the 16 bare #N links in proposal.md section 2 as typed [epic:#N]/[story:#N](url) references on develop (develop's proposal.md is still the skeleton), and link tasks #5-#7, #29 in section 4. |
| G08 | skeleton / skeleton | 7 of 33 | 0 of 7 | 0 / 5 of 7 | 1 of 5 | 0 / 0 | ⚠️ Gaps | Link the epics, stories and tasks (only 7 of 33 are linked, none typed) from proposal.md as [epic:#N]/[story:#N] in section 2 and [task:#N] in section 4, then add sp: labels to stories. |
| G09 | skeleton / skeleton | 0 of 15 | 0 of 0 | 0 / 0 of 0 | 1 of 3 | 1 / 0 | ❌ Broken | Merge PR #22 (goals) and finish #10: list every issue in proposal.md section 4 as [task:#N](url) and add epics/stories linked from section 2; proposal.md links 0 of 15 issues. |
| G10 | skeleton / skeleton | 0 of 9 | 0 of 0 | 0 / 0 of 0 | 1 of 2 | 14 / 4 | ❌ Broken | Stop pushing to main (14 direct commits on main, 4 on develop): open PRs into develop, and link #15 plus new epics/stories from proposal.md section 2 and tasks #4-#9, #13 from section 4 as typed references. |
| G11 | skeleton / skeleton | 2 of 11 | 0 of 2 | 0 / 1 of 2 | 0 of 7 | 1 / 1 | ❌ Broken | Link every issue from proposal.md as typed references ([epic:#4](...) in §2; [task:#N](...) for #7, #8, #9, #13, #17, #20 etc. in §4), fix the bare/misplaced #13, and add sp: + Sprint 1 to #3, #13 and the meeting issues (or close them). |
| G12 | 0 links / 10 links | 10 of 17 | 0 of 10 | 3 / 4 of 10 | 3 of 13 | 1 / 1 | ⚠️ Gaps | Use typed refs in §4 ([task:#N](https://github.com/.../issues/N), 10 links are bare today), link the 7 unlinked issues (#27, #28-#32, #36) or close/merge the five duplicate setup issues, then open §2 epics and stories. |
| G13 | 0 links / 0 links | 0 of 24 | 0 of 0 | 0 / 0 of 0 | 2 of 11 | 1 / 0 | ❌ Broken | Link all 24 issues from proposal.md on develop as typed references: [epic:#16], [epic:#17], [epic:#18] and the 9 stories in §2, tasks #8 #10 #11 #12 #13 #15 (and process issues) in §4, then make every story carry its own sp: and a Sprint milestone (12 stories have none; #25-#27 and tasks #12, #13 have no milestone). |
| G14 | skeleton / skeleton | 0 of 4 | 0 of 0 | 0 / 0 of 0 | 2 of 7 | 1 / 1 | ❌ Broken | Move the submitted proposal text into proposal/proposal.md (83 template placeholders remain), write §2, then link the issues as typed references and file epics/stories that match the sandbox. |
| G15 | skeleton / skeleton | 0 of 6 | 0 of 0 | 0 / 0 of 0 | 3 of 8 | 4 / 4 | ❌ Broken | Link #6 and #9 in §2 and #10, #11, #12, #16 in §4 of proposal.md as typed references, put the Sprint 1 milestone on #12 and #16, and route code and proposal changes through PRs into develop instead of 4 direct commits to main. |
| G16 | 12 links / 10 links | 21 of 21 | 0 of 21 | 4 / 6 of 21 | 5 of 16 | 3 / 3 | ⚠️ Gaps | Rewrite all 21 links in proposal.md as typed references ([epic:#11], [story:#14], [task:#27] ...) with the matching kind, and make the Sprint board (linked in README as users/garybs16/projects/2) publicly readable with a board view holding every open issue. |
| G17 | skeleton / skeleton | 0 of 0 | 0 of 0 | 0 / 0 of 0 | 4 of 4 | 8 / 1 | ❌ Broken | File the first Sprint 1 tasks with sp: (navigation UI, NASA ingest, playback, swipe profile, recommender), link them from proposal.md sections 2/4 as typed references, and stop pushing proposal edits straight to main (use PRs into develop that close an issue). |
| G18 | skeleton / skeleton | 0 of 12 | 0 of 0 | 0 / 0 of 0 | 0 of 7 | 1 / 1 | ❌ Broken | Fill proposal.md §2/§4 (still skeleton) and link all 12 issues as typed references (epics/stories in §2, tasks in §4), then give the stories #18/#20 and tasks #2/#15 their own sp: in Sprint 1 and close or delete #13. |
| G19 | 11 links / skeleton | 12 of 12 | 0 of 12 | 0 / 1 of 12 | 1 of 2 | 36 / 28 | ⚠️ Gaps | Stop the 36 direct commits to main (work on feature branches, PRs into develop that close issues) and convert the 12 bare links in proposal.md into typed references ([epic:#2], [story:#8], [task:#11]), with the task in §4 and the Sprint board made readable. |
| G20 | 3 links / skeleton | 3 of 16 | 0 of 3 | 0 / 0 of 3 | 1 of 3 | 1 / 1 | ⚠️ Gaps | Link the 13 unlinked issues from proposal.md as typed references (stories #13-#15, #18-#20, #22-#23 in §2; tasks #11, #24, #26-#28 in §4) and add sp: plus a Sprint milestone to the 8 stories. |

## Sprint board and story points

Rules 5 and 6 above: one GitHub Projects board per team, linked to the repository, with a **board-layout Sprint Board view** and every open issue on it.

| Group | Sprint board | Open issues on the board | Board view | Missing own sp:/Sprint | sp: under a story (remove) | sp: on an epic (remove) |
|---|---|---|---|---|---|---|
| G01 | ✅ [CPSC490-01-BGAF](https://github.com/users/LeDuy23/projects/2) ⚠️ not linked to the repo | 0 of 16 | ❌ View 1 (table) | 10 | none | none |
| G02 | ✅ [CPSC490-LinuxLarpers](https://github.com/users/eliThomass/projects/4) | 15 of 15 | ✅ | 2 | none | none |
| G03 | ❌ none (README links github.com/users/eccortes4/projects/1 but it isn't readable (private, or wrong URL)) | – | – | 8 (Sprint 1 rule) | none | none |
| G04 | ✅ [CPSC490-G04-EpicEngineers](https://github.com/users/Bryancostco/projects/1) | 0 of 0 | ✅ | 5 | none | none |
| G05 | ❌ none | – | – | none | none | none |
| G06 | ✅ [@Joshbolus's Sprints for CPSC 490 project G6](https://github.com/users/Joshbolus/projects/1) | 5 of 5 | ✅ | 2 | none | none |
| G07 | ✅ [CPSC490-G7-MightyMorphin](https://github.com/orgs/CPSC490-Team-Proj/projects/1) | 20 of 21 | ❌ View 1 (table) | none | none | none |
| G08 | ✅ [CPSC490-G08-Crime-Busters](https://github.com/users/miketruong91/projects/1) | 30 of 32 | ✅ | 9 | none | none |
| G09 | ✅ [CPSC490-G09-SigmaSquad](https://github.com/users/TylerWard741/projects/1) | 13 of 13 | ✅ | 3 (Sprint 1 rule) | none | none |
| G10 | ✅ [Sprint board](https://github.com/users/Alexander-Sanchez2/projects/2) | 2 of 2 | ✅ | 2 | none | none |
| G11 | ✅ [CPSC490-G11-5Guys](https://github.com/users/Card1n/projects/1) ⚠️ not linked to the repo | 6 of 7 | ✅ | 5 | none | none |
| G12 | ✅ [CPSC490-G12-ACJMM](https://github.com/users/CharlesSinde/projects/1) | 7 of 7 | ✅ | none | none | none |
| G13 | ✅ [CPSC 490-05](https://github.com/users/ktnwin/projects/3) | 20 of 23 | ✅ | 18 | none | none |
| G14 | ✅ [CPSC490-G14-Cyber-Squad](https://github.com/users/jvillacorte/projects/1) | 3 of 4 | ✅ | 1 | none | none |
| G15 | ✅ [@Isaiah714's Sprint Board-1](https://github.com/users/Isaiah714/projects/4) | 1 of 4 | ✅ | 2 | none | none |
| G16 | ❌ none (README links github.com/users/garybs16/projects/2 but it isn't readable (private, or wrong URL)) | – | – | none | none | none |
| G17 | ❌ none | – | – | none | none | none |
| G18 | ✅ [CPSC490-G18-ProStrats](https://github.com/users/austin2578/projects/1) | 3 of 4 | ✅ | 8 | none | none |
| G19 | ❌ none (README links github.com/users/sopper75/projects/1 but it isn't readable (private, or wrong URL)) | – | – | none | none | none |
| G20 | ✅ [CPSC490-G20-Solos](https://github.com/users/muntay89/projects/2) | 16 of 16 | ✅ | 8 | none | none |

## Every group, by number

| Group | Project | Board | README | Status | Not tracked yet | Next step |
|---|---|---|---|---|---|---|
| G01 BGAF | Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting | 21 issues (1 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** | none | Merge open PRs #35/#36 into develop, convert the 18 bare #N links to typed [epic:#N](url) form, and add every open issue to the Sprint board (0 items now). |
| G02 Linux Larpers | Distributed Signal Capture for Multi-Node Analysis | 23 issues; epics, stories, points, Sprint 1 | matches | ⚠️ **Partial** | multi-node distribution and sync; Bluetooth capture; fingerprinting; localization; dashboard; active-recording detection | Finish §2 (#40/#41): goals and objectives for capture, fingerprinting, location and dashboard, file their epics and stories, and fix the #16/#17 parent loop. |
| G03 California | Three AIs and Literate Programming | 9 issues; points, Sprint 1 | matches | ⚠️ **Process only** | all five core elements; no feature issues exist | Write §2 (#17) with 2-3 goals and measurable objectives, then file one epic per goal and sp: stories for the three AI stages (recognize, generate code, compute/verify) in Sprint 2. |
| G04 Epic Engineers | Polygon Prediction Market PNL and Trader Profitability Analytics | 7 issues; points, Sprint 1 | matches | ⚠️ **Process only** | Trade parsing; Resolution matching; PNL computation; Trader ranking and edge analysis; Dashboard | Use the kickoff-notes scope (phase 1 proxy-wallet PNL, phase 2 EOA linking, client dashboard) to write §2 goals and objectives, file 2-3 epics with sp: stories in Sprint 2, and merge #21 so proposal.md replaces the template. |
| G05 Fighting Mongooses | WILS | 0 issues; no epics or stories | not yet | ❌ **No issues** | All core elements (no issues exist) | Run the bootstrap to create the missing epic/user-story/sp:/task labels, commit the real proposal into proposal/proposal.md and the team README, and file Sprint 1 tasks with sp: for each proposal section. |
| G06 Forecast Market Analytics | GapWise: An LLM Study Assistant with Adaptive Weak-Spot Tracking | 5 issues (1 new); epics, stories, Sprint 1 | matches | ⚠️ **Partial** | Answer checking and per-concept mastery tracker (the core idea) has no story issue; Assignment notifications/motivation; Evaluation vs non-adaptive baseline; Flashcards/summaries per subject | Create the missing story issues (stories 1.3, 1.4, 2.1-2.3 are only text in the epic bodies), add one for the weak-spot tracker, and give every story an sp: label in Sprint 1. |
| G07 Mighty Morphin | Online Material Database | 24 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** | none | Merge #30 so develop has the goals, convert the 16 links in proposal.md to typed references, add #28/#4/#1 or close them, and replace the course-template README with the project README. |
| G08 Crime Busters | Interactive Crime Map and Database | 33 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** | none | Add sp: labels to every story and unparented task in a Sprint milestone, close junk epics #6/#7, and fill the template placeholders in task bodies. |
| G09 Sigma Squad | Vehicle Maintenance Logger | 15 issues; points, Sprint 1 | n/a | ⚠️ **Process only** | Every product element; all 15 issues are proposal/setup writing tasks | Create epics for the 2-3 section 2 goals with stories for the objectives (record ingestion, recommendations, reminders), each story with sp: in a Sprint milestone. |
| G10 Team Jiddak | On-Chain Stablecoin Flow and Wash Trading Detection | 9 issues (1 new); epics, points, Sprint 1 | matches | ⚠️ **Partial** | Goal 2 epic and objectives 2.1-2.3; Goal 3 epic and objectives 3.1-3.3; Stories for objectives 1.1-1.3; Validation strategy | Create epics for Goals 2 and 3 and a user story per objective (1.1-3.3, section 2 text verbatim) with sp: in Sprint 1/2, and get them linked in proposal.md. |
| G11 5 Guys | Marathon Tracker | 11 issues; epics, points, Sprint 1 | not yet | ⚠️ **Partial** | ML analysis against public marathon data; Storing/reviewing run logs; Display route on map and calculate distance/elapsed/pace objectives (Goal 1 objectives have no stories); Goals 2-3 not yet written | Decide the core (individual GPS+ML analysis per the proposal, or live event tracking per epic #4 and meeting notes), then write Goal 1 objectives in proposal §2 and file one story per objective. |
| G12 ACJMM | Explainable 6G Waveform Classification | 17 issues (1 new); points, Sprint 1 | not yet | ⚠️ **Partial** | Peak detection and parameter estimation; GUI/CLI and interface control document; Explainability layer; Robustness/evaluation across channel conditions; No Goals/Objectives (§2) written, so no epics or stories | Write §2 Goals and Objectives, file one epic per goal and one story per objective (peak picking, parameter estimation, classifier baselines, GUI/CLI, explanation), and fill the README (title still TBD). |
| G13 BYKX | Assignment Motivation Initiative Year-Round Assistant | 24 issues; epics, stories, Sprint 1 | matches | ✅ **Aligned** | Platform choice is inconsistent: abstract/§3 say Windows desktop with Windows notifications, §4/§5 say Python+JS web app; issues #12/#13 assume web/HTTP and a "smart calendar" | Make each story title the §2 objective verbatim (drop the "Objective n.n:" prefix), replace the placeholder bodies (#17 epic and all 12 story bodies are still template text), and give each story its own sp: in a Sprint milestone. |
| G14 Cyber Squad | Rogue-Lite Cyber Sandbox | 4 issues; epics, points, Sprint 1 | not yet | ❌ **Mismatch** | Every core element; §2 Goals and Objectives is unwritten, so there are no stories to file | Agree on one project (the proposal is the Cyber Sandbox), commit the proposal text into proposal.md, write §2 goals, and replace the web scanner epic with epics and stories for the sandbox. |
| G15 HIBBI-01 | Low End Hardware ECS Game Engine with Game | 6 issues; epics, stories, points, Sprint 1 | not yet | ⚠️ **Partial** | ECS implementation; Game-creation interface / showcase game; Benchmarking and performance evaluation; Memory management; Story for closing the window (listed in epic #6, no issue) | Write §2 goals and objectives (rendering, ECS, game creation, benchmarking), then retitle #6 and #9 to match, file stories for the missing objectives, and stop committing directly to main (4 direct commits). |
| G16 Neuroprosthetic | BridgeWatch: Real-Time Detection of Cross-Chain Bridge Exploits | 21 issues (2 new); epics, stories, points, Sprint 1 | matches | ✅ **Aligned** | none | Convert the 21 bare issue links in proposal.md to typed references ([epic:#11](url), [story:#14](url), [task:#27](url)), then fix the Sprint board (README link is not readable) so every open issue is on it. |
| G17 Sonic Scape | SonicScape | 0 issues; no epics or stories | matches | ❌ **No issues** | Space-themed navigation UI; NASA API ingestion/parser; Music playback and music data source; Swipe rating; Preference profile / recommendation engine | Copy the abstract and introduction into proposal/proposal.md, write section 2, file Sprint 1 tasks with sp: for the five core systems (and open a Sprint board), link each from proposal.md as typed references, and open PRs into develop that close them. |
| G18 Team ProStrats | Project Rogue | 12 issues; epics, stories, Sprint 1 | matches | ⚠️ **Process only** | Class system; Weapon replacement / Mastery / affixes; Attributes, boons, respec; Branching route map and handcrafted rooms; Core combat and platforming; Playtest plan for build variety / meaningful decisions | Write proposal §2 with one objective per core system (classes, weapon Mastery, attributes/boons, branching rooms, combat, playtest measures), file each as a story under an epic titled verbatim from §2 with its own sp: and Sprint milestone, and link every issue from proposal.md as typed references. |
| G19 Titan Security | Radar over WiFi | 12 issues; epics, stories, points, Sprint 1 | not yet | ✅ **Aligned** | none | Stop committing to main: merge develop (with the linked proposal.md) to main through a PR, fill the README summary and team rows, and fill §4 so task #11 is cited there. |
| G20 Solos | Insomnia | 16 issues (16 new); epics, stories | matches | ✅ **Aligned** | Unpredictable monster placement/encounters (only distinct behaviors are tracked, not varied placement) | Write §2 in proposal.md with each goal and objective verbatim, cite all 8 stories there as typed references and the 5 tasks in §4, give the 8 stories sp: plus a Sprint 1 milestone, and add the project title to the proposal. |

## How to get to *Aligned*

Follow the course README, [§4 Epics and user stories on the issue board](https://github.com/kyoungshin/CPSC490#4-epics-and-user-stories-on-the-issue-board). In short:

1. Each **goal** in your proposal §2 *Goals and Objectives* is one **epic** issue (label `epic`). Its body lists its user stories as a task list (`- [ ] #12`).
2. Each **objective** under a goal is one **user story** issue (label `user-story`), **titled with the objective itself, in the exact words of proposal §2**: an action word plus what gets completed, with a number wherever possible. Not a feature name, and not a paraphrase. A user-story sentence goes in the issue body only when the objective has a real user, and it is optional.
3. Every story in a sprint has exactly one assignee, a `Sprint N` milestone, a `priority:` label and an `sp: N` label (1, 2, 3, 5, 8; `sp: 8` means split it). Points go on the objective only, never on the epic or the tasks under it. A writing task with no objective above it carries its own points.
4. Link every epic and story from proposal §2, and every other work item (feature, enhancement, bug, task, sub-task) from §4, each as a typed reference: `[epic:#1](https://github.com/OWNER/REPO/issues/1)`, `[story:#3](…)`, `[feature:#6](…)`, `[task:#5](…)`. Make the README on `main` say what the proposal says: title, sponsor code, and a one-paragraph summary.
5. A work item that isn't under a user story carries its own `sp:` points in a Sprint milestone. In Sprint 1, until your epics and stories exist, every issue is a task with `sp:` in Sprint 1.
6. Change the repository only through pull requests from a feature branch into `develop`, each closing an issue that proposal.md links. Document first, then workflow, then code.

*Group numbers are written GNN (G01–G20). Sponsor codes only; no mentor names. Earlier editions are in this file's git history.*
