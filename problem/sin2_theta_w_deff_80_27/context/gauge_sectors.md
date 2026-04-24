# Context: Gauge sector assignment (q₂ ↔ U(1)_Y, q₃ ↔ SU(2)_L)

## Imported from

`../../../sync_cost/derivations/gauge_dictionary.md`
`../../../sync_cost/derivations/gauge_sector_lovelock.md`

## Statement

Within the gauge structure SU(3) × SU(2) × U(1) derived from the
Klein-bottle Z₆ center and Utiyama's theorem, the duty-cycle
dictionary assigns:

- **q₂ = 2** → the **U(1)_Y** hypercharge sector (double-cover
  structure, two eigenvalues under the order-2 generator).
- **q₃ = 3** → the **SU(2)_L** weak-isospin sector (triple-cover
  structure, three eigenvalues under the order-3 generator).
- **q₂ · q₃ = 6** → the Z₆ = Z₂ × Z₃ center acting on both.
- **SU(3)** color corresponds to the third denominator class not
  in play for the electroweak mixing calculation.

## Role in this problem

The bare formula

    sin²θ_W = duty(U(1)_Y) / (duty(U(1)_Y) + duty(SU(2)_L))
            = duty(q₂) / (duty(q₂) + duty(q₃))
            = q₂^d / (q₂^d + q₃^d)

follows directly from this identification: sin²θ_W is the ratio
of the U(1)_Y coupling strength (duty of q₂) to the total
(U(1)_Y + SU(2)_L) coupling strength at the electroweak branching
scale.

## Usage constraints

- The assignment q₂ ↔ U(1)_Y (not q₂ ↔ SU(2)_L) is fixed by the
  gauge dictionary. Inverting the assignment gives
  27/(8+27) = cos²θ_W, not sin²θ_W.
- The "duty of q₂ in the numerator" convention is tied to the
  standard `sin²θ_W = g'²/(g² + g'²)` definition via
  g ↔ SU(2), g' ↔ U(1).

## Cross-references

- `../../../sync_cost/derivations/gauge_dictionary.md`
- `../../../sync_cost/derivations/gauge_sector_lovelock.md`
  (SU(3)×SU(2)×U(1) uniqueness)
- `../../../sync_cost/derivations/duty_cycle_dictionary.md` §3
