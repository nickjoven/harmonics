# W states from substrate — narrowing the apparatus, then extending it

## Status

**T1a worked example, with a two-sided finding: narrowing then
extension.** Tests whether the substrate's `Q ∈ ℤ/2ℤ`-invariant
apparatus from `ghz_from_substrate.md` (PR #184) generalizes
naturally to the W state — the canonical 3-mode entangled state
LOCC-inequivalent to GHZ.

**Initial narrowing.** The substrate's bare Pauli-Z₂ Q-invariant
underdetermines W. W lives in the 4-dimensional `σ_z⊗σ_z⊗σ_z = −1`
subspace; the single triple-parity invariant captures W's Z-basis
behavior (`⟨ZZZ⟩ = −1`) but doesn't single W out within that
subspace. W is *not* a stabilizer state — only one of three Pauli
stabilizers needed for a 3-qubit pure state.

**Extension (the substantive finding).** With a single new
substrate primitive — *Dicke characterization* `(N, k)`: k
excitations symmetrically distributed among N modes — the substrate
apparatus extends naturally to W and the full Dicke family. The
extension composes with the existing pair-wise EPR/Bell apparatus
through a recursive Schmidt-like decomposition:

    D(N, k) = √(k/N) · D(N−1, k−1) ⊗ |1⟩ + √((N−k)/N) · D(N−1, k) ⊗ |0⟩.

The weights `(k/N, (N−k)/N)` come from substrate combinatorics
(symmetric distribution of the k excitation tokens), *not* from QM
substitution. Numerically verified for `D(3,1) = W`, `D(4,1) = W4`,
`D(4,2)`, `D(4,3)`, `D(5,2)`: the substrate-native recursive
construction reproduces each state exactly (error `~10⁻¹⁶`); the
substrate's pair-wise apparatus on the AB cut, conditioned on
C-mode outcome, reproduces W's full correlation structure
(`⟨XXZ⟩ = +2/3`, `⟨XXX⟩ = 0`, `⟨XYY⟩ = 0`) independently of
substitution.

**Refined reach.** The substrate's natural apparatus, with the
Dicke `(N, k)` primitive added, covers:

- **Continuous-θ single-mode states** (full Bloch sphere per mode
  via basin geometry — includes magic states like `|T⟩`);
- **Pair-wise pure states** (Bell states and generalizations; via
  EPR/Bell apparatus with substitution — `epr_bell_assembly_theorem.md`);
- **Pauli stabilizer states** (GHZ, cluster, error-correcting codes;
  Gottesman–Knill regime; substrate data `O(N)` via stabilizer
  generators);
- **Dicke states** (W, `D(N, k)` for any `k`; superradiance,
  symmetric photon states, collective quantum optics; substrate
  data `O(1)` via the `(N, k)` primitive);
- **Tensor products** of the above (e.g., `|T⟩ ⊗ |Φ⁺⟩` is
  substrate-handled as `(single-mode at θ_T) ⊗ (Bell)`).

Genuinely outside the reach (numerically verified — see batch-2
boundary tests below):

- *Coherent superpositions across substrate-natural classes* (e.g.,
  `(|GHZ⟩ + |W⟩)/√2` — zero Pauli stabilizers, not Dicke);
- *Generic non-symmetric non-stabilizer states* (e.g., asymmetric
  `(|001⟩ + 2|010⟩ + |100⟩)/√6` — one Pauli stabilizer, not Dicke);
- *Phase-twisted symmetric states* (e.g., `(T⊗I⊗I)|W⟩` — one Pauli
  stabilizer, max Dicke overlap² `0.87` but not Dicke; continuous
  phase entangled with multi-mode topology);
- *Generic bond-dimension-≥2 MPS* not aligned with stabilizer/Dicke
  structure;
- *Haar-random pure states* (5/5 sampled: zero stabilizers, max
  Dicke overlap² `< 0.5`).

**Why this is a positive result, with honest scoping.** Most
physics-relevant multipartite entanglement falls within the
substrate's natural reach: codes, Bell states, GHZ, cluster states
(stabilizer); superradiance and symmetric collective states
(Dicke); single-mode magic states tensored into stabilizer/Dicke
substrate. The substrate's natural reach is *broader* than the
stabilizer-only Gottesman–Knill regime via the Dicke extension.

The substrate's reach is a **strict subset of
classically-tractable multipartite QM**: substrate covers
stabilizer ∪ Dicke ∪ continuous-single-mode-tensor-products, but
generic bond-dimension-2 MPS states (also classically tractable)
are outside the substrate apparatus. So the alignment is partial,
not exact — substrate captures the *discrete-symmetry-plus-
single-mode-continuous* subset of classically-tractable states.

What remains genuinely outside is the "magic-state-injected-
into-multi-mode-entanglement" regime where quantum-computational
advantage lives — and the boundary is now precisely identified
through batch-2 boundary tests.

No new substrate inviolable. The Dicke `(N, k)` primitive is an
extension of the apparatus, not a new substrate axiom; it
composes the existing Q-mod-2 conservation (`Q = k mod 2`),
pair-wise EPR/Bell apparatus, and the symmetric distribution
constraint into a substrate-native multi-mode characterization.

---

## QM correlations for W (verified numerically)

The W state:

    |W⟩  =  (|001⟩ + |010⟩ + |100⟩) / √3   =   D(3, 1).

Computed expectation values (numerically verified):

| Observable | `⟨W| O |W⟩` | Notes |
|---|---|---|
| `σ_z ⊗ σ_z ⊗ σ_z` | **−1** | Definite; W is a `Z_{ABC}` eigenstate |
| `σ_x ⊗ σ_x ⊗ σ_x` | **0** | No 3-mode X correlation |
| `σ_x ⊗ σ_y ⊗ σ_y` | 0 | |
| `σ_y ⊗ σ_x ⊗ σ_y` | 0 | |
| `σ_y ⊗ σ_y ⊗ σ_x` | 0 | |
| `σ_x ⊗ σ_x ⊗ σ_z` | **+2/3** | Mixed-basis: non-trivial |
| `σ_x ⊗ σ_z ⊗ σ_x` | +2/3 | |
| `σ_z ⊗ σ_x ⊗ σ_x` | +2/3 | |
| `σ_y ⊗ σ_y ⊗ σ_z` | +2/3 | |
| `σ_x ⊗ σ_z ⊗ σ_z` | 0 | |

The Mermin parameter (`M = ⟨XYY⟩ + ⟨YXY⟩ + ⟨YYX⟩ − ⟨XXX⟩`):

    M_W  =  0 + 0 + 0 − 0  =  0.        |M_W| = 0.

**W does *not* violate the Mermin inequality** `|M| ≤ 2`, despite
being a genuinely 3-mode entangled state. The Mermin inequality is
a test for GHZ-style correlations specifically; LOCC-inequivalent
states like W need different Bell-style inequalities (e.g.,
Cabello–Wootters) to detect their multi-mode entanglement.

For comparison, GHZ saturates `|M| = 4` (matching the QM bound).

---

## W's pair-wise reduced state

Tracing out the third mode:

    ρ_{AB}(W)  =  (1/3) |00⟩⟨00|  +  (2/3) |Ψ⁺⟩⟨Ψ⁺|

where `|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2`. Verified numerically (eigenvalues
`1/3, 2/3, 0, 0`). For comparison, GHZ's pair-wise marginal
`ρ_{AB}(GHZ) = (1/2)(|00⟩⟨00| + |11⟩⟨11|)` is a classical mixture
with no entanglement.

This is a foundational distinction: GHZ's multi-mode entanglement
vanishes upon tracing out *any* mode; W's persists in pair-wise
reduced states. Both are "genuinely 3-mode entangled" but in
different senses. The substrate apparatus must reflect this.

---

## Substrate's bare Q apparatus applied to W

For the substrate's `Q_{ABC} ∈ ℤ/2ℤ` invariant alone (no Dicke
extension yet):

