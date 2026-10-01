# Group repository readiness

**CPSC 490 · Fall 2026 · swept 1 Oct 2026, 23:25 UTC** (first sweep 18 Sep, 20:00 UTC).

All 20 teams, ordered by group number. **Sixteen repositories are ready; four are partial** (Groups 12, 13, 15 and 19 — see below). Four failures so far traced to bugs in the course scaffold, the fourth found today; all are fixed and no team is blamed for them. **Every group except 19 has an instructor pull request open: merge it.** During sprints this page is re-swept every Tuesday and Thursday at noon (Pacific).

### Since the last sweep (1 Oct, 19:41 UTC)

**A fourth scaffold bug, and it was the instructor's.** Groups 03, 05, 08 and 18 have had a **red `Repository harness` on `develop` since their first push**. The course guide, which the copy step brings in as your `README.md`, linked `docs/sponsored-projects.md` with a relative path. That page is left out of the team copy, so gate G4 failed on a link you never wrote. **No team is blamed.** It is fixed upstream (commit `27186ef`), and the course repository now runs the harness on exactly what a team copies, so it cannot happen again. The one-line fix is in each team's open instructor PR: **G03 #7, G05 #2, G08 #2, G18 #4, all green. Merge it.**

**New course rule: writing tasks carry story points.** A proposal-writing task with no parent story gets its own `sp:` label ([First Steps guide, Step 3.2](https://kyoungshin.github.io/CPSC490/first-steps.html)). Tasks filed under an objective stay unpointed. `scripts/sprint_report.py` now names unpointed writing tasks. **Every group except 19 has an instructor PR that brings in the updated script. Merge it:** G01 #17 · G02 #27 · G03 #7 · G04 #8 · G05 #2 · G06 #2 · G07 #3 · G08 #2 · G09 #2 · G10 #2 · G11 #16 · G12 #14 · G13 #29 · G15 #2 · G16 #8 · G17 #4 · G18 #4 · G20 #7. Group 14 merged its PR (#11) within the hour.

**Four groups went ready → partial:**
- **Groups 12 and 13: the branch ruleset blocks every branch.** Both rulesets are named for `main` and `develop`, but their *Target branches* is set to **All branches**, so no one can push any branch, feature branches included. The setup guide never said how to fill in that field; it does now (commit `d08d532`). Because of this, their instructor PRs (#14, #29) had to come from a fork and show no CI. **Fix (team leader):** Settings → Rules → Rulesets → open the ruleset → *Target branches* → remove *All branches* → *Add target* → *Include by pattern* → `main`, then again → `develop` → Save.
- **Group 19: GitHub Issues are turned off** in the repository's settings, so the team cannot file the epics and stories due by 11 Oct. Earlier editions read this as "no team-filed issues yet", which was a misread. **Fix (repository owner `sopper75`):** Settings → General → Features → tick **Issues**.
- **Group 15: no `proposal/` folder** on `develop`, so harness gate G1 is red. Copy `proposal/` from the course scaffold (the *Scaffold missing* recipe below).

**Group 13 (BYKX) filed the class's largest backlog:**
- three project epics, #16–#18 (*Goal 1–3*: assignment management, deadlines, progress tracking and reminders);
- twelve user stories (#19–#27, #31–#33);
- a process epic, #30 *Goal 0*, with its stories and tasks in Sprint 1.

The project stories carry no `sp:` points yet.

**Group 12 (ACJMM) filed twelve unlabeled issues: six titles, each filed twice.** #8–#13 and #15–#20 are both *Peak Picking*, *GUI Development*, *Command Line interface/ICD Dev*, *Waveform Identification Algorithm*, *Explainable AI Layer* and *Modulation Type Classifier Re-Training*. Close one copy of each, then label the rest: `epic` for goals, `user-story` for objectives.

**Group 04 (Epic Engineers)** filed proposal-writing tasks with story points (#10 `sp: 1`, #11 `sp: 3`) and a research sub-task (#12), all in Sprint 1. **Group 11** added two more writing tasks (#13, #17).

**Groups 06–10 (4 PM check):**
- no commits on `main` or `develop` since Sprint 1 began (28 Sep);
- no pull requests;
- every `proposal/proposal.md` is still the untouched template;
- only Group 07 has an issue (#1, `epic`).

**HW#4 (§0 Abstract and §1 Introduction, written in `proposal.md`) is due Sun 4 Oct.**

**Class totals:**
- Team-filed issues: **87** (was 53), from eleven groups.
- Groups using the **Sprint 1** milestone: **9** — 02, 03, 04, 11, 12, 13, 14, 16, 18.
- Groups with story points on their issues: **5** — 02, 03, 04, 14, 16.
- Graded artifact (labels): project epics from **Groups 02, 07, 11, 13 and 14**; user stories from **Groups 02 (six), 13 (twelve) and 16 (one)**.
- **Nine groups have filed nothing yet**: 05, 06, 08, 09, 10, 15, 17, 19, 20. Group 19 cannot until Issues are turned on.

**Goals & Objectives lock Sun 11 Oct** (end of Sprint 1): every group's epics and user stories should be filed by then.

*Earlier (1 Oct, 19:41 UTC edition):*

**Group 02 (Linux Larpers) built the class's first full sprint backlog.** It filed 17 issues:
- an epic, #20 *Goal 0: Submit a complete, reviewed CPSC 490 proposal*;
- five user stories for the proposal sections (#21–#25, *Objective 0.1–0.5*), each with story points;
- a prototype user story, #16 *Objective 1.1 (Prototype): Demonstrate Wi-Fi access point discovery and metadata collection through a runnable backend*, with its tasks #17 and #18;
- writing and setup tasks.

The proposal-section stories and their tasks sit in the **Sprint 1** milestone, and the prototype story in Sprint 2.

**Group 11 (5 Guys) filed its first epic**, #4 *Live runner tracking*, plus proposal-writing tasks (#3, #7, #8, #9) and two meeting issues — all in Sprint 1.

**Group 12 (ACJMM) filed three issues labeled `epic`**: #4 *Assign Project Tasks to Team Members*, #5 *Create Basic System Design Diagrams (UML Diagram)*, #6 *Collect Requirements for Respective Tasks*. These read as process tasks rather than project goals.

**Group 13 (BYKX) filed its first six issues**: proposal tasks (#10 README, #11 proposal draft, #15 §1.1) and design tasks (#8 backend framework, #12 frontend framework, #13 data model diagram).

**Group 01 (BGAF) renamed to the convention** — `LeDuy23/CPSC490-01-BGAF` → `LeDuy23/CPSC490-G01-BGAF` (same repository; the old address redirects) — and filed six issues: five proposal and research tasks (#9, #10, #12, #13, #14) and a mentor meeting (#11).

**Group 18 (Team ProStrats)** filed its first team issue, #2 *Set up Team ProStrats project README*.

**Class totals:**
- Team-filed issues: **53** (was 13), from eleven groups.
- Groups using the **Sprint 1** milestone: **8** — 02, 03, 11, 12, 13, 14, 16, 18.
- Groups with story points on their issues: **4** — 02, 03, 14, 16.
- Graded artifact (labels): project epics from **Groups 02, 07, 11 and 14**; process tasks labeled `epic` from Groups 04 and 12; user stories from **Groups 02 (six) and 16 (one)**.
- **Nine groups have filed nothing yet**: 05, 06, 08, 09, 10, 15, 17, 19, 20.

**Goals & Objectives lock Sun 11 Oct** (end of Sprint 1): every group's epics and user stories should be filed by then.

*Earlier (29 Sep, 19:43 UTC edition):*

### Since the 27 Sep, 16:42 UTC edition

**Group 20 (Solos) went *partial* → ready — every team is now ready.** Renamed `muntay89/CPSC490-G20-California` → `muntay89/CPSC490-G20-Solos` (same repository; the old address redirects), merged instructor PRs #1 and #4 (`.github/` now present), and ran bootstrap (4 milestones, `develop`) — all three items this page asked for.

**Group 16 (Neuroprosthetic) filed the class's first user story** — issue #5, *Prototype v0: BridgeWatch bridge-drain detection on live Ethereum data*, labeled `user-story`, `priority: high`, 8 story points.

**Group 03 (California) filed three proposal-writing tasks** — #2 *Update README*, #4 *First draft of Abstract*, #5 *Introduction (up to related work)* — labeled `documentation` with story points. Team-filed issues across the class: **13** (was 9), from seven groups.

**Sprint 1 is under way** (28 Sep – 11 Oct; reviews Tue 29 Sep §01 and Thu 1 Oct §05). Graded artifact so far: **two project epics (Groups 07 and 14) and one user story (Group 16)** — the other 17 groups have none yet.

*Earlier (27 Sep, 16:42 UTC edition):*

**Group 03 (California) filed its first team issue** — #1, *Meeting #1 - 9/26/26* (no labels yet). Team-filed issues across the class: **9** (was 8), from six groups.

No other group changed status. Group 20 is still the only *partial* repository.

**Sprint 1 starts tomorrow (Sun 28 Sep).** Sprint reviews Tue 29 Sep (§01) and Thu 1 Oct (§05) look at epics and user stories — two project epics exist class-wide (Groups 07 and 14) and **no team has filed a user story yet**.

*Earlier (25 Sep, 03:54 UTC edition):*

**Group 17 (Sonic Scape) went *partial* → ready.** Bootstrap ran this evening (4 milestones, `develop`) — the one step it had left.

**Group 18 (Team ProStrats) went *partial* → ready.** Renamed `490ProjectRogue` → `austin2578/CPSC490-G18-ProStrats` (same repository; the old address redirects), copied the full scaffold (`.github/` intact) and ran bootstrap (4 milestones, `develop`) — all three items this page asked for, within hours of being found.

**Group 16 (Neuroprosthetic) renamed** `garybs16/CPSC490` → `garybs16/CPSC490-G16-Neuroprosthetic` (same repository). It was already ready; now its name identifies the group.

**Group 14 filed the class's second project epic** — issue #8, *Create web scanner*, labeled `epic`. Team-filed issues across the class: **8** (was 7).

*Evening, 24 Sep (23:08 UTC):*

Group 18's repository was found (then named `490ProjectRogue`, README only), so for the first time **all 20 teams had a findable repository**.

Group 17 merged instructor PR #1 (restores `proposal/proposal.md`).

Group 14 filed two team issues (#4 *CODEOWNERS*, #6 *sync develop with main*).

**Sponsored projects (24–25 Sep, all 9 filled):** Raytheon selected four teams — **G02 → RTX-4** *Distributed Signal Capture for Multi-Node Analysis*, **G03 → RTX-3** *Three AIs and Literate Programming*, **G12 → RTX-1** *Explainable 6G Waveform Classification*, **G19 → RTX-2** *Radar Over WiFi (ROW)*. **G07** already has Edwards **EL-1** *Online Materials Database*. SonarX selected four — **G01 → SNX-4** *Hyperliquid Order Book Reconstruction and Algorithmic Strategy Backtesting*, **G04 → SNX-1** *Polygon Prediction Market PNL and Trader Profitability Analytics*, **G10 → SNX-2** *On-Chain Stablecoin Flow and Wash Trading Detection*, **G16 → SNX-3** *Cross-Chain Bridge Activity and Exploit Detection*. Every other group runs its own project.

*Midday, 24 Sep:* **Group 14 (Cyber Squad) went *partial* → ready.** The repository moved from the `The-Cyber-Squad` organization to `jvillacorte/CPSC490-G14-Cyber-Squad` (same repo; the old address redirects), and at 16:37 UTC the team granted `kyoungshin` **write** access, copied the full scaffold (`.github/` intact) and ran bootstrap (4 milestones, `develop`) — all three items this page asked for.

*Morning, 24 Sep:* no group moved overnight.

**Correction (24 Sep morning):** the last edition said no team had filed an epic yet. That was wrong — **Group 07's issue #1 (*project objectives*) is labeled `epic`** and is real project content, the class's first. Group 04's two issues also carry the `epic` label, but they are README setup tasks. No team has filed a user story yet.

*Evening, 23 Sep:* Group 15 shared its repository with the instructor and went *partial* → ready.

*Earlier (23 Sep morning):* seven groups moved overnight — G09 *empty* → ready, G13 surfaced ready, G19 bootstrapped, G15's repo appeared, G01/G02 merged their instructor PRs, G03/G07 fixed their repo names.

**Notice (19 Sep):** proposal formatting rules are explicit in the scaffold (`proposal/proposal.md` + README) — template cover page unchanged, Times New Roman 11-pt, 1.5 spacing, 1.0-inch margins, template numbering/indentation exactly, Final Paper > 50 pages. Pre-19-Sep scaffold copies: read the course repo's copy.

**Notice (23 Sep):** the sprint schedule's **Homework #4 due date is Sun 4 Oct**, not 27 Sep — corrected in the course repo's `docs/sprint-schedule.md` (commit `6a12d4c`). Canvas has the authoritative dates; if your copy of the schedule says 27 Sep, it is the old one.

**Still waiting:** no instructor PRs are open anywhere. Issues filed by teams across all 20 groups: **53**, from eleven groups (01, 02, 03, 04, 07, 11, 12, 13, 14, 16, 18). Nine groups have filed none: 05, 06, 08, 09, 10, 15, 17, 19, 20.

### Summary

| Count | Status |
|---:|---|
| **16** *(was 20)* | ✅ **Ready** — scaffold, bootstrap, CI green (or green once the instructor PR is merged) |
| **4** *(was 0)* | ⚠️ **Partial** — repo exists, setup incomplete, or a setting blocks the work (12, 13, 15, 19) |
| **0** *(was 0)* | ❌ **Empty or never shared** — nothing gradeable |
| **0** *(was 0)* | ⬜ **No repository** found anywhere |

> **Sprint 1 runs Sun 28 Sep – Sun 11 Oct; Goals & Objectives lock on the 11th.** Issues filed *by teams* across all 20 groups so far: **87**. Epics and user stories are the graded artifact:
> - project epics from **Groups 02, 07, 11, 13 and 14**;
> - user stories from **Groups 02, 13 and 16** only;
> - **nine groups have filed nothing**.

## Every group, by number

Everything in the *What to do* column is the team's own next step. For most groups the work now is the sprint backlog:
- **Project epics:** Groups 02, 07, 11, 13 and 14.
- **User stories:** Groups 02, 13 and 16 only.
- **Any issue at all:** eleven groups.
- **Open instructor PR to merge:** every group except 14 (merged) and 19.

| Grp | Team | Repository | Status | What's wrong | What to do |
|---|---|---|---|---|---|
| 01 | BGAF | `LeDuy23/CPSC490-G01-BGAF` | ✅ ready | Instructor PR #2 **merged** 23 Sep. **Renamed to the `G01` form** 30 Sep–1 Oct. Filed six issues: five proposal and research tasks (#9, #10, #12, #13, #14) and a mentor meeting (#11). | **Merge instructor PR #17.** Turn the proposal's goals into an epic and user stories; put Sprint 1 work in the Sprint 1 milestone. |
| 02 | Linux Larpers | `eliThomass/CPSC490-G02-Linux-Larpers` | ✅ ready | **The class's first full sprint backlog** (17 issues). It has a proposal epic (#20), five proposal-section user stories with story points (#21–#25) and a prototype user story (#16) with tasks (#17, #18). It uses the Sprint 1 and Sprint 2 milestones. | **Merge instructor PR #27.** Add the project's other goals as epics, each broken into stories. |
| 03 | California | `eccortes4/CPSC490-G03-California` | ✅ ready | Harness red on `develop` since the first push — **the instructor's bug**, not yours (relative link to a course-only page). Created, shared, scaffolded and bootstrapped within hours on 20 Sep; **renamed to the `CPSC490` convention** overnight. Filed four team issues — meeting notes (#1) and three proposal-writing tasks with story points (#2, #4, #5). | **Merge instructor PR #7** (fixes the harness and updates the sprint report). Then file the project's epics and user stories alongside the proposal tasks. |
| 04 | Epic Engineers | `Bryancostco/CPSC490-G04-EpicEngineers` | ✅ ready | Created 22 Sep and done right the first time: correctly named, write access granted, scaffold intact, bootstrap complete. Two team issues filed (#1, #3); on 1 Oct added proposal-writing tasks with story points (#10 `sp: 1`, #11 `sp: 3`) and a research sub-task (#12), all in Sprint 1. | **Merge instructor PR #8.** Then turn the proposal's goals into epics and user stories. |
| 05 | Fighting Mongooses | `M-Kwatcher/CPSC490-G05-Fighting-Mongooses` | ✅ ready | Harness red on `develop` since the first push — **the instructor's bug**, not yours. New, correctly-named repo created 22 Sep with write access, scaffold and bootstrap complete — supersedes the old unshared `a-t-tran/CPSC490-Project`. No team-filed issues yet. | **Merge instructor PR #2** (fixes the harness). File epics and stories. |
| 06 | Forecast Market Analytics | `Joshbolus/CPSC490-G06-Forecast-Market-Analytics` | ✅ ready | Renamed, shared and scaffolded since the email; last commit 19 Sep. **4 PM check, 1 Oct:** no commits since Sprint 1 began, no PRs, `proposal.md` is the untouched template, no team-filed issues. | **Merge instructor PR #2.** Start HW#4 in `proposal.md` (due Sun 4 Oct); file epics and stories. |
| 07 | Mighty Morphines | `CPSC490-Team-Proj/CPSC490-G07-MightyMorphin` | ✅ ready | **Renamed to `G07`** (leading zero fixed). Issue #1 (*project objectives*) is labeled `epic` — **the class's first project epic**. Bootstrap complete. **4 PM check, 1 Oct:** no commits since Sprint 1 began, no PRs, `proposal.md` is the untouched template. | **Merge instructor PR #3.** Start HW#4 in `proposal.md` (due Sun 4 Oct); break the epic into user stories. |
| 08 | Crime Busters | `miketruong91/CPSC490-G08-Crime-Busters` | ✅ ready | Harness red on `develop` since the first push — **the instructor's bug**, not yours. **4 PM check, 1 Oct:** no commits since Sprint 1 began, `proposal.md` untouched. Created, named to convention, shared with write access, scaffolded and bootstrapped. No team-filed issues yet. | **Merge instructor PR #2** (fixes the harness). Start HW#4 in `proposal.md` (due Sun 4 Oct); file epics and stories. |
| 09 | Sigma Squad | `TylerWard741/CPSC490-G09-SigmaSquad` | ✅ ready | Was **empty** for nine days; on 23 Sep: renamed to `G09`, full scaffold pushed (`.github/` intact), bootstrap complete (4 milestones, `develop`). **4 PM check, 1 Oct:** no commits since Sprint 1 began, `proposal.md` untouched, no team-filed issues. | **Merge instructor PR #2.** Start HW#4 in `proposal.md` (due Sun 4 Oct); file epics and stories. |
| 10 | Team Jiddak | `Alexander-Sanchez2/CPSC490-G10-Team_Jiddak` | ✅ ready | Bootstrap complete 22 Sep. The re-copy's scaffold internals are still duplicated loose at the repo root — cosmetic. **4 PM check, 1 Oct:** no commits since Sprint 1 began, `proposal.md` untouched, no team-filed issues — the only sponsored team (SNX-2) with nothing filed. | **Merge instructor PR #2.** Start HW#4 in `proposal.md` (due Sun 4 Oct); file epics and stories. Optionally delete the stray root-level duplicates. |
| 11 | 5 Guys | `markachavez2003-lab/CPSC490-G11-5Guys` | ✅ ready | Re-copied the scaffold and re-ran bootstrap to completion on 20 Sep. Filed the class's first team issue; on 30 Sep–1 Oct added **epic #4 *Live runner tracking***, proposal-writing tasks (#3, #7–#9) and meeting issues, all in Sprint 1. | **Merge instructor PR #16.** Break the epic into user stories with story points. |
| 12 | ACJMM | `CharlesSinde/CPSC490-G12-ACJMM` | ⚠️ partial | **Ruleset targets *All branches***, so no branch can be pushed (instructor PR #14 came from a fork). On 1 Oct filed twelve unlabeled issues — six titles, each twice (#8–#13 = #15–#20). Scaffold pushed 19 Sep, bootstrap complete. Filed a team issue on 22 Sep (#3, *Find Case Study Topic*), then three issues labeled `epic` (#4–#6). Those three are team process tasks rather than project goals. | **Team leader:** set the ruleset's *Target branches* to `main` and `develop` only. Close the duplicate issues; label goals `epic` and objectives `user-story`. Merge PR #14. |
| 13 | BYKX | `ktnwin/CPSC490-G13-BYKX` | ⚠️ partial | **Ruleset targets *All branches***, so no branch can be pushed (instructor PR #29 came from a fork). On 1 Oct filed **the class's largest backlog**: project epics #16–#18, twelve user stories, and a Sprint 1 process epic #30. **Found** 23 Sep. A private repo created 13 Sep, invisible until `kyoungshin` was added (with write access) — arrives fully scaffolded and bootstrapped (4 milestones, `develop`). Filed its first six issues on 30 Sep–1 Oct: proposal tasks (#10, #11, #15) and design tasks (#8, #12, #13). | **Team leader:** set the ruleset's *Target branches* to `main` and `develop` only. Add `sp:` points to the user stories. Merge PR #29. |
| 14 | Cyber Squad | `jvillacorte/CPSC490-G14-Cyber-Squad` | ✅ ready | **Fixed everything on 24 Sep:** moved from the `The-Cyber-Squad` organization (old address redirects), granted `kyoungshin` **write** access, copied the full scaffold (`.github/` intact) and ran bootstrap (4 milestones, `develop`). Filed two repo-maintenance issues on 24 Sep (#4, #6), then **issue #8, *Create web scanner*, labeled `epic` — the class's second project epic.** | Break the epic into user stories. |
| 15 | HIBBI-01 | `Isaiah714/CPSC490-G15-HIBBI-01` | ⚠️ partial | **No `proposal/` folder on `develop`**, so harness gate G1 is red. **Shared with the instructor** (write access) on 23 Sep — the one step it was missing. Scaffolded and bootstrapped (4 milestones, `develop`, `.github/` present). No team-filed issues yet. | Copy `proposal/` from the course scaffold (recipe below). Merge instructor PR #2. File epics and stories. |
| 16 | Neuroprosthetic | `garybs16/CPSC490-G16-Neuroprosthetic` | ✅ ready | Fully set up — 4 milestones, all labels, `develop`, harness present. **Renamed to the convention 24 Sep** (was just `CPSC490`). **Filed the class's first user story** 29 Sep (#5, *Prototype v0: BridgeWatch…*, 8 points). | **Merge instructor PR #8.** Group the story under a project epic, and keep splitting v0 into stories. |
| 17 | Sonic Scape | `vibhorbh/CPSC490-G17-SonicScape` | ✅ ready | Merged instructor PR #1 on 24 Sep, then **ran bootstrap** the same evening (4 milestones, `develop`). No team-filed issues yet. | **Merge instructor PR #4.** File epics and stories. |
| 18 | Team ProStrats | `austin2578/CPSC490-G18-ProStrats` | ✅ ready | Harness red on `develop` since the first push — **the instructor's bug**, not yours. Found 24 Sep as a README-only repo; the same evening **renamed to the convention, copied the full scaffold (`.github/` intact) and ran bootstrap** (4 milestones, `develop`). Filed its first team issue on 1 Oct (#2, *Set up Team ProStrats project README*). | **Merge instructor PR #4** (fixes the harness). File epics and stories. |
| 19 | Titan Security | `sopper75/CPSC490-G19-TitanSecurity` | ⚠️ partial | **Bootstrap run** 23 Sep (4 milestones, `develop`) — the one item this row asked for. **GitHub Issues are turned off** in the repository's settings, so no issue can be filed. Earlier editions misread this as "no team-filed issues yet". | **Owner `sopper75`:** Settings → General → Features → tick **Issues**. Then file epics and stories before 11 Oct. |
| 20 | Solos | `muntay89/CPSC490-G20-Solos` | ✅ ready | **Fixed everything 27–29 Sep:** renamed from `…-California` to its own team name, merged instructor PRs #1 and #4 (`.github/` present), and ran bootstrap (4 milestones, `develop`). No team-filed issues yet. | **Merge instructor PR #7.** File epics and stories. |

## The fixes

Every group has now completed setup. These recipes are kept for reference (a new teammate's clone, or a re-run), and all are run by the team from inside their own repository.

### Scaffold missing

From inside your repository, copy the scaffold (repos are named `CPSC490-G<NN>-<TeamName>` — two digits, so sorting works):

```bash
# from inside your repo
git clone --depth 1 https://github.com/kyoungshin/CPSC490.git ../scaffold
(cd ../scaffold && git archive HEAD) | tar -x -C .
rm -rf ../scaffold

# VERIFY — all four must print, .github especially
ls -d .github .gitignore docs scripts

git add -A && git commit -m "chore: course scaffolding" && git push
```

Make sure every teammate *and* `kyoungshin` are collaborators (Settings → Collaborators).

### Complete the setup (all 20 groups have done this)

Run the same copy command as above — it overwrites cleanly and, unlike dragging files from an unzipped download, it cannot lose the hidden `.github/` folder. Then complete the setup:

```bash
gh auth login                     # once
gh auth refresh -s project,repo   # needed for the board
bash scripts/bootstrap.sh

python .github/scripts/check_repo.py   # expect HARNESS GREEN
```

`bootstrap.sh` is safe to re-run and skips whatever already exists.

### Repository needs renaming

Only the repo **owner** can rename — the instructor cannot do this for you. Settings → General → Repository name.

Afterwards every teammate must re-point their local clone, or pushes will fail:

```bash
git remote set-url origin \
  https://github.com/<owner>/CPSC490-G<NN>-<TeamName>.git
git remote -v   # confirm
```

Every group now follows the naming convention; Group 01 was the last to rename (1 Oct).

---

*Re-swept 1 Oct 2026 (19:41 UTC) against every repository the instructor can see, plus a public GitHub search for `CPSC490` and `CPSC-490` repos created since August (repos from earlier semesters are excluded); the first sweep was 18 Sep, 20:00 UTC. A private repository that has not added `kyoungshin` is invisible to both, so "no repository" means none was findable — not proof none exists (Group 13's repo existed for ten days, and Group 18's for eleven, before becoming visible). Group attributions for unshared repos are inferred from usernames, profile names and commit identities. Repos whose owner matches no enrolled student are excluded.*
