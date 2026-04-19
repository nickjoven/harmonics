# Statistical conventions for session closure docs

This doc defines the operational meaning of σ-statements,
%-statements, and "closed" used in the seven session closure
docs. Where a doc's wording is loose, this defines the strict
sense.

## σ — observational z-score, default

**Operational definition.** Unless explicitly noted otherwise,
"X σ" in session docs means

    σ = |prediction − observation_central| / observation_uncertainty

where `observation_uncertainty` is the 1-σ measurement error
quoted by the source experiment (e.g. PDG, NuFIT, Planck). The
prediction is treated as exact (no theory-side uncertainty
propagated).

This is the **observational z-score**: a measure of how many
standard deviations the framework's point prediction sits from
the observed mean. NOT a Bayesian posterior, NOT a goodness-of-
fit χ² over multiple observables, and NOT a confidence interval.

When predictions DO have uncertainty (e.g. from `K*` propagation),
docs that compute combined σ explicitly state so. Default
assumption: prediction is exact unless flagged.

## %-statement — relative deviation

**Operational definition.** "Within X%" means

    relative deviation = |prediction − observation| / observation

reported as a percentage. NOT divided by uncertainty. Used when
the observation has no quoted uncertainty, or when we want a
scale-free comparison independent of measurement error.

Example: PMNS θ_12 = 30° vs observed 33.5° → (33.5−30)/33.5 ≈
10%. The "12%" stated in `mixing_angle_audit.md` is the rounded
version.

## "Closed" — three operational meanings

The word "closed" appears in session docs with three distinct
senses. Each closure should be read with its corresponding
sense.

### (C-numerical) "Closed at X σ"

Numerical match between framework prediction and observation,
with z-score X (per the σ definition above). The closure stands
or falls on the observation matching the prediction within the
quoted measurement uncertainty.

Examples in this session:

- Down-type factor 6: PDG ratio 5.989 ± 0.271; framework predicts
  6 exactly; z-score = 0.04 σ. **(C-numerical)**.
- Ω_b: Planck 0.0493 ± 0.0003; framework predicts 0.04932 (with
  |r|² = 0.937 correction); z-score = 0.07 σ (rounded to 0.1
  σ). **(C-numerical)**.
- Neutrino splittings: NuFIT Δm²_31 and Δm²_21 with z-scores
  0.31 σ and 0.12 σ. **(C-numerical)**.

### (C-structural) "Closed structurally"

A condition required by a framework theorem is met by the
framework's setup. The closure is logical, not numerical — there
is no Z-score because there is no observable being matched, only
an internal consistency check.

Examples:

- K = K_c residual: gap1_theorem.md requires K > K_c. For
  identical oscillators K_c = 0. Framework operates at K > 0.
  Therefore K > K_c is satisfied. **(C-structural)**.
- D2 cascade saturation: q=3 is an inner Stern-Brocot
  denominator structurally analogous to the saturation
  endpoints elsewhere. Numerical scan confirms but doesn't
  prove. **(C-structural with caveat)**.

### (C-attribution) "Closed elsewhere"

The work was done in another framework doc; this session merely
reconciles the status. No new derivation; no numerical match
computed in this session.

Examples:

- ℓ_c diffusion length: closed by hierarchy_gaussian_lattice.md
  via ℓ_c = ℓ_P with ℓ_P derived from R. **(C-attribution)**.
- Neutrino masses: closed by item12_neutrino_solar_closure.py.
  **(C-attribution)** — though the closure file itself is
  C-numerical.

## Per-closure σ table (precise)

| Closure | Sense | σ | observation source | observation_unc |
|---|---|---|---|---|
| Down-type factor 6 | C-numerical | 0.04 σ | PDG 2024 m_b/m_s, m_s/m_d | dominated by m_s (8.6% rel.) |
| Ω_b residual via \|r\|² | C-numerical | 0.07 σ | Planck 2018 baryon density | 0.6% rel. on Ω_b |
| Ω_DM (downstream of above) | C-numerical | 0.20 σ | Planck 2018 | 2.6% rel. on Ω_DM |
| Ω_Λ (cross-check) | C-numerical | 0.07 σ | Planck 2018 | 1% rel. on Ω_Λ |
| Mass-sector q=2 √w identity | C-structural | n/a | n/a | coordinate convention |
| Neutrino Δm²_31 (atm) | C-numerical | 0.31 σ | NuFIT 5.2 | 1% rel. |
| Neutrino Δm²_21 (solar) | C-numerical | 0.12 σ | NuFIT 5.2 | 3% rel. |
| K = K_c residual | C-structural | n/a | n/a | identical-oscillator setup |
| ℓ_c diffusion length (S1) | C-attribution / C-structural | n/a | n/a | free-parameter count |
| ℓ_c at observable scale (S2) | C-structural | ratio = λ_unlock | Madelung form: `ℏ/(2m)` | framework-derived Lyapunov, not free parameter |
| PMNS θ_12 | %-only | 10% rel. | NuFIT 5.2: 33.5° | uncertainty not propagated |
| PMNS θ_23 | %-only | 5% rel. | NuFIT 5.2: 45° | uncertainty not propagated |
| PMNS θ_13 | NOT closed | — | NuFIT 5.2: 8.6° | tree-level 28° off by 3.3× |
| All CKM angles | NOT closed | — | PDG | requires QCD running |

