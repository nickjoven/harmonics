"""
Self-consistent decoherence v3: susceptibility-based fluctuations.

The correct fluctuation power near a synchronization transition:

    P(ω) ∝ χ(ω) = 1 / |K_eff(ω) - K_c(ω)|

This is the susceptibility — it diverges at criticality, but
DECREASES in both the deeply locked and deeply unlocked phases.

The self-consistent loop becomes:
    D = D₀ + η × ∫ χ(ω') dω'
    K_c = 2D
    χ(ω) = 1 / |K_eff(ω) - 2D|

Feedback structure:
    - Near criticality: D↑ → K_c↑ → closer to critical → χ↑ → D↑  (positive)
    - Past criticality: D↑ → K_c↑ → deeply unlocked → χ↓ → D↓    (negative)

The positive feedback near criticality + negative feedback past it
= STABLE FIXED POINT AT CRITICALITY.

This is self-organized criticality.

Usage:
    python sync_cost/derivations/self_consistent_D_v3.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI


def arnold_tongue_coupling(omega, K_base=1.0, n_max=12):
    K_eff = 0.0
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            center = p / q
            width = K_base ** q / q
            sigma = width * 0.5
            if sigma < 1e-10:
                continue
            dist = abs(omega - center)
            K_eff += (K_base / q) * math.exp(-0.5 * (dist / sigma) ** 2)
    return K_eff


class SOCSystem:
    """Self-organized criticality via susceptibility feedback."""

    def __init__(self, n_points=300, omega_min=0.05, omega_max=0.95,
                 K_base=0.8, n_max=12, eta=0.1, D_0=0.3,
                 regularizer=0.01):
        self.n = n_points
        self.omega = [omega_min + i * (omega_max - omega_min) / (n_points - 1)
                      for i in range(n_points)]
        self.d_omega = (omega_max - omega_min) / (n_points - 1)
        self.K_base = K_base
        self.n_max = n_max
        self.eta = eta
        self.D_0 = D_0
        self.reg = regularizer  # prevents χ divergence

        self.K_eff = [arnold_tongue_coupling(w, K_base, n_max) for w in self.omega]
        self.D = D_0  # scalar: mean-field (uniform) decoherence
        self.chi = [0.0] * n_points
        self.r = [0.0] * n_points

    def compute_state(self):
        """Compute χ and r from current D."""
        K_c = 2 * self.D
        for i in range(self.n):
            delta = self.K_eff[i] - K_c
            self.chi[i] = 1.0 / (abs(delta) + self.reg)
            if delta > 0:
                self.r[i] = math.sqrt(delta / self.K_eff[i]) if self.K_eff[i] > 0 else 0
            else:
                self.r[i] = 0.0

    def total_susceptibility(self):
        return sum(self.chi[i] * self.d_omega for i in range(self.n))

    def iterate(self, damping=0.5, n_iter=500, verbose=False):
        history = []

        for it in range(n_iter):
            self.compute_state()
            total_chi = self.total_susceptibility()

            # New D from self-consistency
            D_new = self.D_0 + self.eta * total_chi

            # Find state at 1/φ
            idx_phi = min(range(self.n), key=lambda i: abs(self.omega[i] - INV_PHI))
            K_c = 2 * self.D
            delta_phi = self.K_eff[idx_phi] - K_c

            history.append({
                'iter': it,
                'D': self.D,
                'K_c': K_c,
                'total_chi': total_chi,
                'delta_phi': delta_phi,
                'r_phi': self.r[idx_phi],
                'chi_phi': self.chi[idx_phi],
            })

            old_D = self.D
            self.D = damping * old_D + (1 - damping) * D_new
            change = abs(self.D - old_D)

            if change < 1e-12 and it > 10:
                break

        return history

    def find_phi_index(self):
        return min(range(self.n), key=lambda i: abs(self.omega[i] - INV_PHI))

    def tilt_and_running_at(self, idx):
        if idx < 2 or idx >= self.n - 2:
            return 0, 0
        ln_chi = [math.log(max(self.chi[idx + d], 1e-30)) for d in [-2, -1, 0, 1, 2]]
        h = math.log(self.omega[idx + 1]) - math.log(self.omega[idx])
        tilt = (-ln_chi[4] + 8 * ln_chi[3] - 8 * ln_chi[1] + ln_chi[0]) / (12 * h)
        running = (-ln_chi[4] + 16 * ln_chi[3] - 30 * ln_chi[2] + 16 * ln_chi[1] - ln_chi[0]) / (12 * h ** 2)
        return tilt, running

    def profile(self):
        K_c = 2 * self.D
        print(f"  {'ω':>8s}  {'K_eff':>8s}  {'K_eff-Kc':>10s}  {'r':>8s}  {'χ':>10s}  {'note':>8s}")
        print("  " + "-" * 65)
        step = max(1, self.n // 20)
        for i in range(0, self.n, step):
            note = ""
            w = self.omega[i]
            if abs(w - INV_PHI) < 0.01: note = "1/φ"
            elif abs(w - 0.5) < 0.01: note = "1/2"
            elif abs(w - 1/3) < 0.02: note = "1/3"
            elif abs(w - 2/3) < 0.02: note = "2/3"
            elif abs(w - 3/5) < 0.01: note = "3/5"
            elif abs(w - 5/8) < 0.01: note = "5/8"
            elif abs(w - INV_PHI**2) < 0.01: note = "1/φ²"
            delta = self.K_eff[i] - K_c
            print(f"  {w:8.3f}  {self.K_eff[i]:8.4f}  {delta:+10.4f}  "
                  f"{self.r[i]:8.4f}  {self.chi[i]:10.4f}  {note:>8s}")

    def count_critical(self, threshold=0.05):
        """Count frequencies within threshold of criticality."""
        K_c = 2 * self.D
        return sum(1 for i in range(self.n) if abs(self.K_eff[i] - K_c) < threshold)


if __name__ == "__main__":
    print("=" * 80)
    print("  SELF-ORGANIZED CRITICALITY VIA SUSCEPTIBILITY FEEDBACK")
    print("=" * 80)

    # --- 1. Show the feedback structure ---
    print(f"\n{'─'*80}")
    print("  1. FEEDBACK STRUCTURE: χ vs D at selected frequencies")
    print(f"{'─'*80}")

    K_eff_phi = arnold_tongue_coupling(INV_PHI, K_base=0.8, n_max=12)
    K_eff_half = arnold_tongue_coupling(0.5, K_base=0.8, n_max=12)
    K_eff_third = arnold_tongue_coupling(1/3, K_base=0.8, n_max=12)

    print(f"\n  K_eff(1/φ) = {K_eff_phi:.4f}")
    print(f"  K_eff(1/2) = {K_eff_half:.4f}")
    print(f"  K_eff(1/3) = {K_eff_third:.4f}")

    print(f"\n  {'D':>8s}  {'K_c=2D':>8s}  {'χ(1/φ)':>10s}  {'χ(1/2)':>10s}  {'χ(1/3)':>10s}  {'which peaks':>15s}")
    print("  " + "-" * 65)

    reg = 0.01
    for D_10 in range(1, 20):
        D = D_10 * 0.05
        K_c = 2 * D
        chi_phi = 1 / (abs(K_eff_phi - K_c) + reg)
        chi_half = 1 / (abs(K_eff_half - K_c) + reg)
        chi_third = 1 / (abs(K_eff_third - K_c) + reg)
        peak = "1/φ" if chi_phi > chi_half and chi_phi > chi_third else "1/2" if chi_half > chi_third else "1/3"
        print(f"  {D:8.2f}  {K_c:8.2f}  {chi_phi:10.2f}  {chi_half:10.2f}  {chi_third:10.2f}  {peak:>15s}")

    # --- 2. Self-consistent iteration ---
    print(f"\n{'─'*80}")
    print("  2. SELF-CONSISTENT FIXED POINT")
    print(f"{'─'*80}")

    print(f"\n  {'D₀':>8s}  {'η':>6s}  {'D_final':>10s}  {'K/2D(1/φ)':>10s}  {'r(1/φ)':>8s}  {'n_s':>8s}  {'running':>10s}  {'phase':>10s}")
    print("  " + "-" * 85)

    for D_0_10 in range(1, 15):
        D_0 = D_0_10 * 0.05
        for eta in [0.01, 0.05, 0.1, 0.5, 1.0]:
            sys = SOCSystem(n_points=300, K_base=0.8, n_max=12,
                            eta=eta, D_0=D_0, regularizer=0.01)
            history = sys.iterate(damping=0.5, n_iter=1000)
            final = history[-1]
            idx = sys.find_phi_index()
            tilt, run = sys.tilt_and_running_at(idx)
            ns = 1 + tilt
            crit = sys.K_eff[idx] / (2 * sys.D) if sys.D > 0 else 999
            phase = "locked" if crit > 1.05 else "critical" if crit > 0.95 else "unlocked"
            marker = ""
            if abs(ns - 0.9649) < 0.02: marker += " n_s!"
            if phase == "critical": marker += " CRIT!"
            if marker:
                print(f"  {D_0:8.2f}  {eta:6.2f}  {sys.D:10.4f}  {crit:10.4f}  "
                      f"{sys.r[idx]:8.4f}  {ns:8.4f}  {run:+10.4f}  {phase:>10s}{marker}")

    # --- 3. Convergence trace for a good case ---
    print(f"\n{'─'*80}")
    print("  3. CONVERGENCE TRACE")
    print(f"{'─'*80}")

    # Target: D that puts K_c = 2D near K_eff(1/φ)
    # K_eff(1/φ) ≈ 1.508, so D ≈ 0.754 at criticality
    # D₀ should be < 0.754, η × total_χ makes up the rest

    for D_0, eta in [(0.3, 0.5), (0.5, 0.1), (0.1, 1.0)]:
        print(f"\n  D₀ = {D_0}, η = {eta}:")
        sys = SOCSystem(n_points=300, K_base=0.8, n_max=12,
                        eta=eta, D_0=D_0, regularizer=0.01)
        history = sys.iterate(damping=0.3, n_iter=500)

        print(f"  {'iter':>6s}  {'D':>10s}  {'K_c':>8s}  {'Δ(1/φ)':>10s}  {'r(1/φ)':>8s}  {'χ(1/φ)':>10s}  {'Σχ':>10s}")
        print("  " + "-" * 70)
        for h in history:
            if h['iter'] < 15 or h['iter'] % 20 == 0 or h['iter'] == len(history)-1:
                print(f"  {h['iter']:6d}  {h['D']:10.4f}  {h['K_c']:8.4f}  {h['delta_phi']:+10.4f}  "
                      f"{h['r_phi']:8.4f}  {h['chi_phi']:10.4f}  {h['total_chi']:10.4f}")

        # Final profile
        print(f"\n  Final state (D = {sys.D:.4f}):")
        sys.profile()

        idx = sys.find_phi_index()
        tilt, run = sys.tilt_and_running_at(idx)
        crit = sys.K_eff[idx] / (2 * sys.D) if sys.D > 0 else 999
        print(f"\n  At 1/φ: K_eff/2D = {crit:.4f}, n_s = {1+tilt:.4f}, running = {run:+.4f}")

        # Which frequency is closest to critical?
        K_c = 2 * sys.D
        closest_idx = min(range(sys.n), key=lambda i: abs(sys.K_eff[i] - K_c))
        print(f"  Closest to critical: ω = {sys.omega[closest_idx]:.4f} "
              f"(K_eff = {sys.K_eff[closest_idx]:.4f}, Δ = {sys.K_eff[closest_idx]-K_c:+.4f})")

        # Find the frequency with maximum χ
        max_chi_idx = max(range(sys.n), key=lambda i: sys.chi[i])
        print(f"  Max χ at: ω = {sys.omega[max_chi_idx]:.4f} "
              f"(χ = {sys.chi[max_chi_idx]:.4f})")

    # --- 4. What frequency does the system tune to? ---
    print(f"\n{'─'*80}")
    print("  4. WHICH FREQUENCY DOES THE CRITICAL SURFACE SELECT?")
    print(f"{'─'*80}")

    print(f"\n  At the fixed point, K_c = 2D passes through the K_eff landscape.")
    print(f"  Which frequencies end up exactly critical?")
    print(f"\n  {'D₀':>6s}  {'η':>6s}  {'D*':>8s}  {'K_c*':>8s}  {'ω_crit':>8s}  {'near':>10s}  {'max χ at':>10s}")
    print("  " + "-" * 65)

    for D_0 in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        for eta in [0.1, 0.5, 1.0, 2.0]:
            sys = SOCSystem(n_points=500, K_base=0.8, n_max=12,
                            eta=eta, D_0=D_0, regularizer=0.005)
            sys.iterate(damping=0.3, n_iter=500)

            K_c = 2 * sys.D
            # Find frequency closest to critical
            closest = min(range(sys.n), key=lambda i: abs(sys.K_eff[i] - K_c))
            max_chi = max(range(sys.n), key=lambda i: sys.chi[i])

            near = ""
            w = sys.omega[closest]
            if abs(w - INV_PHI) < 0.02: near = "1/φ!"
            elif abs(w - 0.5) < 0.02: near = "1/2"
            elif abs(w - 1/3) < 0.02: near = "1/3"
            elif abs(w - 2/3) < 0.02: near = "2/3"
            elif abs(w - 3/5) < 0.02: near = "3/5"
            elif abs(w - 5/8) < 0.02: near = "5/8"
            elif abs(w - INV_PHI**2) < 0.02: near = "1/φ²"
            else:
                # Find nearest simple rational
                for q in range(1, 10):
                    for p in range(0, q+1):
                        if math.gcd(p,q)==1 and abs(w - p/q) < 0.02:
                            near = f"{p}/{q}"

            near_chi = ""
            wc = sys.omega[max_chi]
            if abs(wc - INV_PHI) < 0.02: near_chi = "1/φ!"

            print(f"  {D_0:6.2f}  {eta:6.2f}  {sys.D:8.4f}  {K_c:8.4f}  "
                  f"{sys.omega[closest]:8.4f}  {near:>10s}  {sys.omega[max_chi]:8.4f} {near_chi}")

    # --- 5. Summary ---
    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")
    print(f"""
  With susceptibility-based fluctuations (P ∝ χ = 1/|K_eff - K_c|):

  The feedback structure is:
    - Subcritical (locked):    D↑ → closer to critical → χ↑ → D↑  (positive)
    - At criticality:          D↑ → past critical      → χ↓ → D↓  (negative)
    - Supercritical (unlocked): D↑ → further from crit  → χ↓ → D↓  (negative)

  This creates a STABLE FIXED POINT where K_c = 2D intersects the
  K_eff(ω) landscape at the point of maximum susceptibility.

  The question: does this intersection preferentially land at 1/φ?
  Or does it land at whatever K_eff happens to equal 2D?

  If K_eff has a maximum at 1/φ (Fibonacci pile-up), then the
  critical surface crosses the PEAK of K_eff there, meaning 1/φ
  is the LAST frequency to become critical as D increases.
  All other frequencies go critical (and past critical) first.

  The fixed point D* is where the total susceptibility, integrated
  over all frequencies, self-consistently produces D*. This depends
  on the full landscape of K_eff, not just the value at 1/φ.
""")
