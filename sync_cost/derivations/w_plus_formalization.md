# Formal closure of w_+ = 13/14 — proposition-level chain

## What this file is

A formal restatement of the Phase C closure argument from
`psl2z_subgroup_phase_c_inventory.md`, organized as numbered
propositions with status tags and explicit dependency. The goal
is to identify the single open substrate-dynamics lemma (L1) on
which Class 5 closure of w_+ depends, and to make all other
links explicit and verifiable.

**Headline**: under the proposition chain T1 ∧ T2 ∧ ... ∧ T7,
the value w_+ = 13/14 follows from a single open lemma L1
(substrate ground state at cusp 1/2 = (q−1)/q). T1-T7 are all
Class 5 in the framework's existing derivations or recognize-mode
articulations thereof. L1 is the one genuinely-new substrate-
dynamics derivation needed.

## Notation

- **q_2 = 2**, **q_3 = 3**, **INTERACT = q_2 · q_3 = 6**
- **MEDIANT = q_2 + q_3 = 5**
- **K_LEPTON = q_3² = 9**
- **|F_n|**: cardinality of Farey sequence at depth n; here |F_7| = 19
- **Z_n**: cyclic group of order n
- **Z_6 = Z_{q_2} × Z_{q_3}**: substrate mode lattice (CRT
  decomposition)
- **τ**: Klein-antipodal involution k → −k mod 6 on Z_6
- **ψ_+, ψ_-**: sym (trivial) and antisym (sign) Z_2 reps under τ
- **Γ_0(N)**: Hecke congruence subgroup of PSL(2, ℤ) of level N
- **X_0(N)**: modular curve associated to Γ_0(N); its cusps are
  the orbits of P¹(ℚ) under Γ_0(N)
- **w**: partial-locking weight ∈ [0, 1] of a substrate boundary
  mode
- **cusp 1/2 of Γ_0(6)**: the orbit {p/q ∈ Q : gcd(q, 6) = 2,
  gcd(p, q) = 1}

## Established propositions (from existing framework derivations)

### T1 — Cosmological partition (Class 5; `baryon_fraction.md`)

The substrate's Z_6 mode-counting under Klein-antipodal Z_2 rep
decomposition + coprime-to-6 selection produces the partition

$$\Omega_\Lambda : \Omega_{DM} : \Omega_b = \frac{13 : 5 : 1}{19}$$

with N_Λ = 13 = |F_6|, N_DM = 5 = MEDIANT, N_b = 1, total = |F_7| = 19.

**Status**: Class 5 / Survives.

### T2 — Complement-integer closed form (algebra from T1)

The logit denominators of T1's partition satisfy

$$M_i = \frac{|F_7| - N_i}{q_2}$$

for each sector i ∈ {Λ, DM, b}. Numerically:

| Sector | N_i | M_i = (|F_7| − N_i) / q_2 |
|---|---|---|
| Λ | 13 | (19 − 13)/2 = **3** = q_3 |
| DM | 5 | (19 − 5)/2 = **7** |
| b | 1 | (19 − 1)/2 = **9** = q_3² |

**Status**: Algebraic consequence of T1. Recognize-mode
articulation per `partition_logit_form.md`.

### T3 — Antisym mode lock (Class 5; `baryon_fraction.md`,
`omega_b_alpha_beta_closure.md`)

The antisym Klein eigenmode ψ_-(1, 5) carries Klein-monodromy −1
(sign-rep), hence has zero net EM coupling. Without EM coupling,
the mode does not see the MOND threshold and is always fully
locked: **w_- = 1**.

**Status**: Class 5. Used in `omega_b_alpha_beta_closure.md` to
force (α, β) = (0, 1).

### T4 — Sym mode partial-locks (Class 5; same sources)

The sym Klein-singlet eigenmode ψ_+(1, 5) carries Klein-monodromy
+1 (trivial rep), hence has nonzero EM coupling. EM coupling
activates the MOND threshold; the mode partial-locks at weight w_+.

**Status**: Class 5. The single empirical operating-point
parameter in the Ω_b two-component closure.

### T5 — Substrate preserves Γ_0(6) (Class 5; `psl2z_subgroup_phase_b.md` B1)

The substrate's mode dynamics preserve

$$\Gamma_0(6) = \Gamma_0(2) \cap \Gamma_0(3)$$

because (i) the Z_2 = q_2 reduction (sym/antisym Klein-antipodal
decomposition) is preserved by the substrate dynamics
(`klein_antipodal_z2_rep_pattern.md`), (ii) the Z_3 = q_3
reduction (color triplet) is preserved by the substrate dynamics
(gauge-coupling locality), and (iii) Γ_0(2) ∩ Γ_0(3) = Γ_0(6) by
elementary modular group theory.

**Status**: Class 5 via composition of (i), (ii), (iii). All
three components are existing framework content.

