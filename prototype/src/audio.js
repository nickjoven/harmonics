// audio.js — per-tile click synthesis using Web Audio API.
//
// Each oscillator gets a soft click whenever its phase crosses zero. With
// many oscillators, this is loud; we limit to a configurable subset and
// duck the gain by 1/sqrt(active count) to keep total loudness bounded.

const TWO_PI = Math.PI * 2;

export class AudioBus {
  constructor() {
    this.ctx = null;
    this.master = null;
    this.lastTheta = null;
    this.enabled = false;
    this.maxVoices = 32;
    this.lastClickAt = null; // per-oscillator throttle
  }

  init() {
    if (this.ctx) return;
    this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    this.master = this.ctx.createGain();
    this.master.gain.value = 0.18;
    this.master.connect(this.ctx.destination);
  }

  enable(engine) {
    this.init();
    if (this.ctx.state === "suspended") this.ctx.resume();
    this.enabled = true;
    this.lastTheta = Float64Array.from(engine.theta);
    this.lastClickAt = new Float32Array(engine.N);
  }

  disable() {
    this.enabled = false;
  }

  // Call after each engine.step batch. Detects phase wrap (θ crossing 2π)
  // and emits a click for each crossing tile, subject to voice cap.
  tick(engine) {
    if (!this.enabled) return;
    const N = engine.N;
    if (!this.lastTheta || this.lastTheta.length !== N) {
      this.lastTheta = Float64Array.from(engine.theta);
      this.lastClickAt = new Float32Array(N);
      return;
    }

    const now = this.ctx.currentTime;
    let toClick = [];
    for (let i = 0; i < N; i++) {
      const prev = this.lastTheta[i];
      const cur = engine.theta[i];
      // Detect downward wrap (θ jumped from near 2π back to near 0).
      if (cur < prev - Math.PI) {
        // Throttle: at least 80 ms between clicks per oscillator.
        if (now - this.lastClickAt[i] > 0.08) {
          toClick.push(i);
          this.lastClickAt[i] = now;
        }
      }
      this.lastTheta[i] = cur;
    }

    // Cap voices per tick.
    if (toClick.length > this.maxVoices) {
      // Spread by index hash so we don't always clip the same set.
      toClick = toClick.slice(0, this.maxVoices);
    }

    if (toClick.length === 0) return;
    const ducking = 1 / Math.sqrt(Math.max(1, toClick.length));

    for (const i of toClick) {
      const omega = engine.omegas[i];
      const freq = 220 + 600 * omega; // pitch by bare frequency
      this._click(freq, ducking, i, N);
    }
  }

  _click(freq, gain, i, N) {
    const ctx = this.ctx;
    const t = ctx.currentTime;
    const osc = ctx.createOscillator();
    const env = ctx.createGain();
    const pan = ctx.createStereoPanner ? ctx.createStereoPanner() : null;

    osc.type = "triangle";
    osc.frequency.value = freq;

    env.gain.setValueAtTime(0, t);
    env.gain.linearRampToValueAtTime(gain * 0.5, t + 0.002);
    env.gain.exponentialRampToValueAtTime(0.0001, t + 0.06);

    osc.connect(env);
    if (pan) {
      pan.pan.value = (i / Math.max(1, N - 1)) * 2 - 1;
      env.connect(pan);
      pan.connect(this.master);
    } else {
      env.connect(this.master);
    }

    osc.start(t);
    osc.stop(t + 0.08);
  }
}