- W has **definite** `Q_{ABC} = 1` (every basis state has parity 1).
- This correctly predicts `⟨ZZZ⟩ = −1`.
- This correctly predicts `⟨XXX⟩ = ⟨XYY⟩ = ⟨YXY⟩ = ⟨YYX⟩ = 0` by
  the standard substrate argument that X-Y-plane joint expectations
  vanish for definite Z-parity sectors.

The bare Q apparatus alone does *not* predict:
- Mixed-basis non-trivial correlations like `⟨XXZ⟩_W = +2/3`.
- W's specific position within the 4-dimensional `Z_{ABC} = −1`
  subspace.

To predict W's full correlation structure substrate-natively, the
apparatus needs the Dicke extension — developed in the next two
sections.

---

## The Dicke extension: substrate-natural primitive

### Definition

A **Dicke state** `D(N, k)` is the equal superposition of all
`N`-bit strings with exactly `k` ones:

    D(N, k)  =  (N choose k)^{-1/2} · Σ_{|s|=k} |s⟩.

Special cases: `D(N, 0) = |0...0⟩`, `D(N, N) = |1...1⟩`,
`D(2, 1) = |Ψ⁺⟩` (the symmetric Bell state), `D(3, 1) = W`.

### Substrate characterization

The substrate primitive: a `D(N, k)` state is specified by **two
integers** `(N, k)` and a permutation-symmetric distribution of `k`
"excitation tokens" among `N` modes. This is substrate-native
combinatorial data, `O(1)` per state regardless of `N`.

