"""
Item 12: Higgs lambda residual -- wider scan for closed forms.

The previous scan (item12_other_residuals.py) looked only for
(small prefactor)/F_k^2 forms and found nothing under 0.5%.
That scan was too narrow. This script widens the space to
include:

  (1) Simple integer denominators 1/N for N up to ~500, with
      structural factorizations (q_2, q_3, framework integers)
  (2) Two-factor products p/(q^a F_k^b)
  (3) Cross-sector forms involving both q_2 and q_3
  (4) Forms that include 19 (Farey partition), 13 (F_6 count),
      and other framework-primary integers
"""

import math
from itertools import product


PHI = (1 + math.sqrt(5)) / 2
Q2, Q3 = 2, 3
K_LEPTON = Q3 ** 2         # 9
K_QUARK = Q2 ** 3          # 8
MEDIANT = Q2 + Q3          # 5
INTERACT = Q2 * Q3         # 6


# Observed Higgs values (PDG 2024)
M_H = 125.25
V_GEV = 246.22
LAMBDA_OBS = M_H ** 2 / (2 * V_GEV ** 2)
LAMBDA_TREE = 1 / Q2 ** 3   # 1/8 = 0.125
RES = LAMBDA_OBS - LAMBDA_TREE   # ~0.00438


def fib(k):
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


def structural_reading(N):
    """Try to express N in terms of framework-primary integers."""
    readings = []
    # Direct factorizations
    if N == Q2 ** 2 * Q3 * 19:
        readings.append("q_2^2 * q_3 * 19")
    if N == 12 * 19:
        readings.append("(2 q_2 q_3) * 19 = 2 * interaction * |F_7|")
    if N == 4 * 57:
        readings.append("q_2^2 * 57")
    if N == K_LEPTON * MEDIANT ** 2:
        readings.append("k_lepton * (q_2+q_3)^2 = 9 * 25")
    if N == (Q3 * MEDIANT) ** 2:
        readings.append("(q_3 * (q_2+q_3))^2 = 15^2")
    if N == K_LEPTON * K_QUARK * Q3:
        readings.append("k_lepton * k_quark * q_3")
    if N == K_QUARK * K_LEPTON:
        readings.append("k_lepton * k_quark")
    if N == INTERACT ** 3:
        readings.append("(q_2 q_3)^3")
    if N == Q3 ** 5:
        readings.append("q_3^5")
    # Fibonacci
    for k in range(3, 15):
        if N == fib(k):
            readings.append(f"F_{k}")
        if N == fib(k) ** 2:
            readings.append(f"F_{k}^2")
    # Simple products
    for a in [1, 2, 3, 4, 5, 6, 8, 9]:
        for b in [1, 2, 3, 5, 6, 13, 19]:
            if N == a * b and a * b > 10:
                pass  # skip generic
    return readings or ["(no clean structural reading)"]


