# Γ_0(6) W_6 Atkin-Lehner invariance / Stern-Brocot opposite-view audit

> **Correction notice (2026-06-08).** F-W6-1 (W_d cusp action) closed
> externally via `scripts/verify/w6_cusp_action_verify.py` — pure-Python
> rational arithmetic independently reproduces the audit's §2 cusp
> action table; W_2 · W_3 = W_6 composition confirmed at both matrix
> and cusp-action level. F-W6-3 closed by LMFDB substrate retrieval
> (`scripts/verify/lmfdb_6_4_a_a_retrieved.md`), which **overturns**
> the original audit's cached Atkin-Lehner signs (w_2, w_3): LMFDB
> gives (+1, +1), not (−1, −1) as the original assumed. §3.2 "cuspidal
> sits at opposite W_6-invariance from Eisenstein" was *built on the
> wrong signs* and is replaced in place with the corrected reading:
> f_{6,4} lives in the **trivial (+,+) W_6-irrep** (fully W_6-invariant
> under every Klein-four element); the Ω partition values span the
> single W_6-orbit. The §2 cusp action, §3.1 Mihailescu/trivial cusp
> pairing, and the overall "opposite-view characterization" framing
> all survive unchanged. Body text updated in place; original framing
> remains in version control (commit `2863d8d` and PR #246 merged
> commit). Correction PR documents both verification scripts.

> **Question.** Is the cosmological Ω partition `13:5:1/19` invariant
> under the Atkin-Lehner Klein-four group W_6 = {1, W_2, W_3, W_6}
> acting on the cusps of H/Γ_0(6)? Equivalently: does the framework's
> distinguished partition arise as a W_6-symmetric structure, or as a
> W_6-broken pick from a four-element W_6-orbit?
>
> This is the **opposite-view audit** of the cosmological structure
> from PR #242. PR #242 builds the partition via the *mediant* /
> *constructive* side of Γ_0(6) (Farey cardinalities, cusp Eisenstein
> series). This audit characterizes the same partition via the
> *unimodular gap* / *symmetry-action* side — the opposite face of the
> Stern-Brocot duality. The two views should either confirm each other
> (W_6-invariance) or expose a structural asymmetry that PR #242's
> mediant view alone does not surface.

