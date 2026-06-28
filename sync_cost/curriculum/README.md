# Curriculum

A reader-facing teaching arc for the framework. The framework's derivation
docs build outward from named mathematical objects (Stern-Brocot trees,
Klein bottles, Farey rationals); this curriculum builds *inward* — starting
from phenomena and constructions a reader can follow with no prior
math background, and arriving at the same named objects from the other
side.

History and naming come *after* the construction. A reader finishes a
module having built the object themselves, then learns what
mathematicians have called it for the last 200 years. The name is the
reward, not the prerequisite.

## How to read it

Modules are numbered in suggested order. Each module is a folder
containing:

- `README.md` — the **assertion** (one or two sentences) and the
  **construction** (the prose + figure that builds the object).
- `engine.py` (or other code) — a **runnable demonstration**. The
  reader can run it, change parameters, see the construction work in
  practice.
- `history.md` — the **naming reveal**. Released after the
  construction. Contains the conventional names, theorem statements,
  dates, and references.

A reader can skip `history.md` entirely on first pass and still
understand everything downstream.

## The modules

0. **Shapes have jobs** — 90°, parabola, square. Each shape is the
   *answer* to a physical or combinatorial question, not a thing to
   recognize. (Necessitates: nothing prior. Plants: orthogonality,
   bifurcation boundary, discrete binary symmetry.)
1. **Two things that affect each other** — coupled pendula on a shared
   support; integer-ratio mode-locking emerges with no integers put
   in by hand. (Necessitates: Module 0. Plants: mode-locking.)
2. **The shape of stable locking** — wedge-shaped stability regions in
   the coupling-vs-mismatch plane. (Necessitates: Module 1. Plants:
   stability wedges. Names: Arnold tongues.)
3. **Combining two locks** — discovering the (a+c)/(b+d) rule by
   tabulation of empirical lock points. (Necessitates: Module 2.
   Plants: combining rule. Names: mediant; Stern 1858 / Brocot 1860.)
4. **The tree the rule builds** — iterating the mediant generates
   every rational exactly once. (Necessitates: Module 3. Plants:
   enumeration of rationals. Names: Stern-Brocot tree, Farey sequence.)
5. **Where the joint state lives** — phase tori, quotients by physical
   symmetries, and what surfaces survive the exclusions.
   (Necessitates: Module 1. Plants: configuration space. Names:
   torus, Möbius strip, Klein bottle, real projective plane.)
6. **Why only 2 and 3** — exhaustive search for consecutive perfect
   powers; (8, 9) is alone. (Necessitates: Module 4. Plants: minimal
   integer pair. Names: Catalan's conjecture, Mihailescu 2002.)
7. **Where on the tree are we** — depth as cosmic address; rational
   constants as positions, not measurements. (Necessitates: Modules
   4–6. Plants: address-vs-quantity. Names: H₀, Ω_Λ = 13/19.)
8. **The named framework** — connecting back to the existing
   derivation graph. The reader can now read any top-tier doc in
   `sync_cost/derivations/` and recognize the construction.

## Status

Active. Module 0 is written as the pattern template. Modules 1–8 are
roadmap-only at this stage; each will be promoted to its own folder
when written.

The arc may be refined as modules are produced and reviewed. The
sequence is currently linear; later versions may admit branches if
sub-arcs become natural (e.g., parallel tracks for "the topology side"
and "the rationals side" through Module 5).

## Companion to existing pedagogy

The only existing audience-facing pedagogical material in the repo —
[`../derivations/medium_change_demo.md`](../derivations/medium_change_demo.md) —
is positioned at roughly Module 7 of this arc: it asks the reader to
distinguish address-from-quantity using the tuba/contrabass/loudspeaker
trio. That demo assumes the reader has already accepted the framework's
move at step 4 ("now make the framework move"). This curriculum is the
on-ramp that arrives at that demo with the construction in hand.

When Module 7 is written, it will integrate `medium_change_demo.md`
directly rather than duplicate it.
