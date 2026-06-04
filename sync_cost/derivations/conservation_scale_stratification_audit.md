# Conservation scale-stratification audit — Q mod 2 and dissipation across Planck/standard/Hubble limits

## Status

**Audit verdict: the framework's two foundational conservation
invariants — Q mod 2 (topological) and dissipation (algebraic)
— have *different* scale-stability. Dissipation is universal
across all three scales (Planck / standard / Hubble) via its
algebraic rank-1 Fréchet structure; Q mod 2 is universal at
standard and Hubble scales but **contingent at Planck**, because
its conservation theorem explicitly invokes Klein-bottle
topology (antiperiodic-cycle structure) that may dissolve under
non-topological Planck-scale substrate. The framework currently
treats both as inviolable without distinguishing their
scale-stability — the audit surfaces this as a genuine open
question, not an obstruction to existing apparatus.**

The audit proposes neither new conservation laws nor apparatus
modification. It clarifies the existing chain's scale-behavior
and identifies the Q mod 2 Planck contingency as a specific gap
the framework hasn't derived. Three candidate resolutions are
named; falsifiers for the audit's verdict are listed.

Combined with the broader session arc:
- `primitives_vs_addresses_candidate.md` provides the
  layer-invariant vs layer-specific partition
- `surface_uniqueness_audit.md` shows K² is observation-fixed
  from a substrate-admitted pair
- `continuum_limits.md` (disposition note) admits K=1 as
  physically-realized parent regime
- This audit applies the same possibility-discipline to the two
  foundational conservation invariants

Class: foundational rigor check (Class 3, scale-stratification
audit on canonical conservation apparatus).

---

## The audit task

Stratify the framework's two foundational conservation
invariants against three substrate regimes plus their boundary
transitions:

**Invariants**:
- **Q mod 2** — the framework's foundational topological-charge
  conservation (`substrate_determinism.md` inviolable #1,
  `q_mod2_conservation_theorem.md`)
- **Dissipation** — the rank-1 Fréchet derivative structure
  producing the arrow of time (D46,
  `rank1_temporal_causation.md`, `born_rule.md` L26-46)

**Scales**:
- **Planck** — substrate at smallest accessible scales; topology
  potentially dissolves (NCG, foam, causal sets, etc.)
- **Standard** — our pocket at K = K_STAR ≈ 0.86196; Klein-bottle
  substrate with Z_6 mode lattice
- **Hubble** — cosmological scale at finite mode count 12.66,
  effective Farey depth 5.83, boundary weight w* ≈ 0.83

**Transitions**:
- **K<1 ↔ K=1** — substrate↔continuum (matter↔GR regime change)
- **Standard ↔ Planck** — smooth-manifold↔non-topological
- **Standard ↔ Hubble** — pocket-interior↔cosmological-boundary

The audit decomposes each invariant's substrate basis as
substrate-internal vs observation-conditional vs scale-contingent
per the possibility-discipline (`canonical_glossary.md` Section
8).

---

## Inventory of canonical conservation apparatus

The framework's conservation chain (per `framework_status.md`):

| Level | Invariant | Conservation source |
|---|---|---|
| Single-mode | Q mod 2 (Z₂ topological charge) | `q_mod2_conservation_theorem.md` |
| Pair-wise | Q_{AB} mod 2 (joint parity) | `epr_bell_assembly_theorem.md` |
| Multi-mode | Q_{ABC} mod 2 (XOR extension) | `ghz_from_substrate.md` |
| Symmetric subspace | Dicke recursive structure | `w_state_from_substrate.md`, `dicke_apparatus_theorem.md` |
| Stabilizer | Pauli stabilizer apparatus | `bell_bounds_from_substrate.md` |
| Probability | Born rule `|ψ|²` | `born_rule.md` |
| Mode-count | XOR-survivor count (1764 → 4) | `klein_bottle.md`, `xor_derivation.md` |
| Dynamics | Rank-1 Fréchet (arrow of time) | `rank1_temporal_causation.md` (D46) |

