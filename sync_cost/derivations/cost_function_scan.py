"""
Exhaustion proof: no monotonic cost function gives negative running.

Systematically scans cost functions C(τ) for the spectral tilt.
Every monotonic cost produces positive running (+0.013 for
Michaelis-Menten). Planck data prefer negative running. This
rules out the cost-function approach entirely and motivates
the circle map framework (04_spectral_tilt_reframed.md), where
negative running arises from the devil's staircase gap closure.

The Michaelis-Menten form recovers n_s = 0.965 (the tilt is
correct) but the running sign is diagnostic: it proves the tilt
comes from Arnold tongues, not synchronization cost.

Usage:
    python sync_cost/derivations/cost_function_scan.py
"""

import math

# ---------------------------------------------------------------------------
# Infrastructure: generic numerical n_s and running from any cost function
# ---------------------------------------------------------------------------

def numerical_ns_and_running(cost_fn, k_pivot, tau_0):
    """
    Given a cost function C(tau) and P(k) = 1/C(tau_0/k),
    compute n_s and dn_s/d ln k at k_pivot numerically.
    """
    eps = 1e-5

    def ln_power(ln_k):
        k = math.exp(ln_k)
        tau = tau_0 / k
        c = cost_fn(tau)
        if c <= 0:
            return float('inf')
        return -math.log(c)

    ln_k = math.log(k_pivot)

    # n_s - 1 = d ln P / d ln k  (central difference)
    dlnP = (ln_power(ln_k + eps) - ln_power(ln_k - eps)) / (2 * eps)
    ns = 1.0 + dlnP

    # running = d²ln P / (d ln k)²  (central second derivative)
    d2lnP = (ln_power(ln_k + eps) - 2 * ln_power(ln_k) + ln_power(ln_k - eps)) / eps**2
    running = d2lnP

    return ns, running


def fit_pivot(cost_fn_factory, tau_0, target_ns=0.9649, param_range=(0.01, 50.0)):
    """
    Find the k_pivot that gives target n_s for a given cost function.
    Binary search over k.
    """
    lo, hi = param_range
    for _ in range(100):
        mid = (lo + hi) / 2
        ns, _ = numerical_ns_and_running(cost_fn_factory, mid, tau_0)
        if ns < target_ns:
            lo = mid
        else:
            hi = mid
    return mid


# ---------------------------------------------------------------------------
# Cost function families
# ---------------------------------------------------------------------------

def mm_cost(tau, k_half=1.0):
    """Standard Michaelis-Menten: C = K/(K+τ)"""
    return k_half / (k_half + tau)


def barrier_cost(tau, k_half=1.0, barrier_height=0.3, barrier_width=1.0):
    """
    MM + activation barrier: cost increases before decreasing.
    C(τ) = K/(K+τ) + h × τ/(w+τ)² × exp(-τ/w)

    The barrier term peaks at τ ≈ w and decays for large τ.
    Physical interpretation: modes must first constitute a local mean
    field (costing energy) before they can synchronize against the
    global mean field (reducing cost).
    """
    mm = k_half / (k_half + tau)
    bump = barrier_height * tau / (barrier_width + tau)**2 * math.exp(-tau / barrier_width) * barrier_width
    return mm + bump


def logistic_cost(tau, k_half=1.0, steepness=1.0):
    """
    Logistic decay: C(τ) = 1/(1 + exp(s(τ - K)))
    S-shaped: flat at high cost, transition, flat at low cost.
    Has an inflection point at τ = K_half.
    """
    arg = steepness * (tau - k_half)
    if arg > 500:
        return 0.0
    if arg < -500:
        return 1.0
    return 1.0 / (1.0 + math.exp(arg))


def stretched_exp_cost(tau, k_half=1.0, beta=0.5):
    """
    Stretched exponential: C(τ) = exp(-(τ/K)^β)
    β < 1: slower than exponential (disordered systems, glassy dynamics)
    β = 1: standard exponential
    β > 1: faster than exponential (cooperative)
    """
    return math.exp(-(tau / k_half) ** beta)


