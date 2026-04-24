"""
build_claim_chain.py

Generate docs/claim-chain.html from MANIFEST.yml — the single canonical
view of what the framework claims and what it declines to claim. The
scorecard, bare K=1 identities, anchors, and proof chains are emitted
in one page with source links back into sync_cost/derivations/.

Re-run after any MANIFEST.yml edit to keep the page in sync.

Usage:
    python3 scripts/build_claim_chain.py
"""

import html
import json
import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "MANIFEST.yml"
OUT_PATH = ROOT / "docs" / "claim-chain.html"
DERIV_DIR = "sync_cost/derivations"


_SIBLING_REPOS = {
    "rfe": "https://github.com/nickjoven/rfe",
    "proslambenomenos": "https://github.com/nickjoven/proslambenomenos",
    "201": "https://github.com/nickjoven/201",
    "intersections": "https://github.com/nickjoven/intersections",
    "submediant-site": "https://github.com/nickjoven/submediant-site",
}


def _linkify_sources(sources):
    """Turn a list of derivation ids, filename stems, or sibling-repo
    names into a comma-separated list of links. Unknown tokens fall
    through to plain text."""
    if not sources:
        return "&mdash;"
    deriv_root = ROOT / DERIV_DIR
    out = []
    for s in sources:
        s = str(s)
        if s in _SIBLING_REPOS:
            out.append(
                f'<a href="{_SIBLING_REPOS[s]}">'
                f'{html.escape(s)}</a>'
            )
        elif s and not s.startswith("D") and "/" not in s and (
            (deriv_root / f"{s}.md").exists()
            or (deriv_root / f"{s}.py").exists()
        ):
            ext = "md" if (deriv_root / f"{s}.md").exists() else "py"
            target = f"../{DERIV_DIR}/{s}.{ext}"
            out.append(f'<a href="{html.escape(target)}">{html.escape(s)}</a>')
        else:
            out.append(html.escape(s))
    return ", ".join(out)


def render_scorecard_row(key, entry):
    name = html.escape(str(entry.get("name", key)))
    computed = html.escape(str(entry.get("computed", "")))
    observed = html.escape(str(entry.get("observed", "")))
    residual = html.escape(str(entry.get("residual", "")))
    sources = _linkify_sources(entry.get("source", []))
    return (
        f"<tr>\n"
        f"  <td>{name}</td>\n"
        f'  <td class="val">{computed}</td>\n'
        f'  <td class="val">{observed}</td>\n'
        f'  <td class="val">{residual}</td>\n'
        f"  <td>{sources}</td>\n"
        f"</tr>"
    )


def render_bare_row(key, entry):
    form = html.escape(str(entry.get("form", "")))
    value = html.escape(str(entry.get("value", "")))
    status = html.escape(str(entry.get("status", "")))
    gap = html.escape(str(entry.get("m_z_gap", "&mdash;")))
    sources = _linkify_sources(entry.get("source", []))
    return (
        f"<tr>\n"
        f"  <td><code>{html.escape(key)}</code></td>\n"
        f'  <td class="val">{form}</td>\n'
        f'  <td class="val">{value}</td>\n'
        f'  <td class="val">{gap}</td>\n'
        f"  <td>{sources}</td>\n"
        f"</tr>"
    )


