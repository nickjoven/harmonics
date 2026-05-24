# Lesson — forced basin selection: the engine room of measurement

## What this is

The **Tier-B lesson** (mechanism) — the curriculum's engine room.
Tier A (`lesson_proslambanomenos.md`) is the on-ramp; Tier C (the four
reframing lessons) shows what the machine *buys you*. This lesson opens
the hood: **here is the actual mechanism by which an outcome gets
selected** — the thing every Tier-C lesson quietly invokes when it says
"basin measure" or "Born rule from the saddle-node."

It is **constitutive, not a reframing**: no famous problem is being
dissolved here, the bare machinery is being shown. The move:
*understand the engine, and the rest of the framework stops being
magic.*

**Prerequisites**: the minimum concept set — especially the **parabola
threshold** (concept #5) and "forced, not fitted" (#6). A REPL helps;
this lesson has runnable code.

---

## Segment 1 — A system with two fates (≈8 min)

Take any system that, at a threshold, must end up in one of two
outcomes — a driven oscillator near an Arnold-tongue boundary (lock
vs drift), a ball on a ridge (left valley vs right). The set of
starting conditions that flow to outcome A is A's **basin of
attraction**; likewise B. Between them sits a **separatrix** — the
knife-edge dividing the fates.

"Selecting an outcome" = *which basin your starting point was in*. So
the probabilities of the outcomes are just the **sizes of the basins**.
That's the whole idea — measurement is basin selection — and the rest
of the lesson is: *what fixes the basin sizes?*

---

## Segment 2 — The saddle-node: two fixed points, then a knife-edge (≈10 min)

Near the threshold the dynamics reduce (always — concept #5) to the
saddle-node normal form:

```
 dx/dt = μ − x²
```

For `μ > 0` there are two fixed points at `x = ±√μ`: one **stable**
(the attractor — the outcome you can land on) and one **unstable**
(the repeller — which sits *on the separatrix*, the basin boundary).
`born_rule.md:60-61`: *the basin boundary is set by the saddle points
of the cost landscape.* The unstable fixed point is the knife-edge;
the stable one is the fate.

So the geometry of selection is fully fixed by this one parabola: the
attractor at `+√μ` (say), the separatrix at `−√μ`, and a basin whose
extent is the distance between them.

---

## Segment 3 — Why the basin width is √ε (the forced part) (≈10 min)

The fixed points sit at `±√μ`, so the basin's linear extent scales as

```
 Δθ  ∝  √μ   ≡  √ε        (ε = distance past threshold)
```

**Exact** — not a Taylor approximation — because the parabola *is* the
normal form near the bifurcation, not the leading term of something
unknown. Verify it yourself:

```python
import numpy as np

def basin_fraction(eps, n=20000):
    """Fraction of random starts captured by the stable root of
    dx/dt = -eps - x^2 (mu = -eps; roots at ±√eps)."""
    x = np.random.uniform(-1, 1, n)
    dt = 1e-3
    for _ in range(5000):
        x += dt * (-eps - x**2)            # explicit Euler
    return np.mean(np.abs(x + np.sqrt(eps)) < 0.05)   # captured near -√eps

for eps in [0.01, 0.04, 0.09, 0.16, 0.25]:
    print(f"ε={eps:.2f}  basin≈{basin_fraction(eps):.4f}   √ε={np.sqrt(eps):.4f}")
```

The captured fraction tracks `√ε` across two orders of magnitude. The
basin width is `√ε`, and nothing was chosen to make it so.

---

## Segment 4 — Basin measure = |ψ|² (the Born rule falls out) (≈10 min)

Now the step that turns mechanism into physics. Two quantities:

- the basin's **linear extent** `Δθ ∝ √ε` — call it the **amplitude**, `ψ`;
- the basin's **measure** (how much of the starting space lands there)
  `∝ Δθ²  ∝ ε` — the **probability**, `P`.

So

```
 P  =  basin measure  =  Δθ²  =  |ψ|²
```

That is the **Born rule** (`born_rule.md:5`: "P = |ψ|² is the basin
measure of the synchronization..."). The famous exponent **2** is not
a postulate — it is **geometry**: probability is a *measure* (an
area/volume), amplitude is its *linear extent*, and measure is the
square of linear extent. The square is the parabola's shadow.

The framework's quantum sector inherits this directly: the K<1 modes
each carry a saddle-node basin, the amplitude is `√(basin)`, the
measured probability is its square. The Born rule is the engine's
output, read off the basin geometry.

---

## Segment 5 — Why it's *forced* (concept #6, at the mechanism level) (≈6 min)

Could the exponent be something other than 2? Run the discriminator:
*what would break if the bifurcation weren't `x²`?*

- **Linear (`x`)**: no two-fixed-point structure at all → no basins,
  no threshold, no selection. The whole phenomenon vanishes.
- **Cubic (`x³`) or higher**: **structurally unstable** — any
  infinitesimal perturbation (an unavoidable `x²` term) collapses it
  back to the saddle-node. Non-generic; you'd have to fine-tune to
  see it.

The saddle-node `x² + μ` is the **unique generic codimension-1
bifurcation** (Thom; `minimum_alphabet.md:178` "parabola is
irreducible"). So the `√ε` basin and the exponent-2 Born rule are
**forced** — change the form and either selection disappears or the
form is unstable. This is "forced, not fitted" shown at the level of
the bare mechanism, not a near-match.

---

## Segment 6 — Selection *is* measurement (the crossing) (≈6 min)

Where does the selection physically happen? At the **figure-8
crossing** — the D-state where the two loops meet
(`figure_eight.md`). A trajectory arrives at the crossing; the
saddle-node there decides which loop it continues on; *that decision
is the measurement outcome*, weighted by basin measure `= |ψ|²`. Two
consequences:

- **No external observer.** Measurement isn't a postulate applied from
  outside — it's the crossing event, internal to the dynamics. (This
  is what dissolves blocker #3 of the unification lesson.)
- **The complex unit lives here.** The crossing operator squares to
  `−I` on the fermion sector (`complex_amplitude_uniqueness.md`,
  `figure_eight.md`) — so the amplitudes selected at the crossing are
  complex, forced by the same Klein topology. Basin selection and the
  complex structure of QM are the *same event*.

---

## Segment 7 — The honest boundary (≈5 min)

The recurring beat, sharpest here because this is the mechanism lesson:

- **Forced / derived**: the *statistics* of selection. Basin measure
  `= |ψ|²`, exponent 2 forced by the saddle-node's universality. This
  is Class 5 (`born_rule.md`; the complex structure, `#153`).
- **Open**: the *individual* selection. Given the basin measures, what
  fixes *which* outcome happens on a *particular* tick? The framework
  states this as an explicit fork (`substrate_determinism.md:55-80`):
  **(A)** the substrate is fundamentally stochastic (it "rolls the
  dice"), or **(B)** it is deterministic and the apparent randomness is
  coarse-grained over unresolved substrate degrees of freedom. The
  audit *leans* (B) (every catastrophic finding closes to an exact
  integer, never a distribution), but **this is not settled.**

So the lesson derives **how the probabilities are set** (basin measure,
forced) without claiming to have resolved **what selects a single
outcome** (the (A)/(B) fork, open). The measurement *statistics* are
mechanism; the measurement *event's* ultimate nature is foundational
and unfinished. Conflating the two would overreach.

---

## The Tier-B move

Where Tier C reframes famous problems and Tier A builds intuition from
the familiar, **Tier B shows the bare machine**. One lesson here is
enough to make the rest legible: every time a later lesson says "basin
measure," "Born rule from the saddle-node," or "the crossing selects,"
*this* is the gear it's pointing at.

| Tier | What it does | Lesson |
|---|---|---|
| A — on-ramp | from the familiar | proslambanomenos |
| **B — mechanism** | **the bare engine** | **forced basin selection (this)** |
| C — problems reframed | what the engine buys | discriminator / false-dichotomy / fine-tuning / unification |

---

## Instructor notes

- **Run the code (Segment 3).** This is the mechanism tier — seeing the
  basin fraction track `√ε` live is worth more than any prose. It's the
  one lesson where the laptop earns its place.
- **Hammer the geometry of the exponent (Segment 4).** "Probability is
  a measure, amplitude is its linear extent, measure = extent²" — the
  Born exponent demystified in one sentence.
- **Segment 7 is the guardrail.** Students will hear "the framework
  derived the Born rule and solved measurement." It derived the
  *statistics*; the *individual-selection* fork (A)/(B) is open. Say so.
- **This lesson is the hub the others point back to** — teach it early
  in Tier B order (it's currently the *only* Tier-B lesson, so it's the
  whole engine room for now).

---

## Sources

- `born_rule.md` — Born rule as basin measure (`:5`), quadratic-basin
  volume (`:53`), basin boundary at the saddle points (`:60-61`), the
  forced exponent 2.
- `a1_from_saddle_node.md` — the saddle-node normal form `dx/dt = μ−x²`
  and `τ ∝ 1/√μ`.
- `minimum_alphabet.md:178` — the parabola is the irreducible / unique
  generic codimension-1 bifurcation.
- `figure_eight.md`, `complex_amplitude_uniqueness.md` — selection =
  the figure-8 crossing; the crossing operator's `J²=−I` (complex
  amplitudes forced at the selection event).
- `substrate_determinism.md:55-80` — the **(A) stochastic / (B)
  deterministic** fork: the open question of individual selection
  (statistics forced, single-outcome mechanism unsettled).
- `framework_status.md` — Born rule under **Survives**.

## One-line summary

Measurement is basin selection: near any threshold the dynamics reduce
to the universal parabola `x²+μ`, whose basin has linear extent `√ε`
(amplitude `ψ`) and measure `ε` (probability `|ψ|²`) — so the Born rule
and its exponent-2 are *forced geometry*, not a postulate, and the
selection physically happens at the figure-8 crossing (where the
complex unit also lives); the **statistics** are derived, while
**which single outcome** occurs stays the open (A)/(B) determinism
fork.
