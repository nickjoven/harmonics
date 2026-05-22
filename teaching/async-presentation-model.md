# Async presentation model for Harmonics

This is a teaching layer for `nickjoven/harmonics`. Its job is not to
compress the repository into a single proof. Its job is to let a curious
viewer enter the framework at the right altitude, learn one idea at a
time, and always know which claims are structural, which are anchors, and
which have been declined.

Audience assumption: a YouTube science channel subscriber. They are
comfortable with waves, gravity, quantum mystery, and "here is the
equation in the background," but they should not need graduate physics
to follow the story.

Public commitment: the science is accessible, and the status of each
claim is explicit.

## The core presentation problem

The repository already has many presentation surfaces:

- `README.md`: narrative front door and catalog.
- `docs/index.html`: reference table and proof-chain overview.
- `docs/mastery-graph.html` plus `docs/mastery-graph.json`: concept
  graph written in plain language.
- `docs/claim-chain.html` and `docs/claim-chain-views.html`: claim-chain
  views, including math and syllogism readings.
- `sync_cost/derivations/structural_lemmas.md`: nine load-bearing lemmas.
- `sync_cost/derivations/canonical_glossary.md`: vocabulary translation.
- `sync_cost/derivations/phenomenology_cross_reference.md`: observable
  comparison with claim status.
- `sync_cost/derivations/derivation_atlas.md`: long-form chain from
  primitives to predictions.
- `prototype/index.html`: metronome wall and devil's-staircase demo.
- `RESULTS.md`: Stribeck and clarinet lattice results.

The hurdle is not lack of material. The hurdle is uncontrolled entry.
A viewer can encounter a prediction before the mechanism, a mechanism
before the vocabulary, or a stale claim before a later audit.

The async model fixes that by separating the public path from the receipt
path.

## Source of truth hierarchy

Use this hierarchy when sources disagree:

1. `MANIFEST.yml` for canonical quantitative claims.
2. `sync_cost/derivations/framework_status.md` for live claim status.
3. `sync_cost/derivations/statistical_conventions.md` for public
   claim language and Z1-Z3 discipline.
4. `sync_cost/derivations/phenomenology_cross_reference.md` for
   observation-facing summaries.
5. `sync_cost/derivations/structural_lemmas.md` for proof-source
   pointers.
6. Individual derivation files for details.
7. `README.md` only when it agrees with the stricter status files.

Important public-language rule: do not say "zero free parameters" as a
framework-level claim. The repo's stricter convention retires that phrase.
Use "structural, Z1-Z3", "derived against named anchors", "bare K=1
reference only", "anchor-side", "Class 2 coincidence", or "declined".

Also important: do not present `sin^2 theta_W = 8/35`, `alpha_s/alpha_2 =
27/8`, `m_H/v = 1/2`, `lambda_H = 1/8`, or `1/alpha_em = 35` as
observable-scale predictions. In the current status layer they are bare
K=1 references or declined/near-match material, not M_Z predictions.

## The async learner stack

Each lesson exists in five layers. A viewer can stop after any layer and
still leave with a coherent understanding.

1. **Video** - 6 to 10 minutes. One idea, one visual, one claim status.
2. **Card** - a short web/markdown page: "what you saw", "what it means",
   "what the framework claims", "what it does not claim".
3. **Demo** - interactive when possible, static visual when not.
4. **Receipt trail** - source links into the repo.
5. **Deep dive** - derivation atlas or individual derivation files.

The video earns curiosity. The card stabilizes vocabulary. The demo makes
the abstraction manipulable. The receipt trail keeps trust. The deep dive
serves the specialist without forcing everyone else into specialist mode.

## Episode contract

Every episode should answer the same six prompts:

1. **What ordinary phenomenon are we starting from?**
   Example: metronomes synchronizing, a bowed string slipping and sticking,
   a swing absorbing energy at resonance.

2. **What standard physics name does this already have?**
   Example: phase, resonance, mode locking, Arnold tongues, saddle-node
   bifurcation, Stern-Brocot tree.

3. **What is the framework's move?**
   Example: the medium is continuous, but stable locks are discrete.

4. **What can the viewer see or compute?**
   Example: move the K slider and watch rational plateaus appear.

5. **What claim status applies?**
   Structural/Z1-Z3, anchor-side, bare reference only, Class 2, declined,
   or open.

6. **Where are the receipts?**
   Link to exactly two to five source files, not twenty.

## Visual grammar

The framework needs fewer symbols in public and more stable pictures.
Use these recurring visuals:

- **Clock hand on a circle**: phase.
- **Two clocks tugging each other**: coupling.
- **Rational plateaus on a staircase**: mode locking.
- **Fraction tree**: Stern-Brocot and the mediant.
- **Tongue map**: Arnold tongues and stability regions.
- **Loop with a flip**: Klein bottle topology.
- **Two-lane road labeled K = 1 and K < 1**: the non-smooth regime split.
- **Status badge**: structural, anchor-side, bare reference, declined.

