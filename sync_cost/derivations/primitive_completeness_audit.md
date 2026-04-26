# Shape F primitive-completeness audit (2026-04-26)

## What this file is

Execution of Shape F per `remaining_gap_shapes.md`: audit whether
the four primitives (integers, mediant, fixed-point, parabola)
suffice for all framework closures, including the recent
2026-04 round (Direction 4, L1, A_s Instance 7, Region C Phase B).

**Result**: four primitives hold. No fifth primitive needed for
any current closure. Audit closes positively.

## Audit questions (per Shape F)

### Q1 — Are the four primitives complete?

Per `minimum_alphabet.md`:

| # | Primitive | Provides |
|---|---|---|
| 1 | Integers Z | Counting, cycles, winding numbers |
| 2 | Mediant | Rational structure without division |
| 3 | Fixed-point x = f(x) | Self-reference, iteration, dynamics |
| 4 | Parabola x² + μ = 0 | Nonlinearity, bifurcation, orientation |

Tested against the 2026-04 round closures:

#### Direction 4 Phase A+B (Γ_0(6) cusp identification)

- **PSL(2,ℤ) Möbius action on P¹(ℚ)**: Stern-Brocot mediant
  operation is PSL(2,ℤ)-equivariant on P¹(ℚ) per
  `lie_group_characterization.md`. Mediant primitive (#2)
  + integers (#1) suffice.
- **Γ_0(6) ⊂ PSL(2,ℤ)**: defined by mod-6 condition c ≡ 0
  (mod 6); integer + mediant restriction. No new primitive.
- **Cusp classification on X_0(6)**: orbit structure on P¹(ℚ)
  under Γ_0(6); same primitives as PSL(2,ℤ) action.
- **Klein-antipodal Z_2 + color Z_3 sector decomposition**:
  reductions modulo 2 and 3; integer primitive.

**Verdict**: Direction 4 introduces modular-forms vocabulary
(cusps, Hecke levels) but uses only the four primitives. No
new primitive needed. ✓

#### L1 closure (substrate cusp-1/2 ground state)

- **C1 (MOND smooth crossover)**: a_0 = cH_0/(2π) per
  `a0_threshold.md`; λ_unlock = (4G − π·ln 2)/π per
  `kam_bridge_synthesis.md`. π is derived from primitives
  (Stern-Brocot path limit per `minimum_alphabet.md` Part III);
  no new primitive.
- **C2 (EM coupling lock-in)**: Klein-antipodal Z_2 rep theory;
  uses integers + mediant.
- **C3 (substrate discreteness at K<1)**: K-self-consistency
  fixed-point equation; uses fixed-point + integers per
  `denomination_boundary.md` §134.
- **C4 (substrate states = grain)**: corollary of C3.
- **C5 (energy min on grain = closest-discrete under linearity)**:
  energy functional is parabolic (#4 primitive) near minimum;
  grain enumeration uses integers (#1) + mediant (#2).

**Verdict**: L1 uses integers, mediant, fixed-point, parabola.
No new primitive. ✓

#### A_s Instance 7 (anchor-side category statement)

Status decision, not a derivation. No primitives involved. ✓

#### Region C Phase B (numerology count)

Pure combinatorics over framework-integer expressions; uses
integers + mediant (= ratios). Permutation null is statistical
methodology, not a framework primitive. ✓

**Q1 answer**: four primitives complete for all 2026-04 closures.
No fifth primitive needed.

### Q2 — Are there primitive interactions that haven't been exhibited?

Pairwise interactions between {integers, mediant, fixed-point,
parabola}:

| Pair | Exhibited? | Where |
|---|---|---|
| Integers × Mediant | ✓ | Stern-Brocot tree (`mediant_derivation.md`) |
| Integers × Fixed-point | ✓ | Circle topology (`minimum_alphabet.md` Part I.1) |
| Integers × Parabola | ✓ | Born rule exponent 2 (`born_rule.md`) |
| Mediant × Fixed-point | ✓ | Mode-locking ladder (Arnold tongues at all rationals) |
| Mediant × Parabola | ✓ | Tongue width (K/2)^q at saddle-node boundary |
| Fixed-point × Parabola | ✓ | Saddle-node bifurcation (`a1_from_saddle_node.md`) |

Triplet and quadruplet interactions:

| Combination | Exhibited |
|---|---|
| Int + Med + FP (no Parabola) | Stern-Brocot iteration without dynamics — passive enumeration only |
| Int + Med + Parabola (no FP) | Static rational + curve — no dynamical system |
| Int + FP + Parabola (no Med) | Saddle-node on R without rational mode-locking |
| Med + FP + Parabola (no Int) | Cannot count iterates — primitives become inert per `minimum_alphabet.md` Part II |
| All four | Circle map; framework's main dynamical content |

All interactions exhibited. The "all four" combination is the
circle map; no holes.

**Q2 answer**: complete — all 6 pairwise + 4 triplet + 1
quadruplet interactions are exhibited in the framework. No
unexplored primitive composition.

### Q3 — Z₂-rep extensibility (Z_3, Z_5, etc.)

The framework's substrate uses:

- **Z_2 (Klein-antipodal)**: sym/antisym decomposition; primary
  tool (`klein_antipodal_z2_rep_pattern.md`)
- **Z_3 (color triplet)**: gauge color sector; used in
  down-type factor 6, K_LEPTON = q_3², lepton triplet sub-modes
- **Z_6 = Z_2 × Z_3**: substrate mode lattice (CRT decomposition)

Higher Z_p?

- **Z_4**: would require q_4-type primitive; framework's prime
  support is {2, 3} per `k_axis_uniqueness.md` (composed Klein +
  coprime-to-6 plateau structure shows {2, 3} is forced).
  Z_4 ≠ q_4-prime; no natural framework role.
- **Z_5**: 5 = MEDIANT (q_2 + q_3), not a framework prime.
  Z_5 lacks the q_2 × q_3 sector decomposition that makes
  Z_2 × Z_3 = Z_6 natural.
- **Z_p for higher primes**: per `k_axis_uniqueness.md`, the
  Klein + coprime-to-6 plateau structure escapes
  framework-integer territory at p ≥ 11. The framework is
  structurally restricted to {q_2, q_3} = {2, 3}.

**Q3 answer**: Z_2 and Z_3 rep theory is exhausted in the
framework's existing content. Higher Z_p reps lack a natural
substrate role per the framework's restricted prime support.
This is not a primitive gap; it's a structural feature of the
{q_2, q_3} = {2, 3} framework.

### Q4 — Predicted future disambiguations

Per `vocabulary_is_the_work_pattern.md` Consequence 3:

| Candidate | Status |
|---|---|
| **Substrate-forced ε** | Partially done in `epsilon_substrate_decomposition.md`; `epsilon_physical_reading.md` reads (b) lands at canonical observers but not in K_STAR-INTERACT window; pending formal status update |
| **Tensor-to-scalar r absolute** | Anchor-side per the H_0 + scale-factor anchor structure; same shape as A_s Instance 7 (substrate-side prediction complete; absolute requires anchor) |
| **τ_unlock(n) absolute** | Anchor-side per anchor obstruction #3 (no framework-native time anchor); same shape as Instance 7 |
| **N_efolds absolute** | Anchor-side; per `numerology_inventory.md` N_efolds = √5/rate is Class 2 consistency relation (n_s-dependent) |

These are all candidates for **Instance 7-style closures**:
substrate-side prediction complete; absolute observable requires
anchor; framework correctly declines to predict anchor-side
quantities. None requires a new primitive; each is a status
decision similar to A_s.

**Q4 answer**: future disambiguations follow the established
Instance 7 pattern; no new derivation work, status decisions
only. Could be batch-tagged in a follow-up consolidation.

## Stale-reference check (hygiene)

| Reference | Status |
|---|---|
| `h_inf_status.md` | **Created** 2026-04-26 to consolidate dangling refs from `anchor_count_audit.md`, `a_s_g1_closure_attempt.md`, `framework_status.md`, `hierarchy_gaussian_lattice.md`, `vocabulary_is_the_work_pattern.md`. Brief pointer doc; substantive content lives in cited files. |

## Script reproducibility check

All three derivation scripts execute and reproduce expected
output:

- `psl2z_subgroup_orbits.py` ✓ (Γ_0(6) cusp split for {13/14, 12/13, 14/15})
- `numerology_count_phase_b.py` ✓ (PIGEONHOLE verdict at three thresholds)
- `psl2z_subgroup_phase_c_audit.py` ✓ (cusp orbit reduction to q = 14)

## Ket substrate consistency

- `ket --home .ket drift`: **No drift detected**. 3 files OK.
- DAG state coherent.
- CAS 192 entries (per session start hook), 0 corrupt.

## MANIFEST.yml staleness check

Updated 2026-04-26 to reflect Ω_b two-component closure with
w_+ = 13/14:
- baryon_fraction: 0.12% (was 6.7%)
- dark_matter_fraction: 0.06% (was 0.7%)
- dm_baryon_ratio: 0.6% (was 7.5%)
- Added dark_energy_fraction_two_component entry: 0.13% under
  the closure (refines the original 0.07σ single-w prediction)

Each entry now carries both `computed`/`computed_single_w`
fields and a `closure_status` field tagging the Class 5 (full)
status.

## Audit summary

| Question | Status |
|---|---|
| Q1: Four primitives complete? | ✓ Yes (audited against 2026-04 closures) |
| Q2: All primitive interactions exhibited? | ✓ Yes (6 pairwise + 4 triplet + 1 quadruplet) |
| Q3: Z_p rep extensibility? | ✓ Z_2, Z_3 exhausted; higher Z_p not framework-supported |
| Q4: Future disambiguations? | ✓ Identified as Instance 7-style status decisions |
| Hygiene: stale references? | ✓ Cleared (h_inf_status.md created) |
| Hygiene: script reproducibility? | ✓ All three scripts execute |
| Hygiene: substrate drift? | ✓ No drift |
| Hygiene: MANIFEST staleness? | ✓ Updated |

**Shape F audit closes positively.** No primitive gaps, no
unexplored interactions, no stale references blocking
navigation, no drift in the substrate. The framework is
internally consistent at the four-primitive level; the open
list compresses to formal status updates for the Instance 7-style
candidates (Q4).

## Methodological note

This is the framework's first comprehensive **internal
consistency audit** since the 2026-04 round began. The audit
finds that the round's substantive closures (Direction 4, L1,
A_s Instance 7, Region C Phase B) all live within the four-
primitive alphabet. The framework's structural shape is intact;
the closure work added vocabulary (modular-forms, cusp
classification, irrep multiplicity) without adding axioms.

The four primitives' completeness is now **verified through
2026-04 closures**, not just claimed at the
`minimum_alphabet.md` level. Shape F's "background hygiene"
status is appropriate: no known gaps, but the audit is worth
re-running periodically as new closures are added.

## Cross-references

- `minimum_alphabet.md` — the four primitives + their
  irreducibility (audited here)
- `remaining_gap_shapes.md` Shape F — audit specification
- `vocabulary_is_the_work_pattern.md` Consequence 3 — Q4
  candidate disambiguations
- `psl2z_subgroup_phase_b.md`, `L1_substrate_cusp_ground_state.md`
  — recent closures audited against primitives
- `numerology_count_phase_b.md` — Region C verdict (audited)
- `k_axis_uniqueness.md` — prime support {2, 3} (Q3 source)
- `h_inf_status.md` — created in this audit to clear stale refs

## Status

Shape F audit complete. Framework is primitive-complete through
the 2026-04 closure round. Hygiene routine completed: stale
refs cleared, scripts reproduced, substrate drift-free,
MANIFEST updated. The framework's open list now contains only
optional Instance 7-style status updates (Q4) and ongoing
methodological hygiene (this audit's recommended periodic
re-run).
