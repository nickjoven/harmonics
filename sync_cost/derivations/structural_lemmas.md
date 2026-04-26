# Structural lemmas

## What this file is

A compact catalogue of the framework's load-bearing structural
lemmas, each stated formally with proof source, applicable Z1-Z3
status, and substrate / anchor classification. Intended as a
preprint companion piece for readers who want the formal core
without reading the full derivation atlas.

Each lemma is independently statable; the proof source citation
points to the doc(s) where the substantive derivation lives.
Where a lemma is "recognize-mode," its proof is composition of
existing framework results; the citation gives the composing
chain.

The numbering is by structural priority (1 = headline closure,
2-5 = supporting closures, 6-9 = constituent and methodological
results), not chronological derivation order. For full
derivation history see the source docs and `framework_status.md`.

## Notation

- **q_2 = 2**, **q_3 = 3**: framework primes
- **MEDIANT = q_2 + q_3 = 5**, **INTERACT = q_2 · q_3 = 6**
- **K_LEPTON = q_3² = 9**
- **|F_n|**: cardinality of the Farey sequence at depth n
  (|F_4| = 7, |F_5| = 11, |F_6| = 13, |F_7| = 19)
- **Z_n**: cyclic group of order n
- **Γ_0(N)**: Hecke congruence subgroup of PSL(2, ℤ) at level N
- **X_0(N)**: modular curve of Γ_0(N); cusps are Γ_0(N)-orbits of P¹(ℚ)
- **ψ_+, ψ_-**: sym (trivial) and antisym (sign) Z_2 reps under
  the Klein-antipodal involution τ: k ↦ -k (mod 6) on Z_6
- **w**: partial-locking weight ∈ [0, 1] of a substrate boundary
  mode at the EM-MOND threshold
- **Z1-Z3**: statistical-conventions discipline per
  `statistical_conventions.md` (Z1: ≤ 1σ; Z2: no fitted O(1)
  factors; Z3: only structural inputs)

---

## Lemma 1 — w_+ closure (headline)

Let Z_6 ≅ Z_2 × Z_3 be the substrate mode space, and let Γ_0(6)
be the induced modular constraint. Let ψ_+(1, 5) be the unique
EM-coupled Klein-singlet boundary mode in the coprime-to-6
sector.

Assume ψ_+(1, 5) is canonically associated with the cusp 1/2 of
X_0(6), and that the admissible cusp grain at denominator q is
selected by the nearest-to-unity representative

    w_+ = (q − 1) / q.

Then the Z_6 matter-sector closure fixes

    q = 14,

hence

    w_+ = 13/14.

Under the normalized closure map

    (w_+, 5, 12 + w_+) ↦ (Ω_b, Ω_DM, Ω_Λ),

where

    Ω_b   = w_+ / (17 + 2w_+),
    Ω_DM  = 5 / (17 + 2w_+),
    Ω_Λ   = (12 + w_+) / (17 + 2w_+),

one obtains

    Ω_b   = 13/264,
    Ω_DM  = 35/132,
    Ω_Λ   = 181/264.

Thus the induced closure partition is

    Ω_b : Ω_DM : Ω_Λ = 13 : 70 : 181.

**Proof source**: `w_plus_formalization.md` (T1-T7 + L1
composition); `L1_substrate_cusp_ground_state.md` (L1 closure);
`omega_b_alpha_beta_closure.md` (closure map derivation);
`psl2z_subgroup_phase_b.md` (cusp 1/2 association).

**Status**: Class 5 / Survives. Numerical residuals on Planck
2018: Ω_b 0.12%, Ω_DM 0.06%, Ω_Λ 0.13%; all sub-σ. Z1-Z3 pass.
Substrate-side.

---

## Lemma 2 — Sign-rep no-EM (the (α, β) closure)

Let ψ_-(p, q-p) be the antisym Klein-antipodal eigenmode on a
coprime pair {p, q-p} ⊂ Z_q under the involution τ: k ↦ -k
(mod q). Then ψ_- has Klein-monodromy −1 (sign rep), which
annihilates the mode's net EM coupling.

Therefore ψ_- does not see the MOND threshold, has no
partial-decoupling dynamics, and locks at

    w_- = 1.

For the cosmic partition under the two-component closure, this
forces the parameters (α, β) = (0, 1).

**Proof source**: `baryon_fraction.md` (sign-rep monodromy
content); `omega_b_alpha_beta_closure.md` ((α, β) closure
derivation).

**Status**: Class 5 / Survives. Recognize-mode closure: the
content was already in `baryon_fraction.md`'s "monodromy −1
kills net EM" language; the lemma articulates it as forcing
(α, β) = (0, 1) and w_- = 1. Substrate-side.

---

## Lemma 3 — Two-anchor minimum (D.3 closure)

The substrate's continuum limits at K = 1 (Einstein) and K < 1
(Schrödinger) are non-smoothly separated by the K = 1
critical-line tongue-coverage discontinuity (per N11 of
`continuity_in_K_nulls.md`).

