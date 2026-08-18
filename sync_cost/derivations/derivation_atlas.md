<!-- edition 2 (2026-08-14) · prior text: git show 2c4fd6c:sync_cost/derivations/derivation_atlas.md · ERRATA.md E1/E13/E15/E17 -->
<!-- provides: shallow-combinatorial-derivation-depth status=definition -->
<!-- provides: no-alternative-constraint-satisfaction status=conjectured -->
# Derivation Atlas — from four primitives to physical predictions

## Prelude

This document is a single linear walkthrough of the framework's
derivation chain, beginning with the four primitives and ending
with the predictions the framework makes about cosmological,
particle, and dynamical observables. It is the third deliverable
of the legitimacy homework, alongside the canonical glossary and
the phenomenology cross-reference.

The intended reader is a working physicist or mathematician who
has not encountered the framework before. The atlas does not
assume prior exposure to framework vocabulary; the canonical
glossary handles vocabulary translation, and this atlas develops
each term in context as the derivation chain reaches it.

The mathematics used is standard. Stern-Brocot trees and Farey
sequences are nineteenth-century number theory. The representation
theory of finite cyclic groups is undergraduate algebra. The
modular group PSL(2, ℤ) and its congruence subgroups Γ_0(N) are
standard graduate-level material on modular forms. Saddle-node
bifurcation theory follows from Thom's classification. Arnold
tongues and the devil's staircase are classical results in the
theory of circle maps. None of this mathematics is novel.

What is novel is the composition: that these standard mathematical
objects, when assembled in the order this atlas presents, generate
the universe's quantitative structure. That claim is checkable
against observation, and the atlas walks through what gets
predicted, what does not, and what the residuals look like.

The atlas is verbose by design. Each derivation step is stated
explicitly, with its mathematical content separated from its
physical interpretation. Readers who want the short version
should consult the phenomenology cross-reference. Readers who
want the conceptual map should consult the canonical glossary.
This document is for the reader who wants to follow the chain
in full.

The structure of the document mirrors the order of the
derivations. Part I introduces the four primitives and proves
their irreducibility. Part II constructs the derived objects
(circle, rationals, continuum, circle map) from the primitives.
Part III develops the dynamical content (Arnold tongues, mode
locking, the devil's staircase). Part IV establishes the substrate
structure (the Z_6 mode lattice, Klein-antipodal Z_2, color
Z_3). Parts V through IX present the specific physical
derivations: geometric and topological, coupling regimes,
cosmological, modular, and particle. Part X states the
methodological framework that distinguishes structural derivations
from numerology. Part XI synthesizes what the framework provides
and explicitly notes what it does not claim.

A note on length and cadence. The atlas is approximately the
length of a long dissertation chapter or a short monograph. It
does not lend itself to skimming. Readers who skim are likely
to encounter the framework's conclusions without the derivation
chain that supports them, which is exactly the kind of
encounter the atlas is designed to prevent.

---

## Part I — The four primitives

The framework rests on four irreducible primitives. Each is
necessary in the sense that without it, the others become inert.
Each is sufficient in the sense that, taken together, they
generate the rationals ℚ, the unit circle S¹(ℚ) = ℚ/ℤ, and the
canonical mode-locked dynamical system (the circle map) on which
the rest of the derivation chain operates.

The four primitives are: the integers ℤ, the mediant operation
on adjacent fractions, the fixed-point condition x = f(x), and
the parabolic bifurcation x² + μ = 0. They are not a sample of
elementary mathematical objects chosen for parsimony; they are
the minimal set whose composition generates the framework's
content. The arguments for irreducibility and sufficiency are
in `minimum_alphabet.md`, and Part I summarizes them.

### §1.1 — Integers

The integers ℤ provide counting. Counting is required for any
notion of cycle, period, or winding number. A periodic orbit of
period q must complete an integer number of returns to itself;
without integers, the very statement of periodicity has no
content. Counting is also required for any iteration: f^q(x)
demands q ∈ ℤ.

The integers are taken as a primitive rather than constructed
from set-theoretic axioms because the framework operates at the
level of physical structure, not foundational set theory. The
Peano axioms or the von Neumann construction of ℕ would suffice
to ground the integers if needed; the framework's claim is that
this grounding is the appropriate starting point for deriving
physical structure, not that the integers themselves require
no further foundation.

The integers' role across the chain: they parametrize Farey
sequence depths, they index cyclic group elements (Z_2, Z_3,
Z_6), they provide winding numbers for orbits on S¹, they label
modular subgroup levels (Γ_0(N) for integer N), and they appear
as the small framework integers (q_2, q_3, MEDIANT, INTERACT,
K_QUARK, K_LEPTON, |F_n|) whose specific values determine the
framework's quantitative predictions.

### §1.2 — Mediant

The mediant of two fractions a/b and c/d is (a+c)/(b+d). It
is defined using only integer addition; no division is performed.
The mediant of two adjacent fractions in lowest terms produces
a third fraction that lies strictly between them and that, by
the Stern-Brocot theorem (Stern 1858, Brocot 1860), is the
unique rational with the smallest denominator in the interval
(a/b, c/d).

The mediant is essential because the integers alone, even with
the parabola providing algebraic irrationals like √μ, cannot
reach the interior rationals like 1/3 or 2/5. Division would
construct them, but division is not in the framework's primitive
set; the mediant is the operation that generates ℚ from ℤ
without invoking division. This is significant for the
framework's claim of minimality: ℚ is derivable rather than
postulated.

The Stern-Brocot tree is the iterated application of the mediant
operation starting from the boundary fractions 0/1 and 1/0. At
level n, the tree contains 2^n new fractions, each the mediant
of two adjacent fractions from the previous level. The tree
enumerates ℚ_{>0} exactly once: every positive rational appears
at a unique finite depth, and the depth corresponds to the
fraction's complexity (depth roughly equals the length of the
continued-fraction expansion).

The mediant's role across the chain: it generates ℚ, it provides
the configuration space for mode-locked oscillators (each
rational corresponds to a mode-locked plateau), it generates
the action of PSL(2, ℤ) on the projective line P¹(ℚ), and it
gives the substrate's discrete state space at K < 1.

### §1.3 — Fixed-point

The fixed-point condition x = f(x) closes the dynamical loop.
Without it, the integers count but nothing iterates; the
mediants build a tree but nothing evolves on it; the parabola
defines a curve but not a dynamical system. Self-reference (the
state determines the map that determines the state) is what
turns the static catalog of numbers and shapes into a dynamics.

The fixed-point condition is not satisfied by all maps, and
the maps that do satisfy it have specific structural features.
A periodic orbit of period q with winding number p/q is the
intersection of two conditions: f^q(x) = x (return to start)
and f^q(x) = x + p (advanced by p in the integer-counted phase
space). Combining the two: x + p ≡ x in the phase space, which
forces p ≡ 0 modulo the phase space's natural unit. Since p is
arbitrary in ℤ, the phase space must quotient by ℤ. The phase
space is therefore S¹ = ℝ/ℤ. This is the derivation of the
circle (§2.1 below) from integers and fixed-point alone.

The fixed-point condition is the framework's primitive for
self-consistent state. In K-self-consistency derivations, the
substrate's coupling K satisfies K = K(modes locked at K), an
implicit equation whose solution is the operating point. In
mode-counting arguments, the partition (Ω_Λ : Ω_DM : Ω_b)
satisfies sum-to-one constraints by fixed-point relations
between the sectors.

### §1.4 — Parabola

The parabola x² + μ = 0 provides the framework's primitive for
bifurcation and orientation. For μ < 0, the parabola has two
real roots ±√(-μ); the dynamics near a saddle-node bifurcation
sends trajectories toward the stable root and away from the
unstable root, giving an orientation to the local phase space.

The parabola is the unique generic codimension-1 bifurcation on
S¹. This is a structural-stability result. Other normal forms
(x³, x^(3/2), x^n for n > 2) either require additional symmetry
to occur generically (x³ requires Z_2 symmetry for pitchfork
bifurcation), are non-smooth (x^(3/2)), or are structurally
unstable (x^n for n > 2 perturbs to dominant quadratic). Only
x² + μ = 0 is generic; only it occurs at boundaries of mode-
locked plateaus in the standard circle map without additional
assumptions.

The parabola's role: it provides the saddle-node normal form
near tongue boundaries (which forces the Born rule exponent;
§5.3), it gives orientation to S¹ (§2.2), and it underlies the
framework's energy-functional structure for partial-locking
dynamics (which closes L1 in the Direction 4 chain; Part VIII).

The parabola also provides square roots ±√(-μ), which is how
algebraic irrationals enter the framework's value set without
being primitives. The full algebraic closure of ℚ is derivable
from integers + mediant + parabola; it is not postulated.

### §1.5 — Irreducibility of each primitive

Each primitive is shown necessary by exhibiting what fails
without it.

Without integers, the mediant has no operands to combine, the
parabola's two roots cannot be counted as distinct objects,
the fixed-point equation has no iterate count (f^q requires
q ∈ ℤ), and there is no winding number, no period, no discrete
structure of any kind. The other three primitives become inert.

Without the mediant, the available number system is ℤ (from
integers) plus the algebraic irrationals like √μ (from the
parabola). The interior rationals like 1/3 and 2/5 are
unreachable. Division would construct them but division is not
composition of the remaining three primitives. The Stern-Brocot
tree, the mode-locked plateaus, and the framework's discrete
substrate state space all collapse without the mediant.

Without the fixed-point equation, the integers count but nothing
iterates, the mediants build a tree but nothing evolves on it,
and the parabola defines a curve but not a dynamical system.
There is no orbit, no periodicity, no S¹, no convergence, no
attractor. The system becomes a static catalog of numbers and
shapes with no dynamics.

Without the parabola, all maps on the circle are linear: θ ↦
θ + Ω. Linear circle maps have constant winding number W = Ω
for all initial conditions; there are no tongues, no mode
locking, no bifurcation, no basins. The Born rule's specific
exponent (probability proportional to |ψ|², exponent 2) requires
the saddle-node universal codimension-1 form; no other generic
exponent is structurally stable.

Each of the four primitives is therefore necessary; none can be
derived from the other three.

### §1.6 — Sufficiency: the four primitives generate ℚ and S¹(ℚ)

Composition of the four primitives generates the rationals ℚ
(from integers + mediant via the Stern-Brocot tree) and the
unit circle S¹(ℚ) = ℚ/ℤ (from the rationals quotiented by the
integer winding equivalence imposed by integers + fixed-point).
The continuum ℝ is the Dedekind completion of ℚ under the
standard metric. The continuum is therefore not a primitive; it
emerges as a limit. The framework explicitly does not assume
continuous structure at the substrate level; the substrate is
discrete (this becomes important in Part VI when discussing
K < 1 substrate dynamics versus the K = 1 continuum limit).

