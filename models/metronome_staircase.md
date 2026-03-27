# Two Metronomes on a Shelf

## The $20 experiment that shows the devil's staircase

### Setup

Two mechanical metronomes on a shared wobbly surface (a board
on two cans, a skateboard on pencils, a book on foam).

Set them to ALMOST the same tempo. The shared surface couples
them weakly through vibration.

### Equipment

- 2 mechanical metronomes (~$8 each)
- 1 wobbly platform (a board balanced on two soda cans)
- 1 smartphone (to record audio)
- Software: any audio analysis tool with beat detection

### What to record

Record the audio of both metronomes ticking for 10+ minutes.
Extract the tick times for each metronome. Compute the phase
difference θ₁(t) − θ₂(t) over time.

### What to look for

**The devil's staircase in the phase difference plot:**

1. **Plateaus** — periods where the phase difference is constant
   (the metronomes are synchronized at a rational ratio). The
   plateaus occur at p/q fractions of the beat period.

2. **Jumps** — sudden transitions between plateaus (the metronomes
   slip from one ratio to another). Each jump is a D-state
   traversal.

3. **Fractal structure** — zoom into any gap between plateaus
   and find smaller plateaus at higher-q rationals. The structure
   is self-similar with scaling φ².

### Predictions

| Quantity | Predicted | How to measure |
|----------|-----------|----------------|
| Plateau widths | ∝ 1/q² | Duration of each sync period |
| Jump amplitude | ∝ √ε | Phase change during each slip |
| Stick duration | ∝ 1/√ε | Time spent in each plateau |
| τ × Δθ | constant | Product of stick time and jump size |
| Fractal dimension | 0.855 | Box counting on the phase plot |
| Plateau ordering | Stern-Brocot | Which ratios appear in what order |

### Variations

**Coupling strength:** Press the board down (more contact =
stronger coupling = larger K). The tongues widen. More plateaus
become visible. Fewer jumps.

**Detuning:** Set the metronomes to increasingly different tempos
(larger Ω difference = further from 1/1 tongue center). New
tongues become visible as you scan through the frequency ratio.

**Three metronomes:** Add a third on the same platform. The N=3
threshold (D6) should appear: with two metronomes, only simple
locking occurs. With three, subharmonics emerge. The transition
at N=3 is the Planck threshold in miniature.

### The connection to the framework

The phase difference lives on S¹ (it wraps around after one
full beat). The coupling through the platform is the Kuramoto
sin(θ₁ − θ₂) coupling. The tongue structure is the Arnold
tongue diagram. The staircase is the devil's staircase.

All four primitives are present:
- Integers (the beat counts)
- Mediant (the tongue ordering)
- Fixed point (the locked state)
- Parabola (the saddle-node at each tongue boundary)

The $20 experiment demonstrates the mathematical foundation
of the minimum self-predicting universe.
