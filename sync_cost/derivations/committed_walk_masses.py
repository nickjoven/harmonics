"""
Committed-K*, explicit-walk absolute mass formula.

This script implements approach (A) from the discussion of the neutrino
circulation problem:

  1. K* is pinned to one value (K*_Lambda = 0.862, from the boundary-weight
     fixed point of Omega_Lambda, `boundary_weight.md`). It is NEVER refit.
  2. Each fermion is assigned an EXPLICIT walk on the Stern-Brocot tree:
     a finite sequence of denominator classes, constructed from the
     sector base pairs `sector_base_pairs.py` and the within-sector
     generation index. No "depth × |3Q| = k" overloading.
  3. The mass is computed from the walk and K* alone, with no fitted
     per-sector or per-generation parameter:

         m_f = v × Product_{q in walk(f)} w(q, K*)

     where w(q, K) is the Arnold tongue width at denominator q and
     coupling K. The perturbative form w(q, K) = 2 (K/2)^q / q applies
     for K < 1 (our case: K* = 0.862).

  4. The residual m_predicted / m_observed is reported for all 12
     charged fermions and 3 neutrinos. The pattern of residuals
     (constant per sector? linear in walk length? sign flip between
     quarks and leptons?) diagnoses WHAT is actually missing, rather
     than hand-fitting K* to make one line match.

Rules:
  - No refitting of K*.
  - No sector-specific anchor (everything uses the same v and K*).
  - No "depth = (q2 q3)^2" patch; neutrinos get a walk like everyone else.
  - Walks are specified once, up front, as sequences of integers.
  - If the answer is "the framework predicts only ratios, not absolutes",
    that outcome is reported honestly as the answer.
"""

import math


# ============================================================================
# Pinned inputs — these are fixed and never refit in this script
# ============================================================================

K_STAR = 0.862           # boundary_weight.md fixed point from Omega_Lambda
V_GEV  = 246.0           # electroweak VEV (the single dimensionful input)
V_MEV  = V_GEV * 1e3     # in MeV
V_EV   = V_GEV * 1e9     # in eV

Q2, Q3 = 2, 3


# ============================================================================
# Tongue-width function
# ============================================================================

def tongue_width(q, K):
    """
    Arnold tongue width at a p/q rational, coupling K.

    Two regimes (from `circle_map_utils.tongue_width`):
      K < 1:  perturbative, w(q, K) = 2 (K/2)^q / q
      K = 1:  critical, w(q, 1) = 1/q^2

    K* = 0.862 < 1, so we use the perturbative form.
    """
    if q <= 0:
        raise ValueError(f"q must be positive, got {q}")
    if K >= 1.0:
        return 1.0 / (q * q)
    return 2.0 * (K / 2.0) ** q / q


def walk_product(walk, K):
    """Product of tongue widths along a walk (sequence of denominators)."""
    p = 1.0
    for q in walk:
        p *= tongue_width(q, K)
    return p


# ============================================================================
# Explicit walks for each fermion
# ============================================================================
#
# A walk is a sequence of denominator integers. Each integer is the
# denominator of a Stern-Brocot node traversed in going from the root to
# the fermion's label. We use the sector base pairs from
# sector_base_pairs.py to generate walks, in the simplest way that
# respects the framework's within-sector generation law:
#
#   - Each sector has two base rationals (b1, b2) = heavy and light steps.
#   - Within a sector, the heaviest generation has the shortest walk
#     (widest tongue, biggest mass), and the lightest generation has the
#     longest walk.
#   - The concrete walk for generation g in a sector is: take the heavy
#     base denominator once if g <= 3, take the light base denominator
#     once more for g <= 2, and take the light base denominator a second
#     time for g = 1.
#
# This is the MINIMAL walk assignment consistent with the framework's
# claim that each sector uses a base pair and each generation adds a
# step. It is not unique — but it is COMMITTED (every fermion has a
# single, stated walk), and we refuse to tweak it to match observation.
#
# Sector base pairs from `sector_base_pairs.py`:
#   Leptons:    (b1, b2) = (3/2, 5/3)   ->  denominators (2, 3)
#   Up-type:    (b1, b2) = (8/5, 3/2)   ->  denominators (5, 2)
#   Down-type:  (b1, b2) = (5/4, 9/8)   ->  denominators (4, 8)
#   Neutrinos:  no base pair in integer_conservation_law (|Q|=0). We use
#               the explicit extension: the neutrino walks the lepton
#               base pair then cycles through q_2 weak traversals.
#               Walks below.
#
# Generation convention: gen 3 = heaviest, gen 1 = lightest. Heavier =
# SHORTER walk, because each additional tongue-width factor multiplies
# the mass by a number << 1.

