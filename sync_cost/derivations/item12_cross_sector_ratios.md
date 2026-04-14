# Item 12: cross-sector `a_1²` ratios

## Claim

The three per-sector continuous exponents `a_1(leptons)`,
`a_1(up)`, `a_1(down)` in the generation exponent law satisfy

    a_1(leptons)² : a_1(up)² : a_1(down)²
          1       :   9/4    :    6
          1       : (q_3/q_2)² : q_2 q_3

at PDG 2024 1-σ precision. This reduces the mass sector's
fitted-parameter count from **three** (one `a_1` per sector)
to **one** (`C = a_1(leptons)² ≈ 5.3838`).

## Setup

The generation exponent law is

    m_{g+1}/m_g = b_step^(d a_step)

with `d = 3` and step base `b_step` a sector-specific rational.
In each sector the structural ratio is `a_2/a_1 = q_3/q_2 = 3/2`
(from the backbone derivation). Solving for `a_1` from PDG masses
gives one fitted exponent per sector; the framework's previous
state held three such fits.

The sectors and their base pairs:

| sector | `b_1` | `b_2` | heavy-to-middle ratio | middle-to-light ratio |
|---|---|---|---|---|
| leptons   | 3/2 | 5/3 | `m_τ/m_μ` | `m_μ/m_e` |
| up-type   | 8/5 | 3/2 | `m_t/m_c` | `m_c/m_u` |
| down-type | 5/4 | 9/8 | `m_b/m_s` | `m_s/m_d` |

Extracted `a_1` per sector (PDG 2024, 1-σ propagated):

    a_1(leptons)   = 2.320292 ± 0.000056     (~1e-5 relative)
    a_1(up-type)   = 3.484290 ± 0.011289     (0.32%)
    a_1(down-type) = 5.678221 ± 0.128398     (2.26%)

The quark `a_1` uncertainties are dominated by `m_c` (1.6%) and
`m_s` (9%) respectively; the lepton `a_1` has negligible error.

## Observed ratios

Squared cross-sector ratios:

    a_1(up)² / a_1(lep)² = 2.255 ± 0.015      target 9/4   = 2.250    (0.34σ)
    a_1(dn)² / a_1(lep)² = 5.989 ± 0.271      target 6     = 6.000    (0.04σ)

Both are consistent with exact equality at 1-σ PDG precision,
and in the down-type case well inside 1-σ.

## Structural reading for the 9/4 factor

The up-type base pair `(8/5, 3/2)` is the **Fibonacci shift** of
the lepton pair `(3/2, 5/3)`:

    leptons : (F_4/F_3, F_5/F_4) = (3/2, 5/3)
    up-type : (F_6/F_5, F_4/F_3) = (8/5, 3/2)

Up-type's `b_2` equals leptons' `b_1`. The cross-sector identity

    a_1(up) = (3/2) a_1(leptons)      equivalently    a_1(up) = a_2(leptons)

squared gives

    a_1(up)² / a_1(leptons)² = (q_3/q_2)² = 9/4.

**Evidence**: the numerical identity holds at 0.34 σ using
PDG 2024 quark masses.

**What this is, and isn't**: the identity says that promoting
the lepton sector's "second-step" exponent to an up-type
"first-step" exponent reproduces the up-type data — i.e. one
generation step in the lepton ladder equals one sector shift
from leptons to up-type. This is a non-trivial cross-sector
alignment, and it is consistent with exact equality at PDG
precision. What it is *not* is a derivation of the ratio from
a separate first-principled argument: the ratio is `3/2`
because both the intra-sector generation spacing and the
cross-sector Fibonacci shift pick out the same value
`q_3/q_2 = 3/2`. The coincidence may be a single structural
fact about the backbone (a single Fibonacci step is both an
intra-sector generation step and a lepton-to-up-type sector
shift), or it may be two facts that happen to take the same
numerical value. At current precision the data cannot
distinguish these.

## Structural reading for the 6 factor

The down-type base pair `(5/4, 9/8)` has a distinct topological
property: **both denominators are even**. From
`item12_down_sign_flip.py`, the Klein-bottle parity of a base
pair is

    parity = (-1)^(number of odd denominators)

giving

| sector | base denoms | # even | parity | walk type |
|---|---|---|---|---|
| leptons   | (2, 3) | 1 | -1 | orientation-reversing (single sheet) |
| up-type   | (5, 2) | 1 | -1 | orientation-reversing (single sheet) |
| down-type | (4, 8) | 2 | +1 | **orientation-preserving** (double cover) |