The standard real-valued circle S¹(ℝ) = ℝ/ℤ requires the
continuum; the framework's substrate-level circle is S¹(ℚ).
Continuous functions on S¹(ℝ) (such as sin and cos) are
continuum constructions; their substrate-level analogs are
algebraic, derivable as limits of rational approximations.

This sufficiency claim is verified in Shape F's primitive-
completeness audit (`primitive_completeness_audit.md`), which
checked the four primitives against all closures in the 2026-04
round and found no derivation requiring a fifth primitive.

---

## Part II — Derived objects from the primitives

This part walks through the construction of the framework's
basic mathematical objects (the circle, the rationals, the
continuum, the circle map) from the primitives. The derivations
are not novel; they restate well-known constructions in the
framework's vocabulary. The point of restating them is to make
explicit the chain from primitives to the dynamical system on
which the rest of the framework operates.

### §2.1 — The circle S¹ from integers + fixed-point

A periodic orbit of period q with winding number p/q satisfies
two conditions simultaneously: the fixed-point return condition
f^q(x) = x and the integer-counted advance condition f^q(x) =
x + p. Their combination yields x + p ≡ x in the phase space.
Since p is an arbitrary integer (by the integer primitive), all
integers must be equivalent to zero in the phase space. The
phase space is therefore the quotient ℝ/ℤ = S¹.

This derivation produces the circle as the unique topology
consistent with integer-counted periodic orbits. The mod-1
identification is not a choice of coordinates; it is forced by
the simultaneous existence of integer winding counts and self-
returning orbits.

The substrate-level circle is S¹(ℚ) = ℚ/ℤ, since the rationals
are generated by integers + mediant (§1.6) and the continuum is
not a primitive. The continuous circle S¹(ℝ) emerges only after
Dedekind completion of S¹(ℚ); in the framework's substrate
regime (K < 1), only the rational circle is occupied.

### §2.2 — Orientation from the parabola

The parabola x² + μ = 0 has two roots ±√(-μ) for μ < 0. In a
saddle-node bifurcation, these roots correspond to a stable
attractor and an unstable repeller. The flow near the saddle-
node sends trajectories toward the attractor and away from the
repeller; this asymmetry between the two roots breaks the
naïve symmetry x ↔ -x and provides a local orientation.

On the circle S¹, the saddle-node bifurcation occurs at the
boundary of each mode-locked plateau (Arnold tongue). At the
tongue boundary, two fixed points of the circle map merge and
annihilate; the parabola's two roots correspond to these two
fixed points before annihilation. The direction from the
unstable fixed point toward the stable fixed point defines a
local orientation.

Globally, this means that S¹ is oriented: there is a consistent
notion of "forward" around the circle, derived from the
parabola's asymmetric roots. Orientation is not a fifth
primitive; it is the parabola's two roots read directionally
through the saddle-node dynamics.

### §2.3 — The rationals ℚ from integers + mediant

The Stern-Brocot tree constructs every positive rational
exactly once by iterated mediants starting from the boundary
fractions 0/1 and 1/0:

```
Level 0:  0/1                                    1/0
Level 1:                  1/1
Level 2:        1/2                  2/1
Level 3:   1/3       2/3       3/2       3/1
Level 4: 1/4 2/5  3/5 3/4   4/3 5/3  5/2 4/1
...
```

At each step, the mediant (a+c)/(b+d) of two adjacent fractions
is inserted between them. By the Stern-Brocot theorem, the
mediant is the unique fraction with smallest denominator in the
open interval (a/b, c/d) when a/b and c/d are adjacent in the
tree.

The tree has several structural properties relevant to the
framework. First, every rational in ℚ_{>0} appears at a unique
finite depth. Second, the depth at which a rational appears
correlates with its complexity: the convergents of a fraction's
continued-fraction expansion appear at depths determined by the
expansion's length. Third, the mediant operation generates the
action of PSL(2, ℤ) on the rationals (this is the connection to
modular forms used in Part VIII). Fourth, the tree's binary
structure is order-preserving: traversing the tree in inorder
visits the rationals in increasing order.

Extension to ℚ requires the parabola for orientation (§2.2); the
negative branch mirrors the Stern-Brocot tree across the origin.
With orientation, ℚ = {0} ∪ ℚ_{>0} ∪ (-ℚ_{>0}) is generated by
integers + mediant + parabola.

### §2.4 — The continuum ℝ as completion (not a primitive)

The reals ℝ are not in the framework's primitive set. They
emerge as the Dedekind completion of ℚ, which is the limiting
process where every Cauchy sequence of rationals is identified
with a real number (or, equivalently, where every Dedekind cut
of the rationals defines a real number).

The substrate-level statement is that the continuum is the
K = 1 limit (Part VI, §6.3). At K = 1, all Arnold tongues fill
configuration space completely, the gaps in the devil's
staircase shrink to zero measure, and the substrate's discrete
state space becomes continuous. This is general relativity
(Proof A; `continuum_limits.md` Part I).

At K < 1, there are gaps in the tongue cover. The gaps
correspond to irrational winding numbers that are not in the
mode-locked plateaus. Per `denomination_boundary.md` §134, the
substrate's quantum states live in these gaps. The substrate is
therefore always discrete at any finite coupling K < 1, and
the continuum is never physically realized (the fidelity bound
D9 prevents reaching K = 1 exactly).

This is significant for the framework's foundational claim: the
continuum is derived, not assumed; the substrate's natural
state is discrete; continuous mathematics applies only as the
K = 1 limit, which is general relativity. Quantum mechanics
(K < 1) and general relativity (K = 1) are therefore two
distinct continuum limits of the same discrete substrate, with
non-smooth transition between them (per N11 in
`continuity_in_K_nulls.md`). This is the framework's resolution
of the GR-QM unification problem (Part VI, §6.3).

### §2.5 — The circle map as the canonical assembly

The standard circle map is

θ_{n+1} = θ_n + Ω - (K/2π) sin(2πθ_n)   (mod 1)

where θ ∈ S¹, Ω ∈ ℚ is the bare frequency, K is the coupling
strength, and the (mod 1) operation enforces the S¹ topology.
Each component of the map traces to a primitive:

- θ ∈ S¹: integers + fixed-point (§2.1)
- Ω via Stern-Brocot: integers + mediant (§2.3)
- (mod 1): integers + fixed-point (§2.1)
- sin(2πθ): the parabola, in disguise. Near any tongue boundary,
  the circle map's fixed-point equation reduces to the saddle-
  node normal form δθ² + (Ω - p/q) = 0. The global shape of
  sin determines which tongues exist and their widths, but the
  local dynamics at every boundary depend only on the parabola.
- K: a continuous parameter; emerges from completion in the
  K = 1 continuum limit. At K < 1 substrate level, K labels
  the substrate's coupling regime.

The circle map is therefore the canonical four-primitive
assembly. Its dynamics include Arnold tongues (Part III), mode
locking (Part III), the devil's staircase (Part III), the
Born rule (Part V), and the substrate's discrete configuration
space (Part VI). Most of the framework's quantitative predictions
are downstream of the circle map's structure.

The sine function is not a fifth primitive. It is the global
extension of the local saddle-node parabola's behavior across
all tongue boundaries simultaneously. The framework's substrate
operates at the level of the circle map's local dynamics; the
specific global shape (sine versus other periodic functions)
affects which tongues are widest, but the universality class
of the saddle-node behavior at each boundary depends only on
the parabola.

---

## Part III — Dynamical content from the circle map

The circle map's dynamics at small to moderate K produce the
Arnold tongue structure: mode-locked plateaus at every rational
winding number p/q, with widths scaling as (K/2)^q. This part
develops the dynamical content needed for the framework's
substrate physics.

### §3.1 — Arnold tongues and mode locking

For each rational p/q, the circle map has a range of bare
frequencies Ω near p/q for which the asymptotic winding number
W is exactly p/q. This range is the Arnold tongue at p/q. The
tongue's width at small K scales as (K/2)^q. Smaller q
corresponds to a wider tongue, which means a more stable mode-
locked state.

The tongue at p/q is bounded by two saddle-node bifurcations:
one at the tongue's left edge (where the stable and unstable
fixed points merge as Ω decreases) and one at the right edge
(merging as Ω increases). Inside the tongue, the dynamics has
a stable periodic orbit of period q with winding number p/q.

Mode locking is the dynamical phenomenon by which the system
maintains its winding number against perturbations to the bare
frequency, as long as Ω stays within the tongue. This is the
mechanism for synchronization in coupled oscillators, phase-
locked loops, and biological circadian entrainment, all of
which are standard physics applications of the circle map.

### §3.2 — The devil's staircase

The asymptotic winding number W as a function of bare frequency
Ω, taken at fixed K < 1, is a monotonic function with plateaus
at every rational. The plateaus are the Arnold tongues; their
widths sum to less than 1 at K < 1, leaving gaps where W is
irrational. The function is called the devil's staircase
because of its self-similar plateau structure.

At K = 1, the plateaus' widths sum to exactly 1; the gaps have
zero Lebesgue measure but form a Cantor set. The irrational
winding numbers at K = 1 are confined to this Cantor set. As
K decreases below 1, the tongues narrow and the gaps grow.

The framework's substrate operates at K < 1. The substrate's
mode-locked states correspond to rationals with widths large
enough to be physically realized at the substrate's coupling.
The gaps correspond to irrational winding numbers that are not
substrate states; they are the "cosmological constant fixed
point" or analogous limiting states of the substrate dynamics.

### §3.3 — Tongue widths and the Stern-Brocot stability ordering

The tongue at p/q has width w_pq ~ (K/2)^q at small K. This
means the stability ordering of the tongues (by width) is the
denominator ordering: smaller q gives wider tongues.

The Stern-Brocot tree enumerates rationals by depth, and the
depth correlates with denominator (small-denominator fractions
appear at low depth). Therefore the Stern-Brocot tree's order
is the substrate's stability order: the most stable mode-locked
states are the small-denominator rationals at the top of the
tree.

This is the framework's structural justification for the
Stern-Brocot tree as the configuration space. Per
`mediant_derivation.md`, the tree is not a choice of
discretization; it is the unique enumeration consistent with
the Arnold-tongue stability ordering. Any periodic, antisymmetric,
smooth coupling on S¹ produces tongues at all rationals with
width ordering w ~ (K/2)^q; the Stern-Brocot tree is the
unique enumeration that respects this ordering.

The continuum (ℝ) fails this stability ordering criterion
because between any two reals there are uncountably many
others, with no canonical "simplest" one. Discreteness with
denominator ordering is forced by the dynamics, not chosen.

### §3.4 — K = 1 critical coupling and the continuum limit

At K = 1, the Arnold tongues fill measure 1 of the bare-frequency
axis. The devil's staircase becomes "complete" in the sense
that almost every Ω is in a mode-locked plateau. The remaining
gap structure (the Cantor set) has zero measure but is still
non-empty; the irrationals at K = 1 are still distinguishable
from the rationals.

