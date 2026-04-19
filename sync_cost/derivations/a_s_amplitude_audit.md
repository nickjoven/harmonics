# A_s scalar amplitude: status audit

Attribution audit for Issue #56 Tier 2 item #5 ("initial conditions /
A_s amplitude"). Pattern-matches the PR #67 methodology: vocabulary
disambiguation, then per-doc attribution, then a precise statement
of what remains open.

## Three senses of σ² in the framework

Prior docs use "σ²" for three different quantities. Collapsing them
into one symbol has hidden what is closed and what is not.

| Symbol | Meaning | Value | Derived by |
|---|---|---|---|
| σ²_kernel | kernel normalization per coupling direction | 1/4 | `adm_prefactor_verification.py` from Hamiltonian prefactor 16πG |
| K_eff | effective coupling at Hubble scale, summed over 2d neighbors | 3/2 | `sigma_squared.py` from `K_eff = 4πG ρ_crit L_H²/c²` |
| σ²(d) | tree-measure constraint at Stern-Brocot depth d | depth-dependent | `alphabet_depth21.py` from `1/Σ(1/q²)` |

Reconciliation between the first two (C-structural, closed):

    K_eff = σ²_kernel × 2d  =  (1/4) × 6  =  3/2   for d = 3.

The 2d = 6 is the nearest-neighbor coordination number on a cubic
lattice (`adm_prefactor_verification.py` §4).

The third σ²(d) is a tree-side quantity; its relation to the two
physical-side quantities is the open question for A_s.

## What's closed (C-structural / C-attribution)

- **P(k) shape**: `spectral_tilt_reframed.md` derives the spectral
  tilt n_s from mode-locking / devil's-staircase structure. No cost
  function, no fitting. `alphabet_depth21.py` confirms the self-
  similarity: Δ(ln σ²)/Δd = ln(φ²) per Fibonacci level. **(C-structural)**

- **Pivot identification**: `k_omega_mapping.py` identifies the CMB
  pivot k* = 0.05 Mpc⁻¹ with Fibonacci level d ≈ 5 (13/21 convergent,
  local-level indexing) and the deep Fibonacci index F_21 = 10946
  (tree-depth indexing). The two levels correspond to the same
  pivot scale under different countings; this is a vocabulary
  point, not a physics one. **(C-structural)**

- **σ² kinematic reconciliation**: σ²_kernel = 1/4 vs K_eff = 3/2
  closed as above. **(C-structural)**

## What's open (remaining gap)

`sigma_squared.py` §7 states the gap explicitly:

> The dimensionless A_s in cosmology is measured in different units
> than the tree's σ². The conversion factor involves the Hubble
> volume and Planck units. This is the prefactor verification
> identified in Derivation 12 Part I §7.

**Misattribution identified.** The "Derivation 12 Part I §7" reference
points to `continuum_limits.md` §5a (the file formerly
`12_continuum_limits.md` before the b2deee7 narrative pruning).
That section closes the **ADM prefactor verification** — σ²_kernel = 1/4
producing both 16πG and 8πG via the Gauss-Codazzi embedding. It does
**not** cover the A_s unit conversion.

Two distinct "prefactor verification" problems have been conflated
under one phrase:

| Prefactor problem | Quantity | Status |
|---|---|---|
| ADM prefactor verification | σ²_kernel giving 16πG + 8πG | **closed** (`continuum_limits.md` §5a, `adm_prefactor_verification.py`) |
| A_s unit-conversion prefactor | σ⁴/(4π² q_pivot²) × ? = A_s_obs | **open** — this doc |

`sigma_squared.py` §7's pointer to "Derivation 12 Part I §7" for the
A_s side is therefore **wrong** — it would resolve if the ADM and
A_s prefactor problems were the same. They are not. The ADM side
concerns Einstein-equation coefficients on a spatial slice; the A_s
side concerns the amplitude of a specific correlator
(curvature-perturbation two-point at the pivot), which involves a
Hubble-volume mode count that does not appear in the ADM
constraints.

**No framework doc closes the A_s unit-conversion prefactor.**
`sigma_squared.py`'s comment is a stale cross-reference, not a
closure.

### Numerical status

The formula `A_s = σ⁴ / (4π² q_pivot²)` (from `sigma_squared.py`
inversion of Route 2) evaluated at the framework-natural choices:

| σ² sense | σ² value | q_pivot = F_21 = 10946 | Ratio to observed (2.1e-9) |
|---|---|---|---|
| σ²_kernel | 1/4 | 1.32e-11 | 1/159 |
| K_eff | 3/2 | 4.76e-10 | 1/4.41 |
| σ²(d=21) (tree sum) | ≈ 0.37 at d=21 | 2.9e-11 | 1/72 |

