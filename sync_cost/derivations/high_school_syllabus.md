# High School Syllabus — *The Shape of Physics*

A single-semester (15-week) course accessible to advanced high-school students.
Reaches Ω_Λ = 13/19 as the closing result, derived from first principles by
counting on the Stern-Brocot tree at depth 6.

**Course title:** *The Shape of Physics — Why the universe has the shape it does*
**Length:** 15 weeks × 3 contact hours (lecture + lab combined)
**Prereqs:** Algebra II (functions, fractions, parabola), Geometry (unit
circle, basic trig), Pre-calc (sequences, iteration). No calculus.
**Tools:** A graphing calculator or Desmos; access to the
[`prototype/`](prototype/) metronome wall demo.
**Companion documents in this repo:**
`derivations/comparison_class.md`, `derivations/unitless_check.md`,
`derivations/mediant_derivation.md`, `derivations/farey_partition.md`,
`derivations/three_dimensions.md`.

## Learning outcomes

A student finishing this course can:

1. Explain why the mediant (a+c)/(b+d) is the unique combining operation
   forced by betweenness and stability.
2. Build the Stern-Brocot tree by hand to depth 6 and count its nodes.
3. Describe the devil's staircase as the locking pattern of coupled
   oscillators, and identify φ⁻¹ as the last point to lock.
4. Argue informally that ℝ/ℤ = S¹ and use that to motivate why phases
   can't escape the unit circle.
5. **Derive Ω_Λ = 13/19 from the Farey partition at depth 6.**
6. State three things the framework claims that the Standard Model does not.

## Units and weeks

The course has three arcs of five weeks each. Each arc ends with a
hands-on artifact.

### Arc I — *Counting and locking* (Weeks 1–5)

Goal: convince students that simple-rational frequency ratios are stable in
ways that complicated ones are not, and that this stability has a forced
mathematical structure.

- **Week 1 — Two metronomes.** Live demo of two coupled pendulums (or
  smartphone-app metronomes on a board). Students predict; they discover
  locking. Discussion question: *what fraction is the locked rate?*
- **Week 2 — The mediant rule.** Define the mediant. Hand-build the
  Stern-Brocot tree to depth 4. Worksheet: insert (1+2)/(3+5) = 3/8 between
  1/3 and 2/5; verify it is between, and verify no fraction with smaller
  denominator fits. **Reading:** `derivations/mediant_derivation.md` §1.
- **Week 3 — Why this rule and no other.** Two physical properties:
  betweenness (energy conservation) and minimality (stability). Heuristic
  argument that these force the mediant. Worksheet: "make up a different
  combining rule. Show one of the two properties fails."
- **Week 4 — The metronome wall.** Lab session with the
  [`prototype/`](prototype/) demo. Slider exercise: find the K where the
  first cluster forms. Compare to 2/π ≈ 0.637.
- **Week 5 — The devil's staircase.** Build the staircase by hand: at
  each rational p/q with denominator ≤ 6, draw a horizontal step. Watch
  the staircase emerge. **Artifact:** a printed staircase poster.

### Arc II — *Geometry* (Weeks 6–10)

Goal: convince students that the unit circle, the Klein bottle, and the
golden ratio fall out of the structure rather than being decorative.

- **Week 6 — Phases on a circle.** ℝ vs S¹. Wrap a string around a pole;
  the integer is which loop. Discussion: *why can't phases run off to
  infinity?* Tie to conservation laws in the most colloquial possible way.
- **Week 7 — Why the circle is closed.** Triangle inequality on the unit
  circle: |average of N unit vectors| ≤ 1. Worksheet: compute the average
  for two clusters of phases; show |r| ≤ 1 directly.
- **Week 8 — The golden ratio.** φ as the solution to x² = x + 1. Why φ
  is "the worst rational" (slowest convergent). Lab: race three irrationals
  (π, √2, φ) to lock under coupling — φ loses. Connect: *the staircase's
  self-similarity ratio is φ² = φ + 1.*
- **Week 9 — The Klein bottle.** Paper-craft session: build a Möbius
  strip, then a Klein bottle. Identify the antiperiodic twist on one
  loop but not the other. Discussion: *why does that asymmetry matter?*
  (Preview of fermion/boson distinction in Arc III.)
- **Week 10 — The XOR filter.** Show how the antiperiodic twist forces
  certain modes to vanish — exactly four survive at q ∈ {2, 3}. Count by
  hand. **Artifact:** an annotated paper Klein bottle showing the four
  surviving modes.

### Arc III — *Counting becomes physics* (Weeks 11–15)

Goal: count to a real cosmological number, then place that number in
context.