The K = 1 limit corresponds to the continuum: the substrate's
discrete state space (ℚ at K < 1) extends to the full circle
(ℝ/ℤ at K = 1) as the gaps fill in. Per `continuum_limits.md`
Part I, the dynamics at K = 1 are equivalent to general
relativity: the smooth continuum, the diffeomorphism invariance,
and the geodesic structure all emerge in the K = 1 limit.

The fidelity bound D9 prevents the substrate from reaching
K = 1 exactly; the physical system is always at some K < 1.
The continuum is therefore the limit, not the realized state.
The framework's substrate is always discrete; the continuum is
the unattainable boundary.

### §3.5 — K < 1 substrate and discreteness

At K < 1, there are gaps between the Arnold tongues. The gaps
correspond to bare frequencies Ω for which the dynamics does
not lock to any rational; the asymptotic winding number is
irrational and the orbit is quasiperiodic.

Per `denomination_boundary.md` §134, the substrate's quantum
states live in these gaps. The framework's substrate is
therefore "always discrete" in the sense that the modes
accessible to the substrate are exactly those at rational
winding numbers in the mode-locked plateaus; the gaps are not
populated by substrate states but by quantum modes that are not
yet "denominated" (not yet locked to a specific rational).

This is significant for the framework's quantum mechanics. The
substrate's discrete states are the rational mode-locked plateaus;
the quantum states are the gaps. Quantum mechanics is the
dynamics of the gaps as they shift with K; general relativity
is the K = 1 limit where the gaps close. Per `continuum_limits.md`
Part II, quantum mechanics emerges as the small-ε linearized
limit at K < 1.

The key consequence for Part VIII (the L1 closure) is that the
substrate's state space has a natural quantization grain at
each cusp: at cusp 1/2 of Γ_0(6) with denominator q, the
allowed weights are {1/q, 3/q, ..., (q-1)/q} (the rationals in
the cusp orbit at that denominator). This quantization is not
imposed; it is the substrate's actual state space at finite K.

---

## Part IV — Substrate structure: the Z_6 mode lattice

The substrate's mode space is the Z_6 = ℤ/6ℤ cyclic group. By
the Chinese Remainder Theorem, Z_6 = Z_2 × Z_3, where Z_2 is
generated by the framework's smaller prime q_2 = 2 and Z_3 is
generated by the larger prime q_3 = 3. The framework's substrate
content is structured around this q_2 × q_3 decomposition.

### §4.1 — The Z_6 mode lattice

The substrate's natural mode-counting takes place on Z_6. The
six elements {0, 1, 2, 3, 4, 5} represent six distinguishable
substrate modes. The choice of Z_6 over other small cyclic
groups (Z_4, Z_8, Z_12, etc.) is forced by the framework's
prime support {q_2, q_3} = {2, 3}, which is itself forced by
the K-axis uniqueness probe (`k_axis_uniqueness.md`): the
Klein-antipodal + coprime-to-6 plateau structure escapes
framework-integer territory at primes ≥ 11, restricting the
framework's structurally admissible prime set to {2, 3}.

The cardinality |Z_6| = 6 = q_2 × q_3 = INTERACT is one of the
framework's small framework integers, appearing in the partition
denominator structure (Part VII, §7.1) and in the Hecke level
of the substrate-preserved modular subgroup Γ_0(6) (Part VIII).

### §4.2 — Klein-antipodal Z_2 reduction

The Z_2 quotient of Z_6 corresponds to the Klein-antipodal
involution τ: k ↦ -k (mod 6) on Z_6. The fixed points of τ
are {0, 3} (the elements satisfying 2k ≡ 0 mod 6); the orbits
are {0}, {3}, {1, 5}, and {2, 4} — two singletons and two
two-element orbits.

The Klein-antipodal involution is the framework's Z_2 reduction;
it carries the meaning of "reflection through the substrate's
antipodal axis." Modes that are fixed under τ (the singletons
{0} and {3}) are unchanged by the involution; modes that are
permuted (the two-element orbits {1, 5} and {2, 4}) decompose
into Z_2 representations.

### §4.3 — Color triplet Z_3 sector

The Z_3 quotient of Z_6 corresponds to the cyclic action σ: k
↦ k + 2 (mod 6) on Z_6 (since multiplication by 2 acts as a
generator of Z_3 in Z_6 under the CRT decomposition). The
orbits of σ are {0, 2, 4} and {1, 3, 5} — two three-element
orbits, corresponding to the two cosets of the Z_3 subgroup.

The Z_3 sector is the framework's color triplet. The three-fold
symmetry corresponds to SU(3) color in the Standard Model;
modes within a Z_3 orbit are color-equivalent. The framework
identifies q_3 = 3 with the spatial dimension count
(`three_dimensions.md`) and with the gauge color-triplet count
in the SM gauge group derivation.

The Z_2 and Z_3 actions commute (since Z_2 and Z_3 are coprime
in Z_6 by CRT), so the substrate's mode structure has a
well-defined Z_2 × Z_3 decomposition. Each mode k ∈ Z_6 has
both a Z_2 label (its residue mod 2) and a Z_3 label (its
residue mod 3); these labels are independent.

### §4.4 — Sym/antisym mode decomposition

For each two-element Z_2 orbit {p, τ(p)} = {p, 6-p}, the two
eigenvectors of τ are

ψ_+(p, 6-p) = ψ_p + ψ_{6-p}  (eigenvalue +1, sym, Klein-singlet)
ψ_-(p, 6-p) = ψ_p - ψ_{6-p}  (eigenvalue -1, antisym, sign rep)

The sym mode is the trivial Z_2 representation; the antisym
mode is the sign representation. The fixed points {0} and {3}
are already eigenvectors of τ (with eigenvalue +1), so they are
trivially sym.

This decomposition is the framework's primary tool. It appears
in three independent derivations (per
`klein_antipodal_z2_rep_pattern.md`):

- The cosmic partition Ω_Λ : Ω_DM : Ω_b (Part VII), where the
  baryon mode is the sym Klein-singlet ψ_+(1, 5) intersected
  with the coprime-to-6 condition, and the antisym partner
  ψ_-(1, 5) is dark matter.
- The down-type quark factor 6 (Part IX), where S_3 acting on
  Z_2 × Z_3 produces orbit dimensions {1, 3} = {q_3-trivial,
  q_3-vector} and the factor 6 = |L| = q_2 · q_3 emerges from
  orbit-counting.
- The up-type quark factor 9 (Part IX), where Klein parity -1
  on Fibonacci shift applied to matter modes gives K_LEPTON =
  q_3².

The same Z_2 representation theory generates structurally
independent results across cosmological and particle sectors.
This cross-domain consistency is the framework's strongest
internal evidence for the Z_2 × Z_3 substrate structure.

### §4.5 — Klein-singlet ∩ coprime-to-6 selection

The cosmic partition derivation (`baryon_fraction.md`) requires
a specific selection criterion to identify the baryon mode:
Klein-singlet (sym under Klein-antipodal Z_2) intersected with
coprime-to-6 (numerator coprime to the substrate cardinality).

In Z_6, the elements coprime to 6 are {1, 5} — the boundary
modes that don't share a common factor with 6. The Klein-
antipodal pair {1, 5} therefore gives two eigenvectors:
ψ_+(1, 5) (sym, Klein-singlet) and ψ_-(1, 5) (antisym, sign).

The unique Klein-singlet ∩ coprime-to-6 mode is ψ_+(1, 5). It
is the boundary baryon: a single mode with Klein-monodromy +1
(EM-coupled) and coprime-to-6 (sits at the substrate's
boundary, not in the interior). Its partial-locking weight at
the EM-MOND threshold is the parameter w_+ that Part VIII
derives as 13/14.

The antisym partner ψ_-(1, 5) has Klein-monodromy -1, which
cancels its net EM coupling. It gravitates but doesn't EM-
couple — that is the framework's identification of "dark
matter" as a specific substrate sector rather than a particulate
species.

The framework's specific mode-counting in the Z_6 lattice is
catalogued in `baryon_fraction.md` and reorganized in logit
form in `partition_logit_form.md`. The mode counts (4 inner +
2 boundary in matter sector, etc.) determine the Ω partition's
specific values 13:5:1/19, which Part VII develops.

---

## Part V — Geometric and topological arguments

This part presents one derivation whose result is exact and
established (the Born rule exponent = 2) and two arguments that
are currently open (spatial dimension = 3 and Lorentz symmetry
= Spin(3,1); both were demoted from the scorecard in 2026-08,
D2 disposition).

### §5.1 — Spatial dimension = 3 (open)

Two routes have been proposed. The substrate's mode-counting on
Z_6 = Z_2 × Z_3 identifies q_3 = 3 with the color triplet
count, and the reading lifts this Z_3 sector to three
independent spatial extension directions. `three_dimensions.md`
argues instead through the mediant's SL(2,ℤ) symmetry
completing to SL(2,ℝ), whose dimension 2² − 1 = 3.

Both routes are open. The Z_3-sector lift asserts, and does not
construct, the identification of an internal counting sector
with extension directions. The SL(2,ℝ) route's continuum-
completion step names no mathematical operation (SL(2,ℤ) is
discrete and closed in SL(2,ℝ)), and the same premises admit
d = 2 and d = 1 constructions (`three_dimensions.md`). The
claim returns to the scorecard if a construction forces dim 3
without assuming it.

### §5.2 — Lorentz symmetry = Spin(3,1) (open)

SL(2,ℂ) ≅ Spin(3,1) — the unique simply-connected double cover
of the proper orthochronous Lorentz group, with the spinor
representation realized by SM fermions — is a true imported
theorem, and complexifying SL(2,ℝ) reaches it. Every arrow
leading there is open: the argument inherits the §5.1 break,
and 𝔰𝔩(2,ℝ) is 𝔰𝔬(2,1), not 𝔰𝔬(3), so it cannot serve as the
claimed rotation subalgebra. The published signature argument
additionally rests on a sign rule that contradicts the
orientation character being a homomorphism
(`minkowski_signature.md`).

### §5.3 — Born rule from saddle-node parabola

The Born rule states that the probability of measuring a
quantum state ψ in eigenstate |φ⟩ is |⟨φ|ψ⟩|². The exponent 2
is the framework's derivation target.

Per `born_rule.md` and `a1_from_saddle_node.md`, the derivation
proceeds from the saddle-node normal form (the parabola
primitive) at tongue boundaries in the circle map. Near a
saddle-node bifurcation at parameter μ → 0, the residence time
of the dynamics near the merging fixed points scales as
1/√(-μ) for μ < 0, and the survival probability of a
trajectory near the bifurcation point scales as the inverse of
this residence time.

When the bifurcation is interpreted as a measurement (the
quantum system "deciding" between eigenstates), the resulting
probability has the form |amplitude|^n where n is the
saddle-node exponent. The parabola's universal codimension-1
form fixes n = 2: any other exponent would correspond to a
different codimension, requiring additional structure (symmetry,
fine-tuning) beyond the generic case.