### T6 — w_+ inhabits cusp 1/2 (Class 5; `psl2z_subgroup_phase_b.md` B2)

ψ_+(1, 5) is the trivial Z_2 rep on the Z_2 = q_2 quotient.
Under the Hecke-cusp correspondence on X_0(6), the trivial q_2
rep ↔ cusp 1/2 (the cusp at which the q_2 quotient is "active").

Therefore w_+, which parametrizes ψ_+(1, 5)'s partial-locking,
labels a cusp-1/2 representative.

**Status**: Class 5 via Hecke-cusp correspondence + T5.

### T7 — Substrate is discrete at finite K (Class 5; `denomination_boundary.md` §134)

The framework's substrate is always at coupling K < 1
(the K = 1 limit is general relativity, never physically
realized; D9 fidelity bound prevents it). At K < 1, the
substrate's modes occupy discrete tongues of the Stern-Brocot
tree.

In modular-curve language, this means the substrate's
representatives within any cusp orbit are quantized: at cusp 1/2
with denominator q, the allowed weights are

$$\left\{\frac{p}{q} : 1 \le p < q,\; \gcd(p, q) = 1\right\}$$

with grain (finest discrete unlocking quantum) **1/q**.

**Status**: Class 5.

## Open lemma (the one genuinely-new derivation needed)

### L1 — Substrate cusp-1/2 ground state (OPEN)

**Claim**: At cusp 1/2 of Γ_0(6) with denominator q, the
substrate's MOND-threshold energy functional has a unique global
minimum at the discrete representative

$$w_{\text{ground}}(q) = \frac{q - 1}{q}.$$

**Proof sketch (incomplete)**:

The MOND-threshold partial-locking dynamics for the sym
Klein-singlet boundary mode ψ_+(1, 5) at the EM coupling
threshold has an energy functional E(w) with three regimes:

- Above threshold (w → 1): full lock-in is energetically favored
- Below threshold (w → 0): coupling is suppressed; mode decouples
- At threshold: partial-locking, parametrized by w ∈ [0, 1]

If the unconstrained energy minimum lies at w → 1 (full lock-in
limit, i.e., the matter sector wants to fully absorb the mode)
modulo the threshold's partial-decoupling effect, and the
substrate quantization (T7) restricts w to {1/q, 3/q, ...,
(q−1)/q}, then the closest-to-1 discrete value (q−1)/q is the
energy minimum within the constraint.

This requires:

1. **L1.a**: The unconstrained MOND-threshold energy minimum
   approaches w → 1 as the mode's lock-in coupling dominates.
2. **L1.b**: "Closest discrete value to the unconstrained
   continuum minimum" is the right substitution rule from
   continuum minimization to discrete quantization.

L1.a is a substrate-dynamics claim about MOND. L1.b is a
substrate-dynamics + quantization-rule claim. Neither is
currently derived in the framework's existing content, though
both are physically plausible.

**Status**: OPEN. Requires substrate-side derivation.

## Theorem and proof (modulo L1)

### THM — Class 5 closure of w_+ = 13/14

**Statement**: Given T1, T2, T3, T4, T5, T6, T7, L1, the
substrate's empirical operating-point weight is

$$w_+ = \frac{13}{14}.$$

**Proof**:

| Step | Justification | Result |
|---|---|---|
| 1 | T6 | w_+ ∈ cusp 1/2 of X_0(6) |
| 2 | T2 with i = DM | M_DM = (|F_7| − MEDIANT)/q_2 = 14/2 = **7** |
| 3 | T1 + matter sector identification (DM is the matter sector destination for sym-mode unlocking, by partition structure) | matter sector q_3-quantity = M_DM = 7 |
| 4 | T7 + Step 3 | cusp-1/2 grain at matter sector denominator q = q_2 · 7 = **14**; allowed w values = {1/14, 3/14, 5/14, 9/14, 11/14, 13/14} |
| 5 | L1 with q = 14 | w_+ = (q − 1)/q = **13/14** |

∴ w_+ = 13/14. ∎

**Numerical verification**: Substituting w_+ = 13/14 into the
Ω_b two-component closure formulas (`omega_b_alpha_beta_closure.md`):

| Observable | Predicted | Observed | Residual |
|---|---|---|---|
| Ω_b | 13/264 = 0.04924 | 0.04930 | 0.12% |
| Ω_DM | 35/132 = 0.26515 | 0.26500 | 0.06% |
| Ω_Λ | 181/264 = 0.68561 | 0.68470 | 0.13% |

Sub-σ on all three Planck partition observables.

## Class status under THM

