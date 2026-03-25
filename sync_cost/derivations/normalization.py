"""
Fix the last free parameter: coupling normalization from tongue widths.

D6 says: at the Planck scale, all three coupling stages equalize.
The tongue width at K=1 for denominator q is w = 1/q².

If α_q⁻¹(M_Pl) = C × q² for some universal constant C, then:
  α₁⁻¹(M_Pl) = C × 1 = C
  α₂⁻¹(M_Pl) = C × 4
  α₃⁻¹(M_Pl) = C × 9

Run these DOWN to M_Z using the SM one-loop beta functions.
The three equations give three predictions for (α₁, α₂, α₃) at M_Z
in terms of the single unknown C. Compare against measured values.
Solve for C. Check consistency.
"""

import math

# ── SM parameters ─────────────────────────────────────────────────────────────

M_Z = 91.1876        # GeV
M_Pl = 1.221e19      # GeV

# Measured (PDG 2024)
ALPHA_EM_INV = 127.951  # α_em⁻¹ at M_Z
SIN2_TH_W = 0.23122
ALPHA_S = 0.1179

# Derived measured values (GUT normalized)
ALPHA_1_INV_MEAS = ALPHA_EM_INV * (1 - SIN2_TH_W) * 3 / 5
# Actually: α₁ = (5/3)α_Y, and α_Y = α_em / cos²θ_W
# α₁⁻¹ = (3/5) × α_Y⁻¹ = (3/5) × α_em⁻¹ × cos²θ_W ... no.
# Standard: α₁⁻¹ = (3/5) × (cos²θ_W / α_em) = (3/5) × cos²θ_W × α_em⁻¹
# α_em = g² sin²θ / (4π) = α₂ sin²θ_W
# α₁ = (5/3) α_Y = (5/3)(α_em / cos²θ_W)
# α₁⁻¹ = (3/5) cos²θ_W / α_em = (3/5) cos²θ_W × 127.951
ALPHA_1_INV_MEAS = (3 / 5) * (1 - SIN2_TH_W) * ALPHA_EM_INV
ALPHA_2_INV_MEAS = SIN2_TH_W * ALPHA_EM_INV  # α₂⁻¹ = sin²θ_W / α_em ... no
# α₂ = α_em / sin²θ_W → α₂⁻¹ = sin²θ_W × α_em⁻¹
ALPHA_2_INV_MEAS = SIN2_TH_W * ALPHA_EM_INV
# Wait. α_em = α₂ sin²θ_W. So α₂ = α_em / sin²θ_W. α₂⁻¹ = sin²θ_W / α_em = sin²θ_W × α_em⁻¹
ALPHA_2_INV_MEAS = SIN2_TH_W * ALPHA_EM_INV
ALPHA_3_INV_MEAS = 1 / ALPHA_S

# Verify
print(f"Measured at M_Z:")
print(f"  α₁⁻¹ = {ALPHA_1_INV_MEAS:.2f}  (GUT normalized)")
print(f"  α₂⁻¹ = {ALPHA_2_INV_MEAS:.2f}")
print(f"  α₃⁻¹ = {ALPHA_3_INV_MEAS:.2f}")

# One-loop beta coefficients (SM: 3 gen, 1 Higgs)
B_1 = 41.0 / 10
B_2 = -19.0 / 6
B_3 = -7.0

LN_MPL_MZ = math.log(M_Pl / M_Z)  # ≈ 39.4


def alpha_inv_at_MZ(alpha_inv_Pl, b):
    """Run from M_Pl down to M_Z."""
    return alpha_inv_Pl - (b / (2 * math.pi)) * (-LN_MPL_MZ)
    # Running down: α⁻¹(M_Z) = α⁻¹(M_Pl) + (b/(2π)) × ln(M_Pl/M_Z)


