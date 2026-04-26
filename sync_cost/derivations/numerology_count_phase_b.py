"""
Region C Phase B: numerology count.

Tests whether the framework's 1-3% near-match cloud is statistically
expected by pigeonhole or anomalously dense relative to its null
expectation.

Method (per `numerology_count_phase_a.md`):

1. Enumerate framework-integer expressions of bounded form.
2. For each physical observable, find the closest framework expression.
3. Bin by relative error at 0.1%, 1%, 3% thresholds.
4. Permutation null: 10^4 random shuffles of observable values within
   their range; recompute match counts; build null distribution.
5. p-value the actual count against the null distribution.

Verdict shapes:
- p < 0.001:  cloud is signal (over-represented near-matches)
- 0.05 < p < 0.95: cloud is pigeonhole (matches expected)
- p > 0.999: cloud is anti-signal (avoids matches; informative)
"""

import math
from collections import defaultdict
from itertools import product

import numpy as np


# ============================================================
# Framework integers (canonical set per Instance 7 + Farey counts)
# ============================================================

FRAMEWORK_INTS = [2, 3, 5, 6, 7, 8, 9, 11, 13, 19]
# 2 = q_2, 3 = q_3, 5 = MEDIANT, 6 = INTERACT, 7 = |F_4|,
# 8 = K_QUARK, 9 = K_LEPTON, 11 = |F_5|, 13 = |F_6|, 19 = |F_7|


# ============================================================
# Expression enumeration
# ============================================================

def enumerate_expressions(value_min=1e-3, value_max=1e3):
    """
    Enumerate all framework-integer expressions of bounded forms:
    - n/m       (single ratios)
    - n^a/m^b   (powers, a,b in {1,2,3})
    - n*m / p   (products over single)
    - (n+m)/p   (sums over single)
    - n/(m+p)   (single over sums)

    Filter to value in [value_min, value_max]; deduplicate by value.
    """
    expressions = {}  # value -> list of (formula, value)
    ints = FRAMEWORK_INTS

    # Single ratios n/m
    for n in ints:
        for m in ints:
            v = n / m
            if value_min <= v <= value_max:
                key = round(v, 12)
                expressions.setdefault(key, []).append((f"{n}/{m}", v))

    # Powers n^a / m^b
    for n in ints:
        for m in ints:
            for a in (1, 2, 3):
                for b in (1, 2, 3):
                    v = (n ** a) / (m ** b)
                    if value_min <= v <= value_max:
                        key = round(v, 12)
                        expressions.setdefault(key, []).append(
                            (f"{n}^{a}/{m}^{b}", v))

    # Products over single: n*m/p
    for n in ints:
        for m in ints:
            for p in ints:
                v = (n * m) / p
                if value_min <= v <= value_max:
                    key = round(v, 12)
                    expressions.setdefault(key, []).append(
                        (f"{n}*{m}/{p}", v))

    # Sums: (n+m)/p
    for n in ints:
        for m in ints:
            for p in ints:
                v = (n + m) / p
                if value_min <= v <= value_max:
                    key = round(v, 12)
                    expressions.setdefault(key, []).append(
                        (f"({n}+{m})/{p}", v))

    # Single over sums: n/(m+p)
    for n in ints:
        for m in ints:
            for p in ints:
                v = n / (m + p)
                if value_min <= v <= value_max:
                    key = round(v, 12)
                    expressions.setdefault(key, []).append(
                        (f"{n}/({m}+{p})", v))

    # Compose: (n*m)/(p*q) - cross products
    for n in ints:
        for m in ints:
            for p in ints:
                for q in ints:
                    v = (n * m) / (p * q)
                    if value_min <= v <= value_max:
                        key = round(v, 12)
                        expressions.setdefault(key, []).append(
                            (f"{n}*{m}/{p}*{q}", v))

    # Flatten to list of unique values
    unique_values = sorted(expressions.keys())
    return unique_values, expressions


# ============================================================
# Physical observables
# ============================================================

