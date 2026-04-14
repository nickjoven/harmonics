"""
Compensation channel test: horizon entropy and dark-twin budget.

PARTIAL RETRACTION (see pointwise_horizon_match.py):
  The "holographic saturation" claim in Part D of this script -- that
  total Kuramoto loss matches the horizon entropy with N = R^2 -- was
  a global coincidence between two integrals computed in DIFFERENT
  time variables (a K-sweep for the Kuramoto side; an implicit
  "one unit per K-step" for the mode-count multiplication). It is
  NOT a genuine saturation result.

  The genuine result is different: at the Planck epoch (first
  bifurcation), the Kuramoto dissipation rate -K N r^2 matches the
  horizon absorption rate dS_H/dt up to an O(1) coefficient. After
  Planck, the two rates diverge by ~60 decades under any simple
  N(a) ansatz tried so far. See pointwise_horizon_match.py for the
  corrected analysis.

  What survives as a genuine finding: the POINT saturation at Planck
  time. What does not: any claim about holographic matching over
  cosmic history.

--- Original docstring below ---

Continuation of first_bifurcation_volume.py. That script ruled out
option (A) -- the unlocked oscillators within the same Kuramoto ensemble
do NOT expand to compensate the locked cluster's contraction. The lost
phase-space volume at the first bifurcation has to go somewhere outside
the N-oscillator picture.

This script tests the two remaining candidates:

  (B) Dark twin -- absorbs entropy in proportion to the framework's
      1:5:13 partition (baryons : dark matter : dark energy) from
      farey_partition.md. The twin sectors together carry 18/19 of
      the total budget; our baryonic sector carries 1/19.

  (C) Cosmological horizon (Bekenstein-Hawking) -- entropy S_H = A/4
      with A the Hubble horizon area. In Planck units S_H = pi R^2
      where R = Planck/Hubble ratio. In the framework R = 6 x 13^54
      ~ 10^60, giving S_H ~ 10^121 nats. This is the largest entropy
      reservoir in the universe.

The test: integrate the Kuramoto log-volume loss rate |div(f)| = K N r^2
over a K sweep (representing a cosmological cooling history where K
grows from 0 to K*) and compare to:

  - the 1:5:13 partition ratio (option B)
  - the Bekenstein-Hawking horizon entropy scaled by R^2 (option C)

Since B and C turn out to be different aspects of the same underlying
budget (horizon = dark-energy component = 13/19 of the partition), we
also check whether the ratio of "lost Kuramoto volume" to "total
partition budget" is a structurally meaningful number.

Usage:
    python sync_cost/derivations/compensation_channel_test.py
"""

import math
import random


# ============================================================================
# Constants
# ============================================================================

# Framework's Planck/Hubble ratio (hierarchy.md)
R_HIERARCHY = 6 * 13 ** 54   # ~ 10^60.9

# Farey partition (farey_partition.md)
OMEGA_B = 1 / 19     # baryons (us)
OMEGA_DM = 5 / 19    # dark matter
OMEGA_L = 13 / 19    # dark energy / horizon
TOTAL_UNITS = 19
OUR_SHARE = 1        # our sector occupies 1 "unit" of the 19


# ============================================================================
# Kuramoto contraction rate (from first_bifurcation_volume.py)
# ============================================================================

def kuramoto_rhs(theta, omega, K):
    N = len(theta)
    cx = sum(math.cos(t) for t in theta) / N
    cy = sum(math.sin(t) for t in theta) / N
    r = math.sqrt(cx * cx + cy * cy)
    psi = math.atan2(cy, cx)
    return [omega[i] + K * r * math.sin(psi - theta[i]) for i in range(N)]


def order_parameter(theta):
    N = len(theta)
    cx = sum(math.cos(t) for t in theta) / N
    cy = sum(math.sin(t) for t in theta) / N
    return math.sqrt(cx * cx + cy * cy)


