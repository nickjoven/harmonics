# Makefile — build all visual assets for the harmonics framework.
#
# Usage:
#     make              # build everything
#     make gifs         # top-level animations only
#     make figures      # derivation PNGs only
#     make clean        # remove all generated assets
#
# Dependencies: Python 3, numpy, matplotlib (pillow for GIF writer)

PYTHON ?= python3
DERIVATIONS := sync_cost/derivations

# Scripts that import from repo root (stribeck_lattice, klein_bottle_kuramoto)
export PYTHONPATH := $(CURDIR):$(PYTHONPATH)

# ───────────────────────── Top-level GIFs ─────────────────────────

GIFS := genesis.gif stairs.gif triangles.gif orbit.gif spiral.gif rose.gif

genesis.gif: animate_genesis.py
	$(PYTHON) $<

stairs.gif: animate_mediants.py
	$(PYTHON) $< stairs --save

triangles.gif: animate_mediants.py
	$(PYTHON) $< triangle --save

orbit.gif: animate_mediants.py
	$(PYTHON) $< orbit --save

spiral.gif: animate_mediants.py
	$(PYTHON) $< spiral --save

rose.gif: animate_mediants.py
	$(PYTHON) $< rose --save

# ───────────────────────── Derivation PNGs ─────────────────────────

# Scripts that resolve output via __file__ (run from any directory)
$(DERIVATIONS)/klein_slip_structure.png $(DERIVATIONS)/klein_slip_spectrum.png: $(DERIVATIONS)/klein_slip_structure.py
	cd $(DERIVATIONS) && $(PYTHON) klein_slip_structure.py

$(DERIVATIONS)/staircase_dynamic_spectrum.png $(DERIVATIONS)/square_vs_staircase.png: $(DERIVATIONS)/staircase_spectrum_v2.py
	cd $(DERIVATIONS) && $(PYTHON) staircase_spectrum_v2.py

$(DERIVATIONS)/spectrum_classical.png $(DERIVATIONS)/spectrum_staircase.png: $(DERIVATIONS)/staircase_spectrum.py
	cd $(DERIVATIONS) && $(PYTHON) staircase_spectrum.py

$(DERIVATIONS)/slip_structure.png $(DERIVATIONS)/slip_histogram.png: $(DERIVATIONS)/slip_structure.py
	cd $(DERIVATIONS) && $(PYTHON) slip_structure.py

$(DERIVATIONS)/stable_waveform.png: $(DERIVATIONS)/stable_waveform.py
	cd $(DERIVATIONS) && $(PYTHON) stable_waveform.py

$(DERIVATIONS)/stable_waveform_v2.png: $(DERIVATIONS)/stable_waveform_v2.py
	cd $(DERIVATIONS) && $(PYTHON) stable_waveform_v2.py

$(DERIVATIONS)/denomination_boundary.png: $(DERIVATIONS)/denomination_boundary.py
	cd $(DERIVATIONS) && $(PYTHON) denomination_boundary.py

$(DERIVATIONS)/mediant_test.png: $(DERIVATIONS)/mediant_test.py
	cd $(DERIVATIONS) && $(PYTHON) mediant_test.py

$(DERIVATIONS)/waveform_evolution.png: $(DERIVATIONS)/waveform_evolution.py
	cd $(DERIVATIONS) && $(PYTHON) waveform_evolution.py

# Scripts that use hardcoded relative paths (run from repo root)
$(DERIVATIONS)/klein_device_exploration.png: $(DERIVATIONS)/klein_device_exploration.py
	$(PYTHON) $<

$(DERIVATIONS)/klein_symmetric_coupling.png: $(DERIVATIONS)/klein_symmetric_coupling.py
	$(PYTHON) $<

$(DERIVATIONS)/klein_kuramoto_sweep.png: $(DERIVATIONS)/klein_kuramoto_sweep.py
	$(PYTHON) $<

$(DERIVATIONS)/klein_topological_keff.png: $(DERIVATIONS)/klein_topological_keff.py
	$(PYTHON) $<

$(DERIVATIONS)/window_pinning.png: $(DERIVATIONS)/window_pinning.py
	$(PYTHON) $<

