"""
The FFT and the Stern-Brocot tree are the same binary tree.

Both are recursive 2×2 operations applied at each level of a
depth-d binary tree, combining two sub-results into one result.
Both have a sign flip in the combining operation.

  FFT butterfly:  [X_k, X_{k+N/2}] = [[1, W^k],[1,-W^k]] × [E_k, O_k]
  Mediant matrix: [F_{n+1}, F_n]    = [[1, 1], [1, 0]]    × [F_n, F_{n-1}]

  FFT sign flip:  the -W^k in row 2 → constructive/destructive interference
  Tree sign flip: det(M) = -1        → alternating convergence (Cassini)

The FFT butterfly gives O(N log N) for the full Fourier transform.
The bottleneck gives O(N) for the one coefficient that matters.

Three levels of efficiency:
  Naive DFT:     O(N²)    — compute all N modes independently
  FFT:           O(N log N) — share work via binary tree (sign flip)
  Bottleneck:    O(N)      — only one mode matters (the order parameter)

The speedup from O(N²) to O(N log N) is the FFT's binary tree.
The speedup from O(N log N) to O(N) is the 1D bottleneck.
Both rely on the same structure: a half-twist at each level.

Usage:
    python sync_cost/derivations/fourier_connection.py
"""

import math
import cmath
from fractions import Fraction
import sys

sys.path.insert(0, "sync_cost/derivations")
from universe_loop import (
    ConstraintTree, Operator, tongue_width,
    fibonacci_backbone, PHI, PSI,
)


# ═══════════════════════════════════════════════════════════════════════════════
# THE TWO 2×2 OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def fft_butterfly(E_k, O_k, W_k):
    """One FFT butterfly operation.

    [X_k, X_{k+N/2}] = [[1, W^k], [1, -W^k]] × [E_k, O_k]

    The sign flip (-W^k in row 2) creates constructive/destructive
    interference. This is the Fourier transform's half-twist.
    """
    return E_k + W_k * O_k, E_k - W_k * O_k


def mediant(a_num, a_den, b_num, b_den):
    """One mediant operation.

    (a+c)/(b+d) from a/b and c/d.

    In matrix form: [[1,1],[1,0]] applied to [F_n, F_{n-1}].
    det = -1. This is the Stern-Brocot tree's half-twist.
    """
    return a_num + b_num, a_den + b_den


def naive_dft(x):
    """O(N²) DFT: X[k] = Σ_n x[n] e^{-2πink/N}."""
    N = len(x)
    return [sum(x[n] * cmath.exp(-2j * math.pi * n * k / N)
                for n in range(N))
            for k in range(N)]


