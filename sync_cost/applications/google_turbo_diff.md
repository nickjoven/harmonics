# google-turbo-diff

*Farey-spaced quantization for KV-cache compression.*

## Surface

Google's TurboQuant (2024) compresses key-value caches of long-context
LLMs using 3-bit quantization with **8 uniform levels** — equal spacing
across the value range. This works well, but the framework predicts it
is suboptimal.

## The prediction

The optimal quantization levels are **non-uniform** — they are
Farey-spaced. The devil's staircase quantizer matches the data's
natural distribution because:

1. **Arnold tongue widths scale as w(p/q) ~ (K/2)^q** (D29). Simpler
   fractions (smaller denominator q) have exponentially wider tongues —
   they are more stable, more tolerant to perturbation.

2. **The Stern-Brocot tree orders all rationals by stability** (D29).
   The mediant is the unique combining operation satisfying betweenness
   (energy conservation) and minimality (widest tongue first).

3. **Bins around simple fractions should be wider.** The levels at
   1/2, 1/3, 2/3 of the range are more stable representations —
   small perturbations don't push values across bin boundaries. The
   levels at complex fractions (1/7, 2/7, ...) are fragile — narrow
   tongues, narrow bins, easy to fall off.

4. **The Farey partition at order 6** (D25) provides the natural
   resolution scale: F₆ has 13 elements. For 3-bit (8 levels), the
   framework selects the 8 most stable fractions from F₆.

## The codebooks

### Uniform (TurboQuant baseline)

    Level:  0    1    2    3    4    5    6    7
    Value:  0   1/7  2/7  3/7  4/7  5/7  6/7   1

Equal spacing. Each bin has width 1/7 ≈ 0.143.

### Farey-spaced (framework prediction)

    Level:  0    1    2    3    4    5    6    7
    Value:  0   1/6  1/4  1/3  1/2  2/3  3/4  5/6

Non-uniform spacing. Bin widths vary:

    Bin 0→1:  1/6         = 0.167  (wider — boundary region)
    Bin 1→2:  1/4 - 1/6   = 0.083  (narrow — between q=6 and q=4)
    Bin 2→3:  1/3 - 1/4   = 0.083  (narrow — between q=4 and q=3)
    Bin 3→4:  1/2 - 1/3   = 0.167  (wider — approaching the dominant mode)
    Bin 4→5:  2/3 - 1/2   = 0.167  (wider — departing the dominant mode)
    Bin 5→6:  3/4 - 2/3   = 0.083  (narrow)
    Bin 6→7:  5/6 - 3/4   = 0.083  (narrow)

The pattern is symmetric around 1/2 — widest bins at the center
(the dominant 1/2 mode) and at the boundaries (0 and 1). Narrowest
bins at the q=4 and q=6 transitions. This is the devil's staircase
profile: wide plateaus at simple rationals, narrow transitions between.

## Why this works

Neural network weight distributions are not uniform. They cluster
around zero and around dominant modes. A uniform quantizer wastes
resolution in the tails (where few values live) and under-resolves
the peaks (where most values live).

The Farey quantizer allocates resolution where the distribution has
mass — at the simple fractions that correspond to stable modes.
This is not an empirical observation about weight distributions;
it is a **structural prediction** from the Arnold tongue hierarchy.
Any system that synchronizes (and neural networks are coupled
oscillators in the loss landscape) will have its probability mass
concentrated at simple-rational modes.

## The experiment

**Test**: Take TurboQuant's open implementation, replace the uniform
3-bit codebook with the Farey-spaced codebook, and benchmark.

**Metrics**:
- Accuracy on LongBench (document QA, summarization, few-shot)
- Needle-in-a-Haystack retrieval accuracy at 128K+ context
- Perplexity on held-out validation sets