$(DERIVATIONS)/mobius_exploration.png: $(DERIVATIONS)/mobius_exploration.py
	$(PYTHON) $<

$(DERIVATIONS)/sector_coherence.png: $(DERIVATIONS)/sector_coherence.py
	$(PYTHON) $<

$(DERIVATIONS)/window_normalization.png: $(DERIVATIONS)/window_normalization.py
	$(PYTHON) $<

$(DERIVATIONS)/klein_phase_diagram.png: $(DERIVATIONS)/klein_phase_diagram.py
	$(PYTHON) $<

# ───────────────────────── Aggregate targets ─────────────────────────

FIGURES := \
	$(DERIVATIONS)/klein_slip_structure.png \
	$(DERIVATIONS)/klein_slip_spectrum.png \
	$(DERIVATIONS)/staircase_dynamic_spectrum.png \
	$(DERIVATIONS)/square_vs_staircase.png \
	$(DERIVATIONS)/spectrum_classical.png \
	$(DERIVATIONS)/spectrum_staircase.png \
	$(DERIVATIONS)/slip_structure.png \
	$(DERIVATIONS)/slip_histogram.png \
	$(DERIVATIONS)/stable_waveform.png \
	$(DERIVATIONS)/stable_waveform_v2.png \
	$(DERIVATIONS)/denomination_boundary.png \
	$(DERIVATIONS)/mediant_test.png \
	$(DERIVATIONS)/waveform_evolution.png \
	$(DERIVATIONS)/klein_device_exploration.png \
	$(DERIVATIONS)/klein_symmetric_coupling.png \
	$(DERIVATIONS)/klein_kuramoto_sweep.png \
	$(DERIVATIONS)/klein_topological_keff.png \
	$(DERIVATIONS)/window_pinning.png \
	$(DERIVATIONS)/mobius_exploration.png \
	$(DERIVATIONS)/sector_coherence.png \
	$(DERIVATIONS)/window_normalization.png \
	$(DERIVATIONS)/klein_phase_diagram.png

.PHONY: all gifs figures clean lint lint-fix format bibliography bibliography-check

all: gifs figures

gifs: $(GIFS)

figures: $(FIGURES)

clean:
	rm -f $(GIFS) $(FIGURES)

# ───────────────────────── Linting ─────────────────────────

# Run ruff in check mode across the derivation scripts.
# Config lives in pyproject.toml.
lint:
	ruff check sync_cost/derivations/

# Auto-fix safe issues (unused imports, import ordering, etc.).
# Does NOT touch rules that require human judgment.
lint-fix:
	ruff check --fix sync_cost/derivations/

# Apply ruff's formatter (equivalent to black). Whitespace only,
# no semantic changes. Preview before committing.
format:
	ruff format sync_cost/derivations/

# ───────────────────────── Bibliography ─────────────────────────
#
# Extracts the inline arXiv:/doi: citations from sync_cost/**.md,
# resolves each against the arXiv and CrossRef APIs (cached in
# scripts/bibliography/cache.json), and regenerates references.bib,
# REFERENCES.md, and docs/bibliography.json. Run after adding or
# changing a citation, then commit the artifacts. On main, the
# bibliography.yml workflow regenerates and bot-commits these for you.

bibliography:
	$(PYTHON) scripts/bibliography/build_bibliography.py build

# Validate that every citation resolves to a real paper and the
# generated artifacts are current. Mirrors the CI gate. Add OFFLINE=1
# to validate from cache without touching the network.
bibliography-check:
	$(PYTHON) scripts/bibliography/build_bibliography.py check $(if $(OFFLINE),--offline,)

