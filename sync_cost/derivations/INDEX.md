# Derivation Index

Reading order and dependency graph for the derivation chain.

## Entry Point

Start with [FRAMEWORK.md](../FRAMEWORK.md) for the synchronization cost framework.
Then [spectral_tilt_reframed.md](spectral_tilt_reframed.md) for why we moved
from cost functions to mode-locking.

## The Main Line (read in order)

These build on each other sequentially:

### Phase 1: From cost functions to the circle map

| File | Role |
|------|------|
| `cost_function_scan.py` | Shows ALL monotonic cost functions give wrong running sign. Motivates the pivot. |
| `spectral_tilt_reframed.md` | Narrative: strip away "cost," keep phase, frequency, coupling. |
| `circle_map.py` | The circle map θ_{n+1} = θ_n + Ω - (K/2π)sin(2πθ_n). Arnold tongues and devil's staircase. Foundation for everything after. |

### Phase 2: The golden ratio structure

| File | Role |
|------|------|
| `golden_ratio_pivot.py` | Zoom into 1/φ region. First observation: the golden ratio sits at the widest gap in the staircase. |
| `stern_brocot_map.py` | **Key insight**: sample the staircase on the Stern-Brocot tree, not a decimal grid. The staircase talks in mediants, not decimals. |
| `phi_squared_zoom.py` | **Central result**: the staircase is exactly self-similar at 1/φ with scaling factor φ². Each bracket carries 1/φ² of parent's winding. Δ(ln|ΔW|) = -ln(φ²) per level. |

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
| `born_rule_tongues.py` | **Born rule derived**: Δθ ∝ √ε at every tongue boundary (saddle-node universality). The exponent 2 in |ψ|² is the geometry of parabolas, not a postulate. |
| `planck_threshold.py` | **Planck scale**: N = 3 minimum self-sustaining loop. Three coupling channels (ℏ, c, G) = three stages. 145.8 Fibonacci levels span Planck→Hubble. |
| `collapse_tongues.py` | **Measurement collapse**: τ ∝ 1/√ε (inverse Born rule). Uncertainty relation τ×Δθ = const. Zeno effect at ε→0. Superposition = quasiperiodic gap. |
| `fidelity_calibration.py` | **Fidelity calibration**: resolves C=1 via ε_circle = g_bar/(4πK·a₀). Iteration-to-time: 1 iter = 2π/ω_ref. Stribeck lattice calibration point. |
| `tongue_uncertainty.py` | **Nonlinear corrections**: exact τ×Δθ across full ε range. Sub-Gaussian at large ε. Leading correction ε^(3/2). Conjugate pair (Δθ×λ = 4|μ|) verified. |

### Phase 6: Fidelity bound and unification

| File | Role |
|------|------|
| `fidelity_bound.md` | **Self-referential fidelity bound**: unifies MOND transition and wavefunction collapse as self-referential frequency measurement with bounded resolution. RAR shape, collapse duration, uncertainty relation, and Zeno effect all follow from one constraint: the measurement instrument IS the measured dynamics. |

### Phase 7: Foundations

| File | Role |
|------|------|
| `minimum_alphabet.md` | **Four irreducible primitives**: integers, mediant, fixed-point, parabola. Circle derived from integers + fixed-point (p ≡ 0 in phase space forces R/Z = S¹). All four shown irreducible. QM is the small-ε linearized limit of the tongue dynamics. |

### Phase 8: The field equation

| File | Role |
|------|------|
| `rational_field_equation.md` | **The field equation**: self-consistency condition N(p/q) = N_total × g(p/q) × w(p/q, K₀F[N]) on the Stern-Brocot tree. Exact rational arithmetic forced by alphabet. K=1 is gravity (Einstein via ADM in continuum limit), K<1 is quantum (Schrödinger via linearization). Born rule is population distribution at fixed point. |

### Phase 9: Uniqueness (the capstone)

| File | Role |
|------|------|
| `einstein_from_kuramoto.md` | **Einstein from Kuramoto (QED)**: the rational field equation at K=1, continuum limit, uniquely produces G_μν + Λg_μν = 8πGT_μν. Exact ADM from locked-state Kuramoto statistics. Uniqueness via Lovelock's theorem (1971): no other rank-2 divergence-free tensor exists in 4D. |
| `three_dimensions.md` | **Three dimensions from the mediant**: d=3 is forced, not assumed. Mediant → SL(2,Z) → SL(2,R) in continuum limit. Self-consistent adjacency (geometry defines coupling defines geometry) forces spatial manifold = group itself. dim SL(2,R) = 2²−1 = 3. Complexification via order parameter gives SL(2,C) ≅ Spin(3,1) — Lorentz symmetry. Closes Assumption A1 of Derivation 13. |
| `lie_group_characterization.md` | **SL(2,R) is the unique substrate**: four entrance conditions (arithmetic skeleton from mediant, projective action on P¹, dynamical trichotomy from Iwasawa, Farey-hyperbolic geometry) characterize SL(2,R) uniquely. Bianchi classification eliminates all 3D alternatives. d=3, Einstein, and Lorentz become corollaries of one characterization theorem. |

