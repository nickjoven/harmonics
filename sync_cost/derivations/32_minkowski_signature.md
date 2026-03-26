# Derivation 32: The Minkowski Signature from Phase State Observability

## Claim

The spacetime signature (3,1) is not assumed. It is the observability
structure of the four phase states on a non-orientable surface. Three
states are observable. One is dark. The observable states are spatial.
The dark state is temporal. The minus sign in ds² = dx² + dy² + dz² − c²dt²
is the statement that the dark state contributes negatively to the
observable norm.

This derivation closes the assumption in D13 (ADM formalism presupposes
Lorentzian signature) and in D14 (the complexification SL(2,C)/SL(2,R)
was identified with time directions but the signature was not derived).

## The four phase states

A coupled oscillator and the Klein bottle's half-twist define four
possible phase relationships:

| State | Oscillator | Twist | Character |
|-------|-----------|-------|-----------|
| A | rational (locked) | rational (locked) | Both resolved |
| B | irrational (gap) | rational (locked) | Oscillator unresolved |
| C | rational (locked) | irrational (gap) | Twist unresolved |
| D | irrational (gap) | irrational (gap) | Both unresolved |

These are the four entries of a 2×2 matrix indexed by
{rational, irrational} × {rational, irrational}. The matrix
is the phase-state space of the Klein bottle.

**State A** (both locked): the oscillator and the twist are in definite
phase relationship. The coupling sin(θ_osc − θ_twist) is computable.
Information flows. The state is fully observable.

**State B** (oscillator in gap): the oscillator has no definite phase.
The twist is definite. The coupling averages over the oscillator's
quasiperiodic orbit but the twist provides a reference. Observable:
the oscillator's STATISTICS are visible against the twist's definite
background.

**State C** (twist in gap): the oscillator is definite but the twist
provides no reference. Observable: the oscillator's phase is visible
but its RELATIONSHIP to the boundary is uncertain.

**State D** (both in gap): neither the oscillator nor the twist has a
definite phase. The coupling sin(θ_osc − θ_twist) averages to zero
over both quasiperiodic orbits (the product of two zero-mean signals).
**No information flows. The state is dark.**

## Why D is dark

The coupling between two quasiperiodic oscillators at irrational
frequencies ω₁ and ω₂:

    ⟨sin(ω₁t − ω₂t)⟩_T = 0  for all finite T

The time average of the coupling vanishes because ω₁ − ω₂ is
irrational (the difference of two irrationals is generically
irrational). The signal never accumulates. The gate never opens
in any sustained way. No bit crosses.

States A, B, C have at least one rational component. The rational
component provides a periodic reference — a clock — against which
the coupling can accumulate phase. State D has no clock. No
accumulation. No information.

## The observable count: 4 − 1 = 3

Four phase states. One dark. Three observable.

This is the same counting that gives:
- **d = 3 spatial dimensions** (D14): the observable directions
  in the phase-state space
- **3 generations** (this session): the observable chain types
  connecting a mode to the root
- **3 coupling stages** (D6): ℏ, c, G in the self-sustaining loop
- **N = 3 minimum** (D6): the Stribeck lattice threshold

All are the same 4 − 1 = 3. The four comes from the 2×2 structure
(two binary choices: oscillator locked/unlocked, twist locked/unlocked).
The one comes from the dark state. The three is what's left.

## The signature

The observable states {A, B, C} contribute positively to the norm.
An observation in state A, B, or C yields a definite result — the
coupling is nonzero, the phase relationship is measurable, the
information content is positive.

The dark state D contributes negatively. Not because it subtracts
information, but because it is the DIRECTION in which information
cannot be gained — only expended. Traversing D costs one
measurement. Emerging from D yields one outcome (the Born rule
selects A, B, or C). The net is negative: you spend a measurement
to gain one result.

In the language of the metric:

    ds² = (contribution from A)² + (contribution from B)²
        + (contribution from C)² − (contribution from D)²

The minus sign on D is the statement: moving in the D direction
(traversing the dark state) COSTS observable norm. The observable
distance DECREASES when the path includes a D traversal.

