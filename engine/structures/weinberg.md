# The Weinberg Angle

**Layer 2 structure.** Composed from Layer 1 derived types: duty.md, klein.md.

## Hypothesis

sin²θ_W = q₂³/(q₂³ + q₃³)

## Derivation

From **duty.md** + **klein.md**:

1. The electroweak mixing angle θ_W governs the partition of coupling strength between the electromagnetic and weak sectors.
2. The total coupling budget is the sum of duty cycles for the two Klein bottle periods: duty(q₂) + duty(q₃) = 1/q₂³ + 1/q₃³.
3. The weak-hypercharge fraction is determined by the *smaller* duty cycle (the q₃ sector):
   - sin²θ_W = duty(q₃) / [duty(q₂) + duty(q₃)]
   - = (1/q₃³) / [(1/q₂³) + (1/q₃³)]
4. Multiplying numerator and denominator by q₂³q₃³:
   - sin²θ_W = q₂³ / (q₂³ + q₃³)
   - = 8 / (8 + 27)
   - = **8/35**

## Prediction

**sin²θ_W = 8/35 = 0.22857...**

## Test

Observed: sin²θ_W(M_Z) = 0.23122 ± 0.00004

**Residual: 1.1%**, consistent with radiative corrections from the bare value to M_Z.

## Dependencies

- `derived/duty.md` — provides the 1/q³ duty-cycle scaling
- `derived/klein.md` — provides the two fundamental periods q₂ = 2, q₃ = 3
- `primitives/z.md` — integers underlying the periods
- `primitives/mediant.md` — adjacency structure that selects the periods