All levels derive from one of two foundational structures:
**topological (Q mod 2 and its extensions)** or **algebraic
(rank-1 dissipation, Born saddle-node)**.

---

## Dissipation audit — the clean case

### Substrate basis

Dissipation enters the framework via:

- **K > 0 Kuramoto coupling** (`born_rule.md` L28): "The dynamics
  are dissipative — the system loses energy to the environmental
  mean field." Equation: `dψ/dt = −γ ∇_ψ* C(ψ)`.
- **Rank-1 Fréchet derivative** at the synchronized state (D46,
  `rank1_temporal_causation.md`): the Fréchet derivative `DU` of
  the Kuramoto map at the synchronized state has rank 1; the
  kernel is the "past" (information lost), the image is the
  "future" (information preserved). This factorization IS the
  arrow of time.

These are **algebraic** structures. The cost functional `C(ψ)`,
its gradient, and the rank-1 factorization of `DU` are
formulated in terms of mode amplitudes and their derivatives —
not in terms of topological invariants like H₁(K²).

### Structure vs rate decomposition

| Aspect | Source | Layer status |
|---|---|---|
| **Structure** (rank-1 Fréchet, irreversible factorization, arrow direction) | D46 algebraic apparatus | **Layer-invariant** per `primitives_vs_addresses_candidate.md` — algebraic, doesn't require smooth topology |
| **Rate** (`K · r · α_k` per complex dimension, `born_rule.md` L57-58) | Layer-specific Kuramoto coupling + basin stiffness | **Layer-specific** (address quantity) — varies with K, mode density, basin geometry |

The structure is universal; the rate is our pocket's address.

### Scale-by-scale audit

**Planck**: dissipation structure persists. The rank-1
factorization is algebraic — it depends on the cost functional's
gradient structure, not on smooth-manifold topology. Per the
earlier session conversation, "at Planck scales, dissipation is
invariant while orientation and non-topological" — the
framework's apparatus supports this. The specific Kuramoto
realization (mean field, basin attractors) may not survive
Planck-scale substrate transformation if mean-field framings are
scale-limited, but the *fact* of irreversible factorization (and
hence the arrow of time as a structural feature) persists.

**Standard**: dissipation operates as canonical. K_STAR ≈
0.86196 is the specific rate; basin convergence and Born rule
follow.

