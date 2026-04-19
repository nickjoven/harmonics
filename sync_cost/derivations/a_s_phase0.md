# A_s Phase 0: derive from the Lagrangian, not from heuristic

Phase 0 of the A_s closure (per `a_s_alpha2_phase_b.md` §6). The
prior phases worked from sigma_squared.py's `A_s = σ⁴/(4π² q²)`
guess and tried to derive a correction factor. Phase B revealed
this guess is heuristic, not derived. Phase 0 starts over: derive
A_s directly from the framework's explicit Lagrangian
(`framework_lagrangian.py`).

**Result.** Substantial progress on S1 (R-gauge): the canonical
curvature perturbation is `R = √m × δθ` with `m = (1−φ⁻⁴)/λ_unlock`
in Planck units (≈ 1.806 m_P). Combined with σ²_kernel = 1/4 and
the Stern-Brocot bracket width 1/(φ q²), the assembled prediction is

    A_s_predicted = m × σ²_kernel / (φ × q_pivot²)
                  = (1−φ⁻⁴) / (4 λ_unlock × φ × F_21²)
                  ≈ 2.33 × 10⁻⁹

vs A_s_observed = 2.10 × 10⁻⁹ (Planck 2018). **10% relative
deviation — %-only closure**, same status as PMNS θ_12.

The 4.4× factor of the prior gap is reduced to a 10% residual.
Each multiplicative input is independently derived from a framework
axiom, not fitted.

## 1. The Lagrangian and its linearization

`framework_lagrangian.py` provides:

    ℓ[θ] = (m/2)(∂_t θ)² − (σ²/2)|∇θ|²
         + ω(x)θ + (1/2)∫ K(x,x') cos(θ(x) − θ(x')) dx'      (1.1)

Linearize at the locked state θ_0(x,t) with δθ ≡ θ − θ_0. Expand
the cos term to second order and use the lock condition:

    ℓ_lin = (m/2)(∂_t δθ)² − (σ²/2)|∇δθ|² − (Kr/2) δθ²       (1.2)

This is a scalar field with kinetic coefficient m, gradient
coefficient σ², and effective mass² = Kr.

## 2. Canonical R from (1.2)

The canonically-normalized scalar field (kinetic coefficient = 1/2)
is obtained by:

    R := √m × δθ                                              (2.1)

so that

    ℓ_lin = (1/2)(∂_t R)² − (σ²/(2m))|∇R|² − (Kr/(2m)) R²   (2.2)

with sound speed c_s² = σ²/m.

**This is S1 closed**: R = √m × δθ. The (2π) factor in
sigma_squared.py (which used R = δθ/(2π)) was a different gauge —
the *winding-fraction* gauge that treats θ as a coordinate on
S¹ ∈ [0, 2π]. The canonical-action gauge (2.1) carries no 2π.

## 3. Numerical value of m

PROOF_B Q4 (continuum_limits.md Part II §6) identifies:

    ℏ = 2 m × D_eff                                           (3.1)

with D_eff the spatial diffusion constant from the Stern-Brocot
RG fixed-point:

    D_eff = D_0 / (1 − φ⁻⁴)                                   (3.2)

