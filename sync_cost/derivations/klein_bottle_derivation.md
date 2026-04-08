# The Klein Bottle from Self-Consistency

## Claim

The Klein bottle is not assumed. It is the unique compact surface
compatible with the four primitives, the phase-state structure, and
the arrow of time. The torus and real projective plane are both
excluded by self-consistency arguments.

---

## Part I: Why a surface at all

### Why exactly two S¹ factors

**Lemma (two factors from the mediant).** The configuration surface
has exactly two periodic directions because the mediant operates on
2-component objects (fractions p/q), generating 2×2 matrices.

**Proof.** The four primitives give S¹ (integers + fixed point, D10
Lemma 1). On S¹, modes are indexed by rational winding numbers p/q.
The mediant (a+c)/(b+d) is the fundamental operation that builds the
configuration space (D10 Part I.3, D29).

A fraction p/q is a 2-component object: numerator p and denominator q.
The mediant of a/b and c/d is the column sum of:

    M = ((a, c), (b, d))    ∈ SL(2, Z)    (Farey adjacency: |ad-bc|=1)

The left and right mediant steps are:

    L = ((1, 0), (1, 1)),   R = ((1, 1), (0, 1))

These generate SL(2, Z) (Stern 1858). The "2" in SL(2) is not a choice
— it is the number of components in a fraction. A fraction is
irreducibly binary: a numerator and a denominator, related by the
ratio operation. You cannot represent p/q faithfully as a 1-component
object (scalars lose the distinction between 2/4 and 1/2 in the tree),
and a 3-component representation of a 2-component object carries
redundancy that reduces back to 2.

The configuration of a mode on the circle is therefore specified by a
point in a space acted on by SL(2, Z). The fundamental domain of this
action is a quotient of the space of 2-vectors — which has 2 real
dimensions. Each dimension is periodic (the phase lives on S¹). The
configuration surface is therefore S¹ × S¹ / (identifications).

More concretely: the self-consistency condition (the mean field
determines the locking that produces the mean field) requires **two**
independent phase variables:

- **The oscillator phase** θ ∈ S¹: where the mode sits.
- **The mean-field phase** ψ ∈ S¹: the collective phase that couples
  back to the oscillator.

These are the two components of the fraction made dynamical. The
numerator indexes the winding (how many times the phase wraps — the
oscillator's state θ). The denominator indexes the period (how many
iterations before return — the coupling structure ψ). The coupling
term sin(ψ − θ) in the Kuramoto equation is a function of their
difference. The self-consistency condition r e^{iψ} = ⟨e^{iθ}⟩ relates
them but does not identify them.

Two independent S¹ variables span a 2-dimensional surface: the quotient
of [0,1] × [0,1] under boundary identifications. The question is:
**which identifications?** □

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

**RP² kills continuous momenta.** The first homology H₁(RP²; Z) = Z₂
has no free part. The free part of H₁ indexes continuous quantum numbers
(momenta, wavevectors). Without it, there are no propagating wave modes
— only discrete topological sectors. A framework with no propagating
modes cannot describe fields, particles, or dynamics. This excludes RP²
independently of the bifurcation argument.

---

## Part IV: Excluding T² — fermions and the arrow of time

### The homological argument (primary)

The first homology groups of the three candidate surfaces are:

    H₁(T²; Z)  = Z ⊕ Z       (free rank 2, no torsion)
    H₁(K²; Z)  = Z ⊕ Z₂      (free rank 1, Z₂ torsion)
    H₁(RP²; Z) = Z₂           (free rank 0, Z₂ torsion)

**Fermions require Z₂ torsion in H₁.** The antisymmetry of the
fermionic wavefunction under particle exchange (ψ(x₁,x₂) = −ψ(x₂,x₁))
requires a topological operation that produces a −1 sign. This is a
representation of Z₂: the trivial representation gives +1 (bosons),
the sign representation gives −1 (fermions). If H₁ has no Z₂ torsion,
there is no topological mechanism to produce the −1. All modes transform
trivially under all loop traversals. Only bosonic statistics are
possible.

**The torus has no torsion.** H₁(T²; Z) = Z ⊕ Z. The group Z has no
elements of finite order. There is no loop on the torus whose single
traversal produces −1 while double traversal produces +1. Every
representation of π₁(T²) = Z × Z assigns continuous phases (not signs)
to the generators. All wavenumbers are integers. No half-integer
wavenumbers exist. No spinor representations. No fermions.

**The Klein bottle has Z₂ torsion.** H₁(K²; Z) = Z ⊕ Z₂. The Z₂
factor comes from the antiperiodic identification: traversing the
x-loop once gives θ → θ + π (a −1 sign on the wavefunction), while
traversing twice gives θ → θ + 2π = θ (back to +1). Functions on K²
decompose into two classes:

