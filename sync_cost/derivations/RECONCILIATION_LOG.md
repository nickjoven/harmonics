# Reconciliation log — 2026-04-13

Timeline-driven cross-branch reconciliation.  Not a plan document,
not a derivation.  Just: which files are canonical, which are stale,
and what needs to move.

## The timeline

```
Apr 9  02:02  07ba6ed  "The half-twist as frustrated tension"
                        ← merge base.  Last commit shared by both
                          branches.

Apr 9  02:50+ empirical-predictions diverges and develops the mass
              sector, item 12, tongue audit, neutrino closures,
              K_STAR_PRECISE.  88 commits over 4 days.

Apr 13 00:44  386fcaf  "Neutrino solar closure: -1/36"
                        ← empirical-predictions HEAD.  The canonical
                          current state.

Apr 13 06:11  46d86cf  "colony: scaffold"
                        ← summarize-commits-questions starts, from
                          07ba6ed, without pulling in any of the
                          88 commits of empirical-predictions work.

Apr 13 22:06  bbfeacd  "Cross-branch consistency plan"
                        ← summarize HEAD.  13 commits that re-derived
                          (slightly differently) things empirical
                          -predictions had already closed.
```

The undisciplined branching: summarize-commits-questions started
**4 days after** empirical-predictions began and **~6 hours after**
it produced its canonical state, from the merge-base as if the
intervening 88 commits didn't exist.

Every closure claim on summarize needs to be checked against the
earlier (authoritative) empirical-predictions state.

## Canonical source of truth

**Branch:**  `claude/empirical-predictions-P25ZK`
**HEAD:**    `386fcaf` (Apr 13 00:44)

The canonical files on empirical-predictions that supersede work
on summarize:

| canonical file | introduced | status |
|---|---|---|
| `mass_sector_closure.md`              | `1e40044` Apr 9 14:52 | cross-link uniqueness theorem |
| `integer_conservation_law.py`         | `dd3cd5d` Apr 9 14:15 | depth · \|3Q\| = k_sector |
| `item12_K_star_closure.py`            | `0a28688` Apr 12 20:48 | K_STAR_PRECISE joint fit |
| `item12_C_from_K_star.py`             | `1c72dd2` Apr 11 14:49 | a_1(lep) · K* = q_2 = 2 |
| `item12_cross_sector_derivation.py`   | `545703b` Apr 11 14:35 | a_1² · K*² = N_sector |
| `item12_neutrino_solar_closure.py`    | `386fcaf` Apr 13 00:44 | neutrino solar -1/36 |
| `tongue_formula_accuracy.py`          | `35c9a8c` Apr 11 18:01 | reading (D) tongue audit |
| `framework_constants.py`              | `c36d636` Apr 12 21:03 | K_STAR_PRECISE = 0.86196052 |
| `boundary_weight.py`                  | `b85d043` Apr 13 00:21 | four-inconsistency fix |

## Per-file classification of summarize

Listed in commit order on summarize-commits-questions-P25ZK.

### SURVIVORS — port to empirical-predictions

| file | first commit | canonical? | reason |
|---|---|---|---|
| `colony.html` + `index.html` link | `46d86cf`, `9aeeadd`, `31c2db0` | **SURVIVES** | Pure visualization, no conflict with any empirical file. Landing-page link modifies `index.html` (merge required). |
| `lowest_integer_tensions.py` | `d884da2` | **SURVIVES** | Pedagogical enumeration of seven independent tensions that all pick out (2,3). Complements but does not duplicate the cross-link theorem in `mass_sector_closure.md`. The theorem proves uniqueness analytically; the tensions script shows how uniqueness appears from seven independent directions. No numerical claim that conflicts with canonical. |
| `lowest_integer_closure.py` | `9df641d` | **SURVIVES** | Generator-side reading: bounded-operation closure of (2,3) hits the self-predicting set. Complements the cross-link theorem from the opposite direction (filter side). No numerical claim that conflicts with canonical. |

### STALE — do NOT port; superseded by earlier empirical-predictions work

| file | first commit | superseded by | gap |
|---|---|---|---|
| `quark_mass_closure.py` | `4f2e9cb` | `item12_cross_sector_derivation.py` + `sector_base_pairs.py` | Uses lepton Fibonacci pair forced on quarks, producing `F = {13, 35, 9}`. Canonical uses **per-sector base pairs** giving `N = {4, 9, 24}`. Both fit PDG, but canonical is structural (from Klein parity and Fibonacci shift); mine is averaged. |
| `a1_closed_form.py` | `26b4550` | `item12_C_from_K_star.py` | `ln(13) − 2/(3e) = 2.31970` is a closed form for the **combined-τ/e Fibonacci-ladder a_1**. The canonical a_1 is `log(m_τ/m_μ)/(d·log(3/2)) = 2.32029` (single-step). The two definitions differ by the 0.04% intra-lepton `a_2/a_1 = 3/2` residual. Under K_STAR_PRECISE, the canonical identity `a_1·K* = 2` closes at **0.00σ**; my closed form is for a different number and closes to itself at 0.02σ. **Near-coincidence, not a structural result.** |
| `cross_sector_closure.py` | `493e80f` | `item12_cross_sector_derivation.py` | Same as `a1_closed_form.py`: extends the averaged Fibonacci-ladder projection to quarks. The resulting `F = {13, 35, 9}` is a non-canonical reading. |
| `neutrino_cross_sector.py` | `1fbeeba` | `item12_neutrino_solar_closure.py` (Apr 13 00:44) | Uses `m_3/m_1 ≈ 5.4` from the older index.html D16 formula `(K*/2)^(-2)`. Canonical is `m_3/m_1 = q_2³ = 8` with depth `35 = q_2³+q_3³`, solar `-1/36` correction, both splittings < 0.5σ. My `a_1^ν = ln(φ)` reading is a near-coincidence on the superseded formula. |
| `K_star_identity.py` | `1fbeeba` (`88bcfa1` correction) | `item12_K_star_closure.py` | Algebraic identity `(2/(3e))·denom = ln(125/12)/e` is true but doesn't derive K*. The claim `K* = ln(125/12)/e` is 0.015% off K_STAR_PRECISE. Walked back in `88bcfa1`. Not a canonical result. |
| `a1_derivation_sketch.md` | `2739c84` | — | Based on the stale `a1_closed_form.py`. The three-part decomposition it proposes (K\*, denom, F_sector) uses the wrong projection. Stale. |
| `framework_constants.py` (summarize version) | `88bcfa1` | `framework_constants.py` (empirical) | I restored a **subset** from the `.pyc` cache. The empirical version has more fields (PDG masses, per-sector values, coupling references). Strict subset — stale. |
| `CONSISTENCY_PLAN.md` | `bbfeacd` | — | My own plan document that misidentified five questions needing user decisions. The user pointed out they were already decided on empirical-predictions. Stale as written — **replaced by this log**. |

