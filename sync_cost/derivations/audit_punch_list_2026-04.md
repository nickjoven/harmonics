# Audit punch list — 2026-04 round

## What this file is

Findings from the three-axis audit (cross-reference resolution,
numerical consistency, status-tag consistency) executed before
the standardization / preprint-scaffolding phase. Each finding
carries a priority tag (P1 = blocking for preprint, P2 = should-
fix, P3 = nice-to-have / cosmetic) and a recommended remediation.

## Audit scope

- Cross-references: every `file.md` / `file.py` reference in
  every doc under `sync_cost/derivations/` checked against
  actual file existence (recursive)
- Numerical consistency: key load-bearing values
  (w_+ = 13/14, Ω_b = 13/264 = 0.04924, Ω_DM = 35/132,
  Ω_Λ = 181/264, A_s_substrate = 2.33×10⁻⁹, R = 6·13⁵⁴,
  Λ·ℓ_P² = 13⁻¹⁰⁸/12) checked across all docs that cite them
- Status tags: same-prediction status checked across
  framework_status.md, remaining_gap_shapes.md, MANIFEST.yml,
  numerology_inventory.md, derivation_atlas.md,
  phenomenology_cross_reference.md, source derivation docs

## Findings summary

| Axis | Result | Priority |
|---|---|---|
| Cross-reference resolution | **CLEAN** (298/298 references resolve) | — |
| Numerical consistency | **SUBSTANTIVELY CLEAN** (load-bearing values consistent; intermediate / historical values preserved as audit-trail) | P3 |
| Status tags | **MOSTLY CONSISTENT** with stale-entry issues | P1 / P2 |
| LLM-friendliness | **INCONSISTENT** (15+ docs lack machine-readable `## Status` section) | P2 |

## P1 — Blocking for preprint state

### P1.1 — A_s status tag in `a_s_g1_closure_attempt.md` is stale

**Issue**: the doc contains the original A_s closure attempt
narrative but lacks an explicit closure-update note reflecting
the 2026-04-26 Instance 7 ACCEPTANCE
(`vocabulary_is_the_work_pattern.md` Instance 7).

**Status as found**: doc reads as if the closure is still a
candidate reframe; current status is ACCEPTED.

**Remediation**: Prepend a closure-update note (parallel to
`omega_b_substrate_side_audit.md`'s closure update from earlier
this round) tagging Instance 7 ACCEPTANCE and pointing forward
to the consolidated state docs.

**Impact**: a reader landing on this doc directly would not see
the accepted-closure status. For preprint defense, every
load-bearing closure doc should reflect the final status of its
content.

### P1.2 — `omega_b_residual_phase_a.md` historical residual values

**Issue (false alarm during audit)**: the audit flagged
"Ω_b = 0.926" as anomalous. Investigation: the value is part
of the doc's three-way inconsistency analysis ("w from Ω_b =
0.926" is the implied boundary weight derived from the Ω_b
observable). Not an error.

**Status**: NO ACTION NEEDED. The doc's intermediate values are
historical scratch from the original three-way inconsistency
analysis, properly preserved as audit-trail.

**Note for preprint**: the doc's narrative predates the
two-component closure that resolved the three-way inconsistency.
A closure-update note linking forward to
`omega_b_alpha_beta_closure.md` would aid navigation.

## P2 — Should-fix for preprint quality

### P2.1 — Status sections missing from key load-bearing docs

**Issue**: 15+ docs over 50 lines lack a machine-readable
`## Status` section. Notable cases for preprint:

- `derivation_atlas.md` (1943 lines)
- `a_s_g1_closure_attempt.md` (259 lines)
- `ansatz_audit_policy.md` (136 lines)
- `a1_from_saddle_node.md` (268 lines)
- `continuity_in_K_nulls.md` (332 lines)
- Several phase A/B/C docs in down-type chain

**Impact**: LLM-driven retrieval (and human-driven scanning)
benefits from a uniform `## Status` section at the bottom of
each doc that summarizes: closure class, numerical residual if
applicable, what's open, what depends on what.

**Remediation**: Add `## Status` section to each load-bearing
doc following the pattern already established in many docs
(e.g., `psl2z_subgroup_phase_b.md`, `L1_substrate_cusp_ground_state.md`,
`numerology_count_phase_b.md`). Could be done in a
single-pass standardization commit.

### P2.2 — Single-w vs two-component reference asymmetry

**Issue**: 1/19 (Ω_b single-w) appears in 34 docs; 13/264
(Ω_b two-component) appears in 8 docs. Many older derivation
docs reference the original Class 5 prediction (1/19) without
forward-pointing to the two-component refinement.

