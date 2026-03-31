#!/usr/bin/env python3
"""
Per-mode convergence rate at the computation frontier.

The existing derivation (our_address.py) computes a single global
convergence rate: rho = 2/pi, giving digits = -log10(rho^N).

This is the AVERAGE rate. But modes don't converge uniformly.
A mode p/q with denominator q has:
  - Tongue width w(q) = 1/q^2 at K=1  (Gauss-Kuzmin)
  - Penetration depth epsilon(q) that depends on how far past
    the tongue boundary the effective coupling has pushed
  - Floquet rate lambda(q) = 2*sqrt(pi * K * epsilon(q))
  - Per-oscillation contraction rho(q) = exp(-lambda(q))
  - Digits after N oscillations: -log10(rho(q)^N)

The question: does the per-mode picture reproduce the global
"9 digits" when aggregated, and where does it break down?

STRUCTURE OF THE DERIVATION:

  1. For each Farey mode p/q in F_6, compute:
     - tongue width (sets the locking threshold)
     - penetration depth (how far past threshold at K* = 0.862)
     - Floquet rate (per-oscillation convergence)
     - digits resolved after 931 total oscillations

  2. Identify the FRONTIER: the mode(s) where digits ~ 0-1,
     i.e., where locking is currently in progress.

  3. Check: is there a mode that is mid-passage right now?
     If so, that mode IS the quantum-classical boundary.

Usage:
    python3 sync_cost/derivations/convergence_frontier.py
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import tongue_width


PHI = (1 + math.sqrt(5)) / 2
LN_PHI_SQ = math.log(PHI ** 2)


def euler_phi(n):
    """Euler totient function."""
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def farey_sequence(n):
    """Generate Farey sequence F_n as list of Fraction."""
    fracs = [Fraction(0, 1), Fraction(1, 1)]
    for q in range(1, n + 1):
        for p in range(1, q):
            if math.gcd(p, q) == 1:
                fracs.append(Fraction(p, q))
    return sorted(set(fracs))


def floquet_rate(epsilon, K):
    """
    Analytical Floquet convergence rate for the 0/1 tongue.

    lambda = 2 * sqrt(pi * K * epsilon)    for small epsilon

    This is derived from the saddle-node normal form:
      f'(theta*) = 1 - K cos(2pi theta*)
      Near boundary: cos(2pi theta*) ~ 2pi * sqrt(epsilon / (pi K))
      So f' ~ 1 - 2 sqrt(pi K epsilon)
      lambda = -ln|f'| ~ 2 sqrt(pi K epsilon)   for small epsilon

    For higher-q tongues (period-q orbits), the per-CYCLE rate is
    the same (same saddle-node geometry), but each cycle takes q
    iterations. So the per-iteration rate is lambda/q.
    """
    if epsilon <= 0:
        return 0.0
    return 2 * math.sqrt(math.pi * K * epsilon)


# ═══════════════════════════════════════════════════════════════════════
# CONSTANTS (from framework)
# ═══════════════════════════════════════════════════════════════════════

K_STAR = 0.862          # self-consistent coupling from universe_loop.py
K_C = 2 / math.pi       # Kuramoto critical coupling (global average)
N_FAREY = 6              # Farey depth
F6 = farey_sequence(N_FAREY)

# From our_address.py
OSCILLATIONS_PER_HUBBLE = sum(q * euler_phi(q) for q in range(1, N_FAREY + 1))
HUBBLE_CYCLES = 19.2     # derived from Friedmann integration
TOTAL_OSCILLATIONS = HUBBLE_CYCLES * OSCILLATIONS_PER_HUBBLE


def main():
    print("=" * 80)
    print("  PER-MODE CONVERGENCE AT THE COMPUTATION FRONTIER")
    print("=" * 80)

    # ── 1. Global baseline ────────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  1. GLOBAL BASELINE (existing calculation)")
    print(f"{'─' * 80}\n")

    rho_global = K_C
    digits_global = -math.log10(rho_global ** TOTAL_OSCILLATIONS)
    print(f"  rho_global      = 2/pi = {rho_global:.6f}")
    print(f"  oscillations    = {OSCILLATIONS_PER_HUBBLE} per Hubble cycle"
          f" x {HUBBLE_CYCLES} cycles = {TOTAL_OSCILLATIONS:.0f}")
    print(f"  digits (global) = -log10({rho_global:.4f}^{TOTAL_OSCILLATIONS:.0f})"
          f" = {digits_global:.1f}")

    # ── 2. Per-mode convergence ───────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  2. PER-MODE CONVERGENCE RATES")
    print(f"{'─' * 80}\n")
    print(f"  For each mode p/q in F_6, compute:")
    print(f"    - tongue width w(q) at K* = {K_STAR}")
    print(f"    - penetration depth epsilon = w(q) (fraction of tongue entered)")
    print(f"    - Floquet rate lambda per oscillation")
    print(f"    - contraction ratio rho(q) = exp(-lambda/q) per iteration")
    print(f"    - digits after {TOTAL_OSCILLATIONS:.0f} oscillations")
    print()

    print(f"  {'p/q':>8s}  {'q':>3s}  {'w(q)':>10s}  {'epsilon':>10s}"
          f"  {'lambda':>10s}  {'lam/q':>10s}  {'rho(q)':>10s}"
          f"  {'digits':>8s}  {'status':>12s}")
    print("  " + "-" * 95)

    interior_modes = [f for f in F6 if 0 < f < 1]
    mode_data = []

    for frac in interior_modes:
        p, q = frac.numerator, frac.denominator

        w = tongue_width(1, q, K_STAR)

        # Penetration depth: how far inside the tongue is this mode?
        # At K_STAR, the effective coupling K_eff = K_STAR * |r*|
        # The tongue exists with width w(q, K_STAR).
        # For a mode at the CENTER of its tongue, epsilon = w/2.
        # This is the maximum depth; actual depth depends on where
        # in the tongue the mode's natural frequency sits.
        #
        # Key assumption to test: modes at center of tongue.
        epsilon = w / 2

        # Floquet rate (per cycle of the orbit)
        lam = floquet_rate(epsilon, K_STAR)

        # Per-iteration rate: a period-q orbit takes q iterations
        # per cycle, so the per-iteration contraction is lambda/q
        lam_per_iter = lam / q

        # Contraction ratio per iteration
        rho_q = math.exp(-lam_per_iter) if lam_per_iter > 0 else 1.0

        # Number of iterations this mode experiences:
        # Each oscillation of the full system includes contributions
        # from all modes. Mode p/q contributes q iterations per cycle.
        # But the mode-weighted count already accounts for this.
        #
        # Total iterations for mode p/q = total_oscillations
        # (each "oscillation" is one pass through the self-consistency loop)
        if rho_q < 1.0:
            digits = -math.log10(rho_q) * TOTAL_OSCILLATIONS
        else:
            digits = 0.0

        # Status
        if digits > 10:
            status = "CLASSICAL"
        elif digits > 1:
            status = "RESOLVING"
        elif digits > 0.01:
            status = "FRONTIER"
        else:
            status = "UNLOCKED"

        mode_data.append({
            'frac': frac, 'p': p, 'q': q, 'w': w, 'eps': epsilon,
            'lam': lam, 'lam_q': lam_per_iter, 'rho': rho_q,
            'digits': digits, 'status': status,
        })

        print(f"  {p}/{q:>2d}      {q:>3d}  {w:10.6f}  {epsilon:10.6f}"
              f"  {lam:10.6f}  {lam_per_iter:10.6f}  {rho_q:10.6f}"
              f"  {digits:8.1f}  {status:>12s}")

    # ── 3. Aggregate check ────────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  3. AGGREGATE: does per-mode picture match global?")
    print(f"{'─' * 80}\n")

    # The global rate rho = 2/pi should be related to the
    # mode-weighted average of per-mode rho(q).
    # Weight each mode by its Farey measure phi(q)/q^2.
    total_weight = 0
    weighted_log_rho = 0
    for md in mode_data:
        q = md['q']
        weight = euler_phi(q) / (q * q)
        total_weight += weight
        if md['rho'] < 1:
            weighted_log_rho += weight * math.log(md['rho'])

    if total_weight > 0:
        rho_aggregate = math.exp(weighted_log_rho / total_weight)
    else:
        rho_aggregate = 1.0

    digits_aggregate = -math.log10(rho_aggregate) * TOTAL_OSCILLATIONS

    print(f"  Global rho (2/pi):           {rho_global:.6f}")
    print(f"  Aggregate rho (mode-weighted): {rho_aggregate:.6f}")
    print(f"  Match: {'YES' if abs(rho_global - rho_aggregate) < 0.05 else 'NO'}"
          f"  (delta = {abs(rho_global - rho_aggregate):.6f})")
    print()
    print(f"  Global digits:     {digits_global:.1f}")
    print(f"  Aggregate digits:  {digits_aggregate:.1f}")

    # ── 4. The frontier ──────────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  4. THE FRONTIER: where is convergence currently active?")
    print(f"{'─' * 80}\n")

    frontier = [md for md in mode_data if md['status'] == 'FRONTIER']
    resolving = [md for md in mode_data if md['status'] == 'RESOLVING']
    classical = [md for md in mode_data if md['status'] == 'CLASSICAL']
    unlocked = [md for md in mode_data if md['status'] == 'UNLOCKED']

    print(f"  CLASSICAL (digits > 10): {len(classical)} modes"
          f"  — fully locked, deterministic")
    for md in classical:
        print(f"    {md['p']}/{md['q']} : {md['digits']:.1f} digits")

    print(f"\n  RESOLVING (1-10 digits): {len(resolving)} modes"
          f"  — locked but convergence still active")
    for md in resolving:
        print(f"    {md['p']}/{md['q']} : {md['digits']:.1f} digits")

    print(f"\n  FRONTIER (< 1 digit):    {len(frontier)} modes"
          f"  — mid-passage, quantum regime")
    for md in frontier:
        print(f"    {md['p']}/{md['q']} : {md['digits']:.3f} digits")

    print(f"\n  UNLOCKED (0 digits):     {len(unlocked)} modes"
          f"  — below coupling threshold")
    for md in unlocked:
        print(f"    {md['p']}/{md['q']} : {md['digits']:.3f} digits")

    # ── 5. Breakdown analysis ─────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  5. WHERE DOES THIS BREAK DOWN?")
    print(f"{'─' * 80}\n")

    print("""  Known issues with this per-mode calculation:

  1. PENETRATION DEPTH ASSUMPTION: We used epsilon = w/2 (center of tongue).
     In reality, each mode's natural frequency places it at a specific depth.
     The distribution g* determines these depths self-consistently — you can't
     compute epsilon without knowing g*, and g* depends on all epsilons.
     This is the self-referential loop that the fixed-point resolves.

  2. FLOQUET RATE GENERALIZATION: The analytical lambda = 2*sqrt(pi*K*eps)
     is exact only for the 0/1 tongue (period-1). For higher-q tongues,
     the saddle-node geometry is the same but the Floquet multiplier
     is the product of q derivatives around the orbit, not a single one.
     The scaling tau ~ 1/sqrt(eps) still holds, but the constant C(q)
     may depend on q in a way not captured here.

  3. MODE COUPLING: Modes don't converge independently. Locking of mode
     p/q changes the effective coupling for all other modes (through |r|).
     The global fixed-point equation handles this implicitly, but the
     per-mode picture treats them as independent. This is the key gap
     between the structural derivation and the dynamical one.

  4. THE REFRESH RATE QUESTION: We used total_oscillations = 931 for all
     modes. But if mode p/q takes q iterations per cycle, it has
     experienced 931/q full locking cycles, not 931. A q=6 mode has
     had ~155 cycles to converge. A q=1 mode has had ~931.
     This q-dependence may be crucial at the frontier.