The Born rule's specific exponent is therefore forced by the
saddle-node universality, which is forced by the parabola
primitive's irreducibility. No other generic exponent on S¹ is
structurally stable.

Result: Born rule exponent = 2, exact.

The contrast with standard physics: standard quantum mechanics
postulates the Born rule. Various derivations have been
proposed (Gleason's theorem under specific axioms, decoherence-
based arguments, frequentist arguments) but none derives the
exponent from first principles without assumptions equivalent
to the Born rule itself. The framework's derivation grounds the
exponent in the universal saddle-node bifurcation.

### §5.4 — Uncertainty relation

The framework derives an uncertainty relation τ × Δθ = 1.000000
(exact at the substrate level), where τ is a characteristic time
and Δθ is the corresponding phase uncertainty. The relation is
the substrate-level analog of Heisenberg's uncertainty
relation, derived from the saddle-node dynamics + the discrete
substrate structure.

Per D7 and D9 of the derivation chain, the uncertainty bound is
exact at K < 1 (the substrate level) and saturates at the
substrate's natural quantization grain.

Result: τ × Δθ = 1, exact.

---

## Part VI — Coupling regimes and operating points

The framework's substrate has a coupling parameter K that
distinguishes physical regimes. K = 1 is the continuum limit
(general relativity); K < 1 is the discrete substrate (quantum
mechanics emerges as small-ε limit). Multiple distinct K's
appear in the framework, and disambiguating them is essential
to avoid the K_c-style vocabulary trap that
`vocabulary_is_the_work_pattern.md` Instance 4 documents.

### §6.1 — K-coupling parameter and the K-zoo

The framework has at least four distinct K's, each playing a
different structural role:

- **K_map = 1**: the circle map's golden-mean critical line; the
  K = 1 limit at which Arnold tongues fill measure 1.
- **K_c**: the standard Kuramoto critical coupling for
  synchronization. For identical oscillators, K_c = 0; for
  disordered Kuramoto, K_c > 0. The framework's substrate has
  identical oscillators, so K_c = 0; this is not the same as
  the framework's matter-sector operating coupling.
- **K_STAR ≈ 0.86196**: the matter-sector operating coupling
  derived in `item12_K_star_closure.py` from joint matter-sector
  closure (Higgs sector + lepton sector + quark sector
  consistency). K_STAR is the substrate's actual operating
  point in the matter sector.
- **K_0 ~ 3**: the RFE iteration nucleation threshold, distinct
  from K_STAR and K_c. Used in the RFE simulation chain for
  threshold dynamics.

The K-zoo disambiguation is one of the framework's recurring
vocabulary issues. Instance 4 of
`vocabulary_is_the_work_pattern.md` records the specific
confusion: applying disordered-Kuramoto K_c (~0.5-1 depending on
distribution) to the framework's setup gave residuals; the
correct K_c for identical oscillators is 0, which dissolves the
residual without further work.

### §6.2 — K_STAR matter sector operating point

The K_STAR ≈ 0.86196 operating coupling appears in the
framework's matter-sector closures (`item12_K_star_closure.py`,
`mass_sector_closure.md`). It is determined by joint
self-consistency of the Higgs sector, lepton sector, and quark
sector mass formulas, with no individually fitted parameters.

K_STAR sits in the INTERACT plateau of the K-axis uniqueness
probe (`k_axis_uniqueness.md`): the composed Klein-antipodal +
coprime-to-6 orbit count at K = K_STAR matches the framework
integer 6 = INTERACT, with the staircase-resolved max-q at
plateau tolerance ≤ 5e-4 reaching q = 8. K_STAR's placement in
this plateau is a non-tuning alignment between the
independently derived K_STAR and the substrate's natural orbit
count.

### §6.3 — The K = 1 ↔ K < 1 sector decoupling

The framework's two continuum limits — general relativity at
K = 1 and quantum mechanics at K < 1 — are non-smoothly
separated by the K = 1 critical line. Per N11 of
`continuity_in_K_nulls.md`, the tongue coverage discontinuity at
K = 1 prevents a smooth interpolation between the two regimes.

This is the framework's structural answer to the GR-QM
unification problem. Standard physics has searched for a smooth
unification (a single equation that reduces to GR in one limit
and QM in another); the framework's claim is that no such
smooth unification exists because the two regimes are
non-smoothly separated. They share a common substrate (the
discrete Stern-Brocot tree at K < 1, completing to the
continuum at K = 1), but the transition between them is not
analytic.

Per the D.3 closure (`path_closures_iter3.md`), this non-smooth
separation forces independent anchors per sector. The
cosmological anchor (H_0) governs the K = 1 GR sector; the
particle anchor (v_EW) governs the K < 1 QM sector. The
two-anchor minimum is therefore structural, not a derivation
gap.

### §6.4 — λ_unlock partial-decoupling rate

Per `kam_bridge_synthesis.md`, the substrate has a partial-
decoupling rate

λ_unlock = (4G - π · ln 2) / π

where G is Catalan's constant. This is the Arnold Lyapunov
rate on the Z_2 quotient of the substrate; it characterizes how
modes partial-decouple at the MOND threshold.

λ_unlock is a real-analytic constant; it does not require
fitting. It enters the framework's substrate-side A_s prediction
and the partial-locking dynamics that determine w_+ at cusp
1/2 of Γ_0(6).

### §6.5 — MOND threshold a_0 derived from Λ

Per `a0_threshold.md`, the MOND acceleration scale is

a_0 = c · H_0 / (2π)

where H_0 is the Hubble constant. The 1/(2π) factor is
substrate-derived from the relation Λ ↔ H_0 ↔ a_0; the absolute
scale of a_0 follows from H_0 (anchor input).

Numerically: a_0 = 1.25 × 10⁻¹⁰ m/s² from H_0 = 67.4
km/s/Mpc; the Lelli et al. 2017 RAR observation gives
1.2 × 10⁻¹⁰ m/s², a 4% match.

The MOND threshold is the framework's substrate feature for
partial-decoupling at low acceleration. Above the threshold
(a > a_0), modes lock fully (Newtonian dynamics); below the
threshold (a < a_0), modes decouple from full lock (MOND-
modified dynamics); at the threshold (a = a_0), modes partial-
lock at weight w that depends on the substrate's coupling and
the mode's specific structure.

For the boundary mode ψ_+(1, 5), the partial-locking weight is
w_+, which Part VIII derives as 13/14 from the cusp-1/2 ground
state in the substrate's Hecke modular structure.

### §6.6 — Substrate discreteness as quantization apparatus

The substrate is discrete at K < 1 (per §3.5 + §6.3). The
discreteness is not a coarse-graining of an underlying
continuum; it is the substrate's actual state space. At cusp
1/2 of Γ_0(6) with denominator q, the substrate's accessible
weights are {1/q, 3/q, ..., (q-1)/q}, the rationals in the
cusp orbit at that denominator.

This discreteness functions as the substrate's measurement
apparatus for soft boundaries. The MOND threshold, considered
in pure continuum, is a smooth crossover with no specific
w-location; "where is w_+?" has no operational answer in
continuum. The substrate's grain provides the answer: the
substrate is at the grain state minimizing the energy
functional, and under local linearity (the energy functional's
curvature scale exceeds the grain spacing), this is uniquely
the closest grain state to the unconstrained continuum minimum.

This is the L1 closure (`L1_substrate_cusp_ground_state.md`)
that Part VIII develops in detail. The closure's load-bearing
content is that substrate discreteness IS the operational
apparatus for the MOND threshold's location, not an artifact of
discretization superimposed on an underlying continuum.

---

## Part VII — Cosmological derivations

This part presents the framework's cosmological predictions:
the Planck-Hubble hierarchy R, the cosmological constant
Λ · ℓ_P², the cosmic partition Ω_Λ : Ω_DM : Ω_b, the two-
component closure for Ω_b, and the substrate-side A_s.

### §7.1 — The cosmic partition Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19

The framework's substrate has a Z_6 mode lattice (Part IV).
Per `baryon_fraction.md`, the cosmic partition is derived by
mode-counting on Z_6 with three filters:

- Klein-singlet selection (sym under Klein-antipodal Z_2)
- Coprime-to-6 selection (numerator coprime to substrate
  cardinality)
- Inner versus boundary distinction

The mode count for each cosmological sector:

- Inner modes {0, 2, 3, 4}: always locked (4 modes)
- Antisym boundary ψ_-(1, 5): always locked (1 mode, no EM)
- Sym boundary ψ_+(1, 5): partial-locked at w (1 mode)

At the framework's static prediction (single-w, w = 1):
- Matter sector: 4 + 1 + 1 = 6 modes (= INTERACT)
- DM sector: MEDIANT = 5 modes
- DE sector: |F_6| = 13 modes (Farey count at depth 6)
- Total: |F_7| = 19 modes (Farey count at depth 7)

The partition is

Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19

Numerically: Ω_Λ = 13/19 = 0.6842, Ω_DM = 5/19 = 0.2632,
Ω_b = 1/19 = 0.0526.

Comparison to Planck 2018:
- Ω_Λ_obs = 0.6847 ± 0.0073: 0.07σ match
- Ω_DM_obs = 0.265 ± 0.007: 0.7% off
- Ω_b_obs = 0.0493 ± 0.0003: 6.7% off (the original Floor)

The single-w partition is the framework's "first-order"
prediction. The two-component closure (§7.4) refines it.

### §7.2 — The Planck/Hubble hierarchy R = 6 · 13⁵⁴

Per `hierarchy_gaussian_lattice.md`, the ratio of the Hubble
length to the Planck length is

R = L_H / ℓ_P = 6 · 13⁵⁴

where 6 = INTERACT and 13 = |F_6| are framework integers, and
54 = q_2 · q_3³ = 2 · 27 is the depth count.

Numerically: R = 6 · 13⁵⁴ ≈ 8.533 × 10⁶⁰. The observed value
(from H_0 and ℓ_P) is 8.492 × 10⁶⁰; the residual is 0.48%.

R is the largest dimensionless number in cosmology (the ratio
between the universe's smallest natural length scale and its
largest natural length scale). The framework's derivation
gives it as a depth-54 stratification, with each step
multiplying by a substrate factor. This is the framework's
"depth machine" for producing very small or very large
dimensionless ratios.

### §7.3 — The cosmological constant Λ · ℓ_P² = 13⁻¹⁰⁸ / 12

Combining R = 6 · 13⁵⁴ (§7.2) with the substrate's structural
identity:

Λ · ℓ_P² = 3 / R² = 3 / (6 · 13⁵⁴)² = 3 / (36 · 13¹⁰⁸) = 13⁻¹⁰⁸ / 12

Numerically: Λ · ℓ_P² ≈ 10⁻¹²¹·⁵, observed ~10⁻¹²¹·⁵; the
exponent matches to 0.1%.

