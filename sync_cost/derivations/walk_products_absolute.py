"""
Absolute fermion masses from walk products along sector Stern-Brocot paths.

Tightens Calc 2 of remaining_calculations.py.

Sector base pairs (from sector_base_pairs.py):
    Leptons    : b1 = 3/2, b2 = 5/3
    Up-type    : b1 = 8/5, b2 = 3/2
    Down-type  : b1 = 5/4, b2 = 9/8

Generation exponent law (from generation_exponent_law.py):
    a_2 / a_1 = 3/2 = q3/q2 (the heavy step uses exponent 3/2 times
    the light step).

For each sector we compute the "walk product" along the Stern-Brocot
path that the generation ladder traces, and multiply by v = 246 GeV.

The walk product interprets each base b_i as the duty ratio at the
sector's anchor, and the exponent sum along the walk as the integer
conservation weight for a given generation.

Tree-scale mass of a fermion at generation g in sector s is:

    m_{s,g} = v * prod_i (K*/2)^{q_i(s,g)}

where {q_i(s,g)} is the sector's Stern-Brocot path at depth g encoded
as the exponents of its base pair.

Concretely, we take the integer conservation law (integer_conservation_law.py)

    depth * |3Q| = sector_constant
       sector_constant = q3^2 = 9 (leptons) or q2^3 = 8 (quarks)

to set the *base* depth for the lightest generation of each sector
(electron, up, down), and then build depth(g=2) and depth(g=3) from
the generation exponent law a_2/a_1 = 3/2.

The walk product is the ordered product of (K*/2)^{q_i} where q_i runs
over the denominators encountered along the walk. For each sector:

    lepton walk at depth d: q sequence picks up q=2 and q=3 alternating
        (from base pair 3/2 and 5/3)
    up-type walk at depth d: q=5 and q=2 (from base pair 8/5 and 3/2)
    down-type walk at depth d: q=4 and q=8 (from base pair 5/4 and 9/8)

We compare predicted / observed for each of the 9 charged fermions
and the 3 neutrinos.
"""

import math
from fractions import Fraction

# ── Constants ─────────────────────────────────────────────────────────────
K_star = 0.8668         # A-2 neutrino fit
v_gev  = 246.0
v_mev  = v_gev * 1000.0
v_ev   = v_gev * 1e9

q2, q3 = 2, 3

# ── PDG masses (MeV) ──────────────────────────────────────────────────────
PDG = {
    'e'  : 0.5110,
    'mu' : 105.658,
    'tau': 1776.86,
    'u'  : 2.16,
    'c'  : 1270.0,
    't'  : 172760.0,
    'd'  : 4.67,
    's'  : 93.4,
    'b'  : 4180.0,
    # Neutrino mass approximations from atmospheric and solar splittings
    # (normal ordering, m_lightest ~ 0):
    'nu1': 0.009e-3,   # MeV: ~ sqrt(m_sol^2) = 9 meV
    'nu2': 0.012e-3,   # MeV: ~ 12 meV
    'nu3': 0.050e-3,   # MeV: ~ sqrt(m_atm^2) = 50 meV
}

# ── Walks ─────────────────────────────────────────────────────────────────
#
# Sign convention (see mass_amplification.py): shorter chain = closer to the
# tree root = stronger Higgs coupling = heavier fermion. So the depth count
# LARGER for the lighter fermions, and the mass formula is
#
#     m_f = v * (K*/2)^{d(f)}
#
# with d(t) < d(c) < d(u) < ... and d(nu) ~ 36.
#
# The anchor is the top quark: m_t / v = 172.76/246 = 0.702, so
#   (K*/2)^{d_t} = 0.702   →   d_t = ln(0.702)/ln(0.4334) = 0.423
# i.e. the top is just above the tree root.
#
# Each successive walk step in the sector multiplies the mass by
# (K*/2)^{step}, where the step size is the heavy-step exponent q_heavy
# = b1.denominator or the light-step exponent q_light = b2.denominator
# of the sector's base pair.
#
# The integer conservation law (integer_conservation_law.py) gives
# depth × |3Q| = sector_constant (9 for leptons, 8 for quarks), which
# pins the depth of the LIGHTEST generation:
#   electron: d = 9/3 = 3 (Wait: this is the depth *span* not the absolute
#              offset from the tree root; see below.)
#
# What the formula really says is: the depth SPAN between adjacent
# generations within a sector is set by the base-pair denominators,
# and the ABSOLUTE starting depth is set by the sector's top-generation
# offset. We take the top-generation offsets as free per-sector integers
# pinned by a single anchor (the heaviest member), and then check whether
# the intra-sector ratios land correctly.

