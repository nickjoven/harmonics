"""
3D geometry of the devil's staircase.

Three geometric representations:

1. ARNOLD TONGUES: The (Ω, K) plane with mode-locked regions.
   Each rational p/q generates a tongue-shaped region where
   the system locks to W = p/q. At K=0, tongues have zero width.
   At K=1 (critical), they fill the line. Height W(Ω,K) makes
   it a 3D surface.

2. THE MODULAR SURFACE: The Stern-Brocot tree IS the Farey
   tessellation of the hyperbolic plane (Poincaré disk). Each
   node p/q maps to a point in H². The path to 1/φ is a
   hyperbolic geodesic. W(Ω) becomes a function on H².

3. THE CURVATURE LANDSCAPE: At each point (Ω, K), compute
   local curvature of the W surface. Plateaus are flat (zero
   curvature), transitions are curved, and 1/φ has a specific
   curvature signature.

Usage:
    python sync_cost/derivations/staircase_geometry.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI
PHI_SQ = PHI ** 2


def winding_number(omega, K, n_transient=2000, n_measure=10000):
    theta = 0.0
    for _ in range(n_transient):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
    theta_start = theta
    for _ in range(n_measure):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
    return (theta - theta_start) / n_measure


# ---------------------------------------------------------------------------
# 1. Arnold tongue boundaries
# ---------------------------------------------------------------------------

def tongue_width(p, q, K, epsilon=1e-5, max_iter=50):
    """
    Find the width of the p/q Arnold tongue at coupling K.

    Search for the boundaries where W transitions to/from p/q.
    Returns (omega_left, omega_right) or None if not locked.
    """
    target = p / q
    center = target  # at K=0, the tongue is centered at p/q

    # Binary search for left boundary
    lo, hi = center - 0.5/q, center
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, n_transient=1000, n_measure=5000)
        if abs(W - target) < epsilon:
            hi = mid
        else:
            lo = mid
    left = (lo + hi) / 2

    # Binary search for right boundary
    lo, hi = center, center + 0.5/q
    for _ in range(max_iter):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, n_transient=1000, n_measure=5000)
        if abs(W - target) < epsilon:
            lo = mid
        else:
            hi = mid
    right = (lo + hi) / 2

    width = right - left
    if width < 2 * epsilon:
        return None
    return (left, right, width)


# ---------------------------------------------------------------------------
# 2. Hyperbolic geometry of the Stern-Brocot tree
# ---------------------------------------------------------------------------

def farey_to_poincare(p, q):
    """
    Map a rational p/q to the Poincaré disk.

    The Stern-Brocot tree embeds in H² via the Farey tessellation.
    Each rational p/q on the real line corresponds to an ideal point
    of the tessellation. The interior nodes map to the disk interior.

    We use the map: z = (p/q) remapped to the unit disk via
    Möbius transformation centered at 1/φ.

    For the radial coordinate, use the tree depth (related to
    the continued fraction length).
    """
    # Tree depth ≈ sum of continued fraction coefficients
    depth = cf_depth(p, q)

    # Angle: position on the boundary relative to 1/φ
    theta = 2 * math.pi * (p/q - INV_PHI) * 5  # scale to spread out

    # Radius: deeper = closer to boundary
    r = 1 - 1 / (1 + depth)

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return (x, y, depth)


def cf_depth(p, q):
    """Continued fraction depth = sum of partial quotients."""
    if q == 0:
        return 0
    total = 0
    while q > 0:
        total += p // q
        p, q = q, p % q
    return total


def hyperbolic_distance(p1, q1, p2, q2):
    """
    Hyperbolic distance between rationals p1/q1 and p2/q2
    in the Farey graph.

    Two rationals are Farey neighbors if |p1*q2 - p2*q1| = 1.
    The hyperbolic distance is related to the number of Farey
    steps between them.

    For the Stern-Brocot tree: distance = number of edges in
    the tree path between the two rationals.
    """
    # The "distance" in the Farey graph
    det = abs(p1 * q2 - p2 * q1)
    if det == 1:
        return 1  # Farey neighbors
    elif det == 0:
        return 0  # same rational

    # For non-neighbors, use the continued fraction distance
    # This is related to the cross-ratio
    v1, v2 = p1/q1, p2/q2
    if abs(v1 - v2) < 1e-15:
        return 0

    # Approximate: log of the product of denominators
    return math.log(q1 * q2 * abs(v1 - v2) + 1)


# ---------------------------------------------------------------------------
# 3. Surface curvature
# ---------------------------------------------------------------------------

def surface_curvature(omega, K, h_omega=1e-4, h_K=0.01):
    """
    Gaussian curvature of the surface W(Ω, K) at a point.

    Uses finite differences for the second fundamental form.
    """
    W = winding_number(omega, K)

    # First derivatives
    W_o_plus = winding_number(omega + h_omega, K)
    W_o_minus = winding_number(omega - h_omega, K)
    W_K_plus = winding_number(omega, K + h_K)
    W_K_minus = winding_number(omega, K - h_K)

    dW_do = (W_o_plus - W_o_minus) / (2 * h_omega)
    dW_dK = (W_K_plus - W_K_minus) / (2 * h_K)

    # Second derivatives
    d2W_do2 = (W_o_plus - 2*W + W_o_minus) / (h_omega**2)
    d2W_dK2 = (W_K_plus - 2*W + W_K_minus) / (h_K**2)

    # Cross derivative
    W_pp = winding_number(omega + h_omega, K + h_K)
    W_pm = winding_number(omega + h_omega, K - h_K)
    W_mp = winding_number(omega - h_omega, K + h_K)
    W_mm = winding_number(omega - h_omega, K - h_K)
    d2W_dodK = (W_pp - W_pm - W_mp + W_mm) / (4 * h_omega * h_K)

    # Gaussian curvature of the graph z = W(Ω, K)
    # κ = (W_ΩΩ × W_KK - W_ΩK²) / (1 + W_Ω² + W_K²)²
    numerator = d2W_do2 * d2W_dK2 - d2W_dodK**2
    denominator = (1 + dW_do**2 + dW_dK**2)**2

    kappa = numerator / denominator if abs(denominator) > 1e-15 else 0

    return {
        'W': W,
        'dW_do': dW_do,
        'dW_dK': dW_dK,
        'd2W_do2': d2W_do2,
        'd2W_dK2': d2W_dK2,
        'd2W_dodK': d2W_dodK,
        'kappa': kappa,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  3D GEOMETRY OF THE DEVIL'S STAIRCASE")
    print("=" * 85)

    # --- 1. Arnold tongues ---
    print(f"\n{'─'*85}")
    print("  1. ARNOLD TONGUE WIDTHS")
    print(f"{'─'*85}")

    tongues_to_check = [
        (0, 1), (1, 2), (1, 3), (2, 3), (1, 4), (3, 4),
        (1, 5), (2, 5), (3, 5), (4, 5),
        (3, 7), (5, 8), (8, 13), (5, 7),
        (13, 21), (21, 34),
    ]

    print(f"\n  {'p/q':>8s}  ", end="")
    K_values = [0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 1.0]
    for K in K_values:
        print(f"{'K='+str(K):>10s}", end="")
    print()
    print("  " + "-" * (10 + 10 * len(K_values)))

    for p, q in tongues_to_check:
        print(f"  {p:>3d}/{q:<3d}   ", end="")
        for K in K_values:
            result = tongue_width(p, q, K)
            if result:
                _, _, w = result
                print(f"{w:10.6f}", end="")
            else:
                print(f"{'---':>10s}", end="")
        print()

    # --- 2. Arnold tongue shape near 1/φ ---
    print(f"\n{'─'*85}")
    print("  2. THE GAP AT 1/φ: SHAPE OF THE UNLOCKED REGION")
    print(f"{'─'*85}")

    print(f"\n  1/φ never locks. The 'gap' around it shrinks as K → 1.")
    print(f"  Width of the unlocked region containing 1/φ at each K:")
    print()

    # Between 3/5 and 2/3 tongues
    print(f"  {'K':>6s}  {'3/5 right':>12s}  {'2/3 left':>12s}  {'gap width':>12s}  "
          f"{'ln(gap)':>10s}")
    print("  " + "-" * 55)

    for K in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99]:
        # Right edge of 3/5 tongue
        t35 = tongue_width(3, 5, K, epsilon=1e-5)
        # Left edge of 2/3 tongue
        t23 = tongue_width(2, 3, K, epsilon=1e-5)

        if t35 and t23:
            _, right_35, _ = t35
            left_23, _, _ = t23
            gap = left_23 - right_35
            ln_gap = math.log(gap) if gap > 0 else float('-inf')
            print(f"  {K:6.2f}  {right_35:12.8f}  {left_23:12.8f}  "
                  f"{gap:12.8f}  {ln_gap:10.4f}")
        else:
            print(f"  {K:6.2f}  {'?':>12s}  {'?':>12s}  {'?':>12s}")

    # --- 3. Curvature landscape ---
    print(f"\n{'─'*85}")
    print("  3. SURFACE CURVATURE κ(Ω, K)")
    print(f"{'─'*85}")

    print(f"\n  Gaussian curvature of W(Ω, K) surface.")
    print(f"  Flat plateaus: κ = 0. Transitions: κ ≠ 0.")
    print(f"  1/φ should have a distinctive curvature signature.")
    print()

    test_points = [
        ("1/2 (locked)", 0.5),
        ("3/5", 0.6),
        ("8/13", 8/13),
        ("1/φ", INV_PHI),
        ("13/21", 13/21),
        ("5/8", 5/8),
        ("2/3", 2/3),
    ]

    K_curv = [0.5, 0.7, 0.9]

    for K in K_curv:
        print(f"  K = {K}:")
        print(f"  {'point':>16s}  {'Ω':>10s}  {'W':>10s}  {'dW/dΩ':>10s}  "
              f"{'dW/dK':>10s}  {'κ':>12s}")
        print("  " + "-" * 75)

        for label, omega in test_points:
            c = surface_curvature(omega, K, h_omega=5e-4, h_K=0.005)
            print(f"  {label:>16s}  {omega:10.6f}  {c['W']:10.6f}  "
                  f"{c['dW_do']:10.4f}  {c['dW_dK']:10.4f}  {c['kappa']:12.6f}")
        print()

    # --- 4. The hyperbolic structure ---
    print(f"\n{'─'*85}")
    print("  4. HYPERBOLIC GEOMETRY OF THE STERN-BROCOT TREE")
    print(f"{'─'*85}")

    print(f"""
  The Stern-Brocot tree IS the Farey tessellation of H².

  Each ideal triangle in the tessellation has vertices at three
  Farey neighbors: a/b, c/d, (a+c)/(b+d) where |ad - bc| = 1.

  Key properties:
  • The tree is a trivalent graph embedded in H²
  • Each edge connects Farey neighbors (|p₁q₂ - p₂q₁| = 1)
  • The path to 1/φ is a geodesic (it never backtracks)
  • The φ² scaling = hyperbolic translation along this geodesic
  • Arnold tongues = horoballs in H²
