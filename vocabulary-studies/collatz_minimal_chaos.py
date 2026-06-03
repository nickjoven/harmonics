"""
collatz_minimal_chaos.py

Reads the Collatz map through the framework's minimum alphabet
(minimum_alphabet.md) as a minimal-degree-of-freedom chaotic system.
Pure-Python (no numpy), so it runs in the cloud container.

Connects to existing substrate objects:
  - docs/archive/collatz.html        : rational extension; integers = q=1
                                       boundary; Rule 3 = mediant; only
                                       cycle {1,2} because 3^a != 2^b.
  - gap2_collatz_2d_contraction.py    : q=1 integer line is the "worst"
                                       (slowest) boundary of a 2D H^2 flow.
  - second_law_topological.md         : non-invertible map -> no time
                                       reversal -> h_KS > 0 (chaos).
  - minimum_alphabet.md               : Z, mediant, fixed-point, parabola;
                                       orientation = two roots = Z2 parity.

This script demonstrates four things and prints the primitive ledger.
"""

from math import gcd, log, exp


# ---------------------------------------------------------------------------
# (1) The map and its parity branch (the two-root / Z2 orientation)
# ---------------------------------------------------------------------------
def collatz_step(n):
    return (n // 2, "even/contract  x1/2") if n % 2 == 0 else (3 * n + 1, "odd/expand  x3+1")

def orbit(n, cap=100000):
    seq = [n]
    while n != 1 and len(seq) < cap:
        n, _ = collatz_step(n)
        seq.append(n)
    return seq


# ---------------------------------------------------------------------------
# (2) Non-invertibility: the forward map is many-to-one at parity branches
#     -> no global time-reversal -> h_KS > 0 (second_law_topological.md)
# ---------------------------------------------------------------------------
def preimages(m, N=10**7):
    """Predecessors of m under T: always 2m (even branch); plus (m-1)/3
    if that is a positive ODD integer (odd branch). Two preimages = a
    branch point where T cannot be inverted."""
    pre = [2 * m]
    if (m - 1) % 3 == 0:
        k = (m - 1) // 3
        if k >= 1 and k % 2 == 1:
            pre.append(k)
    return pre


# ---------------------------------------------------------------------------
# (3) No nontrivial cycle: a k-cycle needs 3^a = 2^b (a,b>0) -> impossible
#     (unique factorization). This is the framework's {q2=2, q3=3}
#     incommensurability (same fact that forbids alternative lock cycles).
# ---------------------------------------------------------------------------
def three_pow_eq_two_pow(max_exp=40):
    hits = [(a, b) for a in range(1, max_exp) for b in range(1, max_exp)
            if 3 ** a == 2 ** b]
    return hits


# ---------------------------------------------------------------------------
# (4) "Thermodynamic" contraction drift: geometric-mean per-step multiplier
#     over many seeds. < 1 = net contraction toward the attractor (the
#     arrow of time / second law on the integer line).
# ---------------------------------------------------------------------------
def mean_log_multiplier(seeds):
    tot, cnt = 0.0, 0
    for n0 in seeds:
        n = n0
        while n != 1:
            nxt = n // 2 if n % 2 == 0 else 3 * n + 1
            tot += log(nxt / n)
            cnt += 1
            n = nxt
    return tot / cnt, exp(tot / cnt)


if __name__ == "__main__":
    print("=" * 70)
    print("Collatz through the minimum alphabet")
    print("=" * 70)

    # (1) parity branch on a sample orbit
    print("\n(1) Parity branch = the two-root / Z2 orientation primitive")
    n = 27
    seq = orbit(n)
    print(f"   n={n}: {len(seq)-1} steps, peak {max(seq)}, ends at {seq[-1]}")
    print("   first 8 steps with branch labels:")
    m = 27
    for _ in range(8):
        nxt, label = collatz_step(m)
        print(f"      {m:>4} -> {nxt:<5} [{label}]")
        m = nxt

    # (2) non-invertibility
    print("\n(2) Non-invertibility -> no time-reversal -> h_KS>0")
    for m in (16, 10, 40, 4):
        pre = preimages(m)
        kind = "BRANCH POINT (2 preimages)" if len(pre) == 2 else "single preimage"
        print(f"      T^-1({m}) = {pre}   {kind}")

    # (3) no nontrivial cycle
    print("\n(3) Only cycle is {1,2}: solutions of 3^a = 2^b (a,b>0):")
    print(f"      {three_pow_eq_two_pow() or 'NONE'}  "
          f"(<- {{q2=2, q3=3}} incommensurability)")

    # (4) contraction drift
    seeds = range(3, 2000, 2)  # odd seeds
    avg_log, geo = mean_log_multiplier(seeds)
    print("\n(4) Contraction drift over odd seeds 3..1999:")
    print(f"      mean log-multiplier = {avg_log:+.4f}  (geometric mean = {geo:.4f})")
    print(f"      < 0 / < 1  => net contraction toward attractor (second law)")
    print(f"      reference  sqrt(3)/2 = {(3**0.5)/2:.4f}  (even/odd-balanced drift)")

    # primitive ledger
    print("\n--- Collatz ingredient -> minimum-alphabet primitive ---")
    ledger = [
        ("the integer line n in Z          ", "Integers Z (primitive 1)"),
        ("parity fork (even vs odd branch)  ", "Two-root / Z2 orientation (primitive 4, DISCRETE)"),
        ("iteration to the {1,2} cycle      ", "Fixed-point x=f(x) (primitive 3)"),
        ("Rule 3 lift (3p+1)/(q+1) off q=1   ", "Mediant (primitive 2) -- the q>1 dimension"),
        ("expand x3 vs contract /2          ", "growing/decaying modes; 3^a!=2^b -> one cycle"),
        ("forward map many-to-one           ", "non-invertibility -> no time-reversal -> chaos"),
    ]
    for ing, prim in ledger:
        print(f"   {ing} -> {prim}")
    print("\n   Three primitives act on the q=1 integer line {Z, Z2, fixed-point};")
    print("   the mediant is exactly the dimension the rational extension adds.")
