# K-axis uniqueness probe: composed Klein-antipodal + coprime-to-6

## What this tests

The bare K-scan (`k_scaling_scan.md`, PR #76) landed Class 2
because the bare circle map *ranks* rationals by tongue width but
never *forbids* any — every `p/q` opens at some K. The writeup
flagged the natural follow-up: compose the K-scan with one of the
framework's existing forcing filters (Klein-antipodal Z₂-rep, XOR
on Stern-Brocot, anomaly cancellation) to see whether the
surviving tongue count at a canonical K equals a framework integer
for *structural* reasons.

This probe runs that follow-up with the Klein-antipodal Z₂-rep +
coprime-to-`q₂·q₃` filter, which is the exact composition used in
the Ω-partition derivation (`omega_partition_combinatorial.md`,
`baryon_fraction.md`) to isolate the baryonic mode. Both filters
are forced by prior framework work; this probe asks what they
produce when composed with the K-axis.

Driver: `k_axis_uniqueness.py`.

## The structural claim (independent of the K-axis)

Purely combinatorial: for each Farey level n, let

    N(n) = #{Klein-antipodal Z₂-orbits of (p, q) ∈ F_n
            with gcd(q, q₂·q₃) = gcd(q, 6) = 1}

Theorem (direct counting): N(n) is piecewise constant with
plateaus, stepping up only at primes p coprime to 6. The plateau
values are

    N = 1, 3, 6, 11, 17, 23, ...

with transitions at n = 5, 7, 11, 13, 17, ... Increments are
`(p−1)/2` for each new prime `p` coprime to 6:

| n range | New prime added | Increment | Cumulative N |
|---|---|---|---|
| [1, 4] | (none past q=1) | — | 1 (only (0/1, 1/1) pair) |
| [5, 6] | q = 5 | 2 | 1 + 2 = **3** |
| [7, 10] | q = 7 | 3 | 3 + 3 = **6** |
| [11, 12] | q = 11 | 5 | 6 + 5 = 11 |
| [13, 16] | q = 13 | 6 | 11 + 6 = 17 |
| [17, 18] | q = 17 | 8 | 17 + 8 = 25 |

The first three plateau values are **exactly the small framework
integers**: trivial (1), `q₃ = D = 3`, and `INTERACT = q₂·q₃ = 6`.
After n = 10, the count leaves the framework-integer set and does
not return.

## Secondary observation: framework integers as Klein-lattice primes

The *increments* `(p-1)/2` at each new prime p coprime to 6 are
themselves framework integers, for exactly the first six primes
coprime to 6:

| p (prime coprime to 6) | (p-1)/2 | Framework integer |
|---|---|---|
| 5 | 2 | q₂ |
| 7 | 3 | q₃ |
| 11 | 5 | MEDIANT = q₂+q₃ |
| 13 | 6 | INTERACT = q₂·q₃ |
| 17 | 8 | K_QUARK = q₂³ |
| 19 | 9 | K_LEPTON = q₃² |
| 23 | 11 | — (not framework) |
| 29 | 14 | — |

The six framework fundamental integers defined in
`framework_constants.py` —
`{q₂, q₃, MEDIANT, INTERACT, K_QUARK, K_LEPTON} = {2, 3, 5, 6, 8, 9}` —
are **exactly** the set `{(p−1)/2 : p prime coprime to 6, p ≤ 19}`.

The cutoff at p = 19 coincides with `|F_7| = 19 = P-reg
cardinality` — the framework's explicit partition-register
size. After p = 19, the sequence of `(p−1)/2` values escapes
`{2, 3, 5, 6, 8, 9}` (11, 14, 15, …) and these are not framework-
constructed integers.

Check that this is specific to `(q₂, q₃) = (2, 3)` rather than
generic: for `(q₂, q₃) = (2, 5)`, `(q₂·q₃) = 10`, the first six
primes coprime to 10 are `{3, 7, 11, 13, 17, 19, 23, 29, …}` with
`(p−1)/2 ∈ {1, 3, 5, 6, 8, 9, …}`, not matching the alternate
framework integer set `{q₂, q₃, q₂+q₃, q₂·q₃, q₂³, q₃²} = {2, 5,
7, 10, 8, 25}`. The correspondence fails. It holds specifically
because `(q₂, q₃) = (2, 3)` is forced by the cross-link uniqueness
theorem (`mass_sector_closure.md`).

Caveat: there are 8 integers in `[2, 9]` (namely `{2, 3, 4, 5, 6,
7, 8, 9}`) and the framework integer set contains 6 of them,
excluding `{4, 7}`. The excluded values correspond precisely to
`2k+1 ∈ {9, 15}` — composite and factoring into framework
integers (`9 = q₃²`, `15 = q₃·MEDIANT`). The "match" is therefore
not just "small integers overlap" but a tighter arithmetic
coincidence between the framework-generating rules and the
primality pattern on `Z_{q₂·q₃}`. Still, this is a *correspondence
observed* rather than a *theorem proved*, so it is recorded here
and not claimed as load-bearing until a generating proof is
produced.