- Even: f(θ + π) = f(θ). Integer wavenumbers. Representations of
  SO(3,1). **Bosons.**
- Odd: f(θ + π) = −f(θ). Half-integer wavenumbers. Representations
  of the double cover Spin(3,1) that do not descend to SO(3,1).
  **Fermions (spinors).**

The Pauli exclusion principle follows directly: two identical fermions
at the same point require ψ(x,x) = −ψ(x,x), hence ψ(x,x) = 0.
The −1 is a topological fact about the Klein bottle, not an additional
postulate.

**Therefore: the existence of fermions excludes the torus.**

### The arrow-of-time argument (secondary, independent)

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

**Theorem.** Let Σ be a compact connected surface without boundary,
obtained as a quotient of [0,L₁] × [0,L₂] under boundary
identifications. Suppose:

1. **Periodicity**: both raw variables live on S¹ (from P1 + P3).
2. **Bifurcation**: the dynamics on Σ admit codimension-1 saddle-node
   bifurcations (from P4, the parabola).
3. **Fermions**: the surface must support both bosonic and fermionic
   representations (Z₂ torsion in H₁ with nonzero free rank).
4. **Self-consistency**: the mean field determines the locking that
   produces the mean field (P3, the fixed-point condition).

Then Σ ≅ K² (the Klein bottle).

### Proof

Condition (1) requires Σ to be a quotient of S¹ × S¹ — a torus or
a quotient of a torus. The candidates are T², K², RP².

Condition (2) excludes RP²: both directions antiperiodic identifies
the two roots of x² + μ = 0, destroying the saddle-node structure
(Part III above). Independently, H₁(RP²) = Z₂ has no free part,
so no continuous momenta exist (Part III).

Condition (3) excludes T²: H₁(T²) = Z ⊕ Z has no Z₂ torsion, so
no fermionic representations are possible (Part IV). Only bosonic
statistics exist on a torus.

Conditions (1)–(3) together leave only K². Its homology
H₁(K²) = Z ⊕ Z₂ provides both continuous momenta (free part Z)
and the boson-fermion distinction (torsion part Z₂).

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
| Non-orientability | Postulated | **Derived**: forced by fermion existence (Z₂ torsion) |
| Why not torus | Not addressed | **Excluded**: H₁(T²) has no torsion → no fermions |
| Why not RP² | Not addressed | **Excluded**: kills bifurcation + no free momenta |
| XOR filter | Derived from K² (D19) | Now grounded: K² itself is derived |
| Boson-fermion distinction | Not addressed | **Derived**: even/odd reps of Klein bottle Z₂ |
| Spin-statistics connection | External postulate | **Derived**: Z₂ torsion in H₁(K²) |

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

## Part VIII: The rational observer picture

The Klein bottle populated by locked modes at rational winding numbers
gives a concrete physical picture of the framework.

### The observers

Each rational p/q on the Stern-Brocot tree is an observer: a mode
locked at winding number p/q, advancing forward through the Klein
bottle's antiperiodic direction. The observer at p/q:

- Has accumulated phase offset (p/q) × π relative to the reference.
- Completes p full half-twists every q periods of the reference clock.
- After q reference periods: returns to original phase if p is even
  (bosonic traversal), or returns twisted by π if p is odd (fermionic
  traversal — needs 2q periods for true return).

The even/odd distinction in p is the XOR constraint playing out in
time. Observers with odd p see the double cover; they are spinors.

### The communication network

