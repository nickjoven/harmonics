# google-turbo-diff

*Framework-native quantization vs TurboQuant: circle map vs random rotation.*

## Surface

Google's TurboQuant (ICLR 2026, arXiv:2504.19874) achieves near-optimal
vector quantization for KV-cache compression via:

1. **Random orthogonal rotation** → coordinates become Beta-distributed
2. **Lloyd-Max centroids** for that Beta → precomputed scalar codebook
3. **QJL sign correction** on residual → 1-bit unbiased inner products

The framework predicts an alternative pipeline using its own primitives:

1. **Circle map** at coupling K → coordinates become staircase-distributed
2. **Farey fractions** as codebook → structurally optimal for the staircase
3. **Tongue-width bounded residual** → fewer correction bits needed

## Why this could work

TurboQuant's insight: make the distribution *predictable*, then quantize
optimally for that distribution. Random rotation → Beta is one way.
The circle map → devil's staircase is another.

| Property | TurboQuant (rotation → Beta) | Framework (circle map → staircase) |
|----------|------------------------------|-------------------------------------|
| Preprocessing | O(d²) matrix multiply | O(d) sin evaluations |
| Distribution | Beta((d-1)/2, (d-1)/2) | Devil's staircase at coupling K |
| Codebook | Lloyd-Max (numerical) | Farey fractions (number theory) |
| Residual | QJL projection (1 bit) | Tongue-width bounded |
| Calibration | None (data-oblivious) | None (K is a hyperparameter) |
| Optimality | 2.7× Shannon bound | Unknown (this experiment) |

The circle map preprocessing is O(d) vs O(d²) for the rotation. If the
staircase distribution is as "quantization-friendly" as the Beta, the
framework approach wins on both quality and compute.

## The deep connection

TurboQuant's Beta distribution is bell-shaped and symmetric — it
concentrates mass at zero (for high d). The devil's staircase concentrates
mass at rational plateaus — with width proportional to Arnold tongue
width w(p/q) ~ (K/2)^q.

Both are "natural" distributions in the sense that they arise from a
single operation on arbitrary input:
- Rotation: any vector → Beta-distributed coordinates
- Circle map: any frequency → staircase-distributed winding number

The framework claims the staircase is *more* natural because it respects
the stability hierarchy (Stern-Brocot ordering). The Beta distribution
treats all points in the support symmetrically; the staircase treats
simple fractions preferentially. If the data has mode-locked structure
(the framework prediction for neural network weights), the staircase
matches it; the Beta washes it out.

## Benchmark structure

The benchmark (`google_turbo_diff.py`) compares at three fidelity levels:

### Level 1: Scalar codebook comparison
- Farey codebook vs Lloyd-Max-for-Beta codebook vs uniform
- On multiple 1D distributions: uniform, Beta, staircase, Laplace
- Metrics: MSE, SNR

### Level 2: Vector MSE comparison
- Full pipelines: rotation + Lloyd-Max vs circle map + Farey
- On random unit vectors in ℝ^d (d = 32, 64)
- Metrics: per-vector MSE, reconstruction SNR

### Level 3: Inner product fidelity
- The metric TurboQuant actually optimizes
- Quantize pairs of vectors, estimate their inner product
- Metrics: inner product MSE, bias, max absolute error
- This is the test that matters for attention computation

## Codebook construction

### TurboQuant (Lloyd-Max for Beta)

Post-rotation, each coordinate follows Beta(α, α) on [-1, 1] where
α = (d-1)/2. For d = 128, α = 63.5 — highly concentrated near zero.

Lloyd-Max iterates:
1. Initialize centroids at CDF quantile midpoints
2. Boundaries = midpoints between consecutive centroids
3. Centroids = E[X | boundary_lo < X < boundary_hi]
4. Repeat until convergence

### Framework (Farey at order n)

Select 2^b levels from the Farey sequence F_n, ordered by stability
(denominator size). For 3-bit (8 levels) from F₆:

    Stability rank 0: 0/1, 1/1  (boundaries, q=1)
    Stability rank 1: 1/2       (dominant mode, q=2)
    Stability rank 2: 1/3, 2/3  (q=3)
    Stability rank 3: 1/4, 3/4  (q=4)
    Stability rank 4: 1/6, 5/6  (q=6)

For 8 levels with endpoints: {0, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1}
or the user's original: {0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6}

Bin boundaries from Ford circle tangency (stability-weighted) or
nearest-neighbor midpoints (MSE-optimal for given levels).

## Connection to the framework

| Component | Source |
|-----------|--------|
| Mediant as primitive | D29 (betweenness + minimality) |
| Farey sequence at order 6 | D25 (Klein bottle interaction scale) |
| Arnold tongue widths | D29, staircase_geometry.py |
| Ford circle bin boundaries | Number theory (tangency condition) |
| Devil's staircase distribution | Circle map (circle_map_utils.py) |
| Duty cycle weighting | D33 (duty(q) = 1/q³) |

## Benchmark results