- **Week 11 — The Farey partition.** Define F_n = the fractions p/q
  with q ≤ n in lowest terms. Compute |F_6| = 13 by hand (use Euler's
  totient: 1 + φ(1) + φ(2) + ... + φ(6) = 13). Compute q₂q₃ = 6.
  **Reading:** `derivations/farey_partition.md`.
- **Week 12 — Ω_Λ = 13/19.** State the Farey-partition result:
  Ω_Λ = |F_6| / (|F_6| + q₂q₃) = 13 / (13 + 6) = 13/19 = 0.6842.
  Pull up Planck 2018 measurement: 0.685 ± 0.007. *This is the click
  moment.* Class discussion.
- **Week 13 — Why dimensions are forced.** Sketch (without rigor) that
  d = 3 falls out of the mediant being a 2×2 matrix operation, and the
  group it generates being three-dimensional. **Reading:**
  `derivations/three_dimensions.md` §1 only (skip Lie algebra parts).
- **Week 14 — What we did and did not do.** The framework derives
  Ω_Λ. The Standard Model doesn't try to. Read
  `derivations/comparison_class.md` together. Discussion: *what other
  questions might be derivable, and which aren't?*
- **Week 15 — Final project.** Each student picks one quantity from a
  list (Ω_Λ, sin²θ_W = 8/35, n_s ≈ 0.965, d = 3, three generations) and
  presents an 8-minute talk explaining how it follows from the
  structure. **Artifact:** student presentations recorded.

## Assessment

| Component | Weight | Notes |
|---|---|---|
| Weekly worksheets (W1–W14) | 40% | Lowest two dropped. |
| Three artifacts (staircase poster, Klein bottle, recording) | 30% | One per arc. |
| Midterm at Week 8 | 15% | Cumulative through Arc I + early Arc II. |
| Final presentation (Week 15) | 15% | Group of two; 8 minutes. |

## What's deliberately deferred

This is a structural-only course. The following are *not* covered:

- Brouwer's fixed-point theorem (replaced by hand-wavy "a continuous
  process on a closed shape has a stationary point")
- The Lie algebra dim SL(2,ℝ) = 3 proof (replaced by stating the result)
- Friedmann integration (replaced by stating that the universe age
  follows from H₀ and Ω_Λ)
- Kuramoto self-consistency derivation (replaced by the metronome wall
  demo)
- Full Klein-bottle XOR proof (replaced by counting the four modes by
  hand)

A student who wants more goes on to the collegiate course. The HS
course's success criterion is: *can the student derive Ω_Λ = 13/19 by
counting on the Stern-Brocot tree at depth 6, with no help?* If yes,
the structural intuition has landed.

## Why this works at the HS level

Three reasons the course is HS-tractable despite the deep payoff:

1. **The arithmetic is elementary.** 13 = 1 + φ(1) + φ(2) + φ(3) +
   φ(4) + φ(5) + φ(6) = 1 + 1 + 1 + 2 + 2 + 4 + 2 = 13. A motivated
   tenth-grader can do this in five minutes.

2. **The structural claims are visual.** The metronome wall demo,
   the paper Klein bottle, and the Stern-Brocot tree all admit
   hands-on reproduction.

3. **The "click" is real.** Most HS science courses end at "and then
   you'll learn this in college." This one ends at "we just derived
   the dark-energy fraction by counting fractions, and the value
   matches what astronomers measured." That moment carries a course.

## Pedagogical landmines

Three places where this course can fail without active management:

1. **The numerology charge.** Some students (or skeptical parents)
   will say "13/19 is a coincidence." Defuse with `comparison_class.md`
   and the test from `unitless_check.md`: an alien civilization gets
   the same 13/19, no matter what units they use. The number is
   structural, not numerological.

2. **The "but the Standard Model is fine" objection.** Students may
   feel they're being shown a competing theory. Use Week 14 to
   disabuse: the framework answers questions the Standard Model
   doesn't pose. They are not in competition.

3. **Information overload at Arc III.** Counting to 13 and to 6 by
   hand is fine. Counting to F₂₁ = 17,711 (the CMB pivot level) is
   not. Resist the temptation to push deeper than depth 6 in Week 11.

## Distribution

Single Markdown file plus the prototype demo. Teachers download both,
print the worksheets, and run the demo on a projector or shared link.

## Status

A standalone HS-level adaptation of the three-unit collegiate
sequence (Foundations / Structure / Address). Cited from the
collegiate syllabus as a feeder option for advanced HS students.

The course's structural claims are derived elsewhere in this repo;
this document is the lesson plan, not the proofs.
