# The gluon's properties in framework terms: a reframing

> Strip away "which gluon." There was never a question — the eight
> gluons ARE the eight su(3)-sector mode transitions on the Klein
> 4-mode graph. The only thing the framework declines is the
> *anchor-side value* of α_s(M_Z), not the identification.

## The problem with "eight colored force carriers"

The textbook narrative gives the gluon a stack of primitive
properties: there are eight of them, they are massless, they carry
color charge (and so self-interact), they mediate the strong force,
and the strong coupling runs (asymptotic freedom + confinement).
Read literally, this is eight special objects, each carrying a
color label, posited to mediate QCD.

The framework does not posit gluons. The gauge dictionary
(`gauge_dictionary.md`) **forces** the identification: the Klein
bottle's 4-mode graph has 12 directed edges, decomposing as 8
cross-sector + 4 within-sector, matched to the 12 generators of
`su(3) ⊕ su(2) ⊕ u(1)` (8 off-diagonal + 4 Cartan). The su(3)
factor — 6 roots + 2 Cartan (`T₃, T₈`) = **8 generators** — is the
gluon octet. There is no "which gluon" question: the 8 su(3)-sector
mode transitions ARE the 8 gluons, and `gauge_dictionary.md` #3a
labels this correspondence **FORCED** by the graph/algebra
structure.

This document promotes that forced correspondence to a standing
gluon ontology, the same move as `photon_reframing.md`,
`higgs_reframing.md`, and `graviton_reframing.md`. **The gluon is
not a fundamental object. The su(3)-sector mode transition is.**

## What the gluon is

**A gluon is an su(3)-sector mode transition on the Klein 4-mode
graph.** SU(3) arises as the framework's color `Z₃` promoted to its
Lie-group home (`gauge_dictionary.md` Identification #2: the
arithmetic `Z₃` from GCD mod 3 on the XOR-filtered Stern-Brocot
tree IS the center `Z(SU(3))`; `gauge_factorization.md` for the
factorization). The eight gluons are the eight generators of su(3):

- **6 roots** ↔ 6 of the 8 cross-sector edges (the off-diagonal
  raising/lowering operators that move between color-fiber basis
  vectors)
- **2 Cartan** (`T₃, T₈`) ↔ 2 within-sector edges (the diagonal
  generators)

There is nothing further to identify. The eight are indistinguishable
except by their generator labels, exactly as the eight su(3)
generators are in the Standard Model.

## The precise statement

**A gluon is an su(3)-sector mode transition (one of the 8 su(3)
generators realized as edges on the Klein 4-mode graph). "Eight
massless colored force carriers with a running coupling" is the
coarse-grained shadow, with each clause forced:**

| Stated property | Framework term | Forced by |
|---|---|---|
| **Eight of them** | the 8 generators of su(3) = 6 cross-sector roots + 2 within-sector Cartan | `gauge_dictionary.md` #3a: 8 su(3)-sector edges ↔ 8 su(3) generators (FORCED) |
| **SU(3) color structure** | the framework `Z₃` (GCD mod 3 on XOR-filtered tree) promoted to `Z(SU(3))` | `gauge_dictionary.md` #2 + `gauge_factorization.md` (Cartan classification, centers Z₂ and Z₃) |
| **Color triplet (3 charges)** | the 3-element `Z₃`-torsor fiber (`q_2 = 3` scaling representatives) | `gauge_dictionary.md` #2 (regular rep of Z₃ on its 3-element underlying set) |
| **Carry color (self-interact)** | cross-sector edges move between color-fiber basis vectors — the gluons themselves change color | off-diagonal su(3) roots are non-abelian (the 6 roots) |
| **Masslessness** | no compact-`K` eigenfrequency — a mode transition, not an oscillator (same as photon/graviton) | absence of a compact-part eigenvalue (`speed_of_light.md`, `photon_reframing.md`) |
| **β-function / running** | the duty-cycle ratio runs as `K⁻¹`: `α_s(K) = (K²/8)·\|r\|(K)`, `d ln α_s/d ln K = 2 + d ln\|r\|/d ln K` | tongue-width K-dependence `(K/2)^q` at `q=2` partner (`beta_from_tongues.md` §4b) |
| **Asymptotic freedom / confinement** | high-K (UV) weak coupling, K→0 (IR) strong coupling — the duty ratio crosses over | the `(K/2)^q` exponential → power-law crossover near K=1 (`beta_from_tongues.md` §3) |

The "force carrier" clause dissolves the same way as for the
graviton: the framework has no exchanged-particle mediation, it has
mode transitions on the substrate graph. The gluon is the name for
an su(3)-sector transition, not an exchange on a background.

## What this does not derive — the refined bright line

This is a reframing, not a new prediction. The honest residual is
**not** an identification gap (there is none); it is an **anchor-side
amplitude gap**, the same shape as the photon's numerical `c` and
the A_s/Instance-7 closure:

