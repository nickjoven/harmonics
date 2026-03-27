# Round Robin, Gearbox, and Particle Trajectories

## The Round Robin: coupled oscillators in a ring

### The design

N oscillators in a ring, each coupled to its neighbors:

```
    [1] ——K——> [2] ——K——> [3] ——K——> ... ——K——> [N] ——K——> [1]
```

Each oscillator has a natural frequency ω_i. The coupling K
is the same between all neighbors. The ring topology means
the first oscillator couples to the last — the snake eats
its tail.

### What the framework predicts

The ring IS the figure-8, extended to N nodes:

- At low K: all oscillators run independently. No structure.
- At threshold K_c: the first tongue opens. Two adjacent
  oscillators lock. The lock propagates around the ring.
- Above threshold: mode-locking cascades. The steady state is
  a standing wave on the ring with specific winding number p/q
  determined by the frequency distribution.
- At K = 1: the entire ring is phase-locked. One mode. The
  mean field. The self-consistent fixed point.

The winding number of the steady state IS a Stern-Brocot
fraction. The ring "selects" the simplest rational compatible
with its frequency distribution — the widest tongue that
fits the data.

### The round-robin exploit

Instead of fighting the mode-locking (trying to keep
oscillators independent), DESIGN the natural frequencies
to produce a SPECIFIC winding number:

1. Choose target winding number p/q (the desired steady state)
2. Set ω_i = p/q + small detuning δ_i (all oscillators near
   the target tongue)
3. Set K above the tongue threshold for p/q
4. The ring locks to p/q — the steady state is the target

The exploit: the ring COMPUTES the target winding number by
settling to the fixed point. You don't compute p/q numerically —
the ring computes it physically. The convergence time is
τ ∝ 1/√ε (saddle-node), and the result is exact (it's a
mode-lock, not an approximation).

### Physical round-robin applications

**Frequency synthesis:** a ring of N voltage-controlled
oscillators (VCOs), each coupled capacitively. Set the VCO
frequencies near the target ratio. The ring locks to the
EXACT rational. Output: a signal at frequency p/q × f_reference,
with the stability of a mode-lock (not a PLL — no feedback
loop, no jitter from the loop filter).

**Distributed clock:** N nodes in a network, each with a local
oscillator. The coupling is the network latency. The ring
topology arises naturally (ring networks, token rings, ring
buses). The mode-lock synchronizes all clocks to a common
rational multiple of the master clock — without a central
master. The synchronization IS the fixed point.

**Analog computer:** a ring of N oscillators where the winding
number encodes the answer. Set up the natural frequencies to
encode the problem. Let the ring lock. Read the winding number.
The answer is a rational — exact, not approximate. The
computation is the convergence to the fixed point.

---

## The Perfect Gearbox: the Ouroboros

### Gears ARE the Stern-Brocot tree

A gear with T₁ teeth on the input meshing with T₂ teeth on
the output produces a frequency ratio of T₁/T₂. This is a
rational number. The gear mesh IS the tongue — the teeth
force exact mode-locking at T₁/T₂. There is no slip (in an
ideal gear). The tongue width is infinite (the teeth don't
allow any detuning).

A gearbox with multiple stages is a COMPOSITION of rationals:

    Stage 1: T₁/T₂
    Stage 2: T₃/T₄
    Overall: (T₁ × T₃) / (T₂ × T₄)

This is the mediant structure: each stage inserts a new rational
between the input and output frequencies. The gearbox IS the
Stern-Brocot tree, with each gear stage being one level of the
tree.

### The Ouroboros gearbox

Connect the output shaft back to the input shaft through the
gear train:

```
    Input → [Stage 1] → [Stage 2] → ... → [Stage N] → Input
```

The output drives the input. The self-consistent gear ratio
is x = f(x) — the fixed point of the gear train's transfer
function.

**What happens physically:**

- If the total gear ratio > 1: the output spins faster than the
  input. Each cycle, the speed increases. The system accelerates
  without bound... unless friction (decoherence, D) limits it.
  The steady state: the gear train spins at the speed where the
  driving torque (from the feedback) equals the friction torque.
  This is the self-consistent |r|.

- If the total gear ratio = 1: the system maintains whatever
  speed it's given. No acceleration, no deceleration. A perfect
  flywheel. This is the x = f(x) = x trivial fixed point.

- If the total gear ratio < 1: the output spins slower. Each
  cycle, the speed decreases. The system decelerates to zero...
  unless an external drive compensates. With an external drive:
  the steady state is the speed where the drive power equals the
  deceleration from the gear ratio. Another fixed point.

### The non-trivial Ouroboros

The interesting case: a gearbox where the ratio CHANGES with
speed (nonlinear gears, variable-ratio transmission).

    f(ω) = ω × R(ω)

where R(ω) is the speed-dependent gear ratio. The fixed point:

    ω* = ω* × R(ω*)  →  R(ω*) = 1

The system settles to the speed where the effective gear ratio
is exactly 1. This speed is determined by the shape of R(ω) —
the nonlinear gear profile.

**Design principle:** choose the gear profile R(ω) so that
R(ω) = 1 at the desired operating speed. The Ouroboros
automatically seeks and maintains that speed. No control system
needed. The gearbox IS the controller.

### The mechanical devil's staircase

A continuously variable transmission (CVT) with a specific
nonlinear profile:

    R(ω) = the devil's staircase function W(ω)

