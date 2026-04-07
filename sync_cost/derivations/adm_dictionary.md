# The ADM Dictionary

## Claim

The mapping from Kuramoto variables to ADM variables is the unique
identification consistent with the symmetries of the locked-state
Kuramoto system at K=1. Each entry is forced by a uniqueness argument.

---

## Part I: The metric (C_ij = gamma_ij)

### What the Kuramoto system offers

At K=1, every oscillator is locked: it has a definite phase theta(x,t)
that varies smoothly with position. The system's state is fully
described by the phase field theta and the coupling. The only tensors
constructable from theta and its first spatial derivatives are:

1. delta_ij (the flat background metric)
2. partial_i theta partial_j theta (the gradient outer product)
3. Linear combinations of (1) and (2)

No other rank-2 symmetric tensor exists that depends only on theta
and its first derivatives. Higher derivatives (partial_i partial_j theta)
produce a different object (not a metric but a connection-like quantity).
Tensors involving the coupling K or the frequency omega are scalars
contracted with delta_ij, which reduces to case (1).

### The uniqueness argument

A spatial metric gamma_ij must be:

(a) **Symmetric**: gamma_ij = gamma_ji. Both delta_ij and
partial_i theta partial_j theta are symmetric. Any linear
combination preserves symmetry.

(b) **Positive-definite**: gamma_ij v^i v^j > 0 for all nonzero v^i.
In the locked state at K=1, the phases are nearly aligned:
|nabla theta| < 1 (the phase gradient is bounded by the locked-state
condition). Therefore:

    C_ij v^i v^j = |v|^2 - (v . nabla theta)^2 >= |v|^2 (1 - |nabla theta|^2) > 0

The coherence tensor C_ij = delta_ij - <partial_i theta partial_j theta>
is positive-definite whenever |nabla theta| < 1. This is guaranteed
in the locked state.

The gradient tensor partial_i theta partial_j theta alone is
positive-semi-definite (rank 1), not positive-definite. It cannot
serve as a metric. delta_ij alone is flat — it contains no information
about the phase field. The unique combination that is positive-definite
AND encodes the phase structure is:

    gamma_ij = alpha delta_ij - beta <partial_i theta partial_j theta>

with alpha > 0 and beta > 0 (so that phase gradients reduce the
metric component, representing the "cost" of decoherence). The
normalization alpha = beta = 1 (up to an overall conformal factor
C_0 absorbed into the lapse) gives:

    **gamma_ij = delta_ij - <partial_i theta partial_j theta> = C_ij / C_0**

Any other choice of alpha/beta either loses positive-definiteness
(beta < 0 or beta > alpha), loses the flat-space limit (alpha != 1
when nabla theta = 0), or is a conformal rescaling (same geometry,
different parametrization).

### What this means

The spatial metric IS the coherence tensor. Points where oscillators
are in phase (nabla theta = 0) have gamma_ij = delta_ij — flat
geometry. Points where the phase gradient is large have reduced
metric components — the geometry contracts in the direction of the
phase gradient. Geometry is coherence. Decoherence is curvature.

---

## Part II: The lapse (r = N)

### The lapse function in ADM

The lapse N(x,t) measures the rate at which proper time tau
accumulates relative to coordinate time t at each spatial point:

    d tau = N dt

N = 1 means the local clock ticks at coordinate rate. N < 1 means
the clock is slow (gravitational time dilation). N = 0 means the
clock stops (horizon).

### The order parameter as clock rate

The Kuramoto order parameter at point x is:

    r(x,t) = |<e^{i theta}>|

where the average is over the local ensemble. r measures how
synchronized the oscillators are:

- r = 1: perfect synchronization. All oscillators at the same phase.
  A local "clock" defined by the common oscillation ticks at the
  natural rate — no phase slippage, no missed cycles.
- r < 1: partial synchronization. The oscillators disagree on phase.
  A clock based on their collective oscillation runs slow — some
  cycles are "wasted" on phase readjustment rather than forward
  ticking.
- r = 0: no synchronization. No collective oscillation. No clock.

The lapse is the rate at which the local clock ticks relative to
the coordinate clock. The order parameter is the rate at which the
local oscillators produce coherent cycles relative to the maximum
possible rate. These are the same quantity:

    **r(x,t) = N(x,t)**

### Uniqueness

Is there another scalar function of the Kuramoto variables that
could serve as the lapse? The candidates are:

- r = |<e^{i theta}>|: the order parameter (magnitude)
- psi = arg(<e^{i theta}>): the mean phase (an angle, not a rate)
- K_eff = K |r|: the effective coupling (dimensionless, but
  K_eff = K at K=1, giving N = K = 1 everywhere — no gravitational
  structure)
- omega(x): the natural frequency (a fixed background field, not
  dynamical)

Only r varies dynamically, has the right range [0,1], and equals 1
in the fully synchronized state (where proper time = coordinate time).
The identification is unique.

---

