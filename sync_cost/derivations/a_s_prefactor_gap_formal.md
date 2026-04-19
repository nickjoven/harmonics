# A_s prefactor gap: formal statement

Companion to `a_s_amplitude_audit.md`. The audit doc identifies the
gap as "a missing unit-volume factor." This doc formalizes the gap
as a specific proof obligation: what exactly needs to be derived,
and what constitutes closure.

**Convention.** Throughout: ℓ_P, t_P, M_P from `framework_constants`.
Natural units 8πG = c = ℏ = 1 unless noted. `q_pivot = F_{n+1}` where
`n` is the Fibonacci level of the CMB pivot. `σ²` always refers to
the **kernel normalization** `σ²_kernel = 1/4` per
`continuum_limits.md` §5a, unless explicitly marked `K_eff`.

## 1. Observable

The scalar amplitude A_s is defined by:

    P_R(k) = (2π² / k³) A_s (k/k*)^{n_s - 1}                     (1.1)

where P_R is the comoving curvature-perturbation power spectrum,
k* = 0.05 Mpc⁻¹ is the pivot, and A_s is dimensionless. Planck 2018
measures A_s = (2.10 ± 0.03) × 10⁻⁹.

Equivalently, writing the two-point correlator in k-space:

    ⟨R(k) R*(k')⟩ = (2π)³ δ³(k - k') × (2π²/k³) A_s × (k/k*)^{n_s-1}  (1.2)

The A_s to be predicted is this dimensionless number.

## 2. Framework inputs (axioms for this proof)

The following are taken as established by prior derivations. Each
carries a citation to its closure.

**A1** (ADM-Kuramoto dictionary). The curvature perturbation R is
identified with the Kuramoto phase fluctuation δθ around the locked
mean field: `R(x,t) = δθ(x,t) / (2π)` modulo a gauge choice.
[`continuum_limits.md` Part II]

**A2** (kernel normalization). σ²_kernel = 1/4, per coupling
direction. [`continuum_limits.md` §5a, `adm_prefactor_verification.py`]

**A3** (tongue width at K = 1). At the critical coupling, the
Arnold tongue at bracket p/q has Lebesgue width
`w(p/q) = σ²_kernel / q²` on the Ω-axis. [`boundary_weight.py`,
`field_equation_cmb.py`]

**A4** (Fibonacci pivot). The CMB pivot k* = 0.05 Mpc⁻¹ sits at
Fibonacci level `n_pivot` with `q_pivot = F_{n_pivot + 1}`. The
linear mapping `n(k) = n_pivot + rate × ln(k/k*)` with
`rate = (1 - n_s) / (-ln φ²) ≈ 0.0365 levels per e-fold`.
[`k_omega_mapping.py`]

**A5** (tilt from self-similarity). `n_s - 1 = -rate × ln(φ²)` is
the staircase self-similarity at the pivot bracket. Derivation of
the shape requires no additional input beyond A3–A4.
[`spectral_tilt_reframed.md`, `alphabet_depth21.py`]

**A6** (Hubble-scale coupling). `K_eff = 4πG ρ_crit L_H² / c² = 3/2`
in natural units. `K_eff / σ²_kernel = 6 = 2d` counts the
coordination number for `d = 3`. [`sigma_squared.py`,
`adm_prefactor_verification.py`]

## 3. The prediction chain

The framework-side calculation proceeds in four steps.

**Step 1: Fluctuation variance at bracket p/q.**

In the locked state, the variance of δθ at bracket p/q scales with
the bracket's weight. Per `spectral_tilt_reframed.md`:

    ⟨δθ²⟩(p/q) ∝ w(p/q) / (K_eff × r*)²                         (3.1)

with r* the locked-state order parameter. The proportionality
constant at this step is a combinatorial factor from the
distribution `g(ω)` of locked oscillators at bracket p/q. **This
constant has not been computed in the framework.** Call it `α₁`.

**Step 2: Bracket-to-k Jacobian.**

Converting from bracket (Ω-axis) to k (physical wavenumber) at the
pivot requires the Jacobian `|dΩ/dk|_{k=k*}`. Per A4, at the pivot:

    ω(n) = 1/φ + O(φ^{-2n})    (staircase parametrization)       (3.2)
    k(n) = k* × exp((n - n_pivot) / rate)                        (3.3)

The Jacobian `|dn/d ln k| = rate = (1 - n_s) / ln(φ²)`. **The
n-to-Ω Jacobian** `|dΩ/dn|` **at the pivot has not been derived
from first principles** — `k_omega_mapping.py` writes `Ω(n)` as the
staircase-center formula but does not compute its derivative at
the pivot bracket as a definite number. Call this Jacobian `α₂`.

**Step 3: δθ to R conversion.**

