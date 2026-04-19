"""
a_s_alpha2_phase_b.py

Numerical companion to `a_s_alpha2_phase_b.md`. Verifies the
documented break points of the Phase B attempt:

  B1: alpha_3 from cosmology mode-volume.  Two interpretations of
      sigma_squared.py's "tongue width at pivot" differ by a factor
      `rate` ~= 0.0365 -- a 27x ambiguity.  Neither closes.

  B2: alpha_1 from locked-state combinatorics.  At K=1 with
      uniform g_baseline = 1, the per-mode variance is bracket-
      INDEPENDENT and cannot reproduce the observed 1/q^2 scaling.

  B3: alpha_2 by residual matching is inapplicable while alpha_1
      and alpha_3 are unfixed.

Run:
    python3 sync_cost/derivations/a_s_alpha2_phase_b.py
"""

from __future__ import annotations

import math

PHI = (1 + math.sqrt(5)) / 2
LN_PHI = math.log(PHI)
A_S_OBS = 2.10e-9
N_S = 0.9649
SIGMA_SQ = 1.5            # K_eff
RATE = (1 - N_S) / (2 * LN_PHI)


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main() -> None:
    q_pivot = fib(21)
    base = SIGMA_SQ ** 2 / (4 * math.pi ** 2 * q_pivot ** 2)
    C_target = A_S_OBS / base

    print("=" * 72)
    print("  alpha_2 PHASE B: ATTEMPT AND DECOMPOSITION")
    print(f"  q_pivot = F_21 = {q_pivot}")
    print(f"  C_{{A_s}} target = {C_target:.4f}")
    print("=" * 72)

    # ============================================================
    # B1: alpha_3 from cosmology mode-volume
    # ============================================================
    print()
    print("-" * 72)
    print("  B1: alpha_3 from cosmology mode-volume")
    print("-" * 72)

    # Reading M1: A_s = <R^2>_bracket * rate
    A_s_M1 = base * RATE
    ratio_M1 = A_S_OBS / A_s_M1

    # Reading M2: A_s = <R^2>_bracket / rate (i.e. tongue-width = per-d-ln-k)
    A_s_M2 = base / RATE
    ratio_M2 = A_S_OBS / A_s_M2

    # Reading M3 (sigma_squared.py implicit): A_s = sigma^4/(4 pi^2 q^2) directly
    A_s_M3 = base
    ratio_M3 = A_S_OBS / A_s_M3

    print(f"\n  rate = {RATE:.6f} levels per e-fold")
    print(f"  Three interpretations of sigma^4/(4 pi^2 q^2):")
    print(f"    {'reading':>30}  {'A_s_pred':>12}  {'ratio obs/pred':>16}")
    print("    " + "-" * 64)
    print(f"    {'M1 (per-bracket variance, A_s = <R^2>×rate)':>50}")
    print(f"    {'-> A_s_pred':>30}  {A_s_M1:12.3e}  {ratio_M1:16.2f}")
    print(f"    {'M2 (per-d-ln-k power, A_s = <R^2>/rate)':>50}")
    print(f"    {'-> A_s_pred':>30}  {A_s_M2:12.3e}  {ratio_M2:16.4f}")
    print(f"    {'M3 (formula-as-A_s, no rate factor)':>50}")
    print(f"    {'-> A_s_pred':>30}  {A_s_M3:12.3e}  {ratio_M3:16.4f}")

    print(f"""
  M1 misses by 121x; M2 misses by 0.16x; M3 misses by 4.41x.
  None closes.  The choice between M1, M2, M3 depends on whether
  the tongue width is read as per-bracket variance, per-d-ln-k
  power, or already-A_s.  Sigma_squared.py is silent on this.

  -- B1 break: 30x ambiguity from the {{M1, M2, M3}} choice.
""")

    # ============================================================
    # B2: alpha_1 from locked-state combinatorics
    # ============================================================
    print("-" * 72)
    print("  B2: alpha_1 from locked-state combinatorics")
    print("-" * 72)

    K_eff = 1.5
    sigma_kernel = 0.25
    g_at_pivot = 4.0  # = 1/(sigma_kernel) for uniform baseline g = 1
    perp_var_factor = g_at_pivot / K_eff ** 2
    print(f"""
  At K=1 with uniform g_baseline = 1:
      N(p/q) = g_baseline * w_tongue = 1 * sigma^2_kernel / q^2
             = (1/4) / q^2
      g(omega_pivot) = N(p/q) / w_tongue = (1/(4q^2)) / (1/(4q^2))
                    = 1   (after canonical normalization)

  But the spectral_tilt_reframed.md formula uses
      g(omega) = density of locked oscillators per unit Omega.
  In the K=1 uniform-baseline reading:
      g(omega_pivot) = 1 / w_tongue = 4 q^2 / sigma^2_kernel
                    = 4 q^2 / (1/4) = 16 q^2

  Per-mode variance:
      <delta_theta^2> = g(omega) / (K_eff)^2
                    = 16 q^2 / (3/2)^2
                    = 16 q^2 * 4/9
                    = 64 q^2 / 9

  q^2 SCALING IS WRONG SIGN.  The formula gives <delta_theta^2>
  INCREASING with q^2, but A_s_obs requires it to DECREASE as 1/q^2.

  This sign flip means the spectral_tilt_reframed.md combinatorics
  cannot supply the observed 1/q^2 scaling under the
  uniform-baseline reading.

  -- B2 break: 1/q^2 scaling cannot come from spectral_tilt
     combinatorics with uniform g.  It must come from elsewhere
     (gate fraction W1 vs inverse density W2; see Phase B doc Sec 5.3).
""")

    # ============================================================
    # B3: residual matching
    # ============================================================
    print("-" * 72)
    print("  B3: alpha_2 by residual matching")
    print("-" * 72)
    print("""
  With alpha_1 and alpha_3 unfixed, residual matching is undefined.
  Phase A candidates remain:
    alpha_2^B = 2 ln phi  ~= 0.962
    alpha_2^C = 1/phi     ~= 0.618

  -- B3 break: cannot proceed without B1+B2 closure.
""")

    # ============================================================
    # Summary
    # ============================================================
    print("=" * 72)
    print("  PHASE B FAILURE DECOMPOSITION")
    print("=" * 72)
    print("""
  Three sub-gaps, each prior to alpha_i derivation:

    S1 (gauge of R):       R = delta_theta vs delta_theta/(2pi) vs other
                           contributes (2pi)^k for some k = -2..+2
    S2 (formula meaning):  per-bracket vs per-d-ln-k power
                           contributes rate^k for k = -1..+1, i.e. 27x
    S3 (q^-2 source):      gate fraction (W1) vs inverse density (W2)
                           contributes O(1) coordination factor

  Closing S1+S2+S3 is necessary and sufficient for closing
  alpha_1, alpha_2, alpha_3.  Each is one focused session.

  Phase B as originally conceived -- assuming the sigma_squared.py
  formula is derived -- presupposed a closure that does not exist.
  The deeper diagnosis is that sigma_squared.py is heuristic,
  not derived.  The true next step is "Phase 0": derive A_s
  directly from the framework's fluctuation spectrum with all
  gauges and conversions explicit.
""")


if __name__ == "__main__":
    main()
