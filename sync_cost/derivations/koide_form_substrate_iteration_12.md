# Koide form substrate derivation — iteration 12

## Status

**Iteration 12.** Tests whether the two residual ingredients
identified in iteration 11 can be substrate-derived from
foundational quantities. Targets Options A and B from iteration
11's recommended next iterations.

**Result: ingredients derived modulo two explicit structural
assumptions.** Both ingredients (i) the diagonal weight `q_3 = 3`
per generation in the matrix `M = q_3 I − q_2 J`, and (ii) the
off-diagonal weight `−q_2 = −2` per pair, follow from
substrate-derived foundational quantities — the lepton sector
mode budget `k_lepton = q_3² = 9` (`mass_sector_closure.md`) and
the number of generations `n_gens = 3 = q_3`
(`generation_mechanism.md`), and the Klein-antipodal Z_2
involution `τ` of order `q_2 = 2` (`klein_bottle.md` D19) — via
two **structural assumptions** that must be examined:

- **Assumption U** (Uniform distribution): the `k_lepton = q_3²`
  modes distribute uniformly across the `n_gens = q_3` generations.
- **Assumption Z** (Z_2-order-as-coupling): the Klein-antipodal Z_2
  contributes attractive coupling weight `q_2` per pair.

If both assumptions hold as substrate-natural, the matrix
`M = q_3 I − q_2 J` is fully substrate-derived and the Koide
constraint `K_lepton = q_2/q_3` closes (Floor → Survives).

**Both assumptions are *plausible* substrate readings but not
*independently derived***. This iteration explicitly identifies
them as the residual derivation work and proposes substrate-
natural justifications for each.

No new substrate primitive. The iteration converts the iteration-11
residual into two named structural assumptions with substrate-
internal candidate justifications, leaving final closure pending
verification of the assumptions.

Class: foundational consolidation (Class 3, iteration step 12,
ingredient derivation with explicit structural assumptions).

---

## Ingredient (i) — Diagonal weight `q_3` per generation

### The derivation

The framework's lepton sector has total mode budget:

    k_lepton  =  q_3²  =  9

derived from `mass_sector_closure.md` Theorem (squared SU(2)
adjoint dimension via chirality-doubling).

The number of generations:

    n_gens  =  3  =  q_3

derived from `generation_mechanism.md` §1 (three observable phase
states from `{locked, unlocked}²` − 1 dark, with `q_3 = 3`
matching color triplet count and spatial dimensions).

**Substrate-arithmetic identity**:

    k_lepton / n_gens  =  q_3² / q_3  =  q_3

This is two substrate-derived quantities divided. The arithmetic is
trivial; the substantive step is identifying *what* this quotient
represents.

**Substrate-natural reading**: "modes per generation" — each
generation carries `q_3` modes' worth of structure, derived as the
total lepton mode budget divided uniformly across the
substrate-derived number of generations.

### Assumption U — Uniform distribution

For the quotient `k_lepton / n_gens` to give the *per-generation
contribution* to the matrix diagonal, the `k_lepton` modes must
distribute *uniformly* across the `n_gens` generations.

**Substrate-natural justifications for Assumption U**:

1. **Permutation symmetry**: in the absence of additional
   distinguishing substrate structure on the lepton sector at the
   matrix-form level, the three generations are interchangeable
   under permutation. The matrix `M`'s diagonal must therefore
   have equal entries (`S_3`-equivariance), forcing uniform
   distribution.

2. **Information minimization**: the substrate-natural cost
   function on lepton amplitude space should have minimal
   information distinguishing generations beyond what the bare-tree
   formula already encodes (via base ratios `(1, 7, 26)` and sector
   exponent `5/2`). Uniform per-generation contribution adds no
   extra information; non-uniform would require additional
   substrate input.

3. **Hierarchy decoupling**: the bare-tree formula already encodes
   the mass hierarchy. The matrix `M`'s diagonal expresses the
   substrate-natural "self-energy" per generation independent of
   hierarchy. Uniform distribution is the minimal choice.

These justifications are plausible but not independently
substrate-derived. Assumption U remains an explicit structural
assumption pending verification.

---

## Ingredient (ii) — Off-diagonal weight `−q_2` per pair

### The derivation

The Klein-antipodal involution `τ` (`klein_bottle.md` D19) has
order:

    |τ|  =  q_2  =  2

(τ is a Z_2 involution: τ² = identity).

The three pairs of generations `(e, μ)`, `(e, τ)`, `(μ, τ)` form a
complete pair-wise coupling structure.

**Substrate-natural reading**: each pair of generations is coupled
through one Klein-antipodal Z_2 toggle. The "coupling strength"
inherits from the Z_2 order, giving `q_2 = 2` per pair. The sign
is negative (attractive) because locked-pair configurations have
lower substrate cost than antialigned configurations.

