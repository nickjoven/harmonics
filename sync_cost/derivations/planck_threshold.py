"""
Planck scale from the self-sustaining synchronization threshold.

The question: what is the minimum "domain" where the synchronization
substrate can sustain itself? Below this scale, the mean field can't
constitute itself — there aren't enough coupling stages.

Three converging arguments:

1. LATTICE ARGUMENT (N = 3):
   The Stribeck lattice needs N ≥ 3 elements for frequency conversion.
   At N = 2, the medium passes through linearly. At N = 3, the
   subharmonic crosses over and new structure emerges. Three is the
   minimum chain length for self-sustaining mode-locking.

2. STAIRCASE ARGUMENT (deepest level):
   The devil's staircase is self-similar at 1/φ with scaling φ².
   Each level is φ² narrower than the last. The staircase "runs out"
   when a bracket becomes narrower than the minimum resolvable
   frequency — set by ΔE·Δt ≥ ℏ/2 (uncertainty) and the coupling
   constants. The deepest level is the Planck scale.

3. DIMENSIONAL ARGUMENT (three constants):
   l_P = √(ℏG/c³) is built from exactly three constants.
   Three is the minimum self-sustaining chain length.
   Each constant corresponds to one coupling channel:
       c  — synchronization rate (mediator)
       ℏ  — local phase coupling (quantum)
       G  — global amplitude coupling (gravity)
   You need all three to close the loop.

The pattern: THREE keeps appearing. Not 2, not 4. Three coupling
stages, three constants, three spatial dimensions. This script
explores whether these are the same three.

Usage:
    python sync_cost/derivations/planck_threshold.py
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import H_0_SI

from circle_map_utils import (circle_map_step, winding_number,
                              PHI, INV_PHI, PHI_SQ, LN_PHI_SQ,
                              fibonacci_sequence)


# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

HBAR = 1.054571817e-34   # J·s (reduced Planck)
G = 6.67430e-11          # m³/(kg·s²) (Newton)
C = 2.99792458e8         # m/s (speed of light)
KB = 1.380649e-23        # J/K (Boltzmann)

L_PLANCK = math.sqrt(HBAR * G / C**3)       # 1.616e-35 m
T_PLANCK = math.sqrt(HBAR * G / C**5)       # 5.391e-44 s
M_PLANCK = math.sqrt(HBAR * C / G)          # 2.176e-8 kg
E_PLANCK = math.sqrt(HBAR * C**5 / G)       # 1.956e9 J
OMEGA_PLANCK = 1 / T_PLANCK                 # 1.855e43 rad/s


# ---------------------------------------------------------------------------
# Coupled circle map chain (discrete analog of the Stribeck lattice)
# ---------------------------------------------------------------------------

def coupled_circle_map_chain(N, omega_drive, K_coupling, K_internal,
                              n_steps=50000, n_transient=10000):
    """
    Chain of N circle map oscillators, coupled to nearest neighbors.

    Element 0 is driven at omega_drive.
    Each element has internal frequency INV_PHI (the "natural" frequency).
    Coupling between neighbors is K_coupling.
    Self-coupling (to the drive, element 0 only) is K_internal.

    Returns the effective winding number at each element.

    The circle map for element i:
        θ_i(n+1) = θ_i(n) + ω_i - (K_int/2π)sin(2πθ_i(n))
                   - (K_c/2π)sin(2π(θ_i(n) - θ_{i-1}(n)))
                   - (K_c/2π)sin(2π(θ_i(n) - θ_{i+1}(n)))

    Element 0: driven at omega_drive (forced)
    Elements 1..N-1: free with natural frequency INV_PHI
    """
    theta = [0.0] * N
    omega_natural = [INV_PHI] * N
    omega_natural[0] = omega_drive

    # Transient
    for _ in range(n_transient):
        new_theta = [0.0] * N
        for i in range(N):
            # Self-term
            t = theta[i] + omega_natural[i]
            t -= K_internal / (2 * math.pi) * math.sin(2 * math.pi * theta[i])

            # Coupling to left
            if i > 0:
                t -= K_coupling / (2 * math.pi) * math.sin(
                    2 * math.pi * (theta[i] - theta[i - 1]))

            # Coupling to right
            if i < N - 1:
                t -= K_coupling / (2 * math.pi) * math.sin(
                    2 * math.pi * (theta[i] - theta[i + 1]))

            new_theta[i] = t
        theta = new_theta

    # Measure winding numbers
    theta_start = theta[:]
    for _ in range(n_steps):
        new_theta = [0.0] * N
        for i in range(N):
            t = theta[i] + omega_natural[i]
            t -= K_internal / (2 * math.pi) * math.sin(2 * math.pi * theta[i])

            if i > 0:
                t -= K_coupling / (2 * math.pi) * math.sin(
                    2 * math.pi * (theta[i] - theta[i - 1]))
            if i < N - 1:
                t -= K_coupling / (2 * math.pi) * math.sin(
                    2 * math.pi * (theta[i] - theta[i + 1]))

            new_theta[i] = t
        theta = new_theta

    windings = [(theta[i] - theta_start[i]) / n_steps for i in range(N)]
    return windings


def frequency_conversion_ratio(windings, omega_drive):
    """
    Measure how much the last element's frequency differs from the drive.

    If the chain converts frequency, the last element's winding number
    will differ from the drive frequency.

    Returns the ratio |W_last - omega_drive| / |W_last - 1/φ|.
    Large ratio = element locked to drive (no conversion).
    Small ratio = element locked to natural frequency (conversion happened).
    """
    W_last = windings[-1]
    dist_drive = abs(W_last - omega_drive)
    dist_natural = abs(W_last - INV_PHI)
    if dist_natural < 1e-10:
        return float('inf')  # perfectly at natural frequency
    return dist_drive / dist_natural


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  PLANCK SCALE FROM SELF-SUSTAINING SYNCHRONIZATION THRESHOLD")
    print("=" * 85)

    # === 1. N = 3 IN THE CIRCLE MAP CHAIN ===
    print(f"\n{'─'*85}")
    print("  1. N = 3 IN THE CIRCLE MAP CHAIN")
    print(f"{'─'*85}")

    print(f"""
  The Stribeck lattice shows N = 3 is the minimum chain for frequency
  conversion (RESULTS.md). Does the same threshold appear in coupled
  circle maps?

  Setup: N coupled circle maps. Element 0 driven at ω_d = 0.8.
  All others have natural frequency 1/φ ≈ 0.618.
  Question: does the last element lock to ω_d or relax to 1/φ?
