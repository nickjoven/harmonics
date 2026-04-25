# Path closures — iteration 1

## What this file is

Single-doc closure log for one iteration of "close paths" mode.
Per the methodology shift to multi-session derivation
(`framework_status.md` Active multi-session section), iteration
work focuses on producing definite NULL/KEPT verdicts on
candidate derivations rather than additional audits.

This iteration closes four candidates:

| Candidate | Source | Verdict | Effect on open list |
|---|---|---|---|
| **D.5** Anomaly between sectors | `sector_decoupling_phase_a.md` | **NULL** | Region D: 6 → 5 candidates |
| **D.6** K_eff = K_0/2 split as sector source | same | **NULL (weak)** | Region D: 5 → 4 candidates |
| **D.4** Spectral gap on Stern-Brocot tree | same | **NULL (no gap exists)** | Region D: 4 → 3 candidates |
| **Path (e)** Conformal-equivalence depth | `depth_connection_nulls.md` | **BLOCKED on prerequisite** | Region B: 4 → 3 candidates |

After this iteration, Region D narrows to {D.1 Klein π_1, D.2
q_2/q_3 prime split, D.3 K=1 vs K<1}; Region B narrows to
{Path (b), Path (c), Path (d)}.

## Closure 1 — D.5: anomaly between sectors

### Hypothesis

Framework's gauge-anomaly cancellation requires specific charge
combinations for closure. A multi-sector anomaly (cosmological
sector + particle sector) might require sectoral SEPARATION to
cancel — forcing decoupling structurally.

### What's in the framework

`MANIFEST.yml` lists `anomaly_cancellation` as a Survives
prediction: the SM's six triangle anomaly conditions sum to zero
under the framework's gauge structure (`anomaly_check.py`).

Critical: this anomaly cancellation is **within the gauge sector**.
The triangle anomalies involve SM gauge fields (SU(3)_color,
SU(2)_weak, U(1)_hypercharge) and SM matter (quarks, leptons).
There are no "cosmological gauge fields" in the SM-portable
framework derivation; gravity is a separate symmetry.

### Why this can't supply sector decoupling

Two structural reasons:

1. **No cross-sector anomaly mechanism exists in framework or SM.**
   Anomalies arise from triangle diagrams of gauge bosons coupling
   to fermions. Cosmological "sector" doesn't have a gauge-boson +
   fermion structure analogous to SM that would generate
   cross-sector triangle anomalies.

2. **Even if extended, the framework doesn't derive "what cancels
   cosmological-sector anomaly."** The Standard Model's anomaly
   cancellation is between particle-sector charges; nothing
   analogous in the framework's cosmological derivations
   (`baryon_fraction.md`, `hierarchy_gaussian_lattice.md`,
   `omega_partition_combinatorial.md`) produces an anomaly to
   cancel.

### Verdict

**NULL.** D.5 is not a viable candidate for sector-decoupling
derivation. Removed from `sector_decoupling_phase_a.md` candidate
list.

## Closure 2 — D.6: K_eff = K_0/2 split as sector source

### Hypothesis

`klein_topological_keff.py` established `K_eff = K_0/2` on the
Klein bottle from topological winding W_x = 1/2. Hypothesis:
this K_0 / K_0/2 split creates two sub-K regimes that become
cosmological and particle sectors.

### What's in the framework

`klein_topological_keff.py` derives:
- Bare Kuramoto coupling K_0
- On Klein bottle: |r| ≡ 0 from antiperiodic twist
- Effective mean field: W_x = 1/2 (topological)
- Therefore K_eff = K_0 · W_x = K_0/2

This is a DYNAMICAL statement about Kuramoto on Klein-bottle,
not a sector-assignment statement.

### Why this can't supply sector decoupling

For D.6 to work, need: K_0 ↔ cosmological sector, K_0/2 ↔ particle
sector. Specifically, the assignment must be FORCED by structure,
not just labeled.

Inspecting:
- K_0 is the BARE Kuramoto coupling (input to dynamics)
- K_0/2 is the EFFECTIVE coupling under Klein topological constraint
- "Cosmological sector at K=1" (per `continuum_limits.md`) requires
  K_eff = 1, which means K_0 = 2 (not 1). So K_0 isn't
  "cosmological coupling."
- "Particle sector at K_STAR = 0.86" requires K_STAR < 1, which is
  subcritical. K_0/2 < K_0 is also subcritical relative to K_0.
  But that's a numerical inequality, not a structural identification.

