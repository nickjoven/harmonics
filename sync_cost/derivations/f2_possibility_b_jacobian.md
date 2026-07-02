# F2 Possibility B — Jacobian at the 4-mode XOR fixed point

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
The finding is **honest-null closure for Possibility B, in both
the discrete and continuum regimes**, for the reasons below. No
positive derivation is claimed; no fitted structure is asserted.

Consequence for F2: Possibility A ([[xor_continuum_limit]]
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

### Local mediant coupling: sparse but abelian

Mediant adjacency on the Stern-Brocot tree doesn't directly apply
to the 4 modes {A, B, C, D} — these are kink-content labels, not
rationals. The natural adjacency is the off-diagonal Hamiltonian
graph: `α ↔ β` when H_αβ is a single-excitation-flip amplitude:

- A ↔ B (create q₂=3 periodic 2π kink)
- A ↔ C (create q₁=3 antiperiodic π half-twist)
- A ↔ D (create composite; two-excitation, doubly suppressed)
- B ↔ D (differ by q₂ sector 3→2 plus half-twist add)
- C ↔ D (add q₂=2 kink to C's half-twist)
- B ↔ C: cross-sector, sector (2,3)→(3,2), requires topology change,
  strongly suppressed

The adjacency graph is a rooted tree (A at root, C nearest child,
B and D further) — **not a Cayley graph of a non-abelian group**.
The Jacobian in this basis is a sparse 4×4 with Schwinger-
suppressed off-diagonals; its symmetry group is the automorphisms
of the mode graph plus generic phase rotations, all abelian.

**No non-abelian structure emerges from mediant/adjacency coupling
on the discrete 4-mode substrate.**

### Hierarchical coupling: same conclusion

Ancestor/descendant structure on the Stern-Brocot rationals
{1/2, 1/3, 2/3} that underlie the (2,3) denominator classes gives
a graph with 1/2 as the parent of 1/3 and 2/3 (both mediants of
0/1 or 1/1 with 1/2). Mapping this back to modes {A, B, C, D}
requires the kink-content ↔ rational correspondence, which
factors through:

- q₂=3 kink (mode B) ↔ 1/3 or 2/3 winding in periodic-y
- q₁=3 half-twist (mode C) ↔ 1/3 winding in antiperiodic-x
- Mode D ↔ product of C and q₂=2 kink at 1/2

The hierarchical structure produces a tree-like coupling matrix.
Its symmetry group inherits the (mode) ↔ (rational) mapping's
automorphisms — the Z₂ swap 1/3 ↔ 2/3 in periodic-y, and
generic phase rotations. Abelian. No SU(3) or SU(2).

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

**Discrete regime conclusion**: for every candidate F, and directly
from the substrate-derived Hamiltonian spectrum, the 4-mode
XOR-filtered Jacobian's symmetry group is abelian — at most
U(1)^4. No non-abelian gauge structure, no room for
SU(3)×SU(2)×U(1). **B refuted in the discrete regime.**

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

## Combined honest-null closure

Possibility B has:

- **In the discrete regime**: a well-defined 4-mode XOR fixed
  point (the substrate-derived Hamiltonian) whose symmetry group
  is abelian (at most U(1)^4). B refuted.
- **In the continuum regime**: the 4-mode structure that B's
  criterion invokes does not exist. B's premise fails to hold.

There is no regime where B's closure criterion is **both**
well-defined **and** could yield SU(3)×SU(2)×U(1). B is closed as
an **honest-null** result with named obstruction: the XOR filter
that defines the 4-mode structure is discrete-only, and the
resulting discrete Hamiltonian's spectrum (substrate-derived,
non-degenerate) admits only abelian symmetry.

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
  `anchor_count_reaudit.md`. B's honest-null closure is one of the
  "multiple substrate-aligned techniques refuted" the discriminator
  requires; with the frame-bundle also closed (PR-1) that gives two
  named obstructions. A third — attempting Possibility A and
  finding a specific finite-tree obstruction — would let the
  discriminator activate.

The F2 epic issue (#268) closure criteria are otherwise unchanged.
B's honest-null closure counts as Wave-3 progress per the epic
body ("negative results being a valid outcome").

## What is **not** claimed

- **No claim that A is closed either way.** This doc addresses B
  only; A remains open, with its closure criterion articulated
  in `f2_scoping.md`.
- **No claim that the 4-mode Hamiltonian is the "wrong" object.**
  It is the substrate-derived object for the K=1 4-mode reduction.
  It just doesn't carry gauge structure.
- **No claim that F[N] for K < 1 is derived.** D11 Q #1 stays open.
  This doc's discrete-regime analysis bounds the answer across
  candidate forms; a specific derived F would sharpen but not
  overturn the conclusion (the substrate-derived Hamiltonian
  spectrum is the same object regardless of which F you route
  through, in the K=1 discrete limit).
- **No claim that SU(3)×SU(2)×U(1) is impossible in the framework.**
  The combinatorial identification Z_6 = Z_2 × Z_3
  (`gauge_factorization.md`) stands as Class 3. B's closure would
  have promoted it to forced; B's honest-null leaves it at
  Class 3.

## Downstream updates (proposed, not applied here)

Not edited in this PR — proposed for follow-up PRs:

- `framework_status.md` — new entry under an appropriate section
  (Eliminated? Honest-null? — the ledger's existing categories
  don't have an obvious slot for "possibility within an epic
  closed with named obstruction"; this may require a new category
  or a `[[f2_epic_state]]` pointer doc)
- `MANIFEST.yml::scorecard::gauge_group::closure_status` —
  refresh to note that B is closed honest-null; the entry stays
  at Class 5 combinatorial identification, not promoted to
  continuum-limit derivation
- `f2_scoping.md` §"Open possibilities" — mark B as closed
  honest-null, cite this doc

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

## Status

**F2 Possibility B: honest-null closure.** The 4-mode XOR-filtered
Jacobian is well-defined in the discrete regime and yields an
abelian symmetry group (at most U(1)^4) directly from the
substrate-derived non-degenerate spectrum
{0, 3.645, 9.580, 11.515}; the bright-line "scalar coupling → B
refuted" is struck for all-to-all F, and dimension counting rules
out SU(3)×SU(2)×U(1) inside u(4) for the derived spectrum. In the
continuum regime, the XOR filter dissolves per
[[xor_continuum_limit]], so B's premise ("4-mode XOR-filtered fixed
point") does not exist as a distinct object. No regime supports B's
closure criterion.

Open: (a) Possibility A ("discrete is physical") — now bears F2's
remaining weight; closure requires the finite tree to reproduce
gauge theory predictions without continuum limit. (b) Discriminator-
decline — B's honest-null joins the frame-bundle negative result
as a second named obstruction, one short of the multi-technique
threshold the Basepoint Principle requires. (c) D11 Open Q #1 —
F[N] for intermediate K remains underived; this doc's discrete-
regime bounds are stable across candidate forms, so closing Q #1
would sharpen but not overturn B's honest-null.

Side: substrate-side, honest-null closure of a Wave-3 possibility.
Class: partial F2 progress via named obstruction (Wave-3 valid
outcome per #268 epic body). Not a new derivation; a bounded
closure of one of the epic's two open possibilities.
Downstream: PR-4 candidates — (i) attempt Possibility A on a
specific finite-tree observable (anomaly cancellation is the
scoping doc's example); (ii) discriminator-decline articulation
if A hits its own obstruction. Selection deferred to a #268
epic-comment after this PR merges.
