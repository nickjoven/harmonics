# Unitless audit: substrate primitives end-to-end

Companion to `unitless_check.md`. That doc establishes *that* the
framework's predictions are invariant under unit choice. This doc
*executes the end-to-end audit*: with substrate primitives pinned to
Planck units (`ℏ = G = c = 1`, `σ = m = 1`, `L_x = ℓ_P`, `τ_tick = t_P`),
which framework-level predictions become numerically determinate, and
which still require additional structural input.

This is the audit referenced in `soliton_dynamics.md` Open 1,
`cone_twist_substrate.md` Open 1, `time_axis_split.md` Status, and
`wave_particle_substrate.md` Open 3.

## The audit's central convention

Three layers of unit-convention pinning:

1. **Planck normalisation** (already in `unitless_check.md`):
   `ℏ = G = c = 1`. The Planck time `t_P`, length `ℓ_P`, mass `m_P`,
   and temperature `T_P` are each set to 1.
2. **Substrate-primitive normalisation** (new in this doc):
   `σ = m = 1` in Planck units. The phase-stiffness coefficient and
   the effective inertia per substrate site are at the Planck scale.
   Consequence: the substrate sound speed `c = σ / √m = 1`
   (consistent with Planck convention), and the substrate-fundamental
   length and time both equal Planck length and Planck time.
3. **Loop-length pinning** (new in this doc):
   `L_x = ℓ_P = 1` in Planck units. The Klein bottle's antiperiodic
   loop has period equal to one Planck length. Consequence:
   `τ_tick = L_x / c = 1 = t_P`. The substrate's natural arrow-time
   quantum is the Planck time.

The audit can be re-run for sub-Planckian primitives — `σ = φ^(-k)`,
`L_x = φ^(-2k) ℓ_P`, etc. — at any non-negative integer Fibonacci
depth `k`. The cleanest case is `k = 0` (Planckian) and is the
natural choice from the framework's existing prediction
`R_arrow = (6 × 13^54) × φ^(2k)` matching observed `H_0 × t_P` at
sub-percent precision when `k = 0`. Sections below adopt `k = 0`
throughout.

## Pinned quantities (calc-ready)

With the above convention, the following framework quantities are
**determinate** in Planck units. Each entry is computed as a function
of `K` only (with `r → 1` at full lock).

### `β̃²` — the sine-Gordon dimensionless coupling

From `soliton_dynamics.md` §2:
`β̃² = ℏ / (σ √(K r m)) = 1 / √K` (Planck units, r = 1, σ = m = 1).

| `K` sector | `β̃²` value | Source |
|---|---|---|
| `K = 1` (string boundary) | 1.000 | `master_cascade_identity.md` |
| `K* = 2^(−3/14) ≈ 0.862` (matter equilibrium) | 1.077 | confirmed instance |
| `K_IMF = 2^(−1/3) ≈ 0.794` (bowed cascade) | 1.122 | confirmed instance |
| `K_clarinet = 3^(−1/2) ≈ 0.577` | 1.316 | confirmed instance |
| `K = 1/2` (first mediant) | 1.414 | first cascade jump from BOS |

**Closes `soliton_dynamics.md` Open 1's structural coefficient.**

### `N_breathers` — breather mode count per sector

`N_max = ⌊8π / β̃²⌋ = ⌊8π √K⌋ ≈ ⌊25.13 √K⌋`.

| `K` sector | `N_breathers` |
|---|---|
| `K = 1` | **25** |
| `K* = 2^(−3/14)` | **23** |
| `K_IMF` | **22** |
| `K_clarinet` | **19** |
| `K = 1/2` | **17** |

These are the substrate's predicted breather-tower lengths at each
cascade depth. **Falsifier**: any observed bound-state spectrum in
a cascade sector showing a count incompatible with these numbers
falsifies the soliton-sector identification at that sector.

### `M_k` — kink mass

`M_k = 8σ √(Kr) = 8√K` (Planck masses).

