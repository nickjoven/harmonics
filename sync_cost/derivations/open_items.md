# Open Items

Active problems and unclosed derivations. Closed items are listed in a
short appendix at the bottom; the full history is in git.

---

## 1. a₁ ≈ 2.320 (lepton base exponent)

- a₁ is a *fitted continuous exponent* in the Fibonacci power-law
  mass formulation (formulation B: m ∝ (3/2)^{a_1 n}, (5/3)^{a_1 n},
  etc. per sector). Each sector gets its own fitted a_1.
- A discrete walk interpretation was tested and ruled out:
  `committed_walk_masses.py` attempted a walk-sum reading at the
  committed K* = 0.862, but the walk-independent quantity
  `log(m/v)/log(K*/2)` gives messy non-integer within-sector deltas
  (leptons land at +3.35/+6.34, not clean +3/+6) and the
  `a₂/a₁ = 3/2` ratio is not recovered from the walk-product formula
  at all. The "nearly-integer" appearance in that script was an
  artifact of specific naive walk choices.
- The item remains open, but the scope is now wider: this is a
  symptom of the mass sector's deeper issue — see the new
  "Continuous mass formulation" item below. a₁ will only get a
  principled value once the mass formula is derived from the field
  equation directly, rather than fitted per sector.

## 2. Quark masses at physical scales

- Tree-scale base pairs derived (`sector_base_pairs.py`).
- QCD running from tree scale through flavor thresholds is standard
  SM physics applied to these boundary conditions; not yet run
  end-to-end.
- **What would close it:** execute the RG pipeline with the
  tree-scale values as boundary conditions, compare to PDG pole
  masses.

## 3. A_s amplitude (scalar power spectrum)

- Mapping rate derived. Absolute amplitude requires v = 246 GeV
  (see item 6).
- **What would close it:** solve item 6.

## 4. Cosmological dynamics K(t)

- Friedmann structure identified; K(t) evolution from the field
  equation is not derived.
- Separate problem in the gravity/cosmology sector, not touched by
  the mass sector closure.

## 5. Measurement outcome problem

- Mechanism derived; specific outcome requires inaccessible initial
  condition (Bohmian-status). Likely irreducible.

## 6. One dimensionful scale v = 246 GeV

- Single dimensionful input. Any framework needs one scale for units.
- All dimensionless ratios are derived.

## 7. Planck-scale non-metricity O(l_P/L)

- Prediction from Gap 1 (Christoffel connection). Not tech-accessible
  with current instruments.

## 8. N_efolds = 61.3 ± 0.7

- Prediction, falsifiable by CMB-S4 (~2028). Independent of all
  other items.

## 9. sin²θ_W running compatibility — CLOSED (reclassified as near-coincidence)

- `sinW_running_check.py` showed the tree-scale rational 8/35
  does not run to 0.2312 at M_Z under SM 1-loop betas from any
  high scale (sign wrong, absolute values go negative, matching
  scale ~54 GeV).
- `sinw_fixed_point.py` tested whether both branches (tree ≠ M_Pl;
  running is K→μ) could be simultaneously true as a fixed point.
  Numerical circle-map tongue widths at K ∈ [0.93, 0.99] give
  α_s/α_2 ratios in [3.66, 3.99] (all above observed 3.488) and
  sin²θ_W in [0.200, 0.214] (all below observed 0.23121). No K*
  reproduces either constraint, so no joint fixed point exists.
- **Resolution:** 8/35 is a **measure-theoretic identity** (Ford
  circle / Gauss-Kuzmin measure of the 1/3 tongue in the
  tongue-filling limit), not a dynamical value at any K. Its 1.1%
  agreement with observed sin²θ_W at M_Z is a numerical
  near-coincidence of the smallest nontrivial rational of the form
  q_a^3 / (q_a^3 + q_b^3), not a derivation via running.