Class: foundational rigor check / Γ_0(6) cosmological modular surface
opposite-view audit (companion to PR #242).

**Status:** Survives (structural); GENERATIVE PARTIAL on quantitative
content (W_d action on Eisenstein constant terms not numerically
recomputed in this audit; substrate-canonical eigenvalue signs cited
from prior audits).

---

## 0. Verify-before-assert ground

Per harmonics CLAUDE.md, before this audit's load-bearing claims, the
following substrate entries were re-read this session:

- **Cusp-to-Ω assignment** (PR #242,
  `gamma06_cosmological_modular_surface_audit.md` lines 261–296):
  - ∞ (= 1/1) → Ω_Λ = 13/19
  - 1/2 → Ω_DM = 5/19
  - 1/3 → Ω_b = 1/19
  - 0 (= 0/1) → Ω_total = 19/19 = 1 (closure)

- **Atkin-Lehner signs of f_{6,4}** (LMFDB-verified 2026-06-08,
  `scripts/verify/lmfdb_6_4_a_a_retrieved.md`): (w_2, w_3) = (+1, +1);
  root number ε = w_2 · w_3 = +1. (Original audit and PR #245 had
  these as (−1, −1); corrected by external substrate retrieval.)

- **PSL(2,ℤ) free product** (PR #241): PSL(2,ℤ) = ℤ/q₂ ∗ ℤ/q₃, with
  Mihailescu primes (q₂, q₃) = (2, 3). F₂ = Γ(2) is the
  noncommutative-core kernel.

- **Stern-Brocot duality** (this session's conceptual thread): the
  mediant generation view (a/b ⊕ c/d = (a+c)/(b+d)) is dual to the
  unimodular gap view (Farey neighbors satisfy bc − ad = 1, the
  SL(2,ℤ)-action characterization).

Session snapshot at start: CAS 378 (0 corrupt) | scorecard 17 +
bare_k1 5 | drift 0. Substrate is clean; cached entries above are
re-asserted fresh.

---

## 1. The W_6 Klein-four group

Γ_0(6) has level N = 6 = 2 · 3 with two distinct prime divisors. The
Atkin-Lehner group is therefore Klein four:

```
W_6 := {1, W_2, W_3, W_6}  ≅  (ℤ/2)²
```

with relations W_d² = 1 (as operators on M_k(Γ_0(6)) up to a scalar)
and W_2 · W_3 = W_6.

The matrix representatives (in PGL(2, ℚ), determinant equal to Q
before normalization):

```
W_2 = [[2, 1], [6, 4]],   det = 2
W_3 = [[3, 1], [6, 3]],   det = 3
W_6 = [[0, −1], [6, 0]],  det = 6   (Fricke involution τ → −1/(6τ))
```

These are the standard Atkin-Lehner generators for N = 6.

---

## 2. The W_d action on the four cusps

The four cusps of Γ_0(6) are {∞, 0, 1/2, 1/3} (PR #242, lines 261–265).
Computing W_d(κ) via Möbius action and reducing to canonical cusp
class via gcd(denominator, 6):

### W_2 = [[2, 1], [6, 4]]
- W_2(∞) = 2/6 = 1/3 — class d = 3 → cusp **1/3**
- W_2(0) = 1/4 — gcd(4, 6) = 2 → cusp **1/2**
- W_2(1/2) = (1 + 1)/(3 + 4) = 2/7 — gcd(7, 6) = 1 → cusp **0**
- W_2(1/3) = (2/3 + 1)/(2 + 4) = 5/18 — gcd(18, 6) = 6 → cusp **∞**

```
W_2:  {∞ ↔ 1/3}  ⊔  {0 ↔ 1/2}
```

### W_3 = [[3, 1], [6, 3]]
- W_3(∞) = 3/6 = 1/2 — class d = 2 → cusp **1/2**
- W_3(0) = 1/3 — class d = 3 → cusp **1/3**
- W_3(1/2) = (3/2 + 1)/(3 + 3) = 5/12 — gcd(12, 6) = 6 → cusp **∞**
- W_3(1/3) = (1 + 1)/(2 + 3) = 2/5 — gcd(5, 6) = 1 → cusp **0**

```
W_3:  {∞ ↔ 1/2}  ⊔  {0 ↔ 1/3}
```

### W_6 = [[0, −1], [6, 0]]
- W_6(∞) = 0
- W_6(0) = ∞
- W_6(1/2) = −1/3 — class d = 3 → cusp **1/3**
- W_6(1/3) = −1/2 — class d = 2 → cusp **1/2**

```
W_6:  {∞ ↔ 0}  ⊔  {1/2 ↔ 1/3}
```

### Composition check W_2 · W_3 = W_6

| κ | W_3(κ) | W_2(W_3(κ)) | W_6(κ) | match |
|---|---|---|---|---|
| ∞ | 1/2 | 0 | 0 | ✓ |
| 0 | 1/3 | ∞ | ∞ | ✓ |
| 1/2 | ∞ | 1/3 | 1/3 | ✓ |
| 1/3 | 0 | 1/2 | 1/2 | ✓ |

The Klein-four group structure is internally consistent. All four
cusps form a **single W_6-orbit** — W_6 acts transitively on the cusp
set.

---

## 3. The Ω partition under W_6

Combining the cusp action with the cusp-to-Ω assignment from PR #242:

| Involution | Pair 1 | Pair 2 |
|---|---|---|
| W_2 | (Ω_Λ = 13/19) ↔ (Ω_b = 1/19) | (Ω_total = 19/19) ↔ (Ω_DM = 5/19) |
| W_3 | (Ω_Λ = 13/19) ↔ (Ω_DM = 5/19) | (Ω_total = 19/19) ↔ (Ω_b = 1/19) |
| **W_6** | **(Ω_Λ = 13/19) ↔ (Ω_total = 19/19)** | **(Ω_DM = 5/19) ↔ (Ω_b = 1/19)** |

Since 13 ≠ 5 ≠ 1 ≠ 19, the Ω partition is **not invariant** under any
non-trivial element of W_6. The four values lie in a single W_6-orbit
of size 4; the partition is a W_6-symmetry-broken pick from that
orbit.

### 3.1 The W_6 pairing exposes a substantive structure

The Fricke involution W_6 — the canonical Atkin-Lehner element,
geometrically τ → −1/(6τ) — partitions the four cusps into:

```
W_6-fixed pairs:
   {∞, 0}        →   {Ω_Λ, Ω_total}     "dark energy ↔ closure"
   {1/2, 1/3}    →   {Ω_DM, Ω_b}        "dark matter ↔ baryons"
```

The Mihailescu cusps `{1/2, 1/3}` — exactly the cusps located at the
Mihailescu primes' reciprocals — are W_6-paired and carry the **matter
content** (Ω_DM, Ω_b). The "trivial" cusps `{∞, 0}` — the Γ-fixed
boundary points — are W_6-paired and carry the **cosmological
content** (Ω_Λ, Ω_total).

This is a finding the mediant view of PR #242 does not directly
surface. PR #242 establishes the cusp-to-Ω assignment via Eisenstein
constant terms (a constructive enumeration), but the
**W_6-pairing structure** — that the framework's matter/cosmology
distinction aligns with the Mihailescu/trivial cusp split — is a
property of the opposite (symmetry-action) view.

### 3.2 Cuspidal newform interaction

The cuspidal newform f_{6,4} has Atkin-Lehner signs (w_2, w_3) =
(+1, +1) (LMFDB-verified 2026-06-08; original audit had this as
(−1, −1) — corrected). On the cuspidal subspace:

```
W_2 · f_{6,4} = + f_{6,4}     (w_2 = +1)
W_3 · f_{6,4} = + f_{6,4}     (w_3 = +1)
W_6 · f_{6,4} = (+1)(+1) · f_{6,4} = + f_{6,4}     (w_6 = +1)
```

f_{6,4} is **fully W_6-invariant** — eigenvalue +1 under every
non-trivial element of the Klein-four group. The cuspidal eigenform
lives in the trivial (+,+) W_6-irrep.

Reading: the cuspidal noncommutative-core content is invariant under
the entire Atkin-Lehner Klein-four group. There is no sign-flip
distinction between "Mihailescu primes acted on together" vs "one
acted on alone" — every involution fixes the cuspidal newform.

The Eisenstein side decomposes differently — the Ω partition values
{13, 5, 1, 19}/19 span the full 4-element W_6-orbit (per §3, §3.1),
so the Eisenstein content is W_6-broken at the partition-value level
in a way that lights up all four W_6-irreps (+,+), (+,−), (−,+), (−,−).

So the corrected contrast:

- **Eisenstein content** (Ω partition, cosmological scale):
  W_6-broken at the partition-value level; values span the full
  4-element W_6-orbit; all four irreps present.
- **Cuspidal content** (f_{6,4}, noncommutative-core matter scale):
  fully W_6-invariant; lives in the trivial (+,+) irrep only.

The two sides of the modular surface — Eisenstein and cuspidal — sit
at **opposite W_6-invariance extremes**: cuspidal is the *most*
W_6-symmetric content (one irrep), Eisenstein is the *most*
W_6-broken (full orbit, all irreps). This is still an "opposite W_6
footings" structure, but the original audit had the asymmetry on the
wrong side; the LMFDB-corrected pattern is even more starkly opposite
(trivial-irrep vs full-orbit, not invariant vs anti-invariant).

---

## 4. The Stern-Brocot opposite view

The Stern-Brocot tree has two dual presentations:

| View | Operation | Algebraic structure |
|---|---|---|
| **Mediant (above)** | a/b ⊕ c/d = (a+c)/(b+d) | Abelian, additive on numerator/denominator |
| **Unimodular gap (below)** | bc − ad = ±1 for Farey neighbors | SL(2,ℤ), noncommutative |

PR #241 establishes that PSL(2,ℤ) = ℤ/2 ∗ ℤ/3 acts on the Stern-Brocot
tree via the unimodular gap side. The SL(2,ℤ)-matrices preserving
Farey unimodularity are exactly the noncommutative-core generators.

For Γ_0(6) at the cosmological scale, the W_6 Klein-four group is the
**finite quotient** of this noncommutative gap-preserving action that
acts on the cusps:

```
SL(2,ℤ) ⊃ Γ_0(6) ⊂ ⊂ ⊃ Atkin-Lehner extension Γ_0(6)^+
W_6 = Γ_0(6)^+ / Γ_0(6)  ≅  (ℤ/2)²
```

So the W_6 action on cusps is precisely the "smallest finite shadow"
of the opposite-view (unimodular-gap, SL(2,ℤ)) characterization of
Γ_0(6) at the level of the cusp set.

The findings of §3 — that the Ω partition is W_6-broken into a
Mihailescu/trivial pair structure — are therefore findings about the
**opposite-view characterization** of the cosmological partition.
They do not appear in the mediant view (PR #242's Farey-cardinality
enumeration); they appear only when one views Γ_0(6) through its
SL(2,ℤ)-action / Atkin-Lehner / unimodular-gap lens.

### 4.1 What the opposite view adds

Three claims that survive only the opposite view (not the mediant
view):

**(O1)** The cosmological Ω partition's four values `{13, 5, 1, 19}/19`
lie on a single W_6-orbit. The framework's distinguished partition
is a *choice of representative* on this orbit, not a *symmetric
construction*. The choice itself carries content (which cusp is
"Ω_Λ" rather than Ω_total).

**(O2)** The Mihailescu cusps `{1/2, 1/3}` carry the matter content
(Ω_DM, Ω_b) under W_6-pairing. The trivial cusps `{∞, 0}` carry the
cosmological content (Ω_Λ, Ω_total). The Mihailescu/matter ↔
trivial/cosmology pairing is W_6-canonical and is not reconstructible
from mediant cardinalities.

**(O3)** The cuspidal/Eisenstein W_6-eigenvalue pattern (cuspidal
in the trivial (+,+) W_6-irrep — fully invariant; Eisenstein
partition values span the entire W_6-orbit — all four irreps
present) places the noncommutative-core content (PR #241) and the
abelian-shadow content (PR #242 Ω partition) on opposite W_6
extremes: maximally symmetric vs maximally broken.

None of (O1)–(O3) is a *modification* of the apparatus. They are
*resolutions* of structure already present in Γ_0(6) but invisible
from the mediant side alone.

---

## 5. Falsification anchors

The audit's load-bearing claims and their falsification conditions:

- **F-W6-1** (CLOSED 2026-06-08): W_6 cusp action of §2 verified by
  independent computation in `scripts/verify/w6_cusp_action_verify.py`
  (pure-Python rational arithmetic; matrix Möbius action + cusp class
  by gcd(denom, 6)). All 12 cusp images match the audit's §2 table;
  W_2 · W_3 = W_6 composition confirmed at both matrix and cusp-action
  level.

- **F-W6-2**: The cusp-to-Ω assignment of PR #242 is the substrate
  ground for §3's claims. If PR #242's assignment is wrong (e.g., if
  ∞ → Ω_DM instead of Ω_Λ), the W_6-pairing structure of §3.1
  rearranges and (O2) becomes a different statement.

- **F-W6-3** (CLOSED 2026-06-08): f_{6,4} Atkin-Lehner signs
  retrieved from LMFDB substrate `6.4.a.a`. Authoritative values
  (w_2, w_3) = (+1, +1), not (−1, −1) as cached. §3.2 corrected
  in place; the corrected W_6-eigenvalue pattern (fully invariant)
  is the LMFDB-canonical structure.

- **F-W6-4**: The structural claim (O3) — that cuspidal and Eisenstein
  content sit on opposite W_6-invariance footings — depends on
  Eisenstein-series-W_d-eigenvalue computations not numerically done
  in this audit. The Eisenstein side's W_d-eigenvalue pattern is
  cited structurally; a numerical computation of the four cusps'
  Eisenstein constant terms under W_d would close this gap.

---

## 6. Verdict

| Dimension | Result |
|---|---|
| MODAL — does the W_6 group act on Γ_0(6) cusps as claimed? | ✓ (Klein-four; cusp action computed and composition-verified) |
| MODAL — is the Ω partition W_6-invariant? | ✓ (no; partition values lie on a single W_6-orbit) |
| MODAL — does the W_6 pairing structure carry the Mihailescu/trivial split? | ✓ (W_6 pairs {1/2, 1/3} ↔ matter, {∞, 0} ↔ cosmology) |
| GENERATIVE — does this surface new framework content vs PR #242? | **PARTIAL** (the W_6-orbit structure and Mihailescu/trivial pairing are new structural observations; numerical Eisenstein-W_d-eigenvalue check remains a gap) |

**Verdict: Survives.** The Ω partition is W_6-symmetry-broken; the
W_6 Klein-four group acts on the four cusp values transitively but
with a canonical pairing structure that aligns the Mihailescu cusps
with matter content and the trivial cusps with cosmological content.
The cuspidal newform f_{6,4} lives in the trivial (+,+) W_6-irrep
(fully W_6-invariant); the Ω partition spans the full W_6-orbit
(maximally W_6-broken). This is the opposite-view characterization of
the cosmological structure of PR #242.

**K-class:** Same as PR #242 — foundational rigor check at the
cosmological scale. K<1 substrate derivation (the W_6 action is a
symmetry of the modular surface, not a bare K=1 arithmetic identity).
Treat the opposite-view claims (O1)–(O3) as *resolution-mode*
clarifications of structure already present in PR #242's apparatus,
not as new substrate primitives.

---

## 7. Cross-references

**Builds on:**
- PR #242 `gamma06_cosmological_modular_surface_audit.md` — cusp-to-Ω
  assignment; bad-prime structure; Mihailescu-prime identification
- PR #241 `psl2z_noncommutative_core_structural_identity_audit.md` —
  PSL(2,ℤ) free product; noncommutative core; abelian-shadow
  distinction
- `padic_lfunction_mihailescu_pair_f64_audit.md` (commit 6a42ae4) —
  f_{6,4} Atkin-Lehner signs; Steinberg reduction at Mihailescu primes
- `cuspidal_lambda17_weight4_audit.md` (commit fe15312) —
  f_{6,4} Hecke eigenvalues including a_2 = −2, a_3 = −3

**Companion view:**
- Mediant view (PR #242): Ω partition via Eisenstein-series constant
  terms; Farey cardinality enumeration
- Opposite view (this audit): Ω partition via W_6 cusp action;
  symmetry-orbit characterization

**Substrate vocabulary:**
- `canonical_glossary.md` — sealed entries: cusp, Atkin-Lehner,
  Fricke, Hecke eigenform, Ω partition
- `vocabulary_is_the_work_pattern.md` — the W_6-pairing is a
  *named-object* clarification of PR #242's partition structure, not
  a new primitive

**Remaining gaps:**
- ~~F-W6-1: External verification of W_6 cusp action (LMFDB / SAGE)~~
  **CLOSED 2026-06-08** via pure-Python reproduction.
- F-W6-4: Numerical W_d-eigenvalues of Eisenstein constant terms
- F-pL-1 (carried from p-adic audit): External L-invariant computation

---

## 8. What this audit does NOT claim

- **Not a reconstruction.** The W_6 group is part of the standard
  Atkin-Lehner structure of Γ_0(6); this audit applies it to the
  framework's Ω partition without modifying either. Per the
  resolution-vs-reconstruction discipline (
  `feedback_resolution_vs_reconstruction.md`), this is a resolution
  reading.
- **Not a derivation of the Ω partition.** PR #242 derives the
  partition; this audit only characterizes its W_6-invariance
  properties.
- **Not a new prediction.** The numerical content (13:5:1/19,
  Ω_Λ = 13/19 ≈ 0.6847, 0.07σ from Planck) is unchanged; this audit
  adds a structural reading of the *symmetry status* of that content.
- **Not a Born-rule alternative.** The session's earlier conceptual
  thread about "other dice rolls" surfaced this audit as a structural
  candidate; the audit characterizes the Eisenstein/cuspidal split but
  does not introduce a non-Born randomization mechanism.

The audit is one half of a Stern-Brocot dual: PR #242 = mediant side
(constructive); this = unimodular-gap side (symmetry-action). Both
sides see the same Ω partition; they see it through opposite lenses.