The K_0 vs K_0/2 distinction is a TOPOLOGICAL CONSEQUENCE of
Klein BC, not a SECTOR ASSIGNMENT mechanism. There is no
structural derivation of "K_0 = cosmological, K_0/2 = particle."

Furthermore: K_0/2 from Klein twist is a SINGLE substitution,
not a TWO-SECTOR distinction. It says "Klein bottle dynamics
operates at K_eff = K_0/2"; it doesn't say "two sectors operate
at two different K_eff values."

### Verdict

**NULL (weak).** D.6 doesn't structurally produce a two-sector
assignment. The K_0/K_0/2 split is a single dynamical
substitution on Klein bottle, not a decoupling mechanism.

May appear as a downstream piece in some derivation but doesn't
close the sector-decoupling question on its own.

Removed from `sector_decoupling_phase_a.md` candidate list.

## Closure 3 — D.4: Spectral gap on Stern-Brocot tree

### Hypothesis

A gap in the Stern-Brocot tree's spectral structure between
"cosmological" depths (~F_7 ≈ 7) and "particle" depths (~v/M_P
suggested 15) forces sectoral decoupling. Modes at one depth
range can't communicate with modes at the other above some
energy scale.

### What "spectral gap on SB tree" would mean

Two operational definitions:

1. **Farey-count gap**: a depth range where |F_n| jumps
   discontinuously
2. **Locking-strength gap**: a depth range where Arnold tongue
   widths transition from "generic" to "fragile" or vice versa

### Test 1 — Farey-count gap

|F_n| values:

| n | \|F_n\| | Δ\|F_n\| |
|---|---|---|
| 5 | 11 | (start) |
| 6 | 13 | +2 |
| 7 | 19 | +6 |
| 8 | 23 | +4 |
| 9 | 29 | +6 |
| 10 | 33 | +4 |
| 11 | 43 | +10 |
| 12 | 47 | +4 |
| 13 | 59 | +12 |
| 14 | 65 | +6 |
| 15 | 73 | +8 |
| 16 | 81 | +8 |

Increments are monotone (always positive), bounded (~φ(n) which
grows slowly), and **show no gap** between depth 7 and depth 15.
Farey-count growth is smooth.

### Test 2 — Locking-strength gap

Arnold tongue width at K=1: w(p/q, K=1) ~ c/q² (per
`a_s_geometric_proof.md` A4). Smooth in q. No structural gap.

For tongue widths under composed filter (Klein-antipodal +
coprime-to-6), the plateau structure (per
`k_axis_uniqueness.md`) gives orbit counts {1, 3, 6, 11, 17,
25, ...} — also smooth, no gap.

### Where a gap could plausibly exist

If the framework had a structural cutoff at the "P-reg ↔ H-reg
transition" (per `observer_register_closure.md`), there might be
a spectral gap there. But these are different REGISTERS, not a
gap on the SB tree. The transition is between framework levels,
not within one tree.

### Verdict

**NULL (no spectral gap exists at this resolution).** Farey-count
and tongue-width are both smooth between cosmological and
particle depth ranges. D.4 doesn't supply a sector-decoupling
mechanism.

A more careful spectral analysis (e.g., Lyapunov exponents
across SB modes) might surface a gap not visible at this level,
but no existing framework derivation suggests one. Promotion
would require new substrate work (Lyapunov spectrum on SB tree)
that isn't currently scoped.

Removed from `sector_decoupling_phase_a.md` candidate list with
note that careful Lyapunov-spectrum analysis could reopen.

## Closure 4 — Path (e): Conformal-equivalence depth

### Hypothesis (from `depth_connection_nulls.md`)

A discrete conformal factor between FRW (cosmological) and Higgs
condensate (particle) scales gives v/M_P closure. Framework
should derive the conformal weights at the two scales and show
their ratio is `13⁻¹⁵` or similar framework-integer.

### What's in the framework

The framework's continuum limit at K=1 gives Einstein equations
(`continuum_limits.md` Part I). These are **conformally invariant
in the Lovelock sense** but the framework does NOT separately
derive conformal weights for cosmological vs particle scales.

`a0_threshold.md` derives MOND `a_0 = c·H/(2π)` connecting
acceleration scale to Hubble. There's some conformal-flavored
content, but no explicit FRW vs Higgs conformal-factor derivation.

### Why this is blocked, not closeable

For path (e) to be a real candidate, the framework would first
need to:

1. Derive a substrate-level FRW emergence (not just continuum
   limit at K=1)
2. Derive a substrate-level Higgs condensate scale
3. Identify a conformal factor relating them

