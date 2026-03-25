# Derivation 18: The Möbius Container

## Claim

A bounded, compact, non-orientable surface changes the Kuramoto
self-consistency equation from an open dissipative system to a closed
resonator. On such a surface, excitations cannot escape — they reflect,
interfere, and accumulate until standing waves form at rational phase
divisions. The rational divisions are not approximate. They are exact,
forced by boundary conditions, and stable enough to persist for
arbitrarily many cycles.

This is calculable. The boundary conditions are specifiable, the geometry
is well-defined, the dynamics are known. What follows is the simulation
target: Kuramoto on a compact non-orientable surface, with the minimal
parameters to produce one stable rational division from a perturbation
of rest.

## Why the container changes everything

### The open-system objection

The standard critique of synchronization-as-gravity: beat frequencies
dissipate into unbounded space, coupling strength falls off, nothing
collects the signal. On R³, this is correct. A finite perturbation
spreads, dilutes, and the coherence signal decays as 1/r².

### The compact-surface answer

On a compact surface, nothing escapes. Every excitation reflects at the
boundary (if there is one) or wraps around (if the surface is closed).
The dynamics are:

1. **Reflection**: excitation hits boundary → reverses → encounters
   itself on the return path
2. **Interference**: reflected and incident waves superpose → standing
   wave pattern determined by boundary conditions
3. **Accumulation**: energy that would dissipate on an open manifold
   is trapped → effective coupling strength grows with each traversal
4. **Saturation**: standing wave pattern stabilizes when input matches
   reflected loss → fixed point of the dynamics

This is a resonant cavity. The rational divisions (mode-locked plateaus)
are the resonant modes. On an open manifold they are transient; on a
compact surface they are attractors.

### Why Möbius specifically

A Möbius strip has one boundary and one side. A perturbation traversing
the strip encounters itself with reversed orientation after one full
traversal. This is forced self-interference — not optional, not
tunable, built into the topology.

Consequences:

- **No inside/outside leakage**: the excitation has nowhere to go
  except back through the structure
- **Orientation reversal**: after one circuit, "phase advance" has
  become "phase retard." The perturbation interferes destructively
  with its own image at odd harmonics and constructively at even —
  this selects specific rational divisions
- **Subharmonic generation**: the half-twist means the fundamental
  round-trip is 2L (twice the strip length), exactly as in Kawano
  et al. (2025) where the bow contact on a bowed string creates a
  subharmonic by introducing a reflective boundary with effective
  frequency ratio 2:1

The Möbius geometry is not decorative. It is the minimal topology that
forces self-interference with orientation reversal.

## The simulation target

### Domain

A Möbius strip parametrized by:

- **Length** L along the non-orientable loop (identified: x ~ x + 2L
  with orientation reversal at x = L)
- **Width** W across the strip (one boundary at w = 0, free or
  reflecting; identification w → -w at x = x + L gives the twist)

For the minimal simulation, W can be collapsed — use the 1D
non-orientable circle: the interval [0, L] with identification
θ(0) = -θ(L) (antiperiodic boundary condition). This is the
simplest compact non-orientable domain.

### Oscillators

Place N oscillators uniformly on [0, L]:

    x_i = (i - 1/2) L/N,    i = 1, ..., N

Each oscillator has:
- Phase θ_i(t) ∈ [0, 2π)
- Natural frequency ω_i drawn from distribution g(ω)

### Dynamics

Kuramoto with nearest-neighbor coupling on the Möbius domain:

    dθ_i/dt = ω_i + (K/2)[sin(θ_{i+1} - θ_i) + sin(θ_{i-1} - θ_i)]

with the **antiperiodic boundary condition**:

    θ_{N+1}(t) ≡ θ_1(t) + π    (the half-twist)

This is the standard Kuramoto ring except the boundary wraps with a
π phase shift. The shift is the topological content of the Möbius strip.

### Initial condition: perturbation from rest

All oscillators start at θ_i(0) = 0 (uniform phase, "at rest"), with
a single localized perturbation:

    θ_j(0) = ε    (one oscillator displaced by ε)

