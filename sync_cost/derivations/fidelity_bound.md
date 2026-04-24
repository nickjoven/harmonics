# The Self-Referential Fidelity Bound

## Claim

The MOND transition and wavefunction collapse are instances of the
same structure: a system measuring which attractor it belongs to,
using dynamics constituted by the same process being measured. The
fidelity of this self-measurement is bounded, and the bound determines:

1. The shape of the RAR interpolating function (MOND)
2. The collapse duration τ ∝ 1/√ε (quantum measurement)
3. The τ × Δθ = const uncertainty relation
4. The quantum Zeno effect

All four follow from one fact: resolving a frequency requires
accumulating cycles, and the available cycles are bounded by the
reference oscillator's own period.

## The frequency resolution bound

Any oscillator measuring a frequency difference Δω against a
reference at frequency ω_ref requires observation time:

    T_obs ≥ 1/Δω

to distinguish the two frequencies. This is not quantum mechanics —
it is the Fourier uncertainty of any periodic process. A pendulum
cannot determine its own frequency to better than 1/T in time T.

The maximum observation time is set by the reference oscillator:

    T_max ~ 1/ω_ref

Therefore the minimum resolvable frequency difference is:

    Δω_min ~ ω_ref

The system cannot distinguish ω from ω_ref when |ω - ω_ref| ≲ ω_ref.
The transition is inherently O(1)-fuzzy in units of the reference
frequency.

## Instance 1: The MOND transition

A circular orbit is a gravitational pendulum (Derivation 3):

    ω_orbit² = g(R) / R

The cosmic reference oscillator has frequency H. The critical
acceleration is:

    a₀ = cH/(2π)

corresponding to ω_orbit = H. The frequency resolution bound says
the transition between "locked to H" and "free from H" is smooth,
not sharp. The system cannot determine which side of a₀ it is on
when g ≈ a₀ — because the measurement instrument (the orbit itself,
ticking at ω_orbit) runs at the same rate as the reference (H).

### The RAR shape from the fidelity bound

The McGaugh+2016 interpolating function:

    g_obs = g_bar / [1 - exp(-√(g_bar/a₀))]

has the form of a resolution function. Define x = g_bar/a₀ =
(ω_orbit/H)². Then:

    g_obs/g_bar = 1 / [1 - exp(-√x)]

The exponential rollover encodes how many "cycles of evidence" the
orbit has accumulated:

- x >> 1 (g >> a₀, ω >> H): many cycles per Hubble time. The orbit
  resolves itself as Newtonian with high fidelity. g_obs → g_bar.

- x ~ 1 (g ~ a₀, ω ~ H): O(1) cycles. The orbit cannot resolve
  which regime it belongs to. Transition zone.

- x << 1 (g << a₀, ω << H): fewer than one cycle per Hubble time.
  The orbit is fully entrained. g_obs → √(g_bar × a₀) (deep MOND).

The interpolating function is not phenomenological — it is the
transfer function of a self-referential frequency measurement with
bounded fidelity.

### Observational consequence

The scatter in the RAR should be maximal at g_bar ≈ a₀ and decrease
on both sides. This is observed (Lelli+2017, McGaugh+2016). The
scatter is not measurement noise — it is the physical indeterminacy
of a frequency comparison at its resolution limit.

## Instance 2: Wavefunction collapse

A quantum system between two attractors (Arnold tongues at winding
numbers W₁ and W₂) has frequency gap:

    Δω = |ω₁ - ω₂|

To determine which attractor it will lock to, the system must
accumulate enough phase to resolve Δω. The time required:

    τ_resolve ~ 1/Δω

This is the collapse duration. Near a tongue boundary (small ε),
the gap closes:

    Δω ∝ √ε    (saddle-node normal form, Derivation 1)

Therefore:

    τ ∝ 1/√ε

which is the collapse scaling from Derivation 7. The same result,
from a frequency resolution argument instead of a Floquet multiplier
calculation.

