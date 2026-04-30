// Visual-regression tests for the metronome wall prototype.
//
// Captures pixel-stable screenshots of the staircase and wall canvases at
// four canonical K values and asserts against committed baselines. The
// baselines are platform-stable (Linux Chromium); see
// .github/workflows/update-visual-baselines.yml for regenerating them.
//
// First-run note: if baselines are not yet committed, this spec will fail.
// Run the update-visual-baselines workflow once to seed them.

import { test, expect } from "@playwright/test";

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

for (const { name, K, label } of presets) {
  test.describe(`Visual: ${label}`, () => {
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