### Phase 10: The variable denominator

| File | Role |
|------|------|
| `variable_denominator.md` | **Hz with a changing denominator**: cycles per second assumes a fixed second. When time is synchronization rate, the denominator changes between cycles. Total operations = self-referential phase integral, not rate × time. De Sitter fixed point is where Hz stabilizes (orientable). ~19 Hubble cycles completed; Stern-Brocot tree depth bounded by reference stability. Connects fidelity bound to Lloyd's computational bound. |

### Phase 11: Temporal causation

| File | Role |
|------|------|
| `rank1_temporal_causation.md` | **Rank-1 as temporal causation**: the rank-1 Fréchet derivative of U is not an algebraic accident but the linearized expression of causation through a single channel. SO(2) rank-1 → center manifold → scalar bottleneck |r| → ker(DU) is the past, im(DU) is the future. The arrow of time is the rank-1 factorization. |

### Phase 12: The Möbius container

| File | Role |
|------|------|
| `mobius_container.md` | **Bounded container as simulation target**: Kuramoto on a compact non-orientable surface (antiperiodic BC). The Möbius geometry forces self-interference — excitations reflect, accumulate, and lock to rational phase divisions. Odd modes selected by topology. Minimal parameters: N = 3, K > 4γ, any ε > 0. Fully specified simulation with observables. |
| `mobius_kuramoto.py` | Numerical experiment: Kuramoto ring with antiperiodic BC. Phase diagram (N, K/K_c) → locked rational. Comparison with periodic BC (cylinder) to verify odd-mode selection. |
| `coherence_length_mobius.py` | Arm formation: perturbation propagates freely, reflects off twist at t_reflect = Nγ/(2K), snaps to quantized gradient (2n+1)π/N. Confirmed: single arm at K/K_c = 1.5 for N = 3–55. |
| `field_equation_mobius.py` | D11 field equation on Möbius domain: topology breaks scale invariance. Möbius twist suppresses odd-q modes, steepens density slope 2.5×. |

### Phase 13: The Klein bottle

| File | Role |
|------|------|
| `klein_bottle.md` | **Fully closed non-orientable container**. Two antiperiodic directions with XOR parity constraint. 2D field equation collapses 1,764 pairs to exactly 4 modes at (q₁,q₂) = (2,3) and (3,2). Fractions {1/3, 1/2, 2/3} = quark charges + weak isospin. Leptons = boundary (q=1). Time = periodic direction; space = antiperiodic. r ≈ 0.5 is topological equilibrium. Configuration budget structurally safe. Pythagorean connection: octave-fifth tension as minimal fixed point. |
| `klein_bottle_kuramoto.py` | 3×3 simulation: Klein bottle forces 1/3 and 1/4 phase divisions at all coupling strengths. Torus → trivial sync. Aspect ratio independent. |
| `field_equation_klein.py` | 2D field equation with XOR + twist: 1,764 → 4 modes. Population ratio 0.675 ≈ 2/3 under golden input. Only (q=2, q=3) and (q=3, q=2) survive. |
| `physical_correlates.py` | Systematic comparison: {1/3, 2/3} = quark charges (exact), {1/2} = weak isospin (exact), {2, 3} = SU(2), SU(3) ranks (exact). 3 generations from Iwasawa KAN. Leptons = boundary q=1. |
| `dimension_loop.py` | F₃ = F₂² − 1 = 3: the unique Fibonacci identity linking Klein bottle q=3, spatial dimension d=3, and proslambenomenos Λ/3. |
| `coupling_running.py` | β-functions from topology (zero free parameters). α₃/α₂ = 2/3 at 10⁸ GeV (see-saw scale). |
| `normalization_v2.py` | α ∝ q²: α₃/α₂ = 9/4 at 17 TeV (hierarchy scale). Two Klein bottle ratios → two physical scales, linked the way SUSY GUTs link them but without superpartners. |
| `xor_continuum_limit.md` | **The load-bearing computation.** Takes the XOR-filtered tree to K=1 continuum limit. Result: Klein bottle gives O(3) → Pin⁺(3) ≅ SU(2) × Z₂ from the frame bundle, but NOT SU(3) and NOT Yang-Mills. The XOR denominator-parity filter dissolves in the continuum — it is a discrete structure with no smooth analog. Honest negative: the frame bundle route does not produce the Standard Model. Two open paths remain: (1) the physical system is discrete (finite tree IS the configuration space), (2) gauge structure emerges from the mean-field functional F, not the tangent bundle. |
| `discrete_gauge.md` | The two open paths formalized as five binary-outcome computations. Path 1 (discrete is physical): anomaly cancellation from charges, depth sweep vs β-ratio, tongue overlap vs structure constants. Path 2 (gauge from F): Jacobian at 4-mode fixed point, Z₂ algebra generation. Three immediate (anomaly, depth sweep, Jacobian), two subsequent. |
| `discrete_gauge_resolution.md` | **The verdict.** All five D21 computations complete. Path 2 (gauge from F) closed: Jacobian rank-1, Z₂ stays Z₂. Path 1 (discrete is physical) partially confirmed: anomaly cancellation exact, Z₆ = center(SU(2)×SU(3)) from GCD, confinement asymmetry (q=2 open, q=3 locked) from XOR. But tongue overlaps abelian, depth sweep doesn't match β-functions. The Klein bottle determines charges, center, and confinement pattern — the kinematics of gauge theory — but not the dynamics (Yang-Mills). The gauge structure is discrete, not continuum. |
| `gauge_sector_lovelock.md` | **Yang-Mills from the Klein bottle.** The gauge-sector analog of D13 (Lovelock). Center Z₆ + Cartan classification → SU(3) × SU(2) × U(1) uniquely. Utiyama's theorem + second-order + Lorentz invariance → Yang-Mills uniquely. Same logical structure as Einstein from Lovelock: classification theorem applied to topological premises. Closes the dynamics gap from D41. |
| `gell_mann_nishijima.md` | **Q = T₃ + Y/2 derived from geometry.** The factor 1/2 is the order of the y-reflection in the Klein bottle identification (0,y)~(1,1-y). T₃ from the twist (antiperiodic direction), Y from the periodic direction. At the identification boundary, the reflection y→1−y has order 2, so its generator on charge-Y states is Y/2. The full SM charge table follows from topology alone. Closes the GNN gap from D42. |
| `higgs_from_tongue_boundary.md` | **Electroweak symmetry breaking from the tongue boundary.** The Higgs doublet is the tongue boundary mode of the open q=2 fiber (Y=1 forced by neutral-VEV requirement + GNN). The Mexican hat potential is the universal saddle-node normal form at the Arnold tongue boundary (D1, D7). Tachyonic mass from the system living on the gap side (r≈0.5 equilibrium). SU(2)×U(1)→U(1)_em breaking, 3 massive + 1 massless gauge bosons, 1 physical Higgs. Structure derived; numerical values (v, m_H, θ_W) require coupling scale. |
| `coupling_scales.md` | **D₀ = 1/2 is not free.** The bare diffusion constant on the Stern-Brocot tree is fixed by its geometry (symmetric binary random walk with unit root spacing). D_eff = (5+3√5)/20 ≈ 0.585. All dimensionless ratios determined. The absolute scale reduces to one dimensionful input (root oscillator frequency) that no mathematical framework can produce. **θ = 0** from Pin⁺(3) on the Klein bottle — the strong CP problem dissolves like the cosmological constant problem (D24). |
| `engineering_targets.md` | Four physical devices from established results (independent of particle physics conjecture). N=3 Möbius resonator (benchtop, immediate), 4-state Klein bottle memory (9 oscillators), bifurcation sensor (critical slowing near K_c), r≈0.5 metamaterial (topologically protected partial coherence). |
| `three_zeros.md` | **Three structurally distinct zeros** in the Klein bottle algebra: (0,0) the forbidden mode, 0 the additive identity, and the zero of the order parameter. Their conflation hides the 1+3 decomposition — one timelike zero (periodic direction) and three spacelike zeros (antiperiodic direction). |

