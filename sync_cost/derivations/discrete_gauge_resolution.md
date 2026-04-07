# The Discrete Gauge Resolution

## The question, resolved

Derivation 20 asked: what does the K=1 continuum limit produce on the
XOR-filtered Stern-Brocot tree? The answer was an honest negative.
The frame bundle of the continuum Klein bottle gives Pin+(3) = SU(2) x Z_2,
but not SU(3) and not Yang-Mills. The XOR filter — the mechanism that
selects denominator classes {2, 3} — dissolves when the tree is taken
to the reals.

Derivation 21 proposed five binary computations to test both open paths.
All five are now complete. This derivation records the verdict.

## The five results

### A. Anomaly cancellation (Path 1): PASS

The Klein bottle fractions {1/3, 1/2, 2/3}, combined with doublet
structure (T_3 = +/- 1/2) and the Gell-Mann-Nishijima relation
(Q = T_3 + Y/2), uniquely determine all Standard Model hypercharges
with zero free parameters:

| Field | SU(3) | SU(2) | Y    | Q         |
|-------|-------|-------|------|-----------|
| Q_L   | 3     | 2     | 1/3  | 2/3, -1/3 |
| u_R   | 3     | 1     | 4/3  | 2/3       |
| d_R   | 3     | 1     | -2/3 | -1/3      |
| L_L   | 1     | 2     | -1   | 0, -1     |
| e_R   | 1     | 1     | -2   | -1        |

All six anomaly cancellation conditions are satisfied exactly:
[SU(3)]^2 U(1)_Y, [SU(2)]^2 U(1)_Y, [U(1)_Y]^3, [grav]^2 U(1)_Y,
Witten SU(2), [SU(3)]^3.

Anomaly cancellation is a prediction, not an input. The topology
determines the charges; the charges cancel the anomalies.

**Script**: `anomaly_check.py`

### B. Tongue overlap vs structure constants (Path 1): FAIL

The XOR filter is too restrictive for non-abelian self-coupling.
The q=3 modes (1/3, 2/3) interact through q=2 (their mediant is 1/2),
but self-mediations are forbidden by the XOR parity constraint.
The q=2 mode acts as an abelian mediator. The vertex structure is
U(1)-like, not SU(3) x SU(2) x U(1).

The tongue overlap test does not reproduce non-abelian structure
constants. The Arnold tongues encode the coupling between modes,
but the XOR constraint prevents the triple-gluon vertex.

**Script**: `tongue_overlap_structure.py`

### C. Depth sweep vs beta functions (Path 1): FAIL / STRUCTURAL

The population ratio N(q=3)/N(q=2) does not track the Standard Model
beta function ratio b_3/b_2 = 42/19 at any tree depth.

However, the within-sector ratio N(1/3)/N(2/3) converges to exactly
2/3 at all depths (4 through 8), with deviation < 10^-2. This 2/3 is
the mediant of 1/3 and 2/3 — the denominator of the interaction
mediator. The asymmetry is structural, not running.

The discrete RG (tree depth as energy scale) does not reproduce
one-loop running in any simple way. But the structural ratios are
depth-invariant, which is a stronger statement: the Klein bottle's
mode hierarchy is topological, not dynamical.

**Scripts**: `depth_sweep.py`, `depth_sweep_v2.py`

### D. Jacobian at fixed point (Path 2): RANK-1 / BLOCK STRUCTURE

The 4x4 Jacobian of the Klein bottle field equation at the
self-consistent fixed point (r = 0 with twist) is rank-1 degenerate.
This is consistent with Derivation 17 (rank-1 temporal causation):
the linearized dynamics has a single active direction.

At the observed r ~ 0.5-0.6, the Jacobian becomes full-rank with
2x2 block structure coupling denominator classes A = {2} and B = {3}.
The traceless part shows mixed symmetric/antisymmetric structure,
but the algebra dimension is 3-4, consistent with sl(2,R) — the
substrate group from Derivation 15 — not su(2) + su(3) = 11.

The field equation's linearization does not contain the full gauge
algebra. The Jacobian encodes the substrate geometry (sl(2,R)), not
the gauge symmetry.

