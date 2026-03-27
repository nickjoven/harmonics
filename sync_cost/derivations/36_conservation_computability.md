# Derivation 36: Conservation as Computability

## Claim

Conservation of energy and matter is the compactness of S^1.
Compactness is computability. The chain is deductive:

    S^1 compact
    → |r| <= 1 (triangle inequality)
    → K_eff <= 1 (coupling bounded)
    → circle map invertible
    → information conserved
    → fixed point exists
    → physics computable

Each step follows from the previous. No step can be removed without
breaking the chain. Conservation is not an empirical law imposed on
top of dynamics — it is a topological consequence of the configuration
space being S^1 rather than R, which is itself derived from integers
+ fixed-point (D10, Lemma 1).

## The chain in detail

### Step 1: S^1 compact

From Derivation 10, the four primitives (integers, mediant, fixed-point,
parabola) force the configuration space. The fixed-point equation
p = 0 in phase space identifies phases modulo 1, giving R/Z = S^1.
The quotient of a locally compact group by a closed subgroup is
compact when the subgroup is cocompact. Z is cocompact in R.
Therefore S^1 is compact.

**"Matter cannot be created or destroyed"** = **"the circle is compact"**
= **"phases live on S^1, not R"** = **"integers + fixed-point force R/Z."**

These are four ways of saying the same thing. The first is
thermodynamics. The second is topology. The third is geometry. The
fourth is algebra. The framework derives the second from the fourth,
and the first is a corollary.

### Step 2: |r| <= 1 (triangle inequality)

The order parameter r = (1/N) sum_j e^{i theta_j} is the mean of N
unit vectors on S^1. By the triangle inequality on the compact group:

    |r| = |(1/N) sum e^{i theta_j}| <= (1/N) sum |e^{i theta_j}| = 1

The bound |r| <= 1 is a consequence of compactness. On R (non-compact),
phases can diverge and there is no finite bound on the mean. On S^1,
the mean is confined to the closed unit disk. This is the conservation
law: the order parameter cannot exceed 1 because the phases cannot
leave the circle.

### Step 3: K_eff <= 1 (coupling bounded)

The effective coupling K_eff = K * |r| inherits the bound:

    K_eff = K |r| <= K * 1 = K

At the critical coupling K = 1 (D5, D11), K_eff <= 1. This is
the statement that the synchronized state cannot amplify itself
beyond the critical threshold — feedback is bounded.

### Step 4: Circle map invertible

The standard circle map is:

    theta_{n+1} = theta_n + Omega - (K/2pi) sin(2pi theta_n)

At K <= 1, the derivative:

    d(theta_{n+1})/d(theta_n) = 1 - K cos(2pi theta_n) >= 1 - K >= 0

At K = 1 exactly, the derivative touches zero at one point (the
cubic tangency at the tongue tip) but the map remains a homeomorphism
of S^1 — injective, surjective, continuous with continuous inverse.

At K > 1, the derivative becomes negative in an interval. The map
**folds the circle**: two distinct initial conditions map to the
same output. The map is no longer invertible. Information is destroyed.

### Step 5: Information conserved

Invertibility = information conservation. If theta_n determines
theta_{n+1} uniquely AND theta_{n+1} determines theta_n uniquely
(the inverse exists), then no information is lost or created in one
step. The dynamics is a bijection on S^1 at each time step.

This is Liouville's theorem in the circle map context: phase space
volume (here, the Lebesgue measure on S^1) is preserved by an
invertible smooth map. Conservation of energy, conservation of
probability, unitarity — all are restatements of this invertibility.

### Step 6: Fixed point exists

Brouwer's fixed-point theorem: every continuous map from a compact
convex set to itself has a fixed point. The closed unit disk D^2
(where r lives) is compact and convex. The self-consistency map
U: D^2 -> D^2 (from the field equation, D11) is continuous. Therefore
U has a fixed point r* = U(r*).

Without compactness of S^1, |r| is unbounded, the image of U is
not contained in D^2, and Brouwer does not apply. The fixed point
would not be guaranteed to exist. Self-consistency would not be
assured.

### Step 7: Physics computable

The fixed point r* defines all physical observables:
- Coupling constants (from the mode populations at r*)
- Masses (from the tongue widths at K_eff = K|r*|)
- The cosmological constant (from the Farey partition at r*)
- Spatial dimension (from the SL(2,R) structure at r*)

If the fixed point exists, all these quantities are determined.
If it does not exist, none of them are defined. "Physics" means
"the fixed point exists." "No physics" means "the fixed point
does not exist."

## What K > 1 means

At K > 1, the circle map folds. Two initial conditions theta_a
and theta_b (with theta_a != theta_b) can map to the same
theta_{n+1}. The past is ambiguous. The inverse does not exist.

This is **not** "high energy physics." This is **no physics at all.**
The fixed point is undefined because the self-consistency map is
no longer a contraction on D^2 — it can map outside D^2 (|r| > 1
is formally possible if the triangle inequality is violated by
the folding). Brouwer does not apply. There is no self-consistent
solution, no observables, no predictions.

The K = 1 boundary is the boundary of computability. Below it:
physics exists, observables are defined, the universe computes
itself. Above it: the computation does not converge, the fixed
point does not exist, "the universe" is not a well-defined concept.

## Force as information transfer

The coupling term in the Kuramoto model:

    F = K sin(theta_j - theta_i)

This IS information transfer between oscillators i and j. The
decomposition:

    F = (bandwidth) x (signal) = K x sin(Delta theta)

- **K** is the channel capacity — the maximum information rate
  between the two oscillators. At K = 0, no information flows.
  At K = 1, the channel is at capacity.