### Phase 14: The cosmological parameters

| File | Role |
|------|------|
| `vacuum_energy.md` | **The cosmological constant problem dissolves**: QFT sums all modes; the Klein bottle has exactly 4. Vacuum energy is not 10¹²⁰ times too large — it was computed on the wrong configuration space. The physical mode count is the XOR-filtered count, not the continuum estimate. |
| `farey_partition.md` | **Ω_Λ = 13/19**: at the Klein bottle's resolution (q = 2, 3), the Farey sequence F₆ has |F₆| = 13 terms. The energy partition between locked (Λ) and unlocked (matter) modes gives Ω_Λ = |F₆|/(|F₆| + 6) = 13/19 = 0.6842. Observed: 0.685 ± 0.007. Residual: **0.07σ**. |
| `hierarchy.md` | **R = 6 × 13⁵⁴**: the Planck/Hubble ratio from Klein bottle arithmetic. Prefactor 6 = q₂ × q₃ = 2 × 3. Base 13 = |F₆|. Exponent 54 = q₂ × q₃³. Computed: 8.45 × 10⁶⁰. Observed: 8.49 × 10⁶⁰. Residual: **0.48%**. |
| `exponent.md` | **Why the exponent is q₂q₃³**: the exponent 54 = 2 × 27 = q₂ × q₃^d where d = 3 is the spatial dimension. Each factor has a specific origin. Λl_P² = 13⁻¹⁰⁸/12. Residual in exponent: **0.1%**. |
| `farey_proof.md` | **Why the Farey partition**: closes the gap from D25. The step from "Klein bottle has {2,3}" to "energy partition = |F_n|/(|F_n| + n)" is derived, not observed. SO(2) structure of the locked/unlocked boundary forces the Farey counting. |
| `mediant_derivation.md` | **The mediant is not an axiom**: the mediant (a+c)/(b+d) is derived as the unique operation satisfying monotonicity-preservation, denominator-additivity, and convergent-stability simultaneously. The configuration space is unique — no other combining rule produces a complete ordered field in the continuum limit. Closes the foundational gap from D10. |

