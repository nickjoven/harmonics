# The Klein Bottle from Self-Consistency

## Claim

The Klein bottle is not assumed. It is the unique compact surface
compatible with the four primitives, the phase-state structure, and
the arrow of time. The torus and real projective plane are both
excluded by self-consistency arguments.

---

## Part I: Why a surface at all

### From S¹ to S¹ × S¹

The four primitives give:

1. **Integers + fixed point → S¹** (Lemma 1, D10). A period-q orbit
   satisfies f^q(x) = x and f^q(x) = x + p, so p ≡ 0 mod 1 and
   R/Z = S¹.

2. **Mediant operates on pairs.** A fraction p/q has two components
   (numerator, denominator). The mediant (a+c)/(b+d) combines two
   fractions. The Stern-Brocot tree is the Cayley graph of the free
   monoid on L, R — both 2×2 matrices in SL(2,Z).

The configuration of a single mode is specified by a fraction p/q on
S¹. But the self-consistency condition (the mean field determines the
locking that produces the mean field) requires **two** independent
phase variables:

- **The oscillator phase** θ: where the mode sits on S¹.
- **The boundary/coupling phase** ψ: the mean-field phase that couples
  back to the oscillator.

The coupling term sin(ψ − θ) in the Kuramoto equation is a function of
the difference between these two phases. The self-consistency condition
r e^{iψ} = ⟨e^{iθ}⟩ relates them but does not identify them — they are
distinct degrees of freedom.

Two independent S¹ variables span a 2-dimensional surface. The surface
is a quotient of [0,1] × [0,1] under boundary identifications. The
question is: **which identifications?**

### Why compact and without boundary

Compactness follows from S¹ being compact (Lemma 1). The surface is a
quotient of a compact set under continuous identifications, hence compact.
No boundary: the identifications glue all edges, because each S¹ is
periodic (no endpoints).

---

## Part II: Three candidate surfaces

From a fundamental domain [0,L₁] × [0,L₂], the closed compact surfaces
without boundary constructable from edge identifications are:

1. **Torus T²**: both directions periodic.
   - (x + L₁, y) ~ (x, y)
   - (x, y + L₂) ~ (x, y)

2. **Klein bottle K²**: one direction antiperiodic with reflection.
   - (x + L₁, y) ~ (x, L₂ − y) with a half-twist (θ → θ + π)
   - (x, y + L₂) ~ (x, y)

3. **Real projective plane RP²**: both directions antiperiodic.
   - (x + L₁, y) ~ (x, L₂ − y) with half-twist
   - (x, y + L₂) ~ (L₁ − x, y) with half-twist

(The sphere S² cannot be obtained from rectangle identifications. Higher-
genus surfaces require additional handles, which have no motivation from
the two-S¹ structure.)

---

## Part III: Excluding RP² — the parabola has two roots, not one

RP² is the quotient of S² by the antipodal map z → −z. It requires
antiperiodic identification in BOTH directions. In the Kuramoto
framework, this means both the oscillator phase θ and the mean-field
phase ψ undergo half-twists at their respective boundaries.

The parabola (P4: x² + μ = 0) has **two** roots x = ±√(−μ) when
μ < 0 (the tongue-interior regime). At every tongue boundary, there is
one stable node and one unstable node. The two roots are related by a
sign flip: the stable node at +√(−μ) and the unstable at −√(−μ).

On RP², both directions carry half-twists. A mode traversing both
directions experiences two sign flips: (−1) × (−1) = +1. The double
twist returns to the original sign. This means the two roots of the
parabola are identified — the stable and unstable nodes become the
same point. But this destroys the bifurcation structure: a saddle-node
requires two distinct fixed points (one stable, one unstable). If
they're identified, there is no bifurcation, no tongue boundary, no
Born rule, no mode-locking.

**RP² kills the parabola.** The codimension-1 bifurcation (P4) requires
that the two roots remain distinct. This is compatible with at most one
antiperiodic direction — not two.

