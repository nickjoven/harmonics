"""
r_residual_audit.py

Audit of the "0.48% R residual" claim in hierarchy_gaussian_lattice.md.

Observation: the same doc quotes TWO different values for the
observed R = L_H / ell_P:

  Line 15:   R_obs ≈ 8.49×10^60   →   residual 0.48%   (from t_H/t_P)
  Line 125:  R_obs ≈ 7.14×10^60   →   residual ~19%    (unclear source)

These differ by ~19%. Only one can be right. This script verifies
which against current cosmological constants.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import C_LIGHT, G_NEWTON, H_0_SI, HBAR

# Planck 2018 cosmological constants (consensus values; framework_constants)
H_0 = H_0_SI                      # 67.4 km/s/Mpc in s^-1  ≈ 2.184e-18
c = C_LIGHT                       # m/s
G = G_NEWTON                      # m^3 kg^-1 s^-2
hbar = HBAR                       # J·s
Omega_Lambda = 0.6847             # Planck 2018

# Planck-scale quantities
ell_P = math.sqrt(hbar * G / c**3)
t_P = ell_P / c
m_P = math.sqrt(hbar * c / G)

# Hubble-scale quantities
t_H = 1.0 / H_0
L_H_Hubble = c / H_0

# Cosmological constant
Lambda = 3 * Omega_Lambda * H_0**2 / c**2
L_H_deSitter = math.sqrt(3 / Lambda)  # = c/(H_0 sqrt(Omega_Lambda))

# Framework prediction
R_pred = 6 * 13**54

print("=" * 72)
print("  R residual audit")
print("=" * 72)
print()
print(f"  H_0              = {H_0:.4e} s^-1  (67.4 km/s/Mpc)")
print(f"  t_H  = 1/H_0     = {t_H:.4e} s")
print(f"  L_H  = c/H_0     = {L_H_Hubble:.4e} m  (Hubble radius)")
print(f"  L_H' = sqrt(3/Lambda) = {L_H_deSitter:.4e} m  (de Sitter horizon)")
print()
print(f"  ell_P            = {ell_P:.4e} m")
print(f"  t_P              = {t_P:.4e} s")
print()

# Observed R candidates
R_tH_tP = t_H / t_P
R_LH_ellP = L_H_Hubble / ell_P
R_dS_ellP = L_H_deSitter / ell_P

print("  Candidate R_obs values:")
print(f"    t_H / t_P                = {R_tH_tP:.3e}")
print(f"    (c/H_0) / ell_P          = {R_LH_ellP:.3e}")
print(f"    sqrt(3/Lambda) / ell_P   = {R_dS_ellP:.3e}")
print()
print(f"  Framework prediction:")
print(f"    R_pred = 6 · 13^54        = {R_pred:.3e}")
print()

# Residuals
print("  Residuals (|R_pred - R_obs| / R_obs):")
print(f"    vs t_H/t_P               = {abs(R_pred - R_tH_tP)/R_tH_tP * 100:.2f}%")
print(f"    vs (c/H_0)/ell_P         = {abs(R_pred - R_LH_ellP)/R_LH_ellP * 100:.2f}%")
print(f"    vs sqrt(3/Lambda)/ell_P  = {abs(R_pred - R_dS_ellP)/R_dS_ellP * 100:.2f}%")
print()
print("-" * 72)
print("  Doc line 15 quotes R_obs = 8.49×10^60 → 0.48% residual.")
print("  Doc line 125 quotes R_obs = 7.14×10^60 → ~19% residual.")
print()
print(f"  Actual computed t_H / t_P  = {R_tH_tP:.3e}")
print(f"  Line-15 value (8.49e60):   {'MATCHES' if abs(R_tH_tP - 8.49e60)/8.49e60 < 0.01 else 'MISMATCH'}")
print(f"  Line-125 value (7.14e60):  {'MATCHES' if abs(R_tH_tP - 7.14e60)/7.14e60 < 0.01 else 'MISMATCH -- STALE/WRONG'}")
print()

# Where might 7.14e60 come from?
print("-" * 72)
print("  Tracing line 125's 7.14e60 (diagnostic):")
ratio = R_tH_tP / 7.14e60
print(f"    (current t_H/t_P) / 7.14e60 = {ratio:.3f}")
print(f"    ratio ≈ 1.19 suggests: possibly stale value from earlier")
print(f"    cosmology (higher H_0 ~ 73 km/s/Mpc or similar) or a")
print(f"    unit/convention mismatch. Not reproducible from current")
print(f"    Planck 2018 + standard Planck units.")
print()

print("=" * 72)
print("  VERDICT")
print("=" * 72)
print(f"""
  The "0.48% residual" at line 15 is CORRECT:
      R_pred = 6·13^54     = {R_pred:.3e}
      R_obs  = t_H / t_P   = {R_tH_tP:.3e}
      residual             = {abs(R_pred - R_tH_tP)/R_tH_tP * 100:.2f}%

  The "~19% error" / "7.14×10^60" statement at line 125 is STALE
  or erroneous.  The correct current value is 8.49×10^60
  (residual 0.48%), consistent with line 15.

  Recommended edit to hierarchy_gaussian_lattice.md line 124-127:

    OLD:
      "R = 6 × 13^54 ≈ 8.53 × 10^60 vs observed ≈ 7.14 × 10^60.
       The ~19% error in ℓ_P (from the square root) may indicate
       a sub-leading correction or a mismatch in the identification
       L_H = √(3/Λ)."

    NEW:
      "R = 6 × 13^54 ≈ 8.53 × 10^60 vs observed t_H/t_P = c/(H_0 ell_P)
       ≈ 8.49 × 10^60 (0.48% residual, consistent with line 15).
       The de Sitter identification L_H = √(3/Λ) gives a larger value
       ~1.02 × 10^61 (20% over), which may indicate the framework's
       R matches the Hubble-radius identification, not the de Sitter
       horizon one."

  Issue #56 item 13 "the 0.48% residual in R" is accurate; no
  update needed there.
""")
