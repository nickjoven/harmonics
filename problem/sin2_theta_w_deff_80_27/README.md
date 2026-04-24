# Problem: sin²θ_W via d_eff = 80/27

## What this directory is

A single-problem, textbook-structured attempt to promote
`sinw_effective_dimension.md`'s proposal from Class 4 (needs audit)
to Class 5 (explicitly NOT numerology) in
`../../sync_cost/derivations/numerology_inventory.md`.

If it closes, `sin²θ_W(M_Z, MS-bar)` returns from
`MANIFEST.yml:bare_k1_identities` to `MANIFEST.yml:scorecard` as
the framework's first particle-sector Z1-Z3 derivation of a gauge
coupling. If any of the three gaps resists formalization, the
proposal joins the nulls.

## Structure

| File | Role |
|---|---|
| `claim.md` | Formal statement of the prediction and Z1-Z3 target |
| `context/` | Imported framework machinery (minimal set) |
| `nulls/` | Four prior null results that constrain the derivation space |
| `gaps/` | Three unformalized steps — what must be proven |
| `attempts/` | Working derivations (fills as work proceeds) |
| `status.md` | Current pass/fail for each gap and the overall status |

## Reading order

1. `claim.md` — what's being predicted and what "success" means
2. `nulls/*.md` — four mechanisms already ruled out (space of options)
3. `context/*.md` — framework inputs the derivation imports
4. `gaps/*.md` — the three specific unformalized steps
5. `status.md` — where each gap currently stands
6. `attempts/*.md` — proof attempts (once started)

## Closure criteria

- **Structural promotion (→ Survives / Class 5).** All three gaps
  formalized with named derivations. Prediction continues to match
  PDG MS-bar at ≤ 1σ (currently 0.5σ). Z1 ∧ Z2 ∧ Z3 per
  `statistical_conventions.md`.
- **Partial resolution.** Some gaps formalized, others not. Promote
  from Class 4 to Class 3 or Class 2 accordingly; record precisely
  which steps are derived and which remain heuristic.
- **Rejection.** Any gap shown to be structurally impossible, or
  shown to require a fitted parameter, retires the proposal as
  Null 5 in `../../sync_cost/derivations/sinw_fixed_point.md`'s
  lineage.

## Constraints from the nulls

Before attempting any derivation, note that four classes of
derivation have been ruled out (see `nulls/`):

1. Bare 8/35 as direct M_Z prediction — fails (1.1% gap, class
   1 numerology in MANIFEST).
2. SM 1-loop RG from M_Pl → M_Z — incompatible sign and magnitude.
3. K-scanning joint fixed point — no K* reproduces either α_s/α_2
   or sin²θ_W.
4. K → μ duty map with |r| decoherence tax — fails under joint
   constraints.

The d_eff = 80/27 proposal must succeed on a path distinct from
all four. That distinctness is the content of the three gaps.

## Cross-references

| File | Relation |
|---|---|
| `../../sync_cost/derivations/sinw_effective_dimension.md` | Source of the proposal |
| `../../sync_cost/derivations/numerology_inventory.md` §Class 4 | Current classification |
| `../../sync_cost/derivations/statistical_conventions.md` | Z1-Z3 criteria |
| `../../MANIFEST.yml:bare_k1_identities.sin2_theta_W` | Current demoted status |
| `../../sync_cost/derivations/framework_status.md` | Target: Survives if closed |
