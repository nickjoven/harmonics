# Module 2 — Two waves on one medium

## The assertion

When two waves share a single medium, what happens depends on how they
are coupled. If the coupling is *linear*, they reorganize into
independent combinations set at right angles to each other and trade
energy back and forth — but they never fall into step. If the coupling
can *saturate* (a nonlinearity), something new becomes possible: past a
threshold in coupling strength, two waves of different natural
frequency abandon their own rhythms and run at one shared rhythm, in a
whole-number ratio. No whole number was put in. The whole number is
where the framework's integers come from — and it comes from the
coupling, not from counting anything.

## Why this module exists

Module 1 built one wave. The universe does not contain one wave. The
moment two waves occupy the same medium, they interact, and the
character of that interaction is the hinge the entire framework turns
on. Get it right and every later integer — the mode counts, the
rationals, the small primes — has a home. Get it wrong (assume the
integers come from cutting space into pixels) and the framework reads
as just another discretized-spacetime theory, which it explicitly is
not.

This module constructs the interaction in two regimes, in order, and
lets the reader watch the whole numbers appear in the second one with
nothing whole put in by hand.

## Regime 1 — linear coupling reorganizes but does not lock

Take two of the pendulum-like oscillators from Module 1, identical,
each with the same natural frequency, and join them with a weak spring.
Displace the first, hold the second still, and let go.

Run `python3 engine.py --demo normalmodes` and watch the energy in the
first pendulum. It does not stay put. Over about seventeen time units
it drains completely into the second pendulum; over the next seventeen
it drains completely back. The two pendula trade the energy back and
forth, indefinitely, in a slow throb.

Underneath that throb, the coupled pair is doing something exactly
describable. There are two special *combinations* of the two pendula:

- **both moving together**, in the same direction — this combination
  oscillates at the bare natural frequency ω₀, because when both
  pendula move identically the coupling spring is never stretched and
  contributes nothing;
- **the two moving oppositely**, mirror-image — this combination
  oscillates *faster*, at √(ω₀² + 2κ), because now the spring is
  stretched on every swing and adds its stiffness.

These two combinations are the reason for Module 0's right angle. In
the plane whose axes are "position of pendulum 1" and "position of
pendulum 2," the together-combination and the opposite-combination
are two new axes rotated 45° from the originals — and they sit at 90°
to *each other*. That right angle is the orthogonality role from
Module 0 in its "does no work" reading: along each of these axes, the
coupling does no work that would drain energy out of that combination.
Each combination therefore evolves completely independently of the
other, each at its own single frequency. The coupling has not tied the
two pendula together into one rhythm; it has *re-carved* them into two
independent patterns.

The throb you see is just these two independent patterns, at slightly
different frequencies, drifting in and out of phase. When they are in
phase the motion piles onto pendulum 1; a while later, out of phase,
it piles onto pendulum 2. The energy sloshes at the frequency
*difference* of the two patterns.

The essential negative result: **linear coupling never locks.** Two
linearly coupled oscillators of *different* natural frequency do not
fall into a common rhythm at all — they produce a motion built from
two unrelated frequencies that never settle onto a whole-number
relationship. Reorganization, yes. Energy trading, yes. Locking, no.
For that we need the coupling to do something a spring cannot.

## Regime 2 — saturating coupling locks, and the integer appears

Replace the linear spring with a coupling that *saturates* — one whose
pull grows as the two waves fall out of step but then levels off
instead of growing without bound. (Any real coupling does this
eventually; a spring that never saturates is the idealization, not the
rule.) The cleanest form to write is one where each oscillator is
nudged by the *sine* of its phase lag behind the other:

```
    θ₁' = ω₁ + K sin(θ₂ − θ₁)
    θ₂' = ω₂ + K sin(θ₁ − θ₂)
```

Here θ is the phase (where in its cycle each oscillator is), ω is its
natural frequency, and K is the coupling strength. Give the two
oscillators *different* natural frequencies — ω₁ = 1.0 and ω₂ = 1.6, a
mismatch of Δω = 0.6 — and sweep K upward.

Run `python3 engine.py --demo locking`. The quantity measured is the
*beat*: the difference between the two oscillators' actual running
frequencies once the dust settles.

- At **K = 0** (no coupling) each runs at its own frequency; the beat
  is 0.6, the full mismatch.
