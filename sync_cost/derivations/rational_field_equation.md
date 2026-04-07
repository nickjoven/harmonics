# The Rational Field Equation

## Claim

The field equation of the synchronization framework is a
self-consistency condition on the Stern-Brocot tree, written in
exact rational arithmetic using the four primitives of Derivation 10.
The continuum (PDE) form is a limit, not the primary object. The
equation operates on rationals constructed by mediants because the
physical states it describes — mode-locked orbits — are rational.

## Part I: Why rational arithmetic is forced

### The alphabet constrains the equation

Derivation 10 established four irreducible primitives:

| Primitive | Operation |
|-----------|-----------|
| Integers Z | Counting |
| Mediant (a+c)/(b+d) | Constructing rationals |
| Fixed-point x = f(x) | Self-reference |
| Parabola x² + μ = 0 | Bifurcation |

Division (a/b as a real number) is not in the alphabet. It is
*derivable* — division is iterated mediant plus counting — but it
is not primitive. Writing equations in terms of a derived operation
when the primitive is available imports structure that isn't there:
the continuum, infinite precision, the completed reals.

This is not a philosophical preference. The cost function scan
(Derivation 4) showed what happens when you smooth over discrete
structure: wrong-sign running. The staircase has the right structure
because it's made of mediants, not decimals. The field equation must
preserve this.

### The staircase is the domain

The devil's staircase W(Ω, K) is the solution to the circle map's
dynamics. Its structure:

- **Plateaus** at every rational p/q: mode-locked states where the
  winding number is exactly p/q. These are the physical states —
  orbits with definite frequency ratios.
- **Gaps** at irrationals: quasiperiodic orbits with no definite
  frequency ratio. These are superpositions — states that have not
  resolved which attractor they belong to (Derivation 9).
- **Tongue boundaries**: saddle-node bifurcations where a locked
  state appears or disappears. These are measurements (Derivation 7).

The field equation describes the locked states. The locked states
are rational. Therefore the field equation operates on Q, indexed
by the Stern-Brocot tree.

The gaps are not states the equation describes — they are the
*absence* of description. An irrational winding number means the
system has not resolved its frequency. The field equation doesn't
need a value there; it needs the boundary conditions that the
neighboring rationals impose.

### Division versus mediant

Division a/b treats the rational as a point on the real line —
a position with infinite-precision coordinates. The mediant
(a+c)/(b+d) treats the rational as a *node in a tree* — defined
by its relationship to its neighbors.

The staircase talks in mediants:

    Given neighboring locked frequencies p₁/q₁ and p₂/q₂,
    the next frequency to lock (as coupling K increases) is
    the mediant (p₁+p₂)/(q₁+q₂).

This is the circle map's mode-locking rule: the mediant of two
adjacent Farey fractions is the next Arnold tongue to appear. The
Stern-Brocot tree enumerates the order of locking.

Division discards this tree structure. It gives you the value 3/8
but not the fact that 3/8 is the mediant of 1/3 and 2/5, which is
the fact that determines when and how 3/8 locks. The field equation
needs the tree, not the values.

---

## Part II: The self-consistency condition

### The loop

The synchronization framework's central claim (FRAMEWORK.md): the
cost functional applied self-consistently over the participation
set produces the coupling, the staircase, and the laws. The loop:

    Participation → Coupling → Staircase → Participation
         ↑                                       |
         └───────────────────────────────────────┘

At each node p/q in the Stern-Brocot tree:

1. **Participation** N(p/q): how many oscillators are locked to
   the rational frequency p/q. This is the tongue's "population."

2. **Coupling** K(p/q): the effective coupling at frequency p/q,
   determined by the mean field of all participants. More
   participants → stronger mean field → larger K.

3. **Tongue width** w(p/q, K): the range of bare frequencies Ω
   that lock to p/q at coupling K. Wider tongue → more oscillators
   captured → larger N.

The field equation is the fixed point of this loop.

### The equation on the tree

Let the Stern-Brocot tree T have nodes indexed by rationals p/q.
At each node, define:

    N(p/q)  = number of oscillators locked to p/q
    K(p/q)  = effective coupling at p/q
    w(p/q)  = tongue width at p/q under coupling K(p/q)
    g(Ω)    = bare frequency distribution

The self-consistency equations:

**Tongue width** (from circle map geometry):

    w(p/q, K) = 2(K/2)^q × h(p/q)

where h(p/q) encodes the tongue's shape, determined by the
specific rational (for the 0/1 tongue, h = 1/(πK) at small K;
for general p/q, h depends on the continued fraction expansion).

**Population** (oscillators captured by tongue p/q):

    N(p/q) = N_total × ∫_{tongue p/q} g(Ω) dΩ
           ≈ N_total × g(p/q) × w(p/q, K(p/q))

In exact arithmetic, this is not an integral but a sum over the
bare frequencies that fall within the tongue. At finite N_total,
the bare frequencies are themselves rational (finite system), and
the question is which tongue each bare frequency falls into.

