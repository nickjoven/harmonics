"""
lambda_unlock_closed_form.py

Closed-form derivation of the Klein-bottle Lyapunov exponent on
the unlocked sector at critical coupling:

    lambda_unlock(K=1) = (4G - pi ln 2) / pi

where G = Catalan's constant ~= 0.9159656.  Used in
a_s_geometric_proof.md as axiom A5 and pinned by
test_lambda_unlock_closed_form in test_framework_constants.py.

Derivation
----------
The defining integral (gap2_spatialization sub-C, integrated over
the expanding sector and per-period normalized):

    lambda_unlock(K) = (1/pi) * integral over [pi/2, 3 pi/2] of
                        ln(1 + K|cos theta|) dtheta

At K = 1, substitute phi = theta - pi (so |cos(phi+pi)| = |cos phi|)
and use symmetry:

    integral = 2 * integral_[0, pi/2] of ln(1 + cos phi) dphi
             = 2 * integral_[0, pi/2] of ln(2 cos^2(phi/2)) dphi
             = pi ln 2 + 4 * integral_[0, pi/2] of ln cos(phi/2) dphi

Substitute u = phi/2:

    = pi ln 2 + 8 * integral_[0, pi/4] of ln cos u du

Apply the identity (Bromwich, Inghum):

    integral_[0, pi/4] of ln cos u du = G/2 - (pi/4) ln 2

so

    integral = pi ln 2 + 8 * [G/2 - (pi/4) ln 2]
             = pi ln 2 + 4G - 2 pi ln 2
             = 4G - pi ln 2

Per-period (divide by pi):

    lambda_unlock(1) = (4G - pi ln 2) / pi
                    = 4 G/pi - ln 2
                    ~= 0.473096

Run:
    python3 sync_cost/derivations/lambda_unlock_closed_form.py
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import LAMBDA_UNLOCK

CATALAN = 0.9159655941772190
PI = math.pi


def integrate(f, a, b, N=100000):
    """Simpson's rule."""
    h = (b - a) / N
    s = f(a) + f(b)
    for i in range(1, N):
        x = a + i * h
        w = 4 if i % 2 else 2
        s += w * f(x)
    return s * h / 3


def main() -> None:
    print("=" * 72)
    print("  lambda_unlock(K=1) closed form")
    print("=" * 72)

    closed_form_integral = 4 * CATALAN - PI * math.log(2)
    closed_form_normalized = closed_form_integral / PI

    numerical_integral = integrate(
        lambda t: math.log(1 + abs(math.cos(t))), PI / 2, 3 * PI / 2
    )
    numerical_normalized = numerical_integral / PI

    print(f"""
  Defining integral (per gap2_spatialization sub-C):
    I(K=1) = integral over [pi/2, 3 pi/2] of ln(1 + |cos theta|) dtheta

  Closed-form value:    4G - pi ln 2  = {closed_form_integral:.10f}
  Numerical (Simpson):                = {numerical_integral:.10f}
  Match:                                {abs(numerical_integral - closed_form_integral):.2e}

  Per-period normalization (/ pi):
    lambda_unlock(1) = (4G - pi ln 2)/pi = {closed_form_normalized:.10f}
    Numerical:                            {numerical_normalized:.10f}
    framework_constants.LAMBDA_UNLOCK:    {LAMBDA_UNLOCK:.10f}

    Match: {'PASS' if abs(LAMBDA_UNLOCK - closed_form_normalized) < 1e-4 else 'FAIL'}
""")


if __name__ == "__main__":
    main()
