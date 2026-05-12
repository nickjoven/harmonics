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

## Quantitative structure: the arrow-axis is integer-counted

Reading the split through the wave–particle synthesis
(`wave_particle_substrate.md`) makes the qualitative time-axis split
quantitative on the arrow side. **The arrow-direction is integer-
counted in units of a substrate time quantum**; the clock-direction
remains continuous. The two aspects of time are wave–particle dual
to each other: arrow-time is particle-side (mediant, discrete event
count), clock-time is wave-side (EML, continuous breathing).

### The substrate time quantum

Each forced Z₂-violation triggers a substrate repair-event whose
phase-2 propagating-loop traversal (per `sine_gordon_substrate.md`
"Z_2-graded topological charge") takes time

    τ_tick = L_x / c

where `L_x` is the antiperiodic-loop length on the Klein bottle and
`c = σ / √m` is the substrate sound speed (from
`soliton_dynamics.md` §1 dispersion). `τ_tick` is the framework's
**natural unit of arrow-time** — universal, substrate-primitive,
same for every observer.

Arrow-time accumulation between two events is then

    Δτ_arrow = N_events × τ_tick

with `N_events` the integer count of Z₂-repair events along the
worldline between the two events. The arrow-axis is **discrete** at
the substrate level; the continuous arrow-time of conventional
physics is the coarse-grained limit of many ticks averaged.

The clock-axis remains continuous — it is the wave-side aspect of
time, breathing in the periodic y-direction, parametrising cosmic
age and Friedmann time as conventionally read.

### Two channels for the local repair rate

The local repair-event rate `Γ_repair(x, t)` factors into two
distinct substrate channels:

| Channel | Mechanism | Rate scaling |
|---|---|---|
| **Pair-production** (Schwinger-like) | Vortex–antivortex pairs spontaneously created from the substrate vacuum by a local K-gradient or substrate curvature; the cone-twist seam's natural activity | `Γ_pair ∝ \|∇K\|² exp(−π S_v / (ℏ \|∇K\|))` — exponentially suppressed below a critical K-gradient. Sets cosmological / dark-sector arrow-rate. |
| **Phase-slip** (thermally activated) | A locked-tongue's phase wraps by 2π — a discrete slip within a single cascade sector | `Γ_slip ∝ ω_p exp(−E_slip / (k_B T))` — Kramers escape; thermally activated at any temperature. Sets local matter-sector arrow-rate. |

Both `S_v` (vortex-pair action) and `E_slip` (phase-slip activation
energy) are framework-internal quantities derivable from substrate
primitives `(σ, K, r, m)`. Their *form* is fixed by the mechanism;
their *numerical coefficients* await the end-to-end unit-convention
pinning of `unitless_check.md`.

The two channels dominate in different regimes: pair-production at
cosmological scale (where K-gradients are the substrate's natural
large-scale structure), phase-slip at lab scale (where ambient
temperature dominates).

### Cosmological prediction

The substrate-averaged pair-production rate sets the cosmological
expansion rate:

    H(t) = κ_pair × ⟨Γ_pair(t)⟩_substrate

with `κ_pair` a contrabass-class structural prefactor. **The cosmic
expansion rate is literally the substrate's K-gradient-driven
repair rate, up to a structural prefactor.** This reads
`half_twist_dynamics.md`'s cosmological-constant / Hubble-rate
identification through the substrate-time quantum: `H_0` is the
inverse of the time taken for the substrate to repair one
cosmologically-averaged Z₂-violation, multiplied by the structural
prefactor `κ_pair`.

The `Ω_Λ = 13/19` ratio then has a second-order reading: the
equilibrium channel-partition between K-gradient-driven activity
(wave-side, dark energy) and locked-tongue phase activity (particle-
side, matter). Both are repair events; the ratio is structural and
matches the existing `half_twist_dynamics.md` derivation.

### Status

Class 3 (derivation grade) for the form `τ_tick = L_x/c`,
`dτ_arrow / dt = τ_tick × Γ_repair`, and the channel decomposition.
Conditional on `unitless_check.md` end-to-end for the numerical
coefficient `κ_pair` and for `E_slip(σ, K, r)`,
`S_v(σ, K, r, m)`. Same bookkeeping status as
`soliton_dynamics.md` Open 1.

The doc-internal claim added by this section: **arrow-time is
discrete; clock-time is continuous; they are wave–particle dual to
each other.** This is a structural consequence of the existing
split, not a new postulate.

### Falsifiers (sharpened)

1. **Continuous arrow-time at the substrate scale.** Any precision
   measurement showing arrow-time intervals are not quantised in
   units of `τ_tick` (i.e., that arbitrarily small smooth variation
   exists at the substrate's natural arrow-time scale) falsifies the
   discrete-arrow commitment. Test is hard because `τ_tick` is
   likely sub-Planckian, but in principle the discrete-step
   signature could appear in short-time correlation functions.
2. **`H(t)` not tracking pair-production rate.** Any cosmological
   observation finding `H(t)` evolution incompatible with
   substrate-averaged pair-production rate (at the substrate's
   K-gradient profile) falsifies prediction A.
3. **Channel-partition violation.** Any cosmological observation
   where the dark-sector / matter ratio differs from `13/19` for a
   substrate-internal reason (not just anchor-scaling) falsifies
   the channel-partition reading of `Ω_Λ`.
4. **Lab-scale clock temperature dependence.** Any atomic-clock-rate
   temperature dependence (gravity and known thermal effects on the
   atomic transition controlled for) inconsistent with calculable
   `E_slip` from substrate primitives. Currently this is a
   *negative* falsifier: existing atomic clocks show no such
   dependence to `Δτ/τ ≲ 10⁻¹⁸`, which constrains `E_slip >> k_B T_atomic`,
   consistent with `E_slip` being a substrate-fundamental scale.



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
- `wave_particle_substrate.md` — reads the time-axis split as the
  wave–particle duality applied to time: arrow = particle-side
  (discrete, mediant-counted), clock = wave-side (continuous,
  EML-breathing). Source of the quantitative-structure section
  above.
- `cone_twist_substrate.md` — Schwinger-like vortex-pair production
  at the seam is the pair-production channel of the local repair
  rate.
- `soliton_dynamics.md` — substrate sound speed `c = σ/√m` sets the
  `τ_tick = L_x/c` quantum; linear-wave dispersion is the same
  speed.
- `half_twist_dynamics.md` — cosmological breathing-mode
  identification with `H_0` is reread here as the structural
  prefactor `κ_pair` linking `H(t)` to substrate pair-production
  rate.