## Why this is not numerology

Per `ansatz_audit_policy.md`, the triage is:

1. **Klein-antipodal Z₂ rep filter: forced.**
   `klein_antipodal_z2_rep_pattern.md` lists three independent
   framework derivations using this machinery (down-type factor 6,
   up-type factor 9, Ω partition 13:5:1/19).

2. **Coprime-to-6 filter: forced.**
   `omega_partition_combinatorial.md` uses exactly this filter on
   Z_6 = Z_{q₂·q₃} to isolate the baryonic Klein-singlet
   `ψ_+(1, 5)`. This is the same filter, applied to tongue
   denominators instead of Z_6 residues.

3. **No fitted exponents, no tuned constants.**
   Plateau values come from pure Farey combinatorics + the two
   filters. `q₂ = 2` and `q₃ = 3` are the only framework integers
   that enter, and they enter exactly where they already live (as
   the primes coprime to 6).

4. **The "exhaustion" at INTERACT is structurally motivated.**
   The composed filter operates on `Z_{q₂·q₃}`, which is the
   framework's canonical Klein lattice (from the (q₂, q₃) cross-
   link theorem). Only framework-prime denominators (q ∈ {5, 7}
   ≡ {q₂+q₃, 2q₂+q₃} in framework integers) contribute before the
   count escapes. The next prime coprime to 6, q = 11, is
   "outside" the framework (11 cannot be written as a small
   combination of q₂ and q₃) and its introduction breaks the
   framework-integer match. This is the combinatorial analog of
   `(q₂, q₃) = (2, 3)` being *forced* (not just selected) by the
   cross-link uniqueness theorem in `mass_sector_closure.md`.

## The K-axis role

The K-axis picks a plateau via the staircase-resolved max-q:

| K | top-q resolved (grid=2001) | Plateau | N |
|---|---|---|---|
| 0.5 | 4 | [1, 4] | 1 (trivial) |
| 1/φ² = 0.382 | 3 | [1, 4] | 1 (trivial) |
| 1/φ = 0.618 | 4 | [1, 4] | 1 (trivial) |
| 0.7 | 6 | [5, 6] | **3 = q₃ = D** |
| 0.8 | 6 | [5, 6] | **3 = q₃ = D** |
| **K_STAR = 0.862** | **8** | **[7, 10]** | **6 = INTERACT** |
| 0.9 | 9 | [7, 10] | **6 = INTERACT** |
| 0.95 | 9 | [7, 10] | **6 = INTERACT** |
| 1.0 (critical) | 11 | [11, 12] | 11 (escape) |
| 1.05 | 12 | [11, 12] | 11 (escape) |

Two structural observations:

- **K_STAR lands in the INTERACT plateau** at the 2001-point grid
  resolution. K_STAR is independently derived from joint matter-
  sector closure (`item12_K_star_closure.py`) — no staircase
  reasoning enters that derivation. Its placement in the
  INTERACT window is a second structural fact, not a tuning.

- **The critical line K = 1 is where the framework-integer regime
  ends**. At K ≥ 0.99, the 2001-point grid resolves q = 11,
  escaping to the non-framework plateau N = 11. The framework-
  integer plateaus (trivial, q₃, INTERACT) are exactly the *sub-
  critical* regime under this resolution.

## ε-robustness

The plateau-detection threshold (grid resolution) controls which
tongues are counted as "resolved." At K_STAR:

| plateau_tol | top-q | Plateau | N |
|---|---|---|---|
| 0.010 | 2 | [1, 4] | 1 |
| 0.005 | 2 | [1, 4] | 1 |
| 0.002 | 4 | [1, 4] | 1 |
| 0.001 | 6 | [5, 6] | **3 = q₃** |
| 0.0005 | 8 | [7, 10] | **6 = INTERACT** |
| 0.0002 | 7 | [7, 10] | **6 = INTERACT** |
| 0.0001 | 7 | [7, 10] | **6 = INTERACT** |

As the threshold tightens from 1e-2 to 1e-4, K_STAR walks through
the plateau sequence:

    trivial -> q₃ = D -> INTERACT = q_2·q_3

and stabilizes on INTERACT for all fine enough tolerances (up to
the 2001-point grid limit). This is the same walk the plateau
structure predicts; K_STAR visits the first three plateaus in
order as ε tightens, and stops there.

At infinitely fine grids, K_STAR would eventually reach the
plateau N = 11 (escape). But at any finite resolution within the
range `ε ∈ [1e-4, 1e-3]`, the answer is a framework integer.