---

## Part IV: Excluding T² — the arrow of time

### The torus is time-reversible

On the torus, both directions are periodic. The identification
(x + L₁, y) ~ (x, y) preserves orientation: traversing the x-loop
returns the observer to the same state with no sign change, no
reflection, no twist.

The dynamics on a torus are time-reversible in the following sense:
the boundary conditions do not distinguish "forward" from "backward"
traversal of either loop. If θ(x, y) is a solution, then θ(L₁ − x, y)
is also a solution (the x-loop is traversed in reverse). Similarly for
the y-direction. The torus treats both directions symmetrically and
both traversal orientations equivalently.

### Dissipative dynamics break time-reversal

The Kuramoto equation with K > 0 is dissipative:

    ∂θ/∂t = ω + Kr sin(ψ − θ)

The coupling term Kr sin(ψ − θ) drives θ toward ψ (when sin > 0) and
never drives it away on average. This is an arrow: the system converges
toward the locked state, not away from it. The time-reversed dynamics
(ψ driven away from θ) are not physical solutions of the same equation.

More precisely (D46, rank-1 temporal causation): the Fréchet derivative
of the Kuramoto map U at the synchronized state has rank 1. The kernel
ker(DU) is the "past" (information that is lost), the image im(DU) is
the "future" (information that is preserved). The rank-1 factorization
is the arrow of time.

### The dark state is directional

From D32 (Minkowski signature): the dark state D is the unique
all-irrational phase state. Traversing D costs observable norm —
it contributes −c²dt² to the metric. The minus sign means D has a
preferred direction: traversal toward the future (convergence) is
physical; traversal toward the past (divergence) is not.

On a torus, traversing either loop in either direction is equivalent.
There is no "dark direction." The torus can only produce signature
(2,0) on the surface — both directions contribute positively to the
norm. A torus-based framework produces Euclidean signature, not
Lorentzian.

### The Klein bottle encodes the arrow

On the Klein bottle, the antiperiodic direction (x-loop) has a
half-twist: θ → θ + π upon traversal. This twist:

1. **Reverses the coupling sign**: sin(ψ − θ − π) = −sin(ψ − θ).
   The attractive coupling becomes repulsive upon traversal. The
   observer who has traversed the loop sees the dynamics "running
   backward" — the arrow of time has flipped.

2. **Reflects the y-coordinate**: y → L₂ − y. The observer's
   spatial reference frame is mirrored upon traversal.

3. **Cannot be undone by a continuous deformation**: the Klein
   bottle is non-orientable, so there is no way to consistently
   define "forward" and "backward" globally. The arrow of time is
   a local phenomenon (each observer has a definite forward direction)
   that cannot be extended to a global orientation.

This is exactly the structure of time in physics:
- Locally, time has a direction (entropy increases, wavefunctions
  collapse, the Born rule selects outcomes).
- Globally, time's direction cannot be defined (CPT theorem: the laws
  of physics are invariant under simultaneous reversal of charge,
  parity, and time).

The Klein bottle is the unique surface where:
- One direction is periodic (spatial: no preferred orientation)
- One direction is antiperiodic (temporal: local arrow, global
  non-orientability)
- The two are coupled by a reflection (y → L₂ − y) that encodes
  the correlation between spatial parity and temporal direction

---

## Part V: The self-consistency argument

### Statement

**Theorem (unproven, conjectured).** Let Σ be a compact connected
surface without boundary, obtained as a quotient of [0,L₁] × [0,L₂]
under boundary identifications. Suppose:

1. **Periodicity**: both raw variables live on S¹ (from P1 + P3).
2. **Bifurcation**: the dynamics on Σ admit codimension-1 saddle-node
   bifurcations (from P4, the parabola).
3. **Dissipation**: the dynamics have a preferred direction (arrow of
   time from the rank-1 structure of the Kuramoto map).
