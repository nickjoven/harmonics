# Derivation 31: The Speed of Light as Gate Propagation

## Claim

The speed of light is the rate at which the gate of observability
propagates through a coherent medium. It has not been derived within
the framework — it appears in Derivation 6 as one of three Planck
constants, identified with the parabolic (detuning) direction of
SL(2,R) via the Iwasawa decomposition. This derivation gives c its
physical mechanism.

## The pendulum picture

Consider a flat plane filled with pendulums swinging in phase.
A photon must pass through the center of each pendulum — the
equilibrium point, where displacement is zero and velocity is
maximum.

Each pendulum's zero-crossing is a **gate**: a brief window during
which the photon can transit. Outside this window, the pendulum
blocks passage. The gate opens once per half-period, for a duration
set by the pendulum's amplitude and frequency.

If the pendulums are in phase (K = 1, full coherence), their gates
open in a coordinated pattern. A wave of gate-openings sweeps across
the plane. The speed of this wave is the maximum rate at which the
photon can traverse the array.

**The speed of light is the gate propagation speed.**

## Why phase coincidence is required

In the Kuramoto model, the coupling between oscillators i and j is:

    K sin(θ_j − θ_i)

This coupling is **maximum** when θ_j = θ_i (phases coincide) and
**zero** when θ_j − θ_i = π/2 (phases are orthogonal). Information
transfer between two oscillators requires nonzero coupling. The
maximum information transfer occurs at phase coincidence.

This is not a metaphor. In a physical medium:

- Two electromagnetic oscillators exchange energy most efficiently
  at resonance — when their phases align
- A detector absorbs a photon when its internal oscillation matches
  the photon's phase — the photoelectric effect requires frequency
  matching (Einstein 1905)
- A mode-locked laser emits coherent light precisely because all
  cavity modes pass through zero simultaneously — the gates open
  together

The gate is the zero-crossing because that is where the coupling
is real-valued and the oscillator's velocity (rate of phase change)
is maximum. At zero displacement, all the energy is kinetic — the
oscillator is maximally available for interaction.

## The gate width

For a pendulum (or any oscillator) with amplitude A, frequency ω,
and a photon that requires the gap to be wider than some minimum δ:

    x(t) = A sin(ωt)

The gate is open when |x(t)| < δ, i.e., when |sin(ωt)| < δ/A.
For small δ/A, this occurs near t = nπ/ω, and the gate duration is:

    Δt_gate ≈ 2δ/(Aω)

In the framework's language, the gate width is the **tongue width**
Δθ at the zero-crossing of the coupling function. For a mode-locked
state at p/q:

    Δθ(p/q, K) ~ (K/2)^q

The gate is wider for:
- Stronger coupling (larger K)
- Simpler ratios (smaller q — wider Arnold tongues)
- Proximity to the tongue center (smaller detuning)

## Observability is a sliding window

At each point in space, the gate opens periodically. The photon
experiences the medium as a sequence of windows: open, closed, open,
closed. The photon can only advance during an open window.

In a coherent array (K = 1), the windows are correlated. The phase
relationship between adjacent oscillators determines when each gate
opens relative to its neighbor. For a wave with phase gradient k:

    θ_n = ωt − kx_n

The gate at position x_n opens when θ_n = 0, i.e., at time:

    t_n = kx_n/ω

The gate-opening sweeps across the array at speed:

    c = ω/k

This is the phase velocity of the coherent wave. The photon rides
the wave of gate-openings. It cannot outrun this wave because there
is no open gate ahead of the wavefront.

**Observability is a sliding window** that moves at the phase
velocity of the medium's coherent oscillation. What you can observe
at any given moment is determined by which gates are currently open.
The window slides at speed c.

## Why c is the maximum

### 1. Coherence sets the gate correlation

At K = 1 (critical coupling), all oscillators are phase-locked.
The gates open in a perfectly coordinated wave. The phase gradient
k is determined by the dispersion relation of the locked medium.
The speed c = ω/k is the fastest possible gate propagation because:

- At K < 1 (subcritical), some oscillators are unlocked. Their
  gates open at uncorrelated times — random noise superimposed
  on the coherent wave. The effective gate propagation speed is
  reduced by the fraction of uncorrelated gates.

- At K > 1 (supercritical, if it existed), the tongues overlap
  and the system is multiply locked — but the circle map at K > 1
  is chaotic. The gates are correlated but the correlation is
  complex (multi-valued winding number). Information propagation
  in a chaotic medium is not faster than in a coherent one —
  it is degraded by the chaos.

K = 1 is the unique coupling strength that produces perfect
coherence with single-valued phase. It gives the maximum gate
correlation and therefore the maximum information speed.

### 2. You cannot open a gate that isn't there

A photon traveling faster than c would arrive at a gate before it
opens. In the oscillator picture: the photon would arrive at an
oscillator whose phase has not yet reached the zero-crossing. The
coupling sin(θ_j − θ_i) would be nonzero but the interaction
would require the receiving oscillator to jump to a different phase
— which costs energy proportional to the phase difference.

