# Module 2 — History and naming

Read this after working through `README.md` and `engine.py`. You built
two things without names: the independent combinations that reorganize
two linearly coupled oscillators, and the shared rhythm two
nonlinearly coupled oscillators fall into. Both have names, and the
second one has a first-recorded-sighting that is one of the best
stories in the history of physics.

## The independent combinations — normal modes

The two special combinations of Regime 1 — both pendula together
(slow), the two opposed (fast) — are called **normal modes**. A normal
mode is a pattern of motion in which every part of a coupled system
oscillates at a *single* shared frequency, so that the pattern keeps
its shape and simply breathes in and out. Any motion of the coupled
system, however complicated, is a sum of its normal modes.

The systematic theory is due to **Joseph-Louis Lagrange** (*Mécanique
analytique*, 1788) and was given its full treatment for vibrating
systems by **Lord Rayleigh** (*The Theory of Sound*, 1877). Rayleigh
is also the source of the modern understanding of the slow throb you
watched the energy make: the **beat**, an amplitude oscillation at the
*difference* of two nearby frequencies. Two normal modes at ω_s and
ω_d beat against each other at ω_d − ω_s, and that beat is the energy
sloshing from one pendulum to the other and back.

The right angle between the normal-mode axes is not a coincidence of
this example. For any system whose energy is a sum of squared
displacements and squared velocities — which covers essentially every
small-oscillation problem — the normal modes are guaranteed to be
mutually **orthogonal**. This is the same orthogonality Module 0
introduced through the right angle "at which a push does no work,"
now doing structural work: orthogonal modes cannot pump energy into
one another, which is exactly why each evolves independently.

## The shared rhythm — synchronization, entrainment, mode-locking

The phenomenon of Regime 2 — two oscillators of different natural
frequency abandoning their own rhythms for a shared one once coupled
strongly enough — has three interchangeable names, depending on field:
**synchronization**, **entrainment**, and **mode-locking**. All three
name the same event: the frequency ratio of two coupled oscillators
snapping to a fixed rational value and holding there against
perturbation.

Its first recorded observation is famous. In **February 1665**,
**Christiaan Huygens**, confined to bed by illness, noticed that two of
his pendulum clocks hanging from the same wooden beam had drifted into
*exactly opposite* swings — and that if he disturbed one, within about
half an hour they returned to the same opposed lockstep. He traced the
cause to tiny vibrations passing through the shared beam and called it,
in a letter to his father, *"the sympathy of two clocks."* That shared
beam is the "one medium" of this module's title; those two clocks are
the two waves; the opposed lockstep is the 1 : 1 mode-lock (in
antiphase). Huygens had found, and correctly explained, coupled-
oscillator synchronization 310 years before it had a mathematical
theory.

## The locking threshold — Adler, and the two-oscillator Kuramoto model

The equation you integrated for the phase lag,

```
    φ' = Δω − 2K sin φ,
```

is the **Adler equation**, written down by **Robert Adler** in 1946
("A Study of Locking Phenomena in Oscillators") to explain how one
electronic oscillator can be captured by another. Its content is
exactly the threshold you measured: a stationary lag (a lock) exists
only when |Δω| ≤ 2K, i.e. when the coupling K reaches
**K_c = Δω/2**. Below threshold the lag runs instead of resting, and
its running rate — the beat you tabulated — is √(Δω² − (2K)²), which
collapses to zero with a vertical tangent at K_c. That collapse is
**critical slowing down**, a signature shared with phase transitions
throughout physics.

The symmetric two-oscillator system,

```
    θ₁' = ω₁ + K sin(θ₂ − θ₁),   θ₂' = ω₂ + K sin(θ₁ − θ₂),
```

is the smallest case of the **Kuramoto model** (Yoshiki Kuramoto,
1975), the standard model of synchronization for large populations of
coupled oscillators. The threshold K_c = Δω/2 is the two-oscillator
Kuramoto locking threshold; it is the same K_c that appears throughout
the framework's own substrate dynamics.

## The wedge, deferred

The locked band |Δω| ≤ 2K that widens with coupling — the wedge you
saw beginning in the `band` demo — is the **1 : 1 Arnold tongue**. The
full family of tongues, one over every rational ratio, is the subject
of Module 3, where the name and its author (Vladimir Arnold, 1961) are
introduced properly. It is deferred because the single wedge you have
seen is not yet the structure; the structure is all the wedges at once,
and how their widths order themselves by the simplicity of the ratio.

## The two kinds of whole number, named

The distinction the module closes on has standard names too:

- The **counting** integers are the *mode numbers* of a bounded
  resonator — the eigenvalue index of a boundary-value problem. This
  is the quantization of a string, a drum, an organ pipe, and (in the
  Schrödinger picture) an electron in a box. It comes from spatial
  boundary conditions.
- The **locking** integers are the *rotation numbers* of coupled
  oscillators — the rational winding ratio of a mode-locked state. This
  is the quantization of the circle map, the phase-locked loop, the
  cardiac pacemaker, and (this framework's claim) the physical
  constants.

Both are real physics. The framework builds on the second. Keeping
them apart is the single most useful thing to carry out of this
module.

## What you now have

Names for everything you constructed: normal modes and beats
(Lagrange, Rayleigh) for the linear regime; synchronization /
entrainment / mode-locking (Huygens' sympathy of clocks, Adler's
threshold, Kuramoto's model) for the nonlinear regime; and the two
kinds of whole number, counting versus locking, cleanly separated.

Module 3 takes the single wedge and asks for the whole family: the
map of every lock at once. Module 4 asks the question that turns two
known locks into a third — and finds the combining rule that generates
every tree in the rest of the curriculum.
