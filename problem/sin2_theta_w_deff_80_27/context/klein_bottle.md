# Context: Klein-bottle denominator classes (q₂, q₃) = (2, 3)

## Imported from

`../../../sync_cost/derivations/klein_bottle_derivation.md`

## Statement

The framework fixes (q₂, q₃) = (2, 3) uniquely through a pair
of algebraic cross-link identities:

    q₂² − 1 = q₃      (i.e., 4 − 1 = 3)
    q₃² − 1 = q₂³     (i.e., 9 − 1 = 8)

A short case analysis shows (q₂, q₃) = (2, 3) is the unique
positive integer solution. See
`../../../sync_cost/derivations/mass_sector_closure.md` for the
proof and its role in the gauge adjoint identification.

## Role in this problem

- q₂ = 2 → U(1)_Y hypercharge sector
  (identified in `gauge_sectors.md`).
- q₃ = 3 → SU(2)_L weak sector.
- The bare formula `sin²θ_W = q₂^d / (q₂^d + q₃^d)` uses both
  integers at d = 3:

      sin²θ_W (bare) = 2³ / (2³ + 3³) = 8/35.

- The d_eff correction `1/q₃^d = 1/27` uses q₃ specifically; the
  asymmetric choice (q₃ only, not q₂) is the content of
  `gaps/g2_q3_vs_q2_asymmetry.md`.

## Usage constraints

- (q₂, q₃) = (2, 3) is forced; not variable in the derivation.
- Any argument that requires (q₂, q₃) to take other values
  violates the Klein-bottle uniqueness and is outside the
  framework.

## Cross-references

- `../../../sync_cost/derivations/klein_bottle_derivation.md`
- `../../../sync_cost/derivations/mass_sector_closure.md`
  (uniqueness proof)
- `../gaps/g2_q3_vs_q2_asymmetry.md`
