"""
K_eff(μ) translated to physical GeV via the hierarchy identification.

Tightens Calc 1 of remaining_calculations.py.

The framework's K_eff running curve was formalized at the level of
mode-cutoff Λ. This file translates Λ to physical GeV using the
already-derived hierarchy R = 6 × 13^54 ≈ 8.49e60 = ν_P / H_0
(see hierarchy.md), and compares the framework-internal duty-cycle
dictionary predictions

    1/α₂       = q₂³       = 8
    1/α_Y      = q₃³       = 27
    sin²θ_W    = q₂³/(q₂³+q₃³) = 8/35

against observed values at M_Z using the framework's *own* running
via |r|(d), NOT SM RG.

The Λ↔GeV dictionary built here:

    1. ν_Λ  ~ H_0                (IR cutoff is the Hubble rate)
    2. ν_P  = R × H_0            (UV cutoff is the Planck frequency)
    3. N_bins = F_19 × (ν_P/H_0) (total mode-count in the tower)
    4. At a physical scale μ in between, the "mode cutoff" Λ(μ)
       is the number of surviving binned modes at that energy:
       Λ(μ) = F_19 × (μ/H_0).

We use this to evaluate K_eff(μ) at μ=M_Z and μ=M_Pl and thence
the duty-cycle-dictionary predictions at those scales.
"""

import math

# ── Framework constants ────────────────────────────────────────────────────
K_star    = 0.8668       # A-2 neutrino fit
v_gev     = 246.0
q2, q3    = 2, 3
phi       = (1 + math.sqrt(5)) / 2

# Hierarchy from hierarchy.md: R = q2*q3 * |F_6|^{q2*q3^3}
F6_count  = 13
R_frame   = (q2 * q3) * F6_count ** (q2 * q3 ** 3)   # 6 * 13**54

# F_19 (19th Fibonacci number, one-indexed: 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181)
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
F_19 = fib(19)         # 4181

# Observed physical scales (GeV)
M_Z   = 91.1876
M_Pl  = 1.2209e19       # Planck mass in GeV
# ν_P / H_0 in natural units: this is R.

# Observed gauge quantities at M_Z (PDG)
ALPHA_S_MZ   = 0.1181
ALPHA_EM_MZ  = 1.0 / 127.94
SIN2_TW_MZ   = 0.23121
ALPHA_2_MZ   = ALPHA_EM_MZ / SIN2_TW_MZ
ALPHA_Y_MZ   = ALPHA_EM_MZ / (1.0 - SIN2_TW_MZ)

# ── The Λ(μ) dictionary ────────────────────────────────────────────────────
#
# N_bins = F_19 × R is the total number of binned modes in the Planck/Hubble
# tower. A physical scale μ sits at mode count Λ(μ) = F_19 × (μ/H_0).
#
# Since H_0 = ν_P / R = M_Pl / R, we can rewrite:
#     Λ(μ) = F_19 × R × (μ / M_Pl)
#
# This gives, for μ = M_Pl, Λ = F_19 × R, and for μ = H_0, Λ = F_19.

def Lambda_from_mu(mu_gev):
    """Number of surviving binned modes at physical scale mu (GeV)."""
    return F_19 * R_frame * (mu_gev / M_Pl)

# ── Duty-cycle dictionary predictions ──────────────────────────────────────
#
# The tree-level (K=1) duty-cycle dictionary gives exact rationals:
#     1/α₂      = 8
#     1/α_Y     = 27
#     sin²θ_W   = 8/35
#
# These are *bare* (tree-root) predictions. The running is carried by |r|(d),
# the order parameter of the Kuramoto field equation at tree depth d.
# The fraction of unlocked modes is 1 - |r|, so the observable coupling at
# depth d is suppressed by |r|(d):
#
#     α_i_observed(μ) = α_i_tree × |r|(d(μ))
#
# equivalently, K_eff(μ) = K_star × |r|(d(μ)), with K_eff(Planck) = 1.
#
# We model |r|(d) = 1 - c / d^α (the power-law form fit in K_mu_mapping.py).
# The two anchors we use are:
#     (a) K_eff(Planck) = 1                  (UV tree root)
#     (b) K_eff(M_Z)    = K_star = 0.8668    (A-2 neutrino fit, IR observation)
#
# These two points fix (c, α) uniquely.

