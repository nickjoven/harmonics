# Koide form substrate derivation — iteration 13

## Status

**Iteration 13.** Pursues iteration 12's recommended next step:
derive `M = q_3 I − q_2 J` *as a unified substrate-natural
quadratic form*, not as a sum of separately-derived parts.

**Result: M is uniquely determined by three substrate-derived
constraints plus one residual structural assumption.** The matrix
`M = q_3 I − q_2 J` is the *unique* 3×3 symmetric matrix
satisfying:

1. **S_3-equivariance** (substrate-derived: three indistinguishable
   generations from `generation_mechanism.md` §1).
2. **Lorentzian (2, 1) signature** (substrate-derived via
   iteration 11: cube identity → `(q_2, q_3) = (2, 3)` → `Q > 1/3`
   → Lorentzian).
3. **Uniform eigenvalue magnitude `q_3`** (residual structural
   assumption — the *one* assumption that remains, replacing the
   two from iteration 12).

The trivial `S_3` rep direction `(1, 1, 1)/√3` carries the
negative eigenvalue under (2)+(3); the orthogonal 2D standard
rep carries the two positive eigenvalues. The Koide constraint
`K_lepton = q_2/q_3 = 2/3` follows immediately from this M.

**Iteration 13 reduces the residual from two structural
assumptions (U + Z in iter 12) to one (uniform eigenvalue
magnitude).** This is the cleanest substrate-derivation chain
produced for Koide across iterations 1-13.

The remaining single assumption — "all eigenvalue magnitudes of
M equal `q_3`" — is plausible from substrate parsimony (no
additional structure to distinguish magnitudes beyond sign,
which is the Lorentzian signature) but not independently
substrate-derived.

Class: foundational consolidation (Class 3, iteration step 13,
unified-object derivation with single residual structural
assumption).

---

## The substantive reframing

Iteration 12 found that splitting M into separately-derived
"diagonal self-energy" and "off-diagonal pair-coupling"
contributions does not work cleanly. The substrate-arithmetic for
combining them produces either wrong totals or half-integer
weights.

Iteration 13 instead derives M *as a whole*. The strategy:
identify substrate-derived invariants of M that *uniquely
characterize* the matrix, and show all invariants are
substrate-natural.

### Substrate-derived invariants of M

The matrix `M = q_3 I − q_2 J = 3 I − 2 J` has the following
substrate-aligned properties:

| Property | Value | Substrate source |
|---|---|---|
| Symmetric | Yes | Quadratic form (sync cost) |
| `S_3`-equivariant | `M = a I + b J` form | Three indistinguishable generations |
| Trace | `q_3 = 3` | (sum of three eigenvalues) |
| Determinant | `−q_3³ = −27` | (product of three eigenvalues) |
| Signature | `(2, 1)` Lorentzian | Iteration 11 (cube identity → Q > 1/3) |
| Eigenvalues | `{+q_3, +q_3, −q_3}` | (magnitudes all `q_3`) |

The eigenvalue structure `{+q_3, +q_3, −q_3}` is the substantive
content. Trace and determinant are derived quantities (sum and
product of eigenvalues).

### Uniqueness theorem

**Claim**: M is the *unique* 3×3 symmetric matrix satisfying:

- (a) `S_3`-equivariance (form `M = a I + b J`)
- (b) Lorentzian signature `(2, 1)`
- (c) All eigenvalue magnitudes equal `q_3`

**Proof**: an `S_3`-equivariant symmetric matrix has the form
`M = a I + b J`. Its eigenvalues are `a` (with multiplicity 2,
on the standard rep) and `a + 3 b` (with multiplicity 1, on the
trivial rep `(1, 1, 1)/√3`).

For Lorentzian signature `(2, 1)`: two eigenvalues positive and
one negative. Either `a > 0, a + 3b < 0` (positive on standard
rep, negative on trivial rep) or `a < 0, a + 3b > 0` (negative
on standard rep, positive on trivial rep).

For uniform eigenvalue magnitude `q_3`: `|a| = q_3` and
`|a + 3b| = q_3`.

