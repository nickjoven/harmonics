"""
D21-E v3: Self-consistent r with UNREDUCED twist.

The key insight from the explore agent: the order parameter twist
(-1)^q uses the REDUCED denominator. For fiber representatives,
Fraction(3,9).denominator = 3, so the twist is (-1)^3 = -1.
But the UNREDUCED denominator is 9, giving (-1)^9 = -1 (same).

However: Fraction(2,6).denominator = 3, twist = (-1)^3 = -1.
But unreduced: (-1)^6 = +1. DIFFERENT.

Scaling by k=2: kq = 2q. (-1)^{2q} = +1 always. TWIST KILLED.
Scaling by k=3: kq = 3q. (-1)^{3q} = (-1)^q. TWIST PRESERVED.

This asymmetry between k=2 and k=3 in the twist is the
non-commutativity of scaling with the Klein bottle topology.
It should produce non-trivial fiber dynamics when r is
self-consistent.
"""

import sys
import math
import numpy as np
from fractions import Fraction
from math import gcd

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from circle_map_utils import INV_PHI


def tongue_width_unreduced(p, q, K):
    if q == 0:
        return 0.0
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    return 2 * (K / 2) ** q / q


# ============================================================
# Extended mode space with UNREDUCED denominators
# ============================================================

BASE_MODES = [
    (1, 3, 1, 2),   # (p1, q1, p2, q2) — base mode 0
    (1, 2, 1, 3),   # base mode 1
    (1, 2, 2, 3),   # base mode 2
    (2, 3, 1, 2),   # base mode 3
]

def build_modes(max_k=3):
    modes = []
    for base_idx, (p1, q1, p2, q2) in enumerate(BASE_MODES):
        for k1 in range(1, max_k + 1):
            for k2 in range(1, max_k + 1):
                kp1, kq1 = k1 * p1, k1 * q1
                kp2, kq2 = k2 * p2, k2 * q2
                xor_ok = (kq1 + kq2) % 2 == 1
                if xor_ok:
                    # Twist sign on UNREDUCED denominator
                    twist_sign = (-1) ** kq1
                    modes.append({
                        'base_idx': base_idx,
                        'p1': kp1, 'q1': kq1,
                        'p2': kp2, 'q2': kq2,
                        'k1': k1, 'k2': k2,
                        'f1': kp1 / kq1,
                        'f2': kp2 / kq2,
                        'phase': 2 * math.pi * (kp1/kq1 + kp2/kq2),
                        'twist': twist_sign,
                        'twist_reduced': (-1) ** (q1),  # for comparison
                    })
    return modes


# ============================================================
# Show the twist asymmetry
# ============================================================

print("=" * 70)
print("  TWIST SIGN: REDUCED vs UNREDUCED")
print("=" * 70)

modes = build_modes(max_k=4)
print(f"\n  {'mode':>20s}  {'k':>6s}  {'kq1':>4s}  {'twist_unred':>12s}  {'twist_red':>10s}  {'DIFFER?':>8s}")
for m in modes:
    p1, q1 = BASE_MODES[m['base_idx']][:2]
    differ = "***" if m['twist'] != m['twist_reduced'] else ""
    print(f"  ({m['p1']}/{m['q1']},{m['p2']}/{m['q2']})"
          f"  ({m['k1']},{m['k2']})"
          f"  {m['q1']:4d}"
          f"  {m['twist']:12d}"
          f"  {m['twist_reduced']:10d}"
          f"  {differ:>8s}")


# ============================================================
# Self-consistent field equation with unreduced twist
# ============================================================

def compute_r(pops, modes, use_unreduced_twist=True):
    """Order parameter with choice of twist convention."""
    total = np.sum(pops)
    if total == 0:
        return 0j
    r = 0j
    for i, m in enumerate(modes):
        twist = m['twist'] if use_unreduced_twist else m['twist_reduced']
        r += pops[i] * twist * (math.cos(m['phase']) + 1j * math.sin(m['phase']))
    return r / total


def field_step(pops, modes, g_func, K0, use_unreduced_twist=True):
    """One step of self-consistent field equation."""
    r = compute_r(pops, modes, use_unreduced_twist)
    K_eff = K0 * max(abs(r), 1e-15)

    raw = np.zeros(len(modes))
    for i, m in enumerate(modes):
        g = g_func(m['f1'], m['f2'])
        w1 = tongue_width_unreduced(m['p1'], m['q1'], K_eff)
        w2 = tongue_width_unreduced(m['p2'], m['q2'], K_eff)
        raw[i] = g * w1 * w2

    total_pop = np.sum(pops)
    Z = np.sum(raw)
    if Z > 0:
        raw *= total_pop / Z
    return raw, r


def solve(modes, g_func, K0, use_unreduced_twist=True,
          n_iter=3000, damping=0.1):
    n = len(modes)
    pops = np.ones(n)
    r_history = []
    for it in range(n_iter):
        new_pops, r = field_step(pops, modes, g_func, K0, use_unreduced_twist)
        pops = (1 - damping) * pops + damping * new_pops
        r_history.append(r)
    return pops, r_history


