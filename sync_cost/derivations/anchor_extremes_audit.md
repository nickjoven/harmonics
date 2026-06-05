# Anchors at extremes audit (chain extension)

## Status

**Extension of the conservation chain inventory** from
`born_rule_mode_count_extremes_audit.md` (PR #222) to cover
the framework's two **observational anchors** — H_0
(cosmological) and v_EW (particle-sector) — across the three
regimes (Planck / Standard / Hubble).

**Verdict**: anchors are a **fourth layer-status category**
beyond the three identified in the parent audit chain.

- **Count is structurally forced** (two), by the non-smooth K=1
  critical line separating the cosmological (Einstein, K=1) and
  matter (Schrödinger, K<1) regimes per
  `anchor_count_audit.md`'s 2026-04-25 closure.
- **Values are observational inputs**, not derived from substrate
  primitives. H_0 = 67–73 km/s/Mpc (subject to the H_0 tension);
  v_EW = 246 GeV.
- **Constancy across regimes is an assumption of the apparatus,
  not a derivation**. This is the structural feature the audit
  surfaces explicitly.

The **H_0 tension** (CMB-derived 67.4 vs distance-ladder 73
km/s/Mpc at 4–5σ) is the closest current empirical falsifier
candidate for the constancy assumption.

The four-invariant layer-status taxonomy from PR #222 (pure
algebraic, hybrid, pure topological) extends to five categories
with the addition of **pure address (observational anchor)** —
inputs that are neither algebraic-derivable nor
topology-derivable, whose count is structurally forced and whose
values are observational.