The Q-mod-2 invariant is recovered as `Q_{1...N} = k mod 2`. The
single-mode marginal probability of `|1⟩` is `k/N`. The
permutation-symmetry constraint is the substrate-native way of
saying "the k tokens are indistinguishable" — no per-mode label
needed.

### Recursive Schmidt structure (substrate-derived)

Project `D(N, k)` on a single mode (say the N-th) in the Z basis.
Substrate combinatorics give:

    D(N, k) = √(k/N) · D(N−1, k−1) ⊗ |1⟩  +  √((N−k)/N) · D(N−1, k) ⊗ |0⟩.

The weights `(k/N, (N−k)/N)` are the substrate-native combinatorial
weights: of the `(N choose k)` ways to place `k` tokens among `N`
modes, `(N−1 choose k−1)` have a token at mode N (probability
`k/N`) and `(N−1 choose k)` don't (probability `(N−k)/N`). The
conditional states are themselves Dicke states of one fewer mode —
the substrate primitive *closes* under conditioning.

This recursion is verified numerically for `D(3,1), D(4,1),
D(4,2), D(4,3), D(5,2)`: substrate-recursive construction
reproduces the QM state exactly (error `~10⁻¹⁶`).

### Reach

The Dicke `(N, k)` primitive gives the substrate `O(1)` data per
state for the entire Dicke family. For general permutation-symmetric
states on N modes (the `(N+1)`-dim symmetric subspace of
`(ℂ²)^{⊗N}`), discrete distributions over `k ∈ {0,…,N}` give `O(N)`
data — still polynomial.

The Dicke family covers:
- W states and their N-mode generalizations `D(N, 1)`.
- The "dual" `D(N, N−1)` (related by global `σ_x`).
- All `D(N, k)`: superradiance states (Dicke 1954), the relevant
  states for collective spontaneous emission in N-atom ensembles.
- Symmetric photon Fock states `|N, k⟩` with `k` photons in a
  symmetric mode and `N−k` in another.

For physics applications, the Dicke family is structurally important
in quantum optics, collective light–matter interactions, and
symmetric many-body systems. Adding the `(N, k)` primitive to the
substrate apparatus pulls these into reach.

---

## Substrate-independent derivation of W's correlations

The Dicke extension lets the substrate apparatus derive W's
correlations *independently* of QM substitution. The derivation:

### Step 1 — substrate writes W's Schmidt decomposition

By the recursive Dicke structure (substrate combinatorics):

    W = D(3, 1)
      = √(1/3) · D(2, 0) ⊗ |1⟩_C  +  √(2/3) · D(2, 1) ⊗ |0⟩_C
      = √(1/3) · |00⟩_{AB} ⊗ |1⟩_C  +  √(2/3) · |Ψ⁺⟩_{AB} ⊗ |0⟩_C.

The substrate-native objects in this decomposition:
- `(N = 2, k = 0)` Dicke `= |00⟩_{AB}` — trivial substrate object,
  Q_{AB} = 0.
- `(N = 2, k = 1)` Dicke `= |Ψ⁺⟩_{AB}` — the symmetric Bell state,
  Q_{AB} = 1, handled by the pair-wise EPR/Bell apparatus
  (`epr_bell_assembly_theorem.md`).
