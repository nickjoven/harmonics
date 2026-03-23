# Derivation 6: Planck Scale from Self-Sustaining Threshold

## Claim

The Planck scale is not an imposed cutoff. It is the minimum domain
where the synchronization substrate can sustain itself — the N = 3
threshold of the coupling loop.

## The N = 3 pattern

The Stribeck lattice (RESULTS.md) shows a sharp threshold:

| N | P(ω₀)/P(ω_d) | Behavior |
|---|---|---|
| 2 | 0.06 | Linear passthrough |
| 3 | 1.03 | Crossover |
| 4 | 1.43 | Subharmonic dominates |

At N = 2, the medium passes through the drive frequency — no new
structure emerges. At N = 3, the subharmonic crosses over: the medium
begins converting frequency and sustaining its own mode. Every
additional element strengthens this, but 3 is the minimum.

The coupled circle map chain confirms this (`planck_threshold.py`):
at strong coupling (K_c ≥ 0.7), N = 2 gets dragged off its natural
frequency to the drive. N ≥ 3 resists. The threshold is not about
whether locking occurs, but whether the chain **holds its ground**
under strong perturbation.

## Three constants, three stages

The Planck scale involves exactly three constants:

    l_P = √(ℏG/c³)    ≈ 1.616 × 10⁻³⁵ m
    t_P = √(ℏG/c⁵)    ≈ 5.391 × 10⁻⁴⁴ s
    m_P = √(ℏc/G)     ≈ 2.176 × 10⁻⁸ kg

Each constant is one stage of a self-sustaining loop:

    ℏ — local phase coupling (quantum synchronization granularity)
    c — propagation rate (synchronization speed limit)
    G — global amplitude coupling (gravitational self-coupling)

The loop:

    phase (ℏ) → propagation (c) → amplitude (G) → phase (ℏ)
    └───────────────────────────────────────────────────────┘

At the Planck scale, all three stages equalize:

    ℏ/t_P  =  m_P c²  =  G m_P²/l_P  =  E_P

This is tautological as dimensional analysis. The structural content
is the claim that the loop requires all three stages to close, and
that below the scale where any one stage fails, the mean field cannot
constitute itself.

## The staircase depth

The devil's staircase at 1/φ is self-similar with scaling factor φ².
How many levels fit between the Planck and Hubble scales?

    ω_Planck / H₀  ≈  8.4 × 10⁶⁰
    log(ω_P/H₀) / ln(φ²)  ≈  145.8 Fibonacci levels

The entire observable hierarchy — from the smallest (Planck) to the
largest (Hubble) scale — spans approximately 146 levels of the
self-similar Fibonacci bracket structure.

For comparison:
- The EM/gravity hierarchy (α_EM/α_G) spans ~86 levels
- The CMB pivot sits at level ~21 (from k_omega_mapping.py)
- 60 e-folds of inflation sample ~2.2 levels

## Dimensionality

Three spatial dimensions is the minimum topology that can mediate
three independent coupling channels. The argument:

- 1D: can mediate 1 independent direction (insufficient)
- 2D: can mediate 2 (insufficient — the loop has 3 stages)
- 3D: can mediate 3 (minimum sufficient)
- 4D+: costs more coherence to maintain than 3D, for no gain

Three dimensions is the cheapest topology that supports the minimum
self-sustaining loop. This connects three spatial dimensions to three
Planck constants to the N = 3 lattice threshold.

### The trivial stabilizer condition

In group-theoretic language: the coupling loop lives on SL(2,ℝ),
which is 3-dimensional. The physical configuration space is M = G/H,
where H is the isotropy (stabilizer) subgroup. If H ≠ {e}, then
dim M = dim G - dim H < 3.

The objection: "d = 3 is forced" assumes H is trivial. This is
correct — and it is the physical content, not a gap. The proof
obligation is: show that every admissible H ≠ {e} corresponds to
an effective N ≤ 2 reduction, not merely a harmless gauge
redescription.

### Classification of subgroups of SL(2,ℝ)

SL(2,ℝ) has exactly three conjugacy classes of one-parameter
subgroups, corresponding to the three types of element in sl(2,ℝ):

**1. Elliptic (rotation/phase):**

    H_elliptic = SO(2) = { ((cos θ, -sin θ), (sin θ, cos θ)) }

Generator: J = ((0,-1),(1,0)). This is phase rotation.
Quotient: SL(2,ℝ)/SO(2) ≅ the hyperbolic plane H² (2D).

