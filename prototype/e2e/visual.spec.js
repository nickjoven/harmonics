// Visual-regression tests for the metronome wall prototype.
//
// Captures pixel-stable screenshots of the staircase and wall canvases at
// four canonical K values and asserts against committed baselines. The
// baselines are platform-stable (Linux Chromium); see
// .github/workflows/update-visual-baselines.yml for regenerating them.
//
// Self-gating: if no baselines are committed yet, the entire spec is
// skipped — so regular CI stays green until the update-visual-baselines
// workflow has run once and seeded baselines. The seeder workflow sets
// FORCE_VISUAL=1 to override the skip and actually capture baselines.

import { test, expect } from "@playwright/test";
import { existsSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SNAPSHOT_DIR = join(__dirname, "visual.spec.js-snapshots");
const HAS_BASELINES = existsSync(SNAPSHOT_DIR);
const FORCE = process.env.FORCE_VISUAL === "1";
const SHOULD_RUN = HAS_BASELINES || FORCE;

const drive = async (page, K, steps = 9000) => {
  await page.evaluate(([k, n]) => {
    window.__sim.setK(k);
    window.__sim.engine.reset();
    window.__sim.step(n);
  }, [K, steps]);
  // Allow one rAF tick for the canvas to repaint after stepping.
  await page.waitForTimeout(120);
};

const presets = [
  { name: "K0", K: 0, label: "K = 0 (disordered)" },
  { name: "K_subcritical", K: 0.3, label: "K = 0.3 (subcritical)" },
  { name: "K_c", K: 2 / Math.PI, label: "K = K_c = 2/π" },
  { name: "K1", K: 1.0, label: "K = 1 (saturated)" },
];

const group = SHOULD_RUN ? test.describe : test.describe.skip;

for (const { name, K, label } of presets) {
  group(`Visual: ${label}`, () => {
    test(`staircase at ${name}`, async ({ page }) => {
      await page.goto("/");
      await drive(page, K);
      await expect(page.locator("#staircase canvas")).toHaveScreenshot(
        `staircase-${name}.png`,
        { maxDiffPixelRatio: 0.05 }
      );
    });

    test(`wall at ${name}`, async ({ page }) => {
      await page.goto("/");
      await drive(page, K);
      await expect(page.locator("#wall canvas")).toHaveScreenshot(
        `wall-${name}.png`,
        { maxDiffPixelRatio: 0.10 }
      );
    });
  });
}
