# Why the Exponent Is q₂q₃³

## The question

Derivation 26 showed R = 6 × 13⁵⁴ matches R_observed to 0.48%.
The base (13 = |F₆|) and prefactor (6 = q₂q₃) are derived. The
exponent 54 = 2 × 27 = q₂ × q₃³ is stated but not derived.

This derivation shows: the exponent is q₂ × q₃^d where d = 3 is
the spatial dimension. Each factor has a specific origin. The result
is a consequence of three established facts, not a new assumption.

## The three inputs

1. **The Klein bottle has two directions** (D19):
   - x-direction: antiperiodic (the twist). Carries spatial structure.
   - y-direction: periodic (no twist). Carries temporal evolution.

2. **The x-direction maps to d = 3 spatial dimensions** (D23):
   The Jacobian eigenspace at the Klein bottle fixed point has a
   1 + 3 decomposition: one temporal eigenvalue (3/4) and three
   degenerate spatial eigenvalues (−1/4 each). The 3-fold degeneracy
   IS d = 3 (shown in D23 to equal n² − 1 = F₃ = dim SL(2,ℝ)).

3. **Each direction has a denominator class** (D19):
   - x-direction (spatial): modes at q₃ = 3 (the 1/3, 2/3 fractions)
   - y-direction (temporal): modes at q₂ = 2 (the 1/2 fraction)

## The resolution in each dimension

### Spatial resolution

The x-direction of the Klein bottle maps to d = 3 spatial dimensions.
Each spatial dimension inherits its Farey resolution from the
x-direction's denominator class q₃ = 3.

In one spatial dimension: q₃ = 3 resolution levels.

In d independent spatial dimensions: the total resolution is the
product of the per-dimension resolutions (the dimensions are
independent axes of the Stern-Brocot product tree):

    Resolution_spatial = q₃^d = 3³ = 27

This is the standard mode-counting argument: in a d-dimensional box,
the number of independent resolution levels scales as the resolution
per axis raised to the d-th power. The Klein bottle's spatial
resolution q₃ per axis, raised to d = 3 axes, gives 27.

### Temporal resolution

The y-direction of the Klein bottle maps to 1 temporal dimension.
Its denominator class is q₂ = 2.

    Resolution_temporal = q₂ = 2

The temporal direction does not raise to a power because there is one
temporal dimension, not d of them. Time is the periodic direction —
it ticks. Each tick resolves one binary distinction (q₂ = 2: the
oscillation between the two orientations of the periodic cycle).

### Total resolution exponent

The total resolution across all dimensions is the product of the
spatial and temporal resolutions:

    Exponent = Resolution_temporal × Resolution_spatial
             = q₂ × q₃^d
             = 2 × 27
             = 54

This counts the total number of independent resolution steps the
universe performs across its full (d+1)-dimensional structure:
- 2 temporal steps (one binary tick of the periodic direction)
- 27 spatial steps (3 levels in each of 3 spatial dimensions)
- Product: 54 total

## The assignment is forced

The assignment q₃ → spatial, q₂ → temporal is not a choice. It is
determined by the Klein bottle topology:

- **Spatial = antiperiodic** (D19, "Where time lives"): the
  x-direction carries the twist, which prevents it from being a
  clock (you return orientation-reversed). It carries spatial
  structure — the 1/3 and 1/4 phase divisions.

- **Temporal = periodic**: the y-direction has no twist. You return
  to the same state after one traversal. This is what a clock does.

- **q₃ = 3 is spatial** because the antiperiodic direction's modes
  have denominator 3 (the fractions 1/3 and 2/3). The twist
  selects the odd-denominator modes in this direction.

- **q₂ = 2 is temporal** because the periodic direction's mode has
  denominator 2 (the fraction 1/2). The periodic BC selects the
  simplest nontrivial mode.

The larger denominator (q₃ = 3) is spatial because the spatial
direction has the richer structure (the twist forces nontrivial
modes). The smaller denominator (q₂ = 2) is temporal because the
temporal direction has the simpler structure (periodic, no twist).

Reversing the assignment (q₂ → spatial, q₃ → temporal) would give
exponent q₃ × q₂^d = 3 × 8 = 24, and R = 6 × 13²⁴ ≈ 10²⁷·⁶.
This is 33 orders of magnitude too small. Only the correct assignment
produces the observed hierarchy.

## The complete formula

Assembling:

    R = (q₂q₃) × |F_{q₂q₃}|^{q₂ × q₃^d}

    = (2 × 3) × |F_6|^{2 × 3³}

    = 6 × 13⁵⁴

Each component:

| Symbol | Value | Source | Role |
|--------|-------|--------|------|
| q₂ | 2 | Klein bottle (D19) | Temporal denominator class |
| q₃ | 3 | Klein bottle (D19) | Spatial denominator class |
| d | 3 | D14 / D23 (= q₃ = n²−1) | Spatial dimensions |
| q₂q₃ | 6 | Product | Interaction scale (prefactor) |
| \|F₆\| | 13 | Farey count (D25) | States per resolution step |
| q₂q₃^d | 54 | This derivation | Total resolution exponent |

Note that d = q₃ = 3: the spatial dimension equals the spatial
denominator class. This is the dimension loop (D23): the Klein
bottle selects q₃ = 3, which is dim SL(2,ℝ) = n²−1, which is the
spatial dimension d. The exponent q₂q₃^d = q₂q₃^{q₃} = 2 × 3³
is self-referential: q₃ appears both as the base and the exponent
of the spatial factor.

## The self-referential structure

The exponent q₂ × q₃^d involves d = q₃. So:

    Exponent = q₂ × q₃^{q₃}

This is q₃ raised to its own power (the tetration floor). The
hierarchy is ultimately set by the self-referential evaluation of
the spatial denominator: how many resolution steps are needed when
the number of dimensions equals the resolution per dimension.

    3³ = 27 means: 3 dimensions, each with 3 resolution levels.
    The resolution IS the dimension IS the denominator class.

If d were 2 (and q₃ = 2): 2² = 4. If d were 5 (and q₃ = 5):
5⁵ = 3125. The specific value d = q₃ = 3 gives 3³ = 27, which
multiplied by q₂ = 2 gives 54, which as an exponent of 13 gives
the observed hierarchy.

The self-reference is the content: a universe whose spatial dimension
equals its spatial resolution class produces a hierarchy of exactly
this size. No other value of d is self-consistent (D14 derives d = 3
independently), so no other hierarchy is possible.

## Status

**Derived**: the exponent q₂q₃^d = 54 follows from three established
results:
1. The Klein bottle assigns q₃ to spatial, q₂ to temporal (D19)
2. The spatial direction maps to d = 3 independent dimensions (D23)
3. Independent dimensions multiply their resolutions (standard
   mode counting)

The assignment is forced by the topology (antiperiodic = spatial,
periodic = temporal). The dimensionality d = 3 = q₃ is the dimension
loop closing again. The self-referential structure q₃^{q₃} is the
origin of the specific numerical value.

**Complete**: with this derivation, the full chain from the Klein
bottle to the cosmological parameters is closed:

    Klein bottle topology
    → denominator classes {2, 3}
    → Farey count |F₆| = 13
    → Ω_Λ = 13/19                    (D25, 0.07σ)
    → R = 6 × 13⁵⁴                  (D26, 0.48%)
    → Λl_P² = 13⁻¹⁰⁸/12            (D26, 0.1%)
    → exponent = q₂ × q₃^d = 54     (D27, derived)

Three inputs: q₂ = 2, q₃ = 3, |F₆| = 13.
Three outputs: Ω_Λ, R, Λ.
Zero free parameters.
