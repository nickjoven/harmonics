# Status

## Overall

**G1 returned null — 1 of 3 Z-conditions met, 2 of 3 gaps now
structurally unlikely to close without a new mechanism.**

- **Z1 (numerical match at ≤ 1σ):** ✓ Met. Prediction 0.23123
  vs PDG MS-bar at M_Z 0.23121 ± 0.00004 = 0.5σ.
- **Z2 (no un-derived O(1) factors):** ✗ Not met — **G1 tested
  three candidate mechanisms (box-counting dim, width/period
  re-derivation, measure re-normalization) and all three fail
  to produce `d → d_eff = d − 1/q₃^d` from framework
  primitives.** See `attempts/g1_computation_result.md`.
- **Z3 (anchors labeled):** ✗ Not met. G3 open.

**Implication.** The sin²θ_W = 2^(80/27)/(2^(80/27)+3^(80/27))
proposal is a 0.5σ numerical match but **not a derivation**.
Since G1 does not close, G2 (q₃ vs q₂ asymmetry) and G3 (scheme
identification) no longer matter for promotion — they were
conditional on G1.

**Recommended reclassification.** Move
sin²θ_W(d_eff = 80/27) from Class 4 (`numerology_inventory.md`
audit candidate) to **Class 2** (noted coincidence, no framework
claim of derivation) — analogous to the Pythagorean-comma vs
K_Greene 0.17% coincidence.

## Gap-by-gap

### G1 — Occupied interval → effective dimension reduction

**Status:** **Null (2026-04-23).** `attempts/g1_computation_result.md`
tests three candidate mechanisms — box-counting dimension of
iterated complement, direct width/period re-derivation on `D`,
measure re-normalization — and all three fail to produce the
substitution `d → d_eff = d − 1/q₃^d` from framework primitives.

The ansatz treats "surviving Lebesgue fraction `1 − 1/q₃^d`" as
a "fractional dimension contribution" that enters as an
exponent. Neither identification is standard: the Cantor-style
box-counting gives d_H ≈ 0.948 not 26/27, and direct
re-derivation of `w/period` on the complement leaves the duty
unchanged at 1/q³.

**The 80/27 value is a numerical ansatz, not a derivation.**
Z2 sub-1 cannot close without a different mechanism not yet
proposed.

### G2 — Why only q₃ correction, not q₂

**Status:** **Moot (conditional on G1).** Since G1 did not
produce the `d → d_eff` substitution at all, the question of
whether the correction comes from q₂ or q₃ does not arise.
Would be reopened if a new G1 mechanism were proposed.

### G3 — Scheme identification (framework root ↔ MS-bar at M_Z)

**Status:** **Moot (conditional on G1).** G3 was to show the
root-level d_eff formula maps to MS-bar at M_Z. No such formula
derives from primitives (G1 null), so G3 has nothing to identify.
Would be reopened if G1 re-opens.

## History

| Date | Event |
|---|---|
| 2026-04-23 | Pilot problem scaffolded. Claim, nulls, context, gaps formalized. |
| 2026-04-23 | G1 attempt run. Three candidate mechanisms tested; all three fail to derive `d → d_eff = d − 1/q₃^d` from framework primitives. See `attempts/g1_computation_result.md`. |
| 2026-04-23 | G2 and G3 rendered moot by G1 null (they were conditional on G1). |

## Outcome

The pilot closes with a **negative verdict on the d_eff = 80/27
proposal as a derivation**. The 0.5σ numerical match is real
but reduces to a coincidence under Z1-Z3 accounting.

## Next action

- **Reclassify** sin²θ_W(d_eff = 80/27) in
  `../../sync_cost/derivations/numerology_inventory.md` from
  Class 4 to Class 2 (noted coincidence, no framework
  derivation).
- **Update** `../../sync_cost/derivations/sinw_effective_dimension.md`
  to note the G1 null finding (the occupied-interval → dimension
  argument doesn't derive from any of box-counting, direct
  re-derivation, or measure re-normalization).
- **Optionally log** a possible fifth null in
  `sinw_fixed_point.md`'s lineage: "d_eff = 80/27 ansatz as a
  structural derivation — tested, null."

## Cross-references

- `./claim.md`
- `./gaps/` — three open derivations
- `./nulls/` — four ruled-out mechanisms
- `./context/` — framework inputs
- `../../sync_cost/derivations/statistical_conventions.md` —
  Z1-Z3 definitions