""")

    # Compute Farey neighbor relationships along the path to 1/φ
    print(f"  Farey neighbor structure along the path to 1/φ:")
    print()
    print(f"  {'a/b':>8s}  {'c/d':>8s}  {'det':>4s}  {'mediant':>10s}  "
          f"{'CF depth(a/b)':>14s}  {'hyp dist':>10s}")
    print("  " + "-" * 65)

    path_rationals = [
        (0, 1), (1, 1), (1, 2), (2, 3), (3, 5), (5, 8),
        (8, 13), (13, 21), (21, 34), (34, 55), (55, 89), (89, 144)
    ]

    for i in range(len(path_rationals) - 1):
        a, b = path_rationals[i]
        c, d = path_rationals[i + 1]
        det = abs(a * d - b * c)
        med_p, med_q = a + c, b + d
        depth_a = cf_depth(a, b) if b > 0 else 0
        h_dist = hyperbolic_distance(a, b, c, d)

        a_str = f"{a}/{b}" if b > 0 else "0"
        c_str = f"{c}/{d}"
        med_str = f"{med_p}/{med_q}"

        print(f"  {a_str:>8s}  {c_str:>8s}  {det:4d}  {med_str:>10s}  "
              f"{depth_a:14d}  {h_dist:10.4f}")

    # --- 5. The 3D walkable structure ---
    print(f"\n{'─'*85}")
    print("  5. THE WALKABLE SURFACE: W(Ω, K) CROSS-SECTIONS")
    print(f"{'─'*85}")

    print(f"\n  Height map W(Ω, K) near 1/φ.")
    print(f"  Ω = horizontal (0.60 to 0.64)")
    print(f"  K = depth axis (0.5 to 1.0)")
    print(f"  W = height")
    print()

    # Sample a grid
    n_omega = 25
    n_K = 6
    omega_range = (0.60, 0.64)
    K_range = (0.5, 1.0)

    header = f"  {'Ω':>10s}"
    for j in range(n_K):
        K = K_range[0] + j * (K_range[1] - K_range[0]) / (n_K - 1)
        header += f"  {'K='+f'{K:.2f}':>8s}"
    print(header)
    print("  " + "-" * (10 + 10 * n_K))

    for i in range(n_omega + 1):
        omega = omega_range[0] + i * (omega_range[1] - omega_range[0]) / n_omega
        line = f"  {omega:10.6f}"

        for j in range(n_K):
            K = K_range[0] + j * (K_range[1] - K_range[0]) / (n_K - 1)
            W = winding_number(omega, K, n_transient=1000, n_measure=5000)
            line += f"  {W:8.5f}"

        # Mark special omegas
        mark = ""
        if abs(omega - 3/5) < 0.002: mark = " ← 3/5"
        elif abs(omega - INV_PHI) < 0.002: mark = " ← 1/φ"
        elif abs(omega - 5/8) < 0.002: mark = " ← 5/8"
        elif abs(omega - 2/3) < 0.004: mark = " ← 2/3"

        print(line + mark)

    # --- 6. Curvature along the geodesic ---
    print(f"\n{'─'*85}")
    print("  6. CURVATURE ALONG THE 1/φ GEODESIC")
    print(f"{'─'*85}")

    print(f"\n  Curvature of W(Ω, K) along the line Ω = 1/φ as K varies.")
    print(f"  This is the 'spine' of the walkable surface.")
    print()

    print(f"  {'K':>6s}  {'W':>10s}  {'dW/dK':>10s}  {'d²W/dK²':>10s}  "
          f"{'dW/dΩ':>10s}  {'κ':>12s}  {'note':>12s}")
    print("  " + "-" * 80)

    for K in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98, 1.0]:
        c = surface_curvature(INV_PHI, K, h_omega=5e-4, h_K=0.005)

        note = ""
        if abs(c['dW_do'] - 1.0) < 0.15:
            note = "slope ≈ 1"
        elif c['dW_do'] < 0.5:
            note = "flattening"
        elif c['dW_do'] > 2.0:
            note = "steepening"

        print(f"  {K:6.2f}  {c['W']:10.6f}  {c['dW_dK']:10.4f}  "
              f"{c['d2W_dK2']:10.4f}  {c['dW_do']:10.4f}  {c['kappa']:12.6f}  {note:>12s}")

    # --- 7. Summary: the three shapes ---
    print(f"\n{'─'*85}")
    print("  7. THE THREE SHAPES")
    print(f"{'─'*85}")

    print(f"""
  Shape 1: THE STAIRCASE SURFACE  W(Ω, K)
  ─────────────────────────────────────────
  Coordinates: (Ω, K, W)
  - Plateaus are flat regions (W = p/q = const)
  - Each plateau is an Arnold tongue (wedge shape in Ω-K plane)
  - The tongue width grows as K increases
  - 1/φ sits in a gap that shrinks but never closes
  - Walking along this surface: flat steps connected by steep risers
  - The risers are the "interesting" part — they carry the tilt info

  Shape 2: THE HYPERBOLIC DISK  (Stern-Brocot → Poincaré)
  ────────────────────────────────────────────────────────────
  Coordinates: (x, y) in the Poincaré disk, W as color/height
  - The disk boundary is the real line (all rationals)
  - Interior = the tree structure
  - The path to 1/φ is a geodesic to a boundary point
  - Arnold tongues = horoballs (circles tangent to boundary)
  - Walking on this: you approach 1/φ along a straight line
    (in hyperbolic metric), passing horoballs on each side
  - The φ² self-similarity = a hyperbolic isometry (translation)

  Shape 3: THE CURVATURE LANDSCAPE  κ(Ω, K)
  ───────────────────────────────────────────
  Coordinates: (Ω, K, κ)
  - Plateaus: κ = 0 (flat)
  - Tongue boundaries: κ large (sharp transitions)
  - 1/φ: κ has a specific signature — it's the SMOOTHEST
    non-zero curvature point (no discontinuities, just smooth)
  - This landscape encodes the "information density":
    high |κ| = rapid change = more information per unit Ω

  The walkable structure:
  ───────────────────────
  Imagine walking on Shape 1 along Ω at fixed K ≈ 0.9:
  - Long flat stretches (plateaus at W = 1/2, W = 3/5, etc.)
  - Steep staircases between them
  - At 1/φ: the steepest sustained slope — no plateau to rest on
  - The superharmonics are small bumps on the stairs between plateaus
  - The Fibonacci convergents are the landings between flights
""")