### Phase 15: The observational line

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
| `born_rule.md` | Resolved | Born rule from basin measure + tongue geometry |
| `spectral_tilt.md` | Superseded | Original cost function approach (see 04) |
| `a0_threshold.md` | Current | MOND acceleration scale from synchronization cost |
| `spectral_tilt_reframed.md` | **Current** | Tilt from mode-locking structure (replaces 02) |
| `two_forces.md` | Current | Two-force (sync/decoherence) narrative |
| `planck_scale.md` | Current | Planck scale from N = 3 self-sustaining threshold |
| `measurement_collapse.md` | Current | Collapse as tongue traversal (duration, uncertainty, Zeno) |
| `high_z_mond.md` | Current | High-z MOND predictions: a₀(z) = cH(z)/(2π) tested against surveys |
| `fidelity_bound.md` | **Current** | Self-referential fidelity bound unifying MOND + collapse (see Phase 6) |
| `minimum_alphabet.md` | **Current** | Four irreducible primitives (integers, mediant, fixed-point, parabola); circle derived; QM as small-ε limit |
| `rational_field_equation.md` | **Current** | Self-consistency on Stern-Brocot tree; exact rational arithmetic; K=1 gravity, K<1 quantum; Born rule as fixed-point population |
| `continuum_limits.md` | **Current** | K=1 → Einstein (ADM evolution + constraints); K<1 linearized → Schrödinger (Madelung + Stern-Brocot osmotic velocity) |
| `einstein_from_kuramoto.md` | **Current** | Exact ADM from Kuramoto; uniqueness via Lovelock; Einstein as sole output at K=1 (capstone) |
| `three_dimensions.md` | **Current** | d=3 from mediant → SL(2,R) + self-consistent adjacency; closes Assumption A1; Lorentz from complexification |
| `lie_group_characterization.md` | **Current** | SL(2,R) is the unique continuum substrate: four entrance conditions (arithmetic skeleton, projective action, dynamical trichotomy, Farey geometry) eliminate all alternatives via Bianchi classification. Closes the "why this group?" gap from Derivation 6. |
| `variable_denominator.md` | **Current** | Hz assumes a fixed denominator. When time is synchronization rate, the denominator changes between cycles. Total operations = self-referential integral, not rate × time. De Sitter as the orientable fixed point where Hz stabilizes. ~19 Hubble cycles completed; tree depth bounded accordingly. |
| `rank1_temporal_causation.md` | **Current** | Rank-1 Fréchet derivative as temporal causation: ker(DU) = the past (decayed modes), im(DU) = the future (one active direction), ⟨v,·⟩ = the present (scalar sufficient statistic). Forced by SO(2) rank-1 × codimension-1 × Markov. |
| `mobius_container.md` | **Current** | Bounded Möbius container. Antiperiodic BC forces rational divisions from single perturbation. Coherence length analysis: arms form freely, snap to quantized gradient at t_reflect. N=3 minimum. |
| `klein_bottle.md` | **Current** | Fully closed non-orientable container. XOR parity constraint collapses 1,764 mode pairs to 4 survivors at (q₁,q₂) = (2,3) and (3,2). Population ratio 2/3 = perfect fifth. F₃ = F₂²−1 closes the dimension loop. Charge identification fully resolved: D41 (center Z₆, confinement), D42 (Yang-Mills), D43 (GNN), D44 (Higgs). |
| `xor_continuum_limit.md` | **Current** | The XOR-filtered continuum limit does NOT produce SU(3) or Yang-Mills from the frame bundle. Pin⁺(3) ≅ SU(2) × Z₂ emerges but this is spin/parity, not weak gauge. The discrete XOR filter dissolves in the continuum. Two open paths: discrete-is-physical, or gauge from mean-field F. |
| `discrete_gauge.md` | **Resolved** | Five binary computations specified. All complete — see D41 for verdict. |
| `discrete_gauge_resolution.md` | **Current** | Resolves D20/D21. Path 2 closed (Jacobian rank-1). Path 1 partial: charges, center Z₆, confinement correct; dynamics not yet derived. Gauge structure is discrete, not continuum. Provides premises for D42. |
| `gauge_sector_lovelock.md` | **Current** | Yang-Mills uniqueness from Klein bottle premises via Utiyama + Cartan. Gauge-sector analog of D13 (Lovelock). Closes dynamics gap from D41. SU(3) × SU(2) × U(1) → Yang-Mills, same logical structure as Einstein from Lovelock. |
| `gell_mann_nishijima.md` | **Current** | Q = T₃ + Y/2 derived from Klein bottle identification geometry. The 1/2 is the order of the y-reflection. Closes the GNN input from D42. Full SM charge table from topology alone. |
| `higgs_from_tongue_boundary.md` | **Current** | Higgs mechanism from tongue boundary of open q=2 fiber. Scalar doublet (Y=1), Mexican hat (saddle-node), tachyonic mass (gap side), SU(2)×U(1)→U(1)_em. Structure derived; numerical values require D45. |
| `coupling_scales.md` | **Current** | D₀ = 1/2 from tree geometry. All dimensionless ratios determined. One dimensionful input irreducible. θ = 0 from Pin⁺(3) non-orientability. |
| `engineering_targets.md` | **Proposed** | Four physical devices from established results (independent of particle physics conjecture). N=3 Möbius resonator (benchtop, immediate), 4-state Klein bottle memory (9 oscillators), bifurcation sensor (critical slowing near K_c), r≈0.5 metamaterial (topologically protected partial coherence). |
| `three_zeros.md` | **Current** | Three structurally distinct zeros in the Klein bottle algebra. Conflation hides 1+3 decomposition: one timelike zero (periodic) + three spacelike zeros (antiperiodic). |
| `vacuum_energy.md` | **Current** | Cosmological constant problem dissolves: QFT sums all modes, Klein bottle has exactly 4. Vacuum energy computed on wrong configuration space. |
| `farey_partition.md` | **Current** | Ω_Λ = |F₆|/(|F₆| + 6) = 13/19 = 0.6842 vs observed 0.685 ± 0.007. Residual 0.07σ. |
| `hierarchy.md` | **Current** | R = 6 × 13⁵⁴ ≈ 8.45 × 10⁶⁰ vs observed 8.49 × 10⁶⁰. Prefactor from q₂q₃, base from |F₆|, exponent from q₂q₃³. Residual 0.48%. |
| `exponent.md` | **Current** | Exponent 54 = q₂ × q₃^d derived. Λl_P² = 13⁻¹⁰⁸/12. Residual in exponent 0.1%. |
| `farey_proof.md` | **Current** | Farey partition derived (not observed): SO(2) structure at locked/unlocked boundary forces Farey counting. Closes D25 gap. |
| `mediant_derivation.md` | **Current** | Mediant derived as unique operation satisfying monotonicity-preservation + denominator-additivity + convergent-stability. Configuration space is unique. Closes D10 foundational gap. |
| `denomination_boundary.md` | **Current** | Three open questions unified: denomination boundary = devil's staircase in K-space. Staircase is variational minimum (brachistochrone). Pythagorean comma = 19 = Ω_Λ denominator. XOR asymmetry: q=2 open, q=3 locked = confinement. Klein bottle topology inverts mode hierarchy (torus: 1/1 dominates; Klein: 1/3 dominates). GCD as gauge transformation gives Z₆ = center(SU(2)×SU(3)). |
| `speed_of_light.md` | **Current** | c as gate propagation speed of the coherent medium. Phase coincidence = gate. K=1 = maximum gate correlation = maximum speed. Nilpotent N₊ = constant velocity (N₊²=0 → no acceleration). Coherence = speed differential. Lorentz boost = relative phase gradient. |
| `minkowski_signature.md` | **Current** | **(3,1) signature derived from phase-state observability.** Four phase states {A,B,C,D} from {locked,unlocked}². D (both unlocked) is dark — coupling averages to zero. Three observable + one dark = signature (3,1). i² = −1 from double half-twist on Klein bottle. Closes the signature assumption in D13 (ADM). Same 4−1=3 as spatial dimensions, generations, and coupling stages. D state = time = virtual particles = measurement process. |
| `cosmological_cycle.md` | **Current** | **The universe passes the baton.** The gap-twin at 18.7% spacetime duty (57.2% per dimension) has the same physics at reduced amplitude. The stick-slip boundary sweeps modes from tongues to gaps as K decreases. The Klein bottle half-twist swaps sector labels at each handoff. De Sitter equilibrium at Ω_Λ = 13/19 is the fixed point of the exchange. 12 gap channels (φ(13)=12) mediate the transfer. The cosmological cycle is a two-voice round in the key of 13/19. |
| `conservation_computability.md` | **Derived** | **Conservation as computability.** S¹ compact → |r| ≤ 1 → K_eff ≤ 1 → circle map invertible → information conserved → fixed point exists → physics computable. "Matter cannot be created or destroyed" = "the circle is compact" = "integers + fixed-point → R/Z." K>1 is not high energy but no physics (map folds, fixed point undefined). Force F = K sin(Δθ) IS information transfer. GCD reduction eliminates 39% of positions (ancestors cover them). Stern-Brocot tree as persistent content-addressed append-only structure whose root hash is the fixed point. Verification O(1), computation O(n) — asymmetry is topological (Brouwer). |
| `figure_eight.md` | **Derived** | **The figure-eight topology.** Klein bottle self-intersection in 3D = lemniscate. Loop 1 = sector (2,3), Loop 2 = sector (3,2). Crossing point = D state = present moment. sin²θ_W = 8/35 is the crossing probability. Photon = crossing event, Z = near-miss, W± = charged crossings. J² = −I from double half-twist (i² = −1 is the twist operator squared). The fixed point IS the figure-8, not a point on it. CPT: C = loop swap, P = mode swap, T = twist reversal; CPT = identity. The figure-8 is ∞: finite structure, infinite traversal. |
| `boundary_weight.md` | **Derived** | **The boundary weight dissolves n=5 vs n=6.** Ω_Λ(w) = (11+2w)/(16+3w) where w ∈ [0,1] is fractional weight of q=6 modes. dΩ_Λ/dw = −1/(16+3w)² < 0: strictly monotone, unique w* for any observed Ω_Λ. Topology predicts Ω_Λ ∈ [0.6842, 0.6875]; dynamics give w* = 0.83 at K* = 0.862. Effective mode count 12.66, effective depth 5.83. Resolves proofreader gaps #1 (n not integer), #7 (Ω_Λ from fixed point), #8 (uniqueness from monotonicity). The "13" is the w=1 limit; the physical answer is 12.66. |
| `stribeck_vortex.md` | **Derived** | **The Stribeck vortex regime map.** Vortex velocity field v(r) composed with Stribeck friction K(v) yields radial coupling profile K(r) with overcritical core (K > 1, fold, reversed energy flow) and subcritical annulus (K < 1, mode-locked, forward flow). Critical radii from quadratic; r_c,inner × r_c,outer = r_core² (Vieta). Fold measure μ = arccos(1/K)/π = stop band fraction (Bragg identification K = sec(κΛ), exact). Fold present at all K > 1; chaos generic but not uniform. D36 reconciled: local K > 1 compatible with global K_eff ≤ 1. Gravity sector has complementary structure: K_eff = √(1-2M/r) → 0 at horizon (decoherence), not K > 1 (overcoupling). K > 1 regime exists only in material systems. Photonic crystal: K_stat = 1.636, μ(0) = 29.1% (arXiv:2601.21704). |

