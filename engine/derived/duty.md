# duty(q) = 1/q^d — The Gate Availability

**Layer 1 derived type.** Proved from Layer 0 primitives and Layer 1 derivations.

## Hypothesis

The gate availability (duty cycle) of a mode with denominator `q` scales as `1/q^d`, where `d = 3` is the spatial dimension.

## Derivation

From **mediant** (via rationals.md) + **dimension.md**:

1. **Tongue width** `w(q) = 1/q²`: the width of the Arnold tongue at rotation number `p/q` is determined by the Gauss-Kuzmin measure on continued fractions. This measure arises from the hyperbolic area element at the cusps of the modular surface SL(2, Z)\H. The cusp width scales as `1/q²`.

2. **Period** `T(q) = q`: the orbit period of a `p/q`-locked mode is `q` iterates (from Z — `q` successive applications of the map).

3. **Duty cycle** = fraction of time the gate is open:

       duty(q) = w(q) / T(q) = (1/q²) / q = 1/q³ = 1/q^d

   where `d = 3` from dimension.md.

## Prediction

Coupling ratios between modes are ratios of their `q^d` values.

Specifically, the ratio of coupling strengths at denominators `q_a` and `q_b` is:

    duty(q_a) / duty(q_b) = q_b^3 / q_a^3

## Test

The strong-to-weak coupling ratio for `q₃ = 3` and `q₂ = 2`:

    α_s / α₂ = duty(2) / duty(3) = 3³ / 2³ = 27/8 = 3.375

Observed ratio: **3.488** (from the Standard Model coupling constants at the Z-boson mass scale).

Residual: |3.488 - 3.375| / 3.375 = **3.2%**

This 3.2% residual is expected to be accounted for by running (RG flow) corrections — the `q^3` scaling is the tree-level result.

## Dependencies

- `primitives/z.md` — provides the orbit period `T(q) = q`
- `primitives/mediant.md` — provides the tongue structure via the Stern-Brocot tree
- `derived/rationals.md` — provides the cusp geometry of SL(2, Z)\H
- `derived/dimension.md` — provides `d = 3`
