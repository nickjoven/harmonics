# Layer-invariant primitives vs layer-specific addresses (candidate methodology)

## Status

**Candidate distinction, not yet sealed.** This doc proposes a
methodological distinction between two classes of framework
objects, motivated by the recursive Kuramoto reading discussed
in the conversation following `surface_uniqueness_audit.md` and
`continuum_limits.md`'s disposition note. The distinction:

- **Layer-invariant primitives**: framework objects that recur
  unchanged at every layer of a possibly-recursive pocket-medium
  hierarchy. These bottom out at the substrate's minimal
  commitments and have the same form whether describing our
  pocket, a parent medium, or a meta-parent.

- **Layer-specific addresses**: framework objects whose VALUES
  vary layer by layer, encoding our pocket's specific position
  in any parent's vocabulary. The framework derives these for
  our layer; under the recursive reading, they are our
  coordinates rather than universal facts.

This is **substrate-admitted, not substrate-forced**, per
`canonical_glossary.md` Section 8's possibility-discipline. The
framework's apparatus is consistent with the distinction but
does not currently force it. Sealing as a methodology
preference (analogous to
`feedback_resolution_vs_reconstruction.md`) would require either
empirical evidence for the pocket-medium structure or a
substrate-internal derivation forcing the layer-recursion.

The doc is **first candidate** of its kind — the framework has
not previously distinguished primitives from addresses in this
sense. Other candidates may follow; this one is the seed.

Class: foundational rigor proposal (Class 3 candidate, awaiting
verification work for sealing).

---

## The proposed distinction

### Layer-invariant primitives

These are the framework's universal substrate commitments. They
have the same form at every layer of any recursive hierarchy
(if one exists), because they ARE the framework's minimal
expressive vocabulary.

**Verified layer-invariant** (would recur at every layer):

- **The four primitives** (`minimum_alphabet.md`):
  1. Integers Z
  2. Mediant (a + c) / (b + d)
  3. Fixed-point x = f(x)
  4. Parabola x² + μ = 0

