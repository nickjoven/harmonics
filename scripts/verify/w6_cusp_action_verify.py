"""
External verification of W_6 Klein-four Atkin-Lehner cusp action on Γ_0(6).

Closes F-W6-1 of gamma06_w6_invariance_opposite_view_audit.md (PR #246).

Independently reproduces the cusp action computed in §2 of the audit:
  W_2: {∞ ↔ 1/3}, {0 ↔ 1/2}
  W_3: {∞ ↔ 1/2}, {0 ↔ 1/3}
  W_6: {∞ ↔ 0},   {1/2 ↔ 1/3}

Method: exact rational arithmetic via fractions.Fraction; cusp class
determined by gcd(denominator, N=6) per standard Γ_0(N) cusp
parametrization.
"""

from fractions import Fraction
from math import gcd


N = 6

# Atkin-Lehner matrix representatives for Γ_0(6).
# W_Q = [[Q*a, b], [N*c, Q*d]] with Q*a*d - (N/Q)*b*c = 1, det = Q.
W = {
    2: ((2, 1), (6, 4)),   # det = 8 − 6 = 2
    3: ((3, 1), (6, 3)),   # det = 9 − 6 = 3
    6: ((0, -1), (6, 0)),  # det = 0 − (−6) = 6  (Fricke τ → −1/(6τ))
}


def cusp_class(p_q):
    """Return Γ_0(6) cusp class label given a rational or 'inf'.

    Cusps of Γ_0(N) for N = 6 are parametrized by divisors d | N
    representing gcd(denominator, N). The 4 classes are d ∈ {1, 2, 3, 6}.
    Class d = 1 contains 0; class d = 6 contains ∞.
    """
    if p_q == "inf":
        return 6  # ∞ is in cusp class d = 6
    num = p_q.numerator
    den = p_q.denominator
    if num == 0:
        return 1  # 0 is in cusp class d = 1
    g = gcd(abs(den), N)
    return g


CUSP_LABEL = {1: "0", 2: "1/2", 3: "1/3", 6: "∞"}
CUSP_REPS = {
    "∞": "inf",
    "0": Fraction(0, 1),
    "1/2": Fraction(1, 2),
    "1/3": Fraction(1, 3),
}


def mobius(M, tau):
    """Apply Möbius transformation [[a,b],[c,d]] to tau (Fraction or 'inf')."""
    (a, b), (c, d) = M
    if tau == "inf":
        # M(∞) = a/c (or ∞ if c == 0)
        if c == 0:
            return "inf"
        return Fraction(a, c)
    num = a * tau + b
    den = c * tau + d
    if den == 0:
        return "inf"
    return Fraction(num, den)


def verify_W(Q):
    """Compute W_Q action on the 4 cusps and return as dict."""
    M = W[Q]
    result = {}
    for label, rep in CUSP_REPS.items():
        image = mobius(M, rep)
        klass = cusp_class(image)
        result[label] = CUSP_LABEL[klass]
    return result


def compose(M1, M2):
    """Matrix product M1 · M2."""
    (a1, b1), (c1, d1) = M1
    (a2, b2), (c2, d2) = M2
    return (
        (a1 * a2 + b1 * c2, a1 * b2 + b1 * d2),
        (c1 * a2 + d1 * c2, c1 * b2 + d1 * d2),
    )


def main():
    print("W_d cusp action on Γ_0(6), N = 6")
    print("=" * 50)
    print()

    expected = {
        2: {"∞": "1/3", "0": "1/2", "1/2": "0", "1/3": "∞"},
        3: {"∞": "1/2", "0": "1/3", "1/2": "∞", "1/3": "0"},
        6: {"∞": "0", "0": "∞", "1/2": "1/3", "1/3": "1/2"},
    }

    all_ok = True
    for Q in (2, 3, 6):
        det = (
            W[Q][0][0] * W[Q][1][1] - W[Q][0][1] * W[Q][1][0]
        )
        print(f"W_{Q} = {W[Q]}, det = {det}")
        result = verify_W(Q)
        for cusp_in, cusp_out in result.items():
            exp = expected[Q][cusp_in]
            ok = "✓" if cusp_out == exp else "✗"
            if cusp_out != exp:
                all_ok = False
            print(f"   W_{Q}({cusp_in:>4}) = {cusp_out:<4}  (expected {exp})  {ok}")
        print()

    print("Composition check W_2 · W_3 (as matrices) vs W_6 action on cusps")
    print("-" * 50)
    M_23 = compose(W[2], W[3])
    (a, b), (c, d) = M_23
    det_23 = a * d - b * c
    print(f"W_2 · W_3 matrix = {M_23}, det = {det_23} (= 6 ✓ matches W_6)")
    print()

    # The composition matrix has det = 6 but may differ from the canonical W_6
    # by a scalar in the Atkin-Lehner normalization. What must agree is the
    # cusp action.
    for label, rep in CUSP_REPS.items():
        image_via_23 = mobius(M_23, rep)
        klass_via_23 = cusp_class(image_via_23)
        result_W6 = verify_W(6)[label]
        match = "✓" if CUSP_LABEL[klass_via_23] == result_W6 else "✗"
        if CUSP_LABEL[klass_via_23] != result_W6:
            all_ok = False
        print(
            f"   (W_2·W_3)({label:>4}) = {CUSP_LABEL[klass_via_23]:<4}  "
            f"W_6({label:>4}) = {result_W6:<4}  {match}"
        )

    print()
    print("=" * 50)
    print(f"Audit §2 W_d cusp action: {'CONFIRMED' if all_ok else 'FAILED'}")
    print(f"Klein-four W_2·W_3 = W_6 on cusps: {'CONFIRMED' if all_ok else 'FAILED'}")


if __name__ == "__main__":
    main()