def main():
    print("\n" + "=" * 70)
    print("  COUPLING NORMALIZATION FROM TONGUE WIDTHS")
    print("=" * 70)

    # ── The boundary condition ────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  BOUNDARY CONDITION: α_q⁻¹(M_Pl) = C × q²")
    print(f"{'─' * 70}")

    print(f"""
  Tongue width at K=1: w(p/q) = 1/q²
  Coupling inversely proportional to tongue width:
    α_q⁻¹ ∝ q²  (wider tongue = weaker coupling = larger α⁻¹)

  At M_Pl:
    α₁⁻¹(M_Pl) = C × 1² = C
    α₂⁻¹(M_Pl) = C × 2² = 4C
    α₃⁻¹(M_Pl) = C × 3² = 9C

  Run to M_Z using SM β-functions:
    α_i⁻¹(M_Z) = α_i⁻¹(M_Pl) + (b_i/(2π)) × ln(M_Pl/M_Z)

  ln(M_Pl/M_Z) = {LN_MPL_MZ:.2f}
  """)

    # ── Compute α_i⁻¹(M_Z) as function of C ──────────────────────────
    shift_1 = (B_1 / (2 * math.pi)) * LN_MPL_MZ
    shift_2 = (B_2 / (2 * math.pi)) * LN_MPL_MZ
    shift_3 = (B_3 / (2 * math.pi)) * LN_MPL_MZ

    print(f"  β-function shifts from M_Pl to M_Z:")
    print(f"    Δ₁ = (b₁/2π) × ln(M_Pl/M_Z) = {shift_1:+.2f}")
    print(f"    Δ₂ = (b₂/2π) × ln(M_Pl/M_Z) = {shift_2:+.2f}")
    print(f"    Δ₃ = (b₃/2π) × ln(M_Pl/M_Z) = {shift_3:+.2f}")

    # α₁⁻¹(M_Z) = C + Δ₁
    # α₂⁻¹(M_Z) = 4C + Δ₂
    # α₃⁻¹(M_Z) = 9C + Δ₃

    print(f"\n  Predicted at M_Z:")
    print(f"    α₁⁻¹(M_Z) = C + ({shift_1:.2f}) = C + {shift_1:.2f}")
    print(f"    α₂⁻¹(M_Z) = 4C + ({shift_2:.2f}) = 4C {shift_2:+.2f}")
    print(f"    α₃⁻¹(M_Z) = 9C + ({shift_3:.2f}) = 9C {shift_3:+.2f}")

    # ── Solve for C from each measured coupling ───────────────────────
    print(f"\n{'─' * 70}")
    print("  SOLVING FOR C FROM EACH COUPLING")
    print(f"{'─' * 70}")

    C_from_1 = (ALPHA_1_INV_MEAS - shift_1) / 1
    C_from_2 = (ALPHA_2_INV_MEAS - shift_2) / 4
    C_from_3 = (ALPHA_3_INV_MEAS - shift_3) / 9

    print(f"\n  From α₁: C = (α₁⁻¹(M_Z) - Δ₁) / 1  = ({ALPHA_1_INV_MEAS:.2f} - {shift_1:.2f}) / 1  = {C_from_1:.2f}")
    print(f"  From α₂: C = (α₂⁻¹(M_Z) - Δ₂) / 4  = ({ALPHA_2_INV_MEAS:.2f} - {shift_2:.2f}) / 4 = {C_from_2:.2f}")
    print(f"  From α₃: C = (α₃⁻¹(M_Z) - Δ₃) / 9  = ({ALPHA_3_INV_MEAS:.2f} - {shift_3:.2f}) / 9 = {C_from_3:.2f}")

    C_mean = (C_from_1 + C_from_2 + C_from_3) / 3
    C_spread = max(C_from_1, C_from_2, C_from_3) - min(C_from_1, C_from_2, C_from_3)
    print(f"\n  Mean C = {C_mean:.2f}")
    print(f"  Spread = {C_spread:.2f}  ({C_spread/C_mean*100:.1f}% of mean)")

    # ── Best-fit C and predictions ────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  PREDICTIONS AT BEST-FIT C")
    print(f"{'─' * 70}")

    # Least-squares: minimize Σ (α_i⁻¹(predicted) - α_i⁻¹(measured))²
    # α_i⁻¹(pred) = q_i² × C + Δ_i
    # d/dC [Σ (q_i²C + Δ_i - α_i_meas)²] = 0
    # Σ q_i² (q_i²C + Δ_i - α_i_meas) = 0
    # C × Σ q_i⁴ = Σ q_i² (α_i_meas - Δ_i)
    q = [1, 2, 3]
    alpha_meas = [ALPHA_1_INV_MEAS, ALPHA_2_INV_MEAS, ALPHA_3_INV_MEAS]
    shifts = [shift_1, shift_2, shift_3]

    sum_q4 = sum(qi ** 4 for qi in q)
    sum_q2_target = sum(qi ** 2 * (alpha_meas[i] - shifts[i]) for i, qi in enumerate(q))
    C_best = sum_q2_target / sum_q4

    print(f"\n  Least-squares C = {C_best:.4f}")
    print(f"\n  {'Coupling':>10s}  {'q':>3s}  {'Predicted':>10s}  {'Measured':>10s}  {'Residual':>10s}  {'Rel %':>8s}")
    print("  " + "-" * 55)

    for i, qi in enumerate(q):
        pred = qi ** 2 * C_best + shifts[i]
        meas = alpha_meas[i]
        resid = pred - meas
        rel = resid / meas * 100
        name = ["α₁⁻¹", "α₂⁻¹", "α₃⁻¹"][i]
        print(f"  {name:>10s}  {qi:3d}  {pred:10.2f}  {meas:10.2f}  {resid:+10.2f}  {rel:+8.1f}%")

    # ── What C means physically ───────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  WHAT C MEANS")
    print(f"{'─' * 70}")

    alpha_unified = 1 / C_best if C_best > 0 else float('inf')
    print(f"""
  C = α₁⁻¹(M_Pl) = {C_best:.2f}
  α_unified(M_Pl) = 1/C = {alpha_unified:.4f} = 1/{C_best:.1f}

  At M_Pl, the three couplings are:
    α₁(M_Pl) = 1/C       = {1/C_best:.6f}   = 1/{C_best:.1f}
    α₂(M_Pl) = 1/(4C)    = {1/(4*C_best):.6f}   = 1/{4*C_best:.1f}
    α₃(M_Pl) = 1/(9C)    = {1/(9*C_best):.6f}   = 1/{9*C_best:.1f}

  The ratios at M_Pl:
    α₂/α₁ = 1/4          (the tongue width ratio)
    α₃/α₁ = 1/9          (the tongue width ratio)
    α₃/α₂ = 4/9          (the tongue width ratio)

  These are EXACT at M_Pl in this scheme. The departures at M_Z
  are entirely due to the running, which is determined by the
  topology (gauge groups + generations + charges).
  """)

    # ── Alternative: C from α_s only ──────────────────────────────────
    print(f"{'─' * 70}")
    print("  PREDICTION: USE α_s(M_Z) ALONE TO PREDICT α_em AND sin²θ_W")
    print(f"{'─' * 70}")

    C_from_alpha_s = C_from_3
    print(f"\n  C from α_s alone: {C_from_alpha_s:.4f}")

    pred_1 = 1 * C_from_alpha_s + shift_1
    pred_2 = 4 * C_from_alpha_s + shift_2
    pred_3 = 9 * C_from_alpha_s + shift_3

    # sin²θ_W = α₁/(α₁ + α₂) ... no.
    # sin²θ_W = g'²/(g² + g'²) where g' is U(1)_Y coupling, g is SU(2)
    # With GUT normalization: α₁ = (5/3)g'²/(4π), α₂ = g²/(4π)
    # sin²θ_W = g'²/(g² + g'²) = (3/5)α₁ / ((3/5)α₁ + α₂)
    # = (3/5)/α₁⁻¹ / ((3/5)/α₁⁻¹ + 1/α₂⁻¹)
    # = (3/5)α₂⁻¹ / ((3/5)α₂⁻¹ + α₁⁻¹) ... hmm
    # Simpler: sin²θ_W = α_em/α₂
    # α_em⁻¹ = α₁⁻¹ × (3/5) + α₂⁻¹ ... no.
    # 1/α_em = 1/α₂ + (3/5)/α₁ → α_em⁻¹ = α₂⁻¹ + (3/5)α₁⁻¹ ... also no.
    # The correct relation: α_em⁻¹ = (3/5)α₁⁻¹ + α₂⁻¹
    # (This follows from 1/e² = 1/g² + 1/g'² and the (5/3) normalization)
    pred_alpha_em_inv = (3 / 5) * pred_1 + pred_2
    pred_sin2_tw = pred_alpha_em_inv / pred_2 if pred_2 > 0 else 0
    # Wait: sin²θ_W = α_em/α₂ = (1/α_em⁻¹)/(1/α₂⁻¹) = α₂⁻¹/α_em⁻¹ ... no
    # sin²θ_W = g'²/(g²+g'²) and α_em = e²/(4π) where 1/e² = 1/g² + 1/g'²
    # So α_em⁻¹ = α₂⁻¹ + α_Y⁻¹ where α_Y = (3/5)α₁
    # α_em⁻¹ = α₂⁻¹ + (5/3)α₁⁻¹ ... let me just use the standard formula.
    # sin²θ_W = 1 - M_W²/M_Z² = α_em × π / (√2 G_F M_W²) ... too complicated.
    # At tree level: sin²θ_W = g'²/(g²+g'²)
    # g'² = (5/3) × 4πα₁, g² = 4πα₂
    # sin²θ_W = (5/3)α₁ / ((5/3)α₁ + α₂)
    #          = (5/3)/pred_1 / ((5/3)/pred_1 + 1/pred_2)
    #          = (5/3)pred_2 / ((5/3)pred_2 + pred_1)
    pred_sin2 = (5 / 3) * (1 / pred_1) / ((5 / 3) * (1 / pred_1) + 1 / pred_2)

    pred_alpha_em = 1 / ((5 / 3) * pred_1 + pred_2)  # hmm, let me use 1/α_em = 1/α₂ + (3/5)/α₁
    # Actually: 1/α_em = 1/α₂ + 1/α_Y. α_Y = (3/5)α₁. 1/α_Y = (5/3)α₁⁻¹ = (5/3)pred_1
    # No wait: α₁ = (5/3)α_Y, so α_Y = (3/5)α₁, and α_Y⁻¹ = (5/3)α₁⁻¹ = (5/3)pred_1
    # α_em⁻¹ = α₂⁻¹ + α_Y⁻¹ = pred_2 + (5/3)pred_1
    pred_aem_inv = pred_2 + (5 / 3) * pred_1

    # sin²θ_W = α_em / α₂ = (1/pred_aem_inv) / (1/pred_2) = pred_2 / pred_aem_inv
    pred_s2tw = pred_2 / pred_aem_inv

    pred_alpha_s = 1 / pred_3

    print(f"\n  Predicted from α_s(M_Z) = {ALPHA_S} alone:")
    print(f"    C = {C_from_alpha_s:.4f}")
    print(f"    α₁⁻¹(M_Z) = {pred_1:.2f}  (measured: {ALPHA_1_INV_MEAS:.2f}, Δ = {(pred_1-ALPHA_1_INV_MEAS)/ALPHA_1_INV_MEAS*100:+.1f}%)")
    print(f"    α₂⁻¹(M_Z) = {pred_2:.2f}  (measured: {ALPHA_2_INV_MEAS:.2f}, Δ = {(pred_2-ALPHA_2_INV_MEAS)/ALPHA_2_INV_MEAS*100:+.1f}%)")
    print(f"    α₃⁻¹(M_Z) = {pred_3:.2f}  (measured: {ALPHA_3_INV_MEAS:.2f}, by construction)")
    print(f"    α_em⁻¹(M_Z) = {pred_aem_inv:.2f}  (measured: {ALPHA_EM_INV:.2f}, Δ = {(pred_aem_inv-ALPHA_EM_INV)/ALPHA_EM_INV*100:+.1f}%)")
    print(f"    sin²θ_W(M_Z) = {pred_s2tw:.4f}  (measured: {SIN2_TH_W:.4f}, Δ = {(pred_s2tw-SIN2_TH_W)/SIN2_TH_W*100:+.1f}%)")

    print(f"\n{'=' * 70}")
    print(f"  ONE INPUT: α_s(M_Z) = {ALPHA_S}")
    print(f"  ZERO FREE PARAMETERS (topology determines β-functions)")
    print(f"  BOUNDARY CONDITION: α_q⁻¹(M_Pl) = C × q² (tongue widths)")
    print(f"")
    print(f"  PREDICTIONS:")
    print(f"    α_em⁻¹(M_Z) = {pred_aem_inv:.1f}  (measured: {ALPHA_EM_INV:.1f})")
    print(f"    sin²θ_W(M_Z) = {pred_s2tw:.4f}  (measured: {SIN2_TH_W:.5f})")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