Avoid beginning with a Klein bottle, Standard Model gauge groups, or a
large predictions table. Those are payoff, not entry point.

## Series spine

### 0. The promise and the boundary

Hook: physics has two kinds of questions: "what happens if these numbers
are true?" and "why these numbers?"

Plain claim: the Standard Model is excellent at the first question. This
framework tries to answer a subset of the second by deriving some
dimensionless structure from coupled oscillators, topology, and number
theory.

Status: methodological orientation, not a prediction.

Primary sources:

- `README.md`, especially "What this framework does not do".
- `sync_cost/derivations/statistical_conventions.md`.
- `sync_cost/derivations/phenomenology_cross_reference.md`.

### 1. Phase is a clock hand

Hook: a repeating thing is easier to draw as a hand moving around a clock
than as a number marching forever.

Teach: phase, recurrence, modulo a period, winding number.

Framework move: once phase lives on a loop, integer winding numbers become
natural. Quantization can come from dynamics on a continuous loop, not
from pixelated space.

Demo: clock hand animation or `docs/mastery-graph.html` nodes for
recurrence, phase loop, modulo, winding.

Status: standard physics and topology groundwork.

Primary sources:

- `docs/mastery-graph.json`.
- `sync_cost/derivations/dynamical_quantization.md`.
- `sync_cost/derivations/canonical_glossary.md`.

### 2. Coupled oscillators prefer simple ratios

Hook: two rhythms that almost match can pull each other into sync.
Sometimes they lock one-to-one; sometimes they lock two-to-one or
three-to-two.

Teach: resonance, coupled oscillators, mode locking, Arnold tongues.

Framework move: the stable records of the dynamics are rational locks
`p/q`.

Demo: `prototype/index.html` metronome wall; K slider; devil's staircase.

Status: standard dynamical-systems phenomenon used as framework substrate.

Primary sources:

- `prototype/README.md`.
- `sync_cost/derivations/dynamical_quantization.md`.
- `sync_cost/derivations/tongue_widths_exact.py`.

### 3. The simplest fraction between two fractions

Hook: if one oscillator wants 1/2 and another wants 1/3, the simplest
compromise is `(1+1)/(2+3) = 2/5`.

Teach: mediant, Stern-Brocot tree, best rational approximations.

Framework move: if stable locks prefer the lowest denominator available
between neighbors, the mediant is not a decorative trick. It is the
combining rule.

Demo: `sync_cost/applications/stern_brocot_walk.html`.

Status: structural derivation with explicit scope limits.

Primary sources:

- `sync_cost/derivations/mediant_derivation.md`.
- `sync_cost/derivations/farey_partition.md`.
- `sync_cost/applications/stern_brocot_walk.html`.

### 4. Continuous medium, discrete locks

Hook: a guitar string is continuous, but the notes it supports are
discrete.

Teach: the difference between the medium and the stable modes of the
medium.

Framework move: the framework is not claiming pixelated spacetime. It is
claiming continuous dynamics whose stable locked states form a discrete
record.

Demo: devil's staircase, with flat plateaus appearing as K increases.

Status: pedagogical/methodological core.

Primary sources:

- `sync_cost/derivations/dynamical_quantization.md`.
- `docs/knobs/coupling.html`.
- `prototype/README.md`.

### 5. The split: K = 1 and K < 1

Hook: the same system can behave like a smooth continuum in one regime and
like a filtered set of locks in another.

Teach: coupling strength K; continuum limit; subcritical regime.

Framework move: K = 1 is the Einstein-side continuum limit; K < 1 is the
Schrodinger-side partial-synchronization limit. The split is non-smooth,
which is why the framework uses two dimensional anchors: cosmological
`H_0` and particle-sector `v_EW`.

Status: structural feature, not a missing simplification.

Primary sources:

- `sync_cost/derivations/structural_lemmas.md` Lemma 3.
- `sync_cost/derivations/dynamical_quantization.md`.
- `MANIFEST.yml` dimensionful input note.

### 6. Why squares show up in probability

Hook: near a threshold, small changes often grow like a square root or a
square. That is not quantum magic yet; it is common bifurcation geometry.

Teach: saddle-node bifurcation, basin measure, Born rule exponent.

Framework move: probability proportional to `|psi|^2` comes from basin
volume near saddle-node boundaries.

Status: Survives/Class 5 in current status layer.

Primary sources:

- `sync_cost/derivations/born_rule.md`.
- `sync_cost/derivations/a1_from_saddle_node.md`.
- `sync_cost/derivations/structural_lemmas.md` Lemma 7.

### 7. Counting locked modes gives a cosmic partition

