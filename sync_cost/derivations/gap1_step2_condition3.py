"""
Gap 1, Step 2: Measure the 1/N scaling of Condition 3.

Condition 3: ⟨cos(ψ-θ_j) ∂_j θ⟩ = ∂_j ψ

Uses GLOBAL (all-to-all) Kuramoto coupling — the model that the
derivation chain actually refers to. The mean field is:

    r e^{iψ} = (1/N) Σ_j e^{iθ_j}

At K ≥ K_c (the critical coupling), the system locks and |r| → 1
as the frequency spread → 0.

The correction to Condition 3 involves ⟨φ² ∂θ⟩ where φ = ψ - θ.
We measure how this scales with N.
"""

import numpy as np


def kuramoto_global_locked(N, K=2.0, omega_scale=0.1, seed=None, dt=0.01, steps=50000):
    """
    Find the locked state of N globally coupled Kuramoto oscillators.

    dθ_j/dt = ω_j + (K/N) Σ_k sin(θ_k - θ_j)
            = ω_j + K r sin(ψ - θ_j)

    At K > K_c = 2/(π g(0)) ≈ 2σ√(2π)/π for Gaussian g(ω),
    the system achieves partial synchronization with |r| > 0.
    For small ω_scale and K=2, we get near-full locking.
    """
    rng = np.random.default_rng(seed)

    omega = omega_scale * rng.standard_normal(N)
    omega -= omega.mean()

    theta = rng.uniform(-0.3, 0.3, N)  # start near locked

    for step in range(steps):
        z = np.mean(np.exp(1j * theta))
        r = np.abs(z)
        psi = np.angle(z)

        dtheta = omega + K * r * np.sin(psi - theta)
        theta += dt * dtheta

        if step > 1000 and np.max(np.abs(dtheta)) < 1e-12:
            break

    # Final state
    z = np.mean(np.exp(1j * theta))
    r = np.abs(z)
    psi = np.angle(z)

    return theta, omega, r, psi


def measure_condition3_global(theta, omega, r, psi, N):
    """
    Measure Condition 3 for global Kuramoto.

    In the global model, ψ is spatially constant (global mean field).
    So ∂_j ψ = 0. And Condition 3 becomes:

        ⟨cos(ψ - θ_j) ∂_j θ⟩ = 0

    where ∂_j θ is a spatial gradient. For globally coupled oscillators
    indexed by j, we use the "frequency ordering" as a spatial coordinate:
    sort oscillators by ω, then ∂_j θ ≈ θ_{j+1} - θ_{j-1}.

    Actually, the more precise test is the ENSEMBLE average version:
    In the locked state at K >> K_c, each oscillator has φ_j = ψ - θ_j
    small. The ensemble version of Condition 3 is:

        (1/N) Σ_j cos(φ_j) ∂θ_j/∂x  vs  ∂ψ/∂x

    For global coupling ∂ψ/∂x = 0, so the condition is:

        (1/N) Σ_j cos(φ_j) v_j = 0

    where v_j = ω_j + Kr sin(ψ - θ_j) is the instantaneous velocity.
    At the fixed point v_j = 0 for locked oscillators, so the condition
    is trivially satisfied for locked oscillators.

    The nontrivial test: how well does

        (1/N) Σ_j cos(φ_j) ω_j  =  Kr × (1/N) Σ_j cos(φ_j) sin(φ_j)

    hold? The LHS is the frequency-weighted cosine moment. The RHS
    involves the sin-cos cross-correlation.

    More directly: test the three moments that matter for the connection.
    """
    phi = psi - theta  # phase offsets

    # Key moments
    cos_phi = np.cos(phi)
    sin_phi = np.sin(phi)
    phi2 = phi**2

    # Ensemble averages
    mean_cos = np.mean(cos_phi)          # should be ≈ r
    mean_sin = np.mean(sin_phi)          # should be ≈ 0
    mean_phi2 = np.mean(phi2)            # variance of phase offset
    mean_phi2_omega = np.mean(phi2 * omega)  # ⟨φ² ω⟩ - the correction term

    # Condition 3 correction: ⟨cos(φ) ω⟩ vs r × ⟨ω⟩ = 0
    # Full expansion: ⟨cos(φ) ω⟩ = ⟨(1 - φ²/2 + ...) ω⟩ = ⟨ω⟩ - (1/2)⟨φ²ω⟩ + ...
    # Since ⟨ω⟩ = 0, the leading term IS (1/2)⟨φ²ω⟩
    cos_phi_omega = np.mean(cos_phi * omega)
    correction = cos_phi_omega  # should be ≈ -(1/2)⟨φ²ω⟩

    # Condition 4: ⟨sin(φ) ω⟩ should be 0
    sin_phi_omega = np.mean(sin_phi * omega)

    return {
        'r': r,
        'mean_phi2': mean_phi2,
        'cos_phi_omega': cos_phi_omega,
        'half_phi2_omega': 0.5 * mean_phi2_omega,
        'sin_phi_omega': sin_phi_omega,
        'correction_magnitude': abs(cos_phi_omega),
    }