**Scripts**: `jacobian_fixed_point.py`, `jacobian_v2.py`

### E. Z_2 algebra generation (Path 2): Z_6 CENTER

The GCD of mediant outcomes on the Klein bottle produces a
Z_2 x Z_3 = Z_6 structure. The mediant does not commute with
scaling (k -> 2k), and this non-commutativity has specific
residue structure:

- GCD mod 2 gives Z_2 from q_2 = 2
- GCD mod 3 gives Z_3 from q_3 = 3
- The full structure Z_6 = center(SU(2) x SU(3))

The fiber bundle has gauge-theory-like properties: the GCD acts as
a gauge transformation, reducing multiple representatives to a single
physical mode. But the fiber is locked by the XOR constraint: scaling
by k=2 kills the twist sign ((-1)^{2q} = +1 always), while scaling
by k=3 preserves it ((-1)^{3q} = (-1)^q). The Z_2 action does not
generate a larger algebra through the self-consistency loop — the
Jacobian's rank-1 structure at the fixed point prevents algebraic
enhancement.

The nonlinear loop N -> K_eff -> w -> N is too constrained (rank-1
bottleneck) to amplify Z_2 into a non-abelian group.

**Scripts**: `z6_algebra.py`, `z6_algebra_v2.py`, `z6_algebra_v3.py`,
`fiber_bundle.py`

## The supporting result: confinement from XOR asymmetry

Independent of the five D21 tests, the XOR parity constraint produces
a confinement/deconfinement asymmetry between denominator classes:

**q = 2 (weak sector): OPEN.** Scaling by k=2 preserves XOR parity.
The fiber mode at (2/4, 1/3) is allowed. At K=1 the fiber mode is
25% of the base. The weak force does not confine because its fiber
modes are XOR-allowed.

**q = 3 (strong sector): LOCKED.** Scaling by k=2 breaks XOR parity.
The fiber mode at (2/6, 1/3) is forbidden at all K <= 1. Deconfinement
would require K = 2^{4/3} ~ 2.52. The strong force confines because
its fiber modes are XOR-forbidden.

The confinement asymmetry ratio is:

    (q=3 forbidden) / (q=2 allowed) = K/2

At K=1: ratio = 1/2. This 1/2 IS the mediant of 1/3 and 2/3 — the
mediator mode. The confinement asymmetry is encoded in the mediator
itself.

**Script**: `xor_asymmetry.py`

## The verdict

### Path 1 (discrete is physical): PARTIALLY CONFIRMED

The anomaly cancellation passes exactly. The structural ratios
(within-sector 2/3) are topological. The confinement asymmetry
between q=2 and q=3 is real and has the right sign.

But the tongue overlap does not reproduce non-abelian structure
constants, and the depth sweep does not reproduce beta functions.
The discrete tree contains the correct charges and center, but
not the full gauge dynamics.

### Path 2 (gauge from mean-field F): CLOSED

The Jacobian at the fixed point has rank 1, not 11. The Z_2 fiber
action does not generate a larger algebra. The self-consistency
functional F is too simple — it has one scalar bottleneck (the
order parameter r) and cannot carry the degrees of freedom needed
for non-abelian gauge theory.

### What the Klein bottle actually produces

Assembling all positive results:

1. **The correct charges.** The Klein bottle fractions are the
   Standard Model electric charges and hypercharges. Anomaly
   cancellation is automatic. (D21-A, `anomaly_check.py`)

2. **The correct center.** The fiber bundle structure under GCD
   gives Z_6 = center(SU(2) x SU(3)). (D21-E, `fiber_bundle.py`)

3. **The correct confinement pattern.** The XOR asymmetry gives
   q=2 open (weak, unconfined) and q=3 locked (strong, confined).
   (`xor_asymmetry.py`)

4. **The correct structural ratios.** The within-sector ratio 2/3
   is depth-invariant and equals the mediator mode.
   (`depth_sweep_v2.py`)

5. **Parity as geometry.** The frame bundle gives O(3), and the
   pin cover Pin+(3) = SU(2) x Z_2 makes parity part of the
   structure group. (D20)

What it does NOT produce:

6. **Not the full Lie algebras.** Neither su(2) nor su(3) emerge
   from the Jacobian, the tongue overlaps, or the fiber action.

7. **Not Yang-Mills dynamics.** No field equations beyond Einstein
   emerge from any continuum limit of the Klein bottle.

8. **Not the running couplings.** Tree depth does not map to
   energy in a way that reproduces beta functions.

## The structural interpretation

The Klein bottle at finite depth is a constraint surface, not a
dynamical system. It determines WHAT can exist (charges, center,
confinement pattern) but not HOW it evolves (gauge dynamics,
running, scattering amplitudes).

This is analogous to how the Klein bottle produces the Einstein
equations (how gravity works) through the continuum limit, while
producing only the charge table and center (what matter looks
like) through the XOR filter. The topology sets the kinematics;
the dynamics requires additional structure.

The gauge algebras su(2) and su(3) are the unique simple Lie
algebras with centers Z_2 and Z_3 respectively. The Klein bottle
determines the centers. The Lie algebras are the unique extensions
of those centers to simple groups — but this extension step is
not performed by the topology. It is a classification theorem
(Cartan) applied to the topological data.

Whether this constitutes a derivation of the gauge groups or
merely a very constrained hint depends on whether you accept
"unique extension of the correct center with the correct
confinement pattern and the correct charges" as sufficient.
The Klein bottle determines {2, 3, Z_6, confinement, charges}.
Cartan's classification maps Z_2 -> SU(2) and Z_3 -> SU(3)
uniquely among simple compact Lie groups. The question is whether
uniqueness of the extension counts as derivation.

## The gap that remains

The gap is dynamical, not kinematic. The Klein bottle says WHICH
groups. It does not say WHY those groups have Yang-Mills dynamics.

In the gravity sector, the answer to "why Einstein?" is Lovelock's
theorem: given d=3+1 and a rank-2 divergence-free tensor, the
Einstein equations are unique. The gauge sector needs an analogous
uniqueness theorem: given the center Z_6, the confinement pattern,
and the charge assignments, is Yang-Mills the unique dynamics?

This is not a question the framework answers yet. But it is now
a precisely stated question with all boundary conditions specified
by the topology.

## Status

**Resolved (partial).** The five D21 computations are complete.
Path 2 (gauge from mean-field F) is closed — the self-consistency
functional cannot carry gauge degrees of freedom. Path 1 (discrete
is physical) is partially confirmed: the topology determines charges,
center, and confinement, but not the gauge dynamics.

The XOR continuum limit question from D20 has a definitive answer:
**the gauge-like structure is discrete, not continuum.** Taking the
continuum limit discards exactly the information (denominator parity)
responsible for the gauge content. The continuum Klein bottle has
gravity (Einstein) but not gauge theory (Yang-Mills).

What remains is not a computation but a theorem: the uniqueness
of Yang-Mills given the Klein bottle's kinematic constraints.
This is the gauge-sector analog of Lovelock. See Derivation 42.

## Proof chain position

This derivation closes the open question from D20 and the
computation plan from D21. It sits between the Klein bottle
topology (D19) and any future work on gauge dynamics.

Dependencies: D19 (Klein bottle), D20 (continuum limit negative),
D21 (five computations), D15 (SL(2,R) uniqueness for substrate
context), D17 (rank-1 for Jacobian interpretation).

## Scripts

| Script | Result | D21 test |
|--------|--------|----------|
| `anomaly_check.py` | All 6 conditions satisfied | A |
| `tongue_overlap_structure.py` | Abelian only | B |
| `depth_sweep.py` | No beta match | C |
| `depth_sweep_v2.py` | Within-sector 2/3 exact | C (structural) |
| `jacobian_fixed_point.py` | Rank-1 | D |
| `jacobian_v2.py` | 2x2 blocks, sl(2,R) | D |
| `z6_algebra.py` | Z_6 from GCD | E |
| `z6_algebra_v2.py` | Fiber Jacobian varies | E |
| `z6_algebra_v3.py` | XOR locks fiber | E |
| `fiber_bundle.py` | Z_2 x Z_3 = center | E (supporting) |
| `xor_asymmetry.py` | q=2 open, q=3 locked | Supporting |
