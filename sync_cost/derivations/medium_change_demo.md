# Medium-change demo: address vs. structure

A physical demonstration of the distinction between the framework's two
categorically different kinds of predicted constants. Suitable for
classroom use, lecture openers, or as a reading aid for the README's
second clarifying note.

## The setup

Three sources, each playing a low E (the musical note at ~41 Hz when
sounded at the bottom of the contrabass / tuba register):

- a **tuba** in air,
- a **contrabass** (acoustic double bass) in air,
- an **electromagnetic loudspeaker** driven by a 41 Hz electrical signal,
  in air.

In ordinary listening conditions, all three produce a recognizable low E
at approximately the same pitch. They sound different — different
timbre, different harmonic content — but the perceived fundamental is
roughly the same.

## Now change the medium

Repeat the experiment in a chamber filled with helium gas. The speed of
sound in helium at room temperature is approximately 970 m/s, versus
343 m/s in air — a ratio of about 2.83. What happens to the perceived
pitch of each source:

| Source | Pitch in air | Pitch in helium | Change | Why |
|---|---|---|---|---|
| Tuba (low E) | ≈ 41 Hz | ≈ 116 Hz | jumps up by a factor of ~2.83 (about 1.5 octaves, or 18 semitones) | Resonance frequency of the air column inside the instrument is `c/(2L)`; changing `c` changes the pitch. |
| Contrabass (low E) | ≈ 41 Hz | ≈ 41 Hz | unchanged | Resonance frequency of the string is (1/2L)·√(T/μ); depends on string tension and density, not on the surrounding medium. |
| Loudspeaker (driven at 41 Hz) | 41 Hz at the cone | 41 Hz at the cone | unchanged at the source; transmission is faster | The cone's velocity is dictated by the input voltage waveform, not by any internal resonance. |

The *Donald Duck effect* familiar from inhaling helium is exactly the
tuba case applied to the human vocal tract: the vocal folds vibrate
at roughly the same rate (string-like, structure-locked), but the
formants — the resonant peaks of the vocal-tract air column — shift
upward, producing the cartoon-character voice. The folds are the
contrabass; the formants are the tuba.

## What the experiment reveals

Three categorically different physical phenomena are producing
acoustically similar outputs:

- **Tuba**: a standing wave whose frequency is set by a property of
  the *medium* (the speed of sound in the air column). Changing the
  medium changes the frequency.
- **Contrabass**: a standing wave whose frequency is set by a property
  of the *structure* (the string's tension and linear density).
  Changing the medium does not affect the frequency.
- **Loudspeaker**: not a standing wave at all. The cone is a *driven
  oscillator*. The frequency comes from outside the system entirely.

Without the helium experiment, all three sound roughly the same at
~41 Hz and the difference is invisible. With the medium swap, the
three categories separate sharply.

## The framework's claim

The framework asserts that the universe has constants of all three
categories, and that conflating them is the most common reading error
when first encountering the framework's predictions.

| Category | Example physical constant | What it depends on | Behavior under "medium swap" |
|---|---|---|---|
| Tuba (medium-dependent) | The Hubble constant H₀ | The current cosmic synchronization rate of the Stern-Brocot substrate at our depth | Would change for an observer at a different depth on the tree (different epoch, different K) |
| Contrabass (structure-dependent) | Ω_Λ = 13/19; sin²θ_W = 8/35; α_s/α_2 = 27/8; K_c = 2/π | The forced combinatorial structure (Stern-Brocot tree, Klein-bottle topology, Z_6 mode counting) | Unchanged under any "medium swap"; the same for every observer at every epoch |
| Loudspeaker (input-driven) | Anything fitted post-hoc to data — most Standard Model parameters as currently treated | An external input that happens to match observation | "Unchanged" trivially; the value is whatever you put in |

The framework's empirical content is the contrabass row: dimensionless
rationals derived from the structure, the same for every observer.

The framework's "address" content (Tier 5 in the
[FRAMEWORK.md](../FRAMEWORK.md) hierarchy) is the tuba row: dimensionful
quantities that locate us on the structure. They are real and
measurable, but they are *coordinates*, not parameters of physics.

The Standard Model treats all of its constants as the loudspeaker
row — values to be measured and inserted into the Lagrangian. This
framework's claim is that some of those values are tuba-pitches in
disguise (medium-dependent, observer-dependent at cosmic scale) and
others are contrabass-pitches (structural, observer-independent).
Disentangling them is the framework's main empirical move.

## A second trio: bowed string vs. clarinet vs. flute

The tuba/contrabass/speaker comparison establishes address-vs-structure.
A second trio — three real orchestral instruments — sharpens the same
distinction in a different direction and ties it to the framework's
two universal generators (`mediant` for discrete structure, `eml` for
continuous dynamics).

The fundamental frequency formulas:

| Instrument | Formula | What sets the pitch |
|---|---|---|
| Bowed string (violin, cello, contrabass) | `f = (n / 2L) · √(T/μ)` | string tension `T`, linear density `μ`, length `L` — all mechanical, all internal |
| B♭ clarinet (closed cylinder approximation) | `f = (n / 4L) · c_medium` | air column length `L` × the speed of sound `c_medium` |
| Concert flute (open tube) | `f = (n / 2L) · c_medium` | same, plus an aero-acoustic edge tone that's also `c`-dependent |

