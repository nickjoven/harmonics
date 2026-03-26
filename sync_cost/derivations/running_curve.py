#!/usr/bin/env python3
"""
The running curve: duty(2,K)/duty(3,K) vs α_s(μ)/α₂(μ).

One free mapping K → μ. If the SHAPE matches, it's not coincidence.

SM running at 1-loop:
    α_s(μ) = α_s(M_Z) / [1 + (α_s(M_Z) × b₃ / 2π) × ln(μ/M_Z)]
    α₂(μ)  = α₂(M_Z) / [1 + (α₂(M_Z) × b₂ / 2π) × ln(μ/M_Z)]

    b₃ = 11 - 2n_f/3 = 7  (for n_f=6 quarks)
    b₂ = 22/3 - n_f/3 - n_H/6 = 19/6  (SM with 1 Higgs)

Usage:
    python3 sync_cost/derivations/running_curve.py
"""

import math
import sys

sys.path.insert(0, "sync_cost/derivations")


# ── SM parameters ─────────────────────────────────────────────────────────────

MZ = 91.1876          # GeV
ALPHA_S_MZ = 0.1179
ALPHA_EM_MZ = 1/127.95
SIN2_TW = 0.23121
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW

# 1-loop β-function coefficients (SM, n_f=6, n_H=1)
B3 = 7.0              # SU(3): 11 - 2×6/3
B2 = 19.0 / 6.0       # SU(2): 22/3 - 6/3 - 1/6


def alpha_s_1loop(mu):
    """1-loop running of α_s from M_Z to μ."""
    L = math.log(mu / MZ)
    denom = 1 + ALPHA_S_MZ * B3 / (2 * math.pi) * L
    if denom <= 0:
        return float('inf')  # Landau pole
    return ALPHA_S_MZ / denom


def alpha_2_1loop(mu):
    """1-loop running of α₂ from M_Z to μ."""
    L = math.log(mu / MZ)
    denom = 1 + ALPHA_2_MZ * B2 / (2 * math.pi) * L
    if denom <= 0:
        return float('inf')
    return ALPHA_2_MZ / denom


def ratio_sm(mu):
    """SM 1-loop α_s/α₂ at scale μ."""
    a3 = alpha_s_1loop(mu)
    a2 = alpha_2_1loop(mu)
    if a2 <= 0 or a2 == float('inf'):
        return float('inf')
    return a3 / a2


# ── Tongue width and duty ────────────────────────────────────────────────────

def tongue_width(q, K):
    if q == 0:
        return 0.0
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    w_pert = 2 * (K / 2) ** q / q
    w_crit = 1.0 / (q * q)
    if K <= 0.5:
        return w_pert
    elif K >= 1.0:
        return w_crit
    else:
        t = (K - 0.5) / 0.5
        t = t * t * (3 - 2 * t)
        return w_pert * (1 - t) + w_crit * t


def duty(q, K):
    return tongue_width(q, K) / q


def duty_ratio(K):
    d2 = duty(2, K)
    d3 = duty(3, K)
    if d3 < 1e-50:
        return float('inf')
    return d2 / d3


# ── Find K for a given ratio ─────────────────────────────────────────────────

