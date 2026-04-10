"""
Integral mass formula test.

Hypothesis (from the discussion of why discrete walk-sums fail to
reproduce the within-sector ratios cleanly):

  The mass formula should use integrals over a measure on q-space,
  not discrete sums of denominators.

This script tests the simplest integral form:

  m_f / v = integral over a q-window [alpha_f, beta_f] of a measure mu(q)

with mu(q) chosen to be one of the natural framework measures:

  (a) (K*/2)^q dq                  -- bare exponential, no Ford weighting
  (b) (K*/2)^q / q dq               -- tongue width per period (weighted by 1/q)
  (c) (K*/2)^q / q^2 dq             -- Ford circle measure 1/q^2
  (d) (K*/2)^q / q^3 dq             -- duty cycle measure 1/q^d with d = 3

For each measure, treat the 12 fermions (heaviest to lightest) as
filling the q half-line cumulatively. Each fermion's mass is the
integral over [beta_{f-1}, beta_f]. Solving for beta_f gives the
"q-coordinate" of each fermion's UPPER edge in the cumulative
ordering. If those edges land on a clean integer pattern, the
integral form is doing structural work.

K* is pinned to 0.862 (boundary_weight.md), the same value used in
committed_walk_masses.py. Never refit.
"""

import math

# ============================================================================
# Pinned inputs
# ============================================================================

K_STAR = 0.862
V_GEV  = 246.0
V_MEV  = V_GEV * 1e3
LN_HALF_K = math.log(K_STAR / 2.0)   # negative (~ -0.842)


# Observed masses in MeV, ordered heaviest -> lightest
FERMIONS = [
    ("top",     172760.0),
    ("bottom",  4180.0),
    ("tau",     1776.86),
    ("charm",   1270.0),
    ("strange", 93.4),
    ("mu",      105.6583755),
    ("down",    4.67),
    ("up",      2.16),
    ("e",       0.51099895),
    ("nu_tau",  50.0e-9),
    ("nu_mu",   8.6e-9),
    ("nu_e",    1.0e-9),
]
# Reorder heaviest to lightest
FERMIONS.sort(key=lambda t: -t[1])


# ============================================================================
# Antiderivatives for each candidate measure
#
# (a) integral (K/2)^q dq          = (K/2)^q / ln(K/2)
# (b) integral (K/2)^q / q dq      = -E_1(-q ln(K/2))  (exp integral)
# (c) integral (K/2)^q / q^2 dq    = no closed form, numerical
# (d) integral (K/2)^q / q^3 dq    = no closed form, numerical
#
# For the cumulative test, we just need numerical integrals between
# successive boundaries. Use the trapezoid / direct evaluation form.
# ============================================================================

def antideriv_a(q):
    """Antiderivative of (K/2)^q dq."""
    return math.exp(q * LN_HALF_K) / LN_HALF_K  # negative for K<2

def integral_a(q1, q2):
    """∫_{q1}^{q2} (K/2)^q dq"""
    return antideriv_a(q2) - antideriv_a(q1)

def integral_numeric(q1, q2, exponent_d, n=2000):
    """∫_{q1}^{q2} (K/2)^q / q^exponent_d dq, by trapezoid."""
    if q1 <= 0:
        q1 = 1e-9
    h = (q2 - q1) / n
    s = 0.0
    for i in range(n + 1):
        q = q1 + i * h
        f = math.exp(q * LN_HALF_K) / (q ** exponent_d)
        if i == 0 or i == n:
            s += 0.5 * f
        else:
            s += f
    return s * h


# ============================================================================
# Cumulative inversion for each measure
# ============================================================================

def find_beta_a(beta_prev, m_over_v):
    """
    Solve integral_a(beta_prev, beta_new) = m_over_v for beta_new,
    given measure (a) which has a closed form.

    integral_a(b, B) = (exp(B ln(K/2)) - exp(b ln(K/2))) / ln(K/2)
    => exp(B ln(K/2)) = exp(b ln(K/2)) + m_over_v * ln(K/2)
    => B = log(exp(b ln(K/2)) + m_over_v * ln(K/2)) / ln(K/2)
    """
    inside = math.exp(beta_prev * LN_HALF_K) + m_over_v * LN_HALF_K
    if inside <= 0:
        return None
    return math.log(inside) / LN_HALF_K


