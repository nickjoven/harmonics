"""
Substrate-mode evolution: 5-iteration extension of the 1D time loop.

Iterations:
  1. Continuous time   (RK4 instead of for loop)
  2. Mode coupling     (Kuramoto-style sin(phi_m - phi_n))
  3. Chirality flips   (Aut(Z_n) = Z_2 inversion events)
  4. CRT composites    (Z_6 = Z_2 x Z_3; Z_12 = Z_4 x Z_3 derived)
  5. Kibble-Zurek      (Z_2 defect pair nucleation on K crossings)

Pure Python; no numpy/scipy dependency.
"""

import math


# =========================================================================
# SUBSTRATE STRUCTURE
# =========================================================================

K_STAR   = 2 ** (-3.0 / 14.0)               # CHAIN_KSTAR.md
T_RELAX  = 10.0
T_TOTAL  = 30.0
DT       = 0.01

PRIMITIVE_MODES  = [2, 3, 4]                # Mihailescu primitives
COMPOSITE_MODES  = {6: (2, 3), 12: (4, 3)}  # CRT-derived
CHIRAL_MODES     = [3, 4]                   # Aut(Z_n) = Z_2 nontrivial

OMEGA = {n: 2 * math.pi / n for n in PRIMITIVE_MODES}

COUPLING = {                                # Kuramoto coupling on shared carriers
    (2, 3): 0.15, (3, 2): 0.15,             # Z_6 = Z_2 * Z_3
    (3, 4): 0.10, (4, 3): 0.10,             # Z_12 = Z_4 * Z_3
    (2, 4): 0.08, (4, 2): 0.08,             # r^2 of Z_4
}


# =========================================================================
# STATE LAYOUT
# State vector y = [K, phi_2, phi_3, phi_4, chi_3, chi_4]
# =========================================================================

IDX_K     = 0
IDX_PHASE = {n: 1 + i for i, n in enumerate(PRIMITIVE_MODES)}
IDX_CHIR  = {n: 1 + len(PRIMITIVE_MODES) + i for i, n in enumerate(CHIRAL_MODES)}
N_STATE   = 1 + len(PRIMITIVE_MODES) + len(CHIRAL_MODES)


# =========================================================================
# ITERATION 5 — Kibble-Zurek defect tracking
# =========================================================================
# Z_2 half-vortex pair nucleation when K crosses critical neighborhood.
# For Z_2 substrate (d=2, nu=1, z=1):  rho_defect ~ tau_quench^(-1)

K_CRITICAL_BAND = 0.05                      # critical neighborhood width
NU, Z, D        = 1.0, 1.0, 2.0             # KZ exponents for Z_2 substrate


class DefectLog:
    """Tracks Kibble-Zurek Z_2 half-vortex pair events."""

    def __init__(self):
        self.events = []                    # list of (t, count_added, tau_q)
        self.total  = 0
        self.prev_K = None
        self.prev_t = None

    def maybe_nucleate(self, t, K):
        """Spawn defects on critical-neighborhood crossing."""
        K_critical = K_STAR + K_CRITICAL_BAND
        if self.prev_K is not None:
            crossing = (self.prev_K > K_critical) and (K <= K_critical)
            if crossing:
                # local quench rate from finite-difference slope
                dK_dt = abs((K - self.prev_K) / (t - self.prev_t))
                tau_q = 1.0 / max(dK_dt, 1e-9)
                # KZ scaling: rho ~ tau_q^(-d*nu/(1+nu*z))
                exponent = -D * NU / (1.0 + NU * Z)
                n_pairs  = max(1, int(round(tau_q ** exponent)))
                self.total += 2 * n_pairs    # each pair = 2 quantized defects (+1/2, -1/2)
                self.events.append((t, 2 * n_pairs, tau_q))
        self.prev_K = K
        self.prev_t = t


# =========================================================================
# DYNAMICS — ITERATIONS 1, 2, 3, 4 COMBINED
# =========================================================================

def rhs(t, y):
    """RHS of the substrate ODE system."""
    K = y[IDX_K]
    phases = {n: y[IDX_PHASE[n]] for n in PRIMITIVE_MODES}
    chir   = {n: (y[IDX_CHIR[n]] if n in CHIRAL_MODES else 1.0)
              for n in PRIMITIVE_MODES}

    dy = [0.0] * N_STATE
    # K-iteration (1): K relaxes toward K_STAR
    dy[IDX_K] = (K_STAR - K) / T_RELAX

    # Phase dynamics (1) + coupling (2) + chirality modulation (3)
    for n in PRIMITIVE_MODES:
        dphi = chir[n] * OMEGA[n]
        for m in PRIMITIVE_MODES:
            if (n, m) in COUPLING:
                dphi += COUPLING[(n, m)] * math.sin(chir[m] * phases[m] -
                                                    chir[n] * phases[n])
        dy[IDX_PHASE[n]] = dphi

    # Chirality (3) is constant between events; dy[chir_*] = 0
    return dy


def rk4_step(t, y, dt):
    """Standard fourth-order Runge-Kutta step."""
    k1 = rhs(t,           y)
    k2 = rhs(t + dt/2,    [y[i] + dt/2 * k1[i] for i in range(N_STATE)])
    k3 = rhs(t + dt/2,    [y[i] + dt/2 * k2[i] for i in range(N_STATE)])
    k4 = rhs(t + dt,      [y[i] + dt   * k3[i] for i in range(N_STATE)])
    return [y[i] + dt/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])
            for i in range(N_STATE)]


