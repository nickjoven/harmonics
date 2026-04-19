# α₂ derivation, Phase B: attempt and decomposition of failure

Phase B of the α₂ closure (per `a_s_alpha2_phase_a.md`). Plan:
derive α₃ (mode volume) and α₁ (combinatorial) from first
principles; α₂ then forced by residual.

**Result: Phase B does not close.** This document records the
attempt and decomposes the failure into three structural
ambiguities, each of which must be settled before any α_i can be
derived without fit. The deliverable is a precise statement of
those three sub-gaps, not a closure.

## 1. Methodology

For each step Bj, attempt the derivation as planned in Phase A §5.
At each break point, record:

- **What is non-unique** (multiple plausible answers).
- **Why it is non-unique** (a missing structural input).
- **What input would make it unique**.

A "successful" Phase B derives all three α_i unambiguously. A
"failed" Phase B identifies the precise inputs whose absence forces
the ambiguity.

## 2. B1 attempt: α₃ from cosmology mode-volume

**Setup.** Standard cosmology defines

    A_s = k³ P_R(k)/(2π²)                                       (2.1)

at k = k_pivot. In a comoving box of size L, the per-mode
spectral density is `⟨R*(k) R(k)⟩ = V_C P_R(k)` with V_C = L³.
The dimensionless A_s integrates over d ln k:

    ⟨R²⟩_real_space = ∫ d ln k × A_s × (k/k*)^{n_s−1}

For a single Stern-Brocot bracket spanning Δ ln k = 1/rate ≈ 27.4
e-folds (per Phase A: rate = (1−n_s)/ln φ² = 0.0365 levels/e-fold,
so one level covers 1/rate e-folds of k), the per-bracket variance
is approximately `⟨R²⟩_bracket ≈ A_s × Δ ln k = A_s / rate`.

**Inverting**:

    A_s = ⟨R²⟩_bracket × rate                                   (2.2)

This is the cleanest cosmology-side definition of A_s in terms of
a per-bracket quantity. **It is unambiguous.**

**Framework side.** The framework provides ⟨R²⟩_bracket via:

    ⟨R²⟩_bracket = ⟨δθ²⟩_bracket / (4π²)        (gauge: R = δθ/(2π))   (2.3)

Combining (2.2) with (2.3):

    A_s = ⟨δθ²⟩_bracket × rate / (4π²)                          (2.4)

**Numerical check at the pivot.** sigma_squared.py reads
`⟨δθ²⟩_bracket = σ² × (tongue width) = σ⁴/q²`. At σ² = K_eff = 3/2,
q = F_21 = 10946:

    ⟨δθ²⟩_bracket(sigma_squared.py reading) = (3/2)²/10946² = 1.879×10⁻⁸
    A_s_pred (Eq. 2.4)                       = 1.879e-8 × 0.0365 / (4π²)
                                              = 1.74×10⁻¹¹

vs A_s_obs = 2.1×10⁻⁹. **Off by factor 121.** Wrong direction
from the C_{A_s} = 4.415 of the formal gap doc.

**Sign of the residual: opposite.** Multiplying sigma_squared.py's
formula by `rate` makes the prediction *worse*, not better. The
implication: sigma_squared.py's `σ⁴/q²` is **already** the per-
log-k power, i.e. `A_s = σ⁴/(4π² q²) × C_{A_s}`, and the missing
factor 4.415 has nothing to do with `rate`.

**B1 break point #1.** sigma_squared.py's formula treats `σ²/q²`
(tongue width) as **either** the per-bracket variance **or** the
per-d-ln-k power, but not both. The two readings differ by `rate`
≈ 0.0365, so the implied A_s differs by ~30×. The framework has no
internal mechanism to disambiguate.

This is a **gauge-of-formula** problem: which spectral density is
A_s identified with? The standard cosmology answer is
"A_s is per d ln k", but the framework writes a per-bracket
variance — the conversion needs an explicit Jacobian
that sigma_squared.py omits.

**Result of B1**: α₃ depends on the gauge choice. At least two
plausible α₃ values, differing by ~30×. **Not closed.**

## 3. B2 attempt: α₁ from locked-state combinatorics

**Setup.** Per `spectral_tilt_reframed.md` Eq. 3.1:

    ⟨δθ²⟩(ω) ∝ g(ω) / (K_eff r*)²                              (3.1)

In the K=1 locked state with r* = 1, the denominator is
(K_eff)² = (3/2)² = 9/4. The bracket-localized variance is then

    ⟨δθ²⟩_pivot = (4/9) × g(ω_pivot) × (combinatorial)         (3.2)

**Field equation steady state.** The locked-state population at
bracket p/q satisfies `N(p/q) = g_baseline × w(p/q)` (per
field_equation_cmb.py at K_eff = 1). With uniform `g_baseline = 1`
and tongue width `w(p/q) = σ²_kernel/q² = 1/(4q²)`:

    N(p/q) ∝ 1/q²                                               (3.3)