# ───────────────────────── Preview ─────────────────────────
#
# Local preview server for the framework's visual layer. The dag
# viewer shows the framework's document graph: nodes are
# derivation docs, edges are cross-references between them
# (typed grounds/derives/proposes when a `## Lineage` block is
# present, otherwise untyped references inferred from prose
# mentions). Hover/click for context. Other viewers cover the
# reference index, claim chain, glossary, and full derivation
# text.
#
# Usage:
#     make preview         # default: derivation graph (dag.html)
#     make preview-index   # reference index
#     make preview-claims  # claim-chain view
#     make preview-port PREVIEW_PORT=8080   # override port
#
# Open the printed URL in a browser. Stop with Ctrl-C.
# Override PREVIEW_PORT to pick a different port (default 8765).
#
# This regenerates docs/derivation-graph.json from current
# sources before serving, so the graph reflects whatever is in
# your working tree. If regen fails, the server still starts
# with the existing graph.

PREVIEW_PORT ?= 8765
PREVIEW_URL := http://localhost:$(PREVIEW_PORT)

# Browser opener, auto-detected: wslview/xdg-open (Linux), open (mac),
# explorer.exe (WSL without wslu). Override: make preview BROWSER=firefox
# Disable auto-open entirely: make preview BROWSER=:
BROWSER ?= $(shell command -v wslview 2>/dev/null || command -v xdg-open 2>/dev/null \
	|| command -v open 2>/dev/null || command -v explorer.exe 2>/dev/null || echo :)

# Open $(1) once the server (started after this line) is listening.
# explorer.exe exits nonzero even on success, hence the || true.
define OPEN_BROWSER
	@( sleep 1; $(BROWSER) "$(1)" >/dev/null 2>&1 || true ) &
endef

preview: preview-dag

preview-dag:
	@echo "==> Regenerating derivation graph from current sources..."
	@$(PYTHON) scripts/build_derivation_graph.py 2>&1 | tail -1 || \
		echo "    (regen failed; using existing graph)"
	@echo ""
	@echo "==> Preview server starting on port $(PREVIEW_PORT)."
	@echo "==> Open in browser to see the framework's connections:"
	@echo "==>"
	@echo "==>   http://localhost:$(PREVIEW_PORT)/docs/dag.html"
	@echo "==>"
	@echo "==> Other viewers:"
	@echo "==>   /docs/index.html        — reference index"
	@echo "==>   /docs/claim-chain.html  — claim chain (scorecard)"
	@echo "==>   /docs/glossary.html     — glossary"
	@echo "==>   /docs/derivations.html  — full derivation text"
	@echo "==>   /docs/preprint.html     — preprint view"
	@echo "==>"
	@echo "==> Press Ctrl-C to stop the server."
	@echo ""
	$(call OPEN_BROWSER,$(PREVIEW_URL)/docs/dag.html)
	@$(PYTHON) -m http.server $(PREVIEW_PORT)

preview-index:
	@$(PYTHON) scripts/build_derivation_graph.py 2>&1 | tail -1 || true
	@echo "==> $(PREVIEW_URL)/docs/index.html"
	@echo "==> Ctrl-C to stop."
	$(call OPEN_BROWSER,$(PREVIEW_URL)/docs/index.html)
	@$(PYTHON) -m http.server $(PREVIEW_PORT)

preview-claims:
	@echo "==> $(PREVIEW_URL)/docs/claim-chain.html"
	@echo "==> Ctrl-C to stop."
	$(call OPEN_BROWSER,$(PREVIEW_URL)/docs/claim-chain.html)
	@$(PYTHON) -m http.server $(PREVIEW_PORT)

# Serve + open any docs page by stem: make preview-page PAGE=curriculum
PAGE ?= dag
preview-page:
	@test -f docs/$(PAGE).html || \
		{ echo "==> no docs/$(PAGE).html — see 'make preview-list'"; exit 1; }
	@echo "==> $(PREVIEW_URL)/docs/$(PAGE).html"
	@echo "==> Ctrl-C to stop."
	$(call OPEN_BROWSER,$(PREVIEW_URL)/docs/$(PAGE).html)
	@$(PYTHON) -m http.server $(PREVIEW_PORT)

# Every frontend artifact, as clickable preview URLs.
preview-list:
	@$(PYTHON) scripts/site_nav_audit.py --list | sed 's|^|  $(PREVIEW_URL)/|'

# Is the site a navigable tree? Reports nav-orphans and full orphans.
nav-audit:
	@$(PYTHON) scripts/site_nav_audit.py || true