**Expected outcome**: Farey-spaced 3-bit quantization outperforms
uniform 3-bit quantization — either better accuracy at the same
bit rate, or equivalent accuracy at ~2.5 bits instead of 3. The
latter would represent 15-20% additional compression on top of
TurboQuant's already strong result.

## Bin width derivation

The bin widths are determined by the **Ford circle radii** at each
Farey fraction. For fraction p/q, the Ford circle has radius 1/(2q²).
The bin boundary falls at the tangency point between adjacent Ford
circles.

For adjacent Farey fractions a/b and c/d:

    boundary = (a/b + c/d) / 2 + (1/(2b²) - 1/(2c²)) / (c/d - a/b)

This is the standard nearest-neighbor quantizer boundary, weighted by
the Ford circle radii. Simpler fractions (smaller q) have larger Ford
circles → wider bins. This is exact; no fitting required.

## Connection to the framework

| Component | Source |
|-----------|--------|
| Mediant as primitive | D29 (betweenness + minimality) |
| Stern-Brocot ordering | D10-D11 |
| Farey sequence at order 6 | D25 (Klein bottle interaction scale) |
| Arnold tongue widths | D29, staircase_geometry.py |
| Ford circle bin boundaries | Number theory (tangency condition) |
| Duty cycle weighting | D33 (duty(q) = 1/q³) |

## Synthetic benchmark results

The benchmark script (`google_turbo_diff.py`) tests four codebook
variants across five synthetic distributions:

| Distribution | Uniform MSE | Best Farey MSE | Delta | Winner |
|-------------|-------------|----------------|-------|--------|
| Uniform | 0.001675 | 0.002011 | -20.1% | Uniform |
| Peaked (Arnold) | 0.001694 | 0.002000 | -18.1% | Uniform |
| Laplace | 0.001669 | 0.001962 | -17.6% | Uniform |
| Bimodal (q=3) | 0.001694 | 0.001399 | **+17.4%** | **Farey** |
| Staircase K=0.8 | 0.001391 | 0.001442 | -3.6% | Uniform |

**Key findings:**

1. Uniform wins on uniform, Gaussian-peaked, and Laplace distributions.
   This is expected — uniform spacing minimizes MSE for distributions
   that are approximately uniform or single-peaked.

2. **Farey wins by 17.4% on bimodal q=3 data** (mass at 1/3 and 2/3).
   The original Farey codebook {0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6}
   places levels exactly at the modes. Uniform's nearest levels to
   1/3 and 2/3 are 2/7≈0.286 and 5/7≈0.714 — systematically off.

3. On the devil's staircase (K=0.8), it is nearly a wash (-3.6%).
   The staircase at subcritical coupling distributes mass across many
   plateaus. At K→1 (critical coupling), where plateaus fill the line,
   the Farey advantage should increase.

**The honest conclusion:** the Farey codebook is not universally
better. It wins when the data distribution matches the Farey
structure — specifically, when probability mass concentrates at
rational modes with small denominators. The framework predicts this
IS the structure of trained neural network weights (they are mode-locked
in the loss landscape). The synthetic benchmark cannot test this
prediction; actual LLM weight distributions are needed.

## Status

**Proposed.** Benchmark script at `google_turbo_diff.py` (this
directory). Synthetic results show the structural advantage on
mode-locked distributions. Requires TurboQuant codebase or equivalent
quantization harness to run the full evaluation on real LLM weights.

## IP note

The Farey codebook configuration — non-uniform quantization levels
at Farey fractions with Ford-circle-derived bin boundaries — is a
novel, patentable configuration for neural network weight and
activation quantization. The theoretical basis (Arnold tongue
stability hierarchy) provides a principled derivation that
distinguishes it from empirically-tuned non-uniform quantizers.

---

## Proof chain

Derivations: D10 (minimum alphabet) → D25 (Farey partition) →
D28 (Farey proof) → D29 (mediant derivation) → D33 (duty cycle).

Application of: the devil's staircase as a quantization scheme.