Each regime requires its own anchor scale. The K = 1 (Einstein)
sector is anchored by H_0; the K < 1 (Schrödinger) sector is
anchored by v_EW. The minimum dimensional input is therefore
the pair (H_0, v_EW).

Reduction to one anchor is structurally obstructed: the
non-smooth K = 1 ↔ K < 1 transition prevents a single anchor
from covering both sectors simultaneously.

**Proof source**: `continuum_limits.md` Parts I-II;
`continuity_in_K_nulls.md` N11; `path_closures_iter3.md` (D.3
closure); `anchor_count_audit.md` (consolidated reframe).

**Status**: Class 5 / Survives. The two-anchor minimum is a
structural feature, not a derivation gap. Substrate-side
classification of which observables fall on which anchor side
is explicit per `coupling_scales.md`.

---

## Lemma 4 — Cosmic partition (single-w)

Mode-counting on Z_6 = Z_{q_2} × Z_{q_3} under three filters
produces the cosmic partition:

(i) Klein-singlet selection: select modes ψ that are sym
(trivial Z_2 rep) under the Klein-antipodal involution τ.

(ii) Coprime-to-INTERACT selection: select modes whose Z_6
indices are coprime to INTERACT = 6.

(iii) Inner/boundary distinction: among Z_6 = {0, 1, 2, 3, 4, 5},
the elements {0, 2, 3, 4} are inner; {1, 5} are boundary.

Then the three sector mode counts are

    N_Λ  = |F_6|     = 13   (DE),
    N_DM = MEDIANT  = 5    (DM, coprime sym pair antisym component),
    N_b  = 1               (boundary baryon ψ_+(1, 5)),

with total |F_7| = 19. The cosmic partition is

    Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19.

**Proof source**: `baryon_fraction.md`;
`omega_partition_combinatorial.md`; `farey_partition.md`.

**Status**: Class 5 / Survives. Single-w (static) prediction;
the two-component refinement (Lemma 1) gives the operating-point
predictions. Both are framework Class 5. Z1: 0.07σ on Ω_Λ at
single-w. Substrate-side.

---

## Lemma 5 — q_3-quantity closed form

For the cosmic partition with sector mode counts (N_Λ, N_DM,
N_b) = (13, 5, 1) and total |F_7| = 19, the logit complement
integer of each sector satisfies

    M_i = (|F_7| − N_i) / q_2

for i ∈ {Λ, DM, b}. Numerically:

    M_Λ  = (19 − 13) / 2 = 3   = q_3,
    M_DM = (19 − 5) / 2  = 7,
    M_b  = (19 − 1) / 2  = 9   = K_LEPTON = q_3².

The q_3-quantity sequence (3, 7, 9) is forced by the partition's
complement structure, not a separate input. In particular:

- The matter sector's M_DM = 7 is NOT a free parameter; it
  follows from the partition's existing Class 5 derivation
  (Lemma 4).
- The cusp grain at the matter sector under Lemma 1 is q = q_2
  · M_DM = 14, hence w_+ = 13/14 by closest-to-unity selection.

**Proof source**: `partition_logit_form.md` (logit form
algebra); `psl2z_subgroup_phase_c_inventory.md` (matter
sector identification).

**Status**: Class 5 (algebraic consequence of Lemma 4).
Substrate-side. Resolves what would otherwise appear as an
independent open derivation of |F_4| = 7.

---

## Lemma 6 — Hecke cusp ↔ Z_p rep correspondence

