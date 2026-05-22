# Entry-point teaching reference

This is a second teaching layer for `nickjoven/harmonics`. It answers:

- Can each repository entry point become an accessible teaching reference?
- What should a learner understand before using it?
- What should they be able to do afterward?
- Are state standards or concept-understanding metrics useful?

Short answer: yes, an accessible reference is possible for each entry
point, but not every entry point should become a full lesson. The better
unit is a small reference card with a stable pattern:

1. ordinary phenomenon
2. plain-language idea
3. standard physics/math name
4. framework move
5. learner task
6. claim status
7. receipt links

## Standards stance

State standards can help, but only lightly. They are best used as a
translation layer, not as curriculum authority.

Useful:

- NGSS-style science practices: model, argue from evidence, use math,
  interpret data, define system boundaries.
- Common-Core-style mathematical practices: reason quantitatively, use
  structure, move between representations, check units and assumptions.
- AP or intro-physics topic progressions: waves, oscillations, fields,
  energy, probability, symmetry.
- Concept-inventory style checks: ask for transfer to a new example,
  not recitation of the repo's vocabulary.

Not useful:

- Exact state-code alignment at this stage.
- Treating the framework as high-school curriculum.
- Making the audience pass through all prerequisite math before the
  story can begin.

The practical metric should be: can the learner explain the idea in a
new everyday example, manipulate a toy model, and state what the
framework does and does not claim?

## Understanding metrics

Use six lightweight metrics across both simple and hard material.

| Metric | Simple material | Hard material |
|---|---|---|
| Phenomenon recognition | Name the everyday pattern. | Identify the physical regime and assumptions. |
| Model use | Predict what changes when one knob moves. | Derive or reproduce the model relation. |
| Representation translation | Move between words, picture, and simple equation. | Move between derivation, graph, equation, and status table. |
| Quantitative sense | Compute a ratio or threshold. | Reproduce count, residual, or dimensional classification. |
| Transfer | Give a new example with the same structure. | Apply the structure to a neighboring derivation without overclaiming. |
| Claim hygiene | Say "what this does not claim." | Classify as structural, anchor-side, bare reference, Class 2, declined, or open. |

These metrics are more useful than school-grade labels because the
audience is mixed: some viewers are casual science fans, some are
engineers, some are physicists, some are mathematicians. The same card
can serve all of them if it has a visible ladder.

## The two ladders

Every accessible reference should have two ladders.

### Simplicity ladder

1. **Image**: one visual metaphor.
2. **Sentence**: one claim in plain English.
3. **Toy task**: one thing to calculate, move, or predict.
4. **Named concept**: standard term.
5. **Framework move**: what Harmonics adds.

### Hardness ladder

1. **Assumptions**: what must be granted.
2. **Formal object**: equation, group, graph, topology, or count.
3. **Derivation step**: what follows from what.
4. **Audit status**: survives, anchor-side, declined, etc.
5. **Failure mode**: how a learner can over-read it.

The ladders let the same entry point be accessible without being shallow.

## Conceptual entry points E1-E6

These are the six README entry points. Each can be made accessible, but
the public order should usually start with phase/coupling before E1.

| Entry | Teaching card | Simple target | Hard target | Check for understanding | Status caution |
|---|---|---|---|---|---|
| E1: cosmic partition | "Counting locked modes" | Fractions as parts of a whole; pie chart of 13:5:1. | Farey depth, Z6 mode filters, single-w vs two-component closure. | Compute 13/19 and explain why it is a mode count, not a pixel count. | Use `MANIFEST.yml` and `framework_status.md`; avoid framework-level "zero free parameters." |
| E2: MOND threshold | "A cosmic clock sets a low-acceleration threshold" | Orbits below a threshold behave differently. | `a0 = c H0 / (2 pi sqrt(g*))`, RAR, partial locking. | Explain why the threshold is acceleration, not distance. | H0 is an anchor; redshift dependence is a test path. |
| E3: spatial dimension | "Why three directions?" | Space has three independent directions; symmetries constrain directions. | Mediant -> SL(2,R), dimension 3, Lorentz connection. | Give the difference between observing 3D space and deriving a three-dimensional symmetry. | This is hard; teach as an advanced receipt, not an early hook. |
| E4: cosmological constant | "Tiny from repeated depth" | Repeated multiplication can make very small numbers naturally. | `R = 6 * 13^54`, `Lambda l_P^2 = 13^-108 / 12`. | Place `10^-122` on a log scale and describe why "small" is not automatically "tuned." | Needs careful comparison to standard QFT assumptions. |
| E5: strong CP | "A symmetry removes a dial" | Some symmetries forbid a parameter from turning on. | Klein-antipodal Z2 and theta = 0. | Explain how "forbidden by symmetry" differs from "small by accident." | Requires source cleanup: README points indirectly through status map. |
| E6: hierarchy problem | "Not every small ratio is the same problem" | A problem depends on the rules of the theory asking it. | Naturalness, Wilsonian RG, anchor-side vEW, two-anchor minimum. | State the three ingredients of the SM hierarchy framing and which fail to translate. | Teach as epistemic discipline, not as victory lap. |