# ───────────────────────── Owner actions ─────────────────────────
#
# Canonical interface for actions that write the sealed substrate or
# publish (run by Nick, not agents — agent runs are classifier-blocked
# by design). Each target wraps the audited script; nothing here
# duplicates logic.
#
#   make drift              # full drift suite (safe, read-only)
#   make owner-list         # show what would be resealed (read-only)
#   make owner-reseal       # ket put drifted spine files + verify + commit .ket
#   make owner-successions  # seal the 2026-08 stale-arc succession batch
#                           # (18 records + banner trims + regen + verify)
#   make owner-succession OLD=<doc> NEW="<doc> [doc…]" REASON="…"
#                           # one-off committed SUCCEEDS declaration
#   make owner-ket-merge    # merge ket porting-instructions into main + tests
#   make owner-push         # push harmonics corrections branch + ket main
#                           # (PUBLISHES — deliberate final step)

drift:
	$(PYTHON) scripts/drift/run_all.py

owner-list:
	bash scripts/maintenance/owner_actions_2026-08.sh list

owner-reseal:
	bash scripts/maintenance/owner_actions_2026-08.sh reseal

owner-successions:
	$(PYTHON) scripts/maintenance/declare_successions_2026-08.py

owner-succession:
	@test -n "$(OLD)" -a -n "$(NEW)" || \
		{ echo "usage: make owner-succession OLD=<doc> NEW=\"<doc> [doc…]\" REASON=\"…\""; exit 6; }
	$(PYTHON) scripts/maintenance/declare_succession_cli.py $(OLD) $(NEW) --reason "$(REASON)"

owner-ket-merge:
	bash scripts/maintenance/owner_actions_2026-08.sh ket-merge

owner-push:
	bash scripts/maintenance/owner_actions_2026-08.sh push

.PHONY: drift owner-list owner-reseal owner-successions owner-succession \
	owner-ket-merge owner-push

.PHONY: preview preview-dag preview-index preview-claims preview-page \
	preview-list nav-audit preview-live preview-bg preview-stop

# Long-lived preview with auto-rebuild + front-end live-reload.
# Watches sync_cost/derivations/*.md and regenerates the graph
# on any change. The browser auto-reloads via docs/livereload.js
# polling /preview-version. Pure-stdlib implementation; no extra
# dependencies.
#
# Foreground:  Ctrl-C to stop.
# Background:  use 'make preview-bg' / 'make preview-stop'.

preview-live:
	@$(PYTHON) scripts/preview_server.py

PREVIEW_PIDFILE := .preview-server.pid
PREVIEW_LOG := .preview-server.log

preview-bg:
	@if [ -f $(PREVIEW_PIDFILE) ] && kill -0 $$(cat $(PREVIEW_PIDFILE)) 2>/dev/null; then \
		echo "==> Preview server already running (PID $$(cat $(PREVIEW_PIDFILE)))."; \
		echo "==> Stop it first: make preview-stop"; \
		exit 1; \
	fi
	@nohup $(PYTHON) scripts/preview_server.py > $(PREVIEW_LOG) 2>&1 & echo $$! > $(PREVIEW_PIDFILE)
	@sleep 0.5
	@echo "==> Preview server backgrounded (PID $$(cat $(PREVIEW_PIDFILE)))."
	@$(BROWSER) "$(PREVIEW_URL)/docs/dag.html" >/dev/null 2>&1 || true
	@echo "==> URL: http://localhost:$(PREVIEW_PORT)/docs/dag.html"
	@echo "==> Log: $(PREVIEW_LOG)"
	@echo "==> Stop: make preview-stop"

preview-stop:
	@if [ -f $(PREVIEW_PIDFILE) ]; then \
		PID=$$(cat $(PREVIEW_PIDFILE)); \
		if kill -0 $$PID 2>/dev/null; then \
			kill $$PID; \
			echo "==> Stopped preview server (PID $$PID)."; \
		else \
			echo "==> PID file exists but process not running."; \
		fi; \
		rm -f $(PREVIEW_PIDFILE); \
	else \
		echo "==> No PID file ($(PREVIEW_PIDFILE) not found)."; \
	fi