### MODIFIED — not to be merged back

| file | change on summarize | canonical state |
|---|---|---|
| `open_items.md` | I added item-1 and item-2 closure notes based on the stale closed forms. | Canonical `open_items.md` on empirical-predictions has its own state from the item-12 work. Per user instruction, `open_items.md` is the fastest-staling document — **do not trust it on either branch**. Rebuild from code state if needed. |

## What the reconciliation requires

1. **Port three files to empirical-predictions:**
   - `colony.html` (new file, no conflict)
   - `index.html` (merge: add the colony link to the empirical-predictions version; do not overwrite the empirical content)
   - `sync_cost/derivations/lowest_integer_tensions.py` (new file)
   - `sync_cost/derivations/lowest_integer_closure.py` (new file)

2. **Leave the stale files on summarize alone** (do not delete — preserve history), but add a `STALE.md` pointer at the top of each so readers know the canonical is elsewhere. Or: move to `sync_cost/derivations/stale/` on summarize with a README explaining each entry's canonical replacement.

3. **Do NOT merge summarize's `open_items.md` changes.** Canonical `open_items.md` on empirical-predictions is also suspect per user instruction; the source of truth is the derivation files themselves.

4. **Archive summarize** — once the three survivors are ported, summarize-commits-questions-P25ZK can be tagged and left dormant. Do not delete — the reconciliation log and the retracted scripts are part of the record.

## Duplicates discovered in the timeline

The timeline shows some findings were re-derived more than once on the empirical-predictions branch *itself* (not just between branches):

| finding | iterations on empirical | canonical version |
|---|---|---|
| K* value | cited 0.862 → A-2 refit → joint matter-sector | `c36d636` Apr 12 21:03 (K_STAR_PRECISE = 0.86196052) |
| neutrino depth | 36 (5ad40f8 Apr 9) → 35 (a3f7388 Apr 12) | `386fcaf` Apr 13 00:44 (depth 35, m_1/m_3 = 1/8, solar -1/36) |
| lepton +2/F_12² correction | introduced `2673614` Apr 12 01:11 → **RETRACTED** `c36d636` Apr 12 21:03 | retracted; NOT canonical |
| sin²θ_W residual | multiple attempts, some falsified → `2bf8aca` + `7f8f4a6` | `sin²θ_W = 8/35 + 8/F_10²` |
| Higgs λ residual | several incorrect forms retracted (`cca283f`) → `fc677bc` | `λ` residual = 1/228 = 1/(q_2² q_3 \|F_7\|) |
| N = 54 neutrino conjecture | introduced `2673614` → killed `c6a06f8` | not canonical |

The canonical state of empirical-predictions is its **HEAD** (`386fcaf`), not its full commit history.  Earlier commits contain intermediate attempts that were refined or retracted on the same branch.

## User's caution about open_items.md

Confirmed relevant: the open_items.md on both branches has drift.
Specifically:

- **summarize's open_items.md** now claims item 1 is closed by my
  `ln(13) − 2/(3e)` closed form — that's stale, based on a non-canonical
  a_1 definition.
- **empirical-predictions' open_items.md** may similarly lag its own
  recent retractions and closures.

Treatment: do not rely on either.  Derive item status from the
derivation files and the commit history directly.

## Recommended execution order

1. Tag the two branch heads for safety:
   - `git tag pre-reconcile-empirical-2026-04-13 claude/empirical-predictions-P25ZK`
   - `git tag pre-reconcile-summarize-2026-04-13 claude/summarize-commits-questions-P25ZK`
2. Switch to `claude/empirical-predictions-P25ZK`.
3. Cherry-pick `46d86cf` + `9aeeadd` (colony.html build) — conflict-free.
4. Resolve `31c2db0` (landing-page link) against the empirical-predictions `index.html`: add the colony link without overwriting the empirical content.
5. Cherry-pick `d884da2` (`lowest_integer_tensions.py`) — conflict-free.
6. Cherry-pick `9df641d` (`lowest_integer_closure.py`) — conflict-free.
7. Run the three survivors to verify they still execute against empirical-predictions' `framework_constants.py`.
8. Commit a single "reconciliation" note on empirical-predictions pointing at this log for provenance.
9. On summarize: add a `STALE.md` pointer at the top of each retracted file and a README at the branch root explaining the reconciliation.
10. Tag summarize as archived.

This log is itself stale the moment new work happens.  Its purpose
is one-time reconciliation.  Do not treat it as a living document.
