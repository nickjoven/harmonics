"""
ramanujan_pi_decomposition.py

Decompose Ramanujan's 1914 series for 1/pi into the framework's minimum
alphabet (minimum_alphabet.md: integers Z, mediant, fixed-point/iteration,
parabola x^2+mu=0) plus the completion limit (Part III).

The 1914 series (Ramanujan, "Modular equations and approximations to pi";
the N=58 singular-modulus case, Borwein & Borwein 1987):

    1/pi = (2*sqrt2 / 9801) * sum_{k>=0} (4k)! (1103 + 26390 k)
                                          --------------------------
                                            (k!)^4  396^(4k)

This script makes three things explicit and machine-checkable:

  (A) Every ingredient except sqrt2 is built from INTEGERS alone
      (factorials, integer powers, a linear-in-k term). The partial
      sums S_n are therefore exact RATIONALS (computed with Fraction,
      no floating point). pi is reached only in the COMPLETION limit.

  (B) The series is HYPERGEOMETRIC: the term ratio t_{k+1}/t_k is a
      RATIONAL FUNCTION of k. So the sequence of partial sums is an
      ITERATION over Q -- a fixed-point/iteration process on
      mediant-generated rationals, not an independently-specified set
      of terms.

  (C) The single algebraic irrational injected is sqrt2 = the positive
      root of the PARABOLA x^2 - 2 = 0. pi then = (rational) * sqrt2 in
      the limit: a Q-valued Cauchy sequence, completed, scaled by one
      parabola root.

No trig, no pi on the right-hand side. sqrt2 is carried symbolically
(as the root of x^2-2) and only evaluated for the final digit check.
"""

from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 80


def factorial(n: int) -> int:
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def term(k: int) -> Fraction:
    """The k-th summand as an exact rational (integers only)."""
    num = factorial(4 * k) * (1103 + 26390 * k)        # integers
    den = factorial(k) ** 4 * 396 ** (4 * k)           # integers
    return Fraction(num, den)


def term_ratio(k: int) -> Fraction:
    """t_{k+1}/t_k, exact rational -> demonstrates hypergeometric form."""
    return term(k + 1) / term(k)


# ---------------------------------------------------------------------------
# (A)+(B): rational partial sums via iteration; term ratio is rational in k
# ---------------------------------------------------------------------------
N = 12
S = Fraction(0)
print("k :  term ratio t_{k+1}/t_k (exact rational)   ~decimal")
for k in range(0, 6):
    r = term_ratio(k)
    print(f"{k} :  {str(r):>40}   {float(r):.3e}")
print()

for k in range(0, N):
    S += term(k)
print(f"S_{N} (partial sum) is rational: type={type(S).__name__}, "
      f"denominator has {len(str(S.denominator))} digits")

# ---------------------------------------------------------------------------
# (C): the one irrational = parabola root sqrt2; complete and check pi
# ---------------------------------------------------------------------------
sqrt2 = Decimal(2).sqrt()                              # root of x^2 - 2 = 0
inv_pi = (2 * sqrt2 / Decimal(9801)) * Decimal(S.numerator) / Decimal(S.denominator)
pi_est = 1 / inv_pi

ref_pi = Decimal(
    "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899"
)
agree = 0
a, b = str(pi_est), str(ref_pi)
for ca, cb in zip(a, b):
    if ca == cb:
        agree += 1
    else:
        break

print(f"\npi (from {N} terms) = {pi_est}")
print(f"pi (reference)      = {ref_pi}")
print(f"leading characters in agreement: {agree}")

# ---------------------------------------------------------------------------
# Primitive ledger
# ---------------------------------------------------------------------------
print("\n--- ingredient -> minimum-alphabet primitive ---")
ledger = [
    ("(4k)!, (k!)^4              ", "Integers Z (iterated +,*)"),
    ("396^(4k), 9801=99^2         ", "Integers Z (powers)"),
    ("1103 + 26390 k              ", "Integers Z (linear in winding index k)"),
    ("term ratio = rational(k)    ", "Fixed-point/iteration over Q (hypergeometric)"),
    ("rationals Q themselves      ", "Mediant -> Stern-Brocot/PSL(2,Z) Farey structure"),
    ("sum_{k->oo} (infinite sum)  ", "Completion of Q (NOT a primitive; Part III)"),
    ("2*sqrt2                     ", "Parabola x^2 - 2 = 0 (single algebraic irrational)"),
    ("pi (the output)             ", "Completion artifact (cf. 2pi cycle<->radian on S^1)"),
]
for ing, prim in ledger:
    print(f"  {ing} -> {prim}")
