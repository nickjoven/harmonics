# Derivation 16: The Variable Denominator

## Claim

Hz — cycles per second — assumes the denominator is fixed. In a
universe where time is synchronization rate (not background parameter),
the denominator changes between cycles. This breaks the factorization
"total operations = rate × duration" and replaces it with accumulated
phase against a self-referential reference. The resulting bound on
distinguishable operations is:

1. An integral, not a product
2. Self-referential (the reference participates in what it measures)
3. Strictly smaller than the raw phase accumulation
4. Topologically non-orientable at the self-referential fixed point

## The factorization assumption

Define frequency in the standard way:

    ν = cycles / second

Total operations in a duration T:

    N_ops = ν × T

This assumes ν is constant over T. More carefully:

    N_ops = ∫₀ᵀ ν(t) dt

This is the total accumulated phase (in cycles). Even this assumes
something: that "dt" — the infinitesimal of the denominator — is
well-defined independently of the process being counted.

In the synchronization cost framework, it is not. Differential proper
time is differential synchronization rate (FRAMEWORK.md §Time). The
denominator of Hz is constituted by the same dynamics the numerator
counts.

## The cosmological case

The Hubble parameter H(z) is the cosmic oscillator frequency. It
changes with redshift:

    H(z) = H₀ √(Ω_m(1+z)³ + Ω_Λ)