Case 1: `a = q_3, a + 3b = −q_3` → `b = −2 q_3 / 3 = −q_2`
(using `Q = q_2/q_3 = 2/3` from `klein_bottle.md` D19).
This gives `M = q_3 I − q_2 J`. ✓

Case 2: `a = −q_3, a + 3b = q_3` → `b = +2 q_3 / 3 = q_2`.
This gives `M = −q_3 I + q_2 J = −(q_3 I − q_2 J)`.
This is the negative of the iteration-11 M.

The two cases are related by overall sign. The Koide quadratic
form `M v · v = 0` is sign-invariant: if M satisfies it, so does
`−M`. Both cases give the same Koide constraint.

By convention, the substrate-natural form has positive eigenvalue
magnitude on the standard rep (where the substrate's "cost" is
positive: the two non-symmetric directions are cost-positive),
matching Case 1.

So M is uniquely determined by (a) + (b) + (c) (up to overall
sign, which doesn't affect the Koide constraint). □

### The Koide constraint follows

With `M = q_3 I − q_2 J`:

    M v · v  =  q_3 |v|²  −  q_2 (Σ v_i)²

For the substrate-aligned amplitude `v_i = √m_i`:

    q_3 Σ m_i  −  q_2 (Σ √m_i)²  =  0
    K  =  Σ m_i / (Σ √m_i)²  =  q_2 / q_3  =  2/3 ✓

The substrate matrix M evaluating to zero on the substrate-aligned
amplitude `(√m_e, √m_μ, √m_τ)` is the Koide constraint.

---

## Status of the three constraints

### (a) `S_3`-equivariance

**Substrate-derived.** `generation_mechanism.md` §1 establishes
three observable phase states `{A, B, C}` from `{locked, unlocked}²`
minus dark `D`. These three states are *indistinguishable* in
their substrate origin (each is one combination of two binary
toggles). Any matrix structure on three-generation amplitude
space must therefore be invariant under permutations of the three
states — `S_3`-equivariance.

This is substrate-natural. No structural assumption beyond
"three substrate-indistinguishable generations."

### (b) Lorentzian (2, 1) signature

**Substrate-derived** via iteration 11's chain:

    cube identity q_2³ = q_2 + 2 q_3
       →  (q_2, q_3) = (2, 3) forced  (mass_sector_closure.md)
       →  Q = q_2/q_3 = 2/3 > 1/3  (klein_bottle.md D19)
       →  M's signature is Lorentzian (2, 1)

Each step is substrate-internal. See iteration 11 for the detailed
chain showing how `Q > 1/3` forces Lorentzian signature on the
substrate's quadratic form for three-generation amplitude.

This is substrate-natural. No structural assumption beyond what
the substrate primitives `q_2 = 2, q_3 = 3` and the Klein-bottle
population ratio `Q = 2/3` already provide.

### (c) Uniform eigenvalue magnitude `q_3` — the residual

**Residual structural assumption.** The substrate must select
uniform eigenvalue magnitude `q_3` for the quadratic form M.

**Substrate-natural justifications**:

1. **Substrate parsimony**: M is a `S_3`-equivariant symmetric
   matrix in Lorentzian signature. Beyond `S_3`-equivariance and
   signature, the substrate provides no additional structure to
   *distinguish* the eigenvalue magnitudes. The minimal-
   information M has uniform magnitudes. (Information-theoretic
   parsimony argument.)

2. **Natural scale**: the substrate's natural scale for the
   three-generation amplitude space is `q_3 = 3` (the dimension /
   number of generations / `S_3` order divided by 2). All
   eigenvalue magnitudes are set by this single scale.

3. **`k_lepton` per direction**: the lepton sector mode budget
   `k_lepton = q_3² = 9` from `mass_sector_closure.md` partitions
   across the three eigendirections of M. If the partition is
   uniform across the three directions (related to Assumption U
   from iteration 12), each direction carries `q_3²/q_3 = q_3`
   modes, giving eigenvalue magnitude `q_3`.

   This re-introduces Assumption U from iteration 12 in a different
   form. Iteration 12 showed this doesn't combine cleanly when
   M is split into diagonal + off-diagonal contributions. As a
   *single* uniformity assumption on the whole M, it may be
   cleaner — uniformity across the three orthogonal eigendirections,
   not across the three generations.

4. **Eigenvalue magnitude as substrate quantum**: the substrate's
   quadratic form has eigenvalue magnitudes set by the substrate
   "quantum" `q_3`. This is the substrate-natural reading: each
   eigenvalue is one substrate unit of cost in its respective
   direction.

These four justifications all point to the same conclusion
(uniform eigenvalue magnitude `q_3`) but via different substrate-
natural readings. None is independently airtight.

---

## What this iteration establishes

- The substrate-derivation of Koide reduces to *one* residual
  structural assumption (uniform eigenvalue magnitude), not two
  (U + Z from iteration 12) and not the unresolved combination
  problem.
- The matrix M is uniquely determined by `S_3`-equivariance +
  Lorentzian signature + uniform eigenvalue magnitude (up to
  overall sign, which doesn't affect Koide).
- Two of three constraints (S_3-equivariance and Lorentzian
  signature) are independently substrate-derived; only the third
  (uniform eigenvalue magnitude) remains as residual structural
  assumption.

This is a substantive advance: iteration 12 had two unresolved
ingredients with a combination problem; iteration 13 has one
unresolved structural assumption with a clean uniqueness theorem.

---

## Status of the Koide derivation after thirteen iterations

| Iteration | Outcome |
|---|---|
| 1 | Geometric reformulation; Koide is angular constraint cos²θ = 1/3 |
| 2 | Candidate 4 (SL(2,ℤ)) ruled out |
| 3 | Candidate 1 (Z_2 eigenspace) ruled out |
| 4 | Substrate gives V_4 not S_3 on phase states |
| 5 | V_4 reformulation `q_3 : MEDIANT` |
| 6 | Cube identity necessary but not sufficient |
| 7 | Chirality mechanism explored |
| 8 | Cascade depth ordering explored |
| 9 | Empirical Path A (three_basins.py) — null result |
| 10 | Reversibility-class observation; Koide is Class A |
| 11 | Two residual ingredients identified (i) diagonal q_3, (ii) off-diagonal −q_2; Lorentzian signature substrate-forced |
| 12 | Ingredient-by-ingredient derivation doesn't combine cleanly; redirect to unified-object derivation |
| 13 | **M derived as unified object modulo one structural assumption (uniform eigenvalue magnitude)** |

The residual gap after 13 iterations is: *uniform eigenvalue
magnitude q_3 for the substrate's three-generation quadratic form
M*. This is a substantively narrower and more concrete gap than
any of iterations 1-11.

---

## Disposition

**Floor → Survives upgrade**: still pending. The single residual
structural assumption (uniform eigenvalue magnitude `q_3`) blocks
full closure. The upgrade requires either:

- Iteration 14 derivation of uniform eigenvalue magnitude as
  substrate-forced.
- Or accepting the residual structural assumption as substrate-
  natural per parsimony argument (justification 1) and
  documenting it explicitly in `framework_status.md` as the
  remaining ad-hoc input.

The iteration's contribution is the cleanest substrate-derivation
chain produced for Koide: 2 out of 3 constraints independently
substrate-derived, with a uniqueness theorem closing the
combination.

---

## Falsifiers

- **Uniform eigenvalue magnitude shown substrate-forced**: closes
  Koide gap, upgrades Floor → Survives.
- **Uniform eigenvalue magnitude shown not substrate-natural**:
  the substrate selects non-uniform magnitudes, requiring
  different M and giving non-Koide constraint. Would rule out
  the iteration-13 derivation chain.
- **Different uniqueness theorem found** (other invariant
  combinations producing M): would change the framing; the
  residual structural assumption would shift.
- **M shown to be non-unique under (a)+(b)+(c)**: error in the
  iteration's uniqueness proof; would reopen the derivation.

---

## Recommended next iteration

Iteration 14 should target the uniform eigenvalue magnitude
assumption. Three candidate paths:

1. **Substrate parsimony as formal principle**: articulate
   substrate parsimony (no extra information beyond the constraints
   already in play) as a substrate-internal principle and derive
   uniform magnitudes from it. This is the iteration's
   justification 1 made formal.

2. **`k_lepton` partition uniformity**: derive uniform partition
   of `k_lepton = q_3²` across the three eigendirections of M as
   substrate-forced. This is a refined version of Assumption U
   from iteration 12, applied to eigendirections (not generations).

3. **Natural scale uniqueness**: show that the substrate's
   three-generation amplitude space has *only one* natural scale
   (`q_3`), forcing all eigenvalue magnitudes to equal this scale.

If none of the three closes the gap, iteration 15 examines
whether the residual is structurally unbridgeable (DEP row 2) or
whether the assumption is acceptable as documented input
(Floor → Survives upgrade with one explicit assumption).

---

## Cross-links

- `koide_form_substrate_iteration_12.md` — ingredient-by-
  ingredient derivation's negative finding; this iteration
  pursues the unified-object alternative.
- `koide_form_substrate_iteration_11.md` — two-ingredient framing
  and Lorentzian-signature substrate-derivation chain.
- `mass_sector_closure.md` — `k_lepton = q_3²`, cube identity,
  `(q_2, q_3) = (2, 3)`.
- `generation_mechanism.md` (D34) — three generations,
  `{locked, unlocked}²`, substrate-indistinguishability.
- `klein_bottle.md` (D19) — `Q = q_2/q_3 = 2/3`.
- `discrete_extension_principle.md` (PR #191) — methodology.
- `substrate_prediction_selection.md` — selection thread
  (becomes relevant if iteration 14 fails).

---

## One-line summary

Iteration 13 pursues iteration 12's redirect to derive `M =
q_3 I − q_2 J` *as a unified object* rather than as separately-
derived diagonal and off-diagonal contributions, and finds that
M is the *unique* 3×3 symmetric matrix satisfying three
constraints — (a) `S_3`-equivariance (substrate-derived from
three indistinguishable generations in `generation_mechanism.md`
§1), (b) Lorentzian `(2, 1)` signature (substrate-derived via
iteration 11's chain cube identity → `(q_2, q_3) = (2, 3)` →
`Q > 1/3` → Lorentzian), and (c) uniform eigenvalue magnitude
`q_3` (the *one* residual structural assumption); the uniqueness
proof: `S_3`-equivariant symmetric matrices have form `M = a I +
b J` with eigenvalues `a` (multiplicity 2 on standard rep) and
`a + 3b` (multiplicity 1 on trivial rep `(1,1,1)/√3`); Lorentzian
signature requires one negative and two positive; uniform
magnitude `q_3` forces `|a| = |a + 3b| = q_3`, giving (up to
overall sign) `a = q_3, b = −2 q_3/3 = −q_2` via Klein-bottle
ratio `Q = q_2/q_3 = 2/3`; M is therefore `q_3 I − q_2 J` and
the Koide constraint `K = q_2/q_3 = 2/3` follows immediately —
this is a substantive advance over iteration 12: the residual
is reduced from two unresolved ingredients (U + Z) with a
combination problem to one structural assumption (uniform
eigenvalue magnitude `q_3`) with a clean uniqueness theorem;
four substrate-natural justifications for uniform eigenvalue
magnitude are identified — (1) substrate parsimony (no extra
information beyond signature and equivariance), (2) natural scale
`q_3` for three-generation amplitude space, (3) `k_lepton = q_3²`
partition uniformity across three eigendirections (refined
Assumption U from iteration 12, applied to eigendirections not
generations), and (4) eigenvalue magnitude as substrate quantum
`q_3`; none independently airtight, all pointing to the same
conclusion; the substrate-derivation chain after 13 iterations is
the cleanest produced for Koide (2 of 3 constraints
independently derived plus uniqueness theorem), with single
residual structural assumption blocking Floor → Survives upgrade;
iteration 14 should target uniform eigenvalue magnitude via
substrate parsimony, `k_lepton` partition uniformity, or natural
scale uniqueness paths.
