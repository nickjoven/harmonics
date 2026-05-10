"""
clarinet_lattice.py — van der Pol coupled-chain analog of stribeck_lattice.py

Tests the master cascade-lock identity on independent dynamics. Predicts
that the q_3-base cascade (drive at 3*omega_0, "twelfth") locks at
critical chain length N = q_2 = 2, while the q_2-base cascade (drive at
2*omega_0, "octave") locks at N = q_3 = 3 — same as Stribeck.

Result (from session run):
  Drive 3:1 — N=2 locks (P(omega_0)/total = 0.831)
  Drive 2:1 — N=3 locks (P(omega_0)/P(2*omega_0) = 30.9)

This matches the structural prediction from master_cascade_identity.md
exactly: cascade base = drive ratio, cascade depth = the OTHER prime.
"""

import math
import cmath


def simulate(N, A, omega_d, mu=2.0, K_coup=0.5, t_max=400, dt=0.01):
    """Coupled van der Pol chain, drive on element 0, measure element N-1.

    Equation per element i:
        x''_i - mu(1 - x_i^2) x'_i + x_i = K(x_{i-1} - 2 x_i + x_{i+1}) + drive_i
    Boundaries: Neumann (free ends).
    Drive only on element 0: A * cos(omega_d * t).
    """
    n_steps = int(t_max / dt)
    x = [0.01] * N
    v = [0.0] * N
    rec_start = n_steps // 2
    rec = []
    for step in range(n_steps):
        t = step * dt
        new_a = []
        for i in range(N):
            xl = x[i - 1] if i > 0 else x[0]
            xr = x[i + 1] if i < N - 1 else x[N - 1]
            coupling = K_coup * (xl - 2 * x[i] + xr)
            vdp = mu * (1 - x[i] ** 2) * v[i]
            restore = -x[i]
            drive = A * math.cos(omega_d * t) if i == 0 else 0.0
            new_a.append(vdp + restore + coupling + drive)
        for i in range(N):
            v[i] += new_a[i] * dt
            x[i] += v[i] * dt
        if step >= rec_start:
            rec.append(x[N - 1])
    return rec, dt


def power_at(signal, dt, omega):
    """Discrete Fourier amplitude at angular frequency omega."""
    n = len(signal)
    s = sum(signal[k] * cmath.exp(-1j * omega * k * dt) for k in range(n))
    return abs(s) ** 2 / n ** 2


def critical_chain_length(omega_d_ratio, mu=2.0, K_coup=0.5, A=3.0,
                          N_range=(1, 7), threshold=10.0):
    """Find smallest N where the cascade locks (subharmonic dominates drive).

    Returns smallest N with P(omega_0)/P(omega_d) > threshold, or None.
    """
    for N in range(N_range[0], N_range[1] + 1):
        rec, dt = simulate(N, A=A, omega_d=omega_d_ratio, mu=mu, K_coup=K_coup)
        p1 = power_at(rec, dt, 1.0)
        pd = power_at(rec, dt, omega_d_ratio)
        if p1 / (pd + 1e-20) > threshold:
            return N
    return None


def main():
    print("Clarinet-lattice cascade experiment")
    print()
    print("Drive 3:1 (twelfth, q_3 base) — predict critical N = q_2 = 2:")
    for N in [1, 2, 3, 4, 6]:
        rec, dt = simulate(N, A=3.0, omega_d=3.0)
        p1 = power_at(rec, dt, 1.0)
        p3 = power_at(rec, dt, 3.0)
        total = p1 + p3 + power_at(rec, dt, 2.0) + power_at(rec, dt, 5.0) + 1e-20
        print(f"  N={N}: P(w_0)/total = {p1/total:.4f}, P(w_0)/P(3w_0) = {p1/(p3+1e-20):.4f}")
    print()
    print("Drive 2:1 (octave, q_2 base) — predict critical N = q_3 = 3:")
    for N in [1, 2, 3, 4, 6]:
        rec, dt = simulate(N, A=3.0, omega_d=2.0)
        p1 = power_at(rec, dt, 1.0)
        p2 = power_at(rec, dt, 2.0)
        print(f"  N={N}: P(w_0)/P(2w_0) = {p1/(p2+1e-20):.4f}")


if __name__ == "__main__":
    main()
