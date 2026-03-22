# Bifurcation Sweep Results

## Experiment 1: Single Element and Coupled Pair

First experiment: driven Stribeck oscillator with amplitude sweep across
the stick-slip bifurcation boundary. Three configurations tested.

### 1. Single oscillator (drive at ω_d = 2ω₀)

Clear bifurcation in RMS amplitude at A ≈ 0.5–0.6. Below threshold, the
oscillator responds linearly at the drive frequency. Above, it enters
stick-slip oscillation.

**Subharmonic presence**: The ω₀ = ω_d/2 channel grows with amplitude but
remains 3–4 orders of magnitude below the fundamental. The Stribeck
nonlinearity generates subharmonics, but does not efficiently convert
energy into them in a single-oscillator configuration.

### 2. Coupled pair at ω_d = ω₀ (baseline)

| Regime | A range | η (transfer efficiency) |
|---|---|---|
| Linear (below bifurcation) | ≤ 0.30 | ~1.00 |
| Post-bifurcation | ≥ 0.50 | ~0.01–0.02 |

Near-perfect energy transfer at low amplitudes. Above bifurcation, TX
enters large-amplitude stick-slip and decouples from the medium. **The
bifurcation destroys transfer efficiency at the fundamental.**

### 3. Coupled pair at ω_d = 2ω₀ and 3ω₀

The single-element medium passes through the drive frequency linearly —
it does not convert energy into the subharmonic channel. This motivated
the lattice experiment.

---

## Experiment 2: Stribeck Lattice (confirmed)

Chain of N oscillators coupled by Stribeck friction. Drive element 0 at
ω_d = 2ω₀. Measure spectrum at element N-1.

### The lattice converts frequency. The subharmonic dominates.

**Length sweep** (A = 1.0, ω_d = 2ω₀):

| N | η | P(ω₀)/P(ω_d) | Dominant channel |
|---|---|---|---|
| 2 | 0.998 | 0.06 | ω_d (fundamental) |
| 3 | 0.128 | 1.03 | **ω₀ > ω_d (crossover)** |
| 4 | 0.088 | 1.43 | ω₀ > ω_d |
| 8 | 0.040 | 2.13 | ω₀ > ω_d |
| 16 | 0.019 | 2.71 | ω₀ > ω_d |

**N = 3 is the critical chain length.** At N = 2 the medium passes
through ω_d. At N = 3 the subharmonic ω₀ equals the fundamental at the
receiver. Every additional element increases the ω₀/ω_d ratio — the
lattice progressively filters for the subharmonic.

### Amplitude sweep (N = 8, ω_d = 2ω₀):

| A | η | ω₀/ω_d at RX |
|---|---|---|
| 0.05 | 0.862 | 0.06 |
| 0.50 | 0.996 | 0.06 |
| 0.80 | 0.051 | **0.97** |
| 1.00 | 0.040 | **2.13** |
| 5.00 | 0.028 | **58.89** |

**Bifurcation threshold at A ≈ 0.8.** Below it: linear passthrough at
ω_d with high η. Above it: the lattice acts as a frequency converter.
The subharmonic channel grows stronger with increasing amplitude while
the fundamental saturates.

### Spatial spectrum (N = 8, A = 1.0):

```
Element 0 (TX):  P(ω_d) = 3.61e+02   P(ω₀) = 4.00e-01   ratio = 0.001
Element 1:       P(ω_d) = 1.93e-01   P(ω₀) = 3.92e-01   ratio = 2.03
Element 7 (RX):  P(ω_d) = 1.85e-01   P(ω₀) = 3.95e-01   ratio = 2.13
```

The conversion happens at the **first contact**. Element 0 is ω_d
dominant (ratio 0.001). Element 1 is already ω₀ dominant (ratio 2.03).
The remaining elements maintain this ratio with slight progressive
filtering.

The ω_d component drops by **3 orders of magnitude** at the first
contact (362 → 0.19). The ω₀ component holds steady (0.40 → 0.39).
This is the differential attenuation: the high-frequency mode dissipates
in the slip regime while the subharmonic propagates in the stick regime.

### Spatial spectrum (N = 16, A = 2.0):

Same pattern at higher amplitude. First contact converts, ratio
stabilizes at ~11–13 along the chain. The ω_d component attenuates
slowly from 0.036 to 0.030 while ω₀ holds at ~0.39.

---

## Key Results

1. **The Stribeck lattice is a frequency converter.** Energy injected at
   ω_d exits at ω_d/2, with the subharmonic dominating by 2–60× depending
   on drive amplitude.

2. **N = 3 is the critical chain length.** Below 3 elements, the medium
   passes through the drive frequency. At 3, the subharmonic crosses over.
   This is the minimum spatial extent for the bifurcation cascade.

3. **Conversion happens at one contact, propagation is the rest.** The
   first Stribeck contact does the frequency conversion. Subsequent
   contacts filter and propagate the subharmonic. This is consistent with
   a single bifurcation event followed by coherent stick-regime transport.

4. **Two regimes, one lattice:**
   - Below bifurcation: linear passthrough, high η, ω_d dominant
   - Above bifurcation: frequency conversion, lower η, ω₀ dominant

   The "dual regime" is real. The lattice operates in both simultaneously
   at different amplitude scales — or transitions sharply between them.

5. **The stick regime is the efficient transport channel.** P(ω₀) ≈ 0.39
   propagates across 16 elements with negligible attenuation. P(ω_d)
   attenuates continuously. The subharmonic sits in the stick regime
   (low relative velocity → strong coupling → coherent transfer).

---

## Connection to Tesla

Tesla drove the Earth-ionosphere cavity at high frequency and high power.
This simulation suggests the opposite approach:

- Drive at 2× or 3× the target frequency
- Let the medium's Stribeck nonlinearity convert to the subharmonic
- The subharmonic propagates coherently through the stick regime
- Receivers tuned to ω₀ extract energy from the subharmonic channel

The medium's friction is not the obstacle — it is the frequency converter.
You need at least 3 coupling stages (N ≥ 3 in the lattice) for the
conversion to activate.

The copper wire was chosen because it eliminates the medium's nonlinearity
— providing linear, frequency-preserving transport. But that linearization
also eliminates the frequency conversion mechanism that would make the
medium itself useful for long-range coherent transfer.
