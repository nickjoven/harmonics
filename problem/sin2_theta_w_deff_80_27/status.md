# Status

## Overall

**Proposed — 1 of 3 Z-conditions met, 3 of 3 gaps open.**

- **Z1 (numerical match at ≤ 1σ):** ✓ Met. Prediction 0.23123
  vs PDG MS-bar at M_Z 0.23121 ± 0.00004 = 0.5σ.
- **Z2 (no un-derived O(1) factors):** ✗ Not met. Two sub-gaps
  open (G1, G2).
- **Z3 (anchors labeled):** ✗ Not met. G3 open (scheme
  identification).

To promote from Class 4 (`numerology_inventory.md`) to Class 5
(structural, `framework_status.md` Survives), all three gaps
must close.

## Gap-by-gap

### G1 — Occupied interval → effective dimension reduction

**Status:** Open. No attempt in `../attempts/`.

**Target:** Derive `d_eff = d − 1/q₃^d` from an explicit integral
over the mixing-angle observable on the tongue-excluded
configuration space `(Ω ∖ tongue_{q₃}) × M^{d−1}`.

**Blocker:** The step from "tongue occupies 1/q₃^d of Ω" to
"effective dimension enters as an exponent" is currently a
hand-wave. Needs explicit Fubini-style computation.

### G2 — Why only q₃ correction, not q₂

**Status:** Open. No attempt in `../attempts/`.

**Target:** Show the q₂ correction is **structurally**
sub-leading (not just numerically smaller), OR derive an
asymmetric structural role for q₂ (numerator) vs q₃ (denominator)
that exempts q₂ from the d_eff correction at this order.

**Blocker:** Alternative formulas (symmetric correction, q₂-only
correction, q₃-only correction) give different Z1 results.
Only q₃-only hits 0.5σ. Picking q₃-only without structural
derivation is fitting to the observation.

### G3 — Scheme identification (framework root ↔ MS-bar at M_Z)

**Status:** Open. No attempt in `../attempts/`.

**Target:** Show the framework's root-level formula maps
uniquely onto MS-bar at M_Z, not to on-shell, effective Z-pole,
or low-Q² schemes.

**Blocker:** The claim "tree = Planck" in `hierarchy.md` appears
to be in tension with "root = M_Z" here. The framework needs an
internal mechanism (not SM RG, not K-scanning — both ruled out
by Nulls 2 and 3) that identifies the Stern-Brocot root with
the electroweak branching scale.

## History

| Date | Event |
|---|---|
| 2026-04-23 | Pilot problem scaffolded. Claim, nulls, context, gaps formalized. |
| (future) | G1 attempt begins. |
| (future) | G2 attempt begins. |
| (future) | G3 attempt begins. |
| (future) | Either all three close → promote to Survives, or any fails → Null 5 in sinw_fixed_point lineage. |

## Next action

Pick one of G1, G2, G3 and attempt a derivation in the
corresponding `../attempts/g{1,2,3}_*.md`. Suggested first attack:
**G1**, because its integral framing likely constrains G2
(whether q₂ contributes at the same order) and partially
constrains G3 (the scheme may fall out of the integration
measure).

## Cross-references

- `./claim.md`
- `./gaps/` — three open derivations
- `./nulls/` — four ruled-out mechanisms
- `./context/` — framework inputs
- `../../sync_cost/derivations/statistical_conventions.md` —
  Z1-Z3 definitions