def render(manifest: dict) -> str:
    generated = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    # --- Summary counts ---
    scorecard = manifest.get("scorecard", {})
    bare = manifest.get("bare_k1_identities", {})
    primitives = manifest.get("primitives", {})
    anchors = manifest.get("dimensionful_inputs_detail", {})
    klein = manifest.get("klein_bottle", {})
    proof_chains = manifest.get("proof_chains", {})

    # --- Header / summary ---
    summary = (
        f"<p class=\"subtitle\">One canonical view of the claim chain, "
        f"generated from "
        f"<a href=\"https://github.com/nickjoven/harmonics/blob/main/MANIFEST.yml\">"
        f"MANIFEST.yml</a> on {generated}. "
        f"Scorecard: {len(scorecard)} predictions with explicit derivations. "
        f"Bare K=1 identities: {len(bare)} reference values the framework declines "
        f"to predict at M_Z. Two observational anchors "
        f"(<code>H_0</code>, <code>v_EW</code>); see "
        f"<a href=\"../{DERIV_DIR}/anchor_count_audit.md\">anchor_count_audit.md</a>.</p>"
    )

    # --- Anchors section ---
    n_free_p = manifest.get("free_parameters", "?")
    n_free_f = manifest.get("free_functions", "?")
    n_dim = manifest.get("dimensionful_inputs", "?")
    dim_note = html.escape(str(manifest.get("dimensionful_input_note", "")).strip())
    cosm_anchor = anchors.get("cosmological", {})
    part_anchor = anchors.get("particle", {})
    v_gap = anchors.get("v_over_MP_gap", {})
    anchors_html = (
        f"<h2>Inputs</h2>\n"
        f"<table>\n"
        f"  <tr><th>Kind</th><th>Count</th><th>Note</th></tr>\n"
        f'  <tr><td>Free parameters</td><td class="val">{n_free_p}</td><td>&mdash;</td></tr>\n'
        f'  <tr><td>Free functions</td><td class="val">{n_free_f}</td><td>&mdash;</td></tr>\n'
        f'  <tr><td>Dimensionful inputs</td><td class="val">{n_dim}</td>'
        f"<td>{dim_note}</td></tr>\n"
        f"</table>\n"
        f"<h3>Anchors</h3>\n"
        f"<table>\n"
        f"  <tr><th>Sector</th><th>Anchor</th><th>Covers</th></tr>\n"
        f'  <tr><td>Cosmological</td><td class="val">'
        f"{html.escape(str(cosm_anchor.get('anchor', '')))}</td>"
        f'<td class="val">{html.escape(", ".join(cosm_anchor.get("covers", [])))}</td></tr>\n'
        f'  <tr><td>Particle</td><td class="val">'
        f"{html.escape(str(part_anchor.get('anchor', '')))}</td>"
        f'<td class="val">{html.escape(", ".join(part_anchor.get("covers", [])))}</td></tr>\n'
        f"</table>\n"
        f'<p><strong>v / M_P open gap:</strong> observed '
        f'<code>{html.escape(str(v_gap.get("observed", "")))}</code>; '
        f"nearest numerology <code>{html.escape(str(v_gap.get('nearest_numerology', '')))}</code>. "
        f"Status: {html.escape(str(v_gap.get('status', '')))}.</p>"
    )

    # --- Primitives ---
    p_list = primitives.get("list", [])
    prim_rows = "\n".join(
        f'  <li>{html.escape(str(p))}</li>' for p in p_list
    )
    prim_html = (
        f"<h2>Primitives ({primitives.get('count', '?')})</h2>\n"
        f'<p class="subtitle">{html.escape(str(primitives.get("note", "")))}</p>\n'
        f"<ul>\n{prim_rows}\n</ul>"
    )

    # --- Scorecard ---
    sc_rows = "\n".join(
        render_scorecard_row(k, v) for k, v in scorecard.items()
    )
    scorecard_html = (
        f"<h2>Scorecard &mdash; {len(scorecard)} predictions</h2>\n"
        f'<p class="subtitle">Each row has an explicit, scale-consistent '
        f"derivation linked in the source column.</p>\n"
        f"<table>\n"
        f"  <tr><th>Observable</th><th>Computed</th><th>Observed</th>"
        f"<th>Residual</th><th>Source</th></tr>\n"
        f"{sc_rows}\n"
        f"</table>"
    )

    # --- Bare K=1 identities ---
    bare_rows = "\n".join(
        render_bare_row(k, v) for k, v in bare.items()
    )
    bare_html = (
        f"<h2>Bare K=1 identities &mdash; {len(bare)} declined</h2>\n"
        f'<p class="subtitle">Measure-theoretic consequences of '
        f'<code>duty(q) = 1/q^d</code> at critical coupling '
        f"(<a href=\"../{DERIV_DIR}/duty_dimension_proof.md\">duty_dimension_proof.md</a>). "
        f"These are reference values, <strong>not</strong> predictions at M_Z. "
        f"The framework does not currently supply a running mechanism that "
        f"closes the gap to the electroweak scale; see "
        f"<a href=\"../{DERIV_DIR}/numerology_inventory.md\">numerology_inventory.md</a> "
        f"and "
        f"<a href=\"../{DERIV_DIR}/sinw_fixed_point.md\">sinw_fixed_point.md</a>.</p>\n"
        f"<table>\n"
        f"  <tr><th>Identity</th><th>Form</th><th>K=1 value</th>"
        f"<th>M_Z gap</th><th>Source</th></tr>\n"
        f"{bare_rows}\n"
        f"</table>"
    )

    # --- Klein bottle constants ---
    klein_rows = "\n".join(
        f'  <tr><td><code>{html.escape(str(k))}</code></td>'
        f'<td class="val">{html.escape(str(v))}</td></tr>'
        for k, v in klein.items()
    )
    klein_html = (
        f"<h2>Klein bottle constants</h2>\n"
        f'<p class="subtitle">All cosmological and gauge-sector integer '
        f"ratios derive from these.</p>\n"
        f"<table>\n  <tr><th>Symbol</th><th>Value</th></tr>\n"
        f"{klein_rows}\n</table>"
    )

    # --- Proof chains ---
    chain_rows = []
    for letter, c in proof_chains.items():
        name = html.escape(str(c.get("name", "")))
        props = html.escape(str(c.get("propositions", "")))
        repo = html.escape(str(c.get("repo", "")))
        file_ = c.get("file", "")
        note = html.escape(str(c.get("note", "")))
        if repo == "harmonics" and file_:
            link = f'<a href="../{html.escape(file_)}">{html.escape(str(file_))}</a>'
        elif file_:
            link = (
                f'<a href="https://github.com/nickjoven/{html.escape(repo)}'
                f'/blob/main/{html.escape(file_)}">'
                f'{html.escape(str(repo))}/{html.escape(str(file_))}</a>'
            )
        else:
            link = "&mdash;"
        chain_rows.append(
            f"<tr>\n"
            f'  <td class="val">{html.escape(str(letter))}</td>\n'
            f"  <td>{name}</td>\n"
            f'  <td class="val">{props}</td>\n'
            f"  <td>{link}</td>\n"
            f"  <td>{note}</td>\n"
            f"</tr>"
        )
    chains_html = (
        f"<h2>Proof chains ({len(proof_chains)})</h2>\n"
        f"<table>\n"
        f"  <tr><th>Chain</th><th>Name</th><th>Propositions</th>"
        f"<th>Source</th><th>Note</th></tr>\n"
        f'{chr(10).join(chain_rows)}\n'
        f"</table>"
    )

    # --- Other views ---
    other_views = (
        f"<h2>Other views of the same graph</h2>\n"
        f"<table>\n"
        f"  <tr><th>View</th><th>What it shows</th></tr>\n"
        f'  <tr><td><a href="claim-chain-views.html">Three views</a></td>'
        f"<td>Max/MSP patch, pure-math expression tree, and syllogism "
        f"rendering over the curated claim-chain subgraph.</td></tr>\n"
        f'  <tr><td><a href="dag.html">Interactive DAG</a></td>'
        f"<td>108 derivation nodes, 305 edges, with audit trail per file.</td></tr>\n"
        f'  <tr><td><a href="derivations.html">Derivation index</a></td>'
        f"<td>Narrative list of the 47 numbered derivations.</td></tr>\n"
        f'  <tr><td><a href="glossary.html">Glossary</a></td>'
        f"<td>Symbol and term definitions used across the framework.</td></tr>\n"
        f'  <tr><td><a href="index.html">Reference</a></td>'
        f"<td>Quick-reference scorecard and proof chains A/B.</td></tr>\n"
        f'  <tr><td><a href="a_s_proof.html">A_s proof (3D)</a></td>'
        f"<td>Axioms &rarr; observation path for the spectral amplitude.</td></tr>\n"
        f'  <tr><td><a href="cmb-s4.html">CMB-S4</a></td>'
        f"<td>Upcoming-experiment falsifiability notes.</td></tr>\n"
        f"</table>"
    )

    # --- Page frame ---
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Claim Chain &mdash; Harmonics</title>
<meta name="description" content="Canonical view of the harmonics
 claim chain: anchors, primitives, scorecard, bare K=1 identities,
 proof chains. Generated from MANIFEST.yml.">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body, {{delimiters:[
    {{left:'$$',right:'$$',display:true}},
    {{left:'$',right:'$',display:false}}
  ]}});"></script>