- Branch weights `(1/3, 2/3)` from Dicke combinatorics
  (one of three modes hosts the excitation; mode C does or
  doesn't).

No QM input. The decomposition is generated entirely by substrate
primitives.

### Step 2 — apply substrate apparatus to derive `⟨XXZ⟩_W`

For mixed-basis `⟨σ_x ⊗ σ_x ⊗ σ_z⟩_W`, the substrate apparatus:

- Projects on mode-C Z-eigenstates (substrate-native: σ_z on C is
  diagonal in the Schmidt basis).
- Each branch contributes: (branch weight) × (σ_z eigenvalue) ×
  (pair-wise ⟨XX⟩ on AB conditional state).
- Pair-wise substrate apparatus gives `⟨XX⟩ on |00⟩ = 0` (separable
  trivial), `⟨XX⟩ on |Ψ⁺⟩ = +1` (Bell-state X-correlation, derived
  in `epr_bell_assembly_theorem.md`).

Substrate-derived prediction:

    ⟨XXZ⟩_W  =  (2/3) · (+1) · (+1)  +  (1/3) · (−1) · (0)
             =  +2/3.

QM-direct: `⟨XXZ⟩_W = +2/3`. **Match.**

### Step 3 — apply substrate apparatus to derive `⟨XXX⟩_W`

For all-X measurement, project mode C on X eigenstates (substrate:
σ_x basin geometry on single mode). Coherent decomposition:

    W = (1/√2) · |w_+⟩_{AB} ⊗ |+⟩_C  +  (1/√2) · |w_−⟩_{AB} ⊗ |−⟩_C

where `|w_±⟩ = (1/√2)[±√(1/3)|00⟩ + √(2/3)|Ψ⁺⟩]`. The pair-wise
substrate apparatus gives `⟨XX⟩ on |w_±⟩ = 1/3` (numerically;
analytically `(2/3)·1 + cross terms`, where cross terms vanish
because `XX|00⟩ = |11⟩ ⊥ |Ψ⁺⟩`).

Substrate-derived prediction:

    ⟨XXX⟩_W = (1/2) · (1/3) · (+1) + (1/2) · (1/3) · (−1) = 0.

QM-direct: `⟨XXX⟩_W = 0`. **Match.**

### Step 4 — apply substrate apparatus to derive `⟨XYY⟩_W`

Project mode C on σ_y eigenstates. The conditional AB states have
`⟨X ⊗ Y⟩ = 0` for both Y-branches (pair-wise substrate
calculation; the σ_x⊗σ_y operator takes `|Ψ⁺⟩ → i|Ψ⁻⟩` orthogonal
to itself, and `|00⟩ → i|11⟩` orthogonal to itself; cross terms
also vanish).

Substrate-derived prediction: `⟨XYY⟩_W = 0`. QM-direct: `0`.
**Match.**

### Honest scope of the substrate-independent derivation

What the substrate apparatus + Dicke primitive does *independently*:
- Generates W's Schmidt-on-C decomposition from `(N=3, k=1)`
  combinatorics.
- Predicts correlations by composing pair-wise apparatus
  (`⟨XX⟩ on |Ψ⁺⟩`, etc.) with single-mode basis geometry.

What it does *not* do:
- Predict QM's specific form of the Born rule (still inherited
  from the saddle-node basin geometry, per
  `lesson_forced_basin_selection.md`).
- Replace the pair-wise EPR/Bell theorem's substitution mechanism
  for the 2-mode case — that substitution is the *engine* the
  3-mode derivation rides on.

So the Dicke extension makes the substrate's *multi-mode* reach
substrate-independent (no QM substitution at the multi-mode level),
but the 2-mode engine retains the substitution scope from
`epr_bell_assembly_theorem.md`. This is consistent with the
overall substrate apparatus structure.

---

## Boundary mapping: what falls outside the substrate's reach

Tested three candidate boundary states:

### 1. `(|001⟩ − |010⟩)/√2` — actually a stabilizer state

Initial guess: an "anti-symmetric in A,B with Q_{ABC} = 1" state
that's neither GHZ-like nor W-like. Numerical stabilizer count
showed **seven** Pauli stabilizers, including independent
generators `{ZII = +1, IZZ = −1, IXX = −1}`. The state factors as
`|0⟩_A ⊗ |Ψ⁻⟩_{BC}` — a single-qubit Z eigenstate tensored with
the Bell singlet. Substrate apparatus handles this via the
stabilizer-state machinery (tensor product of the single-mode and
pair-wise pieces). **Not a boundary state.**

### 2. `(|GHZ⟩ + |W⟩)/√2` — genuinely outside

Coherent superposition of a GHZ-class state and a W-class state.
Computed: `⟨ZZZ⟩ = −0.5`, `⟨XXX⟩ = +0.5`, `⟨XXZ⟩ ≈ −0.07`.

Pauli stabilizer count: **zero**. Not a stabilizer state.

Not a Dicke state (mixes the GHZ Q-distribution with the W
Q-distribution; not symmetric-with-definite-k).

The substrate's natural apparatus does *not* extend to this state
via `(N, k)` Dicke data or Pauli stabilizers. To handle it,
substrate would need either:
- A primitive for "coherent superposition across natural classes"
  (substrate-foreign — would partially undo the structure
  the natural-class apparatus provides);