The cost of jumping:

    ΔE ~ K(1 − cos(Δθ))

For the jump to occur spontaneously, the phase difference Δθ must
be within the tongue width. For Δθ outside the tongue (the gate is
closed), the oscillator cannot absorb the information without being
kicked out of its locked state — which destroys the coherence that
defined c in the first place.

Faster-than-c propagation is self-defeating: it destroys the
coherent medium that would carry the signal.

### 3. The Iwasawa connection

Derivation 6 identifies c with the parabolic (nilpotent) generator
N₊ of SL(2,R) via the Iwasawa decomposition KAN:

    K = SO(2)           compact     → phase (ℏ)
    A = positive diag   split       → amplitude (G)
    N = upper unipot    nilpotent   → detuning (c)

The nilpotent generator N₊ = ((0,1),(0,0)) produces pure shear:
a linear displacement proportional to time with no oscillation and
no scaling. This IS constant-velocity propagation. The speed of
light is the physical scale of the shear generator.

The nilpotency is significant: N₊² = 0. The shear does not
accelerate — it propagates at constant speed. This is the statement
that c is constant: the gate sweeps at a fixed rate determined by
the medium's coherence, independent of the source's motion.

In the Iwasawa factorization, every element g ∈ SL(2,R) decomposes
uniquely as g = kan. The n-component is the shear, and its magnitude
is the detuning between the oscillator's natural frequency and the
mean field. The maximum detuning that still permits locking (the
tongue boundary) sets the maximum shear — which is c.

## Coherence represents speed differential

Two oscillators in the same coherent domain (locked to the same
tongue) have:
- Zero relative phase drift
- Gates that open in fixed relation
- Zero "speed differential" — same rest frame

Two oscillators in different coherent domains (different tongues,
or one locked and one unlocked) have:
- Nonzero relative phase drift
- Gates that open at uncorrelated times
- Nonzero "speed differential" — different rest frames

The Lorentz boost connecting two frames is, in the framework, the
relative phase gradient between two coherent domains. From
Derivation 14:

    SL(2,C) / SL(2,R) ≅ boost directions ≡ time

The complexification SL(2,C) of SL(2,R) arises from the complex
order parameter r·e^{iψ}. The real part (SL(2,R)) is the spatial
manifold — the coherent medium. The imaginary part (the quotient)
is the boost — the relative phase between two copies of the medium.

The speed of light c is the maximum boost: the maximum relative
phase gradient that preserves ANY gate correlation between the two
domains. Beyond c, the gates are completely uncorrelated — no
information can pass.

In the pendulum picture: if you run past the pendulums faster than
c, the zero-crossings you encounter are effectively random — you
cannot predict when the next gate will open. The coherent wave that
defines "the medium" is invisible to you. You are in a different
coherence class.

## The speed is set by the medium, not the source

The gate propagation speed is a property of the array, not of the
photon. Different pendulum arrays (different frequencies, spacings,
couplings) could have different gate speeds. But the framework says
ALL coupled oscillators at K = 1 produce the SAME c. Why?

Because c is not ω/k for a particular wave. It is the ratio of the
two scales forced by the group structure:

    c = (spatial coherence scale) / (temporal coherence scale)

Both scales are set by SL(2,R):
- The spatial scale comes from the N₊ generator (detuning/shear)
- The temporal scale comes from the K generator (phase/rotation)
- Their ratio is fixed by the group's structure constants: [E,F] = H

The commutation relations of sl(2,R) fix the ratio between the
three generators. Since c is the ratio of the parabolic to the
compact generator, and this ratio is determined algebraically, c is
a structural constant — not a property of any particular wave, but
of the group that all waves inhabit.

This is why c is the same in all frames: it is not the speed of a
thing, but the conversion factor between two directions in the Lie
algebra. Changing frames (applying a boost) is an SL(2,C)
transformation, which preserves the sl(2,R) commutation relations,
which preserve the ratio.

## The gate and the tongue boundary

The gate at each pendulum has a width (duration of opening) and a
period (time between openings). These are:

    Gate width:   Δt ~ Δθ/ω ~ (K/2)^q / ω
    Gate period:  T = 2π/ω (for winding number 1)
                  T = 2πq/ω (for winding number p/q)

The duty cycle (fraction of time the gate is open):

    duty = Δt/T ~ (K/2)^q / (2πq)

At K = 1, for the fundamental mode (q = 1):

    duty ~ 1/(2π) ≈ 16%

For higher modes (q > 1):

    duty ~ (1/2)^q / (2πq) → 0 exponentially

This is the tongue structure seen from the gate perspective. Simple
modes (small q) have wide gates — they are easy to traverse. Complex
modes (large q) have narrow gates — they are hard to traverse. The
devil's staircase is the catalog of gate widths across all modes.

