"""
Medium-swap simulator — framework-native demonstration of the
three-class partition (tuba / contrabass / loudspeaker) from
medium_change_demo.md.

The structural claim, not the instrumental analogy:

  TUBA       — value depends on the medium-state's parameters.
               Dimensional under unit-system swap; depth-dependent
               under Fibonacci-depth swap.
  CONTRABASS — forced rational from substrate combinatorics.  Same
               numerical value in every medium state, *by derivation*.
  LOUDSPEAKER— fitted post-hoc / measured-and-inserted.  Same
               numerical value in every medium state, *by definition*.
               Visually identical to contrabass rows; the C–L
               distinction lives in the "form" column, where
               contrabass rows carry a derived rational and
               loudspeaker rows carry only an input number.

Two medium axes, both framework-native:

  Axis A — Unit-system swap (unitless_check.md territory).
           SI / per-second / Planck / GeV.  Dimensional rows shift;
           dimensionless ratios stay constant.

  Axis B — Fibonacci-depth swap (our_address.py step 2 territory).
           H_0(d) = ω_Planck · φ^(−2d).  Observers at different
           Fibonacci depths see H_0 and t_Hubble shift by φ²ⁿ per
           integer level.  Forced rationals (Ω_Λ, K_c, α_s/α_2,
           K_STAR) are depth-invariant because they are derived from
           substrate combinatorics that do not depend on depth.

All numbers either (a) external observables (CODATA / PDG / Planck 2018),
or (b) derived from substrate primitives (our_address.py + canonical_glossary.md),
or (c) explicitly labeled as SM-fitted inputs.  No notional placeholders.
"""

import math


# =========================================================================
# CLASS LABELS
# =========================================================================

TUBA        = "tuba"
CONTRABASS  = "contrabass"
LOUDSPEAKER = "loudspeaker"

CLASS_TAG  = {TUBA: "T",  CONTRABASS: "C",  LOUDSPEAKER: "L"}


# =========================================================================
# PHYSICAL ANCHORS (CODATA / Planck 2018)
# =========================================================================

HBAR_J_S     = 1.054571817e-34     # J·s   (CODATA)
G_SI         = 6.67430e-11         # m³ kg⁻¹ s⁻²
C_M_S        = 2.99792458e8        # m/s   (exact, SI definition)
KB_J_K       = 1.380649e-23        # J/K   (exact, SI 2019)
EV_J         = 1.602176634e-19     # J     (exact, SI 2019)
GEV_J        = 1.0e9 * EV_J
HBAR_GEV_S   = HBAR_J_S / GEV_J    # GeV·s

M_E_KG       = 9.1093837015e-31    # kg    (CODATA)
M_P_KG       = 1.67262192369e-27   # kg    (CODATA)
M_E_OVER_M_P = M_E_KG / M_P_KG     # ≈ 5.446e-4 (dimensionless ratio)

T_PLANCK_S      = math.sqrt(HBAR_J_S * G_SI / C_M_S ** 5)   # ≈ 5.39e-44 s
L_PLANCK_M      = math.sqrt(HBAR_J_S * G_SI / C_M_S ** 3)
E_PLANCK_J      = math.sqrt(HBAR_J_S * C_M_S ** 5 / G_SI)
M_PLANCK_KG     = math.sqrt(HBAR_J_S * C_M_S / G_SI)
OMEGA_PLANCK_HZ = 1.0 / T_PLANCK_S

H0_KMS_MPC      = 67.4              # Planck 2018
MPC_M           = 3.0857e22
H0_PER_S        = H0_KMS_MPC * 1.0e3 / MPC_M  # ≈ 2.18e-18 s⁻¹
T_HUBBLE_S      = 1.0 / H0_PER_S
T_HUBBLE_YR     = T_HUBBLE_S / 3.156e7

