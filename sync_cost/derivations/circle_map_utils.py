"""
Shared utilities for circle map computations.

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