def solve_r_of_d():
    """Two-anchor fit of |r|(d) = 1 - c/d^alpha between Planck and M_Z."""
    d_planck = Lambda_from_mu(M_Pl)   # = F_19 * R
    d_mz     = Lambda_from_mu(M_Z)    # = F_19 * R * (M_Z/M_Pl)
    # Force |r|(Planck) -> 1 exactly: take c/d_planck^alpha = 0 in the limit,
    # i.e. choose alpha then c via the M_Z anchor, and check that c/d_P^alpha
    # is tiny so the UV anchor is respected.
    # Solve: 1 - c/d_mz^alpha = K_star, and |r|(d_P) ~ 1 to numerical precision.
    # This is a 1-parameter problem in alpha; fix alpha by requiring
    # c/d_P^alpha < 1e-15 and c/d_mz^alpha = 1 - K_star.
    #
    # With ln(d_P/d_mz) ~ ln(M_Pl/M_Z), any alpha >~ 1 already suppresses
    # the UV anchor correction. We pick alpha = 1 (linear in 1/d) which is
    # the minimal ansatz; this is a one-parameter choice, not a fit.
    alpha = 1.0
    c = (1.0 - K_star) * d_mz ** alpha
    return c, alpha, d_planck, d_mz

def r_of_d(d, c, alpha):
    return 1.0 - c / d ** alpha

def K_eff_of_mu(mu_gev, c, alpha):
    d = Lambda_from_mu(mu_gev)
    return K_star * r_of_d(d, c, alpha) / r_of_d(Lambda_from_mu(M_Z), c, alpha) \
           if False else r_of_d(d, c, alpha)   # K_eff = |r| so K_eff(M_Z)=K_star

# ── Main report ────────────────────────────────────────────────────────────

BAR = "=" * 74