This is the framework's constructive derivation of the
cosmological constant. The smallness 10⁻¹²² × M_P⁴ is the
expected behavior of multiplicative depth-54 stratification, not
fine-tuning. Standard QFT estimates of Λ ~ M_P⁴ (the "naive"
expectation) are based on Wilsonian RG with quadratic
divergences; per `hierarchy_problem_translation.md`, neither
applies to the substrate (no Wilsonian RG because the substrate
is discrete; no quadratic divergences because there's no
continuum integral at substrate level). The "cosmological
constant problem" framing is therefore a category error in the
substrate; the framework's derivation simply produces the right
magnitude.

### §7.4 — Two-component closure for Ω_b

The single-w partition (§7.1) gives Ω_b = 1/19 = 0.0526, with
6.7% residual against the observed 0.0493. This was the
framework's headline Floor entry until the 2026-04 round.

Per `omega_b_alpha_beta_closure.md`, the resolution comes from
recognizing that the matter sector's modes have two components,
not one. The boundary modes {1, 5} contribute both a sym
(Klein-singlet) eigenvector ψ_+(1, 5) and an antisym (sign-rep)
eigenvector ψ_-(1, 5):

- ψ_+(1, 5): sym, Klein-monodromy +1, EM-coupled, partial-locks
  at MOND threshold with weight w_+
- ψ_-(1, 5): antisym, Klein-monodromy -1, no EM coupling, no
  MOND threshold, always full lock with weight w_- = 1

The matter sector at partial weight is then 4 (inner) + 1
(antisym boundary, always locked) + w_+ (sym boundary, partial-
locked) = 5 + w_+. The DE sector picks up additional weight
12 + w_+ (the partial unlocking from baryon to DE is
2(1 - w_+); the sym mode contributes to both DE and baryon).

The partition under the two-component closure becomes:

Ω_b = w_+ / (17 + 2w_+)
Ω_DM = 5 / (17 + 2w_+)
Ω_Λ = (12 + w_+) / (17 + 2w_+)

with single free parameter w_+ at this stage.

### §7.5 — The (α, β) = (0, 1) closure from sign-rep no-EM

The two-component closure parameters (α, β) determine how the
matter sector's mode count breaks into components. Per
`omega_b_alpha_beta_closure.md`, (α, β) = (0, 1) is forced by
the structural fact that the antisym mode has no EM coupling
and therefore always locks fully.

The argument: the Klein-monodromy -1 of ψ_-(1, 5) cancels its
net EM coupling. Without EM, the mode does not see the MOND
threshold, so its partial-locking dynamics do not apply; the
mode is at w_- = 1 always. This forces α = 0 (no antisym
contribution to the partial-weight partition) and β = 1 (full
antisym lock).

This is a recognize-mode closure: the structural content
("monodromy -1 kills net EM") is already in `baryon_fraction.md`.
The closure articulates the existing content as forcing (α, β)
= (0, 1).

With (α, β) = (0, 1) and w_- = 1 forced, the closure becomes
single-parameter (w_+ only). Solving Ω_b_pred(w_+) = Ω_b_obs:

w_+ = 0.04930 / (1 - 0.0986) ≈ 0.9298

Predictions at w_+ = 0.9298:
- Ω_b: 0.0493 (0.000%, fit)
- Ω_DM: 0.26512 (0.044% off observed)
- Ω_Λ: 0.68558 (0.129% off observed)

All three sub-σ on the Planck data, with one fit parameter.
The (α, β) = (0, 1) mechanism argument stands on its own; the
value w_+ ≈ 0.93 is and remains an empirical fit. The L1
closure (Part VIII), which claimed to derive w_+ = 13/14
structurally, was retracted to Class 2 in 2026-08: the closure
was written after the fitted value (ERRATA.md E-ledger;
commit forensics in the D1 disposition).

### §7.6 — The spectral tilt n_s

Per `a_s_geometric_proof.md` and the derivation chain D4, the
scalar spectral tilt of CMB fluctuations is

n_s ≈ 0.963 to 0.966

with the precise value depending on the matter-sector closure
parameters. Observed: n_s = 0.9649 ± 0.0042 (Planck 2018).
Residual: < 0.2%.

The derivation grounds n_s in the substrate's static curvature
variance derivation (the same chain that produces A_s) at the
matter pivot scale. The derivation is closed-form (no fitted
parameters); Z1-Z3 status: pass. Class: Survives.

### §7.7 — The substrate-side scalar amplitude A_s

The framework's substrate-side scalar amplitude is

A_s_substrate = (1 - φ⁻⁴) / (4 · λ_unlock · φ · q_pivot²) = 2.33 × 10⁻⁹

derived from the substrate's static curvature variance at the
matter pivot scale (`a_s_geometric_proof.md`, A1-A9). This is
the framework's complete substrate-side prediction.

The observed scalar amplitude is A_s_obs = 2.10 × 10⁻⁹ (Planck
2018), an 11% gap to the substrate-side prediction. The gap is
the inflation amplification factor:

f_amp = (H_inf / M_P)² / (8π² · ε · c_s)

where H_inf and ε are anchor-side (per `h_inf_status.md`). The
framework correctly declines to predict f_amp; this is the
Instance 7 closure (`vocabulary_is_the_work_pattern.md`).

The framework therefore provides:
- A_s_substrate (substrate-side, exact, no fitted parameters)
- The reading that A_s_obs requires anchor-side amplification
- An explicit decline to predict the amplification factor
  (consistent with the two-anchor minimum)

This is the same shape as lattice QCD (bare lattice coupling
versus continuum-renormalized coupling): the framework gives
the bare quantity, and the conversion to the observed quantity
requires anchor-side input. The "11% gap" is therefore not a
derivation gap; it is the explicit boundary between substrate-
side and anchor-side predictions.

---

## Part VIII — Modular structure and the Γ_0(6) closure (retracted to Class 2)

The 2026-04 round presented the closure of w_+ = 13/14 via
Hecke modular structure as its headline Class 5 result. That
status was retracted in 2026-08 (D1 disposition): w_+ = 13/14
is a numerical fit to Planck values — the fitting commit
(400f558) prints "0.000% (fit)" and the structural closure was
written 3h33m later — and no script in the repo computes it.
This part retains the modular walkthrough because the Γ_0(6)
and cusp machinery is genuine mathematics; the selection step
that lands on w_+ = 13/14 (L1, §8.6) is where the chain fails
to be a derivation.

### §8.1 — PSL(2, ℤ) Möbius action on P¹(ℚ)

The modular group PSL(2, ℤ) consists of 2 × 2 matrices with
integer entries and determinant 1, modulo the equivalence
M ~ -M. PSL(2, ℤ) acts on the projective line P¹(ℚ) (the
rationals plus the point at infinity) by Möbius transformations:

M = (a b; c d) acts on x via M(x) = (ax + b) / (cx + d)

The action of PSL(2, ℤ) on P¹(ℚ) is transitive (every two
points are related by some Möbius transformation). The
stabilizer of a point is a parabolic subgroup.

The mediant operation (§2.3) is implicitly a PSL(2, ℤ) action:
the mediant of a/b and c/d is generated by the matrix
(a c; b d) acting on the boundary fractions. Stern-Brocot tree
generation is therefore the iterated PSL(2, ℤ) action on
P¹(ℚ), starting from {0/1, 1/0}.

Per `lie_group_characterization.md` Step 3, the framework's
substrate has a PSL(2, ℤ) symmetry structure: any PSL(2, ℤ)
action that preserves the Farey graph automorphism preserves
the cross-ratio of every quadruple of points in P¹(ℚ). Cross-
ratios are projective invariants and are framework-natural
quantities (as the cross-ratio investigation of w_+ in
`omega_b_w_plus_cross_ratio_search.md` showed).

### §8.2 — Hecke congruence subgroups Γ_0(N)

The Hecke congruence subgroup Γ_0(N) ⊂ PSL(2, ℤ) consists of
matrices M = (a b; c d) with c ≡ 0 (mod N). It is a subgroup
of PSL(2, ℤ) of finite index; the index is N · ∏_{p|N} (1 + 1/p).

For small N:
- Γ_0(2) has index 3 in PSL(2, ℤ); 2 cusps on the modular
  curve X_0(2)
- Γ_0(3) has index 4; 2 cusps on X_0(3)
- Γ_0(6) has index 12; 4 cusps on X_0(6)

Γ_0(6) = Γ_0(2) ∩ Γ_0(3) is the intersection of Γ_0(2) and
Γ_0(3) by elementary modular group theory (since 6 = 2 · 3 and
gcd(2, 3) = 1). This identity is significant: it means
preserving Γ_0(6) is exactly preserving both Γ_0(2) and Γ_0(3)
independently.

### §8.3 — X_0(6) cusp classification

The cusps of the modular curve X_0(N) are the Γ_0(N) orbits of
P¹(ℚ). They parametrize the boundary degenerations of the
moduli space of elliptic curves with Γ_0(N)-level structure.

For Γ_0(6) (squarefree N = 6), the four cusps are indexed by
divisors of 6: d ∈ {1, 2, 3, 6}. The cusp at d corresponds to
the orbit of rationals p/q with gcd(q, 6) = d (in lowest terms).
Specifically:

- Cusp ∞ (d = 1): orbit of rationals with denominator coprime
  to 6 (e.g., p/13, p/11, p/17 for p coprime to denominator)
- Cusp 1/2 (d = 2): orbit of rationals with denominator
  divisible by 2 but not by 3 (e.g., p/2, p/4, p/14, p/16)
- Cusp 1/3 (d = 3): orbit of rationals with denominator
  divisible by 3 but not by 2 (e.g., p/3, p/9, p/15, p/27)
- Cusp 0 (d = 6): orbit of rationals with denominator divisible
  by 6 (e.g., p/6, p/12, p/18)

This is computed in `psl2z_subgroup_orbits.py`. The cusp
classification is uniquely determined by the gcd of the
denominator with 6 = INTERACT, which is the framework's natural
substrate cardinality. The match between the cusp index and
the framework's INTERACT primitive is the load-bearing connection
between the substrate's Z_6 mode lattice and the modular
structure of X_0(6).

### §8.4 — Substrate preserves Γ_0(6) = Γ_0(2) ∩ Γ_0(3)

Per `psl2z_subgroup_phase_b.md` B1, the framework's substrate
preserves Γ_0(6). The argument has two parts:

First, the substrate preserves Γ_0(2). The Klein-antipodal Z_2
(the sym/antisym decomposition of §4.4) is the substrate's
preservation of the mod-2 structure of Z_6. Under any substrate
dynamics that preserves the sym/antisym distinction (which is
all of them, per the framework's existing derivations using
the Z_2 rep machinery), the substrate preserves the Hecke level
2.