def find_K(target_ratio, tol=1e-12):
    """Bisect to find K where duty(2)/duty(3) = target."""
    lo, hi = 0.001, 1.0
    # Check boundaries
    r_lo = duty_ratio(lo)
    r_hi = duty_ratio(hi)
    if target_ratio > r_lo or target_ratio < r_hi:
        return None  # out of range
    for _ in range(200):
        mid = (lo + hi) / 2
        r = duty_ratio(mid)
        if r > target_ratio:
            lo = mid
        else:
            hi = mid
        if abs(r - target_ratio) < tol:
            break
    return (lo + hi) / 2


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("  THE RUNNING CURVE")
    print("  duty(2,K)/duty(3,K)  vs  α_s(μ)/α₂(μ)")
    print("=" * 80)

    # ── 1. SM running across energy scales ────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  1. SM 1-LOOP RUNNING: α_s/α₂ vs energy")
    print(f"{'─' * 80}\n")

    energies = [1, 2, 5, 10, 20, 50, MZ, 200, 500, 1000,
                5000, 10000, 50000, 1e6, 1e8, 1e10, 1e13, 1e16]

    sm_data = []
    print(f"  {'μ (GeV)':>12s}  {'α_s':>10s}  {'α₂':>10s}  "
          f"{'α_s/α₂':>10s}  {'K*':>10s}")
    print("  " + "-" * 60)

    for mu in energies:
        a3 = alpha_s_1loop(mu)
        a2 = alpha_2_1loop(mu)
        r = a3 / a2 if a2 > 0 and a2 != float('inf') else float('inf')
        K = find_K(r)
        K_str = f"{K:.6f}" if K is not None else "out of range"

        if mu >= 1000:
            mu_str = f"{mu:.0e}"
        else:
            mu_str = f"{mu:.1f}"

        print(f"  {mu_str:>12s}  {a3:10.4f}  {a2:10.6f}  "
              f"{r:10.4f}  {K_str:>10s}")
        sm_data.append((mu, r, K))

    # ── 2. Fix K→μ mapping at M_Z, predict everywhere else ───────────────
    print(f"\n{'─' * 80}")
    print("  2. K → μ MAPPING (fixed at M_Z)")
    print(f"{'─' * 80}\n")

    K_mz = find_K(ratio_sm(MZ))
    print(f"  Anchor: K* = {K_mz:.6f} at μ = M_Z = {MZ:.2f} GeV")
    print()

    # Build a table: for each energy, compute SM ratio and duty ratio at K(μ)
    # First, determine K(μ) by finding what K gives the SM ratio
    # Then compare the SHAPES

    # The shape test: does d(ratio)/d(lnμ) from SM match d(ratio)/d(K) × dK/d(lnμ)?
    # If we use a linear K→lnμ mapping: K(μ) = K_mz + slope × ln(μ/MZ)
    # Find slope from a second anchor point

    # Use μ = 1 GeV as second anchor
    K_1gev = find_K(ratio_sm(1.0))
    if K_1gev is not None and K_mz is not None:
        slope = (K_1gev - K_mz) / math.log(1.0 / MZ)
        print(f"  Linear mapping: K(μ) = {K_mz:.6f} + {slope:.6f} × ln(μ/M_Z)")
        print(f"  K(1 GeV)  = {K_1gev:.6f}")
        print(f"  K(M_Z)    = {K_mz:.6f}")
        print(f"  slope     = {slope:.6f}")
    else:
        slope = None
        print("  Cannot establish linear mapping")

    # ── 3. Shape comparison ───────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  3. SHAPE COMPARISON: duty curve vs SM running")
    print(f"{'─' * 80}\n")

    if slope is not None:
        print(f"  Using linear K(μ) = {K_mz:.4f} + {slope:.6f} × ln(μ/{MZ:.1f})")
        print(f"  (Two-point fit: anchored at 1 GeV and M_Z)")
        print()
        print(f"  {'μ (GeV)':>12s}  {'K(μ)':>8s}  {'duty ratio':>12s}  "
              f"{'SM ratio':>12s}  {'Δ':>8s}  {'Δ%':>8s}")
        print("  " + "-" * 70)

        total_err = 0.0
        n_pts = 0

        for mu in [1, 2, 5, 10, 20, 50, MZ, 200, 500, 1000,
                   5000, 10000]:
            K_mu = K_mz + slope * math.log(mu / MZ)
            if K_mu < 0.001 or K_mu > 1.0:
                continue
            dr = duty_ratio(K_mu)
            sr = ratio_sm(mu)
            delta = dr - sr
            pct = abs(delta) / sr * 100

            if mu >= 1000:
                mu_str = f"{mu:.0e}"
            else:
                mu_str = f"{mu:.1f}"

            print(f"  {mu_str:>12s}  {K_mu:8.4f}  {dr:12.4f}  "
                  f"{sr:12.4f}  {delta:+8.4f}  {pct:8.2f}%")
            total_err += pct ** 2
            n_pts += 1

        rms = math.sqrt(total_err / n_pts) if n_pts > 0 else 0
        print(f"\n  RMS error: {rms:.2f}%")

    # ── 4. Best-fit mapping (log-linear) ──────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  4. NONLINEAR K(μ): fitting the shape")
    print(f"{'─' * 80}\n")

    # For each SM energy point, find the exact K
    # Then fit K vs ln(μ) to see what mapping works
    print(f"  Exact K at each energy (inverting duty ratio = SM ratio):")
    print()
    print(f"  {'μ (GeV)':>12s}  {'SM ratio':>12s}  {'K_exact':>12s}  "
          f"{'ln(μ/MZ)':>12s}")
    print("  " + "-" * 56)

    fit_x = []  # ln(μ/MZ)
    fit_y = []  # K_exact

    for mu in [1, 2, 5, 10, 20, 50, MZ, 200, 500, 1000,
               5000, 10000, 50000, 1e6, 1e8]:
        sr = ratio_sm(mu)
        K_ex = find_K(sr)
        lnmu = math.log(mu / MZ)

        if K_ex is not None:
            if mu >= 1000:
                mu_str = f"{mu:.0e}"
            else:
                mu_str = f"{mu:.1f}"
            print(f"  {mu_str:>12s}  {sr:12.4f}  {K_ex:12.6f}  "
                  f"{lnmu:12.4f}")
            fit_x.append(lnmu)
            fit_y.append(K_ex)

    # Linear regression K = a + b × ln(μ/MZ)
    if len(fit_x) >= 3:
        n = len(fit_x)
        mx = sum(fit_x) / n
        my = sum(fit_y) / n
        sxx = sum((x - mx) ** 2 for x in fit_x)
        sxy = sum((x - mx) * (y - my) for x, y in zip(fit_x, fit_y))
        if sxx > 0:
            b = sxy / sxx
            a = my - b * mx
            print(f"\n  Linear fit: K = {a:.6f} + {b:.8f} × ln(μ/M_Z)")

            # Residuals
            print(f"\n  {'μ (GeV)':>12s}  {'K_exact':>10s}  "
                  f"{'K_fit':>10s}  {'residual':>10s}")
            print("  " + "-" * 48)

            max_resid = 0
            for x, y, mu in zip(fit_x, fit_y,
                                [1, 2, 5, 10, 20, 50, MZ, 200, 500, 1000,
                                 5000, 10000, 50000, 1e6, 1e8][:len(fit_x)]):
                K_fit = a + b * x
                resid = y - K_fit
                max_resid = max(max_resid, abs(resid))
                if mu >= 1000:
                    mu_str = f"{mu:.0e}"
                else:
                    mu_str = f"{mu:.1f}"
                print(f"  {mu_str:>12s}  {y:10.6f}  {K_fit:10.6f}  "
                      f"{resid:+10.6f}")

            print(f"\n  Max residual in K: {max_resid:.6f}")
            print(f"  If residual is small → K(μ) is linear in ln(μ)")
            print(f"  If residual is large → K(μ) is nonlinear (the shape differs)")

    # ── 5. The logarithmic derivative (β-function shape) ─────────────────
    print(f"\n{'─' * 80}")
    print("  5. β-FUNCTION SHAPE: d(ln ratio)/d(ln μ)")
    print(f"{'─' * 80}\n")

    print(f"  SM: d(ln(α_s/α₂))/d(lnμ) is the β-function of the ratio.")
    print(f"  Duty: d(ln(duty₂/duty₃))/d(K) × dK/d(lnμ) is the tree β.")
    print()

    dK = 1e-6
    print(f"  {'μ (GeV)':>12s}  {'β_SM':>12s}  {'β_duty':>12s}  "
          f"{'ratio β':>12s}")
    print("  " + "-" * 52)

    for mu in [2, 10, 50, MZ, 200, 1000, 10000]:
        # SM β
        r1 = ratio_sm(mu * 1.01)
        r0 = ratio_sm(mu / 1.01)
        r = ratio_sm(mu)
        beta_sm = (math.log(r1) - math.log(r0)) / (2 * 0.01) if r > 0 and r1 > 0 and r0 > 0 else 0

        # duty β at corresponding K
        K_mu = find_K(r)
        if K_mu is not None and K_mu > dK and K_mu < 1 - dK:
            r_plus = duty_ratio(K_mu + dK)
            r_minus = duty_ratio(K_mu - dK)
            if r_plus > 0 and r_minus > 0:
                beta_duty_dK = (math.log(r_plus) - math.log(r_minus)) / (2 * dK)
            else:
                beta_duty_dK = 0
            # Need dK/dlnμ from the mapping
            if slope is not None and slope != 0:
                beta_duty = beta_duty_dK * slope
            else:
                beta_duty = 0
        else:
            beta_duty = 0

        ratio_beta = beta_duty / beta_sm if beta_sm != 0 else 0

        if mu >= 1000:
            mu_str = f"{mu:.0e}"
        else:
            mu_str = f"{mu:.1f}"

        print(f"  {mu_str:>12s}  {beta_sm:12.6f}  {beta_duty:12.6f}  "
              f"{ratio_beta:12.4f}")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("  VERDICT")
    print(f"{'=' * 80}")
    print(f"""
  The shape comparison tests whether the tongue-width interpolation
  (perturbative ↔ critical) accidentally matches the SM β-function
  (asymptotic freedom ↔ infrared growth).

  If K(μ) is linear in ln(μ) with small residuals:
    → The duty curve has the SAME SHAPE as the SM running.
    → One slope parameter reproduces the entire curve.
    → Not coincidence.

  If K(μ) requires nonlinear corrections:
    → The shapes differ.
    → The tongue-width interpolation is not the β-function.
    → The 3.2% match at M_Z is a point coincidence, not a curve match.

  The test is the RESIDUALS in Section 4.
""")


if __name__ == "__main__":
    main()