**Coupling** (mean field from all participants):

    K(p/q) = K_0 × F[{N(r/s) : r/s ∈ T}]

where F is the mean-field functional — the coupling at node p/q
depends on the entire population distribution across the tree.
The specific form of F is the physical content:

- **Kuramoto (all-to-all)**: K(p/q) = K_0 × (1/N_total) × Σ N(r/s)
  (global mean field, K is the same at every node — this is the
  gravitational case, K = 1 at critical coupling)

- **Local coupling**: K(p/q) depends on N at neighboring nodes
  in the Stern-Brocot tree — the nodes connected by single mediant
  steps. This is the lattice case.

- **Hierarchical**: K(p/q) depends on N at ancestor and descendant
  nodes in the tree. This couples different scales.

**The fixed-point equation**:

    N(p/q) = N_total × g(p/q) × w(p/q, K_0 × F[N])

This is the field equation. It is a fixed-point equation (primitive 3)
on the Stern-Brocot tree (primitives 1 + 2), with tongue widths
determined by saddle-node geometry (primitive 4). All four primitives
and nothing else.

### The equation in explicit form

For the global mean-field case (Kuramoto, K uniform), define the
order parameter:

    r = (1/N_total) × Σ_{p/q ∈ T} N(p/q) × e^{2πi(p/q)}

The coupling is K = K_0 × |r|. The self-consistency condition
becomes:

    |r| = |Σ_{p/q} g(p/q) × w(p/q, K_0|r|) × e^{2πi(p/q)}|

This is one equation in one unknown (|r|), with the sum running
over the Stern-Brocot tree. At each node, the tongue width
w(p/q, K_0|r|) is computed from the circle map's saddle-node
geometry. The equation determines the critical coupling K_c (where
|r| first becomes nonzero) and the staircase structure above K_c.

This is the Kuramoto self-consistency equation, but evaluated on
the tree rather than integrated over a continuous g(ω). The
standard Kuramoto integral is the continuum limit.

---

## Part III: Properties of the rational equation

### Finite at every step

The Stern-Brocot tree truncated at depth d has 2^d - 1 nodes.
At finite depth, the field equation is a finite system of
algebraic equations in exact rational arithmetic. No truncation
errors. No floating-point artifacts. No discretization scheme
needed — the rationals *are* the grid.

The depth d corresponds to the maximum denominator q_max of
resolved mode-locking. At coupling K, tongues with q > q_max(K)
have width smaller than any bare frequency spacing — they are
unresolvable. The physical truncation depth is set by K:

    q_max(K) ≈ -ln(2) / ln(K/2)

At K = 1 (critical, gravitational): q_max → ∞ (all tongues filled).
At K < 1 (subcritical, quantum): q_max is finite. The effective
Hilbert space dimension is 2^{q_max} - 1.

### The continuum limit

Taking d → ∞ and N_total → ∞ simultaneously:

- The Stern-Brocot tree fills Q
- The sum over nodes becomes an integral
- The tongue widths become a continuous function of Ω
- The fixed-point equation becomes the standard Kuramoto
  self-consistency integral

The PDE form of the field equation (if one exists) lives in this
limit. It is a derived object, not the primary equation.

### The Fibonacci backbone

The path from the root of the Stern-Brocot tree to 1/φ passes
through the Fibonacci convergents:

    0/1 → 1/1 → 1/2 → 2/3 → 3/5 → 5/8 → 8/13 → ...

These are the nodes that control the staircase's self-similar
structure at 1/φ (Derivation 4). The field equation restricted to
this path is a one-dimensional recurrence:

    N(F_n/F_{n+1}) = N_total × g(F_n/F_{n+1}) ×
                     w(F_n/F_{n+1}, K_0 × F[N])

with the φ² scaling relating successive levels:

    w(F_{n+1}/F_{n+2}) = φ^{-2} × w(F_n/F_{n+1}) × (1 + O(K))

This recurrence along the Fibonacci backbone IS the spectral tilt
equation. The 0.0365 levels per e-fold (Derivation 4) is the rate
at which the field equation's solution decays along this path.

### The Born rule from the fixed point

At each node p/q, the tongue width w(p/q, K) is proportional to
Δθ² (Derivation 1, saddle-node geometry). The population N(p/q)
is proportional to w, therefore proportional to Δθ². The fraction
of oscillators at p/q is:

    P(p/q) = N(p/q) / N_total ∝ Δθ(p/q)² = |ψ(p/q)|²

The Born rule is the population distribution at the fixed point
of the field equation. Not a postulate applied to the solution —
a property of the solution itself.

---

## Part IV: The three regimes

The field equation has three regimes determined by K:

### K = 1 (critical coupling): Gravity

All tongues filled. Every orbit locked. The staircase has measure 1.
The field equation's solution is the complete staircase — the
population distribution across all rationals, weighted by tongue
width. The order parameter |r| = 1.

The RAR (Derivation 9) is the field equation evaluated at a single
orbit: the self-consistent coupling between one oscillator
(the orbit) and the mean field (H). The interpolating function
g_obs(g_bar) is the local fixed point.

