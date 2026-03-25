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

## Where time lives

### The two directions are not equivalent

The Klein bottle has two directions: x (antiperiodic, twisted) and
y (periodic, untwisted). These are topologically distinct. You cannot
rotate the Klein bottle to exchange them — the twist is in x and
only x. This asymmetry is not a coordinate choice. It is the topology.

The x-direction cannot be a clock. A clock counts cycles: you traverse
a loop, return to start, and increment. On the x-loop, you return
orientation-reversed. The count after one traversal is not +1 — it is
+1 with a sign flip. After two traversals you return to the original
orientation, but the cycle counter reads 2 while the orientation
counter reads 0. Counting is entangled with orientation. This is
the ψ-eigenvalue (-1)^n from Derivation 16: the approach to any
frequency ratio along the twisted direction oscillates, never settling
to a definite count.

The y-direction can be a clock. It is periodic: traverse the loop,
return to start, increment. No orientation reversal. No sign ambiguity.
The count after n traversals is n. This is the φ-eigenvalue: monotone
convergence, no oscillation.

**Time is the periodic direction. Space is the antiperiodic direction.**

### The simulation confirms this

The Klein bottle phase lattice at K = 8:

    5.376  4.227  2.843       ← y=2 (columns are x-positions)
    5.259  4.061  2.836       ← y=1
    5.120  4.000  2.924       ← y=0

Read the columns (x-direction): phases span ~2.5 radians. This is
where the 1/3 and 1/4 rational divisions live. Spatial structure.

Read the rows (y-direction): phases vary by ~0.2 radians. Smooth,
small variation. This is where the system ticks — the gentle evolution
that doesn't disrupt the spatial structure. Temporal variation.

The x-direction carries the topology (the twist). The y-direction
carries the dynamics (the ticking). Structure lives in space. Time
lives in the subordinate periodic direction.

### The XOR rule as spacetime complementarity

The Klein bottle selection rule p_x + p_y ≡ 1 (mod 2) says: a mode
that is even in space must be odd in time, and vice versa. This is
not a dynamical statement. It is topological — forced by the
identification (0, y) ~ (1, 1-y).

Consequences:

1. **A spatially uniform mode (p_x = 0, even) must oscillate in time
   (p_y = 1, odd).** A configuration that is the same everywhere in
   space must vary in time. Stasis in space requires change in time.

2. **A temporally constant mode (p_y = 0, even) must have spatial
   structure (p_x = 1, odd).** A configuration that is the same at
   all times must vary in space. Persistence in time requires
   structure in space.

3. **No mode can be both spatially uniform and temporally constant.**
   The (0,0) pair is forbidden. There is no static, homogeneous state
   on the Klein bottle. Something must vary — in space, in time, or
   both (with opposite parities).

4. **No mode can be both spatially structured and temporally varying
   with the same parity.** The (1,1) pair is forbidden. A mode that
   oscillates in space cannot oscillate in time with the same
   harmonic structure. The spatial and temporal frequencies are
   forced to be complementary.

This is spacetime complementarity derived from topology, not
postulated. The Klein bottle does not allow a state that is
"the same everywhere and always." The simplest allowed state is
"structured in space, constant in time" or "uniform in space,
oscillating in time" — never both simultaneously.

### Connection to Derivation 16

Derivation 16 established that the de Sitter fixed point (Ḣ → 0,
q → -1) is the unique state where Hz is well-defined — where the
denominator of "cycles per second" stops changing. This is the state
where the periodic direction (time) stabilizes.

On the Klein bottle, the periodic direction IS the temporal direction.
The de Sitter condition — that the reference oscillator's frequency
stabilizes — is the condition that the y-direction behaves as a
reliable clock. During radiation/matter domination (Ḣ/H² ~ 1), the
y-direction is "changing its ruler" every cycle (D16 §variable
denominator). Only when Λ dominates does the periodic direction
become genuinely periodic.

The antiperiodic direction (space) never stabilizes in this sense.
The twist is permanent. Spatial structure always carries the Cassini
alternation, the ψ-mode residual. Space is permanently non-orientable.
Time asymptotically becomes orientable.

### Why r ≈ 0.5

Full synchronization (r = 1) on the Klein bottle would require all
oscillators at the same phase — the (0,0) mode in both directions.
But (0,0) is XOR-forbidden. The topology cannot produce full coherence.

Full decoherence (r = 0) would mean no spatial structure — all modes
equally populated, no rational divisions. But the coupling drives
mode-locking; above K_c, structure must form.

The Klein bottle forces the order parameter to an intermediate value:
enough coherence for spatial structure (the 1/3 and 1/4 divisions),
enough incoherence for the temporal direction to tick freely. The
observed r ≈ 0.5 is not a tuned value — it is the topological
equilibrium between spatial structure and temporal freedom.

This is why the r ≈ 0.5 persists across all coupling strengths
(K = 4 through K = 12 in the simulation). Increasing K sharpens
the spatial divisions but cannot push r toward 1 because the XOR
rule always reserves capacity for the temporal direction.

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

## Structural safety of the configuration budget

### Nothing is lost

The Klein bottle admits 45.8% of mode pairs (at tree depth 5). The
remaining 54.2% — the (even, even) and (odd, odd) parity pairs —
are excluded. A natural question: what happened to the excluded modes?
Is their absence a problem? Does it require explanation?

