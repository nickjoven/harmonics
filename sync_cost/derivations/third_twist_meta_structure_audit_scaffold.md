# Third-twist (Z_3) meta-structure audit — scaffold

> **Scaffold notice.** This document is a **scaffold**, not a sealed
> audit. Sections 0–4 are written; sections 5 (framework instance
> catalog), 6 (identity restatement), 7 (signature restatement) are
> templates to be filled in by subsequent audit work. The scaffold
> establishes the question, the verify-before-assert ground, the
> vocabulary-earning criteria, the literature anchor, and the
> numerology trap explicitly, so that the catalog-filling work
> proceeds against a fixed criterion-set rather than absorbing the
> half-twist bias.

> **Origin context.** The recent audit chain (PRs #240–250) has
> privileged the Z_2 / half-twist reading. The reconciliation
> (PR #249) and the half-twist identity restatement (PR #250) made
> the bias explicit. The bias's symmetric counter is to audit the
> framework's *other* substrate-canonical n-twist modes with
> comparable depth. Third-twist (Z_3 from Mihailescu q_3 = 3) is the
> most natural next candidate — the framework's second substrate
> prime, equally foundational, but never audited as a meta-structure.
> This scaffold sets that up. The origin context lives in this
> notice and the PR description; the audit body is canonical.

**Status: SCAFFOLD ONLY.** No verdict assigned yet. The audit will
seal MODAL / GENERATIVE designations once the framework instance
catalog (section 5) is filled and the V1–V5 criteria are checked
against each instance.

Class: foundational rigor check / substrate meta-structure audit.
Resolution-mode throughout — composes existing canonical claims
(Mihailescu primes, PSL(2,ℤ) free product, Eisenstein integers,
Φ_3 cyclotomic content) into a unified meta-structural pattern.
No substrate primitive added or removed.

---

## 0. Scope and discipline

**The question.** Does the substrate's Z_3 cyclic mode (third-twist),
forced by Mihailescu prime q_3 = 3, constitute a meta-structure
across multiple framework instances — parallel to PR #240's
half-twist meta-structure — and if so, what is its identity, its
signature, and its catalog?

**The discipline.** Three explicit constraints:

(D1) **Verify before asserting.** Any structural claim about Z_3
content in an existing audit must be re-read from the substrate
this session; no recall from session memory.

(D2) **Apply the numerology partition.** Each candidate instance of
1/3 or 2/3 in physics or framework content is evaluated against
the V1–V5 criteria (§3). Instances failing one or more criteria
are classified per the framework's Class 1–5 numerology rubric
(`numerology_inventory.md`).

(D3) **No half-twist bias.** The audit must not absorb the recent
Z_2-privileging pattern. Third-twist must be evaluated on its own
substrate-canonical terms: q_3 = 3, ℤ[ω], Φ_3, PSL(2,ℤ) order-3
torsion. Where Z_2 sub-structure appears inside Z_3 (Aut(Z_3) = Z_2;
see §3), it is noted as an *algebraic feature*, not as a re-route
back to the half-twist meta-structure.

---

## 1. Question and motivation

The substrate's two Mihailescu primes (q_2, q_3) = (2, 3) are
equally foundational. Both generate Z_n cyclic content at their
natural orders, both anchor cyclotomic polynomials in the framework
(Φ_2, Φ_3), both appear as torsion orders in PSL(2,ℤ) = ℤ/2 ∗ ℤ/3,
both factor into Z_6 substrate lattice, both are bad primes of
Γ_0(6).

Despite this symmetry at the substrate-prime level, the audit chain
has treated them asymmetrically:

| Mode | Substrate prime | Meta-structure audit | Instance count | Identity restatement |
|---|---|---|---|---|
| **Half-twist** (Z_2) | q_2 = 2 | PR #240 (sealed) | 8 instances catalogued | PR #250 (sealed) |
| **Third-twist** (Z_3) | q_3 = 3 | — | — | — |

This audit is the symmetric counterpart: a third-twist
meta-structure audit *with the V1–V5 criteria explicit upfront* so
that the catalog-filling work distinguishes substrate-canonical Z_3
content from numerological appearances of 3, 1/3, or 2/3.

---

## 2. Verify-before-assert ground

Substrate facts re-read this session, with sources:

**(G1) Mihailescu primes.** (q_2, q_3) = (2, 3); the unique pair of
consecutive perfect powers via the cube identity `q_3² − q_2³ = 1`
= Catalan equation case (p, q) = (2, 3); Mihailescu (2002) for the
forcing. Source: `framework_status.md` PR #214; `canonical_glossary.md`
Section 5.

**(G2) PSL(2,ℤ) free product.** PSL(2,ℤ) = ℤ/q_2 ∗ ℤ/q_3; the
order-3 torsion element is the substrate's primitive Z_3 generator
inside the noncommutative core. F_2 = Γ(2) is the kernel of the
abelianization. Source: PR #241.

**(G3) Eisenstein integers ℤ[ω].** The ring ℤ[ω] with ω = e^(2πi/3) =
primitive 3rd root of unity. UFD; norm form is N(a + bω) = a² − ab +
b²; class number 1. Source: standard algebraic number theory; framework
references in `cyclotomic_content_mass_ratios_audit.md` and
`gamma06_cosmological_modular_surface_audit.md`.

**(G4) Φ_3 cyclotomic.** Φ_3(x) = x² + x + 1; degree 2; roots {ω,
ω²}; Galois group Z_2 (the inversion ω → ω²). Source:
`gamma06_cosmological_modular_surface_audit.md` line 144.

**(G5) Γ_0(6) bad primes.** Both 2 and 3 are bad primes of Γ_0(6);
3 corresponds to the Steinberg local representation with a_3 = −3
(LMFDB-verified per `scripts/verify/lmfdb_6_4_a_a_retrieved.md` and
PR #248). Source: PR #242, PR #248.

**(G6) Z_3 sub-structure inside D_4 ambient.** No — D_4 has no Z_3.
This is a NEGATIVE substrate fact: the lepton state group
reconciliation envelope D_4 (order 8 = q_2³) does NOT contain Z_3
content. Third-twist is NOT a substructure of the matter-scale
ambient. Source: PR #249 (D_4 = ⟨Z_4, V_4⟩).

**(G7) Aut(Z_3) = Z_2.** The automorphism group of Z_3 is Z_2 (the
inversion ω ↔ ω²). This is the substrate-internal Z_2 acting on Z_3;
it is *structurally forced* by |Aut(Z_n)| = φ(n), and φ(3) = 2.
Source: standard group theory; calls for explicit framework
treatment in this audit.

Session snapshot at start: CAS 378 (0 corrupt) | scorecard 17 +
bare_k1 5 | drift 0. Substrate clean; cached entries re-asserted fresh.

---

## 3. Vocabulary-earning criteria (V1–V5)

A rational p/q earns a substrate-canonical vocabulary place if and
only if all five criteria hold:

**(V1) Substrate prime origin.**

p/q traces to Mihailescu primes (q_2, q_3) = (2, 3) through a
specific structural derivation.

- For **1/3**: q = q_3 = 3; substrate origin via Mihailescu's cube
  identity. ✓
- For **2/3**: q = q_3 = 3, p = q_2 = 2. So 2/3 = q_2 / q_3 = the
  Mihailescu prime *ratio* — the cleanest non-trivial rational
  composed from substrate primitives. ✓

**(V2) Cyclic-group action carrier.**

p/q acts as a normalized angle (2π · p/q) on a substrate-canonical
carrier.

- For 1/3 and 2/3: carrier = {ω, ω²} = primitive 3rd roots of unity
  = roots of Φ_3(x) = x² + x + 1; 1/3 generates Z_3 = ⟨ω⟩; 2/3 = ω²
  = ω^{-1} (the inverse generator). ✓

**(V3) Stern-Brocot tree position.**

p/q sits at a substrate-distinguished depth in the Stern-Brocot
mediant tree.

- 1/3 and 2/3 are **the only depth-2 mediants** in the Stern-Brocot
  tree (1/3 = mediant of {0/1, 1/2}; 2/3 = mediant of {1/2, 1/1}).
  Farey set F_3 = {0, 1/3, 1/2, 2/3, 1}. ✓

**(V4) Cyclotomic content.**

p/q appears as a normalized exponent in a cyclotomic structure.

- 1/3 and 2/3 are the cyclotomic content of Φ_3 by definition:
  ω = e^(2πi · 1/3), ω² = e^(2πi · 2/3). ✓

**(V5) Group composition closure.**

p/q composes under the group action to give substrate-canonical
elements.

- 1/3 + 1/3 + 1/3 = 1 ≡ 0 mod 1 (Z_3 closure); 1/3 + 2/3 = 1 ≡ 0
  (additive inverse pair); 2/3 + 2/3 + 2/3 = 2 ≡ 0 (Z_3 closure via
  inverse generator). ✓

**Eligibility verdict: 1/3 and 2/3 pass V1–V5.** Both are
substrate-canonical, cyclotomic Z_3 native, Stern-Brocot depth-2
forced, and composition-closed.

### 3.1 The Z_2 inside Z_3: Aut(Z_3) = Z_2

A structural observation that the audit treats as load-bearing:

1/3 and 2/3 are **not symmetric roles** in the substrate. They are
exchanged by the inversion automorphism of Z_3:

```
       Aut(Z_3) = Z_2 = ⟨inversion⟩,    ω ↔ ω²,    1/3 ↔ 2/3
```

This Z_2 inside Z_3 is the *framework's existing half-twist Z_2
appearing one level up*: even when discussing third-twists, the
substrate forces a Z_2 distinction between 1/3 and 2/3.

This is *not* a numerological coincidence. It is the structural fact
|Aut(Z_n)| = φ(n); for Z_3, φ(3) = 2.

The audit treats (1/3, 2/3) as a coupled pair — a Z_2-orbit inside
Z_3 — and notes where 1/3 and 2/3 appear with **distinct** structural
roles in framework instances (e.g., quark charges +2/3 vs −1/3;
ω vs ω² in modular form Galois orbits; cusp pairings under PSL(2,ℤ)
ℤ/3 generator). Asymmetries between 1/3 and 2/3 *carry information*
about how the Z_2 inversion is broken or preserved at each
substrate level.

### 3.2 Disqualifying conditions

A candidate "1/3" or "2/3" appearance is **not** substrate-canonical
if any of:

- It fails V1: the rational does not trace to Mihailescu primes
  through a structural derivation (e.g., "1/3 from 3 spatial
  dimensions" — V1 fails because q_3 = 3 is a Mihailescu prime,
  not a dimension)
- It fails V2: no cyclic-group action on a substrate-canonical carrier
- It fails V4: not cyclotomic content of Φ_n for any framework-relevant n
- It fails V5: no closure under group composition

A candidate that passes V1–V5 is substrate-canonical; one that fails
≥1 criterion is classified per `numerology_inventory.md` Class 1–5.

---

## 4. Literature anchor: physical phenomena with structural Z_3

The following physical phenomena have been verified-this-session-or-
earlier to carry **structural** (V1–V5 passing) Z_3 content. They
constitute the external substrate anchor for the audit.

### 4.1 Confirmed structural Z_3 phenomena

| Phenomenon | Where 1/3 or 2/3 appears | Structural derivation |
|---|---|---|
| **SU(3) color and U(1)_EM** | Quark electric charges +2/3 (up-type), −1/3 (down-type) | Eigenvalues of U(1)_EM generator in SU(3) ⊂ SU(5) embedding; not arbitrary; standard model textbook (Peskin-Schroeder Ch. 22) |
| **Radiation EOS** | w = p/ρ = 1/3 for massless relativistic fluid | T^μ_μ = ρ − 3p = 0 (traceless stress-energy for massless dispersion); the "3" is spatial dimension d = 3; structural for relativistic radiation |
| **Graphene Brillouin zone Dirac points** | K = (2/3, 1/3) · b_1 + (1/3, 2/3) · b_2; K' = (1/3, 2/3) · b_1 + (2/3, 1/3) · b_2 (reciprocal lattice coordinates) | Forced by hexagonal Bravais lattice's reciprocal hexagonal symmetry + sublattice structure; Castro Neto et al. (RMP 2009) |
| **Eisenstein integers ℤ[ω]** | ω = e^(2πi · 1/3); ω² = e^(2πi · 2/3) | Algebraic ring structure; the fractions ARE the cyclotomic angles; standard algebraic number theory |
| **Z_3 parafermions** | Fractional quantum Hall ν = 12/5 (Read-Rezayi state); Z_3 anyon fusion rules | Z_3 symmetry of microscopic Hamiltonian; quantum dimension √((5+√5)/2); Nayak et al. (RMP 2008) |
| **Trefoil knot / PSL(2,ℤ) order-3 torsion** | Order-3 element of PSL(2,ℤ); appears in three-body hyperbolic dynamics | PSL(2,ℤ) free product structure; framework PR #241 (lunar theory parallel) |
| **SU(3) center in lattice gauge theory** | Z_3 center symmetry; Polyakov loop transformation | Z(3) center of pure SU(3) Yang-Mills; deconfinement transition order parameter; Greensite (2011) |
| **Cosmological "1/3" in MOND / DM** | Various scaling relations (a_0 ~ 1/3 cH_0 in some MOND derivations) | Disputed structural; flag for explicit V1–V5 check |

### 4.2 Numerology traps: phenomena that look like Z_3 but are not

| Apparent 1/3 or 2/3 | Why it's a trap | Class |
|---|---|---|
| **Random walk on 3D lattice has step probability 1/3 in each direction** | Just "1 of 3 choices" arithmetic; the 3 is *number of directions*, not Mihailescu q_3 | Class 1 (confirmed numerology) |
| **Heat capacity 3R in equipartition** | "3 spatial dimensions" arithmetic; structural in the trivial sense but no Z_3 cyclic action | Class 2 (noted coincidence) |
| **Average of three quark masses ≈ nucleon mass / 3** | Arithmetic average; not Z_3 forced; depends on QCD scale | Class 1 |
| **Three flavors of light quarks (u, d, s)** | SU(3)_F is approximate (broken by quark masses); 1/3 here is approximation | Class 2 |
| **1/3-octave in music theory** | 12-tone equal temperament; coincidental arithmetic | Class 1 |
| **Spin-1 multiplicity = 3 → 1/3 weight per state** | Hilbert space dimension; no cyclic action | Class 1 |
| **"Three generations of fermions"** | Generation index; no obvious Z_3 cyclic structure (despite some attempts; e.g., A_4 family symmetry models) | Class 2/3 (suspect by association) |

### 4.3 The trap pattern named

**Anywhere "3" appears as "number of options" or "number of
dimensions" or "arithmetic average over 3 things," 1/3 follows
trivially and means nothing structural.** It is just dividing by 3.

The audit's disciplinary requirement: a candidate Z_3 instance must
pass V1 (Mihailescu prime origin), not just "the number 3 appears."

---

## 5. Framework instance catalog (TEMPLATE — to be filled)

**Status: TEMPLATE.** This section will catalog the framework's
existing audits that engage Z_3 / 1/3 / 2/3 content, evaluating
each instance against V1–V5 and assigning a numerology Class.

The catalog-filling work proceeds in three phases:

### Phase 5.1: Grep across existing audits for Z_3 signatures

Substrate-canonical signatures to grep for:
- `q_3`, `q₃` (Mihailescu prime)
- `ℤ[ω]`, `Z[omega]`, `Eisenstein` (Eisenstein integers)
- `Φ_3`, `Phi_3`, `Phi3` (cyclotomic polynomial)
- `Z_3`, `Z₃`, `ℤ/3` (cyclic group)
- `1/3`, `2/3` (the rationals)
- `ω` as primitive 3rd root of unity
- `PSL(2,ℤ)` order-3 torsion
- `120°`, `2π/3` (rotation angles)
- `Φ_6(x) = x² − x + 1` (the cosmological cyclotomic, which contains Z_3 via Z_6 = Z_2 × Z_3)

### Phase 5.2: Per-instance V1–V5 evaluation

For each instance located in Phase 5.1, fill the catalog row:

| Instance | Location | Carrier | Cyclic action | V1 | V2 | V3 | V4 | V5 | Class | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

(Catalog rows to be filled. Aim for completeness — every existing
audit that references Z_3 content should appear, with explicit V1–V5
check.)

Expected instances (to verify):
- PR #241 PSL(2,ℤ) noncommutative core (q_3 torsion; F_2 = Γ(2))
- PR #242 Γ_0(6) cosmological audit (bad prime 3; Steinberg
  reduction at 3)
- `cyclotomic_content_mass_ratios_audit.md` (Φ_3 in cosmological
  Φ_6 = Z_2 × Z_3)
- `gamma06_cosmological_modular_surface_audit.md` (Φ_3 = Z_3 row in
  cyclotomic table)
- PSL(2,ℤ) free product (= ℤ/2 ∗ ℤ/3)
- Substrate Z_6 lattice (= Z_2 × Z_3)
- Mass hierarchy 26 : 7 : 1 (any Z_3 content?)
- Sector exponent progression 2, 5/2, 3 (the 3 endpoint — but is
  this a Z_3 carrier?)
- Three-body problem PR #241 lunar theory (the "three" of three
  bodies; needs V1 check whether it's Mihailescu q_3 or just
  arithmetic 3)

### Phase 5.3: Aggregate the catalog

Count substrate-canonical instances (V1–V5 passing) vs numerological
(failing). Identify whether a meta-structure emerges (≥ 3 instances
sharing a common derivation chain).

If a meta-structure emerges: proceed to §6 (identity) and §7
(signature).

If no meta-structure: the audit closes negatively — substrate's Z_3
content is *present but non-coherent as a meta-structure*. This
would be a substantive finding on its own.

---

## 6. Identity restatement (DEFERRED until §5 catalog complete)

**Template — parallel to PR #250 half-twist identity.**

Once the catalog is filled, this section will state:

**Identity (3 conjoint conditions):**
- (I1) Order 3 (σ³ = id, σ ≠ id, σ² ≠ id)
- (I2) Primitive Z_3 (not σ_6² of a Z_6 generator; not n-th power
  of higher cyclic mode that is itself canonical)
- (I3) [Geometric-type condition specific to Z_3 — to be derived
  from the catalog, not pre-asserted]

The (I3) condition is the audit's open question. For the half-twist,
(I3) was reflection-character (sign-flip, pair-swap, antipodal
involution, orientation reversal, complex conjugation,
Atkin-Lehner involution). For the third-twist, the analogous
geometric type would be a rotation-character condition (120°
rotation, third-root multiplication, Z_3 anyonic exchange,
SU(3) color rotation, Eisenstein-integer ω-multiplication,
PSL(2,ℤ) ℤ/3 torsion application). The catalog's filled instances
will determine which of these are *substrate-canonical* (vs derived
or numerological).

**Open: 1/3 vs 2/3 as I3 sub-cases?** Aut(Z_3) = Z_2 exchanges them,
suggesting they are roles, not separate identities. The catalog will
test this.

---

## 7. Signature restatement (DEFERRED until §5 catalog complete)

**Template — parallel to PR #250 half-twist signature.**

Once the catalog is filled, this section will state:

**Signature (4 detection tests):**
- (S1) Order-3 carrier transformation (σ³ = id)
- (S2) Primitive Z_3 subgroup (not lifted from a higher cycle)
- (S3) [Rotation-character geometric type — to be derived]
- (S4) Substrate forcing by Mihailescu q_3 = 3 AND a specific
  framework structural anchor

**Disqualifying conditions:**
- Z_n for n ≠ 3 (third-twist requires precisely order 3, not 2, 4, 6, etc.)
- Z_3 element appearing as σ_9³ of a Z_9 generator (if such a Z_9
  envelope is canonical) — derived, not primitive
- "Third-character" fractional content (1/3 appearing as a
  fractional exponent or weight, *not* as a Z_3 group action) —
  parallel to PR #250's "half-character" category

---

## 8. Falsification anchors (preliminary)

- **F-3-1** (no meta-structure): the catalog finds fewer than 3
  instances passing V1–V5; the third-twist does not constitute a
  meta-structure in the framework. Audit closes negatively.
- **F-3-2** (numerology dominant): the catalog finds Z_3 instances
  but >50% fail V1–V5; the framework's "Z_3 content" is largely
  numerological. Audit must triage and re-frame.
- **F-3-3** (Z_2 inversion bias persists): the framework treats 1/3
  and 2/3 symmetrically when the Aut(Z_3) = Z_2 inversion would
  predict asymmetry. Indicates the catalog is not deep enough to
  surface the algebraic structure.
- **F-3-4** (Mihailescu origin failure): some instance of Z_3
  content traces NOT to q_3 = 3 but to a different "3" (number of
  dimensions, number of generations, etc.); this is a V1 failure
  and requires Class 1 demotion.
- **F-3-5** (no rotation-character (I3) coherent across catalog):
  the (I3) geometric type analogous to half-twist's
  reflection-character cannot be uniformly defined across catalog
  instances; the third-twist's identity has no single (I3)
  equivalent. This would be a substantive structural finding: Z_3
  content in the framework is *modal-only*, not generative.

---

## 9. Forward references

After the catalog (§5) is filled and the identity / signature
(§6, §7) are derived, the natural next audits are:

- **Two-thirds twist explicit treatment**: if Aut(Z_3) = Z_2
  asymmetry surfaces in the catalog (1/3 and 2/3 with different
  structural roles), a companion audit can name "two-thirds twist"
  as a substrate-canonical mode in its own right (distinct from
  but coupled to one-third twist).
- **Sixth-twist (Z_6) meta-structure**: Z_6 = Z_2 × Z_3 is the
  substrate's lattice; once half-twist (PR #250) and third-twist
  (this audit, sealed) are both characterized, the Z_6 composite
  becomes auditable.
- **Twelfth-twist (Z_12 = Z_4 × Z_3) meta-structure**: cross-scale
  composite.
- **Higher-order n-twist symmetry audit**: a cyclic-vs-dihedral
  parity audit (parallel to PR #249's D_4 = ⟨Z_4, V_4⟩
  reconciliation) for orders 6, 12.

---

## 10. Cross-references

**Parallel structure:**
- `half_twist_meta_structure_audit.md` (PR #240) — the half-twist
  meta-structure; this audit's structural template
- `half_twist_identity_signature_audit.md` (PR #250) — the
  half-twist identity / signature restatement; the template for
  §6, §7 of this audit

**Substrate ground:**
- `substrate_determinism.md` — Mihailescu primes
- `canonical_glossary.md` Section 5 — Catalan / Mihailescu
- PR #241 `psl2z_noncommutative_core_structural_identity_audit.md`
  — PSL(2,ℤ) free product; ℤ/3 torsion
- PR #242 `gamma06_cosmological_modular_surface_audit.md` —
  Γ_0(6) bad prime 3; Φ_3 cyclotomic
- `cyclotomic_content_mass_ratios_audit.md` — cyclotomic Φ_n at
  framework-native indices

**Bias acknowledgment (origin context):**
- The session preceding this scaffold acknowledged the recent audit
  chain's bias toward Z_2 / half-twist content. This audit is the
  symmetric counter — auditing the framework's Z_3 substrate-mode
  with comparable depth so that the bias is corrected by *parallel
  treatment*, not by retraction.

**Resolution-mode reaffirmation:**
- `feedback_resolution_vs_reconstruction.md` — this audit is
  resolution-mode (composes existing canonical claims into a
  meta-structural reading); not apparatus modification

**Vocabulary discipline:**
- `vocabulary_is_the_work_pattern.md` — the audit's V1–V5
  criteria are the *vocabulary-earning protocol* applied to 1/3
  and 2/3; the criteria are the precondition for naming
  "one-third twist" and "two-thirds twist" as substrate-canonical
  objects, just as PR #250 was the precondition for naming
  "half-twist" sharply

---

## 11. What this scaffold does NOT claim

- **Not a sealed audit.** No MODAL / GENERATIVE verdict assigned;
  §5 catalog must be filled first.
- **Not a substrate primitive.** Z_3 / q_3 = 3 is the substrate
  primitive; this audit clarifies what structures the primitive
  generates as third-twists vs as numerological appearances of "3."
- **Not a replacement for PR #240.** PR #240's half-twist
  meta-structure stands. This audit is the symmetric counterpart at
  the Z_3 level.
- **Not a re-litigation of PR #250.** PR #250's half-twist identity
  restatement is canonical; this audit borrows its structural
  template but does not re-engage its content.
- **Not a privileging argument for Z_3 over Z_2.** Both Mihailescu
  primes are substrate-canonical; the audit's purpose is parallel
  treatment, not replacement of one bias with another.

---

## Appendix A: The (1/3, 2/3) coupled-pair structure

The session's literature scan surfaced an observation worth
preserving as a load-bearing structural fact for the catalog-filling:

**1/3 and 2/3 are exchanged by Aut(Z_3) = Z_2.** They form a single
Z_2-orbit under the inversion automorphism of Z_3.

When the catalog surfaces instances where 1/3 and 2/3 appear with
**distinct** structural roles (e.g., quark up-type charge +2/3 vs
down-type −1/3; ω vs ω² in modular-form Galois orbits; specific
cusp pairings under PSL(2,ℤ) ℤ/3 generator action), the asymmetry
between the pair is the *Z_2-inversion-breaking observable*. Where
the inversion is preserved, 1/3 and 2/3 are degenerate substrate roles;
where broken, they carry distinguishable framework content.

This is the third-twist's *internal* structure: a Z_3 cyclic group
acted on by a Z_2 inversion automorphism, with the pair (1/3, 2/3)
as the orbit. The catalog should evaluate per-instance whether the
inversion is broken or preserved, as part of the V1–V5 evaluation.

This treatment of 1/3 and 2/3 as a *Z_2-coupled pair inside Z_3*
is the audit's deepest structural commitment. It is the
substrate-canonical generalization of "primitive 3rd roots of unity"
that the catalog will test against framework content.
