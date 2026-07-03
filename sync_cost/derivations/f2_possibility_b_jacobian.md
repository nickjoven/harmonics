# F2 Possibility B — Jacobian at the 4-mode XOR fixed point

## Status

**Structural-attempt null for Possibility B of [[f2_scoping]].**
The 4-mode XOR-filtered Jacobian of the D11 field equation is
well-defined only in the discrete regime (the substrate-derived
K=1 Hamiltonian of [[discrete_reduction_computed]]); its symmetry
group is at most U(1)^4, computed **explicitly for all three
D11-named candidate F forms** (all-to-all, local mediant,
hierarchical) and confirmed F-independently by dimension counting
on the derived non-degenerate spectrum {0, 3.645, 9.580, 11.515}
inside u(4). In the continuum regime the XOR filter dissolves per
[[xor_continuum_limit]], so B's stated premise ("4-mode
XOR-filtered fixed point") does not exist as a distinct object.
Obstructions are **exhibited** in both regimes.

Positive record from the explicit computation: the local-mediant
Jacobian carries an approximate SU(2)-like near-degeneracy on the
endpoint mode pair {B, D} broken at ~10⁻⁸ (third-order Schwinger
suppression through the B → A → C → D path). This does not
satisfy B's closure criterion (approximate not exact; SU(2)
alone not SU(3)×SU(2)×U(1)) but is the natural mechanism to
invoke if Possibility A ever needs approximate gauge structure
at high perturbative order.