# Framework primitives
PHI       = (1.0 + math.sqrt(5.0)) / 2.0
PHI_SQ    = PHI * PHI
LN_PHI_SQ = math.log(PHI_SQ)
D_NOW     = math.log(OMEGA_PLANCK_HZ / H0_PER_S) / LN_PHI_SQ   # ≈ 145.7718

# Forced rationals (from canonical_glossary.md, MANIFEST.yml, medium_change_demo.md)
OMEGA_LAMBDA   = 13.0 / 19.0
ALPHA_S_OVER_2 = 27.0 / 8.0
K_C            = 2.0 / math.pi
K_STAR         = 2.0 ** (-3.0 / 14.0)


# =========================================================================
# AXIS A — UNIT-SYSTEM SWAP
# =========================================================================
# For each unit-system column, each row reports the same physical
# quantity expressed in that system.  Dimensionless quantities take the
# same numerical value in every column; dimensional ones do not.

# Conversion helpers
def to_per_second(value, from_unit):
    if from_unit == "Hz":    return value
    if from_unit == "s":     return 1.0 / value
    raise ValueError(from_unit)


UNIT_COLUMNS = ["SI", "per-second (s⁻¹)", "Planck units", "GeV (HEP nat.)"]
BASELINE_UNIT_COLUMN = "SI"


def render_in_units(quantity_label):
    """Return [(unit_col, value, unit_string), ...] for a named observable.

    Quantities are computed directly — no inferred conversions; each
    cell is the framework-canonical or CODATA value in that unit system.
    """
    if quantity_label == "H_0  (Hubble rate)":
        return [
            ("SI",               H0_KMS_MPC,                "km/s/Mpc"),
            ("per-second (s⁻¹)", H0_PER_S,                  "s⁻¹"),
            ("Planck units",     H0_PER_S * T_PLANCK_S,     "/ω_Planck"),
            ("GeV (HEP nat.)",   H0_PER_S * HBAR_GEV_S,     "GeV"),
        ]
    if quantity_label == "t_Hubble  (= 1/H_0)":
        return [
            ("SI",               T_HUBBLE_YR,               "yr"),
            ("per-second (s⁻¹)", T_HUBBLE_S,                "s"),
            ("Planck units",     T_HUBBLE_S / T_PLANCK_S,   "/t_Planck"),
            ("GeV (HEP nat.)",   T_HUBBLE_S / HBAR_GEV_S,   "GeV⁻¹"),
        ]
    if quantity_label == "ω_Planck  (Planck frequency)":
        return [
            ("SI",               OMEGA_PLANCK_HZ,           "Hz"),
            ("per-second (s⁻¹)", OMEGA_PLANCK_HZ,           "s⁻¹"),
            ("Planck units",     1.0,                       "≡ 1"),
            ("GeV (HEP nat.)",   OMEGA_PLANCK_HZ * HBAR_GEV_S, "GeV"),
        ]
    if quantity_label == "m_electron  (electron rest mass)":
        return [
            ("SI",               M_E_KG,                    "kg"),
            ("per-second (s⁻¹)", M_E_KG * C_M_S**2 / HBAR_J_S, "rad/s"),
            ("Planck units",     M_E_KG / M_PLANCK_KG,      "/m_Planck"),
            ("GeV (HEP nat.)",   M_E_KG * C_M_S**2 / GEV_J, "GeV"),
        ]
    if quantity_label == "Ω_Λ  (= 13/19)":
        return [(col, OMEGA_LAMBDA, "—") for col in UNIT_COLUMNS]
    if quantity_label == "α_s / α_2  (= 27/8)":
        return [(col, ALPHA_S_OVER_2, "—") for col in UNIT_COLUMNS]
    if quantity_label == "K_c  (= 2/π)":
        return [(col, K_C, "—") for col in UNIT_COLUMNS]
    if quantity_label == "K_STAR  (= 2^{-3/14})":
        return [(col, K_STAR, "—") for col in UNIT_COLUMNS]
    if quantity_label == "Ω_Λ + Ω_m  (= 1)":
        return [(col, 1.0, "—") for col in UNIT_COLUMNS]
    if quantity_label == "m_e / m_proton  (CODATA fit)":
        return [(col, M_E_OVER_M_P, "—") for col in UNIT_COLUMNS]
    if quantity_label == "n_s  (spectral tilt, Planck 2018 fit)":
        return [(col, 0.9649, "—") for col in UNIT_COLUMNS]
    raise ValueError(quantity_label)


