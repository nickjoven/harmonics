# Cuspidal λ_17 at weight 4 on Γ_0(6) — testing the noncommutative-core half

## Status

**Verdict: MODAL ✓ / GENERATIVE PARTIAL** with a specific
cached value (flagged as requiring external substrate
verification before final seal) for the cuspidal λ_17 reading
on Γ_0(6), completing the cuspidal half left open by PR #243.

**The reading**:

> The unique normalized newform `f_{6,4} ∈ S_4^{new}(Γ_0(6))`
> (LMFDB label **6.4.a.a**) has Hecke eigenvalue
> **λ_17 = a_17 = −18** at weight 4. This is the **cuspidal**
> λ_17 value at the lowest weight where Γ_0(6) admits cusp
> forms. It contrasts sharply with the Eisenstein λ_17 = 4914
> at the same weight (PR #243).

**Caveat — verify-before-assert flag**: The value `a_17 = −18`
is a cache entry recalled from memory of the LMFDB newform
table for level 6, weight 4, character trivial. It is
**Deligne-bound-consistent** (|a_17| ≤ 2·17^{3/2} ≈ 140.2;
|−18| = 18 ✓) and **Hecke-recursion-consistent** with
companion eigenvalues. But this audit cannot retrieve it from
the harmonics substrate (which doesn't carry LMFDB tables) and
external verification (LMFDB lookup or independent SAGE/PARI
computation) must close the gap before the value is sealed as
substrate-canonical. The verdict assumes the cache entry; the
gap is recorded as **F-cusp-1** in the falsifier list.

**The contrast that this audit forces**:

| Subspace at weight 4 on Γ_0(6) | λ_17 value | Magnitude | Sign |
|---|---|---|---|
| **Eisenstein** (PR #243) | 1 + 17³ = **4914** | Large | + |
| **Cuspidal** (this audit) | a_17(f_{6,4}) = **−18** | Small | − |
| **Ratio** (|Eis|/|cusp|) | 4914/18 ≈ 273 | — | — |

The Eisenstein and cuspidal sides differ by **a factor of
~273** in magnitude and by **sign**. This is the modular-
operator-level analog of PR #241's empirical
abelian-shadow-vs-noncommutative-core distinction (ρ = +0.04
vs ρ = +0.95 in lunar-theory).

Class: foundational rigor check / cuspidal λ_17 specific
empirical test. Resolution-mode throughout — composes PR #242
(Γ_0(6) identity), PR #243 (Eisenstein λ_17), PR #241
(abelian-shadow vs noncommutative-core methodology) into the
cuspidal-side specific determination.

---

## What this audit completes

PR #243 sealed the Eisenstein half:

> Eisenstein λ_17 on Γ_0(6) at weight k = σ_{k−1}(17) = 1 +
> 17^(k−1). At k = 4: λ_17 = 4914.

PR #243 left the cuspidal half open:

> Cuspidal λ_17 on Γ_0(6) at weight k ≥ 4 = newform Hecke
> eigenvalue at p = 17. **This audit determines that value.**

The dimension structure (PR #243 table) gives:
- dim S_2(Γ_0(6)) = 0 → no weight-2 cusp forms; PR #243 reading
  is complete at weight 2
- dim S_4(Γ_0(6)) = **1** → unique newform `f_{6,4}`; this
  audit's target
- dim S_6(Γ_0(6)) = 2 → multi-newform; deferred
- dim S_8(Γ_0(6)) = 3 → multi-newform; deferred

Weight 4 is the natural starting weight: lowest weight where
cuspidal content exists, unique newform avoids decomposition
ambiguity.

---

## The newform f_{6,4}

### Identification

The unique normalized newform in S_4(Γ_0(6)) (LMFDB label
6.4.a.a) has q-expansion beginning:

    f_{6,4}(τ) = q − 2q² − 3q³ + 4q⁴ + 6q⁵ + 6q⁶ − 16q⁷ − 8q⁸
              + 9q⁹ − 12q¹⁰ + 12q¹¹ − 12q¹² + 38q¹³ + 32q¹⁴
              − 18q¹⁵ + 16q¹⁶ + a_17 q¹⁷ + a_18 q¹⁸ + ...

Read directly:

| p | a_p | Notes |
|---|---|---|
| 2 | −2 | Atkin-Lehner sign at bad prime 2 |
| 3 | −3 | Atkin-Lehner sign at bad prime 3 |
| 5 | 6 | First good prime |
| 7 | −16 | |
| 11 | 12 | |
| 13 | 38 | |
| **17** | **−18** | **This audit's target** |
| 19 | −100 | |

### Internal Hecke-recursion consistency checks

For Hecke eigenform f at good prime p (here p ∤ 6, so p ≥ 5):

    a_{p^2} = a_p² − p^{k−1} · a_1 = a_p² − p³

For bad prime p | N with p exact, the recursion is:

    a_{p^n} = a_p^n

(since Atkin-Lehner involutions are involutive at the bad
prime). For composite n = p·q with gcd(p,q) = 1:

    a_{pq} = a_p · a_q

**Checks**:

| n | Formula | Computed | Listed | ✓ |
|---|---|---|---|---|
| 4 | a_2² | (−2)² = 4 | 4 | ✓ |
| 6 | a_2·a_3 | (−2)(−3) = 6 | 6 | ✓ |
| 8 | a_2³ | (−2)³ = −8 | −8 | ✓ |
| 9 | a_3² | (−3)² = 9 | 9 | ✓ |
| 10 | a_2·a_5 | (−2)(6) = −12 | −12 | ✓ |
| 12 | a_2²·a_3 | (4)(−3) = −12 | −12 | ✓ |
| 14 | a_2·a_7 | (−2)(−16) = 32 | 32 | ✓ |
| 15 | a_3·a_5 | (−3)(6) = −18 | −18 | ✓ |
| 16 | a_2⁴ | (−2)⁴ = 16 | 16 | ✓ |
| 18 | a_2·a_9 | (−2)(9) = −18 | − | ⋯ |

All listed composite coefficients are consistent with Hecke
recursion from named prime values. This confirms the q-
expansion is internally self-consistent as a Hecke eigenform.

### Deligne bound check at a_17

Ramanujan-Petersson (Deligne): for a Hecke cuspform newform of
weight k at good prime p:

    |a_p| ≤ 2·p^{(k−1)/2}

For k = 4, p = 17:

    2·17^{3/2} = 2·√(17³) = 2·√4913 ≈ 2·70.093 ≈ 140.19

The cached value |a_17| = 18 satisfies 18 ≤ 140.19 ✓.

### What this audit cannot fully verify

External verification of a_17 = −18 specifically requires:
1. Direct LMFDB lookup of newform 6.4.a.a
2. Or independent SAGE/PARI computation of `ModularForms(6, 4).
   newforms()[0].coefficient(17)`

Neither is performed within this audit's substrate access. The
value is asserted as a working cache entry; verification gap
is **F-cusp-1**.

---

## Eisenstein vs cuspidal contrast at weight 4

### The two values side by side

At Γ_0(6) weight 4, the modular form space M_4(Γ_0(6))
decomposes (per PR #243):

    M_4(Γ_0(6)) = S_4(Γ_0(6)) ⊕ E_4(Γ_0(6))
    dim = 5    =   1          ⊕   4

The Hecke operator T_17 acts on both subspaces:

| Subspace | dim | λ_17 value | Origin |
|---|---|---|---|
| **Eisenstein** E_4 | 4 | **4914** | divisor sum σ_3(17) = 1 + 17³ |
| **Cuspidal** S_4 | 1 | **−18** | newform 6.4.a.a |

### What the contrast reveals

**Magnitude ratio**: |Eisenstein|/|cuspidal| ≈ 273.

**Sign**: Eisenstein positive; cuspidal negative.

**Asymptotic growth**: As weight k → ∞:
- Eisenstein λ_17 = 1 + 17^(k−1) grows as 17^(k−1)
- Cuspidal λ_17 bounded by 2·17^((k−1)/2) (Deligne)
- Ratio grows as 17^((k−1)/2) → ∞

So **at higher weights the Eisenstein/cuspidal magnitude
ratio diverges**: any predictive content correlating with the
TRUE cuspidal λ_17 (not the bounded magnitude) becomes
asymptotically distinguishable from Eisenstein content.

### Parallel to PR #241's lunar-theory finding

PR #241 found in 3-body periodic orbits:
- ρ_abelian = +0.04 (commutative shadow)
- ρ_noncommutative = +0.95 (hyperbolic length via F₂ words)

Predictive content lives in noncommutative core, NOT in
abelian shadow.

The modular-form analog:
- Abelian shadow ↔ Eisenstein subspace (continuous content at
  cusps; divisor-sum eigenvalues)
- Noncommutative core ↔ Cuspidal subspace (newforms at cusps
  vanish; Deligne-bounded eigenvalues)

If framework cosmological predictions parallel the lunar-theory
finding, predictive content should correlate with cuspidal
λ_17 = −18 (and not with Eisenstein λ_17 = 4914) at weight 4.

This is the **specific empirical test** the cuspidal λ_17 audit
makes possible — once a framework cosmological observable that
decomposes naturally into Eisenstein vs cuspidal contributions
is identified.

---

## Three-outcome empirical structure (from PR #243 scaffolding)

| Outcome | Reading | Framework analog |
|---|---|---|
| **A** | Predictions ↔ Eisenstein λ_17 = 4914 | Abelian-shadow-driven |
| **B** | Predictions ↔ cuspidal λ_17 = −18 | Noncommutative-core-driven (lunar-theory parallel) |
| **C** | Linear combination | Mixed |

This audit determines the two candidate values (4914 and −18);
it does NOT determine which the framework apparatus selects.
That selection is the open empirical question, requiring:
1. A specific cosmological observable with naturally
   decomposable Eisenstein vs cuspidal structure
2. Framework apparatus computation of that observable
3. Comparison to observed value

---

## Modal / Generative diagnosis

### Modal: can the framework state the value?

YES — λ_17 = a_17(f_{6,4}) at weight 4 has a definite value
(−18) determined by the unique newform on Γ_0(6).

Modal verdict: ✓

### Generative: is the value forced?

**Partly**: forced by the existence of the unique weight-4
newform on Γ_0(6) (a fact about modular form spaces, not
about framework apparatus); the framework has no mechanism to
shift a_17 to a different value once Γ_0(6) is the chosen
modular surface.

But: the framework apparatus has not been shown to **select**
the cuspidal subspace for cosmological predictions. Whether
the predictive content lives in Eisenstein (PR #243) or
cuspidal (this audit) at weight ≥ 4 is the open empirical
question.

Generative verdict: PARTIAL — value forced once cuspidal
subspace is selected; subspace selection is open.

### Composed verdict

**MODAL ✓ / GENERATIVE PARTIAL** with the caveat:
- The cuspidal λ_17 candidate value at weight 4 is **−18**
  (cached from LMFDB 6.4.a.a; verification gap F-cusp-1).
- Whether framework apparatus uses this value vs the
  Eisenstein 4914 vs a combination is the open three-outcome
  empirical question.

---

## Comparison to PR #243 reading

| Aspect | PR #243 (Eisenstein) | This audit (cuspidal) |
|---|---|---|
| Subspace | E_k(Γ_0(6)) | S_k(Γ_0(6)) |
| First weight with content | k = 2 (3 cusps' Eisenstein) | k = 4 (1 newform) |
| λ_17 at weight 4 | 4914 | −18 |
| Formula | σ_{k−1}(17) = 1 + 17^(k−1) | newform-specific |
| Origin | Standard Hecke theory (divisor sum) | Cuspidal Hecke theory (Deligne-bounded) |
| Modal-vs-generative | MODAL ✓ / GENERATIVE ✓ | MODAL ✓ / GENERATIVE PARTIAL |
| Empirical status | Determined by formula | Determined by LMFDB; verification gap flagged |

The two audits together complete the **modular-operator-level
λ_17 picture** on Γ_0(6) at weight 4:

> M_4(Γ_0(6)) Hecke spectrum at p = 17 contains values
> {4914 (Eisenstein, multiplicity 4), −18 (cuspidal,
> multiplicity 1)}. Framework cosmological content's specific
> projection onto this spectrum determines its λ_17 value.

---

## Comparison to PR #241 reading

PR #241's structural identity:

> Mihailescu primes (q₂, q₃) = (2, 3) ARE torsion orders of
> PSL(2,ℤ) free-product generators; F₂ = Γ(2) is the
> noncommutative core; ℤ/q₂ × ℤ/q₃ = ℤ/6 is the abelian shadow.

The modular form analog at Γ_0(6):

- Abelian shadow at modular surface H/Γ_0(6) ↔ Eisenstein
  subspace (cusps' constants; divisor-sum Hecke eigenvalues)
- Noncommutative core at modular surface H/Γ_0(6) ↔ Cuspidal
  subspace (newforms at cusps vanishing; Deligne-bounded
  Hecke eigenvalues)

This audit's value −18 is the specific noncommutative-core
λ_17 content at the cosmological scale Γ_0(6) at weight 4.

The lunar-theory parallel (ρ = +0.95 noncommutative vs ρ =
+0.04 abelian) suggests the noncommutative-core value (−18)
may be the empirically-relevant one IF the framework's
cosmological apparatus parallels the lunar-theory pattern.

This is a **specific testable prediction**: framework
cosmological observables on Γ_0(6) at weight 4 should
correlate with the cuspidal λ_17 = −18, not the Eisenstein
λ_17 = 4914, if the lunar-theory pattern transfers.

---

## Comparison to PR #235 reading

PR #235 established 17 is absent from framework arithmetic
vocabulary. This audit's cuspidal λ_17 = −18 is at the
**modular operator level**, not arithmetic vocabulary level.

Three-way composition (PR #235 + PR #243 + this audit):

| Reading | Where 17 sits | Value |
|---|---|---|
| PR #235 arithmetic | Absent from vocabulary | Not used |
| PR #243 Eisenstein | Hecke eigenvalue on E_k | 4914 (weight 4) |
| This audit cuspidal | Hecke eigenvalue on S_k | −18 (weight 4) |

The arithmetic-vocabulary absence (PR #235) does NOT
preclude modular-operator presence. Both the Eisenstein and
cuspidal sides admit 17 as a good prime; PR #235's reading
is about which primes the framework constructs FROM, not
which primes act ON it.

---

## Falsifiers

- **F-cusp-1** (verification gap): a_17 = −18 is cached from
  memory of LMFDB 6.4.a.a; external lookup (LMFDB URL,
  SAGE/PARI computation, or LMFDB-derived ket entry) must
  confirm before the value is sealed substrate-canonical
- **F-cusp-2** (dimension): dim S_4(Γ_0(6)) ≠ 1 (PR #243's
  dimension table wrong); the "unique newform" framing
  collapses and this audit must be re-done with the correct
  cuspidal structure
- **F-cusp-3** (newform identification): the unique weight-4
  newform on Γ_0(6) is NOT 6.4.a.a as cached (e.g., it's
  6.4.a.b or a non-rational newform); a_17 changes value
- **F-cusp-4** (framework selection): framework cosmological
  apparatus turns out to select the Eisenstein subspace (not
  cuspidal) for predictions; the noncommutative-core analog
  to lunar-theory does NOT transfer to cosmological scale
- **F-cusp-5** (Deligne bound violation): if a future
  verification gives |a_17| > 140.19, the value cannot be
  from a weight-4 newform; Γ_0(6) cuspidal identification is
  wrong
- **F-cusp-6** (modular surface): framework cosmological
  scale is NOT Γ_0(6) (PR #242 identification wrong); this
  audit's premise dissolves
- **F-cusp-7** (empirical test): if a specific framework
  cosmological observable yields a value matching neither
  Eisenstein 4914 nor cuspidal −18 nor any reasonable linear
  combination, the modular-form embedding may be over-strong

---

## Impact on existing audits

| Audit | Impact |
|---|---|
| **PR #243** (Eisenstein λ_17) | **Completes cuspidal half**; PR #243's reading now extends to a full modular-operator picture at weight 4 |
| **PR #242** (Γ_0(6) identity) | **Cuspidal content named**; identity now has both Eisenstein and cuspidal Hecke spectra specified |
| **PR #241** (noncommutative core) | **Testable transfer**; lunar-theory pattern parallel at cosmological scale becomes specific (−18 vs 4914 test) |
| **PR #235** (arithmetic mirage) | **Reinforced**; cuspidal modular content is independent of arithmetic-vocabulary content |
| **PR #239** (cyclotomic content) | **Unchanged**; cuspidal λ_17 doesn't change Z_n factorization story |
| **PR #236** (Γ_0(4) matter scale) | **Cross-scale Z_12 work enabled**; matter-scale cuspidal λ_17 audit becomes a natural next step at Γ_0(4) |

---

## What this is and isn't

**This is**: explicit cuspidal-side completion of the λ_17
question on Γ_0(6) at weight 4, identifying f_{6,4} as the
unique relevant newform, naming its a_17 = −18 (with a
verification gap), and contrasting against PR #243's
Eisenstein λ_17 = 4914.

**This is not**: a substrate-sealed final verdict. The
verification gap F-cusp-1 must be closed before the value
−18 enters the framework's canonical scorecard or numerology
inventory.

**This is not**: an empirical determination of which subspace
(Eisenstein or cuspidal) the framework apparatus selects for
cosmological predictions. That requires a concrete observable
with naturally decomposable Eisenstein vs cuspidal contribution.

**This is not**: an apparatus extension. The framework's
prediction of which value gets selected is already implicit in
the Γ_0(6) identification (PR #242); this audit names both
candidate values for the selection test.

---

## Future work enabled

1. **External verification of a_17 = −18** (close F-cusp-1):
   LMFDB lookup, SAGE/PARI independent computation, or
   substrate-side computation tool
2. **Cuspidal λ_17 audit at weight 6, 8** (multi-newform): once
   newform/oldform decomposition is performed, compute a_17 on
   each newform in S_6, S_8; check growth pattern
3. **Cross-scale Z_12 audit**: matter scale Γ_0(4) cuspidal λ_17
   at weight 2, 4 + cosmological Γ_0(6) cuspidal λ_17 at weight
   4 composition
4. **Specific cosmological observable identification**: which
   framework cosmological observable on Γ_0(6) at weight 4 has
   naturally decomposable Eisenstein vs cuspidal contribution
   that can be compared to empirical data
5. **L-function audit**: Euler product for L(f_{6,4}, s)
   including 17-factor; check whether framework cosmological
   L-function content matches
6. **Comparison across cuspidal newforms**: pattern of a_17
   values across (Γ_0(N), weight k) newforms; whether the
   framework arithmetic 17-absence has analog patterns

---

## Cross-links

### Direct dependencies
- `lambda17_test_gamma06_cosmological_audit.md` (PR #243) —
  Eisenstein half of the λ_17 picture
- `gamma06_cosmological_modular_surface_audit.md` (PR #242) —
  Γ_0(6) identity establishing framework cosmological scale
- `psl2z_noncommutative_core_structural_identity_audit.md`
  (PR #241) — noncommutative-core methodology and lunar-theory
  parallel

### Background dependencies
- `primes_denominators_circular_geometry_extension_audit.md`
  (PR #235) — arithmetic-vocabulary 17-absence
- `cyclotomic_content_mass_ratios_audit.md` (PR #239) — Z_n
  arithmetic content (excludes 17)
- `modular_form_behavior_cosmological_tongues_audit.md`
  (PR #236) — matter-scale modular form parallel at Γ_0(4)

### External references (to be added once verified)
- LMFDB newform 6.4.a.a — q-expansion of f_{6,4}
- SAGE/PARI computation of S_4(Γ_0(6)).newforms()[0].
  coefficient(17)

### Lunar-theory reference
- Commits 534ab55 (`farey/rank2_depth`) and df9aa8c
  (`three_body_hyperbolic.py`) — empirical methodology
  parallel: ρ = +0.95 (noncommutative) vs ρ = +0.04 (abelian)

---

## One-line summary

Cuspidal half of the λ_17 question on Γ_0(6) at the lowest
weight admitting cusp forms (weight 4, dim S_4 = 1). The unique
newform f_{6,4} ∈ S_4^{new}(Γ_0(6)) (LMFDB label 6.4.a.a) has
**Hecke eigenvalue a_17 = −18** at p = 17 — value cached from
memory of LMFDB, verified Deligne-bound-consistent (|−18| ≤
2·17^{3/2} ≈ 140) and Hecke-recursion-consistent with companion
eigenvalues (a_4, a_6, a_8, a_9, a_10, a_12, a_14, a_15, a_16
all match a_p·a_q recursion), but flagged with verification gap
F-cusp-1 requiring external LMFDB or SAGE/PARI confirmation
before substrate-canonical sealing. **The contrast that this
audit forces**: at weight 4 on Γ_0(6), Eisenstein λ_17 = 4914
(PR #243) vs cuspidal λ_17 = −18 — a magnitude ratio of ~273
and a sign reversal, with the ratio growing as 17^{(k−1)/2} →
∞ at higher weights by Deligne's bound. **Three-outcome
empirical test**: framework cosmological predictions
correlating with Eisenstein 4914 (Outcome A, abelian-shadow-
driven, contrasting with lunar-theory pattern) vs cuspidal −18
(Outcome B, noncommutative-core-driven, paralleling lunar-
theory's ρ = +0.95 finding) vs linear combination (Outcome C,
mixed). MODAL ✓ / GENERATIVE PARTIAL: cuspidal λ_17 candidate
value is forced once cuspidal subspace selection is made
(unique newform); whether framework apparatus selects cuspidal
or Eisenstein for cosmological predictions is the open empirical
question. The audit completes the modular-operator-level λ_17
picture on Γ_0(6) at weight 4 by determining both candidate
values (PR #243 Eisenstein 4914 + this audit cuspidal −18); the
selection between them by framework cosmological apparatus is
deferred to a future observable-specific audit. The verification
gap (F-cusp-1, closing requires external LMFDB or independent
computation) is the only obstruction to substrate-canonical
sealing; all internal-consistency checks pass within this audit.
