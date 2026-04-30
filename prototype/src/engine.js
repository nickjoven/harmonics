// engine.js — Kuramoto and circle-map dynamics for the metronome wall.
//
// Two engines, both implementing a common API:
//   step(nSteps?: number): void
//   getOrderParameter(): { r: number, psi: number }
//   getInstantFrequency(i: number): number
//   getLockedFrequency(i: number): number
//
// The KuramotoEngine integrates the mean-field ODE
//   dθⱼ/dt = ωⱼ + K·r·sin(ψ − θⱼ)
// where r·exp(iψ) = (1/N) Σ exp(iθₖ) is the order parameter.
//
// The CircleMapEngine iterates the standard map
//   θₙ₊₁ = θₙ + Ω − (K/2π) sin(2π θₙ)
// per oscillator independently.

const TWO_PI = Math.PI * 2;

// Deterministic pseudo-RNG so initial conditions are reproducible across runs.
export function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function uniformFrequencies(N, lo = 0.05, hi = 0.95, seed = 1) {
  const rng = mulberry32(seed);
  const omegas = new Float64Array(N);
  for (let i = 0; i < N; i++) omegas[i] = lo + (hi - lo) * rng();
  return omegas;
}

export function lorentzianFrequencies(N, gamma = 0.1, center = 0.5, seed = 1) {
  const rng = mulberry32(seed);
  const omegas = new Float64Array(N);
  for (let i = 0; i < N; i++) {
    const u = rng() - 0.5;
    omegas[i] = center + gamma * Math.tan(Math.PI * u);
  }
  return omegas;
}

// Best p/q approximation of x with denominator ≤ maxQ (Stern-Brocot search).
// Returns [p, q, distance].
export function bestRational(x, maxQ = 50) {
  let bestP = 0;
  let bestQ = 1;
  let bestErr = Math.abs(x);
  for (let q = 1; q <= maxQ; q++) {
    const p = Math.round(x * q);
    const err = Math.abs(x - p / q);
    if (err < bestErr) {
      bestP = p;
      bestQ = q;
      bestErr = err;
    }
  }
  return [bestP, bestQ, bestErr];
}

// ── Kuramoto: continuous-time mean-field oscillators on S¹. ──────────────────

export class KuramotoEngine {
  constructor({ N, omegas, K = 0, dt = 0.01, seed = 1, historySize = 1024 }) {
    if (omegas.length !== N) throw new Error("omegas.length must equal N");
    this.N = N;
    this.omegas = Float64Array.from(omegas);
    this.K = K;
    this.dt = dt;
    this.t = 0;

    const rng = mulberry32(seed ^ 0xA5A5A5);
    this.theta = new Float64Array(N);
    this.theta0 = new Float64Array(N);
    for (let j = 0; j < N; j++) {
      this.theta[j] = TWO_PI * rng();
      this.theta0[j] = this.theta[j];
    }

    // Unwrapped phase tracker for measuring locked frequency over a window.
    this.thetaUnwrap = Float64Array.from(this.theta);
    this.thetaPrev = Float64Array.from(this.theta);

    this.historySize = historySize;
    this.history = []; // ring buffer of { t, thetaUnwrap snapshot every K_HIST_STRIDE steps }
    this.stepsSinceSample = 0;
    this.sampleStride = 4;
  }

  setK(K) { this.K = K; }

  setFrequencies(omegas) {
    if (omegas.length !== this.N) throw new Error("length mismatch");
    this.omegas = Float64Array.from(omegas);
  }

  reset() {
    this.t = 0;
    this.theta.set(this.theta0);
    this.thetaUnwrap.set(this.theta0);
    this.thetaPrev.set(this.theta0);
    this.history.length = 0;
    this.stepsSinceSample = 0;
  }

  step(nSteps = 1) {
    const N = this.N;
    const dt = this.dt;
    const K = this.K;

    for (let s = 0; s < nSteps; s++) {
      // Order parameter.
      let cx = 0, cy = 0;
      for (let j = 0; j < N; j++) {
        cx += Math.cos(this.theta[j]);
        cy += Math.sin(this.theta[j]);
      }
      cx /= N; cy /= N;
      const r = Math.sqrt(cx * cx + cy * cy);
      const psi = Math.atan2(cy, cx);

      // Mean-field update.
      this.thetaPrev.set(this.theta);
      const Kr = K * r;
      for (let j = 0; j < N; j++) {
        const dtheta = this.omegas[j] + Kr * Math.sin(psi - this.theta[j]);
        this.theta[j] += dt * dtheta;
        this.thetaUnwrap[j] += dt * dtheta;
      }

      // Wrap theta into [0, 2π) for visualization stability.
      for (let j = 0; j < N; j++) {
        if (this.theta[j] >= TWO_PI) this.theta[j] -= TWO_PI;
        else if (this.theta[j] < 0) this.theta[j] += TWO_PI;
      }

      this.t += dt;
      this.stepsSinceSample++;

      if (this.stepsSinceSample >= this.sampleStride) {
        this.stepsSinceSample = 0;
        if (this.history.length >= this.historySize) this.history.shift();
        this.history.push({
          t: this.t,
          thetaUnwrap: Float64Array.from(this.thetaUnwrap),
        });
      }
    }
  }