Per A1, `R = δθ / (2π)` up to the gauge choice. So
`⟨R²⟩ = ⟨δθ²⟩ / (4π²)`. The (4π²)⁻¹ factor is the origin of the
4π² in `sigma_squared.py`'s formula. **No ambiguity here.**

**Step 4: Correlator to A_s.**

Per (1.1), `A_s = k*³ P_R(k*) / (2π²)`. The conversion from real-
space variance ⟨R²⟩ to the k-space power P_R(k*) introduces a
mode-density factor:

    P_R(k*) = ⟨R²⟩ × V_pivot                                     (3.4)

where `V_pivot` is the comoving volume per k-mode at the pivot.
**This volume is not computed in the framework.** Call it `α₃`.

**Assembled prediction.**

    A_s = α₁ × α₂ × α₃ × σ²_kernel × (K_eff r*)⁻² × q_pivot⁻² / (4π²)   (3.5)

The existing sigma_squared.py formula `A_s = σ⁴ / (4π² q²)` is a
particular closed-form guess: it effectively sets
`α₁ α₂ α₃ (K_eff r*)⁻² = σ²_kernel × K_eff²` (the σ⁴ comes from
σ²_kernel × K_eff², which is dimensionally consistent only if
α₁ α₂ α₃ has specific structure).

## 4. The precise open quantity

Define the **A_s closure coefficient** by:

    C_{A_s} := A_s_observed × 4π² × q_pivot² / (σ²)²            (4.1)

The (σ²)² in the denominator follows from the sigma_squared.py
formula `A_s_framework = (σ²)² / (4π² q²)`; in this convention σ²
appears quadratically, so σ⁴ = (σ²)² where σ² is the scalar
normalization carried through from A2/A6. Using
`σ² = K_eff = 3/2`, `q_pivot = F_21 = 10946`, and the Planck
central value A_s = 2.10 × 10⁻⁹:

    C_{A_s} = 2.10×10⁻⁹ × 4π² × 10946² / (3/2)²
            = 2.10×10⁻⁹ × 39.478 × 1.198×10⁸ / 2.25
            ≈ 4.415

Using `σ² = σ²_kernel = 1/4` (per A2):

    C_{A_s} = 2.10×10⁻⁹ × 4π² × 10946² / (1/4)²
            ≈ 158.93

Sensitivity to the 1-σ Planck error (± 0.03 × 10⁻⁹):
C_{A_s} ∈ [4.352, 4.478] at σ² = 3/2 (± 1.4%).

**Open problem.** Compute C_{A_s} as a closed-form product of
α₁ × α₂ × α₃ with each factor derived from the framework axioms
A1–A6, and show that the resulting closed form matches C_{A_s}
measured above to at least 1% relative deviation.

## 5. Closure criterion

A derivation counts as closure of A_s if and only if:

**(C1)** Each of α₁, α₂, α₃ is expressed in closed form using only
the framework axioms A1–A6 plus standard mathematical operations
(π, e, integers, φ, small rationals).

**(C2)** The product `α₁ × α₂ × α₃` matches the observed
`C_{A_s}` within 1% relative deviation when σ² = K_eff = 3/2 is
used (or within the equivalent tolerance when a different σ²
identification is justified by the derivation).

**(C3)** The derivation does not introduce a new free parameter.
Any new quantity (e.g., a specific pivot level shift) must be
itself derived from prior inputs, not chosen to match observation.

**(C4)** The q_pivot identification (`F_21`) is either taken from A4
or replaced by a derived alternative with stated derivation.

Partial credit (status labels for the audit doc):

- If C1 holds but C2 fails by >1%: **structural sketch, not C-numerical**.
- If C2 holds but C1 introduces a fudge factor: **hidden free parameter**.
- If C3 fails via introduction of a fit: **not C-numerical**.

## 6. Three candidate α factors (for orientation, not closure)

Pattern-matching against CMB literature, plausible forms:

**α₁ (combinatorial)**: for a Farey partition with Σ w(p/q) = 1,
the fraction of phase space at bracket p/q is w(p/q) itself, so
`α₁ ∼ 1`. Weaker variants include the number of Stern-Brocot
children under a given bracket.

**α₂ (n-to-Ω Jacobian)**: at the staircase self-similar point,
`|dΩ/dn| = Ω_pivot × ln(φ²)`. At the golden-ratio pivot,
`Ω_pivot = 1/φ`, giving `α₂ = ln(φ²)/φ ≈ 0.595`.

**α₃ (mode volume)**: the standard cosmology expression is
`V_pivot = 2π²/k*³` per (1.1)–(3.4). The framework-side analog in
the bracket parametrization would be `2π²/Ω_pivot³`, giving
`α₃ = 2π² × φ³ ≈ 83.6`.

Multiplying: `α₁ × α₂ × α₃ ∼ 1 × 0.595 × 83.6 ≈ 49.7`. This is
in the right order of magnitude as `C_{A_s} / (4π²) ≈ 2 / (4π²) ≈
0.05` — but the algebraic combination doesn't clean up under the
substitutions. Does not close.

