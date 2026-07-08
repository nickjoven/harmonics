#!/usr/bin/env python3
"""
Module 5 — The tree the rule builds.

Module 4 found the combining rule (mediant) and iterated it between 0/1 and
1/1 to enumerate the ratios in (0,1). This module runs the SAME rule between
0/1 and 1/0 (zero and infinity), which grows a tree containing EVERY positive
ratio, and proves the two claims Module 4 left open:

  1. every positive fraction appears, exactly once, already in lowest terms;
  2. any two side-by-side fractions a/b, c/d obey  b·c − a·d = 1  — the
     "as-close-as-possible" neighbor condition — at every level.

It also shows that the left/right turns taken to reach a fraction from the top
spell out its continued fraction: the tree is a map, and every rational has a
unique address on it.

Nodes are integer pairs (n, d); the boundary 1/0 stands for infinity, so we
avoid real division entirely.

Four demonstrations:
  - "once"      — build the tree; verify uniqueness, lowest-terms, completeness
  - "neighbors" — verify b·c − a·d = 1 for every adjacent pair, every level
  - "path"      — the L/R address of a fraction is its continued fraction
  - "edges"     — what each edge carries: turn = matrix = mediant = bifurcation

Pure standard library.
"""
import argparse
from math import gcd


def mediant(a, b):
    """Mediant of integer-pair fractions a=(n,d), b=(n,d)."""
    return (a[0] + b[0], a[1] + b[1])


def build_levels(depth):
    """Return list of levels; level k is the ordered row after k insertions,
    grown between the boundaries 0/1 and 1/0."""
    row = [(0, 1), (1, 0)]           # 0  and  infinity
    levels = [row]
    for _ in range(depth):
        new = [row[0]]
        for i in range(len(row) - 1):
            new.append(mediant(row[i], row[i + 1]))
            new.append(row[i + 1])
        row = new
        levels.append(row)
    return levels


def inserted_nodes(levels):
    """All fractions ever inserted (excludes the two boundaries)."""
    seen = []
    for lvl in levels[1:]:
        # freshly inserted nodes sit at odd indices of each level
        for i in range(1, len(lvl), 2):
            seen.append(lvl[i])
    return seen


# --------------------------------------------------------------------------- #
# Demo A — every fraction once, in lowest terms
# --------------------------------------------------------------------------- #

def demo_once():
    print("=" * 70)
    print("A — every positive fraction, exactly once, already in lowest terms")
    print("=" * 70)
    print()
    depth = 12
    levels = build_levels(depth)
    nodes = inserted_nodes(levels)
    print(f"Grew the tree between 0/1 and 1/0 to depth {depth}: "
          f"{len(nodes)} fractions inserted.")
    print()

    # 1. lowest terms
    not_reduced = [(n, d) for (n, d) in nodes if gcd(n, d) != 1]
    print(f"  in lowest terms (gcd = 1)?      "
          f"{'ALL' if not not_reduced else str(len(not_reduced)) + ' FAIL'}")

    # 2. uniqueness
    as_set = set(nodes)
    print(f"  each produced exactly once?     "
          f"{'YES' if len(as_set) == len(nodes) else 'NO — duplicates found'}")

    # 3. completeness: every fraction p/q in lowest terms with q,p up to a
    #    bound must appear somewhere in the tree
    bound = 12
    want = {(p, q) for q in range(1, bound + 1) for p in range(1, bound + 1)
            if gcd(p, q) == 1}
    missing = sorted(want - as_set)
    print(f"  every p/q up to {bound}/{bound} present?   "
          f"{'YES' if not missing else str(len(missing)) + ' MISSING'}")
    if missing[:6]:
        print(f"      (missing sample: {missing[:6]})")
    print()
    print("One rule, run between 0 and infinity, lays down every positive")
    print("fraction once and only once, and never needs reducing — the tree")
    print("produces each ratio directly in lowest terms.")
    print()


# --------------------------------------------------------------------------- #
# Demo B — the neighbor invariant  b·c − a·d = 1
# --------------------------------------------------------------------------- #

