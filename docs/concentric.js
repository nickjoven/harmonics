/*
 * Concentric view — Harmonics
 *
 * Renders a hand-laid polar layout:
 *   - center : the wave-outward root + three ingredients
 *   - R_OBS  : six observations (two gold "walls" diametrically opposed)
 *   - R_FW   : framework nodes pulled from derivation-graph.json,
 *              clustered angularly near the observation they speak to.
 *
 * The info panel updates on hover/click. Framework nodes link to their
 * source markdown on GitHub.
 */

const SVG_NS = 'http://www.w3.org/2000/svg';

const R_ING   = 75;    // ingredient ring (around wave root)
const R_OBS   = 200;   // observation ring
const R_FW    = 360;   // framework-node ring
const FW_SPAN = 0.35;  // radians: angular spread per observation's cluster

const GITHUB_BASE = 'https://github.com/nickjoven/harmonics/blob/main/';

// ----- polar → cartesian ---------------------------------------------------

// observation angles use 12-o'clock-relative clockwise convention for legibility,
// converted to standard SVG math-angle (0 = east, ccw positive, y-down → flip).
function oclockToRadians(oclock) {
  // 12 o'clock = top = -π/2 ; clockwise.
  return -Math.PI / 2 + (oclock / 12) * 2 * Math.PI;
}

function polar(r, angleRad) {
  return [r * Math.cos(angleRad), r * Math.sin(angleRad)];
}

// ----- DOM helpers ---------------------------------------------------------

function svgEl(tag, attrs = {}, parent = null) {
  const el = document.createElementNS(SVG_NS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    el.setAttribute(k, v);
  }
  if (parent) parent.appendChild(el);
  return el;
}

function setInfo(kind, title, summary, linkPath = null) {
  document.querySelector('.info-kind').textContent = kind;
  document.getElementById('info-title').textContent = title;
  document.getElementById('info-summary').textContent = summary;
  const linkEl = document.getElementById('info-link');
  if (linkPath) {
    linkEl.innerHTML = `<a href="${GITHUB_BASE}${linkPath}" target="_blank" rel="noopener">open source &rarr;</a>`;
  } else {
    linkEl.textContent = '';
  }
}

// ----- main ----------------------------------------------------------------