""")

    # ── 6. Corrected per-mode with q-dependent cycle count ────────────────
    print(f"{'─' * 80}")
    print("  6. CORRECTED: accounting for q-dependent cycle count")
    print(f"{'─' * 80}\n")

    print(f"  {'p/q':>8s}  {'q':>3s}  {'cycles':>8s}  {'lam/cycle':>10s}"
          f"  {'rho/cycle':>10s}  {'digits':>8s}  {'status':>12s}")
    print("  " + "-" * 75)

    for md in mode_data:
        q = md['q']
        # Each cycle of a period-q orbit takes q iterations.
        # In TOTAL_OSCILLATIONS iterations, the mode completes
        # TOTAL_OSCILLATIONS / q full cycles.
        full_cycles = TOTAL_OSCILLATIONS / q

        # The Floquet rate lambda is per-CYCLE (not per-iteration).
        lam_per_cycle = md['lam']
        rho_per_cycle = math.exp(-lam_per_cycle) if lam_per_cycle > 0 else 1.0

        if rho_per_cycle < 1.0:
            digits_corrected = -math.log10(rho_per_cycle) * full_cycles
        else:
            digits_corrected = 0.0

        if digits_corrected > 10:
            status = "CLASSICAL"
        elif digits_corrected > 1:
            status = "RESOLVING"
        elif digits_corrected > 0.01:
            status = "FRONTIER"
        else:
            status = "UNLOCKED"

        print(f"  {md['p']}/{q:>2d}      {q:>3d}  {full_cycles:8.0f}"
              f"  {lam_per_cycle:10.6f}  {rho_per_cycle:10.6f}"
              f"  {digits_corrected:8.1f}  {status:>12s}")


    # ── 7. Beyond F_6: where IS the frontier? ──────────────────────────
    print(f"\n{'─' * 80}")
    print("  7. BEYOND F_6: the frontier must be at higher denominators")
    print(f"{'─' * 80}\n")

    print("""  All 11 interior modes of F_6 are deeply classical (24+ digits).
  The frontier — where digits ~ 0-1 — must be at denominators q > 6.
  These are modes OUTSIDE the Farey-6 set: the ones the framework says
  don't participate in the self-predicting set.

  But they still exist on the Stern-Brocot tree. They still have tongues.
  They're just narrower (w ~ 1/q^2), and the penetration depth at K*
  may be too shallow for locking to complete.

  Question: at what denominator q does the mode become mid-passage
  (digits ~ 1) given 941 oscillations at K* = 0.862?
