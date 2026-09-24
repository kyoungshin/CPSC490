# Group repository readiness

**CPSC 490 · Fall 2026 · swept 24 Sep 2026, 15:36 UTC** (first sweep 18 Sep, 20:00 UTC).

All 20 teams, ordered by group number. **Sixteen repositories are ready. Three have problems. One team has no repository at all.** Three earlier failures traced to bugs in the course scaffold, since fixed — affected teams have instructor PRs open, so no team is blamed for them. This page is re-swept every morning.

### Since the last sweep (24 Sep, 03:30 UTC)

**No group moved.** No repository changed status, and none received a push in the twelve hours between sweeps. Team-filed issues are still **5** across five groups (G04 ×2, G07, G11, G12).

**Correction:** the last edition said no team had filed an epic yet. That was wrong — **Group 07's issue #1 (*project objectives*) is labeled `epic`** and is real project content, the class's first. Group 04's two issues also carry the `epic` label, but they are README setup tasks. No team has filed a user story yet.

*Evening, 23 Sep:* Group 15 shared its repository with the instructor and went *partial* → ready.

*Earlier (23 Sep morning):* seven groups moved overnight — G09 *empty* → ready, G13 surfaced ready, G19 bootstrapped, G15's repo appeared, G01/G02 merged their instructor PRs, G03/G07 fixed their repo names.

**Notice (19 Sep):** proposal formatting rules are explicit in the scaffold (`proposal/proposal.md` + README) — template cover page unchanged, Times New Roman 11-pt, 1.5 spacing, 1.0-inch margins, template numbering/indentation exactly, Final Paper > 50 pages. Pre-19-Sep scaffold copies: read the course repo's copy.

**Notice (23 Sep):** the sprint schedule's **Homework #4 due date is Sun 4 Oct**, not 27 Sep — corrected in the course repo's `docs/sprint-schedule.md` (commit `6a12d4c`). Canvas has the authoritative dates; if your copy of the schedule says 27 Sep, it is the old one.