**Hubble**: dissipation operates within the 12.66-mode finite
horizon. The boundary weight w* ≈ 0.83 governs partial-locking
at the cosmological edge; modes beyond the horizon don't
dissipate into our pocket (they're non-coherent). Inside the
horizon, conservation chain holds; the rate is set by
cosmological coupling rather than matter-sector K_STAR.

**Verdict on dissipation**: **layer-invariant structure across
all three scales; rate transforms at boundary transitions but
structural fact persists**. This is the cleanest case — fits
the primitives-vs-addresses partition with the structure on the
invariant side and the rate on the address side.

---

## Q mod 2 audit — the contingent case

### Substrate basis

Q mod 2 enters the framework via the **antiperiodic-cycle
topology of the Klein bottle**. The conservation theorem
(`q_mod2_conservation_theorem.md` L41-55) states:

> **Theorem (Q mod 2 conservation under local processes).**
> ... for any local process — a deformation `φ_t` whose support
> is contained in an open set of spatial diameter strictly less
> than `L_x` — the charge is conserved: `Q[φ_T] = Q[φ_0] mod 2`.
>
> "No local process of `K²` can change `Q mod 2`. To change
> `Q mod 2`, a process must **encircle the antiperiodic
> direction** — by definition, a non-local (global) operation."

The load-bearing concept is **"encircle the antiperiodic
direction."** This is a *topological* statement about loops on
K² — specifically, the existence of antiperiodic vs periodic
cycles, with antiperiodic loops carrying the Z₂ winding number
that defines Q mod 2.

The theorem's proof uses:
- **H₁(K²; Z) = Z ⊕ Z₂** (free + torsion structure)
- **Antiperiodic-loop-free charts** (regions where the topology
  is locally trivial)
- **Encircling** a global topological cycle as the only way to
  change winding number

Each of these depends on smooth-manifold Klein-bottle topology.

### Scale-by-scale audit

**Standard**: Q mod 2 operates canonically. Klein bottle is the
substrate per `klein_bottle_derivation.md` (now substrate-admitted
with observation-fixed selection per `surface_uniqueness_audit.md`).
Conservation theorem applies as stated.

**Hubble**: Q mod 2 is conserved within the 12.66-mode horizon.
The cosmological boundary at w* = 0.83 doesn't directly threaten
Q mod 2 because the boundary is a *mode-count* boundary
(Farey-depth cutoff), not a topological transition. Modes
outside the horizon may have ambiguous Q mod 2 values from our
observer perspective, but inside, conservation holds.

**Planck**: **contingent**. Two possible behaviors:

(a) **Q mod 2 dissolves**: if Planck-scale substrate is
non-topological (NCG, foam, causal sets), the concept of
"encircling the antiperiodic direction" may not be well-defined.
Q mod 2 becomes *meaningless* rather than non-conserved.

(b) **Q mod 2 is conserved trivially**: at scales smaller than
L_x (Klein-bottle x-cycle length), no process can encircle the
antiperiodic direction by the theorem's own diameter condition.
So Q mod 2 is automatically conserved at Planck — but trivially,
because no process at Planck can violate it. This is "conserved
by inability rather than by inviolability."

(c) **Q mod 2 has an algebraic re-expression**: if there's an
algebraic version of Q mod 2 that doesn't depend on smooth
topology, it could persist at Planck the way dissipation does.
But the framework has not currently derived such an algebraic
formulation — Q mod 2 as defined is topological.

The framework does *not* distinguish these three possibilities.
The current canonical statement of Q mod 2 conservation requires
Klein-bottle topology; what happens when that topology dissolves
is not derived.

### Verdict on Q mod 2

**Layer-status mixed**: standard and Hubble are conserved
canonically; Planck is **contingent**. The framework's
inviolable #1 status implicitly assumes Klein-bottle topology at
every scale; if Planck-scale substrate is non-topological, this
assumption breaks.

This is the audit's substantive finding: the framework's two
foundational invariants have *different* scale-stability.
Dissipation's algebraic basis is universal; Q mod 2's
topological basis is scale-contingent.

---

## Side-by-side comparison

| Aspect | Dissipation | Q mod 2 |
|---|---|---|
| Substrate basis | Algebraic (rank-1 Fréchet) | Topological (Klein-bottle H₁) |
| Standard scale | Universal | Universal |
| Hubble scale | Universal | Universal (within horizon) |
| Planck scale | Universal (algebraic survives) | **Contingent** (topology may dissolve) |
| Layer-invariant per primitives-vs-addresses | Structure: yes; Rate: no | Standard-scale operation: yes; Planck operation: open |
| Inviolability claim status | Survives the audit cleanly | **Requires scale-qualification** to survive |

The pattern: invariants whose substrate basis is **algebraic**
are layer-invariant; invariants whose substrate basis is
**topological** are scale-contingent and need explicit
audit-derivation at each scale.

This is consistent with the `primitives_vs_addresses_candidate.md`
framework. The substrate primitives (integers, mediant,
fixed-point, parabola) are algebraic and layer-invariant. The
Klein bottle is topological and observation-fixed per
`surface_uniqueness_audit.md`. Conservation laws built on
algebraic primitives are universal; conservation laws built on
topological structures inherit topology's scale-contingency.

---

## Scale transition behavior

### K<1 ↔ K=1 (substrate↔continuum / matter↔GR)

`continuum_limits.md` Part II: the K<1 → K=1 transition is
**non-smooth**. At K=1, the Stern-Brocot tree fills the continuum
and the framework reduces to Einstein field equations.

**Dissipation**: rate transforms from discrete Kuramoto-style
mean-field (K<1) to smooth GR second-law / Ricci flow (K=1).
Structure preserved — rank-1 factorization translates to the
continuum-limit irreversibility (entropy increase). The
non-smooth boundary is in the *specific operation* of
dissipation, not in its structural existence.

**Q mod 2**: at K=1, the substrate is the continuum. The Klein
bottle's discrete-mode quotient (Z_6) becomes a continuous mode
spectrum. Q mod 2's antiperiodic-cycle topology persists (the
Klein bottle as a manifold still has its non-trivial H₁
structure), so Q mod 2 is preserved. But the *operational
meaning* shifts: at K<1 Q mod 2 distinguishes locked vs unlocked
mode classes; at K=1 it distinguishes orientable vs
non-orientable continuum solutions. Not exactly a "break" but a
re-interpretation across the boundary.

