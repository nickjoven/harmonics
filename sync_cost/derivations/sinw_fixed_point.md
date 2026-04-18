# sin²θ_W Fixed-Point Hypothesis — Ruled Out

## Status

**Ruled out.** The K-scanning hypothesis (that there exists a K*
reproducing both α_s/α_2 and sin²θ_W at M_Z via the framework's
duty-cycle dynamics) fails numerically: no K in [0.93, 0.99]
reproduces either constraint.

The 1.1% residual between 8/35 and the observed sin²θ_W = 0.23121
is resolved by a different mechanism: the effective-dimension
correction d_eff = 80/27 (see `sinw_effective_dimension.md`), which
gives sin²θ_W = 0.23123, within 0.5σ of the PDG value.

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
finite K < 1). The 1.1% residual is not from running — it is
corrected by the effective-dimension mechanism in
`sinw_effective_dimension.md`.

## Scripts

`sinw_fixed_point.py`, `sinW_running_check.py`.
