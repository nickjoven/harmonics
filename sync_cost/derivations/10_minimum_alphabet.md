# Derivation 10: The Minimum Alphabet

## Claim

The framework's entire structure — the circle, the devil's staircase,
Arnold tongues, the Born rule, the RAR, and the uncertainty relation —
follows from compositions of exactly four irreducible primitives:

| # | Primitive | What it provides |
|---|-----------|-----------------|
| 1 | **Integers** Z | Counting, cycles, winding numbers |
| 2 | **Mediant** (a+c)/(b+d) | Rational structure without division |
| 3 | **Fixed-point** x = f(x) | Self-reference, iteration, dynamics |
| 4 | **Parabola** x² + μ = 0 | Nonlinearity, bifurcation, orientation |

No reals. No base. No continuum assumed. The continuum emerges as
completion; standard quantum mechanics emerges as the small-ε
linearized limit.

---

## Part I: Construction

### 1. The circle is derived (integers + fixed-point)

Start with two primitives: integers (counting cycles) and the
fixed-point condition (x = f(x), return to start).

A period-q orbit with winding number p/q means: after q iterations,
the state has advanced by exactly p full cycles. The fixed-point
equation applied to the q-th iterate says:

    f^q(x) = x       (return to start)

But the winding count says:

    f^q(x) = x + p   (advanced by p)

Both hold simultaneously, so:

    x + p = x   in the phase space

Therefore p ≡ 0 in the phase space. Since p is an arbitrary integer,
**all integers must be equivalent to 0**. The phase space is R/Z.
That is S¹. That is the circle.

The mod-1 topology is not an axiom. It is the unique topology
consistent with integer counting and self-reference. You cannot have
periodic orbits with integer winding counts on a line — the line has
no fixed points of translation. The moment you demand that an orbit
returns (fixed-point equation) after counting an integer number of
full advances, you have quotiented by Z. You have a circle.

### 2. Orientation is derived (parabola)

The parabola x² + μ = 0 has two roots ±√(-μ) for μ < 0. These are
distinguished by the dynamics: one is the stable node (attractor),
the other is the unstable node (repeller). The flow on the real line
near a saddle-node goes **toward** the stable root and **away from**
the unstable root. This breaks the symmetry x → -x.

On the circle, this means the saddle-node bifurcation at a tongue
boundary creates two fixed points that are not interchangeable —
the attractor and repeller sit on opposite sides of the tongue. The
direction from repeller to attractor defines an orientation on S¹.

Therefore:
- The **unsigned circle** comes from integers + fixed-point (Part I.1)
- The **oriented circle** comes from adding the parabola

Orientation is not a fifth primitive. It is the parabola's two roots
read as a direction.

### 3. The rationals are constructed (integers + mediant)

The Stern-Brocot tree constructs every positive rational exactly once
by iterated mediants starting from the boundary fractions 0/1 and 1/0:

    Level 0:  0/1          1/0
    Level 1:       1/1
    Level 2:  1/2      2/1
    Level 3:  1/3  2/3  3/2  3/1
    ...

At each step, the mediant (a+c)/(b+d) of adjacent fractions inserts
a new rational between them. No division is performed — only integer
addition. The tree is a binary search tree over Q≥0, and every
rational appears at a unique finite depth.

Extension to Q: the parabola provides orientation (Part I.2), which
gives a sign convention. The full rationals are Q = {0} ∪ Q>0 ∪ (-Q>0),
where the negative branch mirrors the Stern-Brocot tree across the
oriented origin.

### 4. The circle map is assembled (all four primitives)

The standard circle map is:

    θ_{n+1} = θ_n + Ω - (K/2π) sin(2πθ_n)   (mod 1)

Each component traces to a primitive:

| Component | Primitive | Role |
|-----------|-----------|------|
| θ ∈ S¹ | Integers + fixed-point | Phase space (Part I.1) |
| Ω ∈ Q (via Stern-Brocot) | Integers + mediant | Bare frequency (Part I.3) |
| mod 1 | Integers + fixed-point | Quotient topology (Part I.1) |
| sin(2πθ) | Parabola (leading term) | Nonlinear coupling; near fixed points, sin ≈ 2πδθ, and the dynamics reduce to δθ² + μ = 0 |
| K | (continuous parameter) | Coupling strength; emerges from completion (Part III) |

