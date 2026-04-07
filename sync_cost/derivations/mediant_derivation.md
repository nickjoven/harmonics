# The Mediant Is Not an Axiom

## The challenge

The entire framework rests on the mediant (a+c)/(b+d) being the
primitive combining operation. Derivation 10 declared it a primitive.
Derivation 28's proof of Ω_Λ = 13/19 is conditional on this.

If the mediant is merely an axiom — a choice — then the framework
is one choice among many, and the predictions are coincidences that
follow from a lucky choice.

This derivation shows: the mediant is the UNIQUE operation satisfying
two physical properties of coupled oscillators. It is not chosen. It
is forced.

## Two physical properties

### Property 1: Betweenness

When two oscillators at frequencies ν₁ and ν₂ couple, the resulting
locked frequency ν lies between them:

    min(ν₁, ν₂) ≤ ν ≤ max(ν₁, ν₂)

This is not an assumption. It is energy conservation. A coupled
system cannot produce a frequency outside the range of its inputs
without an external energy source. The coupling redistributes
energy between the two oscillators; it does not create energy.

In terms of frequency ratios: if the two oscillators have winding
numbers a/b and c/d (with a/b < c/d), then the locked ratio ω
satisfies:

    a/b ≤ ω ≤ c/d

### Property 2: Minimality (stability)

Among all possible locked frequencies between ν₁ and ν₂, the system
locks to the one with the SMALLEST DENOMINATOR.

This is not an assumption. It is the Arnold tongue structure of
the circle map. The tongue width at rational p/q scales as:

    w(p/q, K) ~ (K/2)^q

The tongue width DECREASES exponentially with the denominator q.
A mode with smaller q has a wider tongue — it is stable over a
larger range of bare frequency and coupling. The coupled system
enters the widest available tongue first, because it is the first
one reached as coupling increases from zero.

The most stable lock is the simplest lock. The simplest fraction
between two given fractions (the one with the smallest denominator)
is the first to appear as coupling increases. This is not a principle
of economy or aesthetics — it is the topology of Arnold tongues.

## The theorem

**Theorem (Stern-Brocot, 1858/1860).** Let a/b and c/d be adjacent
fractions (|ad − bc| = 1). The unique fraction in the open interval
(a/b, c/d) with the smallest denominator is:

    (a + c) / (b + d)

the mediant.

**Proof sketch.** By the theory of continued fractions, the fraction
with the smallest denominator in any interval (α, β) of width
|β − α| = 1/(bd) (where b, d are the denominators of the endpoints)
has denominator b + d. Its numerator is a + c (forced by the
requirement that it lie in the interval and be irreducible). The
Farey adjacency condition |ad − bc| = 1 ensures that no fraction
with smaller denominator exists in the interval. □