Two observers can sustain nonzero time-averaged coupling if and only
if their frequency ratio is rational. Specifically:

    ⟨sin(ω₁t − ω₂t)⟩_T → { nonzero,  ω₁/ω₂ ∈ Q
                             { 0,        ω₁/ω₂ ∉ Q

(For irrational ratio, the phase difference sweeps S¹ ergodically
and the average vanishes.) The rational observers form a discrete
communication network embedded in the continuous surface: the
Stern-Brocot tree.

**Adjacency.** Two observers at p₁/q₁ and p₂/q₂ are nearest neighbors
in this network iff |p₁q₂ − p₂q₁| = 1 (Farey adjacency). This is
the det = ±1 condition of SL(2,Z). The communication graph is the
Farey graph: the 1-skeleton of the ideal triangulation of H².

### The hierarchy

Observers with small denominator q have wide Arnold tongues (strong
coupling, cheap to maintain). Observers with large q have narrow
tongues (weak coupling, expensive). The hierarchy:

| Denominator | Tongue width | Role | Physical |
|-------------|-------------|------|----------|
| q = 1 | O(1) | Fundamental | Ground state / vacuum |
| q = 2 | O(K²) | First sector | SU(2) / weak modes |
| q = 3 | O(K³) | Second sector | SU(3) / strong modes |
| q = 5 | O(K⁵) | Mediants of 2,3 | Interaction modes |
| q large | O(K^q) | High-energy | Resolved only at high K |
| q → ∞ | 0 | Irrational gap | Dark sector (Ω_Λ) |

At coupling K < 1, only finitely many observers exist (finitely many
tongues open). As K → 1, more observers "turn on" at successively
larger q. At K = 1, all rationals are present — the tree is complete,
the observers fill the surface, and the discrete network becomes
the continuous group SL(2,R).

### The self-referential loop

The observers collectively determine the mean field:

    r e^{iψ} = (1/N) Σ_j e^{iθ_j}

The mean field determines the tongue widths (via the coupling
K_eff = K|r|), which determines which observers can sustain
themselves (only those with tongues wide enough to survive at
current K_eff). The fixed point of this loop is the rational field
equation (D11):

    N(p/q) = N_total × g(p/q) × w(p/q, K₀ × F[N])

This is the self-consistency condition (P3) instantiated: the
population of observers at each rational determines the field that
determines the population. The universe is the fixed point.

### What the dark sector is

Irrational positions on the Klein bottle — the gaps between Arnold
tongues — host no observers. No locked mode, no definite phase, no
communication with the rational network. These positions contribute
to the total phase space (and hence to the energy budget) but carry
no information.

The dark energy fraction Ω_Λ = (11 + 2w*)/(16 + 3w*) = 0.6847 is
the fraction of the Klein bottle's phase space that is dark: the gap
measure at the self-consistent coupling K*.

The boundary modes (q = 6, at fractional weight w* = 0.83) are
observers in the process of turning on — partially locked, partially
dark. They sit at the edge of the communication network, able to
sustain coupling most but not all of the time.

### Walking backwards is CPT

An observer attempting to traverse the antiperiodic direction in
reverse encounters: θ → θ − π ≡ θ + π (mod 2π). On S¹, backward
traversal produces the same half-twist as forward traversal. The
Klein bottle does not distinguish forward from backward along the
antiperiodic loop — this is its non-orientability.

The only meaningful "reversal" is the full CPT operation:
- **C** (charge conjugation): swap the Klein bottle's two XOR sectors
  (q₂ ↔ q₃, coupling sign flip)
- **P** (parity): reflect the periodic direction (y → L₂ − y)
- **T** (time reversal): reverse the antiperiodic direction

The compound CPT is a symmetry of the Klein bottle (it maps the
surface to itself). The individual operations C, P, T are not — each
one alone produces a configuration inconsistent with the boundary
conditions. This is the CPT theorem derived from the surface topology.

### The two S¹ factors, physically

The two S¹ variables have distinct physical characters:

- **θ (oscillator phase)**: where the observer sits on S¹. This is the
  periodic direction of the Klein bottle — the spatial variable. It has
  no preferred orientation (y → L₂ − y is a symmetry of the periodic
  BC). This is why space is isotropic.

- **ψ (mean-field phase)**: the collective phase that couples back.
  This is the antiperiodic direction — the temporal variable. It has a
  local arrow (dissipative convergence toward locking) but no global
  orientation (non-orientability). This is why time has a local arrow
  but CPT is a global symmetry.

The two components of a fraction (p and q) become the two components
of spacetime (space and time), distinguished by the Klein bottle's
topology: the numerator p (winding count) maps to the spatial
structure, the denominator q (period) maps to the temporal structure.
The asymmetry between them — one periodic, one antiperiodic — is the
asymmetry between space and time.

---

## Status

**Derived.** The Klein bottle is the unique compact surface built from
the mediant's 2-vector structure, satisfying:

1. Bifurcation preservation (excludes RP²)
2. Fermionic representations (excludes T²)
3. Continuous momenta (excludes RP²)

The argument has three layers of increasing strength:

- **Topological** (primary): H₁(K²) = Z ⊕ Z₂ is the unique homology
  among {T², K², RP²} with both free and torsion parts. Fermions
  require torsion; propagating modes require a free generator.

- **Dynamical** (secondary): the arrow of time from rank-1 Fréchet
  derivative (D46) independently requires non-orientability.

- **Self-consistency** (tertiary): the XOR filter on K² produces the
  correct mode count (12.66 effective modes, Ω_Λ = 0.6847); no XOR
  filter on T² gives a completely different — and excluded — spectrum.

The two-S¹ structure is closed: fractions are irreducibly binary
(numerator, denominator), the mediant operates on 2-vectors in
SL(2,Z), and the configuration surface is the 2-dimensional quotient
of this action. One S¹ per component.

## References

- D10: minimum_alphabet.md (four primitives)
- D14: three_dimensions.md (mediant → SL(2,Z) → SL(2,R))
- D19: xor_derivation.md (XOR filter from Klein bottle BCs)
- D32: minkowski_signature.md (dark state, (3,1) signature)
- D46: rank1_temporal_causation.md (arrow of time from rank-1)
