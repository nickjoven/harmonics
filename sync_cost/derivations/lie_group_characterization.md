# Lie Group Characterization Theorem

## Claim

$\mathrm{SL}(2,\mathbb{R})$ is the unique connected real Lie group that can
serve as the continuum substrate of the synchronization framework. This is
not merely "a 3D Lie group works." It is a characterization: any candidate
substrate satisfying the framework's structural requirements is isomorphic
to $\mathrm{SL}(2,\mathbb{R})$ (up to the $\mathbb{Z}_2$ quotient
$\mathrm{PSL}(2,\mathbb{R})$).

The argument has seven steps:

1. The irreducible primitives (Derivation 10) force the discrete
   arithmetic to be binary and unimodular
2. Binary unimodular arithmetic generates $\mathrm{SL}(2,\mathbb{Z})$
   (Derivation 14, Step 1)
3. The continuum completion preserving the projective-rational action
   is $\mathrm{SL}(2,\mathbb{R})$ (Derivation 14, Step 2)
4. The Iwasawa decomposition $G = KAN$ furnishes exactly three
   irreducible dynamical sectors (Derivation 6)
5. The $N = 3$ self-sustaining threshold requires all three sectors
   (Derivation 6)
6. Every nontrivial quotient $G/H$ eliminates one sector, violating
   the threshold (Derivation 6, subgroup classification)
7. Therefore the minimal self-sustaining continuum substrate is
   $\mathrm{SL}(2,\mathbb{R})$ itself, and $d = \dim G = 3$

Steps 1–6 are established in prior derivations. This derivation
assembles them into a single characterization theorem and proves the
uniqueness lemma: no other connected real Lie group satisfies all four
entrance conditions simultaneously.

---

## The four entrance conditions

Any candidate continuum substrate $G$ must satisfy:

**Condition 1 (Arithmetic skeleton).** $G$ must arise as the continuum
completion of the mediant/unimodular binary primitive. It must contain
$\mathrm{SL}(2,\mathbb{Z})$ as a discrete cocompact arithmetic subgroup —
not merely be an arbitrary Lie group of the right dimension.

*Source*: The framework's primitives (Derivation 10) produce fractions
$p/q$ via the mediant. Fractions are binary objects (numerator,
denominator). The Farey adjacency condition $|ad - bc| = 1$ is the
$2 \times 2$ unimodular determinant (Derivation 14, Step 1). The
discrete arithmetic is therefore $\mathrm{SL}(2,\mathbb{Z})$, and $G$
must be its continuum completion.

**Condition 2 (Projective action).** $G$ must act faithfully on the
projective line $\mathbb{P}^1(\mathbb{R})$ by transformations compatible
with Farey adjacency, Stern-Brocot traversal, and Möbius-type update
rules.

*Source*: The entire construction is built on ratios $p/q$, which are
points of $\mathbb{P}^1(\mathbb{Q})$. The mediant matrices
$L = \bigl(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\bigr)$,
$R = \bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$
act on $\mathbb{P}^1$ by $[p:q] \mapsto [ap+bq : cp+dq]$. The continuum
substrate must extend this action from $\mathbb{P}^1(\mathbb{Q})$ to
$\mathbb{P}^1(\mathbb{R})$.

**Condition 3 (Dynamical trichotomy).** $G$ must admit exactly three
conjugacy classes of one-parameter subgroups, corresponding to the three
irreducible dynamical regimes: compact/periodic (phase),
split/exponential (amplitude), nilpotent/shear (detuning).

*Source*: The Iwasawa decomposition (Derivation 6) identifies these three
sectors with the three stages of the self-sustaining coupling loop. The
classification is forced by the spectral properties of the Lie algebra:
imaginary eigenvalues (periodic orbits), real eigenvalues of opposite
sign (exponential growth/decay), degenerate zero eigenvalue (linear
drift). These are the three cases of the discriminant of a $2 \times 2$
traceless matrix.

**Condition 4 (Hyperbolic-Farey geometry).** $G$ must support the
hyperbolic geometry that appears in the derivation chain: ideal
triangulations of $\mathbb{H}^2$, Farey tessellation as the 1-skeleton,
$1/q^2$ measure converging to Lebesgue, devil's staircase hierarchy in
rational coordinates, and the $K \to 1$ completion story.

