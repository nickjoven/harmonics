# Null 4: K → μ duty map with |r| decoherence tax

## Tested mechanism

Rather than SM 1-loop running (Null 2) or joint K* fixed-point
(Null 3), the hypothesis is that the framework runs via a
**K → μ duty-cycle mapping**, and the 1.1% gap between `8/35`
and `0.23121` is the **decoherence tax** `1 − |r|` at finite K,
where `|r|` is the Kuramoto order parameter at the observation
scale.

## Test

Implicit in `../../../sync_cost/derivations/gate_duty_predictions.py`,
which fits `K*(M_Z)` to α_s/α_2 and reports the resulting
sin²θ_W with the `|r|` correction applied.

## Results

Combined with Null 3: when K* is chosen to match α_s/α_2 at M_Z,
sin²θ_W does not simultaneously match. No single K* closes both
constraints, regardless of whether the 1.1% gap is labelled
"decoherence tax" or not.

## Verdict

- The K → μ duty mapping is a consistent internal mechanism for
  generating scale dependence (different from SM RG), but it
  does not produce a joint fit of α_s/α_2 and sin²θ_W at M_Z.
- The "decoherence tax" framing of the residual is **internally
  consistent** (|r| at finite K does reduce the tree value
  linearly) but **externally inconsistent** (it doesn't line up
  with the dual constraint).

## What this null tells the current problem

- The d_eff = 80/27 proposal does **not** invoke |r| or any
  finite-K decoherence correction. It modifies the bare formula
  directly via a dimensional reduction at K=1.
- Any derivation for `gaps/g1_occupied_interval.md` that
  reintroduces `|r|` or a K-dependent factor will conflict with
  Null 4 and would need to re-test against α_s/α_2 jointly.
- The claim's path is: **K=1 + d_eff structural correction →
  MS-bar at M_Z** via scheme identification (Gap 3), not via
  K-running + |r|.

## Cross-references

- `../../../sync_cost/derivations/gate_duty_predictions.py`
- `../../../sync_cost/derivations/sinw_fixed_point.md` §Conclusion
- `../gaps/g1_occupied_interval.md`
- `../gaps/g3_msbar_identification.md`
