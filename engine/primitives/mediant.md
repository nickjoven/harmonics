# Mediant — The Combining Operation

## Hypothesis

The mediant is the unique combining operation for coupled oscillators. No other binary operation on fractions satisfies both betweenness and minimality simultaneously.

## Definition

Given two adjacent fractions `a/b` and `c/d` where adjacency means `|ad - bc| = 1`:

    mediant(a/b, c/d) = (a + c) / (b + d)

Properties that follow from the definition alone (no external references):

- **Betweenness**: `a/b < (a+c)/(b+d) < c/d` whenever `b, d > 0` and `a/b < c/d`.
- **Minimality**: `(a+c)/(b+d)` has the smallest denominator of any fraction strictly between `a/b` and `c/d`.
- **Adjacency preservation**: `mediant(a/b, c/d)` is adjacent to both `a/b` and `c/d`.

The mediant is not the arithmetic mean. It respects the integer structure of numerator and denominator separately.

## Derivation

From two requirements:

1. **Betweenness** (energy conservation): the result must lie between the inputs.
2. **Minimality** (Arnold tongue stability): the result must have the smallest possible denominator.

These two conditions uniquely determine the mediant. Proved in D29.

## Test (Necessity)

Without mediant:

- Interior rationals are unreachable — there is no way to construct `1/3` from `0/1` and `1/2`.
- The Stern-Brocot tree does not exist — the tree requires a binary operation on adjacent fractions.
- The devil's staircase has no steps — mode-locking widths require mediant iteration.
- Coupled oscillators have no combining rule — frequency locking is undefined.

## Composition Rules

| Combines with | Result | What emerges |
|---|---|---|
| Z | Q and the Stern-Brocot tree | Every rational appears exactly once; the tree is complete |
| Itself (iterated) | The full Stern-Brocot tree | Repeated mediant from `0/1` and `1/0` generates all of Q+ |
| Fixed point | The field equation | Self-consistent mediant iteration gives the locking condition |
| Parabola | Tongue boundaries | Mediant gives the rational, parabola gives the boundary width |