""")

    omega_d = 0.8
    K_int = 0.5  # internal coupling
    K_c = 0.4    # inter-element coupling

    print(f"  ω_drive = {omega_d},  K_internal = {K_int},  K_coupling = {K_c}")
    print(f"\n  {'N':>3s}  {'W_last':>10s}  {'W_0':>10s}  {'dist(1/φ)':>10s}  "
          f"{'dist(ω_d)':>10s}  {'locked to':>12s}")
    print("  " + "-" * 65)

    for N in range(2, 10):
        windings = coupled_circle_map_chain(N, omega_d, K_c, K_int)
        W_last = windings[-1]
        W_0 = windings[0]
        d_phi = abs(W_last - INV_PHI)
        d_drive = abs(W_last - omega_d)

        if d_phi < d_drive:
            locked = "1/φ (natural)"
        elif d_drive < d_phi:
            locked = "ω_d (drive)"
        else:
            locked = "ambiguous"

        print(f"  {N:3d}  {W_last:10.6f}  {W_0:10.6f}  {d_phi:10.6f}  "
              f"{d_drive:10.6f}  {locked:>12s}")

    # === 2. COUPLING SCAN AT N = 2 vs N = 3 ===
    print(f"\n{'─'*85}")
    print("  2. COUPLING SCAN: what K_coupling triggers conversion?")
    print(f"{'─'*85}")

    print(f"\n  At what coupling strength does the last element start")
    print(f"  preferring its natural frequency over the drive?")
    print(f"\n  {'K_c':>6s}  {'W_last(N=2)':>12s}  {'W_last(N=3)':>12s}  "
          f"{'W_last(N=4)':>12s}  {'N=2→':>8s}  {'N=3→':>8s}  {'N=4→':>8s}")
    print("  " + "-" * 75)

    for K_c_10 in range(1, 11):
        K_c = K_c_10 / 10.0
        row = [f"  {K_c:6.2f}"]
        labels = []
        for N in [2, 3, 4]:
            windings = coupled_circle_map_chain(N, omega_d, K_c, K_int)
            W = windings[-1]
            row.append(f"  {W:12.6f}")
            d_phi = abs(W - INV_PHI)
            d_drive = abs(W - omega_d)
            labels.append("1/φ" if d_phi < d_drive else "ω_d")
        print("".join(row) + "".join(f"  {l:>8s}" for l in labels))

    # === 3. THE STAIRCASE RUNS OUT ===
    print(f"\n{'─'*85}")
    print("  3. THE STAIRCASE RUNS OUT: deepest Fibonacci level")
    print(f"{'─'*85}")

    print(f"""
  The devil's staircase at 1/φ has Fibonacci brackets:

      Level n:  width ≈ 1/φ^(2n)

  At what level does the bracket become smaller than the Planck scale?
  The bracket width is a dimensionless frequency ratio. To connect to
  physical scales, we need a reference frequency.

  If the reference is the Planck frequency ω_P = 1/t_P:
      bracket_n = 1/φ^(2n) of ω_P

  The bracket "runs out" when bracket_n × ω_P < ω_P, i.e., at level 0.
  That's trivial — we need a better question.

  Better question: how many Fibonacci levels fit between the Planck
  frequency and the Hubble frequency?