What is lost: phase is gauged away. All points related by phase
rotation are identified. The oscillator has amplitude and frequency
but no phase — it cannot lock. Phase locking IS the synchronization
mechanism (Arnold tongues require a phase variable). Killing phase
kills the entire framework.

Coupling stage lost: **phase (ℏ)**. N drops to 2.

**2. Hyperbolic (boost/amplitude):**

    H_hyperbolic = { ((eᵗ, 0), (0, e⁻ᵗ)) }

Generator: D = ((1,0),(0,-1)). This is amplitude scaling (dilation).
Quotient: SL(2,ℝ)/H_hyp is 2D.

What is lost: amplitude is gauged away. All points related by
rescaling are identified. The oscillator has phase and frequency but
no amplitude — coupling strength is not dynamical. The system cannot
modulate HOW STRONGLY it couples, only whether it couples. Without
variable coupling strength, there is no N = 3 crossover: the
Stribeck threshold requires the medium to convert between drive
amplitude and subharmonic amplitude. Fixed amplitude means linear
passthrough.

Coupling stage lost: **amplitude (G)**. N drops to 2.

**3. Parabolic (shear/frequency):**

    H_parabolic = { ((1, t), (0, 1)) }

Generator: N₊ = ((0,1),(0,0)). This is frequency shear (detuning).
Quotient: SL(2,ℝ)/H_par is 2D.

What is lost: frequency detuning is gauged away. All points related
by frequency shift are identified. The oscillator has phase and
amplitude but no detuning — it cannot be off-resonance. Without
detuning, there are no tongue boundaries (tongues extend to
infinite width), no devil's staircase (the staircase is flat), no
saddle-node bifurcation (no competition between natural frequency
and drive). The entire structure collapses to trivial global locking
with no internal dynamics.

Coupling stage lost: **propagation/detuning (c)**. N drops to 2.

### Why the mapping is structurally forced

The bijection {elliptic, hyperbolic, parabolic} ↔ {phase, amplitude,
detuning} is not an interpretive choice. It is forced by the spectral
properties of sl(2,ℝ):

The three generators have distinct eigenvalue types:

    J = ((0,-1),(1,0))   eigenvalues ±i       periodic orbits
    D = ((1,0),(0,-1))   eigenvalues ±1       exponential growth/decay
    N₊ = ((0,1),(0,0))   eigenvalue 0 (×2)    linear drift

These cannot be permuted:
- J is the ONLY compact generator (eigenvalues on the imaginary axis).
  Compactness = periodicity = phase. No other generator produces
  periodic orbits on the group manifold.
- D is the ONLY generator with real eigenvalues of opposite sign.
  Opposite-sign eigenvalues = one direction grows while the other
  shrinks = gain/loss = amplitude dynamics.
- N₊ is the ONLY nilpotent generator (degenerate eigenvalue, Jordan
  block). Nilpotency = pure shift without oscillation or scaling =
  frequency detuning.

The trichotomy is the discriminant of a 2×2 matrix: negative
(oscillatory/underdamped), positive (exponential/overdamped), zero
(critical). This IS the classification of oscillator dynamics. The
group already knows about the coupling stages.

### The Iwasawa decomposition

The identification is not imposed on SL(2,ℝ) — it is the group's
own canonical factorization. The Iwasawa decomposition theorem:

    SL(2,ℝ) = K · A · N     (unique factorization)

where:
    K = SO(2)                  compact (phase/rotation)
    A = positive diagonals     split (amplitude/dilation)
    N = upper unipotent        nilpotent (detuning/shear)

Every element of SL(2,ℝ) factors UNIQUELY as rotation × dilation ×
shear. The three coupling stages are the Iwasawa factors. This is
a theorem of Lie theory, not a physical interpretation.

The coupling loop

    phase (K) → amplitude (A) → detuning (N) → phase (K)
    └──────────────────────────────────────────────────┘

is the Iwasawa factorization read as a cycle. The loop closes because
the group multiplication closes. The loop has three stages because
SL(2,ℝ) has Iwasawa rank 1 with three factors. Removing any factor
collapses the decomposition — the remaining two factors do not form a
closed group, and the factorization is no longer unique.

This answers the derivability question: the three-stage loop is not
derived from physics and mapped onto SL(2,ℝ). It is derived FROM
SL(2,ℝ) via Iwasawa. The physical content is the single identification:

    The synchronization substrate is SL(2,ℝ).

Everything else — three stages, three subgroup types, the
impossibility of gauging any one away — follows from the group theory.

