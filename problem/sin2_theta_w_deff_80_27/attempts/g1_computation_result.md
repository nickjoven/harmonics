# G1 computation — three mechanisms tested, three fail

## Summary

The substitution `d → d_eff = d − 1/q₃^d = 80/27` reproduces
`sin²θ_W = 0.23123` at 0.5σ from PDG MS-bar at M_Z, but does
**not** derive from framework primitives through any of the
three mechanisms tested below. G1 returns null.

Net effect: Z2 sub-1 does not close; the d_eff formula is an
ansatz whose numerical success is a 0.5σ coincidence, not a
structural derivation.

## What duty(q) = 1/q³ actually proves

From `../../../sync_cost/derivations/duty_dimension_proof.md`
Steps 1a–1c:

- **Width of tongue at p/q:** `w(q) ~ 1/q²` from the
  Gauss-Kuzmin / Ford-circle measure on SL(2,ℤ)-cusps.
- **Period of the q-orbit:** `period(q) = q`, the order of the
  Cartan-subgroup element in the q-th quotient of SL(2,ℝ).
- **Duty = width / period:** `duty(q) = (1/q²) / q = 1/q³`.
- **Exponent structure:** `3 = 2 + 1 = (n² − n) + (n − 1) =
  n² − 1 = dim SL(n,ℝ)` at n=2.

The exponent `d = 3` in `1/q^d` is **the dimension of the SL
group**, not a spatial-container dimension. It emerges from
width-times-period, not from a Ford-circle packing in a
d-dimensional ambient.

## Candidate A — Hausdorff / box-counting dimension of the
tongue complement

Posit that `L_Ω = 1 − 1/q₃^d = 26/27` is the box-counting
dimension of the iterated tongue complement, justifying the
exponent substitution.

Model: self-similar Cantor-like removal where each step
removes a middle interval of fractional length `p = 1/q₃^d =
1/27`, leaving N = 2 pieces each of length `(1 − p)/2`.

Self-similarity condition:

    N · ((1 − p)/2)^{d_H} = 1
    ⇒ d_H = log(N) / log(2/(1 − p))
         = log(2) / log(54/26)
         = log(2) / log(27/13)
         ≈ 0.6931 / 0.7309
         ≈ 0.9483.

Compare to the ansatz value:

    L_Ω = 26/27 ≈ 0.9630.

**Mismatch:** 0.9483 ≠ 0.9630. The "surviving Lebesgue
fraction" is not the Hausdorff dimension of a Cantor-like
iterated complement at this removal ratio.

Generic removal ratio `p` gives
`d_H = log(N) / log(N / (1 − p))`, which equals `1 − p` only
in limits (e.g., `N → ∞` with specific scaling), not at the
framework's specific `p = 1/27`, `N = 2`.

**Result:** Candidate A fails. The "fractional dimension"
reading is not standard box-counting.

## Candidate B — direct width / period re-derivation on `D`

Re-derive `duty_D(q) = w_D(q) / period_D(q)` directly on the
restricted ambient `D = (Ω ∖ T_{q₃}) × M^{d−1}`.

**Width on D.** The Ford circle at p/q (with `q ≠ q₃`) has
diameter `1/q²`. At K=1 in the measure-theoretic limit,
tongues are disjoint, so circles for `q ≠ q₃` live in
`Ω ∖ T_{q₃}` without modification. The circle itself is
unchanged.

    w_D(q) = w(q) = 1/q².

**Period on D.** The q-orbit period is the order of the
Cartan-subgroup element `diag(e^t, e^{-t})` acting on
`S¹ ≅ P¹(ℝ)`. Restricting the ambient to `D` does not remove
this Cartan generator; the orbit still has period q.

    period_D(q) = period(q) = q.

**Duty on D.**

    duty_D(q) = w_D(q) / period_D(q) = (1/q²) / q = 1/q³.

**Result:** Candidate B fails. Duty on `D` is unchanged; the
exponent remains 3, not 80/27.

## Candidate C — measure re-normalization on `D`