Down-type is the one sector whose walks do not pass through the
Klein bottle's antiperiodic direction an odd number of times,
and therefore can be lifted to the **orientable double cover**:
the 2-torus `T² = S¹ × S¹` with the two circles carrying the
`Z_2` (weak isospin) and `Z_3` (color) twist counts of the
underlying Klein bottle.

**Conjecture.** For an orientation-preserving walk, the
effective "mode volume" scales as the product of the two torus
cycle lengths — `q_2 × q_3 = 6` — whereas for an
orientation-reversing walk it scales as the squared Fibonacci
shift ratio `(q_3/q_2)^(2k)` at shift index `k`.

Then:

    leptons   (k = 0 reversing):    a_1²/C = 1
    up-type   (k = 1 reversing):    a_1²/C = (q_3/q_2)² = 9/4
    down-type (double cover):       a_1²/C = q_2 q_3    = 6

**Evidence**: the down-type ratio `a_1(dn)²/a_1(lep)² = 5.989 ± 0.271`
is consistent with exactly `6` at 0.04 σ.

**Status**: this reading is **a conjecture**, not a derivation.
The step "orientation-preserving walk on the Klein bottle
double cover has mode volume `q_2 q_3`" needs a formal argument
from the rational field equation — e.g. a path-integral
computation that shows the normalization of the orientable-lift
walk picks up a factor `q_2 q_3` relative to the base-sheet walk.
The numerical agreement is consistent with the conjecture but
does not prove it. What rules out purely numerical coincidence
is the correlation with the **separately-derived sign flip** of
the down-type residual (`item12_down_sign_flip.py`), which
already uses the same Klein-bottle parity: the sector whose
walk is orientation-preserving is the same sector whose `a_1²`
ratio needs the distinct scaling, and the same Klein parity
assignment explains both.

The joint success of the sign-flip and the magnitude-factor
readings under the **same** parity assignment is what makes
the reading more than a post-hoc fit.

## The remaining constant `C`

    C = a_1(leptons)² = 5.38375376 ± 0.00025765

No clean closed form has been found. Near misses from a
structural scan:

    3 ln(q_2 q_3)           5.3753    0.16%       (33 σ away from C)
    π √3                    5.4414    1.1%
    φ³ + 1                  5.2361    2.7%
    k_lepton/φ²             3.4377    36%

(`3 ln(6)` and `q_3 ln(q_2 q_3)` are algebraically identical at
`q_2 = 2, q_3 = 3`, and count as one near-miss.)

The best near miss `3 ln(q_2 q_3)` is at 0.16% but is still
33 σ away from `C` at lepton PDG precision — lepton masses are
too accurate for this to be consistent with exact equality.

**Proposal**: `C` is the single remaining mass-sector parameter.
It is most plausibly a fixed-point output of the rational field
equation at the lepton sector's Fibonacci convergent — i.e. a
Feigenbaum-style limit computable by iteration of the self-
consistency map, but without a closed form in elementary
functions. Confirming this requires executing the iteration
(this has been flagged in `open_items.md` for a while and has
not been done).

## What this pass closes and does not close

**Closes**:
- The mass sector fit count is reduced from **three** per-sector
  `a_1` values to **one** constant `C`.
- The `9/4` up-type factor is consistent with the Fibonacci shift
  of the base pair at PDG 1 σ.
- The `6` down-type factor is consistent with the Klein-bottle
  double-cover conjecture at PDG 1 σ, in joint agreement with
  the separately-derived parity sign flip.

**Does not close**:
- The intra-lepton ratio `a_2(lep)/a_1(lep) = 1.4994` is 16 σ
  away from exact `3/2` at lepton PDG precision. This is a
  known finite-K residual (`item12_residual_test.py`) and is
  not touched here.
- `C` has no closed form yet.
- The "orientation-preserving walk has mode volume `q_2 q_3`"
  conjecture needs a first-principled derivation from the
  rational field equation.

## Cross-references

- `item12_characterize_a1.py` — the original numerical observation
  of the `1 : 9/4 : 6` pattern.
- `item12_cross_sector_derivation.py` — computational verification
  of the identities at PDG precision with full error propagation.
- `item12_down_sign_flip.py` — the Klein-bottle parity assignment
  used in the `6` factor reading.
- `item12_residual_test.py` — the lepton `C` residual (~1e-4),
  the finite-K correction responsible for the intra-lepton
  16 σ deviation from exact `3/2`.
- `open_items.md` item 12 — the mass-sector status tracker.