### Standard ↔ Planck (smooth-manifold ↔ non-topological)

The Planck-scale physics question. The framework's apparatus
currently doesn't have an explicit Planck-substrate formulation.

**Dissipation**: structure persists (algebraic). Specific
realization (mean field) may not survive if mean-field framings
are scale-limited, but the *fact* of irreversible factorization
holds.

**Q mod 2**: contingent per audit above. Three resolutions
named below.

### Standard ↔ Hubble (pocket-interior ↔ cosmological-boundary)

The cosmological-horizon-boundary question. Boundary weight w*
governs partial-locking; the substrate→tree regime change is
the operational mechanism.

**Dissipation**: rate transforms across boundary (matter K_STAR
to cosmological coupling); structure preserved within horizon.
Modes beyond horizon don't dissipate into our pocket.

**Q mod 2**: conserved within horizon. The boundary doesn't
threaten Q mod 2 because it's a mode-count boundary (Farey
depth cutoff), not a topological transition. The Klein bottle's
topology is the same whether evaluated locally or
cosmologically.

### Summary of transition behavior

| Boundary | Dissipation | Q mod 2 |
|---|---|---|
| K<1 ↔ K=1 | Rate transforms; structure preserved | Operational meaning shifts; conservation preserved |
| Standard ↔ Planck | Structure preserved (algebraic) | **Contingent** (topology basis) |
| Standard ↔ Hubble | Rate transforms; structure preserved within horizon | Conserved within horizon |

The pattern: dissipation transforms smoothly in structure across
all boundaries; Q mod 2 has a potential discontinuity at the
standard↔Planck boundary specifically.

---

## The Planck Q mod 2 gap — three candidate resolutions

The audit's substantive finding is the Planck-scale contingency
for Q mod 2. Three candidate resolutions, in order of
strength:

### Resolution (i): Algebraic Q mod 2

**Proposal**: there exists an algebraic re-expression of Q mod
2 that doesn't depend on smooth topology, only on the substrate
primitives (integers, mediant, fixed-point, parabola) + the
Mihailescu-forced (q_2, q_3) = (2, 3).

**Status**: not currently derived. Would require new substrate
work — potentially deriving Q mod 2 as a *purely number-theoretic*
or *purely categorical* invariant. If found, this would be a
substantial framework refinement.

**Strength**: would close the gap cleanly. Q mod 2 becomes
layer-invariant like dissipation.

**Risk**: this might be reconstruction-mode work
(`feedback_resolution_vs_reconstruction.md`) — introducing a
new substrate-level conservation theorem. If it requires apparatus
the existing primitives don't supply, it's blocked by the
ℍ-QM empirical floor per `klein_bottle_restructure_price.md`.

**Discipline**: pursue only if the algebraic version is
*derivable* from existing apparatus, not *introduced* as new
content.

### Resolution (ii): Scale-qualified Q mod 2