- **Status:** Reclassified. See `sinw_fixed_point.md` for the full
  analysis. The gauge-group derivation in `gauge_sector_lovelock.md`
  (D42) is unaffected — it uses only the center Z_2 × Z_3, not the
  specific sin²θ_W value.

## 10. CKM angles beyond Cabibbo

- θ_12 reproduced to ~3% by arctan√(m_d/m_s) (Gatto-Sartori-Tonin,
  derived as walk overlap, `ckm_from_sl2z.py`).
- θ_13 and θ_23 require full mass-matrix diagonalization — the
  naive sqrt-ratio form is off by factors of 10 and 4.
- **What would close it:** compute the walk overlap at finite tree
  depth with the correct chirality structure.

## 11. Dark twin structure

- Klein bottle's double cover creates a second mode copy. Speculative
  hypothesis: twin sector takes the complement of our gauge budget
  (`dark_twin_formalization.py`).
- Not formally derived.

## 12. Continuous mass formulation

- The framework currently has **two incompatible mass formulations**
  that give different answers:
  - **(A) Discrete walk product** at base (K*/2), with walk-sums as
    integer walk depths along the Stern-Brocot walk.
  - **(B) Fibonacci base power law** at bases (3/2), (5/3), etc.,
    with continuous fitted exponents a_1 per sector.
- Formulation (A) was tested in `committed_walk_masses.py` and
  fails to reproduce within-sector ratios: walk-independent
  log(m/v)/log(K*/2) gives messy non-integer deltas, and the
  a₂/a₁ = 3/2 sector ratio is not recovered from the walk-product
  formula at all.
- The simplest integral formulations were tested in
  `integral_mass_test.py` — four candidate measures on q-space
  (bare exponential, 1/q, 1/q², 1/q³). All four fail: the bare
  exponential saturates after top, and the 1/q^n measures can't
  even reach top's mass starting from q=1.
- Formulation (B) is what gives the famous 0.07% τ/μ and μ/e
  matches, but it uses *continuous fitted exponents per sector*
  and does not yield absolute masses — only ratios within a sector
  once a_1 is fixed.
- The symbol **`depth`** is overloaded across this item. In the
  integer conservation law it's a sector index; in formulation (A)
  it's meant to be the walk length or Σ q_i along the walk; in
  formulation (B) it's the continuous exponent a_1. None of the
  single-formula meanings we have tested work as the mass-formula
  quantity. The overloading is a symptom of the missing continuous
  formulation, not something that can be resolved by picking one
  of the existing meanings.
- **What's missing** is a derivation of the mass formula from the
  field equation directly — likely a 2D phase-space integral, a
  modular/Eisenstein form, an action integral along an explicit
  path, or a spectral trace formula (Selberg-style). Whichever it
  turns out to be, it must yield continuous exponents *naturally*,
  not as fits.
- This item supersedes items 1 and 12 in the previous version
  (fitted a_1 and the heaviest-member "anchor" walk-sums). The
  specific anchor values (0, 5, 7, 36) were artifacts of the naive
  walk choice and the walk-sum-as-depth framing, not structural
  predictions.

## 13. Planck-epoch saturation; post-Planck story is open

- `first_bifurcation_volume.py` established that the Kuramoto flow
  contracts phase-space volume at rate `div(f) = -K N r²` starting
  at the first bifurcation (zero before, nonzero after). This IS
  the arrow of time at the dynamical level — T-symmetry holds for
  `K < K_c` and breaks at `K = K_c`.
- `first_bifurcation_volume.py` also ruled out option (A) — the
  unlocked oscillators within the same Kuramoto ensemble do not
  expand to compensate the locked cluster's contraction. Both
  populations contract; neither carries away the other's volume.