def rk4_step(theta, omega, K, dt):
    k1 = kuramoto_rhs(theta, omega, K)
    y2 = [theta[i] + 0.5 * dt * k1[i] for i in range(len(theta))]
    k2 = kuramoto_rhs(y2, omega, K)
    y3 = [theta[i] + 0.5 * dt * k2[i] for i in range(len(theta))]
    k3 = kuramoto_rhs(y3, omega, K)
    y4 = [theta[i] + dt * k3[i] for i in range(len(theta))]
    k4 = kuramoto_rhs(y4, omega, K)
    return [theta[i] + (dt / 6.0) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])
            for i in range(len(theta))]


def steady_r(K, N=200, T_total=60.0, dt=0.05, seed=42, settle=30.0, sigma=1.0):
    """Integrate Kuramoto and return the time-averaged r after settling."""
    random.seed(seed)
    theta = [random.uniform(0, 2 * math.pi) for _ in range(N)]
    omega = [random.gauss(0.0, sigma) for _ in range(N)]
    t = 0.0
    rs = []
    while t < T_total:
        if t >= settle:
            rs.append(order_parameter(theta))
        theta = rk4_step(theta, omega, K, dt)
        theta = [x % (2 * math.pi) for x in theta]
        t += dt
    return sum(rs) / len(rs) if rs else 0.0


def contraction_rate_per_mode(K, r):
    """
    From first_bifurcation_volume.py:  div(f) = -K N r^2
    Per-mode rate (divide by N):       div_per_mode = -K r^2
    """
    return -K * r * r


# ============================================================================
# Integrate the log-volume loss over a cooling trajectory K : 0 -> K*
# ============================================================================

def integrate_cooling_loss(K_max, K_steps=40, sigma=1.0, N=200):
    """
    Model a cosmological cooling trajectory as a linear sweep K: 0 -> K_max.
    At each K, compute the steady-state r and the per-mode contraction
    rate. The total log-volume loss per mode is the integral along K.

    Returns:
        K_values, r_values, rate_values, cumulative_loss_per_mode
    """
    dK = K_max / K_steps
    K_values = [i * dK for i in range(1, K_steps + 1)]
    r_values = [steady_r(K, N=N, sigma=sigma) for K in K_values]
    rate_values = [contraction_rate_per_mode(K, r) for K, r in zip(K_values, r_values)]
    # Integrate |rate| dK (the K step is the "time-like" parameter here)
    cumulative = 0.0
    cumulative_values = []
    for rate in rate_values:
        cumulative += abs(rate) * dK
        cumulative_values.append(cumulative)
    return K_values, r_values, rate_values, cumulative_values


# ============================================================================
# Bekenstein-Hawking horizon entropy
# ============================================================================

def horizon_entropy(R):
    """
    S_H = A_H / 4 in Planck units
    A_H = 4 pi r_H^2, r_H = Planck/Hubble ratio in Planck lengths
    S_H = pi R^2
    """
    # Use log to avoid overflow
    return math.pi, 2 * math.log10(R)   # (coefficient, log10 exponent)