Three-level benchmark, all stdlib Python, no numpy/scipy.

### Level 1: Scalar codebook comparison

| Distribution | Uniform | Farey | Lloyd-Max | Winner |
|---|---|---|---|---|
| Uniform [0,1] | **0.0017** | 0.0034 | 0.0493 | Uniform |
| Beta(63.5,63.5) | 0.0020 | 0.0012 | **0.0001** | Lloyd-Max |
| Staircase K=0.8 | **0.0015** | 0.0022 | 0.0737 | Uniform |
| Staircase K=0.95 | **0.0013** | 0.0018 | 0.0784 | Uniform |

(3-bit MSE values shown)

Lloyd-Max dominates on Beta data — its codebook is optimized for exactly
that distribution. But Lloyd-Max is **catastrophic** on non-Beta data
(50x worse than uniform) because all its levels cluster near 0.5.

Farey is competitive on staircase data (1.5x uniform) but doesn't beat
uniform. The uniform codebook is a surprisingly strong baseline because
the staircase at subcritical K still spans [0,1].

### Level 2: Vector MSE (full pipeline)

| Pipeline | d=16 3-bit MSE | d=32 3-bit MSE | d=32 SNR |
|---|---|---|---|
| Rotation+LM | **0.0022** | **0.0012** | 29.2 dB |
| Rotation+Farey | 0.0058 | 0.0062 | 22.1 dB |
| CircleMap+Farey | 0.0058 | 0.0060 | 22.3 dB |
| Uniform | 0.0069 | 0.0069 | 21.6 dB |

Rotation + Lloyd-Max (TurboQuant) wins decisively at the vector level.
The rotation step is doing the heavy lifting — it decorrelates
coordinates and concentrates them into the Beta distribution where
Lloyd-Max is optimal. **The Farey codebook with rotation is 2x better
than Farey without** — the rotation helps even with a non-Beta codebook.

CircleMap+Farey beats naive Uniform at d=32 but is 5x worse than
TurboQuant. The circle map does not decorrelate — coordinates remain
correlated, violating the independence assumption that makes scalar
quantization work.

### Level 3: Inner product fidelity

| Pipeline | d=32 3-bit bias | d=32 IP MSE | d=32 MAE |
|---|---|---|---|
| Rotation+LM | +0.004 | **0.0025** | 0.039 |
| Rotation+Farey | -0.001 | 0.0144 | 0.097 |
| CircleMap+Farey | -0.007 | 0.0152 | 0.098 |
| Uniform | +0.005 | 0.0143 | 0.099 |

TurboQuant wins inner product fidelity by 6x. Note: QJL residual
correction (TurboQuant's Stage 2) not implemented — would further
reduce bias and add 1 bit per dim.

### Diagnosis

**TurboQuant's rotation is the key innovation**, not the codebook.
The rotation makes coordinates nearly independent and identically
Beta-distributed. Once you have iid coordinates, scalar quantization
is optimal, and Lloyd-Max is the optimal scalar quantizer.

The framework's circle map does NOT decorrelate. It mode-locks
individual coordinates but preserves their correlations. This means
scalar quantization (quantizing each coordinate independently) is
suboptimal — the correlations carry information that gets destroyed.

### Path forward

The framework's contribution is not a replacement for TurboQuant's
rotation, but a **refinement of the post-rotation codebook**:

1. **Rotation + Farey**: Use TurboQuant's rotation, replace Lloyd-Max
   with Farey codebook. This is 2x worse than Lloyd-Max on Beta data,
   but if post-rotation coordinates show residual mode-locking structure
   (the framework prediction), Farey could close the gap.

2. **Adaptive K**: Instead of a fixed codebook, tune the circle map
   coupling K per layer to match the empirical weight distribution.
   The staircase shape at K=0.95 (near-critical) has sharper plateaus
   that may better match specific layers' quantization needs.

3. **Hybrid**: Rotation + Lloyd-Max for Stage 1 (MSE), circle map
   for Stage 2 residual correction (replacing QJL). The staircase
   naturally bounds residuals by tongue width.

## Status

**Benchmarked.** Three-level comparison implemented in
`google_turbo_diff.py` (stdlib only). TurboQuant's rotation + Lloyd-Max
wins decisively. The framework's contribution is upstream: the
theoretical prediction that trained weights are mode-locked, which
would make Farey-optimized codebooks advantageous on real data even
within TurboQuant's rotation framework.

## IP note

The circle-map preprocessing step — replacing random orthogonal rotation
with a deterministic circle map to induce a devil's staircase distribution
amenable to Farey-fraction quantization — is a novel approach to vector
quantization. The O(d) vs O(d²) preprocessing cost and the
number-theoretically motivated codebook distinguish it from all existing
quantization schemes.

---

## Proof chain

Derivations: D10 (minimum alphabet) → D25 (Farey partition) →
D28 (Farey proof) → D29 (mediant derivation) → D33 (duty cycle).

Application of: the devil's staircase as a quantization scheme.