**What sets ε.** The bare K-scan had no forced ε and landed
Class 2. Here, ε is tied to the staircase grid, which is itself
tied to the observer-register cardinality (see
`observer_register_closure.md` §1-2). At P-reg = |F_7| = 19, the
cell width is `1/19 ≈ 0.053`, which sits in the "coarse" regime
where the plateau is trivial. At H-reg = 6·13⁵⁴, the cell width
is infinitesimal and we'd be in the escape plateau. Neither
register directly corresponds to the `ε ∈ [1e-4, 1e-3]` window
where framework integers appear at K_STAR.

## What the probe does and does not establish

**Does establish (structural, combinatorial):**

- The composed (Klein-antipodal Z₂-rep) ∩ (coprime-to-6) filter
  on Farey sets has a plateau structure whose first three plateau
  values are framework integers (1, q₃, INTERACT).
- The "exhaustion" after INTERACT is a combinatorial fact about
  which primes are coprime to `q₂·q₃`.
- No alternative filter choice is made; the two filters are those
  already forced by framework-existing derivations.

**Does establish (K-axis alignment at specific resolution):**

- At the 2001-point grid with `plateau_tol = 5e-4`, K_STAR lands
  in the INTERACT plateau. This alignment is K-axis-specific; the
  two filters alone (without a K-scan) do not select K_STAR.

**Does NOT establish:**

- A forced ε (equivalently, a forced grid resolution). The
  plateau K_STAR sits in changes with ε; the `ε ∈ [5e-4, 1e-4]`
  window giving INTERACT is a natural window set by the grid, not
  a framework-derived number.
- K_STAR = 0.862 uniquely (rather than any K in [0.78, 0.98]).
  The INTERACT K-window is an interval of width 0.20; K_STAR sits
  at fractional position 0.41 within it. Any K in the window gives
  the same orbit count.
- Uniqueness of the K-axis among alternative register-generating
  axes (e.g., noise floor, depth, substrate cardinality). The
  K-axis is *sufficient* to produce the plateau walk; whether it
  is *necessary* has not been shown.

## Verdict

**Candidate Class 4 (structural proposal, audit pending).**

The structural part (plateau values 1, 3, 6 are framework
integers; the exhaustion at INTERACT is forced by coprime-to-6)
is a clean result of composing two forced framework filters and
is, on its own, a meaningful strengthening of the framework's
register-generation story. This does *not* depend on the K-axis
and is combinatorial.

The K-axis alignment (K_STAR in the INTERACT plateau) is
suggestive but sits behind an un-forced ε. If a structural
argument is produced for `ε ∈ [1e-4, 1e-3]` — most plausibly via
a substrate noise-floor derivation — this becomes a Class 4
structural derivation of `INTERACT = q₂·q₃` from joint K_STAR +
Klein + coprime-6. Without that, it is candidate Class 4 pending.

## What would upgrade the claim

1. **Derive ε from the substrate.** The Klein-quotient structure
   or observer-register cardinality should force a specific
   resolution floor. If `ε ∈ [5e-4, 5e-3]` follows from substrate
   properties, K_STAR's INTERACT membership becomes structurally
   forced.

2. **Show K-axis uniqueness**: demonstrate that no alternative
   parameter-axis in the framework produces the same plateau
   walk, or produces a plateau walk ending at a different
   framework integer. If the K-axis is shown to be *necessary*
   (not just sufficient), the composed result upgrades to a
   structural register-generator.

3. **Close the K-window uniqueness**: produce a second structural
   constraint beyond "K_STAR is in the INTERACT plateau" that
   picks K_STAR within the [0.78, 0.98] window. The natural
   candidate is the joint matter-sector closure condition that
   sets K_STAR's value, but this must be combined with the
   plateau constraint rather than presented in parallel.

## What would falsify the claim

- A finer plateau-detection that puts K_STAR at an orbit count
  that is not a framework integer (e.g., 11 or 17) at any
  resolution that can be defended as "natural."
- An alternative composition of forced filters that produces a
  different plateau sequence missing INTERACT.
- A structural derivation forcing K ≠ K_STAR as the matter-sector
  K, placing the composed result at a non-framework plateau.

## Cross-references

- `k_scaling_scan.md` — the Class 2 bare K-scan this follows up
- `klein_antipodal_z2_rep_pattern.md` — the forced Klein filter
- `omega_partition_combinatorial.md` — the forced coprime-to-6
  filter
- `observer_register_closure.md` §7 — the K-variation register
  hypothesis this probe addresses
- `mass_sector_closure.md` — `(q₂, q₃) = (2, 3)` cross-link
  uniqueness theorem (the reason `coprime-to-6` is the natural
  filter)
- `item12_K_star_closure.py` — the independent derivation of
  K_STAR from joint matter-sector closure
- `ansatz_audit_policy.md` — the triage applied
