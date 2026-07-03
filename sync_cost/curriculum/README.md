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

The arc is rooted at a single object: a wave, propagating outward.
Every subsequent module is a consequence — of what waves do, of what
happens when waves share a medium, of what stable patterns the
sharing forces, of the combinatorics of those patterns, and finally
of where on that combinatorial structure we sit. Module 0 is the
prerequisite that the wave construction will draw on; everything
from Module 1 forward traces back to the wave.

0. **Shapes have jobs** — 90°, parabola, square. Each shape is the
   *answer* to a physical or combinatorial question, not a thing to
   recognize. (Necessitates: nothing prior. Plants: orthogonality,
   bifurcation boundary, discrete binary symmetry.)
1. **What a wave is** — restoration + inertia + coupling →
   outward propagation. Three ingredients combine to produce a
   wave; six familiar physical effects fall out as consequences
   without yet being named. (Necessitates: Module 0. Plants:
   the wave-outward root.)
1a. **The six observations** — names for what Module 1 planted:
    Doppler shift, redshift, time dilation, mass-energy
    equivalence, the Planck wall, the Hubble wall. A companion
    module so that recognition is kept structurally separate from
    construction. (Necessitates: Module 1.)
2. **Two waves on the same medium** — what happens when one wave
   is not alone. Normal-mode decomposition, integer-ratio
   mode-locking emerging with no integers put in by hand.
   (Necessitates: Module 1. Plants: mode-locking.)
3. **The shape of stable locking** — wedge-shaped stability
   regions in the coupling-vs-mismatch plane; the boundary is a
   parabola. (Necessitates: Module 2. Plants: stability wedges.
   Names: Arnold tongues.)
4. **Combining two locks** — discovering the (a+c)/(b+d) rule by
   tabulating empirical lock points. (Necessitates: Module 3.
   Plants: combining rule. Names: mediant; Stern 1858 / Brocot 1860.)
5. **The tree the rule builds** — iterating the mediant generates
   every rational exactly once. (Necessitates: Module 4. Plants:
   enumeration of rationals. Names: Stern-Brocot tree, Farey
   sequence.)
6. **Where the joint state lives** — phase tori, quotients by
   physical symmetries, and what surfaces survive the exclusions.
   (Necessitates: Module 2. Plants: configuration space. Names:
   torus, Möbius strip, Klein bottle, real projective plane.)
7. **Why only 2 and 3** — exhaustive search for consecutive perfect
   powers; (8, 9) is alone. (Necessitates: Module 5. Plants:
   minimal integer pair. Names: Catalan's conjecture, Mihailescu 2002.)
8. **Where on the tree are we** — depth as cosmic address; rational
   constants as positions, not measurements. The walls planted in
   Module 1 reappear here as the Planck and Hubble depths; our
   frequency sits deep in the middle. (Necessitates: Modules 5–7.
   Plants: address-vs-quantity. Names: H₀, Ω_Λ = 13/19.)
9. **The named framework** — connecting back to the existing
   derivation graph. The reader can now read any top-tier doc in
   `sync_cost/derivations/` and recognize the construction.

## Status

Active. Modules 0, 1, and 2 are written; Module 1a and Modules 3–9
are roadmap-only at this stage. Each will be promoted to its own
folder when written.

The arc was reindexed early when it became clear that no module could
sit at the root if "a wave" was not constructed first. The original
ordering treated "two oscillators that interact" as the entry point;
that has been pushed to Module 2, and a single wave (the *one*
object every later claim depends on) now occupies Module 1.

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
