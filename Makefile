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

.PHONY: all gifs figures clean lint lint-fix format

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
