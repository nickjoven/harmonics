"""
tau_mass_prediction.py

If the framework's closed form K_STAR^14 = q_2^(-q_3) = 1/8 is
accepted as exact, it predicts the tau lepton mass to ~22 ppb
precision from the muon mass alone -- a factor of ~3100 tighter
than current PDG experimental precision.

This is the framework's cleanest falsifiable prediction.  Unlike
'derivation' claims that fit existing data, this is a forward
prediction: the framework's closed form + the precisely-known muon
mass = a specific number for m_tau, good to 22 ppb.

DERIVATION:

    Step 1: Assume K_STAR^14 = q_2^(-q_3) = 1/8 (the structural
            closed form from the chain).
    Step 2: Then K_STAR = 2^(-3/14).
    Step 3: Then a_1(lep) = sqrt(N_lep)/K_STAR = 2 * 2^(3/14) = 2^(17/14).
    Step 4: The generation law gives
              m_tau / m_mu = b_1^(d * a_1) = (3/2)^(3 * 2^(17/14))
    Step 5: This is a pure irrational number determined by framework
            primitives {q_2, q_3, d, b_1}.  No experimental input
            on the tau side.
    Step 6: Multiply by precisely-known m_mu to get m_tau.

RESULT:

    (3/2)^(3 * 2^(17/14)) = 16.816354951480701 (exact form in primitives)

    Framework m_tau = 16.81635495 * 105.6583755 MeV
                    = 1776.7887460 MeV

    Uncertainty = m_tau * sigma(m_mu) / m_mu
                = 1776.79 * 2.2e-8
                = 3.87e-5 MeV
                = 22 parts per billion relative

    Framework m_tau = 1776.78875 +/- 0.00004 MeV

COMPARISON:

    PDG 2024 avg:  1776.86  +/- 0.12    MeV  (68 ppm, 0.594 sigma away)
    KEDR 2007:     1776.80  +/- 0.23    MeV  (0.049 sigma -- essentially exact)
    BaBar 2009:    1776.68  +/- 0.43    MeV  (0.255 sigma below)
    Belle 2007:    1776.61  +/- 0.37    MeV  (0.479 sigma below)
    BESIII 2014:   1776.91  +/- 0.16    MeV  (0.776 sigma above -- worst fit)

    Framework:     1776.78875 +/- 0.00004 MeV

    The framework prediction splits the experimental spread almost
    exactly at KEDR's central value.  BESIII (the highest measurement)
    is furthest from the prediction; BaBar and Belle (the lowest)
    overshoot in the opposite direction.  The PDG average sits 0.6
    sigma above the framework value because BESIII pulls it up.

FALSIFIABILITY:

    A future tau mass measurement at sigma < 0.03 MeV could
    definitively confirm or refute this prediction:

      - If central value converges to ~1776.79: framework confirmed
      - If central value converges to ~1776.86: framework refuted
      - Current PDG average can't distinguish these

    Belle II (currently running, projected ~50/ab) and BESIII
    upgrades are expected to achieve sub-0.05 MeV precision in the
    coming years via tau threshold scans.  This IS the decisive
    measurement.

HONEST CAVEATS:

    (i) The prediction assumes K_STAR^14 = 1/8 is EXACT.  This is
        a structural claim from the chain in deriving_14.py,
        farey_depth_proof.py, and octave_doubling.py.  Each step
        of the chain has framework justification, but three steps
        are structural identifications rather than theorems:
          - framework depth = N_lep = 4
          - Klein parity extends to Farey rationals
          - EDO basis has q_2 octave doubling

    (ii) If any of those identifications is wrong, the prediction
         is wrong.  But it is STILL a concrete number, not a
         parameter fit, and it is falsifiable.

    (iii) The prediction is derived from m_mu + the framework's
          closed form + the generation law.  The generation law
          itself is an observed pattern across the three charged
          fermion sectors; if the generation law breaks down at
          the precision we're predicting, the prediction breaks
          down first.

    (iv) The current 0.594 sigma agreement with PDG is CONSISTENT
         with the prediction but does not CONFIRM it.  Confirmation
         requires tighter m_tau data.

SIGNIFICANCE:

    This is the framework's cleanest falsifiable prediction because:

      (a) It's a specific number, not a range.
      (b) It uses only framework primitives + one precisely known
          reference mass (m_mu at 9 digits).
      (c) It's ~3100x tighter than current experimental precision,
          so there's massive room for experiment to resolve it.
      (d) The resolution timeline is concrete (Belle II / BESIII
          upgrades).
      (e) It's falsifiable by a single tau mass measurement with
          better than current precision.

    If the framework is right, future PDG tau mass averages should
    drift DOWNWARD from 1776.86 toward 1776.789 as measurements
    improve.  If the framework is wrong, they should stabilize at
    or above 1776.86.

    This is the session's cleanest closure-candidate output: a
    derived prediction for an independent experimental observable,
    with a clear refutation criterion.
"""

