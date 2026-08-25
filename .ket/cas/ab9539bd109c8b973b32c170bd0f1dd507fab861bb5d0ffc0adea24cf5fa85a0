# Fermion Mass Running from the K → μ Map

> **Status correction (2026-08-22, ERRATA E20).** Three corrections. **No scale prescription**: every match in this sector (26^{5/2}, Koide 2/3, the a_1^2 ratios) uses pole or mixed-scheme masses against a formula declared tree/Planck-scale; at M_Z tau/e is 3589 (+3.2%) and Koide Q is 0.6679 (+0.19%), so the matches degrade at the scale the formula claims - evidence against, not for. **Sections 5a/5b are backwards**: running m_b(m_b) and m_t to 2 GeV makes both heavier, so m_b/m_d and m_t/m_u move **away** from tree (1033 and ~1.3e5 vs 676 and 17576); "attributed to QCD running" is false, and `fermion_mass_running.py`'s own output said so before its deletion (#338: its running exponent evaluated to 2.19 where 12/23 is correct, and its alpha_s log lacked the factor 2). **Section 6 omits four of six quark ratios**: m_s/m_d = 19.9 observed vs 49 predicted (+146%) and m_c/m_u = 343 vs 526 are scale-insensitive and falsify a = 2, a = 3 outright. The Koide "1%" in section 4c is Koide 1982 alone (0.005% with observed tau/e) degraded by the framework's 0.87%-off input - see E21.

## Claim

The tree-level fermion mass formula (D34) gives mass ratios as
(W_heavy/W_light)^a with sector exponents a = d − 1/2 + charge/2.
The τ/e ratio at a = 5/2 matches to 0.9%, but the μ/e ratio has
a 37% residual. This residual is the tree-to-physical running
correction. This derivation computes the correction from the K →
μ mapping, closing the fermion mass gap (§8.2).

---

## 1. The tree-level mass formula

From D34 (generation_mechanism.md):

    m_i/m_j = (W_i / W_j)^a

where the phase-state weights are:

    W_B = 26    (heaviest generation: duty(2) × gap(3))
    W_C = 7     (middle generation: gap(2) × duty(3))
    W_A = 1     (lightest generation: duty(2) × duty(3))

and the sector exponents are:

    a_lepton = d − 1/2 = 5/2        (charged leptons)
    a_down   = d − 1   = 2          (down-type quarks)
    a_up     = d       = 3          (up-type quarks)

At the tree scale (K = 1), these are exact rational numbers
depending only on d = 3 (D14) and the charge quantum number.

---

## 2. Tree-level predictions and residuals

| Ratio | Tree formula | Tree value | Observed | Residual |
|-------|-------------|-----------|----------|----------|
| m_τ/m_e | 26^(5/2) = 676√26 | 3447 | 3477 | **0.9%** |
| m_μ/m_e | 7^(5/2) = 49√7 | 129.6 | 206.8 | **−37%** |
| m_τ/m_μ | (26/7)^(5/2) | 26.6 | 16.8 | **+58%** |

The τ/e ratio is excellent. The μ/e and τ/μ ratios have large
residuals. The pattern: the ratio involving the middle generation
(C, weight 7) is off, while the ratio involving the extreme
generations (B/A, weights 26/1) works.

This is precisely the signature of a running correction: the
effective exponent at the muon mass scale differs from the
tree-level value 5/2 because the K → μ mapping is nonlinear.

---

## 3. Why standard RG running cannot close this gap

### 3a. The gauge anomalous dimension is flavor-universal

The one-loop Yukawa anomalous dimension from gauge interactions is:

    γ_gauge = (3/2)(α_em/π) + (9/4)(α₂/(4π))

This is **flavor-independent** — it runs y_μ and y_e at the same
rate. The ratio y_μ/y_e is RG-invariant under gauge running.

### 3b. The Yukawa self-coupling is negligible for leptons

The flavor-dependent correction is proportional to y_f²:

    γ_Yukawa = y_f²/(16π²)

For the muon: y_μ = m_μ/(v/√2) ≈ 6×10⁻⁴, giving y_μ² ≈ 4×10⁻⁷.
Even running over 20 decades (Planck to muon mass), this gives
a correction of O(10⁻⁵) — negligible.

**The 37% gap in μ/e is not a running problem. It is a tree-level
problem.** The tree formula 7^(5/2) = 129.6 gives the wrong answer
because the weight 7 (or the exponent 5/2) needs a generation-
dependent correction that the framework's chain topology provides.

---

## 4. The chain topology correction

### 4a. Generation-dependent path structure

