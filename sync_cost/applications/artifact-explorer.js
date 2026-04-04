/**
 * Artifact Explorer — unobtrusive, interactive overlay for exploring
 * the mathematical artifacts of the synchronization-cost framework.
 *
 * Usage: include artifacts.js then this file.  Call:
 *   ArtifactExplorer.init("page_id")
 *
 * Configuration (all optional, via ArtifactExplorer.init(pageId, opts)):
 *   trigger      "click" | "hover"   (default "click")
 *   position     "bottom-right" | "bottom-left" | "top-right" | "top-left"
 *   startOpen    boolean (default false)
 *
 * Requires: HARMONICS_ARTIFACTS, HARMONICS_PAGES (from artifacts.js)
 */

/* global HARMONICS_ARTIFACTS, HARMONICS_PAGES, window, document */
(function (root) {
  "use strict";

  // ── Helpers ──────────────────────────────────────────────────────

  function el(tag, attrs, children) {
    var e = document.createElement(tag);
    if (attrs) {
      for (var k in attrs) {
        if (k === "style" && typeof attrs[k] === "object") {
          for (var s in attrs[k]) e.style[s] = attrs[k][s];
        } else if (k === "className") {
          e.className = attrs[k];
        } else if (k.slice(0, 2) === "on") {
          e.addEventListener(k.slice(2).toLowerCase(), attrs[k]);
        } else {
          e.setAttribute(k, attrs[k]);
        }
      }
    }
    if (children) {
      if (!Array.isArray(children)) children = [children];
      for (var i = 0; i < children.length; i++) {
        var c = children[i];
        if (typeof c === "string") c = document.createTextNode(c);
        if (c) e.appendChild(c);
      }
    }
    return e;
  }

  // ── Graph layout (simple force-directed, runs synchronously) ────

  function layoutGraph(nodeIds, edges, width, height) {
    var nodes = {};
    var i, j, n, m, dx, dy, dist, force, ex, ey;

    // Seed positions in a circle
    for (i = 0; i < nodeIds.length; i++) {
      var angle = (i / nodeIds.length) * Math.PI * 2;
      nodes[nodeIds[i]] = {
        x: width / 2 + Math.cos(angle) * width * 0.3,
        y: height / 2 + Math.sin(angle) * height * 0.3,
        vx: 0,
        vy: 0
      };
    }

    // Iterate
    var iterations = 120;
    var repulsion = 2000;
    var attraction = 0.01;
    var damping = 0.85;
    var centerPull = 0.002;

    for (var iter = 0; iter < iterations; iter++) {
      // Repulsion between all pairs
      for (i = 0; i < nodeIds.length; i++) {
        n = nodes[nodeIds[i]];
        for (j = i + 1; j < nodeIds.length; j++) {
          m = nodes[nodeIds[j]];
          dx = n.x - m.x;
          dy = n.y - m.y;
          dist = Math.sqrt(dx * dx + dy * dy) || 1;
          force = repulsion / (dist * dist);
          ex = (dx / dist) * force;
          ey = (dy / dist) * force;
          n.vx += ex;
          n.vy += ey;
          m.vx -= ex;
          m.vy -= ey;
        }
      }

      // Attraction along edges
      for (i = 0; i < edges.length; i++) {
        var a = nodes[edges[i][0]];
        var b = nodes[edges[i][1]];
        if (!a || !b) continue;
        dx = b.x - a.x;
        dy = b.y - a.y;
        dist = Math.sqrt(dx * dx + dy * dy) || 1;
        force = dist * attraction;
        a.vx += (dx / dist) * force;
        a.vy += (dy / dist) * force;
        b.vx -= (dx / dist) * force;
        b.vy -= (dy / dist) * force;
      }

      // Center pull + update
      for (i = 0; i < nodeIds.length; i++) {
        n = nodes[nodeIds[i]];
        n.vx += (width / 2 - n.x) * centerPull;
        n.vy += (height / 2 - n.y) * centerPull;
        n.vx *= damping;
        n.vy *= damping;
        n.x += n.vx;
        n.y += n.vy;
        // Clamp
        n.x = Math.max(30, Math.min(width - 30, n.x));
        n.y = Math.max(18, Math.min(height - 18, n.y));
      }
    }

    return nodes;
  }

  // ── Main module ─────────────────────────────────────────────────

  var Explorer = {};
  var _pageId = null;
  var _opts = {};
  var _panelEl = null;
  var _toggleEl = null;
  var _graphCanvas = null;
  var _open = false;
  var _selected = null;
  var _tab = "list"; // "list" | "graph"
  var _graphPositions = null;
  var _graphNodeIds = null;
  var _graphEdges = null;
  var _hoveredGraphNode = null;
  var _dragNode = null;
  var _dragOffsetX = 0;
  var _dragOffsetY = 0;

  function getPageArtifacts() {
    var page = HARMONICS_PAGES[_pageId];
    if (!page) return [];
    return page.primary.map(function (id) {
      return HARMONICS_ARTIFACTS[id];
    }).filter(Boolean);
  }

  function getAllReachable(startIds) {
    var visited = {};
    var queue = startIds.slice();
    while (queue.length) {
      var id = queue.shift();
      if (visited[id]) continue;
      visited[id] = true;
      var a = HARMONICS_ARTIFACTS[id];
      if (a && a.refs) {
        for (var i = 0; i < a.refs.length; i++) {
          if (!visited[a.refs[i]]) queue.push(a.refs[i]);
        }
      }
    }
    return Object.keys(visited);
  }

  function buildGraphData() {
    var page = HARMONICS_PAGES[_pageId];
    if (!page) return;
    _graphNodeIds = getAllReachable(page.primary);
    _graphEdges = [];
    for (var i = 0; i < _graphNodeIds.length; i++) {
      var a = HARMONICS_ARTIFACTS[_graphNodeIds[i]];
      if (!a || !a.refs) continue;
      for (var j = 0; j < a.refs.length; j++) {
        if (_graphNodeIds.indexOf(a.refs[j]) >= 0) {
          _graphEdges.push([a.refs[j], a.id]); // from dependency to dependent
        }
      }
    }
  }

  // ── Inject styles ───────────────────────────────────────────────

  function injectStyles() {
    if (document.getElementById("artifact-explorer-styles")) return;
    var css =
      "#ae-toggle{" +
        "position:fixed;z-index:10000;width:36px;height:36px;" +
        "background:rgba(30,30,40,0.75);border:1px solid #333;border-radius:50%;" +
        "color:#667;font-size:16px;cursor:pointer;display:flex;align-items:center;" +
        "justify-content:center;transition:all 0.25s;backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);" +
        "font-family:'Courier New',monospace;line-height:1;" +
      "}" +
      "#ae-toggle:hover{color:#aab;border-color:#667;background:rgba(40,40,55,0.9);}" +
      "#ae-toggle.open{color:#99aacc;border-color:#556;}" +
      "#ae-panel{" +
        "position:fixed;z-index:9999;width:340px;max-height:70vh;" +
        "background:rgba(12,12,18,0.92);border:1px solid #222;border-radius:6px;" +
        "backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);" +
        "font-family:'Courier New',Courier,monospace;font-size:11px;color:#889;" +
        "overflow:hidden;display:flex;flex-direction:column;" +
        "box-shadow:0 4px 24px rgba(0,0,0,0.5);" +
        "transition:opacity 0.2s,transform 0.2s;" +
      "}" +
      "#ae-panel.hidden{opacity:0;pointer-events:none;transform:translateY(8px);}" +
      "#ae-tabs{display:flex;border-bottom:1px solid #1a1a22;}" +
      "#ae-tabs button{" +
        "flex:1;background:none;border:none;color:#556;padding:7px 0;cursor:pointer;" +
        "font-family:inherit;font-size:10px;letter-spacing:0.08em;text-transform:uppercase;" +
        "border-bottom:2px solid transparent;transition:all 0.15s;" +
      "}" +
      "#ae-tabs button:hover{color:#889;}" +
      "#ae-tabs button.active{color:#99aacc;border-bottom-color:#4466aa;}" +
      "#ae-list{overflow-y:auto;max-height:calc(70vh - 36px);padding:4px 0;}" +
      "#ae-list .ae-item{" +
        "padding:6px 12px;cursor:pointer;border-left:2px solid transparent;" +
        "transition:all 0.12s;" +
      "}" +
      "#ae-list .ae-item:hover{background:rgba(255,255,255,0.03);border-left-color:#334;}" +
      "#ae-list .ae-item.selected{background:rgba(68,102,170,0.08);border-left-color:#4466aa;}" +
      "#ae-list .ae-name{color:#aabbdd;font-size:12px;}" +
      "#ae-list .ae-symbol{color:#556;margin-left:6px;}" +
      "#ae-detail{padding:10px 12px;border-top:1px solid #1a1a22;}" +
      "#ae-detail .ae-formal{color:#7788bb;margin:4px 0;line-height:1.5;}" +
      "#ae-detail .ae-desc{color:#778;margin:6px 0;line-height:1.5;}" +
      "#ae-detail .ae-refs-title{color:#556;font-size:10px;margin-top:8px;text-transform:uppercase;letter-spacing:0.06em;}" +
      "#ae-detail .ae-ref-link{" +
        "display:inline-block;margin:3px 4px 3px 0;padding:2px 6px;" +
        "background:rgba(68,102,170,0.1);border:1px solid #223;border-radius:3px;" +
        "color:#7799cc;cursor:pointer;font-size:10px;transition:all 0.12s;" +
      "}" +
      "#ae-detail .ae-ref-link:hover{background:rgba(68,102,170,0.2);border-color:#446;}" +
      "#ae-detail .ae-derivation{" +
        "display:inline-block;margin-top:6px;color:#555;font-size:10px;" +
        "text-decoration:none;border-bottom:1px dotted #333;" +
      "}" +
      "#ae-detail .ae-derivation:hover{color:#889;}" +
      "#ae-graph-wrap{position:relative;}" +
      "#ae-graph{display:block;width:100%;cursor:crosshair;}" +
      "#ae-graph-tip{" +
        "position:absolute;pointer-events:none;z-index:2;" +
        "background:rgba(12,12,20,0.95);border:1px solid #334;border-radius:3px;" +
        "padding:4px 8px;font-size:10px;color:#aab;white-space:nowrap;" +
        "display:none;" +
      "}" +
      "#ae-drag-handle{" +
        "height:18px;cursor:move;display:flex;align-items:center;justify-content:center;" +
        "color:#334;font-size:9px;letter-spacing:2px;user-select:none;-webkit-user-select:none;" +
      "}" +
      "#ae-drag-handle:hover{color:#556;}";

    var styleEl = document.createElement("style");
    styleEl.id = "artifact-explorer-styles";
    styleEl.textContent = css;
    document.head.appendChild(styleEl);
  }

  // ── Position helpers ────────────────────────────────────────────

  function applyPosition() {
    var pos = _opts.position || "bottom-right";
    var parts = pos.split("-");
    var vert = parts[0];
    var horiz = parts[1];

    _toggleEl.style.top = vert === "top" ? "12px" : "auto";
    _toggleEl.style.bottom = vert === "bottom" ? "12px" : "auto";
    _toggleEl.style.left = horiz === "left" ? "12px" : "auto";
    _toggleEl.style.right = horiz === "right" ? "12px" : "auto";

    _panelEl.style.top = vert === "top" ? "54px" : "auto";
    _panelEl.style.bottom = vert === "bottom" ? "54px" : "auto";
    _panelEl.style.left = horiz === "left" ? "12px" : "auto";
    _panelEl.style.right = horiz === "right" ? "12px" : "auto";
  }

  // ── Build DOM ───────────────────────────────────────────────────

  function buildUI() {
    // Toggle button
    _toggleEl = el("button", {
      id: "ae-toggle",
      title: "Explore artifacts",
      onClick: function () { toggle(); }
    }, ["\u25c7"]); // ◇

    // Panel
    _panelEl = el("div", { id: "ae-panel", className: "hidden" });

    applyPosition();

    document.body.appendChild(_toggleEl);
    document.body.appendChild(_panelEl);

    renderPanel();
  }

  function renderPanel() {
    _panelEl.innerHTML = "";

    // Drag handle for panel relocation
    var handle = el("div", { id: "ae-drag-handle" }, ["\u2261\u2261\u2261"]);
    var panelDragging = false;
    var panelDragStartX = 0, panelDragStartY = 0;
    var panelStartLeft = 0, panelStartTop = 0;

    handle.addEventListener("mousedown", function (e) {
      panelDragging = true;
      panelDragStartX = e.clientX;
      panelDragStartY = e.clientY;
      var rect = _panelEl.getBoundingClientRect();
      panelStartLeft = rect.left;
      panelStartTop = rect.top;
      // Switch to absolute positioning
      _panelEl.style.right = "auto";
      _panelEl.style.bottom = "auto";
      _panelEl.style.left = panelStartLeft + "px";
      _panelEl.style.top = panelStartTop + "px";
      e.preventDefault();
    });

    function onPanelDrag(e) {
      if (!panelDragging) return;
      var dx = e.clientX - panelDragStartX;
      var dy = e.clientY - panelDragStartY;
      _panelEl.style.left = (panelStartLeft + dx) + "px";
      _panelEl.style.top = (panelStartTop + dy) + "px";
    }
    function onPanelDragEnd() {
      panelDragging = false;
    }
    document.addEventListener("mousemove", onPanelDrag);
    document.addEventListener("mouseup", onPanelDragEnd);
    _panelEl.appendChild(handle);

    // Tabs
    var tabs = el("div", { id: "ae-tabs" });
    var listBtn = el("button", {
      className: _tab === "list" ? "active" : "",
      onClick: function () { _tab = "list"; renderPanel(); }
    }, ["artifacts"]);
    var graphBtn = el("button", {
      className: _tab === "graph" ? "active" : "",
      onClick: function () { _tab = "graph"; renderPanel(); renderGraph(); }
    }, ["graph"]);
    tabs.appendChild(listBtn);
    tabs.appendChild(graphBtn);
    _panelEl.appendChild(tabs);

    if (_tab === "list") {
      renderList();
    } else {
      renderGraphTab();
    }
  }

  function renderList() {
    var listEl = el("div", { id: "ae-list" });
    var arts = getPageArtifacts();

    for (var i = 0; i < arts.length; i++) {
      (function (a) {
        var item = el("div", {
          className: "ae-item" + (_selected === a.id ? " selected" : ""),
          onClick: function () {
            _selected = _selected === a.id ? null : a.id;
            renderPanel();
          }
        }, [
          el("span", { className: "ae-name" }, [a.name]),
          el("span", { className: "ae-symbol" }, [a.symbol])
        ]);
        listEl.appendChild(item);
      })(arts[i]);
    }
    _panelEl.appendChild(listEl);

    // Detail
    if (_selected && HARMONICS_ARTIFACTS[_selected]) {
      renderDetail(HARMONICS_ARTIFACTS[_selected]);
    }
  }

  function renderDetail(a) {
    var detail = el("div", { id: "ae-detail" });
    detail.appendChild(el("div", { className: "ae-formal" }, [a.formal]));
    detail.appendChild(el("div", { className: "ae-desc" }, [a.description]));

    // Refs (what this builds on)
    if (a.refs && a.refs.length > 0) {
      detail.appendChild(el("div", { className: "ae-refs-title" }, ["builds on"]));
      var refsDiv = el("div");
      for (var i = 0; i < a.refs.length; i++) {
        (function (refId) {
          var ref = HARMONICS_ARTIFACTS[refId];
          if (!ref) return;
          refsDiv.appendChild(el("span", {
            className: "ae-ref-link",
            onClick: function () {
              _selected = refId;
              renderPanel();
            }
          }, [ref.name]));
        })(a.refs[i]);
      }
      detail.appendChild(refsDiv);
    }

    // Referenced by (reverse refs)
    var referencedBy = [];
    for (var key in HARMONICS_ARTIFACTS) {
      var other = HARMONICS_ARTIFACTS[key];
      if (other.refs && other.refs.indexOf(a.id) >= 0) {
        referencedBy.push(other);
      }
    }
    if (referencedBy.length > 0) {
      detail.appendChild(el("div", { className: "ae-refs-title" }, ["used by"]));
      var usedDiv = el("div");
      for (var j = 0; j < referencedBy.length; j++) {
        (function (ref) {
          usedDiv.appendChild(el("span", {
            className: "ae-ref-link",
            onClick: function () {
              _selected = ref.id;
              renderPanel();
            }
          }, [ref.name]));
        })(referencedBy[j]);
      }
      detail.appendChild(usedDiv);
    }

    // Derivation link
    if (a.derivation) {
      detail.appendChild(el("a", {
        className: "ae-derivation",
        href: a.derivation,
        target: "_blank"
      }, ["derivation \u2192"]));
    }

    _panelEl.appendChild(detail);
  }

  // ── Graph tab ───────────────────────────────────────────────────

  function renderGraphTab() {
    buildGraphData();
    var wrap = el("div", { id: "ae-graph-wrap" });
    var gw = 336;
    var gh = Math.min(Math.max(_graphNodeIds.length * 26, 200), 400);

    _graphCanvas = el("canvas", {
      id: "ae-graph",
      width: String(gw * 2),
      height: String(gh * 2),
      style: { width: gw + "px", height: gh + "px" }
    });

    var tip = el("div", { id: "ae-graph-tip" });
    wrap.appendChild(_graphCanvas);
    wrap.appendChild(tip);
    _panelEl.appendChild(wrap);

    // ── Mouse / touch interaction: hover, click, drag-to-relocate ──

    function canvasCoords(e) {
      var rect = _graphCanvas.getBoundingClientRect();
      var clientX, clientY;
      if (e.touches && e.touches.length) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      } else {
        clientX = e.clientX;
        clientY = e.clientY;
      }
      return {
        cx: (clientX - rect.left) * 2, // canvas coords (2x for retina)
        cy: (clientY - rect.top) * 2,
        px: clientX - rect.left,        // CSS coords (for tooltip)
        py: clientY - rect.top
      };
    }

    function hitTest(mx, my) {
      if (!_graphPositions) return null;
      for (var i = 0; i < _graphNodeIds.length; i++) {
        var p = _graphPositions[_graphNodeIds[i]];
        var dx = p.x - mx;
        var dy = p.y - my;
        if (dx * dx + dy * dy < 22 * 22) return _graphNodeIds[i];
      }
      return null;
    }

    _graphCanvas.addEventListener("mousemove", function (e) {
      var c = canvasCoords(e);

      if (_dragNode && _graphPositions[_dragNode]) {
        // Relocate the dragged node
        _graphPositions[_dragNode].x = c.cx;
        _graphPositions[_dragNode].y = c.cy;
        tip.style.display = "none";
        _graphCanvas.style.cursor = "grabbing";
        renderGraph();
        return;
      }

      _hoveredGraphNode = hitTest(c.cx, c.cy);

      if (_hoveredGraphNode) {
        var a = HARMONICS_ARTIFACTS[_hoveredGraphNode];
        tip.textContent = a ? a.name + " \u2014 " + a.symbol : _hoveredGraphNode;
        tip.style.display = "block";
        tip.style.left = (c.px + 12) + "px";
        tip.style.top = (c.py - 20) + "px";
        _graphCanvas.style.cursor = "grab";
      } else {
        tip.style.display = "none";
        _graphCanvas.style.cursor = "crosshair";
      }
      renderGraph();
    });

    _graphCanvas.addEventListener("mousedown", function (e) {
      var c = canvasCoords(e);
      var hit = hitTest(c.cx, c.cy);
      if (hit && _graphPositions[hit]) {
        _dragNode = hit;
        _dragOffsetX = _graphPositions[hit].x - c.cx;
        _dragOffsetY = _graphPositions[hit].y - c.cy;
        _graphCanvas.style.cursor = "grabbing";
        e.preventDefault();
      }
    });

    _graphCanvas.addEventListener("mouseup", function (e) {
      if (_dragNode) {
        // If barely moved, treat as click -> select
        _dragNode = null;
        _graphCanvas.style.cursor = _hoveredGraphNode ? "grab" : "crosshair";
      }
    });

    _graphCanvas.addEventListener("click", function (e) {
      if (_hoveredGraphNode) {
        _selected = _hoveredGraphNode;
        _tab = "list";
        renderPanel();
      }
    });

    _graphCanvas.addEventListener("mouseleave", function () {
      _dragNode = null;
      _hoveredGraphNode = null;
      tip.style.display = "none";
      renderGraph();
    });

    // Touch support for drag-to-relocate
    _graphCanvas.addEventListener("touchstart", function (e) {
      var c = canvasCoords(e);
      var hit = hitTest(c.cx, c.cy);
      if (hit && _graphPositions[hit]) {
        _dragNode = hit;
        _dragOffsetX = _graphPositions[hit].x - c.cx;
        _dragOffsetY = _graphPositions[hit].y - c.cy;
        e.preventDefault();
      }
    }, { passive: false });

    _graphCanvas.addEventListener("touchmove", function (e) {
      if (_dragNode && _graphPositions[_dragNode]) {
        var c = canvasCoords(e);
        _graphPositions[_dragNode].x = c.cx;
        _graphPositions[_dragNode].y = c.cy;
        renderGraph();
        e.preventDefault();
      }
    }, { passive: false });

    _graphCanvas.addEventListener("touchend", function () {
      if (_dragNode) {
        _selected = _dragNode;
        _dragNode = null;
        _tab = "list";
        renderPanel();
      }
    });
  }

  function renderGraph() {
    if (!_graphCanvas || !_graphNodeIds) return;
    var cvs = _graphCanvas;
    var ctx = cvs.getContext("2d");
    var w = cvs.width;
    var h = cvs.height;

    ctx.clearRect(0, 0, w, h);

    // Layout
    _graphPositions = layoutGraph(_graphNodeIds, _graphEdges, w, h);

    var page = HARMONICS_PAGES[_pageId];
    var primarySet = {};
    if (page) {
      for (var pi = 0; pi < page.primary.length; pi++) {
        primarySet[page.primary[pi]] = true;
      }
    }

    // Draw edges with arrows
    ctx.lineWidth = 1.5;
    for (var i = 0; i < _graphEdges.length; i++) {
      var fromId = _graphEdges[i][0];
      var toId = _graphEdges[i][1];
      var from = _graphPositions[fromId];
      var to = _graphPositions[toId];
      if (!from || !to) continue;

      var isHighlight = (_hoveredGraphNode === fromId || _hoveredGraphNode === toId);
      ctx.strokeStyle = isHighlight ? "rgba(100,130,200,0.7)" : "rgba(60,70,100,0.35)";
      ctx.lineWidth = isHighlight ? 2 : 1;

      ctx.beginPath();
      ctx.moveTo(from.x, from.y);
      ctx.lineTo(to.x, to.y);
      ctx.stroke();

      // Arrowhead
      var dx = to.x - from.x;
      var dy = to.y - from.y;
      var dist = Math.sqrt(dx * dx + dy * dy) || 1;
      var ux = dx / dist;
      var uy = dy / dist;
      var arrowLen = 8;
      var ax = to.x - ux * 14;
      var ay = to.y - uy * 14;
      ctx.fillStyle = ctx.strokeStyle;
      ctx.beginPath();
      ctx.moveTo(to.x - ux * 12, to.y - uy * 12);
      ctx.lineTo(ax - uy * arrowLen * 0.4, ay + ux * arrowLen * 0.4);
      ctx.lineTo(ax + uy * arrowLen * 0.4, ay - ux * arrowLen * 0.4);
      ctx.closePath();
      ctx.fill();
    }

    // Draw nodes
    for (i = 0; i < _graphNodeIds.length; i++) {
      var nid = _graphNodeIds[i];
      var pos = _graphPositions[nid];
      var isPrimary = primarySet[nid];
      var isHovered = _hoveredGraphNode === nid;
      var isSelected = _selected === nid;
      var a = HARMONICS_ARTIFACTS[nid];

      var radius = isPrimary ? 10 : 7;
      if (isHovered) radius += 3;

      // Glow
      if (isHovered || isSelected) {
        var grad = ctx.createRadialGradient(pos.x, pos.y, 0, pos.x, pos.y, radius * 3);
        grad.addColorStop(0, isSelected ? "rgba(100,130,200,0.25)" : "rgba(100,130,200,0.15)");
        grad.addColorStop(1, "rgba(0,0,0,0)");
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, radius * 3, 0, Math.PI * 2);
        ctx.fill();
      }

      // Node circle
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, radius, 0, Math.PI * 2);
      ctx.fillStyle = isHovered
        ? "rgba(120,150,220,0.9)"
        : isSelected
          ? "rgba(100,130,200,0.8)"
          : isPrimary
            ? "rgba(80,110,180,0.7)"
            : "rgba(60,70,100,0.5)";
      ctx.fill();

      ctx.strokeStyle = isHovered ? "rgba(150,180,255,0.6)" : "rgba(80,90,120,0.3)";
      ctx.lineWidth = 1;
      ctx.stroke();

      // Label
      ctx.font = (isPrimary ? "bold " : "") + "16px 'Courier New', monospace";
      ctx.fillStyle = isHovered
        ? "rgba(200,210,240,0.95)"
        : isPrimary
          ? "rgba(160,170,200,0.8)"
          : "rgba(120,130,160,0.55)";
      ctx.textAlign = "center";
      ctx.textBaseline = "top";
      var label = a ? a.name : nid;
      // Truncate long names
      if (label.length > 16) label = label.slice(0, 14) + "\u2026";
      ctx.fillText(label, pos.x, pos.y + radius + 4);
    }
  }

  // ── Toggle ──────────────────────────────────────────────────────

  function toggle() {
    _open = !_open;
    _panelEl.classList.toggle("hidden", !_open);
    _toggleEl.classList.toggle("open", _open);
    if (_open && _tab === "graph") {
      renderGraph();
    }
  }

  // ── Keyboard shortcut ───────────────────────────────────────────

  function onKey(e) {
    // "?" to toggle, Escape to close
    if (e.key === "?" && !e.ctrlKey && !e.metaKey && !e.altKey) {
      var tag = (e.target.tagName || "").toLowerCase();
      if (tag === "input" || tag === "textarea" || tag === "select") return;
      e.preventDefault();
      toggle();
    }
    if (e.key === "Escape" && _open) {
      toggle();
    }
  }

  // ── Public API ──────────────────────────────────────────────────

  Explorer.init = function (pageId, opts) {
    if (!HARMONICS_ARTIFACTS || !HARMONICS_PAGES) {
      console.warn("ArtifactExplorer: artifacts.js must be loaded first.");
      return;
    }
    _pageId = pageId;
    _opts = opts || {};
    if (_opts.startOpen) _open = true;

    injectStyles();
    buildUI();

    if (_opts.startOpen) {
      _panelEl.classList.remove("hidden");
      _toggleEl.classList.add("open");
    }

    document.addEventListener("keydown", onKey);
  };

  root.ArtifactExplorer = Explorer;

})(typeof window !== "undefined" ? window : this);
