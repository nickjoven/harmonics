#!/usr/bin/env python3
"""
Schwarzschild K(r) profile — Gap B proposal (Derivation 40).

The D12 dictionary identifies K(x,x') = G_γ(x,x') (Green's function
of the spatial metric). What does K(r) look like near a Schwarzschild
source? Three candidate approaches, compared to the Stribeck vortex.

The key question: which approach gives K > 1 inside the horizon and
K < 1 outside, matching the Stribeck vortex regime structure?

Usage:
    python3 sync_cost/derivations/schwarzschild_K_profile.py
"""

import math


# =========================================================================
# Schwarzschild geometry (geometric units: G = c = 1, mass = M)
# =========================================================================

def lapse(r, M=1.0):
    """ADM lapse N = √(1 - 2M/r). Defined for r > 2M."""
    if r <= 2 * M:
        return 0.0
    return math.sqrt(1 - 2 * M / r)


def grr(r, M=1.0):
    """Radial metric component γ_rr = 1/(1 - 2M/r)."""
    if r <= 2 * M:
        return float('inf')
    return 1.0 / (1 - 2 * M / r)


def sqrt_gamma(r, M=1.0):
    """√det(γ) for Schwarzschild spatial metric on t=const slice.
    γ = diag(1/(1-2M/r), r², r²sin²θ). √det = r² sinθ / √(1-2M/r).
    At θ = π/2: √det = r²/√(1-2M/r)."""
    if r <= 2 * M:
        return float('inf')
    return r**2 / math.sqrt(1 - 2 * M / r)


def kretschner(r, M=1.0):
    """Kretschner scalar K_Kr = R_μνρσ R^μνρσ = 48M²/r⁶."""
    return 48 * M**2 / r**6


# =========================================================================
# Approach A: K from lapse (order parameter)
# =========================================================================

def K_lapse(r, M=1.0, K0=1.0):
    """
    K_eff = K₀ × |r_order| where r_order = N = √(1-2M/r).

    D12 dictionary: r (Kuramoto order parameter) = N (lapse).
    D36: K_eff = K₀|r|. With K₀ = 1 at infinity:

      K_eff(r) = √(1 - 2M/r)

    This goes to 0 at the horizon and 1 at infinity.
    K_eff < 1 everywhere outside the horizon.
    Inside the horizon: N is imaginary → K is undefined.

    Problem: K < 1 everywhere, so no overcritical region.
    The "vortex core" analogy doesn't work here.

    But this IS what D36 says: K_eff ≤ 1 globally. The lapse-based
    K never exceeds 1. The exterior is subcritical everywhere.
    """
    N = lapse(r, M)
    return K0 * N


# =========================================================================
# Approach B: K from curvature (local coupling density)
# =========================================================================

def K_curvature(r, M=1.0, a=0.01):
    """
    K(r) based on local curvature relative to the lattice scale a.

    Physical idea: the coupling between oscillators depends on how
    much the geometry distorts over one lattice spacing. Strong
    curvature = strong coupling.

    The tidal acceleration at distance a from a mass M at radius r:
      a_tidal = 2Ma/r³

    Normalized to the lattice spring constant (~ 1/a²):
      K_tidal(r) = 2Ma³/r³

    This gives K > 1 when r < (2Ma³)^{1/3} = r_c.

    For a = l_P (Planck length) and M >> M_P:
      r_c = (2M l_P³)^{1/3}

    This is between the Planck length and the Schwarzschild radius:
      l_P << r_c << 2M

    The overcritical region exists but is deep inside the horizon.
    """
    return 2 * M * a**3 / r**3


# =========================================================================
# Approach C: K from the regularized Green's function
# =========================================================================

