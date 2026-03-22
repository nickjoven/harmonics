# Derivation 7: Measurement Collapse from Tongue Traversal

## Claim

Wavefunction collapse is the transient of a driven nonlinear
oscillator crossing an Arnold tongue boundary. It has physical
duration, follows from the same geometry that produces the Born
rule, and connects to the quantum Zeno effect.

## The tongue picture of quantum states

In the circle map picture, the state of a system is a point (Ω, K)
in the parameter plane:

| State | Location | Orbit type |
|---|---|---|
| **Mode-locked** (classical) | Inside a tongue | Periodic — definite winding number |
| **Superposition** (quantum) | In a gap between tongues | Quasiperiodic — no definite winding number |
| **Measurement** | K increasing (coupling to apparatus) | Gap closing, tongue expanding |
| **Collapse** | Crossing tongue boundary | Transient from quasiperiodic to locked |

Superposition is not mysterious — it is quasiperiodicity. The system
explores the circle densely, participating in the basins of multiple
nearby tongues simultaneously. It has no definite winding number just
as it has no definite measurement outcome.

## Collapse has duration

At an Arnold tongue boundary, the Floquet multiplier is:

    f'(θ*) = 1 - K cos(2πθ*)

At the boundary: f' = 1 (marginal stability).
Inside the tongue: |f'| < 1 (exponential convergence).

The convergence rate per iteration is:

    λ = -ln|f'(θ*)| ≈ 2√(πKε)    for small ε

where ε is the depth past the tongue boundary. The locking time is:

    τ = C/λ ∝ 1/√ε

This is the INVERSE of the Born rule scaling (Δθ ∝ √ε):

- **Deep inside a tongue** (large ε): fast locking, large basin
- **Near the boundary** (small ε): slow locking, small basin
- **At the boundary** (ε = 0): infinite locking time, zero basin

Confirmed analytically and numerically (`collapse_tongues.py`):
τ×√ε converges to a constant as ε → 0.

## The collapse uncertainty relation

Since Δθ ∝ √ε (Born rule) and τ ∝ 1/√ε (collapse time):

    τ × Δθ = constant ≈ 10/√(πK)

This is a measurement uncertainty relation:

    (collapse duration) × (basin discrimination) = constant

You cannot simultaneously have fast collapse AND fine discrimination
between nearby tongues. This emerges from the parabolic geometry of
saddle-node bifurcation — the same geometry that produces |ψ|².

## The quantum Zeno effect

Continuous measurement holds the system at the tongue boundary
(ε → 0 at every measurement step). Each coupling event pushes
the system slightly into a tongue, but the next measurement resets it.

In the limit of continuous measurement: ε stays near zero, τ → ∞.
The system never locks. This is the Zeno effect, arising naturally
from the tongue geometry without a separate postulate.

## Superposition and the golden ratio

At subcritical coupling (K < 1), the devil's staircase has gaps.
The WIDEST gap is at 1/φ — the golden ratio frequency. It is the
last to close as K → 1 (KAM theorem: the golden torus is the
most robust to perturbation).

In the synchronization picture: the "most quantum" state — the one
most resistant to collapse — sits at frequency 1/φ. It requires the
strongest coupling (largest K) to force into a tongue.

## Collapse duration is testable

The framework (FRAMEWORK.md) -- the synchronization cost framework, which derives physical law from coupled-oscillator dynamics and cost minimization -- states: "Collapse has duration, not a
timestamp." The tongue traversal picture makes this concrete and
testable:

1. **Before measurement**: system at (Ω, K₀) in a gap
2. **Measurement begins**: K increases (apparatus couples)
3. **At K_critical**: tongue boundary reaches the system's Ω
4. **During collapse**: transient; duration τ ∝ 1/√(K - K_c)
5. **After collapse**: stably mode-locked

Testable prediction: systems coupled at MINIMUM strength to trigger
collapse (K barely above K_critical) should show anomalously long
decoherence times — slow collapse near threshold. This is distinct
from the Zeno effect (which prevents collapse entirely).

The Stribeck lattice -- a chain of friction-coupled oscillators exhibiting stick-slip bifurcation between coherent and dissipative regimes -- confirms this pattern: the bifurcation threshold
(A ≈ 0.8) shows the longest transients. Deep in either regime
(stick or slip), the system settles quickly.

## Connection to other derivations

**Born rule** (Derivation 1, which derives P = |ψ|² as basin measure of the cost landscape): the same saddle-node geometry gives
Δθ ∝ √ε (basin size) and τ ∝ 1/√ε (locking time). Both emerge
from the parabolic structure at tongue boundaries.

**Planck scale** (Derivation 6, which derives the Planck scale as the N = 3 self-sustaining threshold of the coupling loop): tongue structure requires N ≥ 3
coupling stages. Below the Planck scale, no tongues can form —
no superposition, no collapse, no Born rule.

**Spectral tilt** (Derivation 4, which derives the CMB tilt from mode-locking structure via the devil's staircase of the circle map): the devil's staircase structure
that governs collapse is the same self-similar structure that
produces the CMB power spectrum. The gap at 1/φ that makes it
"most quantum" is the same gap that determines the spectral tilt.

## Status

**Established**:
- Collapse duration τ ∝ 1/√ε (analytical + numerical)
- Uncertainty relation τ × Δθ = constant (from saddle-node geometry)
- Zeno effect as ε → 0 limit (τ → ∞)
- Golden ratio as maximally resistant to collapse (KAM theory)

**Open**:
- Can the collapse duration be connected to decoherence timescales
  measured in experiment? What plays the role of "iteration" in
  physical time?
- The tongue picture gives a sharp transition at K_c. Physical
  measurement coupling is graded, not instantaneous. How does
  continuous K(t) change the picture?
- Multi-tongue collapse: when the system is between several tongues,
  does it cascade through intermediate lockings or jump directly
  to the final state?
