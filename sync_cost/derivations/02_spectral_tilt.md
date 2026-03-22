# Derivation 2: Spectral Tilt from Synchronization Cost Gradient

> The universe is not scale-invariant. It almost is — and the almost
> is the whole story.

## Claim

The CMB spectral tilt n_s ≈ 0.965 encodes the curvature of the
synchronization cost function across scales. The 3.5% deviation from
perfect scale-invariance is the slope of the cost gradient: larger
scales had longer to synchronize and therefore lower net cost, producing
more power.

## Setup

### The primordial power spectrum

The observed CMB power spectrum is nearly scale-invariant:

    P(k) ∝ k^(n_s - 1)

where k is the comoving wavenumber and n_s = 0.9649 ± 0.0042 (Planck
2018). Perfect scale-invariance would be n_s = 1.

### Scale as synchronization time

A mode with wavenumber k corresponds to a physical scale λ = 2π/k.
In the synchronization framework, each mode is a synchronization domain.
Larger scales (smaller k) have:

- More participants in the mean field
- Longer time to synchronize (exited the Hubble horizon earlier)
- Lower residual synchronization cost

Define the synchronization time for mode k:

    τ_sync(k) = τ_exit(k) - τ_0

where τ_exit(k) is the conformal time at which mode k exits the Hubble
horizon and τ_0 is the onset of synchronization (beginning of inflation
or the equivalent cost-minimization epoch).

For quasi-exponential expansion: τ_exit(k) ∝ -1/k (conformal time is
negative and approaching zero). So:

    τ_sync(k) ∝ 1/k

Larger scales (smaller k) have longer synchronization time.

### Cost function

The synchronization cost for a mode that has been synchronizing for
time τ is:

    C(τ) = C_max × K_half / (K_half + τ)

This is the Michaelis-Menten form: saturating, asymptoting to zero
at large τ, with half-maximum cost at τ = K_half.

Properties:
- C(0) = C_max (unsynchronized: maximum cost)
- C(K_half) = C_max/2 (half-synchronized)
- C(τ → ∞) → 0 (fully synchronized: zero residual cost)

### Power as inverse cost

The amplitude of a primordial perturbation mode is determined by how
much cost remains when the mode freezes out (re-enters the horizon or
decouples). Modes with less residual cost have settled more completely
— their amplitude reflects the depth of their cost basin:

    P(k) ∝ 1/C(τ_sync(k))

This is the key physical statement: power is inverse cost. Modes that
synchronized more completely (lower cost) have larger frozen amplitudes
because they explored more of their basin.

## Derivation

Substituting τ_sync(k) = τ_0 / k (where τ_0 absorbs the
proportionality constant):

    C(k) = C_max × K_half / (K_half + τ_0/k)
         = C_max × K_half × k / (K_half × k + τ_0)

So:

    P(k) ∝ 1/C(k) = (K_half × k + τ_0) / (C_max × K_half × k)
         = 1/C_max + τ_0/(C_max × K_half × k)

This has two terms:
- A constant (scale-invariant) term: 1/C_max
- A 1/k correction (red tilt): τ_0/(C_max × K_half × k)

For the power spectrum index, take the logarithmic derivative:

    n_s - 1 = d ln P / d ln k

Let x = K_half × k / τ_0 (dimensionless wavenumber). Then:

    P(k) ∝ (x + 1) / x = 1 + 1/x

    d ln P / d ln k = d ln(1 + 1/x) / d ln x
                    = (-1/x²) / (1 + 1/x)  ×  1
                    = -1 / (x(x + 1))
                    = -1 / (x² + x)

### Evaluating at the pivot scale

The spectral tilt is measured at a pivot scale k_* where x_* =
K_half × k_* / τ_0. The observed value n_s - 1 ≈ -0.035 requires:

    1 / (x_*² + x_*) ≈ 0.035

    x_*² + x_* ≈ 28.6

    x_* ≈ 4.85

This means the pivot scale k_* has synchronized for about 4.85
half-lives of the cost function. This is a reasonable value — the
mode is well into the saturating regime but not fully converged.

### Physical interpretation of K_half

K_half is the synchronization timescale — the time for a mode to
reach half its maximum synchronization depth. In the KE framework:

    K_half = π / (K_c × g(0))

where K_c is the Kuramoto critical coupling and g(0) is the frequency
distribution width. This connects the spectral tilt to the same
synchronization parameters that produce a₀ and H₀.

## Predictions and tensions

