# Down-type double cover — Phase B follow-up: Route 1 null result

Script: `down_type_stabilizer_scan.py`.

## What was tested

Phase B Attempt 5 reached the target factor 6 by positing that
lepton orbits are Z_6-stabilized and down-type orbits have trivial
stabilizer. Route 1 proposed validating this by acting the six
elements of Z_6 = Z_2 × Z_3 on the four XOR modes `{A, B, C, D}`
from `gap3_principal_bundle.py` and reading off the stabilizers.

The scan tested four candidate Z_6-actions:

1. Fiber translation (the principal-bundle action of `gap3_*`)
2. Deck-like action with negation on Z_3 slot
3. Walk holonomy subgroup, varying the reference mode
4. Z_6 as a permutation of `{A, B, C, D}`

## Findings

**Candidates 1 and 2.** The fiber action is free on each fiber,
so every mode has trivial stabilizer. Ratio = 1/1 = 1. Not 6.

**Candidate 3 (interesting).** Walk holonomies from each reference
have a structured pattern:

| sector     | Klein parity | subgroup orders by reference |
|---|---|---|
| lepton     | −1 | {6, 1, 1, 6} over refs A,B,C,D |
| up-type    | −1 | {1, 6, 6, 1} |
| down-type  | +1 | {2, 3, 3, 2} |

**This is a real structural pattern**: Klein-parity-(−1) sectors
always generate either the trivial subgroup or all of Z_6;
Klein-parity-(+1) sectors generate **only proper non-trivial
subgroups** (sizes 2 and 3 — the orders of Z_2 and Z_3). The
down-type walks are excluded from generating the full Z_6 by their
Klein parity.

But the ratio is still not 6:1, and the subgroup sizes depend on
the reference. A reference-free structural anchor is absent from
the Gap 3 / gauge-bundle data.

**Candidate 4.** The symmetric group `S_4` has no element of
order 6 (max order = 4 from 4-cycles). Z_6 does not embed in
`Sym(A, B, C, D)`. The base's natural symmetry is `V_4 = Z_2 × Z_2`
(slot-swap × per-slot conjugation p/q → (q−p)/q), order 4 not 6.

## Consequence: Phase A §6 methodological note was wrong

Phase A §6 suggested the factor `6 = q_2 q_3` comes from the
gauge-center `|Z_6|`, the same integer that appears in the
hierarchy coefficient `R = 6 × 13⁵⁴` via `|Z_6|` as the gauge
center order. The scan rules this out:

- The gauge-center `Z_6` acts freely on mode fibers (from Gap 3),
  so it cannot distinguish sectors by stabilizer size.
- The base modes `{A, B, C, D}` have symmetry group `V_4`, not `Z_6`.
- No reference-free Z_6-action on the base produces the required
  6:1 lepton/down-type split.

**The integer 6 in the hierarchy coefficient and the integer 6 in
the down-type factor are separate structural appearances, not one
unified fact.** Phase A's methodological hope for unification
fails the finite check.

## What the scan does suggest

Candidate 3's pattern — Klein-parity-(+1) walks generate only
**proper non-trivial subgroups** of Z_6 — is a real invariant.
The non-trivial proper subgroups of Z_6 have orders 2 and 3,
whose product is 6. This is suggestive but not a derivation:

> **Speculative reading.** The factor 6 = q_2 · q_3 might be the
> **product of the two non-trivial proper subgroup orders** of Z_6,
> attached to a Klein-parity-(+1) walk because such walks
> generate exactly those subgroups (from each reference). A
> Klein-parity-(−1) walk generates the trivial or full subgroup
> and gets assigned the product `1 · 6 = 6` or `6 · 1 = 6`,
> dividing the ratio back to 1.

The arithmetic works but the structural content needs to be made
precise. Specifically: why is the a_1² scaling a product over
generable subgroup orders? This is not a standard bundle-theoretic
quantity.

## Corrected Phase C (was Phase B) path

Route 1 is closed as a null result. Two candidates remain:

**Route 2 (from the original proposal).** Accept a
representation-assignment theorem as input from elsewhere
(`fiber_bundle.py`, matter-sector bundle construction) and write
Attempt 5 as a derivation with that input cited rather than
derived here. The weakness is circularity with whatever derives
the representation assignment.

**Route 3 (new, from the scan).** Look for a count of cardinality
6 attached to **walk dynamics** rather than **bundle structure**.
Three concrete candidates worth testing:

- **Stern–Brocot walk length.** Count Farey steps from a
  canonical anchor (e.g. 1/2 or the generation root) to the
  base pair. Leptons (3/2, 5/3): 2 steps (1/1 → 3/2, 3/2 → 5/3).
  Down-type (5/4, 9/8): longer walk. If the walk length ratio
  is 6:1 with an appropriate counting convention, that would
  close the derivation via walk geometry rather than bundle
  structure.

- **Homotopy classes on T² of bounded length.** Count closed
  loops on T² up to deck action that project to the down-type
  base pair (or its generation walk). Compare to K².

- **Feigenbaum-style fixed point count.** From
  `item12_C_from_K_star.md` §Open tasks, a Feigenbaum iteration
  at the lepton Fibonacci backbone is proposed. If the iteration
  has periodic orbits of period 6 only under the down-type
  constraints and period 1 for leptons, the ratio emerges from
  orbit dynamics.

**Route 4 (Phase B fallback).** Accept the down-type factor `6`
as a **matched structural fact** at PDG precision without a
topology derivation. This leaves the down-type Type C match open
in Issue #56 and does not reduce the Type C count from 2 to 1.
Shortest path but weakest outcome.

## Status summary

- Down-type double-cover derivation: **not closed** by Phase B
  and Route 1.
- The halt is deeper than a missing representation-assignment
  theorem: no Z_6-action on the base modes produces the ratio.
- Phase A §6's unification hypothesis (down-type 6 = hierarchy 6)
  is **refuted** by the scan.
- The observed Klein-parity / subgroup-order pattern in
  Candidate 3 is real but does not yet yield a reference-free
  derivation.
- Routes 2, 3, and 4 remain; Route 3 is the highest-leverage
  remaining option.

## Cross-references

| File | Role |
|---|---|
| `down_type_double_cover_phase_a.md` | Phase A vocabulary; §6 unification hypothesis is refuted |
| `down_type_double_cover_phase_b.md` | Phase B five attempts; Attempt 5 requires Route 1 |
| `down_type_stabilizer_scan.py` | The calculation producing this null result |
| `gap3_principal_bundle.py` | Source of the four XOR modes and Z_6 action |
| `item12_cross_sector_ratios.md` | Original conjecture, still open |