- **The cube identity structure** `q_3² − q_2³ = 1` (the
  Catalan equation case (p, q) = (2, 3) per
  `mass_sector_closure.md`'s Mihailescu connection)

- **The Mihailescu-forced pair** `(q_2, q_3) = (2, 3)` (unique
  consecutive perfect powers)

- **The XOR rule** on (q_x, q_y) parity from the Klein-bottle
  identification

- **The Z_6 = q_2 × q_3 = 6 mode lattice** with CRT
  decomposition Z_6 = Z_2 × Z_3 (`klein_antipodal_z2_rep_pattern.md`,
  `torus_branch_iteration_1.md`)

- **The φ(6) = 2 coprime-to-6 boundary** structure `{1, 5}`
  (number-theoretic fact, layer-invariant)

These are number-theoretic and topological facts about the
substrate's basic vocabulary. They cannot vary by layer because
they are not values to be derived per layer — they are the
framework's expressive primitives.

### Layer-specific addresses

These are framework objects whose VALUES are derived for our
layer but would have different values at other layers (if any
exist). Under the recursive Kuramoto reading, they are our
coordinates in any parent's substrate.

**Verified layer-specific** (would differ at other layers):

- **K_STAR ≈ 0.86196** (`item12_K_star_closure.py`,
  `framework_constants.py`) — our layer's coupling strength

- **Effective Farey depth ≈ 5.83** (`boundary_weight.md`) — our
  position in OUR Stern-Brocot tree; the parent's address for us
  in its own tree

- **Effective mode count ≈ 12.66** (`boundary_weight.md`) — our
  internal degree-of-freedom count

- **Boundary weight w* ≈ 0.83** (`boundary_weight.md`,
  observation-inverted per `boundary_weight.py` L13-56 audit) —
  our boundary's mode share, equivalently our partial-locking
  fraction

- **Hierarchy ratio R = 6 · 13⁵⁴** (`hierarchy_gaussian_lattice.md`,
  `klein_bottle.md` D26) — our scale span; our linear size in
  the parent's mode-coordinate

- **Ω_Λ = 0.6847** — our cosmological coupling to the parent's
  mean field

- **The two anchors H₀ and v_EW** (`anchor_count_reaudit.md`) —
  the parent's torque magnitudes transferred to our pocket

- **Effective spatial dimension d = 3** and **signature (3, 1)**
  (D14, D32) — these MIGHT be layer-invariant (smallest
  non-trivial dimension permitting required structures) or
  layer-specific (our pocket's particular embedding). Currently
  ambiguous; flagged for further audit.

These quantities are what the framework predicts for OUR layer
through specific substrate apparatus. Under the recursive
Kuramoto reading, the same apparatus would predict DIFFERENT
values for other layers — depending on their K, their boundary
weight, their depth in their parent's tree, etc.

---

## Why this distinction matters

### Methodological clarity

Currently the framework treats K_STAR ≈ 0.86196 and (q_2, q_3) =
(2, 3) as both "substrate-derived." Per the proposed distinction:

- (q_2, q_3) = (2, 3) is **layer-invariant**: forced by
  Mihailescu's theorem at every layer; not a coordinate but a
  universal substrate fact.

- K_STAR = 0.86196 is **layer-specific**: forced by OUR matter-
  sector self-consistency; not a universal fact but an address.

Asking "why K_STAR ≈ 0.86?" becomes "why are we at this
address?" — an observation-conditional question about our
pocket's position. Asking "why (q_2, q_3) = (2, 3)?" remains
"this is what number theory forces in any consistent substrate"
— a structural question with a structural answer.

This sharpens what we credit to substrate-forcing vs what we
credit to observation-conditional layer-positioning.

### Compositional with basepoint principle

The seven verified basepoint instances + candidate 8th surface
choice all fit the pattern "framework supplies torsorial
structure, declines basepoint, observation supplies basepoint."
Under the recursive reading, observation supplies basepoints AT
OUR LAYER. Other layers would have observations supplying their
own basepoints.

The basepoint principle's "anchor torsors" (H₀, v_EW) become
**layer-address coordinates** under the recursive reading.
Their being "declined" by the framework is exactly the layer-
specific character: each layer has its own H₀ analog.

### Compositional with possibility-discipline

`canonical_glossary.md` Section 8's distinction between
"substrate-forced" (apparatus removes alternatives) and
"substrate-admitted" (apparatus consistent but not selecting):

- Layer-invariant primitives are **substrate-forced AT EVERY
  LAYER** — universal structural facts.

- Layer-specific addresses are **substrate-forced AT OUR
  LAYER** by our self-consistency; **substrate-admitted in
  general** as possibility-space coordinates that could take
  other values at other layers.

This is a refinement of the substrate-forced category — it
splits into "universally substrate-forced" (primitives) and
"layer-locally substrate-forced" (addresses).

### The information-theoretic basis (discrete-lossless / quantum-lossy)

The partition has an underlying mechanism: **primitives are
lossless operations on structured content; addresses are lossy
projections to scalar values**. The discrete substrate operates
in the lossless regime; observation enacts the lossy projection
step. This connects the layer-invariant / layer-specific split
to the discrete / quantum boundary and to the
arithmetic-vs-mediant categorical distinction.

**The two parallel distinctions, stacked**:

| Substrate side | Observation side |
|---|---|
| Discrete | Quantum |
| Lossless | Lossy |
| Mediant operations (2-vector preserved) | Arithmetic projection (collapsed to scalar) |
| Layer-invariant primitives | Layer-specific addresses |
| Algebraic identities | Empirical anchors |
| Possibility-space forcing | Basepoint selection |

These are not four parallel distinctions — they are **one
distinction surfaced at four different layers of the framework**.
The substrate operates losslessly on discrete 2-vector (and
higher-arity) content; observation enacts the lossy projection
to specific scalar values.

### Arithmetic vs mediant as the canonical worked example

The cleanest concrete instance of the lossless-vs-lossy partition
is the framework's choice of **mediant** over **arithmetic
division** at the substrate level:

| Operation | Domain → Range | Information behavior |
|---|---|---|
| Arithmetic division `a/b` | ℤ × ℤ_{>0} → ℚ | **Lossy**: collapses representations `(a,b) ~ (ka, kb)`. `(2,4)`, `(1,2)`, `(3,6)` all project to `1/2`; denominator-class information is thrown away. |
| Mediant `(a+c)/(b+d)` | (ℤ²) × (ℤ²) → ℤ² | **Lossless**: operates on the 2-vector representation directly. `(2,4) ⊕ (1,3) = (3,7)` ≠ `(1,2) ⊕ (1,3) = (2,5)`. Numerator and denominator tracked separately; 2-vector structure preserved. |

Arithmetic division is a forgetful functor — projects to the
reduced equivalence class. Mediant is a structural operation —
preserves the 2-vector primitive content. They are *categorically
different* in what they retain, not interchangeable
implementations of "division."

Every framework operation that *works* at the substrate level
operates at the 2-vector / structured layer where mediant is the
natural composition:

- Cube identity `q_3² − q_2³ = 1` treats `(q_2, q_3)` as a
  2-vector; arithmetic reduction would throw away which-is-which
- Klein bottle's `(q_x, q_y)` mode lattice preserves direction-pair
  structure
- CRT `Z_6 = Z_2 × Z_3` is a 2-vector decomposition
- Mihailescu's theorem speaks of `(x, p, y, q)` 4-tuples because
  the perfect-power *structure* is what's unique, not just the
  resulting integer

### What this clarifies about quantum mechanics in the framework

The "quantum" character of physics — Born rule, measurement
collapse, probability rather than certainty — is **not a
fundamental feature of the substrate**. It is the signature of
lossy projection from a discrete-lossless substrate to observed
outcomes.

The Born rule decomposes:

- **Basin geometry** producing `|ψ|²` weighting is
  substrate-forced (saddle-node universality, exponent 2 from
  the parabolic normal form — discrete, lossless, structural).
- **Probability as relative basin volume** is a lossless statement
  about the substrate (basin measure is a definite quantity).
- **Collapse** — realizing one basin specifically — is the lossy
  step. Substrate possibility-space contains all basins;
  observation picks one; the others are unrealized but not
  "wrong."

So "quantum" reduces to "lossy projection of discrete substrate
possibility-space." Not mysterious; the inevitable consequence
of asking a single scalar question of a multi-vector substrate.

### Important caveat: lossless ≠ rational, lossy ≠ irrational

The lossless-lossy distinction is **not** about whether the
result is rational or irrational. It's about whether the
operation preserves substrate structure (integer 2-vectors,
mediant navigation, natural-irrationals closure per
`substrate_determinism.md` inviolable #8) or projects to a
specific observed scalar.

- **Integer + mediant operations**: lossless, structure-preserving
- **Arithmetic projection to rational scalar**: lossy reduction
- **Limit to a natural irrational** (φ, π, e, √n): lossy in the
  sense of being unreachable by finite rational sums, but the
  limit IS substrate-forced (the irrational is a specific
  fixed-point of substrate dynamics, not arbitrary)
- **Arbitrary transcendentals**: excluded by inviolable #8's
  closure — substrate does not admit them

So rationals and natural irrationals both appear on the substrate
side as derived content (rationals via mediant; natural irrationals
via substrate-dynamic limits with specific structural roles).
The lossy projection happens at the substrate → observation
interface regardless of which number-class the projected value
inhabits.

### Implication for the four-status discriminator

The information-theoretic reading sharpens
`canonical_glossary.md` Section 8's possibility-discipline:

- **Substrate-forced** = lossless operations preserving primitive
  structure
- **Substrate-admitted** = primitive structure consistent with
  multiple specific projections (the possibility-space)
- **Observation-fixed** = the specific lossy projection observation
  enacts at our layer
- **Structurally-declined** = lossy projection that would violate
  closure inviolables (e.g., introducing an arbitrary transcendental,
  predicting empirically-falsified physics)

The discipline's four statuses correspond to four different
relationships with the lossless-lossy boundary; what was implicit
becomes mechanism.

---

## What this distinction does NOT establish

- **No claim that recursive layers exist.** The distinction is
  *defined* in terms of a recursive pocket-medium structure;
  whether such recursion is physically realized is observation-
  conditional and the framework currently has no apparatus
  forcing it.

- **No specific predictions distinguishing layers.** The
  distinction would acquire empirical content only if
  observations gave evidence of other layers. Currently:
  speculation-consistent, derivation-empty.

- **No reassignment of substantive results.** The framework's
  predictions for our layer are unchanged. The distinction is
  about how to CHARACTERIZE them, not how to derive them.

- **No automatic seal.** Per the candidate framing: needs
  verification work before sealing as canonical methodology.
  Verification candidates listed below.

---

## What sealing would require

For this distinction to be canonical methodology (parallel to
`feedback_resolution_vs_reconstruction.md`):

(a) **Demonstrate that the layer-invariant set is closed under
the framework's derivations.** The four primitives + cube
identity + Mihailescu pair + Z_6 lattice + XOR rule should
SUFFICE to derive *all* layer-specific quantities. If derivation
of K_STAR or any address quantity requires additional layer-
invariant inputs, the layer-invariant set is incomplete.

(b) **Demonstrate that the layer-specific set is closed under
substitution.** Replacing K_STAR ≈ 0.86 with some other value
in (0, 1) should yield a consistent framework describing a
different layer's pocket. If substitution breaks self-consistency,
the layer-specific character is illusory and the value is
actually layer-invariant.

(c) **At least one additional substantive instance.** A second
methodology distinction following the same primitives-vs-addresses
pattern would confirm the distinction is structural, not
ad hoc. Currently only this one instance is named.

(d) **Compatibility with empirical constraints.** The
distinction must not produce predictions inconsistent with
observed cosmology (e.g., epoch-evolution of "addresses" must
be consistent with observed Ω_Λ stability, fine-structure
constancy, etc.).

These four sealing criteria would convert this candidate to
canonical methodology.

---

## Falsifiers

1. **The four primitives are insufficient.** If a substrate
   construction requires additional primitive vocabulary beyond
   the canonical four, the "layer-invariant primitives = the
   four primitives" claim weakens.

2. **K_STAR is universally substrate-forced.** If a deeper
   derivation showed K_STAR = 0.86196 follows uniquely from
   the layer-invariant primitives without any layer-specific
   input, K_STAR is not an address. The distinction's primary
   layer-specific example collapses.

3. **The cube identity has layer-variation.** If at some layer
   the substrate could close on (q_2, q_3) ≠ (2, 3) without
   contradicting Mihailescu (e.g., if relaxing positive-integer
   constraint at the parent's substrate produces other solutions),
   the Mihailescu-strength layer-invariance argument weakens.

4. **No empirical pocket-medium evidence ever emerges.** If
   observational programs (CMB-S4, LiteBIRD, etc.) constrain
   pocket-medium signatures below the framework's parameter
   space's natural scale, the recursive reading becomes
   empirically excluded and the distinction's motivation
   evaporates — though the distinction itself could still be
   useful as a structural classification.

---

## Cross-links

- `surface_uniqueness_audit.md` — the K²/T² Z₂-torsor at the
  surface-choice layer; provides the "layer" framing this doc
  generalizes.
- `continuum_limits.md` (disposition note at top) — K=1 as
  physical parent regime; the recursive Kuramoto reading
  underlying this distinction.
- `basepoint_principle.md` — methodology framework; anchor
  torsors become layer-address coordinates under this
  distinction.
- `canonical_glossary.md` Section 8 — possibility-discipline;
  this doc refines "substrate-forced" into universally-forced
  vs layer-locally-forced.
- `minimum_alphabet.md` — the four primitives that this doc
  names as the canonical layer-invariant set.
- `mass_sector_closure.md` "Connection to the Catalan equation
  / Mihailescu's theorem" — substrate-forcing of (q_2, q_3) =
  (2, 3) via Mihailescu; the canonical layer-invariant pair.
- `item12_K_star_closure.py`, `framework_constants.py` — K_STAR
  derivation for our layer; layer-specific.
- `boundary_weight.md` — boundary weight w*, effective Farey
  depth 5.83, effective mode count 12.66; layer-specific.
- `hierarchy_gaussian_lattice.md` — hierarchy ratio R =
  6 · 13⁵⁴; layer-specific.
- `anchor_count_reaudit.md` — the two anchors H₀, v_EW as
  declined basepoints; under recursive reading, layer-address
  coordinates.
- `feedback_resolution_vs_reconstruction.md` (memory) —
  methodology preference structure this distinction would
  parallel if sealed.
- `feedback_null_promotion.md` (memory) — discoverability
  methodology; this candidate doc itself is null-promotion-
  compliant (clearly flagged as candidate, not sealed).

---

## One-line summary

This doc proposes a candidate distinction between **layer-
invariant primitives** (the four primitives, the cube identity,
the Mihailescu-forced (q_2, q_3) = (2, 3), the Z_6 lattice, the
XOR rule, the φ(6) = 2 boundary structure — substrate facts
that recur unchanged at every layer of any possibly-recursive
pocket-medium hierarchy) and **layer-specific addresses**
(K_STAR ≈ 0.86196, effective Farey depth 5.83, effective mode
count 12.66, boundary weight w* ≈ 0.83, hierarchy ratio R =
6·13⁵⁴, Ω_Λ = 0.6847, the two anchors H₀ and v_EW — framework
quantities whose VALUES are derived for our layer but would
vary at other layers if recursion is physically realized);
motivated by the recursive Kuramoto reading where our pocket
is one sub-ensemble in a parent's substrate; flagged as the
first candidate of its kind and substrate-admitted (not
substrate-forced); sealing would require demonstrating layer-
invariant set closure under derivation, layer-specific set
closure under substitution, at least one additional substantive
instance, and compatibility with empirical constraints; four
falsifiers named; the distinction sharpens what we credit to
substrate-forcing (the primitives, universally) vs what we
credit to observation-conditional layer-positioning (the
addresses, locally), refining the basepoint principle's anchor
torsors into layer-address coordinates and the possibility-
discipline's substrate-forced category into universally-forced
vs layer-locally-forced sub-categories.
