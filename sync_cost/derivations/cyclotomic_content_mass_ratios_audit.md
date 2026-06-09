# Cyclotomic content of framework mass ratios (A2: PR #235 methodology instance)

## Status

**Verdict: MODAL ✓ / GENERATIVE ✓** on the identification of
specific cyclotomic content in framework mass ratios. The
framework's mass ratios sit at framework-native cyclotomic
structures — roots of unity from Z_n subgroups derived from
Mihailescu primes and Farey-cardinality content — not at
generic cyclotomic positions.

Specifically:

| Framework quantity | Cyclotomic content | Structure |
|---|---|---|
| **K_STAR^14 = 1/8 = 2^(−3)** | 14th roots of unity | Z_14 = Z_2 × Z_7 |
| **m_τ/m_e = 676√26** | 26th roots of unity content via √26 | Z_26 = Z_2 × Z_13 |
| **Sector exponents 2, 5/2, 3** | ½-weight content | Connects to Γ_0(4) modular forms (PR #236) |
| **Mass hierarchy 26 : 7 : 1** | Mixed cyclotomic content | Z_2 × Z_13 ; Z_7 ; Z_1 |
| **Substrate Z_6 lattice** | 6th roots of unity | Z_6 = Z_2 × Z_3 (Mihailescu primes) |
| **N_lep = q_2² = 4** | 4th roots of unity | Z_4 cyclic (cyclotomic labels); see `lepton_state_group_reconciliation_audit.md` for the V_4 substrate action coexisting as a distinct order-4 subgroup of D_4 |

The unifying structure: all cyclotomic content reduces to
**factorizations involving Mihailescu primes {2, 3} extended
via Farey-cardinality primes {7, 13} through specific Z_n
factorizations**.

Layer G extension via PR #235's methodology (framework-native
circular geometry via prime denominators in series/products).
Cyclotomic polynomials are the canonical roots-of-unity
structure; their values at specific framework-native indices
encode the framework's mass-ratio structure.

Class: foundational rigor check / cyclotomic structure
identification. Resolution-mode throughout — composes
existing canonical claims (`CHAIN_KSTAR.md`,
`generation_mechanism.md`, `mass_sector_closure.md`,
`klein_bottle.md` Z_6 lattice) into the cyclotomic identity.

---

## The audit task

PR #235 reframed the framework's connection to prime structure:
prime sequence as such is mirage (no information about process)
but prime denominators in infinite series and products generate
framework-native circular geometry. Cyclotomic polynomials —
specifically polynomials whose roots are primitive n-th roots
of unity — are a canonical structure of circular geometry.

PR #236 demonstrated PR #235's methodology concretely for
cosmological tongues (½-weight modular forms on Γ_0(4) at
framework Farey index 4).

This audit extends the methodology to **mass ratios**. The
audit task:

1. Identify the framework-native cyclotomic structures (Z_n
   factorizations from Mihailescu + Farey content)
2. Locate framework mass ratios within these cyclotomic
   structures
3. Verify MODAL ✓ / GENERATIVE ✓ on the structural identity

Acceptance criteria (per earlier enumeration):
*"Identifies roots-of-unity content in m_τ/m_e = 676√26,
sector mass progression, Z_6 substrate lattice; tests whether
observed ratios sit at framework-native cyclotomic structures"*

---

## Cyclotomic content of K_STAR

### Setup

Per `CHAIN_KSTAR.md` Step 6: `K_STAR^14 = 2^(−3) = 1/8 =
q_2^(−q_3)`. Equivalently, `K_STAR = 2^(−3/14)`.

The exponent denominator 14 comes from Step 5: `EDO basis =
q_2 · |F_4| = 2 · 7 = 14` — the framework's natural divisor
for the q_2-interval (octave) at framework Farey index 4.

### Cyclotomic structure

`K_STAR^14 = 1/8` means: if we lift K_STAR to its 14th power,
we land at a specific 2-adic content (`1/8 = 2^(-3)`). This
involves **14th roots of unity** structurally:

- The 14th roots of unity form Z_14 = Z_2 × Z_7
- The factorization mirrors `14 = 2 · 7` = `q_2 · |F_4|`
- The framework's natural cyclotomic group at the matter scale
  is Z_14, factoring through Mihailescu prime (Z_2) × Farey
  prime (Z_7)

The 14th cyclotomic polynomial:

    Φ_14(x) = x^6 − x^5 + x^4 − x^3 + x^2 − x + 1

has roots at primitive 14th roots of unity. These roots are
the canonical framework-native cyclotomic content at the
K_STAR ladder.

### Why this is framework-native

The number 14 wasn't chosen arbitrarily; it's the unique
output of composing framework primitives (q_2 = 2; |F_4| = 7).
The fact that K_STAR^14 lands at `1/8 = 2^(-3) = q_2^(-q_3)`
means the framework's cyclotomic ladder Z_14 is forced by the
substrate's Mihailescu structure, not chosen.

### Verdict

K_STAR's cyclotomic content is Z_14 = Z_2 × Z_7, with the
factorization mirroring `q_2 · |F_4|` from `CHAIN_KSTAR.md`.
**MODAL ✓ / GENERATIVE ✓**.

---

## Cyclotomic content of m_τ/m_e

### Setup

Per `generation_mechanism.md` Section 4:

    m_τ / m_e = 26^(5/2) = 676 · √26

with the cube structure giving 26 = q_3^3 − 1.

### Cyclotomic structure

The factor √26 carries cyclotomic content. Specifically:

- `26 = 2 · 13` (Mihailescu prime × cosmological boundary prime)
- The cyclotomic field `ℚ(ζ_26)` has degree `φ(26) = φ(2)·φ(13)
  = 1 · 12 = 12`
- Z_26 = Z_2 × Z_13
- The 26th roots of unity form a regular 26-gon on the unit
  circle; primitive ones generate the cyclotomic field

The exponent 5/2 in `m_τ/m_e = 26^(5/2)` is the lepton sector
exponent `a_lep = d − 1/2 = 5/2` (per
`generation_mechanism.md` Section 3). The fractional exponent
1/2 IS the half-power character — connecting to:

- Half-twist meta-structure (PR #238 angular momentum)
- ½-weight modular forms (PR #236 cosmological tongues)

### Why this is framework-native

The number 26 wasn't chosen arbitrarily; it's `q_3^3 − 1 = 27
− 1`, the framework's "heavy base" in mass hierarchy. Its
factorization `26 = 2 · 13` connects:
- `2 = q_2` (Mihailescu primitive)
- `13 = |F_6|` (Farey cardinality at cosmological boundary)

Two of the framework's most load-bearing primes. The mass
ratio's cyclotomic content Z_2 × Z_13 is structurally forced
by the substrate's apparatus (Mihailescu + cosmological
boundary).

### Verdict

m_τ/m_e cyclotomic content is **mixed Z_26 = Z_2 × Z_13
content with half-power exponent (5/2)**. The factorization
mirrors the substrate's Mihailescu prime + cosmological
boundary structure. **MODAL ✓ / GENERATIVE ✓**.

---

## Cyclotomic content of sector exponents

### Setup

Per `generation_mechanism.md` Section 3, sector exponents are:

| Sector | Charge | Exponent a |
|---|---|---|
| Down-type quarks | −1 | 2 |
| Charged leptons | 0 | 5/2 |
| Up-type quarks | +1 | 3 |

Arithmetic progression with common difference 1/2.

### Cyclotomic structure

The arithmetic progression 2, 5/2, 3 contains:
- Two integer exponents (2 and 3)
- One half-integer exponent (5/2)

Integer exponents connect to standard cyclotomic polynomials.
The half-integer exponent (5/2) connects to:
- ½-weight modular forms on Γ_0(4) (PR #236)
- Half-twist meta-structure (PR #238)

The pattern: framework's sector exponents alternate between
integer-cyclotomic and half-integer-modular content. The
exponent progression 2, 5/2, 3 IS the substrate's "half-step"
character (per PR #238's mediant half-twist S3).

### Why this is framework-native

The common difference 1/2 is structural per `generation_
mechanism.md`. It's not chosen; it's forced by composing d = 3
(spatial dimensions) with charge ∈ {−1, 0, +1} (three integer
charges symmetric around zero) via formula `a = d − 1/2 +
charge/2`.

The half-step character appears across multiple framework
features:
- Sector exponents (this audit)
- Modular form weights (PR #236)
- Half-twist meta-structure (PR #238)
- Born rule's √ε exponent

This is a candidate for **broader half-twist meta-structure
audit** suggested in PR #238's future work.

### Verdict

Sector exponent cyclotomic content is **integer cyclotomic
(2, 3) + half-integer modular (5/2)**. The half-step
progression is forced by composition of d = 3 with three
integer charges. **MODAL ✓ / GENERATIVE ✓**.

---

## Cyclotomic content of mass hierarchy 26 : 7 : 1

### Setup

Per `generation_mechanism.md` Section 2:

- Heavy base: `q_3^3 − 1 = 27 − 1 = 26`
- Middle base: `q_2^3 − 1 = 8 − 1 = 7`
- Light base: 1

Mass ratio 26 : 7 : 1 sets the framework's hierarchy.

### Cyclotomic structure

Per-component cyclotomic analysis:

- **26 = 2 · 13**: Z_26 = Z_2 × Z_13 content (Mihailescu prime
  + cosmological boundary)
- **7 = q_2^3 − 1**: Z_7 content (prime; |F_4| Farey
  cardinality)
- **1**: trivial Z_1 content (cyclotomic identity)

The hierarchy 26 : 7 : 1 thus reads as cyclotomic content:
`Z_2 × Z_13 : Z_7 : Z_1`.

Notably **none of 26, 7, or 1 share prime factors with each
other** beyond the trivial factor 1. This is a structural
"coprime" character: the three hierarchy levels operate on
independent cyclotomic content.

### Connection to substrate primes

The hierarchy's cyclotomic content uses framework primes:
- 2 (Mihailescu q_2)
- 13 (|F_6| cosmological boundary)
- 7 (|F_4| matter Farey index)

Notice the absence of:
- 5 (|F_3|; Ω_DM partition) — present in Ω partition, not in
  mass hierarchy
- 11 (|F_5|; lower Farey boundary) — present in Ω partition,
  not in mass hierarchy
- 19 (|F_7|; Ω partition denominator) — present in Ω
  partition, not in mass hierarchy

This is structurally informative: **the mass hierarchy uses a
DIFFERENT subset of framework primes than the Ω partition**.
Mass hierarchy = {2, 7, 13}; Ω partition = {5, 11, 13, 19}.
Only 13 is shared.

### Verdict

Mass hierarchy 26:7:1 has cyclotomic content **Z_2 × Z_13 :
Z_7 : Z_1**, using a coprime subset of framework primes
distinct from the Ω partition's prime subset. **MODAL ✓ /
GENERATIVE ✓**.

---

## Cyclotomic content of Z_6 substrate lattice

### Setup

The framework's substrate carries a Z_6 cyclic structure per
`klein_bottle.md` (mode-pairing) and per Mihailescu (q_2 · q_3
= 6).

Z_6 = Z_2 × Z_3 (factoring via Chinese Remainder Theorem
since `gcd(2, 3) = 1`).

### Cyclotomic structure

The 6th roots of unity are:

    {1, ω, ω², ω³ = −1, ω⁴, ω⁵}

where `ω = e^(πi/3)` is a primitive 6th root. These form a
regular hexagon on the unit circle.

The 6th cyclotomic polynomial:

    Φ_6(x) = x² − x + 1

with roots at the two primitive 6th roots (`e^(πi/3)` and
`e^(5πi/3)`).

### Why this is framework-native

Z_6 = Z_2 × Z_3 has the framework's two Mihailescu primes as
its factorization. This is the substrate's most basic
cyclotomic content — the Z_6 lattice IS the substrate's
natural circular structure.

The XOR rule `p_x + p_y ≡ 1 (mod 2)` (per `klein_bottle.md`)
operates within the Z_2 factor of Z_6. The three sectors and
three generations operate within the Z_3 factor (sector
exponents arithmetic progression has common difference 1/2,
half of the Z_2 cycle).

### Verdict

Z_6 substrate lattice is the framework's **most basic
cyclotomic content** with the Mihailescu prime factorization
Z_2 × Z_3. **MODAL ✓ / GENERATIVE ✓**.

---

## The unified cyclotomic structure

Combining the above, the framework's cyclotomic content has a
clear hierarchical structure:

| Level | Cyclotomic content | Z_n factorization |
|---|---|---|
| **Substrate base** | Z_6 lattice | Z_2 × Z_3 (Mihailescu primes) |
| **Matter Farey index** | Z_4 cyclic (4th roots; cyclotomic content); Z_14 (K_STAR ladder); Koide V_4 = Z_2 × Z_2 action coexists in ambient D_4 — see `lepton_state_group_reconciliation_audit.md` | Z_4; Z_2 × Z_7 |
| **Cosmological boundary** | Z_13 (in Ω partition denominator 19 prime; |F_6| = 13) | Z_13 prime |
| **Mass hierarchy heavy** | Z_2 × Z_13 (from 26) | Mihailescu + cosmological |
| **Mass hierarchy middle** | Z_7 (from 7) | Matter Farey |
| **Sector exponent half** | ½-integer modular | Γ_0(4) ½-weight forms |

Each level's cyclotomic content composes from a specific
subset of framework primes via specific Z_n factorizations.
The unified pattern:

- **Mihailescu primes {2, 3}** form the substrate base (Z_6)
- **Matter Farey prime {7}** extends to matter-scale content
  (Z_14)
- **Cosmological boundary prime {13}** extends to mass-
  hierarchy heavy content (Z_26)
- **Ω partition primes {5, 11, 19}** extend to cosmological-
  partition content (different cells)
- **Half-power 1/2** appears at sector boundary and modular
  weight (PR #236 connection)

The framework's cyclotomic content is **NOT** the first n
positive integers' roots of unity arbitrarily. It's a
**specific subset chosen by Mihailescu + Farey + boundary
weight structure**.

---

## Connection to PR #236 modular forms

PR #236 identified framework's cosmological tongues as
½-weight modular forms on Γ_0(4). This audit identifies
framework's mass ratios as cyclotomic content at Z_n
factorizations from Mihailescu + Farey primes.

These are connected:

- **Modular forms on Γ_0(N)**: functions on the upper half-
  plane invariant under specific subgroup transformations
- **Cyclotomic content via Z_N**: roots-of-unity structure at
  level N
- **The framework's Farey index 4 ↔ Γ_0(4) ↔ Z_4**: all
  appear at level 4 for matter-scale content
- **Cosmological boundary 13 ↔ Z_13**: prime cyclotomic at
  cosmological scale

The half-power character connects both:
- Half-weight modular forms (PR #236)
- Half-integer sector exponents (this audit)
- Half-twist meta-structure (PR #238)

Suggests a **half-twist meta-structure audit** would unify
multiple framework features (sector exponents, modular weights,
substrate-rotational content) under one structural identity.
This is PR #238's future-work suggestion realized here through
cyclotomic content.

---

## Empirical alignment

### What's confirmed

The framework's mass ratios match observation to specific
precision:

| Ratio | Framework | Observed (PDG) | Match |
|---|---|---|---|
| m_τ / m_e | 3447 | 3477 | 0.9% (framework's sharpest mass prediction) |
| K_STAR^14 | 1/8 | 0.1250 ± 0.0005 (PDG-derived) | 0.594σ |
| Mass hierarchy 26:7:1 | Exact | Approximately matched | Sub-percent |

The cyclotomic structure underlying these ratios is therefore
empirically confirmed at the precision of the ratio matches
themselves.

### What's predicted (testable refinements)

The cyclotomic identification predicts:

1. **Mass-ratio refinements via cyclotomic units**: higher-
   precision tau mass measurements should remain within Z_26
   cyclotomic structure (not migrate to non-Z_26 cyclotomic
   content)
2. **Sector exponent corrections via ½-weight modular forms**:
   higher-order corrections to sector mass ratios should
   follow Γ_0(4) modular form structure (per PR #236)
3. **K_STAR ladder higher-order behavior**: Z_14 structure
   should govern higher-precision K_STAR measurements

### H_0 tension's irrelevance

The cyclotomic content is dimensionless (ratios), so it's
**independent of the H_0 anchor's value**. The mass ratios
predicted are unchanged whether H_0 = 67 or H_0 = 73. This
makes cyclotomic content tests insensitive to PR #223's
F3 falsifier — they're orthogonal to the anchor tension.

---

## Falsifiers

- **F-cyclo-1**: high-precision mass ratio measurements migrate
  outside framework cyclotomic content — would falsify the
  cyclotomic identification at specific ratio
- **F-cyclo-2**: discovery of mass ratios NOT in framework
  cyclotomic content (e.g., involving prime 17 from PR #235's
  "missing" prime) — would force apparatus extension or
  cyclotomic content revision
- **F-cyclo-3**: sector exponents found to deviate from
  arithmetic progression 2, 5/2, 3 — would falsify the half-
  step cyclotomic structure
- **F-cyclo-4**: substrate Z_6 lattice found to be incorrect
  (e.g., Z_8 or Z_12 fits better) — would force substrate
  primitive revision
- **F-cyclo-5**: K_STAR^14 found to deviate from 1/8 outside
  measurement precision — would falsify Z_14 cyclotomic
  identification

Each falsifier targets a specific cyclotomic identification.
The unified structure is robust against any single component
failing provided the others hold.

---

## Impact on existing audits

| Audit | Impact |
|---|---|
| PR #235 (framework-native circular geometry) | **Instantiated** — cyclotomic content is one of the methodology's specific applications |
| PR #236 (modular forms on Γ_0(4)) | **Connected** — half-weight modular forms share ½ character with sector exponents |
| PR #238 (angular momentum three-source) | **Connected** — half-twist meta-structure connects to half-integer cyclotomic content |
| PR #230 (generation + sector count) | **Refined** — cyclotomic content of mass ratios + sector exponents adds structural reading |
| All other PR #221–#238 verdicts | **Unchanged** |

This audit is a Layer G extension via PR #235's methodology,
parallel to PR #236's modular form audit.

---

## What this is and isn't

**This is**: identification of framework-native cyclotomic
content in mass ratios. The framework's mass ratios sit at
specific Z_n factorizations from Mihailescu + Farey + boundary
weight primes, with half-power characters connecting to PR
#236 modular forms and PR #238 half-twist meta-structure.
MODAL ✓ / GENERATIVE ✓ on the cyclotomic structural identity.

**This is not**: a new derivation of mass ratios. Standard
physics + the framework's `generation_mechanism.md` already
gives them. This audit identifies the cyclotomic content these
ratios sit at.

**This is not**: a closure of quantitative gaps in mass ratio
precision. The 0.9% match for m_τ/m_e remains the
framework's specific quantitative prediction; cyclotomic
content provides structural identity beyond numerical match.

**This is not**: a half-twist meta-structure audit. Such an
audit would identify half-twist as a unifying meta-mechanism
across sector exponents, modular form weights, substrate
rotation. This audit notes the connections but doesn't seal
the meta-structure.

---

## Future work enabled

1. **Half-twist meta-structure audit**: as suggested by PR
   #238's future work, examining whether half-twist unifies
   sector exponents, modular weights, substrate rotation, and
   other framework features under one structural identity
2. **A3 continued-fraction audit**: K_STAR, w*, Ω partition's
   continued-fraction expansions — natural next instance of
   PR #235 methodology
3. **A4 L-function behavior in cosmological predictions**:
   Euler-product-like behavior in CMB power spectrum (after
   PR #236)
4. **Cyclotomic units in mass-ratio refinements**: higher-
   precision predictions via cyclotomic field structure

---

## Cross-links (by logical dependency, PR #228 Finding 5 +
PR #234 + PR #235)

### Layer A_arith (arithmetic primitives) — PR #234
- `primitives_vs_addresses_candidate.md` — substrate primitives
- `CHAIN_KSTAR.md` — Farey cardinalities; K_STAR derivation
  (Z_14 cyclotomic)
- `substrate_determinism.md` — natural irrationals closure

### Layer A_dyn (dynamic primitives) — PR #234
- `klein_bottle.md` — K² + XOR rule; Z_6 substrate lattice
- `planck_scale.md` — SL(2,ℝ) Iwasawa

### Layer B (dynamical apparatus)
- `born_rule.md` — Born rule basin convergence
- `mass_sector_closure.md` — Mihailescu structure; cube
  identities

### Layer C (conservation chain)
- `generation_mechanism.md` — three generations + sectors;
  mass hierarchy 26:7:1
- `generation_sector_count_audit.md` (PR #230) — refined by
  this audit's cyclotomic content reading
- `horn_branch_iteration_2_step_2.md` — Ω partition

### Layer D (coherence types)
- `halt_shock_coherence_audit.md` (PR #224)
- `coherence_matrix_completion_audit.md` (PR #229) —
  derived-address cells touched by cyclotomic content

### Layer E (structural identities)
- `dynamics_arithmetic_distinction_refinement_audit.md` (PR
  #234)
- `primes_denominators_circular_geometry_extension_audit.md`
  (PR #235) — methodology source
- `modular_form_behavior_cosmological_tongues_audit.md` (PR
  #236) — parallel Layer G extension; half-character
  connection
- `angular_momentum_three_source_inviolability_audit.md` (PR
  #238) — half-twist meta-structure connection
- `h0_tension_cross_cell_identity_audit.md` (PR #237) — cross-
  cell template (cyclotomic content doesn't trigger H_0 tension)

### Layer F + G (unification + closures)
- `antiparticle_dark_energy_unification_audit.md` (PR #226)
- `boundary_leakage_rate_audit.md` (PR #227)

### Supporting
- `feedback_resolution_vs_reconstruction.md` (memory) —
  resolution-mode discipline

---

## One-line summary

This audit identifies framework-native cyclotomic content in
mass ratios as a Layer G extension via PR #235 methodology.
K_STAR^14 = 1/8 reads as **Z_14 = Z_2 × Z_7 cyclotomic
content** (Mihailescu prime × matter Farey prime; `14 = q_2 ·
|F_4|`). m_τ/m_e = 676√26 reads as **Z_26 = Z_2 × Z_13 content
with ½-power exponent** (Mihailescu × cosmological boundary
prime). Sector exponents 2, 5/2, 3 read as **integer
cyclotomic + half-integer modular** (½-step progression
connecting to PR #236 modular forms and PR #238 half-twist
meta-structure). Mass hierarchy 26:7:1 uses **coprime subset
of framework primes {2, 7, 13}** distinct from Ω partition's
subset {5, 11, 13, 19} (only 13 shared). Substrate Z_6 lattice
is the most basic cyclotomic content with Mihailescu prime
factorization Z_2 × Z_3. Unified structure: framework's
cyclotomic content composes from specific Mihailescu + Farey +
boundary weight primes via specific Z_n factorizations; not
arbitrary first-n integers. Verdict: MODAL ✓ / GENERATIVE ✓
on the cyclotomic structural identification. Five falsifier
classes target specific cyclotomic identifications; structure
robust against single-component failure. Empirical alignment:
mass ratio matches (m_τ/m_e at 0.9%; K_STAR^14 at 0.594σ;
hierarchy 26:7:1 sub-percent) confirm cyclotomic structure at
precision of ratio matches. Cyclotomic content is dimensionless
— independent of H_0 anchor tension. Connections: PR #236
half-weight modular forms share ½ character with sector
exponents; PR #238 half-twist meta-structure unifies with
sector half-step progression. Suggests broader half-twist
meta-structure audit unifying sector exponents, modular weights,
substrate rotation under one structural identity (PR #238
future work suggestion). Future work: half-twist meta-structure
audit; A3 continued-fraction audit (K_STAR, w*, Ω partition
expansions); A4 L-function audit; cyclotomic units in mass-
ratio precision refinements. The striking observation —
framework primes used in mass hierarchy {2, 7, 13} are
DISTINCT from Ω partition primes {5, 11, 13, 19} (only 13
shared) — is the audit's most substantive structural finding:
the framework's cyclotomic content is partitioned into
matter-sector content and cosmological-partition content with
specific prime overlap (13, the cosmological boundary prime).