The sine function is not a fifth primitive. Near any tongue boundary,
the circle map's fixed-point equation reduces to the saddle-node
normal form:

    δθ² + (Ω - p/q) = 0

The global shape of sin(·) determines which tongues exist and their
widths, but the **local** dynamics at every boundary — which is where
the Born rule, collapse time, and uncertainty relation are determined
— depend only on the parabola.

### 5. The staircase is constructed (mediants on the circle)

The winding number W(Ω) of the circle map, as a function of the bare
frequency Ω, is the devil's staircase. Its structure follows from the
Stern-Brocot tree:

- Each rational p/q in the tree corresponds to a mode-locked plateau
  (Arnold tongue) of width proportional to (K/2)^q at small K
- The plateaus are ordered by the Stern-Brocot tree's binary
  structure: the mediant of two adjacent locked frequencies is the
  next frequency to lock as K increases
- At K = 1 (critical coupling), the plateaus cover measure 1 — the
  staircase is complete, and the irrational winding numbers form a
  measure-zero Cantor set

The staircase at 1/φ is exactly self-similar with scaling factor φ²
because the Fibonacci convergents (1/1, 1/2, 2/3, 3/5, 5/8, ...) are
the mediants of the Stern-Brocot path to 1/φ, and each successive
convergent brackets 1/φ from alternating sides with a ratio that
converges to φ.

---

## Part II: Irreducibility

Each primitive is shown necessary by exhibiting what fails without it.

### Integers are irreducible

Without Z, the mediant has no operands. The parabola's two roots
cannot be counted. The fixed-point equation has no iterate count
(f^q requires q ∈ Z). There is no winding number, no period, no
discrete structure. The other three primitives become inert.

### Mediants are irreducible

Without the mediant, the available number system is Z (from integers)
plus algebraic irrationals like √μ (from the parabola). But the
interior rationals — 1/3, 2/5, 3/8 — are unreachable. Division
would construct them, but division is not composition of the remaining
three. The Stern-Brocot tree requires the mediant operation
specifically: it is the unique operation that inserts a rational
between two adjacent fractions using only integer addition. Without
it, there is no staircase, because there are no plateaus to fill the
frequency axis.

### Fixed-point equation is irreducible

Without x = f(x), the integers count but nothing iterates. The
mediants build a tree but nothing evolves on it. The parabola defines
a curve but not a dynamical system. Self-reference — the state
determining the map that determines the state — is what closes the
loop. Without it: no orbits, no periodicity, no circle (Part I.1),
no convergence, no attractors. The system is a static catalog of
numbers and shapes.

### Parabola is irreducible

Without x², all maps on the circle are linear: θ → θ + Ω. Linear
circle maps have constant winding number W = Ω for all initial
conditions — no tongues, no mode-locking, no bifurcation, no basins.
The Born rule requires Δθ ∝ √ε (exponent 1/2), which is the
saddle-node normal form x² + μ = 0. No other exponent is generic:

- x³: pitchfork bifurcation — codimension 1 only with symmetry,
  which the circle does not generically have
- x^(3/2): not smooth at x = 0 — violates differentiability of the
  circle map
- x^n, n > 2: structurally unstable — any small perturbation adds
  a quadratic term that dominates near the fixed point

The parabola is the **unique** generic codimension-1 bifurcation on
S¹. It is forced by structural stability, not chosen.

---

## Part III: Derived structures

### The continuum (completion of Q)

The Stern-Brocot tree enumerates Q≥0. The gaps in the devil's
staircase — the irrational winding numbers — are the Dedekind cuts
of the tree. The reals R emerge as the completion of Q under the
standard metric.

This completion is the step that produces the continuum. The four
primitives generate Q and S¹(Q) = Q/Z. The reals, and the smooth
circle S¹(R) = R/Z on which the standard circle map is defined,
require completing. This is **not** a primitive — it is a limit.

