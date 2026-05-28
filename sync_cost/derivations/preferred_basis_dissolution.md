# Preferred-basis dissolution

## Status

**Inviolable-companion dissolution articulated** — the QM
preferred-basis problem (why measurement settles on position
eigenstates, or energy eigenstates, or any other specific basis
rather than arbitrary superpositions) dissolves into **basin
selection** on the framework's substrate. Each measurement is the
system identifying which basin of attraction it sits in
(`lesson_forced_basin_selection.md`); the basin's natural coordinates
*are* the measurement's basis. No separate preferred-basis axiom is
required, and no global "preferred basis" exists — each measurement
context supplies its own basis via the substrate's saddle-node
bifurcation geometry.

Not a new derivation; a synthesis of ingredients already in the
corpus. The substrate is phase as the primary variable
(`substrate_determinism.md`, `figure_eight.md`); measurement is
basin selection (`lesson_forced_basin_selection.md`); the basin
width is `√ε` exactly (the saddle-node normal form, not a Taylor
approximation). The Born rule `= |ψ|²` is already structurally
forced (`figure_eight.md`, via `J² = −I`).

No new primitive.

This doc completes the framework's measurement-side dissolution
program:

- `collapse_dissolution.md` (#177) — dissolves the apparent
  non-unitary projection postulate (the measurement-problem-side).
- *This doc* — dissolves the preferred-basis problem (the
  basis-selection-side).
- `figure_eight.md` — Born rule `|ψ|²` structurally forced from
  `J² = −I` (the statistic).

Together, the framework's QM apparatus is complete at the structural
level: substrate phase + basin selection + Born statistic, with no
QM axiom remaining beyond the substrate itself.

---

## The statement

**Claim (preferred-basis dissolution).** On the framework's substrate
the QM preferred-basis problem is not a postulate but a near-tautology:
every measurement is a *basin selection* — the system identifying
which attractor it belongs to — and the basin's natural coordinates
are the measurement's basis. The basis is **local to the measurement
context**, fixed by the saddle-node geometry at the relevant
bifurcation. **There is no global "preferred basis"**; instead, each
measurement context supplies its own basis structurally, via the
substrate's bifurcation structure at that context.

What standard QM calls "the preferred basis" is therefore not a
property of the wavefunction, the Hamiltonian, the environment, or
the substrate-as-a-whole. It is a property of the *measurement
context's* saddle-node geometry — a local, structural quantity that
varies with context but does not require a separate axiom to select.

---

## Derivation

### Step 1 — The substrate's primary variable is phase

The framework's substrate (Klein-bottle rhythm locking, Z₂-graded)
has *phase* as the primary observable variable
(`substrate_determinism.md`'s discrete tick, `figure_eight.md`'s
phase-on-the-loop, `born_rule.md`'s phase-difference-as-observable).
Phase is the substrate's natural coordinate; everything else
(position, momentum, energy, ...) is an emergent observable in
specific measurement contexts.

This is not a postulate of this doc; it is the substrate's
already-installed apparatus.

### Step 2 — Measurement is basin selection

`lesson_forced_basin_selection.md` (the Tier-B engine-room lesson)
states the framework's mechanism for measurement explicitly:

> "Selecting an outcome" = which basin your starting point was in.
> So the probabilities of the outcomes are just the sizes of the
> basins. That's the whole idea — measurement is basin selection —
> and the rest of the lesson is: what fixes the basin sizes?
> (`lesson_forced_basin_selection.md` §1)

A measurement of a quantum system *is* the substrate's identification
of which basin of attraction the system flowed into. The basins are
fixed by the substrate's dynamics at the measurement context's
parameter values.

### Step 3 — Basin structure = saddle-node geometry

Near any measurement threshold the dynamics reduce (always, by
codimension-1 universality / Thom; `lesson_forced_basin_selection.md`
§2) to the saddle-node normal form

    dx/dt = μ − x²

For `μ > 0` there are two fixed points at `x = ±√μ`: one stable
(the attractor — the outcome), one unstable (the repeller — the
separatrix, the basin boundary). The basin's linear extent is

    Δθ ∝ √μ ≡ √ε        (ε = distance past threshold)

— **exactly**, not approximately, because the parabola *is* the
normal form at the bifurcation, not the leading term of something
unknown.

The basin's natural coordinates — the variable `x` itself plus the
attractor/separatrix axis — are determined entirely by the saddle-
node geometry. This is what "the basin structure" means.

### Step 4 — The basin's natural coordinates are the measurement's basis

The QM preferred-basis question asks: among all the bases the
Hilbert space supports (position, momentum, energy, arbitrary
superpositions), which is the basis the measurement *finds itself
in*?

On the framework's substrate, the answer is read off step 3: the
basis is whatever the basin's natural coordinates are at the
measurement context's saddle-node. The attractor axis is one basis
element; the separatrix-normal direction (the basin's width axis)
is its complement. The "basis" is what the substrate's local
bifurcation geometry says it is.

Different measurement contexts realize *different* saddle-nodes —
different `ε`, different basin widths, different basin axes — and
therefore different bases. Position-measurement contexts realize
position-basin geometries; momentum-measurement contexts realize
momentum-basin geometries; etc. The contexts differ in *which
substrate coupling* drives the bifurcation; the substrate's phase
variable is invariant, but its couplings to context differ.

So the "preferred basis" *varies with measurement context* and is
*structurally specified* in each context by its saddle-node
geometry. There is no global preferred basis to axiomatize.

### Combined

Steps 1–4 close the dissolution. The QM preferred-basis problem
asks "which basis is the basis"; the framework answers "the basin's
natural coordinates from the saddle-node at this measurement
context." The substrate carries no separate preferred-basis
postulate, because it carries the *mechanism* for generating bases
from local bifurcation geometry, which is enough.

---

## What this says (and what it does not)

It **says**:

- The QM preferred-basis problem dissolves structurally: no global
  preferred basis axiom is required; each measurement context's
  saddle-node geometry supplies its own basis.
- The basin's natural coordinates *are* the measurement's basis,
  fixed by the substrate's bifurcation structure at that context.
- The substrate's phase variable is invariant; the emergent
  observables (position, momentum, energy, ...) come from how the
  substrate's phase-coupling realizes specific saddle-nodes in
  specific contexts.
- Decoherence-style einselection is replaced by *basin geometry* as
  the basis-selection mechanism — the saddle-node's structure is
  the einselector, not an environmental robustness argument.

It does **not** say:

- That this predicts *which* observable is measured in any specific
  experimental context. The basin geometry at each context is fixed
  by the substrate-coupling specification of that context — which
  is the experimental setup, not derivable from substrate primitives
  alone.
- That position is universally preferred, or that the position-
  momentum split is itself a substrate consequence. The framework's
  substrate is phase; *position* and *momentum* are emergent
  observables in specific measurement contexts; the position/momentum
  duality is the basin/co-basin axis pair at certain contexts, not
  a substrate-level distinction. (Position-measurements set up
  different saddle-nodes than momentum-measurements; both are
  emergent from how the substrate couples to the measurement
  apparatus.)
- That this resolves all QM interpretational debates. It is a
  structural dissolution of *one specific* puzzle (the basis-
  selection question); it does not adjudicate Copenhagen vs.
  many-worlds vs. Bohm at the ontological level. The framework's
  stance is structural: there is no preferred-basis problem on this
  substrate because there is no separate preferred-basis axiom to
  reconcile, and the appearance of basis-selection has a derived
  mechanism (basin geometry).
- That the framework derives the Hilbert space, the operators, or
  the specific Hamiltonians of QM. Those remain open in the same
  column as the magnitude of gravity (`equivalence_dissolution.md`'s
  parallel): the framework supplies the *form* (basis ≡ basin) and
  declines the *magnitudes* (specific operator spectra, specific
  energy values) per the Basepoint Principle.

---

## Distinct from interpretational positions

The framework's stance on basis selection is structural, not
interpretive. To make this concrete:

- **Decoherence / einselection** (Zurek, Joos-Zeh): the environment
  selects "robust" bases via decoherence-induced einselection. The
  preferred basis is "what survives interaction with the environment."
  The framework rejects the need for environmental machinery: the
  saddle-node's basin geometry *is* the basis at every context, no
  environment required beyond the measurement-context's substrate
  coupling. (Decoherence still applies as an effective description
  in many cases, but it is not a foundational requirement.)
- **Many-worlds**: every measurement branches into all bases; the
  preferred-basis problem is "which branching." The framework does
  not need branching: each measurement context has *one* basin
  geometry and *one* selected basis, structurally specified. No
  branching ontology is invoked.
- **Copenhagen**: which observable is measured is an external act
  by an observer; the preferred basis is a postulate of the
  measurement-as-act framework. The framework rejects the external-
  observer postulate: the basis-selection is internal to the
  substrate's saddle-node dynamics, and the observer is part of
  the substrate-coupling specification, not an external act.

The framework's position: there is no preferred-basis problem
because the substrate carries the *mechanism* for generating a basis
per context (saddle-node basin geometry), and no separate
basis-selection axiom is required.

---

## Exhibited consequences

- **Born rule operational meaning sharpened.** The Born statistic
  `|⟨φ|ψ⟩|²` is already structurally forced (`figure_eight.md`,
  `born_rule.md`). The dissolution here clarifies *what `|φ⟩`
  represents*: it is a basis state in the saddle-node's basin
  coordinates at the measurement context, not an axiomatic "preferred
  basis state."
- **Uncertainty relation as basin geometry.** The basin width
  `Δθ ∝ √ε` at the saddle-node *is* the uncertainty in the
  context's basis. The uncertainty relation `τΔθ = const`
  (`fidelity_bound.md`) reads as a consistency condition on the
  basin geometry — the saddle-node's two axes (attractor +
  separatrix) carry conjugate-variable structure.
- **Decoherence as basin-gradient.** When environmental coupling
  pushes the system off-attractor, the basin gradient drags it
  back; "decoherence" is the substrate's natural relaxation along
  basin gradients, not a separate environmental mechanism.
- **The "context" of a measurement is substrate-specified.** What a
  measurement context "is" reduces to which couplings the substrate
  realizes at that context. The framework does not predict *which*
  context arises in a specific lab setup — that is the experimental
  specification — but the basis in that context is structurally
  fixed by the saddle-node.
- **One pillar of the framework's measurement-side dissolution
  program is in place.** Together with `collapse_dissolution.md`
  (no non-unitary projection postulate) and `born_rule.md` /
  `figure_eight.md` (Born statistic structurally forced), the
  framework's QM apparatus is complete at the structural level.

---

## Falsifiers

- **A demonstrable preferred basis that is *not* explicable as a
  saddle-node basin geometry.** If experimental evidence supports
  a "true preferred basis" that survives all contexts — say, an
  observable whose basis is invariant under change of measurement
  apparatus, *not* fixed by local saddle-node — the dissolution
  fails: the substrate would need a separate preferred-basis
  postulate.
- **A measurement whose basis does not track its saddle-node
  geometry.** The dissolution predicts that the basis a measurement
  realizes is the basin's coordinates at the relevant saddle-node.
  A measurement whose realized basis diverges from this prediction
  (at sufficient experimental precision) would void step 4.
- **The basin width `Δθ ∝ √ε` failing to track measurement
  uncertainty.** Since the basin width *is* the uncertainty in the
  context's basis, a measurement whose observed uncertainty does
  not scale as `√ε` (the parabola threshold's exact form) would
  void step 3 — and possibly require revising the basin-selection
  reading of measurement entirely.
- **Decoherence in isolated systems** (no environmental coupling).
  The dissolution explains decoherence as basin-gradient relaxation,
  not as environmental interaction. A demonstration that decoherence
  proceeds without any saddle-node basin gradient would be a
  separate effect requiring its own substrate machinery.

---

## Why this matters

The QM preferred-basis problem had been sitting on the implicit-
import ledger — the framework's collapse dissolution
(`collapse_dissolution.md`) handled the apparent non-unitary
projection, but the basis-selection question was named as a
remaining open item in the capstone synthesis
(`gr_qm_unification_synthesis.md`, "What this does not say" §). This
doc closes that gap: there is no preferred-basis problem on this
substrate, because the saddle-node basin geometry supplies a basis
per context, structurally.

The dissolution completes the framework's measurement-side
program. Together with collapse dissolution and the Born-rule
derivation, the framework's QM apparatus is now articulated at the
structural level with no remaining basis-selection axiom.

Class: foundational consolidation (Class 3, articulation). The arc
closed is the unstated reliance on a "preferred basis" outside the
saddle-node basin geometry the framework already has installed.

---

## Cross-links

- `lesson_forced_basin_selection.md` — the Tier-B engine-room lesson;
  the apparatus this dissolution rests on (measurement = basin
  selection; basin = saddle-node).
- `collapse_dissolution.md` (PR #177) — companion dissolution; the
  measurement-problem-side, while this doc handles the basis-
  selection-side. Both reference the same substrate apparatus
  (unitary substrate + fidelity bound + basin selection).
- `figure_eight.md` — Born rule from `J² = −I`; the statistic.
- `born_rule.md` — basin measure as Born rule.
- `substrate_determinism.md` — inviolables #1 (Q-mod-2), #3
  (unitarity), #5 (Born exponent). The substrate's foundational
  apparatus.
- `gr_qm_unification_synthesis.md` (PR #181) — the capstone synthesis
  named this as one of two open items remaining; this doc closes
  one of them.
- `salpeter_gate_disposition.md` — companion disposition of the
  *other* open item from the capstone synthesis (cascade↔Salpeter
  dual gate).
- `fidelity_bound.md` — the uncertainty relation `τΔθ = const`
  reading as basin-geometry consistency.
- `equivalence_dissolution.md` (PR #176) — companion structural
  dissolution at the same articulation level; "the principle is a
  near-tautology" shape.
- `a1_from_saddle_node.md` — the saddle-node derivation of the Born
  rule's exponent (cited as load-bearing).
- `epr_bell_assembly_theorem.md` — uses the substrate's basis-
  selection mechanism in the EPR/Bell construction; this dissolution
  clarifies what "basis" means in that theorem.

---

## One-line summary

The QM preferred-basis problem dissolves into basin selection: the
saddle-node geometry at each measurement context supplies its own
basis (the basin's natural coordinates), the substrate's phase
variable is invariant, and no separate "preferred basis" axiom is
required — completing the framework's measurement-side dissolution
program alongside collapse dissolution (`collapse_dissolution.md`)
and the structurally-forced Born statistic (`figure_eight.md`).