""")

    H0 = H_0_SI   # Hubble parameter (rad/s), 67.4 km/s/Mpc; framework_constants
    freq_ratio = OMEGA_PLANCK / H0

    n_levels = math.log(freq_ratio) / LN_PHI_SQ

    print(f"  Planck frequency:  ω_P = {OMEGA_PLANCK:.3e} rad/s")
    print(f"  Hubble frequency:  H₀  = {H0:.3e} rad/s")
    print(f"  Ratio:             ω_P/H₀ = {freq_ratio:.3e}")
    print(f"  log(ratio):        {math.log(freq_ratio):.2f}")
    print(f"  ln(φ²):            {LN_PHI_SQ:.6f}")
    print(f"  Fibonacci levels:  {n_levels:.1f}")

    print(f"\n  The hierarchy ω_P/H₀ spans {n_levels:.1f} Fibonacci levels.")
    print(f"  This is the depth of the self-similar staircase between")
    print(f"  the smallest (Planck) and largest (Hubble) scales.")

    # Check: what Fibonacci number is at level ~146?
    fibs = fibonacci_sequence(200)
    n_lvl = int(round(n_levels))
    if n_lvl < len(fibs):
        print(f"\n  F_{n_lvl} ≈ φ^{n_lvl}/√5 ≈ {PHI**n_lvl / math.sqrt(5):.3e}")
    print(f"  φ^(2 × {n_levels:.1f}) ≈ {PHI**(2*n_levels):.3e}  (≈ ω_P/H₀ ✓)")

    # === 4. THREE CONSTANTS, THREE STAGES ===
    print(f"\n{'─'*85}")
    print("  4. THREE CONSTANTS, THREE STAGES")
    print(f"{'─'*85}")

    print(f"""
  The Planck length is:   l_P = √(ℏG/c³) = {L_PLANCK:.4e} m
  The Planck time is:     t_P = √(ℏG/c⁵) = {T_PLANCK:.4e} s
  The Planck mass is:     m_P = √(ℏc/G)  = {M_PLANCK:.4e} kg
  The Planck energy is:   E_P = √(ℏc⁵/G) = {E_PLANCK:.4e} J

  Three constants enter: ℏ, G, c. What do they represent in
  the synchronization framework?

  c  = synchronization rate.
       The maximum speed at which phase information propagates.
       Sets the clock. ONE coupling stage.

  ℏ  = local phase coupling quantum.
       The minimum action for a phase synchronization event.
       Sets the granularity. ONE coupling stage.

  G  = global amplitude coupling constant.
       Sets the strength of mean-field (gravitational) coupling.
       ONE coupling stage.

  To form a SELF-SUSTAINING loop, you need all three:
      phase (ℏ) → propagation (c) → amplitude (G) → phase (ℏ)
      └──────────────────────────────────────────────────┘

  This is a chain of length 3. Below the scale where all three
  participate, the loop can't close — the mean field can't
  constitute itself. That scale is the Planck scale.