""")

    print(f"  {'q':>4s}  {'w(q)':>12s}  {'eps=w/2':>12s}  {'lambda':>10s}"
          f"  {'cycles':>8s}  {'digits':>8s}  {'status':>12s}")
    print("  " + "-" * 80)

    for q in range(1, 51):
        w = tongue_width(1, q, K_STAR)
        eps = w / 2
        lam = floquet_rate(eps, K_STAR)
        full_cycles = TOTAL_OSCILLATIONS / q
        rho_cycle = math.exp(-lam) if lam > 0 else 1.0

        if rho_cycle < 1.0:
            digits = -math.log10(rho_cycle) * full_cycles
        else:
            digits = 0.0

        if digits > 100:
            status = "CLASSICAL"
        elif digits > 10:
            status = "classical"
        elif digits > 1:
            status = "RESOLVING"
        elif digits > 0.01:
            status = "FRONTIER"
        else:
            status = "UNLOCKED"

        if q <= 10 or status in ("RESOLVING", "FRONTIER", "UNLOCKED") or q % 5 == 0:
            print(f"  {q:4d}  {w:12.8f}  {eps:12.8f}  {lam:10.6f}"
                  f"  {full_cycles:8.0f}  {digits:8.1f}  {status:>12s}")

    # ── 8. The critical denominator ───────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  8. THE CRITICAL DENOMINATOR: q where digits = 1")
    print(f"{'─' * 80}\n")

    # Binary search for the q where digits crosses 1
    for q in range(1, 1000):
        w = tongue_width(1, q, K_STAR)
        eps = w / 2
        lam = floquet_rate(eps, K_STAR)
        full_cycles = TOTAL_OSCILLATIONS / q
        rho_cycle = math.exp(-lam) if lam > 0 else 1.0
        if rho_cycle < 1.0:
            digits = -math.log10(rho_cycle) * full_cycles
        else:
            digits = 0.0
        if digits < 1.0:
            print(f"  First mode with < 1 digit: q = {q}")
            print(f"    w(q) = {w:.2e}, eps = {eps:.2e}")
            print(f"    lambda = {lam:.6f}, cycles = {full_cycles:.0f}")
            print(f"    digits = {digits:.4f}")
            print()

            # What scale does this correspond to?
            # The Stern-Brocot tree level for denominator q is ~ log_phi(q)
            tree_level = math.log(q) / math.log(PHI)
            frac_of_depth = tree_level / 145.8
            print(f"    Tree level ~ log_phi({q}) = {tree_level:.1f}")
            print(f"    Fraction of total depth (145.8): {frac_of_depth:.4f}")
            print(f"    This is {'NEAR' if frac_of_depth > 0.9 else 'FAR FROM'}"
                  f" the Planck scale")
            break


    # ── 9. CARDINALITY SHEDDING: where does the mode count drop? ────────
    print(f"\n{'─' * 80}")
    print("  9. CARDINALITY SHEDDING: coverage by q-band")
    print(f"{'─' * 80}\n")

    print("""  The framework claims |F_6| = 13 is the self-predicting set.
  But modes with q > 6 have nonzero tongue widths at K* = 0.862.
  How much of the frequency axis do they claim?

  If q > 6 modes collectively cover a negligible fraction, the
  cardinality is effectively shed there. If they cover a significant
  fraction, the 13-mode picture is incomplete.
