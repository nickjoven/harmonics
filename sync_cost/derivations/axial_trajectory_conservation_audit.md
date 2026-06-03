# Axial trajectory conservation audit — chirality fineness verdict

## Status

**Audit verdict: APPARATUS INSUFFICIENT.** The framework's
current Klein-Z_2 antiperiodic structure conflates four
structurally distinct ± axes (direction of travel, spin,
chirality, arrow of time) into a single Z_2. The geometric
progression `string → cylinder → cone` of unlocked ± axes
requires these to be carried independently. The framework
carries one Z_2 doing multiple jobs at once, and that single
Z_2 is *not* fine-grained enough to host chirality-distinguishing
dissipation of the kind regime-change Class B/C work would
require.

Class: precondition audit for horn-branch regime-change work
(Class 3 articulation, verdict on existing apparatus capacity).
Precondition for Task 105 (horn-branch dissipation analysis);
independent of Task 106 (torus-branch winding geometry).

---

## What the audit checked

Four targets, mapping to the four ± distinctions identified in
the `string → cylinder → cone` progression and the prior
conversation's regime-change framing:

1. **Klein-Z_2 antipodal structure** — does it carry chirality
   as an independent axis, or does it collapse direction-of-travel
   and handedness into a single ±?
2. **V_4 phase states (A, B, C, D)** — are they chirality-labeled
   or chirality-blind?
3. **`k_lepton = q_3²` chirality-doubling claim** — is the
   doubling factor explicit in the V_4 structure or implicit?
4. **Cascade depth** — does it have a directional structure
   (apex-ward vs base-ward in cone terms) or is it a scalar level
   index?

---

## What the audit found

### Target 1 — Klein-Z_2 antiperiodic structure

The Klein bottle has **two directions**:

- **x: antiperiodic** (twisted, orientation-reversing on full
  traversal). Identification: `(0, y) ~ (1, 1-y)`. Sign-flip on
  return: `f(x+L_x, y) = −f(x, L_y−y)`.
- **y: periodic** (untwisted, ordinary cycle). Identification:
  `(x, 0) ~ (x, 1)`. No sign-flip.

The single antiperiodic direction does multiple jobs:

| Job | Source |
|---|---|
| Complex amplitudes (J² = −I) | `complex_amplitude_uniqueness.md` Step 2 |
| Spin / fermion Z_2 | implicit in same |
| Arrow of time / irreversibility | `klein_bottle.md` §"Where time lives" L274 |
| Substrate's only Z_2 carrying the half-twist | `klein_bottle.md` §"Two directions" L280 |

**The four jobs share one Z_2.** Anything that flips sign on
x-traversal flips all four simultaneously. There is no
mechanism in the current apparatus for chirality to flip
independently of spin, or for direction-of-travel to flip
independently of arrow-of-time.

**Verdict on Target 1: insufficient resolution.** The Z_2 is
real but bundled.

### Target 2 — V_4 phase states (A, B, C, D)

`generation_mechanism.md` §1 labels V_4 states by
`{locked, unlocked}²` over the two foundational primes `q_2, q_3`:

| State | q_2 locking | q_3 locking |
|---|---|---|
| A | locked | locked |
| B | locked | unlocked |
| C | unlocked | locked |
| D | unlocked | unlocked |

**No chirality labels.** The four states are distinguished by
their locking profile, not by handedness. There is no L/R or
±-chirality label on V_4 states.

V_4 has a natural Z_2 × Z_2 structure, but neither Z_2 is
labeled as chirality — they're labeled as "is q_2 locked?" and
"is q_3 locked?" respectively. These are *substrate-mode-state*
distinctions, not handedness distinctions.

**Verdict on Target 2: chirality-blind.** The V_4 structure
distinguishes lock-state-pairs but not chirality.

### Target 3 — k_lepton = q_3² chirality-doubling claim

`mass_sector_closure.md` L54-64:

> A lepton sits in an SU(2) doublet ... the left-handed and
> right-handed components each contribute an SU(2) adjoint
> worth of interactions:
>
>     k_lepton = (chiral copies) × (adj dim) = 2 × 3 = 6 ?
>
> No. The formula is *squared*, not doubled:
>
>     k_lepton = (dim adj SU(2))² = 9

The framework explicitly considers chirality-doubling (the `2 × 3
= 6` naive reading) and **rejects it in favor of squaring**. The
squared formula `q_3² = 9` is the actual structural derivation;
the "chirality" appellation in subsequent prose (L121-123) is a
*retrospective gloss* explaining the q_3² vs q_2³ asymmetry
between sectors (leptons squared, quarks not).

The chirality structure is therefore:

- **Invoked as a structural fact** to explain why leptons get
  squared adjoint and quarks get direct adjoint.
