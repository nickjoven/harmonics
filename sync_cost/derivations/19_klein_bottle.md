# Derivation 19: The Klein Bottle

## Claim

The Möbius strip (Derivation 18) has one boundary. Excitations reflect
off that boundary, which is why the container works — but the boundary
is a degree of freedom the geometry doesn't determine. The Klein bottle
is the compact, non-orientable surface with **no boundary**. Nothing
enters, nothing exits, nothing reflects — everything circulates. It is
the fully closed variant of the Möbius container.

On the Klein bottle, the Kuramoto self-consistency equation has two
independent antiperiodic directions. The topology imposes two
simultaneous constraints on which rational phase divisions can form.
The intersection of these two constraints is more restrictive than
either alone — fewer modes survive, and those that do are locked by
two independent boundary conditions, not one.

If the particle spectrum question has an answer in this framework,
it is here.

## The Klein bottle as a quotient

### Construction

The Klein bottle K² is the quotient of the unit square [0,1] × [0,1]
under two identifications:

    (x, 0) ~ (x, 1)           periodic in y (like a torus)
    (0, y) ~ (1, 1-y)         antiperiodic in x (the twist)

The first identification rolls the square into a cylinder. The second
glues the cylinder ends with a reflection — the Möbius half-twist,
but now applied to a closed surface rather than a strip.

### Comparison with other compact surfaces

| Surface | Orientable | Boundary | x-BC | y-BC |
|---------|-----------|----------|------|------|
| Torus T² | Yes | None | periodic | periodic |
| Cylinder | Yes | Two | periodic | free |
| Möbius strip | No | One | antiperiodic | free |
| Klein bottle K² | No | None | antiperiodic | periodic |

The Klein bottle is the unique compact non-orientable surface obtainable
from a rectangle by edge identifications without self-intersection in 4D.
(In 3D it self-intersects, but topologically it is well-defined.)

### Why no boundary matters

On the Möbius strip, the boundary at w = 0 is where modes reflect.
The reflection conditions couple to the dynamics — different boundary
conditions (free, fixed, mixed) give different mode spectra. This is
an input the geometry doesn't fix.

On the Klein bottle, there is no boundary. The mode spectrum is
determined **entirely** by the topology. No boundary conditions to
choose. The only inputs are the surface itself and the coupling.

## Kuramoto on the Klein bottle

### Oscillator lattice

Place N_x × N_y oscillators on the Klein bottle:

    θ_{i,j}(t),    i = 1,...,N_x,   j = 1,...,N_y

with nearest-neighbor coupling in both directions.

### Boundary conditions

**y-direction (periodic):**

    θ_{i, N_y+1} = θ_{i, 1}
    θ_{i, 0}     = θ_{i, N_y}

**x-direction (antiperiodic with reflection):**

    θ_{N_x+1, j} = θ_{1, N_y+1-j} + π
    θ_{0, j}     = θ_{N_x, N_y+1-j} - π

The x-wrap both shifts phase by π (the half-twist) AND reverses the
y-coordinate (the reflection). This is the Klein bottle identification.

### Dynamics

    dθ_{i,j}/dt = ω_{i,j}
        + (K_x/2)[sin(θ_{i+1,j} - θ_{i,j}) + sin(θ_{i-1,j} - θ_{i,j})]
        + (K_y/2)[sin(θ_{i,j+1} - θ_{i,j}) + sin(θ_{i,j-1} - θ_{i,j})]

where the neighbors at the boundaries are given by the identifications
above. K_x and K_y are the coupling strengths in each direction; if
K_x = K_y the coupling is isotropic.

### Mode analysis

On the torus (both directions periodic), the allowed spatial modes are:

    exp(2πi m x/L_x) × exp(2πi n y/L_y),    m, n ∈ Z

On the Klein bottle, the antiperiodic+reflected x-BC restricts the modes.
A function f(x,y) on the Klein bottle must satisfy:

    f(x + L_x, y) = f(x, L_y - y) × e^{iπ}    [antiperiodic + reflection]
    f(x, y + L_y) = f(x, y)                     [periodic]

