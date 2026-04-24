# G1 attempt: integral derivation of d_eff = d − 1/q₃^d

**Status:** First-pass attempt. Identifies the natural symbolic setup, finds where the hand-wave can be made precise, and isolates the one structural step that still needs work to clear Z2.

## Setup — symbols

- **Configuration space.** `C = Ω × M^{d−1}` where
  - `Ω = [0, 1]` is the rotation-number (frequency) axis, with
    Lebesgue measure `dω`.
  - `M^{d−1}` is the (d−1)-dimensional spatial manifold (here a
    flat torus from `klein_bottle.md`'s base × the residual
    spatial direction), with Riemannian volume `dx`.
  - `d = 3` (`context/three_dimensions.md`).

- **Tongues.** For each rational `p/q ∈ [0,1]` with `(p, q) = 1`,
  let
  - `T_q ⊂ C` denote the K=1 Arnold tongue at p/q.
  - `μ(T_q) = 1/q^d`, the K=1 duty (`context/duty_dimension.md`).
  - The tongue is a **strip**: full extent in `M^{d−1}`, finite
    width `w_q(K=1) = 1/q^d` in `Ω`. Geometrically, a
    `M^{d−1}`-fibre bundle over a `Ω`-segment.

- **Sector indicator.** Let
  - `χ_Y(c)` = indicator function for the "U(1)_Y is active" region
    at configuration `c ∈ C` — coincides with `T_{q₂}` per
    `context/gauge_sectors.md`.
  - `χ_W(c)` = indicator for the "SU(2)_L is active" region —
    coincides with `T_{q₃}`.

- **Bare mixing angle.** Define

      sin²θ_W ≡ ⟨χ_Y⟩ / (⟨χ_Y⟩ + ⟨χ_W⟩)

  where `⟨·⟩ = ∫_C (·) dω dx / vol(C)` is the K=1 measure
  average.

## Bare result reproduced

- `⟨χ_Y⟩ = μ(T_{q₂}) = 1/q₂^d`
- `⟨χ_W⟩ = μ(T_{q₃}) = 1/q₃^d`
- `sin²θ_W (bare) = (1/q₂^d) / (1/q₂^d + 1/q₃^d) = q₃^d / (q₂^d + q₃^d)`

**Convention check.** The version in `claim.md` writes
`sin²θ_W = q₂^d / (q₂^d + q₃^d) = 8/35`. The expressions are
related by the swap `Y ↔ W` in the sector identification
(`context/gauge_sectors.md`) — consistent with the standard
`g'²/(g²+g'²)` definition. We adopt the claim's convention
hereafter:

      sin²θ_W = q₂^d / (q₂^d + q₃^d).

## The geometric move (where the hand-wave lives)

- The **measurement domain** for the mixing-angle ratio is
  argued to be the **complement of the q₃ tongue**:

      D = C \ T_{q₃}.

  Heuristic reason: where the q₃ tongue is "active" (locked),
  the SU(2)_L coupling is dominated by the q₃ resonance and the
  Y-vs-W competition is degenerate; the meaningful comparison
  happens in `D`.

- On `D`, the volume decomposes as

      vol(D) = vol(Ω \ tongue_strip_Ω) · vol(M^{d−1})
             = (1 − 1/q₃^d) · vol(M^{d−1}).

- The **effective Ω-extent**, normalized to the original `[0,1]`,
  is `L_Ω = 1 − 1/q₃^d`.

- **Effective dimension as additive composition.** The
  configuration space's "dimension contribution" is read as
  - `M^{d−1}` contributes `(d − 1)` (untouched).
  - `Ω`, originally contributing `1`, now contributes `L_Ω`
    (its surviving fractional length).
  - Total: `d_eff = (d − 1) + L_Ω = d − 1/q₃^d`.

- For `(q₃, d) = (3, 3)`:

      d_eff = 3 − 1/27 = 80/27.

## Where the substitution d → d_eff in the duty formula gets its
purchase

- The K=1 Ford-circle stacking that produces `duty(q) = 1/q^d`
  is built on the configuration space `C = Ω × M^{d−1}`. The
  exponent `d` is **the dimension of the stacking ambient
  space**, not a free parameter.

- A clean way to see why the exponent depends on the ambient
  dimension:
  - The Ford-circle of denominator q has linear scale `r_q ~
    1/q` in each independent ambient direction.
  - In a d-dimensional ambient, the volume of a single circle
    scales as `r_q^d ~ 1/q^d`. Sum over coprime numerators is
    O(φ(q)/q^d); the "duty per q" is `1/q^d`.