## What this audit changes

For each session closure doc, the σ-statements should be read
through this convention. Specific edits applied:

1. `neutrino_mass_audit.md`: σ values are observational z-scores
   from NuFIT 5.2; this is implicit but not explicitly stated.
   Adding a footer clarification.

2. `omega_b_residual_phase_b.md`: 0.1 σ is rounded from 0.07 σ
   (script's tolerance). Both are < 1σ; the closure stands.
   No change needed but the precision is now documented.

3. `mixing_angle_audit.md`: "12%" and "5%" are relative
   deviations, NOT σ. The PMNS uncertainties (typical ~1°) are
   small enough that proper σ-z-scores would be larger
   (e.g. (33.5−30)/1.0 = 3.5 σ for θ_12). Adding a clarifying
   note that the existing %-statements DON'T include
   measurement uncertainty.

4. `down_type_double_cover_closed.md`: "PDG agreement 0.04σ"
   correctly uses the observational z-score; the prediction
   (exactly 6) has no propagated uncertainty.

5. `gap2_sub_e_status_reconciled.md`: "factor ~9 ... not fully
   derived" — already corrected in prior audit. No σ claim made
   here; appropriate.

## What "closed" means for each session closure (re-stated)

| # | Closure | Senses |
|---|---|---|
| 1 | Down-type factor 6 | C-numerical (0.04 σ) + C-structural (D1 rep theory) |
| 2 | Mass-sector √w at q=2 | C-structural (coordinate convention) |
| 3 | Ω_b residual | C-numerical (0.07 σ; Phase B verified) |
| 4 | K_c critical case | C-structural (theorem's K_c = 0 for setup) |
| 5 | ℓ_c diffusion length | C-attribution (already done) + free-parameter sense (S1) |
| 6 | PMNS θ_12, θ_23 | %-only (10%, 5%) — not σ-closed |
| 7 | Neutrino masses | C-attribution + C-numerical (0.12-0.31 σ in source file) |

This makes explicit what each closure entails. Closures 1, 3, 7
are full numerical matches within observational error. Closures
2, 4, 5 are structural / definitional. Closure 6 is %-level
agreement but does not formally pass a σ test if PMNS
uncertainties are properly propagated.

## Loose statistical language flagged for explicit revision

**θ_23 = 45° vs predicted 42.79°.** PDG/NuFIT typically quote
θ_23 with ~1° uncertainty. Then the z-score is

    z = |45 − 42.79| / 1 ≈ 2.2 σ

This is NOT "close to closed" in the σ-sense; it is a 2-σ
tension. The "5% gap" framing in `mixing_angle_audit.md`
understates this. The doc needs a clarifying note.

**θ_12 = 33.5° vs predicted 30°.** PDG typical uncertainty ~0.7°.

    z = |33.5 − 30| / 0.7 ≈ 5 σ

This is a 5-σ tension in σ-terms — the "12% gap" framing
substantially understates it.

**Conclusion for closure 6.** The PMNS predictions match
observations at the **few-percent level**, which would only be
called "closed" under a relaxed criterion. They are not
closed at the σ-level using current PMNS measurement
uncertainties.

Updating `mixing_angle_audit.md` and the PR description to make
this distinction explicit.

## Cross-references

| Doc | σ convention used |
|---|---|
| `down_type_double_cover_closed.md` | C-numerical, 0.04 σ correct |
| `omega_b_residual_phase_b.md` | C-numerical, 0.07 σ exact |
| `neutrino_mass_audit.md` | C-numerical, NuFIT z-scores |
| `mass_sector_sqrt_w_phase_b.md` | C-structural; no σ claim |
| `k_critical_phase_b.md` | C-structural; no σ claim |
| `gap2_sub_e_status_reconciled.md` | C-attribution + free-parameter; no σ |
| `mixing_angle_audit.md` | %-only — DOES NOT pass σ-test (this audit) |
| `session_audit.md` | Identifies the two prior overclaims |
| **this doc** | Defines all conventions used above |
