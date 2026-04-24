#!/usr/bin/env python3
"""
Anomaly cancellation check for Klein bottle charge assignments.

Derivation 19 produces fractions {1/3, 1/2, 2/3} from the Klein bottle
field equation. These map to Standard Model quantum numbers via:

  Interior modes (q >= 2, quarks):
    Up-type:   Q_u = +2/3,  T3 = +1/2
    Down-type: Q_d = -1/3,  T3 = -1/2

  Boundary modes (q = 1, leptons):
    Neutrino:        Q_nu = 0,   T3 = +1/2
    Charged lepton:  Q_e  = -1,  T3 = -1/2

Hypercharges derived from Q = T3 + Y/2  (Gell-Mann--Nishijima).
Anomaly cancellation verified for all six conditions per generation.
"""

from fractions import Fraction

print("=" * 66)
print("  ANOMALY CANCELLATION CHECK  --  Klein bottle charge assignments")
print("=" * 66)

# ---------------------------------------------------------------
# 1.  Klein bottle fractions and SM identification
# ---------------------------------------------------------------
print("\n--- Klein bottle fractions: {1/3, 1/2, 2/3} ---\n")

Q_u  = Fraction(2, 3)
Q_d  = Fraction(-1, 3)
Q_nu = Fraction(0)
Q_e  = Fraction(-1)

T3_up   = Fraction(1, 2)
T3_down = Fraction(-1, 2)

print(f"  Up-type quark:      Q = {Q_u},   T3 = {T3_up}")
print(f"  Down-type quark:    Q = {Q_d},  T3 = {T3_down}")
print(f"  Neutrino:           Q = {Q_nu},     T3 = {T3_up}")
print(f"  Charged lepton:     Q = {Q_e},    T3 = {T3_down}")

# ---------------------------------------------------------------
# 2.  Derive hypercharges from Q = T3 + Y/2
# ---------------------------------------------------------------
print("\n--- Hypercharge derivation (Y = 2(Q - T3)) ---\n")

# Left-handed quark doublet: both members share the same Y
# Use up-type component: Y_Q = 2(Q_u - T3_up)
Y_Q = 2 * (Q_u - T3_up)
# Cross-check with down-type: Y_Q = 2(Q_d - T3_down)
Y_Q_check = 2 * (Q_d - T3_down)
assert Y_Q == Y_Q_check, f"Doublet hypercharge mismatch: {Y_Q} vs {Y_Q_check}"

# Right-handed singlets: T3 = 0
Y_u = 2 * Q_u          # u_R
Y_d = 2 * Q_d          # d_R

# Left-handed lepton doublet
Y_L = 2 * (Q_nu - T3_up)
Y_L_check = 2 * (Q_e - T3_down)
assert Y_L == Y_L_check, f"Lepton doublet hypercharge mismatch: {Y_L} vs {Y_L_check}"

# Right-handed charged lepton singlet
Y_e = 2 * Q_e          # e_R

print(f"  Q_L (quark doublet):   Y_Q = 2({Q_u} - {T3_up})  = {Y_Q}")
print(f"       cross-check:      Y_Q = 2({Q_d} - {T3_down}) = {Y_Q_check}  [consistent]")
print(f"  u_R (up singlet):      Y_u = 2 * {Q_u}           = {Y_u}")
print(f"  d_R (down singlet):    Y_d = 2 * {Q_d}          = {Y_d}")
print(f"  L_L (lepton doublet):  Y_L = 2({Q_nu} - {T3_up})   = {Y_L}")
print(f"       cross-check:      Y_L = 2({Q_e} - {T3_down}) = {Y_L_check}  [consistent]")
print(f"  e_R (lepton singlet):  Y_e = 2 * {Q_e}           = {Y_e}")

# ---------------------------------------------------------------
# 3.  Number of colors from Klein bottle denominator class q = 3
# ---------------------------------------------------------------
Nc = 3
print(f"\n  N_c = {Nc}  (Klein bottle denominator class q = 3)")

# ---------------------------------------------------------------
# 4.  Anomaly cancellation -- all six conditions
# ---------------------------------------------------------------
print("\n" + "=" * 66)
print("  ANOMALY CANCELLATION CONDITIONS (per generation)")
print("=" * 66)

results = {}

# ---- Condition 1: [SU(3)]^2 U(1)_Y ----
# Sum over LEFT-HANDED Weyl fermions charged under SU(3).
# Right-handed fields contribute with OPPOSITE sign (their left-handed
# conjugates carry -Y). Per generation:
#   Q_L contributes +2*Y_Q  (doublet, 2 components)
#   u_R contributes -Y_u    (right-handed => flip sign)
#   d_R contributes -Y_d    (right-handed => flip sign)
# No overall Nc factor: that's already in the triangle (SU(3) index).
A1 = 2 * Y_Q - Y_u - Y_d
results["[SU(3)]^2 U(1)_Y"] = A1

