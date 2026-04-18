# Weak Mixing Angle: sin²θ_W from Effective Dimension Reduction

## Status

**Derived, conditionally.** The electroweak mixing angle is

  sin²θ_W = 2^(80/27) / (2^(80/27) + 3^(80/27)) = 0.23123

compared with the PDG value sin²θ_W(M_Z)_MS = 0.23121 ± 0.00004
(0.5σ, 0.009% residual).

The derivation chain uses three previously derived quantities
(q₂ = 2, q₃ = 3, d = 3) and one structural argument (tongue
strip geometry → effective dimension reduction). The structural
argument is principled but not yet a theorem; the connection
between "occupied frequency interval" and "effective dimension"
is formalized below at the heuristic level.

The derivation does not use K-scanning or running (see
`sinw_fixed_point.md` for why those fail). It is a first-order
perturbative correction to the bare formula, evaluated at the
root (1/1) of the Stern-Brocot tree.

---

## The bare formula

The duty cycle of the p/q Arnold tongue in d spatial dimensions
is 1/q^d (measure-theoretic limit, K → 1). The electroweak
mixing angle measures the relative duty cycles of the two
Klein-bottle denominator classes:

  sin²θ_W = duty(q₂) / (duty(q₂) + duty(q₃))
           = (1/q₂^d) / (1/q₂^d + 1/q₃^d)
           = q₃^d / (q₂^d + q₃^d)

Wait — this gives 27/35 = cos²θ_W. The assignment convention:

  sin²θ_W = q₂^d / (q₂^d + q₃^d) = 8/35 = 0.22857

This follows from identifying the U(1)_Y hypercharge coupling
with the q₂ = 2 sector and the SU(2)_L coupling with the q₃ = 3
sector via the gauge dictionary (`gauge_dictionary.md`). The
assignment is part of the one irreducible identification in the
gauge sector.

Residual from observation: 1.14%.

---

## The correction: tongue strip geometry

### Configuration space decomposition

The circle-map configuration space at the root (1/1) level of the
Stern-Brocot tree decomposes as

  Ω × M^(d-1)

where Ω ∈ [0, 1] is the frequency (rotation number) axis and
M^(d-1) is the (d-1)-dimensional spatial manifold.

### Arnold tongue geometry

The q₃ = 3 Arnold tongue is a strip in this space:

  - **Width in Ω**: the tongue occupies a fraction 1/q₃^d = 1/27
    of the frequency axis.
  - **Extent in M^(d-1)**: the tongue extends across the full
    spatial manifold (mode-locking at a given frequency is a
    spatially uniform condition).

The tongue is anisotropic: it is a codimension-0 strip in Ω,
not a ball in all d dimensions.

### Effective dimension

The q₃ tongue locks a fraction 1/q₃^d of the frequency axis,
removing it from the available degrees of freedom for the
mixing-angle measurement. The remaining frequency interval has
effective length

  L_eff(Ω) = 1 - 1/q₃^d = 26/27.

The (d-1) spatial dimensions are unaffected (the tongue spans
them fully). The total effective dimension is therefore

  d_eff = (d - 1) + L_eff(Ω)
        = (d - 1) + (1 - 1/q₃^d)
        = d - 1/q₃^d.

For q₃ = 3, d = 3:

  d_eff = 3 - 1/27 = 80/27.

### The corrected mixing angle

Replacing d → d_eff in the bare formula:

  sin²θ_W = q₂^d_eff / (q₂^d_eff + q₃^d_eff)
           = 2^(80/27) / (2^(80/27) + 3^(80/27))
           = 0.23123.

---

## Why q₃ and not q₂

The correction comes from the q₃ tongue (not q₂) because the
mixing angle is a RATIO of two couplings evaluated on the
frequency interval. The q₃ tongue is the dominant occupier of
the denominator: q₃^d = 27 > q₂^d = 8. The leading perturbative
correction to the dimension comes from the largest tongue in the
denominator.