The question: does this perturbation grow, propagate, reflect off the
antiperiodic boundary, interfere with itself, and produce a stable
rational phase division?

### Parameters to determine

Three free parameters:

1. **N** — number of oscillators. Derivation 6 says N = 3 is the
   minimum self-sustaining chain. Start there.
2. **K** — coupling strength relative to frequency spread. The
   framework gives K_c = 2/(πg(0)) as the synchronization threshold.
   Scan K/K_c from 0 to 2.
3. **ε** — initial perturbation magnitude. The question is whether
   any ε > 0 suffices, or whether there is a threshold.

The frequency distribution g(ω) should be the framework's self-consistent
g* from the rational field equation (Derivation 11), but for the
minimal simulation, a Lorentzian of half-width γ centered at ω₀
suffices (this admits the Ott-Antonsen reduction).

## What "one stable rational division" means

A rational division p/q is a state where the phase difference between
oscillators (or between an oscillator and the mean field) locks to
2πp/q. "Stable" means:

1. The phase difference persists for t → ∞ (or for T >> 1/γ in the
   dissipative case)
2. Small perturbations around the locked state decay (Lyapunov stable)
3. The winding number of the phase trajectory is exactly p/q (not
   approximately)

On the Möbius domain, the antiperiodic boundary condition θ(L) = θ(0)+π
forces the total phase winding across the strip to be (2n+1)π/L for
integer n. This quantizes the allowed spatial modes to odd multiples
of π/L — the even modes are forbidden by the topology.

The first stable rational division is the lowest-energy odd mode:
a standing wave with one antinode, winding number 1/2 (half-period
across the strip length).

## Analytical predictions

### N = 3 on the Möbius ring

Three oscillators with antiperiodic boundary:

    dθ₁/dt = ω₁ + (K/2)[sin(θ₂ - θ₁) + sin(θ₃ - θ₁ + π)]
    dθ₂/dt = ω₂ + (K/2)[sin(θ₃ - θ₂) + sin(θ₁ - θ₂)]
    dθ₃/dt = ω₃ + (K/2)[sin(θ₁ - θ₃ - π) + sin(θ₂ - θ₃)]

The +π in the coupling of oscillator 1 to oscillator 3 (and the -π
in 3 to 1) is the Möbius twist. Note that sin(α + π) = -sin(α), so
the twist converts the attractive coupling to repulsive across the
boundary seam.

At the fixed point with identical frequencies (ω₁ = ω₂ = ω₃ = ω₀),
the uniform state θ₁ = θ₂ = θ₃ is NOT a fixed point (the boundary
term gives -sin(π) ≠ 0... actually sin(π) = 0, so the uniform state
IS marginally compatible). The first nontrivial solution has:

    θ₁ = 0, θ₂ = π/3, θ₃ = 2π/3

This is the 1/3 rational division — three oscillators equally spaced
in phase, with the boundary twist accommodated by the 2π/3 spacing
(since θ₃ + π = 2π/3 + π ≡ 5π/3, and the next oscillator wraps to
θ₁ = 0 ≡ 2π, giving a phase jump of 2π - 5π/3 = π/3, consistent).

Whether this is stable depends on K. The Jacobian of the N = 3 system
at this fixed point determines the critical coupling.

### Critical coupling on the Möbius ring

For the standard (periodic) Kuramoto ring with N oscillators and
identical frequencies, the fully synchronized state θ_i = const is
stable for any K > 0. On the Möbius ring, the antiperiodic boundary
shifts the stability threshold.

The eigenvalues of the coupling matrix on the Möbius ring are:

    λ_k = -2K sin²(π(2k+1)/(2N)),    k = 0, 1, ..., N-1

(odd modes only, due to antiperiodicity). The most dangerous mode
(smallest |λ|) is k = 0:

    λ₀ = -2K sin²(π/(2N))

Stability requires λ₀ < 0, which holds for all K > 0. But with
frequency disorder (ω_i not identical), the effective threshold is:

    K_c^{Möbius} = Δω / sin(π/(2N))

