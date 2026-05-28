# Collapse dissolution

## Status

**Inviolable-companion dissolution articulated** — apparent
wavefunction collapse (the non-unitary projection step of textbook
QM) reduces to fidelity-bounded self-measurement on the framework's
substrate. The measurement problem — the apparent contradiction
between unitary Schrödinger evolution and non-unitary projection —
dissolves structurally: there is no projection postulate to
reconcile, because the substrate carries no such postulate.

Not a new derivation; a synthesis of ingredients already in the
corpus. The substrate is unitary (#3, bicone Z₂ rigidity); the
fidelity bound (`fidelity_bound.md` §"Instance 2: Wavefunction
collapse") supplies the apparent-collapse mechanism as the system
identifying its attractor under bounded frequency resolution; the
Born rule `= |ψ|²` is already structurally forced (`figure_eight.md`,
via `J² = −I`).

No new primitive.

This doc is the QM-side companion to `equivalence_dissolution.md`'s
GR-side pillar of the Tier-C GR-QM unification capstone
(`lesson_epr_gr_qm_unification.md` §"The measurement problem,
geometrized", L39).

---

## The statement

**Claim (collapse dissolution).** On the framework's substrate the
apparent wavefunction collapse is not a non-unitary postulate but a
near-tautology: the substrate dynamics are unitary, the system
measures its attractor membership using its own oscillation as the
reference, and the fidelity of that self-measurement is bounded by
the Fourier resolution `Δω · T_obs ≥ 1`. The appearance of collapse
*is* the system identifying its attractor under the bound — the
dynamics never leave the unitary substrate.

The dissolution is structural, not interpretive: it removes the
*non-unitary projection postulate* from the framework's import ledger
and lands the appearance of collapse on a derived mechanism. The
*specific* collapse magnitudes (amplitudes, exact timescales in
physical units) remain anchor-declined per the Basepoint Principle.

---

## Derivation

### Step 1 — The substrate is unitary

Inviolable #3 (`substrate_determinism.md` L174–176):

> **Unitarity / information conservation.** Bicone Z₂ rigidity
> (`wave_particle_substrate.md`). No topology-changing process; no
> information loss.

The substrate carries no non-unitary mechanism by which a state
could "collapse." Whatever appearance of collapse a measurement
produces, the underlying substrate evolution preserves the
bicone's Z₂-rigid information content.

### Step 2 — Self-measurement is bounded by frequency resolution

`fidelity_bound.md` §"The frequency resolution bound": any
oscillator measuring `Δω` against a reference at `ω_ref` requires
observation time `T_obs ≥ 1/Δω`. The maximum observation time is
set by the reference itself (`T_max ~ 1/ω_ref`), so the minimum
resolvable frequency difference is `Δω_min ~ ω_ref`. *When the
system is its own reference* (self-measurement), this bound is
constitutive, not imposed.

The fidelity bound applies wherever a substrate mode tries to
identify which tongue (attractor) it lives in by accumulating
cycles against a clock that the mode itself participates in
constituting.

### Step 3 — The appearance of collapse is attractor identification under the bound

`fidelity_bound.md` §"Instance 2: Wavefunction collapse" already
does this work: the collapse duration `τ ~ 1/√ε` emerges from the
Floquet damping of the self-consistency equation
`g_obs = g_bar + α · g_obs` (where `α = exp(−√(g_bar/a₀))` is the
gravitational instance's damping factor; the same structure holds
for the QM instance with `ε` the tongue depth). The
`τ × Δθ = const` uncertainty is the Fourier identity. The Zeno
effect is interrupted measurement: continuous re-initialization of
the measurement prevents the system from accumulating enough cycles
to identify its tongue.

What standard QM calls "collapse" is the system identifying which
tongue it is in — a process that proceeds via the substrate's
ordinary (unitary) dynamics under the fidelity bound. No projection
postulate is invoked. The dynamics never leave step 1's unitary
substrate.

### Step 4 — The Born rule is already structurally forced

`figure_eight.md` derives the Born exponent `= 2` from `J² = −I`,
the twist operator on the figure-8 topology. The probabilities
reported in the apparent-collapse statistics take the form
`|⟨φ | ψ⟩|²` because that is structurally forced — independent of
any non-unitary mechanism. The Born rule is *consistent with* step
1's unitary substrate; it does not require the substrate to fail
in order to obtain.

### Combined

Steps 1–4 close the gap. The substrate is unitary; the fidelity
bound supplies the apparent-collapse mechanism; the Born rule is
the structurally forced statistic. There is no non-unitary
projection step to reconcile with unitary Schrödinger evolution —
because there is no projection step on this substrate at all. The
measurement problem dissolves into a fidelity-bounded
self-measurement instance of unitary dynamics.

---

## What this says (and what it does not)

It **says**:

- The measurement problem dissolves structurally: no postulated
  non-unitary collapse mechanism exists on this substrate; what
  looks like collapse is fidelity-bounded self-measurement.
- The collapse-duration form (`τ ~ 1/√ε`), the uncertainty relation
  (`τΔθ = const`), the Zeno effect, and the Born exponent (`= 2`)
  are *all* consequences of already-installed apparatus.
- No interpretational debate (Copenhagen vs many-worlds vs Bohm)
  needs adjudicating to make the framework internally consistent.
  The framework is structurally unitary-only; the appearance of
  collapse is the system's self-measurement, not an ontological
  event.

It does **not** say:

- That this resolves the preferred-basis problem. Why is position
  (rather than momentum, or some other observable) the typical
  observable a measurement settles into? The framework's substrate
  has phase as the primary variable; basis-selection questions
  reduce to "what is the basis of the substrate's encoding" —
  open work, not closed by this doc.
- That this predicts specific collapse times or amplitudes in
  absolute units. The framework supplies the *form*
  (`τ ~ 1/√ε`; Born exponent `= 2`); the *magnitude* in physical
  units rides on anchors (`H₀` for the MOND-side instance, the
  environmental coupling frequency `ω_env` for the QM-side
  instance), per the Basepoint Principle. The calibration in
  `fidelity_bound.md` §"Status — Resolved" makes the dimensionful
  fit; that calibration is anchor-conditional, not derived from
  primitives alone.
- That this is a full interpretation of quantum mechanics. It is
  a structural dissolution of one specific puzzle (the non-unitary
  projection postulate's coexistence with unitary evolution). It
  declines to take positions on, e.g., the ontological status of
  branches in many-worlds, the existence of consciousness as a
  measurement participant, or the Wigner's-friend scenario at
  arbitrary nesting depth.
- That all QM phenomena reduce to this mechanism. Much of QM
  lives entirely in step 1's unitary substrate without invoking
  step 2's fidelity bound at all (free evolution; standard
  Hamiltonian dynamics). Step 2 is the apparatus that engages
  when self-measurement is the question.

This is the same discipline applied to equivalence
(`equivalence_dissolution.md`): derive *form* of the relevant
principle from substrate, decline *magnitude* of the system the
principle applies to.

---

## Distinct from interpretational positions

The framework's stance here is structural, not interpretive. To
make this concrete:

- **Copenhagen** requires a non-unitary projection postulate as an
  axiom alongside unitary evolution. The framework rejects this:
  step 1 says the substrate is unitary; step 3 gives the
  appearance of collapse a derived mechanism, eliminating the need
  for a projection axiom.
- **Many-worlds** requires unitarity-only + universal Schrödinger
  + a measure problem on branches. The framework's stance is
  structurally compatible with universal unitarity (step 1) but
  does *not* need the branching ontology: the appearance of
  collapse is fidelity-bounded self-measurement on a *single*
  substrate, not a branching of worlds.
- **Bohmian / hidden variables** require either non-local
  (Bohmian) or super-deterministic structure. The framework's
  apparent non-locality is *topological* (Klein-bottle Z₂,
  inviolable #1; see `q_mod2_conservation_theorem.md`); Bell's
  theorem in its standard form does not apply, because the
  substrate is non-orientable (see `epr_bell_assembly_theorem.md`).
  No hidden variables are introduced.

The framework's position: there is no measurement problem on this
substrate because there is no non-unitary postulate to reconcile,
and the appearance of collapse has a derived mechanism.

---

## Exhibited consequences

- **Born rule operational meaning.** The Born exponent `= 2` is
  already structurally forced (`figure_eight.md`); this doc tells
  you that the statistic obtains operationally because
  fidelity-bounded self-measurement on a unitary substrate yields
  the `|⟨φ | ψ⟩|²` reporting structure.
- **Uncertainty relation `τΔθ = const`.** Fourier identity on the
  substrate; structural, not postulated.
  (`fidelity_bound.md` §"The uncertainty relation".)
- **Quantum Zeno effect.** Interrupted self-measurement; the
  system never accumulates enough cycles to identify its tongue.
  (`fidelity_bound.md` §"The Zeno effect".)
- **Collapse duration `τ ~ 1/√ε`.** Floquet damping of the
  self-consistency equation. (`fidelity_bound.md` "Resolved"
  items.)
- **The MOND-side analog.** The RAR interpolating function
  `g_obs = g_bar / [1 − exp(−√(g_bar/a₀))]` is the *same*
  fidelity-bound mechanism in the gravitational instance, not a
  separate phenomenon. (`fidelity_bound.md` §"Instance 1: The
  MOND transition".) The two instances *are* the same structure,
  per the explicit unifying table at `fidelity_bound.md` L149.
- **One pillar of the Tier-C GR-QM unification capstone.** With
  `equivalence_dissolution.md` (GR pillar) and this doc (QM
  pillar) both consolidated, `lesson_epr_gr_qm_unification.md`
  becomes writable as the synthesis it was always meant to be.

---

## Falsifiers

- **Demonstrable non-unitary residual in a perfectly isolated
  system.** If a closed system can be shown to undergo non-unitary
  evolution at sufficient sensitivity — no environmental
  decoherence, no measurement — step 1's unitary-substrate claim
  is voided and this dissolution fails. Current bounds (cavity
  QED, trapped ions, superconducting qubit Ramsey fringes) find
  no such residual; consistent with this doc.
- **`τ × Δω` not constant at fixed substrate parameters.** A
  controlled experiment (cavity QED, trapped ions) measuring the
  product across systems with varying `Δω` would test the
  Fourier-identity prediction. A measured deviation would void
  step 2.
- **Collapse duration not scaling as `1/√ε`.** The Floquet damping
  in step 3 is geometric. Observed collapse-duration scaling that
  deviates from `1/√ε` across systems — at fixed coupling — would
  void step 3.
- **Composition-dependent collapse statistics.** If the apparent
  collapse statistics depend on the *composition* of the measured
  body (rather than only on the substrate's tongue structure),
  then the "attractor identification" framing fails and a
  composition-sensitive mechanism is required. The framework
  predicts the statistics depend only on the tongue structure
  (which is universal across compositions on the same substrate).
- **A demonstrable preferred-basis selector outside the
  framework's substrate.** A successful derivation, in a
  competing framework, of *which* observable is measured (the
  preferred-basis problem) that requires postulating dynamics
  outside this substrate's apparatus would *not* falsify the
  dissolution per se, but would mark a place where the framework
  must extend rather than reduce.

---

## Distinct from the magnitude / mechanism distinction

The framework dissolves the *non-unitary postulate*, not the
*magnitude* of measurement-induced effects. Specific collapse
times in seconds, specific amplitudes, the exact coupling
constants of environmental decoherence — all remain
anchor-declined. This doc consolidates the structural piece (no
projection postulate needed); the magnitude piece is and remains
out of class.

In the corpus's existing taxonomy this is the same status as the
Born exponent: the exponent `= 2` is forced; the absolute
amplitudes of wavefunctions are not. Here the structural absence
of a non-unitary postulate is forced; the absolute collapse
timescales in physical units are not.

---

## Why this matters

The measurement problem had been sitting unmarked on the import
ledger — the framework consumed unitarity (#3) and the Born rule
(`figure_eight.md`) without explicitly addressing the apparent
contradiction with the projection postulate of standard QM. This
doc closes that gap: there is no contradiction, because the
framework's substrate carries no projection postulate. The
appearance of collapse is the structural signature of
fidelity-bounded self-measurement on a unitary substrate.

The dissolution is also one of the two pillars of the Tier-C
GR-QM unification capstone (`lesson_epr_gr_qm_unification.md`
§"The measurement problem, geometrized", L39). The equivalence
dissolution (`equivalence_dissolution.md`) put the GR side in the
derived column; this puts the QM side in. With both pillars
consolidated, the capstone becomes writable as the synthesis it
was always meant to be.

Class: foundational consolidation (Class 3, articulation). The
arc closed is the unstated reliance on a non-unitary projection
step that the framework's apparatus never actually needed.

---

## Cross-links

- `substrate_determinism.md` — the 10 inviolables; this
  dissolution rests on #3 (unitarity / bicone Z₂ rigidity) and is
  consistent with #2 (no-rescaling, the magnitude side stays
  anchor-declined).
- `wave_particle_substrate.md` — bicone Z₂ rigidity itself; the
  substrate of #3.
- `fidelity_bound.md` — the apparatus for steps 2–3; the
  apparent-collapse mechanism, the unifying table at L149, the
  collapse-duration calibration (`τ × C/√(g_bar/a₀)` form), and
  the MOND-side analog.
- `figure_eight.md` — the Born rule from `J² = −I`; step 4's
  source.
- `equivalence_dissolution.md` — companion dissolution doc; the
  GR pillar of the Tier-C capstone.
- `q_mod2_conservation_theorem.md` — companion
  inviolable-articulation doc; same house style.
- `lesson_epr_gr_qm_unification.md` — Tier-C capstone; this doc
  supplies the QM-side pillar referenced at L39.
- `epr_bell_assembly_theorem.md` — EPR/Bell-side structural
  articulation; companion to this dissolution at the foundational
  layer.
- `no_rescaling.md` — inviolable #2; collapse magnitudes remain
  anchor-declined.
- `basin_11_connection_exploration.md` — the dominant 1/1
  attractor's neighborhood; the "which tongue is the system in?"
  question lives here for the deepest substrate basin.

---

## One-line summary

The substrate is unitary (`#3`); apparent wavefunction collapse is
the system identifying its attractor under the fidelity bound
(`fidelity_bound.md`); the Born rule `= |ψ|²` is already
structurally forced (`figure_eight.md`); therefore the measurement
problem dissolves into fidelity-bounded self-measurement on a
unitary substrate, requiring no non-unitary postulate.
