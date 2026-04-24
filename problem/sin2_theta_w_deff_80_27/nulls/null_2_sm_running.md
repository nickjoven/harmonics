# Null 2: SM 1-loop running from tree = M_Pl to M_Z

## Tested mechanism

- Tree-scale boundary condition: `sin²θ_W = 8/35` at μ = M_Pl
  (framework's "tree = Planck" identification via R = 6·13⁵⁴).
- SM 1-loop β-functions (determined by SU(3)×SU(2)×U(1) with
  three generations and one Higgs doublet):

    b₂ = −19/6,   b_Y = 41/6,   b₁ = 41/10  (GUT-norm)

- Hypothesis: running this boundary condition from M_Pl down to
  M_Z with 1-loop RG gives the observed 0.23121.

## Test

`../../../sync_cost/derivations/sinW_running_check.py` evaluates
1-loop RG explicitly.

## Results

- **Starting at M_Z** (observed value) and running UP to M_Pl:
  sin²θ_W(M_Pl) ≈ 0.47 (under standard initial conditions at M_Z),
  not 0.22857.
- **Sign test**: `d sin²θ_W / d ln μ` at M_Z has the **opposite
  sign** to what "tree at M_Pl → observed at M_Z" would require.
  SM running moves sin²θ_W *up* with scale from M_Z to M_Pl, not
  down.
- **Scale where SM running gives 8/35**: μ ≈ 54 GeV (an
  unstructured scale, not Planck, not any framework scale).
- **Forward run from M_Pl → M_Z under the "tree = 8/35"
  boundary**: 1/α_Y crosses zero (Landau pole) before reaching
  M_Z. Unphysical.

## Verdict

**SM 1-loop RG running does not connect `8/35` at Planck to
`0.23121` at M_Z.** The 1.1% match at M_Z is an accidental
near-coincidence at an unstructured electroweak scale, not the
consequence of a framework → observation running chain.

## What this null tells the current problem

- **The claim must not rely on SM RG running to bridge tree and
  M_Z.** The d_eff = 80/27 proposal sidesteps RG entirely:
  d_eff modifies the formula itself at the root, not its running.
  This is consistent with Null 2 only if the root value **is**
  identified with MS-bar at M_Z by a non-RG mechanism —
  which is the content of `gaps/g3_msbar_identification.md`.
- Equivalently: whatever maps the framework's root to MS-bar at
  M_Z cannot be SM 1-loop running; it must be a scheme-matching
  identification internal to the framework.

## Cross-references

- `../../../sync_cost/derivations/sinW_running_check.py`
- `../../../sync_cost/derivations/sinw_fixed_point.md` §Conclusion
- `../gaps/g3_msbar_identification.md`
