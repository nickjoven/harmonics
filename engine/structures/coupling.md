# Coupling Constants from Duty Cycles

**Layer 2 structure.** Composed from Layer 1 derived types: duty.md, klein.md.

## Hypothesis

The strong/weak coupling ratio is q₃³/q₂³.

## Derivation

From **duty.md** + **klein.md**:

1. The Klein bottle has two fundamental periods: q₂ = 2 and q₃ = 3 (the two smallest primes, forced by the adjacency structure of modes).
2. The duty cycle of a mode-locked tongue at rotation number p/q scales as 1/q³ (from duty.md: the tongue width at criticality).
3. The coupling constant for the sector governed by period q is proportional to the duty cycle of the *partner* period. This is the **crossed dictionary**: α_q = duty(partner_q) × |r|.
4. Therefore:
   - α_s (strong, governed by q₃) gets its strength from duty(q₂) = 1/q₂³ = 1/8
   - α₂ (weak, governed by q₂) gets its strength from duty(q₃) = 1/q₃³ = 1/27
5. The ratio: α_s/α₂ = duty(q₂)/duty(q₃) = (1/q₂³)/(1/q₃³) = q₃³/q₂³ = 27/8

## Prediction

**α_s/α₂ = 27/8 = 3.375**

## Test

Observed ratio at M_Z: α_s(M_Z)/α₂(M_Z) ≈ 0.1179/0.0338 ≈ 3.488

**Residual: 3.2%**, accounted for by running of the coupling constants between the crossing scale and M_Z.

## Dependencies

- `derived/duty.md` — provides the 1/q³ duty-cycle scaling
- `derived/klein.md` — provides the two fundamental periods q₂ = 2, q₃ = 3
- `primitives/z.md` — integers underlying the periods
- `primitives/mediant.md` — adjacency structure that selects the periods