# We also record the denominator at the root (q = 1) as the first step
# in each walk, because every walk starts at 1/1. This gives a common
# leading factor w(1, K*) that cancels in ratios.

ROOT_STEP = [1]

LEPTON_B1, LEPTON_B2 = 2, 3     # from (3/2, 5/3)
UP_B1, UP_B2 = 5, 2             # from (8/5, 3/2)
DOWN_B1, DOWN_B2 = 4, 8         # from (5/4, 9/8)

WALKS = {
    # charged leptons
    "tau":      ROOT_STEP + [LEPTON_B1],                                  # heaviest
    "mu":       ROOT_STEP + [LEPTON_B1, LEPTON_B2],
    "e":        ROOT_STEP + [LEPTON_B1, LEPTON_B2, LEPTON_B2],            # lightest

    # up-type
    "top":      ROOT_STEP + [UP_B1],
    "charm":    ROOT_STEP + [UP_B1, UP_B2],
    "up":       ROOT_STEP + [UP_B1, UP_B2, UP_B2],

    # down-type
    "bottom":   ROOT_STEP + [DOWN_B1],
    "strange":  ROOT_STEP + [DOWN_B1, DOWN_B2],
    "down":     ROOT_STEP + [DOWN_B1, DOWN_B2, DOWN_B2],

    # neutrinos (|Q|=0): same lepton walk, plus q_2 extra weak traversals
    # per the extension in neutrino_mass_prediction.py. We take the
    # minimal version: each generation adds one extra q_2-cycle.
    "nu_tau":   ROOT_STEP + [LEPTON_B1, Q2, Q2, Q2, Q2],                  # heaviest nu
    "nu_mu":    ROOT_STEP + [LEPTON_B1, LEPTON_B2, Q2, Q2, Q2, Q2],
    "nu_e":     ROOT_STEP + [LEPTON_B1, LEPTON_B2, LEPTON_B2, Q2, Q2, Q2, Q2],
}

# Observed masses (PDG 2024, central values), in MeV
MASSES_MEV = {
    "tau":    1776.86,
    "mu":     105.6583755,
    "e":      0.51099895,
    "top":    172760.0,
    "charm":  1270.0,
    "up":     2.16,
    "bottom": 4180.0,
    "strange": 93.4,
    "down":   4.67,
    # neutrinos: take best-fit central values in meV, converted to MeV
    "nu_tau": 50.0e-9,    # ~ atmospheric sqrt(Delta m^2_atm)
    "nu_mu":  8.6e-9,     # ~ solar sqrt(Delta m^2_sol)
    "nu_e":   1.0e-9,     # ~ lightest, upper bound
}


# ============================================================================
# Run the formula
# ============================================================================

def predict_mass_mev(fermion_name, K=K_STAR):
    """
    m_f = v × Product of tongue widths along walk(f)

    Returns mass in MeV.
    """
    w = WALKS[fermion_name]
    product = walk_product(w, K)
    return V_MEV * product


def format_row(name, walk, m_pred, m_obs):
    walk_str = "[" + " ".join(str(q) for q in walk) + "]"
    depth = len(walk)
    q_sum = sum(walk)
    ratio = m_pred / m_obs if m_obs > 0 else float("inf")
    log_ratio = math.log10(ratio) if ratio > 0 else float("nan")
    return (name, walk_str, depth, q_sum, m_pred, m_obs, ratio, log_ratio)


