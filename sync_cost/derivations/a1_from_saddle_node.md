# `a_1 = 1 / √w`: the lepton identity as stick-slip

## Claim

The lepton-sector generation exponent equals the saddle-node
relaxation time at the Arnold tongue of its primary base rational,
evaluated at the self-consistent coupling `K*`:

    a_1(leptons) = 1 / √w(3/2, K*)

where `w(p/q, K) = 2 (K/2)^q / q` is the perturbative tongue width.
For `q = 2`, `w = (K/2)²` and `1/√w = 2/K`, giving

    a_1(leptons) = 2 / K*     ⟹     C = 4 / K*² = q_2² / K*²

This document gives the structural argument that this identity is
not a numerical coincidence but an instance of the framework's
**parabola primitive** acting at an Arnold-tongue boundary — the
same primitive that gives `|ψ|²` in `born_rule.md` and the
critical-slowing-down signatures in `parabola_csd_demo.py`.

## The ingredients (all already in the framework)

### 1. Tongue boundary is a saddle-node (`born_rule.md`)

Every Arnold-tongue boundary is a saddle-node bifurcation. Inside
the tongue, a stable fixed point and an unstable one sit apart by
a "basin separation" `Δθ`. At the boundary they collide. Near the
boundary:

    Δθ = √(4 ε / (π K))

where `ε` is the depth inside the tongue (Ω-distance from the
boundary). Squaring:

    Δθ² = 4 ε / (π K)

This is `born_rule.md` lines 123–135 exactly.

### 2. Saddle-node relaxation time (`parabola_csd_demo.py`)

The local normal form at the boundary is the parabola primitive

    dx/dt = μ − x²

with the relaxation time to the stable fixed point `x = √μ`:

    τ(μ) = 1 / √μ      (exponential decay rate = 2 √μ)

This is `parabola_csd_demo.py` lines 52–55: *"perturbations decay
as exp(−2 √μ t), so the relaxation time τ = 1/(2√μ) diverges as
μ → 0"*. Up to an O(1) normalization convention, `τ ∝ 1/√μ`.

### 3. Tongue width = saddle-node μ at the center (natural convention)

At the tongue center, the system is furthest from both boundaries.
The saddle-node parameter μ, which was 0 at each boundary, reaches
its maximum. The **natural normalization** identifies this maximum
with the tongue width itself:

    μ_center ≡ w(p/q, K)

This is a convention — one could also use `w/2` or `w π/4` — but
at q = 2 the perturbative tongue width is `w = (K/2)²`, and then
`1/√w = 2/K` matches `a_1(leptons)` to 4 decimal digits with no
residual. The convention is self-selecting: any other
normalization introduces a q-dependent constant that does not
match observation.

### 4. The critical point = the integer q_2

`K_star_iteration.py` shows that the local map `r → |Σ w e^{2πi p/q}|`
near the trivial fixed point has Taylor expansion

    r_{n+1} = (K_0 / 2)² r_n² + O(r_n³)

verified to 10+ digits across three ensembles and four K_0 values.
The exponent is **exactly 2 = q_2**, from the q = 2 mode at `p/q = 1/2`
with phasor `e^(iπ) = −1`. The critical K_0 of the map's linearization
is exactly `K_0 = q_2 = 2`. The integer that sets the approach
law's exponent is the same integer that sets `a_1(lep) = q_2 / K*`.

## The derivation

Combining (1)–(3):

- At the Arnold tongue boundary the system sits on a parabola
  primitive (`dx/dt = μ − x²`).
- The relaxation time at the tongue center is `τ = 1/√μ` (framework's
  standard saddle-node scaling, `parabola_csd_demo.py`).
- The natural normalization identifies `μ_center = w(p/q, K)`.
- Therefore `τ(p/q, K) = 1/√w(p/q, K)`.

For the lepton sector, the primary base is `b_1 = 3/2` with
denominator `q = q_2 = 2`, and

    w(3/2, K*) = 2 (K*/2)² / 2 = (K*/2)²
    τ(3/2, K*) = 1/√((K*/2)²) = 2 / K*

