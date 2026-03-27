# Models

Applied models derived from the synchronization cost framework.

Each model identifies the **minimum self-predicting mode set** for
a specific physical system — the Farey equivalent at that scale —
and computes only the coprime modes. The GCD reduction provides the rest.

## The principle

Cost per mode is fixed: 1/q³ (the duty cycle, set by d=3).
Mode COUNT is reducible: only the coprime Farey fractions contribute.
Everything else is an ancestor in disguise.

Savings = (modes currently used) / (minimum Farey modes needed).

## Models

### Immediate (buildable now)

| Model | File | Status |
|-------|------|--------|
| Two metronomes | `metronome_staircase.md` | Proposed |
| N=3 Möbius resonator | `mobius_resonator.md` | Proposed (D22) |
| Quantum chemistry mode reduction | `farey_orbitals.md` | Concept |

### Speculative (require domain expertise)

| Model | File | Status |
|-------|------|--------|
| Lattice QCD Farey modes | `lattice_farey.md` | Concept |
| Atmospheric stick-slip (tornado/lightning) | `atmospheric.md` | Concept |
| Protein folding locked modes | `protein_modes.md` | Concept |

## License

CC0 1.0 Universal — no rights reserved.