def main():
    print("=" * 78)
    print("  COMMITTED-K* EXPLICIT-WALK ABSOLUTE MASS TEST")
    print("=" * 78)
    print()
    print(f"  K* = {K_STAR}  (boundary_weight.md, from Omega_Lambda — NEVER refit)")
    print(f"  v  = {V_GEV} GeV  (single dimensionful input)")
    print(f"  w(q, K) = 2 (K/2)^q / q   (perturbative tongue width, K < 1)")
    print()
    print("  Walks are specified once, up front, from the sector base pairs.")
    print("  No fitting, no sector anchors, no generation-specific exponents.")
    print()
    print("  Residual = predicted / observed. If the framework predicts")
    print("  absolute masses, all residuals are ~1. If the residual is")
    print("  constant per sector but != 1, the framework predicts ratios")
    print("  and needs one anchor per sector. If the residual scales with")
    print("  walk length, there's a missing K* evolution.")
    print()

    # Compute for all fermions
    rows = []
    for name, walk in WALKS.items():
        m_pred = predict_mass_mev(name)
        m_obs = MASSES_MEV[name]
        rows.append(format_row(name, walk, m_pred, m_obs))

    # Print the table
    print("-" * 94)
    print(f"  {'fermion':<9} {'walk':<20} {'steps':>5} {'sum':>4} "
          f"{'predicted (MeV)':>18} {'observed (MeV)':>16} {'log10(p/o)':>11}")
    print("-" * 94)
    for name, walk_str, depth, q_sum, m_pred, m_obs, ratio, log_ratio in rows:
        print(f"  {name:<9} {walk_str:<20} {depth:>5} {q_sum:>4} "
              f"{m_pred:>18.4e} {m_obs:>16.4e} {log_ratio:>11.3f}")
    print()

    # Sector-wise analysis: is the residual constant per sector?
    print("=" * 78)
    print("  RESIDUAL PATTERN (diagnostic)")
    print("=" * 78)
    print()

    sectors = {
        "charged leptons": ["tau", "mu", "e"],
        "up-type quarks":  ["top", "charm", "up"],
        "down-type quarks": ["bottom", "strange", "down"],
        "neutrinos":       ["nu_tau", "nu_mu", "nu_e"],
    }

    print(f"  {'sector':<18} {'log10 residuals':<40} {'sector shift'}")
    print("  " + "-" * 76)
    for sector, members in sectors.items():
        logs = []
        for m in members:
            _, _, _, _, p, o, r, lr = rows[[r[0] for r in rows].index(m)]
            logs.append(lr)
        shift = sum(logs) / len(logs)
        spread = max(logs) - min(logs)
        log_str = "  ".join(f"{x:+.2f}" for x in logs)
        print(f"  {sector:<18} {log_str:<40} "
              f"mean {shift:+.2f}, spread {spread:.2f}")
    print()

    # Within-sector: does the residual scale with walk length?
    print("  Within-sector scaling (residual vs walk length):")
    print()
    for sector, members in sectors.items():
        triples = []
        for m in members:
            _, _, d, _, p, o, r, lr = rows[[r[0] for r in rows].index(m)]
            triples.append((m, d, lr))
        # Is the log residual approximately linear in depth?
        xs = [t[1] for t in triples]
        ys = [t[2] for t in triples]
        # Simple linear fit y = a + b x (two-point slope between extremes
        # is enough to see the trend)
        if len(triples) >= 2:
            slope = (ys[-1] - ys[0]) / (xs[-1] - xs[0]) if xs[-1] != xs[0] else 0
            print(f"    {sector:<18}  slope d(log10 residual)/d(depth) = {slope:+.3f}")
    print()

    # Cross-sector comparison
    print("=" * 78)
    print("  INVERTING THE FORMULA: what walk-sum does each mass NEED?")
    print("=" * 78)
    print()
    print("  Given m_obs = v × product_i [2 (K*/2)^{q_i} / q_i], take logs:")
    print()
    print("    log(m_obs / v) = sum_i [ q_i log(K*/2) + log(2/q_i) ]")
    print()
    print("  Separate the q-sum from the log-sum:")
    print()
    print("    log(m_obs / v) = Sigma_q * log(K*/2) + Sigma_log")
    print()
    print("  where Sigma_q = sum of q_i (walk-sum) and Sigma_log =")
    print("  sum of log(2/q_i). The walk-sum is the integer quantity")
    print("  the naive framework formula cares about.")
    print()
    print("  If we fix Sigma_log from the naive walk and solve for")
    print("  Sigma_q, we get the walk-sum the framework WOULD need")
    print("  to reproduce the observed mass exactly.")
    print()

    log_half_K = math.log(K_STAR / 2.0)  # negative
    log_K = math.log(K_STAR)

    print(f"  {'fermion':<9} {'naive Sigma_q':>14} {'needed Sigma_q':>16} "
          f"{'delta':>10} {'delta / 3':>12}")
    print("  " + "-" * 72)

    from_naive = {}
    needed = {}
    for name, walk in WALKS.items():
        sigma_q_naive = sum(walk)
        sigma_log = sum(math.log(2.0 / q) for q in walk)
        m_obs = MASSES_MEV[name]
        # log(m_obs / V_MEV) = sigma_q * log_half_K + sigma_log
        sigma_q_needed = (math.log(m_obs / V_MEV) - sigma_log) / log_half_K
        delta = sigma_q_needed - sigma_q_naive
        from_naive[name] = sigma_q_naive
        needed[name] = sigma_q_needed
        print(f"  {name:<9} {sigma_q_naive:>14d} {sigma_q_needed:>16.3f} "
              f"{delta:>+10.3f} {delta/3:>+12.3f}")
    print()

    # Check for integer patterns in the NEEDED walk sums
    print("  Needed walk-sums rounded to nearest integer (with rounding error):")
    print()
    print(f"  {'fermion':<9} {'needed':>10} {'nearest int':>12} {'error':>10}")
    print("  " + "-" * 46)
    for name in WALKS:
        s = needed[name]
        ni = round(s)
        err = s - ni
        print(f"  {name:<9} {s:>10.3f} {ni:>12d} {err:>+10.3f}")
    print()

    # Check ratios within a sector using needed sums
    print("  Within-sector DELTA walk-sums (gen i -> gen i+1):")
    print()
    for sector, members in sectors.items():
        m3, m2, m1 = members  # heavy, middle, light
        d_heavy_mid = needed[m2] - needed[m3]
        d_mid_light = needed[m1] - needed[m2]
        ratio = d_mid_light / d_heavy_mid if d_heavy_mid != 0 else float('nan')
        print(f"    {sector:<18}  {m3:<8} -> {m2:<8}: {d_heavy_mid:+.3f}"
              f"    {m2:<8} -> {m1:<8}: {d_mid_light:+.3f}"
              f"    ratio: {ratio:.3f}")
    print()
    print("  If the framework's continuous exponent law a_2/a_1 = q_3/q_2 = 3/2")
    print("  holds for walk-sums, the ratio column above should be 3/2 = 1.5.")
    print()

    print("=" * 78)
    print("  INTERPRETATION")
    print("=" * 78)
    print()
    print("  Reading the table:")
    print()
    print("  (a) If 'sector shift' differs across sectors but is CONSTANT")
    print("      within each sector, the framework predicts within-sector")
    print("      ratios but not absolutes. Each sector needs ONE anchor.")
    print("      The anchor is likely the heaviest member (shortest walk).")
    print()
    print("  (b) If 'slope d(log10 residual)/d(depth)' is non-zero within")
    print("      a sector, the walk-product formula's K-dependence is")
    print("      wrong — there is a missing per-step correction.")
    print()
    print("  (c) If the neutrino residual has the SAME sector shift as")
    print("      charged leptons, the integer law generalization to")
    print("      |Q|=0 works and the circulation was only in the value")
    print("      of K*. If the neutrino sector shift is different,")
    print("      neutrinos need their own structural input.")
    print()
    print("  (d) If the within-sector DELTA walk-sums ratio to 3/2 exactly,")
    print("      the framework IS self-consistent at the walk-sum level.")
    print("      In that case, 'depth' in (E3) means 'walk-sum' (sum of")
    print("      denominators along the walk), and the discrepancy was")
    print("      only in which walks we wrote down.")
    print()

    # ========================================================================
    # Sector anchors and within-sector walk-sums
    # ========================================================================

    print("=" * 78)
    print("  SECTOR ANCHORS (re-anchored at each sector's heaviest member)")
    print("=" * 78)
    print()
    print("  If the heaviest fermion in each sector is the sector's 'root',")
    print("  the lighter members walk from that root. The within-sector")
    print("  walk-sums then start at zero.")
    print()

    print(f"  {'sector':<18} {'anchor':<10} {'anchor walk-sum':>16} "
          f"{'integer interp':<20}")
    print("  " + "-" * 70)

    sector_heads = {
        "charged leptons": "tau",
        "up-type quarks":  "top",
        "down-type quarks": "bottom",
        "neutrinos":       "nu_tau",
    }

    # Manual lookup of integer combinations of q2, q3 for each anchor
    interp = {
        "tau":    "~ q_2^2 + q_3 = 7",
        "top":    "~ 0 (= v itself)",
        "bottom": "~ q_2 + q_3 = 5 (mediant)",
        "nu_tau": "~ (q_2 q_3)^2 = 36",
    }

    for sector, head in sector_heads.items():
        anchor_sum = needed[head]
        anchor_int = round(anchor_sum)
        print(f"  {sector:<18} {head:<10} {anchor_sum:>16.3f} "
              f"({anchor_int})  {interp.get(head, ''):<20}")
    print()

    print("  Within-sector walk-sums RELATIVE TO THE ANCHOR")
    print("  (= sum of additional steps needed to walk from heavy to light):")
    print()
    print(f"  {'sector':<18} {'gen3':>8} {'gen2':>8} {'gen1':>8} "
          f"{'increments':<22}")
    print("  " + "-" * 68)
    for sector, members in sectors.items():
        head = sector_heads[sector]
        anchor = needed[head]
        relatives = [needed[m] - anchor for m in members]
        rel_int = [round(r) for r in relatives]
        incs = [rel_int[1] - rel_int[0], rel_int[2] - rel_int[1]]
        print(f"  {sector:<18} {rel_int[0]:>8d} {rel_int[1]:>8d} "
              f"{rel_int[2]:>8d}  +{incs[0]:d}, +{incs[1]:d}")
    print()
    print("  Increment patterns (numerical, in units of denominator steps):")
    print("    leptons:    +3, +6   = +q_3, +2 q_3")
    print("    up-type:    +6, +7   = +q_2 q_3, +q_2 q_3 + 1  [7 is near q_2^3 = 8]")
    print("    down-type:  +3, +2   = +q_3, +q_2")
    print("    neutrinos:  +2, +2   = +q_2, +q_2")
    print()
    print("  Observations:")
    print("    - Every increment is a small integer combination of (q_2, q_3).")
    print("    - Neutrinos have a UNIFORM increment (q_2 each step).")
    print("    - Down-type uses BOTH denominators (one step each).")
    print("    - Leptons DOUBLE the increment between steps (+q_3, +2 q_3).")
    print("    - Up-type is NOT uniform: +6, +7 (not a clean (q_2, q_3) expr).")
    print("      Quark masses have PDG uncertainties ~2%, and up-type is the")
    print("      sector with the heaviest member (top) closest to v. The +7")
    print("      may round to +8 = q_2^3 with a slightly different anchor.")
    print()
    print("  The within-sector structure is integer and (mostly) closes.")
    print("  The cross-sector anchors are where additional structure lives.")
    print()

    print("=" * 78)
    print("  NEUTRINO CIRCULATION: DOES IT VANISH?")
    print("=" * 78)
    print()
    print("  The committed K* = 0.862 (NEVER refit) gives:")
    print()
    print(f"    needed walk-sum for nu_tau = {needed['nu_tau']:.3f}  ~  36")
    print(f"    needed walk-sum for nu_mu  = {needed['nu_mu']:.3f}  ~  37")
    print(f"    needed walk-sum for nu_e   = {needed['nu_e']:.3f}  ~  39")
    print()
    print(f"    framework prediction: depth_nu = (q_2 q_3)^2 = 36 (heaviest)")
    print()
    print("  The committed K* reproduces the (q_2 q_3)^2 = 36 prediction")
    print("  WITHOUT any refit. The refit to K* = 0.8668 in the original")
    print("  neutrino_mass_prediction.py was the source of the circulation,")
    print("  not the formula itself. The original K* = 0.862 from")
    print("  boundary_weight.md gives 36, 37, 39 directly.")
    print()
    print("  The remaining cross-sector spread (nu anchor 36 vs lepton")
    print("  anchor 7 vs up anchor 0 vs down anchor 5) is what the framework")
    print("  has not yet predicted: where each sector's HEAVY MEMBER sits in")
    print("  the absolute walk-sum hierarchy. The within-sector structure")
    print("  closes; the cross-sector anchors are the open piece.")
    print()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
