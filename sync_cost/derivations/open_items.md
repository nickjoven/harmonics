# Open Items

Active problems and unclosed derivations. Closed items are listed in a
short appendix at the bottom; the full history is in git.

---

## 1. a₁ ≈ 2.320 (lepton base exponent)

- Fixed-point output of the rational field equation. No closed form.
- Understood as a reading through the Fibonacci backbone — the integer
  conservation law fixes the structural form, a₁ is its projection
  onto the observed lepton masses.
- **What would close it:** high-precision iteration of the field
  equation at the Klein bottle's extended mode tower. Computation,
  not a closed form (Feigenbaum-like).

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

## 12. Cross-sector anchors (heaviest-member walk-sums)

- `committed_walk_masses.py` showed that within each sector the
  generation walk-sums are small integer combinations of (q₂, q₃)
  and match observation to |Δ walk-sum| ≤ 0.5. But the walk-sum
  of the *heaviest* member of each sector — the "anchor" — is
  different per sector and is not predicted by a single formula:
  - top (up-type): walk-sum ≈ 0 (≈ v itself)
  - bottom (down-type): walk-sum ≈ 5 = q₂ + q₃
  - tau (charged leptons): walk-sum ≈ 7 (≈ q₂² + q₃)
  - ν_τ (neutrinos): walk-sum ≈ 36 = (q₂q₃)²
- Each anchor is individually expressible in (q₂, q₃), but no
  single formula takes (sector type) → (anchor walk-sum) across
  all four sectors. Absolute masses therefore need four structural
  inputs (one per sector), not zero.
- The up-type within-sector increments (+6, +7) don't fit a clean
  (q₂, q₃) expression the way the other three sectors do
  (leptons +3, +6; down-type +3, +2; neutrinos +2, +2). The +7 is
  close to q₂³ = 8 but not exactly. This may be a PDG-uncertainty
  artifact on the top anchor or a real mismatch; not yet resolved.
- **What would close it:** either derive a formula that emits
  (0, 5, 7, 36) from (q₂, q₃) + sector type, or accept that the
  framework provides within-sector mass structure plus four
  integer anchors as inputs. Honest outcome is likely the latter.

---

## Recently closed (2026-04)

- **Mass sector**: integer conservation law `depth × |3Q| = k_sector`
  connects to gauge adjoint dimensions via the cross-link identity
  `q₂² − 1 = q₃`, `q₃² − 1 = q₂³` (unique solution (2,3)).
  `mass_sector_closure.md`.
- **Neutrino mass scale and K* circulation**: the K*_Λ vs K*_ν
  oscillation (0.862 from `boundary_weight.md` vs 0.8668 refit from
  the A-2 neutrino tightening) is resolved. `committed_walk_masses.py`
  pins K* to the Ω_Λ value (0.862), writes an explicit walk-sum for
  each of the 12 fermions, and inverts the walk-product formula to
  recover the walk-sum each observed mass needs. The three neutrinos
  land at walk-sums 35.5 / 37.2 / 39.2, rounding to 36 / 37 / 39.
  The heaviest-neutrino value (q₂q₃)² = 36 is recovered from the
  committed K* without any refit, so the A-2 refit was not
  structurally required. Majorana prediction from
  4-traversal self-identification stands. `neutrino_mass_prediction.py`
  still uses the older K* but the conclusion is unchanged.
- **4th generation lepton**: forbidden by the integer law
  (depth × 3 > 9 beyond τ). Old ~7.3 GeV prediction superseded.
  `fourth_generation_revisited.md`.
- **Selection rule, lepton/quark 9/8 factor, sector base pair
  algebraic forms**: all resolved at the structural level by the
  mass sector closure.
- **"depth" overloading**: the symbol `depth` was doing three
  different jobs (integer-law sector index, walk length, Yukawa
  exponent). `committed_walk_masses.py` disambiguates: the
  mass-formula quantity is the *walk-sum*, Σ q_i along the Stern-
  Brocot walk. All 12 fermion walk-sums sit within 0.5 of
  integers at K*_Λ = 0.862.

---

## Items that do not fit the "open/closed" frame

- **Cosmological constant**: conditional on the Klein bottle
  configuration space, the 10¹²¹ ratio is the ratio of torus modes
  to Klein bottle modes (not fine-tuning). The value is
  self-consistent but not independently predicted. See
  `vacuum_energy.md`.
- **Chirality asymmetry** (lepton k squared, quark k linear):
  plausible (different L/R reps) but not formally derived.
