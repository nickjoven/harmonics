# Derivation 10: The Minimum Alphabet

## Claim

The framework's entire structure — the circle, the devil's staircase,
Arnold tongues, the Born rule, the RAR, and the uncertainty relation —
follows from compositions of exactly four irreducible primitives:

| # | Primitive | What it provides |
|---|-----------|-----------------|
| 1 | **Integers** | Counting, cycles, winding numbers |
| 2 | **Mediant** (a+c)/(b+d) | Rational structure without division |
| 3 | **Fixed-point** x = f(x) | Self-reference, iteration, dynamics |
| 4 | **Parabola** x² | Nonlinearity, bifurcation, Born rule |

No reals. No base. No continuum assumed. The continuum emerges as
completion; standard quantum mechanics emerges as the small-ε
linearized limit.

## The circle is derived, not assumed

Start with two primitives: integers (counting cycles) and the
fixed-point condition (x = f(x), return to start).

A period-q orbit with winding number p/q means: after q iterations,
the state has advanced by exactly p full cycles. The fixed-point
equation applied to the q-th iterate says:

    f^q(x) = x       (return to start)

But the winding count says:

    f^q(x) = x + p   (advanced by p)

Both hold simultaneously, so:

    x + p = x   in the phase space

Therefore p ≡ 0 in the phase space. Since p is an arbitrary integer,
**all integers must be equivalent to 0**. The phase space is R/Z.
That is S¹. That is the circle.

The mod-1 topology is not an axiom. It is the unique topology
consistent with integer counting and self-reference. You cannot have
periodic orbits with integer winding counts on a line — the line has
no fixed points of translation. The moment you demand that an orbit
returns (fixed-point equation) after counting an integer number of
full advances, you have quotiented by Z. You have a circle.

## Irreducibility of the four primitives

### Integers cannot be derived from the other three

The mediant operation needs integer numerators and denominators to
start. The parabola x² + μ = 0 gives two roots, but "two" requires
counting. Without integers, there is no winding number, no period,
no discrete structure.

### Mediants cannot be derived from integers + fixed-point + parabola

Integers give Z. The fixed-point equation gives dynamics. The
parabola gives bifurcation. But none of them construct the interior
rationals — the 1/3, 2/5, 3/8 that fill the Stern-Brocot tree.
Division would, but division is not in the alphabet. The mediant
(a+c)/(b+d) is the specific operation that builds rationals from
integers without ever dividing. It is irreducible.

### Fixed-point equation cannot be derived from the other three

Without x = f(x), there is no self-reference, no iteration, no
dynamics. The integers count but do not act. The mediants construct
but do not evolve. The parabola is a shape but not a process.
Self-reference is the primitive that makes the system a system
rather than a catalog.

### Parabola cannot be derived from the other three

Without x², everything is linear. Linear maps on the circle have
constant winding number — no tongues, no locking, no bifurcation.
The Born rule (Δθ² ∝ ε) needs the exponent 2, which is the universal
normal form at a saddle-node. No other exponent is generic:

- x³ gives a pitchfork (wrong codimension)
- x^(3/2) is not smooth
- x^n for n > 2 is unstable to quadratic perturbation

The parabola is the simplest nonlinearity and it is forced by
genericity (structurally stable codimension-1 bifurcation on S¹).

## Compositions

Everything in the derivation chain is a composition of these four:

| Structure | Composition |
|-----------|------------|
| **Circle** S¹ | Integers + fixed-point |
| **Devil's staircase** | Mediants on the circle (Stern-Brocot → winding number) |
| **Arnold tongues** | Parabola + circle (saddle-node bifurcation on S¹) |
| **Born rule** \|ψ\|² | Parabola at each tongue boundary (Δθ ∝ √ε) |
| **Tongue uncertainty** τ×Δθ = const | Fixed-point convergence rate + parabola |
| **HUP** Δω·Δt ≥ 1/2 | Linearized limit of tongue uncertainty (small ε) |
| **RAR** g_obs(g_bar) | Floquet exponent (fixed-point convergence rate) in physical coordinates |
| **Planck scale** | N = 3 threshold: minimum integer count for self-sustaining loop |
| **Spectral tilt** | φ² self-similarity of the staircase under the k↔Ω mapping |

## Connection to standard QM

Standard quantum mechanics is what you get when you:

1. **Linearize** the circle map dynamics (small ε, near tongue boundary)
2. **Complete** the rationals to the reals (take the continuum limit)

In the linearized limit:
- The tongue uncertainty τ×Δθ = const reduces to HUP Δω·Δt ≥ 1/2
- The transient is a decaying exponential (Fourier-analyzable)
- The basin measure Δθ² ∝ ε becomes the standard Born rule

QM is the small-ε sector of a system built from four primitives.
The framework does not derive QM — it identifies QM's domain of
validity from above.

## Testable prediction

In the nonlinear regime (large ε, deep inside tongues), the tongue
uncertainty relation gives corrections to the Gaussian
minimum-uncertainty bound. Minimum-uncertainty states that violate
the standard bound are the observable signature of the pre-continuum
structure.

Candidates: systems at strong coupling where the effective ε is
large — potentially measurable in strongly-driven superconducting
circuits or cavity QED systems deep in the mode-locked regime.

## Status

**Established**:
- Circle derived from integers + fixed-point (3-line proof)
- All four primitives shown irreducible
- Composition table verified against Derivations 1–9

**Open**:
- Formalize the completion (rationals → reals) as a specific limit
  of the Stern-Brocot tree. Is the completion unique, or does the
  choice of completion carry physical content?
- The mediant operation builds Q≥0. Negative rationals (and by
  extension, the full circle with orientation) require a sign
  primitive or a convention. Is orientation a fifth primitive, or
  does it follow from the parabola's two roots (±√μ)?
- Quantitative prediction for the minimum-uncertainty violation:
  what is the leading correction term, and at what coupling strength
  does it become measurable?
