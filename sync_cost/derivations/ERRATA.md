# ERRATA

Corrections ledger for the derivation corpus. Policy: **documents
state current truth only** — a corrected doc is republished as a new
edition (marked by an HTML comment on line 1 naming the edition, the
prior text's git ref, and its errata entries). The defect, evidence,
and history live here, not in the reading surface. Audit documents
(`*_audit.md`) are point-in-time records: they are never rewritten
and carry at most a one-line pointer to this file. Prior text of any
edition: `git show <ref>:<path>`.

---

## E1 — XOR fraction-parity rule demoted to conjecture
**File:** `xor_derivation.md` (edition 2). **Fix commit:** this branch; prior text `7190a9b`.
The doc claimed theorem status for `q₁ % 2 ≠ q₂ % 2`. Sections 3–4
prove only the wavenumber-pairing spectrum (line-bundle field); the
QED cited sections that never mention denominators; Section 5's
wavenumber→denominator correspondence is stipulated (its own text
concedes q "unrestricted" in the generic cases); Section 6 has no
equations. The "verification" labeled depth 5 (3,969/1,764/44.4%) is
a 6-round tree (5-round: 961/440), listed a pair its enumeration
excludes (1/2,1/1), and cannot discriminate rule forms: at 6 rounds
numerator-parity XOR also allows exactly 1,764 pairs. Convention
provenance: denominator parity entered via code (`62a95a6`) nine
minutes before the first doc; `q_mod2_mediant_projection.md` pins the
numerator form. Downstream consumers (4-mode collapse, gauge
12-count, {2,3} selection, confinement asymmetry) inherit conjecture
status. Verified by 14-agent fan-out 2026-08-09, all verdicts
CONFIRMED.

## E2 — MSPU Lemma 5 overstated its source
**File:** `MINIMUM_SELF_PREDICTING_UNIVERSE.md` (edition 2). **Fix commit:** this branch; prior `3597650^`.
Lemma 5 stated "the XOR parity filter selects q₂ = 2 and q₃ = 3."
The filter (conjectural, E1) is a pair filter admitting 1,764 pairs,
not a selection; the q = 1 exclusion pointer ("Section 7") had no
supporting argument at the pointer; the {2,3} selection's documented
route is the cube-identity/Mihailescu argument
(`mass_sector_closure.md`), independent of the filter.

## E3 — 12.66/18.49 = 13/19 is false
**Files:** MSPU, `unification_bridge_audits_gaps_1_3.md`, `antiparticle_dark_energy_unification_audit.md`. **Fix commit:** `3597650`.
12.66/18.49 = 0.68469; 13/19 = 0.68421; Δ ≈ 4.8×10⁻⁴. The values are
the fitted interior point (w* = 0.828) and the w = 1 endpoint of the
same pipeline Ω_Λ(w) = (11+2w)/(16+3w). MSPU's "0.00% match" removed:
`boundary_weight.py` obtains w* by algebraic inversion at the
observed Planck value (Class 2, observation-inverted). Predictive
content is the interval [13/19, 11/16].

## E4 — "XOR filter produces 12.66 modes / Ω_Λ" attribution retired
**Files:** `klein_bottle_derivation.md`, `surface_uniqueness_audit.md`. **Fix commit:** `3597650`.
`boundary_weight.py` contains no parity predicate (|F₅| = 11,
|F₆| = 13 count all Farey fractions) and its w* is
observation-inverted, so the Ω_Λ number neither uses nor corroborates
the XOR filter; the contrasting T² count was never computed. The
tertiary "self-consistency" leg of K² uniqueness is retired; K²
uniqueness rests on the topological and dynamical legs.

## E5 — "XOR collapses 1,764 candidates to 4 survivors" misattribution
**Files:** `figure_eight.md` (source), `figure_eight_necessitation_audit.md`, `surface_uniqueness_audit.md`, `pattern_identification_discipline_candidate.md`, `canonical_glossary.md`. **Fix commit:** `3597650`.
The parity filter reduces 3,969 depth-6 pairs to 1,764 allowed; the
field-equation dynamics (`field_equation_klein.py`) collapses those
to 4 dominant modes. 1,764 is the filter's *output*, not its
candidate pool. The two steps have different epistemic status (E1).

## E6 — Confinement asymmetry not supported by xor_asymmetry.py
**File:** `xor_asymmetry.py` (docstring rewritten). **Fix commit:** `3597650`.
Recomputation: every base mode tallies 18/36 fiber modes allowed
("locked" = even-k exclusion only); allowed-and-twist-flipped = 0 in
all sectors (structurally forced), so no sector accesses a conjugate
twist and "SU(2) doesn't confine / SU(3) does" does not follow. The
predicate acts on unreduced denominators (2/6 reduces to the allowed
1/3), an ontology chosen only here. Under XNOR all four base modes
are forbidden.

## E7 — duty(q) = 1/q³ is a definition, not a circle-map law
**File:** `duty_dimension_proof.md` (edition 2). **Fix commit:** `f161d6c`; prior `f161d6c^`.
Measured w(p/q, K=1)·q² falls monotonically (0.2959 → 0.1970,
q = 2..7; `tongue_width_universality.py`, commit 181c29f); the
universal critical exponent is β = ln(δ_FKS)/ln φ = 2.164 (Shenker
δ_FKS = 2.8336), not 2; a uniform c/q² law is impossible (Σφ(q)/q²
diverges vs measure-1 locking; `farey_tongue_width_null.py`).
Downstream (`duty_cycle_dictionary.md` §1–3, `beta_from_tongues.md`
§2) must cite the law as a definition.

## E8 — SM β-coefficient claim retired; K* = 0.892 unsourced
**Files:** `beta_from_tongues.md` (edition 2), `fermion_mass_running.md`. **Fix commit:** `4f2a379`; prior `4f2a379^`.
No tongue-based derivation of any bᵢ exists (§7's 11/3 is imported
Yang–Mills); the "0.3% match" does not reproduce — script RMS
residual 131.89% (per-coefficient 2.2%–227%); K* = 0.892 is produced
by no computation (`beta_from_tongues.py` §2 solve returns exactly
1.0; 0.892 is hardcoded at `decoherence_correction.py:45`). §4d's
identity corrected to ∏(1 − K cos(2πj/q)) = 2(K/2)^q(T_q(1/K) − 1).
Survives: the ratio theorem d ln[duty_a/duty_b]/d ln K = q_a − q_b.
`fermion_mass_running.md`: "~6%" figure had no computation behind it
(actual 24%/78%).

## E9 — K* = 0.892 retired at all satellite sites
**Files:** `vacuum_stress_meta_structure_audit.md` (×2), `quantum_gravity_interpolation.md` (×2), `cosmological_cycle.md`, `K_mu_mapping.py`, `chain_topology_dynamical.py`. **Fix commit:** `b270a66`.
Same root cause as E8; sites now reference 2^(−3/14) or carry the
retirement note.

## E10 — n_s misstatement and "zero free parameters" scrub
**Files:** `artifacts.js`, `README.md` (×3), `index.html`, `SPINE.yml`. **Fix commit:** `5eeb78d`.
Deployed page shipped n_s ≈ 0.9649 from an arithmetic error
(1 − 2/19 = 0.8947); correct pipeline value n_s ≈ 0.9662 (+0.3σ).
"Zero free parameters" claims removed (w₊ is fitted; see MANIFEST
`free_parameters_note`).

## E11 — Small verified mismatches
**Files:** `xor_asymmetry` doc claim (25% → 12.5%), `discrete_gauge_resolution.md` (0.67473, not 2/3), `fm_beat` (bin_amplitude ÷ len(signal) → 1.0). **Fix commit:** `cff85ad`.

## E12 — Arithmetic batch
**Files:** `g2_q3_vs_q2_asymmetry.md` (613/216; 0.23583 ~115σ; 0.2403 ~229σ), `denomination_boundary.md` (table law limit 1, not √2; density interval; d_box = ln φ formula; Σφ(q)/2^q = 1.368, not 1), `koide_iteration_5` (q₂ + 2q₃), `lesson_rotation_curves_a0` (~0.7%), `down_type_double_cover_closed` (~3 sig figs), `k_axis_uniqueness` (25), `epsilon_physical_reading.md` (λ_unlock = 0.4731; ghost citation flagged), `INDEX.md` (D16/D18/D38 delisted), Ω_Λ σ-cluster across 9 files (13/19 = 0.6842 at 0.07σ; 0.6847 at 0.04σ). **Fix commit:** `2204284`.

## E13 — spatial_dimension and lorentz rows demoted to open problems
**File:** `MANIFEST.yml`. **Fix commit:** `84d9c4c`.
The d = 3 chain breaks at three_dimensions.md's undefined "SL(2,Z)
completes to SL(2,R)" step; qd_origins support is circular;
so(2,1) ≠ so(3). Full break anatomy in MANIFEST `open_problems`.

## E17 — strong_cp retraction, d=3 caveats, presentation headliners
**Files:** `MANIFEST.yml` (strong_cp), `coupling_scales.md`, MSPU, `exponent.md`, `three_zeros.md`, `README.md`, `docs/problem-map.md`, `VISUAL_ONTOLOGY_PROMPT.md`. **Fix commit:** this branch.
strong_cp retracted Class 5 → conditional: the θ = 0 argument runs on
the K² premise (ledgered conditional) and its "eta invariant vanishes
for flat Pin+ manifolds" step is an unverified import — flatness does
not generally force vanishing η (2d Pin bordism carries nonzero
invariants on flat representatives, e.g. Arf–Brown–Kervaire ℤ/8);
needs a mathematics audit. d = 3/(3,1) caveats integrated at the
three live sites still asserting the demoted D14/D15 chain (MSPU
predictions list, exponent.md self-consistency claim, three_zeros.md
"same 3" question). Note: the Koide "(2,1) signature" sites were
inspected and NOT caveated — their route is the iteration-11
cube-identity chain, independent of D14/D15. Presentation headliners:
problem-map strong-CP entry conditionalized; README 2026-04 status
snapshot annotated with the D1 retraction; VISUAL_ONTOLOGY_PROMPT's
three "zero free parameters" phrases retired.

## E16 — Repercussive-feedback batch: demotions propagated to consumers
**Files:** `MANIFEST.yml` (gauge_group, anomaly_cancellation), `gauge_dictionary.md`, `tongue_overlap_structure.py`, `duty_cycle_dictionary.md`, `framework_utils.py`, `gell_mann_nishijima.md`. **Fix commit:** this branch.
Corrections E1/E2/E7 and decision D2 changed the status of premises
whose consumers had not been re-statused. Propagated: gauge_group
retracted Class 5 → conditional (12-count consumes the conjectured
4-mode roster; XNOR gives 5 modes/20 transitions; #3b conceded;
cocycles vacuous); anomaly_cancellation retracted Class 5 →
verified-for-imported-charges (D41 hardcodes hypercharges; GMN
back-solves Y from observed Q — "no free parameters" withdrawn at
source); tongue_overlap_structure's "NOT SU(3)×SU(2)×U(1) / too
restrictive" retired as convention-dependent (rule conflation,
grid-flip, slot/pair level mixing, non-adjacent mediants);
duty_cycle_dictionary's "duty theorem"/"proved" language converted to
definition status with D2/E2 dependency notes; framework_utils
duty_cycle docstring aligned. Systemic fix: MANIFEST rows now carry
`premises:` fields checked by `check_premises.py` — Class 5/exact on
an unsettled premise is a machine violation (red/green verified).