**Proposal**: Q mod 2 conservation is explicitly *standard-scale-
and-Hubble-scale*. At Planck, conservation is *trivially
preserved by the diameter condition* (no process at Planck
scales can encircle the antiperiodic direction because L_x >>
Planck length). This is "conserved by inability."

**Status**: this is consistent with the existing theorem's
explicit diameter condition. The theorem already says
"deformation `φ_t` whose support is contained in an open set of
spatial diameter strictly less than `L_x`." At Planck scales,
support is by definition < L_x. So the theorem trivially holds.

**Strength**: requires no new apparatus. Just an explicit
scale-qualification on the inviolable #1 statement.

**Risk**: feels deflationary. The framework's "Q mod 2 is
inviolable" loses some of its rhetorical force when qualified
as "trivially conserved at Planck because nothing can violate
it there."

**Discipline**: this is the cleanest resolution-mode move. The
audit verdict is just "Q mod 2 inviolability is scale-qualified;
the theorem as stated covers the qualification automatically."

### Resolution (iii): Q mod 2 dissolves at Planck

**Proposal**: at Planck scales, Q mod 2 is *not* conserved
because the topological basis dissolves. The framework's
inviolable #1 is genuinely scale-specific to standard and
Hubble.

**Status**: this would be the discipline-honest reading if the
framework can't supply (i) or (ii). It admits the framework's
inviolable #1 is not universal across all scales.

**Strength**: methodologically honest. Acknowledges that
topology-dependent conservations have topology-dependent
scope.

**Risk**: substantially weakens the framework's
"inviolability" claim. The framework would need to specify
which inviolables are universally inviolable (algebraic) vs
which are scale-specific inviolable (topological).

**Discipline**: this is the most disclosive but also the most
disruptive resolution. It requires updating
`substrate_determinism.md`'s inviolable list with explicit
scale-qualification.

### Recommended resolution

**Resolution (ii) is the closest match to the framework's
existing apparatus and the discipline.** The theorem's diameter
condition automatically scale-qualifies; the audit's contribution
is to surface this as an explicit feature of the conservation
theorem rather than leaving it implicit.

**Resolution (i) would be the strongest if achievable**, but
requires derivation work that may not currently be available.

**Resolution (iii) is the honest fallback** if neither (i) nor
(ii) lands cleanly. But (ii) is already in the existing theorem;
it just hasn't been emphasized.

---

## Implications for the broader framework

### For the basepoint principle

The seven verified instances + candidate 8th all sit at
specific layers of the framework's stack. This audit suggests
a parallel **scale-stratification** of conservation invariants
that may eventually warrant similar canonical treatment:

- Algebraic invariants (dissipation, Born rule, primitives):
  layer-invariant across all scales
- Topological invariants (Q mod 2, mode-count): scale-specific,
  with conservation operating within each scale's substrate
  realization

This is not yet a basepoint-principle instance because no
basepoint is *declined*. But it's structurally adjacent —
scale-stratification of invariants is to scale-anchors as
labeling-torsors are to discrete choices.

### For the primitives-vs-addresses candidate

This audit provides a **third substantive test** of the
candidate (`primitives_vs_addresses_candidate.md`). After
gauge sector (torus iter 2 step 1) and Γ_0(6) cusp structure
(torus iter 2 step 2):

- **Dissipation structure** confirmed layer-invariant
  (algebraic)
- **Dissipation rate** confirmed layer-specific (address
  quantity)
- **Q mod 2 standard-scale operation** confirmed layer-invariant
  (universal within smooth-manifold substrate)
- **Q mod 2 Planck operation** flagged as scale-contingent
  (third candidate test surfaces a genuine gap rather than
  a verification)