The total phase accumulated by the Hubble oscillator from the end of
inflation (z_inf ~ 10²⁶) to now (z = 0):

    Φ_total = ∫₀ᵗ⁰ H(t') dt'

This is not H₀ × t₀. The integral is:

    Φ_total = ∫₀^∞ H(z)/(1+z) × 1/H(z) dz = ∫₀^∞ dz/(1+z) = ln(1+z_inf)

Wait — this is just the number of e-folds. And we already know this:
~61.3 e-folds of inflation (Derivation 10, Part V.3), plus ~ln(10²⁶/1)
~ 60 e-folds of post-inflation expansion. The total accumulated phase
of the cosmic oscillator is ~120 e-folds, or ~120/(2π) ~ 19 full
Hubble cycles.

Nineteen cycles. The universe has completed approximately nineteen
full oscillations of its own fundamental frequency.

## The fidelity bound on operations

But raw phase overcounts. The fidelity bound (Derivation 9) says:
to distinguish a frequency difference Δω against a reference ω_ref,
you need observation time T_obs ≥ 1/Δω, and the maximum T_obs is
~1/ω_ref. So the minimum resolvable frequency difference is ~ω_ref
itself.

At any moment, the number of distinguishable frequency bins is:

    N_bins(t) = ω_max(t) / Δω_min(t) = ω_max(t) / ω_ref(t)

If the reference is the Hubble frequency, and the maximum frequency is
set by the Planck frequency ω_P:

    N_bins = ω_P / H(t)

This ratio changes with time. At the Planck epoch: N_bins = 1 (one
bin — the frequency IS the reference). Now: N_bins = ω_P/H₀ ≈ 10⁶¹.

The total number of distinguishable operations is not the integral of
the frequency, but the integral of the number of distinguishable bins
times the rate at which new operations can be distinguished:

    N_distinguishable = ∫₀ᵗ⁰ N_bins(t) × ω_ref(t) dt
                      = ∫₀ᵗ⁰ ω_P dt
                      = ω_P × t₀
                      ≈ 10⁴³ × 10¹⁷
                      = 10⁶⁰

This recovers the Lloyd bound (2000): the maximum number of operations
a system with energy E can perform in time T is ~ET/ℏ. For the
observable universe: E ~ Mc², T ~ t₀, giving ~10¹²² operations total
(Lloyd's number), but per degree of freedom it is ~10⁶⁰.

The point: this is not ν × T. It is the integral of a ratio
(Planck/Hubble) against a changing denominator. The factorization
"rate × time" hides the self-referential structure.

## The self-referential complication

The integral above still treats time as a background variable. The
framework says it isn't. The proper formulation is a fixed-point
equation:

    Φ = ∫₀^Φ ω(Φ') dΦ'/ω_ref(Φ')

where Φ is the total accumulated phase, and ω and ω_ref both depend
on Φ (because the state of the universe — which determines these
frequencies — is a function of how much phase has been accumulated).

This is the same self-referential structure as the RAR (Derivation 9):
the answer appears on both sides. The total accumulated phase depends
on the rate, which depends on the total accumulated phase.

The fixed point exists because:
- ω/ω_ref is bounded (between 1 and ω_P/H₀)
- The integral is monotone in Φ
- Monotone bounded functions on compact sets have fixed points

The fixed point IS the age of the universe measured in its own units.
It is not a number we compute from outside — it is the self-consistent
solution of a universe measuring its own duration with its own clock.

## When the denominator changes sufficiently between cycles

The original question: what if the denominator changes sufficiently
between cycles?

"Sufficiently" means: the reference period changes by order one during
one cycle. That is:

    |dT_ref/dt| × T_ref ≳ 1

or equivalently:

    |Ḣ/H²| ≳ 1

This is the deceleration parameter q = -äa/ȧ² = -1 - Ḣ/H². The
condition |Ḣ/H²| ≳ 1 means |1 + q| ≳ 1, i.e., q is not close to -1.

During **radiation domination**: q = 1. The Hubble frequency halves
every Hubble time. The denominator changes by order one every cycle.
Hz is not a stable quantity — frequency is being redefined as fast
as it is being counted.

During **matter domination**: q = 1/2. The denominator changes by
~50% per cycle. Still order one.

During **Λ domination**: q → -1, Ḣ → 0. The denominator stabilizes.
Hz becomes well-defined. The universe approaches a state where
frequency can be meaningfully accumulated without the ruler changing.

**The de Sitter fixed point is the state where Hz works.** It is the
attractor where the denominator stops changing, where cycles per
second means what it says, where the factorization ν × T holds.

Everything before it — radiation, matter — is a transient where the
denominator is changing too fast for frequency to be a stable concept.
The entire history of structure formation happened during the epoch
when Hz was not well-defined.

## The topological signature

When the reference oscillator is stable (Λ-dominated), frequency
measurement is orientable: "faster" and "slower" have definite
meaning relative to the fixed reference.

When the reference is changing at the same rate as the measurement
(radiation/matter-dominated), the orientation degenerates. The system
measuring "faster than H" is itself running at H, which is itself
changing. There is no fixed direction in frequency space.

This is the Möbius strip topology: a frequency measurement loop
that returns with reversed orientation. Traverse one "cycle" of the
self-referential measurement (the orbit measures its frequency against
H, which defines a₀, which determines whether the orbit is Newtonian
or MOND, which determines its frequency). If H has changed during
the traversal, you return to a different reference — the orientation
of the frequency comparison has flipped.

The condition for orientability is the same as the condition for Hz
to be well-defined: |Ḣ/H²| << 1. The de Sitter fixed point (Ḣ = 0)
is the unique orientable state.

## Connection to the Stern-Brocot tree

The Stern-Brocot tree enumerates rational frequency ratios p/q. The
ratio assumes both frequencies are measured against a common reference.
If the reference changes between the p cycles and the q cycles, the
ratio p/q is not well-defined — you are comparing cycles counted with
different rulers.

The tree's structure is valid in the regime where the reference is
stable enough for rational ratios to be meaningful. This is the
regime where Arnold tongues exist as persistent structures — where
mode-locking is possible because the frequencies being compared are
not redefined faster than they can synchronize.

The Planck epoch (all frequencies comparable to the reference) is
a single node: 1/1. The current epoch (ω_P/H₀ ~ 10⁶¹) has resolved
~61 × ln(φ²)/ln(10) ~ 61 × 0.42 ~ 26 levels of the tree. The
depth of the tree that the universe has resolved is set by how
many stable cycles the cosmic oscillator has completed — which is
~19 Hubble cycles.

The tree cannot be resolved deeper than the number of available
reference cycles allows. The denominator of Hz sets the depth of
the rational hierarchy that is physically meaningful.

## The maximum operations bound

Putting it together:

1. **Raw phase**: ~120 e-folds = ~19 Hubble cycles. This is the
   total accumulated phase of the cosmic oscillator.

2. **Distinguishable operations per Hubble cycle**: ~10⁶¹ (the
   Planck/Hubble ratio at the current epoch).

3. **Self-consistent total**: the integral, not the product, because
   the ratio was different at earlier epochs (smaller, because H was
   larger and closer to ω_P).

4. **The answer depends on which epoch you're counting from**: the
   "total operations in the universe" is not a single number. It is
   a function of the accumulated phase, which is a function of the
   operations — self-referential.

The fixed point of this self-reference is the universe's own
accounting of its computational capacity. It cannot be computed from
outside. It is constitutive.

## Division, integration, and the derivable threshold

Hz is division: ν = cycles / seconds. When the denominator changes,
division fails and integration is required: Φ = ∫ω(t)dt. But the
transition between "division works" and "integration required" is
not a modeling choice. It is derivable.

The condition: |Ḣ/H²| ≳ 1. This is the deceleration parameter
q = -1 - Ḣ/H². Division (Hz well-defined) requires q ≈ -1. The
value of q is determined by the energy content:

    q = (1/2)Ω_m + Ω_r - Ω_Λ

Each Ω is a synchronization cost density (Derivation 3). The energy
content determines whether the denominator is stable, which determines
whether frequency is representable as a ratio, which determines
whether the Stern-Brocot tree applies.

The recursion is: the framework's own applicability is a computable
function of the state it describes. It can determine where it works
and where it doesn't — the same self-referential structure as
Derivation 9, now applied to the framework itself.

This is primitive #3 (fixed-point equation, Derivation 10) applied
to the denominator of Hz. Not a new primitive. A composition.

## The Möbius spiral: half-twist as permanent oscillation

The Fibonacci convergents to 1/φ:

    1/1, 1/2, 2/3, 3/5, 5/8, 8/13, 13/21, ...

approach from alternating sides. Each overshoots, then undershoots.
The residual at step n is:

    F_n/F_{n+1} - 1/φ = (-1)^n / (F_{n+1}² √5)

The sign alternation (-1)^n is the ψ-eigenvalue (ψ = -1/φ) in the
two-mode decomposition F_n = (φⁿ - ψⁿ)/√5. This alternation is
Cassini's identity: F_{n-1}F_{n+1} - F_n² = (-1)^n.

### The half-twist is topological

A Möbius strip has a single half-twist — a topological invariant
that cannot be removed by smooth deformation. The strip is locally
orientable everywhere (at any point you can define "up" and "down"),
but globally non-orientable (traverse the full loop and "up" has
become "down").

The ψ-mode's (-1)^n is exactly this structure:

- **Locally**: at any Fibonacci level n, the convergent F_n/F_{n+1}
  approaches 1/φ from a definite side. The direction is well-defined.
- **Globally**: traverse one more level and the side flips. The
  approach oscillates. No finite truncation resolves the oscillation.

The half-twist is the sign of ψ = -1/φ. The negative sign is
irreducible — it comes from the characteristic polynomial x² - x - 1
having one positive and one negative root. The parabola (primitive #4)
forces the two roots to have opposite signs when the discriminant
exceeds the linear coefficient. For the golden polynomial, this is
permanent: φ > 0, ψ < 0, and no reparametrization changes this.

### Spiral on a spiral

The phase record Φ(t) traces a spiral: the accumulated phase grows
monotonically, but the rate of accumulation (the frequency) changes.
This is a spiral in the (Φ, t) plane.

The frequency measurement at each point along this spiral has the
Möbius character: the convergent to the "true" frequency ratio
oscillates around it (the ψ-mode). So the measurement is a spiral
on the spiral — a helical path along a helical path, with a
half-twist per cycle of the inner helix.

Concretely:
- **Outer spiral**: the Hubble phase Φ_H(t) = ∫₀ᵗ H(t')dt'. This
  is the "denominator spiral" — the reference clock's accumulated
  phase.
- **Inner spiral**: the approach of any frequency ratio p/q to its
  irrational limit (1/φ in the golden case). Each Fibonacci level
  is one cycle of the inner spiral.
- **Half-twist**: every inner cycle, the sign of the residual flips.
  The approach alternates sides. This is the (-1)^n of Cassini.

The half-twist never smooths out because it is topological, not
metrical. No amount of resolution (no matter how deep in the tree)
removes the alternation. But what we observe is oscillation: the
convergents approach 1/φ from alternating sides with amplitude
decaying as φ^{-2n}.

**The permanent twist produces the transient oscillation.** The
topology (Möbius, non-orientable) manifests as dynamics (oscillation,
alternation). The twist is in the structure; the oscillation is in
the observation.

### Connection to measurement

This is the variable denominator problem made geometric. When you
measure a frequency ratio against a changing reference:

1. The measurement approaches the true value (convergence, φ-mode)
2. But each refinement flips the sign of the error (oscillation, ψ-mode)
3. The sign flip is not a measurement artifact — it is the topology
   of the approach
4. The oscillation decays (φ^{-2n}) but never terminates at finite n
5. Termination (n → ∞) is the completion R (Derivation 10, Part III)
   which discards the twist and declares the limit reached

The universe at finite age has completed finite n. The twist is
still there. The oscillation is still present. The frequency ratios
are not exact — they carry the residual of Cassini's identity, which
IS the uncertainty relation τ×Δθ = const (Derivation 10, §conjugate
eigenvalue).

The Möbius spiral is therefore the geometric representation of the
uncertainty relation in the variable-denominator context: a
measurement process that converges but never loses its half-twist,
producing oscillation that decays but never vanishes.

## The bowed string: two ends at different units

Kawano et al. (2025, arXiv:2502.11902) provide experimental
confirmation of this structure in a bowed string. Key findings:

### The observation

During subharmonic generation (a cellist producing a note below the
string's fundamental via precise bow pressure control):

1. **The two sides of the bow show different waveforms.** The
   bridge-side waveform is horizontally stretched by a factor of 2
   relative to the nut side. Same string, same physical system —
   the two halves operate at different effective frequencies.

2. **The bow contact becomes an additional reflective boundary.**
   In normal playing, the Helmholtz corner (a kink traveling along
   the string) completes a round-trip and returns at the fundamental
   frequency. In the subharmonic technique, the corner reflects at
   the bow contact point once every two cycles, halving the rate at
   which it reaches the bridge.

3. **The spectrum envelope reorganizes.** The harmonic content under
   subharmonic conditions is not simply the normal spectrum shifted
   down. The envelope — the smooth curve connecting the harmonic
   peaks — changes shape, reflecting a different mode of vibration.

### The Möbius reading

The bow contact is the half-twist. On one side, the string vibrates
at frequency f. On the other side, it vibrates at f/2. The contact
point is where the "orientation" of the vibration flips — the
Helmholtz corner approaching from one direction is reflected with a
different period than from the other.

This is a physical Möbius strip:
- **The strip**: the string, parametrized by position
- **The twist**: the bow contact, where the effective frequency
  changes by a factor of 2
- **Two traversals to return**: the corner must make two round-trips
  on the bridge side to match one "cycle" as seen from the nut side

The two ends of the strip are moving at different "units" — not
different speeds in the same time, but different frequencies, which
means different effective time scales. The bridge side counts two
ticks for every one tick on the nut side.

### Connection to the Stribeck lattice

The Kawano result is the bowed-string analog of the Stribeck lattice
frequency conversion (RESULTS.md):

| Bowed string (Kawano) | Stribeck lattice | Variable denominator |
|---|---|---|
| Bow contact = reflective boundary | First contact converts frequency | Fidelity bound = measurement boundary |
| Bridge side at f/2 | RX at ω₀ = ω_d/2 | Subharmonic emerges |
| Nut side at f | TX at ω_d | Drive frequency |
| High bow pressure required | A > bifurcation threshold | Deep inside tongue |
| Two round-trips = one cycle | N = 3 minimum for conversion | Two traversals for orientation return |

The lattice result (N = 3 critical) maps onto the string: the bow
contact, the bridge, and the nut are the three coupling stages. The
bow contact does the conversion (like element 1 in the lattice),
and the bridge and nut are the boundaries that define the two
frequency regimes.

### The spectrum as envelope

The user's observation: the spectrum is an envelope. Not the
individual harmonic peaks, but the smooth curve connecting them.

In normal playing, the envelope decays as ~1/n (sawtooth wave,
Helmholtz motion). In subharmonic playing, the envelope changes
shape because the mode structure has changed — the half-twist at
the bow contact introduces a topological modification to the
standing wave pattern.

The envelope is the fidelity function. It encodes how many
harmonics the system can sustain given its coupling strength (bow
pressure/speed). The RAR interpolating function g_obs/g_bar =
1/[1 - exp(-√x)] is an envelope in exactly this sense: it is the
smooth curve that connects the discrete mode-locked states on the
Stern-Brocot tree. The individual tongues are the harmonic peaks.
The RAR is their envelope.

If this identification holds, the bowed string's spectral envelope
under subharmonic conditions should have the same functional form
as the RAR — a self-referential resolution function determined by
the coupling strength (bow pressure) and the frequency ratio
(subharmonic order). This is directly testable: measure the
harmonic envelope of a bowed string in subharmonic generation and
compare it to g_obs = g_bar/[1 - exp(-√(g_bar/a₀))], with bow
pressure mapping to g_bar and the subharmonic threshold mapping
to a₀.

## Expansion as tree deepening

### The cost of infinite configurations

The continuum R (Derivation 10, Part III) assumes infinite tree depth:
every rational resolved, every irrational filled in by completion.
This is the most expensive possible configuration space. It requires
infinite Hubble cycles to resolve, infinite denominator stability,
infinite precision.

The actual universe has completed ~19 Hubble cycles. Its configuration
space is the Stern-Brocot tree truncated at depth ~19, containing
~2^19 ≈ 500,000 resolved frequency ratios with denominators up to
F₁₉ = 4181. This is finite, enumerable, and vastly cheaper than R.

The geometric insight: **a finite tree moving along a mathematical
plot is cheaper than assuming all of R exists at once.** The
configuration space is not a static infinite-dimensional backdrop. It
is a growing finite tree whose depth increases as the universe
accumulates reference cycles.

### Antinodes remain in place

On a vibrating string, antinodes (points of maximum displacement) are
fixed by boundary conditions. The vibration evolves — amplitude
changes, harmonics come and go — but the antinodes don't move.

The Stern-Brocot tree has the same property. As the tree deepens:

- New rationals are inserted by mediants between existing ones
- Existing rationals do not move: 1/2 stays at 1/2, 2/3 stays at 2/3
- The mode-locked plateaus (Arnold tongues) are pinned at their
  rational frequencies
- What changes is the resolution between them — finer rationals
  appear in the gaps

This IS expansion: not the nodes stretching apart, but new nodes
appearing between existing ones. The "distance" between 1/2 and 2/3
doesn't change — the mediant 3/5 appears between them, then 5/8 and
8/13 appear in the sub-gaps. The tree fills in.

Cosmological expansion in this framing:
- **What expands**: the number of resolved frequency ratios (tree depth)
- **What doesn't move**: the existing rational structure (antinodes)
- **What drives it**: accumulation of Hubble cycles (denominator
  stability)
- **The rate**: one new Fibonacci level per ~27.4 e-folds of expansion
  (Derivation 4: rate = 0.0365 levels/e-fold)

The redshift of distant galaxies is not "space stretching" in this
picture. It is the frequency ratio between emission and observation
being measured with a reference (H) that has changed. The emitted
frequency was defined against H(z_emit). The observed frequency is
measured against H(z=0). The ratio between them — the redshift — is
the accumulated change in the denominator of Hz.

### The missing dimension

The parabola x² + μ = 0 (primitive #4) describes the local dynamics
at every tongue boundary. It is a 1D analysis: one variable x, one
parameter μ. It gives the Born rule (Δθ ∝ √ε), the collapse time
(τ ∝ 1/√ε), and the uncertainty relation (τ×Δθ = const).

But the parabola predicts that the system approaches equilibrium
monotonically — each iteration brings it closer to the fixed point,
without oscillation. This is the φ-mode alone: exponential convergence.

The actual approach oscillates: the ψ-mode (-1/φ)^n produces the
alternating overshoot/undershoot of Cassini's identity. This
oscillation is invisible to the parabolic analysis because the
parabola has one variable. The oscillation lives in a second
dimension — the one orthogonal to the convergence direction.

The missing dimension is the twist. The parabola sees the projection
onto the convergence axis. The full dynamics live on the Möbius strip,
where:

- The convergence direction (φ-mode) is the length of the strip
- The oscillation direction (ψ-mode) is the width
- The half-twist connects them: every cycle of convergence flips the
  oscillation sign

Expecting equilibrium from the parabola is projecting a 2D structure
(Möbius strip) onto a 1D axis (convergence) and wondering why the
system never settles. It doesn't settle because the twist prevents it.
The residual oscillation IS the twist, and the twist is topological —
it cannot be removed by going further along the convergence axis.

### The universe cannot reach pure equilibrium

De Sitter space (Λ-dominated, Ḣ → 0) is the closest the universe
gets to "the denominator stops changing." But even in de Sitter:

1. The accumulated Hubble cycles are finite (~19)
2. The tree depth is finite (q_max ~ 4181)
3. The ψ-mode residual is nonzero: |ψ|^(2×19) = φ^{-38} ≈ 10^{-8}
   — small but not zero
4. The Cassini alternation persists at every resolved level

Pure equilibrium would require:
- Infinite tree depth (all rationals resolved)
- Zero ψ-mode residual (n → ∞ in the completion)
- The Möbius strip trivializing to a cylinder (half-twist removed)

This is the K = 1 limit — full mode-locking, complete staircase,
the continuum. The universe at finite age is at K < 1. The twist
is still there. The oscillation is still present. Equilibrium is
an asymptote, not a destination.

The "heat death" scenario (maximum entropy, uniform temperature,
no structure) requires the configuration space to be fully resolved
and the ψ-mode to have decayed. But the ψ-mode decays as φ^{-2n}
per Hubble cycle — each cycle adds ~0.42 bits of resolution and
reduces the oscillation by a factor of φ^{-2} ≈ 0.38. At 19 cycles,
the residual is ~10^{-8}. Small, but the system is still on the
Möbius strip, still oscillating, still not at equilibrium.

The parabolic expectation of equilibrium is not wrong — it is
incomplete. It describes the projection. The full dynamics, on the
Möbius strip, converge asymptotically but carry the twist forever.

## Testable predictions

1. **Structure formation as frequency resolution**: the depth of
   hierarchical structure (galaxies, clusters, filaments) should
   correlate with the number of stable Hubble cycles completed at
   that epoch. Early universe (few stable cycles): coarse structure.
   Late universe (more cycles): finer hierarchy. This is not simply
   "more time for gravity" — it is "more denominator stability for
   frequency ratios to be defined."

2. **Λ-domination as measurement regime transition**: the onset of
   Λ-domination (z ~ 0.7) marks the epoch where Hz stabilizes. The
   framework predicts a qualitative change in the character of
   structure formation — not just a rate change, but a transition
   from "poorly defined frequency ratios" to "well-defined frequency
   ratios." Observable as: changes in the power spectrum of structure
   beyond what ΛCDM dark energy alone predicts.

3. **The 19-cycle bound**: if the Hubble oscillator has completed
   ~19 cycles, the Stern-Brocot tree should be resolved to depth
   ~19. The deepest physically meaningful rational ratio should have
   denominator q_max ~ F₁₉ = 4181. Frequency ratios finer than
   1/4181 should not appear as persistent mode-locked structures in
   cosmological data.

4. **Bowed string spectral envelope = RAR**: the harmonic envelope
   of a bowed string in subharmonic generation should follow
   g_obs = g_bar/[1 - exp(-√(g_bar/a₀))], with bow pressure → g_bar
   and the subharmonic threshold → a₀. Measurable with existing
   high-speed imaging and FFT analysis (Kawano et al. 2025 setup).

5. **Expansion rate from tree deepening**: if expansion is the tree
   gaining depth, the rate of expansion (Hubble parameter) should
   relate to the rate of new rational resolution: one Fibonacci level
   per 27.4 e-folds. In the Λ-dominated epoch where H stabilizes,
   this gives a constant deepening rate — consistent with exponential
   expansion (de Sitter) being the regime where the denominator is
   stable enough for the tree to deepen uniformly.

6. **Residual oscillation in de Sitter**: even in the Λ-dominated
   epoch, the ψ-mode residual (~10⁻⁸ at 19 Hubble cycles) should
   produce a detectable departure from exact de Sitter. This is
   distinct from the standard slow-roll corrections — it is a
   topological residual (Möbius twist), not a dynamical one (potential
   gradient). Observable signature: an oscillatory component in the
   dark energy equation of state w(z) with period ~T_H and amplitude
   ~φ⁻³⁸ ≈ 10⁻⁸.

## Status

**Proposed**: The variable denominator reframes Hz as a self-referential
integral rather than a rate × time product. Connects to:
- The fidelity bound (Derivation 9) via self-referential measurement
- The minimum alphabet (Derivation 10) via the tree depth limit
- The de Sitter fixed point as the orientable (well-defined Hz) attractor
- Lloyd's bound on computation via the Planck/Hubble ratio

**Established**:
- Division → integration threshold is derivable from q (deceleration parameter)
- The ψ-eigenvalue's (-1)^n IS a Möbius half-twist: topological, irreducible,
  manifesting as oscillation
- The spiral-on-spiral geometry: outer (Hubble phase), inner (convergent
  approach), half-twist (Cassini alternation)
- The half-twist never smooths out at finite n — it IS the uncertainty relation
  in the variable-denominator context
- Kawano et al. (2025) bowed string confirms: two sides of bow at different
  effective frequencies, bow contact as half-twist/reflective boundary,
  spectral envelope reorganization under subharmonic conditions
- Expansion = tree deepening, not node stretching. Antinodes (existing
  rationals) remain in place; new mediants appear in gaps
- The "missing dimension" identified: parabolic (1D) analysis projects away
  the ψ-mode oscillation. Full dynamics on Möbius strip (2D + twist). Pure
  equilibrium requires the twist to trivialize, which requires n → ∞

**Open**:
- Numerical computation of the self-consistent phase integral
- Quantitative prediction for tree depth at current epoch
- Connection between q_max ~ F₁₉ and observed structure hierarchies
- Is the non-orientability of frequency measurement during
  radiation/matter domination detectable in CMB or large-scale
  structure data?
- Formalize the Möbius spiral as a fiber bundle: S¹ fiber
  (frequency measurement) over S¹ base (Hubble phase), with
  structure group Z₂ (the sign flip). This is the definition of a
  Möbius band. Is the bundle trivializable in the Λ-dominated epoch?