async function init() {
  const [anchors, graph] = await Promise.all([
    fetch('concentric-anchors.json').then(r => r.json()),
    fetch('derivation-graph.json').then(r => r.json()),
  ]);

  const nodesById = new Map(graph.nodes.map(n => [n.id, n]));
  const svg = document.getElementById('concentric');

  // ---- layer 0: backdrop rings + stability band ------------------------
  const backdrop = svgEl('g', { class: 'cn-backdrop' }, svg);

  // The green "stable band" — a soft rectangle horizontally through center,
  // wide enough to suggest "many decades" between the walls (left/right).
  const bandH = 110;
  svgEl('rect', {
    class: 'cn-band',
    x: -480, y: -bandH / 2, width: 960, height: bandH, rx: 18,
  }, backdrop);
  // band edges
  svgEl('line', {
    class: 'cn-band-edge',
    x1: -480, y1: -bandH / 2, x2: 480, y2: -bandH / 2,
  }, backdrop);
  svgEl('line', {
    class: 'cn-band-edge',
    x1: -480, y1: bandH / 2, x2: 480, y2: bandH / 2,
  }, backdrop);

  // concentric reference rings
  for (const r of [R_ING, R_OBS, R_FW]) {
    svgEl('circle', { class: 'cn-ring', cx: 0, cy: 0, r }, backdrop);
  }

  // ---- layer 1: edges (drawn first so nodes sit on top) ---------------
  const edgeLayer = svgEl('g', { class: 'cn-edges' }, svg);
  const nodeLayer = svgEl('g', { class: 'cn-nodes' }, svg);

  // Place observations by angle
  const obsPositions = new Map();
  for (const obs of anchors.observations) {
    const a = oclockToRadians(obs.angle_oclock);
    obsPositions.set(obs.id, { a, xy: polar(R_OBS, a) });
  }

  // Trunk edges: root → ingredients, then ingredient-cluster → each observation
  for (const obs of anchors.observations) {
    const [x, y] = obsPositions.get(obs.id).xy;
    svgEl('line', {
      class: 'cn-edge cn-edge-trunk',
      x1: 0, y1: 0, x2: x, y2: y,
    }, edgeLayer);
  }

  // Framework-node positions and edges
  const fwPositions = new Map();
  for (const obs of anchors.observations) {
    const { a: obsAngle, xy: obsXY } = obsPositions.get(obs.id);
    const validLinks = obs.links.filter(id => nodesById.has(id));
    if (validLinks.length === 0) continue;
    const n = validLinks.length;
    // spread the cluster over FW_SPAN radians, centered at the observation's angle
    for (let i = 0; i < n; i++) {
      const id = validLinks[i];
      const offset = n === 1 ? 0 : (i / (n - 1) - 0.5) * FW_SPAN;
      const a = obsAngle + offset;
      // dedupe: if this node already placed (e.g. hierarchy_gaussian_lattice
      // is shared between two walls), average the angles
      if (fwPositions.has(id)) {
        const existing = fwPositions.get(id);
        const newAngle = (existing.a + a) / 2;
        const newR = R_FW + 30;  // pull shared nodes further out so they're distinct
        existing.a = newAngle;
        existing.xy = polar(newR, newAngle);
        existing.r = newR;
      } else {
        fwPositions.set(id, { a, xy: polar(R_FW, a), r: R_FW, parents: [obs.id] });
      }
      const entry = fwPositions.get(id);
      if (!entry.parents.includes(obs.id)) entry.parents.push(obs.id);

      // edge from observation to framework node
      const [fx, fy] = entry.xy;
      svgEl('line', {
        class: 'cn-edge',
        x1: obsXY[0], y1: obsXY[1], x2: fx, y2: fy,
        'data-fw-id': id,
        'data-obs-id': obs.id,
      }, edgeLayer);
    }
  }

  // ---- layer 2: ingredient nodes (between root and observation ring) --
  const ingredients = anchors.ingredients;
  for (let i = 0; i < ingredients.length; i++) {
    const ing = ingredients[i];
    // three ingredients, equally spaced. Start at 10 o'clock (a nice top-leftish).
    const a = oclockToRadians(10 + i * 4);
    const [x, y] = polar(R_ING, a);
    const g = svgEl('g', {
      class: 'cn-node cn-ingredient',
      transform: `translate(${x}, ${y})`,
    }, nodeLayer);
    svgEl('circle', { cx: 0, cy: 0, r: 7 }, g);
    // label outside the circle (toward the periphery)
    const [lx, ly] = polar(R_ING + 22, a);
    const t = svgEl('text', {
      x: lx - x, y: ly - y, 'text-anchor': 'middle', 'dominant-baseline': 'middle',
    }, g);
    t.textContent = ing.label;
    g.addEventListener('mouseenter', () => setInfo('ingredient', ing.label, ing.summary));
  }

  // ---- layer 3: the wave-outward root --------------------------------
  const root = anchors.root;
  const gRoot = svgEl('g', { class: 'cn-node cn-root', transform: 'translate(0, 0)' }, nodeLayer);
  svgEl('circle', { cx: 0, cy: 0, r: 30 }, gRoot);
  const rootText = svgEl('text', {
    x: 0, y: 0, 'text-anchor': 'middle', 'dominant-baseline': 'middle',
  }, gRoot);
  rootText.textContent = 'wave';
  const rootText2 = svgEl('text', {
    x: 0, y: 13, 'text-anchor': 'middle', 'dominant-baseline': 'middle',
  }, gRoot);
  rootText2.textContent = 'outward';
  gRoot.addEventListener('mouseenter', () => setInfo('root', root.label, root.summary,
    'sync_cost/curriculum/01_what_a_wave_is/README.md'));

  // ---- layer 4: observations -----------------------------------------
  for (const obs of anchors.observations) {
    const { a, xy: [x, y] } = obsPositions.get(obs.id);
    const isWall = !!obs.is_wall;
    const g = svgEl('g', {
      class: `cn-node cn-observation${isWall ? ' cn-wall' : ''}`,
      transform: `translate(${x}, ${y})`,
      'data-obs-id': obs.id,
    }, nodeLayer);
    svgEl('circle', { cx: 0, cy: 0, r: isWall ? 12 : 9 }, g);
    // label outside the circle, away from center
    const labelR = R_OBS + (isWall ? 30 : 24);
    const [lx, ly] = polar(labelR, a);
    const t = svgEl('text', {
      x: lx - x, y: ly - y, 'text-anchor': 'middle', 'dominant-baseline': 'middle',
    }, g);
    t.textContent = obs.label;
    g.addEventListener('mouseenter', () => {
      setInfo(isWall ? 'wall' : 'observation', obs.label, obs.summary);
      highlightObsLinks(obs.id);
    });
    g.addEventListener('mouseleave', () => clearHighlight());
  }

  // ---- layer 5: framework nodes --------------------------------------
  for (const [id, pos] of fwPositions) {
    const node = nodesById.get(id);
    const { a, xy: [x, y] } = pos;
    const g = svgEl('g', {
      class: 'cn-node cn-framework',
      transform: `translate(${x}, ${y})`,
      'data-fw-id': id,
    }, nodeLayer);
    svgEl('circle', { cx: 0, cy: 0, r: 5 }, g);
    // label radially outward, rotated to follow the angle
    const [lx, ly] = polar(pos.r + 14, a);
    const angleDeg = a * 180 / Math.PI;
    // flip the label upright on the left side of the diagram
    const flip = (a > Math.PI / 2 || a < -Math.PI / 2) ? 180 : 0;
    const t = svgEl('text', {
      x: 0, y: 0,
      'text-anchor': flip ? 'end' : 'start',
      'dominant-baseline': 'middle',
      transform: `translate(${lx - x}, ${ly - y}) rotate(${angleDeg + flip})`,
    }, g);
    // shorten label for readability
    const label = (node.title || id).replace(/\s*\([^)]*\)/g, '');
    t.textContent = label.length > 38 ? label.slice(0, 35) + '…' : label;
    g.addEventListener('mouseenter', () => setInfo('framework claim', node.title || id,
      (node.summary || 'No summary.').slice(0, 320), node.path));
    g.addEventListener('click', () => {
      if (node.path) window.open(GITHUB_BASE + node.path, '_blank', 'noopener');
    });
  }

  // ---- layer 6: "you are here" marker --------------------------------
  const here = svgEl('g', { class: 'cn-node', transform: 'translate(0, 60)' }, nodeLayer);
  svgEl('circle', { class: 'cn-here', cx: 0, cy: 0, r: 4 }, here);
  const hereLabel = svgEl('text', {
    class: 'cn-here-label', x: 0, y: 24,
  }, here);
  hereLabel.textContent = 'we are here';
  here.addEventListener('mouseenter', () =>
    setInfo('where we live', anchors.our_band.label, anchors.our_band.summary));

  // ---- helpers: highlight on observation hover -----------------------

  function highlightObsLinks(obsId) {
    const obs = anchors.observations.find(o => o.id === obsId);
    if (!obs) return;
    const liveSet = new Set(obs.links);
    document.querySelectorAll('.cn-node.cn-framework').forEach(el => {
      const fid = el.getAttribute('data-fw-id');
      if (!liveSet.has(fid)) el.classList.add('cn-dim');
      else el.classList.add('cn-active');
    });
    document.querySelectorAll('.cn-edges line').forEach(el => {
      const eObs = el.getAttribute('data-obs-id');
      if (eObs && eObs !== obsId) el.style.opacity = '0.1';
    });
  }

  function clearHighlight() {
    document.querySelectorAll('.cn-node.cn-framework').forEach(el => {
      el.classList.remove('cn-dim');
      el.classList.remove('cn-active');
    });
    document.querySelectorAll('.cn-edges line').forEach(el => {
      el.style.opacity = '';
    });
  }
}

init().catch(err => {
  console.error('concentric.js init failed:', err);
  document.getElementById('info-summary').textContent =
    'Failed to load graph data: ' + err.message;
});