def K_green(r, M=1.0, a=0.01):
    """
    K(r) from the coincident-point Green's function G_γ(r,r;a).

    The scalar Green's function on the Schwarzschild spatial slice
    satisfies: ∇²_γ G = δ³(x-x')/√γ

    The flat-space Green's function is G₀ = 1/(4πa) at cutoff a.
    The curved-space correction (Hadamard-DeWitt):

      G(r,r;a) = G₀ × [1 + a² R(r)/6 + ...]

    where R is the Ricci scalar. For vacuum Schwarzschild, R = 0.
    But the spatial Ricci scalar ³R of the t=const slice is nonzero:

      ³R = 2M/r³ × (1 - 2M/r)^{-1}

    So the leading correction is:

      G(r,r;a) ≈ (1/4πa) × [1 + a² × M/(3r³(1-2M/r))]

    Normalizing K = G/G_flat = G × 4πa:

      K(r) = 1 + a² M / (3r³(1-2M/r))

    This exceeds 1 everywhere outside the horizon (³R > 0) and
    diverges at the horizon. The overcritical condition K > K_crit
    for some threshold K_crit defines a critical radius.
    """
    if r <= 2 * M:
        return float('inf')
    three_R = 2 * M / (r**3 * (1 - 2 * M / r))
    return 1.0 + a**2 * three_R / 6


# =========================================================================
# Approach D: K from the Stribeck analogy (inverse lapse)
# =========================================================================

def K_inverse_lapse(r, M=1.0):
    """
    K(r) = 1/N² = 1/(1 - 2M/r) = γ_rr.

    Physical idea: the coupling is the radial metric component.
    Near the horizon, γ_rr → ∞ (strong coupling, fold).
    At infinity, γ_rr → 1 (K = 1, critical).
    At r > 2M: K > 1 always (everything outside is overcritical!).

    This is wrong for the Stribeck vortex analogy (we need K < 1
    in the exterior). But it captures the GR physics: the radial
    proper distance ds = dr/√(1-2M/r) diverges at the horizon.

    The issue: this gives K > 1 everywhere, with K → 1 only at
    infinity. There is no subcritical exterior.
    """
    if r <= 2 * M:
        return float('inf')
    return 1.0 / (1 - 2 * M / r)


# =========================================================================
# Main
# =========================================================================