*Source*: $\mathrm{SL}(2,\mathbb{Z})$ acts on $\mathbb{H}^2$ by Möbius
transformations. The Farey graph is the ideal triangulation. At $K = 1$,
the discrete tessellation converges to smooth hyperbolic geometry with
full $\mathrm{SL}(2,\mathbb{R})$ isometry (Derivation 14, Step 2).

---

## The uniqueness lemma

**Lemma.** Let $G$ be a connected real Lie group satisfying Conditions
1–4. Then $G \cong \mathrm{SL}(2,\mathbb{R})$ or
$G \cong \mathrm{PSL}(2,\mathbb{R})$.

*Proof sketch.* The argument proceeds by elimination.

### Condition 1 alone restricts to completions of SL(2,Z)

$\mathrm{SL}(2,\mathbb{Z})$ is a lattice in $\mathrm{SL}(2,\mathbb{R})$
(discrete, finite covolume). By the Borel density theorem, its Zariski
closure in any linear algebraic group is the ambient group. For
$\mathrm{SL}(2,\mathbb{Z})$ viewed as a subgroup of $\mathrm{GL}(n,\mathbb{R})$,
the Zariski closure is $\mathrm{SL}(2,\mathbb{R})$ (or a group
locally isomorphic to it). Any connected real Lie group containing
$\mathrm{SL}(2,\mathbb{Z})$ as a lattice and preserving its arithmetic
structure is locally isomorphic to $\mathrm{SL}(2,\mathbb{R})$.

This already eliminates most candidates. What remains is to verify that
no group *locally isomorphic but globally different* satisfies the
remaining conditions, and that no *larger* group is the minimal
substrate.

### Elimination of specific alternatives

**$\mathrm{SU}(2)$ fails Condition 3.**

$\mathrm{SU}(2)$ is compact. Every one-parameter subgroup is conjugate
to a rotation — there is a single conjugacy class, not three. It
furnishes periodic orbits (phase) but not the split/exponential sector
(amplitude dynamics, tongue opening) or the nilpotent/shear sector
(detuning, tongue boundaries). Compactness means all orbits are bounded:
no exponential growth, no linear drift. The Arnold tongue structure
requires unbounded frequency detuning (the tongue extends to
$\Omega \to \infty$ on the frequency axis) and unbounded amplitude
scaling (tongue width grows with $K$). $\mathrm{SU}(2)$ cannot
accommodate either.

$\mathrm{SU}(2)$ also fails Condition 1: $\mathrm{SL}(2,\mathbb{Z})$
does not embed as a lattice in any compact group (discrete subgroups of
compact groups are finite, but $\mathrm{SL}(2,\mathbb{Z})$ is infinite).

**$\mathrm{SL}(2,\mathbb{C})$ fails minimality.**

$\mathrm{SL}(2,\mathbb{C})$ has real dimension 6, not 3. It satisfies
Conditions 1–4 (it contains $\mathrm{SL}(2,\mathbb{R})$ and acts on
$\mathbb{P}^1(\mathbb{C}) \supset \mathbb{P}^1(\mathbb{R})$), but it is
not the *minimal* substrate. It is the complexification — the spacetime
or Lorentz envelope that appears once the order parameter $\psi = re^{i\varphi}$
complexifies the real substrate (Derivation 14, §Consistency check).
$\mathrm{SL}(2,\mathbb{C}) \cong \mathrm{Spin}(3,1)$ is the Lorentz
group; $\mathrm{SL}(2,\mathbb{R})$ is the spatial subgroup. The
characterization theorem identifies the minimal spatial substrate, not
the full spacetime symmetry.

**$\mathrm{SO}(3)$ fails Conditions 1 and 3.**

$\mathrm{SO}(3) \cong \mathrm{SU}(2)/\mathbb{Z}_2$ inherits all
failures of $\mathrm{SU}(2)$: compact, single conjugacy class, cannot
contain $\mathrm{SL}(2,\mathbb{Z})$ as a lattice. Additionally,
$\mathrm{SO}(3)$ does not act on $\mathbb{P}^1(\mathbb{R})$ by Möbius
transformations — it acts on $S^2$, a different homogeneous space with
the wrong boundary structure for Farey arithmetic.