Second, the substrate preserves Γ_0(3). The color triplet Z_3
(the gauge-color sector of §4.3) is the substrate's preservation
of the mod-3 structure of Z_6. Color preservation is a gauge-
locality requirement; the substrate dynamics doesn't transition
color states into non-color sectors. This preserves Γ_0(3).

Third, by Γ_0(6) = Γ_0(2) ∩ Γ_0(3), the substrate preserves
Γ_0(6).

This is a recognize-mode argument: the framework's existing q_2
× q_3 sector decomposition (already Class 5 in `klein_antipodal_z2_rep_pattern.md`)
is exactly the modular-curve restatement of Γ_0(6) preservation.
No new substrate primitive is required; the substrate's natural
mode-counting on Z_6 = Z_2 × Z_3 corresponds to the cusp
structure of X_0(6) at level INTERACT.

### §8.5 — ψ_+(1, 5) inhabits cusp 1/2

The boundary mode ψ_+(1, 5) is the trivial Z_2 representation
(sym, Klein-singlet) on the boundary {1, 5} of the substrate.
Per `psl2z_subgroup_phase_b.md` B2, the trivial Z_2 rep on the
substrate corresponds to the cusp 1/2 of X_0(6).

The argument: the cusps of X_0(6) classify how a mode "factors
through" the Z_2 and Z_3 reductions. At cusp ∞ (d = 1), no
factor is "active" — the mode has neither q_2 nor q_3
structure. At cusp 1/2 (d = 2), the q_2 reduction is "active"
— the mode has a q_2-flavored factor in its denominator. At
cusp 1/3 (d = 3), the q_3 reduction is "active." At cusp 0
(d = 6), both are active.

The boundary mode ψ_+(1, 5) is in the q_2 sector (the sym
Klein-singlet, which is a Z_2 representation), so it inhabits
the cusp 1/2 of X_0(6). This is a Hecke-cusp identification of
the substrate's mode, derived from group theory + modular forms,
independent of the EM-MOND reading.

The independence matters because the EM-MOND reading
(`omega_b_alpha_beta_closure.md`) uses the same q_2-sector
identification ("EM coupling = q_2 sector"); the cusp
identification is parallel but routed through pure modular
structure, avoiding circularity.

### §8.6 — L1: substrate ground state at cusp 1/2

The cusp 1/2 of Γ_0(6) is an infinite orbit. At denominator q
(with gcd(q, 6) = 2), the orbit contains the discrete
representatives {1/q, 3/q, 5/q, ..., (q-1)/q} (the rationals in
the orbit at that denominator, with numerators coprime to q).

The substrate at K < 1 is discrete (Part VI, §6.6). Its
accessible weights at cusp 1/2 with denominator q are exactly
this discrete set. The substrate's ground state is the weight
that minimizes the energy functional.

Per `L1_substrate_cusp_ground_state.md`, the energy functional
is the MOND-threshold partial-locking energy. Five composing
results (C1-C5):

- C1: MOND threshold is a smooth curve (per `a0_threshold.md`,
  `kam_bridge_synthesis.md`)
- C2: EM coupling drives lock-in toward w → 1 (per
  `baryon_fraction.md` sym/antisym contrast: antisym has no EM
  and locks at w_- = 1, so EM-only would give w → 1 absent
  threshold suppression)
- C3: Substrate is discrete at K < 1 (per
  `denomination_boundary.md` §134)
- C4: Substrate states ARE the grain (corollary of C3)
- C5: Energy minimum on grain = closest-discrete to continuum
  minimum, under local linearity (the energy functional's
  curvature scale exceeds the grain spacing)

L1.a (continuum minimum at w → 1) follows from C1 + C2.
L1.b (closest-discrete quantization rule) follows from C3 + C4
+ C5.

L1 closes: the substrate's ground state at cusp 1/2 with
denominator q is

w_ground(q) = (q - 1) / q

— the closest-to-1 discrete representative.

Conceptually, the substrate's discreteness IS the operational
apparatus for the soft MOND boundary. In pure continuum, "where
is w_+?" has no operational answer (the threshold is smooth,
not sharp). The substrate's grain provides the resolution: the
substrate is at THIS specific grain state, the one minimizing
the continuum energy among the discrete options. The continuum
energy minimum at w → 1 (driven by EM lock-in) selects the
grain state closest to 1, which is (q-1)/q. Local linearity
(smooth E with curvature exceeding grain spacing) ensures this
selection is unique.

### §8.7 — w_+ = 13/14: complete two-component closure

The matter sector's denominator q at cusp 1/2 is determined by
the substrate's mode count for the matter sector. Per
`partition_logit_form.md` and the closed form M_i = (|F_7| -
N_i) / q_2 from §7.4-7.5, the matter sector's q_3-quantity is

M_DM = (|F_7| - MEDIANT) / q_2 = (19 - 5) / 2 = 7

The cusp 1/2 grain at the matter sector has q = q_2 · M_DM =
2 · 7 = 14.

By L1 (§8.6), the substrate ground state at q = 14 is

w_+ = (14 - 1) / 14 = 13 / 14

The chain as presented in 2026-04, with current statuses:

1. T1: Z_6 + Klein → partition (13:5:1)/19 (bare partition —
   a reference, not a prediction; `baryon_fraction.md`)
2. T2: M_i = (|F_7| - N_i)/q_2 → q_3-quantities (3, 7, 9)
   (algebra)
3. T3: ψ_-(1, 5) sign-rep no-EM ⟹ w_- = 1 (structural)
4. T4: ψ_+(1, 5) trivial Klein, EM-coupled, partial-locks at
   w_+ (structural; the *value* of w_+ is not fixed here)
5. T5: Substrate preserves Γ_0(6) = Γ_0(2) ∩ Γ_0(3) (§8.4)
6. T6: ψ_+(1, 5) trivial q_2 rep ↔ cusp 1/2 of X_0(6) (§8.5)
7. T7: Substrate at K < 1 is discrete; cusp-1/2 grain at q is
   1/q (§6.6)
8. L1: Substrate ground state at cusp 1/2 = (q-1)/q — the
   selection step. Retracted: written after the fitted value,
   overruling the repo's own Class-2 self-audit; it selects
   the number the fit had already produced.

Composition therefore yields Class 2 (observation-fitted), not
Class 5. Numerical realization at w_+ = 13/14:

| Observable | Predicted | Observed | Residual |
|---|---|---|---|
| Ω_b | 13/264 = 0.04924 | 0.04930 | by construction of the fit |
| Ω_DM | 35/132 = 0.26515 | 0.26500 | by construction of the fit |
| Ω_Λ | 181/264 = 0.68561 | 0.68470 | by construction of the fit |

The sub-σ residuals are inherited from the fit, not evidence
for the selection step. The canonical substrate-side object is
the bare partition 13:5:1/19 — a reference, not a prediction
(D1 disposition; MANIFEST scorecard).

---

## Part IX — Particle physics derivations

This part presents the framework's particle-physics derivations:
the SM gauge group, anomaly cancellation, the strong CP angle,
the down-type and up-type quark factors, and the bare K = 1
identities for the EW / Higgs sector.

### §9.1 — SM gauge group SU(3) × SU(2) × U(1) (conditional)

The framework reads the Standard Model gauge group off the
substrate's q_3 (color triplet → SU(3)), q_2 (Klein-antipodal
→ SU(2)), and U(1) hypercharge (derivation chain D41, D42).
The claim is conditional, retracted from Class 5 in 2026-08:
the 12-transition count consumes the 4-mode roster, which
rests on the conjectured XOR fraction-parity translation
(`xor_derivation.md` §5). If that translation is proven, the
group reading follows; until then the specific group is
conditional on an unsettled premise, and the strongest
independent leg is Yang-Mills uniqueness via Utiyama + Cartan
given the substrate's kinematics (`gauge_sector_lovelock.md`).

### §9.2 — Anomaly cancellation as substrate identities

The Standard Model has six anomaly-cancellation conditions for
gauge anomalies. Each requires the sum of certain charges over
all fermions to vanish. In standard physics, the cancellation
is a constraint on the matter content; the SM's specific matter
content (with three generations) is "lucky" to satisfy all six
conditions.

Per derivation chain D41, the framework verifies these
conditions as identities — for the imported charge assignment:
D41 hardcodes the SM hypercharges rather than deriving them
(retracted from "substrate identity" status, 2026-08). The
computation confirms that the standard assignment cancels all
six anomalies (a true, standard fact); it does not explain why
the substrate selects that assignment. Gell-Mann–Nishijima
holds with Y back-solved from the known charges, not derived
(`gell_mann_nishijima.md`).

### §9.3 — Strong CP θ = 0 from substrate symmetry

The Standard Model has a free parameter θ in the QCD Lagrangian
that is observationally constrained to |θ| < 10⁻¹⁰ but is
naturally O(1) in absence of fine-tuning. This is the strong CP
problem; standard solutions invoke a Peccei-Quinn axion or
other mechanism to dynamically suppress θ.

Per derivation chain D45, the framework proposes θ = 0 exactly
from Pin⁺(3) topology. The claim is conditional, retracted
from Class 5 in 2026-08: the derivation runs entirely on the
K² configuration space, whose selection is an unsettled
premise (`klein_bottle_derivation.md`), and the
eta-invariant-vanishing step is an unverified import
(`coupling_scales.md` Part V). If those premises hold, the
substrate admits no θ-term and strong CP dissolves with no
axion and no tuning; any measurement of θ ≠ 0 falsifies the
chain outright.

### §9.4 — Down-type quark factor 6 from S_3 orbits

Per `down_type_double_cover_closed.md`, the ratio of down-type
to lepton base-pair exponents is

a_1(down)² / a_1(lep)² = q_2 · q_3 = 6

