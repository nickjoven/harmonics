# Instrument-family taxonomy of the framework

The framework's substrate sectors map cleanly onto four classical
instrument families. This is a teaching frame, not a derivation — but
the mapping is structurally tight enough to organize how the framework's
predictions cluster.

## The four voices

| Sector | Instrument | K regime | Spectrum | Fragmentation slope | Kink mass / M_k(K=1) |
|---|---|---|---|---|---|
| Gravitational K = 1 | string | K = 1 | linear, sustained | -2 (Press–Schechter) | 1.000 |
| Inflation near-K = 1 | flute | K ≈ 0.976 | fundamental + weak overtones | n_s = 0.965 (tilt) | ≈ 0.988 |
| Baryonic q_2-cascade | bowed string | K = 2^(-1/3) | sawtooth, all-Farey | -7/3 (Salpeter) | 0.891 |
| q_3-cascade | clarinet | K = 3^(-1/2) | square, odd-Farey | -5/2 (predicted) | 0.760 |

The two rightmost columns are independent predictions on the same
K-zoo: the fragmentation slope from `mass_function_family.md`, the
kink mass from `sine_gordon_substrate.md`. Each voice carries both.

## Vocabulary: two independent axes wear the word "square"

The "Spectrum" column conflates two physically independent properties.
Keeping them separate matters for reading the kink results:

- **Bore geometry → *which* harmonics (structural).** A cylindrical
  bore (clarinet) selects ODD harmonics; a conical bore (sax) admits
  ALL. This is the q_3 vs q_2, antiperiodic vs periodic, Klein vs
  torus, fermion vs boson axis — fixed by the substrate, independent
  of coupling. "Square, odd-Farey" above means odd-harmonic *timbre*
  in this sense, nothing more.
- **Reed drive → *how sharp* (dynamical).** Whether the waveform has
  hard jumps (kink-bearing, square/sawtooth) or is rounded (sinusoid)
  is set by the excitation strength — i.e. whether the coupling K
  clears the cluster-sync onset K_c = 2/pi. Above onset: sharp,
  plateaued, hosts kinks. Below: smooth, no localized kink. See
  `cascade_kink_onset.py`.

A real clarinet is "square" on **both** axes: a cylindrical bore
(odd harmonics) PLUS a stick-slip reed — a relaxation oscillator
beating against the mouthpiece, which is the same stick-slip
mechanism that seeds the framework (Stribeck/Kawano). The bore makes
it odd; the reed makes it audibly sharp.

**Caveat — the metaphor under-drives the clarinet sector.** The
framework's clarinet cascade coupling K = 3^(-1/2) = 0.577 sits
BELOW the onset K_c = 2/pi = 0.637, so the clarinet *sector* is
odd-harmonic but *smooth* — no kink — which does NOT match the
audibly-square (sharp, stick-slip) real clarinet. The reed's
kink-bearing character lives in the above-onset sectors (bowed,
Z_6, K*), not at the clarinet cascade coupling. So do not read
"clarinet = square" as "the clarinet sector hosts sharp kinks":
the bore axis (odd harmonics) and the drive axis (sharpness)
decouple here. This is exactly why the instrument mapping is a
teaching frame, not a derivation.

## Why two reed-instrument families

The framework has two natural cascade bases (q_2, q_3). These map to
the two reed-instrument overblow ratios:

- Sax / oboe / bowed string: overblow at the octave (factor 2 = q_2).
- Clarinet: overblow at the twelfth (factor 3 = q_3).

The bowed–clarinet asymmetry in acoustics is exactly the q_2 / q_3
asymmetry in the framework. Both come from the same algebraic
structure (cylindrical vs. effective-conical resonance).

## Saxophone counterfactual

The conical-bore, all-harmonic saxophone corresponds to a torus
substrate (periodic identification, no Z_2 flip). The framework chose
the Klein bottle (clarinet substrate) — non-orientable, antiperiodic.

This choice is structurally forced: the Klein-bottle commitment is
the same commitment as admitting fermions (spin structure). The torus
admits only bosons. The framework's commitment to a "clarinet
substrate" is the commitment to a fermionic universe.

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
- `klein_bottle.md` — substrate commitment = clarinet substrate
- `medium_change_demo.md` — bowed-string vs. flute physical instance
  of the lambda / EML split