- **Substitution in the modified ambient.** When the available
  ambient is `M^{d−1} × (Ω \ tongue_{q₃})` instead of
  `M^{d−1} × Ω`, the Ford-circle stacking lives on a space
  whose dimension is `d_eff` in the **box-counting / scaling**
  sense:
  - Linear scale per ambient direction: `r_q ~ 1/q` (unchanged).
  - Volume of one Ford-circle in the modified ambient:
    `r_q^{(d−1)} · (length contribution from Ω \ tongue)`.
  - The `Ω \ tongue` contribution at scale `r_q`: the available
    Ω-extent is `(1 − 1/q₃^d)`, but at the relevant Ford-circle
    scale `1/q`, the *effective* extent enters as the
    fractional-power factor `(1 − 1/q₃^d) ~ r_q^{1 − 1/q₃^d}`
    by the box-counting identification of available extent with
    a fractional dimensional contribution.
  - **This is the step that must be made rigorous.**

- Combining: `r_q^{(d−1)} · r_q^{1 − 1/q₃^d} = r_q^{d − 1/q₃^d}
  = r_q^{d_eff}`. So `duty_{D}(q) = 1/q^{d_eff}`.

## Recovering the corrected formula

- Repeating the K=1 measure average on `D`:

      ⟨χ_Y⟩_D = duty_D(q₂) = 1/q₂^{d_eff}
      ⟨χ_W⟩_D = duty_D(q₃) = 1/q₃^{d_eff}

- Then

      sin²θ_W (D) = q₂^{d_eff} / (q₂^{d_eff} + q₃^{d_eff})
                  = 2^{80/27} / (2^{80/27} + 3^{80/27})
                  ≈ 0.23123.

  Z1 is met (0.5σ vs PDG MS-bar at M_Z).

## What this attempt closes vs leaves open

- **Closes.**
  - The decomposition of `C` into `Ω × M^{d−1}` and the strip
    geometry of `T_{q₃}` (from imported context).
  - The volume identity `vol(D)/vol(C) = 1 − 1/q₃^d` (from
    the duty `μ(T_{q₃}) = 1/q₃^d` at K=1).
  - The reading `d_eff = (d − 1) + L_Ω` as the additive sum of
    untouched spatial contribution plus surviving Ω fraction.
  - The substitution `d → d_eff` in the duty formula, conditional
    on the box-counting scaling step below.

- **Leaves open (the residual hand-wave).**
  - The identification `(1 − 1/q₃^d) ~ r_q^{1 − 1/q₃^d}` —
    the move from "available Ω extent is `1 − 1/q₃^d`" to "the
    Ω-direction contributes `r_q^{1 − 1/q₃^d}` to the stacking
    volume" — uses a **box-counting / Hausdorff-style scaling**
    identification. This is geometrically natural for sets with
    fractal complements, but needs an explicit derivation showing:
    1. The complement `Ω \ tongue_{q₃}` has well-defined
       fractional box-counting dimension at scale `r_q`.
    2. Its scaling contribution to the duty integral is exactly
       the factor `r_q^{L_Ω}`, not (e.g.) `L_Ω · r_q` or some
       other combination.

- This residual step is what would, if formalized, complete G1.

## Open question for G1

- **Is `(1 − 1/q₃^d)` really a fractional dimension of the
  complement?** The complement `Ω \ tongue_{q₃}` is just
  `[0, 1] \ [some interval of length 1/q₃^d]` — Lebesgue
  dimension 1, not fractional. The "fractional dimension"
  reading would only hold if the **iterated removal** of all
  q₃-resonance neighborhoods at every depth produces a
  Cantor-like set with Hausdorff dim `1 − 1/q₃^d` exactly.

- That iterated structure is plausible (Arnold-tongue boundaries
  are Cantor-fractal in the KAM regime) but the specific
  Hausdorff dimension `1 − 1/q₃^d` would need to be shown.

- **Alternative path:** if the "fractional dimension" reading
  doesn't work, an explicit volume integral over `D` with
  Ford-circle stacking might still produce the substitution
  `d → d_eff` via a different mechanism (e.g., a renormalization
  of the duty per unit Ω-length on the complement). That path
  is open in `attempts/g1_renormalized_duty.md` (not yet drafted).

## Suggested next steps

1. **Compute the box-counting dimension of the iterated tongue
   complement** `Ω \ ⋃_p T_{p/q₃}^{depth}` at the K=1 limit. If
   it equals `1 − 1/q₃^d`, the residual hand-wave closes.
2. **Or compute the explicit Ford-circle stacking volume on
   `D`** without the dimension argument, by direct integration,
   and check whether the substitution `d → d_eff` emerges.

Either route, if successful, completes G1 and removes the Z2
sub-1 obstruction. If neither works, the d_eff substitution is
not derivable from this geometric setup and the claim demotes
back to "ansatz fitting at 0.5σ."

## Cross-references

- `../claim.md`
- `../context/duty_dimension.md`
- `../context/three_dimensions.md`
- `../context/klein_bottle.md`
- `../context/gauge_sectors.md`
- `../gaps/g1_occupied_interval.md`
- `../nulls/null_3_k_scan.md` (no finite-K mechanism allowed)
