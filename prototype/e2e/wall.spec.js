// End-to-end smoke tests for the metronome wall prototype.
//
// Tests use the window.__sim test hook (defined in src/main.js) to advance
// the simulation deterministically, decoupling assertions from rAF timing
// in CI environments.

import { test, expect } from "@playwright/test";

const STEPS_LONG = 6000;   // long enough for K = K_c to settle
const STEPS_SETTLED = 9000; // long enough for K = 1 saturation

const drive = async (page, K, steps = STEPS_LONG) => {
  await page.evaluate(([k, n]) => {
    window.__sim.setK(k);
    window.__sim.engine.reset();
    window.__sim.step(n);
  }, [K, steps]);
};

const state = async (page) => page.evaluate(() => window.__sim.state());

test.describe("Metronome wall", () => {
  test("page loads with all panels and controls", async ({ page }) => {
    await page.goto("/");
    await expect(page.locator("#wall canvas")).toBeVisible();
    await expect(page.locator("#staircase canvas")).toBeVisible();
    await expect(page.locator("#k-slider")).toBeVisible();
    await expect(page.locator("#dist-select")).toBeVisible();
    await expect(page.locator("#audio-toggle")).toBeVisible();
    // Test hook is exposed.
    const ok = await page.evaluate(() => typeof window.__sim?.step === "function");
    expect(ok).toBe(true);
  });

  test("K = 0 leaves the system disordered", async ({ page }) => {
    await page.goto("/");
    await drive(page, 0, STEPS_LONG);
    const s = await state(page);
    // |r| should stay close to its 1/sqrt(N) noise floor at K = 0.
    expect(s.r).toBeLessThan(0.30);
  });

  test("K = K_c crosses the synchronization threshold", async ({ page }) => {
    await page.goto("/");
    await drive(page, 2 / Math.PI, STEPS_LONG);
    const s = await state(page);
    // For uniform g(ω) on width 1, K_c = 2/π. Past threshold |r| > 0.4.
    expect(s.r).toBeGreaterThan(0.4);
  });

  test("K = 1 saturates |r| above 0.85", async ({ page }) => {
    await page.goto("/");
    await drive(page, 1.0, STEPS_SETTLED);
    const s = await state(page);
    expect(s.r).toBeGreaterThan(0.85);
    expect(s.clusters).toBeLessThan(20);
  });

  test("K is monotonic in |r| past threshold", async ({ page }) => {
    await page.goto("/");
    await drive(page, 0.0, STEPS_LONG);
    const r0 = (await state(page)).r;
    await drive(page, 2 / Math.PI, STEPS_LONG);
    const rc = (await state(page)).r;
    await drive(page, 1.0, STEPS_SETTLED);
    const r1 = (await state(page)).r;
    expect(rc).toBeGreaterThan(r0);
    expect(r1).toBeGreaterThan(rc);
  });

  test("slider updates the K readout", async ({ page }) => {
    await page.goto("/");
    await page.locator("#k-slider").evaluate((el, v) => {
      el.value = String(v);
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, 0.812);
    await page.waitForTimeout(50);
    const k = parseFloat(await page.locator("#k-readout").textContent());
    expect(k).toBeCloseTo(0.812, 2);
  });

  test("staircase canvas paints non-empty content at K = 1", async ({ page }) => {
    await page.goto("/");
    await drive(page, 1.0, STEPS_SETTLED);
    // Allow one rAF tick for the canvas to repaint after stepping.
    await page.waitForTimeout(120);

    const variance = await page.locator("#staircase canvas").evaluate((c) => {
      const ctx = c.getContext("2d");
      const { data } = ctx.getImageData(0, 0, c.width, c.height);
      let sum = 0, sumSq = 0, n = 0;
      for (let i = 0; i < data.length; i += 4) {
        const v = (data[i] + data[i + 1] + data[i + 2]) / 3;
        sum += v;
        sumSq += v * v;
        n++;
      }
      const mean = sum / n;
      return sumSq / n - mean * mean;
    });
    expect(variance).toBeGreaterThan(20);
  });
});

test.describe("Validation harness", () => {
  test("tongue_widths page reports zero failures", async ({ page }) => {
    await page.goto("/test/tongue_widths.html");
    await expect(page.locator("#summary")).toContainText(/0 fail/, {
      timeout: 90_000,
    });
    await expect(page.locator("#summary")).not.toHaveClass(/summary-fail/);
  });
});
