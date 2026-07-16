/* nav.js — render the site nav from nav.json (the single source of truth).
 *
 * Usage on any docs page:
 *   <nav data-site-nav><a href="index.html">Reference</a></nav>
 *   <script src="nav.js" defer></script>
 *
 * The placeholder's fallback content is replaced once nav.json loads;
 * without JS (or if the fetch fails) the fallback link still works.
 * Styles are scoped under [data-site-nav] and lean on style.css tokens
 * where present, with literal fallbacks so unstyled pages (genesis,
 * framework_predictions) render identically.
 */
(function () {
  "use strict";

  var css = [
    "nav[data-site-nav] { display: flex; flex-wrap: wrap; align-items: baseline;",
    "  gap: 0.4em 1.6em; margin-bottom: 2.5em; padding-bottom: 1em;",
    "  border-bottom: 1px solid var(--border, #333);",
    "  font-size: 0.9em; letter-spacing: 0.04em; }",
    "nav[data-site-nav] .nav-group { display: inline-flex; align-items: baseline;",
    "  gap: 0 1.1em; }",
    "nav[data-site-nav] .nav-group + .nav-group { margin-left: 0.6em;",
    "  padding-left: 1.6em; border-left: 1px solid var(--border, #333); }",
    "nav[data-site-nav] .nav-label { font-size: 0.78em; text-transform: uppercase;",
    "  letter-spacing: 0.14em; color: var(--text-dim, #888); margin-right: 0.3em; }",
    "nav[data-site-nav] a { border-bottom: none; text-decoration: none;",
    "  color: var(--text-dim, #888); }",
    "nav[data-site-nav] a:hover, nav[data-site-nav] a.active {",
    "  color: var(--text-bright, #eee); }",
    "nav[data-site-nav] a.active { border-bottom: 1px solid var(--accent, #7aa2f7); }",
  ].join("\n");

  function here(href, base) {
    var target = new URL(href, base).pathname;
    return target === location.pathname ||
      (target.endsWith("/index.html") &&
       target.replace(/index\.html$/, "") === location.pathname);
  }

  function link(item, base) {
    var a = document.createElement("a");
    a.href = item.href;
    a.textContent = item.title;
    if (here(item.href, base)) a.className = "active";
    return a;
  }

  function render(nav, data) {
    var base = document.currentScript ? document.currentScript.src : location.href;
    nav.textContent = "";
    var home = document.createElement("span");
    home.className = "nav-group";
    home.appendChild(link(data.home, base));
    nav.appendChild(home);
    data.groups.forEach(function (group) {
      var span = document.createElement("span");
      span.className = "nav-group";
      var label = document.createElement("span");
      label.className = "nav-label";
      label.textContent = group.label;
      span.appendChild(label);
      group.items.forEach(function (item) {
        span.appendChild(link(item, base));
      });
      nav.appendChild(span);
    });
  }

  var nav = document.querySelector("nav[data-site-nav]");
  if (!nav) return;

  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  var script = document.currentScript;
  var jsonUrl = new URL("nav.json", script ? script.src : location.href);
  fetch(jsonUrl)
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) { render(nav, data); })
    .catch(function () { /* fallback content stays */ });
})();
