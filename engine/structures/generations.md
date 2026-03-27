# Three Generations

**Layer 2 structure.** Composed from Layer 1 derived types: signature.md, duty.md.

## Hypothesis

The generation count = observable phase states = 2² - 1 = 3.

## Derivation

From **signature.md** + **duty.md**:

1. The Klein bottle figure-8 immersion has **4 phase states** {A, B, C, D}, corresponding to the 4 modes of the (3,1) signature (from signature.md).
2. Of these 4 states, **3 are observable** (A, B, C) and **1 is dark** (D — the timelike mode, whose twist makes it unobservable as a free particle).
3. Each observable phase state defines a distinct chain type connecting a mode to the root of the Stern-Brocot tree. These three chain types ARE the three generations.
4. The **mass hierarchy** comes from the phase-state weights:
   - Each generation's mass is weighted by powers of the duty-cycle base.
   - The base ratios involve q₃³ - 1 = 26 and q₂³ - 1 = 7.
   - Generation ordering: B : C : A with seed ratio **26 : 7 : 1**.

## Prediction

- **3 generations** of fermions
- Mass ratio seed: **26 : 7 : 1**
- Lepton mass ratio: m_τ/m_e = 26^(5/2) = 3447

## Test

- Observed generations: **3** ✓
- Observed m_τ/m_e = 1776.86/0.51100 = **3477**
- Predicted: 26^(5/2) = **3447**
- **Residual: 0.9%**

## Dependencies

- `derived/signature.md` — provides the 4 phase states and (3,1) decomposition
- `derived/duty.md` — provides the duty-cycle weights for mass hierarchy
- `derived/klein.md` — provides the Klein bottle modes
- `derived/circle.md` — provides the phase space S¹
- `primitives/z.md` — integers
- `primitives/fixpoint.md` — self-consistency condition
