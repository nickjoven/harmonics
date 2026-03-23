# Derivation Index

Reading order and dependency graph for the spectral tilt derivation chain.

## Entry Point

Start with [FRAMEWORK.md](../FRAMEWORK.md) for the synchronization cost framework.
Then [04_spectral_tilt_reframed.md](04_spectral_tilt_reframed.md) for why we moved
from cost functions to mode-locking.

## The Main Line (read in order)

These build on each other sequentially:

### Phase 1: From cost functions to the circle map

| File | Role |
|------|------|
| `cost_function_scan.py` | Shows ALL monotonic cost functions give wrong running sign. Motivates the pivot. |
| `04_spectral_tilt_reframed.md` | Narrative: strip away "cost," keep phase, frequency, coupling. |
| `circle_map.py` | The circle map θ_{n+1} = θ_n + Ω - (K/2π)sin(2πθ_n). Arnold tongues and devil's staircase. Foundation for everything after. |

### Phase 2: The golden ratio structure

| File | Role |
|------|------|
| `golden_ratio_pivot.py` | Zoom into 1/φ region. First observation: the golden ratio sits at the widest gap in the staircase. |
| `stern_brocot_map.py` | **Key insight**: sample the staircase on the Stern-Brocot tree, not a decimal grid. The staircase talks in mediants, not decimals. |
| `phi_squared_zoom.py` | **Central result**: the staircase is exactly self-similar at 1/φ with scaling factor φ². Each bracket carries 1/φ² of parent's winding. Δ(ln\|ΔW\|) = -ln(φ²) per level. |

### Phase 3: Connecting to the CMB

| File | Role |
|------|------|
| `k_omega_mapping.py` | **The mapping**: staircase provides exact scale-invariance; the k↔Ω mapping provides the tilt. rate = 0.0365 levels/e-fold. Observable universe samples 2.2 Fibonacci levels. Amplitude A_s places pivot at level ~21 (F₂₁ = 17711). |
| `superharmonic_regime.py` | The non-Fibonacci rationals within each bracket: overtone structure. Same fractal at sub-Fibonacci zoom. |
| `staircase_geometry.py` | Three 3D representations: Arnold tongue surface W(Ω,K), hyperbolic disk (Stern-Brocot as Farey tessellation of H²), curvature landscape. |

### Phase 4: Structural foundations

| File | Role |
|------|------|
| `fibonacci_ones.py` | The two 1s in the Fibonacci seed carry positional information. The ψ-mode (eigenvalue -1/φ) creates the alternating convergence. Fibonacci/Lucas are sin/cos of the golden oscillation. |

### Phase 5: Born rule and Planck scale

| File | Role |
|------|------|
| `born_rule_tongues.py` | **Born rule derived**: Δθ ∝ √ε at every tongue boundary (saddle-node universality). The exponent 2 in \|ψ\|² is the geometry of parabolas, not a postulate. |
| `planck_threshold.py` | **Planck scale**: N = 3 minimum self-sustaining loop. Three coupling channels (ℏ, c, G) = three stages. 145.8 Fibonacci levels span Planck→Hubble. |
| `collapse_tongues.py` | **Measurement collapse**: τ ∝ 1/√ε (inverse Born rule). Uncertainty relation τ×Δθ = const. Zeno effect at ε→0. Superposition = quasiperiodic gap. |

### Phase 6: Fidelity bound and unification

| File | Role |
|------|------|
| `09_fidelity_bound.md` | **Self-referential fidelity bound**: unifies MOND transition and wavefunction collapse as self-referential frequency measurement with bounded resolution. RAR shape, collapse duration, uncertainty relation, and Zeno effect all follow from one constraint: the measurement instrument IS the measured dynamics. |

### Phase 7: The observational line

| File | Role |
|------|------|
| `predict_highz.py` | Zero-free-parameter V_circ and f_DM predictions for KLASS, GEKO, CRISTAL. Az9 (Pope+2023) as first test point. |
| `fetch_catalogs.py` | Astroquery/VizieR data acquisition for high-z kinematic surveys. |
| `a0_observable.py` | Extract a₀ from RC100 observables via RAR inversion. |
| `fdm_redshift.py` | Dark matter fraction evolution with redshift in RC100. |
| `rar_high_z.py` | Radial acceleration relation analysis at high-z. |
| `load_rc100.py` | RC100 galaxy catalog loading (100 high-z galaxies with kinematics). |

## Markdown Derivations

| File | Status | Role |
|------|--------|------|
| `01_born_rule.md` | Resolved | Born rule from basin measure + tongue geometry |
| `02_spectral_tilt.md` | Superseded | Original cost function approach (see 04) |
| `03_a0_threshold.md` | Current | MOND acceleration scale from synchronization cost |
| `04_spectral_tilt_reframed.md` | **Current** | Tilt from mode-locking structure (replaces 02) |
| `05_two_forces.md` | Current | Two-force (sync/decoherence) narrative |
| `06_planck_scale.md` | Current | Planck scale from N = 3 self-sustaining threshold |
| `07_measurement_collapse.md` | Current | Collapse as tongue traversal (duration, uncertainty, Zeno) |
| `08_high_z_mond.md` | Current | High-z MOND predictions: a₀(z) = cH(z)/(2π) tested against surveys |
| `09_fidelity_bound.md` | **Current** | Self-referential fidelity bound unifying MOND + collapse (see Phase 6) |

## Supporting / Earlier Work

These are referenced but not on the main line:

| File | Role | Status |
|------|------|--------|
| `spectral_tilt_numerical.py` | Early Michaelis-Menten cost function approach | Superseded by circle map line |
| `mode_locking_spectrum.py` | First attempt at P(k) from Arnold tongues | Superseded by stern_brocot_map |
| `coherence_decoherence.py` | Two-force model (synchronization vs decoherence) | Context for `one_force.py` |
| `one_force.py` | K is both synchronization and decoherence | Feeds into circle map understanding |
| `self_consistent_D_v3.py` | Susceptibility-based fluctuation power | Earlier approach |

## Key Results (the short version)

1. The devil's staircase at 1/φ is **exactly self-similar** with scaling factor φ²
2. This gives a **flat** power spectrum in natural (Stern-Brocot) coordinates
3. The observed tilt n_s - 1 = -0.035 comes from the **k ↔ Ω mapping**
4. rate = (n_s - 1)/(-ln φ²) = 0.0365 Fibonacci levels per e-fold
5. The observable universe samples **2.2 levels** of the hierarchy
6. Amplitude A_s ≈ 2.1×10⁻⁹ places the pivot at **level ~21** (F₂₁ = 17711)
7. The ψ-eigenmode (-1/φ) creates the **alternating approach** from both sides
8. The MOND transition and wavefunction collapse are **the same structure**: self-referential frequency measurement with bounded fidelity (Derivation 9)

## Shared Code

`circle_map_utils.py` — shared constants (PHI, INV_PHI, PHI_SQ, PSI, LN_PHI_SQ),
`winding_number()`, `circle_map_step()`, `fibonacci_sequence()`,
`fibonacci_convergents()`, and `farey_mediants()`.

Imported by: stern_brocot_map, phi_squared_zoom, k_omega_mapping,
superharmonic_regime, staircase_geometry.

Note: `circle_map.py` retains its own implementation (different semantics —
uses mod and tracks total advance). It was the first file written and has
its own internal structure.
