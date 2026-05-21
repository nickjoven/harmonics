# Articulation audit — 2026-05 round

## What this file is

Findings from a four-axis articulation audit conducted in the
session following the inviolable-#1-theorem and √r_n-correction
articulations (PRs #147, #148). The audit asks: of the framework's
content that is *correct but not articulated as a unified
table/theorem/reading*, what would benefit from precise
articulation in the house style of `q_mod2_conservation_theorem.md`
/ `photon_reframing.md` / `higgs_reframing.md` / `mass_function_family.md`?

The audit also re-checks every major *honest decline* against
structural input since approximately 2026-04, asking whether the
discriminator has shifted (Basepoint feature → still-feature, or
shifted to articulation-candidate). Verdict: **zero declines
shifted; all reconfirmed or elevated**. The discipline is locked,
which is itself a finding.

This file is inventory-only. It identifies what to articulate; it
does not draft the articulations. Each finding lists existing
material, articulation difficulty, and discipline-edge risk so the
selection step is honest.

## Audit scope

Four parallel surveys:

- **Axis A (particle ontologies)**: which Standard-Model particles
  have explicit framework-native ontology articulations vs scattered
  content vs correctly declined.
- **Axis B (twin-pair structures)**: which "two-of-a-kind" framework
  structures have unified comparison tables vs scattered content.
- **Axis C (inviolable theorems)**: of the 10 inviolables in
  `substrate_determinism.md`, which have standalone theorems
  (only #1 currently; via `q_mod2_conservation_theorem.md`) and
  which would benefit from articulation.
- **Axis D (honest-decline re-check)**: for the framework's major
  honest declines, has structural input since 2026-04 shifted the
  discriminator?

## Findings summary

| Axis | Articulation candidates (P1/P2) | Decline-confirmed | Already-articulated |
|---|---|---|---|
| A — particles | W/Z (P1), gluons (P2, with bright line), electron (P3) | graviton OI, baryon OI, flavor assignments | photon (PR closed, see below), Higgs, quarks, neutrinos |
| B — twin pairs | K=1 vs K<1 continuum limits (P1), H_0 vs v_EW anchors (P1), 4 bright-line patterns (P2), 2 Z₂'s expanded (P2), Z_6/Z_2/Z_3 factor composition (P3) | — | mediant/EML primitives, mass-mechanism family |
| C — inviolables | #2 no-rescaling (P1), #7 half-twist = π (P1), #5 Born rule = \|ψ\|² (P2) | #3, #4, #6, #8, #9, #10 (various reasons; see Axis C) | #1 Q mod 2 conservation (PR #147) |
| D — declines | — | **all 7 reconfirmed or elevated** | — |

P1 = high-value, ready (existing pieces + low difficulty + zero risk)
P2 = high-value, needs one formalization step or has a bright-line caveat
P3 = lower priority or marginal value

## P1 — Ready articulations (existing pieces + low difficulty + zero risk)

### P1.1 — Two continuum limits comparison table (K=1 Einstein vs K<1 Schrödinger)

**Issue**: `continuum_limits.md` is structured as "Part I" + "Part II"
with separate headings; no side-by-side comparison table. The non-
smooth separation at K=1 (forced by `continuity_in_K_nulls.md` N11
and the K=1 ↔ K<1 sector-decoupling re-audit) is implicit in the
two-part structure but never explicit as a reference.

**Material exists**: `continuum_limits.md` Parts I/II; `PROOF_A_gravity.md`;
`PROOF_B_quantum.md`; `continuity_in_K_nulls.md` N11; `framework_status.md`
Survives row "K=1 ↔ K<1 sector decoupling".

**Articulation difficulty**: easy — assemble columns ("Regime |
Condition | Continuum equation | Primary object | Required anchor |
Observable sector | Class") from existing material.

**Discipline-edge risk**: zero. Decoupling is Class-3 rigorous
(`path_closures_iter3.md` D.3).

**Impact**: closes a known reader-friction point. The non-smooth
separation is the framework's deepest dynamical claim; the side-by-
side reading would make it citable.

### P1.2 — Two dimensional anchors comparison (H_0 cosmological vs v_EW particle)

**Issue**: H_0 and v_EW are documented separately
(`anchor_count_reaudit.md` L36-76 has the five-obstruction table;
`basepoint_principle.md` L62-95 articulates the canonical instance;
`hierarchy_problem_translation.md` covers the hierarchy framing).
None of these places carries a single unified table: "K=1 sector
forces H_0 | K<1 sector forces v_EW | Distinguishing structural
fact | Combined: two-anchor minimality."

**Material exists**: `anchor_count_reaudit.md`, `basepoint_principle.md`,
`continuum_limits.md` Parts I/II, `path_closures_iter3.md` D.3,
`MANIFEST.yml` `dimensionful_inputs` block.

**Articulation difficulty**: easy — extract and unify into one
table; nothing new.

**Discipline-edge risk**: zero. Decoupling is Class-3 rigorous.

**Impact**: makes the canonical Basepoint instance citable in one
place; tightens the Survives entry for two-anchor minimality.

### P1.3 — Inviolable #2: no-rescaling identity, standalone theorem

**Issue**: `no_rescaling.md` (L21-85) articulates the principle
fully — statement, examples table, three-layer justification, practical
consequence — but is **not packaged as a formal theorem** (statement,
proof, falsifiers) in the style of `q_mod2_conservation_theorem.md`.

**Material exists**: `no_rescaling.md` (the principle is essentially
complete in prose form).

**Articulation difficulty**: easy — repackage as theorem-proof-
falsifiers, formalize "identity under Planck units" as a precise
statement, extract falsifiers from the existing three-layer
argument.

**Discipline-edge risk**: zero. The principle is committed; no
Class-3 forced items block it.

**Impact**: makes the principle citable as a theorem, parallel to
inviolable #1.

### P1.4 — Inviolable #7: half-twist phase = π, standalone theorem

**Issue**: The topological argument for the AB-phase = π is
distributed across `cone_twist_substrate.md` L85-100 (the θ-term
with prefactor π/2) and `orthogonal_kink_interaction.md` L52-76
(crossing-detail-independent topological invariance). No single
doc states it as a theorem with falsifiers.

**Material exists**: `cone_twist_substrate.md` §5.2,
`orthogonal_kink_interaction.md` §"Conservation laws."

**Articulation difficulty**: easy — state Z₂-generator argument
formally, list falsifiers (e.g., "phase = π/2 or 2π would falsify
Z₂ coverage").

**Discipline-edge risk**: zero. Topologically forced.

**Impact**: consolidates the AB-phase prediction's defense against
crossing-geometry objections.

### P1.5 — Particle ontology: W/Z bosons reframing

**Issue**: The Higgs reframing (`higgs_reframing.md`) treats W/Z as
locked modes at the q=2 tongue boundary; mass predictions m_W, m_Z
via tongue-width duty cycles; sin²θ_W via Fibonacci corrections (the
bare K=1 identity 8/35 sits in `MANIFEST.yml` `bare_k1_identities`).
But no standalone reframing doc with a unified property table.

**Material exists**: `higgs_reframing.md`, `higgs_from_tongue_boundary.md`,
`duty_cycle_dictionary.md`, `MANIFEST.yml` `bare_k1_identities`,
`framework_status.md` "Floor (numerology cloud)" entries for α_s/α_2
and m_H/v.

**Articulation difficulty**: easy — assemble the seven-fold table
(mass / coupling / width / Weinberg-angle role / EW symmetry-breaking
mechanism / generation-universality / decay structure) from existing
content.

**Discipline-edge risk**: zero on the masses/couplings/symmetry roles
(all derive). The observable-identification (which specific 4-mode
configuration carries the W vs Z quantum numbers) is **honestly
declined** as Class-2 per `proposed_residual_closure.md` §C; the
articulation must explicitly flag this boundary.

**Impact**: highest-value particle articulation. Brings the W/Z
into the same articulation tier as the photon and Higgs.

## P2 — Should-articulate (one formalization step or a bright-line caveat)

### P2.1 — Four bright-line patterns comparison table

**Issue**: Basepoint Principle, no-rescaling, two-anchor minimality,
and anchor-side amplification (Instance 7) each have their own doc
(`basepoint_principle.md`, `no_rescaling.md`, `anchor_count_reaudit.md`,
`vocabulary_is_the_work_pattern.md` Instance 7). The claim that all
four instantiate "structurally-forced decline" is stated in prose
but never tabulated as "Pattern | Declined item | Forcing
(inviolable/torsor/obstruction) | Status."

**Material exists**: All four parent docs.

**Articulation difficulty**: easy synthesis, but `no_rescaling.md`
should be confirmed-readable first (Axis B agent flagged this).

**Discipline-edge risk**: low-medium. The Basepoint Principle is
Class-3 (`basepoint_principle.md` L112); A_s/Instance 7 ACCEPTED.
The table is synthesis, not new derivation.

**Impact**: makes the meta-pattern citable. The framework's
broadest cross-cutting structural insight gets a single home.

### P2.2 — Two Z₂'s comparison table, expanded

**Issue**: `sine_gordon_substrate.md` L214-221 has a brief two-row
table (Z₂ structure | Action | Consequence). It is correct but
buried. Expanding to include "when each applies | where each appears
in the framework | which observables depend on which" would help
readers avoid conflating the coordinate-antiperiodicity Z₂ with the
field-half-twist Z₂.

**Material exists**: `klein_bottle.md`, `sine_gordon_substrate.md`,
`q_mod2_conservation_theorem.md` (the standalone for the coordinate
Z₂), `framework_lagrangian.py` Part 6, `cone_twist_substrate.md`.

**Articulation difficulty**: easy — expand the existing table.

**Discipline-edge risk**: zero. Both are inviolables.

**Impact**: prevents the framework's most common local reading
error. Particularly useful for readers studying the AB-phase or the
soliton-sector content.

### P2.3 — Particle ontology: gluons reframing (with explicit bright line)

**Issue**: Gluons are mentioned across `gauge_dictionary.md`,
`gauge_factorization.md`, `cosmological_cycle.md` L218, and
`beta_from_tongues.md` (β-function K-running). The 8 gluon
generators match the 8 cross-sector edges in the Klein 4-mode graph;
SU(3) color from Z_3; running from tongue-width K-dependence;
masslessness from tongue-boundary. A seven-fold property table is
writable.

**Material exists**: `gauge_dictionary.md`, `gauge_factorization.md`,
`beta_from_tongues.md`, `cosmological_cycle.md` L218 (the inline
"channels between q=3 modes" remark).

**Articulation difficulty**: medium — content is more scattered
than W/Z; one or two cross-doc identifications need consolidating.

**Discipline-edge risk**: medium. The gauge structure forces; the
observable-identification (which mode-transition is *observed as*
the gluon) is **honestly declined** as Class-2. The articulation
must explicitly list the bright line, parallel to W/Z.

**Impact**: completes the SU(3) ontology in the same form as the
SU(2)×U(1) content. Without this, the framework's gauge dictionary
remains lopsided.

### P2.4 — Inviolable #5: Born rule = |ψ|² standalone theorem

**Issue**: `born_rule.md` and `figure_eight.md` L80-94 derive `J² = −I`
from the figure-eight crossing geometry, and `born_rule_parameter_free.md`
(referenced in `proposed_residual_closure.md`) provides the parameter-
free version. The pieces support the inviolable; no standalone
statement-and-proof exists.

**Material exists**: `figure_eight.md`, `born_rule.md`,
`born_rule_parameter_free.md`, `wave_particle_substrate.md` L108-142.

**Articulation difficulty**: medium — one missing step: the precise
map from `J²` topology to Born measure. The mechanism is present;
the formal proof would tighten the existing arguments.

**Discipline-edge risk**: low. The Born rule is derived (not
primitive); the framework has committed to its correctness.

**Impact**: closes a long-standing question ("where does the Born
rule come from?") with a topological answer in standalone form.
Parallels inviolable #1's standalone form.

## P3 — Lower priority / marginal value

### P3.1 — Z_6 / Z_2 / Z_3 gauge-factor composition table

**Issue**: `phenomenology_cross_reference.md` L36 names the
composition (Z_6 substrate + Klein-antipodal Z_2 + color Z_3 →
SU(3)×SU(2)×U(1)). Detailed gauge dictionary in `gauge_dictionary.md`
and `gauge_factorization.md`. A single table showing the explicit
factor-by-factor composition does not exist.

**Difficulty**: medium synthesis — needs careful cross-doc
identification.

**Risk**: medium. `gauge_factorization.md` would need to be checked
first; the explicit composition may already be there in a form I
haven't surfaced.

**Impact**: useful but not blocking; the gauge dictionary already
carries the content in prose.

### P3.2 — Electron / charged-lepton reframing

**Issue**: Lepton masses enter via `a1_from_saddle_node.md`; ratios
via cascade scaling; charge from Klein-antipodal Z_2 rep; generation
mechanism elsewhere. A unified property table is writable.

**Difficulty**: medium-low.

**Risk**: low. Charge, mass-mechanism, and SU(2)_L doublet structure
derive; flavor identification (electron vs μ vs τ as specific
substrate states) is honestly declined.

**Impact**: parallels Higgs/photon/W-Z/gluon ontology suite. Lower
priority because lepton masses are already in numerics-form
(`numerology_inventory.md`, `phenomenology_cross_reference.md` L442:
"Some Class 5 (factors 6, 9), most Class 2").

### P3.3 — Two Klein π₁ sectors expanded

**Issue**: `framework_status.md` Survives row mentions
"Klein π₁ sector assignment: cosmological → no-twist; particle →
twist." `path_closures_iter4.md` is cited for the forcing. A side-
by-side detail is not surfaced.

**Difficulty**: low (if `path_closures_iter4.md` has the detail
ready) or medium (if needs synthesis).

**Risk**: low.

**Impact**: marginal; the assignment is briefly stated in the
Survives row and rarely the friction point.

## Honest-decline lock (Axis D)

The framework's seven major honest declines were re-checked against
structural input since approximately 2026-04. **None shifted.** All
are either reconfirmed at higher confidence or *elevated* to
foundational-principle level. The discipline is locked. For the
record:

| Decline | Status under re-check |
|---|---|
| Observable-identification per K-zoo sector | Reconfirmed; Basepoint feature. No structural mode-partition discriminator exists in the corpus. |
| v / M_P ≈ 13⁻¹⁵ gap | Promoted to structural feature (prime-5 absence verified). |
| 1-3% particle-sector numerology cloud | Reconfirmed pigeonhole at α=0.05 across thresholds (`numerology_count_phase_b.md`). |
| Inflation duration / H_inflation | Formally justified under Basepoint Principle (`inflation_seam_anchor_closure.md` + `basepoint_principle.md`). |
| R1 / "continuum requires discrete" | Elevated: ∅-entailment now first-class principle via Basepoint. |
| K_c finite-n Fibonacci closed form | Reconfirmed out-of-scope (external KAM math, not a framework gap). |
| `r_n` value at K_n < 1 | Reconfirmed Class-2; three candidate routes catalogued, none executable absent a mode-partition forcing argument. |

**Finding**: the framework's discriminator (Basepoint Principle
forcing vs operational gap) is multiply-verified and stable. Future
articulation work should respect these as locked, not as candidates.

## Particle ontology bright lines (do NOT articulate)

The articulation audit explicitly identifies the following as
**honest declines** that articulation work should not cross:

- **Baryon observable-identification** (proton vs neutron;
  specific quark substructure). Framework derives that baryons are
  kink composites and their mass spectrum; identification is
  Class-2 declined. See `framework_status.md` L40,
  `proposed_residual_closure.md` §C.
- **Flavor assignments** (electron vs μ vs τ; u vs d vs c vs s vs
  t vs b; ν_e vs ν_μ vs ν_τ). Framework derives generation count
  and mass ratios; flavor identification is Class-2 declined.
- **Graviton observable-identification**. The Einstein-equation
  derivation (`einstein_from_kuramoto.md`) is structural; the
  graviton-as-substrate-mode identification is declined.
- **Gluon observable-identification**. SU(3) and β-function derive;
  which mode-transition is *observed as* the gluon is declined.

Any P1/P2/P3 articulation that touches these must list the bright
line explicitly — the W/Z reframing (P1.5) and gluon reframing
(P2.3) both flag this in their entries above.

## Out-of-scope items

The audit found no shifted declines and identified the following
classes as *not* candidates for this round:

- **PR #145 (photon-as-Ø-mode reframing)**: closed without merging;
  not re-opened by this audit. The seven-fold table format is
  borrowed from that PR's draft for the W/Z and gluon entries
  above. If the photon-reframing decision is revisited, it would
  follow the same P1 pattern.
- **Existing inviolable theorems #3, #4, #6, #8, #9, #10**: each
  has reasons against standalone articulation in this round (Axis
  C agent report): #3 entangled with derived Z₂ structure; #4
  defensive (reduction-audit closure); #6 already load-bearing as
  separate theorems; #8/#9/#10 require formalization of
  foundational concepts (expressibility closure, repair events,
  Planck floor) not yet mature.
- **Already-articulated**: the Higgs, photon (closed PR), quarks,
  neutrinos, mediant/EML primitives, mass-mechanism family. Listed
  in the findings summary but not re-articulated.

## Recommended remediation sequence

Five P1 items + four P2 items + three P3 items. Recommended
execution order:

1. **P1.1** (continuum limits table) — single new doc, ~80 lines,
   no risk.
2. **P1.2** (two anchors table) — single new doc, ~70 lines, no
   risk.
3. **P1.3** (no-rescaling theorem) — repackage `no_rescaling.md`
   content into a `no_rescaling_theorem.md` matching
   `q_mod2_conservation_theorem.md`'s structure, ~150 lines.
4. **P1.4** (half-twist = π theorem) — new `half_twist_phase_theorem.md`,
   ~150 lines.
5. **P1.5** (W/Z reframing) — new `wz_reframing.md` with seven-fold
   table + observable-identification bright line, ~180 lines.
6. **P2.1** (four bright-line patterns table) — verify
   `no_rescaling.md` content first, then a synthesis doc, ~100 lines.
7. **P2.2** (two Z₂'s expanded table) — small expansion of existing
   table in `sine_gordon_substrate.md` or a new short reference doc.
8. **P2.3** (gluons reframing) — new `gluon_reframing.md` with
   bright line, ~180 lines.
9. **P2.4** (Born rule theorem) — new `born_rule_theorem.md`,
   ~170 lines.
10. **P3.1-P3.3** — defer to a follow-up round.

P1.1-P1.5 alone is roughly five new docs totalling ~600-700 lines,
each landing within a session. The set is independent (no shared
dependencies that would force sequential ordering), so they could be
landed in any order or in parallel via subagents with synthesis on
this end.

## Cross-references

- `audit_punch_list_2026-04.md` — prior audit (cross-reference /
  numerical / status-tag axes); this round's parallel.
- `framework_status.md` — Survives / Floor / Fails / Eliminated /
  Proposed catalog; this audit identifies what could be added to
  Survives via articulation.
- `thread_chronology.md` — resolved-thread ledger; the articulations
  in P1-P2 would each warrant a new row.
- `numerology_inventory.md` — Class 1-5 inventory; Axis D leans on
  it heavily.
- `basepoint_principle.md` — the Class-3 principle on which the
  decline-discipline rests; Axis D's lock validates it.

## Status

Audit complete. Findings: 5 × P1, 4 × P2, 3 × P3 articulation
candidates; 7 declines reconfirmed or elevated (none shifted); 4
particle-ontology bright lines explicitly listed as do-not-cross.

The framework's articulation surface is larger than the audit
expected, and its decline-discipline is tighter than the audit
expected. Both are healthy signs.

Recommended next step: execute P1.1 + P1.2 (the two side-by-side
tables) as a single PR — they are the highest-value lowest-lift
items and exercise no new physics. P1.3-P1.5 follow in sequence.
P2 items can be parallelized once P1 lands.