At each rational ω = p/q, the transmission ratio locks to p/q
(the gear teeth engage). Between rationals, the ratio slides
continuously (the CVT adjusts). The result: a transmission that
preferentially locks to rational gear ratios (stable, efficient,
no slip) and smoothly transitions between them.

This is a physical implementation of the Stern-Brocot tree as a
mechanical device. The "teeth" are the tongues. The smooth
transitions are the gaps. The staircase is the transfer function.

---

## Particle Trajectories as Tongue Sequences

### The Feynman diagram is a Stern-Brocot path

In the framework, a particle propagating through space is a
gate sweep (D31). The speed is c (the gate propagation speed).
An interaction (vertex in a Feynman diagram) is a tongue
boundary crossing — a D-state traversal where the particle's
mode-locking changes.

Each vertex in a Feynman diagram corresponds to:
- Two incoming modes (the parent fractions a/b and c/d)
- One outgoing mode (the mediant (a+c)/(b+d))
- Conservation of energy-momentum (betweenness: the mediant
  is between the parents)
- Selection of the simplest product (minimality: the mediant
  has the smallest denominator)

The Feynman diagram IS the Stern-Brocot tree drawn sideways,
with time flowing left to right.

### Predictable trajectories given starting conditions

If you know:
- The initial mode (which tongue: p/q)
- The coupling K at the interaction point
- The modes of the other incoming particles

Then the framework predicts:
- The outgoing mode (the mediant, determined by adjacency)
- The probability of the interaction (the tongue width at
  the outgoing mode: 1/q_out²)
- The kinematics (energy-momentum from the mediant's value)

This is deterministic given the starting conditions. The
Stern-Brocot tree IS the S-matrix: it tells you the output
of any scattering event from the inputs.

### Constraints from known laws

The framework's predictions must be consistent with:

**Conservation of energy-momentum:** guaranteed by betweenness
(the mediant is between the parents on the frequency axis).

**CPT symmetry:** guaranteed by the figure-8 topology (C = loop
swap, P = mode swap, T = twist reversal, CPT = identity).

**Spin-statistics:** guaranteed by the figure-8 crossing
(fermions = loops, pick up sign under twist; bosons = crossings,
no sign pickup).

**Unitarity (probability conservation):** guaranteed by
compactness (S¹ compact → |r| ≤ 1 → the S-matrix is bounded
→ probabilities sum to 1).

**Gauge invariance:** guaranteed by the GCD reduction (reducing
a fraction doesn't change the physics, just the representation).

Each "known law" is a CONSEQUENCE of the four primitives, not
an additional constraint. The framework doesn't need to be
checked against these laws — it derives them.

### Cross-sections from tongue widths

The scattering cross-section for a process at mode p/q:

    σ(p/q) ∝ w(p/q)² = 1/q⁴

(The Born rule: probability ∝ Δθ² ∝ w².)

The cross-section decreases as the FOURTH power of the
denominator. Simple processes (low q) have large cross-sections.
Complex processes (high q) are rare. This is the standard
perturbative expansion — but derived from the tongue structure,
not from a coupling constant expansion.

The ratio of cross-sections:

    σ(q=2) / σ(q=3) = (1/16) / (1/81) = 81/16 = 5.0625

This predicts the ratio of weak to strong interaction
cross-sections at tree scale. The running (K → μ mapping)
modifies this at observation scale.

---

## The Perfect Clock: the Ouroboros oscillator

The simplest implementation of the framework:

```
[Oscillator] → [Frequency divider (÷q)] → [Phase comparator] → [Oscillator]
```

The oscillator's output is divided by q, compared to a reference,
and the error drives the oscillator. The fixed point: the
oscillator runs at exactly q × f_reference.

This IS a phase-locked loop (PLL). The framework adds: the PLL's
lock range is the Arnold tongue at p/q. The acquisition time is
τ ∝ 1/√ε. The phase noise is Δθ ∝ √ε. The product τ × Δθ = const.

The Ouroboros version: remove the external reference. Feed the
divided output back directly:

```
[Oscillator] → [÷q] → [Phase comparator] → [Oscillator]
                 ↑                              |
                 └──────────────────────────────┘
```

The oscillator locks to the frequency where its divided output
matches its own phase. This is x = f(x). The frequency is
self-determined. No reference. No external input. The oscillator
IS the reference.

The self-referential PLL runs at a frequency determined by
the divider ratio q and the phase comparator's transfer function.
For a linear phase comparator: any frequency works (trivial
fixed point). For a NONLINEAR phase comparator (the parabola):
the saddle-node selects a unique frequency. The Ouroboros
oscillator has one specific self-consistent frequency.

This is a crystal oscillator without the crystal. The
"crystal" is the self-consistency condition. The frequency
stability comes from the fixed-point attractor, not from a
physical resonator.

---

## Summary

| Design | What it computes | The fixed point |
|--------|-----------------|-----------------|
| Round robin ring | Winding number p/q | Mode-locked steady state |
| Ouroboros gearbox | Self-consistent speed ω* | R(ω*) = 1 |
| Mechanical staircase | The devil's staircase | CVT transfer function |
| Particle trajectory | Scattering output | Mediant of input modes |
| Ouroboros oscillator | Self-consistent frequency | f = f(f) without reference |

Each is a physical implementation of x = f(x) applied to a
specific domain. The framework doesn't just predict — it DESIGNS.
The tongue structure tells you what to build. The fixed point
tells you what it will do. The look-ahead tells you how it will
get there.