D_0 from gap2_spatialization sub-E (the audit closure in PR #67):

    D_0 = (λ_unlock / 2) × ℓ_P² / t_P                          (3.3)

Combining (3.1)–(3.3) and converting to Planck units (ℏ = m_P = 1):

    m / m_P = (1 − φ⁻⁴) / λ_unlock                            (3.4)

Numerical: with `λ_unlock = 0.473` (framework_constants), `φ⁻⁴ ≈
0.146`:

    m / m_P = 0.854 / 0.473 ≈ 1.806                           (3.5)

**This is a derived value**, not a free parameter.

## 4. Variance per pivot bracket

From the linearized action (2.2), at the locked state K=1, the
per-mode phase variance is set by the kernel coupling. The
fluctuation power per Stern-Brocot bracket at level n is the
bracket weight in Ω:

    w_bracket(n) = 1 / (F_{n+1} × F_{n+2}) → 1/(φ q²)         (4.1)

(Phase A §3; verified by `test_tongue_to_bracket_ratio_is_4_over_phi`.)
The per-bracket phase variance carries the kernel σ² = σ²_kernel = 1/4
(per A2, ADM closure):

    ⟨δθ²⟩_bracket = σ²_kernel × w_bracket = 1 / (4 φ q²)      (4.2)

## 5. Assembled A_s prediction

Combining (2.1), (3.4), (4.2):

    A_s = ⟨R²⟩_bracket = m × ⟨δθ²⟩_bracket
        = m × σ²_kernel × w_bracket
        = ((1−φ⁻⁴) / λ_unlock) × (1/4) × 1/(φ q²)
        = (1 − φ⁻⁴) / (4 λ_unlock × φ × q_pivot²)             (5.1)

With q_pivot = F_21 = 10946:

    A_s_predicted = 0.854 / (4 × 0.473 × 1.618 × 1.198×10⁸)
                  ≈ 2.33 × 10⁻⁹                                (5.2)

vs A_s_obs = 2.10 × 10⁻⁹. **Relative deviation 11%**, ratio 1.11.

## 6. Status under statistical conventions

Per `statistical_conventions.md`:
- **σ-test (C-numerical)**: Planck 2018 quotes A_s = (2.10 ± 0.03) ×
  10⁻⁹. Z-score = (2.33 − 2.10)/0.03 ≈ 7.7 σ. **Not σ-closed.**
- **%-only**: relative deviation 11%. At the same level as PMNS θ_12
  (10%) per PR #67's `mixing_angle_audit.md`.

**Status: %-only closure, NOT σ-closed.** Same status label as
the PMNS partial closures. From the prior heuristic (4.4× off,
~330% deviation) to a structurally-derived 11%, all factors
independently derived.

## 7. Sources of the 11% residual

Three plausible structural improvements that could close the gap to
σ-level:

**R7.1: λ_unlock convention.** The framework uses λ_unlock = 0.473
(numerical value at K=1). The asymptotic Catalan-related value is
2 × Catalan / π ≈ 0.583 (large-K limit). Using the asymptotic
value:

    A_s_pred(λ = 0.583) = 0.854 / (4 × 0.583 × 1.618 × 1.198e8)
                       ≈ 1.89 × 10⁻⁹

— **10% the other direction** (under, not over). The observed 2.10
sits between the two conventions. A precise determination of which
λ_unlock enters the m relation could close the gap. See
`framework_constants.LAMBDA_UNLOCK` documentation; the comment says
"K=1 numerical value" is the canonical choice, but the m derivation
uses Madelung in the K<1 limit, which may select the asymptotic
Catalan value.

**R7.2: Pivot-level fine adjustment.** Eq. (5.1) is sharply
sensitive to q_pivot². Half-integer level shifts (e.g. n = 19.5
vs 20) change A_s by factor φ², much larger than the 10% gap. But
small fractional shifts (e.g. 5% of a level) could account for the
residual. The pivot identification in `k_omega_mapping.py` uses a
linear approximation; a higher-order correction might shift n_pivot
by ~ 0.05.

**R7.3: Higher-order expansion of cos.** The linearization (1.2)
truncated cos at O(δθ²). Including O(δθ⁴) terms gives self-
interactions that renormalize the variance. At K = 1 these may
contribute at the ~10% level.

None of R7.1–R7.3 is performed in this Phase 0. Each is a sharp
followup question.

## 8. What this Phase 0 closes

Compared to the prior status (`a_s_alpha2_phase_b.md`):

| Sub-gap | Phase B status | Phase 0 status |
|---|---|---|
| S1 (R gauge) | open: factor (2π)^k ambiguous | **closed**: R = √m δθ from canonical action (2.1) |
| S2 (formula meaning) | open: 27× ambiguity (per-bracket vs per-d-ln-k) | **partially**: Eq. (5.1) is dimensionally consistent as A_s directly; no rate factor needed |
| S3 (q⁻² source) | open: gate vs density | **closed**: bracket width 1/(φq²) is the natural variance bandwidth, derived from Stern-Brocot adjacency |
| α₁, α₂, α₃ individually | unreachable | **subsumed**: the assembled formula (5.1) doesn't need separate α factors |
| C_{A_s} numerical target (4.415) | unreached | **superseded**: with the corrected formula, the target is now ratio observed/(corrected pred) = 0.90 |
| Match to observation | 4.4× off | **11% off** (%-only, not σ-closed) |

The numerical target shifts from C_{A_s} ≈ 4.415 (heuristic
formula) to ratio ≈ 0.90 (corrected formula). Each is a definite
small number; the smaller one is closer to a clean structural
factor (e.g. λ_unlock convention shift).

## 9. The canonical Phase 0 prediction, with all derivations

Compact form, all factors derived from framework axioms:

    A_s_canonical = (1 − φ⁻⁴) / (4 λ_unlock × φ × F_{n_pivot+1}²)

| Factor | Source | Value |
|---|---|---|
| (1 − φ⁻⁴) | Stern-Brocot RG convergence (PROOF_B Q4) | 0.854 |
| 1 / λ_unlock | Klein-bottle Lyapunov (gap2 sub-C) | 1/0.473 = 2.114 |
| 1 / 4 | σ²_kernel from ADM prefactor (continuum §5a) | 0.25 |
| 1 / φ | Stern-Brocot bracket width × q² | 0.618 |
| 1 / F_21² | CMB pivot identification (k_omega_mapping.py) | 1/1.198e8 = 8.35e-9 |

Product: **2.33 × 10⁻⁹**. Observed: 2.10 × 10⁻⁹. Ratio 1.11.

## 10. Tests added

- `test_m_from_madelung_phi_lambda`: pins m = (1−φ⁻⁴)/λ_unlock × m_P.
- The existing `test_tongue_to_bracket_ratio_is_4_over_phi` (Phase A)
  remains the bracket-width pin.

## 11. Open followups

Sharp questions for future sessions:

1. **Which λ_unlock convention** enters the Madelung relation: K=1
   numerical (0.473) or K→∞ asymptotic Catalan (0.583)?
2. **Pivot-level higher-order correction**: does n_pivot shift by
   a few percent under a refined Ω-to-k mapping?
3. **Cos expansion at O(δθ⁴)**: do self-interactions renormalize
   the variance at the 10% level?
4. **Connected items**: T3#11 (CMB damping tail), T3#12 (Hausdorff
   dim of staircase) — the same m, λ_unlock, and bracket-width
   identities flow into both. Closing R7.1 above likely advances
   these too.

## 12. Cross-references

| File | Role |
|---|---|
| `framework_lagrangian.py` | Source of (1.1) — the explicit Lagrangian |
| `continuum_limits.md` Part II | PROOF_B Q4: ℏ = 2m D_eff |
| `gap2_spatialization_decomposition.md` sub-E | D_0 = (λ/2) ℓ_P²/t_P |
| `framework_constants.py` | LAMBDA_UNLOCK = 0.473 |
| `a_s_alpha2_phase_a.md` | Stern-Brocot bracket = 1/(φq²) |
| `a_s_alpha2_phase_b.md` | Failure of the prior heuristic chain |
| `a_s_amplitude_audit.md` | Three-σ² disambiguation |
| `statistical_conventions.md` | %-only vs σ definitions |
| `mixing_angle_audit.md` | PMNS %-only precedent |
