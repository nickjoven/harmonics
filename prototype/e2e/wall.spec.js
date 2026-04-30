// End-to-end smoke tests for the metronome wall prototype.
// Each test asserts a structural claim that should hold regardless of
// rendering details: K=0 stays disordered, K_c shows first cluster,
// K=0.99 produces high |r| and a mostly-locked wall.

import { test, expect } from "@playwright/test";

const settle = async (page, ms = 2500) => {
  // Wait for several Kuramoto integration windows so locked-frequency
  // averages stabilize.
  await page.waitForTimeout(ms);
};

const readNumber = async (page, selector) => {
  const text = (await page.locator(selector).textContent()).trim();
  return parseFloat(text);
};

test.describe("Metronome wall", () => {
  test("page loads with all panels and controls", async ({ page }) => {
    await page.goto("/");
    await expect(page.locator("#wall canvas")).toBeVisible();
    await expect(page.locator("#staircase canvas")).toBeVisible();
    await expect(page.locator("#k-slider")).toBeVisible();
    await expect(page.locator("#dist-select")).toBeVisible();
    await expect(page.locator("#audio-toggle")).toBeVisible();
  });

  test("K = 0 leaves the system disordered", async ({ page }) => {
    await page.goto("/");
    await page.locator("button[data-preset=K0]").click();
    await settle(page, 3000);
    const r = await readNumber(page, "#r-readout");
    // |r| should stay low (noise-floor) at K = 0 with N = 100.
    expect(r).toBeLessThan(0.35);
  });

  test("K = K_c forms a visible cluster", async ({ page }) => {
    await page.goto("/");
    await page.locator("button[data-preset=Kc]").click();
    await settle(page, 4000);
    const r = await readNumber(page, "#r-readout");
    // Above threshold |r| grows; conservative lower bound.
    expect(r).toBeGreaterThan(0.25);
  });

  test("K = 1 locks the wall and saturates |r|", async ({ page }) => {
    await page.goto("/");
    await page.locator("button[data-preset=K1]").click();
    await settle(page, 5000);
    const r = await readNumber(page, "#r-readout");
    expect(r).toBeGreaterThan(0.85);
    const clusters = await readNumber(page, "#cluster-readout");
    expect(clusters).toBeLessThan(15);
  });

  test("slider updates the readout", async ({ page }) => {
    await page.goto("/");
    await page.locator("#k-slider").evaluate((el, v) => {
      el.value = String(v);
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, 0.812);
    const k = await readNumber(page, "#k-readout");
    expect(k).toBeCloseTo(0.812, 2);
  });

  test("staircase canvas paints non-empty content at K=0.99", async ({ page }) => {
    await page.goto("/");
    await page.locator("#k-slider").evaluate((el, v) => {
      el.value = String(v);
      el.dispatchEvent(new Event("input", { bubbles: true }));
    }, 0.99);
    await settle(page, 5000);

    // Sample the staircase canvas pixel buffer; a rendered plot has
    // non-trivial chroma variance.
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
    // Harness runs a tight numeric loop in JS; give it generous time.
    await expect(page.locator("#summary")).toContainText(/0 fail/, {
      timeout: 90_000,
    });
    await expect(page.locator("#summary")).not.toHaveClass(/summary-fail/);
  });
});
