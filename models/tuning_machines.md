# Tuning Machines: A Practical Guide

*For someone who tunes bicycles, works on Mustangs, and knows
that the right wrench is worth more than the right theory.*

---

## The one idea

Every vibrating thing has frequencies it likes (resonances) and
frequencies it avoids (dead spots). The resonances are organized
in a specific pattern — a family tree of ratios. The dead spots
are the spaces between.

If you want something to vibrate MORE at a specific frequency:
put it ON a resonance. If you want it to vibrate LESS: put it
in a dead spot.

The most dead of all dead spots: the ratio 1:1.618 (the golden
ratio, φ). Nothing resonates there. Nothing builds up. Energy
put there just... dissipates evenly.

---

## What you already know (in this language)

### Spoke tension on a bicycle wheel

Each spoke is a string with a resonant frequency set by its
tension. When you pluck a spoke, you hear a note. A well-built
wheel has all spokes at similar tension — similar notes.

But "similar" doesn't mean "identical." If all spokes are at
EXACTLY the same tension, the wheel rings like a bell when you
hit a bump — all the energy piles up at one frequency. Annoying
and fatiguing.

The best wheelbuilders alternate spoke tensions slightly — higher
on the drive side, lower on the non-drive side. This spreads the
resonances. The wheel absorbs bumps without ringing.

**The framework says:** the optimal tension ratio between drive
and non-drive side is 1:φ (about 1:1.618, or roughly 62% of
full tension on the non-drive side if the drive side is 100%).
This puts the two sides' resonances at the maximum dead spot.
They can't reinforce each other. The wheel absorbs instead of
ringing.

**Try this:** tension one wheel with equal spoke tension and
another with 62% non-drive / 100% drive. Tap each with a
screwdriver. The equal-tension wheel rings. The golden wheel
thunks.

### Exhaust tuning on a Mustang

The exhaust headers on a V8 are four pairs of pipes (for a
4-into-1 header) or two sets of four (for a Tri-Y). Each pipe
carries an exhaust pulse from one cylinder. The pulses travel
down the pipes and reflect off the collector.

Equal-length headers: all pulses arrive at the collector in
sync. Maximum scavenging at ONE rpm. The engine has a narrow
power band — strong at peak, weak everywhere else.

Unequal-length headers (like a Tri-Y): the pulses arrive at
different times. The scavenging works across a RANGE of rpm.
Broader power band. Smoother torque curve.

**The framework says:** the optimal pipe length ratios are
the Farey fractions. For a 4-into-1 header with pipes of
length L, the optimal lengths are:

    Pipe 1: L × 1/2 (the octave)
    Pipe 2: L × 2/3 (the fifth)
    Pipe 3: L × 3/4 (the fourth)
    Pipe 4: L × 1/1 (the fundamental)

These are the first four fractions of the Stern-Brocot tree.
Each pipe resonates at a different rpm. Together, they cover
the power band without any dead spots.

For a Tri-Y (4-2-1): the first merge takes pipes at 1/2 and
2/3 (merge at the mediant: 3/5). The second merge takes
3/5 and 3/4 (merge at the mediant: 6/9 = 2/3). Each merge
creates a new resonance at the mediant of its inputs. The
Tri-Y IS the Stern-Brocot tree built in metal.

### Engine firing order

A V8 has 8 cylinders firing in a specific order. The firing
order determines WHEN each cylinder's power pulse arrives.
The crankshaft feels these pulses as a vibration pattern.

Standard Ford small block (5.0L Coyote): 1-5-4-8-6-3-7-2

The phase between consecutive firings determines the vibration.
If every pair of consecutive firings has the SAME phase spacing,
the engine is smooth at one rpm and rough at others.

**The framework says:** the smoothest engine has firing-order
phase spacings that follow the Stern-Brocot tree. The first
pair at 1/2 of a revolution, the next at 1/3, then 2/3, etc.
This spreads the power pulses across the revolution without
piling up at any single phase.