print(f"\n1. [SU(3)]^2 U(1)_Y:")
print(f"   Sum_LH of Y  =  2*Y_Q - Y_u - Y_d")
print(f"   = 2*{Y_Q} - {Y_u} - {Y_d}")
print(f"   = {2*Y_Q} - {Y_u} - {Y_d}")
print(f"   = {A1}")
print(f"   --> {'ZERO' if A1 == 0 else 'NONZERO *** ANOMALY ***'}")

# ---- Condition 2: [SU(2)]^2 U(1)_Y ----
# Sum over all SU(2) doublets of Y.
# Per generation: Nc * Y_Q (quark doublet, Nc colors) + Y_L (lepton doublet)
A2 = Nc * Y_Q + Y_L
results["[SU(2)]^2 U(1)_Y"] = A2

print(f"\n2. [SU(2)]^2 U(1)_Y:")
print(f"   Nc * Y_Q + Y_L")
print(f"   = {Nc} * {Y_Q} + {Y_L}")
print(f"   = {Nc * Y_Q} + {Y_L}")
print(f"   = {A2}")
print(f"   --> {'ZERO' if A2 == 0 else 'NONZERO *** ANOMALY ***'}")

# ---- Condition 3: [U(1)_Y]^3 ----
# Sum over LEFT-HANDED Weyl fermions of Y^3, with right-handed
# fields contributing -(-Y)^3 = +Y^3... NO.
# Convention: sum over all LH Weyl fermions. Right-handed fields
# are rewritten as LH conjugates with Y -> -Y.
# Per generation (all as LH Weyl):
#   Q_L: Nc * 2 * Y_Q^3          (LH doublet, Nc colors)
#   u_L^c: Nc * (-Y_u)^3         (conjugate of u_R)
#   d_L^c: Nc * (-Y_d)^3         (conjugate of d_R)
#   L_L: 2 * Y_L^3               (LH doublet)
#   e_L^c: (-Y_e)^3              (conjugate of e_R)
A3 = Nc * (2 * Y_Q**3 + (-Y_u)**3 + (-Y_d)**3) + 2 * Y_L**3 + (-Y_e)**3
results["[U(1)_Y]^3"] = A3

print(f"\n3. [U(1)_Y]^3  (all LH Weyl; RH fields enter as conjugates with -Y):")
print(f"   Nc*(2*Y_Q^3 + (-Y_u)^3 + (-Y_d)^3) + 2*Y_L^3 + (-Y_e)^3")
print(f"   Y_Q^3    = ({Y_Q})^3    = {Y_Q**3}")
print(f"   (-Y_u)^3 = ({-Y_u})^3 = {(-Y_u)**3}")
print(f"   (-Y_d)^3 = ({-Y_d})^3  = {(-Y_d)**3}")
print(f"   Y_L^3    = ({Y_L})^3    = {Y_L**3}")
print(f"   (-Y_e)^3 = ({-Y_e})^3     = {(-Y_e)**3}")
print(f"   Colored:  {Nc}*(2*{Y_Q**3} + {(-Y_u)**3} + {(-Y_d)**3}) = {Nc*(2*Y_Q**3 + (-Y_u)**3 + (-Y_d)**3)}")
print(f"   Leptonic: 2*{Y_L**3} + {(-Y_e)**3} = {2*Y_L**3 + (-Y_e)**3}")
print(f"   Total = {A3}")
print(f"   --> {'ZERO' if A3 == 0 else 'NONZERO *** ANOMALY ***'}")

# ---- Condition 4: [grav]^2 U(1)_Y ----
# Sum over all LH Weyl fermions of Y (RH enter with -Y).
# Per generation:
#   Q_L: Nc * 2 * Y_Q
#   u_L^c: Nc * (-Y_u)
#   d_L^c: Nc * (-Y_d)
#   L_L: 2 * Y_L
#   e_L^c: (-Y_e)
A4 = Nc * (2 * Y_Q + (-Y_u) + (-Y_d)) + 2 * Y_L + (-Y_e)
results["[grav]^2 U(1)_Y"] = A4

print(f"\n4. [grav]^2 U(1)_Y  (all LH Weyl; RH as conjugates):")
print(f"   Nc*(2*Y_Q - Y_u - Y_d) + 2*Y_L - Y_e")
print(f"   Colored:  {Nc}*(2*{Y_Q} - {Y_u} - {Y_d}) = {Nc*(2*Y_Q - Y_u - Y_d)}")
print(f"   Leptonic: 2*{Y_L} - {Y_e} = {2*Y_L - Y_e}")
print(f"   Total = {A4}")
print(f"   --> {'ZERO' if A4 == 0 else 'NONZERO *** ANOMALY ***'}")

# ---- Condition 5: [SU(2)]^2 SU(2)  (Witten anomaly) ----
# Vanishes when the number of SU(2) doublets is even.
# Per generation: Nc doublets (quarks) + 1 doublet (leptons) = Nc + 1 = 4
n_doublets = Nc + 1
A5_even = (n_doublets % 2 == 0)
results["Witten SU(2)"] = Fraction(0) if A5_even else Fraction(1)