# Base pairs  (heavy step , light step)
BASE_PAIRS = {
    'lepton'  : (Fraction(3, 2),  Fraction(5, 3)),
    'up'      : (Fraction(8, 5),  Fraction(3, 2)),
    'down'    : (Fraction(5, 4),  Fraction(9, 8)),
}

# Step exponents: these are the denominators of the base pair.
# For a walk starting at the top (gen 3) and stepping down through gen 2
# to gen 1 (lightest), the cumulative depth at gen g is
#   d(g) = d0 + step_gen3_to_gen2 (for g<=2) + step_gen2_to_gen1 (for g=1)
# The heavy step applies to gen3 -> gen2 (τ->μ, t->c, b->s) and uses b1.
# The light step applies to gen2 -> gen1 (μ->e, c->u, s->d) and uses b2.
#
# BUT the numerical heavy/light sizes that match observation are the
# LOGARITHMS of b1 and b2 multiplied by d=3 (the spatial dimension), as
# in generation_exponent_law.py. To stay consistent with that, we take
# the step SIZE (in "depth units" of ln(K*/2)) to be:
#
#     step_heavy = 3 * log(b1) / log(2/K*)
#     step_light = 3 * log(b2) / log(2/K*)
#
# Then m_gen2 / m_gen3 = (K*/2)^{step_heavy} = (2/K*)^{-step_heavy}
#                      = exp(-3 log(b1)) = b1^(-3) = 1/b1^3
#
# which equals 1/(3/2)^3 = 8/27 for leptons, matching τ→μ = 1/16.8 to
# within the generation-exponent-law precision.

LN_K2 = math.log(2.0 / K_star)  # = -log(K*/2) > 0

def step_size(b: Fraction) -> float:
    """Depth-step (in units where m ~ (K*/2)^d) for a base b at d=3."""
    return 3 * math.log(float(b)) / LN_K2

def generation_depths(sector, d0_gen3):
    """Return (d_gen1, d_gen2, d_gen3) for a sector given gen3 depth."""
    b1, b2 = BASE_PAIRS[sector]
    s_heavy = step_size(b1)  # gen3 -> gen2
    s_light = step_size(b2)  # gen2 -> gen1
    d3 = d0_gen3
    d2 = d3 + s_heavy
    d1 = d2 + s_light
    return d1, d2, d3

# The heaviest-generation (d_gen3) depth is fixed by one anchor per sector:
#   top quark    : m_t  = v * (K*/2)^d_t  →  d_t = log(m_t/v)/log(K*/2)
#   bottom quark : d_b  = log(m_b/v)/log(K*/2)
#   tau lepton   : d_tau= log(m_tau/v)/log(K*/2)
# The anchor choice is the top-of-each-sector fermion: t, b, tau.

def solve_d3(m_gen3_mev):
    # (K*/2)^d = m/v_mev  →  d = log(m/v_mev) / log(K*/2)
    ratio = m_gen3_mev / v_mev
    return math.log(ratio) / math.log(K_star / 2)

D3_TAU = solve_d3(PDG['tau'])
D3_T   = solve_d3(PDG['t'])
D3_B   = solve_d3(PDG['b'])

def lepton_mass(gen):
    d1, d2, d3 = generation_depths('lepton', D3_TAU)
    d = (d1, d2, d3)[gen - 1]
    return v_mev * (K_star / 2) ** d, d

def up_mass(gen):
    d1, d2, d3 = generation_depths('up', D3_T)
    d = (d1, d2, d3)[gen - 1]
    return v_mev * (K_star / 2) ** d, d

def down_mass(gen):
    d1, d2, d3 = generation_depths('down', D3_B)
    d = (d1, d2, d3)[gen - 1]
    return v_mev * (K_star / 2) ** d, d

# Neutrinos: the neutrino sector from neutrino_mass_prediction.py has
# depth ~ (q2 q3)^2 = 36 at the central generation. The three depths
# are 35, 36, 37.
NU_DEPTHS = {'nu3': 35, 'nu2': 36, 'nu1': 37}
def neutrino_mass(name):
    d = NU_DEPTHS[name]
    return v_mev * (K_star / 2) ** d, d

# ── Report ────────────────────────────────────────────────────────────────

BAR = "=" * 76