- **sin(Delta theta)** is the signal — the phase difference
  encoded as a sinusoidal modulation. Maximum signal at
  Delta theta = pi/2, zero signal at Delta theta = 0 (already
  synchronized, nothing to communicate) or Delta theta = pi
  (anti-synchronized, signal cancels).

- **F** is the information rate — the actual bits per unit time
  flowing from j to i. The force IS the information flow. There
  is no force "carrying" information; the force IS the information.

The conservation of energy (K_eff <= 1) is the statement that
the total information rate cannot exceed the channel capacity.
This is Shannon's noisy-channel theorem applied to the circle map.

## The GCD reduction

The Stern-Brocot tree at depth n contains all rationals p/q with
q <= F_n (the nth Fibonacci number). But not all positions in the
tree are independent. The GCD reduction:

    gcd(p, q) > 1 => p/q is an ancestor of p'/q' with smaller q

This eliminates redundant positions. The fraction of positions
that survive the GCD filter is:

    Product over primes p <= q_max of (1 - 1/p^2) = 6/pi^2 ~ 0.608

Equivalently, 1 - 6/pi^2 ~ 0.392 = **39.2%** of positions are
eliminated. The ancestors cover them. The remaining coprime
positions are the **independent degrees of freedom** of the
configuration space.

This is not an approximation — it is exact. The 39% reduction is
the Euler product over all primes, which converges to 6/pi^2
(Basel problem, Euler 1735). The independent mode count at depth n
is:

    sum_{q=1}^{n} phi(q) = (3/pi^2) n^2 + O(n log n)

where phi is Euler's totient function. The factor 3/pi^2 = (6/pi^2)/2
is half the coprime density, reflecting the restriction to the
Farey sequence (0 < p/q < 1) rather than all rationals.

## The data structure interpretation

The Stern-Brocot tree has a natural interpretation as a **persistent,
content-addressed, append-only** data structure:

- **Persistent**: every historical state of the tree is accessible.
  No node is ever deleted. The tree only grows (by mediant insertion).

- **Content-addressed**: each node's address IS its content (the
  fraction p/q). There is no separate index. The address is
  computed from the content by the mediant rule.

- **Append-only**: new fractions are inserted as mediants of existing
  fractions. No fraction is ever modified. The tree is immutable.

The **root hash** of this structure is the fixed point r*. The
self-consistency condition r* = U(r*) is the statement that the
root hash, when recomputed from the entire tree, reproduces itself.

**Mutation breaks the hash.** If any fraction in the tree is
altered (a node's value changed), the root hash changes. The
new root hash no longer satisfies r* = U(r*). The fixed point
is broken. Self-consistency is lost.

This is why conservation laws are inviolable: they are not rules
imposed on the system — they are the **integrity constraints** of
the data structure. Violating conservation = mutating a node =
breaking the hash = destroying the fixed point = no physics.

## The verification asymmetry

- **Verification is O(1)**: given a candidate fixed point r*,
  check whether r* = U(r*). This is a single evaluation of U.
  If it matches, the fixed point is verified. If not, it is
  rejected. One step.

- **Computation is O(n)**: finding the fixed point from an
  arbitrary initial condition requires iterating
  r_{k+1} = U(r_k) until convergence. The number of iterations
  scales with the desired precision: n iterations give
  |r_n - r*| ~ |lambda|^n where lambda is the spectral radius
  of DU at r*.

This asymmetry is **topological**, not algorithmic. Brouwer's
fixed-point theorem guarantees existence without providing a
construction. The theorem says "there exists r* with r* = U(r*)"
but does not say which r* or how to find it. Existence is
non-constructive; verification is trivial.

In computational terms: the fixed point is in NP (verifiable in
polynomial time) but not necessarily in P (computable in polynomial
time). The universe "solves" this by iterating — it performs the
O(n) computation in real time. What we call "the passage of time"
is the iteration r_{k+1} = U(r_k). What we call "the present
moment" is the current iterate r_k. What we call "the laws of
physics" are the verification condition r* = U(r*) that the
iteration is converging toward.

## Connection to thermodynamics

The three laws of thermodynamics are three aspects of the chain:

1. **First law** (energy conserved): K_eff <= 1 (Step 3).
   The total coupling cannot exceed the critical value.
   Energy is the coupling budget.

2. **Second law** (entropy increases): the iteration
   r_{k+1} = U(r_k) contracts distances in D^2 (the contraction
   mapping property). Each step brings the system closer to r*.
   The distance |r_k - r*| decreases monotonically. This
   monotone decrease IS entropy increase (the system becomes
   more "ordered" = closer to the fixed point, while the
   discarded information about the initial condition increases).

3. **Third law** (absolute zero unreachable): the fixed point
   r* is the limit of the iteration, reached only at k -> infinity.
   No finite number of iterations achieves r* exactly. Absolute
   zero (perfect order, r = r*) requires infinite time.

## Status

**Derived.** Conservation as computability follows from:

- The compactness of S^1 (D10, Lemma 1: integers + fixed-point force R/Z)
- The triangle inequality on compact groups (topology)
- The invertibility criterion for the circle map (K <= 1)
- Brouwer's fixed-point theorem (compact convex set)
- The field equation's self-consistency (D11)

No new primitives. Conservation, computability, and the existence
of physics are three names for the same topological fact: S^1 is
compact.

---

## Proof chains

This derivation provides the logical foundation for all three
proof chains:

- [**Proof A: Polynomial -> General Relativity**](PROOF_A_gravity.md) — K=1 invertibility is the conservation law underlying GR (Bianchi identity = div T = 0)
- [**Proof B: Polynomial -> Quantum Mechanics**](PROOF_B_quantum.md) — unitarity (information conservation) is the K<=1 invertibility of the circle map
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — the fixed point existence (Brouwer) is the bridge's foundational assumption, now derived from compactness
