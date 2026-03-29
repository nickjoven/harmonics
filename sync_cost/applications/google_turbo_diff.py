"""
google-turbo-diff: Framework-native quantization vs TurboQuant.

Three fidelity levels comparing two quantization philosophies:
  TurboQuant: random rotation → Beta distribution → Lloyd-Max centroids
  Framework:  circle map → devil's staircase → Farey fraction centroids

All stdlib. No numpy, no scipy.

Usage:
    python sync_cost/applications/google_turbo_diff.py [--level 1|2|3|all]
"""

from __future__ import annotations
import math
import sys
from fractions import Fraction
from typing import NamedTuple


# ===================================================================
# SECTION 1: Number theory primitives
# ===================================================================

def farey_sequence(n: int) -> list[Fraction]:
    """Farey sequence F_n: all irreducible fractions with denominator <= n."""
    fracs = set()
    for d in range(1, n + 1):
        for num in range(0, d + 1):
            fracs.add(Fraction(num, d))
    return sorted(fracs)


def euler_totient(n: int) -> int:
    result = n
    p, temp = 2, n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def farey_count(n: int) -> int:
    return 1 + sum(euler_totient(k) for k in range(1, n + 1))


def select_farey_codebook(n_levels: int, order: int = 6) -> list[float]:
    """
    Select n_levels from F_order, prioritizing stability (smallest q).

    Endpoints 0 and 1 always included. Remaining levels filled by
    ascending denominator, then by proximity to 1/2 within same q.
    """
    F = farey_sequence(order)

    # Group by denominator
    by_q: dict[int, list[Fraction]] = {}
    for f in F:
        q = f.denominator
        if q not in by_q:
            by_q[q] = []
        by_q[q].append(f)

    # Always include endpoints
    selected = {Fraction(0, 1), Fraction(1, 1)}

    # Fill remaining by stability rank (ascending q), breaking ties
    # by closeness to 1/2 (most stable mode)
    for q in sorted(by_q.keys()):
        candidates = sorted(by_q[q], key=lambda f: abs(float(f) - 0.5))
        for f in candidates:
            if len(selected) >= n_levels:
                break
            selected.add(f)
        if len(selected) >= n_levels:
            break

    result = sorted(float(f) for f in selected)
    return result[:n_levels]


def ford_radius(q: int) -> float:
    """Ford circle radius for denominator q: 1/(2q²)."""
    return 1.0 / (2.0 * q * q)


# ===================================================================
# SECTION 2: Circle map and devil's staircase
# ===================================================================

def circle_map_iterate(theta: float, omega: float, K: float) -> float:
    """Single iteration: θ_{n+1} = θ_n + ω - (K/2π)sin(2πθ_n)."""
    return theta + omega - (K / (2.0 * math.pi)) * math.sin(2.0 * math.pi * theta)


def winding_number(omega: float, K: float,
                   n_transient: int = 80, n_measure: int = 200) -> float:
    """Winding number W(ω, K) of the circle map."""
    theta = 0.0
    k_over_2pi = K / (2.0 * math.pi)
    two_pi = 2.0 * math.pi
    for _ in range(n_transient):
        theta = theta + omega - k_over_2pi * math.sin(two_pi * theta)
    total = 0.0
    for _ in range(n_measure):
        new_theta = theta + omega - k_over_2pi * math.sin(two_pi * theta)
        total += new_theta - theta
        theta = new_theta
    return total / n_measure


def staircase_transform(values: list[float], K: float) -> list[float]:
    """
    Apply the devil's staircase transform: map each value through W(·, K).

    This is the framework's analogue of TurboQuant's random rotation.
    It makes the distribution predictable (staircase-shaped) regardless
    of input distribution.
    """
    return [winding_number(v, K) for v in values]


# ===================================================================
# SECTION 3: Beta distribution and Lloyd-Max
# ===================================================================