- Continuous-parameter substrate structure (Hilbert-space-like,
  also substrate-foreign).

**This is the actual boundary.**

### 3. Asymmetric `(|001⟩ + 2|010⟩ + |100⟩)/√6` — genuinely outside

Same Z-parity sector as W (`⟨ZZZ⟩ = −1`, Q_{ABC} = 1) but with
asymmetric coefficients (mode B has weight `4/6` while A and C
each have `1/6`).

Pauli stabilizer count: **one** (only `Z⊗Z⊗Z = −1`). Far short of
the 3 needed for a stabilizer state.

Not a Dicke state — the permutation symmetry is explicitly broken
by the asymmetric coefficients.

The substrate's natural apparatus does *not* extend to this state
without additional structure that would specify the asymmetric
weighting.

---

## Boundary tests, batch 2

Three additional state classes tested to sharpen the boundary:

### 4. `|T⟩_A ⊗ |Φ⁺⟩_{BC}` (single-qubit magic × Bell pair) — in reach

`|T⟩ = cos(π/8)|0⟩ + e^{iπ/4}sin(π/8)|1⟩` is a single-qubit magic
state (continuous-parameter Bloch-sphere point). Combined with a
Bell pair via tensor product.

Pauli stabilizer count: **3** (not enough for a stabilizer state on
3 qubits). Max Dicke overlap²: `0.43` (not Dicke).