### Phase 16: The denomination boundary

| File | Role |
|------|------|
| `denomination_boundary.md` | **The three open questions are one**: entropy-vs-energy boundary = devil's staircase in K-space. Discrete substrate = K < 1 truncation. Degeneracy resolution = mediant, not perturbation theory. **The staircase is a brachistochrone**: path of least synchronization cost through frequency space. Plateau fraction maximized (10%→64% as K: 0.3→0.99, TV invariant at 1.0). Square-staircase spectral gap = periodicity vs mode-locking (integer harmonics 1/n vs rational harmonics (K/2)^q). |
| `denomination_boundary.py` | Intermittency test at F_n = 3.0 and mode-lock onset sweep. Intermittency confirmed (σ = 0.08). |
| `mediant_test.py` | **Mediant resolution confirmed**: all 6 Stern-Brocot mediants present at parent degeneracy points. Two mediants (3/5, 4/3) exceed parents — tree selects the resolution mode. |
| `staircase_spectrum.py` | Fourier analysis of classical waveforms vs devil's staircase (static). |
| `staircase_spectrum_v2.py` | **Dynamic spectrum**: circle map time series at K = 0–1, square vs staircase comparison, variational (shortest path) test. Plateau fraction and total variation computed. |
| `pythagorean_comma_variational.py` | **The comma is the Klein bottle's failure to close**: 12 fifths + 7 octaves = 19 transitions = Ω_Λ denominator. The 19 in 13/19 is the comma cycle length. Cost ratio → 2 at K → 1. The comma is irreducible because the Stern-Brocot tree has no loops. |
| `waveform_evolution.py` | Waveform progression: sine → clipped → trapezoidal → subharmonic limit cycle. |
| `stable_waveform.py` | Coupling sweep showing stable locked orbits in the mode-locking window. |
| `stable_waveform_v2.py` | Refined: spatial progression at high coupling, element 1–5 waveform comparison. |
| `tongue_overlap_structure.py` | D21-B: Tongue overlap test. The XOR filter produces abelian vertex structure only — mediant(1/3,2/3)=1/2 but self-coupling is forbidden. |
| `path_holonomy.py` | Transport group between {1/2,1/3,2/3} generates SL(2,Z) (non-abelian, infinite). Triangle loop holonomy trivial, but paths non-commutative. |
| `fiber_bundle.py` | **GCD as gauge transformation**: scaling doesn't commute with mediant. GCD mod 3 gives Z₃, mod 2 gives Z₂. Full structure Z₆ = center(SU(2)×SU(3)). |
| `z6_algebra.py` | D21-E v1: Fiber flat under field equation (tongue widths use reduced denominators). |
| `z6_algebra_v2.py` | D21-E v2: Depth-dependent tongue widths — still flat (product structure, rank-1 Jacobian). |
| `z6_algebra_v3.py` | D21-E v3: XOR filter locks the fiber — twist sign frozen because allowed scalings preserve parity. |
| `xor_asymmetry.py` | **XOR asymmetry = confinement**: q=2 (even) fiber open → SU(2) unconfined. q=3 (odd) fiber locked → SU(3) confines. Asymmetry ratio = K/2 = the mediator mode. |
| `slip_structure.py` | Slip is not flat: velocity histogram shows sub-plateaus at mediant frequencies. Dwell time graded by Stern-Brocot depth. |
| `klein_slip_structure.py` | **Klein bottle reshapes mode occupation**: torus locks to 1/1 (59%), Klein locks to 1/3 (48%). Topology inverts the hierarchy. The slip is where particle physics lives. |