(Full proof: Hardy & Wright, "An Introduction to the Theory of
Numbers," Chapter III; or Brocot's original construction.)

## The derivation

**Step 1.** Physical systems of coupled oscillators satisfy
betweenness (energy conservation) and minimality (Arnold tongue
stability).

**Step 2.** The Stern-Brocot theorem says: the unique operation
satisfying betweenness and minimality on adjacent rationals is
the mediant.

**Step 3.** Therefore the mediant is the unique combining operation
for coupled oscillator frequency ratios.

The mediant is not an axiom. It is a theorem about the ONLY
operation consistent with energy conservation and Arnold tongue
stability applied to frequency ratios.

## What this replaces

Derivation 10 listed four primitives:
1. Integers Z
2. Mediant (a+c)/(b+d)
3. Fixed-point x = f(x)
4. Parabola x² + μ = 0

With this derivation, primitive (2) is replaced by:

2'. **Coupled oscillators satisfy betweenness and minimality.**

The mediant is then a DERIVED operation — the unique one consistent
with (2'). The framework's primitives become:

1. Integers Z (counting)
2. Coupled oscillators with betweenness and minimality (→ mediant)
3. Fixed-point x = f(x) (self-reference)
4. Parabola x² + μ = 0 (bifurcation)

Primitive (2') is more physical and less algebraic than (2). It
refers to energy conservation and stability — properties that can
be tested experimentally — rather than to an algebraic operation
that must be taken on faith.

## The different shapes

Different combining operations on pairs (a, b) produce different
algebraic structures:

| Operation | Formula | Structure | Physical meaning |
|-----------|---------|-----------|-----------------|
| Complex multiplication | (a,b)·(c,d) = (ac−bd, ad+bc) | ℂ | Rotation + scaling |
| Quaternion multiplication | 4-component | ℍ | 3D rotation |
| Component-wise multiplication | (ac, bd) | Coordinate scaling | Independent axes |
| **Mediant (component-wise addition)** | **(a+c, b+d)** | **Stern-Brocot tree** | **Mode-locking** |

Each operation answers a different physical question:
- Complex multiplication: "what happens when you compose two
  rotations?" → phase composition
- Mediant: "what happens when two oscillators couple?" → frequency
  locking

The physical context determines the operation. For coupled
oscillators (the Kuramoto model, the framework's substrate), the
relevant question is mode-locking, not rotation. The mediant is
the answer to the mode-locking question. Complex multiplication
is the answer to the rotation question. They are different because
the physics is different.

The "shape" of each algebra:
- Complex numbers: the unit circle (S¹). Multiplication preserves
  the circle.
- Mediants: the Stern-Brocot tree. The mediant preserves Farey
  adjacency.

These are genuinely different topological structures. S¹ is a
smooth manifold. The Stern-Brocot tree is a discrete binary tree.
The framework uses the tree, not the circle, because the physical
process (synchronization) produces a tree of rational lockings,
not a smooth rotation.

## The chain, axiom-free

With the mediant derived from betweenness + minimality:

    Energy conservation + Arnold tongue stability
    → mediant is the unique combining operation (Stern-Brocot theorem)
    → Stern-Brocot tree is the configuration space (D10-D11)
    → Klein bottle selects {q₂=2, q₃=3} (D19)
    → Farey count |F₆| = 13 (number theory)
    → SO(2) invariance → (|F_n|, n) are the only scalars (D28 Step 0)
    → Mediant-consistent partition: C/(C+S) (D28 Steps 2-4)
    → Ω_Λ = 13/19 (D25)

No axioms beyond "coupled oscillators conserve energy and lock to
the most stable ratio." The rest is mathematics.

## Why the Stern-Brocot tree and not a continuum

### The continuum fails minimality

A continuous frequency space ℝ satisfies betweenness: given any
two reals, their average (or any convex combination) lies between
them. But ℝ does NOT satisfy minimality: between any two reals
there are uncountably many others, and no canonical "simplest" one
exists. The arithmetic mean, geometric mean, and harmonic mean are
all "between" but none is "simplest" because ℝ has no ordering by
complexity.

Minimality requires a DISCRETE ordering by denominator: p/q is
simpler than p'/q' when q < q'. This ordering is not imposed — it
is the stability ordering of the Arnold tongues. A mode with smaller
q has tongue width w ~ (K/2)^q — exponentially wider, therefore
exponentially more stable. The simplest fraction is the most
physically robust one.

The Stern-Brocot tree IS this ordering. It enumerates all rationals
by increasing denominator, with each mediant being the simplest
rational in its interval. No continuum structure has this property.

### Why not a different discretization

The Arnold tongue structure at rational p/q follows from Fourier
analysis of the coupling function. The Kuramoto coupling
sin(θ_j − θ_i) has a single Fourier harmonic. Its iterates
produce tongues at ALL rationals p/q, with width scaling as
(K/2)^q — ordered by denominator.

Any periodic, antisymmetric coupling function can be expanded in
a Fourier series. The fundamental mode (sin) dominates at weak
coupling. The tongue structure at all rationals, ordered by
denominator q, is universal — it does not depend on the specific
coupling function, only on its periodicity and antisymmetry.

A different discretization (powers of 2, decimals, algebraic
numbers) would not reproduce this tongue ordering because the
tongues occur at ALL rationals, not at a subset. The Stern-Brocot
tree is the unique enumeration that respects the tongue width
ordering.

### The universality argument

The result rests on three properties of the coupling:
1. **Periodicity** (phases are circular: θ ∈ S¹)
2. **Antisymmetry** (coupling is mutual: f(θ) = −f(−θ))
3. **Smoothness** (Fourier series converges)

Any coupling satisfying (1)-(3) produces Arnold tongues at all
rationals, ordered by denominator. The Stern-Brocot tree is the
configuration space of the resulting dynamics. No other structure
emerges.

If the coupling were not periodic (e.g., linear springs), there
would be no mode-locking and no rational structure. If it were not
antisymmetric, the coupling would not be mutual and the system
would not synchronize. If it were not smooth, the Fourier analysis
would fail.

The three properties (1)-(3) are the defining properties of
coupled oscillators on a circle. They are not choices — they are
the definition of the physical system. The Stern-Brocot tree is
their unique consequence.

## Status

**Derived.** The mediant is the unique operation satisfying
betweenness (energy conservation) and minimality (widest Arnold
tongue). The Stern-Brocot theorem (1858/1860) proves this.
The framework's primitive (2) is replaced by a physical property
(2') that is experimentally verifiable.

The Stern-Brocot tree is the unique configuration space arising from
coupled oscillators with periodic, antisymmetric, smooth coupling.
It is not a choice of discretization — it is the Arnold tongue
structure, which is universal for this class of dynamical systems.

The prediction Ω_Λ = 13/19 now rests on:
- Coupled oscillators conserve energy (testable)
- Coupled oscillators lock to the most stable ratio (testable,
  demonstrated in every synchronization experiment since Huygens)
- The Klein bottle topology (D18-D19, simulation-confirmed)
- Number theory (the Farey count, Euler totient)
- SO(2) invariance (the Kuramoto symmetry)

None of these are axioms in the sense of "assumed without
justification." They are physical properties and mathematical
theorems.

---

## Proof chains

This derivation is the starting proposition (P2) in both end-to-end
proof chains:

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md) — 8 propositions from the mediant to Einstein
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md) — the subcritical branch to Schrödinger + Born rule
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — cosmological parameters connecting both legs
