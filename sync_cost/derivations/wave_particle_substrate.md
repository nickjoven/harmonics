# Wave–particle substrate: the four-object framework synthesis

Top-level synthesis doc, parallel in level to `expressibility_split.md`,
`comparison_class.md`, and `unitless_check.md`. Names the framework's
structural ontology in full and reads its sectors (matter / dark
energy, time-arrow / time-clock, experience / counterfactuals) as a
single wave–particle duality enacted on the substrate.

No new primitives. Every claim in this doc is a rereading of pieces
already in the framework. The contribution is **what the pieces add
up to** when assembled.

## Claim

Four objects are sufficient to specify the framework's structural
content:

1. **Two universal generators** — `mediant` (discrete combinatorics)
   and `eml` (continuous transcendentals); see `expressibility_split.md`.
2. **One operator** — the half-twist `θ → θ + π` of
   `klein_bottle.md`'s single antiperiodic direction; converts
   particle-side configurations to wave-side amplitudes (Wick rotation).
3. **One coordinate** — the K-axis (cascade-depth direction); the
   stage on which the duality is parametrised.
4. **One topology** — the Klein bottle; the rigidity that keeps the
   composition consistent (unitarity).

Everything else — matter, dark energy, time, experience, mass spectra,
gauge bosons, kinks, vortices, breathers, the K-zoo, the seam — is a
configuration of these four. The framework is **unusually parsimonious**
for an ontology that touches this much physics; that parsimony is the
synthesis worth committing.

## The two generators are wave–particle duality

`expressibility_split.md` formalises the claim that no single universal
generator suffices: the framework's content splits between **mediant**
(integer mode counts, Stern–Brocot enumeration, Farey arithmetic) and
**EML** (`eml(x, y) = exp(x) − ln(y)`, the Sheffer-stroke generator of
elementary continuous mathematics). That split is methodological in
`expressibility_split.md`. Read through dynamics, it is **wave–particle
duality**.

| Generator | Algebra | Physical reading |
|---|---|---|
| Mediant | discrete, combinatorial, integer-mode-counted | **Particle side**: localized, fiber-bound, structure-locked. |
| EML | continuous, transcendental, asymptotic | **Wave side**: delocalized, inter-fiber, never-quite-reached. |

The claim is not analogy. Particle excitations on the substrate are
locked at cascade fixed points (`master_cascade_identity.md`'s K-zoo
— mediant-generated). Wave amplitudes are EML-generated functions on
the K-axis continuum. The two generators are not two languages for the
same content; they are the **dynamical poles** of substrate physics.

This makes wave–particle complementarity an **identity of the
framework**, not an additional commitment. Asking "is the electron a
wave or a particle?" is asking "does this excitation live on the
mediant side or the EML side?" The framework's answer is: it lives at
their composition — on a single fiber (mediant) with continuous
amplitude (EML) — and the half-twist is what permits the composition.

## The half-twist is the particle ↔ wave conversion operator

The single antiperiodic direction of `klein_bottle.md` carries a
half-twist `θ → θ + π` on the field, equivalent to `e^{iπ} = −1` on
half-integer x-mode amplitudes. Three apparently-different framework
processes are all instances of this operator acting:

1. **Vortex worldline crossing the bicone seam** —
   `cone_twist_substrate.md` §3. Each crossing picks up phase `e^{iπ}`.
2. **Cross-sector tunnelling** — `soliton_dynamics.md` Open 2. A kink
   tunnelling between cascade sectors picks up a Euclidean-time path
   weighted by `e^{−S_inst}`.
3. **Schwinger-like vortex-pair production at a K-gradient seam** —
   `cone_twist_substrate.md` §5.1. A virtual pair becomes real through
   tunnelling across the seam.

These are not three processes. They are **one operator acting on three
configurations**. The Wick rotation factor `e^{iπ/2}` (square root of
the half-twist phase) is the same factor that:

- Converts a real-time propagator `e^{−iEt}` into a Euclidean-time
  amplitude `e^{−Eτ}` in standard QFT;
- Converts a particle worldline into a wave amplitude in the path
  integral;
- Converts a kink (particle-side soliton) into a breather (wave-side
  bound state) via Coleman's fermion–boson duality in 1+1D.