def demo_neighbors():
    print("=" * 70)
    print("B — side-by-side fractions obey  b·c − a·d = 1  (unimodular)")
    print("=" * 70)
    print()
    depth = 12
    levels = build_levels(depth)
    print(f"Check every adjacent pair a/b, c/d at every level up to depth "
          f"{depth}: is b·c − a·d always 1?")
    print()
    worst = None
    total_pairs = 0
    for k, lvl in enumerate(levels):
        for i in range(len(lvl) - 1):
            (a, b), (c, d) = lvl[i], lvl[i + 1]
            det = b * c - a * d
            total_pairs += 1
            if det != 1:
                worst = (k, lvl[i], lvl[i + 1], det)
    print(f"  adjacent pairs checked: {total_pairs}")
    if worst is None:
        print(f"  b·c − a·d = 1 for EVERY pair at EVERY level:  CONFIRMED")
    else:
        print(f"  FAILED at level {worst[0]}: {worst[1]},{worst[2]} -> {worst[3]}")
    print()
    print("This determinant-1 property is exactly Module 4's 'as close as two")
    print("fractions can be.' It is preserved by every mediant insertion — the")
    print("new fraction is a neighbor of both parents — so it holds all the way")
    print("down. It is also why the mediant is always the simplest fraction in")
    print("the gap, hence (Module 3) the widest lock.")
    print()
    # show one level to make it concrete
    lvl = levels[4]
    row = "  ".join(f"{n}/{d}" for (n, d) in lvl)
    print(f"  level 4 row:  {row}")
    print()


# --------------------------------------------------------------------------- #
# Demo C — the L/R address of a fraction is its continued fraction
# --------------------------------------------------------------------------- #

def address_of(target):
    """Walk from 1/1 toward target using mediant boundaries; return L/R string."""
    p, q = target
    lo, hi = (0, 1), (1, 0)
    path = []
    for _ in range(10000):
        mid = mediant(lo, hi)
        if mid == (p, q):
            return "".join(path)
        # compare target to mid:  p/q  vs  mid[0]/mid[1]  via cross-multiply
        if p * mid[1] < mid[0] * q:
            path.append("L")
            hi = mid
        else:
            path.append("R")
            lo = mid
    return "".join(path)


def run_length_encode(s):
    if not s:
        return []
    out = []
    cur, n = s[0], 1
    for ch in s[1:]:
        if ch == cur:
            n += 1
        else:
            out.append((cur, n))
            cur, n = ch, 1
    out.append((cur, n))
    return out