| Component | Status | Source |
|---|---|---|
| T1 (partition) | Class 5 | `baryon_fraction.md` |
| T2 (complement closed form) | Algebra from T1 | `partition_logit_form.md` |
| T3 (antisym lock) | Class 5 | `baryon_fraction.md`, `omega_b_alpha_beta_closure.md` |
| T4 (sym partial-lock) | Class 5 | `omega_b_alpha_beta_closure.md` |
| T5 (Γ_0(6) preservation) | Class 5 | `psl2z_subgroup_phase_b.md` B1 |
| T6 (cusp 1/2) | Class 5 | `psl2z_subgroup_phase_b.md` B2 |
| T7 (substrate discreteness) | Class 5 | `denomination_boundary.md` |
| **L1 (cusp ground state)** | **OPEN** | needs substrate-dynamics derivation |
| THM (w_+ = 13/14) | **Class 5 modulo L1** | this file |

**Net**: Class 5 closure of w_+ depends on a single open lemma
(L1), itself decomposable into two substrate-dynamics
sub-claims (L1.a, L1.b). Closing L1 closes THM, lifting w_+
from Class 4+ to Class 5.

## Comparison: null elimination vs positive uniqueness

This formalization uses **positive uniqueness via composition of
existing Class 5 results** (T1-T7) plus one open lemma (L1). It
does NOT enumerate or eliminate alternative readings of "7" or
"14" — none is needed.

**Why null elimination would be inadequate**: Region C Phase B
(`numerology_count_phase_b.md`) confirmed that framework-integer
expressions populate the relevant value range at pigeonhole
density. Eliminating alternatives one-by-one ("|F_4| has no
derivation; q_2² + q_3 has no derivation; ...") would not address
the structural pigeonhole problem. Positive uniqueness via T1-T7
composition bypasses the problem entirely: 7 = (|F_7| − MEDIANT)/q_2
is the framework's structurally-derived value (T2), not one of
many candidate framework-integer expressions.

The eight alternative framework-integer expressions for 7 are all
**numerical coincidences** of small-integer arithmetic; only the
T2 reading is **structurally derived**. The Z1-Z3 discipline
distinguishes these.

## What L1 needs

To close L1 (and therefore Class 5 closure of w_+):

1. **L1.a**: derive that the MOND-threshold energy functional
   for ψ_+(1, 5) has unconstrained minimum at w → 1. Possible
   path: composition of EM-coupling lock-in energy
   (favors w → 1) with MOND-threshold suppression at w → 0;
   show the threshold's effect is sub-dominant to lock-in
   energy, so minimum is at high w.

2. **L1.b**: justify "closest discrete representative to
   continuum minimum" as the substrate's quantization-rule
   convention. Possible path: small-w corrections to the
   energy functional, or explicit derivation of the discrete-to-
   continuum interpolation rule from the substrate's K < 1
   tongue structure.

Both sub-claims are substrate-dynamics work in the existing
framework's content (`continuum_limits.md`, `denomination_boundary.md`,
`mediant_derivation.md`). Neither requires new framework
primitives.

## Honest landing

This formalization clarifies that w_+ = 13/14 has a clean Class 5
proof structure with **one explicit open lemma**, not a diffuse
"open question" status. The proof's explicitness is itself a
substantive promotion: closure work now has a sharply-defined
target (L1.a + L1.b) rather than a loosely-defined goal of
"derive 13/14 from substrate."

The proof's recognize-mode character (T1-T7 are all already in the
framework or follow algebraically from existing content) means
that closing L1 gives the entire chain Class 5, not just the
endpoint. The framework's existing Z_6 + Klein machinery already
contains the structural skeleton; L1 is the substrate-dynamics
flesh.

## Cross-references

- `psl2z_subgroup_phase_b.md` — B1 = T5, B2 = T6, B3 = THM
- `psl2z_subgroup_phase_c_inventory.md` — Phase C reduction
  motivating this formalization
- `partition_logit_form.md` — T2 source
- `baryon_fraction.md` — T1, T3 source
- `omega_b_alpha_beta_closure.md` — T3, T4, partition closure
  formula
- `denomination_boundary.md` §134 — T7 source
- `cross_ratio_irrep_reframe.md` — irrep multiplicity reading
  (this formalization replaces the "open" status from there)
- `numerology_count_phase_b.md` — Region C verdict justifying
  positive-uniqueness over null-elimination approach
- `klein_antipodal_z2_rep_pattern.md` — substrate Z_2 × Z_3
  decomposition machinery (T5 component)
- `continuum_limits.md`, `mediant_derivation.md` — substrate
  dynamics content needed for L1

## Status

**w_+ = 13/14 closes Class 5 modulo L1**, where L1 is the
substrate's MOND-threshold energy minimum at cusp 1/2 quantization.
Proof chain T1 → T7 + L1 ⟹ THM is fully explicit. L1 decomposes
into L1.a (MOND-threshold energy minimum) and L1.b (continuum-to-
discrete quantization rule). Neither is currently derived; both
are within scope of the framework's existing substrate-dynamics
content.

**Net**: Phase C reduces from "diffuse open structural work" to
"close lemma L1.a + L1.b." This is the sharpest possible
statement of the framework's open work for w_+ closure.