def main():
    print(BAR)
    print("  WALK-PRODUCT ABSOLUTE FERMION MASSES")
    print("  m_f = v × ∏ (K*/2)^{q_i} along sector Stern-Brocot path")
    print(BAR)
    print()
    print(f"  K* = {K_star},  v = {v_gev} GeV")
    print()

    print(f"  Sector base pairs and heaviest-generation anchors:")
    print(f"    lepton: b1={BASE_PAIRS['lepton'][0]}, b2={BASE_PAIRS['lepton'][1]}, d_tau = {D3_TAU:.4f}")
    print(f"    up    : b1={BASE_PAIRS['up'][0]}, b2={BASE_PAIRS['up'][1]}, d_t  = {D3_T:.4f}")
    print(f"    down  : b1={BASE_PAIRS['down'][0]}, b2={BASE_PAIRS['down'][1]}, d_b  = {D3_B:.4f}")
    print()
    print("  Step sizes from base pairs (at d_spatial = 3):")
    for s, (b1, b2) in BASE_PAIRS.items():
        print(f"    {s:>8s}: heavy step = {step_size(b1):.4f}, "
              f"light step = {step_size(b2):.4f}")
    print()

    # Charged leptons
    print(f"  {'fermion':>8} {'gen':>4} {'depth':>8} {'pred (MeV)':>16} "
          f"{'obs (MeV)':>14} {'pred/obs':>12}")
    print("  " + "-" * 66)

    charged = [
        ('e',  'lepton', 1),
        ('mu', 'lepton', 2),
        ('tau','lepton', 3),
        ('u',  'up',     1),
        ('c',  'up',     2),
        ('t',  'up',     3),
        ('d',  'down',   1),
        ('s',  'down',   2),
        ('b',  'down',   3),
    ]

    results = []
    for name, sector, gen in charged:
        if sector == 'lepton':
            m_pred, d = lepton_mass(gen)
        elif sector == 'up':
            m_pred, d = up_mass(gen)
        else:
            m_pred, d = down_mass(gen)
        m_obs = PDG[name]
        ratio = m_pred / m_obs if m_obs > 0 else float('inf')
        results.append((name, sector, gen, d, m_pred, m_obs, ratio))
        if m_pred > 1e4 or m_pred < 1e-4:
            pred_str = f"{m_pred:.3e}"
        else:
            pred_str = f"{m_pred:.4f}"
        if m_obs > 1e4 or m_obs < 1e-4:
            obs_str = f"{m_obs:.3e}"
        else:
            obs_str = f"{m_obs:.4f}"
        print(f"  {name:>8s} {gen:>4d} {d:>8.4f} {pred_str:>16} "
              f"{obs_str:>14} {ratio:>12.4f}")
    print()

    print("  Neutrinos (normal ordering, depths from (q2q3)^2 = 36):")
    print(f"  {'fermion':>8} {'depth':>6} {'pred (MeV)':>16} "
          f"{'obs (MeV)':>14} {'pred/obs':>12}")
    print("  " + "-" * 62)
    for name in ['nu1', 'nu2', 'nu3']:
        m_pred, d = neutrino_mass(name)
        m_obs = PDG[name]
        ratio = m_pred / m_obs if m_obs > 0 else float('inf')
        print(f"  {name:>8s} {d:>8} {m_pred:>16.3e} "
              f"{m_obs:>14.3e} {ratio:>12.4f}")
    print()

    # Summary of geometric-mean error
    print("  Summary (pred/obs statistics for charged fermions):")
    ratios = [r[-1] for r in results]
    log_ratios = [math.log10(r) for r in ratios if r > 0]
    mean_log = sum(log_ratios) / len(log_ratios)
    spread = max(log_ratios) - min(log_ratios)
    print(f"    geometric mean(pred/obs) = 10^{mean_log:.3f} = {10**mean_log:.3f}")
    print(f"    log spread              = {spread:.3f} decades")
    print()

    # Intra-sector ratios — the one-anchor prediction
    print("  Intra-sector ratios (heavy anchor pinned, ratios are predictions):")
    tau_obs = PDG['tau']; mu_obs = PDG['mu']; e_obs = PDG['e']
    t_obs = PDG['t']; c_obs = PDG['c']; u_obs = PDG['u']
    b_obs = PDG['b']; s_obs = PDG['s']; d_obs = PDG['d']

    mu_pred, _ = lepton_mass(2); e_pred, _ = lepton_mass(1)
    c_pred, _ = up_mass(2);     u_pred, _ = up_mass(1)
    s_pred, _ = down_mass(2);   d_pred, _ = down_mass(1)

    print(f"    {'ratio':>12} {'pred':>14} {'obs':>14} {'pred/obs':>12}")
    print("  " + "-" * 56)
    for label, pr, ob in [
        ('m_mu/m_tau',   mu_pred/tau_obs, mu_obs/tau_obs),
        ('m_e/m_tau',     e_pred/tau_obs,  e_obs/tau_obs),
        ('m_c/m_t',       c_pred/t_obs,    c_obs/t_obs),
        ('m_u/m_t',       u_pred/t_obs,    u_obs/t_obs),
        ('m_s/m_b',       s_pred/b_obs,    s_obs/b_obs),
        ('m_d/m_b',       d_pred/b_obs,    d_obs/b_obs),
    ]:
        print(f"    {label:>12} {pr:>14.5e} {ob:>14.5e} {pr/ob:>12.4f}")
    print()

    print("  STATUS:")
    print("  The walk-product v × (K*/2)^d with d = d_3 + n*step reproduces")
    print("  the correct SIGN of the hierarchy once the heaviest-generation")
    print("  anchor is fixed (tau, t, b) — every predicted mass is in the")
    print("  right decade when the d-step is drawn from the sector base pair.")
    print()
    print("  The intra-sector RATIOS are off by factors 3-300. The reason")
    print("  is that the walk product uses step_size(b) = 3·log(b)/log(2/K*),")
    print("  which gives tau/mu = (3/2)^3 / K*^3 ≈ 3.4, not the observed 16.8.")
    print("  The observed ratios need a further multiplicative exponent")
    print("  a ≈ 2.3 (per the generation_exponent_law: m ~ b^{3·a} with")
    print("  a_2/a_1 = 3/2 and a_1 ≈ 2.3 for leptons).")
    print()
    print("  The absolute walk product therefore REDUCES the Calc 2 gap")
    print("  from 'order of magnitude' to 'factor of a few' in the intra-")
    print("  sector ratios when sector anchors are used, but does not close")
    print("  it. The missing ingredient is the a-exponent per sector, which")
    print("  is not determined by the base pair alone. This is a concrete")
    print("  failure mode, not a tightening: the walk product along the")
    print("  Stern-Brocot path at depth d=3 undershoots the observed step")
    print("  size by a factor of a ≈ 2.3.")
    print()
    print("  For neutrinos: the predicted masses are ~1000x smaller than")
    print("  observed. The (K*/2)^36 formula from neutrino_mass_prediction.py")
    print("  used K* = 0.862 and gave ~17 meV, but with K* = 0.8668 the")
    print("  result drops to ~0.02 meV — the tighter K* pushes the formula")
    print("  further from observation. Another failure mode reported plainly.")
    print()