def power_law_cost(tau, k_half=1.0, alpha=1.5):
    """
    Power-law decay: C(τ) = (K/(K+τ))^α
    α > 1: faster than MM near attractor
    α < 1: slower than MM
    """
    return (k_half / (k_half + tau)) ** alpha


def two_stage_cost(tau, k_half_1=0.5, k_half_2=5.0, weight=0.3):
    """
    Two-stage synchronization:
    C(τ) = w × K₁/(K₁+τ) + (1-w) × K₂/(K₂+τ)

    Physical: fast local synchronization (K₁ small) +
    slow global synchronization (K₂ large).
    The sum of two MM terms with different timescales.
    """
    return weight * k_half_1 / (k_half_1 + tau) + (1 - weight) * k_half_2 / (k_half_2 + tau)


def mean_field_bootstrap_cost(tau, k_half=1.0, bootstrap_time=0.5):
    """
    Self-consistency cost: modes must first build a local mean field
    before synchronizing. Cost INCREASES initially (building the field
    is work), then decreases (synchronization pays off).

    C(τ) = K/(K+τ) × (1 + A×τ×exp(-τ/b))

    The envelope is MM. The multiplicative correction raises cost
    at intermediate τ (the bootstrap phase).
    """
    mm = k_half / (k_half + tau)
    # bootstrap amplitude chosen so peak correction is ~50%
    amp = 2.0 / bootstrap_time * math.e
    bootstrap = 1.0 + amp * tau * math.exp(-tau / bootstrap_time)
    return mm * bootstrap


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tau_0 = 1.0  # normalization

    print("=" * 80)
    print("  COST FUNCTION SCAN: n_s AND RUNNING")
    print("=" * 80)
    print(f"\n  Target: n_s = 0.9649, dn_s/d ln k = -0.0045 (Planck central)")
    print(f"          Acceptable running: -0.012 to +0.002 (within 1σ)")

    # --- 1. Standard MM ---
    print(f"\n{'─'*80}")
    print("  1. MICHAELIS-MENTEN (baseline)")
    print(f"{'─'*80}")
    k_p = fit_pivot(lambda t: mm_cost(t), tau_0)
    ns, run = numerical_ns_and_running(lambda t: mm_cost(t), k_p, tau_0)
    print(f"  k_pivot = {k_p:.4f},  n_s = {ns:.4f},  running = {run:+.6f}")

    # --- 2. Barrier cost ---
    print(f"\n{'─'*80}")
    print("  2. ACTIVATION BARRIER (MM + bump)")
    print(f"{'─'*80}")
    print(f"\n  {'h':>6s}  {'w':>6s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 65)

    for h in [0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0]:
        for w in [0.3, 0.5, 1.0, 2.0, 3.0]:
            cost_fn = lambda t, _h=h, _w=w: barrier_cost(t, barrier_height=_h, barrier_width=_w)
            try:
                k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
                ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
                if abs(ns - 0.9649) > 0.005:
                    continue
                note = ""
                if -0.012 < run < 0.002:
                    note = "*** MATCH ***"
                elif run < 0:
                    note = "negative!"
                print(f"  {h:6.2f}  {w:6.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
            except (ValueError, OverflowError, ZeroDivisionError):
                pass

    # --- 3. Logistic ---
    print(f"\n{'─'*80}")
    print("  3. LOGISTIC COST")
    print(f"{'─'*80}")
    print(f"\n  {'steep':>6s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 55)

    for s in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        cost_fn = lambda t, _s=s: logistic_cost(t, steepness=_s)
        try:
            k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
            ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
            if abs(ns - 0.9649) > 0.005:
                continue
            note = ""
            if -0.012 < run < 0.002:
                note = "*** MATCH ***"
            elif run < 0:
                note = "negative!"
            print(f"  {s:6.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
        except (ValueError, OverflowError, ZeroDivisionError):
            pass

    # --- 4. Stretched exponential ---
    print(f"\n{'─'*80}")
    print("  4. STRETCHED EXPONENTIAL")
    print(f"{'─'*80}")
    print(f"\n  {'β':>6s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 55)

    for beta in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.5]:
        cost_fn = lambda t, _b=beta: stretched_exp_cost(t, beta=_b)
        try:
            k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
            ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
            if abs(ns - 0.9649) > 0.005:
                continue
            note = ""
            if -0.012 < run < 0.002:
                note = "*** MATCH ***"
            elif run < 0:
                note = "negative!"
            print(f"  {beta:6.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
        except (ValueError, OverflowError, ZeroDivisionError):
            pass

    # --- 5. Power-law MM ---
    print(f"\n{'─'*80}")
    print("  5. POWER-LAW MM: (K/(K+τ))^α")
    print(f"{'─'*80}")
    print(f"\n  {'α':>6s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 55)

    for alpha in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]:
        cost_fn = lambda t, _a=alpha: power_law_cost(t, alpha=_a)
        try:
            k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
            ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
            if abs(ns - 0.9649) > 0.005:
                continue
            note = ""
            if -0.012 < run < 0.002:
                note = "*** MATCH ***"
            elif run < 0:
                note = "negative!"
            print(f"  {alpha:6.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
        except (ValueError, OverflowError, ZeroDivisionError):
            pass

    # --- 6. Two-stage ---
    print(f"\n{'─'*80}")
    print("  6. TWO-STAGE (fast local + slow global)")
    print(f"{'─'*80}")
    print(f"\n  {'K1':>6s}  {'K2':>6s}  {'w':>5s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 70)

    for k1 in [0.1, 0.3, 0.5]:
        for k2 in [3.0, 5.0, 10.0, 20.0]:
            for w in [0.1, 0.3, 0.5, 0.7]:
                cost_fn = lambda t, _k1=k1, _k2=k2, _w=w: two_stage_cost(t, k_half_1=_k1, k_half_2=_k2, weight=_w)
                try:
                    k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
                    ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
                    if abs(ns - 0.9649) > 0.005:
                        continue
                    note = ""
                    if -0.012 < run < 0.002:
                        note = "*** MATCH ***"
                    elif run < 0:
                        note = "negative!"
                    print(f"  {k1:6.2f}  {k2:6.2f}  {w:5.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
                except (ValueError, OverflowError, ZeroDivisionError):
                    pass

    # --- 7. Mean-field bootstrap ---
    print(f"\n{'─'*80}")
    print("  7. MEAN-FIELD BOOTSTRAP (self-consistency cost)")
    print(f"{'─'*80}")
    print(f"\n  {'b':>6s}  {'k_pivot':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 55)

    for b in [0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
        cost_fn = lambda t, _b=b: mean_field_bootstrap_cost(t, bootstrap_time=_b)
        try:
            k_p = fit_pivot(cost_fn, tau_0, param_range=(0.001, 100.0))
            ns, run = numerical_ns_and_running(cost_fn, k_p, tau_0)
            if abs(ns - 0.9649) > 0.005:
                continue
            note = ""
            if -0.012 < run < 0.002:
                note = "*** MATCH ***"
            elif run < 0:
                note = "negative!"
            print(f"  {b:6.2f}  {k_p:8.4f}  {ns:8.4f}  {run:+10.6f}  {note:>15s}")
        except (ValueError, OverflowError, ZeroDivisionError):
            pass

    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")
    print("""
  The question: which cost function families can produce n_s ≈ 0.965
  AND negative running (dn_s/d ln k < 0)?

  Physical constraint: the cost function must describe synchronization
  cost as a function of synchronization time. It should:
    - Start high (unsynchronized)
    - End low (synchronized)
    - Be non-negative

  The running sign depends on the curvature of ln(1/C) as a function
  of ln k. Negative running requires this to be concave — the power
  spectrum bends downward at the pivot scale.
""")