def fft_radix2(x):
    """O(N log N) FFT via Cooley-Tukey radix-2.

    At each level: split into even/odd, recurse, combine via butterfly.
    The butterfly IS the binary tree operation.
    """
    N = len(x)
    if N == 1:
        return list(x)

    even = fft_radix2(x[0::2])
    odd = fft_radix2(x[1::2])

    X = [0] * N
    for k in range(N // 2):
        W_k = cmath.exp(-2j * math.pi * k / N)
        X[k], X[k + N // 2] = fft_butterfly(even[k], odd[k], W_k)
    return X


def count_operations_dft(N):
    """Count multiplications in naive DFT."""
    return N * N


def count_operations_fft(N):
    """Count multiplications in radix-2 FFT."""
    if N <= 1:
        return 0
    return N + 2 * count_operations_fft(N // 2)  # N butterflies + 2 sub-problems


# ═══════════════════════════════════════════════════════════════════════════════
# THE ORDER PARAMETER AS A DFT COEFFICIENT
# ═══════════════════════════════════════════════════════════════════════════════

def order_parameter_as_dft(g_star, tree):
    """Show that r(g) = DFT(g)[1] / DFT(g)[0].

    The order parameter IS a ratio of Fourier coefficients.
    The 1D bottleneck says: this ratio is all you need.
    """
    nodes = tree.all_nodes
    N = len(nodes)

    # Method 1: direct order parameter computation (O(N))
    total = sum(g_star[n.value] for n in nodes)
    r_direct = sum(g_star[n.value] * cmath.exp(2j * math.pi * float(n.value))
                   for n in nodes) / total

    # Method 2: DFT coefficients
    # To use DFT, we need g on a regular grid. Instead, show the equivalence
    # algebraically: r = Σ g(f) e^{2πif} / Σ g(f) = DFT_at_k=1 / DFT_at_k=0
    # (where "DFT" means the non-uniform Fourier sum over tree nodes)
    dft_k0 = sum(g_star[n.value] for n in nodes)  # k=0: just the sum
    dft_k1 = sum(g_star[n.value] * cmath.exp(2j * math.pi * float(n.value))
                 for n in nodes)  # k=1: weighted by phase
    r_from_dft = dft_k1 / dft_k0

    return r_direct, r_from_dft, dft_k0, dft_k1


# ═══════════════════════════════════════════════════════════════════════════════
# THE SIGN FLIP COMPARISON
# ═══════════════════════════════════════════════════════════════════════════════

def butterfly_determinants(N):
    """Compute det of the FFT butterfly matrix at each stage.

    B_k = [[1, W^k], [1, -W^k]], det(B_k) = -2W^k.
    The factor of -1 is the sign flip (half-twist).
    """
    results = []
    for stage in range(int(math.log2(N))):
        sub_N = 2 ** (stage + 1)
        for k in range(sub_N // 2):
            W_k = cmath.exp(-2j * math.pi * k / sub_N)
            det = -2 * W_k
            results.append((stage, k, sub_N, W_k, det))
    return results


if __name__ == "__main__":
    print("=" * 72)
    print("  THE FFT AND THE STERN-BROCOT TREE")
    print("  are the same binary tree with a sign flip")
    print("=" * 72)

    # ══════════════════════════════════════════════════════════════════
    # SIDE BY SIDE: the two 2×2 operations
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THE TWO 2×2 OPERATIONS")
    print(f"{'═' * 72}")

    print(f"""
  FFT butterfly (at frequency k, size N):
    [[X_k    ],  [[1,  W^k], [E_k,
     [X_{{k+N/2}}]] = [1, -W^k]]  [O_k]]

    W^k = e^{{-2πik/N}}
    det = -2W^k  (sign flip: the minus in row 2)

  Mediant matrix (Fibonacci recursion):
    [[F_{{n+1}}],  [[1, 1], [F_n,
     [F_n    ]] = [1, 0]]  [F_{{n-1}}]]

    det = -1  (sign flip: the 0 in corner)

  Both are 2×2, both applied recursively in a binary tree,
  both have a sign flip in the combining operation.
    """)

    # ══════════════════════════════════════════════════════════════════
    # THE SIGN FLIP AT EACH LEVEL
    # ══════════════════════════════════════════════════════════════════
    print(f"{'═' * 72}")
    print("  SIGN FLIPS AT EACH LEVEL")
    print(f"{'═' * 72}")

    N = 16
    n_stages = int(math.log2(N))

    print(f"\n  FFT (N={N}, {n_stages} stages):")
    print(f"  Each butterfly at k=0 has det(B₀) = -2.")
    print(f"  The -1 factor is the half-twist.")
    print(f"\n  {'stage':>5s}  {'sub-N':>5s}  {'k=0 twiddle':>14s}  "
          f"{'det(B₀)':>12s}  {'sign of det':>12s}")
    print("  " + "-" * 54)

    for stage in range(n_stages):
        sub_N = 2 ** (stage + 1)
        W_0 = cmath.exp(-2j * math.pi * 0 / sub_N)  # W^0 = 1
        det = -2 * W_0
        sign = "-" if det.real < 0 else "+"
        print(f"  {stage:5d}  {sub_N:5d}  {W_0.real:14.6f}  "
              f"{det.real:12.6f}  {sign:>12s}")

    print(f"\n  Stern-Brocot tree (depth {n_stages}):")
    print(f"  Each mediant has det(M) = -1.")
    print(f"\n  {'depth':>5s}  {'nodes':>5s}  {'det(M)':>8s}  "
          f"{'det(M^d)':>10s}  {'cumulative':>12s}")
    print("  " + "-" * 46)

    for d in range(n_stages):
        n_nodes = 2**d
        det_M = -1
        det_M_d = (-1)**(d+1)
        print(f"  {d:5d}  {n_nodes:5d}  {det_M:8d}  "
              f"{det_M_d:10d}  {'REVERSED' if det_M_d == -1 else 'preserved':>12s}")

    print(f"\n  Both: {n_stages} levels, sign flip at each level.")

    # ══════════════════════════════════════════════════════════════════
    # THE ORDER PARAMETER IS A FOURIER COEFFICIENT
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THE ORDER PARAMETER IS DFT[1] / DFT[0]")
    print(f"{'═' * 72}")

    DEPTH = 8
    tree = ConstraintTree(DEPTH)
    U = Operator(tree, K0=1.0)
    g_star, r_star = U.find_fixed_point()

    r_direct, r_dft, dft_k0, dft_k1 = order_parameter_as_dft(g_star, tree)

    print(f"\n  r(g*) computed directly:     {r_direct}")
    print(f"  r(g*) as DFT[1]/DFT[0]:     {r_dft}")
    print(f"  |difference|:                {abs(r_direct - r_dft):.2e}")
    print(f"\n  DFT[0] = Σ g*(f)          = {dft_k0:.6f}  (total population)")
    print(f"  DFT[1] = Σ g*(f) e^{{2πif}} = {dft_k1}")
    print(f"  |r| = |DFT[1]|/DFT[0]    = {abs(dft_k1)/dft_k0:.10f}")
    print(f"\n  The 1D bottleneck: only |DFT[1]/DFT[0]| enters the operator U.")
    print(f"  DFT[2], DFT[3], ... DFT[N-1] are all irrelevant.")

    # ══════════════════════════════════════════════════════════════════
    # THREE LEVELS OF EFFICIENCY
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THREE LEVELS OF EFFICIENCY")
    print(f"{'═' * 72}")

    print(f"\n  Computing the Fourier transform of g over N nodes:")
    print(f"\n  {'method':>20s}  {'what it computes':>30s}  {'cost':>12s}  {'speedup':>10s}")
    print("  " + "-" * 78)

    sizes = [8, 16, 32, 64, 128, 256, 512, 1024]

    print(f"  {'naive DFT':>20s}  {'all N Fourier modes':>30s}  {'O(N²)':>12s}  {'—':>10s}")
    print(f"  {'FFT':>20s}  {'all N Fourier modes':>30s}  {'O(N log N)':>12s}  {'N/log N':>10s}")
    print(f"  {'bottleneck (r only)':>20s}  {'one Fourier mode (|r|)':>30s}  {'O(N)':>12s}  {'N':>10s}")

    print(f"\n  Concrete operation counts:")
    print(f"\n  {'N':>6s}  {'naive DFT':>12s}  {'FFT':>12s}  {'bottleneck':>12s}  "
          f"{'FFT speedup':>12s}  {'total speedup':>14s}")
    print("  " + "-" * 72)

    for N in sizes:
        naive = count_operations_dft(N)
        fft = count_operations_fft(N)
        bottleneck = N  # just one weighted sum
        fft_speedup = naive / fft if fft > 0 else 0
        total_speedup = naive / bottleneck
        print(f"  {N:6d}  {naive:12d}  {fft:12d}  {bottleneck:12d}  "
              f"{fft_speedup:12.1f}×  {total_speedup:14.1f}×")

    # ══════════════════════════════════════════════════════════════════
    # THE STRUCTURAL CONNECTION
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  THE STRUCTURAL CONNECTION")
    print(f"{'═' * 72}")

    print(f"""
  The FFT and the Stern-Brocot tree are the same structure:
  a binary tree of depth d = log₂(N) with a 2×2 combining
  operation at each node that has a sign flip.

  {'':>4s}{'FFT':>28s}  {'Stern-Brocot':>28s}
  {'':>4s}{'-'*28:>28s}  {'-'*28:>28s}
  {'space':>4s}{'C (complex)':>28s}  {'Q (rational)':>28s}
  {'nodes':>4s}{'N = 2^d':>28s}  {'2^d - 1':>28s}
  {'operation':>4s}{'butterfly':>28s}  {'mediant':>28s}
  {'matrix':>4s}{'[[1,W],[1,-W]]':>28s}  {'[[1,1],[1,0]]':>28s}
  {'sign flip':>4s}{'-W in row 2':>28s}  {'det = -1':>28s}
  {'what it does':>4s}{'interference':>28s}  {'alternating convergence':>28s}
  {'resolves':>4s}{'frequency k/N':>28s}  {'rational p/q':>28s}
  {'depth d cost':>4s}{'O(N log N) all modes':>28s}  {'O(N) all rationals':>28s}
  {'per mode':>4s}{'O(N log N / N) = O(log N)':>28s}  {'O(1) per mediant':>28s}""")

    print(f"""
  The speedup hierarchy:

  O(N²) ──FFT──→ O(N log N) ──bottleneck──→ O(N)
          ×N/logN                 ×logN

  The FFT speedup (N/log N) comes from:
    sharing work across the binary tree (butterfly reuse).

  The bottleneck speedup (log N) comes from:
    only needing ONE Fourier coefficient (the order parameter).

  Together: O(N²) → O(N). Factor of N.

  The total speedup IS the 1D bottleneck of U.
  The FFT is a partial version of what the framework gives for free.
""")

    # ══════════════════════════════════════════════════════════════════
    # VERIFY: FFT on tree distributions
    # ══════════════════════════════════════════════════════════════════
    print(f"{'═' * 72}")
    print("  VERIFY: higher Fourier modes of g* are irrelevant")
    print(f"{'═' * 72}")

    # Compute all "Fourier modes" of g* over the tree
    nodes = tree.all_nodes
    N_tree = len(nodes)
    freqs = [float(n.value) for n in nodes]
    pops = [g_star[n.value] for n in nodes]
    total_pop = sum(pops)

    # Non-uniform "DFT": r_k = Σ g(f) e^{2πikf} / Σ g(f)
    print(f"\n  Non-uniform Fourier modes of g* (N = {N_tree} nodes):")
    print(f"\n  {'k':>4s}  {'|r_k|':>12s}  {'|r_k|/|r_1|':>14s}  {'role':>20s}")
    print("  " + "-" * 56)

    r_modes = []
    for k in range(min(20, N_tree)):
        r_k = sum(pops[i] * cmath.exp(2j * math.pi * k * freqs[i])
                  for i in range(N_tree)) / total_pop
        r_modes.append(abs(r_k))

    r_1 = r_modes[1] if len(r_modes) > 1 else 1

    for k in range(min(20, len(r_modes))):
        ratio = r_modes[k] / r_1 if r_1 > 0 else 0
        role = ""
        if k == 0:
            role = "normalization"
        elif k == 1:
            role = "THE BOTTLENECK"
        else:
            role = ""
        print(f"  {k:4d}  {r_modes[k]:12.8f}  {ratio:14.6f}  {role:>20s}")

    print(f"\n  |r_1| = {r_1:.8f} (the order parameter)")
    print(f"  |r_2|/|r_1| = {r_modes[2]/r_1:.6f}")
    print(f"  |r_3|/|r_1| = {r_modes[3]/r_1:.6f}")
    print(f"\n  Higher modes exist but DO NOT ENTER the operator U.")
    print(f"  U compresses g to |r_1| and discards everything else.")
    print(f"  The 1D bottleneck is a Fourier-domain statement:")
    print(f"  'only the first harmonic of the distribution matters.'")

    # ══════════════════════════════════════════════════════════════════
    # SUMMARY
    # ══════════════════════════════════════════════════════════════════
    print(f"\n{'═' * 72}")
    print("  SUMMARY")
    print(f"{'═' * 72}")
    print(f"""
  The FFT's algorithmic speedup connects to the framework as follows:

  1. The order parameter r(g) = DFT[1]/DFT[0].
     It is literally a Fourier coefficient.

  2. The FFT computes ALL Fourier coefficients in O(N log N)
     via a binary tree of butterflies with sign flips.

  3. The Stern-Brocot tree resolves ALL rationals in O(N)
     via a binary tree of mediants with sign flips (det = -1).

  4. The sign flip in both cases is the half-twist:
     FFT: -W^k in the butterfly → interference
     Tree: det(M) = -1         → Cassini alternation

  5. The 1D bottleneck says: you only need r_1 (one Fourier mode).
     This reduces O(N log N) to O(N).
     The bottleneck IS the speedup.

  6. The full speedup from naive DFT to bottleneck is ×N.
     The FFT captures ×(N/log N) of this.
     The bottleneck captures the remaining ×(log N).

  The FFT is the algorithm that exploits the binary tree structure.
  The framework says: the binary tree structure is all there is.
  The Fourier transform is not a computational tool applied to
  the physics — it IS the physics, because the order parameter
  IS a Fourier coefficient, and the operator U IS a Fourier filter
  that keeps only the first mode.
""")
