# Group repository readiness

**CPSC 490 · Fall 2026 · swept 23 Sep 2026, 15:36 UTC** (first sweep 18 Sep, 20:00 UTC). *Morning edition.*

All 20 teams, ordered by group number. **Fifteen repositories are ready. Four have problems. One team has no repository at all.** Three earlier failures traced to bugs in the course scaffold, since fixed — affected teams have instructor PRs open, so no team is blamed for them. This page is re-swept every morning.

### Since the last sweep (22 Sep, 19:11 UTC)

**The biggest overnight move yet — seven groups changed, every one an upgrade.** Group 09 (Sigma Squad) went from *empty* to **ready**: renamed to `G09`, full scaffold pushed, bootstrap complete (4 milestones, `develop`). Group 13 (BYKX) surfaced as **ready** — a private repo created 13 Sep that only became visible once `kyoungshin` was added, and it arrived fully scaffolded and bootstrapped. Group 19 (Titan Security) ran bootstrap: *partial* → **ready**. Group 15 (HIBBI-01) now has a repository, `Isaiah714/CPSC490-G15-HIBBI-01`, scaffolded and bootstrapped — but **not shared with the instructor**, so it lands as *partial* until `kyoungshin` is added with write access. Groups 01 and 02 merged their instructor PRs (#2 and #1). Groups 03 and 07 fixed their repo names (`CPSC490-G03-California`, `CPSC490-G07-MightyMorphin`), and Group 07 filed its first team issue. Team-filed issues now **5** across four groups (G04 ×2, G07, G11, G12).

**Notice (19 Sep):** proposal formatting rules are explicit in the scaffold (`proposal/proposal.md` + README) — template cover page unchanged, Times New Roman 11-pt, 1.5 spacing, 1.0-inch margins, template numbering/indentation exactly, Final Paper > 50 pages. Pre-19-Sep scaffold copies: read the course repo's copy.

**Notice (23 Sep):** the sprint schedule's **Homework #4 due date is Sun 4 Oct**, not 27 Sep — corrected in the course repo's `docs/sprint-schedule.md` (commit `6a12d4c`). Canvas has the authoritative dates; if your copy of the schedule says 27 Sep, it is the old one.

**Still waiting:** instructor PRs open and green in **G17** (#1) and **G20** (#1, #4). Issues filed by teams across all 20 groups: **5** (G04's two setup issues, G07's project-objectives issue, G11's project-brainstorm issue, G12's case-study-topic issue).

### Summary

| Count | Status |
|---:|---|
| **15** *(was 12)* | ✅ **Ready** — scaffold, bootstrap, CI green |
| **4** *(was 4)* | ⚠️ **Partial** — repo exists, setup incomplete or unshared |
| **0** *(was 1)* | ❌ **Empty or never shared** — nothing gradeable |
| **1** *(was 3)* | ⬜ **No repository** found anywhere |

> **Sprint 1 starts Sun 28 Sep** and runs to 11 Oct. First sprint reviews: **Tue 29 Sep** (§01) and **Thu 1 Oct** (§05). Issues filed *by teams* across all 20 groups so far: **5** — epics and user stories are the graded artifact, and none has been filed yet.

## Every group, by number

"Instructor PR" means a pull request is already open in that repo fixing a scaffold bug — the team only needs to review and merge it. Everything in the *What to do* column is the team's own next step. Even a *ready* repository has work to do: no team has filed a single epic or story yet — only four have filed any issue at all.

| Grp | Team | Repository | Status | What's wrong | What to do |
|---|---|---|---|---|---|
| 01 | BGAF | `LeDuy23/CPSC490-01-BGAF` | ✅ ready | Nothing blocking. Instructor PR #2 **merged** 23 Sep. Repo name reads `01` rather than `G01`. No team-filed issues. | File your epics and stories. Optionally rename to the `G01` form. |
| 02 | Linux Larpers | `eliThomass/CPSC490-G02-Linux-Larpers` | ✅ ready | Nothing blocking. Instructor PR #1 **merged** 22 Sep. No team-filed issues. | File epics and stories. |
| 03 | California | `eccortes4/CPSC490-G03-California` | ✅ ready | Created, shared, scaffolded and bootstrapped within hours on 20 Sep; **renamed to the `CPSC490` convention** overnight. No team-filed issues yet. | File epics and stories. |
| 04 | Epic Engineers | `Bryancostco/CPSC490-G04-EpicEngineers` | ✅ ready | Created 22 Sep and done right the first time: correctly named, write access granted, scaffold intact, bootstrap complete. Two team issues filed (#1, #3); new commits 23 Sep. | File your epics and stories — the two setup issues are a good start. |
| 05 | Fighting Mongooses | `M-Kwatcher/CPSC490-G05-Fighting-Mongooses` | ✅ ready | New, correctly-named repo created 22 Sep with write access, scaffold and bootstrap complete — supersedes the old unshared `a-t-tran/CPSC490-Project`. No team-filed issues yet. | File epics and stories. |
| 06 | Forecast Market Analytics | `Joshbolus/CPSC490-G06-Forecast-Market-Analytics` | ✅ ready | Renamed, shared and scaffolded since the email; new commits 23 Sep. No team-filed issues yet. | File epics and stories. |
| 07 | Mighty Morphines | `CPSC490-Team-Proj/CPSC490-G07-MightyMorphin` | ✅ ready · 🆕 moved | **Renamed to `G07`** (leading zero fixed) and filed the team's first issue (#1, project objectives) on 22 Sep. Bootstrap complete. | File epics and stories. |
| 08 | Crime Busters | `miketruong91/CPSC490-G08-Crime-Busters` | ✅ ready | Created, named to convention, shared with write access, scaffolded and bootstrapped. No team-filed issues yet. | File epics and stories. |
| 09 | Sigma Squad | `TylerWard741/CPSC490-G09-SigmaSquad` | ✅ ready · 🆕 moved | Was **empty** for nine days. Overnight: renamed to `G09`, full scaffold pushed (`.github/` intact), bootstrap complete (4 milestones, `develop`). No team-filed issues yet. | File epics and stories. |
| 10 | Team Jiddak | `Alexander-Sanchez2/CPSC490-G10-Team_Jiddak` | ✅ ready | Bootstrap complete 22 Sep. The re-copy's scaffold internals are still duplicated loose at the repo root — cosmetic. No team-filed issues yet. | File epics and stories. Optionally delete the stray root-level duplicates. |
| 11 | 5 Guys | `markachavez2003-lab/CPSC490-G11-5Guys` | ✅ ready | Re-copied the scaffold and re-ran bootstrap to completion on 20 Sep. Filed the class's first team issue. | File epics and stories. |
| 12 | ACJMM | `CharlesSinde/CPSC490-G12-ACJMM` | ✅ ready | Scaffold pushed 19 Sep, bootstrap complete. Filed a team issue on 22 Sep (#3, *Find Case Study Topic*). | File epics and stories. |
| 13 | BYKX | `ktnwin/CPSC490-G13-BYKX` | ✅ ready · 🆕 moved | **Found.** A private repo created 13 Sep, invisible until `kyoungshin` was added (with write access) — arrives fully scaffolded and bootstrapped (4 milestones, `develop`). No team-filed issues yet. | File epics and stories. |
| 14 | Cyber Squad | `The-Cyber-Squad/CPSC490-G14-Cyber-Squad` | ⚠️ partial | Only `LICENSE` and `README.md` in the repo — **scaffold essentially not copied**. Also granted only **read-only** access, so the instructor cannot open fix PRs here. Unchanged since 14 Sep. | Grant `kyoungshin` **write** access, copy the scaffold, run bootstrap. |
| 15 | HIBBI-01 | `Isaiah714/CPSC490-G15-HIBBI-01` | ⚠️ partial · 🆕 moved | **Repo exists (public, created 22 Sep), scaffolded and bootstrapped** (4 milestones, `develop`, `.github/` present) — but `kyoungshin` has **not been added as a collaborator**, so nothing here can be graded or fixed by PR yet. | **Settings → Collaborators → add `kyoungshin` with write access.** Then file epics and stories. |
| 16 | Neuroprosthetic | `garybs16/CPSC490` | ✅ ready | Fully set up — 4 milestones, all labels, `develop`, harness present. **But the name is just `CPSC490`**, which identifies no group. No team-filed issues. | Rename to `CPSC490-G16-Neuroprosthetic`. Then file epics and stories. |
| 17 | Sonic Scape | `vibhorbh/CPSC490-G17-SonicScape` | ⚠️ partial | Was missing `proposal/proposal.md`, which failed two gates. Bootstrap never run. Instructor PR #1 restores the file and is green — still unmerged. Unchanged since 18 Sep. | Merge PR #1, then run bootstrap. |
| 18 | Team ProStrats | — | ⬜ no repo | No repository found. **The only team with nothing findable.** | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 19 | Titan Security | `sopper75/CPSC490-G19-TitanSecurity` | ✅ ready · 🆕 moved | **Bootstrap run** overnight (4 milestones, `develop`) — the one item this row asked for. No team-filed issues yet. | File epics and stories. |
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

### Repo exists but was never shared — groups 15 (not shared) · 14 (read-only)

Your work cannot be graded and no fix PRs can reach you until the instructor has access.

**Settings → Collaborators → Add people → `kyoungshin`**, with **write** permission. Group 15's repo is otherwise complete — this one step makes it ready. Group 14 granted read-only, which is not enough.

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

*Re-swept 23 Sep 2026 (15:36 UTC, morning edition) against every repository the instructor can see, plus a public GitHub search for `CPSC490` and `CPSC-490` repos created since August (repos from earlier semesters are excluded); the first sweep was 18 Sep, 20:00 UTC. A private repository that has not added `kyoungshin` is invisible to both, so "no repository" means none was findable — not proof none exists (Group 13's repo existed for ten days before it became visible). Group attributions for unshared repos are inferred from usernames, profile names and commit identities. Repos whose owner matches no enrolled student are excluded.*