Under [[basepoint_principle]]: Possibility B is **structurally
declined** (obstructions exhibited on the substrate's own
outputs) rather than operationally open. B joins the frame-bundle
approach ([[xor_continuum_limit]] §"What the topology does NOT
produce") as a second closed technique for F2.

**This closes Possibility B, not the F2 epic (#268).** The epic
remains open on Possibility A ("discrete is physical"), whose
closure criterion (finite tree reproduces gauge theory predictions
without continuum limit) is untouched by this doc. Per the F2
scoping doc's own three-way discriminator, honest-null closure of
F2 requires "multiple substrate-aligned techniques refuted with
named obstruction"; two of the four scoping-doc techniques are
now closed (frame-bundle in PR-1, F[N] Jacobian here), leaving
Possibility A's finite-tree techniques (Wilson-action on the
discrete tree; RG flow on the XOR-filtered measure) as the
remaining substrate-aligned attempts.

Class: 3 (arc-closing step for one F2 possibility; no new
primitive). Canonical vocabulary: **productive null** at the
possibility-arc level per [[canonical_glossary]] Section 8 —
"an arc that surfaces obstructions on substrate-admitted
possibility-space" — but stronger than the Koide-iter-14
disposition (operationally open, no obstruction proven), because
obstructions ARE exhibited here.

---

## What this doc is — and what it is not

Possibility B of [[f2_scoping]] (F2 epic, #268) claims that
gauge groups emerge from the Kuramoto mean-field functional F[N]
of `rational_field_equation.md` (D11) at the 4-mode XOR-filtered
fixed point, with **structure constants matching SU(3)×SU(2)×U(1)**.
The scoping doc identified this as the headline B calculation
and articulated a bright line:

> **Bright line**: if the averaging produces a scalar (rather than
> non-abelian-valued) coupling, Possibility B is refuted regardless
> of the structure constants that might appear in a more detailed
> analysis.

This doc executes that calculation on the substrate as it stands.
No positive derivation is claimed; no fitted structure is
asserted. Framework-wide vocabulary alignment (per Koide-iter-14
template): B is a **structural-attempt null** — the ledger's
`Eliminated` shelf category for "structural attempts tested null"
([[framework_status]] line 184), not the empirical shelf category
Koide K_lepton = 2/3 was moved to.

Consequence for the F2 epic: Possibility A ([[xor_continuum_limit]]
reading 1, "discrete is physical") now bears the entire remaining
weight of the F2 question, or the framework must move to a
Basepoint-Principle discriminator-decline
([[basepoint_principle]], [[anchor_count_reaudit]] pattern).

## The substrate state — what B has to work with

### F[N] is D11 Open Q #1

`rational_field_equation.md` (D11) Part II defines the field
equation and the mean-field functional F: {N(r/s) : r/s ∈ T} → ℝ
that carries the coupling:

    N(p/q) = N_total × g(p/q) × w(p/q, K_0 × F[N])

D11 Part VI Open Q #1 states this explicitly:

> Compute the mean-field functional F explicitly. For the
> gravitational case (K = 1, all-to-all), F is the Kuramoto
> order parameter. For local coupling (lattice), F depends on
> the Stern-Brocot tree metric. What is the correct F for
> intermediate cases?

The three candidate forms:

1. **All-to-all** (Kuramoto): F = (1/N_total) Σ_{r/s} N(r/s)
2. **Local (mediant coupling)**: F(p/q) depends on N at mediant
   neighbors in the Stern-Brocot tree
3. **Hierarchical**: F(p/q) depends on N at ancestor / descendant
   nodes

D11 does not derive which form the substrate forces. For B's
closure criterion to be well-defined, we need either a derived F
or a bounded analysis across all candidate forms. This doc does
the latter.

### The 4-mode XOR fixed point at K=1 is derived

`discrete_reduction_computed.md` (the canonical S_v(K=1) doc,
supersedes the earlier symmetric-spectrum reading of 16) delivers
the four XOR-surviving modes explicitly:

| Mode | Sector | Excitation |
|---|---|---|
| **A** | (2,3) both locked | vacuum, `φ ≡ 0` |
| **B** | (2,3), q₂=3 unlocked | full 2π kink, periodic-y, 3 sites |
| **C** | (3,2), q₁=3 unlocked | π half-twist, antiperiodic-x, 3 sites |
| **D** | (3,2), q₁=3 & q₂=2 unlocked | q₁=3 half-twist + q₂=2 kink + crossing |

With diagonal Hamiltonian (Planck units):

    H_AA = 0
    H_BB = 2π²/3 + 3 ≈ 9.580
    H_CC = π²/6  + 2 ≈ 3.645
    H_DD = π²/6 + 2 + π² + 2 − 4 ≈ 11.515

The **B/C asymmetry** (H_BB ≠ H_CC) is structural, grounded in
`xor_derivation.md` §3.3's homotopy theorem — every antiperiodic-x
configuration accumulates net π (not 2π). This resolves what
would otherwise be a load-bearing assumption.

Off-diagonal amplitudes are Schwinger-suppressed:
`g_αβ ∼ exp(−S_excitation)`, with the largest being A↔C
(≈ exp(−3.645) ≈ 0.026). Eigenvalue corrections are O(g²/ΔE) ≲ 10⁻⁴.
The 4×4 matrix is near-diagonal.

## The natural observable — analog to PR-2's cos(φ_a − φ_b)

PR-2 (`f2_fm_beat_results.md`) noted that the composite-mode
observable cos(φ_a − φ_b) is the natural physical operator whose
K=0 spectrum realizes the audit's modal selection rule. The
analog on the 4-mode substrate is direct: **the Hamiltonian
eigenspectrum itself**. Each energy level H_αα is directly
observable (as excitation energy from vacuum); each off-diagonal
element H_αβ governs a transition amplitude. Unlike the frequency
domain of PR-2, no derived observable is needed — the substrate's
own operators are the probes.

This means B's closure criterion translates to: does the 4×4
Hamiltonian's symmetry group contain SU(3)×SU(2)×U(1)?

## The discrete-regime Jacobian

### All-to-all F: Jacobian is rank-1

Linearizing the field equation around the 4-mode fixed point N*:

    δN(α) = N_total × g(α) × w'(α, K_0F*) × K_0 × Σ_β (∂F/∂N_β)|_{N*} × δN(β)

The Jacobian's α-row is:

    J_{αβ} = N_total × g(α) × w'(α, K_0F*) × K_0 × (∂F/∂N_β)|_{N*}

For all-to-all F: ∂F/∂N_β = 1/N_total (independent of β).
Every column of J is the same vector `g(α) × w'(α, K_0F*) × K_0`;
J is **rank 1**. A rank-1 Jacobian has one nonzero eigenvalue,
one associated eigenvector, and a 3-dimensional kernel — no
Lie-algebra structure to speak of, and certainly no
non-abelian-valued coupling.

**Bright line: struck. B refuted for all-to-all F.**

### Local mediant F: explicit Jacobian

Mediant adjacency on the Stern-Brocot tree doesn't directly apply
to the 4 modes {A, B, C, D} — these are kink-content labels, not
rationals. The natural adjacency is the single-flip Hamiltonian
graph. From `discrete_reduction_computed.md`'s off-diagonal
Schwinger-suppression structure, the single-flip amplitudes are:

- g_AB = exp(−S_B) = exp(−9.580) ≈ 6.9×10⁻⁵
- g_AC = exp(−S_C) = exp(−3.645) ≈ 0.026
- g_CD = exp(−S_{q₂=2 kink}) = exp(−11.870) ≈ 6.9×10⁻⁶

No single-flip A–D (two-excitation), B–C (cross-sector, topology
change), or B–D (sector flip + excitation add). **The adjacency
graph is the path B–A–C–D.**

Local F treated as vector-valued (per-node K, D11 line 144):
`F_α[N] = c_α + Σ_{β~α} g_{αβ} N_β`. Jacobian
`J_{αβ} = d_α × ∂F_α/∂N_β` where
`d_α = N_total × g(α) × w'(α, K₀F*_α) × K₀`.

Similarity-transformed to symmetric form (ordering B, A, C, D):

    J_sym = [  0     α_AB    0      0    ]
            [ α_AB    0     α_AC    0    ]
            [  0     α_AC    0     α_CD  ]
            [  0      0     α_CD    0    ]

with `α_AB = √(d_A d_B)·g_AB ≈ 6.9×10⁻⁵`,
`α_AC = √(d_A d_C)·g_AC ≈ 0.026`,
`α_CD = √(d_C d_D)·g_CD ≈ 6.9×10⁻⁶` (using `d_α ≈ 1`
normalization; the qualitative structure is d-independent).

Tridiagonal weighted path-graph adjacency. **Leading-order
eigenvalues** (with α_AB, α_CD → 0):
- {A, C} block: eigenvalues ±α_AC ≈ ±0.026
- {B, D} isolated: two zero eigenvalues

The leading-order **2-fold zero degeneracy on {B, D}** is a
genuine structural feature — it would support an approximate
SU(2)-like near-symmetry on that subspace. Degeneracy-lifting:
direct second-order shifts cancel
(`⟨B|H_eff|B⟩ = |α_AB|²(−1/α_AC + 1/α_AC) = 0`); first
non-vanishing splitting is **third-order** through the
B → A → C → D path:

    δ ~ α_AB · α_CD / α_AC ≈ 1.8×10⁻⁸

The {B, D} near-symmetry is broken at the **10⁻⁸ level** by
Schwinger-suppressed transition amplitudes.

**This still fails B's closure criterion** for four reasons:
1. The near-symmetry is approximate (broken at 10⁻⁸), not exact
2. It's SU(2)-like on {B, D} only — no SU(3) anywhere
3. {B, D} are the endpoint modes (2π periodic-y kink; half-twist +
   q₂=2 kink + crossing) — not structurally paired the way
   weak-isospin doublets are. The near-degeneracy is a graph-
   topology artifact of the path adjacency, not a substrate-
   forced flavor symmetry
4. B requires **SU(3)×SU(2)×U(1) exact with matching structure
   constants**, not an approximate SU(2) at high perturbative
   order

**Local mediant F: full symmetry group U(1)^4 exact; approximate
SU(2)-like on {B, D} broken at 10⁻⁸. B refuted.**

Worth recording honestly: the leading-order {B, D} degeneracy is
a genuine structural feature of the local-mediant Jacobian on the
substrate-derived path adjacency, and it would be the natural
mechanism to invoke if Possibility A ever needed to produce
approximate gauge structure at high perturbative order.

### Hierarchical F: explicit Jacobian

Hierarchical coupling by sector labels {(2,3): A, B} and
{(3,2): C, D}. F_α depends on N at same-sector modes only.

Block-diagonal Jacobian (in the sector basis):

    J_sym = [  0     β_AB    0      0    ]
            [ β_AB    0      0      0    ]
            [  0      0      0     β_CD  ]
            [  0      0     β_CD    0    ]

Each 2×2 block has eigenvalues ±|β|. Total spectrum:
(+β_AB, −β_AB, +β_CD, −β_CD).

Generically β_AB ≠ β_CD: the intra-sector couplings in (2,3) and
(3,2) come from structurally distinct sectors — different
denominator parities, different homotopy behavior per
`xor_derivation.md` §3.3. The B/C asymmetry that forces
H_BB ≠ H_CC forces the analogous inter-sector coupling asymmetry.

Symmetry between sectors would require β_AB = β_CD, which the
substrate does not deliver — the same homotopy theorem that
breaks the H_BB = H_CC symmetry breaks it here first.

**Hierarchical F: symmetry group U(1)^4 exact. No emergent
non-abelian structure. B refuted.**

### Spectrum-based analysis: same conclusion, structural version

Skipping F entirely: the 4×4 Hamiltonian has non-degenerate
spectrum {0, 3.645, 9.580, 11.515}. For any Hermitian 4×4 matrix
with non-degenerate spectrum, the symmetry group (matrices
commuting with it) is U(1)^4 — one phase per eigenvector.

Dimension counting rules out SU(3)×SU(2)×U(1): dim = 8+3+1 = 12,
while dim(U(1)^4) = 4. Even the ambient u(4) (dim 16) does not
contain SU(3)×SU(2)×U(1) as a subgroup — SU(3) requires at least
a 3-dimensional fundamental representation, and its
complement-partner SU(2) requires 2 more dimensions, total ≥ 5 > 4.

The pre-derivation symmetric spectrum (0, 8, 8, 16) that this
doc's canonical replacement supersedes WOULD have carried
partial structure: {B, C} degeneracy at 8 could have supported
an SU(2)-like action. **But H_BB ≠ H_CC is forced by
`xor_derivation.md` §3.3's homotopy theorem — the asymmetry is
substrate-derived, not a modeling choice**. The SU(2)-degenerate
reading is ruled out at the substrate level, not by convention.

### Discrete regime summary — all three F candidates explicitly computed

| Candidate F | Jacobian structure | Symmetry group | B closure? |
|---|---|---|---|
| **All-to-all** | rank-1 outer product | U(1) × 3-dim kernel | Refuted (bright line struck) |
| **Local mediant** | tridiagonal path B–A–C–D | U(1)^4 exact; approximate SU(2)-like on {B, D} broken at ~10⁻⁸ | Refuted — approximate not exact; SU(2) not SU(3); endpoint modes not doublet partners |
| **Hierarchical (by sector)** | block-diagonal 2⊕2 with β_AB ≠ β_CD | U(1)^4 exact, no emergent symmetry | Refuted — homotopy theorem breaks inter-sector symmetry |

Directly from the substrate-derived Hamiltonian spectrum (spectrum
argument, F-independent), any Hermitian 4×4 with non-degenerate
spectrum has symmetry group U(1)^4, and dimension counting rules
out SU(3)×SU(2)×U(1) inside u(4). The three-way explicit
computation confirms the F-agnostic spectrum argument at the
matrix level and adds one refined observation: the local-mediant
case carries an **approximate SU(2)-like near-degeneracy on {B, D}
broken at ~10⁻⁸**, a graph-topology artifact of the path
adjacency. It doesn't satisfy B's closure criterion (exact,
matching SU(3)×SU(2)×U(1)) but is the natural mechanism to
invoke if Possibility A ever needed approximate gauge structure
at high perturbative order.

**Discrete regime conclusion: B refuted across all three candidate
F forms and directly from the substrate-derived spectrum.**

## The continuum-regime Jacobian

Possibility B's letter is about the **continuum limit** of F[N].
The scoping doc places B in the continuum, following D11 Part III
§"The continuum limit" and D11 Part V §"Kuramoto → Synchronization
field equation" — take d → ∞ and N_total → ∞ simultaneously.

**But the 4-mode XOR structure does not survive this limit.**
[[xor_continuum_limit]] §"The continuum limit of the filter"
states this explicitly:

> In the continuum limit (d → ∞, Farey measure → Lebesgue), the
> distinction between even and odd denominators vanishes — every
> real number is a limit of rationals with both even and odd
> denominators. The XOR filter, defined by denominator parity,
> has no direct analog on the reals.

And §"The gap, precisely stated":

> The Klein bottle's field equation at finite depth selects
> denominator classes {2, 3}. These numerically match {SU(2),
> SU(3)}. But in the continuum limit, the mechanism that selects
> these denominators (the XOR filter on the Stern-Brocot tree)
> dissolves — the discrete parity distinction has no direct
> analog on the continuum Klein bottle.

So in the continuum limit, the "4-mode XOR fixed point" is not a
distinct object from the general Kuramoto continuum fixed point.
There is no 4-mode subspace to compute a Jacobian on; the field
equation runs on all of Q (in the limit, all of ℝ), and its
Jacobian is the standard Kuramoto continuum object, which
carries no discrete-mode structure at all.

**Continuum regime conclusion**: Possibility B's closure criterion
is not well-defined in the continuum — the "4-mode XOR-filtered
fixed point" it names does not exist as a distinct object when the
XOR filter dissolves. **B's premise is untenable in the continuum.**

## Combined disposition — structural-attempt null

Possibility B has:

- **In the discrete regime**: a well-defined 4-mode XOR fixed
  point (the substrate-derived Hamiltonian) whose symmetry group
  is abelian (at most U(1)^4). B refuted.
- **In the continuum regime**: the 4-mode structure that B's
  criterion invokes does not exist. B's premise fails to hold.

There is no regime where B's closure criterion is **both**
well-defined **and** could yield SU(3)×SU(2)×U(1). Obstructions
are exhibited in both regimes: the substrate-derived non-
degenerate spectrum (discrete) and the XOR-filter dissolution
(continuum). Per [[framework_status]] line 184's ledger category,
this is a **structural-attempt null** — B moves to the
`Eliminated` shelf as a derivation-strategy attempt tested null,
not to the empirical shelf (which houses noted-but-not-derived
values like Koide K_lepton = 2/3 or sin²θ_W).

## What this means for F2 (updates to [[f2_scoping]])

The scoping doc articulated F2 as reducing to two remaining
possibilities after the frame-bundle negative result. With B now
closed:

- **Possibility A ("discrete is physical")** now bears the entire
  remaining weight of the F2 gauge-structure question. Its
  closure criterion is unchanged: show that the finite Stern-Brocot
  tree at depth d reproduces gauge theory predictions
  (cross-sections, anomaly cancellation, coupling running) without
  taking the continuum limit. This is a **paradigm shift** — commit
  to "the universe is discrete at depth d; gauge groups live in
  finite combinatorics, not Lie algebras" — not a gap closure.

- **Discriminator-decline** remains available: show that gauge
  structure necessarily requires an observational anchor parallel
  to the two-anchor minimum's disposition in
  `anchor_count_reaudit.md`. B's structural-attempt null is one of
  the "multiple substrate-aligned techniques refuted" the
  discriminator requires; with the frame-bundle also closed (PR-1)
  that gives two named obstructions. A third — attempting
  Possibility A and finding a specific finite-tree obstruction —
  would let the discriminator activate.

The F2 epic issue (#268) closure criteria are otherwise unchanged.
B's structural-attempt null counts as Wave-3 progress per the
epic body ("negative results being a valid outcome").

## What is **not** claimed

- **No claim that A is closed either way.** This doc addresses B
  only; A remains open, with its closure criterion articulated
  in `f2_scoping.md`.
- **No claim that the 4-mode Hamiltonian is the "wrong" object.**
  It is the substrate-derived object for the K=1 4-mode reduction.
  It just doesn't carry gauge structure.
- **No claim that F[N] for K < 1 is derived.** D11 Q #1 stays open.
  This doc's discrete-regime analysis explicitly computes Jacobians
  for all three D11-named candidate F forms (all-to-all, local
  mediant, hierarchical); each fails B's closure criterion. The
  spectrum argument (dimension counting on the substrate-derived
  Hamiltonian) is F-independent and gives the same conclusion
  directly. A future substrate-derived F would need to escape
  BOTH the F-agnostic spectrum bound AND the three explicit
  candidate results to reopen B, which is a strong constraint.

- **Positive record**: the local-mediant Jacobian carries an
  approximate SU(2)-like near-degeneracy on {B, D} broken at
  ~10⁻⁸ (third-order Schwinger suppression). This is a genuine
  structural feature of the path-adjacency Jacobian, discovered
  by the explicit computation rather than the spectrum argument.
  It does not satisfy B's closure criterion (approximate, not
  exact; SU(2)-like, not SU(3)×SU(2)×U(1)) but is worth recording
  as a possible mechanism for approximate gauge structure at high
  perturbative order if Possibility A ever needs it.
- **No claim that SU(3)×SU(2)×U(1) is impossible in the framework.**
  The combinatorial identification Z_6 = Z_2 × Z_3
  (`gauge_factorization.md`) stands as Class 3. B's closure would
  have promoted it to forced; B's structural-attempt null
  leaves it at Class 3.

## The disposition update

Applied to the framework's canonical ledgers in follow-up PRs
(not edited here):

| Item | Previous | Updated |
|---|---|---|
| `framework_status.md` **Eliminated** section | 5 structural-attempt nulls listed (line 184-190) | Add: "F2 Possibility B — F[N] Jacobian at 4-mode XOR fixed point — abelian symmetry (U(1)^4 at derived spectrum) + XOR dissolves in continuum; both regimes obstruct SU(3)×SU(2)×U(1). See `f2_possibility_b_jacobian.md`" |
| `MANIFEST.yml::scorecard::gauge_group::closure_status` | Class 5 (exact) — combinatorial Z_6 = Z_2 × Z_3 | Unchanged — the combinatorial identification stands at Class 5; B's null forecloses its promotion to continuum-limit derivation but does not demote the existing identification |
| `f2_scoping.md` §"Open possibilities" | A and B both open | B marked closed (structural-attempt null); A remains open; pointer to this doc |
| F2 epic (#268) | Two possibilities open | One remaining (A); progress toward "multiple techniques refuted" threshold for eventual honest-null closure of F2 itself (2 of 4 scoping-doc techniques now closed) |

Not proposed:

- No new entry on the empirical shelf (B is not a value, it is
  a derivation strategy)
- No update to Class 5 gauge_group identification — the Z_6 =
  Z_2 × Z_3 combinatorial coincidence stands independent of B
- No discriminator-decline yet; two named obstructions is one
  short of the "multiple techniques" threshold per the scoping
  doc's own criteria

## Cross-references

| File | Role |
|---|---|
| `f2_scoping.md` (#271) | The Class-3 articulation this PR-3 executes against |
| `rational_field_equation.md` (D11) | The mean-field functional F[N] and Open Q #1 |
| `xor_continuum_limit.md` | The XOR-filter-dissolves-in-continuum result that closes B's continuum reading |
| `discrete_reduction_computed.md` | The substrate-derived 4-mode Hamiltonian at K=1 |
| `xor_derivation.md` §3.3 | The homotopy theorem forcing H_BB ≠ H_CC |
| `figure_eight.md` D19 | The four-mode sector definitions |
| `basepoint_principle.md` | The discriminator framework A now sits closer to |
| `anchor_count_reaudit.md` | Template for a discriminator-decline closure |
| `gauge_factorization.md` | The Z_6 = Z_2 × Z_3 combinatorial identification — Class 3 stands |

## One-line summary

Possibility B of the F2 epic — gauge groups from the F[N]
Jacobian at the 4-mode XOR fixed point with structure constants
matching SU(3)×SU(2)×U(1) — closes as a **structural-attempt null**
with obstructions exhibited in both regimes: the substrate-derived
non-degenerate spectrum {0, 3.645, 9.580, 11.515} admits at most
U(1)^4 symmetry (dimension counting rules out SU(3)×SU(2)×U(1)
inside u(4)) in the discrete regime — with the local-mediant F
Jacobian's explicit computation additionally revealing an
approximate SU(2)-like near-degeneracy on the endpoint mode pair
{B, D} broken at ~10⁻⁸ (third-order Schwinger suppression), a
path-adjacency artifact that doesn't satisfy B's closure criterion
but records a possible mechanism for approximate high-order
gauge structure — and the XOR filter that defines the 4-mode
structure dissolves in the continuum regime; Possibility B moves
to [[framework_status]]'s `Eliminated` shelf as a
derivation-strategy null. The F2 epic itself remains open on
Possibility A ("discrete is physical"); this doc closes one of
its two remaining substrate-aligned techniques, joining the frame-
bundle refutation from [[xor_continuum_limit]].
