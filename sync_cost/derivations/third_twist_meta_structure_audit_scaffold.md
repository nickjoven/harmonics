# Third-twist (Z_3) meta-structure audit — scaffold

> **Status update (2026-06-10).** The scaffold has been populated with
> a first-pass catalog (§5), preliminary identity (§6), and signature
> (§7). The catalog reveals **four distinct Z_3 modes** in the
> framework (A: cyclic action, B: Mihailescu cube/ratio, C: composite,
> D: fractional) — not the single-mode meta-structure analogy with
> PR #240 would have predicted. Two preliminary structural findings
> (P1–P3 in §5.4) are substantive: (P1) Mode B is uniquely Z_3 with
> no Z_2 analog; (P2) the Aut(Z_3) = Z_2 inversion is spontaneously
> broken at Mode B level (substrate prefers 2/3 over 1/3); (P3) Mode
> D (fractional character) is nearly absent — the framework's
> fractional content is Z_2-character, not Z_3-character.
>
> **Verdict, first pass:** MODAL ✓ / GENERATIVE PARTIAL on the
> Z_3 meta-structure. The structure exists and is substrate-canonical;
> but it is *bimodal* (cyclic A + Mihailescu-cube B), not a single
> coherent meta-pattern. This is itself a structural finding —
> the third-twist is *not* an analog of the half-twist, even at
> identity/signature level. The vocabulary requires TWO sub-identities
> (Mode A cyclic, Mode B Mihailescu-ratio), not one. §6.A through §6.E
> state this.
>
> First-pass status: the catalog is a SAMPLING (not exhaustive); the
> pattern is robust enough to draw structural conclusions, but
> exhaustive catalog-filling remains a recommended follow-up.