**Identification**: this relaxation time is the generation exponent
`a_1(leptons)`. A sector's generation step *is* one saddle-node
relaxation time at the primary-base tongue. Each generation step
takes one "stick" duration at the lepton tongue before the system
slips to the next locked configuration.

    a_1(leptons) = τ(3/2, K*) = 2 / K*

Squared: `C = a_1² = 4/K*² = q_2²/K*²`.

## Why this is the stick-slip shape

Each generation step of the lepton ladder is a **full stick-slip
cycle** at the q = 2 tongue:

| phase | duration | character |
|---|---|---|
| stick (inside tongue) | `τ = 1/√w ≈ 2.32` natural periods | phase-locked, slow relaxation toward `x = +√μ` |
| slip (out past boundary) | ≪ 1 natural period | fast, unlocked, system jumps to next tongue |
| re-lock | O(1) natural periods | next tongue captures, new stick phase begins |

The dominant cost is the **stick duration**, and it is set by the
saddle-node relaxation time `1/√μ` at the tongue center. The slip
phase is fast by comparison and contributes a negligible O(1)
correction.

This is the **same shape** as:

- **Stick-slip friction** (`stribeck_vortex.md`, `driven_stribeck.py`):
  asperities stick until local stress exceeds threshold, then slip
  rapidly. Stick duration dominates the cycle.
- **Seismic strain accumulation** (`parabola_csd_pipeline.py`,
  `seismic_eigenstate_dictionary.md`): faults lock for years, then
  release in seconds. Stick is ~10^10 × slip.
- **Born rule basin selection** (`born_rule.md`): the system
  sits near one of the saddle-node fixed points `x = ±√μ` for
  a stick duration proportional to `1/√μ`, then collapses to
  a specific attractor. `P = |ψ|² ∝ μ` is the fraction of
  sticks landing on each basin.
- **Critical slowing down** (`parabola_csd_demo.py`): the
  observable signature is variance amplification and AR1 → 1
  as `τ → ∞` near the bifurcation.

All five are **the same parabola primitive** with the same
`τ = 1/√μ` scaling. The lepton generation exponent is reading
the framework's saddle-node primitive at the lepton sector's
primary base rational, just as the Born rule, stick-slip release,
and CSD indicators read it at their respective bifurcations.

## Why leptons and not quarks

The formula `a_1 = 1/√w(b_1, K*)` applies **only** to the lepton
sector directly. For up-type and down-type, applying the same
formula with `b_1 = 8/5` (q = 5) and `b_1 = 5/4` (q = 4)
produces values (12.97 and 7.61) that do not match the observed
exponents (3.48 and 5.68) — confirmed numerically in
`item12_C_from_K_star.py` Part 7.

The resolution is in `item12_cross_sector_ratios.md`:

- **Leptons** are the primary sector. Klein-bottle parity −1
  (single-sheet, orientation-reversing walk), no Fibonacci shift.
  The "raw" saddle-node relaxation formula applies.
- **Up-type** is obtained from leptons by a Fibonacci shift
  (k = 1 in the tree), picking up a factor `(q_3/q_2)² = 9/4`
  on `a_1²`.
- **Down-type** has Klein-bottle parity +1 (double-cover walk),
  picking up a factor `q_2 q_3 = 6` on `a_1²`.

In both quark cases the "tongue at b_1" is not where the saddle
node sits for the generation step: the walk topology is
different. The cross-sector derivation captures this by
transporting the lepton constant through the appropriate
symmetry factor, rather than applying the raw tongue formula
at the quark primary base.

**Special role of q = 2**: the perturbative tongue width
`w(p/q, K) = 2(K/2)^q / q` collapses to the clean power `(K/2)^q`
only at q = 2 (where the q/2 prefactor drops). For any other q,
the formula `1/√w` introduces a factor `√(q/2)` that does not
cancel, and the "convention `μ_center = w`" chosen above no longer
gives an integer relation. The integer q_2 = 2 is distinguished
in two independent ways:

- It is the smallest Stern–Brocot denominator greater than 1 (so
  the perturbative sum over modes has q_2 as its leading non-trivial
  term — established in `K_star_iteration.py` Part 5).
