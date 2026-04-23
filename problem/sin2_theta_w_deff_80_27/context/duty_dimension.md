# Context: Duty cycle at K=1 in d dimensions

## Imported from

`../../../sync_cost/derivations/duty_dimension_proof.md`

## Statement

At the measure-theoretic limit K=1 of the Arnold-tongue circle map
in d spatial dimensions, the duty cycle of the p/q rational
tongue is

    duty(q) = 1/q^d.

This is a number-theoretic fact about the tongue's share of the
circle-map measure when the Ford-circle stacking is complete.

## Role in this problem

- The bare formula for sin²θ_W uses `duty(q)`:

      sin²θ_W = duty(q₂) / (duty(q₂) + duty(q₃))
              = q₂^d / (q₂^d + q₃^d).

  (With the sector identification of `gauge_sectors.md`.)

- The d_eff proposal replaces `d → d_eff` with
  `d_eff = d − 1/q₃^d`. The bare formula is the starting point;
  `gaps/g1_occupied_interval.md` must justify the substitution.

## Usage constraints

- The derivation of `duty(q) = 1/q^d` is proven at K=1 only. Any
  finite-K extension brings in the dynamics that `nulls/null_3`
  and `nulls/null_4` already ruled out as the mechanism for the
  0.23121 match.

- The formula takes d as an integer (specifically d = 3 from
  `three_dimensions.md`). **Non-integer exponents d_eff are not
  covered by the bare proof.** Extending the bare formula to
  d_eff is precisely the content of `gaps/g1_occupied_interval.md`.

## Cross-references

- `../../../sync_cost/derivations/duty_dimension_proof.md`
- `../../../sync_cost/derivations/duty_cycle_dictionary.md`
- `../gaps/g1_occupied_interval.md`
