"""
Parabola primitive in the seismic domain: critical slowing down demo.

Shows the framework's parabola primitive (saddle-node normal form
dx/dt = mu - x^2) producing the critical-slowing-down statistical
signatures that seismology, ecology, and climate science already use
as early warning indicators for bifurcation-driven transitions.

This is NOT a seismic prediction. It's a worked example of what the
framework's vocabulary ('approach to a saddle-node', 'tongue boundary
narrowing', 'time-to-release ~ 1/sqrt(epsilon)') looks like in
time-series data. The same code can be applied to real GPS / InSAR /
strain data from a seismic gap by replacing the simulated time series
with a loaded dataset.

The critical slowing down signatures (Scheffer, Carpenter, Dakos):

    1. Variance amplification: as mu -> 0, fluctuations grow as 1/sqrt(mu)
    2. Lag-1 autocorrelation (AR1) -> 1 as mu -> 0 (system responds
       to perturbations more slowly)
    3. Skewness grows (asymmetric toward the unstable side)
    4. Power spectrum reddens (low-frequency dominance)

All four come from the same local mathematics: the parabola y = mu - x^2
near its minimum. That's the framework's parabola primitive.

Cross-references in the framework:
  - stribeck_vortex.md           (stick-slip friction as a primitive application)
  - born_rule.md                 (the SAME parabola, derived for quantum mechanics)
  - framework_lagrangian.py      (the Kuramoto variational principle it comes from)
"""

import math
import random
from typing import List, Tuple


# ============================================================================
# Saddle-node normal form with noise
# ============================================================================

def saddle_node_step(x: float, mu: float, noise_amp: float, dt: float) -> float:
    """
    One Euler step of the saddle-node normal form with additive noise:

        dx/dt = mu - x^2 + sigma * eta(t)

    where eta(t) is white Gaussian noise. For mu > 0 there's a stable
    fixed point at x_star = +sqrt(mu). For mu < 0 there's no fixed
    point and x escapes to -infinity. At mu = 0 the two fixed points
    annihilate (the bifurcation).

    Near mu = 0 from above, the system exhibits critical slowing down:
    perturbations decay as exp(-2 sqrt(mu) t), so the relaxation time
    tau = 1/(2 sqrt(mu)) diverges as mu -> 0.
    """
    drift = mu - x * x
    noise = noise_amp * random.gauss(0, 1) * math.sqrt(dt)
    return x + drift * dt + noise


def simulate_trajectory(mu: float, n_steps: int = 10000,
                        dt: float = 0.01, noise_amp: float = 0.2,
                        seed: int = 42) -> List[float]:
    """
    Simulate the saddle-node system for n_steps at a fixed mu.
    Initialize near the stable fixed point x_star = sqrt(mu) to skip
    the transient.
    """
    random.seed(seed)
    if mu <= 0:
        x = 0.0
    else:
        x = math.sqrt(mu)
    trajectory = []
    for _ in range(n_steps):
        x = saddle_node_step(x, mu, noise_amp, dt)
        trajectory.append(x)
    return trajectory


# ============================================================================
# Critical slowing down indicators
# ============================================================================

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def variance(xs: List[float]) -> float:
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)


def lag1_autocorr(xs: List[float]) -> float:
    """
    Sample lag-1 autocorrelation: correlation of x(t) with x(t+1).
    Approaches 1 as the relaxation time diverges.
    """
    m = mean(xs)
    var = variance(xs)
    if var == 0:
        return 0.0
    num = sum((xs[i] - m) * (xs[i + 1] - m) for i in range(len(xs) - 1))
    den = var * (len(xs) - 1)
    return num / den


def skewness(xs: List[float]) -> float:
    """Sample skewness: third standardized moment."""
    m = mean(xs)
    var = variance(xs)
    if var == 0:
        return 0.0
    sd = math.sqrt(var)
    return sum(((x - m) / sd) ** 3 for x in xs) / len(xs)


def compute_indicators(trajectory: List[float]) -> Tuple[float, float, float, float]:
    """Return (mean, variance, AR1, skewness)."""
    return (mean(trajectory),
            variance(trajectory),
            lag1_autocorr(trajectory),
            skewness(trajectory))


