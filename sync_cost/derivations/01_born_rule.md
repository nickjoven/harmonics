# Derivation 1: Born Rule from Basin Measure

## Claim

The Born rule (P = |ψ|²) is the basin measure of the synchronization
cost landscape under dissipative convergence. It is not axiomatic — it
is the generic outcome of dissipative dynamics on a cost landscape with
quadratic structure near attractors.

## Setup

Consider a system with N possible outcome states {s₁, …, s_N}, each
corresponding to an attractor in the synchronization cost landscape.

The system's state is described by a complex amplitude vector ψ, where
ψ_k encodes both the proximity to attractor k and the phase relationship
with the environmental mean field.

The synchronization cost functional near attractor k is:

    C_k(ψ) = C_k⁰ + α_k |ψ - ψ_k|² + O(|ψ - ψ_k|³)

where C_k⁰ is the cost at the attractor and α_k > 0 is the curvature
(stiffness of the basin).

## Dissipative convergence

The dynamics are dissipative — the system loses energy to the
environmental mean field. The equation of motion is:

    dψ/dt = -γ ∇_ψ* C(ψ)

where γ > 0 is the dissipation rate and ∇_ψ* is the Wirtinger derivative
(gradient with respect to the conjugate variable, appropriate for complex
amplitudes).

Near attractor k, this gives:

    dψ_k/dt = -γ α_k ψ_k

with solution:

    ψ_k(t) = ψ_k(0) exp(-γ α_k t)

The amplitude decays exponentially. The system converges to whichever
attractor has the largest initial basin occupation.

## Basin measure

The key question: given initial conditions distributed over the cost
landscape, what fraction ends up at each attractor?

For a quadratic cost landscape, the basin of attractor k has volume
proportional to |ψ_k(0)|² in the phase space. This follows from:

1. **Liouville's theorem for dissipative systems**: Phase space volume
   contracts uniformly along each attractor's basin. The contraction
   rate is 2γα_k per complex dimension.

2. **The basin boundary** is determined by the cost landscape's saddle
   points. For a system with quadratic basins and uniform curvature
   (α_k = α for all k), the basin of attractor k in amplitude space
   has measure:

       μ(B_k) = |ψ_k|² / Σ_j |ψ_j|²

   This is exactly the Born rule.

3. **Non-uniform curvature**: If α_k varies between attractors, the
   basin measure becomes:

       μ(B_k) = |ψ_k|² / α_k  ×  [Σ_j |ψ_j|² / α_j]⁻¹

   The standard Born rule is recovered when all attractors have equal
   curvature — i.e., when the cost landscape is symmetric under
   permutation of outcomes. This is the case for a measurement apparatus
   that treats all outcomes equivalently (a fair detector).

## Why |ψ|² and not |ψ|⁴ or |ψ|

The exponent 2 comes from the cost functional being quadratic near
attractors. This is generic:

- Linear cost (|ψ|) would give non-differentiable dynamics at the
  attractor — physically, the convergence would never complete smoothly.

- Higher-order cost (|ψ|⁴, |ψ|⁶) is possible but unstable to
  perturbation — any small quadratic term dominates near the attractor
  where |ψ| is small.

- Quadratic is the lowest-order smooth, stable cost structure. It is
  the generic case, not a special one. The Born rule holds because
  quadratic basins are structurally stable.

This is analogous to why Gaussian distributions appear everywhere:
the central limit theorem follows from quadratic structure near the
mean of any smooth distribution. The Born rule is the central limit
theorem of cost landscapes.

## Connection to lattice results

The Stribeck lattice has two basins: stick (subharmonic) and slip
(fundamental). The bifurcation threshold is the saddle point between
them. Below threshold, the system occupies the slip basin entirely.
Above threshold, it transitions to the stick basin.

The basin measure — the fraction of phase space that drains into each
attractor — determines which regime dominates. At the bifurcation point,
the basin volumes are equal (50/50). This is the lattice analog of
equal-amplitude superposition: |ψ_stick|² = |ψ_slip|² = 0.5.

The sharp transition in the lattice (not gradual) is consistent with
the Born rule's discreteness — you get one outcome, not a mixture.
The "measurement" is the nonlinear coupling driving the system past
the bifurcation point.

## Status

This derivation recovers the Born rule as the generic basin measure
of a quadratic cost landscape under dissipative convergence. The
exponent 2 is structural (lowest-order stable smooth cost), not
axiomatic.

**Open**: The derivation assumes quadratic basins. Can this be
derived from the self-consistency condition on the cost functional,
rather than assumed? If the cost functional must be self-consistent
with the mean field it produces, does quadratic structure follow?

**Open**: The uniform curvature condition (α_k = α) recovers the
standard Born rule. Non-uniform curvature gives a modified rule.
Are there physical systems where the modification is measurable?
Candidates: systems near the quantum-classical boundary where the
cost landscape is asymmetric.