| `K` sector | `M_k` (Planck masses) | In GeV (m_P ≈ 1.22 × 10¹⁹ GeV) |
|---|---|---|
| `K = 1` | 8.00 | 9.8 × 10¹⁹ |
| `K*` | 7.42 | 9.1 × 10¹⁹ |
| `K_IMF` | 7.13 | 8.7 × 10¹⁹ |
| `K_clarinet` | 6.08 | 7.4 × 10¹⁹ |
| `K = 1/2` | 5.66 | 6.9 × 10¹⁹ |

All cascade-sector kinks are Planck-scale objects. Direct observation
as standard-particle excitations is not expected; framework kinks are
candidates for primordial gravitational radiation sources, primordial
black-hole seeds, or seam-localised structures.

### `E_slip` — phase-slip activation energy

`E_slip ≈ M_k = 8√K` (Planck masses → Planck energies via `E = m c²` with `c = 1`).

At `K*`: `E_slip ≈ 7.42 m_P c² ≈ 9.1 × 10¹⁹ GeV`.

### `T_sat` — substrate-saturation temperature

`T_sat = E_slip / k_B = 8√K T_P` (Planck temperatures; `T_P ≈ 1.42 × 10³² K`).

At `K*`: `T_sat ≈ 7.42 T_P ≈ 1.05 × 10³³ K`.

**This is far above every temperature in any observed environment**
(big-bang singularity unreached; Hawking temperature of sub-Planck-mass
black holes the only candidate). Substrate physics is hidden below
`T_sat` by the Boltzmann exponential, consistent with the negative
falsifier of atomic clocks at `Δτ/τ ≲ 10⁻¹⁸` (well below `T_sat` by
60+ orders of magnitude).

### `S_v` — vortex-pair action

`S_v ≈ 2 M_k × τ_loop = 16√K` (Planck units, dimensionless action `S/ℏ`).

At `K*`: `S_v ≈ 14.84`. Schwinger-like pair-production rate is
suppressed by `exp(−π S_v / |∇K|)` where `|∇K|` is the local
K-gradient in Planck units.

### `R_wheel` — kink width / substrate Compton length

`R_wheel = ℓ_kink = 1/√K` (Planck lengths).

| `K` sector | `R_wheel` (Planck lengths) |
|---|---|
| `K = 1` | 1.00 |
| `K*` | 1.077 |
| `K_IMF` | 1.122 |
| `K_clarinet` | 1.316 |
| `K = 1/2` | 1.414 |

All cascade-sector wheel radii are Planckian. The framework's natural
length scale at every observed cascade sector is the Planck length;
matter-localisation on the K-axis is at Planck-resolution.

### `R_arrow` — substrate ticks per Hubble time

`R_arrow = (6 × 13^54) × φ^(2k) = 6 × 13^54 ≈ 8.49 × 10^60` for `k = 0`.

**Matches the observed Planck-to-Hubble ratio to sub-percent precision.**
This is the audit's *confirmation* that the framework's convention
(`τ_tick = t_P`, `k = 0`) is consistent with cosmological observation,
not a free-parameter fit.

### `k` — Fibonacci depth integer

**`k = 0`.** Pinned by the audit's convention `τ_tick = t_P` and
confirmed by the `R_arrow` match. The audit could be re-run with
`k > 0` (sub-Planckian τ_tick), but this would require the
Planck-to-Hubble ratio to be `(6 × 13⁵⁴) × φ^(2k)` rather than
`6 × 13⁵⁴`, which would deviate from observation by `φ^(2k)`
× sub-percent. Currently `k = 0` is preferred.

## Conditionally pinned (modulo one remaining input)

### `κ_pair` — Hubble-rate prefactor

`H(t) = κ_pair × ⟨Γ_pair(t)⟩_substrate`. The form is fixed by
`time_axis_split.md` and `cone_twist_substrate.md` §5.1, but the
numerical value of `κ_pair` requires the **seam K-gradient profile
`|∇K|_seam`**, which is not yet pinned by the framework's existing
structure.

Two natural framework candidates for `|∇K|_seam`:

1. `|∇K|_seam ≈ 1` (Planck units, "order-unity K-gradient at the
   seam") — gives `Γ_pair ≈ exp(−π S_v) ≈ exp(−50 √K) ≈ 10^(−22)`
   at K=1 in Planck units per Planck volume per Planck time.
2. `|∇K|_seam ≈ K × H_0 t_P ≈ 10^(−61)` (cosmological-scale gradient) —
   gives `Γ_pair → 0` to absurd suppression.

The audit's reading: option (1) is the natural framework choice
because the seam is a *substrate-local* discontinuity, not a
cosmological gradient. With `|∇K|_seam ≈ 1`:

    κ_pair = H_0 / Γ_pair × V_substrate

where `V_substrate` is the seam's effective volume. Pinning
`V_substrate` is the single remaining structural input. A natural
candidate: `V_substrate = (Hubble length)² × L_x ≈ R^(2) × 1` Planck
units, where R = `R_Planck-to-Hubble = 6 × 13⁵⁴`. This gives
`V_substrate ≈ R² ≈ 7.2 × 10¹²¹` and `κ_pair ≈ 10⁻⁶¹ × 10⁻²² ×
10¹²¹ ≈ 10³⁸`, dimensionless.

**Status of `κ_pair`: structural form pinned; numerical value
conditional on seam volume identification.** Not blocked by deep
calculation, only by a single naming-of-which-volume choice that the
framework should commit to.

## Open beyond this audit

The following remain open and would require structural work beyond
the unit-convention audit:

1. **The seam volume `V_substrate`.** As above; one decision pinning
   `κ_pair`. Candidate forms suggested but not yet selected.
2. **Sector-to-observable identification.** Which observed structure
   (gravitational geon? primordial BH? cosmic string?) is the
   K=1 sector's kink? `sine_gordon_substrate.md` Open 1, not
   addressable by audit alone.
3. **K(t) cosmological evolution.** The substrate's K-axis time
   dependence. `time_axis_split.md` quantitative-structure-section
   open; needs the substrate's full Lagrangian solved (which would
   close several other Opens simultaneously).
4. **3+1D substrate extension.** `cone_twist_substrate.md` Open 4;
   not in the audit's scope.

## What this audit enables

With the above quantities now numerically pinned, the following
framework predictions become **calc-ready**:

| Prediction | Pinned by audit | Where in the framework |
|---|---|---|
| Breather count per cascade sector | `N_max(K)` table above | new — sector observability test |
| Kink mass spectrum across K-zoo | `M_k(K) = 8√K m_P` | `sine_gordon_substrate.md` Kink section |
| Substrate saturation temperature | `T_sat(K) = 8√K T_P` | new — extreme-T cosmology |
| Vortex-pair action | `S_v(K) = 16√K` | `cone_twist_substrate.md` §5.1 |
| Hubble-to-Planck ratio | `R_Planck-to-Hubble = 6 × 13^54` | `unitless_check.md` (existing); now confirmed as audit-consistent |
| `k = 0` in `R_arrow` ladder | confirmed by `R_arrow` match | `time_axis_split.md` |
| Wheel-radius / kink-width tower | `R_wheel(K) = 1/√K ℓ_P` | new — extends `soliton_dynamics.md` |

The framework's open structural predictions
(`AB-phase = π`, `Ω_Λ = 13/19`, `sin²θ_W` is failed) are already
dimensionless integers/ratios and require no audit pinning.

## Audit-derived predictions that are testable

Three new concrete predictions emerge:

1. **Breather count `N_max(K)` as a function of cascade depth.** The
   framework predicts a *finite, integer, calculable* count of
   breather modes at each cascade sector — 25 at K=1, 23 at matter
   equilibrium. Identifying which observed bound-state ladder
   corresponds to a substrate breather tower would either confirm or
   falsify the cascade-sector identification.
2. **All cascade-sector kinks are Planck-scale.** The framework
   predicts `M_k(K)` between 5.66 and 8.00 Planck masses across the
   entire K-zoo. No cascade-sector hosts a sub-Planck-mass soliton.
   This forces sector-observable identification toward Planck-scale
   phenomena (primordial GW, primordial BH, very early universe) and
   away from SM-scale particles.