### The uncertainty relation

The basin separation (amplitude) at the tongue boundary:

    Δθ ∝ √ε    (Born rule, Derivation 1)

The collapse time:

    τ ∝ 1/√ε   (frequency resolution bound)

Therefore:

    τ × Δθ = const

This is the measurement uncertainty relation from Derivation 7, now
understood as a frequency resolution identity: the product of "how
long it takes to resolve" and "how much there is to resolve" is set
by the geometry of the frequency landscape, not by ħ specifically.

ħ enters when we convert from circle map iterations to physical time.
The uncertainty relation is more fundamental than ħ — it holds for
any system resolving a frequency gap against a finite-rate clock.

### The Zeno effect

Continuous measurement resets the phase accumulation at every step.
The system never accumulates enough cycles to resolve Δω. It remains
in the gap between tongues — indefinite superposition. This is the
Zeno effect: not a quantum mystery, but the Fourier limit of
interrupted frequency measurement.

## The unifying structure

Both instances share the same logic:

| | MOND transition | Wavefunction collapse |
|---|---|---|
| **System** | Circular orbit | Quantum state |
| **Reference** | Hubble clock H | Environmental mean field |
| **Observable** | g_bar/a₀ | ε (tongue depth) |
| **Frequency gap** | \|ω_orbit - H\| | Δω ∝ √ε |
| **Resolution time** | T_H ~ 1/H | τ ~ 1/√ε |
| **Fidelity limit** | RAR interpolating function | Collapse uncertainty τΔθ = const |
| **Deep in regime** | Newtonian or deep MOND | Locked or quasiperiodic |
| **At transition** | Smooth, O(1) scatter | Slow collapse, indeterminate |
| **Self-reference** | Orbit measures itself against cosmic clock it participates in | State resolves itself against field it constitutes |

The self-referential character is essential. In both cases:

1. The system IS an oscillator
2. It is trying to determine its own frequency relative to a reference
3. The reference is constituted (at least in part) by the system itself
4. The resolution is bounded because the measurement instrument and
   the measured quantity are the same dynamics

This is not a metaphor. The circle map θ_{n+1} = θ_n + Ω - (K/2π)sin(2πθ_n)
is literally a self-referential frequency equation: the phase θ
determines the effective frequency (through the sin term), which
determines the next phase. The fixed points of this self-reference
are the tongues. The fidelity of "which fixed point?" is bounded by
the gap structure of the staircase.

## Deriving the RAR interpolating function

The RAR is not a phenomenological fit. It is the fixed point of a
self-consistency equation.

### The self-referential equation

An orbit in a gravitational potential has baryonic acceleration g_bar
and total (observed) acceleration g_obs. The entrainment by the Hubble
clock provides additional acceleration proportional to g_obs itself:

    g_obs = g_bar + α × g_obs

where α is the coupling fraction — how much of the total acceleration
comes from entrainment. This is self-referential: g_obs appears on
both sides. The observed acceleration feeds back through the coupling.
The behavior describes itself.

Solving:

    g_obs = g_bar / (1 - α)

### The coupling fraction from tongue geometry

Inside an Arnold tongue, perturbations decay exponentially per
iteration with Floquet convergence rate λ:

    δθ_n ~ exp(-nλ)

The coupling fraction α is the entrainment that survives one
characteristic cycle:

    α = exp(-λ)

Near a tongue boundary, the convergence rate follows from saddle-node
universality (Derivation 1):

    λ ∝ √ε

where ε is the depth inside the tongue. Identifying ε with the
dimensionless acceleration ratio g_bar/a₀:

    α = exp(-√(g_bar/a₀))

### The RAR

Substituting:

    g_obs = g_bar / [1 - exp(-√(g_bar/a₀))]

This is the McGaugh+2016 interpolating function. Derived, not fit.

### The g_bar = 0 state

