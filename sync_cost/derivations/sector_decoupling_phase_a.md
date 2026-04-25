# Sector decoupling derivation (Region D, Anchor obstruction #5) — Phase A

## What this file is

Phase A planning for Region D from the work-map landscape — the
deepest currently-open framework derivation. Committed as the
follow-up to Region C (numerology count) per the methodology
shift from single-session audits to multi-session structural work.

Region D is anchor-count obstruction #5 from `anchor_count_audit.md`:

> **Structural decoupling of sectors.** Cosmological derivations
> (R, Λ, Ω partition) and particle derivations (couplings, mass
> ratios, gauge group) currently close *separately*. No
> cross-sector structural constraint — no shared integer, no
> shared depth count, no shared tongue — forces them to share
> an anchor. Finding such a constraint, even without reducing
> the count, would be the first substantive step.

The reframed question (per `vocabulary_is_the_work_pattern.md`
Instance 6 / `hierarchy_problem_translation.md`):

> **Does the framework PREDICT sector decoupling, or just ALLOW
> it?** If predicted, the two-anchor minimum is a structural
> consequence. If only allowed, two anchors is a framework
> choice that could be revisited.

## Why this derivation, why now

Per `remaining_gap_shapes.md` and the work-map landscape, this
is the **deepest unresolved question** in the framework:

- Path (a) closure showed two-anchor minimum is consistent with
  substrate's prime support {2, 3} not supporting v/M_P closure
  (positive evidence for two anchors)
- SM hierarchy translation showed naturalness language doesn't
  apply (the anchor-count question is reframed, not solved)
- Anchor obstructions #1-#4 reframed as features per
  `vocabulary_is_the_work_pattern.md` Consequence 1

But #5 sits differently: it asks whether the **separation** is
forced or assumed. This is logically prior to whether the
count is two or one — first we need to know the framework's
sector structure is a derivation, then we ask whether two
sectors is forced.

If derivation succeeds: framework's two-anchor structural status
upgrades from "consistent with" to "forced by." Substantial
strengthening.

If derivation fails (no forcing argument can be constructed):
two-anchor minimum remains a framework convention, not a
prediction.

## Scope

Phase A deliverable: a **derivation roadmap**, not the
derivation itself. Specifically:

1. Survey the framework's existing claims about sector structure
2. Identify candidate structural sources of decoupling within
   existing primitives
3. Set up the derivation target precisely (what counts as a proof)
4. List prior nulls relevant
5. Pick the most promising candidate to develop in Phase B

## Existing framework claims about sectors

The framework distinguishes:

| Sector | Anchor | Operating coupling | Klein structure | Stratification depth |
|---|---|---|---|---|
| Cosmological | H_0 | K = 1 (critical) | Z_2 component (orientation-reversing loop?) | depth 54 (R = 6·13⁵⁴) |
| Particle | v_EW | K_STAR ≈ 0.86 | Z_3 component (orientation-preserving loop?) | depth ~15 (suggested by `13⁻¹⁵`) |

These are EMPIRICAL associations from existing derivations,
not derived sector definitions. The framework HAS the two-sector
language but does not currently DERIVE it.

Specifically, the framework's existing derivations:

- `baryon_fraction.md`: cosmological partition uses Klein-singlet ∩
  coprime-to-6 = ψ_+(1,5); other modes are DM/DE
- `coupling_scales.md`, `down_type_double_cover_closed.md`: particle
  sector uses Klein-antipodal Z_2 rep on Z_2 × Z_3 = Z_6 for
  fermion mass ratios
- `continuum_limits.md`: cosmological at K=1 → Einstein equations;
  particle at K<1 (subcritical) → Schrödinger equation

These are at the SAME Klein lattice (Z_6) but at DIFFERENT K's
and DIFFERENT mode-coupling readings.

## Candidate structural sources of decoupling

Six candidates from existing framework primitives:

### Candidate D.1 — Klein bottle's two fundamental loops

The Klein bottle has π_1(K²) = ⟨a, b | abab⁻¹ = 1⟩. Two generators:
- a: orientation-preserving loop
- b: orientation-reversing loop

Hypothesis: cosmological sector lives on a-loop (or quotient by
a), particle on b-loop. Decoupling forced by π_1's relation
abab⁻¹ = 1, which makes them not commute.

