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
| Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19 (combinatorial: Farey + Z₂ rep theory) | `omega_partition_combinatorial.md`, `farey_partition.md`, `baryon_fraction.md` |
| Ω_Λ = 13/19 (0.07σ), Ω_m = 6/19, Ω_DM = 5/19, Ω_b = 1/19 (single-w) | same |
| **Ω_b two-component closure (full Class 5)**: (α, β) = (0, 1), w_- = 1 from sign-rep no-EM, w_+ = 13/14 from cusp-1/2 ground state on X_0(6); zero free parameters at closure level. Predictions: Ω_b = 13/264 (0.12%), Ω_DM = 35/132 (0.06%), Ω_Λ = 181/264 (0.13%) | `omega_b_alpha_beta_closure.md`, `psl2z_subgroup_phase_b.md`, `L1_substrate_cusp_ground_state.md`, `w_plus_formalization.md` |
| Friedmann form at r = 1 | `k_of_t_friedmann.md` |
| λ_unlock = (4G − π ln 2)/π (Arnold Lyapunov on Z₂ quotient) | `kam_bridge_synthesis.md` |
| Born rule |ψ|² from saddle-node | `born_rule.md`, `a1_from_saddle_node.md` |
| a_0 = cH_0/(2π) from Λ (MOND scale) | `a0_threshold.md` |
| Z₂-pair conservation theorem | `z2_pair_conservation.md` |
| **Two-anchor minimality** (H_0 cosmological + v_EW particle) is structural, not a derivation gap; all five anchor-count obstructions reframed/closed | `anchor_count_audit.md` reframe + closure notes; `hierarchy_problem_translation.md`; `path_closures_iter3.md` (D.3 closes #5 structurally) |
| **K=1 ↔ K<1 sector decoupling** (Einstein vs Schrödinger continuum limits) is non-smooth, forces independent anchors per sector | `continuum_limits.md` Parts I/II; `continuity_in_K_nulls.md` N11; `path_closures_iter3.md` |
| **Klein π_1 sector assignment**: cosmological → no-twist, particle → twist; Z_2 rep machinery forces the assignment | `path_closures_iter4.md` (D.1 → Class 5) |

## Floor (structural residual at finite Fibonacci depth)

| Item | Residual | Status | Source |
|---|---|---|---|
| A_s | 11% / 7.7σ | Anchor-side category statement (Instance 7) | `a_s_geometric_proof.md`, `a_s_g1_closure_attempt.md` |
| ~~Ω_b 6.7%~~ → **Ω_b two-component** | 0.12% (full Class 5) | **Promoted Floor → Survives**; L1 closure lifts w_+ value to Class 5 | `omega_b_alpha_beta_closure.md`, `psl2z_subgroup_phase_b.md`, `L1_substrate_cusp_ground_state.md` |
| ~~Ω_c / Ω_b 7.5%~~ | 0.6% (inherits from Ω_b closure) | **Promoted from Floor; full Class 5** | `omega_b_alpha_beta_closure.md` derivative |

A_s remains the only entry in this category after the 2026-04
closure round. The Ω_b row was the Floor's headline entry; per
`omega_b_alpha_beta_closure.md`, the (α, β) = (0, 1), w_- = 1
two-component closure (forced by sign-rep no-EM coupling) is a
Class 5 / Survives candidate at the mechanism+(α,β) level. The
single remaining empirical parameter w_+ ≈ 0.929 sits at the
**Γ_0(6) cusp 1/2 of X_0(6)**, with operating-point representative
13/14 = |F_6|/(q_2·|F_4|) (Class 4+ contingent on Phase C
representative-selection derivation). See
`psl2z_subgroup_phase_b.md` for Direction 4 status.

> **A_s reframe (added 2026-04-25).** Per
> `a_s_g1_closure_attempt.md`, the largest gap (G1
> horizon-crossing amplification) closes against the same
> anchor-import barrier as path (a) (`path_a_walkthrough.md`)
> and as SM hierarchy non-translation
> (`hierarchy_problem_translation.md`). Reading: **A_s = 2.33e-9
> is the framework's complete substrate-side prediction; the
> 11% gap is the inflation-amplification correction, which is
> anchor-side and not currently scoped framework-natively.**
> This is the seventh instance of `vocabulary_is_the_work_pattern.md`.

The hybrid strategy (`Ω_b = (1/19)·|r|²`, `A_s = 2.33·|r|³ × 10⁻⁹`)
matches observation ≤ 1σ for Ω_b and A_s but with different
exponents per observable, no forcing argument for either, and
`|r|` observation-derived rather than framework-native. Per
`hybrid_strategy_audit.md` it is Class 2 numerology, not a Floor
closure. **Superseded for Ω_b by the two-component closure.**

## Floor (particle numerology cloud, 1–3%)

| Item | Residual | Source |
|---|---|---|
| m_H/v = 1/q_2 = 1/2 | 1.7% (12.6σ) | `duty_cycle_dictionary.md` |
| λ_Higgs = 1/(2q_2²) = 1/8 | 3.4% | same |
| α_s/α_2 = q_3³/q_2³ = 27/8 | 3.2% | same |

Same ansatz as confirmed-numerology items below. The 1-3% floor is
numerology ensemble, not structural.

> **Region C Phase B verdict (2026-04-26).** Per
> `numerology_count_phase_b.md`, the 1-3% near-match cloud was
> tested against a permutation null (10⁴ trials, log-uniform
> sampling on the observable range). At all three thresholds
> (0.1%, 1%, 3%), the framework's actual match count is
> statistically consistent with the null at α = 0.05:
> 13/26/31 of 33 observables match within 0.1%/1%/3%; null mean
> 9.5/23.3/27.5; p = 0.13 / 0.20 / 0.07. **Cloud is PIGEONHOLE,
> not signal.** The discriminator (`ansatz_audit_policy.md`
> Step 4 Class 2 default) is calibrated correctly. Future
> near-match closure attempts on these ratios are expected to
> land Class 2 by construction; substrate-structural derivation
> modes (group reps, modular Hecke structure, sign-rep
> monodromy) remain the productive direction.

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
| Twist-map / KAM / cantorus / Lyapunov framings of the ψ_F visualizer | Source inspection confirms gradient descent on a static potential; category error. Mechanism note in `klein_nodal_parity.md` |
| Klein nodal parity (odd-m Möbius vs even-m disjoint arcs at σ=+node) | `klein_nodal_parity.md`: simulator uses Y², which is Z₂-symmetric for all ℓ. The (−1)^ℓ sign flip on Y doesn't survive squaring; dynamics cannot discriminate parity. |
| λ_H = 1/q_2³ + 1/228 correction | `framework_predictions.py:268` and `numerology_inventory.md` Class 1: 1/228 confirmed fitted (not framework-derived); correction removed. Bare identity λ_H = 1/q_2³ = 1/8 remains a declined `bare_k1_identities` entry with 3.4% residual. |

## Proposed (needs audit or experimental input)

| Item | Upgrade criterion |
|---|---|
| K_c(F_n/F_{n+1}) closed form | Explicit form beyond asymptotic δ⁻ⁿ scaling |
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
particle-sector (v_EW). Reduction to one was treated as an open
item in `anchor_count_audit.md` (five specific obstructions); per
`hierarchy_problem_translation.md` and `path_a_walkthrough.md`,
the two-anchor minimum is now read as a **structural feature**
(not a defect to be lifted): the canonical register's prime
support `{2, 3}` cannot reach `15 = 3·5` for the `v/M_P ≈ 13⁻¹⁵`
target, and the SM hierarchy problem (the imported framing under
which "two anchors" looked like a defect) does not translate to
the framework — it lacks the naturalness criterion and quadratic
divergences that make small ratios "problematic" in SM. Re-audit
of the five obstructions per `vocabulary_is_the_work_pattern.md`
Consequence 1 is recommended.

---

## Active multi-session derivations (2026-04-25)

After the "honest landing loop" finding (`klein_bridge_audit_and_probe.md`)
that single-session probes converge on Class 4-mechanism / Class 2-
parameters by construction, the framework's active derivation work
shifted to multi-session structural derivations.

### Closed in 2026-04 round

| Region | Closure status | Outcome |
|---|---|---|
| **D — Sector decoupling** | **Closed** (D.3 → Class 5; D.1 → Class 5) | Anchor obstruction #5 STRUCTURALLY CLOSED via K=1 vs K<1 non-smooth separation; Klein π_1 sector assignment forced by Z_2 rep machinery. See `path_closures_iter3.md`, `path_closures_iter4.md`. |
| **Ω_b (α, β) closure** | **Closed (Tier 1+2)** | Sign-rep no-EM forces w_- = 1; (α, β) = (0, 1) structurally derived; one-parameter w_+ closure to 0.13%. See `omega_b_alpha_beta_closure.md`. |
| **Partition logit form** | **Closed (vocabulary)** | Logit transformation exposes universal q_2 factor in all three sector complements; Λ:DM:b complement integers are 6, 14, 18 = q_2·{q_3, |F_4|, q_3²}. See `partition_logit_form.md`. |
| **Cross-ratio irrep reframe** | **Closed (reframe)** | Multi-candidate ansatz pattern reframed as PSL(2,ℤ) irrep multiplicity; the three w_+ candidates 13/14, 12/13, 14/15 are distinct PSL(2,ℤ) orbits. See `cross_ratio_irrep_reframe.md`. |
| **Direction 4 — PSL(2,ℤ)-subgroup** | **Phase A+B closed; Phase C open** | Γ_0(6) identified as the substrate-preserved subgroup; cusp index = gcd(denom, INTERACT) maps each w_+ candidate to a framework sector; w_+ inhabits cusp 1/2 (q_2 sector) → 13/14. Phase C representative-selection within cusp orbit remains open. See `psl2z_subgroup_phase_a_results.md`, `psl2z_subgroup_phase_b.md`. |

### Currently active

(none — Direction 4 closed, Region C closed)

### Closed in 2026-04-26 second round (Direction 4 Phase C closure)

| Closure | Outcome |
|---|---|
| **L1 (substrate cusp-1/2 ground state)** | **Class 5 closure in recognize mode** per `L1_substrate_cusp_ground_state.md`. Composes MOND smooth crossover (a0_threshold.md) + EM lock-in (baryon_fraction.md) + substrate discreteness (denomination_boundary.md §134) + local linearity. The "soft boundary needs discrete rulers" picture: substrate's grain IS the operational apparatus for the smooth MOND threshold; closest-discrete-to-continuum-min is forced because substrate has no continuum states. |
| **THM (w_+ = 13/14)** | **Class 5 closure** by composition of T1-T7 + L1 per `w_plus_formalization.md`. Ω_b two-component closure becomes fully derived with no remaining empirical parameter at closure level. |

### Closed in 2026-04-26 (Region C Phase B)

| Region | Closure status | Outcome |
|---|---|---|
| **C — Numerology count** | **Closed: PIGEONHOLE** | Per `numerology_count_phase_b.md`: at α=0.05, framework's near-match cloud is statistically consistent with permutation null at all three thresholds (0.1%, 1%, 3%). Honest-landing-loop verdict confirmed. Discriminator is calibrated correctly; further near-match ansatz closure attempts will land Class 2 by construction. |

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
| `numerology_inventory.md` | Full Class 1–5 classification; also the retraction / coincidence lookup (replaces retired `retractions_index.md`) |
| `MANIFEST.yml` | canonical quantitative-claim registry (scorecard + bare_k1_identities + anchors) |
| `hybrid_strategy_audit.md` | Floor residuals vs `|r|^n` closures (Class 2 verdict) |
| `ansatz_audit_policy.md` | Triage policy applied to hybrid closures |
| `anchor_count_audit.md` | two-anchor status and hierarchy-problem context |