def main():
    print("=" * 78)
    print("  HIGGS LAMBDA RESIDUAL: WIDER CLOSED-FORM SCAN")
    print("=" * 78)
    print()
    print(f"  m_H = {M_H} GeV  (PDG 2024)")
    print(f"  v   = {V_GEV} GeV")
    print(f"  lambda_obs  = m_H^2 / (2 v^2) = {LAMBDA_OBS:.10f}")
    print(f"  lambda_tree = 1/q_2^3 = 1/8     = {LAMBDA_TREE:.10f}")
    print(f"  residual    = {RES:.10f}")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  SCAN 1: simple 1/N for integer N, find closest N")
    print("-" * 78)
    print()

    # Scan integers around 1/residual
    N_target = 1 / RES
    print(f"  1/residual = {N_target:.3f}")
    print()
    print(f"  {'N':>6} {'1/N':>14} {'diff':>14} {'rel err':>10} {'readings':<40}")
    print("  " + "-" * 78)
    candidates = []
    for N in range(200, 260):
        pred = 1 / N
        err = abs(pred - RES)
        rel = err / RES
        candidates.append((rel, N, pred))
    candidates.sort()
    for rel, N, pred in candidates[:10]:
        readings = structural_reading(N)
        reading_str = ", ".join(readings[:2])
        flag = " ***" if rel < 0.005 else ""
        print(f"  {N:>6} {pred:>14.10f} {pred - RES:>+14.10f} "
              f"{rel*100:>9.4f}% {reading_str[:40]:<40}{flag}")
    print()

    # Focus on the closest match
    best_N = candidates[0][1]
    best_pred = candidates[0][2]
    best_rel = candidates[0][0]
    print(f"  Best simple 1/N fit: N = {best_N}")
    print(f"    1/{best_N} = {best_pred:.10f}")
    print(f"    residual observed = {RES:.10f}")
    print(f"    rel err = {best_rel*100:.4f}%")
    print(f"    structural reading: {structural_reading(best_N)}")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  SCAN 2: prefactor/N for small integer prefactor")
    print("-" * 78)
    print()

    scan_results = []
    for p in range(1, 21):
        for N in range(20, 3000):
            pred = p / N
            if abs(pred - RES) / RES < 0.01:
                scan_results.append((abs(pred - RES) / RES, p, N, pred))
    scan_results.sort()

    print(f"  Best 10 matches (with rel err < 1%):")
    print()
    print(f"  {'p':>4} {'N':>6} {'p/N':>14} {'rel err':>10} {'structure'}")
    print("  " + "-" * 70)
    seen = set()
    for rel, p, N, pred in scan_results[:20]:
        key = (p, N)
        if key in seen:
            continue
        seen.add(key)
        reading = structural_reading(N)
        reading_str = f"{p}/({', '.join(reading[:1])})"
        flag = " ***" if rel < 0.005 else ""
        print(f"  {p:>4} {N:>6} {pred:>14.8f} {rel*100:>9.4f}% "
              f"{reading_str[:50]}{flag}")
        if len([r for r, _, _, _ in scan_results[:20] if r == rel]) > 0:
            if len(seen) >= 10:
                break
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  VERIFICATION: predicted lambda and m_H under best form")
    print("-" * 78)
    print()
    print(f"  Using the cleanest fit: lambda = 1/8 + 1/{best_N}")
    print(f"    = {LAMBDA_TREE} + {1/best_N:.10f}")
    print(f"    = {LAMBDA_TREE + 1/best_N:.10f}")
    print(f"  Observed lambda = {LAMBDA_OBS:.10f}")
    print(f"  rel err = {abs(LAMBDA_TREE + 1/best_N - LAMBDA_OBS)/LAMBDA_OBS*100:.4f}%")
    print()
    predicted_mH = math.sqrt(2 * (LAMBDA_TREE + 1/best_N) * V_GEV ** 2)
    print(f"  Predicted m_H = sqrt(2 lambda_pred v^2) = {predicted_mH:.4f} GeV")
    print(f"  Observed  m_H = {M_H} GeV")
    print(f"  rel err = {abs(predicted_mH - M_H)/M_H*100:.4f}%")
    print()

    # ------------------------------------------------------------------
    print("-" * 78)
    print("  SANITY: PDG uncertainty on m_H")
    print("-" * 78)
    print()
    M_H_ERR = 0.17   # PDG 2024
    print(f"  m_H = {M_H} +/- {M_H_ERR} GeV")
    print(f"  rel unc = {M_H_ERR/M_H*100:.3f}%")
    print(f"  lambda uncertainty ~ 2 * {M_H_ERR/M_H*100:.3f}% = {2*M_H_ERR/M_H*100:.3f}%")
    print()
    print(f"  If the best fit is within {2*M_H_ERR/M_H*100:.3f}% of observed,")
    print(f"  it's within PDG uncertainty.")
    print()


if __name__ == "__main__":
    main()