Let the substrate preserve Γ_0(INTERACT) = Γ_0(2) ∩ Γ_0(3)
(per the substrate's q_2 × q_3 sector decomposition). Under the
Hecke action, modes ψ on the substrate are classified by their
Z_p (p ∈ {2, 3}) representation:

- ψ trivial under Z_p ⟹ ψ inhabits the cusp 1/p of X_0(6)
- ψ sign rep under Z_p ⟹ ψ inhabits a non-cusp stabilizer
  (or the trivial cusp ∞)
- ψ at the q-coproduct (both Z_2 and Z_3 trivial) ⟹ cusp 0

Specifically, the boundary mode ψ_+(1, 5) (sym Klein-singlet,
trivial Z_2 rep on the {1, 5} pair) inhabits cusp 1/2 of X_0(6).
The cusp class is uniquely determined by the gcd of the mode's
representative denominator with INTERACT = 6.

**Proof source**: `psl2z_subgroup_phase_a_results.md` (cusp
enumeration); `psl2z_subgroup_phase_b.md` B2 (correspondence);
`klein_antipodal_z2_rep_pattern.md` (Z_p rep machinery).

**Status**: Class 5 (Hecke-theoretic restatement of existing
substrate structure). Substrate-side.

---

## Lemma 7 — Born rule exponent

Near a saddle-node bifurcation x² + μ = 0 on S¹, the residence
time of a trajectory near the merging fixed points scales as

    τ(μ) ~ 1 / √(−μ)   for μ → 0⁻.

The corresponding survival probability ⟨P⟩ over an ensemble of
initial conditions has the form

    ⟨P⟩ ~ |amplitude|^n

with exponent n fixed at

    n = 2

by the parabola's universal codimension-1 form. No other generic
exponent on S¹ is structurally stable: x³ requires Z_2 symmetry
(non-generic), x^(3/2) is non-smooth (violates differentiability),
and x^k for k > 2 is structurally unstable (perturbs to dominant
quadratic).

The Born rule exponent (probability ∝ |ψ|²) is therefore forced
by the parabola primitive's irreducibility.

**Proof source**: `born_rule.md`; `a1_from_saddle_node.md`;
`minimum_alphabet.md` Part II (parabola irreducibility).

**Status**: Class 5 / Survives. Result exact. Z1-Z3 pass.
Substrate-side.

---

## Lemma 8 — Spatial dimension

The substrate's natural mode-counting on Z_6 = Z_{q_2} × Z_{q_3}
includes a Z_3 sector corresponding to the color triplet (with
generator σ acting as cyclic shift by 2 (mod 6) on Z_6). The
three-fold symmetry of σ extends to three independent extension
directions in the macroscopic spatial geometry.

Therefore

    spatial dimension = q_3 = 3.

No other spatial dimension is consistent with the substrate's
q_3 = 3 sector under the sym/antisym + Klein-antipodal mode
decomposition. Higher-dimensional theories (extra dimensions,
Kaluza-Klein) are framework-incompatible at the substrate level
but may be valid as effective descriptions of dynamics within
the q_3 = 3 substrate.

**Proof source**: `three_dimensions.md`; D14 of derivation
chain.

**Status**: Class 5 / Survives. Result exact. Substrate-side.

---

## Lemma 9 — Pigeonhole calibration (Region C verdict)

For framework-integer expressions of bounded form

    {n/m, n^a/m^b, n·m/p, (n+m)/p, n/(m+p), n·m/(p·q)}

over the canonical set {2, 3, 5, 6, 7, 8, 9, 11, 13, 19} with
power exponents a, b ∈ {1, 2, 3}, the density of expressions
in the value range [10⁻³, 10³] is approximately 2386 distinct
values.

Against the framework's 33 physical observable values in the
same range, the count of near-matches at relative-error
thresholds {0.1%, 1%, 3%} is, respectively, {13, 26, 31}.

A permutation null (10⁴ trials, log-uniform sampling on the
observable range) gives null-mean counts {9.51, 23.26, 27.49}
with standard deviations {2.62, 2.59, 2.10}. The corresponding
p-values are {0.127, 0.199, 0.066}; none reaches significance
at α = 0.05.

Therefore: multi-candidate framework-integer ansatz patterns at
the 1-3% near-match density are statistically consistent with
pigeonhole, not signal. The discriminator policy
(`ansatz_audit_policy.md` Step 4 default to Class 2 absent
forcing argument) is calibrated correctly.

**Proof source**: `numerology_count_phase_b.md`;
`numerology_count_phase_b.py` (implementation).

**Status**: Class 5 (statistical result with explicit p-values).
Methodological lemma; calibrates the framework's discriminator
for distinguishing structural derivation from numerology.

---

## Composition graph

The lemmas compose into the framework's headline result chain:

    Lemma 4 (cosmic partition single-w)
        ↓
    Lemma 5 (q_3-quantity closed form)
        ↓
    Lemma 6 (Hecke cusp ↔ Z_p rep)        Lemma 2 (sign-rep no-EM)
        ↓                                            ↓
    Lemma 1 (w_+ closure: q = 14, w_+ = 13/14, partition refined)

Lemmas 3, 7, 8 are independent structural results. Lemma 9 is
the methodological calibration that justifies the discriminator
policy used throughout.

## Cross-references

- `w_plus_formalization.md` — full proof structure for Lemma 1
- `L1_substrate_cusp_ground_state.md` — L1 component of Lemma 1
- `omega_b_alpha_beta_closure.md` — Lemma 2 closure
- `path_closures_iter3.md` — Lemma 3 (D.3) closure
- `baryon_fraction.md` — Lemma 4 partition derivation
- `partition_logit_form.md` — Lemma 5 closed form
- `psl2z_subgroup_phase_b.md` — Lemma 6 Hecke correspondence
- `born_rule.md`, `a1_from_saddle_node.md` — Lemma 7 derivation
- `three_dimensions.md` — Lemma 8 spatial dimension
- `numerology_count_phase_b.md` — Lemma 9 calibration
- `derivation_atlas.md` — full derivation chain (lemmas in
  context)
- `phenomenology_cross_reference.md` — observable comparison
  table (lemmas → observations)
- `canonical_glossary.md` — vocabulary translation

## Status

**Structural lemmas v1, 2026-04-26.** Nine load-bearing lemmas
catalogued for preprint citation. Each lemma is independently
statable with proof source, Z1-Z3 status, and substrate /
anchor classification. Composition graph identifies headline
chain (Lemmas 4 → 5 → 6 + 2 → 1) producing the cosmic partition
two-component closure with zero free parameters at the closure
level.

Maintenance: append new lemmas as substrate work produces them;
update Lemma 9 calibration as the observable set or expression
set evolves.

Side: presentation doc; no new derivation content. All proofs
live in cited source docs.
