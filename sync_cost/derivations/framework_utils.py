"""
Framework utility functions -- Fibonacci, Farey, structural readings.

Shared helpers that were previously redefined in 30-40 scripts each.
Import from here instead of redefining.

Contents
--------
    fib(k)                   -- kth Fibonacci number (F_1 = F_2 = 1)
    fib_sequence(k_max)      -- list of F_1 .. F_{k_max}
    farey(n)                 -- Farey sequence of order n
    farey_count(n)           -- |F_n| via Euler totient sum
    euler_phi(n)              -- Euler totient function
    structural_reading(N)    -- string of (q_2, q_3, F_k) factorizations
    scan_fibonacci_squares(target, ...)  -- find best (p, F_k) with p/F_k^2 ~ target
    scan_integer_denoms(target, ...)     -- find best 1/N with 1/N ~ target
    tongue_width(p, q, K)    -- Arnold tongue width (perturbative form)
    duty_cycle(q, d=3)       -- duty(q) = 1/q^d
"""

import math

from framework_constants import (
    F_6_COUNT,
    F_7_COUNT,
    FRAMEWORK_INTEGERS,
    INTERACT,
    K_LEPTON,
    K_QUARK,
    MEDIANT,
    Q2,
    Q3,
)

# ============================================================================
# Fibonacci
# ============================================================================

def fib(k: int) -> int:
    """
    Kth Fibonacci number, with F_1 = F_2 = 1.

    Convention: fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, ...
    """
    if k < 1:
        raise ValueError(f"Fibonacci index must be >= 1, got {k}")
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


def fib_sequence(k_max: int) -> list[int]:
    """List [F_1, F_2, ..., F_{k_max}]."""
    return [fib(k) for k in range(1, k_max + 1)]


# ============================================================================
# Euler totient and Farey sequences
# ============================================================================

def euler_phi(n: int) -> int:
    """Euler's totient function phi(n), the count of integers in [1, n]
    coprime to n."""
    if n < 1:
        return 0
    result = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1
    if m > 1:
        result -= result // m
    return result


def farey_count(n: int) -> int:
    """
    |F_n| = 1 + sum_{k=1}^{n} phi(k), the number of reduced fractions
    p/q with 0 <= p/q <= 1 and q <= n.
    """
    return 1 + sum(euler_phi(k) for k in range(1, n + 1))


def farey(n: int) -> list[tuple[int, int]]:
    """
    Farey sequence of order n as a list of (p, q) pairs, sorted.
    Returns reduced fractions 0/1 through 1/1 with q <= n.
    """
    result = [(0, 1)]
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        result.append((a, b))
    return result


# ============================================================================
# Structural readings of integers in framework vocabulary
# ============================================================================

def structural_reading(N: int) -> list[str]:
    """
    Return a list of framework-primary factorizations of N.

    Empty list (actually [(no clean structural reading)]) if N doesn't
    decompose into framework integers at the level this function tests.
    """
    readings: list[str] = []

    # Direct framework-integer match
    if N in FRAMEWORK_INTEGERS:
        readings.append(f"framework-primary ({N})")

    # Powers of q_2 and q_3
    for a in range(6):
        for b in range(6):
            if Q2 ** a * Q3 ** b == N and (a, b) != (0, 0):
                parts = []
                if a > 0:
                    parts.append(f"q_2^{a}" if a > 1 else "q_2")
                if b > 0:
                    parts.append(f"q_3^{b}" if b > 1 else "q_3")
                readings.append(" * ".join(parts))

    # q_2^a * q_3^b * small Fibonacci / cosmological
    for a in range(5):
        for b in range(5):
            for extra_name, extra_val in [
                ("F_6 = |F_6| = 13", F_6_COUNT),
                ("|F_7| = 19", F_7_COUNT),
                ("(q_2+q_3) = 5", MEDIANT),
                ("(q_2+q_3)^2 = 25", MEDIANT ** 2),
                ("(q_2 q_3) = 6", INTERACT),
                ("(q_2 q_3)^2 = 36", INTERACT ** 2),
                ("k_lepton = 9", K_LEPTON),
                ("k_quark = 8", K_QUARK),
            ]:
                if Q2 ** a * Q3 ** b * extra_val == N and (a + b) >= 0:
                    parts = []
                    if a > 0:
                        parts.append(f"q_2^{a}" if a > 1 else "q_2")
                    if b > 0:
                        parts.append(f"q_3^{b}" if b > 1 else "q_3")
                    parts.append(extra_name.split(" = ")[0])
                    reading = " * ".join(parts)
                    if reading not in readings:
                        readings.append(reading)

    # Fibonacci numbers
    for k in range(3, 16):
        if N == fib(k):
            readings.append(f"F_{k}")
        if N == fib(k) ** 2:
            readings.append(f"F_{k}^2")

    return readings or ["(no clean structural reading)"]