None matches observation at the σ level. Closest is K_eff = 3/2 at
**4.41× too small**. This is the precise numerical content of the
"prefactor verification" gap.

### Candidate factors for the missing 4.41

Numerology (not closures):

- 4π/3 ≈ 4.19 — volume factor of unit 3-sphere; would arise if the
  formula counts modes per 3-volume, not per k-interval
- 4π/3 × 1.05 = 4.40 — the 5% residual could be the same order as
  the PMNS %-only deviations (`mixing_angle_audit.md` pattern)

Neither is a derivation. If the missing factor is 4π/3, the
corrected formula would be `A_s = (4π/3) σ⁴ / (4π² q_pivot²)`
= `σ⁴ / (3π q_pivot²)`. With σ² = 3/2 and q_pivot = F_21, this
gives A_s ≈ 2.0e-9 — 5% below observed. Not verified.

### Sensitivity to pivot-level choice

The formula is quadratic in q_pivot. With σ² = 3/2 fixed:

| d | F_{d+1} | A_s_pred | ratio |
|---|---|---|---|
| 19 | 4181 | 3.26e-9 | 1.55× too large |
| 20 | 6765 | 1.24e-9 | 1.69× too small |
| 21 | 10946 | 4.76e-10 | 4.41× too small |

Observed 2.1e-9 falls between F_19 and F_20, closer to F_19. A
half-integer pivot (d ≈ 19.5) would match, but the framework has no
mechanism for non-integer pivots — the Fibonacci convergents are
discrete.

The 61.3 e-fold N_efolds prediction (from √5 / rate) depends on the
pivot level; recomputing with d_pivot ≠ 21 changes the e-fold count.

## Closure options

Route 1 (attribution recovery) was checked and **ruled out** — the
"Derivation 12 Part I §7" pointer in sigma_squared.py goes to the
ADM prefactor verification (`continuum_limits.md` §5a), which is a
different problem. Two remaining routes:

1. **Unit-volume factor derivation**. Derive the specific 4π/3 (or
   equivalent) factor from the Hubble-volume-to-mode-count conversion.
   This requires writing down the k-space mode density in the
   framework's tree parameterization explicitly. Known territory
   (standard CMB calculation); needs the tree's Ω↔k Jacobian stated
   to prefactor precision. **Medium effort; ~1 session.**

2. **Fresh derivation of A_s from K_eff and the Hubble volume**.
   Start from A_s = ⟨δφ²⟩ at the pivot, express ⟨δφ²⟩ in terms of
   the Kuramoto order-parameter fluctuations (`spectral_tilt_reframed.md`
   Eq. 3: `⟨δθ²⟩(ω) ∝ g(ω)/(Kr)²`), and close with K = K_eff × r*.
   **Heaviest; multi-session.**

Option 1 is the right warm-start for a single session. Option 2 is
the correct long-term answer.

## Fix to apply

`sigma_squared.py` §7's docstring should have its "This is the
prefactor verification identified in Derivation 12 Part I §7" line
corrected — the ADM prefactor verification is closed, the A_s
unit-conversion prefactor remains open. The two should not be
conflated. Applied in the same commit as this audit.

## Status summary for Issue #56

| Aspect | Status | Sense |
|---|---|---|
| P(k) shape (tilt n_s) | closed | C-structural |
| σ²_kernel / K_eff reconciliation | closed | C-structural |
| Pivot level identification | closed | C-structural |
| A_s amplitude prefactor | **open** | — |

Issue #56 Tier 2 item #5 should be refined from "initial conditions /
A_s amplitude" to "A_s prefactor: unit-volume factor in the
σ²-to-observable conversion". The shape of the spectrum and the
tree-side σ² running are both closed; the remaining gap is
well-scoped to a single missing factor.

## Cross-references

| File | Role |
|---|---|
| `sigma_squared.py` | Three-route σ² analysis; flags the prefactor gap at §7 |
| `adm_prefactor_verification.py` | Closes σ²_kernel vs K_eff via 2d=6 coordination |
| `alphabet_depth21.py` | Computes σ²(d) on the SB tree; claims "A_s = σ²(d_pivot)²" but missing the 1/(4π² q²) factor |
| `spectral_tilt_reframed.md` | Derives n_s shape from mode-locking; doesn't derive A_s |
| `k_omega_mapping.py` | k↔Ω mapping; normalizes pivot to A_s as input |
| `field_equation_cmb.py` | Numerical field equation; normalizes pivot to A_s as input |
| `a_s_prefactor_check.py` | Numerical probe of A_s predictions across (σ², pivot) grid |
| `statistical_conventions.md` | σ vs % vs "closed" conventions |