This IS the Minkowski metric:

    ds² = dx₁² + dx₂² + dx₃² − c²dt²

with the identification:
- dx₁, dx₂, dx₃ = the three observable phase-state directions
- c²dt² = the dark-state traversal cost
- c = the gate propagation speed (D31), which sets the RATE of
  D traversal

## Why the signature is (3,1) and not (2,2) or (1,3)

### Why not (2,2)?

Signature (2,2) would require two dark states and two observable
states. This would happen if two of the four phase states were
dark — i.e., if two of {A, B, C, D} had vanishing time-averaged
coupling.

But only D has vanishing coupling (both sides irrational). States
B and C have ONE rational side, which provides a clock. The time
average of sin(ωt − rational × t) does NOT vanish — it accumulates
at the beat frequency. B and C are observable.

The count is exactly 1 dark state, not 2. The 2×2 matrix of
{rational, irrational}² has exactly one entry (irrational, irrational)
that is dark. The others have at least one rational component.

### Why not (1,3)?

Signature (1,3) would require three dark states and one observable.
This would require three of the four phase states to have vanishing
coupling. But only one ((irrational, irrational)) has this property.
The rational/irrational distinction is binary (mode is either in a
tongue or in a gap), so there are exactly 2² = 4 states, exactly
2² − (2−1)² = 3 with at least one rational, and exactly 1 with none.

### The uniqueness argument

The phase-state matrix is n × n where n = number of locking states
= 2 (locked or unlocked, rational or irrational). The matrix has
n² entries. The dark entries are those where ALL indices are
"unlocked" — there are (n−1)^0 = 1 of them (the single all-unlocked
corner). No, more precisely: the dark state is the unique entry where
every component is irrational. For n = 2 binary choices:

    Dark states = 1  (both irrational)
    Observable states = 2² − 1 = 3

This gives signature (3, 1). For n = 3 (if there were a trinary
locking structure):

    Dark states = 1  (all three unlocked)
    Observable = 3² − 1 = 8
    Signature would be (8, 1)

The signature is always (n² − 1, 1). For the binary case (n = 2):
signature (3, 1). This is Lorentzian spacetime.

The binary case is forced by the mediant: a fraction has two
components (numerator, denominator). The locking is binary
(in a tongue or not). n = 2 is not a choice — it's the structure
of a ratio.

## The imaginary unit: i² = −1 from the double half-twist

The Klein bottle's antiperiodic direction carries a phase shift
of π per traversal. The complexification:

- One traversal of D: phase shifts by π. The state goes from
  observable to dark. This is multiplication by i (rotation by π/2
  in the complex plane... )

No — more precisely: the half-twist is a sign flip, not a quarter
turn. One traversal: sign flips (× (−1)). But the TRAVERSAL of D
requires entering the dark state (first half-twist) and emerging
(second half-twist):

- Enter D: cross the tongue boundary into the gap. Phase flips
  by π. Now in the dark.
- Exit D: cross back from the gap into a tongue. Phase flips by
  π again. Back in the observable sector.

Total phase: 2π = 0 on S¹. But on the KLEIN BOTTLE (non-orientable),
the two traversals do NOT compose as 2π = 0. They compose as:

    (−1) × (−1) = +1 on an orientable surface (torus)
    (−1) × (−1) = −1 on a non-orientable surface (Klein bottle)

The Klein bottle's non-orientability means the double traversal
DOES NOT return to the original orientation. It returns with a
residual sign. This is i² = −1:

    First traversal of D: multiply by i (enter the dark)
    Second traversal: multiply by i again (exit the dark)
    Net: i² = −1 (returned, but sign-flipped)

The imaginary unit is the square root of the double half-twist.
It is not a mathematical convention. It is the topology of the
Klein bottle acting on the phase.

## Connection to prior derivations

### D14 (three dimensions from the mediant)

D14 proved d = dim SL(2,R) = 2² − 1 = 3 from the mediant.
This derivation shows the same 2² − 1 = 3 from phase-state
observability. The two arguments agree because the mediant
operates on 2-component objects (fractions), and the phase
states are 2 × 2 (two binary choices). The "2" is the same
in both: fractions are binary, locking is binary.