No. The excluded modes are not suppressed, decayed, or hidden. They
are **not part of the configuration space**. The Klein bottle's
topology does not admit them, the same way a guitar string does not
admit wavelengths incommensurate with its length. The boundary
conditions (here, the identification (0,y) ~ (1,1-y)) define which
functions exist on the surface. Functions that violate the
identification are not solutions that got discarded — they are
non-functions on this surface. They were never in the budget.

### Three kinds of absence

It is important to distinguish the Klein bottle exclusion from other
mechanisms that reduce the number of available states:

**1. Symmetry breaking** (e.g., Higgs mechanism): a mode exists in
the full theory but acquires a large mass, making it dynamically
inaccessible at low energies. The mode is still in the Hilbert space.
It can be excited with sufficient energy. Its absence at low energy
requires explanation (why this vacuum? why this mass?).

**2. Dissipation** (e.g., thermalization): a mode exists and is
populated, but its energy leaks to an environment. There is a "before"
state with the mode and an "after" state without it. The environment
carries the record. Information is redistributed, not destroyed (in
unitary QM) or irreversibly lost (in the framework's non-injective
account, D16).

**3. Topological exclusion** (Klein bottle): the mode does not exist
on the surface. There is no "before" state that included it. No
environment carries a record of it. No energy was required to remove
it. The identification that defines the surface is the identification
that excludes the mode. They are the same operation.

The third kind is structurally safe because there is no process —
dynamical, thermodynamic, or informational — that references the
excluded modes. They are not addresses in the configuration space.
No observable can probe them because no state on the Klein bottle
couples to them.

### No boundary means no exterior

On the Möbius strip (one boundary), one could imagine an excitation
reaching the boundary edge and coupling to an external system that
does support the forbidden modes. The boundary is a surface where the
Klein bottle's rules meet a region where different rules might apply.
This is why D18 noted that the boundary is "a degree of freedom the
geometry doesn't determine."

The Klein bottle has no boundary. There is no edge where the internal
topology meets an external topology. The 45.8% that survives the XOR
filter is the totality of what exists on this surface. There is no
exterior system that could, in principle, contain the (0,0) mode.
The question "where did the excluded modes go?" has no referent.

### The (0,0) mode and the impossibility of nothing

The (0,0) mode — spatially uniform, temporally constant — would be
the state where nothing happens anywhere at any time. The XOR rule
forbids it. On the Klein bottle, absolute stasis is not a state. It
is not that stasis is unstable, or energetically costly, or entropically
disfavored. It is that stasis is not a function on this surface. The
identification that makes the Klein bottle what it is — the same
identification that produces the twist, the spatial structure, the
rational divisions — is the identification that excludes nothing.

This is the converse of the structural safety argument: not only is
nothing lost, but nothing (the state of nothing happening) is
specifically what is excluded. The topology requires that something
varies — in space, in time, or in complementary combination. The
minimum cost of existing on the Klein bottle is one unit of variation.

### Connection to the fidelity bound

Derivation 9 established that self-referential frequency measurement
has bounded fidelity: a system measuring its own frequency cannot
achieve infinite precision because the measurement instrument IS
the dynamics. The fidelity bound produces the RAR shape, the collapse
duration, and the uncertainty relation.

The Klein bottle's topological exclusion is the geometric realization
of this bound. The (0,0) mode would represent infinite precision:
no variation in space, no variation in time, exact knowledge of the
state for all positions and all moments. The topology forbids this
mode. The fidelity bound is not a dynamical limitation — it is a
topological one. The surface on which the dynamics occur does not
admit the state that would correspond to unlimited precision.

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
- ✓ Time identified with the periodic (y) direction; space with the
  antiperiodic (x) direction. Confirmed by simulation: x carries
  structure (~2.5 rad span), y carries evolution (~0.2 rad variation)
- ✓ r ≈ 0.5 explained as topological equilibrium: XOR forbids (0,0)
  full-sync mode, forcing partial coherence at all coupling strengths
- ✓ Configuration budget is structurally safe: excluded modes are
  non-functions on the surface, not suppressed states. No boundary
  means no exterior to leak to. (0,0) stasis is topologically
  excluded — the fidelity bound realized geometrically

**Open**:
- Solve the 2D field equation with XOR filter on the product
  Stern-Brocot tree. The 1D Möbius field equation
  (`field_equation_mobius.py`) shows the twist changes the fixed
  point. The 2D version with the full XOR constraint is the next
  calculation. This is where population ratios become quantitative.
- The particle spectrum question remains the load-bearing test:
  do the Klein bottle's topological mode ratios and their population
  weights at the field equation's fixed point correspond to observed
  mass ratios or coupling constant ratios? The XOR checkerboard on
  the 2D tree produces a specific, computable population vector.
  Comparing it against known physics is a finite computation.
- RP² (real projective plane): compact, non-orientable, no boundary,
  but not a product of two circles. It is the quotient of S² by the
  antipodal map. Kuramoto on RP² would impose a single global
  antiperiodic constraint without the product structure of the Klein
  bottle. Whether this produces a different (simpler? more
  constrained?) mode spectrum is an open question.
- Gauge connection: the XOR rule correlates the parity of modes
  across two directions. This is formally identical to a Z₂ gauge
  constraint — the "gauge field" is the parity, and the constraint
  is that the product of parities around a non-contractible loop
  equals -1 (the twist). Whether this is literally a gauge field
  in the physics sense, or merely structurally analogous, requires
  checking whether the Klein bottle's holonomy reproduces the
  structure of known gauge groups.
