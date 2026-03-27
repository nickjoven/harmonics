# N=3 Möbius Resonator

## The benchtop Klein bottle (from D22)

### Design

Three LC oscillators in a ring with one phase-inverting connection.

```
    [LC₁] ——K——> [LC₂] ——K——> [LC₃] ——(-K)——> [LC₁]
                                        ^
                                   phase inversion
                                   (the half-twist)
```

The phase inversion makes the ring a Möbius strip in phase space.
The antiperiodic BC forces half-integer winding compatibility —
the XOR filter from the Klein bottle.

### Components

| Part | Value | Purpose |
|------|-------|---------|
| 3× inductor | 100 μH | LC oscillator |
| 3× capacitor | 100 pF | LC oscillator (f₀ ≈ 1.6 MHz) |
| 2× coupling cap | 10 pF (tunable) | Normal coupling K |
| 1× inverting transformer | 1:1 | Phase inversion (the twist) |
| 1× varactor or trim cap | tunable | Sweep K through threshold |

Estimated cost: ~$30 in components.

### What to measure

1. **Sweep K** from zero to above threshold by tuning the
   coupling capacitors.

2. **At each K**, measure the output spectrum with an oscilloscope
   FFT or a spectrum analyzer.

3. **Record which modes lock** and at what coupling strength.

### Predictions

| K range | Expected behavior |
|---------|-------------------|
| K < K_c | Three independent oscillators at f₀ |
| K ≈ K_c | Critical slowing, intermittency |
| K > K_c (weak) | q=2 mode locks first (f₀/2 subharmonic) |
| K > K_c (moderate) | q=3 modes lock (f₀/3 and 2f₀/3) |
| K >> K_c | 4-mode collapse: exactly 3 locked + 1 dark |

**The critical prediction:** with the phase-inverting connection,
the mode spectrum should show the XOR filter — only modes with
the correct parity survive. Without the inversion (replace the
transformer with a normal coupling), ALL modes survive. The
difference between the two configurations IS the Klein bottle.

### The 4-mode collapse

At sufficient coupling, the ring should lock to exactly 4 modes
(in the 2D frequency space of the coupled system):

| Mode | (q₁, q₂) | Expected |
|------|-----------|----------|
| A | (2, 3) | locked |
| B | (2, 3') | locked |
| C | (3, 2) | locked |
| D | (3', 2) | locked |

where q₁ is the winding in the periodic direction and q₂ in
the antiperiodic direction. The XOR filter (q₁%2 ≠ q₂%2)
selects exactly these.

### The coupling ratio

The power ratio between the (2,3) and (3,2) sectors should be:

    P(2,3) / P(3,2) = exp(π/2) ≈ 4.81

This is the topological constant from the Klein bottle half-twist
(D30, klein_symmetric_coupling.py). It's a population ratio, not
a coupling ratio — the NUMBER of oscillators that lock to each
sector differs by this factor.

### Control experiment

Replace the inverting transformer with a normal (non-inverting)
connection. The ring becomes a torus, not a Möbius strip. The
XOR filter disappears. ALL mode parities survive. The 4-mode
collapse does NOT occur. The mode spectrum should be richer
(more modes) but without the specific (2,3)/(3,2) selection.

The difference between the two experiments — with and without
the phase inversion — is the entire content of the Klein bottle
topology.