def log_beta_func(a: float, b: float) -> float:
    """log(B(a, b)) = log(Γ(a)) + log(Γ(b)) - log(Γ(a+b))."""
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def beta_pdf(x: float, alpha: float, beta_param: float) -> float:
    """Beta PDF on [0, 1]."""
    if x <= 0.0 or x >= 1.0:
        return 0.0
    log_p = ((alpha - 1) * math.log(x) + (beta_param - 1) * math.log(1 - x)
             - log_beta_func(alpha, beta_param))
    return math.exp(log_p)


def beta_cdf_numerical(x: float, alpha: float, beta_param: float,
                       n_steps: int = 500) -> float:
    """Numerical CDF of Beta distribution via Simpson's rule."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    h = x / n_steps
    total = 0.0
    for i in range(n_steps):
        x0 = i * h
        x1 = (i + 0.5) * h
        x2 = (i + 1) * h
        f0 = beta_pdf(x0, alpha, beta_param)
        f1 = beta_pdf(x1, alpha, beta_param)
        f2 = beta_pdf(x2, alpha, beta_param)
        total += (f0 + 4 * f1 + f2) * h / 6
    return min(1.0, max(0.0, total))


def beta_quantile(p: float, alpha: float, beta_param: float,
                  tol: float = 1e-10) -> float:
    """Inverse CDF of Beta distribution via bisection."""
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if beta_cdf_numerical(mid, alpha, beta_param) < p:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


def beta_conditional_mean(lo: float, hi: float,
                          alpha: float, beta_param: float,
                          n_steps: int = 200) -> float:
    """E[X | lo < X < hi] for Beta(alpha, beta_param)."""
    if hi <= lo:
        return (lo + hi) / 2

    h = (hi - lo) / n_steps
    num = 0.0
    den = 0.0
    for i in range(n_steps):
        x0 = lo + i * h
        x1 = lo + (i + 0.5) * h
        x2 = lo + (i + 1) * h
        for x, w in [(x0, 1), (x1, 4), (x2, 1)]:
            f = beta_pdf(x, alpha, beta_param)
            num += w * x * f
            den += w * f
    if den == 0:
        return (lo + hi) / 2
    return num / den


def lloyd_max_beta(n_levels: int, alpha: float, beta_param: float,
                   max_iter: int = 100, tol: float = 1e-12) -> tuple[list[float], list[float]]:
    """
    Lloyd-Max algorithm for Beta(alpha, beta_param).

    Returns (centroids, boundaries) where:
      - centroids: n_levels optimal quantization levels
      - boundaries: n_levels+1 boundaries (first=-inf sentinel as 0, last=1)
    """
    # Initialize centroids at quantile midpoints
    centroids = []
    for i in range(n_levels):
        p = (i + 0.5) / n_levels
        centroids.append(beta_quantile(p, alpha, beta_param))

    prev_mse = float('inf')
    for iteration in range(max_iter):
        # Update boundaries (midpoints between centroids)
        boundaries = [0.0]
        for i in range(len(centroids) - 1):
            boundaries.append((centroids[i] + centroids[i + 1]) / 2)
        boundaries.append(1.0)

        # Update centroids (conditional expectations)
        new_centroids = []
        for i in range(n_levels):
            cm = beta_conditional_mean(boundaries[i], boundaries[i + 1],
                                       alpha, beta_param)
            new_centroids.append(cm)
        centroids = new_centroids

        # Check convergence
        current_mse = sum((c1 - c2) ** 2 for c1, c2 in
                          zip(centroids, new_centroids))
        if abs(prev_mse - current_mse) < tol:
            break
        prev_mse = current_mse

    # Final boundaries
    boundaries = [0.0]
    for i in range(len(centroids) - 1):
        boundaries.append((centroids[i] + centroids[i + 1]) / 2)
    boundaries.append(1.0)

    return centroids, boundaries


# ===================================================================
# SECTION 4: Quantizer implementations
# ===================================================================

def nearest_neighbor_boundaries(levels: list[float]) -> list[float]:
    """Midpoint boundaries — MSE-optimal for any given set of levels."""
    b = [float('-inf')]
    for i in range(len(levels) - 1):
        b.append((levels[i] + levels[i + 1]) / 2)
    b.append(float('inf'))
    return b


def quantize_scalar(value: float, levels: list[float],
                    boundaries: list[float]) -> tuple[int, float]:
    """Quantize to nearest level. Returns (index, quantized_value)."""
    for i in range(len(levels)):
        if value <= boundaries[i + 1]:
            return i, levels[i]
    return len(levels) - 1, levels[-1]


def quantize_array(values: list[float], levels: list[float],
                   boundaries: list[float]) -> list[float]:
    return [quantize_scalar(v, levels, boundaries)[1] for v in values]


def mse(a: list[float], b: list[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


def snr_db(original: list[float], quantized: list[float]) -> float:
    sig = sum(x * x for x in original) / len(original)
    noise = mse(original, quantized)
    if noise == 0:
        return float('inf')
    return 10 * math.log10(sig / noise)


# ===================================================================
# SECTION 5: Random number generation (stdlib only)
# ===================================================================

class LCG:
    """Linear congruential generator with utility methods."""

    def __init__(self, seed: int = 42):
        self.state = seed

    def next_float(self) -> float:
        self.state = (1103515245 * self.state + 12345) & 0x7FFFFFFF
        return self.state / 0x7FFFFFFF

    def uniform(self, n: int) -> list[float]:
        return [self.next_float() for _ in range(n)]

    def normal(self) -> float:
        """Box-Muller transform."""
        u1 = max(1e-15, self.next_float())
        u2 = self.next_float()
        return math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)

    def normal_list(self, n: int) -> list[float]:
        return [self.normal() for _ in range(n)]

    def beta_sample(self, alpha: float, beta_param: float) -> float:
        """Sample from Beta(alpha, beta). Uses normal approx for large alpha."""
        if alpha > 5 and beta_param > 5:
            # Normal approximation: Beta(a,b) ≈ N(a/(a+b), ab/((a+b)²(a+b+1)))
            mu = alpha / (alpha + beta_param)
            var = (alpha * beta_param) / ((alpha + beta_param) ** 2 * (alpha + beta_param + 1))
            z = self.normal()
            return max(0.0, min(1.0, mu + math.sqrt(var) * z))
        u = self.next_float()
        return beta_quantile(u, alpha, beta_param)

    def beta_samples(self, alpha: float, beta_param: float,
                     n: int) -> list[float]:
        return [self.beta_sample(alpha, beta_param) for _ in range(n)]

    def unit_vector(self, d: int) -> list[float]:
        """Random unit vector in R^d."""
        v = self.normal_list(d)
        norm = math.sqrt(sum(x * x for x in v))
        if norm == 0:
            v[0] = 1.0
            return v
        return [x / norm for x in v]


# ===================================================================
# SECTION 6: Vector operations (stdlib only)
# ===================================================================

def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def vec_sub(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def vec_scale(v: list[float], s: float) -> list[float]:
    return [x * s for x in v]


def gram_schmidt(rows: list[list[float]]) -> list[list[float]]:
    """Orthogonalize rows via Gram-Schmidt. Returns orthonormal rows."""
    result = []
    for v in rows:
        u = v[:]
        for w in result:
            proj = dot(u, w)
            u = [u_i - proj * w_i for u_i, w_i in zip(u, w)]
        n = vec_norm(u)
        if n > 1e-12:
            result.append([x / n for x in u])
    return result


def random_orthogonal(d: int, rng: LCG) -> list[list[float]]:
    """Random orthogonal matrix via QR of Gaussian matrix."""
    rows = [rng.normal_list(d) for _ in range(d)]
    return gram_schmidt(rows)


def mat_vec(mat: list[list[float]], vec: list[float]) -> list[float]:
    """Matrix-vector product."""
    return [dot(row, vec) for row in mat]


def mat_T_vec(mat: list[list[float]], vec: list[float]) -> list[float]:
    """Transpose-matrix-vector product (mat^T @ vec)."""
    d = len(mat[0])
    result = [0.0] * d
    for i, row in enumerate(mat):
        for j in range(d):
            result[j] += row[j] * vec[i]
    return result


# ===================================================================
# SECTION 7: Full quantization pipelines
# ===================================================================

class QuantResult(NamedTuple):
    mse: float
    snr: float
    max_err: float
    bits: float


def pipeline_uniform(values: list[float], n_bits: int) -> QuantResult:
    """Baseline: uniform quantization on [0, 1]."""
    n_levels = 1 << n_bits
    levels = [i / (n_levels - 1) for i in range(n_levels)]
    bounds = nearest_neighbor_boundaries(levels)
    q = quantize_array(values, levels, bounds)
    return QuantResult(
        mse=mse(values, q),
        snr=snr_db(values, q),
        max_err=max(abs(a - b) for a, b in zip(values, q)),
        bits=n_bits,
    )


def pipeline_lloyd_max_beta(values: list[float], n_bits: int,
                            dim: int) -> QuantResult:
    """TurboQuant approach: Lloyd-Max for Beta((d-1)/2, (d-1)/2)."""
    n_levels = 1 << n_bits
    alpha = (dim - 1) / 2.0
    centroids, bounds = lloyd_max_beta(n_levels, alpha, alpha)
    q = quantize_array(values, centroids, bounds)
    return QuantResult(
        mse=mse(values, q),
        snr=snr_db(values, q),
        max_err=max(abs(a - b) for a, b in zip(values, q)),
        bits=n_bits,
    )


def pipeline_farey(values: list[float], n_bits: int,
                   farey_order: int = 6) -> QuantResult:
    """Framework approach: Farey codebook."""
    n_levels = 1 << n_bits
    levels = select_farey_codebook(n_levels, farey_order)
    bounds = nearest_neighbor_boundaries(levels)
    q = quantize_array(values, levels, bounds)
    return QuantResult(
        mse=mse(values, q),
        snr=snr_db(values, q),
        max_err=max(abs(a - b) for a, b in zip(values, q)),
        bits=n_bits,
    )


# ===================================================================
# LEVEL 1: Scalar codebook comparison
# ===================================================================

def level_1_scalar():
    """Compare codebooks on 1D distributions at multiple bit rates."""
    print("=" * 76)
    print("LEVEL 1: Scalar Codebook Comparison")
    print("=" * 76)

    rng = LCG(42)
    N = 2000
    N_staircase = 500  # staircase is O(N * n_iter), keep small

    for n_bits in [2, 3, 4]:
        n_levels = 1 << n_bits
        print(f"\n--- {n_bits}-bit ({n_levels} levels) ---")

        # Build codebooks
        uniform_levels = [i / (n_levels - 1) for i in range(n_levels)]

        # Farey codebook
        farey_levels = select_farey_codebook(n_levels, order=6)
        if n_bits >= 4:
            farey_levels = select_farey_codebook(n_levels, order=10)

        # Lloyd-Max for Beta (dim=128 typical)
        alpha = 63.5  # (128-1)/2
        lm_centroids_raw, lm_bounds_raw = lloyd_max_beta(n_levels, alpha, alpha)
        lm_centroids = lm_centroids_raw

        print(f"  Uniform:    {['%.4f' % x for x in uniform_levels]}")
        print(f"  Farey(F6):  {['%.4f' % x for x in farey_levels]}")
        print(f"  Lloyd-Max:  {['%.4f' % x for x in lm_centroids]}")

        # Boundaries
        uni_b = nearest_neighbor_boundaries(uniform_levels)
        far_b = nearest_neighbor_boundaries(farey_levels)

        # Distributions
        print("  (computing distributions...)", flush=True)
        distributions = {
            "Uniform [0,1]":    rng.uniform(N),
            "Beta(63.5,63.5)":  rng.beta_samples(63.5, 63.5, N),
            "Staircase K=0.8":  staircase_transform(rng.uniform(N_staircase), K=0.8),
            "Staircase K=0.95": staircase_transform(rng.uniform(N_staircase), K=0.95),
        }

        hdr = f"  {'Distribution':<22}"
        for label in ["Uniform", "Farey", "Lloyd-Max"]:
            hdr += f" {label:>12}"
        hdr += f"  {'Best':>10}"
        print(hdr)
        print("  " + "-" * 72)

        for dname, data in distributions.items():
            q_u = quantize_array(data, uniform_levels, uni_b)
            q_f = quantize_array(data, farey_levels, far_b)
            q_l = quantize_array(data, lm_centroids, lm_bounds_raw)

            m_u, m_f, m_l = mse(data, q_u), mse(data, q_f), mse(data, q_l)
            results = [("Uniform", m_u), ("Farey", m_f), ("Lloyd-Max", m_l)]
            best = min(results, key=lambda r: r[1])

            row = f"  {dname:<22}"
            for label, m in results:
                marker = "*" if label == best[0] else " "
                row += f" {m:11.6f}{marker}"
            row += f"  {best[0]:>10}"
            print(row)


# ===================================================================
# LEVEL 2: Vector MSE comparison
# ===================================================================

def level_2_vector():
    """Full vector pipelines: rotation+LM vs circle-map+Farey."""
    print("\n" + "=" * 76)
    print("LEVEL 2: Vector Quantization (MSE)")
    print("=" * 76)

    rng = LCG(123)

    for dim in [16, 32]:
        for n_bits in [2, 3]:
            n_levels = 1 << n_bits
            n_vectors = 50
            print(f"\n--- d={dim}, {n_bits}-bit, {n_vectors} vectors ---")

            # Precompute codebooks
            alpha = (dim - 1) / 2.0
            lm_centroids, lm_bounds = lloyd_max_beta(n_levels, alpha, alpha)
            farey_levels = select_farey_codebook(n_levels, order=6)
            farey_bounds = nearest_neighbor_boundaries(farey_levels)
            uniform_levels = [i / (n_levels - 1) for i in range(n_levels)]
            uniform_bounds = nearest_neighbor_boundaries(uniform_levels)

            # Precompute random orthogonal matrix (shared for all vectors)
            Q = random_orthogonal(dim, rng)

            # Accumulators
            mse_rotation_lm = 0.0
            mse_rotation_farey = 0.0
            mse_cmap_farey = 0.0
            mse_uniform = 0.0

            for _ in range(n_vectors):
                vec = rng.unit_vector(dim)

                # --- Pipeline A: Rotation + Lloyd-Max (TurboQuant) ---
                rotated = mat_vec(Q, vec)
                # Map to [0,1]: (x + 1) / 2 for symmetric Beta
                mapped_a = [(x + 1) / 2 for x in rotated]
                quantized_a = quantize_array(mapped_a, lm_centroids, lm_bounds)
                recon_a = [2 * x - 1 for x in quantized_a]  # back to [-1,1]
                recon_a = mat_T_vec(Q, recon_a)  # inverse rotation
                mse_rotation_lm += sum((a - b) ** 2 for a, b in zip(vec, recon_a)) / dim

                # --- Pipeline B: Rotation + Farey (hybrid) ---
                quantized_b = quantize_array(mapped_a, farey_levels, farey_bounds)
                recon_b = [2 * x - 1 for x in quantized_b]
                recon_b = mat_T_vec(Q, recon_b)
                mse_rotation_farey += sum((a - b) ** 2 for a, b in zip(vec, recon_b)) / dim

                # --- Pipeline C: Circle map + Farey (framework-native) ---
                # Normalize to [0,1] via (x+1)/2, apply staircase, quantize
                mapped_c = [(x + 1) / 2 for x in vec]
                staircase_c = staircase_transform(mapped_c, K=0.8)
                quantized_c = quantize_array(staircase_c, farey_levels, farey_bounds)
                # Inverse: we store the quantized staircase values
                # For reconstruction, map back (staircase is not trivially invertible,
                # so we use the quantized values directly as the representation)
                recon_c = [2 * x - 1 for x in quantized_c]
                mse_cmap_farey += sum((a - b) ** 2 for a, b in zip(vec, recon_c)) / dim

                # --- Pipeline D: Uniform baseline ---
                mapped_d = [(x + 1) / 2 for x in vec]
                quantized_d = quantize_array(mapped_d, uniform_levels, uniform_bounds)
                recon_d = [2 * x - 1 for x in quantized_d]
                mse_uniform += sum((a - b) ** 2 for a, b in zip(vec, recon_d)) / dim

            mse_rotation_lm /= n_vectors
            mse_rotation_farey /= n_vectors
            mse_cmap_farey /= n_vectors
            mse_uniform /= n_vectors

            results = [
                ("Rotation+LM", mse_rotation_lm),
                ("Rotation+Farey", mse_rotation_farey),
                ("CircleMap+Farey", mse_cmap_farey),
                ("Uniform", mse_uniform),
            ]
            best = min(results, key=lambda r: r[1])

            print(f"  {'Pipeline':<20} {'MSE':>12} {'SNR(dB)':>10} {'vs best':>10}")
            print("  " + "-" * 54)
            for label, m in results:
                s = 10 * math.log10(1.0 / m) if m > 0 else float('inf')
                ratio = m / best[1] if best[1] > 0 else float('inf')
                marker = " <--" if label == best[0] else ""
                print(f"  {label:<20} {m:12.6f} {s:10.2f} {ratio:9.2f}x{marker}")


# ===================================================================
# LEVEL 3: Inner product fidelity
# ===================================================================

def level_3_inner_product():
    """The metric that matters: inner product preservation."""
    print("\n" + "=" * 76)
    print("LEVEL 3: Inner Product Fidelity")
    print("=" * 76)

    rng = LCG(777)

    for dim in [16, 32]:
        for n_bits in [2, 3]:
            n_levels = 1 << n_bits
            n_pairs = 80
            print(f"\n--- d={dim}, {n_bits}-bit, {n_pairs} vector pairs ---")

            # Codebooks
            alpha = (dim - 1) / 2.0
            lm_centroids, lm_bounds = lloyd_max_beta(n_levels, alpha, alpha)
            farey_levels = select_farey_codebook(n_levels, order=6)
            farey_bounds = nearest_neighbor_boundaries(farey_levels)
            uniform_levels = [i / (n_levels - 1) for i in range(n_levels)]
            uniform_bounds = nearest_neighbor_boundaries(uniform_levels)

            Q = random_orthogonal(dim, rng)

            # Track inner product errors
            pipelines = {
                "Rotation+LM": {"ip_errors": [], "abs_errors": []},
                "Rotation+Farey": {"ip_errors": [], "abs_errors": []},
                "CircleMap+Farey": {"ip_errors": [], "abs_errors": []},
                "Uniform": {"ip_errors": [], "abs_errors": []},
            }

            for _ in range(n_pairs):
                u = rng.unit_vector(dim)
                v = rng.unit_vector(dim)
                true_ip = dot(u, v)

                # --- Rotation + Lloyd-Max ---
                ru = mat_vec(Q, u)
                rv = mat_vec(Q, v)
                mu = [(x + 1) / 2 for x in ru]
                mv = [(x + 1) / 2 for x in rv]
                qu = quantize_array(mu, lm_centroids, lm_bounds)
                qv = quantize_array(mv, lm_centroids, lm_bounds)
                ru2 = mat_T_vec(Q, [2 * x - 1 for x in qu])
                rv2 = mat_T_vec(Q, [2 * x - 1 for x in qv])
                est_ip = dot(ru2, rv2)
                err = est_ip - true_ip
                pipelines["Rotation+LM"]["ip_errors"].append(err)
                pipelines["Rotation+LM"]["abs_errors"].append(abs(err))

                # --- Rotation + Farey ---
                qu2 = quantize_array(mu, farey_levels, farey_bounds)
                qv2 = quantize_array(mv, farey_levels, farey_bounds)
                ru3 = mat_T_vec(Q, [2 * x - 1 for x in qu2])
                rv3 = mat_T_vec(Q, [2 * x - 1 for x in qv2])
                est_ip2 = dot(ru3, rv3)
                err2 = est_ip2 - true_ip
                pipelines["Rotation+Farey"]["ip_errors"].append(err2)
                pipelines["Rotation+Farey"]["abs_errors"].append(abs(err2))

                # --- Circle map + Farey ---
                su = [(x + 1) / 2 for x in u]
                sv = [(x + 1) / 2 for x in v]
                su_s = staircase_transform(su, K=0.8)
                sv_s = staircase_transform(sv, K=0.8)
                qu3 = quantize_array(su_s, farey_levels, farey_bounds)
                qv3 = quantize_array(sv_s, farey_levels, farey_bounds)
                ru4 = [2 * x - 1 for x in qu3]
                rv4 = [2 * x - 1 for x in qv3]
                est_ip3 = dot(ru4, rv4)
                err3 = est_ip3 - true_ip
                pipelines["CircleMap+Farey"]["ip_errors"].append(err3)
                pipelines["CircleMap+Farey"]["abs_errors"].append(abs(err3))

                # --- Uniform ---
                qu4 = quantize_array(su, uniform_levels, uniform_bounds)
                qv4 = quantize_array(sv, uniform_levels, uniform_bounds)
                ru5 = [2 * x - 1 for x in qu4]
                rv5 = [2 * x - 1 for x in qv4]
                est_ip4 = dot(ru5, rv5)
                err4 = est_ip4 - true_ip
                pipelines["Uniform"]["ip_errors"].append(err4)
                pipelines["Uniform"]["abs_errors"].append(abs(err4))

            print(f"  {'Pipeline':<20} {'Bias':>10} {'IP MSE':>12} {'Max|err|':>10} {'MAE':>10}")
            print("  " + "-" * 64)

            best_mse = float('inf')
            best_name = ""
            for name, data in pipelines.items():
                errs = data["ip_errors"]
                abs_errs = data["abs_errors"]
                bias = sum(errs) / len(errs)
                ip_mse = sum(e * e for e in errs) / len(errs)
                max_abs = max(abs_errs)
                mae = sum(abs_errs) / len(abs_errs)
                if ip_mse < best_mse:
                    best_mse = ip_mse
                    best_name = name
                marker = ""
                print(f"  {name:<20} {bias:+10.6f} {ip_mse:12.6f} {max_abs:10.4f} {mae:10.6f}{marker}")

            print(f"  Best IP MSE: {best_name}")


# ===================================================================
# MAIN
# ===================================================================

def main():
    level = "all"
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:]):
            if arg == "--level" and i + 1 < len(sys.argv) - 1:
                level = sys.argv[i + 2]
            elif arg in ["1", "2", "3", "all"]:
                level = arg

    print("google-turbo-diff: Framework-native vs TurboQuant quantization")
    print(f"Comparing: circle map + Farey vs rotation + Lloyd-Max (Beta)")
    print()

    # Show Farey codebooks
    for bits in [2, 3, 4]:
        n = 1 << bits
        order = 6 if bits <= 3 else 10
        cb = select_farey_codebook(n, order)
        print(f"  Farey {bits}-bit (F{order}): {['%.4f' % x for x in cb]}")
    print(f"  |F_6| = {farey_count(6)}")
    print()

    if level in ["1", "all"]:
        level_1_scalar()

    if level in ["2", "all"]:
        level_2_vector()

    if level in ["3", "all"]:
        level_3_inner_product()

    print("\n" + "=" * 76)
    print("Summary")
    print("=" * 76)
    print("""
  Level 1 (Scalar): Tests codebook quality on known distributions.
    - Lloyd-Max wins on Beta data (by construction).
    - Farey wins on staircase data (by construction).
    - The question is which distribution real weights resemble.

  Level 2 (Vector MSE): Full encode-decode pipeline.
    - Rotation + Lloyd-Max is TurboQuant's actual approach.
    - CircleMap + Farey is the framework-native alternative.
    - Rotation decorrelates coordinates; circle map mode-locks them.

  Level 3 (Inner Product): The attention-relevant metric.
    - Bias matters: biased estimators systematically shift attention.
    - TurboQuant uses QJL to debias (not implemented here — would
      add 1 bit per dim). Framework approach: staircase residuals
      are bounded by tongue widths, giving natural error control.

  Next step: run on actual LLM KV-cache tensors to determine
  whether weight distributions are Beta-like or staircase-like.
""")


if __name__ == "__main__":
    main()