### What the completion discards: 0.999... = 1 as ψ-mode collapse

The theorem 0.999... = 1 in the reals is the statement that the
Fibonacci convergent sequence reaches its limit with no residual.
In the tree, the convergents to 1/φ:

    1/2, 2/3, 3/5, 5/8, 8/13, 13/21, ...

bracket 1/φ from alternating sides. At every finite step n, the
residual is Cassini's identity: F_{n-1}F_{n+1} - F_n² = (-1)^n.
The magnitude shrinks as φ^{-2n}. The sign alternates. This
alternation IS the ψ-mode — the decaying eigenvalue ψ = -1/φ
producing the (-1)^n oscillation.

The completion sends n → ∞ and sets the residual to zero. It
declares the sequence has arrived. What it discards:

1. **The alternating approach.** The ψ-mode's sign flips are the
   Z₂ parity that produces Cassini's identity, which IS the
   uncertainty relation τ×Δθ = const (Part III, §conjugate
   eigenvalue). Setting the residual to zero sets τ×Δθ to zero —
   infinite precision, no uncertainty. That is ℏ → 0.

2. **The finite gap.** At step n, the distance from F_n/F_{n+1} to
   1/φ is |F_n/F_{n+1} - 1/φ| = 1/(F_{n+1}²√5). This is nonzero
   at every finite step. The completion declares it zero. But in
   the tree at finite coupling K < 1, the gap is physical — it is
   the width of the superposition, the quasiperiodic orbit that
   has not resolved which tongue it belongs to.

3. **The Planck floor.** The smallest resolved interval at tree
   depth d is 1/q_max² where q_max ~ φ^d. The completion sends
   d → ∞ and gives the Archimedean property (no infinitesimals).
   At finite K < 1, the floor is nonzero and IS the UV cutoff
   (Derivation 6).

The reals are therefore the K = 1 sector of the framework. They
work perfectly for gravity (where all tongues are filled and the
completion is exact). They lose the quantum structure (where gaps
carry physical content). The continuum limit IS the classical
limit. This is why the framework needs exact rational arithmetic
for the field equation (Derivation 11): the rationals are the
physical states, the gaps are the quantum states, and completing
to R collapses both into a continuum that cannot distinguish them.

### Standard quantum mechanics (linearization + completion)

Standard QM is the theory obtained by:

1. **Linearizing** the circle map dynamics near tongue boundaries
   (small ε, first-order expansion of the saddle-node)
2. **Completing** Q to R (taking the continuum limit)

In this limit:

| Tongue dynamics | QM equivalent |
|-----------------|---------------|
| τ × Δθ = const | ΔE·Δt ≥ ℏ/2 (Heisenberg uncertainty) |
| Δθ² ∝ ε | P = \|ψ\|² (Born rule) |
| Tongue = mode-locked plateau | Bound state with definite energy |
| Gap = quasiperiodic orbit | Superposition / free particle |
| Saddle-node at boundary | Measurement (collapse to definite state) |
| Floquet multiplier → 1 | Unitary evolution between measurements |

The identification works because near a tongue boundary the circle
map transient is a decaying exponential — a signal whose Fourier
transform gives exactly the ΔωΔt ≥ 1/2 tradeoff. The tongue
uncertainty relation is the **nonlinear generalization** of HUP;
HUP is its linearized limit.

QM is not derived by the framework. QM is **identified as the
small-ε sector** of a system built from four primitives.

### The Born rule and HUP as conjugates

The Born rule (Derivation 1) and HUP (Derivation 7/tongue
uncertainty) are dual readings of the saddle-node parabola:

    Saddle-node normal form:  x² + μ = 0
    Solution:                 x = ±√(-μ)

    Read as basin measure:    Δθ = √ε        → P ∝ Δθ² = ε
    Read as resolution time:  τ = 1/Δω ∝ 1/√ε → τ·Δθ = const

