// staircase.js — live W(Ω) plot.
//
// Plots bare frequency ωⱼ on the x-axis and locked frequency
// (dθⱼ/dt averaged over a window, normalized to [0,1] by /2π) on the y-axis.
// As K increases, the cloud organizes into horizontal plateaus at rational
// ratios — the devil's staircase.

export class Staircase {
  constructor(canvas, engine, opts = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.engine = engine;
    this.opts = {
      lo: opts.lo ?? 0,
      hi: opts.hi ?? 1.2,
      ...opts,
    };
    this.resize();
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    this.canvas.height = Math.max(1, Math.floor(rect.height * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  draw() {
    const ctx = this.ctx;
    const rect = this.canvas.getBoundingClientRect();
    const W = rect.width;
    const H = rect.height;

    ctx.clearRect(0, 0, W, H);

    const margin = { l: 36, r: 12, t: 28, b: 28 };
    const plotW = W - margin.l - margin.r;
    const plotH = H - margin.t - margin.b;
    const lo = this.opts.lo;
    const hi = this.opts.hi;

    const xScale = (x) => margin.l + ((x - lo) / (hi - lo)) * plotW;
    const yScale = (y) => margin.t + (1 - (y - lo) / (hi - lo)) * plotH;

    // Reference rationals (× the dominant locked frequency, when one exists).
    const meanLocked = (() => {
      let sum = 0;
      for (let i = 0; i < this.engine.N; i++) sum += this.engine.getLockedFrequency(i);
      return sum / this.engine.N;
    })();
    ctx.strokeStyle = "#2e313a";
    ctx.lineWidth = 1;
    const refs = [1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5];
    ctx.setLineDash([2, 4]);
    for (const r of refs) {
      const yy = yScale(r * meanLocked);
      if (yy < margin.t || yy > margin.t + plotH) continue;
      ctx.beginPath();
      ctx.moveTo(margin.l, yy);
      ctx.lineTo(margin.l + plotW, yy);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Diagonal y=x (uncoupled reference).
    ctx.strokeStyle = "#3a3d44";
    ctx.beginPath();
    ctx.moveTo(xScale(lo), yScale(lo));
    ctx.lineTo(xScale(hi), yScale(hi));
    ctx.stroke();

    // Axes.
    ctx.strokeStyle = "#555";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(margin.l, margin.t);
    ctx.lineTo(margin.l, margin.t + plotH);
    ctx.lineTo(margin.l + plotW, margin.t + plotH);
    ctx.stroke();

    ctx.fillStyle = "#888";
    ctx.font = "11px ui-sans-serif";
    ctx.fillText("Ω (bare)", margin.l + plotW - 50, margin.t + plotH + 20);
    ctx.save();
    ctx.translate(12, margin.t + plotH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("W (locked)", -32, 0);
    ctx.restore();

    // Data points: bare ω vs. locked ω in native engine units.
    const N = this.engine.N;
    for (let i = 0; i < N; i++) {
      const omega = this.engine.omegas[i];
      const lockedF = this.engine.getLockedFrequency(i);
      const x = xScale(omega);
      const y = yScale(lockedF);
      ctx.fillStyle = `hsla(${(((lockedF % 1) + 1) % 1) * 360}, 70%, 60%, 0.7)`;
      ctx.beginPath();
      ctx.arc(x, y, 2, 0, Math.PI * 2);
      ctx.fill();
    }
  }
}