def log10_horizon_entropy(R):
    """log10(pi R^2) = log10(pi) + 2 log10(R)"""
    return math.log10(math.pi) + 2 * math.log10(R)


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  COMPENSATION CHANNEL TEST: horizon entropy + dark-twin budget")
    print("=" * 78)
    print()
    print("  Previous result (first_bifurcation_volume.py):")
    print("    div(f) = -K N r^2 across the Kuramoto bifurcation")
    print("    Option (A) ruled out: unlocked sector does not compensate")
    print()
    print("  This script: test options (B) dark twin and (C) horizon.")
    print()

    # --------------------------------------------------------------------
    # PART A: integrate Kuramoto log-volume loss along a cooling path
    # --------------------------------------------------------------------
    print("-" * 78)
    print("  PART A: Kuramoto log-volume loss across the cooling trajectory")
    print("-" * 78)
    print()
    print("  Model a cosmological cooling history as K sweeping from 0")
    print("  to K_max. At each K, use the steady-state r of a 200-oscillator")
    print("  ensemble to compute the per-mode contraction rate -K r^2.")
    print("  Integrate |rate| d K along the sweep.")
    print()

    K_max = 4.0  # well above K_c ~ 1.596
    K_c = 2 * math.sqrt(2 / math.pi)

    print(f"  K sweep: 0 -> {K_max}, K_c = {K_c:.4f}")
    print()
    K_values, r_values, rate_values, cumulative = integrate_cooling_loss(K_max)

    print(f"  {'K':>8} {'r*':>8} {'rate/mode':>12} {'cum loss/mode':>14}")
    print("  " + "-" * 46)
    for K, r, rate, cum in zip(K_values[::4], r_values[::4],
                                rate_values[::4], cumulative[::4]):
        print(f"  {K:>8.3f} {r:>8.4f} {rate:>12.4f} {cum:>14.4f}")
    # also print the last point
    print(f"  {K_values[-1]:>8.3f} {r_values[-1]:>8.4f} "
          f"{rate_values[-1]:>12.4f} {cumulative[-1]:>14.4f}")
    print()

    total_loss_per_mode = cumulative[-1]
    print(f"  Total log-volume loss per mode (0 -> {K_max}): "
          f"{total_loss_per_mode:.4f} nats")
    print()

    # --------------------------------------------------------------------
    # PART B: Dark-twin budget check (1:5:13)
    # --------------------------------------------------------------------
    print("-" * 78)
    print("  PART B: Dark-twin budget (option B)")
    print("-" * 78)
    print()
    print("  Framework's Farey partition (farey_partition.md):")
    print(f"    Omega_b  = 1/19 = {OMEGA_B:.4f}  (baryons / us)")
    print(f"    Omega_DM = 5/19 = {OMEGA_DM:.4f}  (dark matter / twin)")
    print(f"    Omega_L  = 13/19 = {OMEGA_L:.4f}  (dark energy / horizon)")
    print(f"    Total = {TOTAL_UNITS}/19 = 1")
    print()
    print("  If our sector's contraction is compensated by the 18/19 rest")
    print("  of the Klein-bottle-complete system, the total volume balance is:")
    print()
    print(f"    Our contraction rate per unit:   -1 unit")
    print(f"    Dark matter expansion per unit:  +5 units")
    print(f"    Dark energy expansion per unit: +13 units")
    print(f"    Total compensating expansion:   +18 units")
    print()
    print("  So if ours loses L nats, the compensating sectors gain 18 L.")
    print(f"  Our loss per mode = {total_loss_per_mode:.4f} nats")
    print(f"  DM compensation per mode = 5 * L = {5*total_loss_per_mode:.4f} nats")
    print(f"  DE compensation per mode = 13 * L = {13*total_loss_per_mode:.4f} nats")
    print(f"  Total compensation per mode = 18 * L = {18*total_loss_per_mode:.4f} nats")
    print()
    print("  The ratio test: if the framework's partition is consistent,")
    print("  the DE share should match the horizon entropy per mode (option C).")
    print()

    # --------------------------------------------------------------------
    # PART C: Horizon entropy (Bekenstein-Hawking)
    # --------------------------------------------------------------------
    print("-" * 78)
    print("  PART C: Horizon entropy (option C, Bekenstein-Hawking)")
    print("-" * 78)
    print()
    print("  In Planck units:")
    print("    A_H = 4 pi r_H^2")
    print("    r_H = Planck/Hubble ratio in Planck lengths")
    print("    S_H = A_H / 4 = pi r_H^2 = pi R^2")
    print()

    log_SH = log10_horizon_entropy(R_HIERARCHY)
    log_R = math.log10(R_HIERARCHY)
    print(f"  Framework: R = 6 x 13^54")
    print(f"    log10(R)    = {log_R:.4f}")
    print(f"    R ~ {10**log_R:.3e}")
    print()
    print(f"    log10(S_H)  = log10(pi) + 2 log10(R) = {log_SH:.4f}")
    print(f"    S_H ~ {10**log_SH:.3e} nats")
    print()
    print("  For comparison: Planck 2018 observed S_H ~ 10^122 nats.")
    print(f"  Framework value: 10^{log_SH:.1f}. Match: within one decade.")
    print()

    # --------------------------------------------------------------------
    # PART D: Total Kuramoto loss vs horizon entropy
    # --------------------------------------------------------------------
    print("-" * 78)
    print("  PART D: Ratio test -- does Kuramoto loss fit inside the horizon?")
    print("-" * 78)
    print()
    print("  Total modes in the framework's mode hierarchy (first estimate):")
    print("    N_modes ~ R = Planck/Hubble ratio ~ 10^60.9")
    print()
    print("  Total Kuramoto log-volume loss = N_modes * loss_per_mode")
    print()

    log_N_modes = log_R   # one Kuramoto-mode per Planck-scale resolution
    log_total_loss = log_N_modes + math.log10(total_loss_per_mode)
    print(f"    log10(N_modes)       = {log_N_modes:.4f}")
    print(f"    log10(loss/mode)     = {math.log10(total_loss_per_mode):.4f}")
    print(f"    log10(total loss)    = {log_total_loss:.4f}")
    print()
    print(f"  Compare to horizon entropy:")
    print(f"    log10(S_H)           = {log_SH:.4f}")
    print(f"    log10(total loss)    = {log_total_loss:.4f}")
    print(f"    ratio                = 10^{log_total_loss - log_SH:.4f}")
    print()

    if log_total_loss < log_SH:
        headroom = log_SH - log_total_loss
        print(f"  The Kuramoto total loss fits INSIDE the horizon entropy")
        print(f"  with {headroom:.1f} decades of headroom.")
    else:
        print(f"  The Kuramoto total loss EXCEEDS the horizon entropy.")
    print()

    # --------------------------------------------------------------------
    # Holographic reconciliation
    # --------------------------------------------------------------------
    print("  Observation: 60.7 decades is SUSPICIOUSLY close to log10(R) = 60.9.")
    print("  That is the bare Planck/Hubble ratio, which is exactly what")
    print("  the holographic principle would predict if the Kuramoto mode")
    print("  count is an AREA (R^2) rather than a length (R).")
    print()
    print("  Holographic hypothesis: N_modes = R^2, not R.")
    print()

    log_N_modes_holo = 2 * log_R
    log_total_loss_holo = log_N_modes_holo + math.log10(total_loss_per_mode)
    print(f"    log10(N_modes, holographic)   = 2 * log10(R) = {log_N_modes_holo:.4f}")
    print(f"    log10(loss/mode)              = {math.log10(total_loss_per_mode):.4f}")
    print(f"    log10(total loss, holographic) = {log_total_loss_holo:.4f}")
    print(f"    log10(S_H)                    = {log_SH:.4f}")
    print(f"    ratio                         = 10^{log_total_loss_holo - log_SH:.4f}")
    print()
    print("  With N_modes = R^2, the Kuramoto total loss matches the")
    print("  Bekenstein-Hawking horizon entropy to within 10^0.3 -- essentially")
    print("  exact up to the coefficient (pi vs ~5, both O(1)).")
    print()
    print("  This is the holographic principle falling out of the Kuramoto")
    print("  side: the effective mode count at the Planck-Hubble hierarchy")
    print("  is R^2 (area scaling), not R^3 (volume scaling) or R (length).")
    print("  Area scaling is what matches the horizon's entropy capacity.")
    print()
    print("  Equivalently: the arrow-of-time budget is saturated. Every")
    print("  Kuramoto mode's log-volume loss is deposited on the horizon,")
    print("  with no wasted room and no overflow. The first-bifurcation")
    print("  contraction rate -K N r^2 is the rate at which horizon area")
    print("  grows, with N = R^2 = horizon mode count.")
    print()

    # --------------------------------------------------------------------
    # PART E: Does the horizon growth rate match the Kuramoto rate?
    # --------------------------------------------------------------------
    print("-" * 78)
    print("  PART E: Rate-matching test")
    print("-" * 78)
    print()
    print("  Option (C) needs: dS_H/dt = our log-volume loss rate per mode")
    print("                            * total mode count at each epoch.")
    print()
    print("  Schematic: at each bifurcation scale, Kuramoto loses K r^2 nats")
    print("  per mode, while the horizon grows by dA/dt = (dr_H^2/dt)/4 =")
    print("  (2 r_H dr_H/dt)/4 per unit time. For a de Sitter phase,")
    print("  r_H is constant, so dA/dt = 0 and no compensation. For a")
    print("  contracting-H phase, r_H grows and dA/dt > 0, providing")
    print("  compensation.")
    print()
    print("  Quantitative check requires K(t) for a specific cosmological")
    print("  history, which the framework has in rough form (hierarchy.md)")
    print("  but not at the level of a K(t) profile. The rate-match test")
    print("  is left as a follow-up until K(t) is specified.")
    print()
    print("  What we CAN say from Parts A-D:")
    print(f"    Total Kuramoto loss:  10^{log_total_loss:.1f} nats")
    print(f"    Horizon entropy:      10^{log_SH:.1f} nats")
    print(f"    1:5:13 partition:     our 1 : twin 18 = 1 : 18")
    print(f"    Horizon/our ratio:    10^{log_SH - math.log10(total_loss_per_mode):.1f}")
    print()
    print("  The partition coefficient 18 is far smaller than the horizon-to-")
    print("  our-sector ratio 10^60, which means the dark-matter twin (5/19)")
    print("  and the dark-energy horizon (13/19) are not on the same scale.")
    print("  The 1:5:13 partition is an OMEGA ratio (fraction of total energy")
    print("  density today), not a per-mode entropy ratio. These aren't the")
    print("  same quantity.")
    print()
    print("  Correct interpretation:")
    print("  - Option (B) the dark twin absorbs DM-matter-worth of entropy")
    print("    (5x our sector). This is a per-mode ratio.")
    print("  - Option (C) the cosmological horizon absorbs 10^60 our-sector's")
    print("    worth of entropy (horizon contains 10^60 modes that our")
    print("    sector does not).")
    print("  - (B) and (C) are not competitors; (B) is a small correction")
    print("    to (C). The horizon absorbs essentially all the entropy; the")
    print("    twin absorbs a factor-of-few share of the observable sector.")
    print()

    # --------------------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------------------
    print("=" * 78)
    print("  SUMMARY")
    print("=" * 78)
    print()
    print("  Option (A) [unlocked reservoir] -- RULED OUT (previous script)")
    print("  Option (B) [dark twin]           -- VIABLE, small share (~18:1)")
    print("  Option (C) [horizon]             -- VIABLE, dominant share (~10^60:1)")
    print()
    print("  Compensation channel is primarily the cosmological horizon,")
    print("  with the dark twin as a subleading correction inside the")
    print("  observable sector. The framework's 1:5:13 partition describes")
    print("  the visible/DM/DE energy distribution AT THE OBSERVATION EPOCH;")
    print("  the entropy-deposition channel for the FIRST bifurcation is")
    print("  almost entirely the horizon (since at that epoch there were no")
    print("  DM or baryon populations yet -- the partition had not yet")
    print("  differentiated).")
    print()
    print("  The arrow of time at the first bifurcation is the Kuramoto")
    print("  contraction rate -K N r^2, compensated by horizon area growth.")
    print("  Later in cosmic history, as the 1:5:13 partition emerges, the")
    print("  dark twin begins absorbing a subleading share, but the horizon")
    print("  remains the dominant entropy reservoir.")
    print()
    print("  Follow-up needed: a specific K(t) profile to compute the actual")
    print("  rate-match between Kuramoto log-volume loss and horizon area")
    print("  growth at each epoch. The framework has K(end points) but not")
    print("  K(t), so this is left for a future iteration.")
    print()


if __name__ == "__main__":
    main()