The framework's commitment: **all three of those conversions are the
same physical operation in the substrate** — passage through the
seam, picking up a half-twist phase. The Wick rotation of QFT is not
a calculational trick; it is the operational form of the substrate's
particle ↔ wave conversion operator. Schwinger pair production,
instanton tunnelling, and the cross-sector `S_inst` are then
**one process seen from three angles** — each one the half-twist's
action on a different starting configuration.

This is testable in principle: the AB-like π-phase prediction of
`cone_twist_substrate.md` §5.2 is the **same phase** that would be
seen in an instanton-mediated tunnelling experiment, and the **same
phase** that controls Schwinger-pair-production interference. A
mismatch between the three (different π's at different scales) would
falsify the unification.

## The K-axis parametrises the duality

K-scale is a *value* — the local Kuramoto coupling at a substrate
point. K-axis is the *direction* values vary along — the 1D coordinate
carrying the bicone's radial structure. Neither is particle nor wave;
both are coordinate machinery.

| What sits at K-scale = K_n | What lives on the K-axis continuum |
|---|---|
| Particle excitations (cascade-locked vortices, kinks, matter excitations) | Wave amplitudes (linear-sector modes, breathers, dark-sector inter-fiber currents) |
| Discrete, fiber-bound | Continuous, base-supported |
| Mediant-generated | EML-generated |

The framework's K-axis is the **stage** of wave–particle duality.
Particle physics rides single fibers (matter localizes at one `K_n`);
wave physics rides the continuum between fibers (dark sector spreads
across the K-axis). The K-axis-as-base inversion proposed in
`cone_twist_substrate.md` discussion makes this explicit: K-axis as
the base of a fiber bundle, Klein bottle as the fiber over each
K-scale. Particles ride single fibers; waves are sections of the
bundle.

This gives the framework its **why-don't-we-move-up-and-down** answer:
observers are matter excitations, which by construction are localised
on a single fiber, so observer motion along the K-axis is forbidden by
the particle-side localisation. Dark sector, being inter-fiber, is the
only thing that experiences the K-axis as a free direction. The
asymmetry between local-matter physics and cosmic-scale dark-sector
physics is **structurally** the asymmetry between particle and wave
sides of the same substrate.

## The Klein bottle keeps it rigid

The half-twist is the operator; the Klein bottle is the **rigidity
container** that keeps the operator topologically protected. Three
properties of the Klein bottle make the four-object ontology consistent:

1. **No boundary.** Nothing enters, nothing exits; the duality is
   self-contained.
2. **Single antiperiodic direction.** Exactly one half-twist per
   Klein traversal; Z₂ rigidity, not Z₃ or higher.
3. **Z₂ torsion in H₁.** Half-integer modes (fermions / spinors) and
   integer modes (bosons) are topologically distinguished.

Together these are what `cone_twist_substrate.md` §4 names as
"unitarity = bicone topology rigidity." Information is never lost
because the Klein bottle does not permit the topology changes that
would lose it. The wave–particle duality is enforced; the conversion
operator is well-defined; the K-axis stage is fixed.

## Three mappings, fully named

### Matter / dark energy

| Particle (mediant, fiber-bound) | Wave (EML, inter-fiber) |
|---|---|
| **Matter**. Localised on a single cascade fixed point `K_n`. Sees the K-axis as a fixed background. Standard-Model phenomenology lives here. | **Dark energy**. Inter-fiber, spread across the K-axis continuum. Sees the K-axis as a free direction. Cosmological-scale phenomenology lives here. `half_twist_dynamics.md`'s breathing-mode exchange is the inter-fiber repair channel. |

### Time-arrow / time-clock

`time_axis_split.md` splits time into two axes; here both are read
through wave–particle duality:

| Particle (arrow, antiperiodic x) | Wave (clock, periodic y) |
|---|---|
| **Time-arrow**. Irreversible. Each tick a Z₂-charge repair event (per the forced-violation resolution mechanism — see "Open" below). Discrete, counted, particle-side. | **Time-clock**. Cyclic substrate breathing. Continuous, transcendental, wave-side. `H_0` is its rate. |

This recovers, structurally, the existing framework split with a new
reading: arrow is discrete because it counts repair events; clock is
continuous because it breathes.

### Experience / counterfactuals

| Particle (realised worldline) | Wave (un-realised support) |
|---|---|
| **Observer experience**. A single matter worldline through the substrate. By construction particle-side. | **Counterfactual histories**. The path-integral measure on all worldlines the observer did not take. By construction wave-side. Inaccessible to local matter measurement; visible only through dark-sector observations that integrate over many fibers. |

This is the structural reason dark sector phenomenology can carry
information that local-matter phenomenology cannot: it integrates over
counterfactuals.

## Status

**Class 3 (synthesis grade).** Every claim is a rereading of existing
framework pieces, assembled into a single ontology. The contribution
is **what the pieces add up to**; no new derivations are imported.

The four-object ontology is unusually parsimonious — fewer objects
than any comparable framework — and that parsimony is the synthesis's
own falsifier: if any of the four objects can be removed (or if a
fifth is required), the synthesis fails.

### What this does establish

- Wave–particle duality is structurally what the lambda / EML split
  *is* when read through dynamics.
- The half-twist is the conversion operator between the two sides;
  Wick rotation, Schwinger pair production, and instanton tunnelling
  are the same operator acting on different inputs.
- Matter / dark energy, time-arrow / time-clock, and experience /
  counterfactuals are three instances of the same particle / wave
  split applied to three substrate sectors.
- The framework's content is specified by **four objects**, full stop.

### What this does not establish (open)

1. **K-axis-as-base formalisation.** The fiber-bundle reading — K-axis
   as base, Klein bottle as fiber — was introduced in the
   `cone_twist_substrate.md` discussion as the natural geometric next
   step. It is consistent with this synthesis but has not been written
   up as a derivation.
2. **Forced-violation resolution mechanism.** Three phases of
   substrate repair (local-stress / propagating-loop / asymptotic),
   with the deep claim that "time is what passes during substrate
   repair of would-be violations," were sketched in conversation
   leading to this doc. Not yet promoted to a derivation.
3. **The Wick-rotation = half-twist identification's quantitative
   consequences.** Specifically: the cross-sector tunnelling action
   `S_inst` (`soliton_dynamics.md` Open 2) should equal the
   AB-like phase of `cone_twist_substrate.md` §5.2 evaluated on a
   Euclidean instanton path. Verifying this triangle is the
   tightest single thing to do next.

## Falsifiers

- **Mismatched π's.** The AB-like seam phase, the Schwinger
  pair-production interference phase, and the instanton-tunnelling
  Wick-rotation phase should all be **the same π** (mod 2π). Any
  measurement showing them numerically different falsifies the
  half-twist unification.
- **A fifth object required.** If any prediction of the framework
  cannot be expressed as a configuration of the four objects, the
  synthesis fails. The most likely such "fifth" candidate would be a
  new continuous symmetry generator (gauge, conformal) not reducible
  to mediant / EML composition. None has yet been identified.
- **Observer motion along the K-axis.** If matter-bound observers can
  be shown to move freely along the K-axis (not just along the Klein-
  bottle base), the particle-side localisation on single fibers fails
  and the matter / dark-energy split loses its structural origin.

## Cross-links

- `expressibility_split.md` — the lambda / EML methodological split
  that this doc reads through dynamics.
- `cone_twist_substrate.md` — the Z₂-twisted bicone geometry on which
  the duality is enacted; the seam is where the half-twist operates.
- `klein_bottle.md`, `klein_bottle_derivation.md` — the topology that
  provides the rigidity container.
- `time_axis_split.md` — the time-arrow / time-clock split read here
  through wave–particle.
- `master_cascade_identity.md` — the K-zoo (cascade fixed points) at
  which matter localises along the K-axis.
- `half_twist_dynamics.md` — the breathing-mode exchange between
  tongue (matter) and gap (dark) sectors that this doc reads as the
  inter-fiber repair channel.
- `sine_gordon_substrate.md` — the Z₂-graded kink charge, here read
  as the half-twist's action on soliton-class configurations.
- `soliton_dynamics.md` — the kink-antikink S-matrix and breather
  spectrum, here read as the wave-side fluctuation tower around
  particle-side saddle points.
- `klein_bridge_audit_and_probe.md` — companion methodology for
  ontology audit (referenced by `framework_status.md` Active
  Multi-Session Derivations).
- `unitless_check.md`, `comparison_class.md` — the other top-level
  synthesis docs this one sits beside.