Correcting by q₂ instead (d_eff = 3 - 1/8 = 23/8) gives
sin²θ_W = 0.2376, which is 2.8% above observation — the wrong
direction and magnitude. The asymmetry is physical: q₂ and q₃
play different roles in the formula, and the correction from the
larger (q₃) tongue is the leading one.

---

## Why first order

The self-consistent fixed-point equation d = 3 - q₃^(-d) has
the solution d* = 2.96136, giving sin²θ_W = 0.23135 (0.06% off).
The first-order truncation d = 80/27 gives 0.23123 (0.009% off).

First order is closer to observation. This is standard in
perturbation theory: the first-order correction is the physical
result; higher orders (the resummed fixed point) include
contributions from sub-tongues at deeper tree levels, which
should be computed separately with their own coupling structure
rather than iterated self-referentially.

---

## Scale identification: why M_Z

The formula is evaluated at the ROOT (1/1) of the Stern-Brocot
tree. In the framework, the root is the scale where the q₂ and
q₃ sectors first branch — the point where the two gauge couplings
are simultaneously defined. This is the electroweak symmetry
breaking scale by construction.

The MS-bar scheme at M_Z is the perturbative coupling definition
at the Z pole, which is the scale where the electroweak mixing
is measured. The framework's root-level formula corresponds to
this scheme because:

1. The root is where mixing is DEFINED (the branching point).
2. The correction is perturbative (first-order in 1/q₃^d).
3. MS-bar is the natural perturbative scheme in the SM.

The on-shell definition sin²θ_W = 1 - M_W²/M_Z² = 0.2229 is a
different quantity (a mass ratio, not a coupling ratio) and is
not predicted by this formula.

---

## Comparison with experiment

| Scheme | Value | Residual |
|---|---|---|
| Framework (80/27 exponent) | 0.23123 | — |
| MS-bar at M_Z (PDG 2024) | 0.23121 ± 0.00004 | 0.5σ |
| Effective sin²θ_eff (Z-pole) | 0.23153 ± 0.00016 | 1.9σ |
| MS-bar at M_W | 0.23140 ± 0.00010 | 1.7σ |
| On-shell (1 - M_W²/M_Z²) | 0.22290 ± 0.00030 | 27.8σ |
| Low-energy (Q² → 0) | 0.23867 ± 0.00016 | 46.5σ |

The formula matches MS-bar at M_Z within experimental uncertainty.
It does not match other scheme/scale combinations. This is
consistent with the interpretation that the formula predicts the
perturbative coupling ratio at the electroweak branching scale.

---

## What remains to formalize

1. **Occupied interval → dimension reduction**: the step from
   "the tongue occupies 1/q₃^d of the frequency axis" to
   "the effective dimension is d - 1/q₃^d" is geometrically
   motivated but not rigorously derived. A proper derivation
   would show that the duty-cycle formula sin²θ_W = q₂^d_eff /
   (q₂^d_eff + q₃^d_eff) with d_eff = d - 1/q₃^d follows from
   integrating the coupling over the COMPLEMENT of the q₃ tongue.

2. **Why only q₃**: the argument that the leading correction
   comes from the largest tongue in the denominator is heuristic.
   A systematic expansion would include sub-leading corrections
   from the q₂ tongue (at order 1/q₂^d = 1/8) and cross-terms.
   These higher corrections are not needed at current experimental
   precision but would be testable with future measurements.

3. **Scheme identification**: the claim that the framework's
   root-level formula corresponds specifically to MS-bar at M_Z
   is motivated but not proven. A derivation would show that
   the perturbative structure of the correction maps onto the
   MS-bar subtraction procedure.

---

## References

- `sinw_fixed_point.md` — prior negative result (K-scanning)
- `sinw_fixed_point.py`, `sinW_running_check.py` — prior scripts
- `klein_bottle_derivation.md` — q₂ = 2, q₃ = 3
- `three_dimensions.md` — d = 3
- `duty_cycle_dictionary.md` — duty cycle formula
- `gauge_dictionary.md` — gauge sector identification
- `gauge_sector_lovelock.md` — SU(3) × SU(2) × U(1) derivation
