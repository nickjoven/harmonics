# Seismic Eigenstate Dictionary

## Claim

The empirical precursor methods that drive modern seismic gap
assessments (Iquique, Nankai, Cascadia) are already *reading* the
framework's tongue-locking structure — they just call the modes by
their seismological names. This document states the vocabulary
mapping without adding a new tool, and explains what the framework
does and does not contribute.

## What enables the referenced probability updates

The 2024–2026 upward revisions for the Chilean Atacama Trench
gap and the Japanese Nankai / Hokkaido gaps are probabilistic
fusions of six well-established methods, none of which originated
in this framework:

1. **Historical recurrence priors.** Iquique: 1877 M~8.8, ~147 yr
   interseismic, partially released in 2014. Nankai: the 1707 /
   1854 / 1944–1946 cluster gives a 90–150 yr cycle, placing the
   next event in the 2030s–2040s. Base-rate Poisson or BPT
   (Brownian passage time) models.
2. **Plate coupling maps** from GPS + InSAR inversions.
   Yokota & Ishikawa 2016 (Nature) mapped the Nankai locked
   patches from GEONET; IPOC and LISN networks do the same for
   northern Chile. This is the slow-variable channel that
   `parabola_csd_pipeline.py` reads.
3. **Repeating earthquake catalogs.** Kato et al. 2014 (Nature)
   found migrating repeater sequences in the weeks before the
   Iquique M8.2. A repeater is a fault patch that ruptures the
   same asperity at near-regular intervals.
4. **Tremor and slow slip events.** Obara 2002, Rogers & Dragert
   2003. Non-volcanic tremor in the ~2–5 Hz band, clustered
   episodically with aseismic slow slip. Distinct frequency band,
   distinct recurrence.
5. **b-value tracking** (Gutenberg–Richter slope). Wiemer, Wyss:
   the slope relating small-event frequency to magnitude drops
   before some mainshocks — weight migrates into the large-event
   tail.
6. **Coda dv/v monitoring.** Brenguier et al. 2008 (Science):
   ambient-noise cross-correlation measures ~0.1% seismic
   velocity drops in the months before large earthquakes.

Items (1) and (2) are slow-variable / critical slowing down
(CSD). Items (3)–(6) are waveform-based — mode-decomposition,
eigenstate-of-the-medium methods. Both channels fuse into the
probabilistic hazard number; neither alone produces it.

## Framework vocabulary

The Kuramoto substrate on a Klein bottle has a discrete set of
tongue-locked modes indexed by rationals `p/q`:

- `duty(q) = 1/q^d` with `d = 3` — the occupation duty cycle of
  a mode at denominator `q`.
- `tongue_width(p, q, K)` — the coupling-dependent width of the
  Arnol'd tongue around `p/q`. Shrinks to zero at the tongue
  boundary (a saddle-node bifurcation for that individual mode).
- On-backbone modes lie on the Fibonacci path through the
  Stern–Brocot tree and carry the locked Standard Model content.
- Off-backbone modes are broadband / noise channels between
  tongues.

All three helpers live in `framework_utils.py`; the backbone
integers live in `framework_constants.py`.

## The mapping

| Seismic observable | Framework variable |
|---|---|
| A **repeating earthquake family** — a patch that ruptures on a near-constant cycle | A phase-locked mode on a tongue. The recurrence interval is the period of a `p/q` rational; the regularity is the tongue width. |
| **Tremor** at ~2–5 Hz, clustered with slow slip | A different tongue at a smaller `p/q`. Episodic occupation = intermittent locking near the tongue boundary. |
| **Free oscillations** (`_0S_0`, `_0T_2`, …) of the solid Earth after a large event | Literal eigenstates of the elastic continuum. Discrete spectrum. |
| **Background seismicity** between the repeating families | Off-backbone / broadband response between tongues. |
| **b-value** (Gutenberg–Richter slope) | The weight distribution across modes of different denominator. High b = weight on high-`q` (many, small); low b = weight on low-`q` (rare, large). A dropping b-value is weight migrating down the Stern–Brocot tree toward the large-event tongue. |
| **b-value drop before a mainshock** | Tongue fattening on the low-`q` end — the large-event mode becoming easier to enter. |
| **dv/v drop** from coda interferometry | The medium's own eigenspectrum softening. Mode frequencies drifting downward is a generic saddle-node symptom (`ω^2 ∝ ε`, frequency → 0 at the bifurcation). |
| **Repeater migration along the fault** (Kato 2014) | Walk in the Stern–Brocot tree: the occupied tongue set is reorganizing. New rationals becoming accessible is a change in the mode occupancy. |
| **Slow slip events** episodically between locked intervals | The same tongue ungating at slow timescales — the mode is at its boundary and spends part of its time unlocked. |
| **Tremor bursts triggered by tides** | Parametric forcing at the tongue boundary — external drive modulates an already-marginal mode. |
| **Coulomb stress transfer** from a nearby event | An external perturbation that shifts a mode across its tongue boundary. The response is set by the tongue width at the time of the perturbation. |