def continued_fraction(p, q):
    cf = []
    while q:
        cf.append(p // q)
        p, q = q, p % q
    return cf


def matmul(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


# the two turns, as fixed 2x2 integer matrices
L_MAT = [[1, 0], [1, 1]]
R_MAT = [[1, 1], [0, 1]]


def path_matrix(word):
    """Multiply the L/R turns of an address into one 2x2 matrix."""
    M = [[1, 0], [0, 1]]                      # identity: the root, boundaries 1/0 and 0/1
    for ch in word:
        M = matmul(M, L_MAT if ch == "L" else R_MAT)
    return M


def node_of(word):
    """The fraction an address reaches: mediant of its matrix's two columns."""
    M = path_matrix(word)
    return (M[0][0] + M[0][1], M[1][0] + M[1][1])


def demo_edges():
    print("=" * 70)
    print("D — what each edge carries: a turn that is four things at once")
    print("=" * 70)
    print()
    print("A node is a ratio; an EDGE is the step between a ratio and its child.")
    print("Each edge is one turn, L or R, and that single turn is simultaneously")
    print("a matrix, a boundary, a mediant step, and a bifurcation to a narrower")
    print("lock. Walk a few addresses and watch all four fall out of the turns.")
    print()
    targets = ["LLR", "RLR", "LRRLLLLL"]
    for word in targets:
        M = path_matrix(word)
        a, c = M[0][0], M[0][1]
        b, d = M[1][0], M[1][1]
        node = (a + c, b + d)
        det = a * d - b * c                  # SL(2,Z): determinant is +1
        # order the two boundary columns by value so b*c - a*d = 1 reads as in the module
        cols = sorted([(a, b), (c, d)], key=lambda f: f[0] * 1.0 / f[1] if f[1] else float("inf"))
        (la, lb), (rc, rd) = cols
        neigh = lb * rc - la * rd
        print(f"  address {word}  ->  ratio {node[0]}/{node[1]}")
        print(f"    path-matrix [[{a} {c}] [{b} {d}]]   det = {det}   (unimodular, SL(2,Z))")
        print(f"    its two columns are the boundary neighbors {la}/{lb} and {rc}/{rd}")
        print(f"    the node is their mediant: ({la}+{rc})/({lb}+{rd}) = {node[0]}/{node[1]}")
        print(f"    neighbor invariant b*c - a*d = {neigh}  (the same 1 from demo B)")
        print()
    print("Now the physical reading — every edge steps to a NARROWER lock.")
    print("Complexity of a ratio = top + bottom (its Module-3 tongue is wider")
    print("when this is smaller). Down every edge, does complexity strictly grow?")
    print()
    # walk all addresses to depth 9 and compare each child to its parent
    ok = True
    checked = 0
    frontier = ["", "L", "R"]
    for depth in range(1, 10):
        words = []
        for w in _all_words(depth):
            parent = node_of(w[:-1])
            child = node_of(w)
            checked += 1
            if not (child[0] + child[1] > parent[0] + parent[1]):
                ok = False
    print(f"  parent->child complexity strictly increases on all {checked} "
          f"edges to depth 9:  {'CONFIRMED' if ok else 'FAILED'}")
    print()
    print("So an edge is never a lateral move. Every turn takes you from a lock")
    print("to a strictly finer one in the gap beside it — L toward the left")
    print("boundary, R toward the right. The tree's NODES are the locks; its")
    print("EDGES are the bifurcations between them, and the turn L/R is the")
    print("generator (of SL(2,Z)) that carries you across. Module 6 takes these")
    print("turns and asks what they do to a strip given a half-twist.")
    print()


def _all_words(depth):
    """All L/R words of exactly the given length."""
    if depth == 0:
        yield ""
        return
    for w in _all_words(depth - 1):
        yield w + "L"
        yield w + "R"


def demo_path():
    print("=" * 70)
    print("C — a fraction's left/right address is its continued fraction")
    print("=" * 70)
    print()
    print("From the top of the tree, each fraction is reached by a unique")
    print("sequence of Left/Right turns. The run-lengths of that sequence are")
    print("the fraction's continued fraction — its unique address.")
    print()
    targets = [(2, 5), (3, 7), (5, 3), (7, 4), (13, 19)]
    print(f"{'fraction':>10}  {'L/R address':>18}  {'run-lengths':>14}  "
          f"{'continued fraction':>20}")
    print(f"{'-'*10}  {'-'*18}  {'-'*14}  {'-'*20}")
    for (p, q) in targets:
        addr = address_of((p, q))
        rle = run_length_encode(addr)
        runs = [n for (_, n) in rle]
        cf = continued_fraction(p, q)
        print(f"{p:>4}/{q:<5}  {addr:>18}  {str(runs):>14}  {str(cf):>20}")
    print()
    print("The run-length pattern of the address matches the continued-fraction")
    print("digits (up to the standard last-term convention). Every rational has")
    print("one address; every address names one rational. The tree is a perfect")
    print("map of the ratios — the structure the framework's discrete side")
    print("lives on. Module 6 asks what happens to this map when the strip it")
    print("is drawn on is given a half-twist.")
    print()


# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description="Module 5 demonstrations.")
    parser.add_argument(
        "--demo", choices=["once", "neighbors", "path", "edges", "all"],
        default="all")
    args = parser.parse_args()
    if args.demo in ("once", "all"):
        demo_once()
    if args.demo in ("neighbors", "all"):
        demo_neighbors()
    if args.demo in ("path", "all"):
        demo_path()
    if args.demo in ("edges", "all"):
        demo_edges()


if __name__ == "__main__":
    main()
