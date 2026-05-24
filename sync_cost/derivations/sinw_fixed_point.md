# sin²θ_W Fixed-Point Hypothesis — Ruled Out

## Status

**Ruled out.** The K-scanning hypothesis (that there exists a K*
reproducing both α_s/α_2 and sin²θ_W at M_Z via the framework's
duty-cycle dynamics) fails numerically: no K in [0.93, 0.99]
reproduces either constraint.

The 1.1% residual between 8/35 and the observed sin²θ_W = 0.23121
is **not resolved**. The effective-dimension proposal d_eff = 80/27
(`sinw_effective_dimension.md`) reproduces 0.23123 at 0.5σ, but the
d → d_eff substitution fails under all three tested derivation
mechanisms — it is an ansatz fitted to the answer, not a derivation
(`g1_computation_result.md`; `numerology_inventory.md` §Class 2).
The 8/35 identity is a Class-1 near-coincidence at M_Z, not a
prediction; see `negative_results_ledger.md`.

## The hypothesis tested

Two branches for explaining the residual:

- **(i)** The tree scale is not M_Pl but some other scale μ_tree
  where SM running gives sin²θ_W = 8/35.
- **(ii)** The framework's "running" is the K → μ duty-cycle mapping,
  not SM 1-loop RG.

`sinw_fixed_point.py` tested the joint hypothesis: does there exist
a single K* satisfying both constraints simultaneously?

## Result

Neither constraint is met at any K in the critical window.

| K     | duty(2)  | duty(3)  | ratio d2/d3 | sin²θ_W |
|-------|----------|----------|-------------|---------|
| 0.93  | 0.03212  | 0.00805  | 3.993       | 0.2003  |
| 0.96  | 0.03212  | 0.00864  | 3.718       | 0.2120  |
| 0.99  | 0.03492  | 0.00953  | 3.662       | 0.2145  |

Observed at M_Z: α_s/α_2 = 3.488, sin²θ_W = 0.23121. No K
reproduces either value. The joint fixed-point question is moot.

## Conclusion

The identity sin²θ_W = 8/35 is measure-theoretic (Gauss-Kuzmin /
Ford circle measure at K = 1), not dynamical (tongue width at
finite K < 1). It stands only as a bare K=1 reference identity. The
1.1% residual is **not** closed: SM running has the wrong sign
(`sinW_running_check.py`), the K-scan fixed point is ruled out
(above), and the effective-dimension correction is a null ansatz
(`sinw_effective_dimension.md`, `g1_computation_result.md`). See
`negative_results_ledger.md`.

## Scripts

`sinw_fixed_point.py`, `sinW_running_check.py`.