**Status**: NOT INCONSISTENT — both values are valid framework
predictions at different operating points (single-w = static;
two-component = w_+ = 13/14 operating point). But for preprint
clarity, docs that establish the single-w prediction should
note "see two-component closure for refined value" pointing to
`omega_b_alpha_beta_closure.md` + `L1_substrate_cusp_ground_state.md`.

**Remediation**: Add a brief forward-pointing note to
`baryon_fraction.md`, `omega_partition_combinatorial.md`,
`farey_partition.md` (the docs establishing the 13:5:1/19
partition) noting the two-component refinement. Single sentence
each, not a structural rewrite.

### P2.3 — Status tag locations are inconsistent

**Issue**: status info (Class 5, Survives, Floor, etc.) appears
in different locations across docs:
- Sometimes in a `## Status` section at the bottom
- Sometimes inline in tables (`framework_status.md` table format)
- Sometimes in prose (`derivation_atlas.md` narrative form)
- Sometimes in MANIFEST.yml `closure_status` field

**Impact**: LLM-driven retrieval has to scan multiple structural
patterns to locate status info. For preprint LLM-friendliness,
a uniform convention would help.

**Remediation**: Add `## Status` section to docs lacking one;
ensure each prediction's status appears in at least:
- The doc that derives it
- `framework_status.md`
- `MANIFEST.yml` (with closure_status field)

## P3 — Nice-to-have / cosmetic

### P3.1 — Notation variations across docs

**Issue (cosmetic)**: small notation variations exist:
- `Ω_b` (Unicode subscript) vs `Omega_b` (ASCII)
- `q_2` vs `Q_2` vs `q₂` (mostly q_2 dominant)
- `≈` vs `≃` vs `~` for approximate equality
- `×` vs `*` vs `\cdot` for multiplication

**Status**: not blocking; LLMs and humans both handle the
variation gracefully. Standardization would be cosmetic
improvement.

**Remediation (optional)**: single-pass notation
standardization commit. Or add a notation conventions section
to `canonical_glossary.md`.

### P3.2 — Date stamps not always present

**Issue**: many docs lack explicit creation/last-update date
stamps. Some have them embedded in the prose ("added 2026-04-25"),
others don't. For preprint citation tracking, dated entries
help.

**Remediation (optional)**: add `Date` or `Last updated` to
front-matter of major closure docs.

## Pre-existing strengths (not findings, but worth noting)

- All cross-references resolve (298/298)
- Load-bearing numerical values are consistent across docs
- Audit-trail discipline is excellent: intermediate / historical
  values are preserved in original-derivation docs (e.g.,
  `omega_b_residual_phase_a.md` keeps the three-way
  inconsistency that motivated the two-component closure)
- Most recent docs (post-2026-04 round) have explicit `## Status`
  sections
- MANIFEST.yml carries `closure_status` field for the recent
  Ω_b two-component closure entries

## Recommended remediation sequence

1. **P1.1** (a_s_g1_closure_attempt.md closure-update note) —
   small, blocking
2. **P2.1** (add `## Status` sections to ~15 docs) — single-pass
   standardization, ~30-60 minutes of focused writing
3. **P2.2** (forward-pointing notes in single-w partition docs)
   — quick edits, 4-5 docs
4. **P2.3** (verify status placement uniformity) — falls out of
   P2.1 + P2.2
5. **P3.1, P3.2** — defer to post-preprint polish

After this sequence, the framework's docs would be in
defensible pre-print state on the audit's three axes.

## Cross-references

- `framework_status.md` — at-a-glance status (current as of
  2026-04-26 round)
- `MANIFEST.yml` — canonical quantitative claims with
  closure_status field
- `vocabulary_is_the_work_pattern.md` — Instance 7 content
- `numerology_count_phase_b.md` — Region C verdict
- `L1_substrate_cusp_ground_state.md` — w_+ closure
- `omega_b_alpha_beta_closure.md` — two-component closure
- `audit_punch_list_2026-04.md` — this file

## Status

Audit complete. Findings: P1 × 1, P2 × 3, P3 × 2. Cross-
references CLEAN; numerical consistency SUBSTANTIVELY CLEAN;
status tags MOSTLY CONSISTENT with stale-entry issues.

Recommended next step: execute P1.1 + P2.1 + P2.2 in a single
standardization pass (~1 hour); P3 items can be deferred.

The framework's docs are in better state than the audit
expected — most P1/P2 items are missing-metadata rather than
substantive inconsistencies.