**Still waiting:** instructor PRs open and green in **G17** (#1) and **G20** (#1, #4). Issues filed by teams across all 20 groups: **5** (G04's two setup issues, G07's project-objectives issue, G11's project-brainstorm issue, G12's case-study-topic issue).

### Summary

| Count | Status |
|---:|---|
| **16** *(was 16)* | ✅ **Ready** — scaffold, bootstrap, CI green |
| **3** *(was 3)* | ⚠️ **Partial** — repo exists, setup incomplete or unshared |
| **0** *(was 0)* | ❌ **Empty or never shared** — nothing gradeable |
| **1** *(was 1)* | ⬜ **No repository** found anywhere |

> **Sprint 1 starts Sun 28 Sep** and runs to 11 Oct. First sprint reviews: **Tue 29 Sep** (§01) and **Thu 1 Oct** (§05). Issues filed *by teams* across all 20 groups so far: **5**. Epics and user stories are the graded artifact: **one project epic exists (Group 07), and no user story has been filed by any team.**

## Every group, by number

"Instructor PR" means a pull request is already open in that repo fixing a scaffold bug — the team only needs to review and merge it. Everything in the *What to do* column is the team's own next step. Even a *ready* repository has work to do: only Group 07 has filed a project epic, no team has filed a user story, and only five groups have filed any issue at all.

| Grp | Team | Repository | Status | What's wrong | What to do |
|---|---|---|---|---|---|
| 01 | BGAF | `LeDuy23/CPSC490-01-BGAF` | ✅ ready | Nothing blocking. Instructor PR #2 **merged** 23 Sep. Repo name reads `01` rather than `G01`. No team-filed issues. | File your epics and stories. Optionally rename to the `G01` form. |
| 02 | Linux Larpers | `eliThomass/CPSC490-G02-Linux-Larpers` | ✅ ready | Nothing blocking. Instructor PR #1 **merged** 22 Sep. No team-filed issues. | File epics and stories. |
| 03 | California | `eccortes4/CPSC490-G03-California` | ✅ ready | Created, shared, scaffolded and bootstrapped within hours on 20 Sep; **renamed to the `CPSC490` convention** overnight. No team-filed issues yet. | File epics and stories. |
| 04 | Epic Engineers | `Bryancostco/CPSC490-G04-EpicEngineers` | ✅ ready | Created 22 Sep and done right the first time: correctly named, write access granted, scaffold intact, bootstrap complete. Two team issues filed (#1, #3); new commits 23 Sep. | File your epics and stories — the two setup issues are a good start. |
| 05 | Fighting Mongooses | `M-Kwatcher/CPSC490-G05-Fighting-Mongooses` | ✅ ready | New, correctly-named repo created 22 Sep with write access, scaffold and bootstrap complete — supersedes the old unshared `a-t-tran/CPSC490-Project`. No team-filed issues yet. | File epics and stories. |
| 06 | Forecast Market Analytics | `Joshbolus/CPSC490-G06-Forecast-Market-Analytics` | ✅ ready | Renamed, shared and scaffolded since the email; new commits 23 Sep. No team-filed issues yet. | File epics and stories. |
| 07 | Mighty Morphines | `CPSC490-Team-Proj/CPSC490-G07-MightyMorphin` | ✅ ready | **Renamed to `G07`** (leading zero fixed). Issue #1 (*project objectives*) is labeled `epic` — **the class's first project epic**. Bootstrap complete. | Break the epic into user stories. |
| 08 | Crime Busters | `miketruong91/CPSC490-G08-Crime-Busters` | ✅ ready | Created, named to convention, shared with write access, scaffolded and bootstrapped. No team-filed issues yet. | File epics and stories. |
| 09 | Sigma Squad | `TylerWard741/CPSC490-G09-SigmaSquad` | ✅ ready | Was **empty** for nine days; on 23 Sep: renamed to `G09`, full scaffold pushed (`.github/` intact), bootstrap complete (4 milestones, `develop`). No team-filed issues yet. | File epics and stories. |
| 10 | Team Jiddak | `Alexander-Sanchez2/CPSC490-G10-Team_Jiddak` | ✅ ready | Bootstrap complete 22 Sep. The re-copy's scaffold internals are still duplicated loose at the repo root — cosmetic. No team-filed issues yet. | File epics and stories. Optionally delete the stray root-level duplicates. |
| 11 | 5 Guys | `markachavez2003-lab/CPSC490-G11-5Guys` | ✅ ready | Re-copied the scaffold and re-ran bootstrap to completion on 20 Sep. Filed the class's first team issue. | File epics and stories. |
| 12 | ACJMM | `CharlesSinde/CPSC490-G12-ACJMM` | ✅ ready | Scaffold pushed 19 Sep, bootstrap complete. Filed a team issue on 22 Sep (#3, *Find Case Study Topic*). | File epics and stories. |
| 13 | BYKX | `ktnwin/CPSC490-G13-BYKX` | ✅ ready | **Found** 23 Sep. A private repo created 13 Sep, invisible until `kyoungshin` was added (with write access) — arrives fully scaffolded and bootstrapped (4 milestones, `develop`). No team-filed issues yet. | File epics and stories. |
| 14 | Cyber Squad | `The-Cyber-Squad/CPSC490-G14-Cyber-Squad` | ⚠️ partial | Only `LICENSE` and `README.md` in the repo — **scaffold essentially not copied**. Also granted only **read-only** access, so the instructor cannot open fix PRs here. Unchanged since 14 Sep. | Grant `kyoungshin` **write** access, copy the scaffold, run bootstrap. |
| 15 | HIBBI-01 | `Isaiah714/CPSC490-G15-HIBBI-01` | ✅ ready | **Shared with the instructor** (write access) on 23 Sep — the one step it was missing. Scaffolded and bootstrapped (4 milestones, `develop`, `.github/` present). No team-filed issues yet. | File epics and stories. |
| 16 | Neuroprosthetic | `garybs16/CPSC490` | ✅ ready | Fully set up — 4 milestones, all labels, `develop`, harness present. **But the name is just `CPSC490`**, which identifies no group. No team-filed issues. | Rename to `CPSC490-G16-Neuroprosthetic`. Then file epics and stories. |
| 17 | Sonic Scape | `vibhorbh/CPSC490-G17-SonicScape` | ⚠️ partial | Was missing `proposal/proposal.md`, which failed two gates. Bootstrap never run. Instructor PR #1 restores the file and is green — still unmerged. Unchanged since 18 Sep. | Merge PR #1, then run bootstrap. |
| 18 | Team ProStrats | — | ⬜ no repo | No repository found. **The only team with nothing findable.** | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 19 | Titan Security | `sopper75/CPSC490-G19-TitanSecurity` | ✅ ready | **Bootstrap run** 23 Sep (4 milestones, `develop`) — the one item this row asked for. No team-filed issues yet. | File epics and stories. |
| 20 | Solos | `muntay89/CPSC490-G20-California` | ⚠️ partial | **Team name is wrong: it reads California, which is Group 03.** They copied it from the naming example in QUICKSTART — the number is theirs and correct. Also has no `.github/`, so zero CI ever ran, and bootstrap was never run. Instructor PRs #1 and #4 still unmerged. Unchanged since 18 Sep. | Merge instructor PRs #1 and #4, rename to `CPSC490-G20-Solos`, then run bootstrap. |

## The fixes

Four recipes cover every row above. All of them are run by the team, from inside their own repository.

### No repository yet — group 18

Create a repo named `CPSC490-G<NN>-<TeamName>` — two digits, so sorting works. Then copy the scaffold and grant access:

```bash
# from inside your new, empty repo
git clone --depth 1 https://github.com/kyoungshin/CPSC490.git ../scaffold
(cd ../scaffold && git archive HEAD) | tar -x -C .
rm -rf ../scaffold

# VERIFY — all four must print, .github especially
ls -d .github .gitignore docs scripts

git add -A && git commit -m "chore: course scaffolding" && git push
```

Then Settings → Collaborators → add every teammate *and* `kyoungshin`.

### Scaffold missing or incomplete — groups 14 · 17 · 20 (03–13 and 19 have all done this)

Run the same copy command as above — it overwrites cleanly and, unlike dragging files from an unzipped download, it cannot lose the hidden `.github/` folder. Then complete the setup:

```bash
gh auth login                     # once
gh auth refresh -s project,repo   # needed for the board
bash scripts/bootstrap.sh

python .github/scripts/check_repo.py   # expect HARNESS GREEN
```

`bootstrap.sh` is safe to re-run and skips whatever already exists — Group 17 only needs to merge PR #1 and run this one command.

### Instructor access is read-only — group 14

Your work cannot be graded and no fix PRs can reach you until the instructor has write access.

**Settings → Collaborators → `kyoungshin` → change role to write.** Read-only is not enough. (Group 15 did exactly this on 23 Sep and went straight to ready.)

### Repository needs renaming — groups 01 · 16 · 20

Only the repo **owner** can rename — the instructor cannot do this for you. Settings → General → Repository name.

Afterwards every teammate must re-point their local clone, or pushes will fail:

```bash
git remote set-url origin \
  https://github.com/<owner>/CPSC490-G<NN>-<TeamName>.git
git remote -v   # confirm
```

Group 16 is `CPSC490` with no group at all; Group 01 is missing the `G`; Group 20 carries another team's name. Groups 03, 07 and 09 all renamed this week — it takes a minute.

---

*Re-swept 24 Sep 2026 (15:36 UTC) against every repository the instructor can see, plus a public GitHub search for `CPSC490` and `CPSC-490` repos created since August (repos from earlier semesters are excluded); the first sweep was 18 Sep, 20:00 UTC. A private repository that has not added `kyoungshin` is invisible to both, so "no repository" means none was findable — not proof none exists (Group 13's repo existed for ten days before it became visible). Group attributions for unshared repos are inferred from usernames, profile names and commit identities. Repos whose owner matches no enrolled student are excluded.*