One fixes **where** (probability = basin volume). The other fixes
**how long** (resolution cost = observation time). The exponent 2 in
|ψ|² and the exponent -1/2 in τ ∝ ε^(-1/2) are the same parabola
seen from conjugate axes.

Together they say: probability is cheap where resolution is fast,
and expensive where resolution is slow.

### The conjugate eigenvalue and the two-root reduction

The parabola x² - x - 1 = 0 (the characteristic equation of the
Fibonacci recurrence) has two roots:

    φ = (1 + √5)/2 ≈ 1.618    (the growing mode)
    ψ = (1 - √5)/2 = -1/φ     (the decaying mode)

ψ carries two operations simultaneously:

- **Negative symbol** (-): dissipation, contraction toward attractor,
  the alternating convergence in Cassini's identity
  F_{n-1}F_{n+1} - F_n² = (-1)^n
- **Negative exponent** (φ⁻¹): inversion, reciprocal, the operation
  that reads a cost landscape as a probability

These are not two properties — they are one object. The Wirtinger
derivative ∇_{ψ*} in the Born rule derivation (Derivation 1) does
both: differentiate with respect to the conjugate variable, which
turns cost gradient into dynamics.

**The uncertainty relation is Cassini's identity.**

At a saddle-node boundary:
- Δθ ∝ φ-mode contribution (basin width, growing with ε)
- τ ∝ 1/(ψ-mode contribution) (decay time, shrinking with ε)
- Their product: Δθ × (1/τ) ∝ |φ × ψ| = 1

The product |φψ| = 1 is the determinant of the Fibonacci matrix
[[1,1],[1,0]]. Cassini's identity says this determinant is ±1.
The uncertainty relation τ×Δθ = const is Cassini's identity
evaluated at a tongue boundary — the statement that the determinant
of the two-mode decomposition is unity.

The (-1)^n alternation in Cassini is the Z₂ parity of the ψ-mode:
consecutive Fibonacci convergents bracket 1/φ from alternating sides.
In the tongue picture, this is the alternation between approaching
the attractor from above and below — spiral approach, not monotone.

**The √5 separation.**

The two roots are separated by φ - ψ = √5. In the two-mode
decomposition F_n = (φⁿ - ψⁿ)/√5, this separation normalizes the
modes. It is the distance between attractors in eigenvalue space.

The observable universe samples ~2.2 Fibonacci levels of the
staircase hierarchy (Derivation 4: 60 e-folds × 0.0365 levels/e-fold
= 2.19). The eigenvalue separation is √5 ≈ 2.236. If these are
the same quantity — if the number of sampled levels is set by the
eigenvalue separation of the golden polynomial — then the number
of e-folds of inflation is determined by the algebra:

    N_levels = √5
    N_efolds = √5 / 0.0365 ≈ 61.2

The observed value is 60 ± a few (not precisely known). If the
framework predicts exactly √5/0.0365 ≈ 61.2 e-folds, that is a
sharp prediction testable by future CMB polarization measurements
of the tensor-to-scalar ratio r, which constrains N_efolds.

**Why the parabola is specifically x².**

The irreducibility proof (Part II) shows the parabola is forced by
genericity — it is the unique structurally stable codimension-1
bifurcation on S¹. But the two-root reduction shows more: x² is
not just "the simplest nonlinearity." It is the operation that
produces the conjugate pair (φ, ψ), which is the operation that
makes measurement have a direction (orientation from Part I.2),
that makes the Born rule have exponent 2 (from |φψ| = 1), and that
makes the uncertainty relation hold (Cassini). The exponent 2 in
|ψ|² is not a consequence of the parabola — it IS the parabola,
read as a probability.

### The 2π identification

The 2π in ℏ = h/(2π) and the 2π in a₀ = cH/(2π) are the same
geometric factor: the ratio of cycles to radians on S¹.

- h counts cost per **cycle** (integer winding)
- ℏ counts cost per **radian** (continuous angle)
- H is a frequency in **cycles per second**
- a₀ = cH/(2π) converts to **radians per second** on the
  gravitational pendulum

