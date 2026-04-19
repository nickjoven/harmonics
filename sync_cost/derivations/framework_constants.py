"""
Framework constants -- single source of truth.

Centralizes every numerical constant and PDG value used across the
harmonics framework. Importing from here is the only consistent way
to reference framework values; do not redefine these locally.

Contents
--------
Klein bottle integers:
    Q2, Q3         -- denominator classes from XOR filter
    D              -- spatial dimension (= 3)
    K_LEPTON       -- lepton sector constant (q_3^2 = 9)
    K_QUARK        -- quark sector constant (q_2^3 = 8)
    MEDIANT        -- mediant sum q_2 + q_3 = 5
    INTERACT       -- interaction scale q_2 * q_3 = 6
    F_6_COUNT      -- |F_6| = 13
    F_7_COUNT      -- |F_7| = 19
    R_HIERARCHY    -- 6 * 13^54 (Planck/Hubble)

Irrationals:
    PHI, INV_PHI, INV_PHI_SQ

Self-consistent coupling:
    K_STAR          -- 0.86196052, joint matter-sector closure
                       (item12_K_star_closure.py)
    K_STAR_PRECISE  -- alias of K_STAR (kept for backwards compat)
    K_STAR_OVER_2   -- K_STAR / 2

Electroweak scale:
    V_GEV, V_MEV, V_EV

PDG masses (central values, MeV):
    PDG_MASS[name], M_E, M_MU, M_TAU, M_U, M_C, M_T, M_D, M_S, M_B,
    M_H, M_W, M_Z

Couplings at M_Z (PDG 2024):
    ALPHA_S_MZ, ALPHA_EM_MZ, SIN2_TW_MZ, ALPHA_2_MZ, ALPHA_Y_MZ

Cosmological parameters:
    OMEGA_B, OMEGA_DM, OMEGA_L, OMEGA_M (framework fractions)
    H_0_SI         -- Hubble constant (Planck 2018, s^-1)
    H_0_KM_S_MPC   -- Hubble constant in km/s/Mpc (Planck 2018)
    T_H            -- Hubble time (1/H_0), in seconds
    LAMBDA_SI      -- cosmological constant (m^-2, derived from H_0, Omega_L)
    L_H_HUBBLE     -- Hubble radius (c/H_0), meters

Physical constants (SI, CODATA 2022):
    HBAR, G_NEWTON, C_LIGHT

Planck units (derived):
    ELL_P          -- Planck length (m)
    T_P            -- Planck time (s)
    M_P            -- Planck mass (kg)

Kuramoto dynamics:
    LAMBDA_UNLOCK  -- Klein-bottle Lyapunov on unlocked sector
                      (gap2 sub-problem C, at K -> 1)

Framework-special integer set:
    FRAMEWORK_INTEGERS
"""

import math

# ============================================================================
# Klein bottle integers and derived sector constants
# ============================================================================

Q2: int = 2
Q3: int = 3
D: int = 3                                        # spatial dimension

K_LEPTON: int = Q3 ** 2                           # = 9
K_QUARK: int = Q2 ** 3                            # = 8
MEDIANT: int = Q2 + Q3                            # = 5
INTERACT: int = Q2 * Q3                           # = 6

# Farey counts at the interaction scale and one beyond
F_6_COUNT: int = 13                               # |F_6|
F_7_COUNT: int = 19                               # |F_7|

# Planck/Hubble hierarchy ratio
R_HIERARCHY: int = 6 * 13 ** 54                   # ~ 8.5e60


# ============================================================================
# Irrational constants from Fibonacci / golden ratio
# ============================================================================

PHI: float = (1 + math.sqrt(5)) / 2               # golden ratio
INV_PHI: float = 1 / PHI                          # = PHI - 1
INV_PHI_SQ: float = 1 / (PHI * PHI)               # = 2 - PHI


# ============================================================================
# Self-consistent Kuramoto coupling
# ============================================================================

# K_STAR is the framework's fixed-point coupling from the joint matter-
# sector self-consistency closure (item12_K_star_closure.py).  Three
# independent extractions from m_tau/m_mu, m_t/m_c, m_b/m_s via the
# parabola rotation a_1(sector)^2 * K*^2 = N(sector) agree with
# chi^2/dof = 0.06 (<< 1 sigma pairwise), giving
#
#     K*_joint = sqrt(N(sector)) / a_1(sector)
#              = 0.86196052 +/- 2.06e-5
#
# Uses only sector integers {4, 9, 24} (d-independent, from reading D
# + Klein topology) and PDG 2024 mass ratios.  Under this value the
# lepton identity a_1(lep) * K* = q_2 = 2 closes exactly at machine
# precision (residual ~1e-7).
K_STAR: float = 0.86196052

# Backwards-compatible alias (some scripts import this name).
K_STAR_PRECISE: float = K_STAR

K_STAR_OVER_2: float = K_STAR / 2                 # frequent in tongue formulas


# ============================================================================
# Electroweak scale
# ============================================================================

V_GEV: float = 246.22                             # Higgs VEV, from G_F
V_MEV: float = V_GEV * 1e3
V_EV: float = V_GEV * 1e9


# ============================================================================
# PDG masses, central value with 1-sigma uncertainty in MeV
# PDG 2024 unless noted
# ============================================================================