Hook: if the stable records are countable, the universe's large-scale
energy budget may be a counting problem before it is a substance problem.

Teach: Farey depth, mode count, filters, cosmic density fractions.

Framework move: the static single-w partition gives
`Omega_Lambda : Omega_DM : Omega_b = 13 : 5 : 1` over 19. The refined
two-component closure gives `Omega_Lambda = 181/264`,
`Omega_DM = 35/132`, and `Omega_b = 13/264`.

Status: headline structural claim in current status layer.

Primary sources:

- `sync_cost/derivations/farey_partition.md`.
- `sync_cost/derivations/omega_b_alpha_beta_closure.md`.
- `sync_cost/derivations/framework_status.md`.
- `MANIFEST.yml`.

### 8. The honest prediction board

Hook: a theory earns trust not only by what it claims, but by what it
refuses to claim.

Teach: structural/Z1-Z3, anchor-side, bare K=1 reference, Class 2
coincidence, declined.

Framework move: present the current scorecard without turning near-matches
into public claims.

Status: methodological guardrail.

Primary sources:

- `MANIFEST.yml`.
- `sync_cost/derivations/framework_status.md`.
- `sync_cost/derivations/statistical_conventions.md`.
- `sync_cost/derivations/numerology_inventory.md`.

## Optional deep-dive episodes

- **MOND scale from a cosmic clock**: `a_0 = c H_0 / (2 pi)` and why low
  acceleration is a locking threshold. Sources: `a0_threshold.md`,
  `phenomenology_cross_reference.md`, `RESULTS.md`.
- **Spectral tilt from a staircase**: the CMB tilt as mode-locking
  structure near golden-ratio self-similarity. Sources:
  `spectral_tilt_reframed.md`, `staircase_spectrum.py`,
  `docs/cmb-s4.html`.
- **Klein bottle without the circus**: a loop-with-flip selection rule,
  not a visual stunt. Sources: `klein_bottle.md`,
  `dynamical_quantization.md`, `structural_lemmas.md`.
- **The Stribeck lattice**: stick-slip as a physical toy model for
  bifurcation, conversion, and propagation. Sources: `RESULTS.md`,
  `stribeck_lattice.py`, `clarinet_lattice.py`.

## Script template

Use this structure for every video script.

```text
TITLE:
One clear sentence, not a pun.

COLD OPEN (0:00-0:30):
Start with an observable everyday pattern.

SETUP (0:30-1:30):
Name the standard physics idea in plain English.

VISUAL MODEL (1:30-3:00):
One diagram or demo. No derivation yet.

THE FRAMEWORK MOVE (3:00-5:00):
Explain what Harmonics adds or reinterprets.

ONE EQUATION OR COUNT (5:00-6:30):
Show only the equation/count needed for this episode.

CLAIM STATUS (6:30-7:15):
Structural, anchor-side, bare reference, Class 2, declined, or open.

TAKEAWAY (7:15-8:00):
One sentence the viewer can repeat accurately.

RECEIPTS:
2-5 source files.
```

## First script seed

Episode 1 should not start with dark energy. It should start with phase.

Possible opening:

```text
Imagine a clock hand moving smoothly around a circle. If I tell you it is
at 12 o'clock again, I have not told you whether it went around once, ten
times, or a million times. The position is continuous, but the number of
completed laps is an integer.

That tiny fact is the first door into Harmonics. The framework is not
trying to make space out of pixels. It starts with smooth things that
repeat, then asks which repeated motions can leave stable records.

The records are discrete. The medium does not have to be.
```

Visual: a phase hand on a circle, with a small counter for completed
laps. Then two hands with slightly different speeds begin to pull toward
a simple ratio.

Episode takeaway: "Quantization can live in the lock, not in the medium."

## Production checklist

Before publishing any lesson:

- Check the claim against `MANIFEST.yml`.
- Check the status against `framework_status.md`.
- Check language against `statistical_conventions.md`.
- Include a "what this does not claim" sentence.
- Link no more than five receipts.
- Keep one main visual on screen at a time.
- Prefer standard names first, framework vocabulary second.
- Never let a near-match become a prediction by narration.

## Immediate next material to build

1. A one-page public landing card: "Harmonics in eight ideas".
2. Episode 1 full script: "Phase is a clock hand".
3. Episode 2 full script: "Why simple ratios lock".
4. A status-board card that translates `MANIFEST.yml` into public
   categories.
5. A source cleanup pass that aligns the README's opening claims with the
   stricter manifest/status layer.

Companion map: `teaching/entrypoint-teaching-reference.md` translates the
README entry points, deployed docs, interactive resources, and mastery
graph clusters into reference-card targets and understanding checks.

Companion question atlas: `teaching/question-atlas.md` turns those
targets into a complete v0 list of askable moves for cards, scripts,
demos, review, and claim hygiene.