OBSERVABLES = {
    # Cosmological dimensionless ratios
    "Omega_Lambda":        0.6847,
    "Omega_DM":            0.265,
    "Omega_b":             0.0493,
    "Omega_DM/Omega_b":    5.41,
    "Omega_Lambda/Omega_m":  2.176,
    "Omega_Lambda/Omega_DM": 2.583,
    "n_s":                 0.9649,
    "1 - n_s":             0.0351,

    # Higgs-sector
    "m_H/v":               0.5087,
    "lambda_Higgs":        0.129,

    # EW couplings
    "sin2_theta_W":        0.23121,
    "cos2_theta_W":        0.76879,
    "alpha_s/alpha_2":     3.488,
    "alpha_s/alpha_em":    1.2 / 0.0073,  # ~16.4
    "1/alpha_em":          137.036,
    "alpha_em":            0.00730,
    "alpha_s":             0.118,
    "alpha_2":             0.0338,

    # Fermion mass ratios (PDG)
    "m_t/m_b":             41.65,        # 172.76 / 4.18
    "m_b/m_c":             3.30,         # 4.18 / 1.27
    "m_c/m_s":             13.54,        # 1.27 / 0.0938
    "m_s/m_d":             20.0,         # 0.0938 / 0.00467
    "m_d/m_u":             2.16,         # 0.00467 / 0.00216
    "m_b/m_tau":           2.36,         # 4.18 / 1.777
    "m_tau/m_mu":          16.82,        # 1.777 / 0.10566
    "m_mu/m_e":            206.77,       # 0.10566 / 0.000511
    "m_tau/m_e":           3477.5,       # 1.777 / 0.000511

    # CKM (Wolfenstein-ish)
    "|V_us|":              0.2243,
    "|V_cb|":              0.0405,
    "|V_ub|":              0.00382,
    "|V_us|/|V_cb|":       5.54,

    # Other dimensionless
    "B_K":                 0.717,        # Kaon bag parameter
    "f_pi/f_K":            0.836,        # decay constant ratio
}


# ============================================================
# Match analysis
# ============================================================

def find_closest(value, expression_values):
    """Find closest framework expression value; return (closest, rel_error)."""
    arr = np.asarray(expression_values)
    idx = np.argmin(np.abs(arr - value))
    closest = arr[idx]
    rel_err = abs(closest - value) / abs(value)
    return closest, rel_err


def count_matches(observable_values, expression_values, thresholds):
    """Count observables matching within each relative-error threshold."""
    counts = {t: 0 for t in thresholds}
    for v in observable_values:
        _, rel_err = find_closest(v, expression_values)
        for t in thresholds:
            if rel_err <= t:
                counts[t] += 1
    return counts


# ============================================================
# Permutation null: log-uniform within observable range
# ============================================================

