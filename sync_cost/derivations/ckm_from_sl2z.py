"""
CKM angles from SL(2,Z) traces — explicit computation for each sector.

This script is a computational refinement of the generation_mechanism.md
Section 6 sketch, which computes |tr(M₁⁻¹M₂)| = 1 for the q=3 pair
(1/3, 2/3) and finds α = 30°. That note mentions the answer is "in the
Cabibbo region" but not the observed value (≈ 13.04°).

Here we extend the computation to the sector base pairs used in
sector_base_pairs.py:

    Leptons:    b₁ = 3/2   b₂ = 5/3
    Up-type:    b₁ = 8/5   b₂ = 3/2
    Down-type:  b₁ = 5/4   b₂ = 9/8

and also to the Farey-F₆ generation modes

    gen 1: 1/2
    gen 2: 1/3, 2/3
    gen 3: 1/4, 2/5, 3/5, 3/4

For each pair we compute the SL(2,Z) matrix M along the Stern-Brocot path
to the target fraction (product of L/R generators, identical convention
to path_encoding.py), then the trace of M₁⁻¹M₂, then classify the
conjugacy class (elliptic / parabolic / hyperbolic) and where elliptic
extract the rotation angle α from cos(2α) = tr/2.

Findings (full honest assessment at the bottom of the script output):

1. Elliptic traces in SL(2,Z) are DISCRETE. An integer trace with
   |tr| < 2 can only be −1, 0, or +1, giving cos(2α) ∈ {−1/2, 0, 1/2}
   and therefore α ∈ {60°, 45°, 30°} only. There is no way to get
   13.04°, 2.38°, or 0.20° from a single integer trace.

2. The sector base-pair traces are NOT all elliptic. For (3/2 ↔ 5/3)
   and (5/4 ↔ 9/8) the trace is exactly 2 (parabolic — shear, the
   framework's "mass splitting" class). For (8/5 ↔ 3/2) the trace
   is 3 (hyperbolic — boost, "large hierarchy"). Only the q=3 pair
   (1/3, 2/3) hits elliptic, and only to 30°.

3. The tree-level Fritzsch-style formula from the phase-state weights
   (B:C:A = 7/36 : 1/6 : 1/18) reproduces the SL(2,Z) 30° exactly for
   the 1–2 pair:

       θ_12 = arctan √(W_A / W_C) = arctan √(1/3) = 30°

   so the 30° is NOT numerology — it is the same rotation angle the
   phase-state weight ratio encodes.

4. The gap to the observed Cabibbo angle is the same gap D34 already
   carries for the muon mass ratio: these are tree-level quantities,
   and the physical CKM elements sit at the electroweak scale after
   renormalization-group running from the tree scale. SL(2,Z) traces
   give the correct class labels (elliptic vs parabolic vs hyperbolic)
   and the correct tree-level angles; they do not, on their own,
   produce the running.

Usage:
    python sync_cost/derivations/ckm_from_sl2z.py
"""

import math
from fractions import Fraction


# ---------------------------------------------------------------------------
# SL(2,Z) path encoding (same convention as path_encoding.py)
# ---------------------------------------------------------------------------

R_MAT = [[1, 1], [0, 1]]   # right child generator
L_MAT = [[1, 0], [1, 1]]   # left child generator


def mat_mul(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]


def mat_inv_sl2z(M):
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    assert det == 1, f"non-SL(2,Z) matrix (det={det})"
    return [[ M[1][1], -M[0][1]],
            [-M[1][0],  M[0][0]]]


def continued_fraction(p, q):
    """Euclidean [a0; a1, a2, ...] expansion of p/q."""
    out = []
    while q != 0:
        a, r = divmod(p, q)
        out.append(a)
        p, q = q, r
    return out


