# Null 3: K-scanning joint fixed-point hypothesis

## Tested mechanism

There exists K* ∈ [0.93, 0.99] (the "critical" window for
KAM destruction in the framework's duty-cycle dynamics) such that
evaluating the duty cycles at K* simultaneously reproduces:

- α_s / α_2 at M_Z = 3.488, and
- sin²θ_W at M_Z = 0.23121.

## Test

`../../../sync_cost/derivations/sinw_fixed_point.py` swept K
through the window, computing `duty(q_2, K)`, `duty(q_3, K)`,
and deriving both α_s/α_2 and sin²θ_W.

## Results

| K    | duty(2) | duty(3) | α_s/α_2 | sin²θ_W |
|------|---------|---------|---------|---------|
| 0.93 | 0.03212 | 0.00805 | 3.993   | 0.2003  |
| 0.96 | 0.03212 | 0.00864 | 3.718   | 0.2120  |
| 0.99 | 0.03492 | 0.00953 | 3.662   | 0.2145  |

Observed: α_s/α_2 = 3.488, sin²θ_W = 0.23121.

**No K ∈ [0.93, 0.99] reproduces either constraint.**

## Verdict

The identity `sin²θ_W = 8/35` is measure-theoretic (Gauss-Kuzmin
/ Ford-circle measure at K=1), not dynamical (tongue width at
finite K < 1). Finite-K corrections do not close the 1.1% gap in
either direction.

## What this null tells the current problem

- The d_eff proposal is **not a finite-K correction**. It does
  not run K. It evaluates the bare formula at K=1 but with
  `d → d_eff = d − 1/q₃^d`. The correction source is geometric
  (tongue strip width in the (d-1)-dimensional spatial
  manifold), not dynamical (K-dependence).
- The distinction between "K-correction" (Null 3, ruled out) and
  "dimensional correction at K=1" (this claim's mechanism) is
  essential. `gaps/g1_occupied_interval.md` must formalize the
  dimensional reduction without invoking finite-K running.

## Cross-references

- `../../../sync_cost/derivations/sinw_fixed_point.md`
- `../../../sync_cost/derivations/sinw_fixed_point.py`
- `../gaps/g1_occupied_interval.md`