## E15 — Ω partition canon (decision D1: option C)
**Files:** `MANIFEST.yml` (5 cosmology rows), `framework_constants.py`, `scripts/drift/check_manifest_claims.py`. **Fix commit:** this branch.
The two rival Ω families are dispositioned: the single-w bare
partition (1/19, 5/19, 13/19 — computed by `framework_constants.py`
and carried by ~70 docs) is canonical as **substrate-side reference
arithmetic, not a prediction** (Ω_b sits 6.7% from Planck); the
two-component family (13/264, 35/132, 181/264; w₊ = 13/14) is
**retracted Class 5 → Class 2 (observation-fitted)**: w₊ enters as a
numerical fit (`400f558`, table prints "0.000% (fit)"), the Γ_0(6)
cusp account was written 3h33m post-fit, and no script computes the
family. It remains a named refinement with a re-promotion path: a
non-fitted derivation of w₊ plus a computing script.

## E14 — Chain 1 repaired; circle is Axiom 1
**Files:** `minimum_alphabet.md` (edition 2), `mediant_derivation.md`, universality condition (4). **Fix commit:** `d582403`; prior `d582403^`.
The circle-derivation argument presupposes the R/Z identification it
claims to derive — the circle is Axiom 1, motivated not proved.
Mediant validity requires Farey adjacency (bc − ad = 1); the
derivation carries the least-denominator selection + inductive
invariant. Denominator-ordered widths are not universal over
couplings (sin(4πθ) at K = 0.5: w(1/4) = 0.03697 > w(1/3) = 0.01527);
first-harmonic dominance added as condition (4).