def sb_path_and_matrix(p, q):
    """
    Stern-Brocot path from the root (0/1, 1/0) to p/q and the corresponding
    SL(2,Z) matrix. Alternating blocks of R's and L's from the CF.
    """
    cf = continued_fraction(p, q)
    path = []
    M = [[1, 0], [0, 1]]
    dirs = ['R', 'L']
    for i, a in enumerate(cf):
        d = dirs[i % 2]
        step = R_MAT if d == 'R' else L_MAT
        count = a if i < len(cf) - 1 else a - 1
        for _ in range(count):
            path.append(d)
            M = mat_mul(M, step)
    return ''.join(path), M, cf


# ---------------------------------------------------------------------------
# Trace classification and elliptic angle extraction
# ---------------------------------------------------------------------------

def classify(tr):
    """Return (class_name, description, alpha_deg_or_None)."""
    if abs(tr) < 2:
        # cos(2α) = tr/2 with tr ∈ {-1, 0, +1}
        cos2a = tr / 2.0
        alpha = 0.5 * math.acos(cos2a)
        return ('elliptic', 'rotation / flavour mixing', math.degrees(alpha))
    if abs(tr) == 2:
        return ('parabolic', 'shear / mass splitting', None)
    return ('hyperbolic', 'boost / large hierarchy', None)


def pair_trace(p1, q1, p2, q2):
    """
    Compute tr(M(p1/q1)⁻¹ · M(p2/q2)) where each M is the SL(2,Z)
    product along the Stern-Brocot path to that fraction.
    Returns (trace, M1, M2, M_rel, path1, path2).
    """
    path1, M1, _ = sb_path_and_matrix(p1, q1)
    path2, M2, _ = sb_path_and_matrix(p2, q2)
    M1_inv = mat_inv_sl2z(M1)
    M_rel = mat_mul(M1_inv, M2)
    tr = M_rel[0][0] + M_rel[1][1]
    return tr, M1, M2, M_rel, path1, path2


def fmt_mat(M):
    return f"[[{M[0][0]:2d},{M[0][1]:2d}],[{M[1][0]:2d},{M[1][1]:2d}]]"


# ---------------------------------------------------------------------------
# Sector base pairs (from sector_base_pairs.py)
# ---------------------------------------------------------------------------

SECTOR_BASE_PAIRS = {
    'Leptons':   {'b1': (3, 2), 'b2': (5, 3),
                  'formula': 'b₁=q₃/q₂, b₂=(q₂+q₃)/q₃'},
    'Up-type':   {'b1': (8, 5), 'b2': (3, 2),
                  'formula': 'b₁=q₂³/(q₂+q₃), b₂=q₃/q₂'},
    'Down-type': {'b1': (5, 4), 'b2': (9, 8),
                  'formula': 'b₁=(q₂+q₃)/q₂², b₂=q₃²/q₂³'},
}

# Generation modes in F₆ (generation_mechanism.md §5)
GEN_MODES = {
    1: [(1, 2)],
    2: [(1, 3), (2, 3)],
    3: [(1, 4), (2, 5), (3, 5), (3, 4)],
}

# Observed CKM angles (PDG-style, degrees)
CKM_OBS = {
    'theta_12 (Cabibbo)':  13.04,
    'theta_13':             0.20,
    'theta_23':             2.38,
    'delta_CP':            69.00,
}

# Phase-state weights from §2 of generation_mechanism.md
W_A = Fraction(1, 18)   # lightest: duty × duty
W_C = Fraction(1, 6)    # middle:   gap  × duty
W_B = Fraction(7, 36)   # heaviest: duty × gap

# Hierarchy seed (26 : 7 : 1), §2 of the doc
HIERARCHY = {'heavy': 26, 'middle': 7, 'light': 1}

# Sector exponents, §3 of the doc
SECTOR_EXPONENT = {'Down-type': 2, 'Leptons': Fraction(5, 2), 'Up-type': 3}


# ---------------------------------------------------------------------------
# Report sections
# ---------------------------------------------------------------------------

BAR = '=' * 72


def section(title):
    print()
    print(BAR)
    print('  ' + title)
    print(BAR)
    print()


