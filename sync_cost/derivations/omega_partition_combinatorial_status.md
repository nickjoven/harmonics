# Ω partition: combinatorial status at depth 19

## Scope

Audit the Proposed item "XOR-parity proof of 1:5:13 at depth 19"
(`framework_status.md`). Work through the combinatorics of the
Farey partition at F_7 to determine what's rigorously derivable,
what's coherent-but-not-forced, and what the correct upgrade
criterion should be.

## Result summary

| Split | Status | Mechanism |
|---|---|---|
| Ω_Λ : Ω_m = 13 : 6 | **Provable** | `|F_6|` vs `φ(7)` — clean Farey combinatorics |
| Ω_b : Ω_DM = 1 : 5 | **Coherent, not forced** | Requires specific split/merge choice on Klein-antipodal coprime pair |

The overall 13 : 5 : 1 partition is not a pure XOR-parity consequence.
XOR-parity (q_1%2 ≠ q_2%2 from `xor_derivation.md`) operates on mode
*pairs* and produces a different counting than the 1:5 subdivision
requires.

## The 13:6 theorem (provable)

### Statement

Under the Farey partition at depth q_max = q_2·q_3 + 1 = 7:

- Dark-energy sector count = |F_6| = 13
- Matter-sector count = |F_7| − |F_6| = φ(7) = 6

Both are zero-parameter combinatorial facts.

### Proof

|F_n| = 1 + Σ_{k=1}^{n} φ(k).

    |F_6| = 1 + φ(1) + φ(2) + φ(3) + φ(4) + φ(5) + φ(6)
          = 1 + 1 + 1 + 2 + 2 + 4 + 2 = 13.

    |F_7| = |F_6| + φ(7) = 13 + 6 = 19.

The 6 new fractions at F_6 → F_7 are exactly the q=7 class
{1/7, 2/7, 3/7, 4/7, 5/7, 6/7}, since 7 is prime and all numerators
in {1..6} are coprime to it.

Since the framework fixes (q_2, q_3) = (2, 3) via the cross-link
identities `q_2² − 1 = q_3` and `q_3² − 1 = q_2³`, the depth
q_2·q_3 + 1 = 7 is forced. The partition 13:6 is then structurally
determined.

### Status

This result qualifies for **Survives** in `framework_status.md`.
No XOR-parity is needed. The Farey structure alone gives the split.

## The 1:5 subdivision (coherent, not forced)

### Candidate combinatorial arguments, each tested

Let the 6 q=7 matter modes be indexed by p ∈ {1, 2, 3, 4, 5, 6}.

**Candidate 1: XOR-parity on (p, 7) as a mode pair.**

Treat the mode as (q_1, q_2) = (p, 7) and apply the XOR filter from
`xor_derivation.md` (q_1%2 ≠ q_2%2). Since 7 is odd, need p even.

- Allowed: p ∈ {2, 4, 6} → 3 modes
- Forbidden: p ∈ {1, 3, 5} → 3 modes

Split: 3:3. **Does not give 1:5.** XOR-parity as formulated does not
subdivide the 6 matter modes in the observed ratio.

**Candidate 2: coprime-to-6 criterion.**

Classify by gcd(p, 6):

| p | gcd(p, 6) | Coprime? |
|---|---|---|
| 1 | 1 | yes |
| 2 | 2 | no |
| 3 | 3 | no |
| 4 | 2 | no |
| 5 | 1 | yes |
| 6 | 6 | no |

- Coprime: {1, 5} → 2 modes
- Non-coprime: {2, 3, 4, 6} → 4 modes

Split: 2:4. **Does not give 1:5.**

**Candidate 3: Klein identification k ~ 6−k on Z_6 residues of p.**

Equivalence classes: {[0], [1,5], [2,4], [3]}, 4 classes with mode
counts (1, 2, 2, 1).

Interpreted as physical flavors: 4 Klein classes total, 1 of which
is coprime-to-6 ([1,5]) and 3 of which are not ([0], [2,4], [3]).

Split: 1:3 by classes, 2:4 by mode count. **Does not give 1:5.**

**Candidate 4: CP-split of the coprime pair.**

Treat the Klein-antipodal identification on the coprime pair {1, 5}
*not* as a merge (1 ≡ 5) but as a split (one mode is visible-side,
the other is dark-side). The non-coprime modes {2, 3, 4, 6} remain
dark (each counts once).