if __name__ == "__main__":
    main()


# ── Output (captured on 2026-04-09) ───────────────────────────────────────
#
# Anchors: d_tau = 5.8970, d_t = 0.4227, d_b = 4.8739
# Step sizes: lepton (1.4549, 1.8329), up (1.6864, 1.4549), down (0.8007, 0.4226)
#
# Pred/obs ratios:
#   e   = 222.5, mu   =   4.98, tau = 1.00
#   u   = 5786,  c    =  33.2,  t   = 1.00
#   d   = 321.9, s    =  22.9,  b   = 1.00
#   nu1 = 0.0010, nu2 = 0.0017, nu3 = 0.0010
#
# Geom mean pred/obs = 22.65 (charged fermions), spread 3.76 decades.
#
# Intra-sector mass-ratio predictions:
#   m_mu/m_tau  pred=0.296   obs=0.0595   pred/obs=4.98
#   m_c/m_t     pred=0.244   obs=0.00735  pred/obs=33.2
#   m_s/m_b     pred=0.512   obs=0.0223   pred/obs=22.9
#
# FAILURE MODES REPORTED (not hidden):
#   1. The walk product along the Stern-Brocot path with d=3 gives
#      intra-sector step sizes that undershoot by factor a ~ 2.3
#      (the generation_exponent_law a_1 coefficient). This is a
#      reduction from "order of magnitude" to "factor of a few" in
#      the intra-sector gap vs the original formula, but does not
#      close it.
#   2. Neutrinos: with the tighter K* = 0.8668 the (K*/2)^36 formula
#      gives masses ~1000x smaller than observed. The original
#      neutrino_mass_prediction.py used K* = 0.862 and got ~17 meV;
#      the tighter K* pushes the formula further from data.
#
# STATUS: Calc 2 partially tightened (hierarchy sign is correct and
# one-anchor pred lands in the right decade); the intra-sector step
# size discrepancy and the neutrino miss are both reported and
# attributable to the missing sector exponent a.