# ============================================================================
# Closed-form scans
# ============================================================================

def scan_fibonacci_squares(
    target: float,
    max_k: int = 15,
    max_prefactor: int = 40,
) -> tuple[int, int, int, float, float]:
    """
    Find integer prefactor p and Fibonacci index k such that
    p/F_k^2 is closest to target.

    Returns (p, k, F_k, predicted, rel_err) for the best match.
    """
    best = (0, 0, 0, 0.0, float("inf"))
    for k in range(3, max_k + 1):
        Fk = fib(k)
        for p in range(1, max_prefactor + 1):
            pred = p / (Fk * Fk)
            err = abs(pred - target)
            rel = err / abs(target) if target != 0 else err
            if rel < best[4]:
                best = (p, k, Fk, pred, rel)
    return best


def scan_integer_denoms(
    target: float,
    N_range: tuple[int, int] = (10, 3000),
    max_prefactor: int = 10,
) -> list[tuple[float, int, int, float]]:
    """
    Scan p/N for integer N in N_range and prefactor p in [1, max_prefactor].
    Return sorted list of (rel_err, p, N, predicted) for the top 10 fits.
    """
    results = []
    for p in range(1, max_prefactor + 1):
        for N in range(N_range[0], N_range[1] + 1):
            pred = p / N
            rel = abs(pred - target) / abs(target) if target != 0 else abs(pred - target)
            if rel < 0.01:
                results.append((rel, p, N, pred))
    results.sort()
    return results[:10]


# ============================================================================
# Physics helpers
# ============================================================================

def tongue_width(p: int, q: int, K: float) -> float:
    """
    Saddle-node control parameter mu at the q-resonance, coupling K.

    Perturbative form (K < 1): mu(p/q, K) = 2 (K/2)^q / q
    Critical form (K = 1):     mu(p/q, 1) = 1 / q^2

    Naming note: this function is historically called "tongue_width"
    but under reading (D) from noise_dressed_parabola.py and the audit
    in tongue_formula_accuracy.py, the quantity returned here is the
    saddle-node CONTROL PARAMETER mu in (x, mu) normal-form coordinates,
    NOT the Omega-space Arnold tongue width.  The physical Omega-space
    tongue width is mu / pi (e.g. at q=2, mu = (K/2)^2 and
    w_physical = K^2/(4*pi)).  Both are correct in their respective
    parameterizations; they differ by a coordinate Jacobian.

    All framework callers of this function use it as a dimensionless
    amplitude or a ratio (pi cancels), so no numerical adjustment is
    required anywhere downstream.  See tongue_formula_accuracy.py
    Part 6 for the full audit.
    """
    if q <= 0:
        raise ValueError(f"q must be positive, got {q}")
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    if K >= 1.0:
        return 1.0 / (q * q)
    return 2 * (K / 2) ** q / q


def duty_cycle(q: int, d: int = 3) -> float:
    """
    Duty cycle at denominator q in d spatial dimensions.

    duty(q, d) = 1 / q^d

    At d = 3 this is the framework's standard duty-cycle formula,
    equal to alpha_i(tree) for the gauge couplings.
    """
    return 1 / (q ** d)