""")

    # Coverage by q-band at K* and at K=1
    print(f"  {'q':>4s}  {'phi(q)':>6s}  {'w(q,K*)':>12s}  {'band coverage':>14s}"
          f"  {'cumul':>10s}  {'w(q,K=1)':>12s}  {'cumul(K=1)':>12s}")
    print("  " + "-" * 85)

    cumul_kstar = 0.0
    cumul_k1 = 0.0
    for q in range(1, 51):
        phi_q = euler_phi(q)
        w_kstar = tongue_width(1, q, K_STAR)
        w_k1 = tongue_width(1, q, 1.0)
        band_kstar = phi_q * w_kstar
        band_k1 = phi_q * w_k1
        cumul_kstar += band_kstar
        cumul_k1 += band_k1

        if q <= 10 or q % 5 == 0:
            print(f"  {q:4d}  {phi_q:6d}  {w_kstar:12.8f}  {band_kstar:14.8f}"
                  f"  {cumul_kstar:10.6f}  {w_k1:12.8f}  {cumul_k1:12.6f}")

    # What fraction is q <= 6?
    cov_leq6_kstar = sum(euler_phi(q) * tongue_width(1, q, K_STAR) for q in range(1, 7))
    cov_gt6_kstar = cumul_kstar - cov_leq6_kstar
    cov_leq6_k1 = sum(euler_phi(q) * tongue_width(1, q, 1.0) for q in range(1, 7))

    print(f"\n  At K* = {K_STAR}:")
    print(f"    q <= 6 coverage: {cov_leq6_kstar:.6f}"
          f"  ({cov_leq6_kstar/cumul_kstar*100:.1f}% of total)")
    print(f"    q > 6 coverage:  {cov_gt6_kstar:.6f}"
          f"  ({cov_gt6_kstar/cumul_kstar*100:.1f}% of total)")
    print(f"    gap (uncovered):  {1 - cumul_kstar:.6f}")

    print(f"\n  At K = 1.0:")
    print(f"    q <= 6 coverage: {cov_leq6_k1:.6f}")
    print(f"    Total (q->inf):  1.000000  (exact, by Gauss-Kuzmin)")

    # ── 10. REGIME CHANGE: the tongue width formula's boundary ────────────
    print(f"\n{'─' * 80}")
    print("  10. REGIME CHANGE: perturbative vs critical tongue width")
    print(f"{'─' * 80}\n")

    print("""  The tongue width formula interpolates between two regimes:
    K <= 0.5:  w_pert = 2(K/2)^q / q    (perturbative, exponential in q)
    K >= 1.0:  w_crit = 1/q^2            (critical, power-law in q)

  At K* = 0.862, we're in the interpolation zone. The Hermite
  smoothstep t = ((K-0.5)/0.5)^2 * (3 - 2*(K-0.5)/0.5) blends them.

  Key question: do the two regimes DISAGREE about which modes matter?
  If w_pert << w_crit for some q, then the perturbative regime has
  effectively killed that mode while the critical regime keeps it alive.
  The interpolation blends a live mode with a dead one.
