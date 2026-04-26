# PSL(2,ℤ)-subgroup identification — Phase A

## What this file is

Phase A planning for **Direction 4** identified in
`cross_ratio_irrep_reframe.md`: identify which PSL(2,ℤ)-subgroup
the framework's substrate dynamics preserve, so that the irrep
decomposition selects ONE of the cross-ratio candidates (13/14,
12/13, 14/15) for w_+ as the framework's natural operating-point.

This is **structural derivation work**, not ansatz audit. The
multi-candidate Class 2 demotion of w_+ persists at the irrep
level: each candidate is a distinct PSL(2,ℤ) orbit. Forcing
requires identifying the subgroup whose invariant content singles
out one orbit as carried by the framework's dynamics.

## The setup

PSL(2,ℤ) acts on P¹(ℚ) by Möbius transformations. Subgroups
restrict the action; their invariants split orbits differently.

The full PSL(2,ℤ) action gives the Farey-graph automorphism
(per `lie_group_characterization.md` Step 3). Cross-ratios of
Farey 4-tuples are invariants. The three w_+ candidates label
distinct orbits with j-invariants 47364.23, 40708.93, 54531.66.

A subgroup G ⊂ PSL(2,ℤ) splits each PSL(2,ℤ) orbit into G-orbits.
The framework's substrate, if it preserves only G (not the full
PSL(2,ℤ)), would carry one specific G-orbit as its natural
operating-point cross-ratio. Identifying G ≡ identifying which
candidate.

## Candidate subgroups

| Subgroup | Index | What it preserves | Why framework-relevant |
|---|---|---|---|
| **Klein-antipodal Z_2** | ∞ (not finite-index) | {x, −1/x} pairs | Already in framework (sym/antisym decomposition) |
| **Γ(2)** principal congruence level 2 | 6 | mod-2 structure of (a,b,c,d) | Famously the "anharmonic group's quotient" |
| **Γ_0(N)** Hecke congruence | depends | upper-triangular mod N | Modular forms / Hecke operators, level structure |
| **Γ_0(2)** | 3 | mod-2 lower-left zero | Smallest non-trivial Hecke; q_2 connection |
| **Γ_0(3)** | 4 | mod-3 lower-left zero | q_3 connection |
| **Γ_0(6)** | 12 | mod-6 lower-left zero | q_2·q_3 = INTERACT connection |
| **Γ_1(N)** | depends | unipotent mod N | Cusp structure |

The framework already uses Klein-antipodal Z_2 (`klein_antipodal_z2_rep_pattern.md`)
but Z_2 is insufficient: 13/14 and 12/13 are both Klein-antipodal-invariant
(per `cross_ratio_irrep_reframe.md`). A larger subgroup is needed
to split them.

The framework's natural integer scaffolding (q_2 = 2, q_3 = 3,
INTERACT = 6) suggests Γ_0(2), Γ_0(3), or Γ_0(6) as natural
candidates: each Hecke-level matches a framework primitive.

## Phase A deliverables

Phase A is **machinery setup + orbit enumeration**, not closure.

### A1. Enumerate orbits of each candidate subgroup

For each of {Γ(2), Γ_0(2), Γ_0(3), Γ_0(6)}:
- Compute orbits of {13/14, 12/13, 14/15} under the subgroup
- Identify which subgroup splits the three candidates into
  distinct orbits (necessary for the subgroup to "select")
- Identify which subgroup keeps them in distinct orbits (already
  known true for full PSL(2,ℤ)); this is automatic

### A2. Match subgroup signature to framework primitives

For each candidate subgroup that splits the three candidates:
- Identify which framework primitive (q_2, q_3, INTERACT, K_LEPTON,
  MEDIANT, etc.) the subgroup's level corresponds to
- Check if existing framework derivations (`baryon_fraction.md`,
  `partition_logit_form.md`, `klein_antipodal_z2_rep_pattern.md`)
  use the same level structure

