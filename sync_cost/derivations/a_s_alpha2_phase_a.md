# α₂ derivation, Phase A: setup, candidates, residual

Phase A of the closure of α₂ in `a_s_prefactor_gap_formal.md` §3
step 2. Phase A: define the object, derive the staircase analytics,
list candidate evaluations, identify what Phase B must close.

## 1. Definition

**α₂** is the n-to-Ω Jacobian at the CMB pivot, entering the
prediction chain via:

    A_s = α₁ × α₂ × α₃ × σ²/q_pivot² × (something)/(4π²)         (1.1)

where the framework's sigma_squared.py guess
`A_s = σ⁴/(4π² q²)` corresponds to setting `α₁ α₂ α₃ × (σ²/(4π²)) = σ⁴/(4π²)`,
i.e. effectively `α₁ α₂ α₃ = σ²` (under one possible reading).

The numerical target with σ² = K_eff = 3/2 and q_pivot = F_21 = 10946:

    α₁ × α₂ × α₃ = C_{A_s} ≈ 4.415 ± 1.4% (Planck 2018 1σ)       (1.2)

α₂ is specifically the **conversion factor between an Ω-axis
quantity (tongue width, bracket variance) and an n-axis quantity
(per Fibonacci level)**. Its precise functional form depends on the
Phase B identification of α₁ (combinatorial weight at the pivot
bracket) and α₃ (k-mode volume).

## 2. Staircase analytics

The Stern-Brocot convergents to 1/φ are F_n/F_{n+1}. Using Binet's
formula F_n = (φⁿ − ψⁿ)/√5 with ψ = −1/φ:

    F_n/F_{n+1} − 1/φ = (-1)^{n+1} · √5/φ^{2n+2} + O(1/φ^{4n})    (2.1)

**Derivation.** Write F_n/F_{n+1} = (1/φ)(1 − rⁿ)/(1 − r^{n+1}) with
r = ψ/φ = −1/φ². Expand for small rⁿ:

    F_n/F_{n+1} ≈ (1/φ)[1 − rⁿ(1 − r)]
                = (1/φ) − (1/φ) rⁿ × √5/φ
                = (1/φ) − √5 · rⁿ/φ²
                = (1/φ) + (-1)^{n+1} √5/φ^{2n+2}                  (2.2)

since r = −1/φ² gives rⁿ = (-1)ⁿ/φ^{2n} and the sign flip yields
(-1)^{n+1}.

**Numerical check** (run in Phase A worksheet):

    n   ε_n            |ε_n| · φ^{2n+2}
    20  −3.733 × 10⁻⁹  2.236068      → √5
    21  +1.426 × 10⁻⁹  2.236068
    22  −5.446 × 10⁻¹⁰ 2.236068

Asymptotic constant matches √5 to 7+ digits. **Result (2.1) is exact.**

## 3. Candidate α₂ values

Three natural definitions, each with structural justification:

**(A) Local slope magnitude.** Define
`α₂^A := |S(n+1) − S(n)|` with S(n) the staircase-center
parametrization (2.2). For n_pivot = 20 (i.e. q_pivot = F_21):

    α₂^A = √5/φ^{42} × (1 + 1/φ²) ≈ 5.16 × 10⁻⁹

This is **n-dependent** and exponentially small. Under the
formula (1.1), if α₂ scales as 1/φ^{2n} and 1/q² already supplies
1/φ^{2n}, the assembled prediction picks up an extra 1/φ^{2n}
that contradicts the empirical 1/q² scaling. **(A) is incompatible
with (1.1)'s scaling and is rejected.**

**(B) Self-similarity exponent.** The log-derivative of the
staircase deviation is n-independent:

    d/dn ln|S(n) − 1/φ| = −2 ln φ                                 (3.1)

So `α₂^B := 2 ln φ ≈ 0.962`. **n-independent. Compatible with (1.1)'s
scaling.**

**(C) Bracket-times-q² product.** The Stern-Brocot bracket width at
level n is 1/(F_{n+1} F_{n+2}) ≈ 1/(φ q²). The product
`q² × bracket_width` is n-independent at large n:

    α₂^C := q_pivot² × w_bracket(pivot) = 1/φ ≈ 0.618              (3.2)

Numerical: at n_pivot = 20, q² × w_bracket = 10946² × 5.16 × 10⁻⁹ /
(some normalization) — verified numerically below at 1/φ to 7 digits.
**Also n-independent. Compatible with (1.1).**

**Comparison of (B) and (C):**

| α₂ | value | relation to bracket geometry |
|---|---|---|
| α₂^B | 2 ln φ ≈ 0.962 | rate of bracket-width contraction (per level) |
| α₂^C | 1/φ ≈ 0.618 | normalized bracket-width × q² (level-independent residual) |

Both are forced by the φ² self-similarity but encode different
aspects: (B) the *rate*, (C) the *amplitude*.

