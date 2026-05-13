# S_v(K=1) at next-to-leading order

Tightens the audit's leading-order `S_v(K=1) = 16` (`unitless_audit.md`)
against the seam-profile derivation's geometric prediction
`S_v ≈ 16.92` (`seam_profile.md`). The 5.7% gap between the two is
the framework's known NLO precision floor; this doc identifies the
contributions that should close it.

## The gap

| Source | `S_v(K=1)` value |
|---|---|
| Audit, leading order | `2 × M_k × ℓ_kink = 2 × 8 × 1 = 16` |
| Geometric derivation (inverse-implied) | `16.92` |
| Gap | `+5.7%` (audit too low) |

NLO corrections to `S_v` must add approximately `+0.92` Planck units
to close the gap. Equivalently, `S_v(NLO) / S_v(LO) ≈ 1.0575`.

## NLO contributions to the substrate action

Four substrate-level contributions to `S_v(K=1)` beyond the leading
classical estimate, each with a structurally-predicted sign:

### 1. One-loop quantum correction to the kink mass

Standard sine-Gordon kink in 1+1D has a known one-loop correction
(`soliton_dynamics.md` reduction matches the standard sine-Gordon
model):

    ΔM_k(1-loop) = − m_meson × (1/π − 1/4)
                 = − 1 × (0.318 − 0.250)
                 = − 0.068   (Planck masses, at K=1)

Contribution to `S_v`: `ΔS_v(1-loop) = 2 × ΔM_k × ℓ_kink = −0.136`
in Planck units.

**Sign: negative. Direction: away from closure.** This is a small
correction (−0.85%) but it sets the baseline: closure must come from
other contributions overcoming this.

### 2. Bicone target curvature near the K=1 apex

The bicone target manifold has a conical singularity at the K=1 apex
(`a1_from_saddle_node.md` standard A₁ saddle-node, multiplicity
`k_A = 2`). The apex's full angle is `α_A = 2π / k_A = π`; deficit
angle `δ_A = 2π − α_A = π`.

A kink crossing the seam in the radial direction near the apex
samples this conical curvature. The action picks up a Berry-style
correction proportional to the apex's deficit:

    ΔS_v(curvature) ≈ M_k × ℓ_kink × (δ_A / 2π) × β

with `β` a structural geometric coefficient set by the kink's path
relative to the apex. For `δ_A = π` and `k_A = 2`:

    ΔS_v(curvature) = 8 × 1 × (1/2) × β = 4β

For closure: `β = (0.92 + 0.136) / 4 = 0.264`.

**Sign: positive (deficit, conical contribution adds action).
Direction: toward closure.** The numerical value of `β ≈ 0.264`
is close to the framework-natural candidates:

| Framework irrational | Numerical | Match? |
|---|---|---|
| `1/π` | 0.318 | within 20% |
| `1/(π × φ)` | 0.197 | within 35% |
| `(π − e) / √(2π)` | 0.169 | no |
| `1 / 4` | 0.250 | within 5% |
| `8 / (k_A × q_2 q_3)` = `8/24` | 0.333 | within 25% |
| `1 / (2 ln 2)` | 0.721 | no |

The closest single-framework-quantity match is `1/4 = 0.250`, off
from the closure value by ≈ 5%. The cleanest small-prime + Klein
arithmetic match is `8 / (k_A × q_2 q_3) = 8/24 = 1/3 = 0.333`, off
by ≈ 25%.

A *priori* no clean framework number predicts `β = 0.264` exactly.
The framework's prediction at this stage is therefore that `β` lives
in the `[0.25, 0.33]` range based on Klein-arithmetic plausibility,
and that a careful bicone-metric calc would select one value.

### 3. Seam-width correction

The seam's effective width might not be exactly `ℓ_kink = 1/√K`.
Sub-leading corrections from the seam's intrinsic curvature give:

    ℓ_seam = ℓ_kink × (1 + ε_seam)

For closure: `ε_seam = (0.92 + 0.136) / 16 ≈ 0.066`, i.e., the seam
is ≈ 6.6% wider than its leading-order width.

This is structurally similar to (2) but lives in the kink-width
rather than the kink-mass. It would arise from the bicone target's
metric corrections affecting the radial geodesic distance the kink
must cross.

**Sign: positive.** Likely partially redundant with (2) at the
substrate-Lagrangian level; the two should be derived from a single
metric calc that produces both effects simultaneously.

### 4. Multi-cascade interactions at the seam

The seam in the bicone target connects K=1 to *all* K < 1 sectors
simultaneously, not just one. Interactions between cascade-sector
contributions could add a correction.