The y-direction Fourier modes exp(2πi n y/L_y) are standard. The
x-direction modes must satisfy:

    φ_m(x + L_x) × ψ_n(L_y - y) = -φ_m(x) × ψ_n(y)

Using ψ_n(L_y - y) = ψ_{-n}(y) = ψ_n*(y):

    φ_m(x + L_x) = -φ_m(x) × ψ_n(y)/ψ_n*(y)

For this to be consistent (x-part independent of y), we need:

**Case 1: n = 0** (y-constant mode)
    φ_m(x + L_x) = -φ_m(x)
    → antiperiodic in x: m = (2k+1)/2 for integer k
    → half-integer x-modes

**Case 2: n ≠ 0** (y-varying mode)
    The reflection pairs (n, -n). Self-consistent modes combine:
    cos(2πny/L_y) with antiperiodic x-modes: φ_m(x+L_x) = -φ_m(x)
    sin(2πny/L_y) with periodic x-modes: φ_m(x+L_x) = +φ_m(x)

The spectrum splits:

| y-mode | x-mode type | x-wavenumbers | Notes |
|--------|------------|---------------|-------|
| n = 0 (constant) | antiperiodic | (2k+1)π/L_x | Half-integer only |
| cos(2πny/L_y), n > 0 | antiperiodic | (2k+1)π/L_x | Even y × odd x |
| sin(2πny/L_y), n > 0 | periodic | 2kπ/L_x | Odd y × even x |

The total mode count is the same as the torus — no modes are lost. But
the **pairing** between x and y modes is locked by the topology. You
cannot have (even x, even y) or (odd x, odd y) independently. The Klein
bottle forces a correlation between the two directions.

### The Klein bottle selection rule

Define the **parity pair** (p_x, p_y) where p_x = 0 for integer
x-modes and p_x = 1 for half-integer, and p_y = 0 for cosine (even)
y-modes and p_y = 1 for sine (odd) y-modes.

The Klein bottle enforces:

    p_x + p_y = 1 (mod 2)

That is: **opposite parities only.** (even x, odd y) and (odd x, even y)
are allowed. (even, even) and (odd, odd) are forbidden.

This is the XOR constraint. In the language of the Stern-Brocot tree:
if we index modes by two rationals (p₁/q₁, p₂/q₂) for the x and y
directions respectively, the Klein bottle allows only those pairs where
exactly one of the two has the Möbius-compatible parity.

### Relation to D18 field equation results

Derivation 18's field equation on the Möbius domain showed:
- Even-denominator modes dominate (71% vs 57% periodic)
- Odd-denominator modes suppressed by (-1)^q twist
- Fibonacci backbone broken at levels where p+q is even

On the Klein bottle, the constraint is tighter: BOTH directions are
constrained simultaneously, and the XOR rule means the allowed modes
form a subset that neither direction alone would select.

The field equation on the Klein bottle is:

    N(p₁/q₁, p₂/q₂) = N_total × g(p₁/q₁, p₂/q₂)
                        × w(p₁/q₁, K_eff) × w(p₂/q₂, K_eff)

subject to the constraint that only XOR-paired modes are counted in
the order parameter:

    r = Σ N(p₁/q₁, p₂/q₂) × exp(2πi(p₁/q₁ + p₂/q₂))
        × (-1)^{q₁}    [twist in x-direction]

where the sum runs only over pairs with p_x + p_y ≡ 1 (mod 2).

## Minimal simulation: N_x × N_y = 3 × 3

Nine oscillators on the Klein bottle. This is the minimal 2D system.

### Coupling matrix

The 9 oscillators are indexed (i,j) with i,j ∈ {1,2,3}.

Neighbors in x-direction (with Klein bottle wrap):
- (1,j) left neighbor: (3, 4-j) with phase shift -π
- (3,j) right neighbor: (1, 4-j) with phase shift +π