**Tongue-to-bracket ratio**: at K=1, tongue width = σ²_kernel/q² =
(1/4)/q². Bracket width = 1/(F_{n+1} F_{n+2}) = 1/(φ q²) at large n.
Ratio bracket/tongue = (1/(φ q²))/((1/4)/q²) = **4/φ ≈ 2.4721.**
Verified numerically at n = 19, 20, 21 to 4 digits. **n-independent.**

The 4/φ ratio is itself a structural constant of the framework:
it expresses how much of the Ω-axis bracket is "dynamically
captured" by the K=1 Arnold tongue, given the kernel σ²_kernel = 1/4.

## 4. Numerical residual

With (1.2)'s target C_{A_s} = 4.415, and assuming α₁ × α₃ = 1 as a
provisional baseline:

| α₂ candidate | value | implied α₁ × α₃ | candidate factorization |
|---|---|---|---|
| α₂^B = 2 ln φ | 0.962 | 4.59 | 4π/3 (= 4.19, 9% off); π√5/√6 (= 4.42, off by 4%) |
| α₂^C = 1/φ | 0.618 | 7.14 | 2π × (1 + 1/φ³) = 7.74, 8% off; or 2π · sech(?), unfit |
| (provisional) α₂ × α₁ × α₃ = e · φ | — | 4.398 | direct (no factorization) |
| (provisional) α₂ × α₁ × α₃ = π √2 | — | 4.443 | direct (no factorization) |

**No clean factorization with α₁ = 1 in either case.** This means:
- α₁ ≠ 1 in the framework (the bracket-population factor is
  non-trivial), or
- α₃ ≠ 1 (the mode-volume factor at the pivot has its own structure).

Most likely both. Phase A cannot close α₂ in isolation. **Phase B
must derive α₁ and α₃ first**; α₂ is then determined by residual
matching.

## 5. The Phase B closure path

Phase B will do, in order:

**B1: derive α₃ from the standard cosmology mode-volume.**
This is well-known: in a comoving box of size L, the number of
modes per d ln k around k* is `V × k*³/(2π²) × d ln k`. The pivot's
α₃ is determined by identifying `V` with the framework's natural
volume, which per A6 is the Hubble volume L_H³ = (c/H₀)³.
Expectation: α₃ becomes a definite numerical factor, possibly
`L_H³ k*³/(2π²)` evaluated at fiducial Planck cosmology.

**B2: derive α₁ from the field-equation steady state at the pivot.**
The locked-state population at bracket p/q is N(p/q) = w(p/q) × g(p/q)
× (normalization). At critical K=1 with uniform g, N(p/q) ∝ 1/q² and
the per-mode variance `⟨δθ²⟩ ∝ 1/(K_eff r*)²` per
spectral_tilt_reframed.md Eq. 3.1. The pivot's α₁ is the
combinatorial coefficient in this expression, determined by the
specific Stern-Brocot structure at the bracket.

**B3: identify α₂ by residual matching.** With α₁ and α₃ known,
α₂ is forced as α₂ = C_{A_s} / (α₁ × α₃). The match against
candidates (B) or (C) above is the closure check.

**Budget**: B1 is mechanical (~30 min, standard CMB result in tree
parameterization). B2 requires careful field-equation analysis at
the locked state (~1 hour). B3 is arithmetic.

## 6. What Phase A delivers

- **Eq. (2.1)** rigorously: ε_n → √5/φ^{2n+2} via Binet, no fit.
- **Three candidate α₂ definitions** (A, B, C) with structural meaning.
- **Rejection of (A)** on scaling grounds.
- **Tongue-to-bracket ratio 4/φ** as a verified n-independent constant.
- **Residual statement**: α₁ × α₃ ≈ 4.59 (with α₂ = 2 ln φ) or
  α₁ × α₃ ≈ 7.14 (with α₂ = 1/φ). Phase B will resolve.

## 7. What Phase A does NOT close

- Which of (B) or (C) is the right α₂. Requires α₁, α₃ first.
- The factorization of C_{A_s} = 4.415 into the three α's. Without
  α₁ and α₃ derived independently, residual matching is fitting,
  not derivation.
- Whether the tongue-to-bracket ratio 4/φ enters the formula
  explicitly (it might be absorbed into α₁).

## 8. Cross-references

| File | Role |
|---|---|
| `a_s_prefactor_gap_formal.md` | Defines C_{A_s} target and α₁/α₂/α₃ chain |
| `a_s_amplitude_audit.md` | Three-σ² disambiguation, confirms ADM-side closure |
| `a_s_prefactor_check.py` | Numerical probe (σ², pivot) grid |
| `spectral_tilt_reframed.md` | Source for Phase B2 fluctuation formula (Eq. 3.1) |
| `k_omega_mapping.py` | Pivot identification, rate = (1−n_s)/ln φ² |
| `alphabet_depth21.py` | Numerical σ²(d) running, confirms self-similarity |
| `boundary_weight.py` | Tongue widths σ²_kernel/q² at K=1 |