# (label, class, form-string for the "where the number came from" column)
UNIT_OBSERVABLES = [
    # --- TUBA (dimensional; shifts under unit swap) ---
    ("H_0  (Hubble rate)",                 TUBA,        "dimensional [time⁻¹]"),
    ("t_Hubble  (= 1/H_0)",                TUBA,        "dimensional [time]"),
    ("ω_Planck  (Planck frequency)",       TUBA,        "dimensional [time⁻¹]"),
    ("m_electron  (electron rest mass)",   TUBA,        "dimensional [mass]"),
    # --- CONTRABASS (dimensionless rationals from substrate) ---
    ("Ω_Λ  (= 13/19)",                     CONTRABASS,  "13/19  [Stern-Brocot, F_6]"),
    ("α_s / α_2  (= 27/8)",                CONTRABASS,  "q_3³/q_2³  [Mihailescu cube]"),
    ("K_c  (= 2/π)",                       CONTRABASS,  "Kuramoto critical, structural"),
    ("K_STAR  (= 2^{-3/14})",              CONTRABASS,  "K-iteration target, substrate"),
    ("Ω_Λ + Ω_m  (= 1)",                   CONTRABASS,  "closure identity"),
    # --- LOUDSPEAKER (dimensionless SM fits) ---
    ("m_e / m_proton  (CODATA fit)",       LOUDSPEAKER, "measured ratio, inserted"),
    ("n_s  (spectral tilt, Planck 2018 fit)", LOUDSPEAKER, "measured tilt, inserted"),
]


# =========================================================================
# AXIS B — FIBONACCI-DEPTH SWAP
# =========================================================================
# Same observable rows, swept across cosmic depth d using
# H_0(d) = ω_Planck · φ^(−2d) (our_address.py step 2).  Dimensional
# observables that depend on H_0 shift by exactly φ² per integer level.
# Forced rationals and SM fits do not depend on d.

DEPTH_OFFSETS = [-6, -3, -1, 0, +1, +3, +6]
BASELINE_DEPTH_LABEL = "d_now"


def H0_at_depth_per_s(d):
    return OMEGA_PLANCK_HZ * PHI_SQ ** (-d)


def render_at_depth(quantity_label):
    """Same observables as Axis A, but parametric in depth d (in SI units)."""
    values = []
    for offset in DEPTH_OFFSETS:
        d  = D_NOW + offset
        H  = H0_at_depth_per_s(d)
        tH = 1.0 / H
        label = "d_now" if offset == 0 else f"d_now{offset:+d}"
        if quantity_label == "H_0  (km/s/Mpc)":
            values.append((label, H * MPC_M / 1.0e3, "km/s/Mpc"))
        elif quantity_label == "t_Hubble  (yr)":
            values.append((label, tH / 3.156e7,        "yr"))
        elif quantity_label == "ω_Planck  (Hz)":
            values.append((label, OMEGA_PLANCK_HZ,     "Hz"))
        elif quantity_label == "m_electron  (kg)":
            values.append((label, M_E_KG,              "kg"))
        elif quantity_label == "Ω_Λ":
            values.append((label, OMEGA_LAMBDA,        "—"))
        elif quantity_label == "α_s / α_2":
            values.append((label, ALPHA_S_OVER_2,      "—"))
        elif quantity_label == "K_c":
            values.append((label, K_C,                 "—"))
        elif quantity_label == "K_STAR":
            values.append((label, K_STAR,              "—"))
        elif quantity_label == "Ω_Λ + Ω_m":
            values.append((label, 1.0,                 "—"))
        elif quantity_label == "m_e / m_proton":
            values.append((label, M_E_OVER_M_P,        "—"))
        elif quantity_label == "n_s":
            values.append((label, 0.9649,              "—"))
        else:
            raise ValueError(quantity_label)
    return values