Neighbors in y-direction (periodic):
- (i,1) bottom neighbor: (i,3)
- (i,3) top neighbor: (i,1)

### Equations (K_x = K_y = K for isotropy)

For interior oscillator (2,2):

    dθ_{2,2}/dt = ω_{2,2}
        + (K/2)[sin(θ_{3,2} - θ_{2,2}) + sin(θ_{1,2} - θ_{2,2})]
        + (K/2)[sin(θ_{2,3} - θ_{2,2}) + sin(θ_{2,1} - θ_{2,2})]

For boundary oscillator (1,1), left neighbor wraps:

    dθ_{1,1}/dt = ω_{1,1}
        + (K/2)[sin(θ_{2,1} - θ_{1,1}) + sin(θ_{3,3} - π - θ_{1,1})]
        + (K/2)[sin(θ_{1,2} - θ_{1,1}) + sin(θ_{1,3} - θ_{1,1})]

The θ_{3,3} - π term is the Klein bottle identification:
(0, 1) wraps to (N_x, N_y+1-1) = (3, 3) with phase shift -π.

### Predicted fixed points

For identical frequencies ω_{i,j} = ω₀, the XOR selection rule
predicts the lowest-energy configuration distributes phase as:

    θ_{i,j} = α × i + β × j + π × floor(i/N_x) × (N_y+1-2j)/(...)

The exact form requires solving the 9-oscillator system, but the
structure is: a linear phase gradient in each direction, with the
Klein bottle identification locking the relationship between the
two gradients.

The key prediction: the ratio of the x-gradient to the y-gradient
is a rational number forced by the topology, not a free parameter.
On the torus, both gradients are independently free. On the Klein
bottle, the XOR constraint locks them.

## Parameters

For the 3×3 Klein bottle simulation:

1. **N_x = N_y = 3** — minimum 2D system
2. **K** — isotropic coupling; scan K/K_c from 0 to 3
3. **ε** — perturbation of single oscillator from rest
4. **g(ω)** — Lorentzian in both directions (admits Ott-Antonsen)

Compare against:
- **Torus** (periodic × periodic): same lattice, no twist
- **Möbius cylinder** (antiperiodic × free): D18's 1D case extended
- **Klein bottle** (antiperiodic × periodic): the target

## Connection to the field equation

The 2D field equation on the Klein bottle indexes modes by pairs
of rationals from the Stern-Brocot tree. The XOR selection rule
partitions the 2D tree into two classes:

**Allowed (XOR = 1):**
- (1/2, 1/3): even q₁, odd q₂ → (0,1) ✓
- (1/3, 1/2): odd q₁, even q₂ → (1,0) ✓
- (2/3, 1/4): odd q₁, even q₂ → (1,0) ✓

**Forbidden (XOR = 0):**
- (1/2, 1/4): even q₁, even q₂ → (0,0) ✗
- (1/3, 2/3): odd q₁, odd q₂ → (1,1) ✗

The allowed modes form a checkerboard pattern on the 2D Stern-Brocot
lattice. The population at the field equation's fixed point, restricted
to this checkerboard, is the Klein bottle's mode spectrum.

The question is whether this checkerboard-filtered fixed point produces
population ratios that match anything physical.

## Connection to existing derivations

| This derivation | Builds on | What it adds |
|---|---|---|
| Klein bottle topology | D18 (Möbius container) | Removes boundary; two-direction constraint |
| XOR selection rule | D18 (odd-mode selection) | Couples x and y mode parities |
| 2D field equation | D11 (rational field equation) | Extends to product of two Stern-Brocot trees |
| Mode pairing | D16 (half-twist topology) | Second twist direction; correlation between scales |
| 3×3 minimum | D6 (N=3 minimum) | N=3 in EACH direction; 9 = 3² total |

## Simulation results

### 3×3 Klein bottle vs torus (`klein_bottle_kuramoto.py`)

The simulation ran at K = 4, 6, 8, 12 on identical 3×3 lattices with
Lorentzian frequency disorder (γ = 1), single-oscillator perturbation
from rest, and 20,000 integration steps (T = 200, dt = 0.01).

