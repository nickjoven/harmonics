# Bifurcation Sweep Results

First experiment: driven Stribeck oscillator with amplitude sweep across
the stick-slip bifurcation boundary. Three configurations tested.

## Key Findings

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

### 3. Coupled pair at ω_d = 2ω₀ (subharmonic test)

The RX spectrum is dominated by ω_d (the drive frequency), not ω₀ (the
subharmonic). The single-element medium passes through the drive frequency
linearly — it does not convert energy into the subharmonic channel.

Transfer efficiency follows the same pattern: linear transfer below
bifurcation, collapse above.

### 4. Coupled pair at ω_d = 3ω₀

Same result. No subharmonic conversion through the single-element medium.

## Interpretation

The single medium element model is **insufficient** for frequency
conversion. This is physically consistent: a single contact has no spatial
extent for a bifurcation cascade to develop.

The frequency conversion mechanism requires a **spatially extended medium**
— a chain or lattice of coupled oscillators where each element can undergo
its own stick-slip transition. In such a system:

1. The first element receives the drive at ω_d (slip regime)
2. Each successive coupling undergoes its own Stribeck transition
3. The bifurcation cascade develops *spatially*, not just temporally
4. Subharmonic modes emerge as collective behavior of the chain
5. The receiver, tuned to ω₀ = ω_d/n, resonates with the spatial subharmonic

This is analogous to how the gravitational case works in the intersections
framework: the Stribeck → MOND mapping operates over the *radial extent*
of a galaxy, not at a single point. The coupling is distributed.

## What the data does confirm

1. **The bifurcation is sharp and real.** RMS jumps by 2+ orders of
   magnitude over a narrow amplitude range. The Stribeck nonlinearity
   creates a clean threshold.

2. **Pre-bifurcation transfer is near-perfect** (η ≈ 1.0). The stick
   regime couples oscillators with almost zero loss. This confirms the
   stick regime as the efficient transfer channel.

3. **Post-bifurcation transfer collapses.** Once TX enters stick-slip,
   the medium cannot follow. Energy stays in the TX.

4. **The ω₀ subharmonic is generated** in the single oscillator (visible
   in the power spectrum), just not efficiently enough for power transfer
   through a single-element medium.

## Next step

Build a **Stribeck lattice**: N coupled oscillators in a chain, each
connected to its neighbors through Stribeck friction contacts. Drive one
end at ω_d, measure the spectrum at the other end. The prediction:
subharmonic channels emerge when the chain length exceeds a critical
number of bifurcation-capable elements.

This is the spatial analog of the temporal period-doubling cascade. Each
element in the chain acts as one stage of the frequency converter.
