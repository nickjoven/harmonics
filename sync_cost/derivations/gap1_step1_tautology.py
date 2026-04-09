"""
Gap 1, Step 1: Verify the Christoffel tautology.

Given a smooth phase field θ(x) on [0,1]³, define:
    γ_ij = δ_ij - <∂_iθ ∂_jθ>

Compute Γ^k_ij two ways:
  (a) Standard Levi-Civita formula from γ and ∂γ
  (b) From three-point correlations T_ijl of θ

Verify they agree. This is expected to pass trivially (chain rule).
"""

import numpy as np

# --- Setup: smooth phase field on a 3D grid ---
Nx = 32
L = 1.0
dx = L / Nx
x = np.linspace(dx/2, L - dx/2, Nx)
X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

# Random smooth phase field (sum of low-frequency Fourier modes)
np.random.seed(42)
n_modes = 5
theta = np.zeros((Nx, Nx, Nx))
for _ in range(n_modes):
    kx, ky, kz = np.random.randint(1, 4, size=3)
    amp = np.random.uniform(0.05, 0.2)
    phase = np.random.uniform(0, 2*np.pi)
    theta += amp * np.sin(2*np.pi*(kx*X + ky*Y + kz*Z) / L + phase)


def gradient(f, dx):
    """Central difference gradient, periodic BCs."""
    g = np.zeros((3,) + f.shape)
    for i in range(3):
        g[i] = (np.roll(f, -1, axis=i) - np.roll(f, 1, axis=i)) / (2*dx)
    return g


def second_deriv(f, dx, i, j):
    """Second partial derivative ∂_i ∂_j f, central difference."""
    # First take ∂_j
    df_j = (np.roll(f, -1, axis=j) - np.roll(f, 1, axis=j)) / (2*dx)
    # Then take ∂_i
    return (np.roll(df_j, -1, axis=i) - np.roll(df_j, 1, axis=i)) / (2*dx)


# --- Compute the metric γ_ij = δ_ij - ⟨∂_iθ ∂_jθ⟩ ---
# For a single deterministic field, ⟨...⟩ is just the field value itself.
# The metric is pointwise: γ_ij(x) = δ_ij - ∂_iθ(x) ∂_jθ(x)
grad_theta = gradient(theta, dx)  # shape (3, Nx, Nx, Nx)

gamma = np.zeros((3, 3, Nx, Nx, Nx))
dgamma = np.zeros((3, 3, 3, Nx, Nx, Nx))  # ∂_k γ_ij

for i in range(3):
    for j in range(3):
        gamma[i, j] = (1.0 if i == j else 0.0) - grad_theta[i] * grad_theta[j]

# ∂_k γ_ij = -∂_k(∂_iθ ∂_jθ) = -(∂_k∂_iθ)(∂_jθ) - (∂_iθ)(∂_k∂_jθ)
for k in range(3):
    for i in range(3):
        for j in range(3):
            d2_ki = second_deriv(theta, dx, k, i)
            d2_kj = second_deriv(theta, dx, k, j)
            dgamma[k, i, j] = -(d2_ki * grad_theta[j] + grad_theta[i] * d2_kj)


# --- Method (a): Levi-Civita from γ and ∂γ ---
# Γ^k_ij = (1/2) γ^{kl} (∂_i γ_{jl} + ∂_j γ_{il} - ∂_l γ_{ij})

# Invert γ at each point
gamma_inv = np.zeros_like(gamma)
for ix in range(Nx):
    for iy in range(Nx):
        for iz in range(Nx):
            g = gamma[:, :, ix, iy, iz]
            gamma_inv[:, :, ix, iy, iz] = np.linalg.inv(g)

Gamma_LC = np.zeros((3, 3, 3, Nx, Nx, Nx))  # Γ^k_ij
for k in range(3):
    for i in range(3):
        for j in range(3):
            for l in range(3):
                Gamma_LC[k, i, j] += 0.5 * gamma_inv[k, l] * (
                    dgamma[i, j, l] + dgamma[j, i, l] - dgamma[l, i, j]
                )