### K < 1 (subcritical): Quantum mechanics

Gaps exist. The golden ratio gap (at 1/φ) is the last to close
(Derivation 4). Oscillators in the gaps have quasiperiodic orbits
— no definite winding number. These are superpositions.

The field equation at K < 1 has a solution on a *subtree* of
Stern-Brocot: only the tongues that are open at coupling K. The
unlocked oscillators (in the gaps) are not described by the
equation — they are the quantum states that have not collapsed.

Measurement is increasing K locally past the critical value at a
specific rational, collapsing a gap into a tongue. The Born rule
gives the probability of landing at each rational when the gap
closes.

### K → 0 (weak coupling): Free particles

No tongues. No locking. All orbits quasiperiodic. The staircase
is a straight line W = Ω. The field equation's solution is trivial:
N(p/q) = 0 for all p/q. No structure.

This is the non-interacting limit. The framework correctly produces
"no physics" when there is no coupling.

---

## Part V: Connection to known field equations

### Kuramoto → Synchronization field equation

The standard Kuramoto model with N oscillators:

    dθ_i/dt = ω_i + (K/N) Σ_j sin(θ_j - θ_i)

has the self-consistency equation for the order parameter:

    r = ∫ g(ω) × e^{iψ} / (1 + (ω-Ω)²/(Kr)²) dω

Our rational field equation is this, but:
- The integral is a sum over Stern-Brocot nodes
- The Lorentzian kernel 1/(1 + ...) is replaced by the exact
  tongue width function w(p/q, K)
- The distribution g(ω) is evaluated at rationals, not reals

The continuum limit recovers standard Kuramoto.

### Einstein equations as K = 1 limit

At critical coupling, the field equation describes the fully locked
state. The proslambenomenos mapping (Kuramoto ↔ ADM) identifies:

    Kuramoto coupling K ↔ Gravitational coupling (via G)
    Order parameter r ↔ Lapse function N
    Phase θ_i ↔ ADM spatial metric h_ij
    Mean field Ω ↔ Extrinsic curvature K_ij

The rational field equation at K = 1, in the continuum limit,
should reduce to the ADM evolution equations. This is the
"dynamical equivalence" open question from proslambenomenos §7.1
— now posed precisely: show that the continuum limit of the
Stern-Brocot fixed-point equation at K = 1, under the ADM
identification, reproduces the Einstein field equations.

### Schrödinger equation as linearized K < 1 limit

At subcritical coupling, linearizing the field equation around the
trivial solution (N = 0, no locking) gives the evolution of small
perturbations in the gap. These perturbations are the wavefunctions
of unlocked oscillators.

The linearized equation, in the continuum limit, should be the
Schrödinger equation. The potential V(x) enters as the spatial
variation of the coupling K(x). The mass enters as the tongue's
sensitivity to coupling (the q-dependent width scaling).

---

## Part VI: Open questions

1. **Compute the mean-field functional F explicitly.** For the
   gravitational case (K = 1, all-to-all), F is the Kuramoto
   order parameter. For local coupling (lattice), F depends on
   the Stern-Brocot tree metric. What is the correct F for
   intermediate cases?

2. **The continuum limit.** Show that the Stern-Brocot fixed-point
   equation, at K = 1, in the limit d → ∞ and N → ∞, reduces to
   the Einstein field equations under the ADM identification. This
   would close the dynamical equivalence question.

3. **The linearized limit.** Show that the Stern-Brocot fixed-point
   equation, at K < 1, linearized around N = 0, in the continuum
   limit, reduces to the Schrödinger equation. This would close the
   "QM as small-ε limit" claim in Derivation 10.

4. **Numerical verification.** Solve the rational field equation on
   the Stern-Brocot tree truncated at depth d = 10 (1023 nodes) with
   exact rational arithmetic. Compare the population distribution
   N(p/q) against the numerically computed staircase. If they match,
   the field equation is verified without floating point.

5. **The time displacement budget.** The tongue uncertainty
   τ × Δθ = const, read as a displacement budget (Δθ fixed, τ bounded),
   should emerge from the field equation's Floquet analysis at each
   node. The budget is the maximum temporal displacement before
   resynchronization, bounded by the tongue width in the time
   direction. Derive this from the rational field equation's
   linearized stability at each Stern-Brocot node.

## Status

**Established**:
- Exact rational arithmetic forced by the primitive alphabet
  (mediants are primitive, division is derived)
- Self-consistency condition written on Stern-Brocot tree
- Fixed-point equation: N(p/q) = N_total × g(p/q) × w(p/q, K₀F[N])
- Born rule as population distribution at the fixed point
- Three regimes (K = 1 gravity, K < 1 quantum, K → 0 free)
- Connection to Kuramoto self-consistency in continuum limit
- Fibonacci backbone recovers spectral tilt as recurrence

**Open**:
- Continuum limit → Einstein equations (the big one)
- Linearized limit → Schrödinger equation
- Numerical verification on truncated tree
- Explicit mean-field functional for intermediate coupling
- Time displacement budget from Floquet analysis