4. **Self-consistency**: the mean field determines the locking that
   produces the mean field (P3, the fixed-point condition).

Then Σ ≅ K² (the Klein bottle).

### Proof sketch

Condition (1) requires Σ to be a quotient of S¹ × S¹ — a torus or
a quotient of a torus. The candidates are T², K², RP².

Condition (2) excludes RP²: both directions antiperiodic identifies
the two roots of x² + μ = 0, destroying the saddle-node structure
(Part III above).

Condition (3) excludes T²: the torus is orientable, so both directions
are equivalent and neither carries a preferred arrow. The dissipative
dynamics require one direction to be distinguished (the "temporal"
direction where convergence occurs). On the Klein bottle, the
antiperiodic direction carries the arrow through the coupling-sign
reversal upon traversal.

Conditions (1)–(3) together leave only K².

Condition (4) provides the additional check: the self-consistency
equation on K² has the right fixed-point structure (4 surviving
modes from the XOR filter, with the self-consistent boundary weight
w* producing Ω_Λ = 0.6847). On T², the self-consistency equation
would have no XOR filter (all mode pairs allowed), producing a
completely different — and observationally excluded — mode count.

---

## Part VI: What this derivation closes

| Element | Before | After |
|---------|--------|-------|
| Klein bottle topology | **Assumed** (D19) | **Derived**: unique surface from (1)–(3) |
| Non-orientability | Postulated | **Derived**: forced by arrow of time |
| Why not torus | Not addressed | **Excluded**: no dark direction, wrong signature |
| Why not RP² | Not addressed | **Excluded**: kills bifurcation structure |
| XOR filter | Derived from K² (D19) | Now grounded: K² itself is derived |

---

## Part VII: Connection to fermions

The Klein bottle's antiperiodic identification θ → θ + π upon
traversal of the x-loop is a Z₂ action on the phase. This Z₂
naturally divides representations into:

- **Even** (bosonic): functions f with f(θ + π) = f(θ). These are
  periodic under the half-twist. They correspond to integer-spin
  representations of the double cover.

- **Odd** (fermionic): functions f with f(θ + π) = −f(θ). These are
  antiperiodic under the half-twist. They correspond to half-integer-
  spin representations.

The half-twist IS the spin-statistics connection:
- The antiperiodic boundary condition forces half-integer wavenumbers
  (m = k + 1/2) in the x-direction (proven in D19, Section 3.4).
- Half-integer wavenumbers correspond to spinor representations
  (representations of the double cover SL(2,C) that do not descend
  to SO(3,1)).
- Spinors obey Fermi statistics because exchanging two identical
  spinors at the same point requires traversing the antiperiodic loop
  twice, accumulating phase 2π — but on the Klein bottle, this returns
  with a sign (−1)² = +1 for the pair, while a single traversal gives
  −1. The single-particle minus sign is the Pauli exclusion principle.

This connects Item 1 (Klein bottle) to Item 2 (fermions): the same
non-orientability that produces the dark state, the Lorentzian
signature, and the XOR filter also produces the boson-fermion
distinction. Fermions are the odd sector of the Klein bottle's Z₂.

---

## Status

**Conjectured.** The individual exclusion arguments (RP² by bifurcation,
T² by arrow of time) are clear. The synthesis into a uniqueness theorem
(conditions 1–4 ⇒ K²) needs formalization.

The weakest point is the exclusion of the torus: "the torus has no dark
direction" is physically compelling but needs a sharper mathematical
statement. Specifically: prove that dissipative Kuramoto dynamics on T²
cannot produce a (3,1) signature from phase-state observability, while
the same dynamics on K² necessarily do.

## References

- D10: minimum_alphabet.md (four primitives)
- D19: xor_derivation.md (XOR filter from Klein bottle BCs)
- D32: minkowski_signature.md (dark state, (3,1) signature)
- D46: rank1_temporal_causation.md (arrow of time from rank-1)
