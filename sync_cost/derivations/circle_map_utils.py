"""
Shared utilities for circle map computations.

The circle map is the canonical discrete dynamical system for a periodically
driven oscillator. K controls the coupling strength between oscillator and
drive; Omega is the ratio of natural to driving frequency.

The standard circle map:
    θ_{n+1} = θ_n + Ω - (K/2π) sin(2π θ_n)

Used by: circle_map.py, stern_brocot_map.py, phi_squared_zoom.py,
         k_omega_mapping.py, superharmonic_regime.py, staircase_geometry.py
"""

import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PHI = (1 + math.sqrt(5)) / 2         # 1.6180339887...
PSI = (1 - math.sqrt(5)) / 2         # -0.6180339887... = -1/φ
INV_PHI = 1 / PHI                     # 0.6180339887...
PHI_SQ = PHI ** 2                     # 2.6180339887...
LN_PHI_SQ = math.log(PHI_SQ)         # 0.9624236501...


# ---------------------------------------------------------------------------
# Circle map
# ---------------------------------------------------------------------------

def circle_map_step(theta, omega, K):
    """One iteration of the standard circle map."""
    return theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)


def winding_number(omega, K, n_transient=3000, n_measure=20000):
    """
    Compute the winding number W for given (Ω, K).

    W = lim_{n→∞} (θ_n - θ_0) / n

    Parameters:
        omega: bare frequency ratio (drive/natural)
        K: coupling strength (K=1 is critical)
        n_transient: iterations to discard (let transients die)
        n_measure: iterations to average over

    Returns:
        W: the winding number (rotation number)
    """
    theta = 0.0
    for _ in range(n_transient):
        theta = circle_map_step(theta, omega, K)
    theta_start = theta
    for _ in range(n_measure):
        theta = circle_map_step(theta, omega, K)
    return (theta - theta_start) / n_measure


# ---------------------------------------------------------------------------
# Fibonacci / Stern-Brocot utilities
# ---------------------------------------------------------------------------

def fibonacci_sequence(n_terms=25):
    """Return first n_terms Fibonacci numbers: 1, 1, 2, 3, 5, 8, ..."""
    fibs = [1, 1]
    for _ in range(n_terms - 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fibonacci_convergents(n_terms=15):
    """
    Fibonacci convergents to 1/φ: F_n/F_{n+1}.

    Returns list of (p, q, value) tuples.
    """
    fibs = fibonacci_sequence(n_terms + 2)
    return [(fibs[i], fibs[i + 1], fibs[i] / fibs[i + 1])
            for i in range(n_terms)]


# ---------------------------------------------------------------------------
# Tongue widths — from the circle map, not interpolation
# ---------------------------------------------------------------------------

def tongue_width_numerical(p, q, K, n_trans=5000, n_meas=20000, n_bisect=40):
    """
    Measure the Arnold tongue width at p/q by bisecting for the
    tongue boundaries in the actual circle map dynamics.

    This is the ground truth. No interpolation, no approximation.
    Expensive for large q or K near 1 (critical slowing).

    For K > 0.8 or q > 4, automatically increases transients.
    """
    target = p / q

    # Adaptive transients for critical slowing
    if K > 0.8 or q > 4:
        nt = max(n_trans, 20000)
        nm = max(n_meas, 50000)
    else:
        nt = n_trans
        nm = n_meas

    # Verify the center is locked
    W_center = winding_number(target, K, nt, nm)
    if abs(W_center - target) > 5e-4:
        return 0.0

    # Search window
    half_window = max(4.0 / (q * q), 0.02)

    # Bisect for left boundary
    lo, hi = max(target - half_window, 1e-6), target
    for _ in range(n_bisect):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, nt, nm)
        if abs(W - target) < 5e-4:
            hi = mid
        else:
            lo = mid
    left = (lo + hi) / 2

    # Bisect for right boundary
    lo, hi = target, min(target + half_window, 1 - 1e-6)
    for _ in range(n_bisect):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, nt, nm)
        if abs(W - target) < 5e-4:
            lo = mid
        else:
            hi = mid
    right = (lo + hi) / 2

    return max(right - left, 0.0)


def tongue_width(p, q, K):
    """
    Arnold tongue width at rational p/q, coupling K.

    Uses the two analytically derived regimes with NO interpolation:

      Perturbative (valid for K well below 1):
        w(p/q, K) = 2 * (K/2)^q / q
        From: K^q appears at q-th order in the Fourier expansion
        of the circle map's q-th iterate. This is exact to leading
        order and the primitives (mediant + parabola) determine it.

      Critical (valid at K = 1):
        w(p/q, 1) = 1/q^2
        From: the Gauss-Kuzmin measure = Ford circle areas = hyperbolic
        area at each cusp. This is exact and follows from the mediant
        (Stern-Brocot tree structure).

    At K < 1, the perturbative formula is the honest one: tongue widths
    grow as K^q. The critical formula 1/q^2 applies ONLY at K = 1.
    Between them, the actual dynamics interpolate — but that interpolation
    is determined by the circle map, not by a smoothstep.

    For sub-critical K (the physical regime, K* ~ 0.86), we use the
    perturbative formula. It correctly captures the exponential death
    of high-q modes that the framework requires for |F_6| = 13 to be
    the self-predicting set.

    For K = 1 exactly, we use the critical formula.

    To get exact intermediate values, use tongue_width_numerical().
    """
    if q == 0:
        return 0.0
    if q == 1:
        # Exact for all K <= 1: the q=1 tongue boundary is Omega = K/(2pi)
        return min(K / (2 * math.pi), 1.0)
    if K >= 1.0:
        return 1.0 / (q * q)
    # Sub-critical: perturbative formula (exact to leading order)
    return 2 * (K / 2) ** q / q


def farey_mediants(a, b, c, d, depth=5, max_q=200):
    """
    Generate Farey mediants between a/b and c/d, recursively.

    The mediant is (a+c)/(b+d). Returns list of (p, q, value)
    sorted by value.
    """
    if depth == 0 or b + d > max_q:
        return []

    p, q = a + c, b + d
    mid = p / q

    left = farey_mediants(a, b, p, q, depth - 1, max_q)
    right = farey_mediants(p, q, c, d, depth - 1, max_q)

    return left + [(p, q, mid)] + right
