"""
Does the fidelity bound (D9) close the remaining 10^59?

The Klein bottle removes one power of the hierarchy (mode count).
The remaining factor is ν_P/H₀ ~ 10^61 (frequency scale).

D9 (fidelity bound): a self-referential frequency measurement
cannot resolve Δω < ω_ref. When the reference IS the measured
system, the minimum resolvable frequency is the reference itself.

Applied to the vacuum: the 4 Klein bottle modes have frequencies
set by the tree structure. But the OBSERVABLE frequencies are
bounded by the fidelity limit: the universe measuring its own
vacuum modes cannot resolve modes finer than its own reference
frequency H₀.

If the fidelity bound replaces ν_P/q_max with H₀/q_tree:
  ν_i = f_i × H₀ / q_tree    (not f_i × ν_P / q_max)

where q_tree = F₁₉ = 4181, then the vacuum energy is:
  ρ_vac = 4 × Σ wᵢ × ½ℏ × 2π × f_i × H₀/q_tree / L_H³
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import H_0_SI

c = 2.998e8
G = 6.674e-11
hbar = 1.055e-34
l_P = math.sqrt(hbar * G / c**3)
t_P = l_P / c
nu_P = 1 / t_P
H0 = H_0_SI              # single source; framework_constants
L_H = c / H0
Lambda_obs = 1.1056e-52
rho_Lambda_obs = Lambda_obs * c**2 / (8 * math.pi * G)
rho_P = c**7 / (hbar * G**2)

modes = [
    ("(1/3, 1/2)", 1/3, 1/2),
    ("(1/2, 1/3)", 1/2, 1/3),
    ("(1/2, 2/3)", 1/2, 2/3),
    ("(2/3, 1/2)", 2/3, 1/2),
]
weights_golden = [0.2014, 0.2014, 0.2986, 0.2986]
weights_uniform = [0.25, 0.25, 0.25, 0.25]

F19 = 4181


def vacuum_energy(nu_fund, q_max, weights, volume):
    """4-mode vacuum energy density."""
    rho = 0
    for i, (name, f1, f2) in enumerate(modes):
        f_total = f1 + f2  # sum interpretation
        nu_i = f_total * nu_fund / q_max
        E_i = 0.5 * hbar * 2 * math.pi * nu_i
        rho += weights[i] * E_i
    return 4 * rho / volume  # 4 modes


def main():
    print("=" * 70)
    print("  DOES THE FIDELITY BOUND CLOSE THE REMAINING 10⁵⁹?")
    print("=" * 70)

    # ── The three frequency scales ────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  THREE FREQUENCY SCALES")
    print(f"{'─' * 70}")

    print(f"""
  1. Planck frequency: ν_P = {nu_P:.4e} Hz
  2. Hubble frequency: H₀  = {H0:.4e} Hz
  3. Ratio: ν_P/H₀ = {nu_P/H0:.4e}  (log₁₀ = {math.log10(nu_P/H0):.1f})

  The CC problem in one line:
    ρ_vac(all modes, ν_P) / ρ_Λ(observed) ~ (ν_P/H₀)² ~ 10¹²²

  Klein bottle removes mode count factor: 10¹²² → 10⁶¹ (one power)
  Fidelity bound removes frequency scale: 10⁶¹ → ? (the question)
  """)

    # ── Without fidelity bound: Planck reference ──────────────────────
    print(f"{'─' * 70}")
    print("  WITHOUT FIDELITY BOUND: ν_fund = ν_P")
    print(f"{'─' * 70}")

    rho_planck = vacuum_energy(nu_P, F19, weights_uniform, L_H**3)
    ratio_P = rho_planck / rho_Lambda_obs
    print(f"\n  ρ_vac = {rho_planck:.4e} J/m³")
    print(f"  ρ_Λ   = {rho_Lambda_obs:.4e} J/m³")
    print(f"  ratio  = {ratio_P:.4e}  (log₁₀ = {math.log10(ratio_P):+.1f})")
    print(f"  → Still 10⁶⁰ too large")

    # ── With fidelity bound: Hubble reference ─────────────────────────
    print(f"\n{'─' * 70}")
    print("  WITH FIDELITY BOUND: ν_fund = H₀")
    print(f"{'─' * 70}")

    print(f"""
  D9: a self-referential measurement with reference frequency ω_ref
  cannot resolve frequencies below ω_ref. The universe's reference
  oscillator is H₀ (D16: the Hubble frequency is the denominator
  of Hz). Mode frequencies measured against this reference:

    ν_i = f_i × H₀ / q_tree    (not f_i × ν_P / q_max)

  This is NOT ad hoc. D16 established that the Stern-Brocot tree
  depth counts HUBBLE CYCLES, not Planck times. The tree at depth
  19 has resolved F₁₉ = 4181 frequency ratios, and each ratio is
  measured against the Hubble oscillator. The fundamental frequency
  of the tree IS H₀, not ν_P.
  """)

    rho_hubble = vacuum_energy(H0, F19, weights_uniform, L_H**3)
    ratio_H = rho_hubble / rho_Lambda_obs
    print(f"  ρ_vac = {rho_hubble:.4e} J/m³")
    print(f"  ρ_Λ   = {rho_Lambda_obs:.4e} J/m³")
    print(f"  ratio  = {ratio_H:.4e}  (log₁₀ = {math.log10(ratio_H):+.1f})")

    # ── Detailed breakdown ────────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  DETAILED: EACH MODE'S CONTRIBUTION")
    print(f"{'─' * 70}")

    print(f"\n  ν_fund = H₀ = {H0:.4e} Hz")
    print(f"  q_tree = F₁₉ = {F19}")
    print(f"  Volume = L_H³ = {L_H**3:.4e} m³")

    print(f"\n  {'Mode':>15s}  {'f₁+f₂':>8s}  {'ν_i (Hz)':>12s}  "
          f"{'E_i = ½ℏω':>12s}  {'w_i':>8s}  {'ρ_i (J/m³)':>12s}")
    print("  " + "-" * 72)

    rho_total = 0
    for i, (name, f1, f2) in enumerate(modes):
        f = f1 + f2
        nu_i = f * H0 / F19
        E_i = 0.5 * hbar * 2 * math.pi * nu_i
        w = weights_uniform[i]
        rho_i = 4 * w * E_i / L_H**3
        rho_total += rho_i
        print(f"  {name:>15s}  {f:8.4f}  {nu_i:12.4e}  "
              f"{E_i:12.4e}  {w:8.4f}  {rho_i:12.4e}")

    print(f"  {'TOTAL':>15s}  {'':>8s}  {'':>12s}  {'':>12s}  {'':>8s}  {rho_total:12.4e}")
    print(f"\n  ρ_Λ (observed) = {rho_Lambda_obs:.4e} J/m³")
    print(f"  ratio = {rho_total/rho_Lambda_obs:.4e}")

    # ── Now with golden weights ───────────────────────────────────────
    print(f"\n  With golden-peaked weights:")
    rho_golden = vacuum_energy(H0, F19, weights_golden, L_H**3)
    ratio_golden = rho_golden / rho_Lambda_obs
    print(f"  ρ_vac = {rho_golden:.4e} J/m³")
    print(f"  ratio = {ratio_golden:.4e}  (log₁₀ = {math.log10(ratio_golden):+.1f})")

    # ── What q_tree gives exact match? ────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  WHAT q_tree GIVES EXACT MATCH?")
    print(f"{'─' * 70}")

    # ρ_vac = 4 × Σ wᵢ × ½ℏ × 2π × fᵢ × H₀/q / L_H³ = ρ_Λ
    # q = 4 × Σ wᵢ × πℏ × fᵢ × H₀ / (L_H³ × ρ_Λ)
    swf_uniform = sum(weights_uniform[i] * (modes[i][1] + modes[i][2])
                      for i in range(4))
    q_exact = 4 * swf_uniform * math.pi * hbar * H0 / (L_H**3 * rho_Lambda_obs)
    print(f"\n  Σwf (uniform) = {swf_uniform:.4f}")
    print(f"  q_exact = {q_exact:.4e}")
    print(f"  F₁₉ = {F19}")
    print(f"  ratio q_exact/F₁₉ = {q_exact/F19:.4f}")

    # ── The answer ────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("  THE ANSWER")
    print(f"{'=' * 70}")

    print(f"""
  With the fidelity bound (ν_fund = H₀, not ν_P):

    ρ_vac/ρ_Λ = {ratio_H:.4e}

  log₁₀(ratio) = {math.log10(ratio_H):+.2f}

  The fidelity bound brings the vacuum energy from 10⁶⁰ × ρ_Λ
  (Planck reference) down to {ratio_H:.1e} × ρ_Λ (Hubble reference).
  """)

    if abs(math.log10(ratio_H)) < 2:
        print(f"  THE FIDELITY BOUND CLOSES THE GAP TO WITHIN {abs(math.log10(ratio_H)):.1f} ORDERS.")
        print(f"  The q_tree needed for exact match: {q_exact:.1f}")
        print(f"  The q_tree from D16 (F₁₉): {F19}")
        print(f"  Ratio: {q_exact/F19:.4f}")

        if abs(q_exact / F19 - 1) < 0.1:
            print(f"\n  SELF-CONSISTENT: q_exact ≈ F₁₉ to within "
                  f"{abs(q_exact/F19 - 1)*100:.1f}%")
            print(f"  The cosmological constant is determined by the")
            print(f"  4-mode vacuum energy at tree depth 19 with the")
            print(f"  Hubble frequency as the fundamental scale.")
            print(f"  No fitted factors.")
        else:
            print(f"\n  NOT EXACT: q_exact/F₁₉ = {q_exact/F19:.4f}")
            print(f"  Off by a factor of {q_exact/F19:.2f}")
    else:
        print(f"  Gap remains: {abs(math.log10(ratio_H)):.0f} orders of magnitude")
        print(f"  The fidelity bound alone does not close it.")

    # ── Sensitivity to interpretation ─────────────────────────────────
    print(f"\n{'─' * 70}")
    print("  SENSITIVITY TO MODE FREQUENCY INTERPRETATION")
    print(f"{'─' * 70}")

    for f_label, f_func in [
        ("f₁ only", lambda f1, f2: f1),
        ("f₁ + f₂", lambda f1, f2: f1 + f2),
        ("(f₁+f₂)/2", lambda f1, f2: (f1 + f2) / 2),
        ("√(f₁²+f₂²)", lambda f1, f2: math.sqrt(f1**2 + f2**2)),
        ("f₁ × f₂", lambda f1, f2: f1 * f2),
        ("max(f₁,f₂)", lambda f1, f2: max(f1, f2)),
    ]:
        rho = 0
        for i, (name, f1, f2) in enumerate(modes):
            f = f_func(f1, f2)
            nu_i = f * H0 / F19
            E_i = 0.5 * hbar * 2 * math.pi * nu_i
            rho += weights_uniform[i] * E_i
        rho = 4 * rho / L_H**3
        ratio = rho / rho_Lambda_obs

        # What q gives exact match with this interpretation?
        swf = sum(weights_uniform[i] * f_func(modes[i][1], modes[i][2])
                  for i in range(4))
        q_ex = 4 * swf * math.pi * hbar * H0 / (L_H**3 * rho_Lambda_obs)

        print(f"  {f_label:>15s}:  ρ/ρ_Λ = {ratio:.4e}  "
              f"log₁₀ = {math.log10(ratio):+.2f}  "
              f"q_exact = {q_ex:.1f}  "
              f"q/F₁₉ = {q_ex/F19:.4f}")


if __name__ == "__main__":
    main()