""")

    K = K_STAR
    t_raw = (K - 0.5) / 0.5
    t_smooth = t_raw * t_raw * (3 - 2 * t_raw)

    print(f"  K* = {K}, t_raw = {t_raw:.4f}, t_smooth = {t_smooth:.4f}")
    print(f"  Blend: w = w_pert × (1-t) + w_crit × t")
    print(f"         = w_pert × {1-t_smooth:.4f} + w_crit × {t_smooth:.4f}")
    print()

    print(f"  {'q':>4s}  {'w_pert':>12s}  {'w_crit':>12s}  {'ratio':>10s}"
          f"  {'w_blend':>12s}  {'pert_frac':>10s}  {'regime':>10s}")
    print("  " + "-" * 80)

    crossover_q = None
    for q in range(1, 31):
        if q == 1:
            w_pert = K / (2 * math.pi)
            w_crit = K / (2 * math.pi)
        else:
            w_pert = 2 * (K / 2) ** q / q
            w_crit = 1.0 / (q * q)

        ratio = w_pert / w_crit if w_crit > 0 else float('inf')
        w_blend = w_pert * (1 - t_smooth) + w_crit * t_smooth
        pert_frac = w_pert * (1 - t_smooth) / w_blend if w_blend > 0 else 0

        if ratio < 1 and crossover_q is None:
            crossover_q = q

        if ratio > 0.1:
            regime = "PERT"
        elif ratio > 0.001:
            regime = "MIXED"
        else:
            regime = "CRITICAL"

        if q <= 15 or q % 5 == 0:
            print(f"  {q:4d}  {w_pert:12.2e}  {w_crit:12.6f}  {ratio:10.4f}"
                  f"  {w_blend:12.8f}  {pert_frac:10.4f}  {regime:>10s}")

    print(f"\n  Crossover (w_pert < w_crit): q = {crossover_q}")
    print(f"  Below this q, perturbative tongues are WIDER than critical.")
    print(f"  Above this q, perturbative tongues are EXPONENTIALLY NARROWER.")

    # ── 11. THE RESOLUTION: perturbative death vs critical survival ───────
    print(f"\n{'─' * 80}")
    print("  11. RESOLUTION ATTEMPT: what if we use pure perturbative?")
    print(f"{'─' * 80}\n")

    print("""  If the universe is at K* = 0.862 (sub-critical), maybe the
  critical formula w = 1/q^2 is wrong to apply. The perturbative
  formula w = 2(K/2)^q / q kills high-q modes EXPONENTIALLY.

  Under pure perturbative tongues, where is the frontier?
