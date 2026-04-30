// Quick node smoke test: run CircleMapEngine.tongueWidth at K=0.99, p/q=1/2
// and compare to the reference value 0.07259291744413632.

import { CircleMapEngine } from "../src/engine.js";
import { readFileSync } from "fs";

const ref = JSON.parse(readFileSync(new URL("./reference_widths.json", import.meta.url), "utf8"));

let pass = 0, fail = 0, trivial = 0;
const t0 = Date.now();

for (const [p, q] of ref.pq_values) {
  const label = `${p}/${q}`;
  for (const K of ref.K_values) {
    const expected = ref.widths[String(K)][label];
    const measured = CircleMapEngine.tongueWidth(p, q, K);
    let verdict;
    if (expected === 0) {
      verdict = measured <= ref.tolerances.absolute_below ? "trivial" : "fail";
    } else if (expected < ref.tolerances.absolute_below) {
      verdict = Math.abs(measured - expected) <= ref.tolerances.absolute ? "pass" : "fail";
    } else {
      const rel = Math.abs(measured - expected) / expected;
      verdict = rel <= ref.tolerances.relative ? "pass" : "fail";
    }
    if (verdict === "pass") pass++;
    else if (verdict === "fail") fail++;
    else trivial++;
    if (verdict === "fail") {
      console.log(`FAIL  K=${K} ${label}: ref=${expected.toFixed(6)} js=${measured.toFixed(6)}`);
    }
  }
}

const dt = ((Date.now() - t0) / 1000).toFixed(1);
console.log(`\nTotal: ${pass} non-trivial pass · ${trivial} trivial · ${fail} fail · ${dt}s`);
process.exit(fail === 0 ? 0 : 1);
