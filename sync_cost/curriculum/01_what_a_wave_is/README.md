# Module 1 — What a wave is

## The assertion

A wave is the *outward propagation* of a disturbance through a medium
that has three properties: a rest state with a tendency to return to
it, the inertia to overshoot when restored, and the means to pass
disturbances to its neighbors. Given all three, a disturbance does
not stay where it started — it moves.

This module constructs each property from a phenomenon, then puts the
three together and watches the wave appear. Once the wave is on disk,
six familiar physical effects fall out as consequences of the same
construction — planted at the end of this module without yet being
named.

## Why this module exists

Standard physics teaches a wave as a formula: `f(x − vt)`, or `sin(kx
− ωt)`, or a curve drawn on a board. The reader learns to recognize
the shape, find its wavelength and frequency, and compute its phase
velocity. What the reader does not learn — and what this curriculum
needs them to have — is *what makes a wave a wave at all*: under
what conditions does a disturbance propagate, rather than stay where
it started or fade in place?

Without that, every later thing — what we call the Doppler effect,
the redshift, time dilation, mass-energy equivalence, the Planck
scale, the Hubble scale — is a separate fact to memorize. With it,
all six are consequences of the same root structure, and the
framework's deeper claims (mode locking, the mediant, the Klein
bottle, cosmic addresses) arrange themselves as further consequences
along the same outward path.

This module is the root. Three ingredients are constructed, the wave
is assembled from them, and six observations are planted as one-line
hints — names withheld until [Module 1a](../01a_six_observations/).

## Ingredient 1 — restoration

A medium has a *rest state* if there exists a configuration the
medium prefers when undisturbed. "Prefers" means: small displacements
from rest feel a force pulling them back.

The minimal restoring force is one *proportional to displacement*:
displace twice as far, feel twice the force. Why is this the right
choice? Because of the parabola from Module 0.

Module 0 introduced the parabola as the boundary between bound and
unbound. The parabola has a second role, which arrives now: it is
also the *local shape of any minimum*. Near any rest state of any
medium, the energy stored as a function of displacement is a curve
with a minimum. Zoom in close to that minimum and the curve looks
like a parabola — y = ½k·x² for some stiffness k. This is true of
nearly every restoring system you will ever meet, because every
smooth minimum looks parabolic when you stand close enough.

A parabolic energy gives a *linear* restoring force (the slope of a
parabola is a straight line). So the choice "force proportional to
displacement" is not a simplification — it is what the local geometry
of any rest state forces.

Run `python3 engine.py --demo restore` to see this: a particle in a
parabolic well, displaced and released, with the restoring force
plotted against displacement. The force is a straight line through
zero. The particle, with no inertia, snaps to rest and stops. It
does not oscillate.

The parabola is doing real work now. It is not just a recognizable
shape; it is *why* the simplest medium behaves linearly near rest.

## Ingredient 2 — inertia

The particle in the restoring well, released, snaps to rest and stays
there. There is no wave yet — not even an oscillation.

Add inertia. The particle now has mass: when the restoring force
pulls it toward rest, it accelerates, picks up speed, and *cannot
stop at rest* — it overshoots. Past rest, the restoring force now
points the other way. The particle decelerates, reverses, accelerates
back, overshoots again. It oscillates.

The period of this oscillation depends only on the ratio of inertia
(mass) to stiffness:
```
period = 2π · √(mass / stiffness)
```

Heavier particle → slower oscillation. Stiffer well → faster
oscillation. The relation is non-negotiable; it is forced by
restoration + inertia together, with no further structure required.

This is oscillation *at a single point*. It is not yet a wave. A
wave requires that the disturbance propagate — that it move from
where it started to somewhere else. For that, we need a third
ingredient.

Run `python3 engine.py --demo inertia` to see this: same parabolic
well, now with mass. The particle oscillates sinusoidally; the
period scales as √(m/k). Tabulated values are printed for a sweep of
masses.

## Ingredient 3 — coupling

A single point that oscillates is an oscillator, not a wave. Put
many points in a line, each in its own restoring well, each with its
own inertia. Without any further connection between them, each point
oscillates independently. Displace point #5 and points #4 and #6
notice nothing. No propagation.

