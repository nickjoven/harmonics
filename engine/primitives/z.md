# Z — The Integers

## Hypothesis

Counting is irreducible. No simpler structure can replace discrete succession.

## Definition

The natural numbers under the successor function:

- There exists a distinguished element `0`.
- There exists a function `S` such that `S(n)` is the successor of `n`.
- `S` is injective: `S(a) = S(b)` implies `a = b`.
- `0` is not in the range of `S`.
- (Induction) If a property holds for `0` and is preserved by `S`, it holds for all elements.

The integers extend this by closing under additive inverse: for every `n`, there exists `-n` such that `n + (-n) = 0`.

No further structure is assumed. No metric, no topology, no ordering beyond what successor provides.

## Test (Necessity)

Without Z:

- The mediant has no operands — fractions `a/b` require integers `a` and `b`.
- The parabola has no roots to count — multiplicity requires counting.
- The fixed point has no iterate count — `f^n(x)` requires `n` in Z.
- Periodicity is undefined — period `p` requires `p` in Z.

Remove Z and the other three primitives become inert.

## Composition Rules

| Combines with | Result | What emerges |
|---|---|---|
| Mediant | Q (the rationals via the Stern-Brocot tree) | All interior rationals become reachable |
| Fixed point | S^1 (the circle, via periodicity) | Iteration count gives period, period gives the circle |
| Parabola | Orientation (±) and the golden ratio | x^2 - x - 1 = 0 yields phi; ± square roots give orientation |
