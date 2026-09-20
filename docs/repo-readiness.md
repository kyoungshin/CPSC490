# Group repository readiness

**CPSC 490 · Fall 2026 · swept 20 Sep 2026, 02:54 UTC** (first sweep 18 Sep, 20:00 UTC)

All 20 teams, ordered by group number. **Six repositories are ready. Nine have problems. Five teams have no repository at all.** Three earlier failures traced to bugs in the course scaffold, since fixed — affected teams have instructor PRs open, so no team is blamed for them. This page is re-swept every morning.

### Since the last sweep (19 Sep, 23:48 UTC)

**Group 03 (California) appeared.** `eccortes4/CPSC-490-G03-California` was created and shared with the instructor (write access) minutes before this sweep — from *no repository* to *partial*: the scaffold (including `.github/`) is not copied yet and bootstrap has not run. Next: the scaffold recipe below. Yesterday's movers (G08 created→ready, G12 empty→ready) hold.

**New course-repo requirement, posted 19 Sep:** the proposal's formatting rules are now explicit in the scaffold (`proposal/proposal.md` + README): the template's **cover page unchanged**, **Times New Roman 11-point**, **1.5 line spacing**, **1.0-inch margins**, the template's **section numbering and indentation exactly**, and the **Final Project Proposal Paper must exceed 50 pages**. Teams that copied the scaffold before 19 Sep: read the course repo's copy.

