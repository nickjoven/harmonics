"""
Framework constants -- single source of truth.

This module centralizes every numerical constant and PDG value used
across the harmonics framework. Before this module, constants were
redefined independently in 30-50 files with occasional drift (e.g.
K_STAR = 0.862 in some scripts vs 0.8668 in others after a refit
was later retracted). Importing from here is the only consistent
way to reference framework values going forward.

Contents
--------
Integers from the Klein bottle topology:
    Q2, Q3         -- denominator classes from XOR filter
    D              -- spatial dimension (= 3)
    K_LEPTON       -- lepton sector constant (q_3^2 = 9)
    K_QUARK        -- quark sector constant (q_2^3 = 8)
    MEDIANT        -- mediant sum q_2 + q_3 = 5
    INTERACT       -- interaction scale q_2 * q_3 = 6
    F_6_COUNT      -- |F_6| = 13 (Farey 6)
    F_7_COUNT      -- |F_7| = 19 (Farey 7)
    R_HIERARCHY    -- 6 * 13^54 (Planck/Hubble)

Irrationals:
    PHI            -- golden ratio (1 + sqrt(5)) / 2
    INV_PHI        -- 1/phi
    INV_PHI_SQ     -- 1/phi^2 = 2 - phi

Self-consistent coupling:
    K_STAR         -- 0.862 (from boundary_weight.md; canonical)

Electroweak scale:
    V_GEV          -- 246.22 GeV
    V_MEV          -- V_GEV * 1e3
    V_EV           -- V_GEV * 1e9

PDG masses (central values, MeV):
    PDG_MASS[name] -- dict mapping particle name to (central, 1-sigma) in MeV
    M_E, M_MU, M_TAU, M_U, M_C, M_T, M_D, M_S, M_B, M_H, M_W, M_Z

Couplings at M_Z (PDG 2024):
    ALPHA_S_MZ, ALPHA_EM_MZ, SIN2_TW_MZ

Framework-special integer set (used by structural-reading helpers):
    FRAMEWORK_INTEGERS -- small set of integers that come from q_2, q_3,
                          their simple combinations, and cosmological
                          partition numerators
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

# K_STAR is the framework's fixed point coupling from the boundary-weight
# derivation (boundary_weight.md), where Omega_Lambda = 13/19 is matched
# at w* = 0.83 and K* = 0.862. This is the CANONICAL value.
#
# An alternative K_STAR = 0.8668 was fit from neutrino splittings in the
# A-2 work and was later retracted in item12_sin_W_and_signs.py and
# elsewhere (see open_items.md). Use K_STAR below, not 0.8668.
K_STAR: float = 0.862

K_STAR_OVER_2: float = K_STAR / 2                 # 0.431, frequent in tongue formulas


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