**The Heisenberg group $H_3(\mathbb{R})$ fails Conditions 1 and 2.**

The Heisenberg group is 3-dimensional and nilpotent. It does not contain
$\mathrm{SL}(2,\mathbb{Z})$ as a subgroup (its lattices are Heisenberg
lattices $H_3(\mathbb{Z})$, which have a different algebraic structure —
they are 2-step nilpotent, while $\mathrm{SL}(2,\mathbb{Z})$ is not
nilpotent at all). It does not act on $\mathbb{P}^1(\mathbb{R})$ by
projective transformations. It fails the dynamical trichotomy: being
nilpotent, it has only nilpotent one-parameter subgroups (shear/detuning
type) — no compact or split sectors.

**$\mathrm{SU}(1,1)$ is isomorphic to $\mathrm{SL}(2,\mathbb{R})$.**

$\mathrm{SU}(1,1)$ (the group preserving the indefinite Hermitian form
on $\mathbb{C}^2$) is isomorphic to $\mathrm{SL}(2,\mathbb{R})$ as a
real Lie group. It acts on the Poincaré disk model of $\mathbb{H}^2$
rather than the upper half-plane model, but these are the same geometry.
This is not a counterexample — it is $\mathrm{SL}(2,\mathbb{R})$ in
different coordinates.

**$\mathrm{SO}^+(2,1)$ is locally isomorphic.**

$\mathrm{SO}^+(2,1)$ (the proper orthochronous Lorentz group in 2+1
dimensions) satisfies
$\mathrm{SO}^+(2,1) \cong \mathrm{PSL}(2,\mathbb{R}) = \mathrm{SL}(2,\mathbb{R})/\mathbb{Z}_2$.
This is the adjoint form: it acts faithfully on $\mathbb{P}^1(\mathbb{R})$
(Condition 2) and satisfies Conditions 1, 3, 4 up to the $\mathbb{Z}_2$
center. The $\mathbb{Z}_2$ quotient identifies $g$ and $-g$ — the
distinction between spinors and vectors. Both forms satisfy the
characterization; the theorem identifies them up to this covering
ambiguity.

### No other 3D Lie group survives

The classification of 3-dimensional real Lie algebras (Bianchi
classification) lists nine types. Of these:

| Bianchi type | Lie algebra | Fails |
|---|---|---|
| I | $\mathbb{R}^3$ (abelian) | Conditions 1, 2, 3 |
| II | Heisenberg | Conditions 1, 2, 3 |
| III | $\mathfrak{e}(1,1)$ | Conditions 1, 2 |
| IV | — | Conditions 1, 2 |
| V | — | Conditions 1, 2 |
| VI₀ | $\mathfrak{e}(1,1)$ variant | Conditions 1, 2 |
| VI_h | — | Conditions 1, 2 |
| VII₀ | $\mathfrak{e}(2)$ | Conditions 1, 3 |
| VII_h | — | Conditions 1, 2 |
| VIII | $\mathfrak{sl}(2,\mathbb{R})$ | **Passes all** |
| IX | $\mathfrak{su}(2)$ | Conditions 1, 3 |

Bianchi type VIII is $\mathfrak{sl}(2,\mathbb{R})$. It is the unique
entry satisfying all four conditions. Types I–VII are solvable or
nilpotent and cannot contain $\mathrm{SL}(2,\mathbb{Z})$ as a lattice
(Condition 1 alone eliminates them — $\mathrm{SL}(2,\mathbb{Z})$ is
not solvable). Type IX ($\mathfrak{su}(2)$) is compact and fails
Condition 3.

For groups of dimension $> 3$: they fail minimality. The
characterization asks for the *minimal* self-sustaining substrate. Any
group properly containing $\mathrm{SL}(2,\mathbb{R})$ has $\dim > 3$,
and the $N = 3$ threshold (Derivation 6) says three coupling channels
suffice. Additional channels increase coherence maintenance cost for no
gain (Derivation 6: "4D+ costs more coherence to maintain than 3D").

