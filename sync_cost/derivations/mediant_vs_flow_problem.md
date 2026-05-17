# Mediant vs. flow: is a continuous flow *required*? — a hand-decidable problem statement

Competitor #1 (`thread_chronology.md` competing-readings set, held
unrecorded until the mechanics resolved; now ripe — `#TICK`
closed). Posed as a problem someone can decide by hand.

**Not "does the framework have Farey structure" — both readings
predict that.** The sine-circle-map produces the Stern-Brocot/Farey
mode-locking staircase as a textbook result (Arnold tongues); the
discrete mediant generator produces Stern-Brocot *by construction*
(iterated mediants *are* the tree). Farey structure does **not**
discriminate. The question must be posed around the single
structural difference that is quantitative and checkable.

## The two generative hypotheses

- **(Flow)** The confirmed structure is the mode-locking skeleton
  of a continuous circle-map flow (Adler / sine-circle). A
  continuous flow is *required*; discreteness is emergent
  mode-locking.
- **(Mediant)** The confirmed structure is the discrete mediant
  (Stern-Brocot) generator + XOR parity + EML weighting. **No
  flow required**; the continuum is the shadow
  (`substrate_determinism.md`).

The framework currently *asserts* (Mediant) at K=1 (the Finding-3
disposition: at K=1 the tongue-width truncation degenerates and
the 4-mode structure comes from the discrete kink-fills-loop
argument, not from circle-map tongue widths). This problem tests
whether that assertion is **forced** or whether a flow-only
fingerprint sneaks in.

## The single decidable difference: the K=1 complement

Both readings agree the structure *completes* at K=1 (complete
tree / complete staircase / kink-fills-loop). They disagree, in a
quantitative and checkable way, about **what the unlocked
complement at K=1 is**:

- **(Flow)** At the critical coupling the unlocked (quasiperiodic)
  set is a measure-zero **Cantor set of universal Hausdorff
  dimension `D ≈ 0.8700`**, with universal golden-mean scaling
  exponents `α, δ` (sine-circle-map criticality —
  Jensen–Bak–Bohr / Cvitanović universality). This number is
  parameter-free and is a **flow-only fingerprint**: the bare
  discrete mediant tree cannot produce it.
- **(Mediant)** At K=1 the tree is complete and the complement is
  **not a fractal Cantor set of irrationals** — it is "states not
  supported by the discrete substrate" (transcendental / limit
  points = shadow, per `substrate_determinism.md`'s
  discrete-vs-shadow partition: `π, e, φ` are limits, not
  substrate states). **No universal `D`**; the only invariants
  are combinatorial (exact XOR parity, exact 4-mode collapse,
  integer windings).

## The hand-decidable test

1. **Requirement check.** Is there *any* confirmed framework
   result that *requires* the universal critical signature
   (`D ≈ 0.8700`, golden-mean `α/δ`) — i.e., a prediction that is
   circle-map criticality and is **not** reproducible by the bare
   mediant generator? If yes → flow required.
2. **Support check.** Can the substrate dynamics even *support*
   circle-map criticality? `framework_status.md` "Eliminated"
   already records: the simulator is *Adler-only / gradient
   descent on a static potential, not a twist map*
   (`klein_spectrum.py`, `kuramoto_induced_map.py`). An
   Adler/gradient flow is monotone and has **no** critical-
   circle-map K=1 universality. If the substrate is Adler-only,
   the (Flow) reading cannot deliver `D ≈ 0.8700` either — then
   "the flow" is not the critical circle map but a soft Adler
   staircase, which is itself near-indistinguishable from the
   discrete locked structure → the flow is **eliminable by
   parsimony**.
3. **Direct numeric probe (the decisive measurement).** Compute
   the Hausdorff dimension of the K=1 locked-mode complement from
   the existing mode iteration (`field_equation_klein.py` /
   `klein_spectrum.py`):
   - `D ≈ 0.8700` (± universal scaling) ⇒ **flow required**;
     discrete-fundamental falsified; the continuum is fundamental
     and discreteness is emergent mode-locking.
   - complement trivial / empty (no fractal, dimension not the
     universal number) ⇒ **mediant suffices**; the flow is an
     unobservable adjunct, eliminated by the same parsimony move
     as the NAND/4→2 tightening.

## Outcomes

| Finding | Verdict |
|---|---|
| A confirmed result *requires* `D≈0.87`-type universality | **Flow required** — discrete-fundamental falsified |
| Nothing requires it **and** dynamics are Adler-only (no criticality) | **Flow eliminable** — mediant-fundamental favored by parsimony |
| Substrate supports criticality but `D` not yet probed | **Open** — run the K=1 complement Hausdorff-dimension measurement (test 3) |

The framework's existing "Adler-only / not a twist map"
eliminations lean toward row 2 (flow eliminable), but that is
*evidence*, not the decided answer — the decisive artifact is the
test-3 measurement, which has not been run. This document poses
the question; it does not answer it.

## Why this is the right discriminator

It isolates the **one** thing the two readings do not share: a
parameter-free universal *number* (`D ≈ 0.8700`) that the
continuous critical flow predicts and the discrete combinatorial
generator structurally cannot. Everything else (Farey structure,
tongue widths, completion at K=1) is common to both and therefore
useless as a discriminator. It is hand-decidable (a dimension
measurement on an already-coded iteration) and it has a clean
parsimony fallback if the dynamics turn out unable to support
criticality at all.

## Status

Class 3 (problem statement, not a resolution). Poses competitor
#1's discriminator as a hand-decidable question with a single
decisive numeric test. No new primitive. Anchored to the
mechanics now resolved (`#TICK` closed, #2 eliminated): with the
deterministic discrete reading constructively complete, the live
question is no longer "discrete or stochastic" (#2, settled) but
"is the discrete generator *sufficient*, or is a continuous flow
*required*" — this problem decides exactly that.

## Cross-links

- `thread_chronology.md` — competitor #1, now a posed open item
  (`#FLOW`); the discriminator stated here.
- `substrate_determinism.md` — the (Mediant) hypothesis
  (continuum = shadow); discrete-vs-shadow partition defines the
  K=1 complement under (Mediant).
- `tick_continuum_construction.md` — `#TICK` closed: the discrete
  tick constructs the continuum shadow. This problem asks the
  converse-flavoured question: is the *flow* nonetheless required
  to produce the locked structure, or is the mediant generator
  alone sufficient?
- `framework_status.md` — "Eliminated": Adler-only / not-a-twist-
  map evidence relevant to test 2.

## One-line summary

Pose it on the **K=1 complement**: the continuous critical flow
predicts a parameter-free universal Cantor dimension
`D ≈ 0.8700` that the discrete mediant generator structurally
cannot produce — so the decidable question is whether any
confirmed result requires that number (flow required) or whether
the dynamics are Adler-only with a trivial/empty complement (flow
eliminable, mediant-fundamental by parsimony); decisive test is
the K=1 locked-complement Hausdorff-dimension measurement, not
yet run.