The derivation uses S_3 acting on the Z_2 × Z_3 lattice (the
substrate's mode space). The S_3 group has orbit dimensions
{1, 3} = {q_3-trivial, q_3-vector} on the lattice; the factor
6 emerges as |L| = q_2 · q_3 from orbit-counting.

Numerical comparison (using PDG 2024 data for down-type quark
masses): the predicted factor 6 matches observation to 0.04σ.

This is a five-digit match using only the framework integers
q_2 and q_3, with no fitted parameters. Z1-Z3 status: pass.
Class: Survives.

### §9.5 — Up-type quark factor 9 = K_LEPTON

Per `item12_K_star_closure.py`, the up-type quark closure gives

a_1(up) · K_STAR = √N_up = q_3 = 3

where N_up = q_3² = 9 = K_LEPTON. The Klein parity -1 on
Fibonacci shift applied to matter modes gives the q_3² factor
structurally.

Numerical comparison: matches to 0.34σ vs PDG (m_c-dominated
uncertainty). Z1-Z3 status: pass. Class: Survives.

### §9.6 — Generations and the q_3 = 3 framework

The Standard Model has three generations of quarks and leptons.
The framework identifies q_3 = 3 with the spatial dimension
(§5.1) and with the color triplet (§4.3); per the framework's
derivation, the generation count is also q_3 = 3, since the
substrate's natural triplet structure manifests as the
generation triplet.

This identification is not as fully developed as the spatial-
dimension or color-triplet derivations; the generation triplet
appears in framework derivations but isn't always uniquely
forced from substrate structure (some inputs are required to
distinguish generations from other triplet structures).

### §9.7 — Bare K = 1 identities (Higgs sector)

The framework has bare K = 1 identities for the Higgs sector
(`bare_k1_identities.md`):

- m_H / v = 1/q_2 = 1/2 = 0.5 (observed at M_Z: 0.5087, 1.7%
  off)
- λ_Higgs = 1/q_2³ = 1/8 = 0.125 (observed: ~0.129, 3.4% off)
- α_s / α_2 = q_3³ / q_2³ = 27/8 = 3.375 (observed: 3.488,
  3.2% off)
- sin²θ_W = q_2³ / (q_2³ + q_3³) = 8/35 = 0.22857 (observed:
  0.23121, 1.1% off)
- 1/α_em (tree) = q_2³ + q_3³ = 35 (observed at M_Z: 127.95,
  factor 3.7 off)

These are explicitly not predictions at M_Z. The framework does
not currently supply the running mechanism from K = 1 to M_Z;
the bare values are reference identities, and the M_Z values
require RG running that the framework hasn't derived.

Per Region C Phase B's pigeonhole verdict
(`numerology_count_phase_b.md`), the multi-percent matches
between bare K = 1 values and M_Z observations are within the
expected pigeonhole density of small framework-integer
expressions; they are Class 2 / pigeonhole, not Class 5
structural claims.

The framework's honest position: the bare K = 1 identities are
suggestive, but the lack of a derived running prevents
structural claims at M_Z. This is one of the framework's
acknowledged gaps (not a structural failure but a derivational
incompleteness).

---

## Part X — Methodological framework

The framework's methodological discipline is a substantive
contribution alongside its quantitative predictions. The Z1-Z3
discipline (§10.1) distinguishes structural derivations from
numerology. The substrate-side versus anchor-side distinction
(§10.2) identifies what the framework can and cannot predict.
The two-anchor minimum (§10.3) is the framework's explicit
input requirement. The recognize / derive / eliminate modes
(§10.4) characterize productive work. The pigeonhole calibration
(§10.5) sets the discriminator's strictness. The vocabulary-is-
the-work pattern (§10.6) catalogs recurring closure structures.

### §10.1 — Z1-Z3 discipline

Per `statistical_conventions.md`, the framework uses three
criteria to evaluate a candidate prediction:

- **Z1**: numerical match within 1σ of the observed value
- **Z2**: no fitted O(1) factors (the prediction isn't of the
  form "framework integer × fitted_factor ≈ observation")
- **Z3**: only structural inputs (no anchor imports for
  dimensionless ratios)

A prediction passing all three is Class 5 / Survives. Predictions
passing Z1 but failing Z2 are Class 2 / numerology. The
discipline is enforced uniformly: predictions are individually
classified, and the framework does not claim "zero free
parameters" globally (the phrase is retired across the
repository); instead, individual predictions carry their Z1-Z3
status.

The discipline is significant because it prevents the framework
from accumulating numerology coincidences. Every claimed
structural prediction has explicit pass/fail status against
each criterion, and the criteria are applied to all candidate
predictions without exception.

### §10.2 — Substrate-side versus anchor-side

The framework distinguishes two categories of physical content:

- **Substrate-side**: dimensionless ratios and structural
  predictions native to the discrete substrate. Examples:
  Ω_Λ / Ω_DM = 13/5, Born rule exponent = 2, gauge group
  SU(3) × SU(2) × U(1), Klein-monodromy of antisym mode = -1.
- **Anchor-side**: absolute dimensional scales requiring
  observational input. Examples: the value of H_0 in km/s/Mpc,
  v_EW in GeV, the absolute Hubble during inflation H_inf, the
  absolute slow-roll parameter ε.

The framework predicts substrate-side quantities from primitives
without anchor input; anchor-side quantities require explicit
observational anchor (typically H_0 for cosmology, v_EW for
particle physics). The distinction is not a limitation of the
current framework state; it is a structural feature (per the
two-anchor minimum, §10.3).

The Instance 7 closure for A_s applies this distinction: the
substrate-side prediction A_s_substrate = 2.33 × 10⁻⁹ is
complete; the conversion to A_s_obs requires the inflation
amplification factor f_amp, which depends on H_inf and ε
(both anchor-side). The 11% gap is therefore the substrate / 
observable category boundary, not a derivation gap.

### §10.3 — The two-anchor minimum

Per `anchor_count_audit.md`, the framework requires two
independent observational anchors:

- H_0 (cosmological): covers Λ, ℓ_P, t_P, M_P, ρ_crit, and
  cosmic-timeline scales
- v_EW (particle): covers absolute particle masses, ℏ, c, G
  in absolute units, m_H

Per the D.3 closure (`path_closures_iter3.md`), the two-anchor
minimum is structural rather than a derivation gap. The K = 1
versus K < 1 sector decoupling (Part VI, §6.3) is non-smooth;
each regime requires its own anchor scale. The framework's
substrate cannot bridge the two regimes smoothly, so a single
anchor cannot cover both sectors.

This is consistent with the framework's "vocabulary-is-the-
work" pattern (§10.6): the SM-style hierarchy "problem" framing
(why is v_EW << M_P?) doesn't translate to the framework, which
correctly treats the two scales as independent inputs.

### §10.4 — Recognize, derive, eliminate

The framework distinguishes three productive work modes:

- **Recognize**: articulation of existing structural content as
  forcing arguments. Many of the 2026-04 round's Class 5
  closures (D.3, D.1, Ω_b α/β, Direction 4 Phase A/B, L1) close
  in recognize mode by composing existing framework results
  rather than deriving new content.
- **Derive**: new substrate-side derivation of structural
  content not previously articulated. Less common in mature
  closures but essential for new structural claims.
- **Eliminate**: showing a candidate is null or category-
  mismatched. Examples: Klein nodal parity simulator confirmed
  Y² Z_2-symmetric for all ℓ (`klein_nodal_parity.md`); the
  K_c-residual residual dissolved when K_c was correctly
  identified as 0 for identical oscillators (Instance 4).

The honest-landing-loop diagnostic (`klein_bridge_audit_and_probe.md`)
identified that single-session probes converge on Class 4-mechanism
/ Class 2-parameter shape because the discriminator is more
discriminating than the closures. The recognize mode breaks the
loop by composing existing content; the derive mode produces
new content but is harder to land in a single session; the
eliminate mode rules out non-content.

### §10.5 — Pigeonhole calibration (Region C verdict)

Per `numerology_count_phase_b.md`, the framework's Region C
Phase B count tested whether the framework's near-match cloud
(framework integer expressions matching observables within 1-3%)
is statistical pigeonhole or anomalously dense.

The count enumerated 2386 framework-integer expressions in the
range [10⁻³, 10³] and matched against 33 physical observables.
A permutation null (10⁴ trials, log-uniform sampling) gave:

| Threshold | Actual | Null mean ± std | p (null ≥ actual) |
|---|---|---|---|
| 0.1% | 13/33 | 9.51 ± 2.62 | 0.127 |
| 1.0% | 26/33 | 23.26 ± 2.59 | 0.199 |
| 3.0% | 31/33 | 27.49 ± 2.10 | 0.066 |

At α = 0.05, all three thresholds are consistent with the null:
the framework's near-match cloud is statistical pigeonhole, not
signal. The discriminator (`ansatz_audit_policy.md` Step 4
Class 2 default for multi-candidate ansatz) is correctly
calibrated; further closure attempts via near-match enumeration
are expected to land Class 2 by construction.

This calibration is significant for the framework's discipline.
Without it, the framework would have a temptation to chase
multi-percent matches as evidence of structural content; with
it, the framework correctly demotes them and concentrates
structural work on substrate-derivable content (group reps,
modular Hecke structure, sign-rep monodromy) where the recent
Class 5 closures live.

### §10.6 — The vocabulary-is-the-work pattern

Per `vocabulary_is_the_work_pattern.md`, a recurring closure
structure in the framework is: an apparent open obstruction
dissolves when the correct framework-internal vocabulary is
identified. Nine instances are catalogued:

1. Down-type S_3 orbit dimensions
2. Mass sector q = 2 coordinate convention
3. Omega_b cross-sector |r|² interpretation
4. K-zoo (K_c versus K_STAR confusion)
5. Discrete time versus algebraic time
6. SM hierarchy problem (doesn't translate)
7. A_s G1 horizon-crossing amplification (Instance 7, accepted)
8. Ω_b (α, β) parameters (sign-rep no-EM forces w_- = 1)
9. Modular-forms vocabulary for q_2 × q_3 sector taxonomy

Each instance follows the same pattern: setup (apparent
problem), disambiguation (the imported framing maps to no
framework object or to multiple objects ambiguously),
resolution (the correct framework-internal restatement either
dissolves the problem or sharpens it into a different question).

The pattern is structural rather than ad hoc: it characterizes
the recurring relationship between standard physics framings and
the framework's internal vocabulary. Many "open problems" of
standard physics, when restated in framework vocabulary, either
dissolve (hierarchy problem, K_c residual, discrete time) or
map onto well-defined framework-internal quantities that have
existing closures (down-type factor 6, A_s_substrate).

---

## Part XI — Synthesis and non-claims

This final part synthesizes what the framework provides, states
explicitly what it does not claim, maps to standard physics
open problems, and identifies open extensions.

### §11.1 — What the framework provides

The framework provides a constructive treatment of
dimensionless cosmological and particle-physics ratios from
four primitives. Statuses below are current (post-2026-08
correction campaign; forensics in ERRATA.md):

- **Cosmic partition**: the bare partition
  Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19 is the canonical
  substrate-side object — a reference, not a prediction (the
  same partition puts Ω_b 6.7% from observation). The
  two-component refinement (w_+ = 13/14; 181 : 70 : 13 / 264)
  is Class 2: w_+ is a numerical fit and its sub-percent
  residuals hold by construction of the fit
- **Cosmic hierarchy** R = 6 · 13⁵⁴ at 0.48% on observed Planck/
  Hubble ratio
- **Cosmological constant** Λ · ℓ_P² = 13⁻¹⁰⁸/12 at 0.1% in
  exponent on observed value (constructive solution to the CC
  problem)
- **Spectral tilt** n_s ≈ 0.963-0.966 at < 0.2% on Planck 2018
- **Substrate-side scalar amplitude** A_s_substrate = 2.33 × 10⁻⁹
  (complete substrate-side prediction; observable requires
  anchor-side amplification per Instance 7)
- **MOND scale** a_0 = c · H_0 / (2π√g*) = 1.25 × 10⁻¹⁰ m/s² at
  4% on Lelli et al. 2017 RAR (g*-corrected; bare c·H_0/(2π) = 1.04 × 10⁻¹⁰)
- **Spatial dimension** = 3 (open — completion step undefined;
  D2 demotion)
- **Lorentz symmetry** = Spin(3,1) (open — inherits the d = 3
  break; the covering theorem itself is a true import)
- **Born rule** exponent = 2 (exact, from saddle-node parabola)
- **SM gauge group** SU(3) × SU(2) × U(1) (conditional on the
  conjectured XOR parity translation)
- **Strong CP** θ = 0 (conditional on the K² configuration-
  space selection + eta-invariant import)
- **SM anomaly cancellation** all 6 conditions = 0 (verified
  for the imported charge assignment; charges not derived)
- **Down-type quark factor** 6 = q_2 · q_3 (0.04σ on PDG)
- **Up-type quark factor** 9 = q_3² (0.34σ on PDG)
- **Two-anchor minimum** (H_0 + v_EW) is structural, not a gap
- **K = 1 ↔ K < 1 sector decoupling** (GR vs QM continuum
  limits) is non-smooth, forces independent anchors per sector
- **Klein π_1 sector assignment**: cosmological → no-twist,
  particle → twist, forced by Z_2 rep machinery

Plus methodological deliverables: Z1-Z3 discipline, substrate /
anchor-side distinction, two-anchor minimum as structural,
recognize / derive / eliminate modes, pigeonhole calibration,
vocabulary-is-the-work pattern (9 instances).

### §11.2 — What the framework explicitly does not claim

The framework correctly does not predict:

- Absolute H_0 in km/s/Mpc (cosmological anchor)
- Absolute v_EW in GeV (particle-sector anchor)
- Absolute particle masses in physical units (require v_EW)
- Absolute H_inf in physical units (anchor-side; covered by H_0)
- Slow-roll parameter ε in physical units (requires absolute
  time)
- Inflation amplification factor f_amp (requires H_inf + ε)
- A_s_obs = 2.10 × 10⁻⁹ (post-inflation observable; substrate
  predicts 2.33 × 10⁻⁹; gap is anchor-side per Instance 7)
- Ratios that would require primes outside {q_2, q_3} = {2, 3}
  support (per K-axis uniqueness probe; v/M_P ≈ 13⁻¹⁵ is
  anchor-side input, not a derivation gap)
- BSM physics not falling out of substrate structure (no
  predictions for proton decay, dark matter direct detection,
  WIMP cross-sections, etc., because these require additional
  substrate content not currently scoped)
- The SM hierarchy "problem" — translated to framework
  vocabulary, the imported framing requires naturalness +
  Wilsonian RG, neither of which apply to the discrete
  substrate
- Inflation dynamics, reheating, baryogenesis (out of scope at
  current substrate development)
- Higgs-sector running from K = 1 to M_Z (current bare K = 1
  identities are reference values, not predictions at M_Z)

These non-claims are not gaps to be closed; they are structural
features of the framework's two-anchor minimum and substrate /
anchor-side distinction. The framework's discipline (Z1-Z3 +
substrate / anchor) accounts for them explicitly.

### §11.3 — Standard physics problems addressed

The framework engages with several long-standing open problems
in standard physics:

- **Cosmological constant problem**: constructively resolved
  via Λ · ℓ_P² = 13⁻¹⁰⁸/12 derivation + dissolution of the
  imported "naturalness" framing (no Wilsonian RG → no
  quadratic divergences in the substrate)
- **Hierarchy problem (v << M_P)**: doesn't translate per
  Instance 6; v / M_P is anchor-side input
- **Strong CP problem**: θ = 0 proposed via Pin⁺(3) topology,
  conditional on unsettled premises; if they hold, no
  Peccei-Quinn axion required
- **GR-QM unification**: shared substrate, two non-smoothly
  separated continuum limits (K = 1 = Einstein, K < 1 =
  Schrödinger); structural rather than smooth interpolation
- **Galactic rotation without particulate dark matter**: MOND
  scale a_0 derived structurally; "dark matter" identified as
  substrate sector (sign-rep modes with Klein-monodromy -1, no
  EM coupling); the bare-partition abundance Ω_DM = 5/19 sits
  0.7% from Planck (a reference, not a prediction)
- **Origin of three generations**: q_3 = 3 (color triplet
  doubles as generation count in framework reading)
- **Origin of SM gauge group**: read off substrate Z_6 +
  Klein-antipodal Z_2 + color Z_3, conditional on the
  conjectured XOR parity translation
- **Born rule**: derived from saddle-node parabola (forced
  exponent 2)
- **Spatial dimension = 3**: open (both proposed routes break;
  D2 demotion)
- **Origin of cosmic Ω partition**: 13:5:1/19 from Z_6 mode-
  counting + Klein-singlet ∩ coprime-to-6 selection — a
  reference partition, not a prediction
- **EPR / Bell-inequality violation**: pieces present (Born
  rule + Z_2-pair conservation theorem + substrate non-locality
  on Stern-Brocot tree); the `Q mod 2` substrate-Z₂ piece is
  now standalone (`q_mod2_conservation_theorem.md`); the
  assembled EPR/Bell theorem still not articulated

For each of these, the framework provides either a constructive
derivation or a reframing that explains why the imported
problem framing doesn't apply. The framework's claim is not
that it solves all open problems but that the ones it engages
with are addressed within its declared scope.

### §11.4 — Open extensions

The framework's current scope leaves several open extensions:

- **Substrate-inflation derivation**: extending the k-Ω map to
  a depth → time map without H_0; would close the A_s observable
  prediction (currently anchor-side per Instance 7)
- **Higgs sector running from K = 1 to M_Z**: would convert the
  bare K = 1 identities (m_H/v = 1/2, λ_H = 1/8, sin²θ_W =
  8/35) into M_Z predictions; currently the framework
  acknowledges these as reference values
- **EPR theorem**: composition of Born rule + Z_2-pair
  conservation + substrate non-locality into an explicit
  Bell-inequality-violation theorem
- **BSM phenomenology**: predictions for specific BSM signatures
  (proton decay, dark matter direct detection, etc.) require
  substrate development beyond current scope
- **Neutrino sector**: framework has substantial neutrino
  content but absolute neutrino masses are anchor-side; specific
  oscillation parameters not all individually derived
- **CMB-S4 era predictions**: N_efolds = √5 / (2/57) ≈ 63.7
  (band [62, 66]) is a substrate-forced structural prediction
  (cadence closure: `k_of_t_residual_disposition.md`, PRs #178/#179);
  CMB-S4 / LiteBIRD observational test in ~2030 would confirm or
  falsify. (Supersedes the earlier n_s-anchored 61.3 ± 0.7.)

Alongside these extensions, the 2026-08 campaign left genuine
open problems inside the declared scope: the XOR fraction-parity
translation (which the gauge sector is conditional on), the
d = 3 / Lorentz completion, the K² configuration-space
selection, and a derivation of the Ω-partition weights that
would promote the bare reference to a prediction.

---

## Postlude — for the dissertation defense

The defense posture, stated honestly:

The framework provides a constructive treatment, from four
primitives (integers, mediant, fixed-point, parabola), of
dimensionless cosmological and particle-physics ratios that the
standard model treats as observational input. Where it engages
with classical "open problems", the current honest inventory
is: constructively resolved (cosmological constant magnitude,
Born rule, MOND scale), conditional on unsettled premises
(gauge structure, strong CP), open (spatial dimension, Lorentz,
the Ω partition as prediction), or shown to be category errors
of imported framings (hierarchy, sometimes CC) — with explicit
structural reasons in each case.

Anchor-side absolutes (H_0, v_EW, A_s_obs) are correctly
declined; this is a structural feature (two-anchor minimum,
D.3 closure), not a derivational gap.

The mathematics is standard. Stern-Brocot trees, Z_2 / Z_3
representation theory, PSL(2, ℤ) modular forms, Hecke cusps on
X_0(N), Arnold tongues, saddle-node bifurcation theory — all
well-vetted by the broader mathematics community. What is novel
is the composition: that these standard mathematical objects,
when assembled in the order this atlas presents, generate a
quantitative structure whose surviving Class 5 rows (the
cosmological-constant magnitude and hierarchy exponent, the
Born exponent, the MOND scale, the tilt) hold at their stated
residuals — while the retracted and conditional rows mark
exactly where composition outran derivation.

The framework's specific competitive claims versus the standard
model, at current statuses: derivation of the cosmological
constant magnitude and hierarchy exponent (Class 5); the Born
rule exponent from saddle-node universality (versus
postulation); prediction of the MOND scale from Λ (versus
separate fit); identification of dark matter as a substrate
sector (versus particle to be searched for); a conditional
route to the gauge group (pending the XOR translation); and a
bare cosmic-partition reference whose promotion to prediction
awaits a derivation of the weights.

What the framework does not compete with the standard model on:
inflation dynamics, reheating, baryogenesis (anchor-side, not
scoped); specific BSM phenomenology (no fits to LHC anomalies);
absolute particle masses (require v_EW input); detailed CMB
acoustic peak structure beyond the spectral tilt.

The framework's claim, defended honestly: it provides a
structural foundation that makes specific quantitative
predictions where comparable, dissolves several "problems" as
imported framings, and identifies its own anchor-side limits
explicitly. The next phase of work — the legitimacy phase —
involves communicating this position to the broader physics
community, which is a separate undertaking from establishing
the internal consistency that the 2026-04 round closed.

This atlas is the third deliverable of the legitimacy phase,
following the canonical glossary and the phenomenology cross-
reference. Together, they constitute the framework's first
external-facing presentation: vocabulary translation,
phenomenological comparison, and end-to-end derivation chain.
The framework's remaining homework is derivation as well as
communication: the conditional and open rows above name the
proofs still owed.

## Status

**Atlas edition 2, 2026-08-14** (v1: 2026-04-26). End-to-end
walkthrough from four primitives with statuses carried from the
2026-08 correction campaign. Class 5 rows: R, Λ·ℓ_P², n_s,
A_s_substrate, MOND a_0, Born rule, N_efolds cadence, down-type
factor 6, up-type factor 9, two-anchor minimum, sector
decoupling. Conditional: gauge group, anomaly cancellation
(imported charges), strong CP. Open: spatial dimension,
Lorentz. Reference (not prediction): the bare Ω partition;
two-component closure Class 2 (fitted). Authoritative registry:
MANIFEST.yml scorecard; forensics: ERRATA.md.

Companion to `canonical_glossary.md` (vocabulary translation)
and `phenomenology_cross_reference.md` (observation/prediction
comparison).

Maintenance: update when new closures land, observed values
shift significantly, or the underlying derivation chain
extends. The atlas's structure (11 parts) is stable; section-
level updates as substrate work progresses.

Side: presentation doc; no new derivation content. All
derivations cited live in their original source files and are
referenced here.