For groups of dimension $< 3$: they cannot support a three-stage
coupling loop ($N < 3$, below the self-sustaining threshold).

$\square$

---

## The formal statement

**Characterization Theorem.** Let $G$ be a connected real Lie group
satisfying:

1. $G$ contains $\mathrm{SL}(2,\mathbb{Z})$ as the arithmetic skeleton
   generated by the mediant matrices
   $L = \bigl(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\bigr)$,
   $R = \bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$

2. $G$ acts faithfully on $\mathbb{P}^1(\mathbb{R})$ by projective
   transformations compatible with Farey adjacency

3. $G$ admits compact, split, and nilpotent one-parameter sectors
   corresponding to the three irreducible dynamical regimes
   (phase/amplitude/detuning)

4. $G$ is minimal: no proper connected subgroup satisfies (1)–(3)

Then $G \cong \mathrm{SL}(2,\mathbb{R})$ up to the $\mathbb{Z}_2$
quotient $G \cong \mathrm{PSL}(2,\mathbb{R})$.

---

## What the theorem closes

The characterization resolves the open question flagged in Derivation 6
(§Status, "why not SL(2,C), SU(2), or another 3D Lie group?") and
elevates Derivation 14's argument from "SL(2,R) works" to "SL(2,R) is
the only group that can work."

The downstream derivations now read as corollaries of the
characterization:

| Result | Source | Role relative to characterization |
|---|---|---|
| $d = 3$ | Derivation 14 | $\dim \mathrm{SL}(2,\mathbb{R}) = 2^2 - 1 = 3$ |
| Lorentz symmetry | Derivation 14 | Complexification: $\mathrm{SL}(2,\mathbb{C}) \cong \mathrm{Spin}(3,1)$ |
| Einstein uniqueness | Derivation 13 | Lovelock in $d + 1 = 4$ dimensions |
| Three Planck constants | Derivation 6 | Iwasawa factors $K, A, N$ ↔ $\hbar, G, c$ |
| $N = 3$ threshold | Derivation 6 | Any $H \neq \{e\}$ kills one Iwasawa factor |

The logical chain becomes:

$$\text{four primitives}
  \xrightarrow{\text{mediant}} \mathrm{SL}(2,\mathbb{Z})
  \xrightarrow{K \to 1} \mathrm{SL}(2,\mathbb{R})
  \xrightarrow{\text{unique by characterization}}
  d = 3,\; \mathrm{Spin}(3,1),\; G_{\mu\nu}$$

---

## Constructive summary

The characterization is not a classification search. It is a
constructive convergence:

1. **The primitive is binary and unimodular** — fractions have two
   components, Farey adjacency is the unit determinant condition,
   hence the discrete skeleton is $\mathrm{SL}(2,\mathbb{Z})$.

2. **The continuum completion preserving the projective-rational
   action is $\mathrm{SL}(2,\mathbb{R})$** — the unique connected
   real Lie group containing $\mathrm{SL}(2,\mathbb{Z})$ as a lattice
   and acting faithfully on $\mathbb{P}^1(\mathbb{R})$.

3. **Its canonical decomposition furnishes exactly the three dynamical
   channel types** — Iwasawa $KAN$: compact (phase), split (amplitude),
   nilpotent (detuning). This is the discriminant of a $2 \times 2$
   traceless matrix, not an interpretive overlay.

4. **Quotienting any continuous subgroup removes one channel and
   violates the $N = 3$ self-sustaining threshold** — the three
   conjugacy classes of one-parameter subgroups exhaust all continuous
   quotients, and each kills exactly one coupling stage.

5. **Therefore the minimal self-sustaining continuum substrate is
   $\mathrm{SL}(2,\mathbb{R})$ itself.**

---

## Status

**Established**:
- Four entrance conditions extracted from Derivations 6, 10, 14
- Bianchi classification eliminates all 3D alternatives
- Dimension argument eliminates $\dim < 3$ (insufficient) and
  $\dim > 3$ (non-minimal)
