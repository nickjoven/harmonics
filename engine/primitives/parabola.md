# Parabola — The Quadratic Bifurcation

## Hypothesis

The equation `x^2 + mu = 0` is the unique generic codimension-1 bifurcation on S^1. No simpler nonlinearity produces the required structure; no other degree-2 normal form is generic.

## Definition

The polynomial equation in one variable `x` with one parameter `mu`:

    x^2 + mu = 0

Solutions: `x = +/- sqrt(-mu)`.

- When `mu < 0`: two real solutions (two fixed points exist).
- When `mu = 0`: one repeated solution (the bifurcation point, saddle-node).
- When `mu > 0`: no real solutions (fixed points have annihilated).

This is the complete codimension-1 normal form. All higher-order terms are removable by smooth coordinate change. The quadratic is the first term that cannot be removed.

## What It Provides

- **Orientation**: the `+/-` in `sqrt(-mu)` gives two branches, two directions, a sign.
- **The Born exponent**: the squaring in `x^2` is the origin of the exponent 2 in probability (amplitude squared gives probability).
- **The saddle-node bifurcation**: the generic mechanism by which fixed points are created and destroyed.
- **Tongue boundaries**: the parabolic width of Arnold tongues near rational rotation numbers.

## Test (Necessity)

Without the parabola:

- All maps are linear — fixed points exist but never bifurcate.
- No Arnold tongues — tongue width is zero without the quadratic term.
- No mode-locking — the devil's staircase is flat (all steps have zero width).
- No basins of attraction — linear maps have no basin boundaries.
- No Born rule — probability requires the squaring operation.

## Composition Rules

| Combines with | Result | What emerges |
|---|---|---|
| Z | The golden polynomial `x^2 - x - 1 = 0` yielding phi | The most irrational number; the noble numbers; the Fibonacci sequence |
| Fixed point | Saddle-node dynamics | `x = x^2 + mu` gives the universal bifurcation; creation/annihilation of states |
| Mediant | Tongue boundaries | Each rational `p/q` gets a tongue of width proportional to the parabolic opening |
