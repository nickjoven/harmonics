# Signature (3,1) — The Spacetime Metric

**Layer 1 derived type.** Proved from Layer 0 primitives and Layer 1 derivations.

## Hypothesis

The spacetime signature is determined by the observability of phase-locking states. Observable dimensions are spacelike; the dark (unobservable) dimension is timelike.

## Derivation

From **circle.md** + **klein.md**:

1. **Two oscillators on S^1**: each oscillator is either **locked** (phase-coherent, observable) or **unlocked** (incoherent, phase averages to zero).

2. **Four states from {locked, unlocked}²**:

   | State | Oscillator 1 | Oscillator 2 | Observability |
   |-------|-------------|-------------|---------------|
   | A | locked | locked | ✓ observable |
   | B | locked | unlocked | ✓ observable |
   | C | unlocked | locked | ✓ observable |
   | D | unlocked | unlocked | ✗ dark |

3. **State D is dark**: when both oscillators are unlocked, `⟨sin(ω₁t - ω₂t)⟩ = 0` for irrational frequency ratio. No phase coherence is detectable. This state contributes to dynamics but is not directly observable.

4. **Counting**: observable states = **3**, dark states = **1**.

5. **Signature assignment**: observable dimensions are spacelike (measurable distances), the dark dimension is timelike (measurable only via change). This gives signature **(3, 1)**.

## Prediction

The metric is **Lorentzian** with 3 spacelike and 1 timelike dimension.

The Clifford algebra is **Cl(3, 1)**, which has the correct structure to support spinors and the Dirac equation.

## Test

1. **Observed signature** = (3, 1) ✓

2. **Clifford algebra verification**: the figure-8 crossing operators (from `clifford_figure8.py`) satisfy the Cl(3, 1) relations:

       {γ_μ, γ_ν} = 2η_{μν}

   where `η = diag(+1, +1, +1, -1)`.

3. **Why not (1, 3)?** The convention follows from the derivation: the *majority* (observable) states are spacelike. Time is the *residual* — the single dark degree of freedom that parameterizes evolution without being directly measurable.

## Dependencies

- `derived/circle.md` — provides S^1 as the phase space for each oscillator
- `derived/klein.md` — provides the two-oscillator coupling topology and the distinction between orientable/non-orientable directions
- `primitives/fixpoint.md` — provides the locking condition (fixed point of the coupled dynamics)