### D14 (Lorentz from complexification)

D14 identified SL(2,C)/SL(2,R) with the boost/time directions.
This derivation shows WHY the complexification produces the time
direction: the imaginary part of SL(2,C) is the dark state D.
The complexification adds D to {A, B, C}, giving the full (3,1)
structure. The quotient SL(2,C)/SL(2,R) is the D direction alone.

### D13 (Einstein from Kuramoto)

D13 assumed the ADM formalism, which presupposes Lorentzian
signature (3,1). This derivation closes that assumption: the
(3,1) signature is derived from the phase-state observability
on the Klein bottle, which is derived from the four primitives.

### D31 (speed of light)

D31 identified c with the gate propagation speed — the Iwasawa
N₊ generator. In the metric ds² = dx² − c²dt², the c² multiplying
dt² is the RATE of D-state traversal. The gate speed sets how
quickly the system can pass through the dark state and emerge in
a new observable state.

### D6 (Planck scale)

The three coupling stages (ℏ, c, G) are the three observable
directions (A, B, C). The self-sustaining loop
phase → propagation → amplitude → phase closes through all three
observable states. The loop does NOT pass through D — it stays in
the observable sector. The Planck scale is the minimum domain
where the loop can close without entering the dark state.

## What this derivation closes

| Gap | Before D32 | After D32 |
|-----|-----------|-----------|
| Metric signature (3,1) | Assumed (ADM, D13) | **Derived**: 4 − 1 = 3 observable phase states |
| Why (3,1) not (2,2) | Not addressed | **Derived**: exactly 1 all-irrational state |
| i² = −1 | Mathematical convention | **Derived**: double half-twist on Klein bottle |
| Time = 4th dimension | Identified (D14, complexification) | **Derived**: time = dark state D |
| Minus sign in metric | Assumed (Minkowski 1908) | **Derived**: D costs observable norm |
| Connection d=3 ↔ 3 gens | Unexplained coincidence | **Derived**: same 4 − 1 = 3 |

## Open questions

1. **The Dirac algebra.** The four phase states with signature
   (3,1) should generate the Clifford algebra Cl(3,1), which is
   the algebra of the Dirac gamma matrices. The anticommutativity
   {γ_μ, γ_ν} = 2η_{μν} should follow from the phase states'
   mutual relationships. Specifically: the anticommutativity
   should be the statement that two different phase-state
   traversals cannot be performed simultaneously (the system
   is in exactly one of {A, B, C, D} at each moment).

2. **Spinor structure.** SL(2,C) is the double cover of SO⁺(3,1).
   The double cover means spinors (half-integer spin) exist. In
   the phase-state picture, the double cover should correspond to
   the distinction between "entering D from A→D" and "entering D
   from B→D" — two different ways to reach the same dark state,
   related by a sign (the half-twist).

3. **CPT theorem.** Charge conjugation (C), parity (P), and time
   reversal (T) are discrete symmetries of the Lorentz group.
   In the phase-state picture:
   - T (time reversal) = traversing D in the opposite direction
   - P (parity) = swapping B ↔ C (which side is rational)
   - C (charge conjugation) = swapping the Klein bottle's
     two antiperiodic identifications
   CPT should hold because all three operations compose to the
   identity on the Klein bottle (the full symmetry group of the
   non-orientable surface).

## Status

**Derived.** The (3,1) signature follows from:
- Four phase states from {locked, unlocked}² (the 2×2 matrix)
- Exactly one dark state (both unlocked)
- Three observable states
- The dark state's contribution to the norm is negative
  (traversal costs, rather than gains, observable information)

The derivation uses:
- The Klein bottle topology (D19)
- The definition of "observable" (nonzero time-averaged coupling)
- The binary nature of mode-locking (in tongue or in gap)

No additional primitives needed. The signature is a consequence
of the same structure that gives d = 3, three generations, and
the N = 3 threshold.

---

## Proof chains

This derivation connects to all three proof chains as the
signature result:

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md) — closes the signature assumption in ADM (D13)
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md) — the D state is the measurement process
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — the (3,1) structure connects spatial (A,B,C) and temporal (D) sectors