""")

    print(f"  {'q':>4s}  {'w_pert':>12s}  {'eps':>12s}  {'lambda':>10s}"
          f"  {'cycles':>8s}  {'digits':>8s}  {'status':>12s}")
    print("  " + "-" * 75)

    for q in range(1, 21):
        if q == 1:
            w = K / (2 * math.pi)
        else:
            w = 2 * (K / 2) ** q / q
        eps = w / 2
        lam = floquet_rate(eps, K)
        full_cycles = TOTAL_OSCILLATIONS / q
        rho_cycle = math.exp(-lam) if lam > 0 else 1.0
        if rho_cycle < 1.0 and rho_cycle > 0:
            digits = -math.log10(rho_cycle) * full_cycles
        else:
            digits = 0.0

        if digits > 10:
            status = "CLASSICAL"
        elif digits > 1:
            status = "RESOLVING"
        elif digits > 0.01:
            status = "FRONTIER"
        else:
            status = "UNLOCKED"

        print(f"  {q:4d}  {w:12.2e}  {eps:12.2e}  {lam:10.6f}"
              f"  {full_cycles:8.0f}  {digits:8.1f}  {status:>12s}")

    # Under perturbative, find where digits < 1
    for q in range(1, 200):
        if q == 1:
            w = K / (2 * math.pi)
        else:
            w = 2 * (K / 2) ** q / q
        eps = w / 2
        lam = floquet_rate(eps, K)
        full_cycles = TOTAL_OSCILLATIONS / q
        rho_cycle = math.exp(-lam) if lam > 0 else 1.0
        if rho_cycle < 1.0 and rho_cycle > 0:
            digits = -math.log10(rho_cycle) * full_cycles
        else:
            digits = 0.0
        if digits < 1.0:
            tree_level = math.log(q) / math.log(PHI)
            print(f"\n  PERTURBATIVE frontier: q = {q}, digits = {digits:.4f}")
            print(f"    w_pert = {w:.2e}")
            print(f"    Tree level ~ {tree_level:.1f}")
            print(f"    Fraction of depth 145.8: {tree_level/145.8:.4f}")
            break

    # ── 12. SUMMARY ───────────────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  12. FINDINGS")
    print(f"{'─' * 80}\n")

    print("""  CARDINALITY SHEDDING:
    At K* = 0.862, q <= 6 modes claim the large majority of tongue coverage.
    q > 6 modes are individually tiny but collectively non-negligible.
    At K = 1.0, ALL modes contribute (Gauss-Kuzmin sums to 1 exactly).
    The framework uses K* < 1, so the coverage is < 1 — the gap is real.

  REGIME CHANGE:
    The tongue width formula has a crossover at q ~ 5-7 where
    perturbative (exponential death) and critical (power-law survival)
    give different answers. At K* = 0.862, the Hermite blend is ~87%
    critical, which keeps high-q modes alive with w ~ 1/q^2.

    If we use PURE PERTURBATIVE tongues (exponential in q), modes
    die fast and the frontier moves much closer to F_6.

  OPEN QUESTION:
    Which tongue width formula is physically correct at K* = 0.862?
    - If critical (1/q^2): frontier at q~30, far from Planck scale
    - If perturbative (K^q/q): frontier much closer to q~6-8
    - The Hermite blend is a smooth interpolation, NOT a derivation

    This is the crux: the interpolation is an ASSUMPTION, not a theorem.
    The convergence frontier's location depends entirely on which regime
    the tongue widths obey at K* = 0.862. This needs to be derived from
    the circle map dynamics, not interpolated.
""")


if __name__ == "__main__":
    main()