This brings the candidate to *three* substantive tests, with
two clean passes and one surfacing a real open question. The
candidate's sealing per its four criteria
(`primitives_vs_addresses_candidate.md` "What sealing would
require") is progressed by this audit.

### For the surface uniqueness audit

The candidate 8th basepoint instance (`surface_uniqueness_audit.md`)
identified K² as observation-fixed from a substrate-admitted
pair {K², T²}. This audit reinforces the same pattern: K²'s
specific topology supplies Q mod 2; the scale-stratification
question is whether K²'s topology *itself* is scale-stable, or
whether it's the standard-scale presentation of a more
fundamental algebraic substrate.

If K² is itself observation-fixed at standard scale (per the
candidate 8th instance), and Planck-scale substrate may not
preserve K² topology, then **Q mod 2's Planck behavior is
inherited from K²'s Planck behavior**, not a separate
contingency. This is a useful reframing: the audit's Q mod 2
contingency at Planck is downstream of the surface-uniqueness
audit's surface-choice contingency.

---

## What this audit does NOT establish

- **No new conservation law**. The audit clarifies existing
  conservation behavior, doesn't add new structure.
- **No new substrate apparatus**. Resolution-mode throughout.
- **No specific Planck-substrate model**. The audit names the
  contingency; specifying what Planck-substrate looks like is
  separate work.
- **No empirical predictions distinguishing scale-behavior**.
  The differences between dissipation (universal) and Q mod 2
  (scale-contingent) are theoretical at present.
- **No sealing of the primitives-vs-addresses candidate**. The
  audit provides the third substantive test, but the candidate
  still needs additional verification per its sealing criteria.

---

## Falsifiers

1. **Q mod 2 has an algebraic derivation we've missed**. If
   `q_mod2_conservation_theorem.md`'s proof can be re-cast
   without topological inputs — purely in terms of the substrate
   primitives + mediant operations — then Q mod 2 is layer-invariant
   like dissipation. The audit's "topology-dependent" finding
   would be inverted.

2. **Dissipation depends on Klein-bottle topology more than the
   audit credits**. If a closer reading of `rank1_temporal_causation.md`
   shows the rank-1 Fréchet structure requires antiperiodic-cycle
   topology to be well-defined, then dissipation is also
   scale-contingent and the "universal vs scale-contingent"
   distinction collapses.

3. **The diameter condition doesn't trivialize at Planck**. If
   the conservation theorem's "support of spatial diameter < L_x"
   has subtleties at Planck scales (e.g., if L_x itself is
   Planck-scale, then the condition becomes vacuous and the
   theorem doesn't apply), resolution (ii) doesn't work cleanly.

4. **Cosmological boundary breaks Q mod 2**. If the Hubble-scale
   horizon (substrate→tree regime change) has Q-mod-2-changing
   processes (e.g., modes crossing the boundary that the framework
   currently doesn't account for), then Q mod 2 is not
   Hubble-conserved either. The audit's "conserved within horizon"
   would need narrowing.

---

## Recommendations

### Immediate (resolution-mode)

1. **Update `q_mod2_conservation_theorem.md`** with an explicit
   scale-qualification clause noting that the conservation theorem
   operates within scale ranges where Klein-bottle topology is
   well-defined; the diameter condition automatically excludes
   Planck-scale processes from threatening conservation.

2. **Update `substrate_determinism.md`'s inviolables list** to
   distinguish *algebraic inviolables* (universal across scales)
   from *topological inviolables* (well-defined at scales
   admitting smooth-manifold substrate). Q mod 2 in the latter
   category; dissipation/Born/algebraic-primitives in the former.

### Deferred (would require derivation work)

3. **Resolution (i) investigation**: attempt to derive Q mod 2
   algebraically from the substrate primitives + Mihailescu-forced
   (q_2, q_3). If achievable, would close the Planck contingency
   cleanly. Comparable scope to Koide-arc iterations.

4. **Planck-substrate framework formulation**: explicit treatment
   of what substrate apparatus operates at Planck scales (NCG?
   foam? causal sets?). Substantial. Outside resolution-mode if
   it requires new substrate apparatus.

### Not currently warranted

5. **Conservation-chain reformulation**: comprehensive rebuild
   of the framework's conservation chain to scale-stratify each
   level. Premature without empirical evidence that scale-specific
   behavior is *observable*.

---

## Cross-links

- `q_mod2_conservation_theorem.md` — the canonical Q mod 2
  conservation source; the audit centers on its diameter
  condition and topological-loop language.
- `substrate_determinism.md` — inviolables list; the audit
  suggests scale-qualification on inviolable #1.
- `rank1_temporal_causation.md` (D46) — the dissipation
  structural source; algebraic basis confirmed.
- `born_rule.md` L26-46 — Kuramoto dissipation rate structure.
- `klein_bottle.md`, `klein_bottle_derivation.md` — Klein-bottle
  topology that Q mod 2 depends on; surface_uniqueness_audit.md
  reframes Klein-bottle as observation-fixed.
- `surface_uniqueness_audit.md` — companion audit at the
  surface-choice layer; this audit is at the
  conservation-invariant layer with same possibility-discipline
  methodology.
- `continuum_limits.md` (disposition note) — K=1 as
  substrate-admitted parent regime; relevant for K<1↔K=1
  transition behavior.
- `primitives_vs_addresses_candidate.md` — provides the
  layer-invariant vs layer-specific partition that this audit
  applies to conservation invariants; third substantive test of
  the candidate.
- `basepoint_principle.md` — methodology framework; the audit's
  surfaced gap (Planck Q mod 2 contingency) parallels
  basepoint-principle "obstruction not yet exhibited" status
  rather than a closed structural decline.
- `canonical_glossary.md` Section 8 — possibility-discipline
  vocabulary; the audit's substrate-internal vs
  observation-conditional vs scale-contingent decomposition uses
  this framework.
- `klein_bottle_restructure_price.md` — empirical floor; if
  resolution (i) (algebraic Q mod 2) requires apparatus that
  contradicts ℍ-QM empirical exclusion, it's blocked at the same
  layer as the apparatus-extension fallback.
- `feedback_resolution_vs_reconstruction.md` (memory) — methodology
  enforced throughout; the audit stays in resolution-mode.

---

## One-line summary

The framework's two foundational conservation invariants —
**Q mod 2** (topological, from `q_mod2_conservation_theorem.md`)
and **dissipation** (algebraic, from rank-1 Fréchet derivative
in D46) — have *different* scale-stability properties under the
possibility-discipline audit: dissipation's structure
(rank-1 factorization producing the arrow of time) is
**algebraic and layer-invariant** across all three scales
(Planck/standard/Hubble), with only the specific rate being
layer-specific (address); Q mod 2's basis is **topological**
(invokes Klein-bottle antiperiodic-cycle structure), so its
conservation is universal at standard and Hubble scales but
**contingent at Planck** where smooth-manifold topology may
dissolve — three candidate resolutions are named (algebraic Q
mod 2 derivation, scale-qualified Q mod 2 via the theorem's
existing diameter condition, or honest acknowledgment that Q
mod 2 is scale-specific not universally inviolable), with
**resolution (ii) recommended** as the cleanest match to
existing apparatus since the conservation theorem's "support of
spatial diameter < L_x" condition automatically scale-qualifies;
the audit provides a **third substantive test** of the
`primitives_vs_addresses_candidate.md` (after gauge sector and
Γ_0(6) cusp structure), with **two clean passes** (dissipation
structure layer-invariant, dissipation rate layer-specific) and
**one surfaced gap** (Q mod 2 Planck contingency that's
inherited from the surface-choice contingency in
`surface_uniqueness_audit.md`); four falsifiers named;
recommendations include immediate resolution-mode updates to
`q_mod2_conservation_theorem.md` and `substrate_determinism.md`
explicitly noting the scale-qualification, deferred derivation
work on resolution (i) (algebraic Q mod 2), and not currently
pursuing reformulation of the conservation chain since no
empirical scale-specific evidence motivates it; resolution-mode
discipline preserved throughout; no new conservation law,
substrate apparatus, or empirical predictions; the audit
clarifies the existing chain's scale-behavior rather than
modifying it.