def find_beta_numeric(beta_prev, m_over_v, exponent_d, q_step=1e-3, q_max=200):
    """
    Solve integral_numeric(beta_prev, beta_new) = m_over_v for beta_new
    by stepping forward.

    For 1/q^d measures, we anchor the lower bound at q = 1
    (denominators start at 1; the integrand diverges at q -> 0).
    """
    if beta_prev < 1.0 and exponent_d > 0:
        beta_prev = 1.0
    accum = 0.0
    q = beta_prev
    while q < q_max:
        # Trapezoid step
        f1 = math.exp(q * LN_HALF_K) / (q ** exponent_d) if q > 0 else 1e30
        f2 = math.exp((q + q_step) * LN_HALF_K) / ((q + q_step) ** exponent_d)
        slab = 0.5 * (f1 + f2) * q_step
        if accum + slab >= m_over_v:
            # Linear interpolate within this slab
            frac = (m_over_v - accum) / slab
            return q + frac * q_step
        accum += slab
        q += q_step
    return None


# ============================================================================
# Run the test for each measure
# ============================================================================

def run(measure_label, finder):
    print()
    print("=" * 78)
    print(f"  MEASURE {measure_label}")
    print("=" * 78)
    print()
    print(f"  {'fermion':<9} {'m_obs (MeV)':>14} {'cum window upper':>20} "
          f"{'delta from prev':>16}")
    print("  " + "-" * 64)

    beta = 0.0
    prev_beta = 0.0
    for name, m in FERMIONS:
        m_over_v = m / V_MEV
        new_beta = finder(beta, m_over_v)
        if new_beta is None:
            print(f"  {name:<9} {m:>14.6e} {'NO SOLUTION':>20} "
                  f"{'cum overflowed':>16}")
            break
        delta = new_beta - beta
        prev_beta = beta
        beta = new_beta
        print(f"  {name:<9} {m:>14.6e} {beta:>20.4f} {delta:>+16.4f}")
    print()


# Closed-form measure (a)
def finder_a(b, m):
    return find_beta_a(b, m)

# Numerical measures (b), (c), (d)
def make_finder(d):
    return lambda b, m: find_beta_numeric(b, m, d)


def main():
    print()
    print("=" * 78)
    print("  INTEGRAL MASS FORMULA TEST")
    print("=" * 78)
    print()
    print(f"  K* = {K_STAR}  (pinned, never refit)")
    print(f"  v  = {V_GEV} GeV")
    print()
    print(f"  Hypothesis: m_f/v = integral over [beta_(f-1), beta_f] of mu(q)")
    print(f"  Order fermions heaviest -> lightest, integrate cumulatively.")
    print(f"  Each fermion's window upper edge beta_f is the next boundary.")
    print()
    print(f"  If beta_f lands on clean structural integers, the integral form")
    print(f"  is doing real work. If not, the gap is elsewhere.")
    print()

    # The 12 fermions in observed mass order:
    print(f"  {'fermion':<9} {'m_obs (MeV)':>14} {'log(m/v)':>14}")
    print("  " + "-" * 40)
    for name, m in FERMIONS:
        print(f"  {name:<9} {m:>14.6e} {math.log(m/V_MEV):>14.4f}")
    print()

    # Run each measure
    run("(a)  mu(q) = (K*/2)^q dq", finder_a)
    run("(b)  mu(q) = (K*/2)^q / q dq", make_finder(1))
    run("(c)  mu(q) = (K*/2)^q / q^2 dq  [Ford circle measure]",
        make_finder(2))
    run("(d)  mu(q) = (K*/2)^q / q^3 dq  [duty-cycle measure, d=3]",
        make_finder(3))


if __name__ == "__main__":
    main()