But: the state is factorable as `(continuous-θ single mode) ⊗
(stabilizer Bell pair)`. The pair-wise EPR/Bell apparatus already
handles arbitrary single-mode basin angles (the θ parameter is
continuous in the substrate's basin geometry). So this state is
**in reach** via the existing tensor-product extension: substrate
handles each piece, composition is substrate-native.

This shows: the substrate's tensor-product closure is broader than
"stabilizer ⊗ Dicke." It includes `(arbitrary single-mode-via-basin)
⊗ (pair-wise EPR/Bell) ⊗ (stabilizer) ⊗ (Dicke)`. Continuous-θ
single-mode states are substrate-handled by basin geometry, which
is a primary substrate primitive.

### 5. `(T⊗I⊗I)|W⟩` (phase-twisted W) — outside

Apply a single-qubit T-gate (phase rotation by π/4 on `|1⟩`) to
mode A of the W state. Result: same Q_{ABC} = 1 sector (`⟨ZZZ⟩ =
−1`) but broken permutation symmetry (`⟨XXZ⟩ = +0.47` ≠ `⟨ZXX⟩ =
+0.67`).

Pauli stabilizer count: **1** (only `Z⊗Z⊗Z = −1`). Max Dicke
overlap²: `0.87` (close to W but not Dicke; the e^{iπ/4} phase
shifts it off the symmetric subspace).

Substrate-out: the continuous-parameter phase mixed with multi-mode
entanglement is not absorbable into the discrete-symmetry apparatus.
Unlike Test 4, this state is **not factorable** into smaller substrate-
handleable pieces — the magic phase is genuinely entangled with the
3-mode topology. This is the canonical "single-qubit magic injected
into multi-mode entanglement" case.

### 6. Generic bond-dimension-2 MPS — generically outside

Matrix-product states with bond dimension 2 are classically
tractable (polynomial classical description). Tested two MPS samples
with different matrix choices:

- **Sample (a)**: `A⁰ = σ₊/√2, A¹ = σ_z/√2` (Affleck-style
  matrices). Result: **stabilizer**, max Dicke overlap² `1.0`
  (collapses to a Dicke state by matrix degeneracy). Substrate-in
  by coincidence.
- **Sample (b)**: `A⁰ = |0⟩⟨1|, A¹ = σ_z`, different boundary
  conditions. Result: **1 Pauli stabilizer**, max Dicke overlap²
  `0.11`. Not stabilizer, not Dicke. **Substrate-out.**

Conclusion: *generic* MPS states with bond dimension 2 are outside
substrate's natural reach. Specific MPS instances aligned with
stabilizer or Dicke structure are in by coincidence.

**This refines the doc's earlier claim** that substrate reach
"closely matches classically-tractable multipartite QM": substrate
reach is a *strict subset* of classically-tractable, since generic
low-bond-dimension MPS (also classically tractable) is outside the
substrate apparatus. The classically-tractable class is broader.

### 7. Haar-random pure states — generically outside

Five samples from the Haar measure on 3-qubit pure states. Results:

- Pauli stabilizers per sample: `0, 0, 0, 0, 0`. None are
  stabilizer states.
- Max Dicke overlap² per sample: `0.24, 0.26, 0.50, 0.36, 0.23`.
  None are Dicke (all well below `1.0`).

Aggregate: `0/5 stabilizer, 0/5 Dicke` — confirms generic-out boundary.

This is the expected result: generic pure states require all `2^N − 1`
complex parameters for specification; the substrate apparatus's
`O(N)` to `O(1)` data per state cannot cover them. The substrate's
natural reach captures only the *structured*, discrete-symmetry-
characterizable subset of multipartite QM.

### Refined boundary picture

The substrate's natural reach, after batch-2 tests:

| Class | Substrate-handleable? | Mechanism |
|---|---|---|
| Single-mode states (arbitrary θ) | yes | basin geometry (continuous-θ primitive) |
| Bell pairs / pair-wise pure states | yes | EPR/Bell apparatus + substitution |
| 3+ mode stabilizer states (GHZ, cluster, codes) | yes | Pauli stabilizers as Q-invariants |
| 3+ mode Dicke states `D(N, k)` | yes | `(N, k)` recursive Schmidt |
| Tensor products of the above | yes | composition |
| Phase-twisted symmetric states ((T⊗I⊗I)|W⟩) | **no** | continuous param × multi-mode entanglement |
| Coherent class superpositions (|GHZ⟩ + |W⟩)/√2 | **no** | mixes discrete classes |
| Generic MPS (bond dim ≥ 2, non-stabilizer non-Dicke) | **no** | classically tractable but substrate-out |
| Haar-random pure states | **no** | requires all `2^N − 1` parameters |

The substrate's natural reach is **a strict subset of
classically-tractable multipartite QM** — it covers the
discrete-symmetry-characterizable + continuous-single-mode tensor-
closure subset, but excludes generic MPS-classically-tractable
states. This is sharper than the prior claim "closely matches
classically tractable."

The substrate's reach is precisely:

> **(Pauli stabilizer states) ∪ (Dicke states) ∪ (continuous-θ
> single-mode states) ∪ (tensor products thereof), with the EPR/Bell
> apparatus handling 2-mode pure states via substitution.**

Outside this reach: states whose multi-mode entanglement structure
requires continuous-parameter specification beyond what tensor
products can absorb — including generic MPS, phase-twisted
symmetric states, and the canonical "magic state injection" cases
of quantum-computational advantage.

---

## Why W is structurally different from GHZ (revised)

The original framing was "W is non-stabilizer, GHZ is stabilizer."
Refined: W is *not Pauli-stabilizer* but *is substrate-Dicke*,
while GHZ is *Pauli-stabilizer* and *not Dicke*. They live in
different substrate-natural classes:

| State | Pauli-stabilizer | Dicke `(N, k)` | Substrate-natural? |
|---|---|---|---|
| Bell states | yes | yes (`D(2, k)`) | yes |
| GHZ | yes (`XXX, ZZI, IZZ`) | no | yes (stabilizer) |
| W = `D(3,1)` | no (only `ZZZ = −1`) | yes | yes (Dicke) |
| `D(3,2)` = "dual W" | no | yes | yes (Dicke) |
| Cluster states | yes | no | yes (stabilizer) |
| `(|GHZ⟩ + |W⟩)/√2` | no | no | no (outside) |
| `(|001⟩ + 2|010⟩ + |100⟩)/√6` | no | no | no (outside) |

The Pauli-stabilizer apparatus needs `O(N)` data per state
(`N` stabilizer generators); the Dicke apparatus needs `O(1)` data
(`(N, k)`). Both are polynomial-or-better, vastly more compact than
the `2^N` complex parameters of a generic pure state. The
substrate's natural reach is exactly the union of these
discrete-symmetry-characterizable classes (plus their tensor
products).

---

## What this means for the broader QM-reframing thread

### For the GHZ doc's structural-scaling claim

`ghz_from_substrate.md` (PR #184) claimed substrate-native
linear-in-N scaling. This claim is precise:

- For **stabilizer N-mode entanglement**: linear-in-N substrate
  data (`N` stabilizer generators). Matches the
  classically-efficient Gottesman–Knill regime.
- For **Dicke N-mode entanglement**: O(1) substrate data
  (`(N, k)`). Strictly better than stabilizer scaling.
- For **arbitrary N-mode entanglement**: substrate apparatus does
  not extend uniformly; the boundary is at non-stabilizer non-Dicke
  states.

The GHZ doc's specific predictions and Mermin reproduction stand.
What needs precise scope is the "extends to all N-mode
entanglement" implicit claim. With the Dicke extension, the
substrate's natural reach is **stabilizer ∪ Dicke ∪ tensor
products** — broader than stabilizer-only.

### For "toss tensor scaling" in the reframing

Stabilizer states are exactly the classically-efficient subset
(Gottesman–Knill). Dicke states are also classically efficient
(they have polynomial classical description and efficient
simulation algorithms; cf. permutation-invariant matrix product
states). Together, stabilizer ∪ Dicke covers a wide swath of
classically-simulable multipartite entanglement.

The substrate's reframing of "toss tensor scaling" holds for these
classes specifically:
- ✓ Stabilizer entanglement: linear-in-N substrate data, matches
  efficient classical simulation.
- ✓ Dicke entanglement: O(1) substrate data, matches the
  permutation-invariant tensor-network compression.
- ✓ Continuous-θ single-mode states (including `|T⟩` magic):
  handled by basin geometry.
- ✓ Tensor products of the above.
- ✗ Generic non-stabilizer non-Dicke states *with multi-mode
  entanglement* (e.g., generic bond-dim-2 MPS, phase-twisted W,
  magic-spread CNOT outputs): substrate currently doesn't reach.

The substrate's reach is a **strict subset** of
classically-tractable multipartite entanglement — it covers the
*structured* portion (discrete symmetries + single-mode continuous
parameter) but not the *generic* portion (bond-dimension-2+ MPS
with arbitrary continuous parameters in the entanglement
structure). This is foundationally substantive: the substrate
apparatus captures multipartite entanglement that *factors* through
discrete symmetry classes, leaving generic continuous-parameter
entanglement outside.

The boundary roughly aligns with the "structured vs generic"
distinction in classical simulation literature, not exactly with
"classically tractable vs not."

### For the broader QM-reframing program

The methodological principle ("if it can't be expressed from an
event-driven log, that should be proven, not assumed") is
*satisfied* for the natural classes (stabilizer + Dicke + tensor)
and *exhibited as unmet* for the non-stabilizer non-Dicke regime
(`(|GHZ⟩+|W⟩)/√2` is the discriminator).

The reframing thread can claim:

> Substrate apparatus replaces tensor scaling for the
> classically-tractable subset of multipartite quantum mechanics;
> the quantum-computational-advantage regime (magic states,
> non-stabilizer non-Dicke) requires continuous-parameter structure
> the substrate currently does not have.

This is a precise, honest, generative claim. It identifies what
substrate work would push the boundary further and what would not.

---

## Falsifiers

- **A substrate-native characterization of `(|GHZ⟩ + |W⟩)/√2`** in
  `O(N)` data without continuous-parameter Hilbert-space structure.
  Would void the boundary identification and extend the
  substrate's reach into non-stabilizer non-Dicke territory.
- **A demonstration that the Dicke extension's `(N, k)` primitive
  is secretly continuous-parameter** (e.g., by showing the
  combinatorial weights `(k/N, (N−k)/N)` require continuous-real
  input). Standard combinatorics gives rational weights from integer
  data; the primitive remains discrete.
- **A magic-state class shown to be substrate-natural under some
  extension I missed.** For instance, if T-states `|T⟩ = cos(π/8)|0⟩
  + e^{iπ/4}sin(π/8)|1⟩` were derivable from a substrate primitive
  beyond Pauli-Z₂ + Dicke, the reach would extend.
- **An equivalent characterization of "classically simulable" that
  the substrate apparatus does *not* match.** Would shift the
  alignment claim between substrate's reach and the
  Gottesman–Knill-plus-symmetric regime.

---

## Why this matters

T1a's two-sided result — narrowing then extension — exemplifies the
discriminator-clause discipline. The bare Pauli-Z₂ apparatus was
shown insufficient for W (narrowing); a single
substrate-aligned extension (Dicke `(N, k)`) was identified and
verified to handle W and the full Dicke family (extension).
Together they give a precise scope: the substrate's natural reach
is exactly the discrete-symmetry-characterizable multipartite
states (stabilizer ∪ Dicke ∪ tensor products), which closely
matches the classically-tractable subset of multipartite QM.

The boundary is exhibited concretely: `(|GHZ⟩ + |W⟩)/√2` has zero
Pauli stabilizers and is non-Dicke; the substrate's apparatus does
not naturally reach it. The "magic state" regime where quantum
computational advantage lives is the same regime where the
substrate's discrete-symmetry apparatus stops being sufficient.

This is the discipline applied to its sharpest test so far. The
narrowing was real (bare Pauli-Z₂ underdetermined W); the
extension is substantial (Dicke primitive is substrate-native);
the boundary mapping is precise (zero-stabilizer non-Dicke states
are outside).

Class: foundational consolidation (Class 3, articulation) with a
two-sided substantive finding. The arc closed is the question of
whether the substrate's multi-mode apparatus extends to W: it does,
with a single substrate-native primitive; the apparatus then covers
the entire discrete-symmetry-characterizable class of multipartite
states; the boundary at non-stabilizer non-Dicke "magic states" is
identified.

---

## Cross-links

- `ghz_from_substrate.md` (PR #184) — the GHZ-type worked example;
  this doc revises the implicit scope from "all N-mode" to
  "stabilizer ∪ Dicke ∪ tensor products."
- `epr_bell_assembly_theorem.md` (#152) — the pair-wise machinery
  that the substrate's Dicke conditional decomposition rides on
  (substrate-derived `⟨XX⟩ on |Ψ⁺⟩ = +1`, etc.).
- `q_mod2_conservation_theorem.md` (#1) — the foundational Q mod 2
  apparatus. For Dicke states `D(N, k)`, the substrate Q-invariant
  is recovered as `Q = k mod 2`; the Dicke primitive *refines*
  rather than replaces this invariant.
- `meaning_of_two_wip.md` (PR #183) — the binary axis underlying
  Pauli-Z₂. The Dicke primitive uses integer combinatorial weights
  on top of the binary axis structure; it doesn't introduce a new
  "two."
- `gr_qm_unification_synthesis.md` (PR #181) — the capstone
  synthesis. The substrate apparatus's reach is now precisely
  scoped to discrete-symmetry classes; this should be noted under
  scope.
- `predictions_horizon_2026.md` (PR #180) — the prediction suite.
  Stabilizer + Dicke covers most physics-relevant multipartite
  predictions; the non-stabilizer non-Dicke boundary affects
  quantum-computing-advantage claims but not fundamental physics
  predictions.
- `substrate_determinism.md` — the inviolables. The Dicke primitive
  is *not* a new inviolable; it's a substrate-aligned extension
  using existing primitives (Q mod 2 + symmetric distribution +
  pair-wise apparatus).
- `lesson_forced_basin_selection.md` — per-mode basin geometry
  remains the foundation for single-mode Born statistics; the
  Dicke extension composes it with multi-mode symmetric
  distribution.

---

## One-line summary

The substrate's bare Pauli-Z₂ `Q ∈ ℤ/2ℤ` apparatus from
`ghz_from_substrate.md` (PR #184) underdetermines the W state, but
a single substrate-aligned extension — the *Dicke primitive*
`(N, k) = (modes, excitations)` with permutation-symmetric
distribution — closes the gap: the recursive Schmidt structure
`D(N,k) = √(k/N)·D(N−1,k−1)⊗|1⟩ + √((N−k)/N)·D(N−1,k)⊗|0⟩` is
derived from substrate combinatorics (not QM substitution) and
composes with the existing pair-wise EPR/Bell apparatus to
substrate-natively reproduce W's correlations (`⟨XXZ⟩ = +2/3`,
`⟨XXX⟩ = 0`, etc.), verified across the Dicke family
(`D(3,1), D(4,1), D(4,2), D(4,3), D(5,2)`); the substrate's
refined natural reach is **(Pauli stabilizer states) ∪ (Dicke
states) ∪ (continuous-θ single-mode states via basin geometry) ∪
(tensor products thereof)**, a strict subset of classically-tractable
multipartite QM (specifically: excludes generic bond-dim-≥2 MPS,
phase-twisted symmetric states like `(T⊗I⊗I)|W⟩`, and coherent
class-superpositions like `(|GHZ⟩+|W⟩)/√2`); boundary tests
numerically confirm the edge — `(|GHZ⟩+|W⟩)/√2` has zero Pauli
stabilizers and is not Dicke; phase-twisted W has one stabilizer
and `0.87` Dicke overlap² but is not Dicke; Haar-random samples
average zero stabilizers and `< 0.5` Dicke overlap² — placing the
substrate's natural reach at the **discrete-symmetry-plus-
continuous-single-mode-tensor-closure** subset of multipartite
states, with the boundary at "magic state injected into multi-mode
entanglement," the same regime where quantum-computational
advantage is conjectured to live, sharpening rather than
weakening the QM-reframing program's discipline.