def null_distribution(n_observables, expression_values,
                       value_range, thresholds, n_trials=10000, rng=None):
    """
    Generate null distribution of match counts under log-uniform
    sampling within the observable's value range.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    log_lo, log_hi = math.log10(value_range[0]), math.log10(value_range[1])
    arr = np.asarray(expression_values)

    counts_per_trial = {t: [] for t in thresholds}
    for _ in range(n_trials):
        # Sample n_observables values uniformly on log scale
        fake_log = rng.uniform(log_lo, log_hi, size=n_observables)
        fake_vals = 10 ** fake_log

        # Vectorized closest-match
        # For each fake_val, find min |arr - fake_val| / |fake_val|
        # We'll loop since n_observables is small
        for t in thresholds:
            counts_per_trial[t].append(0)

        for v in fake_vals:
            rel_errs = np.abs(arr - v) / abs(v)
            min_err = rel_errs.min()
            for t in thresholds:
                if min_err <= t:
                    counts_per_trial[t][-1] += 1

    return counts_per_trial


# ============================================================
# Run
# ============================================================

def main():
    print("=" * 64)
    print("Region C Phase B: numerology count")
    print("=" * 64)

    # Step 1 — Enumerate
    expr_values, expr_index = enumerate_expressions(
        value_min=1e-3, value_max=1e3)
    print(f"\nFramework integers: {FRAMEWORK_INTS}")
    print(f"Total unique framework expression values: {len(expr_values)}")
    print(f"Range: [{min(expr_values):.4g}, {max(expr_values):.4g}]")

    # Step 2 — Observables
    obs_names = list(OBSERVABLES.keys())
    obs_vals = list(OBSERVABLES.values())
    print(f"\nPhysical observables: {len(obs_vals)}")
    print(f"Observable range: [{min(obs_vals):.4g}, {max(obs_vals):.4g}]")

    # Step 3 — Per-observable closest match
    print(f"\nPer-observable closest-match table:")
    print(f"{'Observable':<28} {'Value':>12} {'Closest':>14} "
          f"{'Rel.Err':>10}")
    print("-" * 70)
    matches_at_threshold = defaultdict(list)
    for name, v in OBSERVABLES.items():
        closest, rel_err = find_closest(v, expr_values)
        # Get a reasonable formula
        formulas = expr_index[round(closest, 12)]
        # Pick shortest formula
        formula = min(formulas, key=lambda x: len(x[0]))[0]
        marker = ""
        if rel_err <= 0.001:
            marker = "  *** (0.1%)"
            matches_at_threshold[0.001].append((name, v, closest, rel_err))
        elif rel_err <= 0.01:
            marker = "  ** (1%)"
            matches_at_threshold[0.01].append((name, v, closest, rel_err))
        elif rel_err <= 0.03:
            marker = "  * (3%)"
            matches_at_threshold[0.03].append((name, v, closest, rel_err))
        print(f"{name:<28} {v:>12.5g} {formula:>14} "
              f"{rel_err*100:>9.3f}%{marker}")

    # Step 4 — Counts at each threshold
    thresholds = [0.001, 0.01, 0.03]
    actual_counts = count_matches(obs_vals, expr_values, thresholds)

    print(f"\n{'Threshold':<14} {'Actual matches':<18}")
    print("-" * 32)
    for t in thresholds:
        print(f"{t*100:>8.1f}%   {actual_counts[t]:>5d} of {len(obs_vals)}")

    # Step 5 — Null distribution
    print(f"\nGenerating permutation null (10000 trials, log-uniform "
          f"on observable range)...")
    obs_range = (min(obs_vals), max(obs_vals))
    null_counts = null_distribution(
        n_observables=len(obs_vals),
        expression_values=expr_values,
        value_range=obs_range,
        thresholds=thresholds,
        n_trials=10000)

    # Step 6 — p-values
    print(f"\n{'Threshold':<14} {'Actual':<10} {'Null mean':<12} "
          f"{'Null std':<10} {'p (actual >= null)':<20}")
    print("-" * 66)
    for t in thresholds:
        actual = actual_counts[t]
        null = np.array(null_counts[t])
        mean = null.mean()
        std = null.std()
        # p = P(null >= actual) under null hypothesis
        p_val = (null >= actual).mean()
        print(f"{t*100:>8.1f}%   {actual:>5d}     {mean:>8.2f}    "
              f"{std:>6.2f}     p = {p_val:.4f}")

    # Step 7 — Verdict
    print(f"\n{'='*64}")
    print("VERDICT")
    print(f"{'='*64}")
    for t in thresholds:
        actual = actual_counts[t]
        null = np.array(null_counts[t])
        p_val = (null >= actual).mean()
        z = (actual - null.mean()) / max(null.std(), 1e-10)
        print(f"\nThreshold {t*100:.1f}%:")
        print(f"  Actual: {actual} matches; null mean: {null.mean():.2f}, "
              f"std: {null.std():.2f}")
        print(f"  z-score: {z:+.2f}  p(null >= actual) = {p_val:.4f}")
        if p_val < 0.05:
            print(f"  → SIGNAL (cloud over-represented; reject null at "
                  f"5%)")
        elif p_val > 0.95:
            print(f"  → ANTI-SIGNAL (cloud under-represented; framework "
                  f"avoids matches)")
        else:
            print(f"  → PIGEONHOLE (matches consistent with null)")

    # Step 8 — Per-threshold match list (for reference)
    print(f"\n{'='*64}")
    print("Matches at each threshold (for inspection)")
    print(f"{'='*64}")
    for t in [0.001, 0.01, 0.03]:
        items = matches_at_threshold[t]
        if items:
            print(f"\nAt {t*100:.1f}% threshold ({len(items)} matches):")
            for name, v, closest, rel_err in items:
                print(f"  {name:<28} = {v:.5g}  ≈ {closest:.5g}  "
                      f"({rel_err*100:.3f}%)")


if __name__ == "__main__":
    main()