**Plausibility**: high — Klein bottle has exactly two generators,
matching exactly two anchors. **Forcing**: needs a derivation
that the two generators carry different sectors structurally,
not by convention. Existing `klein_bottle_derivation.md` and
`klein_connection.md` are the natural starting points.

**Risk**: assigning sectors to generators may itself be a
convention. Could just relabel.

### Candidate D.2 — q_2 vs q_3 sector split

Z_6 = Z_{q_2 q_3} = Z_2 × Z_3 by CRT. Two prime factors.
- Hypothesis: cosmological uses Z_3 factor (q_3, 3 spatial dims);
  particle uses Z_2 factor (q_2, weak SU(2))
- Decoupling: factors are coprime → tensor product → independent

**Plausibility**: high — prime factorization is forced by
mass_sector_closure (q_2, q_3) = (2, 3). **Forcing**: needs
derivation that "Z_3 factor → cosmology" and "Z_2 factor →
particle" follows from substrate, not convention.

**Risk**: which prime → which sector might be convention.

### Candidate D.3 — K = 1 vs K < 1 regimes

Per `continuum_limits.md`, cosmological K=1 (critical) gives
Einstein; particle K<1 (subcritical) gives Schrödinger. Two
distinct regimes of the same dynamics.

**Plausibility**: very high — already in the framework as a
load-bearing fact. **Forcing**: K=1 vs K<1 are distinct
operating points of one substrate; need to show why each sector
is forced to its specific K.

**Risk**: K=1 / K<1 distinction is dynamics, not topology. Might
not give the clean structural decoupling required.

### Candidate D.4 — Spectral gap on the Stern-Brocot tree

The cosmological partition uses Farey level F_7 (depth 7). The
particle sector uses depth ~15. Different depths.

Hypothesis: a spectral gap between depth ranges forces decoupling.
Modes at low Farey depth (cosmological) and high Farey depth
(particle) don't talk to each other above some scale.

**Plausibility**: medium — depth is a natural Stern-Brocot
parameter. **Forcing**: needs a structural argument for why
specific depth ranges correspond to specific sectors.

**Risk**: depth assignment may itself be convention.

### Candidate D.5 — Anomaly cancellation forces sector separation

The framework's gauge-anomaly cancellation requires specific charge
combinations. Anomaly-cancellation between sectors (cosmological vs
particle) might force them to be distinct.

**Plausibility**: low for THIS question — anomaly cancellation
is usually within the gauge sector, not between sectors.
**Forcing**: would need a multi-sector anomaly that couldn't
cancel without sectoral separation.

**Risk**: speculative — no existing framework hint.

### Candidate D.6 — Topological K_eff = K_0/2 from Klein twist

`klein_topological_keff.py` showed `|r| ≡ 0` from Klein twist
gives `K_eff = K_0/2`. Hypothesis: this halving creates two
sub-K regimes (K_0 and K_eff = K_0/2) which become the two
sectors.

**Plausibility**: medium — uses already-derived Klein topological
finding. **Forcing**: K_0 vs K_0/2 split needs to map cleanly
onto cosmological vs particle.

**Risk**: K_0/2 already maps to "subcritical regime" not "particle
sector specifically."

## Ranking by Phase B feasibility

| Candidate | Plausibility | Existing framework support | Single-session Phase B feasibility |
|---|---|---|---|
| D.1 (Klein π_1 generators) | High | `klein_bottle_derivation.md`, `klein_connection.md` | Medium (multi-session likely) |
| D.2 (q_2 vs q_3 prime split) | High | `mass_sector_closure.md` | Medium |
| D.3 (K=1 vs K<1 regimes) | Very high | `continuum_limits.md` | Possible single-session |
| D.4 (spectral gap on SB tree) | Medium | Indirect | Multi-session |
| D.5 (anomaly between sectors) | Low | No existing hint | Speculative |
| D.6 (K_eff = K_0/2 split) | Medium | `klein_topological_keff.py` | Possible single-session |

**Top three candidates** for Phase B development:
- **D.3 (K=1 vs K<1)** — most existing support, possible single-
  session derivation
- **D.1 (Klein π_1 two generators)** — most natural structural
  source, multi-session
- **D.2 (q_2 vs q_3 prime split)** — second-most natural,
  multi-session

