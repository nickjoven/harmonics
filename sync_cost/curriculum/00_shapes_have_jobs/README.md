# Module 0 — Shapes have jobs

## The assertion

Three shapes you already recognize — a 90° angle, a parabola, a square —
are not things to recognize. Each is the *answer* to a physical or
combinatorial question. This module reconstructs the question each
shape answers, so the shape arrives as something forced, not given.

## Why this module exists

Standard math education teaches shapes as objects of recognition. You
learn that a parabola is bowl-shaped, has a vertex, has an equation
y = ax² + bx + c. You learn to find them and calculate things about
them. What you do not learn — and what this curriculum needs you to
have — is *what a parabola is for*: what kind of question has a
parabola as its answer.

Without that recasting, every shape in the curriculum that follows
arrives as a brittle symbol. With it, shapes become roles, and the
later modules can put roles together into something larger.

This module is the foundation. Three short constructions, each
answering one question of the form "what shape does this constraint
force?"

## 90° — the angle at which force does no work

A box sits on a flat floor. You push it. If you push it forward, it
speeds up. If you push it sideways while it moves forward, the
sideways push contributes nothing to how fast it moves forward — its
speed in the forward direction is unaffected by the sideways push.

The angle at which a push contributes nothing to forward motion is
what we call 90°.

This is the *only* angle with this property. At any other angle, some
component of the push aligns with the direction of motion and changes
the speed. At 90°, no component aligns — the push and the motion are
*orthogonal*, which means "they do not share any direction at all."

Run `python3 engine.py --shape angle` and watch the angle sweep from
0° to 180°. The output is the rate at which a unit push changes
kinetic energy. The curve crosses zero exactly at 90°.

90° is not a corner. It is the *answer* to "at what angle does a push
decouple from motion?"

## Parabola — the trajectory that is exactly on the boundary

Throw a ball upward. It comes back down. The path it traces, against
time, is curved.

Throw it harder, and harder. The path stretches. At some critical
launch speed — the escape speed — the ball never returns: it leaves
forever. Below that speed, the path is bounded (a closed shape, an
ellipse in the orbital case). Above it, the path is unbounded (an
open shape, a hyperbola).

At *exactly* the critical speed, the path is neither. It is the
boundary case. That boundary trajectory traces a *parabola*.

A parabola is not a bowl. It is the *shape of the boundary between
bound and unbound*. In any setting with a stable state on one side
and an escape on the other, the parabola appears as the line that
separates the two regimes.

Run `python3 engine.py --shape parabola` and watch the orbit type as
launch speed increases past escape speed. The parabola appears at
exactly one value, between the ellipse and the hyperbola.

The parabola is the answer to "what shape is the boundary between
captured and free?"

## Square — the simplest tile with binary rotational structure

A circle has continuous rotational symmetry — any angle of rotation
leaves it unchanged. A polygon has discrete rotational symmetry —
only certain angles work. A regular triangle: 120°. A regular square:
90°. A regular pentagon: 72°. A regular hexagon: 60°.

Two constraints single the square out:

1. **It tiles the plane.** Only three regular polygons do: the
   triangle (interior angle 60°, six fit around a vertex), the
   square (90°, four fit), and the hexagon (120°, three fit). The
   pentagon (108°) does not — 360 ÷ 108 is not an integer. Neither
   does any regular polygon with seven or more sides.

2. **Its rotational symmetry is a power of two.** Among the three
   tilers, only the square admits the binary chain of half-turn,
   quarter-turn, eighth-turn, sixteenth-turn — each a symmetry of
   the square lattice. The triangle and hexagon admit thirds and
   sixths but not the binary refinements.

The square is the unique regular polygon that is *both* a plane-tile
*and* binary-rotationally-divisible. It is the simplest discrete
object that combines spatial filling with the structure of repeated
halving.

Run `python3 engine.py --shape square` to see the table: for each
regular N-gon up to N = 12, the rotational order, whether it tiles,
and whether its rotational order is divisible by four. Only N = 4
satisfies all three (tiles, and order divisible by 4, and is
non-trivial).

The square is the answer to "what is the simplest shape that tiles
the plane *and* admits the binary structure of halving?"

## What this prepares for

Three roles have been planted, each of which the next modules will
need:

- **Orthogonality** (the 90° role) — when two oscillators interact,
  there is a coordinate change that decouples them; the decoupled
  axes are *at right angles* to the coupling axis. The "force does
  no work" version of 90° is the version that makes this
  decomposition possible.

- **Boundary between captured and free** (the parabola role) — when
  two oscillators are weakly coupled, the boundary between "they
  lock" and "they drift" is a parabola in coupling-strength vs.
  frequency-mismatch space. The parabola will reappear as the most
  important continuous shape in the framework.

- **Tiling with binary rotational structure** (the square role) —
  when the locking pattern is forced to be both space-filling on the
  joint state and recursively bisectable, the answer is discrete and
  small. This is where integer mode counts come from, and where the
  binary structure of every later tree in the curriculum begins.

Module 1 begins with two pendula on a shared support — the simplest
physical system in which all three roles will arrive together.

History and naming for the three shapes (Euclid, Apollonius,
crystallography) is in [`history.md`](history.md). Read it after you
can comfortably re-describe each shape as its role, not its picture.