Magnitude: estimated sub-leading (≲ 1%) by the framework's heuristic
that the K=1 sector dominates the seam's intrinsic structure. The
contribution should be checkable from a full multi-sector
integration.

**Sign: unclear; likely small.**

## Net framework prediction

Combining the four contributions (with leading magnitudes):

| Contribution | Approximate value |
|---|---|
| LO baseline | `S_v(LO) = 16` |
| 1-loop quantum | `−0.136` (−0.85%) |
| Bicone curvature | `+4β` where `β ∈ [0.25, 0.33]` |
| Seam width | included in (3) or partially redundant with (2) |
| Multi-sector | `< 0.16` (≲ 1%) |

For closure (`S_v(NLO) = 16.92`):

- `β ≈ 0.264` (bicone curvature is dominant and gives `+1.06`)
- One-loop subtracts `−0.136`
- Multi-sector contribution is small

This is **internally consistent**: the framework expects bicone
curvature to dominate the NLO correction, with a magnitude in the
ballpark of `M_k × ℓ_kink × δ_A/(2π) × β`, where `β` is a
structural geometric coefficient. The 5.7% gap is closed by
`β ≈ 0.264`, a value the framework would need an explicit
metric calc to derive.

## Falsifier

If a full substrate-Lagrangian-level NLO calc gives:

- `S_v(NLO) ≈ 16.9` (within 1%): **κ_pair = 1 confirmed at NLO**;
  the framework's no-rescaling principle passes at higher precision.
- `S_v(NLO)` significantly above 17 (e.g., 18+): falsifies the
  bicone-curvature dominance assumption; multi-sector or other
  contributions are bigger than expected.
- `S_v(NLO)` significantly below 16.5: falsifies κ_pair = 1
  (audit-pinned `|∇K|_seam ≈ 0.365` doesn't agree with the geometric
  `2√3/9`, so seam-profile derivation must be re-examined).

The framework's structural prediction is the middle case. The
explicit calc is the test.

## Status of the explicit calc

**Not yet done.** Requires:

1. The bicone target manifold's metric in explicit form near the
   K=1 apex (`cone_twist_substrate.md` §1 sketches the structure but
   not the metric).
2. The kink saddle-point with this metric (sine-Gordon kink on a
   curved target — standard technique, not yet applied here).
3. The one-loop fluctuation determinant around the curved-saddle.
4. Summation over multi-cascade contributions.

Each is a separate computation, all substrate-Lagrangian-level. The
audit's structural commitments (substrate primitives at Planck;
`κ_pair = 1`) form the boundary conditions for the calc.

**This is the framework's first calc that is "tractable in
principle" but not done in practice.** It is the natural next-step
substrate-Lagrangian-level work, sitting one step deeper than the
audit.

## Open

1. **Bicone metric near K=1 apex.** Required for (2)–(4) of the
   NLO contributions.
2. **Cone-target sine-Gordon kink saddle-point** with explicit
   metric. Standard machinery; not yet applied.
3. **One-loop determinant** around the curved saddle. Same.
4. **Multi-sector seam integration.** Subleading but worth checking.

Each of these is one substrate-Lagrangian-level paper in standard
math-physics style. None requires new framework primitives; all use
existing tools applied to the framework's specific geometry.

## Cross-links

- `unitless_audit.md` — leading-order `S_v(K=1) = 16` pinning.
- `seam_profile.md` — geometric derivation implying
  `S_v(K=1) ≈ 16.92`; the gap this doc identifies and structures.
- `cone_twist_substrate.md` — bicone target manifold; source of
  the curvature contribution.
- `a1_from_saddle_node.md` — standard A₁ saddle-node giving
  `k_A = 2` and apex angle `α_A = π`.
- `soliton_dynamics.md` — sine-Gordon reduction supplying the
  one-loop kink-mass correction.
- `no_rescaling.md` — the methodological principle this doc tests
  at NLO precision.
- `framework_status.md` — registers this as a Category-A
  bookkeeping item (NLO precision pending).

## Status

Class 4 (structural setup; computation pending). The contributions
are identified, signs are framework-predicted, magnitudes are
estimated within plausible ranges. The explicit substrate-Lagrangian
calc that pins `β ≈ 0.264` is the natural next-step work.

Until that calc is done, the framework's prediction is:

    S_v(K=1, NLO) ≈ 16.9 ± few%

with `≈ 16.9` corresponding to the seam-profile derivation's
exact-match value, and `± few%` being the framework's current NLO
precision floor.