### Phase 17: The speed of light

| File | Role |
|------|------|
| `speed_of_light.md` | **c derived as gate propagation speed**: the speed of light is the rate at which phase coincidence (the "gate of observability") sweeps through a coherent oscillator medium. Pendulums in phase have coordinated zero-crossings; a photon rides the wave of gate-openings. c is maximum because K=1 gives maximum gate correlation. c is constant because it is a structure constant of sl(2,R) (ratio of parabolic to compact generator), preserved by all SL(2,C) transformations. Coherence = zero speed differential = same rest frame. The Lorentz boost is relative phase gradient between coherent domains. Connects to Iwasawa N-factor (Derivation 6), complexification quotient (Derivation 14). |

### Phase 18: The Stribeck vortex

| File | Role |
|------|------|
| `stribeck_vortex.md` | **Local K > 1 reconciled with global K_eff ≤ 1**: the Stribeck vortex regime map K(r) = K(v(r)) produces radial structure — overcritical core surrounded by subcritical annulus. Critical radii from quadratic; r_c,inner × r_c,outer = r_core² (Vieta). Fold at all K > 1; chaos generic but mode-locking windows persist. Triangle inequality on S¹ preserves global self-consistency. |
| `stribeck_vortex_regime.py` | Core computation: regime map K(r), critical radii vs ℓ, fold measure profile, Lyapunov exponent, global order parameter |r| ≤ 1 confirmation, photonic crystal K-mapping (Δn=0.5, f=0.15, Q=50 → K_stat=1.636, μ(0)=29.1%), near-criticality saddle-node scaling. |
| `stribeck_vortex_gaps.py` | Gap-closing: exact quadratic formula for r_c (6-digit match to bisection), Vieta verification (product = r_core² across all ℓ), fine Lyapunov profile revealing mode-locking windows above K = 1, outer crossing scaling (linear in ℓ). |
| `bragg_circle_map.py` | **Bragg → circle map identification**: K = sec(κΛ). Stop band fraction = fold measure μ = arccos(1/K)/π — exact to 4 digits. Reversed energy flow IS the fold. Hexagonal 2D extension derives K_stat = 1 + 2(Δn)²(1 + fπ/√3). |
| `schwarzschild_K_profile.py` | **Gravity sector K(r)**: four candidate profiles near Schwarzschild compared. K_eff = √(1-2M/r) → 0 at horizon (decoherence), not → ∞ (overcritical). D36 absolute in gravity. K > 1 exists only in material systems. Complementary structure to Stribeck vortex. |

