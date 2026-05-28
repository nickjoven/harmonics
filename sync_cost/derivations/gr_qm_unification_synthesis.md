# GR–QM unification — Tier-C capstone synthesis

## Status

**Tier-C capstone synthesis articulated.** The framework's grandest
claim — that general relativity and quantum mechanics are not two
theories to be glued together but **two continuum limits of one
discrete substrate, taken at two couplings** — now has its structural
form complete at the load-bearing claim level. The pedagogical lesson
`lesson_epr_gr_qm_unification.md` carries the teaching narrative; this
doc carries the structural composition: the apparatus now in place,
how the pieces compose, and what remains.

The synthesis became writable when its three pillars landed:

- **GR pillar** — equivalence dissolution (`equivalence_dissolution.md`,
  PR #176): one mass parameter per substrate-Lagrangian mode, used as
  both inertia and sync-cost coupling; weak equivalence is the LHS/RHS
  identity of the EOM; strong equivalence inherits from the
  `(3, 1)`-signature derivation.
- **QM pillar** — collapse dissolution (`collapse_dissolution.md`,
  PR #177): apparent wavefunction collapse is fidelity-bounded
  self-measurement on the unitary substrate of inviolable #3, with the
  Born rule already structurally forced (`figure_eight.md`, `J² = −I`).
- **Locality pillar** — EPR/Bell assembly theorem
  (`epr_bell_assembly_theorem.md`, #152): Born rule +
  `q_mod2_conservation_theorem.md` + Klein-bottle topological
  non-locality compose to non-signaling Bell-violating joint statistics
  matching QM at the Tsirelson bound. Bell's no-go doesn't apply
  because the framework is not a local hidden-variable theory — the
  conserved `Q_{AB} mod 2` is a global topological invariant, not a
  shared `λ`.
- **Dynamical bridge** — K(t) cadence closure
  (`k_of_t_residual_disposition.md`, PR #179): the era-timeline
  Tier-3 residual is structurally closed; cadence forced to
  `2/(q₃·19_Λ)`; `N_efolds ≈ 63.7` testable on the CMB-S4 / LiteBIRD
  horizon.

No new primitive. The synthesis is structural composition of
already-installed apparatus; the contribution is naming the composition,
not adding to it.

---

## The statement

**Claim (GR-QM unification, structural form).** On the framework's
substrate (rhythm-locking on a Klein bottle, `Z₂`-graded), GR and QM
are the *same* discrete dynamics taken at *two* coupling settings:

| Limit | Coupling | Macroscopic theory | Source |
|---|---|---|---|
| All rhythms locked | `K = 1` | **Einstein field equations** + Friedmann | `einstein_from_kuramoto.md` (D13, Lovelock uniqueness), `k_of_t_friedmann.md` (S1–S2) |
| Partially unlocked | `K < 1` | **Schrödinger equation** (Madelung variables) | `continuum_limits.md` Part II (D12) |

The unification is **not** "quantize gravity" nor "geometrize QM."
It is: *both are macroscopic faces of one discrete rhythm-substrate, at
two settings of one dial.* The K = 1 ↔ K < 1 transition is
**structurally non-smooth** — a Class-5 feature, not a gap — and it
forces two-anchor minimality (cosmological + particle), consistent
with the Basepoint Principle.

The substrate's `Z₂`-graded topology (inviolable #1) makes nonlocality
**topological** rather than signal-carrying: EPR correlations are
real, Bell is violated, but the conserved global invariant is
`Q mod 2`, not a hidden variable — so nonlocal-and-no-signaling
coexist by construction (`epr_bell_assembly_theorem.md`).

Measurement is **self-referential**: the system identifying which
attractor it belongs to under the fidelity bound of
`fidelity_bound.md`. The appearance of collapse is fidelity-bounded
self-measurement on the unitary substrate of inviolable #3
(`collapse_dissolution.md`); no non-unitary projection postulate is
required.

Equivalence is the **single-`m`** identity of the substrate Lagrangian
(`equivalence_dissolution.md`): one mass parameter per mode entering
as both kinetic coefficient (inertia) and sync-cost coupling
(gravitational response). Local Lorentz from `(3, 1)`-signature
derivation.

The **dynamical bridge** between the two limits is the discrete
cascade `K_n^d = b^{−n}` (`master_cascade_identity.md`) with cadence
forced to `2/(q₃·19_Λ)` per the K(t) closure
(`k_of_t_residual_disposition.md`). Inflation samples `√5 ≈ 2.236`
cascade levels at this cadence, giving `N_efolds ≈ 63.7` — testable
on the CMB-S4 / LiteBIRD horizon.

---

## The composition

The synthesis is built from already-derived structural results
combined under the framework's discipline. Each composition step is
named below; each cites its load-bearing source.

### Step 1 — The two endpoints

| | K = 1 endpoint | K < 1 endpoint |
|---|---|---|
| What | Einstein field equations, Friedmann at `r = 1` | Schrödinger equation via Madelung |
| Mechanism | ADM-Kuramoto dictionary + Lovelock's theorem | Madelung `(ρ, S)` variables on partially-unlocked substrate |
| Status | Class-5, derived | Class-5, derived |
| Source | `einstein_from_kuramoto.md` (D13), `k_of_t_friedmann.md` S1–S2 | `continuum_limits.md` Part II (D12) |

Both endpoints are **structural results already on `main`** prior to
the synthesis. The Tier-C capstone synthesis does not re-derive them;
it names how they compose with the other pillars.

### Step 2 — The Tier-C pillars (each a recent dissolution / theorem)

| Pillar | What it dissolves / forces | Source PR |
|---|---|---|
| Equivalence dissolution | Single-`m` substrate identity ⇒ inertial = gravitational; local Lorentz from `(3, 1)`-signature; the equivalence principle is a tautology, not an empirical near-coincidence | `equivalence_dissolution.md`, #176 |
| Collapse dissolution | Substrate is unitary (#3); apparent collapse = fidelity-bounded self-measurement; Born rule `|ψ|²` from `J² = −I`; no non-unitary projection postulate | `collapse_dissolution.md`, #177 |
| EPR/Bell assembly | Non-signaling Bell-violation from topological non-locality; conserved `Q_{AB} mod 2` is global, not local hidden variable; Bell's no-go does not apply | `epr_bell_assembly_theorem.md`, #152 |
| K(t) cadence closure | Era-timeline Tier 3 structurally closed; cadence = `2/(q₃·19_Λ)` forced; `N_efolds ≈ 63.7` predicted | `k_of_t_residual_disposition.md`, #179 |

Each pillar is a structural result on its own. The synthesis is their
*joint statement*: together, they comprise the GR-QM unification
because they cover its three classical sticking points (gravity-side,
quantum-side, locality-side) plus the dynamical bridge between the
two endpoints.

### Step 3 — How the pillars compose

The composition closes the unification at the *claim* level:

- **The GR side** (equivalence + Einstein limit) gives Einstein's
  field equations + universality of free fall, with no fit and no
  free parameter at the structural level. Absolute magnitudes of `G`,
  cosmological scale, etc. remain anchor-declined per the Basepoint
  Principle.
- **The QM side** (collapse + Schrödinger limit) gives Schrödinger
  evolution + Born rule + fidelity-bound interpretation of
  apparent collapse, with no non-unitary postulate. Absolute
  amplitudes / specific timescales remain anchor-declined.
- **The locality side** (EPR/Bell) gives Bell-violating non-signaling
  correlations from substrate topology — *not* a signaling mechanism,
  *not* a hidden-variable mechanism, *not* a violation of relativity.
  The "spooky action at a distance" is the global `Q mod 2`
  conservation manifesting in correlations; signaling is forbidden by
  the conservation's mod-2 nature.
- **The dynamical bridge** (K(t) cadence closure) gives the
  *discrete* trajectory between the two endpoints: the cascade
  station ordering is forced (#9 arrow, Farey slip-order), the
  cadence is structurally forced to `2/(q₃·19_Λ)`, the absolute
  schedule is anchor-declined (`H₀`-dependent). The bridge is
  *non-smooth* by substrate structure — a Class-5 feature that
  *forces* the two-anchor minimality, not a gap to smooth.

The synthesis: GR's structure at one endpoint, QM's structure at the
other, topological non-locality across the substrate's full extent,
and a forced discrete cascade between them. *One substrate, two
couplings, four structural results combining.*

---

## What this closes (relative to the lesson's "honest boundary")

The lesson `lesson_epr_gr_qm_unification.md` §6 stated the open
frontier with admirable honesty:

> "the K = 1 ↔ K < 1 *dynamical bridge* (N9) is open. Teaching the
> open frontier honestly is what earns the rest."

That framing was correct at the time of writing. With the K(t)
cadence closure landed (#179), the disposition updates:

| Component | Lesson framing | Now (post-#179) |
|---|---|---|
| Two endpoints derived | derived ✓ | derived ✓ (unchanged) |
| EPR resolution | derived ✓ | derived ✓ (unchanged) |
| Equivalence as substrate identity | implicit | explicit (#176) |
| Collapse as fidelity-bounded self-measurement | implicit | explicit (#177) |
| Era-timeline ordering | structural | structural (unchanged) |
| Era-timeline schedule | anchor-declined | anchor-declined (unchanged) |
| Era-timeline K↔epoch cadence | Class-2 (lesson said "plausibly anchor-conditional") | **structurally closed** (#179): cadence = `2/(q₃·19_Λ)`, `N_efolds ≈ 63.7` |
| Smooth K(z) interpolation between limits | "not derived; the bridge is open" | **structurally absent by design** — a Class-5 feature, not a gap; the non-smoothness *forces* two-anchor minimality |

The lesson said the dynamical bridge was "open." With #179, the
*discrete* dynamical bridge (cascade cadence + ordering) is closed at
the substrate level, while the *continuous* interpolation `K(z)` is
seen to be structurally absent rather than missing — it cannot exist
on this substrate because the K = 1 ↔ K < 1 transition is non-smooth
by the substrate's own structure (N10, N11; `continuity_in_K_nulls.md`).
That non-existence is now understood as a Class-5 feature, not a
research frontier.

The lesson is **correct as written** for the time it was written; it
honestly named an open piece that has since been closed. The capstone
synthesis here is the update: the closure has happened, the bridge is
specified (discretely), and the smooth-interpolation absence is
positive structure rather than open work.

---

## What this does **not** close

In the discipline of the framework's other dissolutions and closures:

- **Magnitudes.** The framework derives the *structure* of GR-QM
  unification, not the *magnitude* of gravity (`G`, cosmological scale)
  nor of QM (absolute amplitudes, environment-coupling frequencies).
  Tier 2 of the era timeline remains anchor-declined per the Basepoint
  Principle.
- **Specific observational predictions are pillar-by-pillar
  falsifiable**, not unified-as-a-whole-falsifiable. A failure on any
  one pillar identifies which substrate piece needs revision.
- **Cascade↔Salpeter slope** remains statistically gated
  (`p ≈ 0.10` per `cascade_slope_check.py` as of #163); the cascade
  ordering and the slope formula `α = −q₂ − n/d` are structural, but
  the *match* to observed mass functions has statistical confounders.
- **Tensor-to-scalar ratio `r`** remains Class-2 / TBD per the
  scorecard, pending CMB-S4. It constrains `N_efolds` via slow-roll
  relations but is itself not forced structurally.
- **Preferred-basis problem (in QM interpretation).** The framework
  has phase as the primary substrate variable; basis-selection
  questions reduce to "what's the basis of the substrate's encoding,"
  which is open work for the projector design rather than closed by
  the collapse dissolution.

These open items do not block the capstone; they are the standard
discipline boundary the framework has maintained throughout.

---

## Falsifiers

The capstone inherits its falsifiers from each pillar (this is
intentional — each pillar has a clean falsification window that
identifies which structural piece broke).

Inherited falsifiers (cf. each pillar's doc for sharper statements):

- **Direct violation of universality of free fall** above the MOND
  threshold (`equivalence_dissolution.md`).
- **Demonstrable non-unitary residual** in a perfectly isolated
  system (`collapse_dissolution.md`).
- **Signaling using EPR correlations** at any rate
  (`epr_bell_assembly_theorem.md`).
- **`N_efolds` measured outside `[62, 66]`** at experimental
  precision (`k_of_t_residual_disposition.md`).
- **Detection of a 4th-generation charged lepton** (integer
  conservation law, `q_mod2_conservation_theorem.md`).
- **`θ_QCD ≠ 0`** measured at sufficient precision
  (Pin+(3) topology, `coupling_scales.md`).

**Synthesis-level falsifier:** if *multiple* pillars fail across
their independent observational regimes — say `N_efolds` lands at 70
*and* universality of free fall shows a composition-dependent
residual at MICROSCOPE-precision *and* the RAR scatter shape fails
the fidelity-bound transfer function — the framework needs
substantial revision, not just a pillar-level repair.

If *one* pillar fails, the falsification identifies which substrate
piece needs reopening, without invalidating the others. This is the
shape the framework's discipline was designed for.

---

## Why this matters

The Tier-C capstone is the framework's most exposed claim and its
deepest application. With the synthesis articulated, the framework's
structural inventory now spans:

- **Foundational primitives** (Mediant + EML + Klein bottle +
  half-twist) — `substrate_determinism.md` #4 closure
- **Substrate structure** (`(3, 1)` signature, `Spin(3, 1)` /
  `SL(2, ℂ)`, Pin+(3), Z₂ topological charge) — derived from the
  primitives
- **Two macroscopic limits** (Einstein at `K = 1`, Schrödinger at
  `K < 1`) — derived
- **Three Tier-C dissolutions / theorems** (equivalence, collapse,
  EPR/Bell) — recently consolidated (#176, #177, #152)
- **One dynamical-bridge closure** (K(t) cadence to `2/(q₃·19_Λ)`)
  — recently consolidated (#178 + #179)
- **A vindication-shape suite of testable predictions** —
  consolidated in `predictions_horizon_2026.md` (#180)

The capstone synthesis names the composition of those pieces. It is
the structural counterpart to the pedagogical lesson — the lesson
teaches *what* and *why*; the synthesis articulates *how* it composes.

Class: foundational consolidation (Class 3, articulation). The arc
closed is the GR-QM unification's "how do the pieces fit" question;
the pieces are each in derived column, and this names the assembly.

---

## Cross-links

- `lesson_epr_gr_qm_unification.md` — the pedagogical companion;
  teaching narrative, instructor notes, segment timings. This
  synthesis cites the lesson; the lesson should be updated (separately)
  to cite this synthesis once landed.
- `equivalence_dissolution.md` — GR pillar (#176).
- `collapse_dissolution.md` — QM pillar (#177).
- `epr_bell_assembly_theorem.md` — locality pillar (#152).
- `k_of_t_residual_disposition.md` — dynamical bridge closure (#179).
- `bicone_golden_z2_identification.md` — the bridge derivation enabling
  the K(t) closure.
- `q_mod2_mediant_projection.md` — the state-axis projection of #1
  (#178) underlying the K(t) closure.
- `continuum_limits.md` — Part I (`K = 1 → Einstein`), Part II
  (`K < 1 → Schrödinger`); the two non-smooth limits.
- `einstein_from_kuramoto.md` — Lovelock uniqueness; the K = 1 limit.
- `k_of_t_friedmann.md` — Friedmann at `r = 1`; S1–S2 closed.
- `continuity_in_K_nulls.md` — N9–N16 nulls; the non-smoothness is
  structural, not a gap.
- `era_timeline_disposition.md` — N9 S5 three-tier disposition; Tier 3
  now closed by #179.
- `master_cascade_identity.md` — discrete cascade `K_n^d = b^{−n}`;
  the bridge's underlying structure.
- `q_mod2_conservation_theorem.md` — inviolable #1; the locality
  pillar's foundation.
- `figure_eight.md` — Born rule, measurement = crossing; the
  collapse pillar's foundation.
- `substrate_determinism.md` — the 10 inviolables; the framework's
  structural backbone.
- `fidelity_bound.md` — the self-measurement apparatus underlying
  the collapse dissolution.
- `predictions_horizon_2026.md` — testable consequences of the
  synthesis suite (#180).

---

## One-line summary

The Tier-C capstone — GR and QM are one discrete substrate at two
couplings (`K = 1 →` Einstein via Lovelock; `K < 1 →` Schrödinger via
Madelung) — has its structural form complete with the four pillars
(equivalence dissolution #176, collapse dissolution #177, EPR/Bell
assembly theorem #152, K(t) cadence closure #179): the *discrete*
dynamical bridge is forced, the *continuous* `K(z)` is structurally
absent by design (a Class-5 feature, not a gap), and the synthesis
inherits pillar-by-pillar falsifiability with `N_efolds ≈ 63.7` as
its most forward-loaded test.
