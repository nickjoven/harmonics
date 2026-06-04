/* livereload.js — front-end optimization that coincides with
 * preview_server.py's auto-rebuild.
 *
 * When the page is served by preview_server.py, this script
 * polls /preview-version every 2 seconds. When the server's
 * version changes (indicating the watcher detected a source
 * edit and regenerated the graph), the page reloads to show
 * the new state.
 *
 * When the page is served from any other source (static
 * hosting, file://, etc.), the initial fetch returns 404 or
 * fails, the script silently disables itself, and the page
 * behaves exactly as before. Zero overhead when not in
 * preview-server context.
 *
 * Include via <script src="livereload.js"></script> at the
 * bottom of pages that should support live reload.
 */
(() => {
  "use strict";

  const POLL_INTERVAL_MS = 2000;
  const VERSION_ENDPOINT = "/preview-version";
  const BANNER_ID = "livereload-banner";

  let currentVersion = null;
  let active = false;

  function showBanner(text, color = "#40c060") {
    let banner = document.getElementById(BANNER_ID);
    if (!banner) {
      banner = document.createElement("div");
      banner.id = BANNER_ID;
      banner.style.cssText = [
        "position: fixed",
        "bottom: 0",
        "right: 0",
        "padding: 4px 12px",
        "font: 11px ui-monospace, monospace",
        "background: #1a1a2e",
        "border-top-left-radius: 4px",
        "border: 1px solid #333",
        "border-bottom: none",
        "border-right: none",
        "z-index: 9999",
        "pointer-events: none",
      ].join(";");
      document.body.appendChild(banner);
    }
    banner.textContent = text;
    banner.style.color = color;
  }

  async function fetchVersion() {
    try {
      const res = await fetch(VERSION_ENDPOINT, { cache: "no-store" });
      if (!res.ok) return null;
      const data = await res.json();
      return data.version || null;
    } catch (e) {
      return null;
    }
  }

  async function init() {
    const initial = await fetchVersion();
    if (initial === null) {
      // Endpoint not available — not running under preview_server.
      // Disable silently.
      return;
    }
    currentVersion = initial;
    active = true;
    showBanner(`livereload active · v${initial.slice(-4)}`);
    setInterval(check, POLL_INTERVAL_MS);
  }

  async function check() {
    if (!active) return;
    const v = await fetchVersion();
    if (v === null) {
      // Server went away; stop polling.
      active = false;
      showBanner("livereload disconnected", "#e94560");
      return;
    }
    if (v !== currentVersion) {
      showBanner(`reloading · v${v.slice(-4)}`, "#f0c040");
      setTimeout(() => window.location.reload(), 200);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