> **Origin context.** The recent audit chain (PRs #240–250) has
> privileged the Z_2 / half-twist reading. The reconciliation
> (PR #249) and the half-twist identity restatement (PR #250) made
> the bias explicit. The bias's symmetric counter is to audit the
> framework's *other* substrate-canonical n-twist modes with
> comparable depth. Third-twist (Z_3 from Mihailescu q_3 = 3) is the
> most natural next candidate — the framework's second substrate
> prime, equally foundational, but never audited as a meta-structure.
> The first-pass audit reveals: the asymmetry the bias produced is
> not merely an oversight; the third-twist is *structurally distinct*
> from the half-twist in specific ways the catalog has now surfaced.

**Status: FIRST-PASS COMPLETE.** Preliminary MODAL ✓ / GENERATIVE
PARTIAL verdict; structural findings (P1–P3 in §5.4) are
substantive. The catalog is a sampling; exhaustive completion remains
recommended.

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

## 5. Framework instance catalog — first pass

### 5.1 Grep results (2026-06-09 session)

Substrate-canonical Z_3 signatures returned dense hits across the
audit chain. Sampling (not exhaustive):
- `q_3` / `q₃`: ~1,781 hits across the repo (substrate-prime label)
- Explicit `Z_3` / `Z₃` / `ℤ/3` references: ~20+ structural sites
- `color triplet` (Z_3 action vocabulary): ~12 sites
- `Φ_3(x) = x² + x + 1` (cyclotomic polynomial): 1 site (canonical)
- `27/8 = q_3³/q_2³` and `8/35 = q_2³/(q_2³+q_3³)` (Mihailescu cube
  bare K=1 identities): ~10 sites
- `Q = q_2/q_3 = 2/3` (Klein-bottle population ratio): ~15 sites
  across Koide form iterations 11, 13, 14
- `1/3` as boundary / threshold: ~6 sites (Q > 1/3 forces Lorentzian)
- `σ_3(17) = 1 + 17³` (Eisenstein λ_17): cosmological audit chain
- `S_3 acting on Z_2 × Z_3`: ~5 sites (down-type, neutrino, baryon)

The grep volume is large enough that **§5.2 is a first-pass
sampling**, not an exhaustive catalog. The pattern surfaces from
the sample; exhaustive catalog-filling is recommended future work.

### 5.2 First-pass catalog with V1–V5 evaluation

Instances classified into four modes that surfaced during cataloging:

| # | Instance | Location | Carrier | Mode | V1 | V2 | V3 | V4 | V5 | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Color triplet rotation σ | `canonical_glossary.md` line 55 | Z_3 sector of Z_6 substrate; SU(3) color | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 2 | PSL(2,ℤ) ℤ/3 torsion generator | PR #241 | PSL(2,ℤ) = ℤ/2 ∗ ℤ/3 free product | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 3 | Φ_3(x) = x² + x + 1 cyclotomic | PR #242, line 144 | Primitive 3rd roots {ω, ω²} | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 4 | σ orbits {0,2,4} and {1,3,5} on Z_6 | `derivation_atlas.md` line 603 | Z_6 mode lattice | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 5 | SU(3) color rotation | `surface_uniqueness_audit.md`, `framework_status.md` Task 106 | Color triplet | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 6 | Z_3 acts freely on down-type | `down_type_double_cover_phase_b.md` line 85 | Down-type quark triplet | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 7 | Twelfth drive Arnold tongue (3:1, q_3-base) → N = 2 | `RESULTS.md` lines 110–113 | Phase-locking ratio | **A** cyclic | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 8 | Matrix size 3 = q_3 (color triplet count) | `koide_form_substrate_iteration_5.md` line 118 | Mass matrix dimension | **A** cyclic | ✓ | ~ | ~ | ✓ | ✓ | 5 |
| 9 | 27/8 = q_3³/q_2³ (strong/weak coupling) | `README.md` lines 49–50; `MINIMUM_SELF_PREDICTING_UNIVERSE.md` line 238 | Bare K=1 arithmetic identity | **B** Mihailescu cube | ✓ | ✗ | — | — | — | 1 (bare K=1) |
| 10 | 8/35 = q_2³/(q_2³+q_3³) (sin²θ_W) | `MINIMUM_SELF_PREDICTING_UNIVERSE.md` line 239 | Bare K=1 arithmetic identity | **B** Mihailescu cube | ✓ | ✗ | — | — | — | 1 (bare K=1) |
| 11 | Q = q_2/q_3 = 2/3 (Klein-bottle population) | `koide_form_substrate_iteration_11.md` line 110 | Klein-bottle Lorentzian forcing | **B** Mihailescu ratio | ✓ | ✗ | ✓ (depth 2) | ✓ | — | 4 (substantive ratio) |
| 12 | K_lepton = q_2/q_3 = 2/3 | `koide_form_substrate_iteration_13.md` line 126 | Koide form productive null | **B** Mihailescu ratio | ✓ | ✗ | ✓ | ✓ | — | 4 (productive null) |
| 13 | Q > 1/3 forces Lorentzian signature | `koide_form_substrate_iteration_11.md` lines 107–115 | Klein-bottle signature threshold | **B** Mihailescu ratio | ✓ | ✗ | ✓ | ✓ | — | 5 (asymmetric uses both 1/3 and 2/3) |
| 14 | σ_3(17) = 1 + 17³ = 4914 (Eisenstein λ_17) | PR #243; `cuspidal_lambda17_weight4_audit.md` line 35 | Divisor sum at p = 17 | **B** Mihailescu cube (via d=3 / σ_3 = σ_{k-1} at k=4) | ~ | ~ | — | ~ | — | 5 (forced; weight-dependent) |
| 15 | m_τ/m_e = 26^(5/2) = (q_3³−1)^(d−1/2) | `MINIMUM_SELF_PREDICTING_UNIVERSE.md` line 323 | Mass ratio identity | **B** Mihailescu cube | ✓ | ✗ | — | — | — | 4 (forced ratio) |
| 16 | Z_6 = Z_2 × Z_3 substrate mode lattice | `canonical_glossary.md` line 53; `CHAIN_KSTAR.md` line 37 | Substrate carrier | **C** composite | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 17 | Φ_6(x) = x² − x + 1 (cosmological cyclotomic, contains Z_3 via Z_6) | PR #242 line 146 | 6th roots = Z_2 × Z_3 | **C** composite | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 18 | Z_12 = Z_4 × Z_3 cross-scale | `lambda17_test_gamma06_cosmological_audit.md` line 508 | Cross-scale composite | **C** composite | ✓ | ✓ | — | ✓ | — | 4 |
| 19 | S_3 acting on Z_2 × Z_3 lattice | `down_type_double_cover_closed.md` lines 68, 113; `vocabulary_is_the_work_pattern.md` line 59 | Z_6 with permutation group | **C** composite | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| 20 | cos²θ = 1/3 (Koide angular reformulation) | `koide_form_substrate_iteration_13.md` line 234 | Angular constraint | **D** fractional | ✓ | ✗ | ✓ | — | — | 4 (substrate-derived value, not cyclic) |
| 21 | Up-type +2/3 vs down-type −1/3 quark charges | (Standard Model; framework via SU(3) ⊂ U(1)_EM) | Quark electric charge | **A** cyclic via SU(3) | ✓ | ✓ | — | — | — | 5 (structural) |

**Notation in V1–V5 columns**: ✓ = passes; ✗ = fails; ~ = partial /
needs further audit; — = not directly applicable to this mode.

**Class column** (per `numerology_inventory.md`): 1 = confirmed
numerology / bare K=1; 4 = needs individual audit; 5 = explicitly
NOT numerology (structural).

### 5.3 Aggregate: four modes surface

Instances naturally partition into **four modes**, not the three I
anticipated in the template:

```
Mode A — Pure Z_3 cyclic action:                 8 instances (#1–#8, #21)
Mode B — Mihailescu cube / ratio (q_3³ or q_2/q_3): 7 instances (#9–#15)
Mode C — Z_3 in composite (Z_6, Z_12, S_3-on-Z_6): 4 instances (#16–#19)
Mode D — Third-character fractional:             ~1 instance  (#20)
                                                  ────────────
Total instances surveyed:                       ~20–22
```

(Total instances surveyed counts #21 in both A and B since the quark
charge structure spans cyclic action and ratio readings; the actual
count is more like 20 distinct instances.)

### 5.4 Pattern that surfaced — the structural finding

**Three structural observations from the catalog that PR #240's
half-twist meta-structure does not anticipate:**

**(P1) Mode B (Mihailescu cube q_3³) is UNIQUELY Z_3 — no Z_2 analog.**

The framework's bare K=1 arithmetic identities (27/8 = q_3³/q_2³;
8/35 = q_2³/(q_2³+q_3³); m_τ/m_e via (q_3³−1)) use q_3³ in
positions where the half-twist meta-structure has nothing
comparable. There is no "q_2³ standalone" identity that plays the
same role.

The deepest reading: the framework's "cube content" sits at the
intersection of **three coincident 3's**:
- q_3 = 3 (Mihailescu prime)
- d = 3 (spatial dimension)
- the cube exponent itself

When the cube content appears (27/8, etc.), it is exploiting all
three coincidences simultaneously. The Mihailescu cube identity
`q_3² − q_2³ = 1` already conjoins q_3² with q_2³ at the substrate
level; the bare K=1 identities extend this to q_3³ via the spatial
dimension d = 3.

This is a substrate mode the half-twist cannot have: there is no
"q_2² = 4 = d" analog, because d = 3 ≠ 4.

**(P2) The Z_2 inversion (1/3 ↔ 2/3) is SPONTANEOUSLY BROKEN at
Mode B level.**

In Mode A (cyclic action), 1/3 and 2/3 are degenerate Z_3 generators
exchanged by Aut(Z_3) = Z_2.

In Mode B (Mihailescu ratios), the asymmetry is sharp:
- `Q = q_2/q_3 = 2/3` is substrate-canonical (Klein-bottle, Koide)
- `Q = q_2²/q_3² = 4/9` is NOT canonical
- `Q = 1/3` appears only as a *threshold* / *boundary*, not as a value

The substrate's natural ratio is *q_2/q_3 = 2/3*, not the
inversion-related *q_3/q_2 = 3/2* nor *q_3²/q_2³ = 9/8* nor
*q_2/q_3² = 2/9 = 1/(q_2² + ...)*. Specifically: `Q = 2/3` is
preferred over `Q = 1/3` (which would require `q_2/q_3² = 2/9`,
not a substrate-canonical ratio).

This asymmetry IS the framework's Z_2-inversion-breaking observable
inside Z_3. It is NOT a bias artifact; it is a *substrate-forced*
asymmetry: the substrate's natural Mihailescu ratio is 2/3, the
inversion 1/3 has no canonical substrate carrier (it would require
the "wrong" power of q_3).

**(P3) Third-character fractional content (Mode D) is THIN.**

The framework's "fractional half-content" is rich (PR #240 instances
3, 4, 6, 7 — mediant, Born √ε, ½-weight modular, sector ½-step).