""")

    # === 5. THE LOOP STRUCTURE ===
    print(f"{'─'*85}")
    print("  5. THE SELF-CONSISTENCY LOOP")
    print(f"{'─'*85}")

    print(f"""
  In the Stribeck lattice:
      TX (drive) → contact 1 → contact 2 → contact 3 → RX (receiver)

  Three contacts, three stages. Below N = 3, no conversion.

  In the Planck loop:
      quantum phase (ℏ) → propagation (c) → gravity (G) → quantum phase
          stage 1            stage 2          stage 3        (closes loop)

  The Planck scale is where the LOOP FIRST CLOSES:

      ℏ/t_P = E_P    (quantum: energy at Planck time)
      E_P = m_P c²    (propagation: mass-energy equivalence)
      G m_P²/l_P = E_P (gravity: self-energy at Planck length)

  Check each:
      ℏ/t_P           = {HBAR/T_PLANCK:.4e} J
      m_P c²          = {M_PLANCK * C**2:.4e} J
      G m_P²/l_P      = {G * M_PLANCK**2 / L_PLANCK:.4e} J
      E_P             = {E_PLANCK:.4e} J

  All four are the SAME energy (to numerical precision).
  This is not a coincidence — it's the definition of Planck units.
  But the INTERPRETATION is new:

      The Planck scale is where quantum coupling, propagation, and
      gravitational self-coupling all cost the same energy.

      Below this scale, one of the three stages can't sustain itself
      at the cost set by the other two. The loop breaks.
      The mean field can't constitute itself.
""")

    # === 6. N = 3 AND DIMENSIONALITY ===
    print(f"{'─'*85}")
    print("  6. N = 3 AND THREE SPATIAL DIMENSIONS")
    print(f"{'─'*85}")

    print(f"""
  The framework claims dimensionality is derived, not assumed:
  "Three spatial dimensions is the lowest-cost mediation topology."

  The pattern:
      N = 3  minimum chain for frequency conversion (lattice)
      3      constants in l_P = √(ℏG/c³) (Planck scale)
      3      spatial dimensions (manifold structure)
      3      stages in the self-sustaining loop

  Are these the same 3?

  Hypothesis: THREE is the minimum number of independent coupling
  channels needed for a self-sustaining synchronization domain.

      - With 1 channel: no coupling, no structure
      - With 2 channels: coupling but no self-consistency check
        (the lattice at N = 2 passes through linearly)
      - With 3 channels: the loop closes, self-consistency is
        enforceable, structure can sustain itself

  If the manifold is "what lowest-cost mediation looks like":
      - 1D: can mediate 1 channel (not enough)
      - 2D: can mediate 2 independent directions (not enough)
      - 3D: can mediate 3 independent channels (minimum sufficient)
      - 4D+: can mediate more, but costs more to maintain coherence

  Three dimensions is the cheapest topology that supports the
  minimum self-sustaining loop. This is why space has 3 dimensions
  AND why the Planck scale involves 3 constants AND why the lattice
  threshold is N = 3.
""")

    # === 7. NUMERICAL PREDICTIONS ===
    print(f"{'─'*85}")
    print("  7. NUMERICAL CONTENT BEYOND DIMENSIONAL ANALYSIS")
    print(f"{'─'*85}")

    print(f"""
  Dimensional analysis gives l_P = √(ℏG/c³). The N = 3 argument
  adds structural content: WHY this combination, not just WHAT.

  But does N = 3 give anything numerically new?

  The lattice gives us the crossover ratio at N = 3:
      P(ω₀)/P(ω_d) = 1.03  at N = 3 (barely above unity)

  Compare to the hierarchy ratios:
""")

    # Ratios that involve the number 3
    alpha_EM = 1 / 137.036  # fine structure constant
    alpha_G_proton = G * (1.67262e-27)**2 / (HBAR * C)  # gravitational coupling (proton)
    alpha_G_planck = G * M_PLANCK**2 / (HBAR * C)  # gravitational coupling (Planck mass)

    print(f"  Fine structure constant:        α_EM = {alpha_EM:.6e}")
    print(f"  Gravitational coupling (proton): α_G = {alpha_G_proton:.6e}")
    print(f"  Ratio α_EM/α_G:                      {alpha_EM/alpha_G_proton:.6e}")
    print(f"  Gravitational coupling (Planck): α_G = {alpha_G_planck:.6f}  (= 1 by construction)")
    print()

    # The Fibonacci level where the hierarchy lives
    em_grav_ratio = alpha_EM / alpha_G_proton
    n_hier = math.log(em_grav_ratio) / LN_PHI_SQ

    print(f"  The EM/gravity hierarchy ratio: {em_grav_ratio:.3e}")
    print(f"  In Fibonacci levels: {n_hier:.1f}")
    print(f"  The Planck/Hubble span: {n_levels:.1f} levels")
    print(f"  Ratio of spans: {n_levels/n_hier:.2f}")

    # === 8. THE MINIMUM SELF-SUSTAINING DOMAIN ===
    print(f"\n{'─'*85}")
    print("  8. THE MINIMUM SELF-SUSTAINING DOMAIN")
    print(f"{'─'*85}")

    print(f"""
  Summary of the argument:

  1. Self-sustaining synchronization requires a minimum chain length.
     In the Stribeck lattice: N = 3.
     In coupled circle maps: N = 3 (the loop must close).

  2. Three independent coupling channels constitute the loop:
     ℏ (phase), c (propagation), G (amplitude).
     The scale where all three equalize is the Planck scale.

  3. Below the Planck scale:
     - One or more stages can't sustain itself at the cost set
       by the others
     - The mean field can't constitute itself (no self-consistency)
     - The manifold structure breaks down
     - "Spacetime" ceases to be a meaningful concept

  4. The Planck scale is NOT a cutoff imposed from outside.
     It's the N = 3 threshold of the synchronization substrate:
     the minimum domain where the loop closes.

  5. Three spatial dimensions is the minimum topology that can
     mediate three independent coupling channels. Same 3.

  Prediction: the Planck scale should show signatures of the
  N = 3 crossover — specifically, the ratio P(natural)/P(drive)
  at the crossover should relate to the fine structure of the
  threshold. The lattice gives 1.03 at N = 3. If the Planck
  scale is the physical N = 3, then near-Planck-scale physics
  should show a similar barely-above-unity crossover in some
  observable ratio.

  This is not yet a quantitative prediction — it's a structural
  one. The N = 3 argument says WHY the Planck scale exists and
  WHY it involves exactly these three constants. The quantitative
  content (the crossover ratio, the exact numerical factors)
  requires connecting the lattice parameters to ℏ, G, c.

  OPEN: derive the numerical prefactor. The Planck scale is
  l_P = √(ℏG/c³) — can the coefficient (here = 1) be derived
  from the N = 3 crossover condition, or is it fixed by
  dimensional analysis alone?
""")

    # === 9. CONNECTION TO BORN RULE ===
    print(f"{'─'*85}")
    print("  9. CONNECTION TO THE BORN RULE RESULT")
    print(f"{'─'*85}")

    print(f"""
  The Born rule derivation (born_rule_tongues.py) showed:

      Δθ² ∝ ε    (basin separation² is linear in tongue depth)

  The Planck scale argument says:

      The tongue structure itself requires N ≥ 3 coupling stages
      to exist. Below the Planck scale, there aren't enough stages
      for tongues to form. No tongues → no basins → no Born rule.

  This gives the Born rule a *domain of validity*:

      P = |ψ|²  holds for scales >> l_P
                 breaks down at scale ~ l_P
                 is undefined below l_P

  The Born rule isn't a universal law — it's a consequence of
  having enough synchronization structure (N ≥ 3) for saddle-node
  bifurcations to form. At the Planck scale, the structure that
  produces |ψ|² is at its minimum viable threshold.

  This is testable in principle: quantum systems engineered to
  operate near the minimum coupling threshold (analogous to N = 3
  in the lattice) should show deviations from Born rule statistics.
  The deviations would be strongest at the crossover, not in the
  deep quantum or deep classical regime.
""")