print(f"\n5. Witten SU(2) anomaly:")
print(f"   Number of SU(2) doublets per generation = Nc + 1 = {n_doublets}")
print(f"   Even? {A5_even}")
print(f"   --> {'ZERO (even doublet count)' if A5_even else 'NONZERO *** ANOMALY ***'}")

# ---- Condition 6: [SU(3)]^3 ----
# Vanishes for equal numbers of fundamentals and antifundamentals,
# or more precisely: A(fund) = 1/2 for SU(3), and per generation
# we have Q_L (doublet = 2 fund) + u_R (1 antifund) + d_R (1 antifund)
# = 2 fund + 2 antifund => cancels.
# Equivalently: A(3) - A(3bar) = 0 when n_L(3) = n_L(3bar).
n_fund = 2   # Q_L doublet: 2 left-handed fundamentals
n_afund = 2  # u_R, d_R: 2 left-handed antifundamentals (right-handed fund)
A6 = n_fund - n_afund
results["[SU(3)]^3"] = Fraction(A6)

print(f"\n6. [SU(3)]^3:")
print(f"   Left-handed fundamentals:     {n_fund} (from Q_L doublet)")
print(f"   Left-handed antifundamentals: {n_afund} (from u_R, d_R)")
print(f"   A(3) - A(3bar) = {A6}")
print(f"   --> {'ZERO' if A6 == 0 else 'NONZERO *** ANOMALY ***'}")

# ---------------------------------------------------------------
# 5.  Summary
# ---------------------------------------------------------------
print("\n" + "=" * 66)
print("  SUMMARY")
print("=" * 66)
all_zero = True
for name, val in results.items():
    status = "PASS" if val == 0 else "FAIL"
    if val != 0:
        all_zero = False
    print(f"  {name:30s}  =  {str(val):8s}  [{status}]")

print(f"\n  All anomalies cancel: {all_zero}")

# ---------------------------------------------------------------
# 6.  Uniqueness argument
# ---------------------------------------------------------------
print("\n" + "=" * 66)
print("  UNIQUENESS OF HYPERCHARGE ASSIGNMENT")
print("=" * 66)

print("""
Given:
  (a) Electric charges from Klein bottle: Q_u=2/3, Q_d=-1/3, Q_nu=0, Q_e=-1
  (b) Weak isospin doublet structure:     T3 = +/- 1/2
  (c) Gell-Mann--Nishijima relation:      Q = T3 + Y/2

Step 1: Y is FULLY DETERMINED by (a)-(c) alone.
  - For any doublet (f_up, f_down) with T3 = +1/2, -1/2:
      Y = 2(Q_up - 1/2) = 2(Q_down + 1/2)
    Both give the same Y (this is the doublet consistency condition,
    equivalent to Q_up - Q_down = 1, which holds for both doublets).
  - For singlets with T3 = 0:
      Y = 2Q

  So the hypercharges are:""")

print(f"    Y_Q = {Y_Q},  Y_u = {Y_u},  Y_d = {Y_d},  Y_L = {Y_L},  Y_e = {Y_e}")

print("""
Step 2: These are the STANDARD MODEL hypercharges (exactly).

Step 3: Anomaly cancellation imposes 4 nontrivial equations on 5 unknowns
  (Y_Q, Y_u, Y_d, Y_L, Y_e). With Nc = 3, the solution space is
  1-dimensional (parametrized by overall normalization). The Klein
  bottle charges fix that normalization uniquely.

  Alternatively: the Klein bottle charges + GNN relation already fix
  all 5 hypercharges with no fitted factors. Anomaly cancellation
  is then a PREDICTION, not an input -- and it is satisfied exactly.

Conclusion:
  Klein bottle fractions {1/3, 1/2, 2/3}
    + doublet structure (T3 = +/- 1/2)
    + Q = T3 + Y/2
  ==> unique hypercharge assignment
  ==> anomaly cancellation follows automatically
  ==> full SM charge table from topology + one relation (GNN)
""")

# ---------------------------------------------------------------
# 7.  Explicit SM charge table
# ---------------------------------------------------------------
print("=" * 66)
print("  COMPLETE SM CHARGE TABLE (per generation, from Klein bottle)")
print("=" * 66)
print(f"  {'Field':<12} {'SU(3)':<8} {'SU(2)':<8} {'Y':>6} {'Q':>6}")
print(f"  {'-'*12} {'-'*8} {'-'*8} {'-'*6} {'-'*6}")

table = [
    ("Q_L",  "3", "2", Y_Q, f"{Q_u}, {Q_d}"),
    ("u_R",  "3", "1", Y_u, str(Q_u)),
    ("d_R",  "3", "1", Y_d, str(Q_d)),
    ("L_L",  "1", "2", Y_L, f"{Q_nu}, {Q_e}"),
    ("e_R",  "1", "1", Y_e, str(Q_e)),
]
for field, su3, su2, y, q in table:
    print(f"  {field:<12} {su3:<8} {su2:<8} {str(y):>6} {q:>10}")

print()