Class: foundational rigor check / conservation chain extension.
Resolution-mode throughout — no apparatus changes; composes
existing canonical claims (anchor_count_audit's two-anchor
verdict, primitives-vs-addresses methodology, PR #221's
structural identity, PR #222's chain extension) into a
regime-mapped reading.

---

## The audit task

The parent stratification audit and PRs #221–#222 audited the
conservation chain's algebraic-and-topological invariants
(dissipation, Q mod 2, Born rule, mode count). The framework's
observational anchors — H_0 and v_EW — sit at a different
structural location: they are the *dimensional inputs* the
framework's dimensionless predictions are anchored to.

`anchor_count_audit.md` audits the *count* of anchors: two,
structurally forced. What it does not do is map anchors against
the three regimes the conservation chain operates in, classify
their layer-status against the rest of the chain, or identify
their empirical-falsifier landscape in the way the other chain
audits do.

The audit asks:

1. **Inventory**: name H_0 and v_EW as conservation-chain
   elements; map their connections to the chain's other
   invariants.
2. **Scale mapping**: how does each anchor operate across the
   three regimes? Where do they "live" structurally?
3. **Layer-status classification**: are anchors algebraic,
   topological, hybrid, or something else?
4. **Gaps**: what's not derived about anchors at extremes?
5. **Falsifiers**: what observations would test the anchor
   structure?

The five-invariant chain — Q mod 2 (+ extensions), dissipation,
Born rule, mode count, anchors — is the current scope of the
framework's foundational conservation apparatus through this PR.

---

## Anchor inventory

The framework has **two** observational anchors, per
`anchor_count_audit.md`:

1. **H_0** (Hubble constant) — cosmological sector. Sets the
   Hubble time `t_H = 1/H_0`, Hubble length `L_H = c/H_0`,
   critical density `ρ_crit = 3H₀²/(8πG)`. Via the framework
   integer `R = 6·13⁵⁴` (from `planck_scale.md`): `t_P = t_H/R`
   and `ℓ_P = L_H/R`. The cosmological sector closes with H_0
   alone + dimensionless ratios.
2. **v_EW** (electroweak vacuum expectation value, 246 GeV) —
   particle sector. Sets all absolute particle masses via
   framework-derived dimensionless ratios. ℏ, c, G in absolute
   units require v_EW per `coupling_scales.md`. The particle
   sector closes with v_EW alone + framework-derived
   dimensionless couplings.

The two anchors are **structurally decoupled** by the non-smooth
K=1 critical line of the substrate's self-consistency equation
(`continuum_limits.md` Part I: K=1 → Einstein;
`continuum_limits.md` Part II: K<1 → Schrödinger;
`continuity_in_K_nulls.md` N11: K=1 ↔ K<1 transition is
non-smooth via tongue-coverage discontinuity). The two-anchor
minimum is therefore **fully structural** per
`anchor_count_audit.md`'s 2026-04-25 closure — not a derivation
gap to be lifted but a structural feature of the framework's
two-regime architecture.

Suggestive but underived: `v/M_P ≈ 13⁻¹⁵ = 1.954×10⁻¹⁷` matches
observed `v/M_P ≈ 2.02×10⁻¹⁷` at 3.1%. Logged as Class 2 in
`numerology_inventory.md`. Not load-bearing for this audit.

---

## H_0 audit

### Substrate basis

H_0 is not derived from substrate primitives. It is the
cosmological-sector observational input. Its structural
*existence* (a single dimensionful anchor for the cosmological
sector) is forced by the framework's apparatus — every
cosmological prediction is anchored to H_0 + framework-derived
dimensionless ratios. Its *value* is observational.

H_0 is connected to the chain's other invariants:

- **Mode count**: Ω_Λ = 0.6847 from 12.66 effective modes (PR
  #222 verdict) is anchored to H_0 via the cosmological sector.
  The 12.66-mode prediction's empirical corroboration depends
  on H_0's anchor status.
- **Planck scale**: ℓ_P, t_P, M_P all derive from H_0 via
  `R = 6·13⁵⁴` (`planck_scale.md`; `anchor_count_audit.md`
  L26-28). This is a **structural integer chain** connecting
  the cosmological anchor to the Planck floor.
- **Dissipation**: rate scales with H_0 in the cosmological
  sector (matter K_STAR ↔ cosmological coupling per the parent
  stratification audit).

### Scale-by-scale audit

**Standard scale**. H_0 is above standard-scale physics (the
matter sector lives at v_EW). H_0 enters standard-scale physics
only through its derived cosmological constants (Λ, ℓ_P, t_P,
M_P) acting as boundary conditions. H_0 itself is not directly
measurable at standard scales; it is inferred from cosmological
observations.

**Hubble scale**. H_0 *is* the Hubble scale. `t_H = 1/H_0` is
the Hubble time; `L_H = c/H_0` is the Hubble length. The
cosmological horizon at the 12.66-mode boundary (w* ≈ 0.83) is
co-defined with H_0. The cosmological sector's closure relies
on H_0 holding its anchor status across cosmological time.

**Planck scale**. ℓ_P and t_P are derived from H_0 via the
framework integer `R = 6·13⁵⁴`. This is a structural depth-count
relation — Planck is 145.8 Fibonacci levels below Hubble per
`planck_scale.md`. At the Planck floor itself, H_0 doesn't
*degrade* the way Q mod 2 / Born rule / mode count do, because
H_0 is not a substrate property — it is the observational
anchor the framework's structural integer chain *terminates at*
on the cosmological end. The Planck floor's substrate degradation
affects what the framework's apparatus can *compute* about
Planck-scale physics; it does not affect H_0's status as the
cosmological-end anchor of the depth-count chain.

### Verdict on H_0

**Layer-status: pure address (observational anchor)**,
structurally connected to the Planck floor via the depth-count
chain `R = 6·13⁵⁴`. Constancy across regimes is **assumed**, not
derived. The H_0 tension is the actionable empirical falsifier
for this constancy.

---

## v_EW audit

### Substrate basis

v_EW = 246 GeV is the particle-sector observational input. Its
structural *existence* (a single dimensionful anchor for the
matter sector) is forced; its *value* is observational. Per
`coupling_scales.md` §IV: "v = 246 GeV — Not derived"; the
absolute scales ℏ, c, G all *require* v in their particle-physics
units.

v_EW is connected to the chain's other invariants:

- **Born rule**: |ψ|² weighting depends on the populated mode
  spectrum, which is K_STAR-located, which is at the
  matter-sector scale anchored by v_EW. The Born rule's
  operating regime is v_EW-anchored.
- **Mode count**: the 14-mode K_STAR location is fixed by
  framework Farey index 4 + Klein bottle structure, but its
  *physical scale* (where in energy/mass units those 14 modes
  live) is anchored to v_EW.
- **Q mod 2**: the K² substrate operates at the matter scale;
  Q mod 2's standard-scale operation is in the regime anchored
  by v_EW.

### Scale-by-scale audit

**Standard scale**. v_EW *is* the matter-sector scale. The
Higgs mechanism produces v_EW as the electroweak vacuum
expectation value; all absolute particle masses derive from v_EW
+ framework-derived dimensionless ratios
(`mass_sector_closure.md`, `coupling_scales.md`). All LHC
phenomenology operates here.

**Hubble scale**. v_EW is sub-Hubble (matter-sector physics
inside the cosmological horizon). Structurally decoupled from
H_0 by the K=1 critical line. The matter sector does not
participate in the cosmological-boundary mode-count truncation
(12.66 vs 14) — those boundary-weight effects happen at the
cosmological scale, not the matter scale.

**Planck scale**. The ratio `v/M_P ≈ 2.02×10⁻¹⁷` is the
"hierarchy problem" in SM language. In framework terms (per
`hierarchy_problem_translation.md`): the SM hierarchy problem
requires three ingredients (small ratio, naturalness criterion,
quadratic UV divergences) and only the first translates to the
framework. The framework does not import naturalness or
divergences; the small ratio is just an observation.

The 13⁻¹⁵ = 1.954×10⁻¹⁷ near-match (3.1% off) is suggestive but
not derived. `path_a_walkthrough.md` shows the canonical
register's prime support {2, 3} cannot reach 15 = 3·5 in any
of three natural sub-action interpretations; this is *positive
evidence* that v/M_P is an independent input rather than a
derivation gap (per `anchor_count_audit.md`'s 2026-04-24 reframe
note).

At the Planck floor itself, v_EW does not degrade — it sits 17
orders of magnitude above Planck. Like H_0, v_EW is an
observational anchor, not a substrate property; the Planck
floor's substrate degradation affects what the framework's
apparatus can *compute* about Planck-scale physics, not v_EW's
status as the matter-end anchor.

### Verdict on v_EW

**Layer-status: pure address (observational anchor)**, with
*only suggestive numerical* connection to the Planck floor (no
R-analog derived; the 13⁻¹⁵ near-match is logged as Class 2
numerology, not a derivation). Constancy across regimes
**assumed**.

---

## Side-by-side: the five-invariant chain

Extending PR #222's table with the anchor row:

| Invariant | Mechanism basis | Operation basis | Standard | Hubble | Planck |
|---|---|---|---|---|---|
| Dissipation | Algebraic (rank-1 Fréchet) | Algebraic | Universal | Universal | Universal |
| Q mod 2 | Topological (K² antiperiodic H₁) | Topological | Conserved | Conserved within horizon | Fuzzy emergence |
| Born rule | Algebraic (saddle-node universality) | Topological (mode spectrum) | Universal | Universal within horizon | Fuzzy emergence (inherits floor) |
| Mode count | Topological (K² Farey/SB lattice) | Topological | 14 modes | 12.66 modes | Fuzzy emergence to zero |
| **Anchors (H_0, v_EW)** | **Observational** | **Observational** | **v_EW anchors matter** | **H_0 anchors cosmos** | **Anchors terminate depth chain (H_0 via R; v_EW only suggestively)** |

Five layer-status categories now identified:

- **Pure algebraic**: dissipation. Layer-invariant.
- **Hybrid** (algebraic mechanism + topological operation): Born
  rule. Universal mechanism; scale-specific operating regime.
- **Pure topological**: Q mod 2, mode count. Scale-specific
  throughout via topology dependence.
- **Pure address (observational anchor)**: H_0, v_EW. Count
  structurally forced (two); values observational; constancy
  across regimes assumed.

---

## Layer-invariance refinement

`primitives_vs_addresses_candidate.md` lists "anchors" as
layer-specific addresses (alongside K_STAR, 12.66, w*, Ω_Λ).
This audit refines that classification: anchors are a *distinct
sub-category of addresses* — fundamental addresses that are
not reducible to other framework objects (unlike K_STAR, which
is derived from `q_2`, `q_3`, and `|F_4|`, or 12.66, which is
derived from w* via the boundary weight formula).

The address taxonomy:

- **Derived addresses**: K_STAR ≈ 0.86, 12.66 modes, w* ≈ 0.83,
  Ω_Λ ≈ 0.6847. Computed from primitives + substrate topology +
  boundary conditions. Their *values* are framework outputs.
- **Anchor addresses**: H_0, v_EW. Observational inputs the
  framework's dimensionless predictions are anchored against.
  Their *values* are framework inputs.

The two-anchor minimum (per the 2026-04-25 closure note) is
**structurally forced** but anchor *values* remain observational.
Count-structure is layer-invariant; values are layer-specific.

---

## Gaps

**Gap 1 — No depth count Planck-to-EW**. The cosmological
sector has `R = 6·13⁵⁴` connecting H_0 to ℓ_P (145.8 Fibonacci
levels). No analogous depth count connects v_EW to ℓ_P. This
is obstruction #2 from `anchor_count_audit.md`, reframed
(2026-04-24) as likely a structural feature of cross-sector
independence rather than a derivation gap. The reframing does
not close the question — it changes what an answer would mean.

**Gap 2 — No framework-native v_EW/ℏ derivation**. Obstruction
#3 from `anchor_count_audit.md`: if v_EW were structurally
pinned (e.g., as the tongue-boundary frequency of a fundamental
locking on the Klein substrate), the matter-sector anchor would
derive. Currently v_EW is observational input. Open.

**Gap 3 — v/M_P numerology vs derivation**. `13⁻¹⁵ = 1.954×10⁻¹⁷`
near-matches observed `v/M_P ≈ 2.02×10⁻¹⁷` at 3.1%. Suggestive
(15 = q_3 · F_5; 13 = |F_6| is the DE-sector integer), but no
structural derivation. Class 2 numerology per
`numerology_inventory.md`. Per `path_a_walkthrough.md`, the
canonical register's prime support {2, 3} cannot reach 15 = 3·5,
which is positive evidence against a derivation existing at all.

**Gap 4 — Anchor constancy across regimes is assumed**. The
framework's apparatus treats H_0 and v_EW as constant across
cosmic time and across scale-regime transitions. No structural
derivation forces this constancy. For H_0, the H_0 tension is
a candidate falsifier for the cosmological anchor's strict
constancy.

**Gap 5 — Cross-sector unification within K=1/K<1 framework
not addressed beyond decoupling closure**. The 2026-04-25
closure note establishes that decoupling is structurally forced
by the K=1 critical line. It does not address whether the two
anchors could share a deeper structural relationship not visible
at the K=1/K<1 separation level — i.e., whether the framework's
own apparatus admits a unification that the existing chain
hasn't surfaced.

---

## Falsifiers

**For anchor count**:

- **F1 — Anchor reduction**. If H_0 or v_EW are derived from
  substrate primitives via a new structural derivation, the
  two-anchor minimum falsifies. Empirically: no signal yet;
  the 2026-04-25 closure suggests count is fully structural.
- **F2 — Third anchor needed**. Discovery of a third
  independent dimensional scale not derivable from H_0 or v_EW
  would falsify the two-anchor minimum upward. Would require
  new physics beyond the framework's current K=1/K<1 partition.

**For anchor constancy**:

- **F3 — H_0 tension is real**. If the CMB-vs-distance-ladder
  H_0 discrepancy (≈67 vs ≈73 km/s/Mpc, 4–5σ) is not resolved
  by systematics and reflects genuine evolution of H_0 with
  cosmological time, the constancy assumption for the
  cosmological anchor falsifies. **Most actionable observational
  falsifier in this audit.** Framework response would need: (a)
  acknowledgement that H_0 is scale/time-dependent within the
  cosmological sector, or (b) a structural derivation of how H_0
  evolves.
- **F4 — v_EW running**. If v_EW (or the EW VEV) is observed
  to vary with energy scale at LHC precision (analogous to
  running couplings but for the VEV itself), the matter-anchor
  constancy assumption falsifies. Currently no such signal.

**For anchor-to-chain connections**:

- **F5 — Ω_Λ moving outside 12.66-mode prediction**. Already
  flagged as F4 in PR #222 (precision measurements of Ω_Λ
  inconsistent with 0.6847). Doubles as anchor-falsifier: Ω_Λ's
  match to 12.66 is *conditional* on H_0's anchor status. If
  Ω_Λ moves outside framework prediction, either the mode count
  derivation falsifies (PR #222 falsifier) or H_0's anchor
  status changes (this audit's falsifier).
- **F6 — v/M_P precision inconsistent with 13⁻¹⁵**. Future
  precision measurements moving v/M_P significantly off
  `1.954×10⁻¹⁷` would test the numerology. Not load-bearing
  (3.1% off; not a derivation; logged Class 2). But would
  remove the "suggestive near-match" from the audit landscape.

---

## Empirical alignment

### H_0 tension (constancy test, most active)

CMB-derived H_0 (Planck 2018): ≈ 67.4 km/s/Mpc. Distance-ladder
H_0 (SH0ES Cepheid + Type Ia): ≈ 73 km/s/Mpc. Discrepancy at
4–5σ across multiple independent methods, persisting under
systematics scrutiny.

Framework reading: H_0 is the cosmological anchor; its
constancy across cosmological time is a structural assumption
of the apparatus. The H_0 tension is the candidate empirical
falsifier (F3) for this assumption.

Three possible outcomes:

1. **Tension resolves to systematics**. Anchor structure
   preserved; framework's constancy assumption stands.
2. **Tension reflects evolving H_0**. The framework needs
   either: (a) acknowledgement that the cosmological anchor is
   epoch-dependent within the cosmological sector, or (b) a
   structural derivation of H_0 evolution.
3. **Tension reflects new cosmological physics** (early dark
   energy, modified gravity, etc.). Framework's K=1 Einstein
   regime would need to accommodate the new physics; anchor
   status might or might not survive.

Currently unresolved; ongoing observational program. The audit
flags this as the most actionable falsifier without taking a
position on which outcome obtains.

### Ω_Λ (anchored prediction via 12.66 modes)

Same alignment as in PR #222: framework's Ω_Λ(w*=0.83) =
0.6847 matches observed 0.685 ± 0.007 at 0.004σ. Anchored to
H_0 — the match is conditional on H_0's status as the
cosmological anchor. If H_0 tension falsifies anchor constancy
(F3), this anchored prediction needs re-evaluation.

### v/M_P near-match

Suggestive numerology only (3.1% off; no structural
derivation; per `path_a_walkthrough.md`'s closure, the canonical
register cannot reach 15 = 3·5). Not load-bearing for the
audit's verdict. Status: noted but unsealed.

### What alignment shows

The audit's strongest empirical contribution is **flagging the
H_0 tension as the actionable falsifier for the cosmological
anchor's constancy**. The Ω_Λ match is conditional on H_0's
status; if H_0 isn't strictly constant, the conditional match
needs to be re-read. v/M_P near-match is decorative.

In contrast with PR #222's three empirical alignments at three
strengths (CMB Ω_Λ strongest, Higgs entanglement most
discriminating, λ_HHH indirect), this audit has **one actionable
falsifier** (H_0 tension) and one conditional alignment (Ω_Λ via
H_0). The anchor sector is less empirically rich for the chain
audit than the substrate-derived invariants, because anchors are
observational inputs rather than derived structural facts —
there is less to corroborate empirically.

---

## What this is and isn't

**This is**: an extension of the conservation chain inventory
to cover the framework's two observational anchors (H_0, v_EW)
across the three regimes. It identifies a fifth layer-status
category (pure address / observational anchor) and refines the
primitives-vs-addresses methodology by distinguishing *derived
addresses* (K_STAR, 12.66, w*, Ω_Λ) from *anchor addresses*
(H_0, v_EW). It connects to the H_0 tension as the most
actionable empirical falsifier for anchor constancy and notes
that the Ω_Λ alignment from PR #222 is conditional on H_0's
anchor status.

**This is not**: a derivation of H_0 or v_EW from substrate
primitives. The anchor structure is observational; the two-anchor
minimum is structurally forced but values remain observational.

**This is not**: a closure of `anchor_count_audit.md`'s open
obstructions (#2 EW depth count, #3 ω₀ derivation). Those remain
open. The reframe notes from 2026-04-24/25 are referenced but
not extended.

**This is not**: a position on the H_0 tension's resolution.
The audit flags the tension as the framework's most actionable
falsifier; it does not predict which of the three outcomes
(systematics / evolving H_0 / new cosmological physics) obtains.

**This is not**: a complete conservation chain audit. Generation
count and sector count remain candidates for future
chain-extension audits.

---

## Open: next chain extensions

After anchors, the natural next chain elements:

1. **Generation count** — three generations of fermions; the
   framework's Klein bottle signature (3, 1) provides the
   structural basis (`klein_bottle.md`, `mass_sector_closure.md`).
   Whether the "3" is layer-invariant (forced by K² signature)
   or scale-specific is partially addressed; an extremes-audit
   would map across regimes.
2. **Sector count** — lepton/quark sectors; tied to the
   substrate's R-eigenstate spectrum
   (`klein_z2_decomposition_falsifier_2.md`'s y-parity reading).
   The third-caveat doc establishes modal sufficiency at
   standard scale; an extremes audit would extend to Planck/
   Hubble.

These would extend the conservation chain audit to cover the
framework's full structural inventory.

---

## Cross-links

- `conservation_scale_stratification_audit.md` — original parent
  audit; this audit extends its inventory.
- `q_mod2_planck_emergence_audit.md` (PR #221) — structural
  identity (Klein-bottle emergence ≡ Planck self-sustenance)
  this audit uses to ground anchor-to-Planck depth-chain
  termination.
- `born_rule_mode_count_extremes_audit.md` (PR #222) — chain
  extension this audit extends; fifth layer-status category
  added here.
- `anchor_count_audit.md` — *the* parent audit on anchor
  counting; this audit extends its scope to regime-mapping and
  layer-status classification but does not re-do the counting
  argument.
- `planck_scale.md` — `R = 6·13⁵⁴` depth count from H_0 to
  Planck; 145.8 Fibonacci levels.
- `coupling_scales.md` §IV — "v = 246 GeV Not derived" table.
- `hierarchy_gaussian_lattice.md` — T4 language softened
  post-`anchor_count_audit` to reflect two-anchor minimum.
- `hierarchy_problem_translation.md` — SM hierarchy problem
  does not translate to framework; "small ratio" is just an
  observation here, not a problem.
- `path_a_walkthrough.md` — canonical register's prime support
  {2, 3} closure; positive evidence that v/M_P derivation does
  not exist.
- `vocabulary_is_the_work_pattern.md` — recurring framework
  move (vocabulary-artifact → null/reframe) exemplified by the
  anchor-count reframing.
- `continuum_limits.md` — K=1 Einstein / K<1 Schrödinger
  non-smooth separation; the structural basis for two-anchor
  decoupling.
- `continuity_in_K_nulls.md` N11 — K=1 ↔ K<1 tongue-coverage
  discontinuity; the substrate-internal mechanism for the
  K=1/K<1 separation.
- `primitives_vs_addresses_candidate.md` — anchors listed as
  layer-specific addresses; this audit refines into derived
  addresses vs anchor addresses.
- `numerology_inventory.md` — `13⁻¹⁵` for v/M_P logged as
  Class 2.
- `klein_bottle_restructure_price.md` — empirical floor.
- `klein_z2_decomposition_falsifier_2.md` — adjacent audit
  pattern (MODAL/GENERATIVE).
- `feedback_resolution_vs_reconstruction.md` (memory) —
  resolution-mode preserved.

---

## One-line summary

This audit extends the conservation chain inventory from
dissipation + Q mod 2 + Born rule + mode count to cover the
framework's two observational anchors (H_0 cosmological, v_EW
particle-sector) across the three regimes (Planck / Standard /
Hubble). Verdict: anchors form a **fifth layer-status category**
(pure address / observational anchor) beyond the four identified
in PRs #221–#222, with count structurally forced (two, per
`anchor_count_audit.md`'s 2026-04-25 closure via the K=1
critical line) and values observational. Constancy across
regimes is **assumed**, not derived. H_0 is connected to the
Planck floor via the structural integer chain `R = 6·13⁵⁴`;
v_EW's connection is only suggestive (13⁻¹⁵ near-match at 3.1%,
no derivation). The **H_0 tension** (CMB ≈ 67 vs distance-ladder
≈ 73 km/s/Mpc, 4–5σ) is the most actionable empirical falsifier
in the audit, testing the cosmological anchor's constancy
assumption. The Ω_Λ alignment from PR #222 is conditional on
H_0's anchor status. Anchor sector is less empirically rich for
chain audit than substrate-derived invariants because anchors
are inputs, not derivations. Next chain extensions: generation
count, sector count.