# (label, class, form-string).  Two of the unit-axis dimensional rows
# (ω_Planck, m_electron) are depth-invariant — they don't depend on H_0 —
# so they're listed here to show that "tuba under unit swap" is not the
# same set as "tuba under depth swap".  This is a real piece of framework
# content: classes are *per-axis*, not absolute.

DEPTH_OBSERVABLES = [
    # --- TUBA UNDER DEPTH (shifts with d) ---
    ("H_0  (km/s/Mpc)",      TUBA,        "ω_Planck · φ^(−2d)  [depth-dependent]"),
    ("t_Hubble  (yr)",       TUBA,        "1/H_0(d)            [depth-dependent]"),
    # --- ROW THAT IS *NOT* TUBA UNDER DEPTH (but IS under unit swap) ---
    ("ω_Planck  (Hz)",       CONTRABASS,  "structural anchor, depth-independent"),
    ("m_electron  (kg)",     CONTRABASS,  "particle rest mass, depth-independent"),
    # --- CONTRABASS (depth-invariant; same forced rationals as Axis A) ---
    ("Ω_Λ",                  CONTRABASS,  "13/19, depth-fixed"),
    ("α_s / α_2",            CONTRABASS,  "27/8, depth-fixed"),
    ("K_c",                  CONTRABASS,  "2/π, depth-fixed"),
    ("K_STAR",               CONTRABASS,  "2^{-3/14}, depth-fixed"),
    ("Ω_Λ + Ω_m",            CONTRABASS,  "= 1, closure"),
    # --- LOUDSPEAKER ---
    ("m_e / m_proton",       LOUDSPEAKER, "measured input"),
    ("n_s",                  LOUDSPEAKER, "measured input"),
]


# =========================================================================
# RENDERING
# =========================================================================

def fmt_val(v):
    if v is None:
        return "      --"
    if abs(v) >= 1.0e5 or (v != 0.0 and abs(v) < 1.0e-3):
        return f"{v:>10.3e}"
    return f"{v:>10.4f}"


def invariance_check(values, base_value, tol=1.0e-9):
    nums = [v for _, v, _ in values if v is not None]
    if not nums or base_value in (None, 0.0):
        return None, False
    shifts   = [abs(v - base_value) / abs(base_value) for v in nums]
    max_shift = max(shifts)
    return max_shift, max_shift < tol


def print_axis_a_table():
    print("=" * 144)
    print("AXIS A — UNIT-SYSTEM SWAP   (each cell = same physical quantity, expressed in that unit system)")
    print("Class:  T = tuba (shifts under swap)   C = contrabass (forced rational, derived)   "
          "L = loudspeaker (fitted input, postulated)")
    print("=" * 144)

    name_w = 38
    cell_w = 16
    header = f"{'observable':<{name_w}} {'cl':>3}  " \
             + "  ".join(f"{c[:cell_w]:>{cell_w}}" for c in UNIT_COLUMNS) \
             + f"  {'invariant?':>11}  {'form':>34}"
    print(header)
    print("-" * len(header))

    for label, cls, form in UNIT_OBSERVABLES:
        cells = render_in_units(label)
        # Reorder to UNIT_COLUMNS just in case
        by_col = {c: (v, u) for (c, v, u) in cells}
        cell_strs = "  ".join(f"{fmt_val(by_col[c][0]):>{cell_w}}" for c in UNIT_COLUMNS)

        base_v, _ = by_col[BASELINE_UNIT_COLUMN]
        values = [(c, by_col[c][0], by_col[c][1]) for c in UNIT_COLUMNS]
        max_shift, invariant = invariance_check(values, base_v)
        inv_str = "= (flat)" if invariant else f"~ ({100*max_shift:.1e}%)" if max_shift else "—"

        print(f"{label[:name_w]:<{name_w}} {CLASS_TAG[cls]:>3}  {cell_strs}  "
              f"{inv_str:>11}  {form:>34}")

    print("-" * len(header))
    print("Reading:")
    print("  T rows shift across columns because they carry dimensions; the numerical value depends on the unit system.")
    print("  C rows are flat because the value is a forced rational (Stern-Brocot 13/19; q_3³/q_2³; etc.) — same number in any unit.")
    print("  L rows are flat for the same numerical reason — but for a *different epistemic reason*: the value was MEASURED")
    print("  and INSERTED, not derived.  The C/L visual ambiguity here is what the framework's main move dissolves.")