def main():
    print("=" * 70)
    print("SCHWARZSCHILD K(r) PROFILE — GAP B PROPOSAL")
    print("=" * 70)
    M = 1.0

    # --- Compare all four approaches ---
    print("\nFour candidate K(r) profiles (M = 1, a = 0.01):")
    print()
    print(f"  {'r/M':>6}  {'K_lapse':>10}  {'K_curv':>10}  {'K_green':>10}  {'K_inv':>10}")
    print("  " + "-" * 50)

    a = 0.01
    for r_frac in [2.01, 2.1, 2.5, 3, 4, 5, 7, 10, 20, 50, 100]:
        r = r_frac * M
        Ka = K_lapse(r, M)
        Kb = K_curvature(r, M, a)
        Kc = K_green(r, M, a)
        Kd = K_inverse_lapse(r, M)
        print(f"  {r_frac:6.2f}  {Ka:10.6f}  {Kb:10.6f}  {Kc:10.6f}  {Kd:10.4f}")

    # --- Analysis ---
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    print("""
  APPROACH A (K = lapse = √(1-2M/r)):
    K < 1 everywhere outside horizon. K → 0 at horizon. K → 1 at ∞.
    No overcritical region. Consistent with D36 (K_eff ≤ 1 globally).
    But: no Stribeck vortex structure. No K > 1 core.
    This is the D36-faithful approach: the exterior is subcritical.

  APPROACH B (K = tidal coupling = 2Ma³/r³):
    K > 1 when r < (2Ma³)^{1/3}. For a = 0.01:
    r_c = (2×1×0.01³)^{1/3} = 0.0272M — deep inside the horizon.
    Overcritical region exists but is Planck-scale, not horizon-scale.
    Does not reproduce the horizon as a K = 1 surface.

  APPROACH C (K = 1 + a²³R/6):
    K > 1 everywhere outside horizon (³R > 0 in Schwarzschild).
    K → ∞ at horizon. K → 1 at infinity.
    The K = 1 surface IS r = ∞. No finite critical radius.
    This says: all of spacetime near a mass is overcritical.
    """)

    # --- The resolution ---
    print("=" * 70)
    print("PROPOSED RESOLUTION")
    print("=" * 70)
    print("""
  The Stribeck vortex and the Schwarzschild geometry have OPPOSITE
  structures, and this is physically correct:

  STRIBECK VORTEX (photonic crystal, fluid):
    - v = 0 at center → K = K_stat > 1 (overcritical core)
    - v increases with r → K drops below 1 (subcritical exterior)
    - The K = 1 surface separates fold from mode-locking
    - Energy flow reverses INSIDE r_c

  SCHWARZSCHILD (gravity):
    - The lapse N = √(1-2M/r) = the order parameter
    - D36 says: K_eff = K₀|r| = K₀N ≤ 1
    - K_eff DECREASES toward the horizon (less coherence, not more)
    - The horizon is where K_eff → 0, not K_eff → ∞

  The horizon is NOT an overcritical boundary. It is a DECOHERENCE
  boundary: the lapse goes to zero, meaning oscillators at the
  horizon have zero synchronization rate. They are fully unlocked
  (the quantum regime of D12 Part II), not overcoupled.

  In the Stribeck picture:
    - A photonic crystal vortex core has K_stat > 1 because the
      medium is static there (v = 0, maximum coupling)
    - A black hole horizon has K_eff → 0 because the medium
      is maximally redshifted there (N → 0, zero coupling)

  These are opposite limits of the SAME coupling landscape:
    - Stribeck vortex: coupling ∝ 1/velocity (high at rest)
    - Schwarzschild:   coupling ∝ lapse (zero at horizon)

  THE PROPOSAL:
    The gravity sector does not have a Stribeck vortex structure.
    It has the INVERSE structure:

    | | Stribeck vortex | Schwarzschild |
    |---|---|---|
    | Core | K > 1, fold, chaos | K → 0, fully unlocked, quantum |
    | Surface | K = 1, critical | K = 1, asymptotic infinity |
    | Exterior | K < 1, mode-locked | Does not apply (K < 1 everywhere) |

    The black hole interior (r < 2M) is not "overcritical" — it is
    "off the map" (the lapse becomes imaginary, time and space swap).
    The framework cannot describe the interior directly because the
    ADM foliation breaks down.

    The K > 1 regime of D40 exists in MATERIAL systems (photonic
    crystals, fluid vortices) where the coupling K is set by the
    medium's velocity-dependent friction. In gravity, the coupling
    K_eff is set by the lapse, which is bounded by |r| ≤ 1. The
    D36 prohibition is absolute in the gravity sector.

  COMPUTATIONAL STATUS: Derived. The Schwarzschild K(r) profile
  is K_eff = √(1-2M/r). No overcritical region exists outside
  the horizon. The gravity sector and the photonic crystal sector
  have complementary, not identical, regime structures.
    """)

    # --- Stribeck vs Schwarzschild comparison ---
    print("=" * 70)
    print("SIDE-BY-SIDE: STRIBECK VORTEX vs SCHWARZSCHILD")
    print("=" * 70)
    print()

    # Stribeck parameters
    K_STAT = 1.8
    K_KIN = 0.3
    V_THR = 1.0
    R_CORE = 1.0 / (2 * math.pi)

    print(f"  {'x (normalized)':>16}  {'K_stribeck':>12}  {'K_schwarz':>12}")
    print("  " + "-" * 44)

    for x_frac in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 2.0, 5.0, 10.0]:
        # Stribeck: x = r/r_core, ℓ = 1
        r_s = x_frac * R_CORE
        v = r_s / (r_s**2 + R_CORE**2) if r_s > 0 else 0
        K_stri = K_KIN + (K_STAT - K_KIN) * math.exp(-(v / V_THR)**2)

        # Schwarzschild: x = r/(2M) - 1, so r = 2M(1+x)
        r_g = 2 * M * (1 + max(x_frac, 0.001))
        K_schw = lapse(r_g, M)

        print(f"  {x_frac:16.2f}  {K_stri:12.4f}  {K_schw:12.4f}")

    print()
    print("  Stribeck: K starts HIGH (1.8) at center, drops to LOW (0.3)")
    print("  Schwarzschild: K starts LOW (0.0) at horizon, rises to HIGH (1.0)")
    print("  They are COMPLEMENTARY, not analogous.")


if __name__ == "__main__":
    main()