from __future__ import annotations

import math

from framework_constants import Q2, Q3


def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


# PDG 2024 values
M_MU = 105.6583755
S_MU = 0.0000023
M_TAU_PDG = 1776.86
S_TAU_PDG = 0.12

B1 = 3.0 / 2.0
D_DIM = 3
N_LEP = Q2 ** 2


# ============================================================================
# (A) The derivation from K_STAR = 2^(-3/14) exact
# ============================================================================

def section_derivation() -> None:
    header("(A) Framework derivation of m_tau from K_STAR closed form")
    print("  Starting assumption:")
    print()
    print("      K_STAR^14 = q_2^(-q_3) = 1/8  (structural closed form)")
    print()
    print("  Step-by-step derivation of m_tau:")
    print()
    print("  1) K_STAR = (1/8)^(1/14) = 2^(-3/14)")
    K_closed = 2 ** (-3/14)
    print(f"     K_STAR = {K_closed:.15f}")
    print()
    print("  2) a_1(lep) = sqrt(N_lep) / K_STAR = 2 / 2^(-3/14) = 2^(17/14)")
    a1_closed = 2 ** (17/14)
    print(f"     a_1(lep) = {a1_closed:.15f}")
    print()
    print("  3) Generation law: m_tau/m_mu = b_1^(d*a_1) = (3/2)^(3*2^(17/14))")
    d_a1 = D_DIM * a1_closed
    ratio_closed = B1 ** d_a1
    print(f"     d * a_1 = {d_a1:.15f}")
    print(f"     (3/2)^(d*a_1) = {ratio_closed:.15f}")
    print()
    print("  4) m_tau = (predicted ratio) * m_mu")
    m_tau_pred = ratio_closed * M_MU
    s_tau_pred = m_tau_pred * S_MU / M_MU  # sigma dominated by m_mu
    print(f"     m_tau (framework) = {m_tau_pred:.10f} MeV")
    print(f"     sigma             = {s_tau_pred:.4e} MeV")
    print(f"     relative sigma    = {s_tau_pred/m_tau_pred*1e9:.1f} parts per billion")
    print()
    print("  The prediction is a pure irrational of framework primitives")
    print("  {q_2, q_3, d, b_1} times the precisely-known m_mu.  No tau")
    print("  experimental input.")
    print()


# ============================================================================
# (B) Comparison to experimental m_tau values
# ============================================================================

def section_comparison() -> None:
    header("(B) Comparison to experimental m_tau measurements")
    a1_closed = 2 ** (17/14)
    ratio_closed = B1 ** (D_DIM * a1_closed)
    m_tau_pred = ratio_closed * M_MU
    s_tau_pred = m_tau_pred * S_MU / M_MU

    print(f"  Framework prediction: m_tau = {m_tau_pred:.5f} +/- {s_tau_pred:.1e} MeV")
    print()
    experiments = [
        ("KEDR 2007",     1776.80, 0.23),
        ("BaBar 2009",    1776.68, math.hypot(0.12, 0.41)),
        ("Belle 2007",    1776.61, math.hypot(0.13, 0.35)),
        ("BESIII 2014",   1776.91, math.hypot(0.12, 0.10)),
        ("PDG 2024 avg",  1776.86, 0.12),
    ]
    print(f"  {'experiment':<14}  {'m_tau':<11}  {'diff vs pred':<14}  {'n_sigma':<10}")
    print("  " + "-" * 55)
    for name, mt, st in experiments:
        diff = mt - m_tau_pred
        n = abs(diff) / st
        mark = "  <-- closest" if n < 0.1 else ""
        print(f"  {name:<14}  {mt:<11.4f}  {diff:+.4f}        {n:.3f}{mark}")
    print()
    print(f"  KEDR 2007 is essentially ON the framework prediction (0.049 sigma).")
    print(f"  BaBar and Belle undershoot (below 1776.79).")
    print(f"  BESIII overshoots (above 1776.79).")
    print(f"  PDG average sits 0.6 sigma above the prediction because it's")
    print(f"  pulled toward BESIII's tightly-reported value.")
    print()


# ============================================================================
# (C) Precision comparison
# ============================================================================