### Proof Chains (geometric proof format)

| File | Role |
|------|------|
| `PROOF_A_gravity.md` | **Polynomial → General Relativity**: 8 propositions. Counting → mediant → Stern-Brocot → field equation → d=3, SL(2,R) → ADM → Lovelock → Einstein. Two inputs (energy conservation, stability), one output. |
| `PROOF_B_quantum.md` | **Polynomial → Quantum Mechanics**: 5 shared + 6 quantum propositions. Same start, diverges at K<1. Unlocked oscillators → Madelung → Schrödinger. Parabola → √ε scaling → Born rule. The subcritical limit of the same equation whose critical limit gives GR. |

The third proof chain — **The Bridge** (cosmological parameters connecting both legs) — lives in [proslambenomenos/PROOF_C_bridge.md](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md). It derives Ω_Λ = 13/19, R = 6×13⁵⁴, and a₀ from the Klein bottle topology + Kuramoto critical coupling.

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
9. The entire framework follows from **four irreducible primitives**: integers, mediant, fixed-point equation, parabola. The circle is derived (integers + fixed-point). QM is the linearized small-ε limit. (Derivation 10)
10. The **field equation** is N(p/q) = N_total × g(p/q) × w(p/q, K₀F[N]) on the Stern-Brocot tree in exact rational arithmetic. K=1 → Einstein (continuum limit), K<1 linearized → Schrödinger. Born rule is the population distribution at the fixed point. (Derivation 11)
11. Both **continuum limits derived structurally**: K=1 gives ADM evolution equations and constraints via coherence tensor differentiation; K<1 gives Schrödinger via Madelung transform with quantum pressure from Stern-Brocot osmotic velocity. One equation, one parameter, three regimes, two PDEs. (Derivation 12)
12. The K=1 continuum limit **uniquely produces Einstein**: Lovelock's theorem (1971) says G_μν + Λg_μν is the only divergence-free rank-2 tensor in 4D built from the metric and its first two derivatives. The Kuramoto→ADM dictionary satisfies all four Lovelock premises. No other field equation is possible. (Derivation 13)
13. **d=3 is forced by the mediant**: fractions have two components → SL(2,Z). Continuum limit → SL(2,R). Self-consistent adjacency forces space = group. dim SL(2) = 2²−1 = 3. Complexification via order parameter → SL(2,C) ≅ Spin(3,1) gives Lorentz. No assumption needed. (Derivation 14)
14. **SL(2,R) is the unique substrate**: four entrance conditions — arithmetic skeleton (SL(2,Z) from mediant), projective action on P¹(R), dynamical trichotomy (Iwasawa KAN), Farey-hyperbolic geometry — characterize SL(2,R) among all connected real Lie groups. Bianchi classification eliminates all 3D alternatives. SU(2) fails (compact, no split/nilpotent sectors). SL(2,C) fails minimality (complexification, dim 6). Heisenberg fails (no arithmetic skeleton, no projective action). d=3, Einstein, and Lorentz become corollaries. (Derivation 15)
15. **The frequency distribution determines itself**: g* = h(g*). The population density at the field equation's fixed point, when fed back as the input distribution, reproduces itself. g* converges from arbitrary initial conditions. **Zero free parameters. Zero free functions.** ([rfe engine](https://github.com/nickjoven/rfe))
16. **Numerical verification**: the field equation at depth 10 produces n_s = 0.963–0.966 vs Planck 0.9649 (Δ < 0.2%). The asymptotic density slope is -0.001 per level — **scale invariance is preserved** by self-consistency. ([`field_equation_cmb.py`](field_equation_cmb.py))
17. **a₀ corrected**: a₀ = c·H₀/(2π) / √g*(1/φ) = 1.25×10⁻¹⁰ m/s² vs observed 1.2×10⁻¹⁰ (4% residual, down from 15%). The correction comes from the fidelity bound's √(g_bar/a₀), where g* at 1/φ = 0.697 modulates the transition.
18. **Ω_Λ = 13/19 = 0.6842** from Farey partition at Klein bottle resolution. Observed: 0.685 ± 0.007. Residual: **0.07σ**. (Derivation 25)
19. **R = 6 × 13⁵⁴ ≈ 8.45 × 10⁶⁰** — Planck/Hubble ratio from Klein bottle arithmetic. Observed: 8.49 × 10⁶⁰. Residual: **0.48%**. (Derivation 26)
20. **Λl_P² = 13⁻¹⁰⁸/12** — cosmological constant in Planck units. Exponent 108 = 2 × q₂q₃³ derived from spatial dimension and Klein bottle denominators. Residual in exponent: **0.1%**. (Derivation 27)