def print_axis_b_table():
    print("\n" + "=" * 144)
    print("AXIS B — FIBONACCI-DEPTH SWAP   (each cell = observable at Fibonacci depth d_now + offset, in SI units)")
    print(f"H_0(d) = ω_Planck · φ^(−2d);   φ² = {PHI_SQ:.4f};   d_now = {D_NOW:.4f}  →  H_0 = {H0_KMS_MPC} km/s/Mpc")
    print(f"Per integer level deeper: H_0 × 1/φ² ≈ {1.0/PHI_SQ:.4f}.  Present Hubble sits *between* integer levels {int(D_NOW)} and {int(D_NOW)+1}.")
    print("=" * 144)

    name_w = 22
    cell_w = 13
    headers = ["d_now" if o == 0 else f"d_now{o:+d}" for o in DEPTH_OFFSETS]
    header = f"{'observable':<{name_w}} {'cl':>3}  " \
             + "  ".join(f"{h:>{cell_w}}" for h in headers) \
             + f"  {'invariant?':>11}  {'form':>40}"
    print(header)
    print("-" * len(header))

    for label, cls, form in DEPTH_OBSERVABLES:
        cells = render_at_depth(label)
        cell_strs = "  ".join(f"{fmt_val(v):>{cell_w}}" for (_, v, _) in cells)

        base_v = next(v for (h, v, _) in cells if h == BASELINE_DEPTH_LABEL)
        max_shift, invariant = invariance_check(cells, base_v)
        inv_str = "= (flat)" if invariant else f"~ ({max_shift:.1e}×)" if max_shift else "—"

        print(f"{label[:name_w]:<{name_w}} {CLASS_TAG[cls]:>3}  {cell_strs}  "
              f"{inv_str:>11}  {form:>40}")

    print("-" * len(header))
    print("Reading:")
    print("  T rows (H_0, t_Hubble) shift by φ²ⁿ per integer level — observers at different depths see different values.")
    print("  ω_Planck and m_electron are *C-class under depth swap* but T-class under unit swap — the partition is per-axis.")
    print("  C rows (13/19, 27/8, 2/π, K_STAR, closure) are exactly flat — forced by substrate combinatorics, depth-blind.")
    print("  L rows (m_e/m_p, n_s) are flat for the trivial reason: input numbers don't depend on cosmic state.")


# =========================================================================
# MAIN
# =========================================================================

def main():
    print_axis_a_table()
    print_axis_b_table()
    print()
    print("Cross-axis observation: a row's class depends on which medium axis you're swapping.")
    print("  ω_Planck is tuba under unit swap (dimensional → different numerical value in each system)")
    print("                  contrabass under depth swap (structural anchor → depth-independent).")
    print("  Ω_Λ = 13/19 is contrabass on *both* axes — that is the framework's strong invariance claim.")
    print()
    print("The two visually-indistinct flatnesses (C vs L) are distinguished by the 'form' column:")
    print("  derived rational (Stern-Brocot, Mihailescu, q_2³/q_3³, 2/π) → contrabass;")
    print("  measured-and-inserted input → loudspeaker.")
    print("Distinguishing the two is the framework's main empirical move (medium_change_demo.md).")


if __name__ == "__main__":
    main()
