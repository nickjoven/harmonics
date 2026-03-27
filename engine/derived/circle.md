# S^1 — The Circle

**Layer 1 derived type.** Proved from Layer 0 primitives: Z, fixpoint.

## Hypothesis

The phase space of periodic motion is the circle S^1 = R/Z.

## Derivation

From **Z** (the integers) + **fixpoint** (the self-consistency condition):

1. Let `f` be a lift of a circle map. The fixed-point condition applied to the `q`-th iterate gives `f^q(x) = x + p` for integers `p, q`.
2. The self-consistency condition requires `f^q(x) = x` on the quotient — the state must equal itself after `q` steps.
3. Therefore `p ≡ 0 (mod 1)`, which means `x` and `x + 1` are identified.
4. This identification is exactly **R/Z = S^1**.

Three lines: iterate (Z), close (fixpoint), quotient (S^1). No geometry is assumed — the circle is *forced* by periodicity plus self-consistency.

## Prediction

The phase space is **compact**: bounded, with no escape to infinity.

Every order parameter valued in S^1 satisfies `|r| ≤ 1`.

## Test

Compactness implies the triangle inequality bound: for any collection of unit phasors,

    |r| = |1/N Σ e^{iθ_k}| ≤ 1/N Σ |e^{iθ_k}| = 1

**Verify**: the Kuramoto order parameter never exceeds 1 in any simulation or observation. This is not an assumption — it is a consequence of S^1 topology.

## Consequence

**Conservation of information** (Section 9 of the theorem). Compactness of the phase space guarantees that the dynamics is measure-preserving on S^1 — no states are created or destroyed. The Liouville measure `dθ/2π` is invariant.

## Dependencies

- `primitives/z.md` — provides the integer iterate count `q` and shift `p`
- `primitives/fixpoint.md` — provides the self-consistency condition `f^q(x) = x`