The hypothesis: the subgroup whose level matches the framework's
existing partition structure (e.g., Γ_0(6) for the q_2·q_3 = 6
factor that appears uniformly in `partition_logit_form.md`) is
the candidate for the substrate's preserved subgroup.

### A3. Identify the substrate-side argument shape

What kind of derivation would force "framework substrate preserves
subgroup G"? Possibilities:

1. **Mode-counting**: the substrate's eigenmode decomposition
   has a specific G-equivariance built in (parallel to how
   sign-rep no-EM forced w_- = 1)
2. **Conserved-quantity argument**: G is the stabilizer of some
   physical conserved quantity (charge, monodromy class, etc.)
3. **Dynamics-preservation**: the substrate's coupling/propagation
   has a manifest G-symmetry

The Klein-antipodal Z_2 = sym/antisym distinction is example (1).
The framework needs the analogous derivation at a higher
G ⊂ PSL(2,ℤ).

## Phase A non-goals

- Phase A does NOT close w_+. Closure requires both subgroup
  identification (A1+A2) and forcing argument (A3 fully derived,
  not just shape-identified)
- Phase A does NOT change Class 2 status of w_+. The closure
  status updates only after the multi-session work completes
- Phase A is preparation, not derivation

## Resources to draw on

- `lie_group_characterization.md` Step 3 — PSL(2,ℤ) Farey
  cross-ratio invariance baseline
- `klein_antipodal_z2_rep_pattern.md` — current Z_2 ⊂ PSL(2,ℤ)
  framework usage, the "subgroup-of-PSL(2,ℤ)" derivation pattern
  to extend
- `partition_logit_form.md` — q_2 × (q_3-sector) factorization;
  if Γ_0(6) is the answer, the logit form's universal q_2 factor
  acquires Hecke-level interpretation
- `cross_ratio_irrep_reframe.md` — the orbits and j-invariants
  established
- `omega_b_w_plus_cross_ratio_search.md` — 24 framework 4-tuples
  giving 13/14; their orbit structure under G ⊂ PSL(2,ℤ) might
  also constrain G

## Phase A execution sketch

This is queued, not yet executed. Recognize-mode probe with
cross-ratio probe-style structure:

1. Compute Γ_0(N) coset representatives for N ∈ {2, 3, 6}
2. Apply cosets to {13/14, 12/13, 14/15}; record orbit splittings
3. Cross-reference with framework primitives to identify the
   "natural" G
4. If a clear winner emerges (one G whose orbits cleanly select
   one candidate AND matches a framework primitive), document
   as Phase A finding
5. If multiple G's are candidates: this is Phase A's deliverable
   (the candidate G shortlist for Phase B forcing-argument
   derivation)

## Phase B (sketch, not for this file)

Phase B is the actual derivation: given the Phase A shortlist,
derive WHY the framework's substrate dynamics preserve G
specifically. Phase B is multi-session structural work; not
recognizable in a single probe.

## Cross-references

- `cross_ratio_irrep_reframe.md` — the reframe identifying this
  direction
- `lie_group_characterization.md` — PSL(2,ℤ) machinery
- `klein_antipodal_z2_rep_pattern.md` — current subgroup usage
- `omega_b_w_plus_cross_ratio_search.md` — cross-ratio search
- `partition_logit_form.md` — q_2 × q_3-sector factorization
- `numerology_count_phase_a.md` — Region C (sharpened by irrep
  null distribution per the reframe)

## Status

Phase A planning document. Direction 4 queued as multi-session
structural work. The four candidate subgroups (Γ(2), Γ_0(2),
Γ_0(3), Γ_0(6)) identified; Γ_0(6) flagged as suggestive given
the framework's q_2·q_3 = 6 = INTERACT structure.

Phase A execution (orbit enumeration + matching) not yet performed.
This document is the queue entry; A1-A3 deliverables defined.