# --- Main ---
print("=== Gap 1, Step 2: Condition 3 Scaling (Global Kuramoto) ===\n")
print("Model: dθ_j/dt = ω_j + K r sin(ψ - θ_j), all-to-all coupling")
print("Condition 3 correction: ⟨cos(φ) ω⟩ should scale as O(1/N)\n")

print(f"{'N':>6} {'|r|':>8} {'⟨φ²⟩':>12} {'⟨cos(φ)ω⟩':>14} "
      f"{'½⟨φ²ω⟩':>14} {'⟨sin(φ)ω⟩':>14}")
print("-" * 75)

N_values = [50, 100, 200, 500, 1000, 2000, 5000, 10000]
results = []

for N in N_values:
    theta, omega, r, psi = kuramoto_global_locked(
        N, K=4.0, omega_scale=0.3, seed=42
    )
    m = measure_condition3_global(theta, omega, r, psi, N)
    results.append((N, m))
    print(f"{N:>6d} {m['r']:>8.5f} {m['mean_phi2']:>12.4e} "
          f"{m['cos_phi_omega']:>14.4e} {m['half_phi2_omega']:>14.4e} "
          f"{m['sin_phi_omega']:>14.4e}")

# --- Scaling analysis ---
print("\n--- Scaling analysis ---\n")

Ns = np.array([r[0] for r in results])
corrs = np.array([abs(r[1]['cos_phi_omega']) for r in results])
phi2s = np.array([r[1]['mean_phi2'] for r in results])
cond4 = np.array([abs(r[1]['sin_phi_omega']) for r in results])

mask = corrs > 0
if mask.sum() >= 3:
    log_N = np.log(Ns[mask])
    log_corr = np.log(corrs[mask])
    log_phi2 = np.log(phi2s[mask])
    log_c4 = np.log(cond4[mask] + 1e-20)

    p_corr = np.polyfit(log_N, log_corr, 1)
    p_phi2 = np.polyfit(log_N, log_phi2, 1)
    p_c4 = np.polyfit(log_N, log_c4, 1)

    print(f"Condition 3 correction |⟨cos(φ)ω⟩| ~ N^{p_corr[0]:.3f}")
    print(f"Phase variance ⟨φ²⟩ ~ N^{p_phi2[0]:.3f}")
    print(f"Condition 4 |⟨sin(φ)ω⟩| ~ N^{p_c4[0]:.3f}")
    print()

    if p_corr[0] < -0.3:
        print(f"✓ Condition 3 correction vanishes as N → ∞")
        if abs(p_corr[0] + 0.5) < 0.2:
            print(f"  Scaling ~ N^{p_corr[0]:.2f} ≈ 1/√N")
            print(f"  (CLT: sum of N iid terms has fluctuation ~ 1/√N)")
        elif abs(p_corr[0] + 1.0) < 0.2:
            print(f"  Scaling ~ N^{p_corr[0]:.2f} ≈ 1/N")
            print(f"  (Stronger than CLT — correlated cancellation)")
        else:
            print(f"  Scaling ~ N^{p_corr[0]:.2f}")
        print()
        print(f"  → Condition 3 holds exactly in the continuum limit (N → ∞)")
        print(f"  → The effective connection Γ̃ = Γ + O(N^{p_corr[0]:.2f})")
        print(f"  → Gap 1 closes in the continuum limit")
    else:
        print(f"✗ Condition 3 correction does NOT vanish (exponent {p_corr[0]:.2f})")
        print(f"  Gap 1 remains genuinely open")

    print()
    if p_c4[0] < -0.3:
        print(f"✓ Condition 4 (torsion-free) also vanishes: ~ N^{p_c4[0]:.2f}")
    else:
        print(f"⚠ Condition 4 scaling unclear: ~ N^{p_c4[0]:.2f}")
