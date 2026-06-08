# LMFDB query — newform 6.4.a.a (substrate retrieval record)

**URL:** https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/6/4/a/a/
**Retrieved:** 2026-06-08
**Context:** External substrate check for Hecke eigenvalues, Atkin-
Lehner signs, and root number of f_{6,4}. Closes F-cusp-1 (PR #244)
and F-W6-3 (PR #246).

## Retrieved values (verbatim)

### Hecke eigenvalues
| p | a_p |
|---|---|
| 2 | −2 |
| 3 | −3 |
| 5 | 6 |
| 7 | −16 |
| 11 | 12 |
| 13 | 38 |
| **17** | **−126** |
| **19** | **+20** |
| 23 | 168 |
| 29 | 30 |
| 31 | 88 |

### Atkin-Lehner signs
- **w_2 = +1**
- **w_3 = +1**

### Root number (Fricke)
- ε = +1

### Basic parameters
- Weight: 4
- Level: 6
- Character orbit: 6.a (trivial)
- Dimension: 1
- Self-dual: yes
- Twist minimal: yes
- Analytic rank: 0

## Cross-checks consistent with retrieved values

### Deligne bound at p = 17
|a_17| ≤ 2 · 17^(3/2) = 140.19...
|−126| = 126 ≤ 140.19 ✓

### Deligne bound at p = 19
|a_19| ≤ 2 · 19^(3/2) = 165.65...
|+20| = 20 ≤ 165.65 ✓

### Steinberg sign relation at Mihailescu primes
For weight k = 4 with multiplicative (Steinberg-type) reduction at p:
- Split multiplicative: a_p = +p, w_p = −1
- Non-split multiplicative: a_p = −p, w_p = +1

Retrieved a_2 = −2, w_2 = +1 → **non-split** multiplicative at p = 2.
Retrieved a_3 = −3, w_3 = +1 → **non-split** multiplicative at p = 3.

Root number ε = w_2 · w_3 = (+1)(+1) = +1, consistent with retrieved ε.

### Sato-Tate angle at p = 17
a_p / (2 · p^((k−1)/2)) = −126 / 140.19 = −0.8988
θ_17 = arccos(−0.8988) ≈ 153.96°
Highly off-center; close to the boundary of the semicircle distribution.

### Hecke recursion (good-prime spot checks)
Using a_2 = −2, a_3 = −3, a_5 = 6, multiplicativity for coprime
indices, and a_{p^k} = a_p · a_{p^(k−1)} − p^(k−1) · a_{p^(k−2)} at
good primes:
- a_4 = a_2² − 2 · a_1 = 4 − 2 = 2  (NB: bad-prime recursion: a_{p^k} = a_p^k for p | N → a_4 = (−2)² = 4)
- a_6 = a_2 · a_3 = 6
- a_15 = a_3 · a_5 = −18
- a_35 = a_5 · a_7 = −96

Spot checks consistent with retrieved values.

## What this overturns

Values asserted in PRs #244, #245, #246 from session cache (NOT
from substrate retrieval), now superseded:

| Quantity | Asserted (prior session cache) | LMFDB substrate (this retrieval) | Status |
|---|---|---|---|
| a_17 | −18 | **−126** | OVERTURNED |
| a_19 | −100 | **+20** | OVERTURNED |
| w_2 | −1 | **+1** | OVERTURNED |
| w_3 | −1 | **+1** | OVERTURNED |
| Reduction type at 2, 3 | "split multiplicative" | **non-split multiplicative** | OVERTURNED |
| Root number ε | +1 | +1 | Confirmed (correct for wrong reason) |
| a_2, a_3, a_5, a_7, a_11, a_13 | as listed | match | Confirmed |
| Weight, level, dim | 4, 6, 1 | match | Confirmed |

## Diagnosis

The prior assertions were cached from session memory of "what LMFDB
6.4.a.a says," never retrieved from the substrate this session. Per
harmonics CLAUDE.md verify-before-assert protocol, this is exactly
the failure mode the protocol exists to prevent: a *fabricated cache
entry* presented at substrate-fact resolution.

The W_d cusp action computation in PR #246 §2 used pure modular
arithmetic and was independently re-derivable; it survives. The
Hecke eigenvalue and Atkin-Lehner sign assertions did not, because
their content is not derivable from modular arithmetic — it requires
substrate retrieval (LMFDB / SAGE) or numerical eigenform computation,
neither of which was performed at the time of original audit.

## Companion verification

`scripts/verify/w6_cusp_action_verify.py` — pure-Python reproduction
of the W_d cusp action, which closes F-W6-1 independently of LMFDB.
Run: `python3 scripts/verify/w6_cusp_action_verify.py`.