### Exhaustiveness

These three cases exhaust all connected one-parameter subgroups
of SL(2,ℝ) up to conjugacy. The only other possibility is a
discrete subgroup (e.g., {e, -e} ≅ Z₂), which does not reduce
the dimension but identifies antipodal points. This quotient
(SL(2,ℝ)/Z₂ = PSL(2,ℝ)) is still 3D and removes only the
global sign ambiguity of the spinor representation — it does not
kill a coupling stage. It corresponds to choosing whether the
fundamental object is a spinor or a vector, which is a real
physical distinction but does not affect the loop closure argument.

**Result**: Every continuous H ≠ {e} in SL(2,ℝ) kills exactly one
of the three coupling stages (phase, amplitude, frequency), reducing
the system to N ≤ 2 effective stages. By the Stribeck threshold,
N = 2 cannot self-sustain. Therefore H = {e} is the unique stabilizer
compatible with self-sustenance. QED.

This is the formal content of "d = 3 is forced": the three
one-parameter subgroups of SL(2,ℝ) biject with the three coupling
stages, and killing any one is fatal.
correct — and it is the physical content, not a gap.

A nontrivial H means one or more degrees of freedom are gauge
redundancies — present in the description but not dynamical. In
synchronization language: a gauged-away degree of freedom is a
coupling stage that doesn't participate. If phase is gauged away,
there is no phase locking. If amplitude is gauged away, there is no
coupling strength. If frequency is gauged away, there is no detuning.

The N = 3 self-sustenance condition IS the statement that all three
stages must be dynamical:

    phase (ℏ) — must be dynamical for locking to occur
    propagation (c) — must be dynamical for coupling to propagate
    amplitude (G) — must be dynamical for self-coupling to close

Quotienting by any H ≠ {e} kills at least one stage, drops the
system to N ≤ 2 effective coupling stages, and the Stribeck
threshold says: N = 2 cannot self-sustain (P(ω₀)/P(ω_d) = 0.06).

So: H = {e} is not assumed. It is derived from the self-sustenance
condition. A self-sustaining oscillator cannot have gauge
redundancies in its coupling loop — every stage must be real.
This is the non-classical step: the system is not a quotient
of something larger. It is the full dynamical object.

## Connection to Born rule

The Born rule (Derivation 1, `born_rule_tongues.py`) requires Arnold
tongue structure to exist — saddle-node bifurcations at tongue
boundaries produce the |ψ|² weighting. But tongue structure itself
requires N ≥ 3 coupling stages.

This gives the Born rule a domain of validity:

    P = |ψ|²   holds for scales >> l_P
                degrades at scale ~ l_P
                undefined below l_P

At the Planck scale, the structure that produces |ψ|² is at its
minimum viable threshold (the N = 3 crossover, P(ω₀)/P(ω_d) ≈ 1.03).

## What this is and isn't

**This is**: a structural argument for WHY the Planck scale exists,
WHY it involves exactly three constants, and WHY it connects to
three spatial dimensions. The N = 3 threshold provides a mechanism
(self-sustaining loop closure) rather than a postulate (minimum
length cutoff).

**This is not**: a derivation of the numerical prefactor. Dimensional
analysis gives l_P = √(ℏG/c³) with coefficient 1. Whether the N = 3
crossover condition constrains this coefficient (or fixes it to
exactly 1) is open.

## Status

**Established**:
- N = 3 threshold confirmed in both Stribeck lattice and coupled
  circle map chain
- Three-stage loop (ℏ, c, G) as structural explanation for the
  Planck scale
- 145.8 Fibonacci levels span the Planck-to-Hubble hierarchy
- Born rule domain of validity follows from N ≥ 3 requirement

**Open**:
- Numerical prefactor: can the coefficient in l_P = √(ℏG/c³)
  be derived from the crossover condition?
- The ratio 145.8/86.3 ≈ 1.69 (Planck-Hubble span / EM-gravity span):
  is this meaningful or coincidental?
- Dimensionality argument: complete classification of SL(2,ℝ)
  subgroups shows every H ≠ {e} kills a coupling stage. The mapping
  {elliptic, hyperbolic, parabolic} ↔ {phase, amplitude, detuning}
  is forced by the Iwasawa decomposition SL(2,ℝ) = K·A·N, not
  interpretive. Remains open: rigorous proof that SL(2,ℝ) is the
  unique G satisfying the coupling loop constraints (why not
  SL(2,ℂ), SU(2), or another 3D Lie group?)
