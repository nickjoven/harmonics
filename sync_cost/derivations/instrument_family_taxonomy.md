# Instrument-family taxonomy of the framework

The framework's substrate sectors map onto classical instrument
families along two independent axes. This is a teaching frame, not a
derivation — but the mapping is structurally tight enough to organize
how the framework's predictions cluster.

## The two independent axes

Two physically independent properties must be kept separate, because a
single instrument name conflates them. A **triangle** wave is
odd-harmonic just as a square wave is — they differ only in *sharpness*
(1/n² vs 1/n harmonic falloff), not in *which* harmonics are present.
So "odd harmonics" does not pick out "clarinet"; it picks out a closed
cylinder, which can be smooth (triangle-like) or sharp (square-like)
depending on how it is driven.

**Axis A — bore geometry → *which* harmonics (structural, set by the
substrate, independent of coupling):**

| Bore | Harmonics | Overblow | Substrate |
|---|---|---|---|
| open cylinder | all (1,2,3,…) | octave (×2 = q_2) | torus / periodic |
| cone | all (1,2,3,…) | octave (×2 = q_2) | torus / periodic |
| closed cylinder | odd (1,3,5,…) | twelfth (×3 = q_3) | Klein / antiperiodic |

Odd harmonics come ONLY from a closed cylinder; "all harmonics" comes
from either an open cylinder or a cone. The framework's antiperiodic
(odd / Klein / fermionic) commitment is specifically the closed
cylinder — the cylinder-vs-cone choice, divorced from how it is driven.

**Axis B — excitation → *how sharp* (dynamical, set by K vs the
cluster-sync onset K_c = 2/pi; see `cascade_kink_onset.py`):**

| Excitation | Character | Waveform | Kink? |
|---|---|---|---|
| flue / air-jet | smooth, gentle | sinusoid / triangle | below onset: none |
| reed | nonlinear pressure valve | square (sharp) | above onset: yes |
| bow | stick-slip relaxation | sawtooth (sharp) | above onset: yes |

The axes are orthogonal. Their 2×2 (harmonic content × sharpness):

| | smooth (flue, below onset) | sharp (reed/bow, above onset) |
|---|---|---|
| **all harmonics** | flute / open flue | bowed string, sax (sawtooth) |
| **odd harmonics** | **stopped flue (Gedackt)** | clarinet (square reed) |

## The framework's voices, re-mapped

| Sector | K | bore (harmonics) | excitation | proper instrument | slope | kink |
|---|---|---|---|---|---|---|
| Gravitational K=1 | 1 | all (full lock) | sustained | string | −2 | M_k=1 |
| Inflation near-K=1 | 0.976 | all | smooth | flute / open flue | n_s tilt | ≈ boundary |
| Baryonic q_2-cascade | 2^(−1/3) | all (octave) | **sharp** (above onset) | bowed string | −7/3 | soft kink |
| q_3-cascade | 3^(−1/2) | odd (twelfth) | **smooth** (below onset) | **stopped flue (Gedackt)** | −5/2 | none |

The q_3 sector is odd-harmonic (closed-cylinder bore) but its coupling
K = 0.577 sits BELOW the onset, so it is *smooth* — a **stopped flue
pipe** (the organ Gedackt / Bourdon / Stopped Diapason: a closed
cylindrical, jet-excited rank that is odd-harmonic AND mellow). That
is exactly odd-but-smooth, the triangle-not-square corner — not a reed
clarinet, whose audible squareness comes from its reed.

**A true clarinet (odd + sharp) is a missing voice.** A real clarinet
is a closed cylinder driven ABOVE onset by a stick-slip reed — the same
relaxation/stick-slip mechanism that seeds the framework
(Stribeck/Kawano). The current cascade has no such sector: its only
odd-bore (b=3) rung, K = 3^(−1/2), is below the kink onset. The
genuinely clarinet-like (odd + sharp, kink-bearing) voice would require
an odd-bore sector above K_c — which the K-zoo does not yet supply.

## Structural anchor (Axis A only)

The substrate commitment lives entirely on Axis A: a CLOSED-CYLINDER
(odd, antiperiodic) bore = the Klein bottle = a spin structure = a
**fermionic** universe; an open-cylinder or conical (all-harmonic,
periodic) bore = the torus = **bosonic**. This is independent of the
excitation (reed vs flue vs bow) — which is the whole point of the
decomposition. The conical, all-harmonic **saxophone** is the
torus/boson counterfactual the framework declined; the framework's
closed-cylinder commitment is the commitment to fermions, regardless of
whether any given sector is driven sharply (reed/bow) or smoothly (flue).

### Bore parity and kink charge are two distinct Z₂'s

The boson/fermion label above is the harmonic-parity superselection of
the *field* half-twist θ → θ + π (`framework_lagrangian.py` Symmetry 6):
states split into even (bosonic) and odd (fermionic) representations,
and a sector's bore parity says which representation its locked modes
occupy. This is a separate Z₂ from the kink's topological charge
Q mod 2, which is the *coordinate* antiperiodicity of the Klein gluing
(`sine_gordon_substrate.md`'s "Distinct from the field half-twist").

The consequence matters for the soliton sector: a kink's boson/fermion
character is fixed by its own half-twist parity (the global
superselection), not by the bore parity of the sector that hosts it.
So kinks need not form in the odd-bore sector. The soft kinks of the
above-onset all-harmonic sectors are legitimate fermions — a
topologically charged soliton sitting in the odd half-twist
representation, the Coleman sine-Gordon ↔ Thirring correspondence —
even though their host bore is all-harmonic. "The odd-bore sector is
fermionic" (its modes occupy the odd representation) and "the kinks are
fermions" (Coleman, via the global half-twist) are two compatible facts
about two different Z₂'s, not a contradiction.

## Why this is useful

- Organizes the K-zoo: each K-value is one instrument's voice.
- Makes the K = 1 vs. K < 1 split physically intuitive.
- Connects framework primitives (q_2, q_3) to acoustic-physics
  primitives.
- Provides external onboarding without requiring readers to absorb
  the full Stern–Brocot / Klein-bottle machinery first.

## Cross-links

- `master_cascade_identity.md` — the four-voice formal structure
- `mass_function_family.md` — each voice predicts a fragmentation slope
- `sine_gordon_substrate.md` — each voice also predicts a kink mass
  via `M_k ∝ √K` (soliton sector)
- `klein_bottle.md` — substrate commitment = closed-cylinder (odd, antiperiodic) bore
- `medium_change_demo.md` — bowed-string vs. flute physical instance
  of the lambda / EML split
