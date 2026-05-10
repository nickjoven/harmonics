# The time-axis split on the Klein bottle

## Claim

On the Klein bottle, two aspects of "time" that conventional physics
bundles together — a clock-like cyclic counter and a forward arrow —
live on **different axes**. This is not a bug. It is a structural
consequence of one direction being orientable and the other not.

The framework's docs have implicitly used both readings without naming
the split, producing apparent contradictions between docs that are
each individually correct about a different aspect of time. This doc
**commits to the distinction itself** as the canonical fact, and
prescribes how subsequent derivations should refer to each aspect.

## The two aspects

In conventional physics on a single time axis:

- **Time-as-clock**: a cyclic counter. Each tick advances the count.
  Recurrence is well-defined.
- **Time-as-arrow**: an irreversibility. Forward and backward are
  distinguishable by physical processes (entropy, dissipation,
  measurement collapse).

Conventionally these are bundled. On the Klein bottle they split:

| Aspect | Direction | Why |
|---|---|---|
| Time-as-clock | y (periodic) | Loop traversal returns cleanly. Counter is unambiguous: after `n` traversals the count is `n`. Observed in the 3×3 simulation as the gentle-ticking axis (~0.2 rad evolution per row). |
| Time-as-arrow | x (antiperiodic) | Traversal sign-flips the field (`f(x+L_x, y) = -f(x, L_y-y)`). Non-orientability provides the symmetry-breaking that gives forward ≠ backward. Carries the rank-1 Fréchet derivative arrow from D46. |

Each is a real aspect of "time" — the framework just doesn't get a
single axis to put both on.

## The convention this doc commits to

**Bare "time" or "temporal direction" is not a meaningful term on the
Klein bottle.** Subsequent derivations must qualify:

- Use **"clock-time"** or **"periodic axis"** when referring to the
  cyclic counter (y-direction).
- Use **"arrow direction"** or **"antiperiodic axis"** when referring
  to the irreversibility-carrying direction (x-direction).
- Use **"the time-axis split"** as a referent when the distinction
  itself is at issue, citing this doc.

When a derivation references existing claims from upstream docs that
say "temporal direction", the reader must determine from context which
aspect is meant. This doc provides the lookup.

## Existing claims, classified

The framework has accumulated a number of claims about "the temporal
direction" or "time". Re-read under the split:

| Claim | Source | Aspect | Reading |
|---|---|---|---|
| "Time is the periodic direction" | `klein_bottle.md:293` | clock | The y-direction is the well-defined cyclic counter. Correct under the split. |
| "Antiperiodic (temporal: local arrow, global non-orientability)" | `klein_bottle_derivation.md:253-255` | arrow | The x-direction carries the irreversibility. Correct under the split. |
| "Antiperiodic in temporal direction, periodic in spatial direction" | `framework_lagrangian.py` Part 1 | arrow | Same as above; the integration domain's orientation-reversing direction is the arrow axis. |
| Friedmann form / Hubble time / cosmological time | `k_of_t_friedmann.md`, `hierarchy_gaussian_lattice.md` | clock | The `t` in Friedmann equations is the cyclic counter. |
| "Walking backwards is CPT" — T = reverse antiperiodic direction | `klein_bottle_derivation.md:447-464` | arrow | T as time-reversal is reversal of the *arrow* direction. CPT compound is a symmetry of the surface. |
| Half-integer wavenumbers from antiperiodic BC | `klein_bottle.md:118-121`, `klein_bottle_derivation.md:335-339` | spatial | Coordinate-Z₂ on the antiperiodic axis. The "antiperiodic" here is the gluing rule of the surface, not the arrow-of-time aspect. |
| Spin-statistics theorem from H₁(K²) torsion | `klein_bottle_derivation.md` Part VII | spatial-Z₂ | Pauli sign comes from coordinate antiperiodicity, not from arrow-time. |
| Rank-1 Fréchet derivative gives the arrow | `D46` | arrow | This is the arrow-direction's content. |
| Kink ↔ antikink under antiperiodic loop | `sine_gordon_substrate.md` | spatial-Z₂ on the antiperiodic axis | Coordinate identification, separate from any temporal interpretation. |

Two takeaways:

1. The "antiperiodic" axis carries multiple structural roles — it is
   simultaneously the spatial direction (per `klein_bottle.md`'s
   convention), the arrow-direction (per the irreversibility argument),
   and the carrier of coordinate-Z₂ (per the spin-statistics and
   soliton derivations). These are not in conflict; the antiperiodic
   axis is rich.

2. The "periodic" axis carries only the clock-counter role. It is
   cleaner.

The apparent contradiction between docs comes from different docs
emphasizing different roles of the antiperiodic axis without naming
the split.

## What this changes for predictions

No observational claim shifts. Every prediction can be re-stated under
the split unambiguously:

- The K=1 continuum limit gives Einstein on a 4-manifold whose time
  axis is the **clock direction** (one periodic axis acting as
  cosmic time, three spatial directions).
- Friedmann dynamics, Hubble running, the cosmic ages — all
  clock-direction.
- The Klein-bottle arrow-direction is not the cosmological clock;
  it is the local-irreversibility direction that carries CPT
  structure, fermion sign, and (with the soliton sector) Z_2-graded
  topological charge.
- Sine-Gordon kinks traverse the **antiperiodic axis**. Whether a
  reader calls that "spatial" or "arrow-time" is a labeling choice;
  the Z_2-graded charge result is the same.

## Usage policy for new derivations

1. Default: use "clock-time" / "periodic axis" / "arrow direction" /
   "antiperiodic axis" instead of the bare term "time" or
   "temporal direction".
2. If the bare term must be used (e.g., quoting an upstream doc),
   add a parenthetical naming the aspect: `time (clock-direction)`
   or `time (arrow-direction)`.
3. When citing `klein_bottle.md:293` ("Time is the periodic
   direction"), read it as a claim about clock-time.
4. When citing `klein_bottle_derivation.md` Part IV ("the antiperiodic
   direction is temporal"), read it as a claim about arrow-time.
5. New claims must specify which aspect they invoke.

## What this doesn't do

- Does **not** revise upstream docs to relabel their language
  uniformly. That's a separate cleanup; the convention here lets
  readers re-interpret existing language correctly without rewriting.
- Does **not** assert that one aspect is "more fundamental" than the
  other. Both are needed: predictions involving cosmic ages live on
  the clock axis; predictions involving CPT, fermion sign, Z_2
  charge, soliton conversion live on the arrow/antiperiodic axis.
- Does **not** address whether the framework can or should derive a
  single "time" combining both. That would require additional
  structure (e.g., a fibration relating the two axes); not in scope.

## Cross-links

- `klein_bottle.md` — section "Where time lives" gives the clock-axis
  argument; correct under the split.
- `klein_bottle_derivation.md` — Part IV "the arrow of time argument"
  gives the arrow-axis argument; correct under the split, applies to
  the arrow direction specifically.
- `framework_lagrangian.py` — uses the arrow-direction as the
  integration domain's "temporal" axis; correct under the split.
- `sine_gordon_substrate.md` — Z_2-graded charge mechanism uses the
  antiperiodic axis directly without committing to a clock-or-arrow
  reading.
- `D46 / rank1_temporal_causation.md` — supplies the arrow-axis
  argument from the rank-1 Fréchet derivative.
