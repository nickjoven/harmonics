// Empirically probe |r| at each K for two candidate normalizations.

import { KuramotoEngine, uniformFrequencies } from "../src/engine.js";

const N = 100;
const TWO_PI = Math.PI * 2;

function probe(K, omegaTransform, simulatedTimeSeconds = 60) {
  const omegas = Float64Array.from(uniformFrequencies(N, 0, 1, 1), omegaTransform);
  const engine = new KuramotoEngine({ N, omegas, K, dt: 0.05, seed: 1, historySize: 600 });
  const totalSteps = Math.floor(simulatedTimeSeconds / engine.dt);
  engine.step(totalSteps);
  return engine.getOrderParameter().r;
}

console.log("\nA) Current normalization: ω = 2π·x, x ∈ [0,1]");
console.log("   Δω = 2π ≈ 6.28; predicted K_c = 2·Δω/π = 4");
for (const K of [0, 0.637, 1.0, 2.0, 4.0, 6.0]) {
  console.log(`   K=${K.toFixed(3)}  |r|=${probe(K, x => TWO_PI * x).toFixed(3)}`);
}

console.log("\nB) Cycle-rate normalization: ω = x, x ∈ [0,1]");
console.log("   Δω = 1; predicted K_c = 2/π ≈ 0.637");
for (const K of [0, 0.3, 0.637, 0.85, 1.0, 1.3]) {
  console.log(`   K=${K.toFixed(3)}  |r|=${probe(K, x => x).toFixed(3)}`);
}
