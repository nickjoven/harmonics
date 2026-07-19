# Tape physics as a dual-regime / basepoint correspondence

> **Question.** Scotch-tape peeling shows stick-slip at the peel front (and,
> in vacuum, emits X-ray flashes correlated with the slip events); magnetic
> cassette recording is high-fidelity *with* a high-frequency AC bias and
> grossly nonlinear *without* it; both are read through phase/frequency
> modulation. Across these tape systems, **does the framework see two
> regimes or a set of fixed points** — and which part of that picture is
> substrate-forced versus basepoint-declined?

**Verdict: MODAL ✓ / GENERATIVE (limited).** The framework states the
correspondence cleanly: tape systems are a tabletop realization of the
substrate's **two non-smoothly-decoupled regimes** (locked K=1 / stick vs
unlocked K<1 / slip), with the **fixed points living inside the locked
regime** as mode-locked states. The high-frequency carrier (peel-rate drive,
AC bias) is the **operational basepoint** that selects the regime. The
framework supplies the two-regime structure and the carrier:signal ratio; it
**declines** the absolute scales (bias frequency, coercivity, X-ray energy)
as basepoint/anchor-side per `basepoint_principle.md`.

This is a **phenomenological correspondence** in the register of the Tesla
note (`RESULTS.md` §"Connection to Tesla") and `medium_change_demo.md`: an
illustration of substrate machinery on a tabletop system, **not** a forced
quantitative prediction. Tape X-ray spectra, bias frequencies and tape
coercivities are external/anchor-side and are not predicted here.

Class: phenomenological correspondence / dual-regime illustration.
Resolution-mode throughout — composes existing canonical claims (the two
continuum limits, the Stribeck stick-slip lattice, the basepoint principle,
the FM-beat correspondence). **No substrate primitive added.**

---

## 0. Verify-before-assert ground

Re-read this session (load-bearing substrate content, read fresh, not recalled):

