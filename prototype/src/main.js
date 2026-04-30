// main.js — wires the engine, wall, staircase, audio, and UI.

import {
  KuramotoEngine,
  uniformFrequencies,
  lorentzianFrequencies,
} from "./engine.js";
import { Wall } from "./wall.js";
import { Staircase } from "./staircase.js";
import { AudioBus } from "./audio.js";
import { UI } from "./ui.js";

const TWO_PI = Math.PI * 2;

const state = {
  N: 100,
  dist: "uniform",
  seed: 1,
};

function makeFrequencies(N, dist, seed) {
  // Bare frequencies in the engine's native units (radians per simulated
  // time unit). Distribution width is 1 by construction so the canonical
  // K_c = 2/π for uniform g(ω) holds exactly.
  switch (dist) {
    case "uniform":
      return uniformFrequencies(N, 0.1, 1.1, seed);
    case "lorentzian":
      return Float64Array.from(
        lorentzianFrequencies(N, 0.08, 0.6, seed),
        (x) => Math.max(0.05, Math.min(1.15, x))
      );
    case "farey": {
      const targets = [1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 2/5, 3/5, 4/5];
      const out = new Float64Array(N);
      for (let i = 0; i < N; i++) {
        const r = targets[i % targets.length];
        const jitter =
          (Math.sin(i * 12.9898 + seed * 78.233) -
            Math.floor(Math.sin(i * 12.9898 + seed * 78.233))) *
            0.04 -
          0.02;
        out[i] = Math.max(0.02, Math.min(1.18, r + jitter));
      }
      return out;
    }
    default:
      return uniformFrequencies(N, 0.1, 1.1, seed);
  }
}

const engine = new KuramotoEngine({
  N: state.N,
  omegas: makeFrequencies(state.N, state.dist, state.seed),
  K: 0,
  dt: 0.05,
  seed: state.seed,
  historySize: 600,
});

const audio = new AudioBus();

const wallCanvas = document.getElementById("wall-canvas");
const stairCanvas = document.getElementById("staircase-canvas");
const wall = new Wall(wallCanvas, engine);
const staircase = new Staircase(stairCanvas, engine, { lo: 0, hi: 1 });

window.addEventListener("resize", () => {
  wall.resize();
  staircase.resize();
});

const ui = new UI({
  engine,
  audio,
  onPreset: (name) => {
    if (name === "K0") ui.setK(0);
    else if (name === "Kc") ui.setK(2 / Math.PI);
    else if (name === "K1") ui.setK(1.0);
    engine.reset();
  },
  onReset: () => {
    engine.setFrequencies(makeFrequencies(state.N, state.dist, ++state.seed));
    engine.reset();
  },
  onDistChange: (dist) => {
    state.dist = dist;
    engine.setFrequencies(makeFrequencies(state.N, state.dist, state.seed));
    engine.reset();
  },
  onNChange: (N) => {
    state.N = N;
    rebuildEngine();
  },
});

function rebuildEngine() {
  // Replace the engine in place. Easier than reconstructing wall/staircase.
  engine.N = state.N;
  engine.omegas = makeFrequencies(state.N, state.dist, state.seed);
  engine.theta = new Float64Array(state.N);
  engine.theta0 = new Float64Array(state.N);
  engine.thetaUnwrap = new Float64Array(state.N);
  engine.thetaPrev = new Float64Array(state.N);
  for (let i = 0; i < state.N; i++) {
    const t = (i / state.N) * TWO_PI;
    engine.theta[i] = t;
    engine.theta0[i] = t;
    engine.thetaUnwrap[i] = t;
    engine.thetaPrev[i] = t;
  }
  engine.history.length = 0;
  engine.t = 0;
  wall.resize();
  staircase.resize();
}

const tooltip = document.getElementById("tooltip");

function loop() {
  engine.step(6);
  audio.tick(engine);
  wall.draw();
  staircase.draw();

  const op = engine.getOrderParameter();
  ui.updateHeader({ r: op.r, clusters: engine.getClusters(0.02) });

  const hover = wall.getHoverInfo();
  if (hover) {
    tooltip.style.display = "block";
    tooltip.style.left = (hover.screenX + 14) + "px";
    tooltip.style.top = (hover.screenY + 14) + "px";
    tooltip.innerHTML =
      `tile #${hover.index}<br>` +
      `bare ω = ${hover.omega.toFixed(3)}<br>` +
      `locked = ${hover.lockedFreq.toFixed(3)}<br>` +
      `≈ ${hover.ratio} (err ${hover.ratioError.toFixed(4)})`;
  } else {
    tooltip.style.display = "none";
  }

  requestAnimationFrame(loop);
}

// Test hook: deterministic stepping for headless e2e (Playwright).
// Tests can call window.__sim.step(2000) to advance simulation
// without depending on requestAnimationFrame timing in CI.
window.__sim = {
  engine,
  step(n) {
    engine.step(n);
  },
  setK(K) {
    ui.setK(K);
  },
  state() {
    const op = engine.getOrderParameter();
    return { r: op.r, psi: op.psi, K: engine.K, clusters: engine.getClusters(0.02) };
  },
};

loop();