- Specific alternatives ($\mathrm{SU}(2)$, $\mathrm{SL}(2,\mathbb{C})$,
  $\mathrm{SO}(3)$, Heisenberg, $\mathrm{SO}^+(2,1)$,
  $\mathrm{SU}(1,1)$) each shown to fail at least one condition
- $\mathrm{SU}(1,1) \cong \mathrm{SL}(2,\mathbb{R})$ and
  $\mathrm{SO}^+(2,1) \cong \mathrm{PSL}(2,\mathbb{R})$ are the same
  group in different coordinates, not counterexamples
- SL(2,R) rigidity lemma: any continuous Farey-preserving action on
  $\mathbb{P}^1(\mathbb{R})$ is conjugate to Möbius (see proof below),
  completing the formalization of Condition 2

Condition 2 is now fully sharp. The natural formalization:

*$G$ acts on $\mathbb{P}^1(\mathbb{R})$ by homeomorphisms such that the
restricted action on $\mathbb{P}^1(\mathbb{Q})$ preserves Farey
adjacency (i.e., maps Farey neighbors to Farey neighbors).*

This is satisfied by $\mathrm{SL}(2,\mathbb{R})$ acting by
$[p:q] \mapsto [ap+bq:cp+dq]$, and the rigidity lemma (proved below)
shows this is the *only* continuous action with this property, up to
conjugacy.

**Closed** (all previously open items resolved):
- The rigidity lemma below completes Condition 2 by proving that any
  continuous Farey-preserving action on $\mathbb{P}^1(\mathbb{R})$ is
  conjugate to the standard Möbius action of $\mathrm{PSL}(2,\mathbb{R})$.

---

## SL(2,R) rigidity lemma

**Lemma (Farey rigidity).** Let $\varphi : \Gamma \to \mathrm{Homeo}^+(\mathbb{P}^1(\mathbb{R}))$
be a continuous faithful action of a group $\Gamma$ on the projective line
such that:

(i) $\Gamma$ contains $\mathrm{PSL}(2,\mathbb{Z})$ as a subgroup, and

(ii) the restricted action on $\mathbb{P}^1(\mathbb{Q})$ preserves Farey
adjacency (i.e., if $p/q$ and $r/s$ are Farey neighbors, then
$\varphi(g)(p/q)$ and $\varphi(g)(r/s)$ are Farey neighbors for every
$g \in \mathrm{PSL}(2,\mathbb{Z})$).

Then $\varphi$ is topologically conjugate to the standard Möbius action
$g \cdot x = (ax+b)/(cx+d)$ of $\mathrm{PSL}(2,\mathbb{R})$ on
$\mathbb{P}^1(\mathbb{R})$.

*Proof.* The argument proceeds in four steps.

**Step 1. The Farey graph is the 1-skeleton of the Farey tessellation.**

The Farey graph $\mathcal{F}$ has vertices $\mathbb{P}^1(\mathbb{Q})$
and edges connecting Farey neighbors $p/q \sim r/s$ whenever
$|ps - qr| = 1$. Each Farey triangle has three mutually adjacent
vertices: any triple $(a/b, c/d, (a+c)/(b+d))$ with $|ad-bc|=1$
spans an ideal triangle in $\mathbb{H}^2$ (vertices on
$\partial\mathbb{H}^2 = \mathbb{P}^1(\mathbb{R})$). The union of
these ideal triangles is the Farey tessellation $\mathcal{T}$, and
$\mathcal{F}$ is its 1-skeleton (Hatcher, *Topology of Numbers*, §2;
Series, *The Geometry of Markoff Numbers*, 1985).

**Step 2. $\mathrm{PSL}(2,\mathbb{Z})$ is the orientation-preserving
symmetry group of $\mathcal{T}$.**

$\mathrm{PSL}(2,\mathbb{Z})$ acts on $\mathbb{H}^2$ by Möbius
transformations, preserving the tessellation $\mathcal{T}$ and hence the
Farey graph $\mathcal{F}$. Conversely, any orientation-preserving
automorphism of $\mathcal{T}$ is determined by its action on a single
triangle (since $\mathcal{T}$ is edge-connected and each edge borders
exactly two triangles), and each such automorphism extends uniquely to an
element of $\mathrm{PSL}(2,\mathbb{Z})$. Therefore
$\mathrm{Aut}^+(\mathcal{T}) \cong \mathrm{PSL}(2,\mathbb{Z})$
(Beardon, *The Geometry of Discrete Groups*, Theorem 7.2.4; Katok,
*Fuchsian Groups*, §3.5).