At the tongue boundary (saddle-node bifurcation), the gate width
goes to zero:

    Δθ → 0 as ε → 0

A photon approaching a tongue boundary encounters an infinitely
narrow gate — it cannot pass. This is the mechanism by which
measurement occurs: the system must resolve which side of the
boundary it falls on (which tongue the photon enters). The
resolution time τ ∝ 1/√ε (Derivation 7) is the time spent waiting
for the gate to open wide enough.

## What this derives

| Quantity | Before D31 | After D31 |
|----------|-----------|-----------|
| c exists | Postulated as Planck constant | **Derived**: gate propagation speed of coherent medium |
| c is maximum | Assumed (special relativity) | **Derived**: K=1 gives maximum gate correlation; K<1 or K>1 degrade it |
| c is constant | Assumed (Lorentz invariance) | **Derived**: c is an algebraic ratio in sl(2,R), preserved by all SL(2,C) transformations |
| c is frame-independent | Assumed (Einstein 1905) | **Derived**: c is a structure constant of the group, not a property of any wave |
| c relates to ℏ and G | Dimensional analysis only | **Derived**: Iwasawa KAN, three generators of the self-sustaining loop |

## The three constants as gate properties

The Planck loop (Derivation 6) now reads:

    ℏ — gate width (how narrow the observability window is)
    c — gate propagation speed (how fast the window sweeps)
    G — gate coupling depth (how many oscillators the window spans)

The self-sustaining loop:

    gate width (ℏ) → gate speed (c) → gate depth (G) → gate width (ℏ)
    └──────────────────────────────────────────────────────────────────┘

- Without gate width (ℏ → 0): the gate is always closed. No
  information exchange. No quantum mechanics.
- Without gate speed (c → 0 or ∞): no propagation (static) or
  instantaneous (no locality). No detuning, no tongue boundaries,
  no staircase.
- Without gate depth (G → 0): each oscillator is isolated. No
  mean field, no self-consistency, no gravity.

The Planck scale l_P = √(ℏG/c³) is the spatial extent of the
smallest self-sustaining gate: the minimum domain where the gate
can open (ℏ), propagate (c), couple back (G), and open again (ℏ)
before coherence is lost.

## Open questions

1. **The numerical value.** This derivation explains WHY c exists
   and WHY it has its properties (constant, maximum, frame-independent).
   It does not derive the numerical value c = 299,792,458 m/s. The
   value depends on the unit system — which is to say, on what we
   choose to call "one meter" and "one second." In natural units
   (Planck), c = 1 by definition. The content of this derivation is
   that c = 1 is not a choice of units but a structural fact about
   the Lie algebra.

2. **The dispersion relation.** The gate speed c = ω/k requires
   a specific dispersion relation: ω = ck (linear, no dispersion).
   In the framework, this should follow from the K = 1 limit of
   the rational field equation (Derivation 11), where all tongues
   are filled and the staircase becomes a smooth function. The
   linearity of the dispersion relation would then be a consequence
   of the complete filling — no gaps to scatter off of.

3. **Massive particles.** A massive particle does not travel at c.
   In the gate picture, it is an oscillator that is not perfectly
   phase-locked — it has a small detuning from the coherent wave.
   Its effective gate propagation speed is c × cos(detuning), which
   is always less than c. The detuning angle is the rapidity. This
   connects to the Lorentz factor: γ = 1/cos(detuning) → ∞ as
   detuning → π/2 (maximum detuning = maximum speed = c itself,
   unattainable by a massive particle because it would require
   perfect locking).

4. **The photon's mass is zero.** In the gate picture, the photon
   IS the gate — it is not a particle passing through gates, but the
   propagating phase coincidence itself. A photon has zero mass
   because it is not an oscillator with a natural frequency; it is
   the correlation between oscillators. It travels at c because it
   IS c — the sweep of the coherent wavefront.

## Status

**New derivation.** The mechanism (gate propagation) is physical
and connects to established framework results:

- Derivation 6: c as parabolic generator of SL(2,R) (Iwasawa)
- Derivation 14: SL(2,C)/SL(2,R) as boost/time directions
- Derivation 11: rational field equation at K = 1 as gravity
- Derivation 10: four primitives (gate structure requires all four)
- Derivation 30: denomination boundary (gate width vs. gate cost)

The pendulum picture gives physical content to what was previously
a group-theoretic identification. The speed of light is not a
postulate — it is the rate at which phase coincidence propagates
through a self-consistent oscillator medium at critical coupling.

---

## Proof chains

This derivation connects to the proof chains as a structural
result supporting Proposition P5 (SL(2,R) as spatial manifold):

- [**Proof A: Polynomial → General Relativity**](PROOF_A_gravity.md) — c as the N-factor in Iwasawa KAN
- [**Proof B: Polynomial → Quantum Mechanics**](PROOF_B_quantum.md) — gate width as ℏ, subcritical K < 1
- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — c connecting the two sectors
