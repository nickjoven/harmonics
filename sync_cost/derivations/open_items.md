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

## 9. sin²θ_W running compatibility

- `sinW_running_check.py` shows the tree-scale rational 8/35 does
  **not** run to the observed 0.2312 at M_Z under SM 1-loop betas:
  sign is wrong, absolute values go negative, matching scale is
  ~54 GeV (not a high scale).
- Either the tree scale is not M_Pl (breaks R = 6×13⁵⁴ as
  Planck/Hubble), or the framework's "running" is the duty-cycle
  K→μ mapping (not SM RG), in which case 1.1% agreement is a fit
  at M_Z, not a high-scale prediction.
- **What would close it:** identify which branch is correct and
  revise either `hierarchy.md` or the 8/35 claim accordingly.

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

---

## Recently closed (2026-04)

- **Mass sector**: integer conservation law `depth × |3Q| = k_sector`
  connects to gauge adjoint dimensions via the cross-link identity
  `q₂² − 1 = q₃`, `q₃² − 1 = q₂³` (unique solution (2,3)).
  `mass_sector_closure.md`.
- **Neutrino mass scale**: depth_ν = (q₂q₃)² = 36, m_ν ~ 17 meV,
  three neutrinos at depths 35/36/37, Majorana from
  4-traversal self-identification. `neutrino_mass_prediction.py`.
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