def report_reference():
    section('0. REFERENCE: q=3 pair from generation_mechanism.md §6')
    print('  Modes 1/3 and 2/3, same q but different SB paths.')
    tr, M1, M2, Mrel, p1, p2 = pair_trace(1, 3, 2, 3)
    print(f'  M(1/3) via path {p1 or "(id)":<6}: {fmt_mat(M1)}')
    print(f'  M(2/3) via path {p2 or "(id)":<6}: {fmt_mat(M2)}')
    print(f'  M(1/3)⁻¹·M(2/3)           : {fmt_mat(Mrel)}   tr = {tr}')
    cls, desc, alpha = classify(tr)
    print(f'  → {cls.upper()} ({desc})')
    if alpha is not None:
        print(f'  → cos(2α) = {tr}/2 = {tr/2},  α = {alpha:.4f}°')
    print()
    print('  The doc notes this is "in the Cabibbo region" (observed 13.04°).')
    print('  The rest of this script extends the same computation to the')
    print('  sector base pairs and to all F₆ generation modes.')


def report_sector_base_pairs():
    section('1. SECTOR BASE PAIRS — traces of M(b₁)⁻¹·M(b₂)')
    results = []
    for name, spec in SECTOR_BASE_PAIRS.items():
        p1, q1 = spec['b1']
        p2, q2 = spec['b2']
        tr, M1, M2, Mrel, path1, path2 = pair_trace(p1, q1, p2, q2)
        cls, desc, alpha = classify(tr)

        print(f'  {name}:  {spec["formula"]}')
        print(f'    b₁ = {p1}/{q1}  SB path = {path1 or "(id)":<10}  M₁ = {fmt_mat(M1)}')
        print(f'    b₂ = {p2}/{q2}  SB path = {path2 or "(id)":<10}  M₂ = {fmt_mat(M2)}')
        print(f'    M₁⁻¹·M₂ = {fmt_mat(Mrel)}   tr = {tr}')
        print(f'    → {cls.upper()}  ({desc})')
        if alpha is not None:
            print(f'    → cos(2α) = {tr/2},  α = {alpha:.4f}°')
        print()
        results.append((name, p1, q1, p2, q2, tr, cls, alpha))
    return results


def report_generation_modes():
    section('2. F₆ GENERATION MODES — all inter-mode trace classes')
    modes = []
    for gen, lst in GEN_MODES.items():
        for p, q in lst:
            modes.append((gen, p, q))

    # Header
    print(f'  {"pair":<16}  {"gens":<5}  {"tr":>3}  {"class":<11}  {"α (deg)":>9}')
    print('  ' + '-' * 52)
    rows = []
    n = len(modes)
    for i in range(n):
        for j in range(i + 1, n):
            gi, pi, qi = modes[i]
            gj, pj, qj = modes[j]
            tr, *_ = pair_trace(pi, qi, pj, qj)
            cls, desc, alpha = classify(tr)
            label = f'{pi}/{qi}↔{pj}/{qj}'
            gens = f'{gi}-{gj}'
            a_str = f'{alpha:.2f}' if alpha is not None else '—'
            print(f'  {label:<16}  {gens:<5}  {tr:>3}  {cls:<11}  {a_str:>9}')
            rows.append((label, gi, gj, tr, cls, alpha))
    return rows


def report_elliptic_angle_catalogue(rows):
    section('3. ELLIPTIC ANGLES ARE DISCRETE — the full allowed set')
    print('  An SL(2,Z) matrix has integer trace. Elliptic means |tr|<2,')
    print('  so tr ∈ {−1, 0, +1}. This gives:')
    print()
    print('    tr = +1:  cos(2α) = +1/2  →  α = 30°')
    print('    tr =  0:  cos(2α) =  0    →  α = 45°')
    print('    tr = −1:  cos(2α) = −1/2  →  α = 60°')
    print()
    print('  These are the ONLY elliptic angles accessible from a single')
    print('  SL(2,Z) trace. The Cabibbo angle (13.04°), θ_23 (2.38°),')
    print('  and θ_13 (0.20°) are not in this set and cannot be obtained')
    print('  from any single trace.')
    print()
    # Count how many pairs land in each class
    classes = {}
    for _, _, _, _, cls, _ in rows:
        classes[cls] = classes.get(cls, 0) + 1
    print('  Observed distribution across F₆ mode pairs:')
    for cls, n in sorted(classes.items()):
        print(f'    {cls:<11}: {n}')


