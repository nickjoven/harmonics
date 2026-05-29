# Dicke apparatus theorem — substrate-internal computation of Pauli matrix elements on Dicke states

## Status

**Theorem-quality result rigorizing the T1a Dicke extension
(`w_state_from_substrate.md`, #187).** The observation that
"substrate's Dicke `(N, k)` primitive + recursive Schmidt +
conditional pair-wise apparatus reproduces W's correlations
numerically" is upgraded to a theorem: *all Pauli matrix elements
on Dicke states are substrate-computable* via a finite recursion
that terminates in the foundational layer's single-mode Pauli
entries.

**Discipline.** Same audit shape as `bell_bounds_from_substrate.md`
(#188) — explicit accounting of what's load-bearing from the
framework's foundational layer vs. what the theorem proves
substrate-internally above that layer. No new substrate primitive.

**Class: foundational consolidation (Class 3, theorem-quality
articulation).** Rigorizes T1a's structural-scaling claim.

---

## Theorem statement

**Theorem (Dicke apparatus).** For every `N ≥ 1`, every pair `0 ≤
k_1, k_2 ≤ N`, and every Pauli string `P = σ_{α_1} ⊗ σ_{α_2} ⊗ ⋯
⊗ σ_{α_N}` with `α_i ∈ {I, x, y, z}`, the matrix element
`⟨D(N, k_1) | P | D(N, k_2)⟩` is computable substrate-internally
via:

1. The **recursive Schmidt structure**
   ```
   D(N, k)  =  √(k/N) · D(N−1, k−1) ⊗ |1⟩  +  √((N−k)/N) · D(N−1, k) ⊗ |0⟩,
   ```
   derived from substrate combinatorics (`w_state_from_substrate.md`,
   §"Recursive Schmidt structure"; numerically verified for
   `D(3,1), D(4,1), D(4,2), D(4,3), D(5,2)`).
2. **Bilinearity** of expectation value (Hilbert space inner
   product, foundational layer).
3. **Pauli action on the projected mode**: the single-mode entries
   `⟨a | σ_α | b⟩` for `a, b ∈ {0, 1}` (foundational layer:
   complex amplitudes on `ℂ²` + Pauli matrices as SU(2)
   generators).

The recursion terminates at the base case `N = 1` (single-mode
Pauli matrix entries from the foundational layer).

**Substrate data per matrix element**: `O(N)` recursion depth;
`O(1)` substrate data per level (the integer `(N, k_1, k_2)` and
combinatorial weights `k_i/N, (N−k_i)/N, √(k_i(N−k_j))/N`); the
substrate apparatus accumulates `O(N²)` Dicke index pairs across
the recursion tree, all derived from token-counting on the
symmetric distribution.

---

## Preliminaries

### Foundational layer (load-bearing; substrate-derived in prior docs)

The theorem is substrate-internal **above the foundational layer**
articulated in `bell_bounds_from_substrate.md` (#188) Audit
section:

1. Complex amplitude field `ℂ` from Klein bottle's antiperiodic
   direction (`complex_amplitude_uniqueness.md`).
2. Pauli matrices `σ_x, σ_y, σ_z` as SU(2) Hermitian generators
   on `ℂ²`.
3. Pauli algebra structure constants (`σ_x σ_z = −i σ_y` etc.) —
   not directly used in this theorem but available for downstream
   composition.
4. Hilbert space inner product `⟨ψ | O | ψ⟩` from complex
   amplitudes + normalization.
5. Q mod 2 conservation in arbitrary basis (inviolable #1) — gives
   Dicke states their `Q = k mod 2` characterization.
6. Single-mode Born rule `P(±) = cos²/sin²((θ − θ_basin)/2)` from
   saddle-node (`born_rule.md`).

### Dicke primitive (from #187)

A Dicke state `D(N, k)` is the equal superposition of all `N`-bit
strings with exactly `k` ones:

    D(N, k)  =  C(N, k)^{−1/2} · Σ_{|s|=k} |s⟩.

Substrate-native characterization: integer pair `(N, k)` with
permutation-symmetric distribution of `k` excitation tokens among
`N` modes. `O(1)` substrate data per state.

Special cases recovered by the foundational layer:
- `D(N, 0) = |0...0⟩`, `D(N, N) = |1...1⟩` — substrate-trivial.
- `D(2, 1) = |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2` — substrate-pair-wise; the
  pair-wise EPR/Bell apparatus from #152 handles its Pauli
  expectations.

### Conditional pair-wise apparatus (from #187)

Given the Schmidt decomposition on mode `N`, the conditional
states on modes `1, …, N−1` are themselves combinations of Dicke
states `D(N−1, k')` with various `k'`. The substrate apparatus
composes these recursively.

---

## Proof

By strong induction on `N`.

### Base case `N = 1`

`D(1, 0) = |0⟩`, `D(1, 1) = |1⟩`. The four matrix elements
`⟨a | σ_α | b⟩` for `a, b ∈ {0, 1}` and `α ∈ {I, x, y, z}` are
single-mode Pauli matrix entries:

| `α` | `⟨0|σ_α|0⟩` | `⟨0|σ_α|1⟩` | `⟨1|σ_α|0⟩` | `⟨1|σ_α|1⟩` |
|---|---|---|---|---|
| `I` | 1 | 0 | 0 | 1 |
| `z` | 1 | 0 | 0 | −1 |
| `x` | 0 | 1 | 1 | 0 |
| `y` | 0 | −i | i | 0 |

These are the standard Pauli matrix entries, given by the
foundational layer (SU(2) generators on `ℂ²`). Base case
established.

### Inductive step

Assume the theorem holds for all `N' < N`. We show it for `N`.

Let `P = P_{1..N−1} ⊗ σ_{α_N}` where `P_{1..N−1}` is a Pauli string
on modes `1, …, N−1` and `α_N ∈ {I, x, y, z}`.

Apply the Schmidt decomposition to both `|D(N, k_1)⟩` and
`|D(N, k_2)⟩`:

    |D(N, k)⟩  =  √(k/N) |D(N−1, k−1)⟩ ⊗ |1⟩  +  √((N−k)/N) |D(N−1, k)⟩ ⊗ |0⟩.

Expand the matrix element bilinearly:

    ⟨D(N, k_1) | P_{1..N−1} ⊗ σ_{α_N} | D(N, k_2)⟩
        =  Σ_{a, b ∈ {0,1}} c^{(k_1)}_a · c^{(k_2)}_b
              · ⟨D(N−1, k_1 − a)| P_{1..N−1} |D(N−1, k_2 − b)⟩
              · ⟨a | σ_{α_N} | b⟩

where the substrate-combinatorial weights are:

    c^{(k)}_0  =  √((N−k)/N),     c^{(k)}_1  =  √(k/N).

(These satisfy `(c^{(k)}_0)² + (c^{(k)}_1)² = 1` — substrate
normalization from token-counting.)

The sum has at most four non-zero terms (corresponding to
`(a, b) ∈ {(0,0), (0,1), (1,0), (1,1)}`), and the non-zero pattern
depends on `α_N`:

#### Case `α_N = I` (identity on last mode)

`⟨a | I | b⟩ = δ_{a, b}`. Non-zero terms `(a, b) = (0, 0)` and
`(1, 1)`:

    ⟨D(N, k_1) | P_{1..N−1} ⊗ I | D(N, k_2)⟩
        =  √(k_1 k_2)/N · ⟨D(N−1, k_1−1) | P_{1..N−1} | D(N−1, k_2−1)⟩
         + √((N−k_1)(N−k_2))/N · ⟨D(N−1, k_1) | P_{1..N−1} | D(N−1, k_2)⟩.

By inductive hypothesis (`N' = N − 1`), both Dicke matrix elements
on the right are substrate-computable. Substrate-combinatorial
weights `√(k_1 k_2)/N` and `√((N−k_1)(N−k_2))/N` follow from
token-counting. ✓

#### Case `α_N = z`

`⟨a | σ_z | b⟩ = (−1)^a · δ_{a, b}`. Same diagonal structure as
identity, with sign flip on the `(1, 1)` branch:

    ⟨D(N, k_1) | P_{1..N−1} ⊗ σ_z | D(N, k_2)⟩
        =  −√(k_1 k_2)/N · ⟨D(N−1, k_1−1) | P_{1..N−1} | D(N−1, k_2−1)⟩
         + √((N−k_1)(N−k_2))/N · ⟨D(N−1, k_1) | P_{1..N−1} | D(N−1, k_2)⟩.

Substrate-computable by inductive hypothesis. ✓

#### Case `α_N = x`

`⟨a | σ_x | b⟩ = δ_{a, 1−b}` (flips `|0⟩ ↔ |1⟩`). Non-zero terms
`(a, b) = (0, 1)` and `(1, 0)` — *cross-terms*:

    ⟨D(N, k_1) | P_{1..N−1} ⊗ σ_x | D(N, k_2)⟩
        =  √((N−k_1) k_2)/N · ⟨D(N−1, k_1) | P_{1..N−1} | D(N−1, k_2−1)⟩
         + √(k_1 (N−k_2))/N · ⟨D(N−1, k_1−1) | P_{1..N−1} | D(N−1, k_2)⟩.

The cross-terms involve **off-diagonal Dicke matrix elements**
(different `k` on left vs. right). These are *exactly* the matrix
elements the inductive hypothesis covers (the theorem statement
includes general `k_1, k_2`, not just diagonal `k_1 = k_2`).
Substrate-computable. ✓

#### Case `α_N = y`

`⟨a | σ_y | b⟩ = i (−1)^b · δ_{a, 1−b}`. Same cross-term structure
as `σ_x`, with imaginary phases:

    ⟨D(N, k_1) | P_{1..N−1} ⊗ σ_y | D(N, k_2)⟩
        =  −i √((N−k_1) k_2)/N · ⟨D(N−1, k_1) | P_{1..N−1} | D(N−1, k_2−1)⟩
         + i √(k_1 (N−k_2))/N · ⟨D(N−1, k_1−1) | P_{1..N−1} | D(N−1, k_2)⟩.

Substrate-computable by inductive hypothesis. ✓

### Termination

Each recursive call reduces `N` by 1. The recursion terminates at
`N = 1` (base case). Substrate data accumulated across recursion
depth: at each level, the Pauli string `P_{1..N−1}` is one shorter;
the index pairs `(k_1, k_2)` may include both `k_i` and `k_i ± 1`.
Total recursion tree has depth `N` and at most `2N + 1` distinct
Dicke index pairs at the deepest level — polynomial substrate
data.

### Q.E.D.

---

## Numerical verification

The recursive decomposition was verified numerically for:

| State | Pauli string | Direct QM | Substrate recursion | Match |
|---|---|---|---|---|
| `D(3, 1) = W` | `σ_z ⊗ σ_x ⊗ σ_z` | `0.0000` | `0.0000` | ✓ |
| `D(3, 1) = W` | `σ_x ⊗ σ_x ⊗ σ_x` | `0.0000` | `0.0000` | ✓ |
| `D(3, 1) = W` | `σ_x ⊗ σ_z ⊗ σ_x` | `+0.6667` | `+0.6667` | ✓ |
| `D(4, 2)` | `σ_z ⊗ σ_z ⊗ σ_z ⊗ σ_z` | `+1.0000` | `+1.0000` | ✓ |
| `D(4, 2)` | `σ_x ⊗ σ_x ⊗ σ_x ⊗ σ_x` | `+1.0000` | `+1.0000` | ✓ |
| `D(4, 2)` | `σ_x ⊗ σ_y ⊗ σ_y ⊗ σ_x` | `+0.3333` | `+0.3333` | ✓ |

Both Z-projection clean cases and X/Y-projection cross-term cases
match QM exactly. (Errors `< 10⁻¹²`.)

---

## Corollaries

### Corollary 1 — Diagonal Pauli expectations

For any Dicke state `D(N, k)` and any Pauli string `P`, the
expectation value `⟨D(N, k)| P | D(N, k)⟩` is substrate-computable.
(Special case `k_1 = k_2 = k` of the theorem.)

This is the result invoked in `w_state_from_substrate.md` (#187)
for W's correlations (`⟨XXZ⟩_W = +2/3`, `⟨XXX⟩_W = 0`, `⟨XYY⟩_W
= 0`). The substrate-internal derivation is now rigorous.

### Corollary 2 — General symmetric subspace

For any state in the symmetric subspace `|sym⟩ = Σ_k c_k |D(N, k)⟩`
(arbitrary complex coefficients `c_k`), substrate computes

    ⟨sym| P |sym⟩  =  Σ_{k_1, k_2} c_{k_1}^* c_{k_2} · ⟨D(N, k_1)| P |D(N, k_2)⟩,

with each Dicke matrix element substrate-computable by the
theorem. The full symmetric subspace of `(ℂ²)^{⊗N}` (dimension
`N + 1`) is therefore substrate-handled.

### Corollary 3 — Polynomial substrate scaling

Each Pauli string expectation requires `O(N)` recursion depth and
`O(N²)` total intermediate Dicke matrix elements. Substrate data
per element: `O(1)` (combinatorial weights + Pauli single-mode
entries). Total substrate cost per Pauli expectation: `O(N²)` —
strictly polynomial.

Compare:
- Naive tensor-product computation: `O(2^N)` Hilbert space
  components.
- Pauli stabilizer apparatus (#184 GHZ doc): `O(N)` per stabilizer
  generator.
- Dicke apparatus (this theorem): `O(N²)` per Pauli expectation
  via recursion, `O(1)` per state for the `(N, k)` characterization.

Substrate's Dicke apparatus is **more compact than tensor products
by exponential factor**, and slightly less compact than Pauli
stabilizer apparatus (which doesn't apply to Dicke states because
they're non-stabilizer per #187).

### Corollary 4 — Symmetric subspace closure

The substrate's Dicke apparatus is *closed* under:
- Conditional projection on any single mode (Schmidt recursion).
- Linear combinations of Dicke states (Corollary 2).
- Pauli expectation evaluation (the theorem).

Not closed under: arbitrary local unitaries (which take the
symmetric subspace outside itself — see #187 boundary mapping for
non-symmetric non-stabilizer states).

---

## Scope and audit

### What this theorem establishes

- Substrate-internal computation of *all* Pauli matrix elements
  `⟨D(N, k_1) | P | D(N, k_2)⟩` for arbitrary `N, k_1, k_2`, Pauli
  string `P`.
- Substrate-internal computation of arbitrary symmetric-subspace
  state Pauli expectations (Corollary 2).
- Polynomial substrate scaling: `O(N²)` per matrix element,
  `O(1)` per Dicke state characterization.

### What this theorem does **not** establish

- **Non-symmetric multi-mode states.** Outside the substrate's
  natural reach per #187 boundary mapping; this theorem doesn't
  push that boundary.
- **Non-Pauli observables.** The theorem covers Pauli strings
  only. General Hermitian observables decompose into Pauli sums
  (foundational layer), so this is not a serious restriction but
  it's a scope limit of this theorem statement.
- **Independent derivation of foundational layer.** Pauli matrices,
  Hilbert space inner product, and complex amplitude structure
  are inherited from prior docs (`complex_amplitude_uniqueness.md`,
  `born_rule.md`, etc.) — see Audit table below.

### Audit: load-bearing components

| Component | Origin | Substrate-derived? |
|---|---|---|
| Pauli matrix entries `⟨a|σ_α|b⟩` | Standard SU(2) on `ℂ²` | Yes via foundational (1)+(2) |
| Schmidt coefficients `√(k/N), √((N−k)/N)` | Token-counting on symmetric distribution | **Substrate-derived in #187, used here** |
| Cross-term weights `√(k(N−k))/N` | Geometric mean of branch weights | **Substrate-derived** |
| Bilinearity of expectation | Hilbert space structure | Foundational (4) |
| Inner products `⟨0\|1⟩ = 0`, etc. | Orthogonality of computational basis | Foundational (4) |
| Recursive Schmidt structure | Substrate combinatorics on `(N, k)` | **Substrate-derived in #187** |
| Termination at `N = 1` base case | Foundational single-mode Pauli entries | Foundational (1)+(2) |
| Induction principle | Standard mathematical logic | Standard math |

**No smuggled QM-postulate.** All apparatus traces back to either
foundational layer (substrate-derived in prior docs) or substrate
combinatorics (substrate-derived in #187). The theorem itself is a
strong-induction argument over substrate-combinatorial
decomposition.

### Comparison to D3 (Bell bounds doc, #188)

D3 derived Bell-style bounds substrate-internally above the
foundational layer for *pair-wise stabilizer* states (singlet) and
*GHZ-type stabilizer* states (3-mode stabilizer).

This doc (D1) derives Pauli matrix elements substrate-internally
above the foundational layer for the *full Dicke family* (and by
Corollary 2, the symmetric subspace of `(ℂ²)^{⊗N}` for any `N`).

D3 + D1 together: the substrate's multipartite QM apparatus is
substrate-internal (above foundational layer) for both natural
classes — Pauli stabilizer states and Dicke states — and their
tensor products.

---

## Falsifiers

- **A Pauli matrix element `⟨D(N, k_1)|P|D(N, k_2)⟩` that the
  recursion computes incorrectly.** Would invalidate either the
  recursive Schmidt decomposition or the case-by-case Pauli
  matrix entries.
- **A symmetric subspace state whose Pauli expectations the
  substrate apparatus cannot compute via Corollary 2.** Would
  contradict the theorem.
- **A counterexample showing the substrate's `(N, k)` data is
  insufficient to specify a Dicke state.** The substrate
  characterization needs to uniquely identify each `D(N, k)`; if
  two distinct Dicke states share the same `(N, k)`, the apparatus
  underdetermines (this is excluded by the standard combinatorial
  definition, but worth flagging).
- **A more efficient substrate computation of Pauli expectations
  than `O(N²)` per element.** Would not invalidate the theorem
  but would tighten Corollary 3's scaling claim.

---

## Cross-links

- `w_state_from_substrate.md` (#187) — T1a Dicke extension that
  this theorem rigorizes; the recursive Schmidt structure is from
  #187, here applied as the proof's induction step.
- `bell_bounds_from_substrate.md` (#188) — D3 substitution-scope
  closure; the foundational layer audit (1)–(6) is shared; this
  theorem deepens the same discipline at the Dicke-state level.
- `ghz_from_substrate.md` (#184) — GHZ stabilizer apparatus; the
  Pauli stabilizer machinery is complementary to the Dicke
  apparatus (different natural classes, both substrate-internal).
- `epr_bell_assembly_theorem.md` (#152) — pair-wise EPR/Bell
  theorem; the base case `D(2, 1) = |Ψ⁺⟩` and the substrate's
  pair-wise apparatus give the `N = 2` recursion step.
- `complex_amplitude_uniqueness.md` — foundational complex amplitude
  field `ℂ` from Klein bottle topology; (1) in the audit.
- `born_rule.md`, `a1_from_saddle_node.md` — foundational
  single-mode Born rule from saddle-node parabola; (6) in the
  audit.
- `q_mod2_conservation_theorem.md`, `substrate_determinism.md`
  inviolable #1 — Q mod 2 conservation; consistent with the
  theorem's `Q = k mod 2` reading of Dicke states.
- `canonical_glossary.md` Section 2 — Dicke primitive entry
  (added in #187 glossary update).
- `framework_status.md` "Survives" — W states T1a row;
  this theorem should be added as a row noting the
  theorem-quality articulation.

---

## Why this matters

T1a (#187) established the substrate's Dicke extension via
observation + numerical verification. D3 (#188) tightened the
substitution scope at the pair-wise level via audit-disciplined
substrate-internal derivation of Bell bounds. D1 (this theorem)
extends the audit discipline to the Dicke extension itself:
the substrate's apparatus for Dicke matrix elements is now
**theorem-quality**, not just observational.

Together, #184 + #187 + #188 + this theorem establish that the
substrate's multipartite QM apparatus is substrate-internal above
the foundational complex-amplitude / Pauli / Q-conservation layer
for:
- Pauli stabilizer states (GHZ, cluster, codes; #184 + #188).
- Dicke states (W, superradiance, symmetric collective; #187 + this theorem).
- Pair-wise pure states (Bell singlet, triplet, etc.; #152 +
  #188).
- The symmetric subspace of `(ℂ²)^{⊗N}` for any `N` (Corollary 2).
- Tensor products of all the above.

The substrate's reach class — `(Pauli stabilizer) ∪ (Dicke) ∪
(continuous-θ single-mode) ∪ (tensor products thereof)` — is now
**theorem-supported at every node**, ready for D2 formalization
as a named substrate-natural multipartite class.

The discriminator-clause discipline is satisfied: substrate
event-log sufficiency is proven (not assumed) for every class in
the substrate's reach, with the foundational layer's contribution
made explicit at every step. The boundary at non-stabilizer
non-Dicke states (verified in #187) remains the substrate's reach
edge.

---

## One-line summary

For every `N ≥ 1`, every pair `0 ≤ k_1, k_2 ≤ N`, and every Pauli
string `P = σ_{α_1} ⊗ ⋯ ⊗ σ_{α_N}`, the matrix element
`⟨D(N, k_1) | P | D(N, k_2)⟩` is substrate-internally computable
via the recursive Schmidt structure `D(N, k) = √(k/N) D(N−1, k−1)
⊗ |1⟩ + √((N−k)/N) D(N−1, k) ⊗ |0⟩` (substrate-derived in #187 from
token-counting on symmetric distribution), bilinearity, and
case-by-case Pauli matrix entries `⟨a | σ_α | b⟩` from the
foundational layer (`complex_amplitude_uniqueness.md` +
`born_rule.md` + standard SU(2) on `ℂ²`); the four cases
(`α_N ∈ {I, z, x, y}`) reduce via strong induction on `N` to
substrate-computable matrix elements on `D(N−1, *)`, terminating at
the foundational single-mode Pauli base case; numerical verification
at `N = 3, 4` confirms the recursive decomposition matches QM
exactly (errors `< 10⁻¹²`); corollaries: all symmetric-subspace
state Pauli expectations substrate-computable, `O(N²)` substrate
cost per Pauli string, substrate apparatus closed under conditional
projection / linear combinations / Pauli expectation evaluation —
upgrading T1a (#187) from observation to theorem and completing the
audit-disciplined substrate-internal derivation chain for the Dicke
half of the substrate's natural multipartite reach.