Try "duty on D = (tongue measure in D) / (measure of D)":

    duty_D(q) = (1/q³) / (1 − 1/q₃^d)
              = (1/q³) · (27/26).

In the mixing-angle ratio:

    sin²θ_W = (q₂^{-3} · 27/26) / ((q₂^{-3} + q₃^{-3}) · 27/26)
            = q₂^{-3} / (q₂^{-3} + q₃^{-3})
            = q₃³ / (q₂³ + q₃³)
            = 27/35
            ≈ 0.77

(or 8/35 under the claim's convention swap).

**The multiplicative factor cancels.**

**Result:** Candidate C returns the bare value, not 0.23123.

## Result table

| Mechanism | Test | Outcome | d_eff produced? |
|---|---|---|---|
| A | Hausdorff / box-counting dim of iterated complement | d_H ≈ 0.9483 ≠ 26/27 | No |
| B | Width / period re-derivation on D | unchanged, duty = 1/q³ | No |
| C | Measure re-normalization on D | cancels in ratio, bare value | No |

## What this tells us

- **The `d → d_eff = d − 1/q₃^d` substitution is an ansatz, not
  a derivation.** It posits that "surviving Lebesgue fraction"
  acts as a "fractional dimension contribution" additive to
  `(d − 1)`, and substitutes the compound into the duty
  exponent as if the exponent were derived from a spatial-
  dimension-style calculation.
- Neither the "fractional dimension" reading (Candidate A) nor
  the width/period re-derivation (Candidate B) nor the measure
  re-normalization (Candidate C) produces the substitution.
- The duty exponent `d = 3` is
  `(n² − n) + (n − 1) = dim SL(n,ℝ)` at n=2 — it derives from
  SL-group structure, not from a spatial-packing dimension
  that can be continuously varied.

## Z2 sub-1: does not close

- **Z1 still met** (0.5σ). The d_eff = 80/27 ansatz reproduces
  `sin²θ_W = 0.23123` numerically.
- **Z2 sub-1 not met.** The "O(1) factor" is the `1/q₃^d`
  subtraction, and no derivation from framework primitives
  produces it. Three independent tests return null.
- **Therefore the full claim cannot promote to scorecard.**

## Reclassification

The sin²θ_W = 2^(80/27)/(2^(80/27) + 3^(80/27)) proposal:

- **Was:** Class 4 audit candidate in
  `../../../sync_cost/derivations/numerology_inventory.md`.
- **Should become:** Class 2 (noted coincidence, no framework
  claim of derivation) — analogous to the Pythagorean-comma vs
  K_Greene coincidence at 0.17%.

The 0.5σ match is real but cannot be derived from the
framework's width/period/dim-SL structure. A different
structural route might exist — no one has found one yet.

## Open routes (unexplored)

- **Different duty-exponent decomposition on D.** If the
  `d = 3` exponent decomposes differently on the restricted
  ambient (not as Cartan-rank + Ford-width), maybe the
  decomposition structurally picks up a `1/q₃^d` correction
  somewhere. Would need a new theorem.
- **"Effective SL group" on D.** If restricting to the
  complement `Ω ∖ T_{q₃}` effectively reduces the SL(2,ℝ)
  action to a subgroup of fractional dimension `80/27`, the
  substitution would derive. Would need a specific
  identification of what that subgroup is.
- **Renormalization of the width or period on D.** If
  `w_D(q)` or `period_D(q)` picks up a q₃-dependent correction
  that I've missed in Candidate B, the duty could shift. Would
  need to re-examine Step 1a/1b of `duty_dimension_proof.md`
  in the presence of an excluded tongue.

None of these is in the repo. Pursuing any would constitute a
new attempt file.

## Cross-references

- `../claim.md`
- `../gaps/g1_occupied_interval.md`
- `../context/duty_dimension.md`
- `../../../sync_cost/derivations/duty_dimension_proof.md`
- `../../../sync_cost/derivations/sinw_effective_dimension.md`
  (the ansatz this computation falsifies as a derivation)
- `../../../sync_cost/derivations/numerology_inventory.md`
  §Class 2 (likely destination for the demoted proposal)