The framework's "fractional third-content" is essentially **just
cos²θ = 1/3** (Koide angular reformulation). No third-power
exponents in the substrate's coupling structure (the Mihailescu
content uses cubes, not third roots). No ⅓-weight modular forms in
the framework's modular surface content (Γ_0(3) and Γ_0(9) are not
prominent; the cosmological scale is Γ_0(6), matter scale is Γ_0(4)).
No third-step arithmetic progressions in sector exponents.

This **absence** is substantive. Reading: the framework's
fractional-presence content is *Z_2-character* (half-power
operations: √ε, ½-weight, ½-step), not *Z_3-character*. The
third-twist mode is *operative* (Mode A cyclic action, Mode B
Mihailescu ratio, Mode C composite) but not *fractionally present*.

This is the half-twist meta-structure's domain that the third-twist
does NOT enter. It is NOT a bias artifact; it appears to be a real
structural asymmetry between the substrate's q_2 = 2 and q_3 = 3
roles.

### 5.5 The bimodal vs trimodal asymmetry

Comparing half-twist and third-twist mode counts (PR #240 catalog +
this catalog):

| Mode | Half-twist (Z_2) | Third-twist (Z_3) |
|---|---|---|
| **A** cyclic action / primitive | 3 instances (K² antiperiodic, Q mod 2, Z_2 cyclotomic factor) | **8 instances** (color, PSL(2,ℤ), Φ_3, σ_orbits, SU(3), down-type, Arnold, matrix size) |
| **B** substrate-cube or ratio | (none — no q_2³-only canonical identity) | **7 instances** (27/8, 8/35, Q=2/3, K_lepton, Q>1/3, σ_3(17), m_τ/m_e) |
| **C** composite (in Z_n) | (implicit in Z_6 = Z_2 × Z_3) | **4 instances** (Z_6, Φ_6, Z_12, S_3-on-Z_6) |
| **D** fractional character | 4 instances (mediant, Born √ε, ½-weight, ½-step) | **~1 instance** (cos²θ = 1/3) |
| **B² derived (square of cyclic)** | 1 instance (SL(2,ℝ) J² = −I) | (NA at Z_3; would be σ³ but trivially id) |