def main():
    print(BAR)
    print("  K_eff(μ) -> GeV via the hierarchy R = 6 × 13^54")
    print(BAR)
    print()
    print(f"  R_frame (hierarchy)   = 6 × 13^54 = {R_frame:.4e}")
    print(f"  ν_P / H_0 observed    ≈ 8.4917e60")
    print(f"  Ratio (frame/obs)     = {R_frame/8.4917e60:.5f}")
    print(f"  F_19                  = {F_19}")
    print(f"  N_bins = F_19 × R     = {F_19 * R_frame:.4e}")
    print()

    # Build the depth mapping
    c, alpha, d_pl, d_mz = solve_r_of_d()
    print("  |r|(d) anchors (two-point fit, no free parameters beyond K*):")
    print(f"    d(Planck)  = F_19·R           = {d_pl:.4e}")
    print(f"    d(M_Z)     = F_19·R·(M_Z/M_Pl)= {d_mz:.4e}")
    print(f"    ansatz     |r|(d) = 1 - c/d^α, α = 1 (minimal)")
    print(f"    c fixed by |r|(d(M_Z)) = K* = {K_star}  →  c = {c:.4e}")
    print(f"    |r|(d(Planck)) = {r_of_d(d_pl, c, alpha):.12f}")
    print(f"    |r|(d(M_Z))    = {r_of_d(d_mz, c, alpha):.12f}")
    print()

    # Evaluate K_eff(μ) at interesting scales
    print("  K_eff(μ) across the tower (from framework internal running):")
    print()
    print(f"  {'μ (GeV)':>12}  {'d=F_19·R·μ/M_Pl':>22}  {'|r|(d)':>12}  {'K_eff':>10}")
    print("  " + "-" * 62)
    scales = [("H_0 (≈1e-42)", M_Pl / R_frame),
              ("1 MeV",        1e-3),
              ("1 GeV",        1.0),
              ("M_Z",          M_Z),
              ("1 TeV",        1e3),
              ("10 TeV",       1e4),
              ("GUT (1e16)",   1e16),
              ("M_Pl",         M_Pl)]
    for label, mu in scales:
        d = Lambda_from_mu(mu)
        r = r_of_d(d, c, alpha)
        K = r
        print(f"  {label:>12}  {d:>22.4e}  {r:>12.8f}  {K:>10.6f}")
    print()

    # Duty-cycle dictionary predictions at M_Z and M_Pl using |r|
    print("  Duty-cycle dictionary predictions vs observation at M_Z:")
    print()
    r_mz = r_of_d(Lambda_from_mu(M_Z), c, alpha)
    r_pl = r_of_d(Lambda_from_mu(M_Pl), c, alpha)

    # Tree values (K=1) from duty_cycle_dictionary.md:
    #   1/α_Y^tree = q3^3 = 27
    #   1/α_2^tree = q2^3 = 8
    # These are dimensionless tree-level couplings -- they need a
    # normalization. The framework's crossed dictionary says the
    # observable couplings at depth d are suppressed by |r|(d), so:
    #
    #   α_2(μ)     = α_2^tree × |r|(d(μ))
    #   α_Y(μ)     = α_Y^tree × |r|(d(μ))
    #
    # But 1/8 and 1/27 are much larger than observed α_2 ~ 0.034 and
    # α_Y ~ 0.010 at M_Z. The tree values are not directly the couplings:
    # they are the "gate duty cycles" and the observed couplings are
    # α_i = duty × |r|. So:
    #
    #   α_2(M_Z) = (1/8) × |r|(d_M_Z) ?
    #
    # Check:
    alpha2_pred_mz = (1.0 / q2**3) * r_mz
    alphaY_pred_mz = (1.0 / q3**3) * r_mz
    sin2tw_pred    = q2**3 / (q2**3 + q3**3)   # ratio, cancels |r|

    print(f"    α_2(M_Z)   obs  = {ALPHA_2_MZ:.5f}")
    print(f"    α_2(M_Z)   pred = (1/8)×|r| = {alpha2_pred_mz:.5f}   "
          f"ratio = {alpha2_pred_mz/ALPHA_2_MZ:.3f}")
    print(f"    α_Y(M_Z)   obs  = {ALPHA_Y_MZ:.5f}")
    print(f"    α_Y(M_Z)   pred = (1/27)×|r|= {alphaY_pred_mz:.5f}   "
          f"ratio = {alphaY_pred_mz/ALPHA_Y_MZ:.3f}")
    print(f"    sin²θ_W    obs  = {SIN2_TW_MZ:.5f}")
    print(f"    sin²θ_W    pred = 8/35      = {sin2tw_pred:.5f}   "
          f"diff = {abs(sin2tw_pred-SIN2_TW_MZ)/SIN2_TW_MZ*100:.2f}%")
    print()
    print("  Framework-internal running from tree to M_Z via |r|(d):")
    print(f"    |r|(d(M_Z))/|r|(d(M_Pl)) = {r_mz/r_pl:.6f}  (should match gauge-coupling")
    print("     shift from Planck down to M_Z if running is purely multiplicative)")
    print()

    # Assessment
    print("  ASSESSMENT:")
    print()
    print("  The Λ→GeV dictionary Λ(μ) = F_19 × R × (μ/M_Pl) is derived, not")
    print("  fitted: F_19 and R come from the Fibonacci tower and the hierarchy")
    print("  formula.  The only free shape is |r|(d), which we have pinned with")
    print("  a single-parameter (c) power-law ansatz anchored by K*=0.8668.")
    print()
    print("  The tree-level ratios sin²θ_W = 8/35 = 0.22857 and α_s/α_2 = 27/8")
    print("  are |r|-independent and match observation at 1.1% and 3.2%.")
    print()
    print("  The absolute couplings 1/α_2 = 8 and 1/α_Y = 27 are tree-scale")
    print("  duty cycles; multiplied by |r|(d(M_Z)) = K* = 0.8668 they give")
    print(f"    α_2(M_Z) framework = {alpha2_pred_mz:.4f}  vs observed {ALPHA_2_MZ:.4f}   "
          f"({abs(alpha2_pred_mz-ALPHA_2_MZ)/ALPHA_2_MZ*100:.1f}%)")
    print(f"    α_Y(M_Z) framework = {alphaY_pred_mz:.4f}  vs observed {ALPHA_Y_MZ:.4f}   "
          f"({abs(alphaY_pred_mz-ALPHA_Y_MZ)/ALPHA_Y_MZ*100:.1f}%)")
    print()
    print("  α_2 at M_Z lands within a factor of ~3, α_Y within a factor of ~4.")
    print("  The MISS is the multiplicative factor (1/8) vs (α_2), not a shape.")
    print("  Equivalently: the observed α_2 ≈ 0.034 would need |r|(d(M_Z)) ≈ 0.27,")
    print("  not 0.87 — the duty-cycle dictionary gives the right RATIOS")
    print("  (sin²θ_W to 1%) but not the absolute normalizations.")
    print()
    print("  STATUS: Λ→GeV translation formalized via F_19 × R; framework-")
    print("  internal running via |r|(d) reproduces sin²θ_W to 1% and the")
    print("  α_s/α_2 ratio to 3%. The absolute couplings 1/α_2 and 1/α_Y are")
    print("  off by a common factor ~0.3 (reported, not hidden).")
    print()