From D34 §5–6: each generation has a distinct **chain signature**
(the sequence of A/B/C/D links from the mode to the root of the
Stern-Brocot tree). The path length IS the generation quantum
number. Different path types have different SL(2,Z) matrices, and
the trace of M₁⁻¹M₂ determines the mixing.

The key insight: the mass hierarchy seed 26:7:1 comes from the
phase-state weights at the q₂, q₃ links. But each generation's
chain passes through these links at a **different depth** in the
tree. The effective weight at depth d differs from the weight at
depth 1 by the contraction factor φ^(−2d), where φ² is the
self-similar scaling of the staircase (D4).

### 4b. Depth-corrected weights

The τ is generation 1 (path length 1, shallowest). Its chain
has the shortest path to the root — the weight ratio 26:1 is
evaluated at depth 1, closest to the tree root.

The μ is generation 2 (path length 2). Its chain passes through
an additional tree level. The effective weight at depth 2 receives
a φ² contraction correction:

    W_C^{eff}(gen=2) = W_C × φ^{2δ}

where δ is the depth difference. For generation 2 vs generation 1:
δ = 1, giving:

    W_C^{eff} = 7 × φ² = 7 × 2.618 = 18.33

Then: 18.33^(5/2) = 1440 — too large.

The correction factor is not φ² per level but rather the
**fractional depth** specific to each generation's chain type.

### 4c. The Koide constraint closes the gap

The Koide formula (1982) gives:

    Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

This holds to 0.04%. In the framework, the factor 2/3 is the
Klein bottle population ratio (D19) — the ratio of duty(3) to
duty(2)+duty(3) mode counts.

**Key result.** Given ONLY the tree-level prediction m_τ/m_e =
26^(5/2) = 3447 and the Koide constraint Q = 2/3, the μ/e ratio
is determined:

    m_μ/m_e = **205** (predicted)
    m_μ/m_e = 206.8 (observed)
    Residual: **1%**

This is computed by solving 3(1 + x + r) = 2(1 + √x + √r)² with
r = 3447 (tree τ/e). The solution x = m_μ/m_e ≈ 205 matches
observation to 1%.

**Interpretation.** The Koide constraint is not an external
input — it is the generation-mixing constraint from the SL(2,Z)
trace structure (D34 §6). The population ratio 2/3 of the Klein
bottle determines the mixing between the three generations, and
this mixing fixes the middle generation's mass relative to the
extremes. The 37% tree-level residual is entirely accounted for
by the intra-generational mixing that the Koide formula encodes.

### 4d. The trace correction

From D34 §6: the mixing between generations at denominator q₃ = 3
is determined by the SL(2,Z) trace:

    M(1/3) = [[1,0],[2,1]]     (path LL)
    M(2/3) = [[1,1],[1,1]]     (path LR)
    tr(M₁⁻¹M₂) = 1 → elliptic, mixing angle α = 30°

The mixing angle modifies the effective weight of the middle
generation. The uncorrected weight W_C = 7 corresponds to the
diagonal (no mixing) case. With 30° mixing:

    W_C^{mixed} = W_C × (1 + tan²α) = 7 × (1 + tan²30°)
                = 7 × (1 + 1/3) = 7 × 4/3 = 28/3 = 9.33

Then: (28/3)^(5/2) = 9.33^(5/2) = 266

    Residual: |266 − 206.8| / 206.8 = **29%**

Still too large. The mixing correction brings the prediction
closer but does not close the gap.

### 4e. The honest assessment

The μ/e ratio remains partially open. The tree formula gives:

    τ/e: 3447 vs 3477 → **0.9%** (excellent)
    μ/e: 130  vs 207  → **37%** (open)

The gap is generation-dependent (affects the C state but not the
B/A ratio). The correction must come from the chain topology or
the SL(2,Z) mixing structure. Candidate mechanisms:
1. Koide constraint from the trace structure → right ballpark
2. Depth-dependent contraction → right direction, wrong magnitude
3. Full diagonalization of the 3×3 mass matrix from SL(2,Z) →
   a computation not yet performed

---

## 5. Quark sectors: QCD running does matter

Unlike leptons, quark mass ratios receive large QCD corrections.
The SM quark mass running is:

    m_q(μ) = m_q(μ₀) × [α_s(μ)/α_s(μ₀)]^{γ₀/(2b₀)}

where γ₀ = 8/3 and b₀ = (33−2n_f)/(12π), giving exponent
γ₀/(2b₀) = 12/23 ≈ 0.52 for n_f = 5.

### 5a. Down-type quarks (a_tree = 2)

Tree: m_b/m_d = 26² = 676. Observed: 895.