# --- Method (b): From θ-correlations ---
# T_ijl = (∂_i∂_j θ)(∂_l θ) + (∂_j θ)(∂_i∂_l θ)
# ∂_k γ_ij = -T_kij  (by chain rule)
# So Γ^k_ij = (1/2) γ^{kl} (-T_{ijl} - T_{jil} + T_{lij})
# But T_kij = -∂_k γ_ij, so this is the same formula. Let's verify directly.

T = np.zeros((3, 3, 3, Nx, Nx, Nx))
for i in range(3):
    for j in range(3):
        for l in range(3):
            d2_ij = second_deriv(theta, dx, i, j)
            d2_il = second_deriv(theta, dx, i, l)
            T[i, j, l] = d2_ij * grad_theta[l] + grad_theta[j] * d2_il

# Note: ∂_k γ_ij = -T_{kij} (the three-point correlation with the
# differentiation indices matching the metric derivative index pattern)
# Verify this identity first:
print("=== Step 1: Christoffel Tautology Verification ===\n")

max_err_dgamma = 0.0
for k in range(3):
    for i in range(3):
        for j in range(3):
            err = np.max(np.abs(dgamma[k, i, j] + T[k, i, j]))
            max_err_dgamma = max(max_err_dgamma, err)

print(f"Identity check: max|∂_k γ_ij + T_kij| = {max_err_dgamma:.2e}")
print(f"  (Should be ~0 up to numerical differentiation error)\n")

# Now compute Christoffel from T:
Gamma_T = np.zeros((3, 3, 3, Nx, Nx, Nx))
for k in range(3):
    for i in range(3):
        for j in range(3):
            for l in range(3):
                # ∂_i γ_{jl} = -T_{ijl}, etc.
                Gamma_T[k, i, j] += 0.5 * gamma_inv[k, l] * (
                    -T[i, j, l] - T[j, i, l] + T[l, i, j]
                )

# Compare
max_diff = 0.0
for k in range(3):
    for i in range(3):
        for j in range(3):
            diff = np.max(np.abs(Gamma_LC[k, i, j] - Gamma_T[k, i, j]))
            max_diff = max(max_diff, diff)

max_gamma = np.max(np.abs(Gamma_LC))
print(f"Christoffel comparison:")
print(f"  max|Γ^k_ij (Levi-Civita)| = {max_gamma:.4e}")
print(f"  max|Γ^k_ij (from T) - Γ^k_ij (LC)| = {max_diff:.2e}")
print(f"  Relative error: {max_diff/max_gamma:.2e}")
print()

if max_diff / max_gamma < 1e-6:
    print("✓ PASS: The three-point correlations reproduce Levi-Civita exactly")
    print("  (up to numerical differentiation error).")
    print("  This confirms the tautology: Γ of γ IS expressible in terms of θ-correlations.")
else:
    print("✗ FAIL: Unexpected discrepancy. Check numerical differentiation.")

print()

# --- Metric compatibility check ---
# ∇_k γ_ij = ∂_k γ_ij - Γ^l_ki γ_lj - Γ^l_kj γ_il
# Should be 0 identically for Levi-Civita

max_nabla_g = 0.0
for k in range(3):
    for i in range(3):
        for j in range(3):
            nabla_g = dgamma[k, i, j].copy()
            for l in range(3):
                nabla_g -= Gamma_LC[l, k, i] * gamma[l, j]
                nabla_g -= Gamma_LC[l, k, j] * gamma[i, l]
            max_nabla_g = max(max_nabla_g, np.max(np.abs(nabla_g)))

print(f"Metric compatibility: max|∇_k γ_ij| = {max_nabla_g:.2e}")
print(f"  (Should be ~0: Levi-Civita is metric-compatible by construction)")