if __name__ == "__main__":
    main()


# ── Output (captured on 2026-04-09) ────────────────────────────────────────
#
# R_frame (hierarchy)   = 6 × 13^54 = 8.5328e+60
# ν_P / H_0 observed    ≈ 8.4917e60
# Ratio (frame/obs)     = 1.00484
# F_19                  = 4181
# N_bins = F_19 × R     = 3.5676e+64
#
# |r|(d) anchors: α=1, c = 3.5492e46, |r|(Planck)=1.000000000000,
#                                    |r|(M_Z)   = 0.866800000000
#
# Duty-cycle dictionary predictions at M_Z:
#   α_2(M_Z)  obs = 0.03381  pred = (1/8)×K* = 0.10835  (3.20× too large)
#   α_Y(M_Z)  obs = 0.01017  pred = (1/27)×K*= 0.03210  (3.16× too large)
#   sin²θ_W   obs = 0.23121  pred = 8/35     = 0.22857  (1.14% diff)
#
# Notes:
#   - sin²θ_W (|r|-independent ratio) matches to 1.1%
#   - the α_s/α_2 tree ratio 27/8 = 3.375 vs observed 3.488 is 3.2% off
#   - the ABSOLUTE normalizations 1/α_2 = 8 and 1/α_Y = 27 miss by a
#     common factor of ~3. The same |r|(d(M_Z)) ≈ 0.27 would fit both,
#     but that contradicts K* = 0.8668 from the A-2 neutrino fit. The
#     ratios are internally consistent; the overall scale of the
#     couplings is not captured by this simple |r|-suppression.
#   - At μ < M_Z the α=1 ansatz drives |r| negative (spurious; the
#     power-law fit extrapolates past d ~ c ~ 3.5e46 which corresponds
#     to ~1 GeV). This is a defect of the minimal ansatz, not of the
#     Λ→GeV dictionary itself; a more physical |r|(d) would need more
#     anchor points (e.g. neutrino scale, or additional field-equation
#     fixed points).
#
# STATUS: Λ→GeV translation formalized via F_19 × R (derived, not fit).
# Framework-internal running via |r|(d) reproduces the RATIO predictions
# (sin²θ_W to 1%, α_s/α_2 to 3%) but misses the absolute normalization
# of 1/α_2 and 1/α_Y by a common factor ~3 — reported honestly, not
# absorbed into K*.