def jacobian_sc(pops, modes, g_func, K0, use_unreduced_twist, eps=1e-7):
    """Jacobian of SELF-CONSISTENT field equation (r computed from pops)."""
    n = len(pops)
    J = np.zeros((n, n))
    for j in range(n):
        pp, pm = pops.copy(), pops.copy()
        pp[j] += eps
        pm[j] -= eps
        fp, _ = field_step(pp, modes, g_func, K0, use_unreduced_twist)
        fm, _ = field_step(pm, modes, g_func, K0, use_unreduced_twist)
        J[:, j] = (fp - fm) / (2 * eps)
    return J


# ============================================================
# Compare reduced vs unreduced twist
# ============================================================

g_golden = lambda f1, f2: math.exp(-5 * ((f1 - INV_PHI)**2 + (f2 - INV_PHI)**2))

for max_k in [3]:
    modes = build_modes(max_k)
    n = len(modes)
    n_base = 4

    P = np.zeros((n_base, n))
    for j, m in enumerate(modes):
        P[m['base_idx'], j] = 1.0
    gauge_dof = n - np.linalg.matrix_rank(P)

    for twist_label, use_unred in [("REDUCED", False), ("UNREDUCED", True)]:
        print(f"\n{'=' * 70}")
        print(f"  SELF-CONSISTENT r — {twist_label} TWIST  (max_k={max_k}, {n} modes)")
        print(f"{'=' * 70}")

        pops, r_hist = solve(modes, g_golden, K0=1.0,
                             use_unreduced_twist=use_unred)
        r_final = r_hist[-1]
        total = np.sum(pops)

        print(f"\n  |r| = {abs(r_final):.8f},  arg(r)/π = {math.atan2(r_final.imag, r_final.real)/math.pi:.6f}")

        # Base populations
        base_pops = np.zeros(n_base)
        for j, m in enumerate(modes):
            base_pops[m['base_idx']] += pops[j]
        print(f"\n  Base populations:")
        for i, (p1, q1, p2, q2) in enumerate(BASE_MODES):
            print(f"    ({p1}/{q1},{p2}/{q2}): {base_pops[i]/total:.6f}")

        # Fiber asymmetry
        print(f"\n  Fiber distribution (top modes per base):")
        for base_idx in range(n_base):
            p1, q1, p2, q2 = BASE_MODES[base_idx]
            fiber = [(j, m, pops[j]) for j, m in enumerate(modes)
                     if m['base_idx'] == base_idx and pops[j] / total > 1e-8]
            fiber.sort(key=lambda x: -x[2])
            for j, m, p in fiber[:4]:
                twist_s = "+" if m['twist'] > 0 else "-"
                print(f"      k=({m['k1']},{m['k2']}) twist={twist_s}: "
                      f"{p/total:.8f}")

        # Jacobian
        J = jacobian_sc(pops, modes, g_golden, K0=1.0,
                        use_unreduced_twist=use_unred)
        rank_J = np.linalg.matrix_rank(J, tol=1e-6)
        eigvals = sorted(np.linalg.eigvals(J), key=lambda x: -abs(x))

        print(f"\n  Jacobian rank: {rank_J}")
        for i in range(min(8, n)):
            ev = eigvals[i]
            if abs(ev) > 1e-10:
                print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  "
                      f"|λ|={abs(ev):.8f}")

        # Fiber Jacobian
        U, s, Vt = np.linalg.svd(P)
        kr = n - np.linalg.matrix_rank(P)
        if kr > 0:
            KB = Vt[-kr:, :]
            J_fiber = KB @ J @ KB.T
            ev_fiber = sorted(np.linalg.eigvals(J_fiber), key=lambda x: -abs(x))
            sig_fiber = sum(1 for ev in ev_fiber if abs(ev) > 1e-6)

            print(f"\n  Fiber Jacobian: {kr}×{kr}")
            print(f"  Significant eigenvalues: {sig_fiber}")
            for i in range(min(6, kr)):
                ev = ev_fiber[i]
                if abs(ev) > 1e-10:
                    print(f"    λ_{i}: {ev.real:12.8f} + {ev.imag:12.8f}i  "
                          f"|λ|={abs(ev):.8f}")

            if sig_fiber > 0:
                J_f0 = J_fiber - (np.trace(J_fiber)/kr) * np.eye(kr)
                basis = [J_f0, J_f0.T]
                comm = J_f0 @ J_f0.T - J_f0.T @ J_f0
                basis.append(comm)
                for b in [J_f0, J_f0.T]:
                    basis.append(b @ comm - comm @ b)
                flat = np.vstack([m.flatten() for m in basis])
                lie_dim = np.linalg.matrix_rank(flat, tol=1e-4)
                print(f"\n  Lie algebra dim: {lie_dim}")
                print(f"  (su(2)=3, su(3)=8, su(2)⊕su(3)=11)")
            else:
                print(f"\n  Fiber is flat (no significant eigenvalues)")

        # Key comparison: does the unreduced twist DIFFER from reduced?
        if twist_label == "UNREDUCED":
            # Count modes where twist differs
            n_differ = sum(1 for m in modes if m['twist'] != m['twist_reduced'])
            print(f"\n  Modes where twist differs: {n_differ} of {n}")
            print(f"  (These are the fiber modes where k=even flips the sign)")

print(f"\n{'=' * 70}")
print("  DONE")
print(f"{'=' * 70}")