**The g(ω) renormalization.** The phase-space density of locked
oscillators at the pivot is `g(ω_pivot) = N_pivot / w_tongue(p/q)`,
which by (3.3) gives:

    g(ω_pivot) = (1/q²) / (1/(4q²)) = 4                         (3.4)

— **bracket-independent at K=1 with uniform baseline g**. Substituting
into (3.2):

    ⟨δθ²⟩_pivot = (4/9) × 4 × (comb) = 16/9 × (comb)            (3.5)

**Bracket-independent**. This means the per-mode phase variance at
the pivot is **the same as at any other bracket** under the
uniform-g assumption.

**The q⁻² problem.** A_s_obs at q_pivot = F_21 demands
⟨δθ²⟩_pivot ∝ 1/q² ∼ 10⁻⁸ (per (2.4) inverted). Per (3.5),
⟨δθ²⟩_pivot ≈ 16/9 × O(1) — bracket-independent — with no q⁻²
factor. **Off by ~q² ≈ 10⁸.**

The 1/q² **must** enter the formula. It is present in
sigma_squared.py via the `tongue width at pivot`, but the
**spectral_tilt_reframed.md** mechanism gives a bracket-INDEPENDENT
per-mode variance. These are inconsistent.

**B2 break point #2.** The per-mode variance is q-independent
under the locked-state combinatorics, but the observable A_s
demands a 1/q² scaling. Either:

- (a) `g_baseline` is non-uniform — concentrated near 1/φ, giving
  more variance at the pivot. This requires deriving `g_baseline`
  from inflation dynamics, which the framework does not do.
- (b) The "tongue width at pivot" in sigma_squared.py is **not**
  the variance bandwidth — it represents the **gate-open fraction**
  during which the pivot mode receives perturbation. The per-d-ln-k
  power then carries the gate fraction directly, not the per-mode
  variance.

Reading (b) reproduces the q⁻² scaling sigma_squared.py-style, but
divorces from the spectral_tilt_reframed.md fluctuation formula.

**Result of B2**: α₁ depends on whether the q⁻² comes from (a) a
sourced spectrum or (b) gate dynamics. **Not closed.**

## 4. B3: α₂ by residual matching

With α₁ and α₃ both unconstrained, residual matching is undefined.
The Phase A candidates (α₂^B = 2 ln φ; α₂^C = 1/φ) remain plausible
but cannot be discriminated. **B3 inapplicable.**

## 5. Decomposition: three structural sub-gaps

The Phase B failure decomposes into three independent ambiguities,
each of which is **prior** to the α_i derivation. Closing any one
narrows the space; closing all three fixes A_s.

### 5.1 Sub-gap S1: gauge of R

Three plausible identifications of the curvature perturbation:

- **G1**: R = δθ (no 2π). Standard if the phase is naturally on
  [0, 1] (winding-number coordinate).
- **G2**: R = δθ/(2π). Standard if δθ is in radians (Kuramoto
  default). **Sigma_squared.py uses G2.**
- **G3**: R = δθ/something else (e.g. √(2π), √V_C/(2π), etc.).
  Possible if R is a renormalized field rather than the bare phase.

**What would close it**: an explicit derivation of the canonical
normalization of R from the framework's Hamiltonian / action.
Currently `continuum_limits.md` Part II identifies the linearized
sector with quantum mechanics but does not pin the curvature-
perturbation gauge.

### 5.2 Sub-gap S2: meaning of "tongue width at pivot" in the variance

sigma_squared.py treats `σ²/q²` as both:
- (M1) per-bracket variance (Eq. 2.3 above).
- (M2) per-d-ln-k power (used in §4 of the script).

These differ by `rate` ≈ 0.0365 → **factor ~30 ambiguity**.

**What would close it**: an explicit derivation of how A_s relates
to the framework's bracket variances. The chain is:

    A_s = (k*³/(2π²)) × P_R(k*) = lim k³ P_R(k)/(2π²)

and P_R(k*) needs to be computed from the bracket variances via
the staircase mode-density. This is **not done in any framework
doc**.

### 5.3 Sub-gap S3: source of the 1/q² scaling

Two structurally distinct mechanisms:
- **W1**: 1/q² as gate-open fraction at the pivot. The Arnold
  tongue at K=1 has width 1/q²; only modes within the tongue
  receive perturbation power.
- **W2**: 1/q² as per-mode variance. The δθ at the pivot is
  smaller because more modes are coupled in (per the inverse
  density of locked states).

Sigma_squared.py implicitly uses W1 (tongue width = gate fraction).
The locked-state combinatorics in §3 above implicitly use W2 and
fail to reproduce 1/q².