**(G1) The two regimes are non-smoothly decoupled.** The rational field
equation has a K=1 (critical / locked) continuum limit reproducing the ADM /
Einstein equations and a K<1 (subcritical / unlocked) limit reproducing
Schrödinger. Source: `continuum_limits.md` Claim §I–II. The two regimes are
separated by the **K=1 critical-line tongue-coverage discontinuity** and each
requires its own anchor; reduction to one is structurally obstructed. Source:
`README.md` §"Two independent anchors" (D.3 closure, `path_closures_iter3.md`)
and `basepoint_principle.md` instance "Dimensional inputs" (#ANCHOR rigorous
#5: two decoupled sectors ⇒ two scale-torsors).

**(G2) Stick = coherent transport, slip = dissipation; the dual regime is
numerically real.** In the Stribeck stick-slip lattice: below the bifurcation,
linear passthrough at the drive frequency (high η, ω_d dominant); above it,
frequency conversion to the subharmonic ω₀ which **propagates in the stick
regime** while the high-frequency mode **dissipates in the slip regime**.
"Two regimes, one lattice … the 'dual regime' is real." Source: `RESULTS.md`
§"Key Results" items 4–5, Experiment 2. Bifurcation threshold at drive
amplitude A ≈ 0.8; critical chain length N = 3.

**(G3) The basepoint discriminator.** The framework supplies torsorial
structure (relations, ratios, discrete counts) and never the basepoints. A
declined basepoint is a **structural feature iff** its absence is structurally
forced (an inviolable / no-equivariant-section / number-theoretic
obstruction), else it stays **open**. A dimensionful scale is an ℝ₊-torsor;
the anchors are unforced relational pegs, dynamically inert by
torsor-invariance. Source: `basepoint_principle.md` Statement, discriminator
table, and "Canonical instance: the dimensional inputs."

**(G4) Phase modulation has a substrate beat identity; amplitude modulation
does not.** With ω_n = 2π/n, the FM-beat identity ω_{ab} = |ω_a − ω_b| holds
iff a, b are consecutive integers; the Mihailescu-bounded composite chain is
{Z_6, Z_12, Z_72}. AM (K-iteration) is exponential relaxation, not cyclic, and
has **no** parallel beat identity. Source:
`fm_beat_crt_correspondence_audit.md` §1, §4, §7.

Session snapshot: CAS 390 (0 corrupt) | drift 0 | git clean | substrate clean.

---

## 1. The three tape systems and their external anchors

All three are **external physics** used as phenomenological anchors. They are
real and citable; none is a framework derivation, and the framework predicts
none of their absolute scales.

| System | External phenomenon | Literature anchor |
|---|---|---|
| **Peeling adhesive tape** | Stick-slip at the peel front; in moderate vacuum the slip events emit nanosecond X-ray flashes (hard enough to image), correlated one-to-one with stick-slip. | Camara, Escobar, Hird & Putterman, *Nature* **455**, 1089 (2008), [doi:10.1038/nature07378](https://doi.org/10.1038/nature07378). |
| **Magnetic cassette recording** | High-frequency AC bias (≫ audio band) linearizes the medium's hysteresis (anhysteretic recording); without bias, recording is grossly nonlinear with a dead zone near zero. | Standard magnetic-recording theory (anhysteretic magnetization; AC-bias linearization). |
| **Phase / frequency modulation readout** | The recovered signal's structure is read as phase/frequency modulation of a carrier. | Connects internally to `fm_beat_crt_correspondence_audit.md`. |

---

## 2. The single mechanism underneath: stick-slip is a relaxation oscillator

A stick-slip cycle is a **relaxation oscillator**: a slow *stick* phase that
loads energy coherently, punctuated by a fast *slip* phase that releases it
dissipatively. This is exactly the substrate's two-regime split read in time:

- **Stick phase ↔ locked / K=1 regime.** Strong coupling at low relative
  velocity (the Stribeck curve's high-μ branch, `driven_stribeck.py`); the
  contact is mode-locked, energy loads coherently. This is the regime where
  the subharmonic *propagates* (G2).
- **Slip phase ↔ unlocked / K<1 regime.** Weak coupling at high relative
  velocity; the stored energy releases as a fast, high-frequency, **dissipative**
  burst. This is the regime where the high-frequency mode *dissipates* (G2).

**Peeling tape (system 1) reads directly off this.** The slip events are the
dissipative release; the nanosecond X-ray flashes (Camara et al. 2008) are the
external signature of that slip-phase energy release (triboelectric charge
separation discharging). The stick phases are the coherent loading between
flashes. Under high-resolution imaging, the discrete, time-localized slip
events are the **locked fixed points of the cycle in time** — the temporal
analog of the mode-locked tongues. The framework's content is the *structure*
(relaxation oscillator = stick-load / slip-release = locked / unlocked); the
*X-ray energy and flash timing are basepoint-side* and are not predicted.

---

## 3. The headline answer: two regimes, with the fixed points inside one of them

The question "two regimes **or** fixed points?" presents a false choice. The
framework's answer is that these are **the same structure at two resolutions**:

1. **There are exactly two regimes.** The locked (K=1 / stick) and unlocked
   (K<1 / slip) regimes are **non-smoothly decoupled** (G1). This is the
   coarse-resolution reading: a medium is in one regime or the other, and the
   transition between them is a bifurcation (sharp), not a crossover.

2. **The fixed points live *inside* the locked regime.** They are the
   mode-locked states — Arnold tongues / remanent magnetization states /
   discrete slip events. The locked regime is *populated* by fixed points
   (the devil's-staircase plateaus). The unlocked regime has **no** fixed
   points: it is the linearized continuum (the gaps of the staircase, the
   anhysteretic line, the dithered-quantizer average).

3. **The high-frequency carrier is the basepoint that selects the regime.**
   The peel-rate drive and the AC bias are high-frequency carriers; whether the
   medium sits in the locked or unlocked regime depends on the carrier relative
   to the signal. By `basepoint_principle.md` (G3), the framework supplies the
   **two-regime structure** and the **carrier:signal ratio** (torsor-invariant),
   and **declines the absolute carrier scale** (an ℝ₊-torsor — bias frequency,
   coercivity, peel rate are unforced relational pegs).

So: **two regimes, with fixed points populating one of them.** Not a choice —
a resolution distinction (`CLAUDE.md`: "bare K=1 vs K<1 is itself a resolution
distinction").

---

## 4. Magnetic recording: the dual regime made concrete (with numerical witness)

Magnetic AC-bias recording is the cleanest of the three, because the two
regimes are directly measurable as transfer-curve linearity.

- **Unbiased ↔ locked / fixed-point regime.** The bare medium follows its
  *normal magnetization curve*: nonlinear, with a **dead zone** near the origin
  where distinct small signals collapse onto the same remanent state. This
  collapse *is* the lock-in: the hysterons near zero never switch, so the
  signal is quantized onto discrete remanent fixed points (the hysteresis
  branches). Low fidelity.
- **AC-biased ↔ unlocked / continuum regime.** A high-frequency carrier
  dithers every hysteron across its loop; as the carrier envelope decays (the
  element leaving the bias-field gap) the medium settles onto the
  *anhysteretic curve* — single-valued and linear through the origin. The dead
  zone closes. High fidelity.

`tape_bias_anhysteretic.py` (repo root, alongside `driven_stribeck.py`) is a
Preisach-ensemble witness of exactly this. Small-signal sweep, N = 4000
hysterons:

| regime | linearity R² | dead-zone fraction |
|---|---|---|
| **UNBIASED (locked)** | 0.805 | 0.50 |
| **AC-BIASED (unlocked)** | 0.9998 | 0.05 |

Same medium, two regimes. The unbiased transfer is nonlinear with a 50% lock-in
dead zone (distinct inputs → same remanent fixed point); the carrier dithers it
into a near-perfectly linear continuum (R² → 1, dead zone closes). The carrier
amplitude that effects this is the **basepoint** — the script sets it, the
framework does not derive it.

**Quantization, two regimes.** "With or without high-frequency [bias],
applying quantization" is the dithered-quantizer question. Without dither, a
quantizer has fixed points (lock-in to levels) — the deterministic
mode-locking regime. With a high-frequency dither (the AC bias), the
quantization error decorrelates and the average follows the input linearly —
the unlocked continuum. The two regimes are **deterministic lock-in (fixed
points)** vs **dithered linear (continuum)**, the same K=1 / K<1 split. There
are not three options; there are two regimes, and the fixed points are the
locked one.

---

## 5. Phase modulation at basepoint-principle resolution

"Phase modulation decomposition … at basepoint principle resolution" is the
instruction to decompose the modulation into its **torsor-invariant** part and
its **basepoint** part:

- **Torsor-invariant (framework supplies it).** Frequency/phase *ratios* and
  *beats*. By `fm_beat_crt_correspondence_audit.md` (G4), FM has a substrate
  beat identity ω_{ab} = |ω_a − ω_b| (consecutive integers; composite chain
  {Z_6, Z_12, Z_72}). The phase structure of a recorded signal decomposes onto
  these substrate beats — the part that is the same for any observer in any
  unit system.
- **Basepoint (framework declines it).** The **carrier scale itself** — the
  absolute frequency the modulation rides on (the AC-bias frequency, the
  cassette tape speed). This is the ℝ₊-torsor anchor; dynamically inert by
  torsor-invariance (G3), it adds a *reading*, not a dynamic.

Note the AM/FM asymmetry (G4) lands exactly on the bias mechanism: the **AC
bias envelope is amplitude modulation** (K-iteration-like exponential decay of
the carrier), which has **no** beat identity — it is the basepoint-setting
process, not signal content. The **signal is phase/frequency modulation**,
which carries the torsor-invariant beats. So "decompose at basepoint
resolution" cleanly partitions: FM = torsor-invariant signal; AM-bias =
basepoint-selection. The decomposition *is* the basepoint principle applied to
the modulation.

---

## 6. K-class assessment

**MODAL ✓.** The framework states the correspondence: each tape system maps
onto the locked/unlocked two-regime structure, with fixed points inside the
locked regime and the carrier as basepoint. All pieces are existing canonical
claims (G1–G4) composed in resolution-mode.

**GENERATIVE (limited).** The substrate *forces* the qualitative structure —
two regimes (not one, not three), fixed points only in the locked regime,
carrier-as-basepoint. It does **not** force any tape observable: X-ray energy,
bias frequency, coercivity, tape speed are all basepoint/anchor-side and
correctly declined. This is a **phenomenological correspondence**, peer to the
Tesla note and `medium_change_demo.md`, **not** a corroborated quantitative
prediction. It does not enter the predictions table.

K-class: this composes **K<1 substrate** content (the two-regime decoupling,
the tongue fixed points, the basepoint discriminator) — not a bare-K=1
arithmetic identity. But its *output* is a correspondence, not a number, so the
K<1/K=1 distinction applies to its inputs, not to a predicted value.

---

## 7. Falsification anchors

- **F-TAPE-1** (regime count). If a tape system exhibited a genuine *third*
  dynamical regime not reducible to locked/unlocked or to a basepoint choice
  between them, the two-regime claim (G1) would be strained. The framework's
  commitment is exactly two, forced by sector decoupling (#ANCHOR #5).
- **F-TAPE-2** (fixed points in the wrong regime). The claim places fixed
  points *inside* the locked regime and a featureless continuum in the
  unlocked regime. A demonstration of stable fixed points in the AC-biased
  (anhysteretic) continuum, or of a featureless continuum in the unbiased
  locked regime, would break the §3 reading. `tape_bias_anhysteretic.py`
  witnesses the predicted placement (dead-zone lock-in unbiased; continuum
  biased).
- **F-TAPE-3** (carrier not basepoint). If the framework could *derive* the
  AC-bias frequency or the tape coercivity from substrate primitives, that
  would **contradict** the basepoint principle (the bright line in
  `basepoint_principle.md` §"Bright line": deriving a declined basepoint
  falsifies the relevant forcing), not vindicate it. The correspondence
  requires these to remain declined.
- **F-TAPE-4** (AM/FM symmetry). If amplitude modulation were found to carry a
  substrate beat identity parallel to FM's, the §5 partition (FM =
  torsor-invariant signal, AM-bias = basepoint-selection) would collapse.
  `fm_beat_crt_correspondence_audit.md` §4 forbids this (AM = exponential, not
  cyclic).

---

## 8. What this audit does NOT claim

- **Not a prediction of any tape observable.** X-ray flash energy/timing
  (Camara et al. 2008), AC-bias frequency, tape coercivity, head-to-tape speed
  are all **external / basepoint-side** and explicitly declined.
- **Not a substrate primitive.** The correspondence composes G1–G4; it adds no
  primitive and no canonical object.
- **Not a corroborated prediction.** It is a phenomenological correspondence
  (Tesla-note / `medium_change_demo.md` register), and does not enter the
  `README.md` predictions table or `MANIFEST.yml`.
- **Not a claim that tape *is* the substrate.** Tape is a tabletop system whose
  dynamics happen to instantiate the same locked/unlocked structure; the
  framework's claim is structural correspondence, not identity.
- **Not an AM beat claim.** The AC-bias envelope is the basepoint-selection
  process; it carries no FM-style beat identity (G4).

---

## 9. Cross-references

**Built on:**
- `continuum_limits.md` — the K=1 (locked) and K<1 (unlocked) regimes as the
  two continuum limits of the rational field equation.
- `basepoint_principle.md` — the discriminator; carrier/scale as ℝ₊-torsor
  basepoint, declined; the bright line (F-TAPE-3).
- `RESULTS.md` (Stribeck lattice, Experiments 1–2) — stick = coherent
  transport, slip = dissipation; "two regimes, one lattice."
- `fm_beat_crt_correspondence_audit.md` — FM has a substrate beat identity, AM
  does not (the §5 partition and F-TAPE-4).

**Composes with:**
- `README.md` §"Two independent anchors" — the K=1/K<1 non-smooth decoupling
  forces two anchors (the regime-count commitment behind F-TAPE-1).
- `medium_change_demo.md` — companion phenomenological-correspondence register
  (tuba/contrabass; structure vs medium).
- `dynamical_quantization.md` — quantization lives in the coupling, not the
  geometry; the dithered-quantizer reading of §4 sits here.

**Simulation reference:**
- `tape_bias_anhysteretic.py` (repo root) — Preisach-ensemble witness of the
  unbiased-locked vs AC-biased-unlocked transfer (R² 0.805 → 0.9998; dead-zone
  0.50 → 0.05).
- `driven_stribeck.py`, `stribeck_lattice.py` (repo root) — the stick-slip
  relaxation-oscillator and lattice dynamics behind §2.

**Vocabulary discipline:**
- `vocabulary_is_the_work_pattern.md` — the audit names the correct framework
  objects (locked/unlocked regimes, mode-locked fixed points, carrier-as-
  basepoint) for a tabletop system, and declines the tabletop's absolute
  scales; naming the objects is the work.

---

## 10. One-line summary

Tape physics — peeling stick-slip (with its slip-correlated X-ray flashes, an
external relaxation-oscillator signature), AC-bias magnetic recording, and
phase-modulated readout — is a tabletop realization of the substrate's **two
non-smoothly-decoupled regimes** (locked K=1 / stick vs unlocked K<1 / slip):
the answer to "two regimes **or** fixed points" is **two regimes, with the
mode-locked fixed points living inside the locked regime and a linearized
continuum in the unlocked regime**, the high-frequency carrier (peel drive, AC
bias) acting as the **operational basepoint** that selects the regime — the
framework supplying the two-regime structure and the carrier:signal ratio and
**declining** the absolute scales (bias frequency, coercivity, X-ray energy) as
ℝ₊-torsor basepoints; a Preisach-ensemble witness (`tape_bias_anhysteretic.py`)
shows the unbiased medium locked onto remanent fixed points with a 50% dead zone
(R²=0.805) and the AC-biased medium dithered into a linear continuum (R²=0.9998,
5% dead zone); MODAL ✓ / GENERATIVE-limited, a phenomenological correspondence
in the Tesla-note / `medium_change_demo.md` register, **not** a corroborated
quantitative prediction and **not** a substrate primitive.