**Still waiting:** instructor PRs open and green in **G01** (#2), **G02** (#1), **G17** (#1), **G20** (#1, #4) — none merged yet. Issues filed by teams across all 20 groups: **1** (G11's project-brainstorm issue).

### Summary

| Count | Status |
|---:|---|
| **6** | ✅ **Ready** — scaffold, bootstrap, CI green |
| **6** *(was 5)* | ⚠️ **Partial** — repo exists, setup incomplete |
| **3** | ❌ **Empty or never shared** — nothing gradeable |
| **5** *(was 6)* | ⬜ **No repository** found anywhere |

> **Sprint 1 starts Sun 28 Sep** and runs to 11 Oct. First sprint reviews: **Tue 29 Sep** (§01) and **Thu 1 Oct** (§05). Issues filed *by teams* across all 20 groups so far: **1** — epics and user stories are the graded artifact.

## Every group, by number

"Instructor PR" means a pull request is already open in that repo fixing a scaffold bug — the team only needs to review and merge it. Everything in the *What to do* column is the team's own next step. Even a *ready* repository has work to do: no team except one has filed a single epic or story yet.

| Grp | Team | Repository | Status | What's wrong | What to do |
|---|---|---|---|---|---|
| 01 | BGAF | `LeDuy23/CPSC490-01-BGAF` | ✅ ready | Nothing blocking. Repo name reads `01` rather than `G01`. Instructor PR #2 still open. No team-filed issues. | Merge PR #2. File your epics and stories. Optionally rename to the `G01` form. |
| 02 | Linux Larpers | `eliThomass/CPSC490-G02-Linux-Larpers` | ✅ ready | Nothing blocking. Instructor PR #1 still open and green. No team-filed issues. | Merge PR #1, then file epics and stories. |
| 03 | California | `eccortes4/CPSC-490-G03-California` | ⚠️ partial · 🆕 moved | Created and shared (write) on 20 Sep — but the scaffold is not copied (`.github/` missing), bootstrap not run. Name uses `CPSC-490` rather than the `CPSC490` convention. | Copy the scaffold with the command below, run bootstrap. Optionally rename to `CPSC490-G03-California`. |
| 04 | Epic Engineers | — | ⬜ no repo | No repository found under any team member's account. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 05 | Fighting Mongooses | `a-t-tran/CPSC490-Project` | ❌ not shared | Repo exists but **the instructor was never added**, so it cannot be graded. No scaffold — one commit only. Unchanged since 18 Sep. | Add `kyoungshin` as collaborator, rename to the convention, copy the scaffold, run bootstrap. |
| 06 | Forecast Market Analytics | `Joshbolus/CPSC490-G06-Forecast-Market-Analytics` | ✅ ready · 🆕 moved | Renamed, shared and scaffolded since the email — the only repository that changed. No team-filed issues yet. | File epics and stories. |
| 07 | Mighty Morphines | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 08 | Crime Busters | `miketruong91/CPSC490-G08-Crime-Busters` | ✅ ready · 🆕 moved | Created, named to convention, shared with write access, scaffolded and bootstrapped — all since the afternoon sweep. No team-filed issues yet. | File epics and stories. |
| 09 | Sigma Squad | `TylerWard741/CPSC490-G9-SigmaSquad` | ❌ empty | **Zero commits.** Repo was created and the instructor added, but nothing has ever been pushed. Name missing the leading zero (`G9`). Unchanged. | Copy the scaffold and push, then run bootstrap. Rename to `G09`. |
| 10 | Team Jiddak | `Alexander-Sanchez2/CPSC490-G10-Team_Jiddak` | ⚠️ partial | Scaffold copied but **no `.github/`** — so no CI, no harness, no templates. Bootstrap never run: 0 milestones, no `develop`. A second repo, `Alexander-Sanchez2/CPSC490`, exists under the same owner without instructor access — probably a stray. | Re-copy the scaffold with the command below (it includes hidden folders), then run bootstrap. Delete or share the stray repo. |
| 11 | 5 Guys | `markachavez2003-lab/CPSC490-G11-5Guys` | ⚠️ partial | **Bootstrap died partway** — exactly 1 milestone of 4, default labels only, no `develop`. No `.github/` either. Unchanged. | Re-copy the scaffold, then re-run bootstrap — it is safe to re-run and skips what exists. |
| 12 | ACJMM | `CharlesSinde/CPSC490-G12-ACJMM` | ✅ ready · 🆕 moved | Was empty since 3 Sep; scaffold pushed and bootstrap completed since the afternoon sweep (4 milestones, `develop`, `.github/` present). No team-filed issues yet. | File epics and stories. |
| 13 | BYKX | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 14 | Cyber Squad | `The-Cyber-Squad/CPSC490-G14-Cyber-Squad` | ⚠️ partial | Only `LICENSE` and `README.md` in the repo — **scaffold essentially not copied**. Also the only team that granted **read-only** access, so the instructor cannot open fix PRs here. Unchanged. | Grant `kyoungshin` **write** access, copy the scaffold, run bootstrap. |
| 15 | HIBBI-01 | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 16 | Neuroprosthetic | `garybs16/CPSC490` | ✅ ready | Fully set up — 4 milestones, all labels, `develop`, harness present. **But the name is just `CPSC490`**, which identifies no group. No team-filed issues. | Rename to `CPSC490-G16-Neuroprosthetic`. Then file epics and stories. |
| 17 | Sonic Scape | `vibhorbh/CPSC490-G17-SonicScape` | ⚠️ partial | Was missing `proposal/proposal.md`, which failed two gates. Bootstrap never run. Instructor PR #1 restores the file and is green — still unmerged. | Merge PR #1, then run bootstrap. |
| 18 | Team ProStrats | — | ⬜ no repo | No repository found. | Create it, copy the scaffold, add `kyoungshin`, run bootstrap. |
| 19 | Titan Security | `23jdo5/CPSC-490-Capstone-Project` *(likely)* | ❌ not shared | A repo exists that probably belongs to this team, but **the instructor was never added** and the owner could not be confirmed from the roster. No scaffold. Unchanged. | Confirm ownership, add `kyoungshin`, rename, copy the scaffold, run bootstrap. |
| 20 | Solos | `muntay89/CPSC490-G20-California` | ⚠️ partial | **Team name is wrong: it reads California, which is Group 03.** They copied it from the naming example in QUICKSTART, which used a real team's name — the number is theirs and correct. Also had no `.github/`, so zero CI ever ran, and bootstrap was never run. Instructor PRs #1 and #4 still unmerged. | Merge instructor PRs #1 and #4, rename to `CPSC490-G20-Solos`, then run bootstrap. |

## The fixes

Four recipes cover every row above. All of them are run by the team, from inside their own repository.

### No repository yet — groups 04 · 07 · 13 · 15 · 18

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

### Scaffold missing or incomplete — groups 03 · 09 · 10 · 11 · 14 · 20 (06, 08 and 12 have done this)

Run the same copy command as above — it overwrites cleanly and, unlike dragging files from an unzipped download, it cannot lose the hidden `.github/` folder. Then complete the setup:

```bash
gh auth login                     # once
gh auth refresh -s project,repo   # needed for the board
bash scripts/bootstrap.sh

python .github/scripts/check_repo.py   # expect HARNESS GREEN
```

`bootstrap.sh` is safe to re-run and skips whatever already exists — so Group 11, whose run stopped after one milestone, should simply run it again.

### Repo exists but was never shared — groups 05 · 19 (06 has done this)

Your work cannot be graded and no fix PRs can reach you until the instructor has access.

**Settings → Collaborators → Add people → `kyoungshin`**, with **write** permission. Group 14 granted read-only, which is not enough.

Then follow the scaffold recipe above.

### Repository needs renaming — groups 01 · 09 · 16 · 19 · 20

Only the repo **owner** can rename — the instructor cannot do this for you. Settings → General → Repository name.

Afterwards every teammate must re-point their local clone, or pushes will fail:

```bash
git remote set-url origin \
  https://github.com/<owner>/CPSC490-G<NN>-<TeamName>.git
git remote -v   # confirm
```

Group 16 is `CPSC490` with no group at all; Group 09 is missing its leading zero; Group 20 carries another team's name. Group 06 did exactly this on 18 Sep — it takes a minute.

---

*Re-swept 20 Sep 2026 (02:54 UTC) against every repository the instructor can see, plus a public GitHub search for `CPSC490` and `CPSC-490` repos created since August (repos from earlier semesters are excluded); the first sweep was 18 Sep, 20:00 UTC. A private repository that has not added `kyoungshin` is invisible to both, so "no repository" means none was findable — not proof none exists. Group attributions for unshared repos are inferred from usernames, profile names and commit identities. Repos whose owner matches no enrolled student are excluded.*