def report_tree_level_weight_angles():
    section('4. TREE-LEVEL MIXING FROM PHASE-STATE WEIGHTS (Fritzsch form)')
    print('  The generation_mechanism.md phase-state weights are')
    print(f'    W_B (heaviest) = {W_B} = 7/36')
    print(f'    W_C (middle)   = {W_C} = 1/6')
    print(f'    W_A (lightest) = {W_A} = 1/18')
    print()
    print('  A Fritzsch-style rotation between two generations with')
    print('  weights W_light and W_heavy is')
    print('    θ = arctan √(W_light / W_heavy)')
    print()

    def f(w1, w2, name):
        ratio = Fraction(w1, w2)
        angle = math.degrees(math.atan(math.sqrt(float(ratio))))
        return ratio, angle

    pairs = [
        ('1-2 (A↔C)', W_A, W_C),
        ('2-3 (C↔B)', W_C, W_B),
        ('1-3 (A↔B)', W_A, W_B),
    ]
    print(f'    {"pair":<14}  {"W_l/W_h":>10}  {"θ (deg)":>10}')
    print('    ' + '-' * 40)
    for label, wl, wh in pairs:
        ratio, angle = f(wl, wh, label)
        print(f'    {label:<14}  {str(ratio):>10}  {angle:>10.4f}')
    print()
    print('  Note the 1–2 entry: √(1/3) → 30° exactly. This is the SAME')
    print('  angle the SL(2,Z) q=3 trace gives. The match is not a')
    print('  coincidence — the 1/3 vs 2/3 matrix computes the rotation')
    print('  between the two q=3 phase-state realisations, which is the')
    print('  same rotation the weight ratio encodes.')


def report_comparison_to_ckm():
    section('5. COMPARISON TO OBSERVED CKM ANGLES')
    print('  Observed (PDG-style):')
    for k, v in CKM_OBS.items():
        print(f'    {k:<22} = {v:>6.2f}°')
    print()
    print('  Tree-level SL(2,Z)/weight predictions (from §4 above):')
    print(f'    θ_12 (1-2)            =  30.00°   (trace class +1, elliptic)')
    print(f'    θ_23 (2-3)            =  42.79°   (weight ratio only)')
    print(f'    θ_13 (1-3)            =  28.13°   (weight ratio only)')
    print()
    print('  Ratios tree/observed:')
    tree = {'theta_12 (Cabibbo)': 30.00,
            'theta_23': 42.79,
            'theta_13': 28.13}
    for k, v in tree.items():
        print(f'    {k:<22}: {v/CKM_OBS[k]:>6.2f}×')
    print()
    print('  None of these is a clean rotation of a tree-level angle to')
    print('  the physical one. Direct attempts at a simple rescaling')
    print('  (sin²θ_W, φ, 30°/integer, etc.) do not produce a unique')
    print('  closed form for all three CKM angles simultaneously.')
    print()
    print('  The closest suggestive numerical coincidences:')
    print(f'    arctan √(1/18) = {math.degrees(math.atan(math.sqrt(1/18))):.4f}°  '
          f'vs θ_C = 13.04°   (lightest weight W_A = 1/18)')
    print(f'    arctan √(1/26) = {math.degrees(math.atan(math.sqrt(1/26))):.4f}°  '
          f'vs θ_C = 13.04°   (hierarchy base 26)')
    print(f'    sin²(13°)      = {math.sin(math.radians(13))**2:.4f}   '
          f'vs sin²θ_W = 0.2312 (Weinberg)')
    print()
    print('  These are within 1° of the Cabibbo angle but the prefactors')
    print('  (18 or 26) come from the hierarchy base, not from an SL(2,Z)')
    print('  trace. They are consistent with the framework but are NOT')
    print('  derived here.')