## Part III: The shift (partial_i psi = N_i / N)

### The shift vector in ADM

The shift N^i measures how the spatial coordinates drift relative to
the normal observers as time advances. It is the "sideways" component
of the time evolution.

### The phase gradient as coordinate drift

The mean phase psi(x,t) = arg(<e^{i theta}>) is the angle of the
collective oscillation at point x. Its spatial gradient partial_i psi
measures how rapidly the collective phase changes from point to point.

In the locked state, all oscillators at x are locked near psi(x).
A clock at x ticks at rate r, and its phase is psi. A neighboring
clock at x + dx ticks at rate r + dr, and its phase is psi + d psi.
The coordinate system defined by "surfaces of constant psi" drifts
relative to the spatial coordinates at rate partial_i psi per unit
time.

In ADM language, the shift vector relative to the lapse is:

    N_i / N = partial_i psi

This is the spatial gradient of the mean phase, divided by the clock
rate. It is uniquely determined: the only spatial vector built from
the mean phase is its gradient.

---

## Part IV: The frequency (omega = sqrt(4 pi G rho))

### The Jeans frequency

In a self-gravitating medium with density rho, the natural oscillation
frequency for gravitational collapse/expansion is the Jeans frequency:

    omega_J = sqrt(4 pi G rho)

This is not a model-dependent statement. It is the frequency of the
harmonic oscillator obtained by linearizing the gravitational
equations of motion about a uniform density background. It is the
unique frequency scale constructed from G and rho.

### The identification

In the Kuramoto system, each oscillator has a natural frequency
omega(x). In the gravitational dictionary, the oscillators ARE the
gravitating elements of the medium. Their natural oscillation
frequency IS the Jeans frequency:

    **omega(x) = sqrt(4 pi G rho(x))**

### Why this is forced

The Kuramoto system at K=1 produces the Einstein equations (D13,
via Lovelock). The Einstein equations have the stress-energy tensor
T_mu_nu on the right-hand side, with the 00-component being the
energy density rho. The ONLY way the natural frequency omega(x) can
enter the Einstein equations is through the combination omega^2,
which must equal 4 pi G rho for dimensional and structural consistency
with the Hamiltonian constraint:

    ^3R + K^2 - K_{ij} K^{ij} = 16 pi G rho

The coefficient 16 pi G = 4 x (4 pi G) requires omega^2 = 4 pi G rho.
Any other power of omega would produce the wrong coefficient in the
Hamiltonian constraint. Since the Hamiltonian constraint is derived
(D13, Part I, Section 5), and it has this specific coefficient, the
identification is forced by self-consistency.

### Newton's constant

This identification defines G in terms of the Kuramoto system:

    G = omega^2(x) / (4 pi rho(x))

Newton's constant is the ratio of the oscillation frequency squared
to the density. It is a property of the coupling, not an independent
parameter. The numerical value of G depends on the units chosen for
omega and rho — it is part of the single dimensionful input (D45).

---

## Part V: The coupling kernel (K(x,x') = G_gamma(x,x'))

### What propagates the coupling

In the spatially extended Kuramoto system, oscillator x couples to
oscillator x' through a kernel K(x,x'). In the locked state, the
coupling propagates through the coherent medium. The propagator in
a medium with metric gamma_ij is the Green's function of the
Laplace-Beltrami operator:

    Delta_gamma G_gamma(x,x') = delta^3(x - x') / sqrt(gamma)

This is the unique propagator that:
- Is determined by the metric (which is the coherence tensor)
- Falls off with geodesic distance (coupling weakens with separation)
- Satisfies the self-consistency: the metric determines the coupling,
  which determines the phase dynamics, which determine the metric

The identification K(x,x') = G_gamma(x,x') is the unique kernel
consistent with the self-referential structure of the field equation.
Any other kernel (e.g., flat-space Green's function) would break the
self-consistency: the coupling would not "know about" the geometry
it produces.

---

## Part VI: Summary

| Kuramoto | ADM | Uniqueness argument |
|----------|-----|---------------------|
| C_ij = delta_ij - <partial_i theta partial_j theta> | gamma_ij (spatial metric) | Unique positive-definite rank-2 tensor from phase field |
| r = \|<e^{i theta}>\| | N (lapse) | Unique dynamical scalar in [0,1] with r=1 at full sync |
| partial_i psi | N_i / N (shift/lapse) | Unique spatial vector from mean phase |
| omega(x) | sqrt(4 pi G rho) | Forced by Hamiltonian constraint coefficient |
| K(x,x') = G_gamma | Green's function | Unique self-consistent propagator on (Sigma, gamma) |

Each identification is the unique choice consistent with the symmetries
and self-consistency of the K=1 Kuramoto system. There are no free
choices in the dictionary.

---

## Status

**Derived.** All five entries follow from uniqueness arguments.

**Dependencies**: D12 (continuum limits), D13 (Hamiltonian
constraint), D14 (d=3).