  getOrderParameter() {
    let cx = 0, cy = 0;
    for (let j = 0; j < this.N; j++) {
      cx += Math.cos(this.theta[j]);
      cy += Math.sin(this.theta[j]);
    }
    cx /= this.N; cy /= this.N;
    return { r: Math.sqrt(cx * cx + cy * cy), psi: Math.atan2(cy, cx) };
  }

  getInstantFrequency(i) {
    // Use the most recent dθ/dt estimate from the last step.
    if (this.history.length < 2) return this.omegas[i];
    const last = this.history[this.history.length - 1];
    const prev = this.history[this.history.length - 2];
    const dt = last.t - prev.t;
    if (dt <= 0) return this.omegas[i];
    return (last.thetaUnwrap[i] - prev.thetaUnwrap[i]) / dt;
  }

  getLockedFrequency(i) {
    // Long-window average to identify locked frequency.
    if (this.history.length < 4) return this.omegas[i];
    const first = this.history[0];
    const last = this.history[this.history.length - 1];
    const dt = last.t - first.t;
    if (dt <= 0) return this.omegas[i];
    return (last.thetaUnwrap[i] - first.thetaUnwrap[i]) / dt;
  }

  // Cluster oscillators by locked frequency (for cluster count display).
  getClusters(tol = 0.01) {
    const freqs = [];
    for (let i = 0; i < this.N; i++) freqs.push(this.getLockedFrequency(i));
    const sorted = [...freqs].sort((a, b) => a - b);
    let count = 0;
    let last = -Infinity;
    for (const f of sorted) {
      if (Math.abs(f - last) > tol) {
        count++;
        last = f;
      }
    }
    return count;
  }
}

// ── Circle map: discrete iteration, used for tongue-width measurement. ───────

export class CircleMapEngine {
  constructor({ N, omegas, K = 0, seed = 1 }) {
    if (omegas.length !== N) throw new Error("omegas.length must equal N");
    this.N = N;
    this.omegas = Float64Array.from(omegas);
    this.K = K;
    this.theta = new Float64Array(N);
    this.theta0 = new Float64Array(N);

    const rng = mulberry32(seed ^ 0x5A5A5A);
    for (let j = 0; j < N; j++) {
      this.theta[j] = rng();
      this.theta0[j] = this.theta[j];
    }
    this.n = 0;
  }

  setK(K) { this.K = K; }

  reset() {
    this.theta.set(this.theta0);
    this.n = 0;
  }

  step(nSteps = 1) {
    const N = this.N;
    const Kfac = this.K / TWO_PI;
    for (let s = 0; s < nSteps; s++) {
      for (let j = 0; j < N; j++) {
        this.theta[j] += this.omegas[j] - Kfac * Math.sin(TWO_PI * this.theta[j]);
      }
      this.n++;
    }
  }

  // Rotation number: (θₙ − θ₀) / n. With sufficient n this converges to a
  // rational p/q if ωⱼ lies inside an Arnold tongue.
  getRotationNumber(i) {
    if (this.n === 0) return this.omegas[i];
    return (this.theta[i] - this.theta0[i]) / this.n;
  }

  // Single-oscillator winding number with explicit transient + measurement.
  // Used by the tongue-width harness; not the live wall.
  static winding(omega, K, nTrans = 5000, nMeas = 20000) {
    const Kfac = K / TWO_PI;
    let theta = 0;
    for (let i = 0; i < nTrans; i++) {
      theta += omega - Kfac * Math.sin(TWO_PI * theta);
    }
    const start = theta;
    for (let i = 0; i < nMeas; i++) {
      theta += omega - Kfac * Math.sin(TWO_PI * theta);
    }
    return (theta - start) / nMeas;
  }

  // Tongue width at p/q via bisection on winding number — mirrors the
  // Python reference at sync_cost/derivations/tongue_widths_exact.py.
  static tongueWidth(p, q, K, opts = {}) {
    const tol = opts.tol ?? 5e-4;
    const nBisect = opts.nBisect ?? 40;

    let nTrans = opts.nTrans ?? 5000;
    let nMeas = opts.nMeas ?? 20000;
    if (K > 0.8) {
      nTrans = Math.max(nTrans, 20000);
      nMeas = Math.max(nMeas, 50000);
    } else if (K > 0.5) {
      nTrans = Math.max(nTrans, 10000);
      nMeas = Math.max(nMeas, 30000);
    }

    const target = p / q;
    const Wcenter = CircleMapEngine.winding(target, K, nTrans, nMeas);
    if (Math.abs(Wcenter - target) > tol) return 0;

    const halfWindow = Math.max(4 / (q * q), 0.02);

    // Bisect left edge.
    let lo = Math.max(target - halfWindow, 0.001);
    let hi = target;
    for (let b = 0; b < nBisect; b++) {
      const mid = 0.5 * (lo + hi);
      const W = CircleMapEngine.winding(mid, K, nTrans, nMeas);
      if (Math.abs(W - target) < tol) hi = mid;
      else lo = mid;
    }
    const left = 0.5 * (lo + hi);

    // Bisect right edge.
    lo = target;
    hi = Math.min(target + halfWindow, 0.999);
    for (let b = 0; b < nBisect; b++) {
      const mid = 0.5 * (lo + hi);
      const W = CircleMapEngine.winding(mid, K, nTrans, nMeas);
      if (Math.abs(W - target) < tol) lo = mid;
      else hi = mid;
    }
    const right = 0.5 * (lo + hi);

    return Math.max(right - left, 0);
  }
}
