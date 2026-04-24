# Claim

## Statement

At the Stern-Brocot tree's root (1/1), the electroweak mixing
angle equals

    sin²θ_W = q₂^{d_eff} / (q₂^{d_eff} + q₃^{d_eff})

with

    d_eff = d − 1/q₃^d

and inputs

    (q₂, q₃, d) = (2, 3, 3)

giving

    d_eff = 3 − 1/27 = 80/27
    sin²θ_W = 2^{80/27} / (2^{80/27} + 3^{80/27}) = 0.23123

## Identification

The predicted value is identified with the MS-bar electroweak
mixing angle at the Z pole:

    sin²θ_W (MS-bar, μ = M_Z).

The on-shell definition `1 − M_W²/M_Z²`, the effective Z-pole
`sin²θ_eff`, and the low-Q² running value are **different
quantities** and not predicted by this claim. Only MS-bar at
M_Z is the target.

## Z1–Z3 target

Per `../../sync_cost/derivations/statistical_conventions.md`:

**Z1 (C-numerical at ≤ 1σ).**
- Observation (PDG 2024): `sin²θ_W(MS, M_Z) = 0.23121 ± 0.00004`.
- Prediction: `0.23123`.
- z-score: `|0.23123 − 0.23121| / 0.00004 = 0.5σ`.
- **Z1 met.**

**Z2 (No un-derived O(1) factors).**
- `q₂`, `q₃` derived in `context/klein_bottle.md`.
- `d = 3` derived in `context/three_dimensions.md`.
- `duty(q) = 1/q^d` derived in `context/duty_dimension.md`.
- Sector assignment (q₂ = U(1)_Y, q₃ = SU(2)_L) derived in
  `context/gauge_sectors.md`.
- **The substitution `d → d_eff = d − 1/q₃^d`** is the new
  ingredient. **Z2 is not yet met** pending `gaps/g1_occupied_interval.md`.
- **The asymmetric choice** (q₃ correction only, no q₂ correction
  or cross-terms) is an O(1) factor that must be derived.
  **Z2 is not yet met** pending `gaps/g2_q3_vs_q2_asymmetry.md`.

**Z3 (Anchors labeled).**
- The prediction is **dimensionless** — no scale-setting anchor
  is required. The only observational input is the MS-bar
  renormalization scheme identification at M_Z.
- **Scheme identification** is a convention mapping, not a
  free parameter — but mapping the framework's "root-level
  perturbative ratio" to the MS-bar subtraction procedure is
  an un-formalized step. **Z3 is not yet met** pending
  `gaps/g3_msbar_identification.md`.

## Success criterion

**Structural promotion** requires all three gaps formalized:

- `gaps/g1_occupied_interval.md` closed → Z2 first component met.
- `gaps/g2_q3_vs_q2_asymmetry.md` closed → Z2 second component met.
- `gaps/g3_msbar_identification.md` closed → Z3 met.

With Z1 already met and the above three gaps closed, Z1 ∧ Z2 ∧ Z3
passes and the prediction promotes to scorecard. In that case the
prediction is **structural**, matching PDG MS-bar at 0.5σ with no
fitted factors.

## Failure criteria

- **Numerical.** The d_eff formula fails to reproduce PDG MS-bar
  at M_Z within 1σ (would require either the current 0.5σ gap to
  widen under improved measurement, or the derivation of d_eff to
  change). Currently Z1 is met.

- **Structural — Gap 1.** The "occupied interval → dimension
  reduction" step is shown to require a fitted factor (anything
  other than exactly `1/q₃^d`). This would make d_eff depend on
  a free parameter and kill Z2.

- **Structural — Gap 2.** The asymmetric q₃-only correction is
  shown to be inconsistent with a systematic perturbative
  expansion. Specifically: if the q₂ correction at order 1/q₂^d
  = 1/8 is not sub-leading to the q₃ correction at order 1/q₃^d
  = 1/27 when properly normalized, the claim's leading-order
  truncation fails.

- **Structural — Gap 3.** The framework's root-level formula is
  shown to correspond to a scheme other than MS-bar at M_Z (e.g.
  on-shell, effective Z-pole, low-Q²). In that case the prediction
  should be compared to that scheme, where it may or may not pass
  Z1.

Any single structural failure retires the proposal as Null 5 in
the `../../sync_cost/derivations/sinw_fixed_point.md` lineage.

## What this claim does NOT claim

- Not a prediction of on-shell sin²θ_W = 1 − M_W²/M_Z² = 0.2229
  (27.8σ from this formula).
- Not a prediction of low-Q² running value 0.2387 (46.5σ off).
- Not a prediction of sin²θ_eff at the Z pole (1.9σ off).
- Not a derivation of either gauge coupling in absolute terms —
  the formula is a ratio at a fixed scale.
- Not a running relation — see `nulls/null_2_sm_running.md` for
  why SM RG-running does not connect the claim to anything else.
