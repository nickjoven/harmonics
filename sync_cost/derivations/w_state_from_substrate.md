# W states from substrate — narrowing the apparatus's reach

## Status

**T1a worked example, with substantive narrowing finding.** Tests
whether the substrate's `Q ∈ ℤ/2ℤ`-invariant apparatus from
`ghz_from_substrate.md` (PR #184) generalizes naturally to the W
state — the canonical 3-mode entangled state LOCC-inequivalent
to GHZ.

**Honest verdict:** the substrate's apparatus *partially* handles W.
The single Q-invariant captures W's Z-basis triple parity
(`Q_{ABC} = 1` definite) but does **not** uniquely characterize the
W state. W lives in a 4-dimensional subspace (`σ_z⊗σ_z⊗σ_z`
eigenvalue `−1`) of the 8-dimensional 3-qubit Hilbert space; the
substrate's single `Q_{ABC}` invariant underdetermines W; the full
prediction of W's correlation structure requires either substitution
from QM (term-by-term identification, same scope as the GHZ doc) or
additional substrate structure beyond the Pauli-Z₂ apparatus.

**The narrowing.** GHZ is a *stabilizer state* (Pauli eigenstate);
W is *not*. The substrate's natural Q-invariant apparatus extends
to stabilizer-style topologies (GHZ, cluster states, error-correcting
codes) but requires additional structure for non-stabilizer states
like W. This is a substantial but bounded reach: stabilizer states
cover most multi-mode entanglement of physics-foundational interest;
non-stabilizer states are predominantly relevant for the
quantum-computational advantage regime (Gottesman–Knill theorem).

This is *not* a falsification of `ghz_from_substrate.md`; it is a
precise narrowing of its structural-scaling claim from "all N-mode
entanglement" to "stabilizer-style N-mode entanglement." The GHZ
doc's predictions and Mermin-violation reproduction stand; what
needs revision is the implicit suggestion that the apparatus
generalizes uniformly to arbitrary multi-mode entangled states.

No new primitive. The contribution is the precise audit: what the
Pauli-Z₂ substrate apparatus covers, and where it stops.

---

## QM correlations for W (verified numerically)

The W state:

    |W⟩  =  (|001⟩ + |010⟩ + |100⟩) / √3.

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

W satisfies the Mermin inequality `|M| ≤ 2` (LHV bound).
**W does *not* violate the Mermin inequality**, despite being a
genuinely 3-mode entangled state. This is well-known: the Mermin
inequality is a test for GHZ-like correlations specifically;
LOCC-inequivalent entangled states (like W) need different Bell-style
inequalities to detect their multi-mode entanglement (e.g., the
Cabello–Wootters inequality, or pair-wise CHSH tests on the
non-trivial reduced states).

For comparison, GHZ saturates `|M| = 4` (matching the QM bound, well
above LHV).

---

## W's pair-wise reduced state

Tracing out the third mode:

    ρ_{AB}(W)  =  (1/3) |00⟩⟨00|  +  (2/3) |Ψ⁺⟩⟨Ψ⁺|

where `|Ψ⁺⟩ = (|01⟩ + |10⟩)/√2`. The pair-wise marginal has weight
`1/3` on the separable `|00⟩` and weight `2/3` on the entangled
Bell state `|Ψ⁺⟩`. Verified numerically (eigenvalues `1/3, 2/3, 0,
0`; the `2/3` eigenvalue corresponds to the entangled component).

For comparison, GHZ's pair-wise marginal:

    ρ_{AB}(GHZ)  =  (1/2) (|00⟩⟨00| + |11⟩⟨11|)

— a classical mixture, no entanglement.

This is a foundational distinction between GHZ and W: GHZ's
multi-mode entanglement vanishes upon tracing out *any* mode,
while W's multi-mode entanglement persists in pair-wise reduced
states. Both are "genuinely 3-mode entangled" but in different
senses.

---

## Substrate Q apparatus applied to W

### What the substrate Q apparatus captures

For the substrate's `Q_{ABC} ∈ ℤ/2ℤ` invariant in the Z basis:

- W has **definite** Q_{ABC} = 1 (every basis state in the superposition
  `(|001⟩ + |010⟩ + |100⟩)/√3` has exactly one `|1⟩`; parity = 1 for
  each).
- This correctly predicts `⟨Z_A Z_B Z_C⟩ = −1` (the all-Z joint
  measurement returns an odd-parity outcome with probability 1; the
  Z_{ABC} eigenvalue is `−1`).
- This correctly predicts `⟨X_A X_B X_C⟩ = 0` for the X-Y plane
  joint measurements: the X-Y plane is "perpendicular" to the
  Z-basis-definite-parity sector; joint outcomes in that plane are
  uncorrelated; expectation value `0`.

The substrate's pair-wise Q distribution for W's reduced state:

- `⟨Z_A Z_B⟩_W = −1/3`, giving `P(Q_{AB} = 0) = 1/3`,
  `P(Q_{AB} = 1) = 2/3` — **mixed** (indeterminate), matching the
  `(1/3) |00⟩⟨00| + (2/3) |Ψ⁺⟩⟨Ψ⁺|` decomposition.
- The pair-wise Q-distribution is substrate-expressible (`(1/3,
  2/3)` weights). The pair-wise marginal `ρ_{AB}` carries
  substrate-readable structure.

So the substrate's Q apparatus captures:
- The Z-basis triple parity of W.
- The X-Y plane joint vanishing for Mermin contexts.
- The pair-wise Q distribution (mixed, as expected for W).

### What the substrate Q apparatus does **not** capture (without substitution)

The substrate's Q apparatus alone does not predict:
- Mixed-basis non-trivial correlations like
  `⟨σ_x ⊗ σ_x ⊗ σ_z⟩_W = +2/3` (and the various permutations). The
  Q-invariant in the Z basis doesn't constrain non-Z-basis joint
  expectations directly.
- W's specific position within the 4-dimensional `Z_{ABC} = −1`
  subspace. Many states share `Q_{ABC} = 1` definite parity; W is
  one of them but the substrate's single Q-invariant doesn't single
  it out.

To predict W's full correlation structure, the substrate apparatus
must either:

1. **Substitute from QM.** Identify W's QM wavefunction → substrate
   apparatus produces substrate-equivalent predictions term-by-term.
   This is the *same* substitution mechanism used in
   `epr_bell_assembly_theorem.md` Clause (a) and
   `ghz_from_substrate.md` Step 3. Works for any specific state, but
   the substrate doesn't *independently* derive the predictions — it
   inherits them via the substrate ↔ QM identification.
2. **Add substrate structure beyond Pauli-Z₂.** A richer
   substrate-native characterization of W (see §"What additional
   substrate structure would handle W" below) would let the substrate
   make independent predictions for non-stabilizer states. Currently
   open work.

The first option is consistent with the substrate apparatus's scope
as defined in the EPR/Bell pair-wise theorem and the GHZ doc. The
second is the path that would extend the substrate's
*independent* predictive power.

---

## Why W is structurally harder than GHZ for the substrate

### The stabilizer-vs-non-stabilizer distinction

A *stabilizer state* on N qubits is the unique +1 eigenstate of an
abelian subgroup of the N-qubit Pauli group, with N independent
commuting Pauli generators (the "stabilizer group"). Stabilizer
states form a finite subset of pure states (combinatorially
specified by the choice of N commuting Pauli generators up to
sign); the Gottesman–Knill theorem (1998) shows they can be
efficiently simulated classically.

GHZ is a stabilizer state: its stabilizer group is generated by

    {σ_x ⊗ σ_x ⊗ σ_x = +1,
     σ_z ⊗ σ_z ⊗ I   = +1,
     I   ⊗ σ_z ⊗ σ_z = +1}.

Three independent generators for a 3-qubit state, defining the
1-dimensional subspace `|GHZ⟩`. The substrate's Pauli-Z₂ apparatus
(`Q ∈ ℤ/2ℤ`-eigenvalues for tensor products of `σ_x`, `σ_y`, `σ_z`)
captures stabilizer states naturally: each stabilizer is a Q-invariant
with `±1` eigenvalue.

**W is not a stabilizer state.** Direct calculation: the only
non-trivial Pauli operator P with `P|W⟩ = ±|W⟩` is
`σ_z ⊗ σ_z ⊗ σ_z = −1`. The substrate's Pauli-Z₂ apparatus gives W
*one* stabilizer-like Q-invariant (out of three needed to fully
specify a 3-qubit state).

The 4-dimensional subspace specified by `Z_{ABC} = −1` includes W
*and* other states (e.g., `(|001⟩ − |010⟩)/√2` is also in this
subspace and is *not* W). To single out W, additional substrate
information beyond the Pauli-Z₂ apparatus is needed.

### Information content per state

For an N-qubit *stabilizer* state, the state is fully specified by
N stabilizer generators. The substrate needs `O(N)` Q-invariants
(one per stabilizer) plus per-mode basin geometry, for `O(N)` total
substrate objects. This is the linear-in-N scaling claimed in the
GHZ doc, and it holds for stabilizer states.

For a general N-qubit pure state in `(ℂ²)^{⊗N}`, the state is
specified by `2^N − 1` complex parameters. Pauli stabilizers cover
only the discrete-symmetry information; non-stabilizer (or "magic")
states need additional continuous-parameter substrate structure.

For W specifically: the symmetric single-excitation structure
(|001⟩, |010⟩, |100⟩ each with equal weight `1/√3`) is a
*permutation-symmetric* constraint that's not Pauli-Z₂. The
substrate would need to express this symmetry constraint to specify
W uniquely.

---

## What additional substrate structure would handle W

Three plausible substrate extensions:

### Option 1 — Permutation-symmetric event-counting

W is the symmetric single-excitation state. Substrate-natively: one
basin-selection event occurs in the substrate, and the substrate's
3-mode topology constrains the event to be distributed
*permutation-symmetrically* across the three modes. The substrate
specification would include:
- `Q_{ABC} = 1` (Z-basis triple parity, gives single-excitation
  constraint)
- A permutation-symmetry constraint (the event is distributed
  symmetrically; substrate-native version of "single-excitation
  symmetric superposition")

This is a substrate-native characterization in `O(N)` data (one Q
+ one symmetry label per N-mode system) — provided the substrate
apparatus extends to express permutation symmetry constraints. Not
currently in the substrate apparatus.

### Option 2 — Higher Z-grading

Beyond `Q ∈ ℤ/2ℤ`, the substrate might admit a higher `ℤ_n` grading
for larger N or for specific entanglement classes. For W, a possible
relevant grading is `ℤ_3` (since W is the "single excitation in 3
modes" state and 3 is involved). Substrate-natively: the substrate's
binary axis structure might extend to a ternary axis for some
topologies, with a corresponding `Q ∈ ℤ/3ℤ` invariant. This is
speculative and not motivated by current substrate primitives.

### Option 3 — Continuous-parameter substrate structure

For non-stabilizer states more generally, the substrate would need
continuous-parameter invariants beyond the Pauli-Z₂ discrete structure.
This is the largest extension and would effectively reintroduce
something Hilbert-space-like — which is what the broader QM-reframing
thread is trying to avoid.

### Honest assessment

Option 1 (permutation-symmetric event-counting) is the most
substrate-aligned extension and would let the substrate handle
W-style symmetric states without invoking Hilbert-space machinery.
Option 2 is structurally interesting but currently unmotivated.
Option 3 would partially undo the reframing.

None of the three is currently in the substrate apparatus. T1a
identifies the work needed; it doesn't carry it out.

---

## The narrowing for the broader QM-reframing thread

### What this means for the GHZ doc's structural-scaling claim

`ghz_from_substrate.md` (PR #184) claimed:

> "For N = 100 entangled modes: 101 substrate objects vs. `2^{100} ≈
> 10^{30}` tensor components."

This claim holds for stabilizer N-mode entanglement (which includes
many physics-relevant cases: GHZ-type cosmological correlations,
cluster states, stabilizer codes). It does *not* hold for arbitrary
N-mode entanglement; non-stabilizer states like W require additional
substrate structure beyond the Pauli-Z₂ apparatus.

The GHZ doc should be read with this scope: *substrate-native
linear-in-N scaling for stabilizer-style multi-mode entanglement*.
The doc itself flags W states as the first falsification test (under
"Falsifiers"); T1a confirms the test reveals a real boundary.

### What this means for "toss tensor scaling" in the reframing

Stabilizer states are exactly the states efficiently simulable
classically. Standard quantum computing's claimed advantage comes
from *non-stabilizer* operations (T gates, magic states, etc.) on
top of stabilizer infrastructure.

For the substrate's reframing claim "toss tensor scaling":
- ✓ For stabilizer-state entanglement, the substrate's linear scaling
  is real and matches the Gottesman–Knill efficient-simulation regime.
- ✗ For non-stabilizer "magic" states (W, T-gate output states,
  etc.), the substrate apparatus is currently insufficient.

The substrate's reach is thus *broader than tensor products for
stabilizer-equivalent cases* but *narrower than tensor products
overall*. The honest reframing is: substrate apparatus replaces
tensor scaling for the classically-efficient subset of N-mode
entanglement; the quantum-computational-advantage regime
(non-stabilizer) is open.

### What this means for the broader QM-reframing program

The methodological principle from earlier ("if it can't be expressed
from an event-driven log, that should be proven, not assumed") is
unaffected. T1a *exhibits* the proof: W's correlation structure
cannot be expressed by the substrate's Pauli-Z₂ event-log alone;
additional substrate structure is needed. The discriminator clause
applied to this case: *the substrate apparatus is currently
insufficient for non-stabilizer N-mode entanglement, and the
relevant Pauli-Z₂ underdetermination is exhibited explicitly*.

This is exactly the kind of audit the discipline asks for. The
narrowing is *generative*: it identifies what substrate work is
needed to extend the reframing's reach (Option 1 or 2 above), and
it prevents the broader reframing doc from overclaiming.

---

## Falsifiers

- **A substrate-native characterization of W** in `O(N)` data,
  without continuous-parameter Hilbert-space structure (Option 1 or
  2 made concrete). Would *void the narrowing* — the substrate
  apparatus would extend to non-stabilizer states naturally.
- **A demonstration that the substrate's Pauli-Z₂ apparatus *does*
  uniquely characterize W** via a derivation I missed. Would also
  void the narrowing.
- **W shown to be a stabilizer state under some equivalent Pauli
  formalism** (e.g., a redefinition of "stabilizer" that includes W).
  Standard Pauli-stabilizer formalism gives only `σ_z⊗σ_z⊗σ_z` as
  W's stabilizer; this is one of three needed for a 3-qubit state;
  the standard formalism confirms W is non-stabilizer. A redefinition
  that admits W would change the substrate apparatus's natural reach.
- **A more permissive notion of "linear-in-N scaling"** that admits
  non-stabilizer states under different counting. Would shift the
  reframing's discipline boundary; needs careful audit to avoid
  hiding the underdetermination.

---

## Why this matters

T1a is the first level-3 worked example to *narrow* (rather than
extend) the substrate's apparatus reach. The GHZ doc (PR #184)
demonstrated the substrate handles a benchmark multi-mode case via
the linear-scaling apparatus; this doc demonstrates the apparatus
does not extend uniformly to all multi-mode cases, with a precise
identification of where the boundary sits (stabilizer vs.
non-stabilizer states).

This is the discriminator-clause discipline applied to the
substrate's multi-mode reach: name the boundary precisely; identify
what additional substrate work would push it. The methodological
principle ("event-log sufficiency should be proven, not assumed")
applies: for non-stabilizer states, the substrate currently *does
not* prove event-log sufficiency; this doc names the gap.

Class: foundational consolidation (Class 3, articulation) with a
substantive narrowing finding. The arc closed is the question of
whether the GHZ doc's structural-scaling claim extends to arbitrary
multi-mode entanglement: it does not; it extends to stabilizer-style
entanglement specifically. The remaining work to extend the substrate
beyond stabilizer states is identified.

---

## Cross-links

- `ghz_from_substrate.md` (PR #184) — the GHZ-type worked example
  this doc narrows; T1a is the most-information test the GHZ doc
  itself flagged in its "Falsifiers" section.
- `epr_bell_assembly_theorem.md` (#152) — the pair-wise machinery;
  W's pair-wise reduced state has structure both docs handle.
- `q_mod2_conservation_theorem.md` (#1) — the foundational Q mod 2
  apparatus that this doc shows is insufficient for non-stabilizer
  states.
- `meaning_of_two_wip.md` (PR #183) — the binary axis structure
  underlying the Pauli-Z₂ apparatus; the narrowing here clarifies
  the apparatus's natural reach.
- `gr_qm_unification_synthesis.md` (PR #181) — the capstone
  synthesis; this narrowing should be cross-referenced under "what
  this does not say" → the substrate's multi-mode reach has bounds.
- `predictions_horizon_2026.md` (PR #180) — the broader prediction
  suite; the substrate's stabilizer-state reach is sufficient for
  physics-foundational predictions; the non-stabilizer narrowing
  affects quantum-computing-advantage claims but not cosmological /
  fundamental-physics claims.
- `substrate_determinism.md` — the 10 inviolables; the Pauli-Z₂
  apparatus underlies #1 (Q mod 2), #3 (bicone Z₂), and several
  others.
- `lesson_forced_basin_selection.md` — the basin geometry per
  measurement; this doc shows the per-mode basin geometry is *not*
  sufficient on its own for non-stabilizer multi-mode states.

---

## One-line summary

The substrate's Pauli-Z₂ `Q ∈ ℤ/2ℤ` apparatus from
`ghz_from_substrate.md` (PR #184) extends naturally to stabilizer
N-mode entangled states (GHZ, cluster, codes — covered by linear-in-N
substrate scaling) but **not** to non-stabilizer "magic" states like
W; W is in the `σ_z ⊗ σ_z ⊗ σ_z = −1` subspace (Q_{ABC} = 1
definite) but the substrate's single Q-invariant underdetermines it
within that 4-dim subspace; substitution from QM still gives
QM-matching predictions, but substrate-independent characterization
requires either permutation-symmetric event-counting structure or
higher-grade invariants beyond the current Pauli-Z₂ apparatus —
which are open derivation work. The narrowing is *generative*: it
identifies where the substrate apparatus needs extension and
prevents the broader QM-reframing program from overclaiming reach
into the quantum-computational-advantage regime.
