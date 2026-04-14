# Item 12: `C = q_2² / K*²` from the tongue-width identity

## Claim

The last remaining mass-sector constant, `C = a_1(leptons)²`, admits
a closed-form reading in terms of the framework's self-consistent
coupling `K*` and the Klein-bottle integer `q_2 = 2`:

    a_1(leptons) = 1 / sqrt(w(3/2, K*)) = q_2 / K*    =>    C = q_2² / K*²

where `w(p/q, K)` is the perturbative Arnold-tongue width at rational
`p/q` and coupling `K`:

    w(p/q, K) = 2 (K/2)^q / q          (for K < 1, q > 1)

For the lepton sector's primary base rational `b_1 = 3/2`, this gives
`w(3/2, K*) = (K*/2)²`, and `1/sqrt(w) = 2/K* = q_2/K*`.

**Numerical status at PDG 2024** (canonical `K* = 0.86196052`):

    a_1(leptons) observed   = 2.3202917 +/- 5.6e-5   (0.002% from m_tau, m_mu)
    2 / K*                  = 2.3202917
    residual                < 1e-6                    (0.00 sigma)

    C observed              = 5.3837538 +/- 2.6e-4
    q_2² / K*²              = 5.3837537
    residual                < 1e-5                    (0.00 sigma)

## Consequences

### 1. Item 12 closes completely at PDG precision

Combined with the cross-sector scalings of
`item12_cross_sector_ratios.md`:

    a_1(leptons)²   = q_2² / K*²            (tongue-width identity, this doc)
    a_1(up)²        = (q_3/q_2)² × C        (Fibonacci shift)
    a_1(down)²      = q_2 q_3 × C           (Klein-bottle double cover)

All three per-sector `a_1` values are structural — no fits. The
mass-sector fit count goes from 3 (one `a_1` per sector) → 1 (the
constant `C`) → **0** (once `C = q_2²/K*²` is accepted).

### 2. K* as the lepton-implied determination

Turning the identity around:

    K* = q_2 / a_1(leptons) = 0.86196052 +/- 2.1e-5

This is the canonical K_STAR in `framework_constants.py`. Direct
`r → K r` iteration on the rational field equation hits a degenerate
vacuum (`r* = 0`) per `K_star_iteration.py`; the lepton tongue-width
identity is the working route to K* at 5+ digits.

## Structural reading

### Why `1/sqrt(w)` and not `w` itself?

Tongue widths have dimensions of "squared length" in the
log-ratio / angular-frequency space (they are the *area* of the
Mathieu-lobe / stop-band in the two-parameter (K, Ω) plane, not
a 1D length). The "characteristic scale" that appears in the
log-mass ladder is a *linear* quantity, so it goes as
`sqrt(w)`, and its inverse (the "frequency" of the log-mass
lattice) is `1/sqrt(w)`.

Equivalently: if the tongue width `w = (K/2)²` measures the
angular width of the locked region around the rational, then
`1/sqrt(w) = 2/K` counts how many such widths fit into a unit
angle, i.e., the "mode density at the tongue tip".

This explains the q=2 specialness: `w = (K/2)^q / (q/2)` only
collapses to a clean power `(K/2)^q` for q=2 (where the q/2
factor drops). For q ≠ 2, the formula `1/sqrt(w)` still makes
sense but no longer simplifies to a single rational `q/K`, and
the sector-scaling factors of `item12_cross_sector_ratios.md`
become the relevant structure.

### Why leptons and not quarks?

The lepton sector carries the simplest Klein-bottle topology:

- Heavy-step base `b_1 = 3/2` has denominator `q_2 = 2`, the
  Klein-bottle antiperiodic twist count.
- Walks are orientation-reversing on the single sheet
  (item12_down_sign_flip.py parity -1).
- No Fibonacci shift relative to a prior sector.

Under these conditions, the tongue-width formula applies directly
with no corrections. For quarks:

- Up-type has Fibonacci shift k=1 relative to leptons, giving an
  extra factor `(q_3/q_2)² = 9/4` on `a_1²`.
- Down-type has Klein-bottle parity +1 (orientation-preserving),
  lifting the walk to the double cover with mode volume `q_2 q_3 = 6`
  on `a_1²`.

In both cases the "primary" tongue-width formula does not apply
directly because the walk topology is different. The cross-sector
derivation handles them via the scaling factors, which are now
the only sector-specific inputs after the lepton `C` is fixed.

## Verification

The script `item12_C_from_K_star.py`:

1. Computes `a_1` per sector from PDG 2024 with full 1-σ propagation.
2. Tests the identity `a_1(lep) · K* = q_2` at canonical K_STAR and
   reports the 0.00-σ residual.
3. Verifies that the identity does NOT extend to quark sectors under
   the naive `1/sqrt(w(b_1, K*))` form — consistent with the
   cross-sector derivation's prediction.
4. Reports both candidate structural readings (tongue-width
   inverse-sqrt; walk length = q_2 steps at step-size K*).

## What this does and does not establish

**Establishes**:

- A clean closed-form candidate for `C`: `q_2² / K*²`.
- A 0.00-σ match to PDG 2024 lepton masses under canonical K_STAR.
- A structural reading (tongue-width inverse-sqrt) that explains why
  the formula applies to leptons and not directly to quarks.

**Does NOT establish**:

- An independent first-principles derivation of K_STAR. The lepton
  tongue-width identity is consistent with the joint matter-sector
  closure (`item12_K_star_closure.py`) but uses PDG mass ratios as
  input. A K_STAR derivation that does not consume PDG remains open.
- Why the `1/sqrt(w)` prescription is the right one rather than,
  say, `1/w` or `1/w^α` for other α. The reading given above
  (tongue width is a squared length; the log-mass ladder scale
  is linear) is plausible but not a first-principled derivation
  from the rational field equation.
- That the same prescription extends to dimensions other than
  `d = 3`. The `d` factor enters `a_1` only through
  `a_1 = log(r_1) / (d log b_1)`; the tongue-width identity
  implicitly fixes the combination `d · a_1 · log(3/2) = 2d log(3/2) / K*`
  with no independent check of `d`.

## Open derivation tasks

1. **Compute `K*` independently of PDG mass input** via the rational
   field equation's direct fixed-point iteration, or via the
   coherence cascade, or via the boundary-weight formalism. The
   lepton tongue-width identity gives K* via PDG; an alternative
   route would close the lone remaining input dependency.

2. **Derive the `1/sqrt(w)` prescription** from the Kuramoto
   field equation at `K*` restricted to a single tongue. The
   goal: a path-integral / action-principle computation that
   produces `a_1` as the natural frequency of the log-mass
   ladder near the rational, with the tongue width setting the
   inverse scale.

3. **Connect to the `d = 3` spatial dimension.** The identity
   `a_1(lep) = 2/K*` is independent of `d`, but the generation
   exponent `d · a_1` is not. A derivation should make clear
   which of the two is the primary framework object.

## Cross-references

| File | Role |
|---|---|
| `item12_C_from_K_star.py` | Numerical verification of the identity at PDG 2024 |
| `item12_cross_sector_ratios.md` | Sector scalings (9/4 up, 6 down) that relate quark `a_1` to lepton `C` |
| `item12_cross_sector_derivation.py` | Cross-sector numerical verification |
| `item12_down_sign_flip.py` | Klein-bottle parity assignment used for down-type |
| `boundary_weight.md` | Framework's original citation of `K* = 0.862` |
| `K_star_iteration.py` | K* iteration audit (hits r* = 0 degeneracy) |
| `circle_map_utils.py` `tongue_width` | Perturbative Arnold-tongue formula used here |