### Assumption Z — Z_2-order-as-coupling

For the Klein-antipodal Z_2's *order* (`q_2 = 2`) to be the
*coupling weight* in the matrix `M`'s off-diagonal, the
substrate's pair-wise coupling structure must be one where the
Z_2 order directly translates to the off-diagonal coefficient.

**Substrate-natural justifications for Assumption Z**:

1. **Z_2 eigenstate cost difference**: a Z_2 involution acting on a
   pair-wise amplitude `(v_i, v_j)` has symmetric `(v_i + v_j)/√2`
   and antisymmetric `(v_i − v_j)/√2` eigenstates with eigenvalues
   `+1` and `−1`. The cost difference between these eigenstates is
   set by the Z_2 order. For `q_2 = 2`, the cost difference equals
   `2` (in substrate units), giving off-diagonal coefficient `−1`
   per eigenstate sign — or `−q_2/2 = −1` per off-diagonal entry
   if the cost is split.

   This reading gives off-diagonal `−1`, not `−q_2 = −2`. Doesn't
   match cleanly. Discarded.

2. **Pair-wise Q_{AB} mod 2 conservation contribution**: the
   pair-wise Q_{AB} mod 2 conservation (`epr_bell_assembly_theorem.md`)
   gives a substrate-aligned Z_2-valued joint invariant per pair.
   The "weight" of this conservation is `q_2 = 2` (order of the
   Z_2). For each pair, the conservation contributes attractive
   coupling with weight `q_2` to the pair's substrate-natural
   joint amplitude cost.

   This gives off-diagonal `−q_2 = −2` per pair. ✓

3. **Klein-bottle population ratio Q = q_2/q_3 = 2/3 partition**:
   the Klein-bottle population ratio `Q = q_2/q_3` distributes
   substrate modes between two classes. Pair-wise coupling
   inherits weight `q_2` (the smaller-class size) per pair,
   matching the off-diagonal `−q_2`.

   This reading is structurally suggestive but the derivation
   chain through "population ratio → pair-wise coupling weight" is
   not explicit.

The justification (2) — pair-wise `Q_{AB} mod 2` conservation as
the substrate origin of off-diagonal `−q_2` — is the most direct.
The framework's pair-wise apparatus from PR #152 provides the
conservation; iteration 12 proposes that the substrate cost
function on lepton amplitude space inherits the conservation's
weight `q_2` as the pair-wise attractive coupling.

This is plausible but not airtight. Assumption Z (specifically the
inheritance from pair-wise Q-conservation to amplitude cost
coefficient) remains an explicit structural assumption pending
verification.

---

## Combining the ingredients

Given Assumptions U and Z:

    M  =  (diagonal contribution from i)  +  (off-diagonal from ii)
        =  q_3 I  +  (−q_2 J_{off-diag})
        =  q_3 I  −  q_2 (J − I)  +  ε I

Wait — there's an ambiguity in whether `J` (all-ones matrix) or `J − I`
(adjacency matrix of complete graph K_3) is the right off-diagonal
contribution.

The Koide-matching matrix uses `J` (all-ones) with off-diagonal
`−q_2`. If the substrate gives `J − I` instead (no self-coupling
contribution from the pair structure), the matrix becomes
`q_3 I − q_2 (J − I) = (q_3 + q_2) I − q_2 J = 5 I − 2 J`.

Computing the Koide value for this alternative `M' = 5 I − 2 J`:

    M' v · v  =  5 |v|² − 2 (Σv)²  =  0
    |v|² / (Σv)²  =  2/5
    K' = 2/5 = 0.4

This does not match Koide `K = 2/3`. So the off-diagonal must use
`J`, not `J − I`. This means the substrate's "pair-wise coupling"
must contribute to the *diagonal* as well as the off-diagonal in
the specific combination `q_3 I − q_2 J = (q_3 − q_2) I + q_2 (I − J)`.

Rewriting: `M = (q_3 − q_2) I − q_2 (J − I) = I − 2 (J − I)`
(for `(q_2, q_3) = (2, 3)`).

This is `1` on diagonal and `−2` off-diagonal. The structural
interpretation is: each generation contributes `q_3 − q_2 = 1` to
its own diagonal *after* pair-wise contributions are accounted
for. The pair-wise weight `−q_2 = −2` then appears on off-diagonal
(and `+q_2 = +2` is added to diagonal by the `+q_2 I` correction).

**This is a structurally cleaner reading**: the bare diagonal is
`q_3 − q_2 = 1` (the "irreducible" self-energy after removing
pair-wise structure), and the pair-wise coupling adds `+q_2`
diagonal and `−q_2` off-diagonal in matched amounts.