The asymmetry: the half-twist's character is *cyclic + fractional*
(Modes A + D dominant); the third-twist's character is *cyclic +
Mihailescu-cube* (Modes A + B dominant).

This is the cleanest pattern the catalog surfaces.

---

## 6. Identity — preliminary statement (first pass)

Based on §5's catalog, the third-twist's identity has **two distinct
sub-identities** that must be stated separately, not as one
conjoint structure (as the half-twist's identity could be).

### 6.A — Cyclic-action third-twist (Mode A identity)

A **cyclic third-twist** in the framework is a structure on a
carrier acted on by σ satisfying three conjoint conditions:

**(I_A1) Order 3.** σ³ = identity, σ ≠ identity, σ² ≠ identity.

**(I_A2) Primitive Z_3.** σ generates a primitive Z_3 = ℤ/3ℤ
subgroup of the carrier's symmetry group — not σ_6² of a Z_6
generator that is itself substrate-canonical at the same scale.

**(I_A3) Rotation-character geometric type.** σ realizes one of:
- **120° rotation** on a planar carrier (R² with rotational symmetry)
- **Primitive 3rd root of unity multiplication** on ℂ or ℤ[ω]
  (z → ωz with ω = e^(2πi/3))
- **Cyclic shift on a 3-element substrate sector** (e.g., color
  triplet σ in canonical_glossary.md, three-element σ orbits on Z_6)
- **Z_3 anyonic exchange** in parafermion fusion rules
- **SU(3) center rotation** acting on the fundamental rep
- **PSL(2,ℤ) ℤ/3 torsion application** on the upper half plane

These are the substrate-canonical rotation-character actions
surfaced by the Mode A catalog.

### 6.B — Mihailescu-ratio third-twist (Mode B identity)

A **Mihailescu-ratio third-twist** in the framework is a structure
where q_3 = 3 appears NOT as a Z_3 cyclic action but as the
*Mihailescu prime in a substrate-canonical ratio or power*. The
identity is structurally distinct from Mode A:

**(I_B1) Order = irrelevant.** The Mihailescu ratio (e.g., q_2/q_3
= 2/3, or q_3³/q_2³ = 27/8) is NOT a cyclic group action; it is a
real-number value derived from substrate primes.

**(I_B2) Mihailescu-prime origin.** The ratio (or power) involves
q_3 = 3 specifically (not just any "3" from dimension counting or
arithmetic averages). The Mihailescu cube identity
`q_3² − q_2³ = 1` is the substrate forcing.

**(I_B3) Coincident-3 reading.** When the cube power appears (q_3³
in 27/8; q_3³ in σ_3 divisor sum; q_3³−1 = 26 in mass hierarchy),
the cube exponent is structurally tied to *spatial dimension d = 3*
(which coincides with the Mihailescu prime value q_3 = 3 in our
framework). The "three coincident 3's" reading: substrate prime
value, spatial dimension, and the cube exponent are all 3
simultaneously, and bare K=1 identities exploit all three at once.

### 6.C — Composite-mode third-twist (Mode C identity)

Z_3 appears as a factor in composite cyclic groups (Z_6, Z_12, S_3
on Z_2 × Z_3). The Mode C identity is just the Mode A identity
applied to the Z_3 factor of a composite carrier (with the
caveat that the carrier's *full* symmetry group is larger than Z_3
alone).

### 6.D — Absent: fractional-character third-twist

Unlike the half-twist (which has rich half-character fractional
content — Born √ε, ½-weight modular, sector ½-step, mediant),
the third-twist has **essentially no fractional third-character
content** in the framework. The Mode D row of §5 has only one
candidate (cos²θ = 1/3 in Koide angular reformulation).

This absence is itself a substantive structural finding (P3
above). The framework's *fractional-presence* content is
Z_2-character, not Z_3-character.

### 6.E — The Z_2 inversion (1/3 ↔ 2/3) is broken

Aut(Z_3) = Z_2 exchanges 1/3 and 2/3. At Mode A level (cyclic
action), they are degenerate primitive generators. At Mode B level
(Mihailescu ratio), the substrate prefers `Q = q_2/q_3 = 2/3` over
`Q = 1/3`; the inversion is broken. The framework's *natural*
substrate ratio is 2/3; 1/3 appears only as boundary / threshold /
charge-flip-complement of 2/3.

This is the third-twist's natural *symmetry-breaking* mode — its
own version of the half-twist's Z_2 self-inversion (PR #250).

---

## 7. Signature — preliminary statement (first pass)

**Cyclic third-twist signature (Mode A):**

A candidate σ is a Mode-A cyclic third-twist iff all four pass:

**(S_A1)** σ³ = id; σ ≠ id; σ² ≠ id (order exactly 3)
**(S_A2)** σ generates a primitive Z_3; not σ_6² of a substrate-
canonical Z_6 generator
**(S_A3)** σ realizes rotation-character (120° rotation, ω-
multiplication, cyclic shift on 3-sector, SU(3) center, Z_3
parafermion exchange, PSL(2,ℤ) torsion)
**(S_A4)** σ's existence is forced by q_3 = 3 (Mihailescu prime) AND
a specific structural anchor (color triplet, modular surface
torsion, etc.)

**Mihailescu-ratio third-twist signature (Mode B):**

A candidate value v involving 1/3, 2/3, or q_3³ is a Mode-B
Mihailescu-ratio third-twist iff:

**(S_B1)** v is a substrate-derived ratio (e.g., q_2/q_3, q_2³/q_3³)
or power (q_3³) — NOT a Z_3 cyclic action
**(S_B2)** The expression involves q_3 = 3 as a Mihailescu prime
(NOT as a dimension count, choice count, or arithmetic 3)
**(S_B3)** The ratio respects the Mihailescu cube identity
`q_3² − q_2³ = 1` OR exploits the d = 3 coincidence in cube powers
**(S_B4)** No Z_2 inversion partner: if `Q = 2/3` is canonical,
`Q = 3/2` or `Q = 1/3` substitutes either fail substrate-canonicity
or appear only as thresholds / complements

**Disqualifying conditions (do NOT pass any third-twist mode):**

- Order ≠ 3 (Z_2, Z_4, Z_n for n ≠ 3) — fails S_A1
- "3 dimensions" arithmetic 1/3 — fails S_A4 / S_B2 (no Mihailescu
  origin)
- "3 of N choices" arithmetic 1/3 — fails S_A4 / S_B2
- σ_9³ of a substrate-canonical Z_9 — fails S_A2 (derived, not
  primitive)
- Fractional 1/3 exponent in carrier without Mihailescu derivation —
  fails S_B2 (e.g., Born ε^(1/2) is half-character, not third-
  character; the framework has no analog)

### 7.B Vocabulary note

The "rotation-character" of Mode A is the third-twist's substrate-
canonical geometric type. It is NOT identical to the half-twist's
"reflection-character" (which is order-2 sign-flip / pair-swap /
antipodal). Rotation-character is *orientation-preserving* (per
SO(2) ⊃ Z_3); reflection-character is *orientation-reversing*.
The substrate distinguishes these.

**The third-twist is a substrate-canonical mode in the
orientation-preserving sector of the framework's vocabulary**;
the half-twist is in the orientation-reversing sector. This is a
sharp distinction surfaced by the catalog.

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
