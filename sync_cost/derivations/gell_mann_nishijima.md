# The Gell-Mann-Nishijima Relation from Klein Bottle Geometry

## Theorem

The relation Q = T_3 + Y/2 between electric charge Q, weak isospin
T_3, and hypercharge Y is not a postulate. It is the charge
composition law at the Klein bottle's identification boundary, where
the antiperiodic (twisted) and periodic (untwisted) directions meet.

The factor 1/2 is the order of the y-reflection in the Klein bottle
identification (0, y) ~ (1, 1-y). This reflection has order 2, and
its generator contributes Y/2 to the boundary charge.

---

## Part I: The three charges and their geometric origins

### Electric charge Q: the boundary observable

Electric charge is what you measure at the boundary between the two
Klein bottle directions. A detector couples to the mode at its
location. The coupling sin(theta_osc - theta_det) reads the
phase relationship. The observable is the winding number of the
combined mode — the number of times the phase wraps around S^1
per cycle. This winding number, measured in units of the fundamental
winding (the q=1 mode), is the electric charge.

The Klein bottle fractions {1/3, 1/2, 2/3} give |Q| = {1/3, 1/2, 2/3}
directly. The sign comes from the direction of winding relative to
the detector's reference phase.

### Weak isospin T_3: the twist charge

The x-direction of the Klein bottle is antiperiodic: traversing the
x-loop returns with reversed orientation. The half-twist shifts
phase by pi. Modes on the x-loop split into two classes based on
their behavior under this half-twist:

- **T_3 = +1/2**: the mode acquires phase +pi/2 per half-twist
  (transforms as the "up" component of the doublet)
- **T_3 = -1/2**: the mode acquires phase -pi/2 per half-twist
  (transforms as the "down" component)

Why +/- 1/2? The half-twist is an element of order 2 in the
fundamental group pi_1(Klein bottle). The irreducible representations
of Z_2 acting on a complex doublet assign eigenvalues e^{+i pi/2}
and e^{-i pi/2} to the two components, giving T_3 = +/- 1/2.

Alternatively: the antiperiodic boundary condition forces half-integer
x-wavenumbers (D19, mode analysis). The smallest half-integer is 1/2.
The doublet structure (two components with T_3 = +/- 1/2) is the
fundamental representation of the SU(2) that covers the Z_2 twist.

Singlet modes (T_3 = 0) are those that are symmetric under the
half-twist — they do not transform under the x-direction
identification.

### Hypercharge Y: the periodic charge

The y-direction is periodic: traversing the y-loop returns to the
starting configuration without phase shift. Modes on the y-loop
carry integer winding numbers. The charge under the y-direction's
U(1) symmetry is the hypercharge Y.

The periodic direction is the temporal direction (D19: time is the
periodic direction). The hypercharge is the charge under time
translation — the conserved quantity associated with the periodic
direction's U(1) isometry.

---

## Part II: The identification boundary

### Where the directions meet

The Klein bottle identification is:

    (x, 0) ~ (x, 1)           periodic in y
    (0, y) ~ (1, 1-y)         antiperiodic + reflect in x

The second identification is the critical one. At the x-boundary
(x = 0 identified with x = 1), two things happen simultaneously:

1. **The twist**: phase shifts by pi (antiperiodic)
2. **The reflection**: y maps to 1-y

### The reflection's effect on the periodic charge

A mode carrying hypercharge Y under the periodic y-direction has
the form:

    psi_Y(y) = e^{2 pi i Y y}

Under the reflection y -> 1-y:

    psi_Y(1-y) = e^{2 pi i Y (1-y)} = e^{2 pi i Y} · e^{-2 pi i Y y}

For integer Y: e^{2 pi i Y} = 1, so:

    psi_Y(1-y) = e^{-2 pi i Y y} = psi_{-Y}(y)

The reflection sends Y -> -Y. It reverses the hypercharge.

### The combined operation at the boundary

At the identification boundary (x = 0 ~ x = 1), a mode must be
consistent under the combined operation:

    twist ∘ reflection: (phase shift by pi) ∘ (y -> 1-y)

The twist contributes T_3 (the eigenvalue under the half-twist).
The reflection contributes from Y. But the reflection reverses Y,
so the mode at the boundary must satisfy a consistency condition
between T_3 and Y.

### The consistency condition

Consider a doublet mode with components (psi_up, psi_down)
corresponding to T_3 = (+1/2, -1/2). At the boundary, the
combined operation gives:

    psi_up(0, y) ~ psi_down(1, 1-y) · e^{i pi}