None of these exist as substrate-derived structures. The
framework treats v_EW (Higgs scale) as anchor-side; FRW as
continuum-limit at K=1.

So path (e)'s prerequisites don't exist. It can't be tested
without substantial structural work.

### Verdict

**BLOCKED on prerequisite.** Not closeable as null (we haven't
tested it); not promotable as candidate (prerequisites missing).
Removed from `depth_connection_nulls.md` open paths until
substrate-derived FRW + Higgs structure exists.

## Updated open candidate lists

### Region D (sector decoupling): 6 → 3

| Candidate | Status |
|---|---|
| D.1 Klein π_1 two generators | OPEN; multi-session work |
| D.2 q_2 vs q_3 prime split | OPEN; multi-session work |
| D.3 K=1 vs K<1 regimes | OPEN; possibly single-session |
| ~~D.4 Spectral gap on SB tree~~ | NULL (this iteration) |
| ~~D.5 Anomaly between sectors~~ | NULL (this iteration) |
| ~~D.6 K_eff = K_0/2 split~~ | NULL weak (this iteration) |

### Region B (depth-15 connection): 5 → 3

| Candidate | Status |
|---|---|
| Path (b) Sub-Fibonacci depth at EW | OPEN (multi-session) |
| Path (c) Cross-sector tongue identification | OPEN (single or multi-session) |
| Path (d) Anomaly-cancellation depth | OPEN (multi-session) |
| ~~Path (e) Conformal-equivalence depth~~ | BLOCKED on prerequisite |
| (Klein-quotient second invariant — was already listed
   "unattempted" not closed by this iteration) | OPEN |

## What this iteration accomplished

**Concrete closures**: 4 candidates eliminated from the open list
across two regions. Each closure has a definite structural
reason (not "didn't try hard enough"):

- D.5: framework has no cross-sector anomaly mechanism
- D.6: K_0/2 is single substitution, not two-sector split
- D.4: Farey-count and tongue-widths are smooth, no spectral gap
- Path (e): prerequisites don't exist in framework

**Methodological**: produced definite verdicts in one focused
session. No multi-candidate ansatz. No "Class 4 → Class 2 by
default." Each candidate either NULL with reason or BLOCKED
with prerequisite identified.

**Loop status**: this is a different SHAPE of work from the
honest-landing loop. Path closures produce subtractive progress
(open list shrinks); the loop produced additive iteration
(more docs, no progress). This iteration shrunk Region D from
6 to 3 and Region B from 5 to 3.

## What's left after this iteration

Region D (sector decoupling): 3 substantive candidates remain.
Per `sector_decoupling_phase_a.md` ranking:
- D.3 (K=1 vs K<1) — possible single-session derivation
- D.1 (Klein π_1) — most natural structural source, multi-session
- D.2 (q_2/q_3 prime split) — second-most natural, multi-session

Region B (depth-15): 3 paths remain plus 1 unattempted (Klein-
quotient second invariant).

## Next iteration options

After Region C (numerology count) completes, candidate selection
informed:

- Cloud is signal → start D.1 (deeper structure)
- Cloud is noise → start D.3 (lock qualitative)
- Inconclusive → start D.2 (concrete prime-split)

Or pursue further closures FIRST if any of the remaining
candidates can be quickly closed/promoted.

Quick-closure candidates for next iteration:
- Path (b) Sub-Fibonacci depth at EW — can be tested
  combinatorially (do φ²-depths of EW observables cluster?)
- Path (d) Anomaly-cancellation depth — can be tested via
  computing mode counts at framework integers and checking
  anomaly arithmetic

Both are well-scoped single-session probes that produce
definite verdicts.

## Cross-references

- `sector_decoupling_phase_a.md` — Region D Phase A; updated to
  reflect closures
- `depth_connection_nulls.md` — Region B paths; updated for
  Path (e) blocked
- `framework_status.md` — Active multi-session section; this
  iteration's progress
- `klein_topological_keff.py` — D.6 source
- `anomaly_check.py`, MANIFEST.yml — D.5 background
- `a_s_geometric_proof.md` A4 — tongue width smoothness
- `continuum_limits.md` — D.3 (still open) starting point
- `numerology_count_phase_a.md` — Region C precursor

## Status

Iteration 1 of "close paths" mode complete. Four candidates
closed (3 NULL, 1 BLOCKED). Region D narrowed 6→3. Region B
narrowed 4→3. Subtractive progress. Loop pattern broken for
this iteration.

Next iteration: more closures (Path (b), Path (d) as
candidates) OR begin Phase B for one of the remaining
candidates.