**Order parameter:**

| K | Torus r | Klein r | Ratio |
|---|---------|---------|-------|
| 4 | 0.979 | 0.478 | 0.49 |
| 6 | 0.991 | 0.547 | 0.55 |
| 8 | 0.995 | 0.577 | 0.58 |
| 12 | 0.998 | 0.607 | 0.61 |

The torus approaches full synchronization at all couplings. The Klein
bottle saturates near r ≈ 0.5–0.6 — partial coherence forced by
topology, not insufficient coupling.

**Phase divisions are topological invariants.** At every K tested,
the x-direction phase differences on the Klein bottle lock to 1/3
and 1/4 of 2π. These do not change with coupling strength — they
sharpen. The torus shows only 0/1 (trivial sync) at all K.

**Phase lattice (K = 8, representative):**

    Klein:                    Torus:
    5.376  4.227  2.843       4.264  4.198  4.025
    5.259  4.061  2.836       4.150  4.049  3.957
    5.120  4.000  2.924       4.033  3.988  3.982

The Klein bottle distributes phase across a ~2.5 radian span with
three distinct columns. The torus collapses to a ~0.28 radian spread.

**Larger lattices and aspect ratios:**

| Lattice | Torus r | Klein r |
|---------|---------|---------|
| 3×3 | 0.995 | 0.577 |
| 5×5 | 0.806 | 0.563 |
| 3×5 | 0.842 | 0.517 |

The Klein bottle order parameter is stable across lattice sizes and
aspect ratios. The 3×5 asymmetric case (N_x ≠ N_y) shows the same
1/3 and 1/4 x-direction locking as the symmetric case — the mode
spectrum does not depend on aspect ratio.

### XOR filter on Stern-Brocot pairs

At tree depth 5 (31 nodes):
- Total pairs: 961
- Allowed (XOR = 1): 440 (45.8%)
- Forbidden (XOR = 0): 521 (54.2%)

The (q_x, q_y) occupancy table confirms the checkerboard: nonzero
entries only where one of q_x, q_y is even and the other odd.

**Fibonacci backbone on Klein bottle:** The convergent pair table
reveals the selection: (1/2, 2/3) ✓ but (1/2, 1/2) ✗. (2/3, 5/8) ✓
but (2/3, 2/3) ✗. No self-pairing allowed. The backbone is
necessarily heterogeneous — each allowed pair mixes two different
Fibonacci levels, one from each parity class.

## Status

**Established**:
- ✓ 3×3 simulation completed: Klein bottle forces 1/3 and 1/4 phase
  divisions at all coupling strengths (K = 4, 6, 8, 12)
- ✓ Torus comparison: trivial sync (r → 0.99) vs structured partial
  coherence (r ≈ 0.48–0.61)
- ✓ XOR filter verified: 45.8% of mode pairs survive on depth-5 tree
- ✓ Aspect ratio independence: 3×5 lattice shows same x-direction
  locking as 3×3 — topology, not geometry, determines structure
- ✓ Fibonacci backbone checkerboard: no self-pairing, heterogeneous
  level mixing forced

**Open**:
- Solve the 2D field equation with XOR filter (extend
  `field_equation_mobius.py` to product tree)
- Does the gradient ratio (x-direction / y-direction) lock to a
  specific rational? The simulation shows both gradients average to
  zero (the lattice is too small for a net gradient to form); larger
  lattices or continuous-limit analysis needed
- The real projective plane RP² (compact, non-orientable, no boundary,
  no product structure) as the irreducible non-orientable surface —
  what does Kuramoto look like there?
- Connection to gauge theory: the Klein bottle's XOR constraint
  correlates modes across directions. Is this the structure of a
  gauge field — a constraint on how phases relate across dimensions?
- The particle spectrum question: compare the Klein bottle's
  topological mode ratios (1/3, 1/4) and their population weights
  against known mass ratios or coupling constant ratios
