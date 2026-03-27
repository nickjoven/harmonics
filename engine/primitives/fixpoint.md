# Fixed Point — The Self-Consistency Condition

## Hypothesis

Self-consistency is irreducible. Any physical state must satisfy `x = f(x)` for some dynamics `f`. This condition cannot be derived from simpler requirements.

## Definition

A fixed point of a map `f` is a value `x` such that:

    x = f(x)

That is: the state equals the output of the dynamics applied to the state.

No external input is assumed. The equation is closed — `x` appears on both sides. This eliminates exactly one degree of freedom: the arbitrary external input that would otherwise be needed to specify the state.

## What It Eliminates

The fixed-point condition removes the need for an external specification of state. Instead of "the state is X because we set it to X," the state is X because X is the unique (or selected) solution of `x = f(x)`.

This is the difference between a parameter and a prediction.

## Test (Necessity)

Without the fixed-point condition:

- Nothing iterates — `f^n(x)` has no reason to converge or cycle.
- No attractors exist — an attractor is a stable fixed point of the iterated map.
- No convergence criterion — there is no way to say "the system has settled."
- No physics — every physical law is a self-consistency condition (Einstein's equation, Schrodinger's equation, Maxwell's equations are all fixed-point conditions on their respective fields).

## Composition Rules

| Combines with | Result | What emerges |
|---|---|---|
| Z | Periodicity and S^1 | Fixed point of `f^p` gives period-`p` orbit; the circle emerges as the quotient Z/pZ |
| Mediant | The field equation | Self-consistent mediant iteration: the locking condition for coupled oscillators |
| Parabola | Saddle-node dynamics | `x = x^2 + mu` is the universal codimension-1 bifurcation; fixed point meets quadratic |
