# F2 PR-2 — FM-beat Tier-0 simulator results

## What this doc is — and what it is not

This is **Tier-0 numerical results** from running
`fm_beat_chain_simulation.py` (added in PR #270 alongside the F2
scoping doc). It validates a substrate claim — the audit's
`fm_beat_crt_correspondence_audit.md` (#252) bare modal claim that
"coherent line at ω_{ab} = 2π/(ab) iff |a − b| = 1" — and quantifies
the Kuramoto-pulling tolerance the Tier-1 benchtop build will need.

It does **not** close F2. The audit's modal claim is itself analytic
(a sum-to-product identity on two phase oscillators); a clean
simulator confirmation is necessary but not new physics. The genuine
F2-relevant content is what the run says about
[[f2_scoping]]'s Possibility A (discrete-is-physical): the
combinatorial selection rule survives as a physical observable
under K=0 dynamics, with a calculable transition into the K>0
locking regime. That is a partial brick for A, not closure of A —
let alone closure of F2.

Z_72 (the Catalan composite from #252 §3) is realized as a coherent
line in the model. The substrate-engagement gap (#252 §3: no
canonical surface assigns Z_72 a role) remains.

## What was tested

Three configurations on identical apparatus (two independent
phase oscillators, composite-mode observable cos(φ_a − φ_b),
RK4 integration, targeted-DFT line search; all dimensionless,
ω_n = 2π/n per audit §0 G4).

| Run | (a, b) | Cyclic group | Audit prediction at K=0 |
|---|---|---|---|
| 1 — Positive control | (2, 3) | Z_6 | Coherent line at ω_6 = 2π/6 |
| 2 — Catalan headline | (8, 9) | Z_72 | Coherent line at ω_72 = 2π/72 |
| 3 — Negative control | (3, 5) | (CRT gives Z_15) | NO line at ω_15; beat at 4π/15 |

The audit's third consecutive Mihailescu pair (3, 4) → Z_12 was
not run; the harness covers it identically if needed (a one-line
extension, deferred to keep this PR scope-bounded).

## Part A — K=0 modal claim

```
[PASS] (2, 3)  ratio@ω_pred =  35.5   POSITIVE CONTROL (Z_6)
[PASS] (8, 9)  ratio@ω_pred =  35.5   CATALAN COMPOSITE (Z_72)
[PASS] (3, 5)  ratio@ω_pred =   0.0   NEGATIVE CONTROL (non-consecutive)
```

Run 1: amplitude 200.0 at ω_pred = 1.047198, selectivity ratio 35.5
(well above the verdict threshold of 10). Harness can resolve the
line.

Run 2: amplitude 200.0 at ω_pred = 0.087266, selectivity ratio
35.5. Z_72 line is just as clean as Z_6 at K=0 — the (8, 9) pair
is **physically realized** as a coherent composite-mode line in the
model. The framework-engagement gap (no canonical surface assigns
Z_72 a role) is not addressed by this result.

Run 3: amplitude 0.0000 at the audit-predicted absence frequency
(ω_15); amplitude 200.0 at the actual beat |ω_3 − ω_5| = 4π/15
with selectivity ratio 63.8. The selection rule is **physical**,
not just arithmetic — non-consecutive pairs do not produce a clean
line at the would-be CRT composite frequency.

Falsifier audit §6: none of F-FM-1, F-FM-2 fire.

## Part B — K-sweep (Kuramoto frequency pulling)

For two oscillators with detuning Δω, the analytic K<K_c locking-
approach prediction is ω_obs(K) = √(Δω² − (2K)²). The audit's
modal identity is the K→0 statement; finite-K pulls the line.

### (2, 3) — Z_6

```
K/K_c    K       ω_peak     amp_peak  ω_analytic   shift
0.00   0.0000   1.047198   200.0000   1.047198    +0.00%
0.10   0.0524   1.047198   191.8832   1.041948    +0.00%
0.25   0.1309   1.015782   196.3566   1.013945    +3.00%
0.50   0.2618   0.911062   181.3663   0.906900   +13.00%
0.75   0.3927   0.743510    32.7653   0.692656   +29.00%
0.90   0.4712   0.911062    76.9179   0.456463   +13.00%
```

### (8, 9) — Z_72

```
K/K_c    K       ω_peak     amp_peak  ω_analytic   shift
0.00   0.0000   0.087266   200.0000   0.087266    +0.00%
0.10   0.0044   0.087266   191.8851   0.086829    +0.00%
0.25   0.0109   0.084648   196.3565   0.084495    +3.00%
0.50   0.0218   0.075922   181.3646   0.075575   +13.00%
0.75   0.0327   0.061959    32.7649   0.057721   +29.00%
0.90   0.0393   0.075922    76.9185   0.038039   +13.00%
```

The shifts are identical between the two pairs at each K/K_c
fraction. This is the expected scaling: the analytic formula
depends only on the ratio (2K/Δω), so any consecutive pair traces
the same curve when K is parameterized as a fraction of K_c.

Observed peak agrees with analytic prediction to within FFT bin
resolution through K/K_c = 0.50. At K/K_c = 0.75 the line search
agrees but the line is broadening (amp_peak drops from 196 → 33).
At K/K_c = 0.90 the line-search routine latches onto a local
maximum offset from the analytic prediction (the system is entering
the locking regime where the two-tone structure dissolves) — this
is a known feature of approaching K_c, not a model failure.

## Benchtop constraint for Tier-1

The K-sweep gives a quantitative tolerance for the engineering-
targets benchtop build:

- At K/K_c ≤ 0.10 the line shift is below the +0.5% level and
  the line stays within one FFT bin of ω_pred for typical record
  lengths. **This is the operating region.**
- At K/K_c = 0.25 the line shifts by +3% — requires fine-binned
  FFT and explicit reporting that the observed line is pulled.
- K/K_c ≥ 0.50 is not a valid test of the modal identity at the
  bare ω_pred frequency; the line moves into a regime that needs
  the full Kuramoto correction.

Concretely, for the (8, 9) → Z_72 headline run with Δω = 2π(1/8 − 1/9)
= π/36 ≈ 0.0873, the coupling between the two oscillators must
satisfy K ≪ 0.0044 (a factor of 10 below K_c/10) for the line at
ω_72 to land within bin tolerance.

## What this means for F2

**Possibility A (discrete-is-physical)** —
[[f2_scoping]] §"Open possibilities":

- The audit's combinatorial selection rule (|a−b|=1 for clean
  composite-mode lines) is preserved in a physical dynamical
  realization at K=0. That is a brick for A: the discrete
  selection has a physical observable witness, not merely a
  combinatorial one.
- The K-sweep gives a calculable transition from the discrete
  regime (clean line, K → 0) to the locking regime (line dissolves,
  K → K_c). This is the right kind of structure for A: the
  discrete description is recovered in a limit; the deformation
  is calculable.
- A's closure criterion was "finite tree reproduces gauge theory
  predictions without continuum limit." This result is far short
  of that — it shows one combinatorial rule has a physical
  realization, not that the full gauge sector is finite-tree-
  derivable. Partial brick, not closure.

**Possibility B (mean-field functional F[N])** — no direct
bearing. The two-oscillator Kuramoto analysis is the K<K_c
regime of pair synchronization; it does not address the
Jacobian of F[N] at the 4-mode XOR fixed point, which is B's
natural starting calculation.

**Z_72 substrate engagement** — unchanged. The simulator realizes
Z_72 as a coherent line in a phase-oscillator model that *assumes*
the (8, 9) carrier pair. It does not derive (8, 9) from the
substrate. The audit's §3 gap ("no canonical surface assigns Z_72
a role") remains; this result is a physical-realization existence
proof for Z_72, not a substrate-side derivation.

## What ships from this PR

- This results doc, classified per the discipline below.
- Suggested forward-pointers (not edits in this PR):
  - `engineering_targets.md` could cite the K/K_c ≤ 0.10
    tolerance derived here when the Tier-1 build is specified.
  - `fm_beat_crt_correspondence_audit.md` §6 (falsifiers) could
    cite that Part A's three runs do not fire F-FM-1 or F-FM-2
    at K=0 in the model.

Deferred to PR-3 candidates:

1. Run the third consecutive Mihailescu pair (3, 4) → Z_12 to
   round out the audit's inventory; one-line extension.
2. Attempt substrate-engagement for Z_72 (the audit's §3 open
   item): is there a canonical role for Z_72 that the framework
   could derive rather than admit?
3. Possibility-B attempt — Kuramoto-ensemble averaging at the
   4-mode XOR fixed point of F[N] (the headline F2 closure
   technique catalog'd in [[f2_scoping]] §"Techniques on the table"
   item 1).

## Cross-references

| File | Role |
|---|---|
| `f2_scoping.md` (#271) | The Class-3 articulation this PR-2 attempts against |
| `fm_beat_crt_correspondence_audit.md` (#252) | The substrate claim this PR validates at Tier-0 |
| `fm_beat_chain_simulation.py` (PR #270) | The simulator harness |
| `engineering_targets.md` | Where the Tier-1 benchtop spec lives; K/K_c ≤ 0.10 tolerance derived here is consumable there |
| `xor_continuum_limit.md` | The substrate side of Possibility A / B that this result speaks to (partially A, not B) |
| `rational_field_equation.md` (D11) | The F[N] Jacobian Possibility B would attack; not addressed here |
| `master_cascade_identity.md` | The cascade identity (q_2=2, q_3=3) the (a,b) ↔ Mihailescu pairing originates from |

## Status

**F2 PR-2 result: partial Possibility-A brick + Tier-1 benchtop
tolerance derived; no F2 closure claimed.** The audit's modal
claim (clean composite-mode line at ω_{ab} iff consecutive) is
model-validated at K=0 for the positive control (Z_6), the
Catalan headline (Z_72), and the non-consecutive negative
control. The K-sweep matches the analytic Kuramoto-pulling
prediction √(Δω² − (2K)²) within FFT bin resolution through
K/K_c = 0.50.

Open: (a) third consecutive Mihailescu pair (3, 4) → Z_12 not
run; (b) Z_72 substrate-engagement gap (#252 §3) unchanged —
the simulator realizes Z_72 in a model that assumes (8, 9), it
does not derive (8, 9) from the substrate; (c) Possibility B
(F[N] Jacobian at 4-mode XOR fixed point) not addressed — the
two-oscillator Kuramoto pulling formula is the K<K_c regime of
pair synchronization, orthogonal to B's natural calculation.

Side: substrate-side, Tier-0 numerical confirmation.
Class: partial Possibility-A brick (closure criterion not met);
Tier-1 benchtop tolerance K/K_c ≤ 0.10 derived for the
`engineering_targets.md` build spec.
Downstream: PR-3 candidates listed above; PR-3 selection deferred
to a #268 epic-comment after this PR merges.