Substrate-arithmetic: `q_3 − q_2 = q_3 − q_2 = 3 − 2 = 1`. With
`q_3 = q_2 + 1` (the consecutive-integer relation), this `1` is
substrate-natural.

### Revised assumption

The cleaner reading replaces Assumption U:

**Assumption U' (irreducible self-energy)**: the substrate's
quadratic form on lepton amplitude space has diagonal contribution
`q_3 − q_2 = 1` per generation (irreducible self-energy independent
of pairing) plus pair-wise contribution `+q_2 = 2` per pair (added
to diagonal) and `−q_2 = −2` per pair (off-diagonal). Total
diagonal: `(q_3 − q_2) + 2 q_2 = q_3 + q_2 = ... wait.

Let me re-derive. With pair-wise contributions added to BOTH
endpoints of each pair:

- Generation A is part of pairs (A,B) and (A,C). Two pairs.
- Each pair contributes `+q_2` to generation A's diagonal.
- Total pair contribution to A's diagonal: `2 q_2 = 4`.
- Plus irreducible self-energy `q_3 − q_2 = 1`.
- Total diagonal: `5`. But M's diagonal is `q_3 = 3`.

Doesn't match. The substrate-natural pair-wise contribution to
diagonal isn't symmetric across pair endpoints.

Alternative: pair-wise contributes `+q_2/2 = +1` to each endpoint:
- Total pair contribution to A's diagonal: `2 × q_2/2 = 2`.
- Plus irreducible self-energy `q_3 − q_2 = 1`.
- Total diagonal: `3 = q_3`. ✓

This works, but it requires "splitting" the pair-wise weight `q_2`
equally between the two pair endpoints. Substrate-naturally: each
endpoint takes `q_2/2 = 1` from each pair.

**Revised Assumption U''**: each pair contributes `q_2` *total*
coupling structure, with `q_2/2` going to each of the two
endpoint diagonals and `−q_2` going to the off-diagonal.

With `q_2 = 2`, `q_2/2 = 1`. Half-integer weights aren't typical
substrate primitives (the framework prefers integer
combinatorics). This casts doubt on the "split" reading.

### The actual substrate derivation needed

The above explorations show that combining diagonal and off-diagonal
contributions from substrate primitives is not straightforward. The
matrix `M = q_3 I − q_2 J` has a *specific* combination that the
substrate must produce; iteration 12 has not derived this combination
cleanly.

Several substrate-natural sub-readings (U, U', U'', Z, and variants)
each produce *some* features of M but not the full matrix.

**Honest status**: ingredient derivation is *not* complete in iteration
12. The structural assumptions U and Z proposed at the iteration
start do not combine in a substrate-natural way to give M without
additional ad-hoc choices. The closure work remains open.

---

## Honest disposition

Iteration 12 sets out to derive the two ingredients (i) and (ii)
from substrate primitives and finds that:

- **Ingredient (i)** can be derived as `q_3 = k_lepton / n_gens =
  q_3² / q_3`, but only under Assumption U (uniform distribution
  across generations). Assumption U is substrate-aligned but not
  independently derived.

- **Ingredient (ii)** can be derived as `−q_2` from Klein-antipodal
  Z_2 of order `q_2`, but only under Assumption Z (Z_2-order-as-
  coupling). Assumption Z is plausible via pair-wise `Q_{AB} mod 2`
  conservation but not independently derived.

- **Combining ingredients** into the specific matrix `M = q_3 I −
  q_2 J` requires additional substrate-arithmetic that doesn't
  cleanly split into "diagonal self-energy" plus "off-diagonal
  pair coupling" without half-integer or otherwise non-natural
  weights.

**Net result**: iteration 12 does not close the Koide gap. It
identifies that the residual ingredients (i) and (ii) from
iteration 11 are *not independently substrate-derivable* in
isolation. The matrix `M = q_3 I − q_2 J` must be derived *as
a whole* substrate-natural object, not by separately deriving
its diagonal and off-diagonal coefficients.

This is informative: it rules out the "ingredient-by-ingredient"
derivation path for the matrix form and points the substrate-
derivation work back to the matrix as a unified substrate-natural
quadratic form.

---

## What this iteration establishes

- The two ingredients (i) and (ii) from iteration 11 cannot be
  independently substrate-derived without additional structural
  assumptions (U and Z) that are themselves not airtight.
- The matrix `M = q_3 I − q_2 J` does not split cleanly into
  separable substrate-derivable diagonal and off-diagonal
  contributions.
- Substrate-derivation of `M` likely requires treating it as a
  unified object (e.g., the substrate's natural quadratic form
  with substrate-primitive trace `q_3` and determinant `−q_3³`),
  not as a sum of separately-derived parts.

This refines the iteration-11 framing: the residual gap is not
"derive (i) and (ii) separately" but "derive `M` as a unified
substrate-natural quadratic form."

---

## Audit

| Component | Status |
|---|---|
| Iteration 11 framing of two-ingredient gap | **Refined** in this iteration |
| Ingredient (i) via `k_lepton / n_gens` arithmetic | Derivable *modulo Assumption U* |
| Ingredient (ii) via Klein-antipodal Z_2 order | Derivable *modulo Assumption Z* |
| Combining (i) and (ii) into specific matrix M | **Does not work cleanly** with substrate-natural weights |
| Substrate derivation of M as unified object | **Open** — the actual remaining work |
| Floor → Survives upgrade | Still pending |

The iteration's contribution is the *negative* finding that the
ingredient-by-ingredient derivation path doesn't work cleanly. The
matrix M must be derived unitarily.

---

## Falsifiers

- **A clean substrate-derivation of M as a unified object is
  produced**: closes the Koide gap. Most plausible path:
  identify the substrate-natural quadratic form with specific
  substrate-primitive invariants (trace `q_3`, determinant
  `−q_3³`, signature `(2, 1)`) and show these are forced.
- **Assumption U or Z is shown to be substrate-natural via a
  derivation not considered here**: would reopen the ingredient-
  by-ingredient path.
- **The matrix M is shown to require non-substrate-primitive
  weights (e.g., half-integer)**: would refute the ingredient-by-
  ingredient framing and force a different derivation chain.

---

## Recommended next iteration

Iteration 13 should:

- Identify the substrate-natural quadratic form on three-generation
  amplitude space *as a unified object*. The substrate-primitive
  invariants of M (trace `q_3`, determinant `−q_3³`, Lorentzian
  `(2, 1)` signature) suggest M is the *unique* substrate-natural
  symmetric matrix with these invariants and `S_3`-equivariance.
- If uniqueness can be substrate-derived, M is forced and the
  Koide gap closes.
- If multiple substrate-natural matrices satisfy the constraints,
  selection question (selection thread, `substrate_prediction_selection.md`)
  re-enters.

---

## Cross-links

- `koide_form_substrate_iteration_11.md` — iteration 11's two-
  ingredient framing, refined here.
- `mass_sector_closure.md` — `k_lepton = q_3²`, `k_quark = q_2³`,
  cube identity, sector closures.
- `generation_mechanism.md` (D34) — three generations,
  `{locked, unlocked}²` structure.
- `klein_bottle.md` (D19) — Klein-antipodal `τ`, `Q = q_2/q_3`.
- `epr_bell_assembly_theorem.md` (#152) — pair-wise `Q_{AB} mod 2`
  conservation.
- `substrate_prediction_selection.md` — selection thread (becomes
  relevant if uniqueness fails).
- `discrete_extension_principle.md` (PR #191) — methodology.

---

## One-line summary

Iteration 12 tests whether the two residual ingredients from
iteration 11 — (i) diagonal weight `q_3` per generation in
`M = q_3 I − q_2 J`, and (ii) off-diagonal weight `−q_2` per pair
— can be independently substrate-derived; ingredient (i) is
derivable as `q_3 = k_lepton / n_gens = q_3² / q_3` *modulo
Assumption U* (uniform distribution of `k_lepton` modes across
generations, plausible from permutation symmetry / information
minimization / hierarchy decoupling but not independently
substrate-derived), and ingredient (ii) is derivable from
Klein-antipodal Z_2 of order `q_2` *modulo Assumption Z* (Z_2-order
inherits as pair-wise coupling weight, plausible via pair-wise
`Q_{AB} mod 2` conservation from `epr_bell_assembly_theorem.md`
PR #152 but not independently substrate-derived); however,
combining the two ingredients into the specific matrix `M = q_3 I
− q_2 J` does *not* work cleanly with substrate-natural weights —
the diagonal `q_3 = 3` and off-diagonal `−q_2 = −2` do not split
into separable "self-energy" and "pair-coupling" contributions
without half-integer or otherwise non-substrate-natural choices;
the iteration's substantive finding is *negative*: the
ingredient-by-ingredient derivation path doesn't work, so the
matrix M must be derived *as a unified substrate-natural
quadratic form* rather than as a sum of separately-derived parts;
this refines the iteration-11 framing of the residual gap and
identifies iteration 13's target as deriving M as a unified
object via its substrate-primitive invariants (trace `q_3`,
determinant `−q_3³`, Lorentzian `(2, 1)` signature, `S_3`-equivariance);
Koide closure remains pending.