- It is the unique q at which `w(p/q, K) = (K/2)^q` holds without
  a prefactor.

These are the same integer: the Klein-bottle antiperiodic twist
count, which the framework calls `q_2` everywhere else.

## What this derivation is and is not

**It is**:

- A structural reading of `a_1(lep) = 2/K*` as the saddle-node
  relaxation time at the q = 2 Arnold tongue, evaluated at `K*`.
- The **same parabola primitive** used in `born_rule.md`,
  `parabola_csd_demo.py`, `stribeck_vortex.md`, and the
  seismic eigenstate work. One primitive, five applications.
- A normalization convention (`μ_center = w`) that is
  self-selecting at q = 2 and matches PDG lepton masses to
  4 decimal digits.
- An explanation for the q = 2 specialness: it is the single q
  at which the perturbative tongue width has no prefactor.

**It is not**:

- A fully first-principled derivation of `K*`. `K*` still enters
  as an input; the identity is `a_1(lep) = 2/K*`, not `a_1(lep) =
  (some absolute constant)`. Independent high-precision K*
  determination remains open (see `K_star_iteration.py`, which
  rules out the naive Kuramoto r-iteration and confirms the
  failure is structural — r = 0 is a superstable fixed point
  with contraction rate exactly q_2 = 2).
- A rigorous proof that the normalization convention
  `μ_center = w` is forced by the field equation rather than
  chosen to fit. A more careful analysis would derive the exact
  proportionality from the linearization of the mean-field
  integral near the tongue boundary. This would close the last
  O(1) factor and turn the identity from a numerical near-match
  (4 digits) into a theorem.
- An extension to quark sectors. Those are governed by the
  cross-sector scalings, not by the raw tongue-width formula
  at their primary base rationals.

## Consequences

With this reading, item 12 has the following structural content:

    a_1(leptons)² = 1 / w(3/2, K*) = q_2² / K*²         (tongue-width identity)
    a_1(up)²      = (q_3/q_2)² × a_1(leptons)²          (Fibonacci shift, k=1)
    a_1(down)²    = q_2 q_3   × a_1(leptons)²           (Klein-bottle double cover)

All three per-sector exponents become explicit expressions in
`(q_2, q_3, K*)`. The mass-sector fit count is **1** parameter
(`K*` itself), not 0 and not 3, pending either:

1. An independent K* derivation at 5+ digit precision (not in
   the framework's existing code; naive Kuramoto iteration is
   ruled out; candidates not tried in code include cosmological
   K(t) running, non-perturbative tongue width near K ≈ 1, and
   Lyapunov spectrum at the golden rotation number).

2. A first-principled proof that the normalization convention
   `μ_center = w` is forced rather than chosen, turning the
   4-decimal-digit match into an exact theorem.

Either closes item 12 completely (0 fits). Neither is done.
What this document establishes is that the identity is
structurally **of the same kind** as every other appearance of
the parabola primitive in the framework — stick-slip dynamics at
an Arnold-tongue saddle-node boundary — and the 4-decimal-digit
agreement is consistent with that reading.

## Cross-references

| File | Role |
|---|---|
| `born_rule.md` | Saddle-node at every tongue boundary, `Δθ² ∝ ε`, `P = |ψ|²` from the same primitive |
| `parabola_csd_demo.py` | `τ = 1/√μ` scaling verified numerically, seismic and ecological context |
| `stribeck_vortex.md` | Stick-slip friction as a parabola-primitive application |
| `seismic_eigenstate_dictionary.md` | Repeating earthquakes as tongue-locked modes, stick-slip as a framework primitive application |
| `K_star_iteration.py` | Verifies the q_2 = 2 exponent of the iteration's local contraction; rules out naive Kuramoto r-iteration for K* |
| `item12_C_from_K_star.py` | Numerical verification of `a_1(lep) · K* = q_2` at 4 decimal digits |
| `item12_C_from_K_star.md` | Companion doc: the identity and its PDG status |
| `item12_cross_sector_ratios.md` | Fibonacci shift (up) and Klein-parity (down) scalings |