- `pointwise_horizon_match.py` did a proper pointwise comparison
  of `|div(f)|` against the horizon growth rate `dS_H/dt` across a
  ΛCDM cosmic history from Planck time to today, using a consistent
  time dictionary (everything in Planck units, scale factor `a` as
  the integration variable, ΛCDM `H(a)` with `Ω_Λ = 13/19`,
  `Ω_m = 6/19`). Result:
  - **At the Planck epoch (first bifurcation)**: the ratio
    `|div(f)| / dS_H/dt ≈ 0.11`, i.e. O(1). Within an O(1) numerical
    coefficient the Kuramoto dissipation rate equals the horizon
    absorption rate. **This is a genuine pointwise saturation at
    the Planck epoch.**
  - **Post-Planck**: the ratio grows by ~60 decades, reaching
    ~10⁶⁰ by today. Under the N(a) = 1/H(a)² ansatz, the Kuramoto
    side vastly overshoots the horizon side at late times.
- The earlier "integrated saturation" claim in
  `compensation_channel_test.py` has been **partially retracted**
  (see the new header block in that file). The integrated match
  there was a global coincidence between two integrals computed in
  different "time" variables (K-sweep vs cosmic time), not a
  genuine cosmological saturation. The Planck-epoch point match
  survives as the real finding.
- **Honest current status:**
  - At the first bifurcation, the Kuramoto dissipation rate is
    matched to the horizon absorption rate up to O(1). The
    holographic budget is set at Planck time. Area scaling wins
    at Planck.
  - After Planck, the rates diverge under the simple ansatze
    tested. Either the mode count N(a) follows a different (not
    holographic) scaling at later epochs, or the Kuramoto
    description is localised to the first bifurcation and doesn't
    extend to later "bifurcations" as independent events.
- **What would close it**: a derivation of `N(a)` from the
  framework's field equation directly, not an ansatz. The current
  attempts (`N = R`, `N = R²`, `N = R³`) all fail in different
  ways — the first two by integrated mismatch, the third by
  cosmological-time divergence. The right N(a) should emerge from
  counting XOR-surviving modes on the Klein bottle at each epoch,
  which depends on the field equation's time evolution.
- Item 4 (`K(t)` cosmological profile) remains a prerequisite, but
  the problem is now more specific: we need both `K(t)` and `N(t)`
  together, with the constraint that their product reproduces the
  horizon growth rate at all epochs, not just Planck.

---

## Recently closed (2026-04)

- **Mass sector**: integer conservation law `depth × |3Q| = k_sector`
  connects to gauge adjoint dimensions via the cross-link identity
  `q₂² − 1 = q₃`, `q₃² − 1 = q₂³` (unique solution (2,3)).
  `mass_sector_closure.md`.
- **Neutrino K* circulation**: the K*_Λ vs K*_ν oscillation (0.862
  from `boundary_weight.md` vs 0.8668 refit from the A-2 neutrino
  tightening) was a symptom of the two incompatible mass
  formulations (see the new "Continuous mass formulation" open
  item). Neither K* value is structurally privileged until the
  right mass formulation is identified — the earlier claim that
  `committed_walk_masses.py` recovers (q₂q₃)² = 36 from committed
  K* is retracted; that 36 was another walk-choice artifact. The
  Majorana neutrino prediction from 4-traversal self-identification
  on the Klein bottle stands as a separate topological result, not
  dependent on the mass formula.
- **4th generation lepton**: forbidden by the integer law
  (depth × 3 > 9 beyond τ). Old ~7.3 GeV prediction superseded.
  `fourth_generation_revisited.md`.
- **Selection rule, lepton/quark 9/8 factor, sector base pair
  algebraic forms**: all resolved at the structural level by the
  mass sector closure.

---

## Items that do not fit the "open/closed" frame

- **Cosmological constant**: conditional on the Klein bottle
  configuration space, the 10¹²¹ ratio is the ratio of torus modes
  to Klein bottle modes (not fine-tuning). The value is
  self-consistent but not independently predicted. See
  `vacuum_energy.md`.
- **Chirality asymmetry** (lepton k squared, quark k linear):
  plausible (different L/R reps) but not formally derived.