## Site and document entry points

These are the practical surfaces a learner can click.

| Resource | Current role | Accessible reference possible? | Best learner task | Best audience |
|---|---|---|---|---|
| `README.md` | Narrative front door plus catalog. | Yes, but it needs a claim-hygiene pass against stricter status files. | Find the first claim, then classify it: structural, anchor-side, or declined. | Curious general reader. |
| `index.html` | Public landing page with situation, equation, scorecard, reading order. | Yes; it should become the guided "start here" page. | Explain the one equation and choose the next path. | General reader to technical reader. |
| `docs/index.html` | Quick reference, predictions, proof chains, primitives. | Yes; best as a status board. | Pick one row and trace its source. | Reader who wants receipts quickly. |
| `docs/glossary.html` | Interactive chalkboard for symbols/numbers. | Yes; make it the "what does this symbol mean?" page. | Click one expression and reproduce the arithmetic. | Any reader stuck on vocabulary. |
| `docs/phenomenon-glossary.html` | Dynamics-first glossary. | Very yes; this is already closest to public teaching. | Start from a phenomenon and recover the textbook name. | Science-channel audience. |
| `docs/derivations.html` | Narrative index of phases and scripts. | Yes, as a map rather than a lesson. | Identify which derivation belongs to which teaching episode. | Technical reader. |
| `docs/preprint.html` | Four-document external presentation. | Yes, but only after orientation. | Choose the right deliverable for a question: glossary, lemmas, cross-reference, atlas. | Specialist, reviewer, collaborator. |
| `docs/mastery-graph.html` | Concept prerequisite graph. | Yes; this should drive the teaching syllabus. | Pick a node, explain its prerequisites, then transfer it to a new example. | Learner at any level. |
| `docs/claim-chain.html` | Manifest-generated claim chain. | Yes, as the public receipt graph. | Follow one prediction from primitive to status. | Skeptical reader. |
| `docs/claim-chain-views.html` | Math, syllogism, and patch-style views. | Yes, as alternate representations. | Translate one node between all three views. | Mathematically playful reader. |
| `docs/dag.html` | Full derivation dependency graph. | Partly; too much for first teaching. | Trace lineage and identify source depth. | Maintainer or advanced reviewer. |
| `prototype/index.html` | Metronome wall demo. | Absolutely; this is the best first interactive. | Move K and predict when simple ratios lock. | General reader. |
| `docs/knobs/*.html` | Single-knob explainers. | Yes; each can be a micro-lesson. | Change one knob and describe what changed. | General reader. |
| `sync_cost/applications/stern_brocot_walk.html` | Walk through mediants. | Yes; ideal for the rationals lesson. | Generate 2/5 from 1/2 and 1/3, then explain why it is "between." | General to math-curious. |
| `sync_cost/applications/mobius_projector.html` and `mobius_views.html` | Modular group visuals. | Yes, but advanced. | Identify a transformation that preserves structure. | Math-curious or specialist. |
| `sync_cost/applications/ontology.html` | Framework ontology browser. | Partly; use after vocabulary stabilizes. | Classify a term as primitive, derived, prediction, or method. | Collaborator. |
| `sync_cost/applications/double_pendulum.html` | Chaotic-coupling reference. | Yes as contrast. | Explain why chaos is not the same thing as mode locking. | General reader. |
| `sync_cost/applications/three_body_catalog.html` | Periodic orbit catalog. | Optional. | Compare periodic orbit, quasi-periodic motion, and lock. | Physics-curious reader. |
| `docs/archive/colony.html` | Smooth zoom archive. | Maybe; use as mood/visual synthesis, not proof. | Name the objects that appear in the zoom. | Returning reader. |
| `docs/archive/collatz.html` | Archived proof attempt. | Yes as methodology, not framework core. | Identify the unresolved step and why honesty matters. | Advanced skeptical reader. |

## Mastery-graph clusters as syllabus units

The existing `docs/mastery-graph.json` already supplies a strong
standards-like structure without importing school standards. Its 13
clusters can become the syllabus taxonomy.