At g_bar = 0: α = exp(0) = 1. The coupling is total. The system is
maximally entrained — sitting at the center of the tongue, deepest
possible locking, maximum basin separation. This is a singular state:
any nonzero g_bar breaks the perfect coupling. α drops below 1 and
the system begins to separate from the cosmic clock.

This is the ground state of the gravitational tongue. It is unique
because:

1. It is the ONLY state where the entrainment coupling is complete
2. Any perturbation (any baryonic mass) can only reduce α
3. The orbit has zero frequency — it is the reference itself
4. Adding mass creates an orbit, which creates a frequency, which
   creates a detuning from H, which reduces the coupling

The RAR traces the trajectory away from this maximally coupled state
as g_bar increases. The deep MOND limit (g_obs → √(g_bar × a₀)) is
the regime where α ≈ 1 - √(g_bar/a₀), the first departure. The
Newtonian limit (g_obs → g_bar) is where α → 0 and the orbit has
fully decoupled from the cosmic clock.

### Why the components are necessary

Each piece has a structural origin:

- **Self-consistency** (g_obs on both sides): the orbit's frequency
  depends on g_obs, which determines the entrainment, which determines
  g_obs. The fixed point is the physics.

- **Exponential** (exp in α): Floquet theory. Inside a tongue,
  convergence is exponential per iteration. This is not a choice —
  it follows from the linearization of any smooth map near a fixed
  point.

- **Square root** (√ in the exponent): saddle-node universality. The
  convergence rate vanishes as √ε at the tongue boundary. This is the
  generic codimension-1 bifurcation for circle maps. The exponent 1/2
  is structurally stable — it cannot be perturbed away.

The entire interpolating function is determined by the tongue geometry.
No fitted factors. No fitting. The function that McGaugh+2016
discovered empirically is the transfer function of a self-referential
oscillator at a saddle-node bifurcation.

## Connection to kk-inference

The Kramers-Kronig early-exit mechanism (kk-inference) provides the
information-theoretic version of the same bound. In a transformer:

- Shallow layers compute the dispersive channel χ' (what changes)
- The KK relation predicts the dissipative channel χ'' (how much
  energy remains to change things)
- When χ'' → 0, remaining layers are inert — early exit