</head>
<body>

<nav>
  <a href="../index.html">Home</a>
  <a href="index.html">Reference</a>
  <a href="claim-chain.html" class="active">Claim chain</a>
  <a href="claim-chain-views.html">Three views</a>
  <a href="glossary.html">Glossary</a>
  <a href="derivations.html">Derivations</a>
  <a href="dag.html">DAG</a>
  <a href="cmb-s4.html">CMB-S4</a>
</nav>

<h1>Claim chain</h1>
{summary}

{anchors_html}

{prim_html}

{scorecard_html}

{bare_html}

{klein_html}

{chains_html}

{other_views}

<footer>
  <p>Generated from
  <a href="https://github.com/nickjoven/harmonics/blob/main/MANIFEST.yml">MANIFEST.yml</a>
  by <code>scripts/build_claim_chain.py</code> &middot;
  <a href="https://github.com/nickjoven/harmonics">source</a> &middot;
  CC0 1.0 Universal.</p>
</footer>

</body>
</html>
"""


def main():
    with open(MANIFEST_PATH) as f:
        manifest = yaml.safe_load(f)
    html_text = render(manifest)
    OUT_PATH.parent.mkdir(exist_ok=True)
    OUT_PATH.write_text(html_text)
    scorecard_n = len(manifest.get("scorecard", {}))
    bare_n = len(manifest.get("bare_k1_identities", {}))
    print(f"Wrote {OUT_PATH} "
          f"({scorecard_n} scorecard, {bare_n} bare identities)")


if __name__ == "__main__":
    main()
