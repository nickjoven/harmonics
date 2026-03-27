# Klein Bottle — Topology and XOR Filter

**Layer 1 derived type.** Proved from Layer 0 primitives and Layer 1 derivations.

## Hypothesis

The non-orientable topology of the Klein bottle selects denominator classes `q₂ = 2` and `q₃ = 3` via a parity (XOR) filter.

## Derivation

From **circle.md** × **circle.md** + antiperiodic boundary conditions:

1. **Two circles**: take S^1 × S^1 (from circle.md applied twice). This is the torus T².

2. **Antiperiodic boundary condition**: impose `θ(x + L) = θ(x) + π` in one direction. This is the minimal non-trivial identification — a half-period shift. The resulting space is the **Klein bottle** K².

3. **Fourier analysis on K²**: the antiperiodic direction allows only **half-integer wavenumbers**. In the Stern-Brocot representation, these correspond to fractions with **even denominators**.

4. **Non-orientability forces XOR**: on K², the orientation-reversing loop means that two coupled modes `(q₁, q₂)` must have opposite parity to be topologically consistent:

       q₁ % 2 ≠ q₂ % 2    (XOR condition)

5. **Selection**: the smallest coprime denominators satisfying XOR are `{2, 3}`. These are the only allowed fundamental modes.

## Prediction

Only modes with opposite denominator parity survive on the Klein bottle. The fundamental pair is `(q₂, q₃) = (2, 3)`.

## Test

**Simulation** (`klein_bottle_kuramoto.py`): a Kuramoto model on the Klein bottle (with the antiperiodic twist) shows **4-mode collapse** at modes `(2, 3)` and `(3, 2)`.

**Control**: the same simulation on the **torus** (no twist, periodic boundary conditions in both directions) does **NOT** show the collapse — all mode pairs are equally accessible.

The XOR filter is a topological consequence, not a dynamical coincidence.

## Dependencies

- `derived/circle.md` — provides S^1, used twice to form the base torus
- `derived/rationals.md` — provides the Stern-Brocot denominator classification
- `primitives/fixpoint.md` — provides the self-consistency that selects the antiperiodic BC as the minimal non-trivial identification
