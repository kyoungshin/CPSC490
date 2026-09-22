# Group repository readiness

**CPSC 490 · Fall 2026 · swept 22 Sep 2026, 19:11 UTC** (first sweep 18 Sep, 20:00 UTC). *Third edition today — an on-demand re-sweep an hour after the 18:20 UTC one.*

All 20 teams, ordered by group number. **Twelve repositories are ready. Five have problems. Three teams have no repository at all.** Three earlier failures traced to bugs in the course scaffold, since fixed — affected teams have instructor PRs open, so no team is blamed for them. This page is re-swept every morning.

### Since the last sweep (22 Sep, 18:20 UTC)

**Two movers, both upgrades — and both landed in the single hour between sweeps.** Group 04 (Epic Engineers) went from *no repository at all* to **ready** in one sitting: `Bryancostco/CPSC490-G04-EpicEngineers` was created at 18:25 UTC, correctly named, shared with write access, scaffolded cleanly and bootstrapped to completion (4 milestones, `develop`) — and the team filed **two** issues on the way in (#1, #3). Group 10 (Team Jiddak) ran bootstrap at 18:53 UTC (4 milestones, `develop`): from *partial* to **ready**; the scaffold internals duplicated at the repo root remain, now cosmetic only. Instructor PRs in G01/G02/G17/G20 remain unmerged; team-filed issues now **4** across three groups (G04 ×2, G11, G12).

**Notice (19 Sep):** proposal formatting rules are explicit in the scaffold (`proposal/proposal.md` + README) — template cover page unchanged, Times New Roman 11-pt, 1.5 spacing, 1.0-inch margins, template numbering/indentation exactly, Final Paper > 50 pages. Pre-19-Sep scaffold copies: read the course repo's copy.

**Still waiting:** instructor PRs open and green in **G01** (#2), **G02** (#1), **G17** (#1), **G20** (#1, #4) — none merged yet. Issues filed by teams across all 20 groups: **4** (G04's two setup issues, G11's project-brainstorm issue, G12's case-study-topic issue).

### Summary

| Count | Status |
|---:|---|
| **12** *(was 10)* | ✅ **Ready** — scaffold, bootstrap, CI green |
| **4** *(was 5)* | ⚠️ **Partial** — repo exists, setup incomplete |
| **1** *(was 1)* | ❌ **Empty or never shared** — nothing gradeable |
| **3** *(was 4)* | ⬜ **No repository** found anywhere |

> **Sprint 1 starts Sun 28 Sep** and runs to 11 Oct. First sprint reviews: **Tue 29 Sep** (§01) and **Thu 1 Oct** (§05). Issues filed *by teams* across all 20 groups so far: **4** — epics and user stories are the graded artifact, and none has been filed yet.

## Every group, by number

"Instructor PR" means a pull request is already open in that repo fixing a scaffold bug — the team only needs to review and merge it. Everything in the *What to do* column is the team's own next step. Even a *ready* repository has work to do: no team has filed a single epic or story yet — only three have filed any issue at all.

| Grp | Team | Repository | Status | What's wrong | What to do |
|---|---|---|---|---|---|
| 01 | BGAF | `LeDuy23/CPSC490-01-BGAF` | ✅ ready | Nothing blocking. Repo name reads `01` rather than `G01`. Instructor PR #2 still open. No team-filed issues. | Merge PR #2. File your epics and stories. Optionally rename to the `G01` form. |
| 02 | Linux Larpers | `eliThomass/CPSC490-G02-Linux-Larpers` | ✅ ready | Nothing blocking. Instructor PR #1 still open and green. No team-filed issues. | Merge PR #1, then file epics and stories. |
| 03 | California | `eccortes4/CPSC-490-G03-California` | ✅ ready | Created, shared, scaffolded and bootstrapped within hours on 20 Sep. Name uses `CPSC-490` rather than the `CPSC490` convention — cosmetic. No team-filed issues yet. | File epics and stories. Optionally rename to `CPSC490-G03-California`. |
| 04 | Epic Engineers | `Bryancostco/CPSC490-G04-EpicEngineers` | ✅ ready · 🆕 moved | Created 22 Sep at 18:25 UTC and done right the first time: correctly named, write access granted, scaffold copied cleanly (`.github/` intact), bootstrap complete (4 milestones, `develop`). Two team issues already filed (#1, #3). | File your epics and stories — the two setup issues are a good start. |
| 05 | Fighting Mongooses | `M-Kwatcher/CPSC490-G05-Fighting-Mongooses` | ✅ ready | New, correctly-named repo created 22 Sep with write access, scaffold and bootstrap complete — supersedes the old unshared `a-t-tran/CPSC490-Project`. No team-filed issues yet. | File epics and stories. |
| 06 | Forecast Market Analytics | `Joshbolus/CPSC490-G06-Forecast-Market-Analytics` | ✅ ready | Renamed, shared and scaffolded since the email. No team-filed issues yet. | File epics and stories. |
| 07 | Mighty Morphines | `CPSC490-Team-Proj/CPSC490-G7-MightyMorphin` | ✅ ready · 🆕 moved | Renamed off Group 03's number and bootstrapped to completion (4 milestones, `develop`) on 22 Sep — everything this row asked for. Name now reads `G7`, missing the leading zero — cosmetic. No team-filed issues yet. | File epics and stories. Optionally rename to `CPSC490-G07-Mighty-Morphines`. |
| 08 | Crime Busters | `miketruong91/CPSC490-G08-Crime-Busters` | ✅ ready | Created, named to convention, shared with write access, scaffolded and bootstrapped. No team-filed issues yet. | File epics and stories. |
| 09 | Sigma Squad | `TylerWard741/CPSC490-G9-SigmaSquad` | ❌ empty | **Zero commits.** Repo was created and the instructor added, but nothing has ever been pushed. Name missing the leading zero (`G9`). Unchanged. | Copy the scaffold and push, then run bootstrap. Rename to `G09`. |
| 10 | Team Jiddak | `Alexander-Sanchez2/CPSC490-G10-Team_Jiddak` | ✅ ready · 🆕 moved | Bootstrap run at 18:53 UTC on 22 Sep (4 milestones, `develop`) — the last blocking item. The re-copy's scaffold internals (`bootstrap.sh`, `ci.yml`, issue templates, example files, lecture slides) are still duplicated loose at the repo root — cosmetic now. No team-filed issues yet. | File epics and stories. Optionally delete the stray root-level duplicates. |
| 11 | 5 Guys | `markachavez2003-lab/CPSC490-G11-5Guys` | ✅ ready | Re-copied the scaffold (`.github/` now present) and re-ran bootstrap to completion (4 milestones, `develop`) on 20 Sep — the exact recovery this row prescribed. The team also filed the class's first issue. | File epics and stories. |
| 12 | ACJMM | `CharlesSinde/CPSC490-G12-ACJMM` | ✅ ready · 🆕 moved | Was empty since 3 Sep; scaffold pushed 19 Sep and bootstrap completed (4 milestones, `develop`, `.github/` present). Filed the class's second team issue on 22 Sep (#3, *Find Case Study Topic*). | File epics and stories. |
| 13 | BYKX | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 14 | Cyber Squad | `The-Cyber-Squad/CPSC490-G14-Cyber-Squad` | ⚠️ partial | Only `LICENSE` and `README.md` in the repo — **scaffold essentially not copied**. Also the only team that granted **read-only** access, so the instructor cannot open fix PRs here. Unchanged since 14 Sep. | Grant `kyoungshin` **write** access, copy the scaffold, run bootstrap. |
| 15 | HIBBI-01 | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 16 | Neuroprosthetic | `garybs16/CPSC490` | ✅ ready | Fully set up — 4 milestones, all labels, `develop`, harness present, new commits 22 Sep. **But the name is just `CPSC490`**, which identifies no group. No team-filed issues. | Rename to `CPSC490-G16-Neuroprosthetic`. Then file epics and stories. |
| 17 | Sonic Scape | `vibhorbh/CPSC490-G17-SonicScape` | ⚠️ partial | Was missing `proposal/proposal.md`, which failed two gates. Bootstrap never run. Instructor PR #1 restores the file and is green — still unmerged. | Merge PR #1, then run bootstrap. |
| 18 | Team ProStrats | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 19 | Titan Security | `sopper75/CPSC490-G19-TitanSecurity` | ⚠️ partial | New, correctly-named repo shared with write access on 20 Sep, scaffold copied including `.github/` — **bootstrap not run yet** (0 milestones, no `develop`). Supersedes the old unshared `23jdo5/CPSC-490-Capstone-Project`. | Run `bash scripts/bootstrap.sh` (see recipe below), then file epics and stories. |
| 20 | Solos | `muntay89/CPSC490-G20-California` | ⚠️ partial | **Team name is wrong: it reads California, which is Group 03.** They copied it from the naming example in QUICKSTART, which used a real team's name — the number is theirs and correct. Also had no `.github/`, so zero CI ever ran, and bootstrap was never run. Instructor PRs #1 and #4 still unmerged. | Merge instructor PRs #1 and #4, rename to `CPSC490-G20-Solos`, then run bootstrap. |

## The fixes

Four recipes cover every row above. All of them are run by the team, from inside their own repository.

### No repository yet — groups 13 · 15 · 18

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

### Scaffold missing or incomplete — groups 09 · 14 · 19 · 20 (03, 04, 05, 06, 07, 08, 10, 11 and 12 have done this)

Run the same copy command as above — it overwrites cleanly and, unlike dragging files from an unzipped download, it cannot lose the hidden `.github/` folder. Then complete the setup:

```bash
gh auth login                     # once
gh auth refresh -s project,repo   # needed for the board
bash scripts/bootstrap.sh

python .github/scripts/check_repo.py   # expect HARNESS GREEN
```

`bootstrap.sh` is safe to re-run and skips whatever already exists — Group 19 only needs this one command.

### Repo exists but was never shared — (no groups left — 03, 05, 06 and 19 have all done this)

Your work cannot be graded and no fix PRs can reach you until the instructor has access.

**Settings → Collaborators → Add people → `kyoungshin`**, with **write** permission. Group 14 granted read-only, which is not enough.

Then follow the scaffold recipe above.

### Repository needs renaming — groups 01 · 07 · 09 · 16 · 20

Only the repo **owner** can rename — the instructor cannot do this for you. Settings → General → Repository name.

Afterwards every teammate must re-point their local clone, or pushes will fail:

```bash
git remote set-url origin \
  https://github.com/<owner>/CPSC490-G<NN>-<TeamName>.git
git remote -v   # confirm
```

Group 16 is `CPSC490` with no group at all; Groups 07 and 09 are missing their leading zeros; Group 20 carries another team's name. Group 07 fixed the wrong group number on 22 Sep — it takes a minute.

---

*Re-swept 22 Sep 2026 (19:11 UTC — third edition today, on demand) against every repository the instructor can see, plus a public GitHub search for `CPSC490` and `CPSC-490` repos created since August (repos from earlier semesters are excluded); the first sweep was 18 Sep, 20:00 UTC. A private repository that has not added `kyoungshin` is invisible to both, so "no repository" means none was findable — not proof none exists. Group attributions for unshared repos are inferred from usernames, profile names and commit identities. Repos whose owner matches no enrolled student are excluded.*