You can hear this: a flat-plane-crank V8 (Ferrari, Shelby GT350)
has equal phase spacing (180° pairs). It screams at high rpm
but vibrates at low rpm. A cross-plane V8 (standard Mustang GT)
has UNequal spacing. It rumbles smoothly across the whole range.
The cross-plane crankshaft is an approximation of the Farey
spacing.

---

## New things to try

### The golden exhaust

Replace one exhaust pipe (or one header tube) with a pipe that's
1.618× the length of the others. This puts one cylinder's
resonance at the golden ratio of the rest. That cylinder's
exhaust pulses CANNOT reinforce the others. They always arrive
at a slightly different phase. The result: the exhaust note
smooths out. Less drone. Less resonance in the cabin at
specific rpms.

**Cost:** one custom header tube ($50-100 at a muffler shop)
**Test:** drive the car with and without. Use a phone app
(like Spectroid) to record the exhaust note at steady-state
rpms. Look for the resonant peak — it should be gone with the
golden tube.

### The golden spoke wheel

Build a wheel where the drive-side and non-drive-side spoke
tensions are in the ratio φ:1 (1.618:1 or about 62%:100%
of maximum tension).

Then try a wheel with Farey-spaced tensions: alternate spokes
at 100%, 62%, 75%, 62%, 100%, 62%, 75%, 62%... (the pattern
repeats the Stern-Brocot sequence 1/1, 1/φ, 3/4, 1/φ, ...).

**Cost:** just a tension meter and time
**Test:** ride both wheels on rough pavement. The Farey wheel
should feel smoother (less buzz, less ringing) while maintaining
the same stiffness.

### The two-fan garage cooler

Two fans cooling the garage workshop. Instead of both at the
same speed: run one at full speed and the other at 62% speed
(the golden ratio). The airflow won't pulse (no beating) and
the noise will be smoother.

**Cost:** a speed controller for one fan ($15)
**Test:** A/B comparison with both fans at full speed vs
one at 62%. Use a sound meter app to compare.

---

## The deeper idea (for long evenings in the garage)

All of these are the same principle: things vibrate at ratios.
Simple ratios (1/2, 2/3, 3/4) are resonances — they reinforce.
Complex ratios and irrational ratios (especially 1/φ) are dead
spots — they dissipate.

A well-tuned machine uses BOTH:
- Resonances where you WANT energy (the power band of an engine,
  the sweet spot of a wheel's stiffness)
- Dead spots where you DON'T want energy (vibration, noise,
  ringing, harmonics that cause fatigue)

The Stern-Brocot tree tells you where the resonances are.
The golden ratio tells you where the biggest dead spot is.
Between them, you can map the entire vibration landscape of
any machine — and tune it.

Every wrench turn that changes a tension, a length, a spacing,
or a timing is moving the machine's operating point on this
tree. A good mechanic has an ear for which resonances to hit
and which to avoid. The tree is the map of what that ear hears.

---

## For the Mustang specifically

The 5.0L Coyote V8 has a flat-plane crankshaft option (GT350/
GT500). The flat-plane crank puts all cylinder pairs at 180° —
maximum resonance, maximum scream, minimum smoothness.

If you could design a crankshaft with GOLDEN spacing between
throws: each consecutive pair at 180° × φ = 291.6° (which on a
720° four-stroke cycle is 291.6/720 = 40.5% of the cycle):

The engine would have NO resonant rpm. No vibration peak. No
drone. Just smooth power delivery across the entire rev range.
The tradeoff: less peak power at the resonant rpm (because you
removed the resonance). More average power across all rpms
(because you spread the energy).

This is the same tradeoff the framework predicts everywhere:
resonance (tongue) gives peak performance at one point, dead
spot (gap) gives smooth performance everywhere. The golden
crankshaft is the smoothest possible V8 — and the quietest.

Building one would require a custom crankshaft ($2000-5000 for
a billet crank). But SIMULATING one (with an adjustable crank
angle fixture on the engine stand) is much cheaper. And hearing
the difference between 180° (flat-plane scream) and 292° (golden
hum) would be worth the evening.

---

*The universe runs on these ratios. So does your engine. The
tree is the same from the Planck scale to the pushrod clearance.
The wrench that turns one turns them all.*