# =========================================================================
# COMPOSITE-MODE QUERIES (ITERATION 4) — CRT-derived
# =========================================================================

def composite_state(y, n):
    """Return joint primitive-factor state for composite mode n."""
    if n in COMPOSITE_MODES:
        p, q = COMPOSITE_MODES[n]
        return {f: (y[IDX_PHASE[f]],
                    y[IDX_CHIR[f]] if f in CHIRAL_MODES else 1.0)
                for f in (p, q)}
    if n in PRIMITIVE_MODES:
        return {n: (y[IDX_PHASE[n]],
                    y[IDX_CHIR[n]] if n in CHIRAL_MODES else 1.0)}
    raise ValueError(f"Unknown mode order {n}")


# =========================================================================
# CHIRALITY-FLIP EVENT DETECTOR (ITERATION 3)
# =========================================================================

def chirality_event_triggered(y_prev, y_curr):
    """Detect half-twist phase upward crossing of pi (Aut(Z_n) = Z_2 trigger)."""
    phi_prev = y_prev[IDX_PHASE[2]] % (2 * math.pi)
    phi_curr = y_curr[IDX_PHASE[2]] % (2 * math.pi)
    return (phi_prev < math.pi) and (phi_curr >= math.pi)


# =========================================================================
# MAIN INTEGRATION LOOP
# =========================================================================

def main():
    # Initial conditions
    y = [0.0] * N_STATE
    y[IDX_K] = 1.0
    for n in CHIRAL_MODES:
        y[IDX_CHIR[n]] = +1.0                # generator (vs -1 = inverse)

    defect_log = DefectLog()
    chirality_flips = []

    t = 0.0
    n_steps = int(T_TOTAL / DT)

    # Sample snapshots for reporting
    snapshot_times = [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
    snapshots = []

    for step in range(n_steps):
        # RK4 step
        y_prev = y[:]
        y = rk4_step(t, y, DT)
        t += DT

        # Kibble-Zurek detection (5)
        defect_log.maybe_nucleate(t, y[IDX_K])

        # Chirality flip event (3)
        if chirality_event_triggered(y_prev, y):
            for n in CHIRAL_MODES:
                y[IDX_CHIR[n]] *= -1.0
            chirality_flips.append((t, [(n, y[IDX_CHIR[n]]) for n in CHIRAL_MODES]))

        # Snapshot capture
        for ts in snapshot_times:
            if abs(t - ts) < DT / 2:
                z6  = composite_state(y, 6)
                z12 = composite_state(y, 12)
                snapshots.append({
                    't':              t,
                    'K':              y[IDX_K],
                    'phases':         {n: y[IDX_PHASE[n]] for n in PRIMITIVE_MODES},
                    'chirality':      {n: y[IDX_CHIR[n]] for n in CHIRAL_MODES},
                    'Z6_state':       z6,
                    'Z12_state':      z12,
                    'defect_count':   defect_log.total,
                    'flip_count':     len(chirality_flips),
                })

    # =====================================================================
    # REPORT
    # =====================================================================

    print(f"Substrate evolution: T = 0 to {T_TOTAL}, dt = {DT}")
    print(f"K_STAR = {K_STAR:.6f}, critical band = {K_CRITICAL_BAND}")
    print("-" * 70)

    print(f"\n{'t':>6} {'K':>10} {'phi_2':>8} {'phi_3':>8} {'phi_4':>8}  "
          f"{'chi_3':>6} {'chi_4':>6}  {'defects':>8} {'flips':>6}")
    print("-" * 90)
    for s in snapshots:
        print(f"{s['t']:>6.2f} {s['K']:>10.6f} "
              f"{s['phases'][2]:>8.3f} {s['phases'][3]:>8.3f} {s['phases'][4]:>8.3f}  "
              f"{s['chirality'][3]:>+6.0f} {s['chirality'][4]:>+6.0f}  "
              f"{s['defect_count']:>8d} {s['flip_count']:>6d}")

    print(f"\nFinal K = {y[IDX_K]:.6f} (target K_STAR = {K_STAR:.6f})")
    print(f"Total chirality flips: {len(chirality_flips)}")
    print(f"Total defects created: {defect_log.total}")
    print(f"KZ events: {len(defect_log.events)}")

    if defect_log.events:
        print("\nKibble-Zurek events (Z_2 half-vortex pair nucleations):")
        for t_evt, n_def, tau_q in defect_log.events:
            print(f"  t = {t_evt:.3f}:  {n_def} defects spawned, tau_q = {tau_q:.4f}")

    if chirality_flips:
        print("\nChirality flips (Aut(Z_n) = Z_2 inversion events):")
        for t_flip, chiralities in chirality_flips[:8]:
            print(f"  t = {t_flip:.3f}:  {chiralities}")
        if len(chirality_flips) > 8:
            print(f"  ... ({len(chirality_flips) - 8} more)")

    print("\nCRT composite-mode queries at final t:")
    print(f"  Z_6 = Z_2 x Z_3 state:  {composite_state(y, 6)}")
    print(f"  Z_12 = Z_4 x Z_3 state: {composite_state(y, 12)}")


if __name__ == "__main__":
    main()
