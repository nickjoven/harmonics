# Readings, Not Constants

## The reframing

Quantities like a₁ = 2.3203 (the lepton generation exponent) are not
universal constants. They are **readings** — projections of the field
equation's fixed point onto a specific topological coordinate system.

A reading is half topology (the coordinate system) and half data (the
quantity being measured). Asking for a closed form for a reading is a
category error: you cannot reduce experimental data to elementary
functions.

The framework's genuine constants are:
- **Rational seeds**: {2, 3, 13, 19} from topology (the addresses)
- **Forced irrationals**: {φ, π, ln(3/2), C} from conversion between
  discrete and continuous structure

The framework's genuine outputs are:
- **Fixed-point values**: {w*, Ω_Λ, a₁} computed by iterating the
  rational field equation. These are projections of ONE fixed point
  onto different observables.

## Single dynamics, multiple regimes

The Klein bottle field equation has one fixed point. Leptons and
quarks are not different solutions — they are different **readings**
of the same fixed point through different gauge coordinate systems.

### The lepton reading

Leptons couple only through SU(2) × U(1). The tree coordinate
(3/2)³ and (5/3)³ for the generation step bases matches the physical
coupling directly. The lepton reading is clean:

    m_τ/m_μ = 16.805 (predicted: 16.817, obs: 16.817, 0.07%)
    m_μ/m_e = 206.92  (predicted: 206.92, obs: 206.77, 0.07%)

### The quark reading

Quarks couple through SU(3) × SU(2) × U(1). The SU(3) coupling
modifies the effective tree structure — the tongue widths are
not just (K/2)^q but are renormalized by the color charge.

The quark reading is NOT "the lepton reading plus QCD running
corrections." It is a **different coordinate system** that
incorporates the color coupling from the start.

When we naively apply the lepton reading to quarks:

    a₂/a₁ (up-type)  = 1.030 (vs 3/2)
    a₂/a₁ (down-type) = 0.626 (vs 3/2)

The large deviations are not "errors to correct" — they signal
that we are using the wrong coordinate system. The right quark
coordinate system would give a₂/a₁ = 3/2 at tree scale with
QCD running built into the coordinate itself.

## The fix (conjectured)

For quarks, the tree coordinate should be:

    base_quark(q, q') = (q'/q)^d_eff

where d_eff is not the spatial dimension (d = 3) but an effective
dimension that includes color. For a charge-2/3 quark coupling to
3 colors, d_eff might be 3 + 2/3 × something. For charge-1/3,
d_eff would differ by the charge ratio.

This is testable: if d_eff can be computed from the charge and
the number of colors, the quark readings should become compatible
with the lepton reading at the tree level.

## Why this is the right framing

Closed forms are searches for reductions. Readings are searches
for compatible coordinates.

If a₁ had a closed form, we would say: "here is a simpler
expression that explains the value." But a₁ depends on the
observed lepton masses — reducing it would be reducing experimental
data to elementary functions, which is not what closed forms do.

If different sector readings are compatible (same fixed point,
different coordinates), we would say: "the same dynamics produce
multiple observables, and the relationships between them are
fixed by the coordinate transformations." This is what the
framework actually claims.

The dissatisfaction with non-closed forms was tracking a real
problem: we were asking for the wrong kind of answer. The right
question is not "what closed form gives a₁?" but "does the same
fixed point produce a₁, w*, Ω_Λ, AND the quark masses through
different readings?"

## Status

**Conjectured.** The reading framework is clearer than the constant
framework but needs concrete demonstration. The lepton generation
exponent law works. The quark extension (with effective dimension
d_eff determined by color coupling) is the next computation.

If d_eff can be derived from the framework's principles, the mass
sector closes: one fixed point, multiple readings, one law per
reading, all consistent.