- As **K rises** the beat shrinks — but not linearly. It follows
  √(Δω² − (2K)²), bending down ever more steeply.
- At **K = 0.3** the beat hits **zero** and stays there. Both
  oscillators now run at *one* frequency. They are locked.

That threshold is not a fitted number. It is exactly
K_c = Δω/2 = 0.3, forced by the coupling equations: a shared rhythm
becomes possible precisely when the coupling K can supply the
2K "pull" needed to bridge the mismatch Δω, i.e. when 2K ≥ Δω.

And here is the whole point of the module. The inputs were three real
numbers — ω₁ = 1.0, ω₂ = 1.6, K. Nowhere among them is a whole number
of any kind. The *output* is that the two oscillators run at a
frequency ratio of exactly **1 : 1** — a whole number, sitting on the
nose, stable against nudges. The 1 was never put in. It is the
attractor the coupling dynamics fall into. **This is where the
framework's integers come from: locked states of coupled waves, not
divisions of space.**

The approach to the lock has a signature worth noticing (visible in
the table): as K climbs toward K_c the beat does not fade smoothly to
zero — it collapses, more and more steeply, because √(Δω² − (2K)²) has
a vertical tangent at the threshold. The system slows critically right
before it locks. That steep collapse is the fingerprint of a genuine
locking transition rather than a gradual blending.

## The locked band, and the first hint of a shape

The 1 : 1 lock is not infinitely fragile. Run
`python3 engine.py --demo band`: hold the coupling fixed at K = 0.3 and
vary the mismatch Δω instead. The pair stays locked for every mismatch
up to Δω = 0.6, and breaks the moment the mismatch exceeds it. The
locked band is exactly |Δω| ≤ 2K.

Raise K and that band widens; lower K and it narrows. If you plot the
locked region in the plane whose axes are "mismatch Δω" and "coupling
K," it is a wedge — a triangle rising to a point at Δω = 0, widening
as K grows. That wedge is the first hint of the shape that Module 3 is
about. And 1 : 1 is not special: there is a wedge like it standing
above *every* whole-number frequency ratio (2 : 1, 3 : 2, 5 : 3, …),
each one a different locked state the same dynamics can fall into. The
whole numbers are not decreed; they are the addresses of the wedges.

## Two kinds of whole number — and which one the framework means

The reader has now met two entirely different ways a whole number can
show up in wave physics, and the difference is the crux of the whole
framework:

- **Counting whole numbers.** A wave trapped in a bounded region fits
  a whole number of half-wavelengths between the walls — one, two,
  three humps, never two-and-a-half. This is the integer `n` in the
  string and pipe formulas from the framework's medium-change demo. It
  comes from the *geometry*: the boundaries, the shape of the box.
- **Locking whole numbers.** Two coupled waves of unequal frequency
  fall into a whole-number *ratio* of running frequencies. This comes
  from the *dynamics*: the coupling, the threshold, the attractor. No
  box, no boundary, no counting of humps — the number is the ratio the
  system locks to.

These are not the same phenomenon wearing two hats. One is spatial
bookkeeping; the other is a dynamical attractor. **The framework's
integers are the second kind.** Its own statement of this is blunt:
the framework's numbers "count mode-locked states, not pixels";
"the discreteness is the dynamics," and "quantization lives in that
coupling, not in the geometry"
([`README.md`](../../../README.md), opening). A reader who leaves this
module with the two kinds of whole number cleanly separated will not
make the single most common error about the framework — reading its
discreteness as space cut into cells.

## What this prepares for

- **Module 3** takes the wedge from the `band` demo seriously and asks
  what the full locked region looks like across all couplings and all
  ratios at once. The answer is a family of wedges, one over every
  rational, with the widest wedges over the simplest ratios — the
  shape the framework's stability arguments live on.
- **Module 4** takes two locks the reader already understands — say a
  1 : 2 and a 1 : 3 — and asks what single ratio sits *between* them as
  the next lock to appear. The answer is a combining rule on the two
  fractions, discovered by tabulation before it is named. That rule is
  the seed of every tree in the rest of the curriculum.

History and naming — the coupled clocks Huygens noticed in 1665, the
independent combinations, the locking threshold, and the people who
named each — is in [`history.md`](history.md). Read it once you can
describe both regimes without the names: the linear one that
reorganizes without locking, and the saturating one that locks into a
whole number nobody put in.
