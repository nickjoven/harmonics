# Klein-bottle bridge: audit + minimal probe

## What this file is

Combined deliverable for the user's instruction "audit existing
Klein-bottle code carefully + implement bridge + run C2 probe."

The audit revealed structural complications I'd underestimated;
the minimal probe surfaces a parallel multi-candidate ansatz
problem. The honest landing is **the bridge alone cannot close
C2** — it needs to be combined with an (α, β) forcing argument
that I separately tagged as needing real derivation work.

## Audit findings (path 2)

### What exists in the framework

Verified by reading source:

| File | Klein-bottle content |
|---|---|
| `klein_bottle_kuramoto.py` (349 lines) | 2D Kuramoto on Klein-BC lattice (Nx ≥ 3 needed); outputs `\|r\|`, `<∂x>`, `<∂y>`, lattice phase pattern, x-differences |
| `klein_kuramoto_sweep.py` (350 lines) | K-sweep on 5×5 Klein vs torus; measures `\|r\|`, gradient ratios, dominant rationals, (2,3) vs (3,2) sector asymmetry |
| `klein_topological_keff.py` (418 lines) | Establishes `\|r\| ≡ 0` on Klein bottle; W_x = 1/2 from antiperiodic twist; K_eff = K_0/2 |
| `klein_within_sector.py` (215 lines) | Field equation has exact (f_1, f_2) ↔ (f_2, f_1) symmetry; asymmetry comes from Kuramoto twist not field equation |
| `klein_phase_diagram.py`, `klein_slip_structure.py`, `klein_symmetric_coupling.py`, `klein_connection.md`, `klein_bottle_tower.py`, `klein_device_exploration.py` | Phase diagrams, slip structure, connection 1-form, multi-scale tower, device exploration |

### What is genuinely missing

Confirmed: **no existing code computes Klein-antipodal sym/antisym
eigenmode populations**. Search for `psi_+`, `psi_-`, `w_+`, `w_-`,
"sym antisym", "Klein singlet" returned no eigenmode-projection
implementations. Bridge IS genuinely missing.

### Structural alignment issue I hadn't noticed

The audit surfaced a derivation-alignment question I had glossed
over:

- **Framework's Klein-Kuramoto BC** (`klein_bottle_kuramoto.py`):
  twist+reflect in **x-direction** (Z_2 axis of the lattice).
- **Z_6 antipodal action used in partition formula**
  (`baryon_fraction.md`, `omega_b_residual_phase_a.md`):
  `k → -k mod 6` acts on Z_6 = Z_2 × Z_3, which under the CRT
  decomposition fixes the Z_2 (x) coordinate and acts on the Z_3
  (y) coordinate as `j → -j mod 3`.

These are **different structural choices**. Both are valid
Klein-bottle structures (the Klein bottle has two fundamental
loops; either can carry the twist), but the bridge needs them
ALIGNED — the lattice's Klein twist must correspond to the
partition formula's antipodal action.

This is a **derivation alignment question**, not a code-writing
question. Resolving it requires choosing or deriving which axis
carries the Klein twist for the Z_6 mode-counting purposes. **A
substantive structural decision.**

### Critical existing constraint

`klein_topological_keff.py` established that `|r| ≡ 0` on the
Klein bottle from sym/antisym cancellation in the order parameter.
This is a **structural fact** that constrains the bridge:

- Sym contribution to `|r|`: nonzero (Klein-singlet retains coherent
  sum)
- Antisym contribution: cancels by sign-flip (sign-rep gives `|r| = 0`)
- Net `|r|` from full state: zero
- Effective mean field: topological winding W_x = 1/2

**Implication for C2**: w_+ and w_- can't both be Kuramoto
order parameters in the standard sense. The natural reading:

- w_+ ∝ sym Kuramoto order parameter (continuous in K)
- w_- ∝ topological invariant (W_x = 1/2 type, K-independent)

This is structurally cleaner than "two tongue widths" but tested
below.

## Minimal probe (path 1, conservative version)

Tested the two-component partition formula
(`omega_b_two_component_sketch.md` Step 3, α = β = 1) under three
fitting strategies. Each fits two of the three Planck observables
exactly and predicts the third.

