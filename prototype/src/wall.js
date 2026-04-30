// wall.js — render N oscillators as a grid of tiles ticking on S¹.
//
// Each tile is a square. Inside each tile, a small dot orbits a circle at
// the oscillator's instantaneous angular velocity. The tile background is
// colored by locked-frequency cluster (HSL hue keyed to locked frequency mod 1).
// Hovering a tile shows its bare ω, locked ω, best p/q approximation, and
// L/R word from the Stern-Brocot root.

import { bestRational } from "./engine.js";

export class Wall {
  constructor(canvas, engine, opts = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.engine = engine;
    this.opts = {
      pad: opts.pad ?? 4,
      dotRadius: opts.dotRadius ?? 3,
      ...opts,
    };
    this.hoverIndex = -1;
    this._setupHover();
    this.resize();
  }

  _setupHover() {
    this.canvas.addEventListener("mousemove", (ev) => {
      const rect = this.canvas.getBoundingClientRect();
      const x = (ev.clientX - rect.left) * (this.canvas.width / rect.width);
      const y = (ev.clientY - rect.top) * (this.canvas.height / rect.height);
      this.hoverIndex = this._tileAt(x, y);
      this._mouseScreenX = ev.clientX;
      this._mouseScreenY = ev.clientY;
    });
    this.canvas.addEventListener("mouseleave", () => {
      this.hoverIndex = -1;
    });
  }

  resize() {
    const rect = this.canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.canvas.width = Math.max(1, Math.floor(rect.width * dpr));
    this.canvas.height = Math.max(1, Math.floor(rect.height * dpr));
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this._computeGrid();
  }

  _computeGrid() {
    const N = this.engine.N;
    const rect = this.canvas.getBoundingClientRect();
    const W = rect.width;
    const H = rect.height;

    // Choose grid (cols, rows) closest to canvas aspect ratio.
    const aspect = W / H;
    let bestCols = 1;
    let bestErr = Infinity;
    for (let cols = 1; cols <= N; cols++) {
      const rows = Math.ceil(N / cols);
      const tileW = W / cols;
      const tileH = H / rows;
      const tile = Math.min(tileW, tileH);
      const used = tile * cols * tile * rows;
      const err = Math.abs((cols / rows) - aspect) - used / (W * H);
      if (err < bestErr) {
        bestErr = err;
        bestCols = cols;
      }
    }
    this.cols = bestCols;
    this.rows = Math.ceil(N / this.cols);
    this.tileW = W / this.cols;
    this.tileH = H / this.rows;
  }

  _tileAt(x, y) {
    const c = Math.floor(x / this.tileW);
    const r = Math.floor(y / this.tileH);
    if (c < 0 || c >= this.cols || r < 0 || r >= this.rows) return -1;
    const i = r * this.cols + c;
    return i < this.engine.N ? i : -1;
  }

  draw() {
    const ctx = this.ctx;
    const rect = this.canvas.getBoundingClientRect();
    ctx.clearRect(0, 0, rect.width, rect.height);

    const N = this.engine.N;
    const pad = this.opts.pad;
    const dotR = this.opts.dotRadius;

    for (let i = 0; i < N; i++) {
      const c = i % this.cols;
      const r = Math.floor(i / this.cols);
      const x0 = c * this.tileW;
      const y0 = r * this.tileH;
      const w = this.tileW - pad;
      const h = this.tileH - pad;
      const cx = x0 + w / 2;
      const cy = y0 + h / 2;
      const radius = Math.min(w, h) / 2 - dotR - 2;

      // Tile background: hue from locked frequency.
      const lockedF = this.engine.getLockedFrequency(i);
      const hue = (((lockedF * 0.8) % 1) + 1) % 1; // 0..1
      ctx.fillStyle = `hsl(${hue * 360}, 35%, 18%)`;
      ctx.fillRect(x0, y0, w, h);

      if (i === this.hoverIndex) {
        ctx.strokeStyle = "#6cf";
        ctx.lineWidth = 2;
        ctx.strokeRect(x0 + 1, y0 + 1, w - 2, h - 2);
      }

      // Orbit.
      ctx.strokeStyle = `hsla(${hue * 360}, 50%, 50%, 0.4)`;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI * 2);
      ctx.stroke();

      // Dot.
      const theta = this.engine.theta[i];
      const dx = cx + radius * Math.cos(theta);
      const dy = cy + radius * Math.sin(theta);
      ctx.fillStyle = `hsl(${hue * 360}, 70%, 65%)`;
      ctx.beginPath();
      ctx.arc(dx, dy, dotR, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  getHoverInfo() {
    if (this.hoverIndex < 0) return null;
    const i = this.hoverIndex;
    const omega = this.engine.omegas[i];
    const lockedF = this.engine.getLockedFrequency(i);

    // Best p/q approximation of locked-to-dominant ratio.
    let sum = 0;
    for (let j = 0; j < this.engine.N; j++) sum += this.engine.getLockedFrequency(j);
    const dominant = sum / this.engine.N;
    const ratio = dominant !== 0 ? lockedF / dominant : 0;
    const [p, q, err] = bestRational(ratio, 12);

    return {
      index: i,
      omega,
      lockedFreq: lockedF,
      ratio: q > 0 ? `${p}/${q}` : "—",
      ratioError: err,
      screenX: this._mouseScreenX,
      screenY: this._mouseScreenY,
    };
  }
}