The fidelity of the χ'' prediction is bounded by the same structure:
you're predicting the cost of future computation from the computation
done so far. The prediction improves as you go deeper (more "cycles
of evidence"), but you can never achieve perfect fidelity without
running all the layers — which defeats the purpose of early exit.

The MOND transition is a gravitational early exit: once ω_orbit < H,
the detailed mass distribution is irrelevant. The quantum collapse
is a dynamical early exit: once the system resolves which tongue it
belongs to, the quasiperiodic exploration stops. Both: the dissipative
channel is exhausted, stop computing.

## Testable predictions

1. **RAR scatter vs g_bar/a₀**: The scatter should peak at g_bar ≈ a₀
   and decrease as (g_bar/a₀)^{-1/2} on the Newtonian side and as
   (g_bar/a₀)^{+1/2} on the MOND side. This is the resolution function
   of the frequency measurement. Current data (McGaugh+2016, Lelli+2017)
   shows this qualitative pattern; quantitative fits are a near-term test.

2. **Collapse timescale at threshold**: Systems near the quantum-classical
   boundary should show collapse duration scaling as 1/Δω, where Δω is
   the frequency gap between competing attractors — not 1/environment-size
   or 1/temperature. Cavity QED and superconducting qubit experiments
   can test this.

3. **Redshift evolution of RAR scatter**: If a₀(z) = cH(z)/(2π), the
   transition region shifts with z. At z ≈ 4-6 where a₀ is 5-6× larger,
   the transition zone moves to higher g_bar. Galaxies that are firmly
   Newtonian at z = 0 may be in the transition zone at z = 5. GEKO and
   CRISTAL can test this.

4. **Zeno suppression in galactic dynamics**: Galaxies undergoing rapid
   interactions (mergers, tidal stripping) are "continuously measured"
   by their environment. The fidelity bound predicts they should show
   anomalous dynamics near a₀ — the transition is disrupted because
   the system never accumulates enough cycles. Post-merger remnants
   should re-establish the RAR on a timescale ~ 1/H(z).

## Status

**Established**: The self-referential fidelity bound unifies:
- RAR shape (frequency resolution of ω_orbit against H)
- Collapse duration (frequency resolution of Δω between tongues)
- τ × Δθ uncertainty relation (Fourier identity)
- Zeno effect (interrupted frequency measurement)

**The key insight**: The bound is not imposed. It is constitutive.
The system cannot exceed its own resolution because the resolution IS
the system — the oscillator measuring its frequency is the oscillation.
The 2π in a₀ = cH/(2π) and the ħ = h/(2π) in ΔEΔt ≥ ħ/2 are the
same geometric factor: the ratio of a cycle to a radian, appearing
because phase is the primary variable and frequency resolution is
the primary constraint.

**Resolved**: One circle map iteration corresponds to one cycle of the
reference oscillator: T_iter = 2π/ω_ref. For the MOND case, ω_ref = H,
giving T_iter = 2π/H ≈ 2.9 × 10^18 s ≈ 90 Gyr. The Floquet decay
timescale in physical units is τ = T_iter × C/√(g_bar/a₀). At g_bar = a₀
(the transition): τ ~ T_H — the orbit needs a Hubble time to resolve
which regime it belongs to, which is why the transition is smooth, not
sharp. Deep Newtonian (g_bar >> a₀): τ << T_H, orbit resolves quickly.
Deep MOND (g_bar << a₀): τ >> T_H, orbit never fully resolves — it
remains entrained. For quantum collapse, ω_ref = ω_env (environmental
coupling frequency), giving T_iter = 2π/ω_env. At 1 GHz coupling:
T_iter = 1 ns, and collapse durations range from 10 ns (ε ~ 1) to
~200 ns (ε ~ 0.003). The Stribeck lattice calibrates at ω₀ = 1 rad/s:
T_iter = 6.28 s; the damping time τ_d = 50 s ≈ 8 periods sets the
resolution floor — tongue structure below ε ~ (T₀/τ_d)² is
unresolvable, analogous to orbits slower than H. See
fidelity_calibration.py.

**Resolved**: The RAR interpolating function g_obs = g_bar/[1 - exp(-√x)]
is the fixed point of the self-consistency equation g_obs = g_bar + α·g_obs,
where α = exp(-√(g_bar/a₀)) is the Floquet damping factor of the
gravitational tongue. The exponential is Floquet convergence; the square
root is saddle-node universality. Derived from tongue geometry, not fit.

**Resolved**: The circle map convergence rate near the 0/1 tongue
boundary is λ_circle = 2√(πKε_circle) per iteration (collapse_tongues.py).
The RAR requires λ = √(g_bar/a₀). These are reconciled by the coordinate
mapping ε_circle = g_bar/(4πK·a₀), so that
λ = 2√(πK · g_bar/(4πK·a₀)) = √(g_bar/a₀). The factor 4πK is the
natural conversion between the circle map's dimensionless depth and the
gravitational ratio. At K = 1 (critical coupling, where tongues fill the
parameter space and every orbit is locked — the gravitational case), the
factor is 4π. This is not fine-tuned: it is absorbed into the definition
a₀ = cH/(2π), and the tongue boundary ε_circle = 0 correctly maps to
g_bar = 0 (the maximally entrained ground state of Derivation 9 §The
g_bar = 0 state). Verified numerically across K ∈ {0.5, 0.7, 0.9, 0.99}:
λ_exact/√(4πK·ε_circle) → 1.0 as ε → 0. See fidelity_calibration.py.
