# Two Forces — Coherence and Decoherence

> Every physical system with a tendency toward order has a competing
> tendency toward disorder. The spectral tilt encodes the equilibrium.

## The missing force

Derivations 02 and 04 modeled the spectral tilt with one drive:
synchronization (coupling K pushes oscillators toward coherence).
Derivation 02 attributed the CMB tilt to a synchronization cost gradient across scales; Derivation 04 replaced the cost function with the devil's staircase of the circle map, resolving a wrong-sign running problem and grounding the tilt in mode-locking structure.
The frequency distribution g(ω), shaped by mode-locking, determined
the power spectrum.

This is incomplete. A one-force model has no equilibrium — it either
locks or doesn't. The real system must have a competing tendency:
something that resists coherence, actively maintains disorder, provides
the "slip" to complement the "stick."

## The two forces

**Synchronization** (K): Coupling between oscillators drives them
toward phase-locking. Effective coupling K_eff(ω) varies with
frequency via Arnold tongue structure. Produces order.

**Decoherence** (D): Drives oscillators apart. Candidates:

1. *Noise*: thermal or quantum fluctuations (dθ_i/dt += η_i(t))
2. *Frequency spread*: natural frequencies drift apart
3. *Self-consistency barrier*: the mean field must be constituted
   before it can be synchronized against, and constitution costs work

The steady state is the balance: r(ω) = f(K_eff(ω) / D(ω)).

For the Kuramoto model with Lorentzian frequency distribution:

    r = sqrt(1 - K_c / K_eff)    when K_eff > K_c = 2D
    r = 0                         when K_eff < K_c

The critical coupling K_c = 2D is set by the decoherence strength.

## The Fibonacci pile-up

A surprising result from the numerical exploration: the effective
coupling at 1/φ is NOT the minimum across frequencies. It is
actually near the MAXIMUM.

This happens because the Fibonacci convergents to 1/φ:

    1/2, 2/3, 3/5, 5/8, 8/13, 13/21, 21/34, ...

pile up at 1/φ, and their Arnold tongue tails overlap. No single
tongue captures the golden ratio, but the accumulated edges of all
Fibonacci tongues create an effective resonance there.

| frequency | K_eff | source of coupling |
|-----------|-------|--------------------|
| 1/2       | low   | single wide tongue |
| 1/3       | low   | single wide tongue |
| 1/φ       | HIGH  | Fibonacci pile-up  |

The coupling at simple rationals comes from one robust resonance.
The coupling at 1/φ comes from many fragile, overlapping resonances.
The total is large but the structure is qualitatively different:
marginal, contested, built from tails rather than centers.

## The critical surface

The phase transition occurs where K_eff(ω) = K_c = 2D. This defines
a critical surface in (ω, K, D) space.

When D is tuned so that 1/φ is exactly critical:

- **At 1/φ**: r ≈ 0, system is at the phase boundary
- **Near simple rationals**: K_eff < 2D, system is UNLOCKED (r = 0)
- **Near Fibonacci convergents**: K_eff ≈ 2D, system is near-critical

This is KAM theory in reverse. In KAM, the golden torus is the last
to break under perturbation (increasing chaos). Here, the golden
frequency is the last to FORM under decoherence (increasing disorder).
The Fibonacci pile-up gives it just enough coupling to survive while
everything else falls into incoherence.

## The power spectrum at criticality

The fluctuation power is:

    P(ω) = D / (K_eff(ω)² × (r(ω)² + ε²))

where ε is a regularizer (quantum/thermal floor).

- **Locked** (r >> ε): P ∝ D/(K_eff × r)² — small, quiet
- **Critical** (r ~ ε): P ∝ D/(K_eff × ε)² — large, divergent
- **Unlocked** (r = 0): P ∝ D/(K_eff × ε)² — large but featureless

At criticality, the system has maximum fluctuations — critical
opalescence. The power spectrum PEAKS at the phase boundary.

If the pivot scale sits at or near 1/φ, and 1/φ is at criticality,
then:

