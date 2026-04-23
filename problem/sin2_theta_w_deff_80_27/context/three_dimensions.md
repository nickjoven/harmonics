# Context: Spatial dimension d = 3

## Imported from

`../../../sync_cost/derivations/three_dimensions.md`

## Statement

The framework's spatial dimension is structurally fixed at d = 3
through the identification

    dim SL(2, ℝ) = 2² − 1 = 3

where SL(2, ℝ) is the adjacency-consistent manifold emerging
from the mediant operator on the Stern-Brocot tree. The "= 3"
is forced by the group-theoretic relation, not a choice.

## Role in this problem

The bare formula `sin²θ_W = q₂^d / (q₂^d + q₃^d)` is evaluated at
d = 3:

    sin²θ_W (bare) = 2³ / (2³ + 3³) = 8/35 = 0.22857.

The d_eff proposal uses d = 3 as the reference and computes the
correction `−1/q₃^d = −1/27`, giving

    d_eff = 3 − 1/27 = 80/27.

## Usage constraints

- d = 3 is an integer at the framework's primitive level. The
  d_eff value is **not** an integer; it is d corrected by a
  fractional (1/q₃^d = 1/27) contribution.
- The reduction d → d_eff is not a change in the spatial
  dimension of the underlying manifold (which remains 3). It is
  an effective dimension seen by the frequency-axis integral.
  Gap 1 must make this distinction rigorous.

## Cross-references

- `../../../sync_cost/derivations/three_dimensions.md`
- `../../../sync_cost/derivations/klein_bottle.md`
- `../gaps/g1_occupied_interval.md`