**These are orientation guesses, not derivations.** Closure requires
deriving each α_i from A1–A6 without fit.

## 7. What's already close

The target C_{A_s}(σ² = 3/2) ≈ 4.415 sits near three plausible
closed forms:

| candidate | value | % deviation from 4.415 |
|---|---|---|
| e · φ | 4.3983 | 0.38% |
| π √2 | 4.4429 | 0.64% |
| 4π / 3 | 4.1888 | 5.40% |

**None of these is derived.** Each is pattern-matching against
well-known transcendentals.

- `e · φ` would require a derivation involving both the RG
  e-folding exponent and the golden-ratio pivot; natural if the
  fluctuation integral over the Fibonacci bracket produces an
  exponential tail times φ (the pivot Ω-coordinate).
- `π √2` would require a factor of √2 from a mode-degeneracy
  argument (boson counting, 2 polarizations, etc.) combined
  with the π from solid-angle integration.
- `4π / 3` is the unit-sphere volume; natural if α₃ is the
  full-sphere mode integral. Deviation is outside the Planck
  1-σ band; this form would only close at ~4σ, not adequate.

If closure to `e · φ` were achieved:

    A_s_predicted = e · φ × (σ²)² / (4π² q_pivot²)
                  = e · φ × (3/2)² / (4π² × F_21²)
                  ≈ 2.093 × 10⁻⁹                                (7.1)

vs observed (2.10 ± 0.03) × 10⁻⁹. Residual ≈ 0.3% — **~0.25σ**
under Planck 2018 uncertainty. Closure at `e · φ` would promote
A_s from Tier 2 "partially closed" to Tier 2 "C-numerical at
< 1σ".

If closure to `π √2` were achieved, A_s_predicted ≈ 2.11 × 10⁻⁹,
residual ≈ 0.5%, ~0.4σ.

**Caveat.** Both `e · φ` and `π √2` hit the target within 1%,
but hitting one target with two unrelated forms is a red flag for
numerological coincidence. The difference between them
(|e·φ − π√2| / 4.415 ≈ 1%) is smaller than the framework's
predictive precision on other quantities (e.g. m_τ/m_e at 0.9%,
α_s/α_2 at 3.2%). A genuine derivation should identify **one**
of them unambiguously and show why the other is excluded.

The question `C_{A_s} = ?` is the crispest form of the open gap.

## 8. Related open gaps

The A_s prefactor shares structure with three other Issue #56
items:

- **Tier 3 #12 (fractal dimension of mode-lock boundary)**:
  computing `α₂` likely requires the Hausdorff dimension of the
  critical devil's staircase at 1/φ. Closing #12 could supply `α₂`.
- **Tier 2 #5 (initial conditions)**: the `α₃` mode-volume factor
  is the same question as the Hubble-volume quantization in the
  k→mode-count conversion. Closure of #5 entails A_s closure.
- **Tier 3 #11 (CMB damping tail)**: the off-pivot running is
  controlled by the same Jacobians as A_s. Closing A_s would
  constrain #11.

Any derivation that supplies all three α factors in closed form
closes A_s and at least partial-closes the three above.

## 9. Summary

| Component | Status | Source |
|---|---|---|
| Observable definition | fixed | Eq. (1.1), standard cosmology |
| σ² disambiguation | closed | `a_s_amplitude_audit.md` |
| ADM prefactor side | closed | `continuum_limits.md` §5a |
| Step 1 coefficient α₁ | **open** | §3 step 1 |
| Step 2 Jacobian α₂ | **open** | §3 step 2 |
| Step 4 mode volume α₃ | **open** | §3 step 4 |
| Numerical target | `C_{A_s} ≈ 1.962 ≈ 2` | §4 |
| Closure criterion | C1–C4 | §5 |

The gap is one specific dimensionless constant to compute. The
calculation is well-scoped: four axiomatic inputs (A1–A6), three
closed-form factors (α₁, α₂, α₃), one numerical target (≈ 2 to 2%).
No open-ended search; no freedom to introduce fit parameters.

## Cross-references

| File | Role |
|---|---|
| `a_s_amplitude_audit.md` | Companion status doc; three-σ² vocabulary fix |
| `a_s_prefactor_check.py` | Numerical probe across (σ², pivot) grid |
| `continuum_limits.md` §5a | ADM σ²_kernel = 1/4 closure |
| `spectral_tilt_reframed.md` | Step 1 fluctuation formula (Eq. 3.1 above) |
| `k_omega_mapping.py` | Step 2 Ω-to-k mapping (no Jacobian yet) |
| `sigma_squared.py` | Step 4 asserted formula (no derivation) |
| `alphabet_depth21.py` | σ²(d) running; confirms tilt shape |
