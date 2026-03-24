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

## Status

**Proposed**: The variable denominator reframes Hz as a self-referential
integral rather than a rate × time product. Connects to:
- The fidelity bound (Derivation 9) via self-referential measurement
- The minimum alphabet (Derivation 10) via the tree depth limit
- The de Sitter fixed point as the orientable (well-defined Hz) attractor
- Lloyd's bound on computation via the Planck/Hubble ratio

**Open**:
- Numerical computation of the self-consistent phase integral
- Quantitative prediction for tree depth at current epoch
- Connection between q_max ~ F₁₉ and observed structure hierarchies
- Formalize the Möbius topology: is the non-orientability of
  frequency measurement during radiation/matter domination detectable
  in CMB or large-scale structure data?