PDG_MASS: dict[str, tuple[float, float]] = {
    # charged leptons
    "e":        (0.51099895,   0.0000000015),
    "mu":       (105.6583755,  0.0000023),
    "tau":      (1776.86,      0.12),

    # up-type quarks
    "u":        (2.16,         0.49),             # MS-bar at 2 GeV
    "c":        (1270.0,       20.0),
    "t":        (172760.0,     400.0),

    # down-type quarks
    "d":        (4.67,         0.48),
    "s":        (93.4,         8.0),
    "b":        (4180.0,       30.0),

    # Higgs and gauge bosons
    "H":        (125250.0,     170.0),            # 125.25 +/- 0.17 GeV
    "W":        (80369.2,      13.3),             # PDG 2024 world average
    "Z":        (91187.6,      2.1),              # PDG world average
}


def mass(name: str) -> float:
    """Central PDG mass in MeV."""
    return PDG_MASS[name][0]


def mass_err(name: str) -> float:
    """1-sigma PDG uncertainty in MeV."""
    return PDG_MASS[name][1]


# Convenience singletons (MeV)
M_E:   float = mass("e")
M_MU:  float = mass("mu")
M_TAU: float = mass("tau")
M_U:   float = mass("u")
M_C:   float = mass("c")
M_T:   float = mass("t")
M_D:   float = mass("d")
M_S:   float = mass("s")
M_B:   float = mass("b")
M_H:   float = mass("H")
M_W:   float = mass("W")
M_Z:   float = mass("Z")


# ============================================================================
# Couplings at M_Z (PDG 2024)
# ============================================================================

ALPHA_S_MZ:   float = 0.1179                      # strong
ALPHA_EM_MZ:  float = 1 / 127.94                  # electromagnetic
SIN2_TW_MZ:   float = 0.23122                     # sin^2(theta_W)

# Derived from sin^2 and alpha_em
ALPHA_2_MZ:   float = ALPHA_EM_MZ / SIN2_TW_MZ
ALPHA_Y_MZ:   float = ALPHA_EM_MZ / (1 - SIN2_TW_MZ)


# ============================================================================
# Cosmological parameters
# ============================================================================

OMEGA_B:  float = 1 / 19                          # baryons
OMEGA_DM: float = 5 / 19                          # dark matter
OMEGA_L:  float = 13 / 19                         # dark energy (= |F_6| / |F_7|)
OMEGA_M:  float = 6 / 19                          # total matter

# Hubble parameter (Planck 2018 TT,TE,EE+lowE+lensing+BAO)
H_0_KM_S_MPC: float = 67.4                        # km / s / Mpc
H_0_SI:       float = H_0_KM_S_MPC * 1e3 / 3.0857e22   # s^-1 ~ 2.184e-18
T_H:          float = 1.0 / H_0_SI                # Hubble time, seconds

# Cosmological constant (from H_0 and Omega_L, observed)
LAMBDA_SI:    float = 3 * 0.6847 * H_0_SI ** 2 / (299792458.0 ** 2)   # m^-2

# Hubble radius (c/H_0)
L_H_HUBBLE:   float = 299792458.0 / H_0_SI        # meters, ~1.373e26


# ============================================================================
# Physical constants (SI, CODATA 2022)
# ============================================================================

HBAR:     float = 1.054571817e-34                 # J * s
G_NEWTON: float = 6.67430e-11                     # m^3 kg^-1 s^-2
C_LIGHT:  float = 299792458.0                     # m / s (exact)


# ============================================================================
# Planck units (derived from HBAR, G_NEWTON, C_LIGHT)
# ============================================================================

ELL_P: float = math.sqrt(HBAR * G_NEWTON / C_LIGHT ** 3)     # ~1.616e-35 m
T_P:   float = ELL_P / C_LIGHT                                # ~5.391e-44 s
M_P:   float = math.sqrt(HBAR * C_LIGHT / G_NEWTON)           # ~2.176e-8 kg


# ============================================================================
# Kuramoto Lyapunov constant
# ============================================================================

# Klein-bottle Lyapunov exponent on the unlocked sector, at K = 1.
# From gap2_spatialization_decomposition.md sub-problem C:
#     lambda_unlock(K) = (1/pi) * integral over [pi/2, 3pi/2] of
#                        ln(1 + K|cos theta|) dtheta
#
# Closed-form K = 1 limit (verified by a_s_phase0_lambda_audit.py):
#     lambda_unlock(1) = (4G - pi ln 2) / pi
#                      = 4 G/pi - ln 2
#                      ~= 0.473096
# where G = Catalan's constant ~= 0.915966.  An earlier comment here
# claimed lambda_unlock(1) = 2 G / pi ~= 0.583; that was INCORRECT --
# the 2 G / pi value does not match the numerical integration of the
# defining integral.  The (4G - pi ln 2)/pi closed form matches
# numerical integration to 9 digits.
LAMBDA_UNLOCK: float = 0.473096


# ============================================================================
# Framework-special integer set
# Integers that come from q_2, q_3, their simple combinations, and the
# cosmological partition. Used by structural-reading helpers.
# ============================================================================

FRAMEWORK_INTEGERS: frozenset[int] = frozenset({
    1,                                            # root
    Q2, Q3,                                       # 2, 3
    Q2 + Q3,                                      # 5 (mediant)
    Q2 * Q3,                                      # 6 (interaction)
    Q2 ** 2,                                      # 4
    Q3 ** 2,                                      # 9 (k_lepton)
    Q2 ** 3,                                      # 8 (k_quark)
    Q2 ** 2 * Q3,                                 # 12 (2 * interaction)
    F_6_COUNT,                                    # 13
    F_7_COUNT,                                    # 19
    (Q2 + Q3) ** 2,                               # 25
    Q2 * Q3 * Q3,                                 # 18 (Q_Y tree inv)
    Q2 ** 3 + Q3 ** 3,                            # 35 (duty budget)
})