1. The power spectrum has its characteristic structure there
2. The tilt comes from the gradient of K_eff across the critical surface
3. The running comes from the curvature of the critical surface
4. The sign of the running depends on which side of the Fibonacci
   pile-up the pivot sits on

## Physical interpretation of D

What IS the decoherence force, physically?

In the Kuramoto model, D is the noise strength — a bath that
randomizes phases. In the cosmological context, candidates include:

1. **Expansion**: the Hubble parameter H acts as a decoherence rate.
   Modes that exit the horizon lose causal contact → phases decohere.
   D ~ H.

2. **Quantum uncertainty**: the uncertainty principle prevents
   perfect phase-locking. D ~ ℏ (or its cosmological analog).

3. **Nonlinearity**: mode-mode coupling scatters phases, acting as
   an effective noise. D depends on the amplitude of fluctuations
   themselves — a self-consistent decoherence.

Option 3 is the most interesting: the system's own fluctuations
provide the decoherence. This makes D state-dependent:

    D_eff ∝ ∫ P(ω') × |coupling(ω, ω')| dω'

The decoherence at frequency ω is driven by the fluctuation power
at all other frequencies. This creates a self-consistent loop:
fluctuations drive decoherence which drives fluctuations.

The fixed point of this loop is the observed power spectrum.

## Connection to the spectral tilt

The spectral tilt n_s - 1 = d ln P / d ln k. In the two-force model:

    n_s - 1 = d ln D / d ln ω
            - 2 d ln K_eff / d ln ω
            - 2 d ln(r² + ε²)^(1/2) / d ln ω

Three contributions:
1. How decoherence varies with scale (if D is scale-dependent)
2. How effective coupling varies with scale (Arnold tongue landscape)
3. How the order parameter varies with scale (proximity to criticality)

Contribution 3 is the new one. Near criticality, r changes rapidly
with ω (because K_eff crosses the critical surface). This contributes
a large, sign-indefinite term to the tilt. The running inherits the
curvature of the critical surface.

## The golden ratio as critical point

Summary of the picture:

- Synchronization and decoherence compete
- The effective coupling landscape K_eff(ω) has structure from
  Arnold tongues, with a Fibonacci pile-up at 1/φ
- The decoherence strength D sets the critical coupling K_c = 2D
- At the right D, the system is critical at 1/φ: the Fibonacci
  pile-up barely overcomes decoherence there, while everything
  else is already incoherent
- The power spectrum reflects this critical state: large fluctuations
  near 1/φ, shaped by the pile-up structure
- The spectral tilt encodes the gradient of the critical surface
- The running encodes its curvature

The golden ratio is not just "the most irrational number." In this
framework, it is the frequency where the tension between coherence
and decoherence is maximally balanced — the critical point of the
coupled oscillator phase transition.

## Status

The numerical exploration (coherence_decoherence.py) confirms the
qualitative picture:
- K_eff peaks near 1/φ due to Fibonacci pile-up
- Setting D critical for 1/φ makes it the last frequency to lock
- n_s ≈ 0.965 with negative running appears in the parameter space

The quantitative magnitudes are not yet controlled — the gaussian
Arnold tongue model is too crude. The next step is either:
1. A proper circle map (standard map) to get realistic tongue shapes
2. An analytical treatment using continued fraction theory directly
3. Self-consistent D (decoherence driven by fluctuations)

## Open questions

1. **What sets D?** If D is self-consistent (driven by fluctuations),
   the system self-tunes to criticality. This would explain why the
   pivot scale is near 1/φ without fine-tuning — it's an attractor.

2. **The ω ↔ k mapping**: we've been treating ω ∝ k. But the
   mapping from oscillator frequency to comoving wavenumber may
   involve the expansion history. If ω ∝ ln k or ω ∝ k^α, the
   tilt and running change.

3. **Why 1/φ and not another noble number?** The noble numbers
   (those with eventually-all-1s continued fractions) are all
   maximally irrational in the same sense. 1/φ is the simplest,
   but is there a selection mechanism?

4. **Connection to n_s = 0.9649**: Is 1 - n_s = 0.0351 expressible
   as a simple function of φ? The numerical coincidence
   1/(4πφ²) = 0.0304 is suggestive but not exact.