| Cluster | Public question | Simple performance | Hard performance |
|---|---|---|---|
| Periodicity | What does it mean to repeat? | Draw phase on a circle. | Use winding number and modulo language correctly. |
| Waves and resonance | How does a system carry rhythm? | Identify resonance and harmonics. | Read a power spectrum as evidence. |
| Coupled oscillators | What happens when rhythms tug each other? | Predict lock vs drift from coupling/detuning. | Use circle-map language and Arnold tongues. |
| Stick-slip and thresholds | Why do regimes switch? | Describe threshold behavior. | Connect partial locking to MOND-like transitions. |
| Parabola and bifurcation | Why does x squared keep appearing? | Recognize a threshold pair appearing/disappearing. | Explain saddle-node universality. |
| Squares | Why probabilities and amplitudes square. | Explain area/basin intuition. | Connect basin measure to Born exponent. |
| Least action | How do equations come from a single functional? | Identify action as "path score." | Connect symmetry to conservation. |
| Quanta | Why some records are whole-numbered. | Distinguish continuous medium from discrete record. | Explain compactness and selection rules. |
| Rationals and best approximation | Why simple fractions matter. | Use the mediant. | Connect Stern-Brocot depth to mode accessibility. |
| Topology | What survives deformation? | Explain loop, flip, no-boundary pictures. | Use topology as a filter on allowed modes. |
| Symmetry and groups | What transformations preserve structure? | Spot a symmetry. | Use group/action language without handwaving. |
| Dimensional inputs and self-consistency | What is a parameter vs an anchor? | Sort a claim into structural or anchor-side. | Apply Z1-Z3 and Class 2/declined logic. |
| Framework predictions | Which claims survive audit? | Read the status badge. | Trace a prediction to source and residual. |

This is effectively a concept-standard map already. It is local to the
repo, tailored to the framework, and less likely to distort the material
than external standards.

## Suggested reference-card format

Each card should fit on one page.

```text
TITLE

Everyday hook:
One familiar phenomenon.

Plain idea:
One paragraph at science-channel level.

Standard name:
Textbook terms, with one-sentence definitions.

Framework move:
What Harmonics adds.

Try it:
One learner action: compute, sketch, move a slider, classify a claim.

Hard receipt:
The formal object and source file.

Claim status:
structural / anchor-side / bare K=1 reference / Class 2 / declined / open

What this does not claim:
One sentence.
```

## Example card: mode locking

Everyday hook: two pendulum clocks on the same shelf gradually settle
into a shared rhythm.

Plain idea: when oscillators influence each other, they may stop drifting
independently and lock into a simple whole-number rhythm.

Standard name: coupled oscillators, detuning, mode locking, Arnold tongue.

Framework move: stable records in the substrate are rational locks `p/q`;
as coupling changes, the available records form a devil's staircase.

Try it: move K in the metronome wall and predict whether a chosen tile
will drift, lock, or join a cluster.

Hard receipt: `prototype/README.md`,
`sync_cost/derivations/dynamical_quantization.md`,
`sync_cost/derivations/tongue_widths_exact.py`.

Claim status: standard dynamical-systems basis used by the framework.

What this does not claim: it does not claim spacetime is made of pixels.

## Example card: claim hygiene

Everyday hook: not every close guess is a good explanation.

Plain idea: a theory should track which matches are forced, which use an
anchor, which are suggestive, and which it declines.

Standard name: model validation, uncertainty, falsifiability, parameter
counting.

Framework move: Harmonics uses status classes such as structural/Z1-Z3,
anchor-side, bare K=1 reference, Class 2 coincidence, declined, and open.

Try it: classify `sin^2 theta_W = 8/35`. The correct current status is
bare K=1 reference, not a prediction at M_Z.

Hard receipt: `MANIFEST.yml`, `framework_status.md`,
`statistical_conventions.md`, `numerology_inventory.md`.

Claim status: methodological guardrail.

What this does not claim: it does not turn every near-match into evidence.

## Build order

1. Turn the mastery-graph clusters into 13 short concept cards.
2. Turn the six README entry points into six claim cards.
3. Turn the deployed resource list into a "where should I click?" guide.
4. Add status badges to every card.
5. Only after that, optionally crosswalk to NGSS/Common-Core/AP language.

This keeps the material teachable first and standards-compatible second.

Companion question atlas: `teaching/question-atlas.md` expands this map
into a complete v0 list of question prompts spanning public entry,
mastery-graph concepts, derivation steps, scorecard items, declined
claims, demos, hard review, falsifiers, and transfer.