1. **Running of the spectral index**: The Michaelis-Menten form predicts:

       dn_s/d ln k = +(2x + 1) / (x² + x)²

   At x_* ≈ 4.85: dn_s/d ln k ≈ **+0.013** (positive running)

   Planck 2018 measures: dn_s/d ln k = -0.0045 ± 0.0067

   **The sign is positive**: n_s approaches 1.0 (scale-invariance) at
   smaller scales (larger k), because those modes had less time to
   synchronize and therefore sit closer to the unsynchronized (flat)
   regime. The Planck central value is negative but consistent with
   zero at ~1σ.

   This is a genuine tension. The MM cost function predicts that
   short-wavelength modes should be *more* scale-invariant than
   long-wavelength modes. The data weakly prefers the opposite.

   The Hill generalization (cooperative synchronization, n > 1) makes
   this worse — sharper transitions increase the running magnitude.
   This rules out simple cooperative extensions.

   **What could resolve it**: A cost function with a non-monotonic
   derivative — one that has an inflection point near the pivot scale.
   Physically: synchronization cost that *increases* before decreasing,
   as when modes must first overcome a barrier before settling. This
   is the cost equivalent of activation energy in chemistry, and it
   would produce negative running over the range where the cost
   function is concave-up.

2. **Tensor-to-scalar ratio**: In this framework, tensor modes
   (gravitational waves) are synchronization cost fluctuations of the
   mean field itself, while scalar modes are cost fluctuations of the
   participants. The ratio r encodes the coupling strength between
   these two cost channels. Prediction: r is set by the ratio of
   mean-field cost to participant cost at the pivot scale.

3. **Scale-dependent tilt**: n_s < 1 at all scales (red tilt), with
   the deviation from scale-invariance *increasing* at larger scales
   (smaller k). At k << k_*, the cost function dominates and the
   spectrum steepens dramatically — consistent with the low-ℓ CMB
   anomalies (quadrupole suppression). These modes are outside the
   synchronization horizon: they couldn't afford to synchronize
   before last scattering.

## Connection to lattice results

The Stribeck lattice shows differential attenuation: high-frequency
modes (ω_d) dissipate while low-frequency modes (ω₀) propagate. This
is exactly the spectral tilt mechanism — the cost gradient across
frequencies, made visible in a chain of oscillators.

In the lattice:
- ω_d is the "unsynchronized" mode (high cost, slip regime)
- ω₀ is the "synchronized" mode (low cost, stick regime)
- The ratio P(ω₀)/P(ω_d) increases with chain length

This mirrors the CMB: larger scales (more synchronization stages)
have more power (lower cost, deeper basin occupation).

## Status

The Michaelis-Menten cost function recovers n_s ≈ 0.965 with one
free parameter (the dimensionless pivot x_* ≈ 4.85).

The running prediction (+0.013) is a discriminator: the sign and
magnitude are testable. The MM form predicts positive running. If
future data confirms negative running, the cost function must have
non-monotonic derivative structure (activation barrier). This would
be a strong constraint on the cost functional's form.

See `spectral_tilt_numerical.py` for the numerical companion.

**Open**: Derive x_* from the KE parameters rather than fitting it.
The connection K_half = π/(K_c × g(0)) provides the route but needs
the frequency distribution g(ω) of primordial oscillators.

**Open**: The positive running is a tension point. What physical
mechanism would introduce an activation barrier into the
synchronization cost? Candidate: the self-consistency condition
itself — modes must first constitute a local mean field before they
can synchronize against the global one, and constituting the local
field costs energy.

**Open**: Does the self-consistency condition on the cost functional
select the Michaelis-Menten form, or is it one of several consistent
choices?

## Superseded by Derivation 04

A systematic scan (`cost_function_scan.py`) showed that **every
monotonically decreasing cost function C(τ) with P ∝ 1/C produces
positive running**. This is structural: ln(1/C(τ₀/k)) is convex in
ln k for any monotone C.

The issue is ontological: "cost" carries optimization structure that
obscures the mechanics. Derivation 04 (`04_spectral_tilt_reframed.md`)
replaces the cost function with the direct mechanical observable:

    P(k) ∝ g(ω) / (Kr)²

where g(ω) is the frequency distribution shaped by mode-locking
(Arnold tongues, devil's staircase). The staircase has both convex
and concave regions — the running sign depends on the pivot's
position on the staircase, not on the monotonicity of an envelope.

Numerical exploration (`mode_locking_spectrum.py`) confirms that
regions with simultaneous red tilt and negative running exist just
past rational plateaus (e.g., near ω = 2/3).