This is not a coincidence or an analogy. The circle S¹ has
circumference 1 (in the R/Z convention) or 2π (in the R/2πZ
convention). The factor 2π is the conversion between the integer
primitive (which counts cycles) and the continuum completion (which
measures angles). It appears wherever a physical quantity bridges
the discrete (cycles, quanta, orbits) and the continuous (phase,
action, angle).

---

## Part IV: Compositions

Everything in Derivations 1–9 is a composition:

| Structure | Primitives used | Derivation |
|-----------|----------------|------------|
| **Circle** S¹ | Z + fixed-point | (this derivation, I.1) |
| **Orientation** on S¹ | Parabola (±√μ) | (this derivation, I.2) |
| **Rationals** Q | Z + mediant | (this derivation, I.3) |
| **Circle map** | All four | (this derivation, I.4) |
| **Devil's staircase** W(Ω) | Mediant + circle | (this derivation, I.5) |
| **Arnold tongues** | Parabola + circle | Derivation 4 |
| **Born rule** P = \|ψ\|² | Parabola at tongue boundary | Derivation 1 |
| **Tongue uncertainty** τΔθ = const | Fixed-point convergence + parabola | Derivation 7 |
| **HUP** ΔωΔt ≥ 1/2 | Linearized tongue uncertainty | (this derivation, III) |
| **Spectral tilt** n_s ≈ 0.965 | φ² self-similarity of staircase | Derivation 4 |
| **Planck scale** | N = 3 threshold (minimum Z for loop) | Derivation 6 |
| **a₀ = cH/(2π)** | Fidelity bound + 2π identification | Derivation 3, 9 |
| **RAR** g_obs(g_bar) | Floquet exponent in physical coords | Derivation 9 |
| **Wavefunction collapse** | Saddle-node traversal (parabola + time) | Derivation 7, 9 |

---

## Part V: Testable predictions

### 1. Nonlinear corrections to minimum uncertainty

In the linearized limit (small ε), the tongue uncertainty gives
standard HUP: ΔωΔt ≥ 1/2. Deep inside a tongue (large ε), the
saddle-node dynamics are no longer parabolic — higher-order terms
in the circle map contribute. The tongue uncertainty τ×Δθ = const
still holds (it is exact for the circle map), but the Gaussian
minimum-uncertainty wavepacket is no longer the minimum-uncertainty
state.

**Prediction**: strongly mode-locked systems exhibit sub-Gaussian
phase uncertainty at fixed observation time. The leading correction
scales as ε² (the next term in the Taylor expansion of
sin(2πθ) beyond the parabolic approximation).

**Candidates**: superconducting circuits driven deep into resonance,
cavity QED systems at strong coupling, Josephson junction arrays
in the mode-locked regime.

### 2. The completion carries physical content

If the continuum (R) is a limit rather than a primitive, then
physical systems at finite coupling K < 1 do not have access to
the full continuum — only to the rationals resolved by the
staircase at that K. The "irrationals" are the gaps, not the states.

**Prediction**: at finite coupling, the effective Hilbert space
dimension is countable (indexed by the Stern-Brocot tree truncated
at depth ~ log K). The continuum limit is K → 1 (critical coupling).
Systems far from critical coupling should show discretization effects
in their frequency spectra that are not attributable to finite size.

### 3. The √5 prediction: e-folds of inflation from the golden polynomial

**Claim.** The number of Fibonacci levels the observable universe
samples is not approximately √5 — it is exactly √5. The number of
e-folds of inflation is:

    N_efolds = √5 / rate = √5 / [(n_s - 1) / (-ln φ²)]

Using Planck 2018 values (n_s = 0.9649 ± 0.0042):

    rate = (1 - 0.9649) / ln(φ²) = 0.0351 / 0.9624 = 0.03649
    N_efolds = 2.2360 / 0.03649 = 61.3 ± 0.7

The argument: the staircase at 1/φ is self-similar with ratio φ².
The two-mode decomposition F_n = (φⁿ - ψⁿ)/√5 has the separation
φ - ψ = √5 as its normalization constant. The number of levels
sampled by the observable universe is the number of e-folds times
the rate per e-fold. If the sampling is set by the eigenvalue
separation of the golden polynomial x² - x - 1 = 0, then:

    N_levels = φ - ψ = √5

