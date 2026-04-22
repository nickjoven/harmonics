"""
Framework predictions -- single structured source of truth.

Every framework numerical prediction is collected here as a
Prediction dataclass, with:

    name               -- short human-readable identifier
    sector             -- 'mass', 'gauge', 'cosmology', 'structural', etc.
    tree_form          -- string expression of the tree-level form
    tree_value         -- float value of the tree-level form
    correction_form    -- string expression of the correction (if any)
    correction_value   -- float value of the correction (if any)
    value              -- float value of the full framework prediction
    observed           -- float observed value
    observed_err       -- 1-sigma PDG uncertainty on observed
    source             -- filename where the derivation lives
    notes              -- free text

Use `all_predictions()` to get the list. Use `table()` to print a
formatted summary.

This replaces the per-script "print a line of output" pattern with
structured data that can be queried, filtered, and reported
consistently.

Usage
-----
    from framework_predictions import all_predictions, table
    table()                         # print full prediction table
    preds = all_predictions()       # get the dataclass list
    for p in preds:
        if p.rel_err_pct() > 1.0:
            print(f"{p.name}: {p.rel_err_pct():.2f}% off")
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Callable, Optional

from framework_constants import (
    ALPHA_S_MZ,
    F_7_COUNT,
    INV_PHI_SQ,
    K_LEPTON,
    K_QUARK,
    K_STAR,
    M_B, M_C, M_D, M_E, M_H, M_MU, M_S, M_T, M_TAU, M_U,
    M_Z,
    MEDIANT,
    OMEGA_L,
    PDG_MASS,
    PHI,
    Q2, Q3,
    SIN2_TW_MZ,
    V_GEV,
)
from framework_utils import fib


# ============================================================================
# Dataclass
# ============================================================================

@dataclass(frozen=True)
class Prediction:
    """One framework prediction with tree form, correction, and observed value."""

    name: str
    sector: str                                   # 'mass', 'gauge', 'cosmology', ...
    tree_form: str                                # e.g. "1/q_2^3"
    tree_value: float
    correction_form: str                          # e.g. "1/(q_2^2 q_3 |F_7|)", or "-"
    correction_value: float                       # 0.0 if no correction
    observed: float
    observed_err: float                           # 1-sigma uncertainty
    source: str                                   # path to source script
    notes: str = ""

    @property
    def value(self) -> float:
        """Full framework value = tree + correction."""
        return self.tree_value + self.correction_value

    @property
    def form(self) -> str:
        """Pretty-printed full form."""
        if self.correction_form and self.correction_form != "-":
            return f"{self.tree_form} + {self.correction_form}"
        return self.tree_form

    @property
    def abs_err(self) -> float:
        return abs(self.value - self.observed)

    def rel_err_pct(self) -> float:
        if self.observed == 0:
            return 0.0
        return self.abs_err / abs(self.observed) * 100

    def sigma_err(self) -> Optional[float]:
        """Distance from observed in PDG sigma units."""
        if self.observed_err == 0:
            return None
        return self.abs_err / self.observed_err

    def within_pdg(self) -> bool:
        """True if the framework prediction is consistent with observation
        within its PDG uncertainty, OR exactly correct when the observed
        value has no uncertainty (structural integers like dim = 3)."""
        if self.observed_err == 0:
            return self.abs_err == 0
        s = self.sigma_err()
        return s is not None and s <= 1.0


# ============================================================================
# Prediction assembly
# ============================================================================

def _all() -> list[Prediction]:
    """Populate the full prediction list."""
    preds: list[Prediction] = []

    # ------------------------------------------------------------------
    # STRUCTURAL (integer predictions, not fit to anything)
    # ------------------------------------------------------------------
    preds.append(Prediction(
        name="spatial dimension d",
        sector="structural",
        tree_form="dim SL(2,R) = n^2 - 1  (n=2)",
        tree_value=3.0,
        correction_form="-",
        correction_value=0.0,
        observed=3.0,
        observed_err=0.0,
        source="three_dimensions.md",
        notes="d = 3 from self-consistent adjacency + Bianchi classification",
    ))

    preds.append(Prediction(
        name="number of generations",
        sector="structural",
        tree_form="2^2 - 1",
        tree_value=3.0,
        correction_form="-",
        correction_value=0.0,
        observed=3.0,
        observed_err=0.0,
        source="klein_bottle.md",
        notes="three observable Klein bottle phase states (locked x unlocked)",
    ))

    # ------------------------------------------------------------------
    # COSMOLOGY
    # ------------------------------------------------------------------
    preds.append(Prediction(
        name="Omega_Lambda",
        sector="cosmology",
        tree_form="|F_6| / |F_7|",
        tree_value=13 / 19,
        correction_form="-",
        correction_value=0.0,
        observed=0.6847,
        observed_err=0.0073,
        source="farey_partition.md",
        notes="Farey inclusion at the interaction-scale boundary",
    ))

    preds.append(Prediction(
        name="Omega_matter",
        sector="cosmology",
        tree_form="phi(7) / |F_7|",
        tree_value=6 / 19,
        correction_form="-",
        correction_value=0.0,
        observed=0.3153,
        observed_err=0.0073,
        source="farey_partition.md",
        notes="Complement of Omega_Lambda, = phi(q_2 q_3 + 1) / |F_{q_2 q_3 + 1}|",
    ))

    preds.append(Prediction(
        name="Planck/Hubble ratio R",
        sector="cosmology",
        tree_form="6 * 13^54",
        tree_value=6 * 13**54,
        correction_form="-",
        correction_value=0.0,
        observed=8.49e60,
        observed_err=0.04e60,
        source="hierarchy.md",
        notes="R from q_2 q_3 * |F_6|^{q_2 q_3^d}",
    ))

    # ------------------------------------------------------------------
    # GAUGE COUPLINGS
    # ------------------------------------------------------------------
    preds.append(Prediction(
        name="sin^2(theta_W) [bare K=1 identity, not a prediction at M_Z]",
        sector="gauge",
        tree_form="q_2^3 / (q_2^3 + q_3^3) = 8/35",
        tree_value=Q2**3 / (Q2**3 + Q3**3),
        correction_form="-",
        correction_value=0.0,
        observed=SIN2_TW_MZ,
        observed_err=0.00004,
        source="duty_dimension_proof.md, numerology_inventory.md (Class 1)",
        notes=(
            "Declined in MANIFEST.yml per honest-null audit. The bare K=1 "
            "identity 8/35 is listed under MANIFEST.bare_k1_identities. The "
            "prior `+ 8/F_10^2` correction was removed (not derived). The "
            "d_eff = 80/27 proposal in sinw_effective_dimension.md is "
            "conditional on three unformalized steps and is not a prediction "
            "here. See sinW_running_check.py and sinw_fixed_point.md."
        ),
    ))

    preds.append(Prediction(
        name="alpha_s / alpha_2",
        sector="gauge",
        tree_form="q_3^3 / q_2^3 = 27/8",
        tree_value=Q3**3 / Q2**3,
        correction_form="1 / q_3^2 = 1/9",
        correction_value=1 / Q3**2,
        observed=ALPHA_S_MZ / (1/29.57),
        observed_err=0.05,
        source="item12_other_residuals.py",
        notes="correction = 1 / k_lepton, cross-sector inverse",
    ))

    preds.append(Prediction(
        name="strong CP angle theta",
        sector="gauge",
        tree_form="0",
        tree_value=0.0,
        correction_form="-",
        correction_value=0.0,
        observed=0.0,
        observed_err=1e-10,
        source="coupled_lagrangian.py",
        notes="from Pin^+(3) topology",
    ))

    # ------------------------------------------------------------------
    # HIGGS SECTOR
    # ------------------------------------------------------------------
    HIGGS_CORR = 1 / (Q2**2 * Q3 * 19)             # 1/228
    preds.append(Prediction(
        name="Higgs quartic lambda",
        sector="higgs",
        tree_form="duty(q_2) = 1/q_2^3 = 1/8",
        tree_value=1 / Q2**3,
        correction_form="1 / (q_2^2 q_3 |F_7|) = 1/228",
        correction_value=HIGGS_CORR,
        observed=M_H ** 2 / (2 * (V_GEV * 1e3) ** 2),
        observed_err=0.00035,
        source="item12_higgs_degeneracy.py, item12_higgs_residual.py",
        notes="1/(2q_2^2) form retired; 1/q_2^3 is forced by sin^2(theta_W)",
    ))

    lambda_pred = 1/Q2**3 + HIGGS_CORR
    mH_pred_gev = sqrt(2 * lambda_pred * V_GEV ** 2)
    preds.append(Prediction(
        name="Higgs mass m_H",
        sector="higgs",
        tree_form="sqrt(2 * lambda_tree) * v",
        tree_value=sqrt(2 * (1/Q2**3)) * V_GEV * 1e3,  # MeV
        correction_form="derived from lambda correction",
        correction_value=(mH_pred_gev * 1e3) - sqrt(2 * (1/Q2**3)) * V_GEV * 1e3,
        observed=M_H,
        observed_err=PDG_MASS["H"][1],
        source="item12_higgs_residual.py",
        notes="m_H = sqrt(2 lambda v^2), lambda = 1/q_2^3 + 1/228",
    ))

    # ------------------------------------------------------------------
    # LEPTON MASS RATIOS
    # ------------------------------------------------------------------
    # From generation exponent law, a_1(leptons)^2 = C = 5 + 1/phi^2 + correction
    # with C_predicted = (5 + 1/phi^2) * (1 + 1/F_10^2)
    C_LEPTONS = (MEDIANT + INV_PHI_SQ) * (1 + 1 / (fib(10) ** 2))
    a1_leptons = sqrt(C_LEPTONS)
    a2_leptons = (Q3 / Q2) * a1_leptons

    preds.append(Prediction(
        name="C = a_1(leptons)^2",
        sector="mass",
        tree_form="(q_2 + q_3) + 1/phi^2",
        tree_value=MEDIANT + INV_PHI_SQ,
        correction_form="* (1 + 1/F_10^2)",
        correction_value=(MEDIANT + INV_PHI_SQ) * (1 / (fib(10) ** 2)),
        observed=2.320292 ** 2,          # from observed m_tau/m_mu
        observed_err=0.00029,
        source="item12_characterize_a1.py, item12_C_from_K_star.py",
        notes="mediant scale + golden-ratio residue + Fibonacci-10 correction",
    ))

    preds.append(Prediction(
        name="m_tau / m_mu",
        sector="mass",
        tree_form="(3/2)^(d * a_1)",
        tree_value=(Q3 / Q2) ** (3 * a1_leptons),
        correction_form="-",
        correction_value=0.0,
        observed=M_TAU / M_MU,
        observed_err=0.0001,
        source="generation_exponent_law.py",
        notes="first-step base (3/2), exponent a_1 from C",
    ))

    preds.append(Prediction(
        name="m_mu / m_e",
        sector="mass",
        tree_form="(5/3)^(d * a_2), a_2 = (q_3/q_2) a_1",
        tree_value=((Q2 + Q3) / Q3) ** (3 * a2_leptons),
        correction_form="-",
        correction_value=0.0,
        observed=M_MU / M_E,
        observed_err=0.0001,
        source="generation_exponent_law.py",
        notes="second-step base (5/3), a_2/a_1 = 3/2 structural",
    ))

    # ------------------------------------------------------------------
    # UP-TYPE QUARK RATIOS
    # ------------------------------------------------------------------
    a1_up = sqrt(C_LEPTONS * (Q3 / Q2) ** 2)
    a2_up = (Q3 / Q2) * a1_up
    preds.append(Prediction(
        name="m_t / m_c",
        sector="mass",
        tree_form="(8/5)^(d * a_1(up))",
        tree_value=(Q2**3 / (Q2 + Q3)) ** (3 * a1_up),
        correction_form="-",
        correction_value=0.0,
        observed=M_T / M_C,
        observed_err=6,
        source="sector_base_pairs.py",
        notes="a_1(up) = (q_3/q_2) * a_1(leptons)",
    ))

    preds.append(Prediction(
        name="m_c / m_u",
        sector="mass",
        tree_form="(3/2)^(d * a_2(up))",
        tree_value=(Q3 / Q2) ** (3 * a2_up),
        correction_form="-",
        correction_value=0.0,
        observed=M_C / M_U,
        observed_err=150,
        source="sector_base_pairs.py",
        notes="same step base as lepton first step; different exponent",
    ))

    # ------------------------------------------------------------------
    # DOWN-TYPE QUARK RATIOS
    # ------------------------------------------------------------------
    # sign-flipped (orientation-preserving walk); use sqrt(C * q_2 q_3)
    # then apply the Z_2 correction
    a1_dn = sqrt(C_LEPTONS * (Q2 * Q3))
    a2_dn = (Q3 / Q2) * a1_dn
    preds.append(Prediction(
        name="m_b / m_s",
        sector="mass",
        tree_form="(5/4)^(d * a_1(dn))",
        tree_value=((Q2 + Q3) / Q2**2) ** (3 * a1_dn),
        correction_form="- (Z_2 frame flip)",
        correction_value=0.0,
        observed=M_B / M_S,
        observed_err=5,
        source="sector_base_pairs.py, item12_down_sign_flip.py",
        notes="down-type in orientation-preserving frame; sign flipped",
    ))

    preds.append(Prediction(
        name="m_s / m_d",
        sector="mass",
        tree_form="(9/8)^(d * a_2(dn))",
        tree_value=(Q3**2 / Q2**3) ** (3 * a2_dn),
        correction_form="-",
        correction_value=0.0,
        observed=M_S / M_D,
        observed_err=10,
        source="sector_base_pairs.py",
        notes="down-type second step",
    ))

    # ------------------------------------------------------------------
    # W/Z RATIO
    # ------------------------------------------------------------------
    preds.append(Prediction(
        name="M_W / M_Z = cos(theta_W)",
        sector="gauge",
        tree_form="sqrt(q_3^3 / (q_2^3 + q_3^3)) = sqrt(27/35)",
        tree_value=sqrt(Q3**3 / (Q2**3 + Q3**3)),
        correction_form="(inherits sin^2 correction)",
        correction_value=0.0,
        observed=PDG_MASS["W"][0] / M_Z,
        observed_err=0.0001,
        source="duty_cycle_dictionary.md",
        notes="from sin^2(theta_W) = 1 - cos^2",
    ))

    return preds


_PREDICTIONS_CACHE: Optional[list[Prediction]] = None


def all_predictions() -> list[Prediction]:
    """Return the full framework prediction list (cached after first call)."""
    global _PREDICTIONS_CACHE
    if _PREDICTIONS_CACHE is None:
        _PREDICTIONS_CACHE = _all()
    return _PREDICTIONS_CACHE


def filter_by(predicate: Callable[[Prediction], bool]) -> list[Prediction]:
    """Filter predictions by an arbitrary predicate."""
    return [p for p in all_predictions() if predicate(p)]


def by_sector(sector: str) -> list[Prediction]:
    return filter_by(lambda p: p.sector == sector)


# ============================================================================
# Pretty-printing
# ============================================================================

def table(show_sources: bool = False) -> None:
    """Print the full prediction table."""
    preds = all_predictions()
    print("=" * 100)
    print(f"  {'FRAMEWORK PREDICTIONS':<96}")
    print("=" * 100)
    print()
    print(f"  {'name':<28} {'sector':<10} {'predicted':>16} {'observed':>16} "
          f"{'rel %':>10} {'sigma':>8}")
    print("  " + "-" * 96)
    for p in preds:
        sigma = p.sigma_err()
        sigma_str = f"{sigma:6.2f}" if sigma is not None else "  --  "
        rel_str = f"{p.rel_err_pct():8.4f}%"
        # Short-form value printing
        if p.value > 1e6 or (p.value < 1e-3 and p.value > 0):
            val_str = f"{p.value:16.4e}"
        else:
            val_str = f"{p.value:16.6f}"
        if p.observed > 1e6 or (p.observed < 1e-3 and p.observed > 0):
            obs_str = f"{p.observed:16.4e}"
        else:
            obs_str = f"{p.observed:16.6f}"
        marker = " *" if p.within_pdg() else "  "
        print(f"  {p.name[:28]:<28} {p.sector:<10} {val_str} {obs_str} "
              f"{rel_str:>10} {sigma_str:>8}{marker}")
    print()
    print("  * = within PDG 1-sigma uncertainty")
    print()
    if show_sources:
        print("  Source scripts:")
        for p in preds:
            print(f"    {p.name:<30} -> {p.source}")
        print()


def summary() -> None:
    """Short summary: how many predictions are within PDG, by sector."""
    preds = all_predictions()
    by_s: dict[str, tuple[int, int]] = {}
    for p in preds:
        count, within = by_s.get(p.sector, (0, 0))
        by_s[p.sector] = (count + 1, within + (1 if p.within_pdg() else 0))
    print("=" * 60)
    print("  PREDICTION SUMMARY BY SECTOR")
    print("=" * 60)
    print()
    print(f"  {'sector':<16} {'count':>8} {'within PDG':>14}")
    print("  " + "-" * 44)
    for sector, (count, within) in sorted(by_s.items()):
        print(f"  {sector:<16} {count:>8} {within:>10} / {count}")
    total = sum(c for c, _ in by_s.values())
    total_within = sum(w for _, w in by_s.values())
    print("  " + "-" * 44)
    print(f"  {'TOTAL':<16} {total:>8} {total_within:>10} / {total}")
    print()


if __name__ == "__main__":
    table()
    summary()