### Test 1: `w_- = 1/2` (topological reading from `klein_topological_keff.py`)

```
w_+    Ω_b      Ω_DM     Ω_Λ
0.4    0.0230   0.2931   0.6839
0.6    0.0341   0.2784   0.6875
0.83   0.0466   0.2619   0.6915
1.0    0.0556   0.2500   0.6944
target 0.0493   0.2650   0.6847
```

**No value of w_+ matches all three observables when w_- is
pinned at 1/2**. The simplest topological reading fails.

### Test 2: Fit (Ω_b, Ω_Λ) exactly, predict Ω_DM

```
w_+ = 0.9241, w_- = 0.9100, δ = +0.0141
Ω_DM predicted: 0.2660 vs observed 0.2650 — 0.38% residual
```

Small asymmetry, third residual within Floor noise.

### Test 3: Three fitting strategies side-by-side

| Fit | (w_+, w_-) | δ | 3rd-observable residual |
|---|---|---|---|
| (Ω_b, Ω_Λ) | (0.924, 0.910) | **+0.014** | 0.38% on Ω_DM |
| (Ω_b, Ω_DM) | (0.918, 0.855) | **+0.064** | 0.15% on Ω_Λ |
| (Ω_DM, Ω_Λ) | (0.946, 0.929) | **+0.017** | 2.03% on Ω_b |

### What the probe shows

**Three different fits give three different (w_+, w_-) pairs and
three different δ values** ranging from +0.014 to +0.064 (4× range).
All three fits leave the third residual within ≤2% (within Floor
noise band).

This is **not closure** — it's **consistency with degenerate fit
parameters**. The two-component partition formula is consistent
with Planck data, but the data does NOT determine (w_+, w_-)
uniquely.

## What this means

The probe surfaces the **same multi-candidate ansatz pattern** as
the C5 β = 1/12 vs 1/(4π) audit. Three observations + 2 free
parameters (w_+, w_-) + ambiguous (α, β) give a multi-dimensional
manifold of consistent fits.

To close C2 structurally, we need BOTH:

1. **Bridge implementation**: compute (w_+, w_-) from Klein-bottle
   substrate dynamics directly, not by fitting Planck. This
   requires the structural alignment resolution above.

2. **(α, β) forcing**: derive the specific partition formula
   coefficients from a mode-flow theorem on the Klein lattice,
   analogous to the down-type Phase D resolution
   (commit `fa7515f`).

**Either alone is insufficient.** Without the bridge, (w_+, w_-)
are fit parameters. Without (α, β) forcing, the partition formula
is an ansatz. Both together would give a structural prediction.

## Status of "is C2 closeable?"

The question reframes:

| Component | Status |
|---|---|
| Klein-bottle dynamics (Kuramoto on lattice) | **EXISTS** in framework |
| Eigenmode decomposition of dynamics | **MISSING** but well-defined; needs alignment |
| (w_+, w_-) extraction from dynamics | **MISSING**; requires alignment + projection |
| Partition formula (two-component generalization) | **EXISTS** in `omega_b_two_component_sketch.md` |
| (α, β) forcing | **MISSING**; requires mode-flow derivation |

Two separate missing pieces, not one. The roadmap's "200-400
line bridge" estimate was for piece (3) alone; the real closure
needs (3) AND (5).

## Honest verdict on C2 closeability

**Closeable in principle**: the framework has all the structural
machinery needed (Klein dynamics, partition formula, eigenmode
catalog). The two missing derivations are well-scoped:

- **Bridge derivation**: pick alignment (which axis carries the
  Klein twist for Z_6 partition purposes), implement eigenmode
  projection, extract (w_+, w_-). ~400-600 lines + structural
  decision.