The columns are not metaphors. A tongue-locked Kuramoto mode and
a repeating earthquake family obey the same equations in the
phase-oscillator reduction: both have a stable phase, a noise
tolerance given by a tongue width, and a saddle-node bifurcation
at the tongue edge. The framework's claim is that the seismic
phenomena are the *same primitives* acting on a different
substrate.

## Two pipeline topologies

The CSD pipeline (`parabola_csd_pipeline.py`) and a
waveform/eigenstate pipeline are structurally different:

|  | CSD pipeline | Waveform / eigenstate pipeline |
|---|---|---|
| Input | One scalar time series (GPS strain) | Event catalog + spectra |
| Order parameter | Single variable `x(t)` | Vector of mode occupancies `{n_{p,q}(t)}` |
| What is tracked | Variance, AR1, skewness of `x` | Tongue widths, mode positions, b-value, dv/v |
| What blows up near release | Variance of `x` → ∞, AR1 → 1 | Low-`q` tongue width → 0, weight migrates down the tree |
| Framework primitive exercised | Parabola (saddle-node local form) | Integers + mediant (which rationals are occupied) + parabola (what happens at each tongue boundary) |
| Question answered | Is the fault approaching **a** saddle-node? | Which **specific** locked configurations remain consistent with today's data? |

CSD watches one scalar get sick. The eigenstate view watches the
whole mode spectrum rearrange. The framework ships both
primitives, so both pipelines are available — they answer
different questions and should be used together, not in
competition.

## What "constrain possibility" means

Given a fault's current mode spectrum (repeater recurrence,
tremor bands, b-value, dv/v), the framework dictionary picks out
which on-backbone rationals are consistent with the data. Modes
not on the dictionary can be present transiently but cannot
*lock* — they decay or migrate to a nearby rational. So the set
of consistent futures is the set of framework-legal tongue
configurations reachable from today's occupancy in a few steps
on the Stern–Brocot tree.

This is a combinatorial constraint, not a continuous one. It
says "the fault can be in any of these discrete locked
configurations, and noise will kick it between them; the
accessible neighbors are the mediant children of the current
occupancy." A tongue width approaching zero narrows the set of
next steps — the possibility space contracts toward a specific
release direction.

## What the framework adds, and what it does not

The framework does **not** produce a new probability number.
The "65% by 2035" figures in the news items come from
time-dependent BPT hazard models plus Bayesian updating on the
coupling maps, and the framework has nothing new to contribute
at that layer.

What it does contribute is the **structural identification**:

- The fault is a Kuramoto substrate.
- Repeating earthquakes are tongue-locked modes.
- Tremor is a different tongue at a different `p/q`.
- b-value is the weight distribution across denominator classes.
- CSD is the local parabola primitive approaching its
  saddle-node — the same parabola that, in the quantum sector,
  gives the Born rule `|ψ|²`.
- Critical slowing down on strain data and critical slowing
  down on quantum measurement outcomes are the *same local
  geometry*.

This is a **unification**, not a tool. Early-warning-signals
machinery (Scheffer, Carpenter, Dakos, ewstools) and standard
seismological catalog analysis (ZMAP, PyOcto, ObsPy-based
workflows) already implement every operation in the mapping
table above. The framework's contribution is naming what they
are doing in the same vocabulary as the quantum and gravity
sectors.

## Cross-references in the framework

| File | What it establishes |
|---|---|
| `stribeck_vortex.md` §"Parabola primitive in the seismic domain" | The parabola primitive as the local normal form for stick-slip release |
| `born_rule.md` Proof B | The *same* parabola giving `|ψ|²` in the quantum sector |
| `parabola_csd_demo.py` | Worked simulation of CSD indicators at a shrinking `μ` |
| `parabola_csd_pipeline.py` | Real-data CSD pipeline over NGL GPS strain series |
| `framework_utils.py` `tongue_width(p, q, K)` | The tongue width formula that seismic mode stability maps onto |
| `framework_utils.py` `duty_cycle(q, d=3)` | The duty cycle that repeater recurrence maps onto |
| `framework_constants.py` | The Stern–Brocot backbone the eigenstate dictionary walks on |

## What a future waveform pipeline would implement

Deferred — the vocabulary map above must be grounded before the
pipeline's mode-occupancy numbers have meaning. When built,
`parabola_waveform_pipeline.py` would:

1. Pull an event catalog from the USGS FDSN event web service
   for a target region (already documented in the CSD pipeline,
   no auth required).
2. Compute a rolling Aki-1965 MLE b-value estimator over the
   catalog, sliced by time window.
3. Identify candidate repeating-earthquake families by
   inter-event interval regularity (a simple stand-in for
   matched-filter detection).
4. Map observed repeater periods and tremor bands to framework
   `(p, q)` rationals via `framework_utils.farey()` and report
   the closest backbone neighbors and their tongue widths.
5. Report mode occupancy and b-value as time series, with
   Kendall-tau trend tests on each.
6. Flag tongue-width collapse and low-`q` weight migration as
   the eigenstate analogues of the CSD pipeline's variance /
   AR1 flags.

The pipeline is not a prediction tool. Its output is a reading of
the current mode occupancy in framework vocabulary, to be
consumed alongside (not in place of) standard hazard models.
