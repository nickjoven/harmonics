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

## 7. Sources of the 11% residual (post-audit)

Audited in `a_s_phase0_lambda_audit.py`. R7.1 is now ruled out;
R7.4 emerges as the most physically plausible.

**R7.1: λ_unlock convention.** ~~~~ **CLOSED — not the source.~~~~
A previous comment in `framework_constants.py` claimed
`λ_unlock(K=1) = 2G/π ≈ 0.583`, suggesting an alternative
convention. The audit showed this comment was a derivation error;
the actual closed form is

    λ_unlock(K=1) = (4G − π ln 2)/π ≈ 0.473096

which matches numerical integration to 9 digits and matches the
existing `LAMBDA_UNLOCK = 0.473`. Comment fixed in this commit.
**The framework value was correct; only the comment was wrong.**
R7.1 is not the source of the 11%.

**R7.2: Pivot-level fine adjustment.** Eq. (5.1) is quadratic in
q_pivot. The exact-match q_eff is `q_eff ≈ 11525`, corresponding to
0.107 levels above F_21 (= 2.94 e-folds smaller scale). This
corresponds to a corrected `N_efolds ≈ 58.4`, vs the framework's
prediction of 61.3. The 11% A_s residual is consistent with the
framework's N_efolds being off by ~3 e-folds. **Plausible but not
yet derived; promoted to R7.4 below.**

**R7.3: Higher-order expansion of cos.** The linearization (1.2)
truncated cos at O(δθ²). Including O(δθ⁴) terms gives self-
interactions that renormalize the variance. At K = 1 these may
contribute at the ~10% level. Not performed here.

**R7.4 (NEW): N_efolds shift.** The framework predicts N_efolds =
√5/rate = 61.3 (alphabet_depth21.py). Standard inflation typically
puts the CMB pivot at N* ≈ 50–60 e-folds before end of inflation,
depending on energy scale and reheating. If the framework's pivot
identification at F_21 corresponds to N* ≈ 61.3 but the actual CMB
pivot is at N* ≈ 58, the q_eff shifts and A_s closes to ~1%.
This converts the A_s 11% residual into a different question:
**is the framework's N_efolds prediction off by ~3 e-folds?**

**Suggestive algebraic match: 19/21.** The residual ratio
A_s_obs/A_s_pred = 0.9020 lands within 0.3% of 19/21 = 0.9048.
Both are framework integers:

- 19 = `|F_7|` (Farey count beyond the pivot bracket;
  also OMEGA partition denominator)
- 21 = F_8 (Fibonacci; the local-pivot denominator at convergent
  13/21 per k_omega_mapping.py n=5 reading)

Equivalently: 1 − 2/21 = 19/21, where 2 = q_2. **No derivation;
flagged as numerological coincidence pending structural argument.**
If `(19/21)` enters the formula as a sector-loss factor, A_s closes
to 0.3%, well within Planck 2018 1σ.

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