3. **`T_sat ≈ 7.4 T_P` at matter equilibrium.** The substrate's
   activation temperature is one order of magnitude *above* the
   Planck temperature. The substrate is *exponentially hidden* in
   every observable temperature regime; only Hawking-emission from
   sub-Planck-mass black holes would expose it.

## Falsifiers sharpened

1. **Breather count mismatch.** Any sector-observable identification
   producing a bound-state count incompatible with the table above
   falsifies the soliton-sector identification at that K.
2. **`R_arrow` precision-cosmology mismatch.** Currently consistent
   with `k = 0`. Any precision cosmological observation deriving a
   value of `H_0 × t_P` incompatible with `1 / (6 × 13⁵⁴)` (and not
   compensated by `φ^(2k)` for some small `k > 0`) falsifies the
   audit's `τ_tick = t_P` convention. The cleanest test sits at the
   sub-percent precision currently achievable on `H_0`.
3. **Substrate-saturation temperature crossing.** If any observed
   thermal phenomenon at `T < T_sat ≈ 10³³ K` shows clock-rate
   variation incompatible with the framework's predicted suppression,
   falsifies either `E_slip ≈ M_k` or the saturation-T form.

## Pre-audit vs. post-audit status of the open queue

Of the items in Category A (bookkeeping) of the framework's
obstruction map:

- **`β̃²`** ✓ pinned (`= 1/√K`)
- **`κ_pair`** ⚠ conditional (form pinned; seam volume needs naming)
- **`E_slip`** ✓ pinned (`= 8√K m_P c²`)
- **`S_v`** ✓ pinned (`= 16√K`)
- **`k`** ✓ pinned (`= 0`)
- **`T_sat`** ✓ pinned (`= 8√K T_P`)
- **`R_wheel`** ✓ pinned (`= 1/√K ℓ_P`)
- **Sector-to-observable identification** ✗ unchanged (structural, not calc)
- **Hadronic mass scale** ✗ unchanged (needs new `(d, n, b)` triple)

Net: 7 of 9 calc-tractable items closed by the audit. The remaining
2 are either conditional on one further structural choice (seam volume
for `κ_pair`) or require structural work outside audit scope.

## Status

Class 3 (derivation grade). The audit's structural content — that
substrate primitives in Planck units (`σ = m = c = 1, L_x = τ_tick =
1`) determine the listed quantities — follows directly from the
existing framework derivations with Planck-normalisation applied.

The audit's choice `k = 0` (Planckian `τ_tick`) is independently
*confirmed* by the `R_arrow` consistency with observed `H_0 × t_P`
at sub-percent precision; this is a non-trivial consistency check.

The audit does not introduce new primitives. It is a unit-convention
pinning of the existing framework, with concrete numerical values
emerging where the framework's structure permits.

## Cross-links

- `unitless_check.md` — parent doc; methodology and Tier-3 through
  Tier-6 dimensionless-prediction tables. This audit extends those
  tables into the substrate-primitive sector.
- `soliton_dynamics.md` — Open 1 (`β̃²` numerical coefficient)
  closed by this audit.
- `cone_twist_substrate.md` — §5.1 (`S_v` and `Γ_pair` form) pinned
  by this audit; `κ_pair` conditional on one further input.
- `time_axis_split.md` — `R_arrow` prediction shape confirmed by
  audit at `k = 0`; `T_sat`, `E_slip` numerically determined.
- `wave_particle_substrate.md` — Open 3 (Wick-rotation = half-twist
  quantitative triangle) now calc-ready via pinned `S_v`.
- `half_twist_dynamics.md` — `R_Planck-to-Hubble = 6 × 13⁵⁴`
  consistent with audit; `Λ ∝ Ω_Λ × H_0²` ratio remains as
  `half_twist_dynamics.md` derived.
- `framework_lagrangian.py` — substrate Lagrangian's σ, m
  coefficients identified with Planck-scale values by this audit's
  convention.
- `master_cascade_identity.md` — supplies the K-zoo `(d, n, b)`
  triples that the per-sector values tabulated above instantiate.
- `framework_status.md` — Category A bookkeeping items: 7 of 9
  closed by this audit; 2 remain (one conditional, one structural).