def section_precision() -> None:
    header("(C) Precision comparison: framework prediction vs PDG")
    a1_closed = 2 ** (17/14)
    ratio_closed = B1 ** (D_DIM * a1_closed)
    m_tau_pred = ratio_closed * M_MU
    s_tau_pred = m_tau_pred * S_MU / M_MU

    print(f"  Framework prediction:  sigma = {s_tau_pred:.2e} MeV = {s_tau_pred/m_tau_pred*1e9:.1f} ppb")
    print(f"  PDG 2024 experimental: sigma = {S_TAU_PDG} MeV = {S_TAU_PDG/M_TAU_PDG*1e6:.1f} ppm")
    print()
    ratio = S_TAU_PDG / s_tau_pred
    print(f"  Framework is {ratio:.0f}x tighter than PDG experimental.")
    print()
    print("  This is because m_mu is known to 22 ppb (9 digits), while")
    print("  m_tau is only known to 68 ppm (5 digits).  The framework's")
    print("  closed form inherits the tighter m_mu precision and projects")
    print("  it onto m_tau via the generation law.")
    print()


# ============================================================================
# (D) Falsifiability criterion
# ============================================================================

def section_falsifiability() -> None:
    header("(D) Falsifiability: what measurement would refute the prediction?")
    a1_closed = 2 ** (17/14)
    ratio_closed = B1 ** (D_DIM * a1_closed)
    m_tau_pred = ratio_closed * M_MU

    print(f"  Framework: m_tau = {m_tau_pred:.5f} MeV")
    print(f"  PDG avg:   m_tau = {M_TAU_PDG} MeV")
    print()
    gap = M_TAU_PDG - m_tau_pred
    print(f"  Current gap: {gap:+.4f} MeV")
    print()
    print("  A future tau mass measurement would:")
    print()
    print("  - CONFIRM the framework if central value converges to 1776.789")
    print("    at precision better than 0.03 MeV.")
    print()
    print("  - REFUTE the framework if central value converges to 1776.86")
    print("    or higher at precision better than 0.03 MeV.")
    print()
    print("  - Remain consistent with both if precision stays at current")
    print("    ~0.1 MeV level.")
    print()
    print("  The current situation is 0.594 sigma consistent -- the")
    print("  framework can't be distinguished from the PDG value at")
    print("  current precision.  Resolution requires tighter data.")
    print()
    print("  Expected timeline: Belle II (projected ~50/ab over program")
    print("  lifetime) and BESIII upgrades should achieve sigma ~ 0.05")
    print("  MeV within the coming years via improved tau threshold scans.")
    print()


# ============================================================================
# (E) Significance
# ============================================================================

def section_significance() -> None:
    header("(E) Significance")
    print("""\
  This is the framework's cleanest falsifiable prediction.  Unlike
  'derivation' claims that fit existing data, this is a FORWARD
  prediction: assume the closed form, compute, check against
  independent measurement.

  What makes it clean:

    (a) Specific number: m_tau = 1776.7887 +/- 0.00004 MeV,
        not a range or a probability distribution.

    (b) Uses only framework primitives + one reference mass.  The
        precision is inherited from m_mu (9 digits), not from a
        fit.

    (c) ~3100x tighter than current experiment.  If future data
        can distinguish 1776.79 from 1776.86, the prediction is
        decisively tested.

    (d) Concrete refutation criterion: a sigma < 0.03 MeV
        measurement would definitively settle it.

    (e) Expected resolution timeline is plausible (Belle II /
        BESIII upgrades).

  What makes it honest:

    The prediction assumes K_STAR^14 = 1/8 is EXACT, which is a
    structural claim from the chain:
      deriving_14.py + farey_depth_proof.py + octave_doubling.py

    If any step of that chain is wrong (specifically: 'framework
    depth = 4', 'Klein parity extends to Farey rationals', or
    'EDO basis = q_2 * |F_d|'), the prediction is wrong in the
    specific direction the chain is wrong.

    But it is STILL a concrete number, not a parameter fit, and
    the test via future tau mass measurement is independent of
    the chain's internal validity.

  INTERPRETATION:

    If future experiments converge on 1776.789 MeV, the framework's
    K_STAR = 2^(-3/14) closed form is confirmed, and by extension
    the six-step derivation chain is substantially validated.

    If future experiments converge on 1776.86 MeV or higher, the
    closed form is wrong, and K_STAR has some other origin that
    the framework hasn't identified.

    Either outcome moves the investigation forward.  The ~0.59
    sigma current agreement is the MOST ambiguous zone; any
    precision improvement in either direction is informative.

  This is the cleanest output of the K_STAR investigation, and
  the right place to pause the session: a specific, falsifiable,
  experimentally-testable prediction, with a defensible structural
  derivation.
""")


def main() -> None:
    print("=" * 78)
    print("  TAU MASS PREDICTION from K_STAR ~ 2^(-3/14) closed form")
    print("=" * 78)
    section_derivation()
    section_comparison()
    section_precision()
    section_falsifiability()
    section_significance()


if __name__ == "__main__":
    main()