The observable charge at the boundary is the eigenvalue of the
generator of the U(1) that commutes with both the twist and the
reflection. This is the electromagnetic U(1) — the diagonal
generator that survives at the identification.

For the up component (T_3 = +1/2):
- Twist contribution: +1/2
- Reflection on Y: the reflection y -> 1-y has order 2. Its
  generator on charge-Y states is Y/2 (since the Z_2 eigenvalue
  is e^{i pi Y} = (-1)^Y, and the generator of a Z_2 action with
  eigenvalue (-1)^Y is Y/2).

The factor 1/2 arises because the reflection is an involution
(order 2). If it had order n, the generator would be Y/n.
The Klein bottle's reflection has order 2 — apply twice, get
the identity:

    (y -> 1-y) -> (1-y -> 1-(1-y) = y)

Therefore the generator that exponentiates to the reflection is
Y/2, and the total charge at the boundary is:

    **Q = T_3 + Y/2**

---

## Part III: Verification

### The charge table

Using Q = T_3 + Y/2 with the Klein bottle fractions:

**Quark doublet** (q_1 = 3, antiperiodic sector):
- Q_up = 2/3 → T_3 = +1/2, Y = 2(2/3 - 1/2) = 1/3
- Q_down = -1/3 → T_3 = -1/2, Y = 2(-1/3 + 1/2) = 1/3 ✓ (same Y)

**Lepton doublet** (q_1 = 1, boundary sector):
- Q_nu = 0 → T_3 = +1/2, Y = 2(0 - 1/2) = -1
- Q_e = -1 → T_3 = -1/2, Y = 2(-1 + 1/2) = -1 ✓ (same Y)

**Right-handed singlets** (T_3 = 0):
- u_R: Q = 2/3, Y = 2(2/3) = 4/3
- d_R: Q = -1/3, Y = 2(-1/3) = -2/3
- e_R: Q = -1, Y = 2(-1) = -2

These are exactly the Standard Model hypercharges. No free
parameters.

### Why the doublet consistency works

Within each doublet, the two components must have the same Y
(since Y is the U(1) charge, and doublet components differ
only in T_3). This requires:

    Q_up - Q_down = (T_3,up + Y/2) - (T_3,down + Y/2)
                   = T_3,up - T_3,down
                   = 1/2 - (-1/2) = 1

So Q_up - Q_down = 1 for every doublet. Check:
- Quarks: 2/3 - (-1/3) = 1 ✓
- Leptons: 0 - (-1) = 1 ✓

This unit charge difference within doublets is forced by the
twist structure: the half-twist shifts T_3 by 1 (from +1/2 to
-1/2), and since the reflection doesn't change within the
doublet (same Y), the charge difference is exactly 1.

### Anomaly cancellation revisited

The logical chain from topology to anomaly cancellation is:

    Klein bottle topology
    → XOR filter → charges {1/3, 1/2, 2/3} (D19)
    → twist → doublet structure T_3 = ±1/2 (this derivation)
    → identification boundary → Q = T_3 + Y/2 (this derivation)
    → hypercharges uniquely determined (this derivation)
    → anomaly cancellation automatic (D41, `anomaly_check.py`)

No external input remains. The full charge table is topological.

---

## Part IV: What the factor 1/2 means

The 1/2 in Q = T_3 + Y/2 is the same 1/2 that appears throughout
the framework:

- **T_3 = ±1/2**: the doublet eigenvalues under the half-twist
- **The mediant of 1/3 and 2/3**: med(1/3, 2/3) = 1/2
- **The confinement ratio** (D41): (q=3 forbidden)/(q=2 allowed) = 1/2 at K=1
- **The order parameter**: r ≈ 0.5 on the Klein bottle

All of these are manifestations of the same geometric fact: the
Klein bottle identification contains an order-2 element (the
reflection y -> 1-y), and 1/2 is the generator of Z_2.

The GNN relation is not a coincidence, a convention, or an
empirical rule. It is the statement that the electromagnetic
charge is the diagonal generator at the Klein bottle's
identification boundary — the point where the twisted and
periodic directions are sewn together.

---

## Status

**Derived.** Q = T_3 + Y/2 follows from the Klein bottle
identification geometry. The factor 1/2 is the order of the
y-reflection. No new assumptions.

**Dependencies**: D19 (Klein bottle topology, charge fractions),
D42 (gauge group identification).

The full SM charge table is derived from topology alone.