## Prior nulls relevant

From the cumulative null inventory:

- `path_a_walkthrough.md` — Klein-fold sub-action of canonical
  register cannot reach 15 = 3·5 via subgroup, stratification,
  or composed filter. **Constraint**: any sector-decoupling
  derivation must work without producing 5 in the substrate
  prime support directly.

- `epsilon_substrate_decomposition.md` N1-N8 — direct register
  cardinalities don't supply intermediate scales.
  **Constraint**: sector decoupling can't rely on intermediate
  registers; only the canonical ones (P-reg, H-reg).

- `continuity_in_K_nulls.md` N9-N16 — extending K=1 derivations
  to K<1 has structural failure modes (most importantly N11
  tongue coverage discontinuity). **Constraint**: D.3 must
  address N11 if it relies on continuous K-running between sectors.

- `omega_b_c5_beta_audit.md` and `klein_bridge_audit_and_probe.md`
  — multi-candidate ansatz pattern endemic. **Constraint**:
  Phase B derivation must produce UNIQUE forcing, not multi-
  candidate fits.

## Closure criterion (Phase B's task)

Phase B closes when:

1. **Specific candidate selected** (probably D.1, D.2, or D.3)
2. **Derivation chain constructed** from selected substrate
   structure to "two sectors are structurally distinct"
3. **Each step passes Z1-Z3** of `statistical_conventions.md`
4. **Cross-checked against prior nulls** (no contradiction)
5. **Verdict**: forcing argument constructed (Class 5 / Survives)
   OR specific obstruction identified (Class 2 / Class 4 with
   diagnostic)

If forcing argument constructed: framework's two-anchor
structural status upgrades from "consistent with" to "forced by";
anchor obstruction #5 closes; Region D is the framework's
deepest derivation closure.

If specific obstruction identified: the obstruction itself is
informative (sharpens the open question further).

## What Phase A does NOT decide

- Which candidate (D.1/D.2/D.3) to develop in Phase B
- The full derivation chain
- Whether forcing argument exists at all (Phase B must construct
  or rule out)
- Multi-session pacing (probably 3-5 sessions per candidate)

These are Phase B decisions.

## Sequencing with Region C

Per the user's commitment: Region C first, Region D after.

Region C produces a binary verdict on the multi-candidate ansatz
pattern. The verdict informs Region D:

- **If Region C verdict is "cloud is signal"**: Region D should
  start with D.1 (Klein π_1) since the framework has more
  structural content than naive expectation, suggesting deeper
  derivations are available.

- **If Region C verdict is "cloud is noise"**: Region D should
  start with D.3 (K=1 vs K<1) since the framework is at
  quantitative completion and the goal becomes locking in the
  qualitative structural claim (sector decoupling).

- **If Region C verdict is "inconclusive"**: Region D should start
  with D.2 (q_2 vs q_3 prime split) as the most concrete
  derivation that doesn't depend on the cloud interpretation.

So Phase B for Region D becomes more pointed AFTER Region C
completes.

## Phase B trigger

Phase A is complete with this document. Phase B begins when:
- Region C completes and informs the candidate choice
- User commits to one of {D.1, D.2, D.3}
- OR a finding from elsewhere in the framework changes the scope

## Status

Phase A complete. Region D scope, candidates, prior nulls,
sequencing with Region C specified. Phase B (the actual sector-
decoupling derivation) deferred until Region C resolves and
candidate is chosen.

## Cross-references

- `anchor_count_audit.md` — obstruction #5 source
- `vocabulary_is_the_work_pattern.md` — Instance 6 (SM hierarchy)
  reframe that motivates this question
- `path_a_walkthrough.md` — positive evidence for two-anchor
  structural status (constrains derivation)
- `hierarchy_problem_translation.md` — parallel reframe context
- `klein_bottle_derivation.md`, `klein_connection.md` — D.1
  starting point
- `mass_sector_closure.md` — D.2 starting point
- `continuum_limits.md` — D.3 starting point
- `klein_topological_keff.py` — D.6 starting point
- `numerology_count_phase_a.md` — Region C Phase A; sequencing
  precursor
- `remaining_gap_shapes.md` Shape C — work-map context
- `statistical_conventions.md` — Z1-Z3 discipline
- `ansatz_audit_policy.md` — policy applied to Phase B