- It does **not** derive the numerical value of **α_s(M_Z)**. The
  framework's bare K=1 identity is `α_s/α_2 = q_3³/q_2³ = 27/8 =
  3.375` (`MANIFEST.yml` `bare_k1_identities.alpha_s_over_alpha_2`,
  `duty_cycle_dictionary.md` §2). The 3.2% gap to the PDG value
  ≈ 3.488 at M_Z is the **anchor-side amplification factor**
  (Instance 7 of `vocabulary_is_the_work_pattern.md`), Class-2 by
  construction (Region C pigeonhole, `numerology_count_phase_b.md`).
  **This is the honest residual** — the framework supplies the
  *structure* of the strong sector (SU(3), the octet, the
  β-function K-running, asymptotic freedom) and correctly declines
  the *renormalized M_Z value*. The bright line is anchor-side, not
  identification-side.
- It does **not** claim QCD bound-state dynamics (confinement
  spectrum, hadron masses from first principles). The β-function
  *structure* runs the right way; the absolute confinement scale
  Λ_QCD is anchor-side.
- It introduces **no new framework integer and no new O(1) factor**
  (the 27/8 bare identity already exists; this doc adds no number).
  C-structural, not C-numerical per `statistical_conventions.md`.
- It changes **no entry in MANIFEST.yml** beyond pointing at the
  existing `bare_k1_identities` entry.

## Why this is NOT an observable-identification decline

The articulation audit (`articulation_audit_2026-05.md`, original
Axis A) first listed "gluon observable-identification" as an honest
decline. The post-audit revision corrected this: there is no
"which mode-transition is *observed as* the gluon" question, because
gluons are not individually distinguishable — they are the 8
generators of su(3), and `gauge_dictionary.md` #3a FORCES the
8-edge ↔ 8-generator correspondence. The decline that *is* real —
α_s(M_Z) — is anchor-side amplification, the same class as the
bare K=1 identities the framework already correctly declines. This
reframing crosses no bright line; it relocates the bright line to
where it actually lives.

## Distinct from the photon and the W/Z

- **Photon** (`photon_reframing.md`): the Ø-mode, the nilpotent
  radical `ℝ·N₊` — the unbroken U(1)_em generator, abelian, no
  self-coupling.
- **Gluons** (this doc): the 8 su(3)-sector transitions — non-abelian
  (the 6 roots carry color), self-coupling.
- **W/Z** (`wz_reframing.md`, when drafted): the su(2)-sector
  transitions at the q=2 tongue boundary — massive (the broken
  generators), the 2 su(2) roots + the mixing into the Cartan.

All four (photon, gluon octet, W/Z) are mode transitions on the same
12-edge Klein 4-mode graph; the gauge group `SU(3)×SU(2)×U(1)`
partitions the 12 edges into the three sectors. The reframings
articulate one sector each; `gauge_dictionary.md` is the master
correspondence.

## Status

**Reframing.** Sibling of `photon_reframing.md`, `graviton_reframing.md`,
`higgs_reframing.md`. Retains all numerical content of its parents
(`gauge_dictionary.md`, `gauge_factorization.md`, `beta_from_tongues.md`,
`duty_cycle_dictionary.md`); changes only the language and the
primary object. C-structural per `statistical_conventions.md`; not
C-numerical; the only numerical content (α_s/α_2 = 27/8) is the
pre-existing bare K=1 identity, unchanged.

The gluon's **identification** is closed at the ontological level —
it was never open; the 8-edge ↔ 8-generator correspondence is
FORCED (`gauge_dictionary.md` #3a). The gluon's **anchor-side
amplitude** (α_s at M_Z, Λ_QCD) is **not** resolved and remains the
honest residual, Instance-7-shaped, Class-2 by construction.

## Cross-references

- `gauge_dictionary.md` — the master correspondence: 12 mode
  transitions ↔ 12 gauge generators (#3a FORCED); `Z₃ ↪ Z(SU(3))`
  (#2). This doc names the su(3) octet as the gluons.
- `gauge_factorization.md` — the SU(3)×SU(2)×U(1) factorization;
  Cartan classification with centers Z₂ and Z₃.
- `beta_from_tongues.md` — the β-function from tongue-width
  K-running (§4b: `α_s(K) = (K²/8)·|r|(K)`; the K⁻¹ ratio running).
- `duty_cycle_dictionary.md` — the bare K=1 identity α_s/α_2 = 27/8
  (§2); the anchor-side residual.
- `MANIFEST.yml` `bare_k1_identities.alpha_s_over_alpha_2` — the
  27/8 entry, Instance-7 declined at M_Z.
- `photon_reframing.md`, `graviton_reframing.md`, `higgs_reframing.md`
  — sibling reframings; the shared no-compact-`K` masslessness, and
  the per-sector partition of the 12-edge graph.
- `vocabulary_is_the_work_pattern.md` Instance 7 — anchor-side
  amplification, the shape of the α_s(M_Z) residual.
- `articulation_audit_2026-05.md` — the audit (and post-audit
  revision) that promoted this from a mis-classified "decline" to a
  P1 articulation with a refined (anchor-side) bright line.

## One-line summary

A gluon is an su(3)-sector mode transition on the Klein 4-mode
graph; the eight gluons ARE the eight su(3) generators (6 roots + 2
Cartan), the correspondence FORCED by `gauge_dictionary.md` #3a —
there was never a "which gluon" question. SU(3) is the color `Z₃`
promoted to its Lie home; masslessness is the photon's reason; the
β-function runs from tongue-width K-dependence. The honest residual
is anchor-side α_s(M_Z) (the 27/8 bare identity's Instance-7
amplification), not identification.