What couples them is a force between neighbors that responds to their
*relative* displacement — the difference between their positions. If
point #5 is displaced upward by 1 unit and point #6 is at rest, point
#6 feels a force pulling it upward (toward #5). If both are
displaced upward by the same amount, point #6 feels nothing from #5
— because the medium between them is not stretched.

The "relative-displacement" form is forced by the medium's symmetry.
If you translate the entire medium uniformly (every point shifts by
the same amount), nothing is stretched and no internal force can
appear. The only force that respects this is one that vanishes when
all displacements are equal — and that is precisely a force on the
*difference*.

Now we have the recipe. Many points, each with restoring force,
inertia, and a coupling force to its neighbors that depends on the
relative displacement. Displace one point. The displacement pulls
the neighbor toward it. The neighbor's inertia means it
accelerates, then overshoots; it now pulls the next neighbor. The
disturbance moves outward.

Run `python3 engine.py --demo wave` to see this: a chain of fifty
coupled points, an impulse at one end, and a printed snapshot of the
displacement profile at successive times. The disturbance is
localized at t=0; by t=20 it has spread to both sides; by t=60 the
two fronts have traveled halfway down the chain.

**That is a wave.** The speed of propagation is set by the ratio of
coupling strength to inertia: stiffer coupling or lighter inertia
gives a faster wave. The relationship is once again non-negotiable:
```
wave speed = √(coupling stiffness / inertia per length)
```

Three ingredients, one outward propagation. Everything from here on
is a consequence.

## Six observations

The wave is now constructed. Here are six effects that follow from
it — each stated as an observation, each unnamed for now.

1. **Observer motion changes the observed frequency.** If a wave is
   travelling outward through a medium and you walk toward its
   source, you encounter wavefronts more often per second than
   someone standing still. Walk away, and you encounter them less
   often. The wave itself did not change; your relative motion
   through it changed what you measure.

2. **Sources receding at cosmic scale appear shifted to lower
   frequencies.** The same effect at the cosmic scale: light from
   distant galaxies, receding from us as the cosmos stretches, is
   measured at lower frequency than it was emitted. The shift grows
   with distance.

3. **Constant-speed waves force time and distance to be measured
   differently for different observers.** For waves whose
   propagation speed is fixed (the same for every observer no matter
   how they move), no walking-faster-or-slower can change that speed.
   But measurements of frequency *do* change with motion. The only
   way for both to be true at once is for each observer to use their
   own measure of time and distance. The wave's constancy forces
   the geometry.

4. **Confining a wave costs energy proportional to the frequency of
   confinement.** A wave packed into a small region must oscillate
   at a high frequency to fit. Confined energy is proportional to
   the frequency it was confined at. The confined energy of a
   wave, pinned to a small region, is what we call its mass.

5. **A wave cannot be confined arbitrarily small.** Pack a wave into
   a small enough region and the confinement energy (from
   observation 4) is large enough that gravity makes the region into
   its own horizon. Below that confinement scale, no wave can be
   defined. There is a smallest length.

6. **A wave cannot extend arbitrarily large.** At the other extreme,
   the cosmos stretches with time. A wave whose wavelength is longer
   than what the cosmos can stretch in one wave-period never
   completes a cycle. There is a largest length.

The two limits — observation 5 and observation 6 — bracket the band
of wavelengths where coherent waves can exist. Between them is a
range of many decades of wavelength.

## What this prepares for

Our familiar physics — sound, light, the mechanical and chemical
processes that make a body work — lives *deep in the middle* of that
band. Many decades of wavelength separate us from the smallest-scale
wall (observation 5), and many decades separate us from the
largest-scale wall (observation 6).

That is why the behavior at our frequency is extremely stable. We
are far from both walls; no boundary correction matters at our
scale; the wave construction we built here describes what we observe
without modification. The dramatic moves the framework makes
elsewhere — at the smallest scales, at the largest — are *moves at
the walls*. Here, locally, the construction holds plainly.

Module 1a names the six observations: Doppler, redshift, time
dilation, mass-energy equivalence, the Planck wall, the Hubble wall.
Read it any time after this module.

Module 2 takes the next step outward from the wave: *what happens
when two waves try to share a single medium*. The answer is the
first place the integers come in.

History and naming for the wave-mechanics ingredients (Hooke, the
wave equation, d'Alembert) is in [`history.md`](history.md). Read
it after you can describe the wave as the consequence of its three
ingredients, not as a formula you recognize.
