#!/usr/bin/env python3
"""
Gap channels in the Farey sequence F₆ and Standard Model gauge bosons.

The Farey sequence F₆ has 13 fractions (|F₆| = 1 + Σ_{q=1}^{6} φ(q) = 13).
Between adjacent fractions there are 12 gaps.  The Standard Model has
8 + 3 + 1 = 12 gauge bosons (gluons + weak bosons + photon).

This script:
  1. Lists all 13 Farey fractions in F₆
  2. Lists all 12 gaps between adjacent fractions
  3. Classifies each gap by denominator parity (Klein bottle XOR logic)
     and by divisibility sector (q mod 2, q mod 3)
  4. Checks whether any natural grouping yields 8 + 3 + 1

Usage:
    python3 sync_cost/derivations/gap_channels.py
"""

import sys
from fractions import Fraction
from math import gcd

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))


# ============================================================
# 1. Build the Farey sequence F₆
# ============================================================

def farey_sequence(n):
    """Return the Farey sequence F_n as a list of Fraction objects."""
    fracs = set()
    for q in range(1, n + 1):
        for p in range(0, q + 1):
            if gcd(p, q) == 1:
                fracs.add(Fraction(p, q))
    return sorted(fracs)


def main():
    N = 6
    F6 = farey_sequence(N)

    print("=" * 75)
    print("  FAREY SEQUENCE F₆ : GAP CHANNELS AND GAUGE BOSONS")
    print("=" * 75)

    # ── 1. List all 13 fractions ────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print(f"  1. THE 13 FAREY FRACTIONS IN F₆  (|F₆| = {len(F6)})")
    print(f"{'─' * 75}\n")

    for i, f in enumerate(F6):
        print(f"    [{i:2d}]  {f}  =  {float(f):.6f}   (q = {f.denominator})")

    assert len(F6) == 13, f"Expected 13 fractions, got {len(F6)}"

    # ── 2. List all 12 gaps ────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print(f"  2. THE 12 GAPS BETWEEN ADJACENT FRACTIONS")
    print(f"{'─' * 75}\n")

    gaps = []
    for i in range(len(F6) - 1):
        left = F6[i]
        right = F6[i + 1]
        width = right - left
        # Farey neighbor property: |ad - bc| = 1 for a/b, c/d adjacent
        cross = right.numerator * left.denominator - left.numerator * right.denominator
        gaps.append({
            "index": i,
            "left": left,
            "right": right,
            "q_left": left.denominator,
            "q_right": right.denominator,
            "width": width,
            "cross": cross,
        })

    print(f"  {'#':>3s}  {'left':>6s}  {'right':>6s}  "
          f"{'q_L':>4s}  {'q_R':>4s}  {'width':>10s}  {'width_float':>12s}  {'|ad-bc|':>7s}")
    print("  " + "-" * 65)

    for g in gaps:
        print(f"  {g['index']:3d}  {str(g['left']):>6s}  {str(g['right']):>6s}  "
              f"{g['q_left']:4d}  {g['q_right']:4d}  "
              f"{str(g['width']):>10s}  {float(g['width']):12.6f}  {g['cross']:7d}")

    assert len(gaps) == 12, f"Expected 12 gaps, got {len(gaps)}"
    assert all(g["cross"] == 1 for g in gaps), "Farey neighbor property violated"
    print(f"\n  All 12 gaps satisfy |ad - bc| = 1  (Farey neighbor property)  [OK]")

    # ── 3. Denominator classes ─────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print(f"  3. DENOMINATOR PARITY CLASSIFICATION (KLEIN BOTTLE XOR)")
    print(f"{'─' * 75}\n")

    print("  Klein bottle XOR rule: q₁ + q₂ parity determines the sector.")
    print("  XOR = 1 (odd sum)  → cross-parity (one even, one odd q)")
    print("  XOR = 0 (even sum) → same-parity (both even or both odd q)")
    print()

    for g in gaps:
        qL, qR = g["q_left"], g["q_right"]
        parity_sum = (qL + qR) % 2
        g["xor"] = parity_sum  # 1 = cross-parity, 0 = same-parity
        g["parity_label"] = "cross" if parity_sum == 1 else "same"

        # Divisibility sectors
        g["div3"] = (qL % 3 == 0) or (qR % 3 == 0)
        g["div2"] = (qL % 2 == 0) or (qR % 2 == 0)
        g["boundary"] = (qL == 1) or (qR == 1)

    print(f"  {'#':>3s}  {'gap':>14s}  {'q_L':>4s}  {'q_R':>4s}  "
          f"{'q_L%2':>5s}  {'q_R%2':>5s}  {'XOR':>4s}  {'parity':>6s}  "
          f"{'div2':>5s}  {'div3':>5s}  {'bdry':>5s}")
    print("  " + "-" * 80)

    for g in gaps:
        print(f"  {g['index']:3d}  "
              f"{str(g['left'])+'/'+str(g['right']):>14s}  "
              f"{g['q_left']:4d}  {g['q_right']:4d}  "
              f"{g['q_left'] % 2:5d}  {g['q_right'] % 2:5d}  "
              f"{g['xor']:4d}  {g['parity_label']:>6s}  "
              f"{'Y' if g['div2'] else '.':>5s}  "
              f"{'Y' if g['div3'] else '.':>5s}  "
              f"{'Y' if g['boundary'] else '.':>5s}")

    # ── 4. Count by XOR parity ─────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print(f"  4. COUNTING BY XOR PARITY")
    print(f"{'─' * 75}\n")

    n_cross = sum(1 for g in gaps if g["xor"] == 1)
    n_same = sum(1 for g in gaps if g["xor"] == 0)

    print(f"  Cross-parity (XOR=1, odd q+q):  {n_cross}")
    print(f"  Same-parity  (XOR=0, even q+q): {n_same}")
    print(f"  Total: {n_cross + n_same}")

    # ── 5. Sector classification: try every natural grouping ──────────
    print(f"\n{'─' * 75}")
    print(f"  5. SEARCHING FOR 8 + 3 + 1 DECOMPOSITION")
    print(f"{'─' * 75}\n")

    # Classification A: by XOR parity and boundary status
    print("  --- Classification A: XOR parity + boundary ---")
    cat_A = {}
    for g in gaps:
        if g["boundary"]:
            label = "boundary (q=1 edge)"
        elif g["xor"] == 1:
            label = "cross-parity (XOR=1)"
        else:
            label = "same-parity (XOR=0)"
        cat_A.setdefault(label, []).append(g["index"])

    for label, indices in sorted(cat_A.items()):
        print(f"    {label:30s}  count = {len(indices):2d}  gaps: {indices}")

    counts_A = sorted([len(v) for v in cat_A.values()], reverse=True)
    match_A = counts_A == [8, 3, 1]
    print(f"  Partition: {'+'.join(str(c) for c in counts_A)}  "
          f"{'  *** MATCHES 8+3+1 ***' if match_A else ''}")

    # Classification B: by divisibility (div by 3, div by 2, neither)
    print("\n  --- Classification B: divisibility sectors ---")
    cat_B = {}
    for g in gaps:
        qL, qR = g["q_left"], g["q_right"]
        both_div3 = (qL % 3 == 0) and (qR % 3 == 0)
        both_div2 = (qL % 2 == 0) and (qR % 2 == 0)
        if both_div3:
            label = "both q div by 3"
        elif both_div2:
            label = "both q div by 2"
        elif g["boundary"]:
            label = "boundary (q=1)"
        else:
            label = "mixed"
        cat_B.setdefault(label, []).append(g["index"])

    for label, indices in sorted(cat_B.items()):
        print(f"    {label:30s}  count = {len(indices):2d}  gaps: {indices}")

    counts_B = sorted([len(v) for v in cat_B.values()], reverse=True)
    match_B = counts_B == [8, 3, 1]
    print(f"  Partition: {'+'.join(str(c) for c in counts_B)}  "
          f"{'  *** MATCHES 8+3+1 ***' if match_B else ''}")

    # Classification C: XOR with q-mod-3 refinement
    print("\n  --- Classification C: XOR parity with q mod 3 refinement ---")
    cat_C = {}
    for g in gaps:
        qL, qR = g["q_left"], g["q_right"]
        if g["xor"] == 1 and not g["div3"]:
            label = "cross-parity, no q div 3  (SU(3) candidate)"
        elif g["div3"]:
            label = "involves q div 3  (SU(2) candidate)"
        else:
            label = "same-parity, no q div 3  (U(1) candidate)"
        cat_C.setdefault(label, []).append(g["index"])

    for label, indices in sorted(cat_C.items()):
        print(f"    {label:45s}  count = {len(indices):2d}  gaps: {indices}")

    counts_C = sorted([len(v) for v in cat_C.values()], reverse=True)
    match_C = counts_C == [8, 3, 1]
    print(f"  Partition: {'+'.join(str(c) for c in counts_C)}  "
          f"{'  *** MATCHES 8+3+1 ***' if match_C else ''}")

    # Classification D: (q_L mod 6, q_R mod 6) orbit structure
    print("\n  --- Classification D: q mod 6 orbit structure ---")
    cat_D = {}
    for g in gaps:
        qL, qR = g["q_left"], g["q_right"]
        pair = (qL % 6, qR % 6)
        label = f"({qL%6}, {qR%6})"
        cat_D.setdefault(label, []).append(g["index"])

    for label, indices in sorted(cat_D.items()):
        print(f"    q mod 6 = {label:10s}  count = {len(indices):2d}  gaps: {indices}")

    # Group the mod-6 pairs by their sum mod 6
    print("\n  Grouped by (q_L + q_R) mod 6:")
    cat_D_sum = {}
    for g in gaps:
        s = (g["q_left"] + g["q_right"]) % 6
        cat_D_sum.setdefault(s, []).append(g["index"])

    for s, indices in sorted(cat_D_sum.items()):
        print(f"    (q_L + q_R) mod 6 = {s}  count = {len(indices):2d}  gaps: {indices}")

    counts_D = sorted([len(v) for v in cat_D_sum.values()], reverse=True)
    match_D = counts_D == [8, 3, 1]
    print(f"  Partition: {'+'.join(str(c) for c in counts_D)}  "
          f"{'  *** MATCHES 8+3+1 ***' if match_D else ''}")

    # Classification E: by max(q_L, q_R)
    print("\n  --- Classification E: by max(q_L, q_R) ---")
    cat_E = {}
    for g in gaps:
        m = max(g["q_left"], g["q_right"])
        cat_E.setdefault(m, []).append(g["index"])

    for m, indices in sorted(cat_E.items()):
        print(f"    max(q) = {m}  count = {len(indices):2d}  gaps: {indices}")

    # Classification F: by q_L * q_R (product = 1/width since |ad-bc|=1)
    print("\n  --- Classification F: by gap width = 1/(q_L * q_R) ---")
    cat_F = {}
    for g in gaps:
        prod = g["q_left"] * g["q_right"]
        cat_F.setdefault(prod, []).append(g["index"])

    for prod, indices in sorted(cat_F.items()):
        print(f"    q_L*q_R = {prod:3d}  width = 1/{prod:<3d}  "
              f"count = {len(indices):2d}  gaps: {indices}")

    # Classification G: XOR parity refined by boundary
    # cross-parity non-boundary, same-parity non-boundary, boundary
    print("\n  --- Classification G: XOR + boundary (explicit 3-way) ---")
    groups = {"cross-parity (non-boundary)": [], "same-parity (non-boundary)": [],
              "boundary": []}
    for g in gaps:
        if g["boundary"]:
            groups["boundary"].append(g["index"])
        elif g["xor"] == 1:
            groups["cross-parity (non-boundary)"].append(g["index"])
        else:
            groups["same-parity (non-boundary)"].append(g["index"])

    for label, indices in groups.items():
        print(f"    {label:35s}  count = {len(indices):2d}  gaps: {indices}")

    counts_G = sorted([len(v) for v in groups.values()], reverse=True)
    match_G = counts_G == [8, 3, 1]
    print(f"  Partition: {'+'.join(str(c) for c in counts_G)}  "
          f"{'  *** MATCHES 8+3+1 ***' if match_G else ''}")

    # ── 6. Gap widths at K=1 ───────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print(f"  6. GAP WIDTHS AT K=1")
    print(f"{'─' * 75}\n")

    total_width = sum(float(g["width"]) for g in gaps)
    print(f"  {'#':>3s}  {'left':>6s} → {'right':>6s}  "
          f"{'width':>12s}  {'width (float)':>14s}  {'fraction of [0,1]':>18s}")
    print("  " + "-" * 65)

    for g in gaps:
        w = g["width"]
        print(f"  {g['index']:3d}  {str(g['left']):>6s} → {str(g['right']):>6s}  "
              f"{str(w):>12s}  {float(w):14.6f}  {float(w)/total_width:18.4%}")

    print(f"\n  Total width: {total_width:.6f}  (must be 1.0: "
          f"{'OK' if abs(total_width - 1.0) < 1e-12 else 'FAIL'})")

    # ── 7. Summary: which classifications give 8+3+1 ──────────────────
    print(f"\n{'─' * 75}")
    print(f"  7. SUMMARY: DOES ANY CLASSIFICATION GIVE 8 + 3 + 1?")
    print(f"{'─' * 75}\n")

    results = [
        ("A: XOR + boundary", counts_A, match_A),
        ("B: divisibility sectors", counts_B, match_B),
        ("C: XOR + q mod 3", counts_C, match_C),
        ("D: (q_L+q_R) mod 6", counts_D, match_D),
        ("G: XOR + boundary (3-way)", counts_G, match_G),
    ]

    any_match = False
    for name, counts, match in results:
        status = "MATCH" if match else "no"
        if match:
            any_match = True
        print(f"    {name:35s}  {'+'.join(str(c) for c in counts):15s}  "
              f"8+3+1? {status}")

    print()
    if any_match:
        print("  *** At least one natural classification gives 8 + 3 + 1. ***")
        print()
        # Print which one(s) match and the physical interpretation
        for name, counts, match in results:
            if match:
                print(f"  Matching classification: {name}")
        print()
        print("  Physical interpretation:")
        print("    - The 12 Farey gaps of F₆ decompose into three sectors")
        print("    - The decomposition matches the gauge boson count 8 + 3 + 1")
        print("    - 8 cross-parity gaps  ↔  8 gluons     (SU(3) color)")
        print("    - 3 same-parity gaps   ↔  3 weak bosons (SU(2) weak)")
        print("    - 1 boundary gap       ↔  1 photon      (U(1) EM)")
    else:
        print("  No natural classification yields exactly 8 + 3 + 1.")
        print("  The 12 gap channels do NOT trivially decompose as")
        print("  8 + 3 + 1 under the classifications tested.")

    print(f"\n{'=' * 75}")


if __name__ == "__main__":
    main()