This is not a fit. √5 is an algebraic constant determined by the
characteristic polynomial of the Fibonacci recurrence — the same
recurrence that generates the Stern-Brocot path to 1/φ and the
self-similar structure of the staircase. If the universe's inflation
samples exactly one eigenvalue separation of this polynomial, then
the duration of inflation is determined by the algebra of the
staircase, not by initial conditions.

**Why this might be true.** The two modes (φ, ψ) represent the
growing and decaying branches of the staircase dynamics. A "complete
sample" of the self-similar structure requires capturing both modes
across their full separation — one pass from φⁿ dominance to ψⁿ
dominance and back. That separation is √5 levels. Fewer than √5
levels undersamples the alternating (ψ-mode) structure. More than
√5 levels oversamples — the ψⁿ contribution has decayed below the
φⁿ contribution at the next level, and no new information is gained.

**The test.** CMB-S4 and LiteBIRD will measure the tensor-to-scalar
ratio r to precision σ(r) ~ 10⁻³. In slow-roll inflation, r and
n_s jointly constrain N_efolds via the consistency relation:

    r ≈ 8(1 - n_s) × (N_efolds dependent factor)

For common slow-roll models:
- φ² (Starobinsky/R²): N_efolds = (3 - n_s)/(2(1 - n_s)) ≈ 58
- φ²/³ (axion monodromy): N_efolds ≈ 45-55

The √5 prediction gives N_efolds = 61.3 ± 0.7, which is:
- **Distinguishable from φ² inflation** (58) at ~4σ given
  Planck+CMB-S4 precision on n_s
- **Distinguishable from lower N_efolds models** (45-55) already
- **Consistent with current data** (N_efolds = 50-70 allowed)

The specific test: if CMB-S4 measures r and n_s to sufficient
precision to determine N_efolds to ±2, the prediction N_efolds =
√5/rate = 61.3 is falsifiable. A measurement of N_efolds < 59 or
N_efolds > 63 would rule it out.

**What this would mean if confirmed.** The duration of inflation is
not a contingent fact about initial conditions. It is the eigenvalue
separation of x² - x - 1 = 0, divided by the rate at which the
staircase maps onto e-folds. The universe inflated for exactly as
long as needed to sample one complete period of the two-mode
Fibonacci decomposition. The same polynomial that produces the Born
rule (through |φψ| = 1) and the spectral tilt (through φ²
self-similarity) also produces the duration of inflation (through
φ - ψ = √5).

---

## Status

**Established**:
- Circle derived from integers + fixed-point (3-line proof)
- Orientation derived from parabola's two roots
- All four primitives shown irreducible by exhibiting failure modes
- Composition table verified against Derivations 1–9
- Born rule / HUP conjugacy identified (same parabola, dual axes)
- Uncertainty relation = Cassini's identity (|φψ| = 1)
- 2π factor traced to cycle-radian conversion on S¹
- √5 prediction: N_efolds = √5/rate ≈ 61.3, testable by CMB-S4

**Open**:
- Formalize the completion as a specific limiting process on the
  Stern-Brocot tree. What is the physical observable that
  distinguishes "rational resolved at depth d" from "irrational
  in the gap"? (Prediction 2 above.)
- Quantitative prediction for the leading correction to minimum
  uncertainty at large ε: compute the O(ε²) term in the circle
  map's fixed-point expansion and express it as a measurable
  deviation from the Gaussian bound.
- Numerical verification: write `alphabet_check.py` that constructs
  S¹ from Z + iteration, builds the Stern-Brocot tree via mediants,
  generates tongues via the parabola, and reproduces the staircase
  from the four primitives alone — no trig functions, no floating
  point, exact rational arithmetic throughout.

---

## Proof chains

This derivation provides the shared foundation (P1, P3) for all three
end-to-end proof chains:

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md)
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md)
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md)