# ============================================================================
# Sweep mu and watch the indicators diverge
# ============================================================================

def main():
    print("=" * 78)
    print("  CRITICAL SLOWING DOWN AT THE PARABOLA PRIMITIVE")
    print("=" * 78)
    print()
    print("  Simulate dx/dt = mu - x^2 + noise at decreasing mu.")
    print("  As mu -> 0+, the system approaches the saddle-node bifurcation.")
    print("  Four critical-slowing-down indicators should grow:")
    print()
    print("    1. Variance   : ~ 1/sqrt(mu)")
    print("    2. Lag-1 AR1  : -> 1")
    print("    3. |Skewness| : grows (asymmetric toward unstable side)")
    print("    4. (Power spectrum reddens -- not computed here)")
    print()
    print("  These are the same statistical signatures that early-warning")
    print("  signal tools (Scheffer / Dakos / ewstools) use on real seismic,")
    print("  ecological, climate, and financial time-series data.")
    print()

    # Range chosen so the trajectory stays bounded at fixed noise.
    # (For mu below ~0.05 the noise kicks the trajectory over the
    # unstable fixed point -- the exact behavior the framework would
    # interpret as 'release'.)
    mu_values = [5.0, 2.0, 1.0, 0.5, 0.3, 0.2, 0.15, 0.1, 0.08]
    print(f"  {'mu':>8} {'sqrt(mu)':>10} {'variance':>12} {'1/sqrt(mu)':>14} "
          f"{'AR1':>10} {'skewness':>12}")
    print("  " + "-" * 72)

    # Fixed noise across mu values so the critical slowing down
    # signature (growing variance) is visible in the raw numbers.
    for mu in mu_values:
        traj = simulate_trajectory(mu, n_steps=20000, dt=0.01,
                                   noise_amp=0.03, seed=1)
        m, var, ar1, skew = compute_indicators(traj)
        pred_var_scaling = 1.0 / math.sqrt(mu)
        print(f"  {mu:>8.4f} {math.sqrt(mu):>10.4f} {var:>12.6f} "
              f"{pred_var_scaling:>14.4f} {ar1:>10.4f} {skew:>+12.4f}")

    print()
    print("  Interpretation:")
    print("    - Variance grows as mu shrinks (critical slowing down).")
    print("    - AR1 approaches 1 (slower response to perturbations).")
    print("    - Skewness stays small here because noise is symmetric;")
    print("      in real data with asymmetric noise, skewness grows too.")
    print()

    # ------------------------------------------------------------------
    # Cross-reference with seismic domain
    # ------------------------------------------------------------------
    print("=" * 78)
    print("  APPLICATION TO SEISMIC STRAIN DATA")
    print("=" * 78)
    print()
    print("  To apply this to real seismic data, replace the simulated")
    print("  trajectory with a rolling window of strain observations:")
    print()
    print("    strain = load_gps_or_insar_data('atacama_trench.csv')")
    print("    window = 1000    # number of samples per window")
    print("    for i in range(0, len(strain) - window, step):")
    print("        chunk = strain[i:i + window]")
    print("        m, var, ar1, skew = compute_indicators(chunk)")
    print("        # track the evolution of these indicators")
    print()
    print("  A seismic gap approaching its release event should show:")
    print("    - Variance trending upward over years")
    print("    - AR1 approaching 1")
    print("    - Possibly asymmetric skewness")
    print()
    print("  The framework's contribution is the IDENTIFICATION:")
    print("  this saddle-node local form IS the framework's parabola")
    print("  primitive, the same local geometry that gives the Born")
    print("  rule's |psi|^2 in the quantum sector. One universal form,")
    print("  two physical applications: measurement collapse and stick-slip")
    print("  release. Same sqrt(epsilon) scaling in both cases.")
    print()
    print("  This is NOT a new tool for seismologists -- the early")
    print("  warning signals literature already has the machinery. What")
    print("  the framework adds is the structural unification with the")
    print("  quantum / Kuramoto side of its own content.")
    print()


if __name__ == "__main__":
    main()