**What would close it**: derive whether tongue width at K=1 enters
the inflaton/curvature spectrum as a multiplicative gate fraction
or as an inverse mode-density, with the structural argument made
explicit (not just a numerical match).

### 5.4 Implication for α_i

The three sub-gaps S1–S3 each contribute one scalar factor to the
A_s prediction. Their product is exactly C_{A_s} ≈ 4.415:

| Sub-gap | Factor magnitude | Notes |
|---|---|---|
| S1 (gauge) | (2π)^k for some k = 0, ±1, ±2 | most likely k = 0 since the (2π)² in sigma_squared.py is consistent |
| S2 (formula meaning) | rate^k for k = -1, 0, +1 | likely k = 0 but the rate-bug shows non-trivial dependence |
| S3 (q⁻² source) | O(1) bracket-coordination factor | likely the missing 4/φ or 4 from lattice coordination |

The 4.415 ≈ e·φ candidate suggests S1 contributes `e` (e-folding
factor from the Hubble-volume conversion) and S3 contributes `φ`
(coordination at the golden-pivot bracket). The π√2 candidate
suggests S1 contributes `√2` (gauge-fixing factor on R) and S3
contributes `π` (solid-angle integration). **The two readings are
indistinguishable without independent S1, S2, S3 closure.**

## 6. Why Phase B failed: the deeper diagnosis

Phase B presupposed sigma_squared.py's formula `A_s = σ⁴/(4π² q²)`
as the framework's A_s prediction, and tried to derive the
correction factor C_{A_s}. The attempt revealed that
sigma_squared.py's formula is itself **not derived** — it's an
order-of-magnitude guess that gets the q-scaling right (likely via
W1) but offers no principled argument for the prefactor.

A real closure of A_s requires going one step earlier: derive A_s
directly from the framework's fluctuation spectrum with all
gauges and conversions explicit. This is a **Phase 0** problem,
not a Phase B problem. Phase B as conceived in Phase A §5 was
predicated on a derivation chain that doesn't exist in the
framework yet.

## 7. What Phase 0 would do

A reformulated path:

**P0.1**: derive the canonical normalization of R from the
linearized Kuramoto action (closes S1).

**P0.2**: derive the staircase mode-density |dN_modes/d ln k| at
the pivot bracket from the Ω-to-k map (closes S2, related to
α₂ in Phase A).

**P0.3**: derive the q⁻² source — either (a) prove the
gate-fraction reading W1 from a Hamiltonian argument, or
(b) prove the inverse-density reading W2 and reconcile with the
spectral_tilt_reframed.md combinatorics (closes S3).

After P0.1 + P0.2 + P0.3, the A_s prediction is unique and
α₁, α₂, α₃ are determined.

**Budget for P0**: each sub-step is ~1 session (focused
calculation, one structural argument). Total: 3 sessions. Heavier
than the original Phase B estimate.

## 8. Status

| Stage | Status |
|---|---|
| Phase A (definition + Binet + 4/φ identity) | **closed** |
| Phase B as conceived | **failed**, decomposed into S1, S2, S3 |
| Sub-gap S1 (R gauge) | **open** |
| Sub-gap S2 (formula meaning) | **open** |
| Sub-gap S3 (q⁻² source) | **open** |
| α₁, α₂, α₃ individual derivation | **unreachable until S1+S2+S3 close** |
| C_{A_s} ≈ 4.415 numerical target | **unchanged** |

## 9. What this Phase B accomplishes

Despite not closing A_s:

- **Identified that sigma_squared.py's starting formula is heuristic.**
  The `A_s = σ⁴/(4π² q²)` reading was being treated as a derived
  framework prediction; it isn't.
- **Pinned the failure to three independent sub-gaps**, each with
  a precise sub-question. Future work knows where to push.
- **Eliminated false routes**: multiplying by `rate` makes things
  worse (B1); the locked-state combinatorics with uniform g gives
  bracket-independent variance and can't supply 1/q² (B2);
  α₂ residual matching is undefined without α₁, α₃ (B3).
- **Reduced the open problem from "derive A_s" to "settle S1, S2,
  S3"**. The latter is structurally cleaner and decomposes into
  smaller, independent sessions.

## 10. Cross-references

| File | Role |
|---|---|
| `a_s_alpha2_phase_a.md` | Phase A: Binet, 4/φ identity, candidate list |
| `a_s_prefactor_gap_formal.md` | Defines C_{A_s} = 4.415 target |
| `a_s_amplitude_audit.md` | Three-σ² disambiguation, identifies sigma_squared.py misattribution |
| `sigma_squared.py` | Source of the **heuristic** A_s formula |
| `spectral_tilt_reframed.md` | Source of (3.1); shows per-mode variance is bracket-independent |
| `continuum_limits.md` Part II | Where R-gauge derivation should go (currently absent) |
| `field_equation_cmb.py` | Confirms N(p/q) ∝ tongue width at K=1 |