## The scorecard

### Cosmological and structural

| Prediction | Computed | Observed | Residual | Source |
|---|---|---|---|---|
| n_s (spectral tilt) | 0.963–0.966 | 0.9649 ± 0.0042 | **< 0.2%** | D4, rfe |
| Born rule exponent | 2 | 2 | **exact** | D1, D9 |
| τ × Δθ (uncertainty) | 1.000000 | — | **exact** | D7, D9 |
| a₀ (MOND scale) | 1.25 × 10⁻¹⁰ m/s² | 1.2 × 10⁻¹⁰ | **4%** | D3, D8, rfe |
| d (spatial dimension) | 3 | 3 | **exact** | D14 |
| Lorentz symmetry | Spin(3,1) | SO⁺(3,1) | **exact** | D14, D15 |
| Spacetime signature | (3,1) | (3,1) | **exact** | D32 |
| Ω_Λ (dark energy) | 13/19 = 0.6842 | 0.685 ± 0.007 | **0.07σ** | D25, D28 |
| R (Planck/Hubble) | 6 × 13⁵⁴ = 8.45 × 10⁶⁰ | 8.49 × 10⁶⁰ | **0.48%** | D26 |
| Λl_P² | 13⁻¹⁰⁸/12 | ~10⁻¹²² | **0.1% in exp** | D27 |
| N_efolds | 61.3 ± 0.7 | TBD | CMB-S4, ~2028 | D10 |

### Gauge sector and particle physics

| Prediction | Computed | Observed | Residual | Source |
|---|---|---|---|---|
| Gauge group | SU(3) × SU(2) × U(1) | SU(3) × SU(2) × U(1) | **exact** | D41, D42 |
| SM anomaly cancellation | all 6 = 0 | all 6 = 0 | **exact** | D41 |
| sin²θ_W (Weinberg) | 8/35 = 0.2286 | 0.2312 | **1.1%** | D33, D37 |
| m_H/v (Higgs ratio) | 1/2 | 0.508 | **1.6%** | D33, D44 |
| λ (Higgs quartic) | 1/8 = 0.125 | ~0.13 | **4%** | D33 |
| α_s/α_2 (coupling ratio) | 27/8 = 3.375 | 3.488 | **3.2%** | D33 |
| θ (strong CP) | 0 | < 10⁻¹⁰ | **exact** | D45 |
| Q = T₃ + Y/2 (GNN) | derived | confirmed | **exact** | D43 |

Free parameters: **0**. Free functions: **0**. Dimensionful inputs: **1** (root oscillator frequency / v = 246 GeV).

## Shared Code

`circle_map_utils.py` — shared constants (PHI, INV_PHI, PHI_SQ, PSI, LN_PHI_SQ),
`winding_number()`, `circle_map_step()`, `fibonacci_sequence()`,
`fibonacci_convergents()`, and `farey_mediants()`.

Imported by: stern_brocot_map, phi_squared_zoom, k_omega_mapping,
superharmonic_regime, staircase_geometry.

Note: `circle_map.py` retains its own implementation (different semantics —
uses mod and tracks total advance). It was the first file written and has
its own internal structure.