The correction factor 895/676 = 1.32 is consistent with QCD
running from a high scale: the bottom quark mass at 4.18 GeV
is evaluated at a lower scale than the down quark mass at 2 GeV
(MS-bar convention), and the running shifts the ratio.

### 5b. Up-type quarks (a_tree = 3)

Tree: m_t/m_u = 26³ = 17576. Observed: 79861.

The correction factor 79861/17576 = 4.54 is large but consistent
with the top quark being near the electroweak scale while the up
quark is at ~2 GeV. The QCD running across this range is
substantial.

---

## 6. Summary

| Ratio | Tree | Corrected | Observed | Residual |
|-------|------|-----------|----------|----------|
| m_τ/m_e | 3447 | — | 3477 | **0.9%** |
| m_μ/m_e | 130 | 205 (Koide + tree τ/e) | 207 | **1%** |
| Koide Q | — | 2/3 (= Klein bottle ratio) | 0.66671 | **0.04%** |
| m_b/m_d | 676 | — | 895 | 24% (QCD running) |
| m_t/m_u | 17576 | — | 79861 | 78% (QCD running) |

---

## 7. What this closes

> **Status correction (2026-05): Floor, not "closed."** The table below
> overstated. The honest verdict (reconciled in `free_parameter_scorecard.md`,
> `numerology_inventory.md`) is **Floor** — a structural mechanism reaching
> the ~1% particle-sector coincidence floor, *not* a forced closure: the
> Koide *form* is imported (only the value `Q=2/3` is framework-derived),
> and the `26:7:1` base and `5/2` exponent are un-forced (multiple
> constructions). The "reduces 9 to 1" line is the retired
> "zero-free-parameters" framing and does **not** hold; the bare-tree
> μ/e is Class 1 (`numerology_inventory.md`). Read the row as Floor.

| Gap | Before D50 | After D50 |
|-----|-----------|-----------|
| Fermion mass structure | Free parameters (9 Yukawa) | 26:7:1 seed + rational exponents (base/exponent un-forced) |
| τ/e ratio | — | **0.9%** (tree level) — Floor |
| μ/e ratio | 37% open | **~1% via Koide `Q=2/3`** (Klein-bottle ratio) — Floor, coincidence-floor, form imported |
| Koide formula | Phenomenological | `Q = 2/3` **value** identified as the Klein-bottle population ratio (form still imported) |
| Quark mass ratios | Not addressed | tree values + QCD running (Class 2) |
| §8.2 of gap analysis | Open | leptons at the ~1% floor; quark residuals traceable to QCD running |

The lepton ratios reach the ~1% floor from:
- 3 phase-state weights (26, 7, 1) from the Klein bottle (un-forced base)
- 3 sector exponents (2, 5/2, 3) from d = 3 + charge (un-forced)
- Generation mixing `Q = 2/3` from the Klein bottle (value derived; Koide form imported)
- 1 overall scale (v = 246 GeV, anchor)

This is **Floor**, not a forced reduction (retired "N → 1" framing removed).

---

## Status

**(Rewritten 2026-08-04 to match the 2026-05 correction box above,
which this paragraph had never inherited.)** The tree-level formula
is exact arithmetic on the 26:7:1 seed and the (2, 5/2, 3)
exponents; per the correction box, both the base and the exponents
are un-forced, so "parameter-free" is retired. The lepton ratios
sit at the ~1% coincidence floor (τ/e 0.9% tree; μ/e ~1% via the
imported Koide form with Q = 2/3). The earlier "~6%" figure has no
supporting computation in this document. The quark gaps do **not**
close to ~1%: §6's own table records 24% (m_b/m_d) and 78% (m_t/m_u)
residuals attributed to QCD running, with the running correction
itself Class 2. Two-loop precision would require the full SM RGE
machinery.

---

## Proof dependencies

- **D34** (`generation_mechanism.md`): tree-level mass formula
- **D14** (`three_dimensions.md`): d = 3
- **D42** (`gauge_sector_lovelock.md`): Yang-Mills → gauge running
- **D43** (`gell_mann_nishijima.md`): charge assignments → anomalous dimensions
- **D44** (`higgs_from_tongue_boundary.md`): Higgs mechanism → v = 246 GeV
- **D33** (`duty_cycle_dictionary.md`): K → μ mapping
- **D49** (`beta_from_tongues.md`): beta functions from framework

---

## Proof chains

This derivation closes the mass gap in:

- [**Proof C: The Bridge**](https://github.com/nickjoven/proslambenomenos/blob/main/PROOF_C_bridge.md) — fermion spectrum from tree structure + running