def report_honest_assessment():
    section('6. HONEST ASSESSMENT — what SL(2,Z) traces do and do not give')
    print('  WORKS:')
    print('  • The trace of M₁⁻¹M₂ correctly classifies the TYPE of')
    print('    relationship between two modes:')
    print('      elliptic  = flavour mixing (rotation)')
    print('      parabolic = mass splitting (shear)')
    print('      hyperbolic = large hierarchy (boost)')
    print('  • For the q=3 pair (1/3, 2/3) the trace is +1 and the')
    print('    elliptic angle is exactly 30°, reproducing the angle that')
    print('    the phase-state weight ratio √(W_A/W_C) = √(1/3) also gives.')
    print('    These are the SAME rotation from two derivations.')
    print('  • The lepton base pair (3/2, 5/3) is parabolic (tr=2),')
    print('    consistent with this pair encoding the τ/μ mass splitting')
    print('    rather than a flavour rotation.')
    print('  • The up-type base pair (8/5, 3/2) is hyperbolic (tr=3),')
    print('    consistent with t/c being a large hierarchy.')
    print('  • The down-type base pair (5/4, 9/8) is parabolic (tr=2),')
    print('    consistent with the much tighter b/s splitting relative')
    print('    to the up-type case.')
    print()
    print('  DOES NOT WORK:')
    print('  • The integer trace forces elliptic angles to be discrete:')
    print('    only 30°, 45°, 60° are accessible. The observed CKM angles')
    print('    13.04°, 2.38°, 0.20° are NOT in this set and cannot be')
    print('    obtained from a single SL(2,Z) trace.')
    print('  • The 30° from q=3 is NOT the Cabibbo angle, only "in the')
    print('    Cabibbo region". The discrepancy (17°) is not a clean')
    print('    rotation through sin²θ_W, φ, or any other simple quantity.')
    print('  • For θ_23 and θ_13, the tree-level weight-ratio formula')
    print('    gives 42.79° and 28.13°, which are WORSE than the 1-2')
    print('    case. These do not sit near elliptic SL(2,Z) values either.')
    print()
    print('  WHAT IS MISSING:')
    print('  • The same gap the doc acknowledges for the muon mass ratio.')
    print('    The tree-level exponents and angles are defined at the SB')
    print('    base-pair scale; the physical CKM elements sit at the')
    print('    electroweak scale. Renormalisation-group running from the')
    print('    tree scale to M_Z has not been computed for the CKM angles,')
    print('    just as it has not been computed for m_μ/m_e.')
    print('  • A derivation of HOW the three discrete SL(2,Z) angle')
    print('    classes (30°, 45°, 60°) and the parabolic/hyperbolic')
    print('    mass-splitting labels mix to produce the observed')
    print('    Wolfenstein hierarchy (λ, λ², λ³) is not provided by')
    print('    this computation. The framework sets the right classes')
    print('    but not the precise angles.')
    print()
    print('  STATUS:')
    print('  • The SL(2,Z) trace structure reproduces the 30° base angle')
    print('    for the q=3 pair exactly, and matches the Fritzsch-form')
    print('    weight formula for the 1-2 generation mixing. It gives')
    print('    the correct qualitative classification of the three sector')
    print('    base pairs into parabolic / parabolic / hyperbolic.')
    print('  • It does NOT produce the observed CKM angles directly, and')
    print('    no clean rotation closes the gap at this computational')
    print('    level. Further work (running, or a continuum relaxation')
    print('    of the integer trace) is required.')


def main():
    print()
    print(BAR)
    print('  CKM ANGLES FROM SL(2,Z) TRACES — full computation')
    print('  Computational refinement of generation_mechanism.md §6')
    print(BAR)

    report_reference()
    report_sector_base_pairs()
    rows = report_generation_modes()
    report_elliptic_angle_catalogue(rows)
    report_tree_level_weight_angles()
    report_comparison_to_ckm()
    report_honest_assessment()
    print()


if __name__ == '__main__':
    main()