- **(α, β) forcing**: derive partition coefficients from mode-flow
  theorem (analogous to down-type Phase D's S_3 orbit dimensions).
  Requires real derivation work, ~3-5 hours focused if pattern
  applies.

**Not closeable in this session**: both pieces require structural
decisions and derivations that exceed implement-and-run scope.

The minimal probe shows the framework would CONFIRM closure (data
is consistent with (w_+, w_-) at 1% level) — but not VERIFY it
(closure isn't unique without the missing derivations).

## Comparison to current state

| Closure attempt | Mechanism | Tier 1 (mechanism) | Tier 2 (params) |
|---|---|---|---|
| Original Floor | "structural residual" | Class 4 (5-way confirmed) | N/A |
| C5 single-w | w(z) runs with H(z) | Class 4 candidate | Class 2 (β multi-candidate) |
| C2 two-component | (w_+, w_-) split | **Class 4 candidate** | **Class 2 (multi-fit, α,β unforced)** |

C2 reproduces the same Tier 1 / Tier 2 split as C5 — both have
substantive mechanisms with unforced parameters. The audit
revealed they're symmetric in this respect, not that C2 is
strictly better than C5.

## What this changes about the work map

`remaining_gap_shapes.md` Shape A.2 (Ω_b) status updates:

- **Pre-this-audit**: "first remaining substrate-side structural
  gap; recommended next probe is C5 z-dependent w."
- **Post C5 attempt**: "C5 mechanism Class 4, β value Class 2
  (1/12 vs 1/(4π) ansatz)."
- **Post C2 sketch**: "C5 and C2 are dual; both close at
  Class 4-mechanism + Class 2-parameters."
- **Post this audit + probe**: "Closure requires TWO separate
  derivations (bridge + (α,β) forcing); neither completable in
  this session; framework has all structural pieces."

The Ω_b residual remains genuine substrate-side work, with two
specific derivations identified as the needed advances.

## Recommendation

The disciplined honest landing:

1. **Don't try to brute-force the bridge implementation** without
   resolving the structural alignment first. The 400-600 line
   estimate was for the TECHNICAL implementation; the alignment
   decision is a SEPARATE structural choice with its own audit
   needed.

2. **Tag both required derivations explicitly** in the framework's
   open list:
   - **Klein-axis alignment for Z_6 partition**: which axis of
     the Klein-bottle BC corresponds to the antipodal action
     `k → -k mod 6`?
   - **(α, β) mode-flow forcing**: derive partition coefficients
     from Klein lattice orbit-dimension counting.

3. **Move to other shapes** (Shape C re-audit, Shape D paths c/d,
   Shape F primitive completeness) which have less ambiguity per
   probe.

4. **Mark Ω_b status**: substrate-side closure available in
   principle, requires two non-trivial derivations, both
   well-scoped but neither single-session.

This is the cleanest honest landing. The user asked me to
implement and audit; the audit revealed implementation requires
prior structural decisions; the minimal probe confirms data
consistency without uniqueness.

## Cross-references

- `omega_b_two_component_sketch.md` — partition formula being
  tested
- `omega_b_c5_closure.md`, `omega_b_c5_beta_audit.md` — parallel
  C5 attempt (same Tier 1 / Tier 2 split)
- `klein_dynamics_roadmap.md` — earlier roadmap; this audit
  refines the implementation estimate
- `klein_bottle_kuramoto.py`, `klein_kuramoto_sweep.py` — existing
  Klein-Kuramoto dynamics
- `klein_topological_keff.py` — `|r| ≡ 0` constraint
- `klein_within_sector.py` — sector-asymmetry mechanism
- `continuity_in_K_nulls.md` — N9-N16 nulls; this audit closes
  on similar ground
- `vocabulary_is_the_work_pattern.md` — disambiguation pattern;
  this is NOT a new instance (the "vocabulary" is correct,
  the derivations are missing)
- `down_type_double_cover_phase_d` (commit `fa7515f`) — precedent
  for orbit-dimension forcing of mode-flow coefficients
- `ansatz_audit_policy.md` — Step 4 default applies (multi-fit
  candidates without forcing → Class 2)
- `framework_status.md` Ω_b entry — needs update to reflect
  two-derivation requirement

## Status

Audit + minimal probe complete. Honest landing: C2 closure is
possible in principle, requires two well-scoped but non-trivial
derivations not completable in single session. Ω_b residual
remains substrate-side genuine open work.