The integer `n = 1, 2, 3, …` is the mode number — how many half-
wavelengths fit in the resonator. **It is the same in all three
formulas.** That integer is the discrete, structural part of every
acoustic resonator; it is forced by the boundary conditions and is
medium-independent.

What differs is the *dimensional anchor* multiplied against `n`:

- the bowed string's anchor is `√(T/μ) / 2L` — entirely properties of
  the string;
- the clarinet's and flute's anchors are proportional to `c_medium`
  — properties of the surrounding gas.

In a helium chamber, with `c_helium ≈ 970` m/s versus
`c_air ≈ 343` m/s (ratio ≈ 2.83), play concert A4 = 440 Hz on each:

| Instrument | Pitch in air | Pitch in helium | Why |
|---|---|---|---|
| Violin | 440 Hz | **440 Hz** | structural anchor; `c` does not appear in the formula |
| B♭ clarinet | 440 Hz | ≈ 1245 Hz (D♯6) | `c`-anchor scales with medium; same fingering would now resonate above the instrument's intended range |
| Concert flute | 440 Hz | ≈ 1245 Hz (D♯6) | same — both column resonance and edge tone scale with `c` |

The bowed string is the structural outlier. Its pitch lives in the
*discrete-counter × structural-anchor* form, and the anchor itself
is medium-independent. The clarinet and flute have the same discrete
counter `n`, but their anchors live in the *medium*.

## The lambda / EML split, made audible

The framework's claim, articulated formally elsewhere in this repo,
is that physics requires two distinct universal generators:

| Generator | Algebra it covers | Framework primitive |
|---|---|---|
| Mediant `(a+c)/(b+d)` | discrete combinatorics: integer mode counts, Farey arithmetic, Stern-Brocot enumeration | integers + mediant |
| EML `eml(x,y) = exp(x) − ln(y)` | continuous transcendentals: Boltzmann weights, partition functions, saddle-node passage | parabola |

The bowed-string / clarinet / flute trio maps onto this split
literally:

- The integer mode number `n` is mediant-side (lambda-side):
  discrete, structure-fixed, the same in any medium.
- The dimensional anchor is EML-side (continuous-side): exponential
  in temperature for partition functions, polynomial in `c` for air
  columns, polynomial in `T/μ` for strings. Continuous, dynamical,
  set by the medium or the material.

The bowed string is the instrument whose anchor is *also* on the
structural side (mechanical properties of the string). The clarinet
and flute have anchors on the dynamical side (medium properties).

Two of the three are EML-anchored; one is mediant-anchored. That ratio
is roughly the framework's claim about physics: most observable
quantities (Hubble rate, masses, couplings) are EML-anchored — they
move under medium swap. A small set of quantities (the dimensionless
ratios `Ω_Λ`, `sin²θ_W`, `α_s/α_2`, `K_c`) are mediant-anchored — they
do not move.

The bowed string is what the framework's predictions look like.
The flute is what the Standard Model has historically taken every
parameter to be.

For the formal articulation of the lambda / EML split as a notational-
invariance claim parallel to `comparison_class.md` and
`unitless_check.md`, see [`expressibility_split.md`](expressibility_split.md).

## The pedagogical sequence

For classroom use, the recommended sequence is:

1. **Audio demo first.** Play recordings of all six sources in air
   (tuba, contrabass, loudspeaker, violin, clarinet, flute). Ask the
   audience to identify which family each belongs to.
2. **Helium demo.** Play the same recordings in helium.
   - Tuba and clarinet and flute shift dramatically — air-column
     resonators.
   - Contrabass and violin do not shift — string resonators.
   - Loudspeaker does not shift, but for a different reason —
     externally driven, no internal resonance.
3. **Write the two tables** above on the board. Establish that
   *categorically different physical phenomena* produce acoustically
   similar outputs; the medium swap separates them.
4. **Then make the framework move.** Introduce `H_0` as a tuba- or
   flute-pitch and `Ω_Λ = 13/19` as a contrabass- or violin-pitch.
   The audience now has the right intuition for *what kind of claim*
   each framework prediction is.

The whole demonstration takes ~15 minutes and primes the audience for
why "the same in any unit system" and "the same at any cosmic epoch"
are non-trivial commitments rather than empty claims.

## Companion documents

- [`comparison_class.md`](comparison_class.md) — the framework's peer
  group (GUTs, string theory, etc.) and why the Standard Model is not
  the comparison.
- [`unitless_check.md`](unitless_check.md) — the formal demonstration
  that every dimensionless prediction of the framework is invariant
  under unit choice (`ℏ = G = c = 1` reproduces every digit).
- [`address_and_quantity.md`](address_and_quantity.md) — the
  conceptual articulation of the address-vs-quantity distinction
  underlying this demo.
- [`expressibility_split.md`](expressibility_split.md) — the formal
  articulation of the lambda / EML split as notational invariance,
  using the bowed-string vs. flute pair as opening intuition.

## Status

Pedagogical / methodological orientation. Cited from the README's
second clarifying note. No new derivations; this document is the
audience-facing analogue of the address-vs-structure split that
already lives in the framework's foundational documents.