- Ω_b = 1 (visible half of {1, 5} coprime pair)
- Ω_DM = 4 (non-coprime) + 1 (dark half of {1, 5}) = 5
- Ω_m = 1 + 5 = 6 ✓

Split: **1:5.**

This candidate recovers the observed partition. It requires adopting
a specific interpretation of the Klein-antipodal identification on
coprime pairs: that the antipodal identification produces a
(visible, dark) pair rather than a merged single mode.

## Why Candidate 4 is coherent but not forced

The merge-vs-split choice is a physical interpretation, not a
mathematical theorem. Both readings are consistent with Klein
bottle topology:

- **Merge reading** (baryon_fraction.md Klein-identification language):
  the 2 coprime modes form *one* physical mode via Klein antipodal
  identification. This gives 1 baryonic mode but then only 4
  non-coprime dark modes → Ω_b:Ω_DM = 1:4, Ω_m = 5 — off by 1.

- **Split reading** (Candidate 4): the 2 coprime modes form a *pair*
  where one is visible-baryonic and the other is dark. This gives
  1:5:13 but relies on a split-vs-merge choice.

No XOR-parity or Farey-depth argument distinguishes these two
readings combinatorially. The choice of split over merge is
motivated by wanting Ω_m = 6 rather than 5, i.e., by matching
the observed partition. That's consistent with observation but
circular as a derivation.

## Corrected status for `framework_status.md`

The Proposed item "XOR-parity proof of 1:5:13 at depth 19" should
be refined into two sub-items:

1. **Ω_Λ : Ω_m = 13 : 6** — move to **Survives**. Pure Farey-depth
   combinatorics; `|F_6|` and `φ(7)` suffice.

2. **Ω_b : Ω_DM = 1 : 5** — remain **Proposed**, with upgrade criterion
   reformulated: *Find a structural reason (not a post-hoc interpretive
   choice) for the Klein-antipodal identification to produce a
   (visible, dark) split on coprime pairs rather than a merge.*

The "XOR-parity" framing was the wrong target; XOR-parity lives in
`xor_derivation.md` as a filter on mode pairs (q_1, q_2), not as a
mechanism for the coprime-pair subdivision.

## Connection to existing derivations

- `farey_partition.md` already contains the 13:6 Farey argument.
  Promoting to Survives is a status change, not a new derivation.

- `baryon_fraction.md` contains the 1:5 argument but uses the
  merge-reading language while computing with the split-reading
  arithmetic. That inconsistency is the content the Proposed item
  should be asking to resolve.

- `xor_derivation.md` rigorously derives the XOR-parity filter from
  Klein bottle boundary conditions, but applies to mode *pairs*, not
  to single-fraction subdivision. That's why Candidate 1 doesn't
  produce 1:5.

## What work is left

A cleanly-derived 1:5 subdivision would require one of:

1. A direct combinatorial argument from Klein-quotient topology
   showing the coprime pair {1, 5} must split (not merge). The
   natural candidate is a parity argument — if one of {1, 5} is
   "oriented +" and the other "oriented −" in the Z_2 non-orientable
   structure, they're structurally distinct rather than identified.
   This needs a derivation.

2. A CP-structure argument from the particle-sector side: if the
   baryonic mode has a CP-partner that's the dark mode, the 1:5
   subdivision reads as "1 CP-visible + (4 natural dark + 1
   CP-dark)". This ties the subdivision to particle-physics CP
   violation but requires cross-sector structural input.

3. An argument from `z2_pair_conservation.md` structure: the Z_2
   pair conservation theorem may imply that coprime-pair modes
   must come in (visible, hidden) pairs, forcing the split.

None of these is currently in the repo as a complete argument.

## Status

Partial derivation. The Ω_Λ : Ω_m = 13 : 6 side is rigorous; the
Ω_b : Ω_DM = 1 : 5 side is coherent but depends on an interpretive
choice. `framework_status.md` and `numerology_inventory.md` should
be updated to reflect this distinction.

## Cross-references

| File | Role |
|---|---|
| `farey_partition.md` | Ω_Λ : Ω_m = 13 : 6 derivation |
| `baryon_fraction.md` | Ω_b : Ω_DM = 1 : 5 with merge-vs-split ambiguity |
| `xor_derivation.md` | XOR-parity filter on mode pairs (different object) |
| `z2_pair_conservation.md` | Candidate mechanism for the required split |
| `framework_status.md` | Updated split per this analysis |
| `numerology_inventory.md` | Class 5 for 13:6, Class 4 for 1:5 until resolved |