- **Not carried as a dynamical axis** along which the dynamics
  can vary. The 9 vs 8 is a one-time count, not a chirality-
  parameterized family.

**Verdict on Target 3: implicit and one-shot.** Chirality
explains a static count but does not provide a dynamical ± axis.

### Target 4 — Cascade depth directionality

Cascade-depth references throughout the framework (e.g.,
`tick_continuum_construction.md`,
`proposed_residual_closure.md`'s kink-mass-ratio reading
`b^(−n/(2d))`) treat depth as a scalar level index `n` — a
non-negative integer counting how deep in the cascade hierarchy
the object lives.

The cascade has *increasing depth* as a direction in the sense
that higher `n` is structurally "deeper," but there is no
explicit **±**-labeled apex-ward vs base-ward distinction. The
cascade is a one-way ladder; "going up" and "going down" the
ladder are operationally distinct (rescaling by `b` or `1/b`)
but are not carried as a Z_2 axis attached to substrate states.

**Verdict on Target 4: scalar index, not ± axis.** The cascade
has direction in the sense of "deeper" vs "shallower" but does
not carry chirality-like ± structure.

---

## Synthesis — what the framework actually has

The framework's current apparatus carries **one Z_2** (the
Klein-bottle x-antiperiodic) doing four jobs (complex amplitudes,
spin, arrow of time, half-twist), **one Z_2 × Z_2** (V_4
locking-states, neither labeled as chirality), **one structural
chirality invocation** (mass-sector squaring), and **one scalar
cascade index** (no Z_2 attached).

Of the **three independent ± axes** the geometric progression
calls for:

| Axis | Geometric progression source | Framework carries it? |
|---|---|---|
| Direction of travel | String level | Bundled into Klein-Z_2 |
| Chirality (helical handedness) | Cylinder level | Invoked structurally, not dynamically |
| Scale direction (apex-ward) | Cone level | Scalar cascade index, not Z_2 |

**Net resolution: roughly 1.5 axes carried, with the second**
**(chirality) only invoked as a one-time structural fact and**
**the third (scale-direction) not Z_2-axed.**

For regime-change Class B/C work that requires
chirality-distinguishing dissipation across the substrate→tree
boundary, this is **insufficient**. Standard SM mass running is
*explicitly chirality-distinguishing*: left-handed and
right-handed components run with different anomalous dimensions
through Yukawa couplings. A horn-branch dissipation profile that
reproduces SM-like running has to carry the same chirality
distinction. The framework's current single bundled Klein-Z_2
cannot host that distinction without further structural work.

---

## Specific implications

### For Task 105 (horn-branch regime change)

**Blocked, with a specific block named.** Horn-branch work
cannot proceed cleanly until chirality is promoted from
"structural fact explaining `k_lepton = q_3²`" to an independent
± axis on which substrate dynamics can vary. This is a
substantial extension, not a small clarification.

Estimated cost of the chirality extension: 2–5 iterations of
foundational substrate work. Plausible directions:

- **Promote V_4's Z_2 × Z_2 to Z_2 × Z_2 × Z_2** with the third
  Z_2 being chirality. This adds a fifth phase state per
  observable, increasing the state count from 4 to 8 (or three
  observable + dark to 7 observable + dark; structural questions
  about the count and observability follow).
- **Distinguish chirality from antiperiodicity** within the
  Klein bottle by introducing a second antiperiodic cycle. But
  this contradicts `complex_amplitude_uniqueness.md` Step 2's
  single-antiperiodic-cycle uniqueness (which forces ℂ rather
  than ℍ). Likely not viable without restructuring the complex-
  amplitude derivation.
- **Add cascade-level chirality** as a ± attached to cascade
  steps (each level can be "left-going" or "right-going" in the
  cascade direction). Compatible with current cascade scalar
  structure, but requires new substrate apparatus for the
  attached Z_2.

None of these is bounded enough to attempt before the audit
verdict is reviewed. Task 105 should not begin until the
extension path is selected and at least its precondition has
been worked.

### For Task 106 (torus-branch winding geometry)

**Independent, can proceed.** The torus-branch question
("does `(q_2, q_3)` arise from torus winding numbers?") is a
foundational structural question that doesn't depend on chirality
resolution. It can be attempted in parallel.

### For framework predictions currently in the moat

**No impact.** The audit verdict concerns whether the framework
can *extend* to close currently-open items (Classes B and C). It
does not affect the predictions currently in `framework_status.md`
Survives category. The moat is unchanged.

### For the Klein-Z_2 / complex-amplitude apparatus

