# Framework status map

At-a-glance inventory. One line per item. Full analysis lives in the
referenced files; this is the bird's-eye view to prevent duplicate
work and re-derivation of eliminated content.

Categories:
- **Survives**: structural derivation present, closes at σ level.
- **Floor (structural)**: structural residual confirmed at finite depth.
- **Floor (numerology cloud)**: particle-sector near-matches, no structural basis.
- **Fails**: confirmed numerology with explicit disproof.
- **Eliminated**: noted coincidences or structural attempts tested null.
- **Proposed**: awaiting audit or experimental resolution.
- **Out of class**: absolute scales requiring observational anchor.

---

## Survives (structural, σ-closed)

| Item | Source |
|---|---|
| R = 6·13⁵⁴ (Planck/Hubble hierarchy) | `hierarchy_gaussian_lattice.md` |
| Λ·ℓ_P² = 13⁻¹⁰⁸/12 = 3/R² | `hierarchy_gaussian_lattice.md` |
| Ω partition 1:5:13/19 (total counts) | `baryon_fraction.md` |
| Ω_Λ = 13/19 (0.07σ), Ω_m = 6/19, Ω_c = 5/19 | `baryon_fraction.md` |
| Friedmann form at r = 1 | `k_of_t_friedmann.md` |
| λ_unlock = (4G − π ln 2)/π (Arnold Lyapunov on Z₂ quotient) | `kam_bridge_synthesis.md` |
| Born rule |ψ|² from saddle-node | `born_rule.md`, `a1_from_saddle_node.md` |
| a_0 = cH_0/(2π) from Λ (MOND scale) | `a0_threshold.md` |
| Z₂-pair conservation theorem | `z2_pair_conservation.md` |

## Floor (structural residual at finite Fibonacci depth, 7–11%)

| Item | Residual | Confirmed by |
|---|---|---|
| A_s | 11% / 7.6σ | `a_s_depth_scan.md` |
| Ω_b | 6.8% / 11σ | `omega_b_enumeration.md` |
| Ω_c / Ω_b | 6.9% / 3.1σ | `residual_audit.py` |

Not a single-factor, not scale-import, not a non-integer-depth
artifact; confirmed five ways. Closure requires either framework-
native fractional-weight mechanism, observational revision, or a
structural rule change.

## Floor (particle numerology cloud, 1–3%)

| Item | Residual | Source |
|---|---|---|
| m_H/v = 1/q_2 = 1/2 | 1.7% (12.6σ) | `duty_cycle_dictionary.md` |
| λ_Higgs = 1/(2q_2²) = 1/8 | 3.4% | same |
| α_s/α_2 = q_3³/q_2³ = 27/8 | 3.2% | same |

Same ansatz as confirmed-numerology items below. The 1-3% floor is
numerology ensemble, not structural.

## Fails (confirmed numerology, do not use as building block)

| Item | Disproof |
|---|---|
| sin²θ_W = 8/35 | `sinW_running_check.py` (SM running rules out Planck-scale origin) |
| 1/α_em (tree) = 35 | Same analysis, same issue |

## Eliminated (coincidences or structural-attempt nulls)

| Item | Why eliminated |
|---|---|
| v/M_P ≈ 13⁻¹⁵ (3.1%) | `yukawa_mediant_cascade.py` null; `z_30_substrate_check.py` dead end |
| φ⁻⁸⁰ ≈ v/M_P (5.3%) | Numerical coincidence only |
| 1/(Pythagorean comma)² ≈ K_Greene (0.17%) | `kam_bridge_synthesis.md` §6, no structural route |
| H_inf from framework integers | `h_inf_status.md` (scale-free reframe: out of class) |
| Mean-field Ψ Arnold-tongue structure | `klein_spectrum.py`, `kuramoto_induced_map.py` (Adler-only) |

## Proposed (needs audit or experimental input)

| Item | Upgrade criterion |
|---|---|
| K_STAR¹⁴ = 1/8 (τ-mass chain step 6) | σ(m_τ) < 0.03 MeV at Belle II / BESIII |
| 26:7:1 generation hierarchy | Framework-derived rational exponent a matching observed m_μ/m_e and m_τ/m_μ simultaneously |
| λ_H = 1/q_2³ + 1/228 correction | Framework origin for 228 = 12·19 |
| N_efolds = √5 / rate ≈ 61.3 | Framework-internal derivation independent of observed n_s |
| K_c(F_n/F_{n+1}) closed form | Explicit form beyond asymptotic δ⁻ⁿ scaling |
| XOR-parity proof of 1:5:13 at depth 19 | Direct combinatorial proof on Klein quotient |
| T2#7 measurement arc technical residuals | Iteration-to-time anchor, multi-tongue cascade, continuous K(t) |

## Out of class (absolute scales, anchor-dependent)

| Item | Anchor required |
|---|---|
| H_inf in GeV | H_0 (cosmological anchor) |
| τ_unlock(n) in seconds | H_0 |
| Reheating temperature in K | H_0 |
| Inflation-end time in seconds | H_0 |
| Absolute M_Planck in kg | H_0 |
| Tensor-to-scalar r (absolute) | H_0 + scale factor |
| Absolute lepton/quark/gauge-boson masses | v_EW (particle-sector anchor) |
| ℏ, c, G in absolute units | v_EW |

Ratios within each sector are in class (MacKay-scaling on Z₂ quotient
for cosmology; dimensionless couplings for particles). Absolute values
require **two** observational anchors — one cosmological (H_0), one
particle-sector (v_EW) — whose reduction to one is an open item; see
`anchor_count_audit.md` for the five specific obstructions.

---

## Usage

Adding a new framework prediction? Check this map first. If the
item is in "Fails" or "Eliminated," do not derive again — consult
the listed disproof file for context.

Promoting an item up a category requires satisfying its upgrade
criterion (for Proposed) or the criteria listed in
`numerology_inventory.md` for the stronger retraction classes.

Moving an item down a category requires an explicit finding with a
committed derivation / audit.

## Cross-references

| File | Role |
|---|---|
| `numerology_inventory.md` | full classification analysis, Class 1-5 |
| `retractions_index.md` | flat lookup by item |
| `residual_audit.py` | cosmological C2b floor measurement |
| `particle_sector_audit.py` | particle C2a floor measurement |
| `negative_tests.py` | regression suite for structural claims |
| `anchor_count_audit.md` | two-anchor status and hierarchy-problem context |
