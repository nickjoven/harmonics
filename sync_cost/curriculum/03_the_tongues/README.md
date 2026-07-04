# Module 3 — The tongues

## The assertion

A single driven oscillator can lock to its driver in any whole-number
ratio — one of its cycles per two of the driver's, two per three, three
per five, and so on. Each ratio commands a whole *region* of driving
rates, not a single one, and those regions are wedges: zero-width where
the coupling vanishes, opening as the coupling grows. The wedges tile
the entire map of "driving rate versus coupling strength," one wedge
over every ratio — and the wedge over a *simpler* ratio is *wider*. The
simplest ratio has the widest, most robust lock. That single fact — the
simplest ratio wins — is the selection principle the rest of the
framework stands on.

## Why this module exists

Module 2 coupled two oscillators to each other and got exactly one
lock: 1 : 1, their frequencies meeting in the middle. Mutual coupling
between two equals can only pull them to a common rate. But the
universe is full of oscillators driven by *other* things — a rhythm
imposed from outside, at its own rate, indifferent to the driven
oscillator's preferences. That asymmetry is what opens up all the other
ratios. A driven oscillator need not match its driver one-for-one; it
can fall into step at *any* whole-number ratio, completing p of its
cycles in the time the driver completes q of its.

This module builds that richer picture and extracts from it the one
principle the framework most depends on: of all the locks competing for
a given oscillator, the one with the simplest ratio is the widest and
sturdiest, and so the one the system actually settles into. Everything
downstream — which specific small integers the framework singles out,
and why — is this principle applied.

## From two coupled to one driven

Take a single oscillator from Module 1 and drive it: give it a periodic
push, once per beat of some external rhythm. Between beats it runs
freely; on each beat it gets nudged by an amount that depends on where
in its own cycle it happens to be.

Rather than follow it continuously, watch it *once per beat* — take a
snapshot of its phase at the same moment in every driver-cycle. Each
snapshot determines the next by a single rule:

```
    θ_next = θ_now + Ω − (K / 2π) sin(2π θ_now)
```

Reading it left to right: the phase advances by a baseline amount Ω —
the number of its own cycles the oscillator would complete per beat if
you switched the driving off — minus a nudge whose size is set by the
coupling strength K and whose sign depends on the current phase through
the sine. The sine is the saturating coupling of Module 2, here doing
its work once per beat instead of continuously. Ω is the tunable knob:
the bare frequency ratio between oscillator and driver.

The quantity that matters is the **locking ratio ρ**: the *average*
phase advance per beat over the long run,

```
    ρ  =  (net phase advance) / (number of beats).
```

If ρ settles to a whole-number ratio p/q, the oscillator is locked —
it completes exactly p cycles for every q beats of the driver, forever.
With the coupling off (K = 0), the rule is just θ_next = θ_now + Ω, so
ρ = Ω exactly and the oscillator drifts through every phase, matching
its driver at no fixed ratio. The interesting behavior is all in what
the coupling does to ρ.

## The staircase

Fix the coupling and sweep the bare rate Ω from 0 to 1, measuring the
locking ratio ρ at each setting. Run `python3 engine.py --demo
staircase`. With the coupling off, ρ would track Ω exactly — a straight
diagonal line. With the coupling on, the line breaks into a **staircase**:
over whole *intervals* of Ω the ratio ρ sticks fast at a whole-number
value, held there against the changing rate, before jumping to climb
again.

Each flat tread of the staircase is a lock. The plot makes the ordering
unmistakable: the longest flat tread sits dead center at ρ = 1/2 — the
simplest ratio strictly between 0 and 1 commands the widest interval.
The next-longest treads are at 1/3 and 2/3; shorter ones at the
quarters; shorter still at the fifths. Between the treads, on the
sloped parts, the oscillator never locks — it drifts through its driver
at an unending irrational ratio. Those drifting rates are real and they
have positive measure, but every one of them is bracketed by locks, and
the simpler the neighboring ratio, the wider the lock.

## The width ordering — the simplest ratio wins

Measure the tread widths directly. Run `python3 engine.py --demo
widths`: for each simple ratio p/q between 0 and 1, it reports the
fraction of the rate-axis over which that lock holds (at full coupling,
K = 1):

| ratio p/q | denominator q | lock width |
|-----------|---------------|-----------|
| 1/2       | 2             | 0.074     |
| 1/3, 2/3  | 3             | 0.031     |
| 1/4, 3/4  | 4             | 0.016     |
| 2/5, 3/5  | 5             | 0.010     |

The width falls monotonically as the denominator grows — cut almost in
half at each step. The lock over the simplest ratio is more than seven
times wider than the locks over the fifths, and the gap widens without
bound as the ratios get more complicated: a ratio with a large
denominator has a lock so narrow it is a thread, destroyed by the
faintest mistuning or noise.

This is the whole point of the module. Robustness of a lock is its
width: a wide lock survives large mismatch, drift, and perturbation; a
narrow one does not. Width is set by the *simplicity* of the ratio —
the size of its denominator — and by nothing else. So among all the
locks competing for a given oscillator, **the simplest ratio is the one
that actually survives.** When a physical system settles into a locked
state, it settles into the simplest ratio available in its
neighborhood, because that is the only lock wide enough to hold.

The framework's own statement of this is exact: stability under
coupling means "the smallest-denominator rational has the widest
[lock] and is therefore the unique" selected one
([`README.md`](../../../README.md), opening). The specific integers the
framework singles out later are not chosen — they are the widest locks,
the ones that win this competition.

## One lock is a wedge

Fix the ratio instead of the coupling, and watch the lock as coupling
grows. Run `python3 engine.py --demo wedge`, tracking the 1 : 2 lock as
K rises from 0 to 1. At K = 0 the lock is a single point on the rate
axis (Ω = 1/2, zero width). As K grows the locked interval opens
steadily — 0.002 wide at K = 0.1, 0.073 wide at K = 1 — a wedge rising
from its point on the zero-coupling axis and fanning open.

Every whole-number ratio has such a wedge, rooted at its own point on
the zero-coupling axis. The full map of "rate versus coupling" is these
wedges packed together: broad triangles over the simple ratios,
narrowing to slivers over the complicated ones, with drifting
(un-locked) rates threading between them. The staircase from the first
demo is one horizontal slice across this map at fixed coupling; the
wedge is one vertical column at fixed ratio.

The *edge* of each wedge — the exact rate at which a lock gives way to
drift — is where a stable locked state and an unstable one meet and
annihilate each other. The local shape of that meeting is the parabola
from Module 0, in its "boundary between bound and unbound" role: on one
side of the parabola two states exist (one stable, giving the lock); on
the other side none exist (drift). The parabola that Module 0 planted
as the boundary between captured and free is, quite literally, the
boundary of every wedge in this map.

## What this prepares for

The wedges do not sit in the map at random. Ask the question Module 4
opens with: given two locks the oscillator already has — say its 1 : 2
and its 1 : 3 — which lock appears *between* them as the coupling
weakens and the wide wedges retreat? There is a definite answer, the
widest ratio in the gap, and finding it by tabulation reveals a simple
arithmetic rule for combining the two fractions into the one that sits
between them. That rule is the generator of every tree in the rest of
the curriculum, and it turns this module's picture — wedges ordered by
simplicity — into a structure that enumerates *all* the ratios in the
exact order their locks appear.

History and naming — the once-per-beat rule and the man who mapped its
wedges, the staircase and why it is called what it is, and the rotation
number that measures the locks — is in [`history.md`](history.md). Read
it once you can describe the staircase and the width ordering without
the names: the simplest ratio holds the widest lock, and the widest
lock is the one that wins.