**Preserved.** The single antiperiodic cycle's role in producing
complex amplitudes is structurally sharp and shouldn't be
disturbed. Any chirality extension has to be *added* (e.g., via
V_4 promotion or cascade-attached Z_2), not *substituted*.

---

## Falsifiers for the audit verdict

The verdict ("apparatus insufficient for chirality-distinguishing
dynamics") would be wrong if:

- **Chirality is already dynamically carried somewhere not
  surveyed in this audit.** Possible: cascade depth might carry
  chirality implicitly via signed running (depth `+n` vs depth
  `−n`). The audit found no evidence for this but did not
  exhaustively survey cascade dynamics docs. Would need a
  positive demonstration from cascade apparatus to overturn.
- **Klein-Z_2 antiperiodicity is more fine-grained than the
  audit credits.** Possible: the `f(x+L_x, y) = −f(x, L_y−y)`
  identification might decompose into independent sign-flip and
  reflection components, with one carrying spin and the other
  carrying chirality. This would require an explicit decomposition
  not currently in `klein_bottle.md` or `complex_amplitude_
  uniqueness.md`.
- **The geometric progression itself is wrong** about chirality
  being a distinct ± axis from spin. Possible at a deep
  theoretical level, but standard physics (Dirac equation,
  electroweak Lagrangian) explicitly treats spin and chirality as
  distinct labels. Unlikely to be wrong without a substantial
  physics-foundations argument.

Each falsifier is concrete and addressable. The verdict should
be considered provisional pending response to the most likely
of these (Klein-Z_2 decomposition).

---

## Recommended next iteration

If the verdict stands, the most direct next-leg work is the
**chirality extension** itself rather than horn-branch closure.
Candidate first iteration:

> Test whether the V_4 structure admits a substrate-internal
> third Z_2 labeled as chirality, without disrupting the
> existing complex-amplitude derivation (single antiperiodic
> cycle) or the lepton vs quark mode-count derivation
> (`k_lepton = q_3²` vs `k_quark = q_2³`).

If V_4 → V_4 × Z_2_chirality is substrate-natural, horn-branch
work becomes attemptable on the extended apparatus. If it isn't,
the chirality extension path branches:

- Add chirality via cascade attachment (Z_2 per cascade step)
- Add chirality via klein-bottle restructure (second antiperiodic
  cycle, conflicting with current ℂ derivation)
- Accept the framework's reach for Class B/C as bounded by
  current apparatus and move Class B and C to permanent empirical
  shelf alongside Koide

The third option is the basepoint-principle-disciplined exit if
the extension paths fail.

---

## Cross-links

- `klein_bottle.md` — Klein bottle structure, antiperiodic
  x-direction, periodic y-direction.
- `complex_amplitude_uniqueness.md` — single antiperiodic cycle
  → ℂ derivation; constraints on adding cycles.
- `mass_sector_closure.md` — `k_lepton = q_3²` derivation,
  chirality invocation, lepton vs quark asymmetry.
- `generation_mechanism.md` (D34) — V_4 phase states from
  `{locked, unlocked}²`, no chirality labels.
- `tick_continuum_construction.md`, `proposed_residual_closure.md`
  — cascade depth scalar index, no directional ± structure.
- `koide_form_substrate_iteration_14.md` — prior conversation's
  identification of chirality fineness as Class B/C precondition.
- Framework progression — three ± axes from `string → cylinder
  → cone` developed in the prior conversation; chirality is the
  cylinder-level axis the framework's Klein-Z_2 doesn't carry
  independently.

---

## One-line summary

The framework's current Klein-Z_2 antiperiodic apparatus carries
roughly 1.5 of the 3 ± axes the regime-change Class B/C work
needs — the single Klein bottle x-antiperiodic does spin, complex
amplitudes, arrow of time, and half-twist simultaneously
(bundled into one Z_2); V_4's Z_2 × Z_2 distinguishes locking
states but not chirality; the `k_lepton = q_3²` chirality
invocation is a one-time structural explanation rather than a
dynamical ± axis; cascade depth is a scalar index without
directional ± structure — so chirality-distinguishing dissipation
of the kind SM mass running requires is not hostable on the
current apparatus, **horn-branch Task 105 is blocked** until a
chirality extension is worked (estimated 2-5 iterations), the
extension itself has three candidate paths (V_4 promotion to
V_4 × Z_2_chirality, cascade-attached Z_2, klein-bottle
restructure with second antiperiodic cycle conflicting with
current ℂ derivation), torus-branch Task 106 is independent and
can proceed in parallel, and the falsifier most worth testing
before committing to the extension work is whether Klein-Z_2's
`(x+L_x, y) → (x, L_y−y)` identification admits an explicit
decomposition into independent sign-flip and reflection
components that the current apparatus implicitly carries
without naming.