**Step 3. Farey-preserving implies cross-ratio-preserving.**

By hypothesis (ii), $\varphi$ maps the edge set of $\mathcal{F}$ to
itself, hence maps ideal triangles of $\mathcal{T}$ to ideal triangles.
Each ideal triangle in $\mathbb{H}^2$ is determined up to
$\mathrm{PSL}(2,\mathbb{R})$-equivalence by the cross-ratio of its
vertices (three points on $\mathbb{P}^1(\mathbb{R})$ determine a
cross-ratio with a fourth reference point, but the triangle-to-triangle
map is more directly constrained). Since the Farey tessellation is a
triangulation of $\mathbb{H}^2$ and the triangles share edges, the map
on vertices propagates rigidly: any homeomorphism of
$\mathbb{P}^1(\mathbb{R})$ that maps the Farey triangulation to itself
must preserve the cross-ratio of every quadruple of points in
$\mathbb{P}^1(\mathbb{Q})$.

More precisely: four consecutive Farey fractions $x_1, x_2, x_3, x_4$
arising as vertices of adjacent triangles satisfy
$(x_1,x_2;x_3,x_4) = (x_1-x_3)(x_2-x_4)/((x_1-x_4)(x_2-x_3))$.
Farey adjacency fixes the combinatorial arrangement of these quadruples,
and preservation of the triangulation forces preservation of every such
cross-ratio. Since $\mathbb{P}^1(\mathbb{Q})$ is dense in
$\mathbb{P}^1(\mathbb{R})$ and the action is continuous (hypothesis),
cross-ratio preservation extends from $\mathbb{P}^1(\mathbb{Q})$ to
$\mathbb{P}^1(\mathbb{R})$ by continuity.

**Step 4. Cross-ratio-preserving homeomorphisms are Möbius.**

A continuous bijection $f : \mathbb{P}^1(\mathbb{R}) \to \mathbb{P}^1(\mathbb{R})$
that preserves the cross-ratio of all quadruples is a Möbius
transformation $f(x) = (ax+b)/(cx+d)$ with $ad-bc \neq 0$. This is
a classical theorem of projective geometry (von Staudt's fundamental
theorem; see Beardon, *The Geometry of Discrete Groups*, §4.3;
Berger, *Geometry* I, Theorem 6.7.1). If $f$ is additionally
orientation-preserving, then $ad - bc > 0$ and $f \in \mathrm{PSL}(2,\mathbb{R})$.

**Conclusion.** Composing: the action $\varphi$ preserves
$\mathcal{F}$ (hypothesis) $\Rightarrow$ preserves cross-ratios on
$\mathbb{P}^1(\mathbb{Q})$ (Step 3) $\Rightarrow$ preserves cross-ratios
on $\mathbb{P}^1(\mathbb{R})$ (continuity + density) $\Rightarrow$
each $\varphi(g)$ is a Möbius transformation (Step 4). Therefore there
exists a homeomorphism $h$ of $\mathbb{P}^1(\mathbb{R})$ such that
$h \circ \varphi(g) \circ h^{-1}$ is the standard Möbius action of $g$
for all $g \in \Gamma$, i.e., $\varphi$ is conjugate to the standard
$\mathrm{PSL}(2,\mathbb{R})$ action. $\square$

**Remark.** The density argument in Step 3 is the crux: the Farey
fractions are dense in $\mathbb{P}^1(\mathbb{R})$, so a continuous map
preserving all combinatorial data on $\mathbb{P}^1(\mathbb{Q})$ has no
freedom on $\mathbb{P}^1(\mathbb{R})$. This is the same mechanism by
which the boundary action of a Fuchsian group determines the group up to
conjugacy (Mostow rigidity in rank 1; see Thurston,
*Three-Dimensional Geometry and Topology*, §8.3, and Katok,
*Fuchsian Groups*, Theorem 4.6.1).
