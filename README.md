# harmonics

Revisiting Nikola Tesla's vision for global wireless charging through the lens
of synchronization dynamics, stick-slip mechanics, and subharmonic resonance.

## Motivation

Tesla's original program for wireless power transmission was abandoned not for
technical reasons but because copper wire infrastructure offered a clear
monetization pathway. The field moved on, and several lines of inquiry were
left unexplored:

- **Stick-slip mechanics** — Stribeck friction models map directly onto
  oscillator coupling regimes. The stick-slip transition describes how energy
  transfers between coherent and incoherent phases, a mechanism central to
  wireless power but largely absent from the literature on Tesla's approach.

- **Bifurcation** — Nonlinear oscillator networks exhibit bifurcation
  cascades that determine whether energy localizes or propagates. Understanding
  these transitions is essential for designing globally coupled resonant
  systems.

- **Subharmonic series** — The proslambenomenos framework derives
  macroscopic constants from a fundamental oscillation frequency. Subharmonic
  resonances (ν/2, ν/3, …) offer coupling channels at scales far below the
  driving frequency, potentially enabling efficient long-range power transfer
  through the medium itself.

## Prior work

This repository extends research from:

| Repository | Focus |
|---|---|
| [proslambenomenos](https://github.com/nickjoven/proslambenomenos) | Cosmological constant as fundamental frequency; Kuramoto synchronization → MOND transition |
| [201](https://github.com/nickjoven/201) | Gravity as synchronization in a frictional medium; metric tensor ↔ friction coefficient mapping |
| [intersections](https://github.com/nickjoven/intersections) | Stick-slip dynamics and dark matter; Stribeck friction ↔ MOND interpolating function; bifurcation analysis |

## Structure

```
harmonics/
├── .ket/          # knowledge substrate (content-addressed memory)
├── ket/           # ket submodule — BLAKE3 CAS, Merkle DAG, MCP tools
├── LICENSE        # CC0 1.0 Universal
└── README.md
```

## License

[CC0 1.0 Universal](LICENSE) — No rights reserved.