where Δω is the frequency spread. For N = 3: sin(π/6) = 1/2, so
K_c = 2Δω. Compare with the standard ring: K_c = 2Δω/sin(π/N) =
2Δω/sin(π/3) = 2Δω/(√3/2) = 4Δω/√3 ≈ 2.31Δω. The Möbius ring
requires **less** coupling to lock — the twist helps, because it
introduces a π phase offset that partially compensates the natural
frequency differences.

### Minimal parameters for one rational division

For N = 3, Lorentzian g(ω) with half-width γ, and initial perturbation
ε:

1. **Coupling**: K > K_c = 2γ/sin(π/6) = 4γ (for N = 3 Möbius)
2. **Perturbation**: any ε > 0 suffices — the locked state is a global
   attractor for K > K_c (Lyapunov, Derivation PRO-LU)
3. **Settling time**: τ ~ 1/(K - K_c) for K near threshold; τ ~ 1/K
   for K >> K_c
4. **Result**: phase locks to 1/3 rational division (the lowest odd
   mode on the 3-element Möbius ring)

The CPU cycle count to produce one stable division:

    N_cycles = τ / dt = (1/K) / dt

For K = 5γ (moderately above threshold), γ = 1, dt = 0.01:
N_cycles ~ 200. Two hundred integration steps. Computationally trivial.

## Connection to existing derivations

| This derivation | Builds on | What it adds |
|---|---|---|
| Antiperiodic boundary | D16 (Möbius topology) | Makes the topology a boundary condition, not a metaphor |
| N = 3 minimum | D6 (Planck scale, N = 3) | Tests N = 3 on a new geometry (Möbius vs cylinder) |
| Rational divisions | D11 (field equation on tree) | Shows tree structure emerging from dynamics on compact surface |
| Global attractor | D-PRO-LU (Lyapunov uniqueness) | Extends uniqueness to non-orientable domain |
| Odd mode selection | D16 (half-twist) | Connects topological invariant to spectral selection rule |
| Subharmonic | Kawano et al. (2025) | Digital twin of the bowed string subharmonic experiment |

## Simulation specification

```
Domain:       1D ring, N oscillators, antiperiodic BC (θ_{N+1} = θ_1 + π)
Dynamics:     Kuramoto with nearest-neighbor coupling
Frequencies:  Lorentzian(ω₀, γ) or self-consistent g*
Parameters:   N ∈ {3, 5, 8, 13, 21}, K/K_c ∈ [0, 3], ε ∈ [0.01, π]
Initial:      θ_i = 0 + ε·δ_{i,1}
Observables:  - Order parameter r(t) = |1/N Σ exp(iθ_i)|
              - Phase differences Δθ_{i,i+1}(t)
              - Winding number W(t) = (1/2π) Σ (θ_{i+1} - θ_i) mod 2π
              - Time to lock: first t where max|dΔθ/dt| < tolerance
              - Which rational p/q the phase locks to
Output:       Phase diagram (N, K/K_c) → {locked rational, lock time, mode}
Compare:      Same parameters on periodic BC (cylinder) — verify Möbius
              selects odd modes that cylinder does not prefer
```

## Status

**Proposed**: simulation target fully specified. The geometry, dynamics,
boundary conditions, parameters, and observables are all explicit. No
new mathematics is required — this is a numerical experiment using known
equations on a known domain.

**What it would establish**: whether the Möbius container produces exact
rational divisions from a single perturbation of rest, and whether the
odd-mode selection rule holds numerically. If confirmed, the "bounded
container" is not a metaphor — it is a resonant cavity for synchronization
dynamics, and the rational phase structure is its spectrum.

**Open**:
- Extension to 2D Möbius strip (finite width W, transverse modes)
- Klein bottle (compact, non-orientable, no boundary) as the fully
  closed variant
- Connection to the bowed string: match simulation parameters to
  Kawano et al. (2025) experimental conditions
- Self-consistent g* on the Möbius domain: does the field equation
  (Derivation 11) have a different fixed point on the non-orientable
  surface?
- The real question: if this is the right container, does it produce
  the known particle spectrum at the known coupling constants?
