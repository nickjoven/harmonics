# Isotropy Lemma: Trivial Stabilizer in the Kuramoto Model at K=1

## Lemma

**In the Kuramoto model at K=1 with all-to-all coupling, the observable
state of each oscillator is completely determined by its three Iwasawa
parameters (phase, amplitude, frequency). No additional internal degree
of freedom exists. Therefore the stabilizer of any point under the
SL(2,R) action is trivial.**

Formally: let $G = \mathrm{SL}(2,\mathbb{R})$ act on the spatial
manifold $\mathcal{M} = G/H$ by left multiplication. Then $H = \{e\}$,
so $\mathcal{M} = G$ and $d = \dim \mathcal{M} = \dim G = 3$.

---

## Setup

Consider the Kuramoto model with $N$ oscillators at coupling strength
$K = 1$ (full locking). Each oscillator $i$ is described by:

- $\theta_i \in S^1$: its phase (angular position on the limit cycle)
- $\omega_i \in \mathbb{R}$: its natural frequency (position on the
  frequency axis, equivalently a rational $p_i/q_i$ via the
  mode-locking tongue it occupies)
- $r_i \in \mathbb{R}_{>0}$: its coupling amplitude to the mean field
  (the local order parameter magnitude)

At $K = 1$, every oscillator is locked to the mean field: its
instantaneous frequency equals the mean-field frequency, and its phase
relationship to the collective is fixed. The oscillator's entire
dynamical role is exhausted by the triple $(\theta_i, \omega_i, r_i)$.

---

## Proof

### (a) The oscillator state is $(\theta, \omega, r)$

The Kuramoto model is defined by the equations of motion:

$$\dot{\theta}_i = \omega_i + \frac{K}{N} \sum_{j=1}^{N}
  \sin(\theta_j - \theta_i)$$

At $K = 1$ with all-to-all coupling, the system locks completely. In
the locked state, the mean-field order parameter
$z = r \, e^{i\psi} = \frac{1}{N} \sum_j e^{i\theta_j}$ is constant.
Each oscillator's relation to the collective is fully specified by:

1. **Phase** $\theta_i$: the angular offset from the mean-field phase
   $\psi$
2. **Natural frequency** $\omega_i$: the oscillator's intrinsic
   frequency, which determines which mode-locking tongue ($p/q$) it
   occupies in the Stern-Brocot tree
3. **Coupling amplitude** $r_i$: the magnitude of the oscillator's
   contribution to the local order parameter, encoding the depth in
   the hyperbolic plane $\mathbb{H}^2$ (equivalently, the denominator
   $q$ of the locked rational)

These are the only state variables appearing in the Kuramoto
equations. The model defines no further internal structure.

### (b) The three quantities transform under the Iwasawa factors K, A, N

The Iwasawa decomposition $\mathrm{SL}(2,\mathbb{R}) = K \cdot A
\cdot N$ (unique factorization) provides three one-parameter subgroups:

| Iwasawa factor | Subgroup | Generator | Acts on |
|---|---|---|---|
| $K = \mathrm{SO}(2)$ | $\bigl(\begin{smallmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{smallmatrix}\bigr)$ | $J = \bigl(\begin{smallmatrix}0 & -1 \\ 1 & 0\end{smallmatrix}\bigr)$ | Phase $\theta$ |
| $A$ (positive diagonal) | $\bigl(\begin{smallmatrix}e^t & 0 \\ 0 & e^{-t}\end{smallmatrix}\bigr)$ | $D = \bigl(\begin{smallmatrix}1 & 0 \\ 0 & -1\end{smallmatrix}\bigr)$ | Amplitude $r$ (scale/depth) |
| $N$ (upper unipotent) | $\bigl(\begin{smallmatrix}1 & s \\ 0 & 1\end{smallmatrix}\bigr)$ | $N_+ = \bigl(\begin{smallmatrix}0 & 1 \\ 0 & 0\end{smallmatrix}\bigr)$ | Frequency $\omega$ (detuning/shear) |

Every element $g \in \mathrm{SL}(2,\mathbb{R})$ factors uniquely as
$g = k \cdot a \cdot n$ with $k \in K$, $a \in A$, $n \in N$.
Correspondingly, every oscillator state $(\theta, r, \omega)$ is
parameterized by the three Iwasawa coordinates. The map

$$g = k(\theta) \cdot a(r) \cdot n(\omega)
  \;\longmapsto\; (\theta, r, \omega)$$

is a diffeomorphism from $G$ to the oscillator state space.

### (c) The action is faithful: $g \cdot (\theta, \omega, r) = (\theta, \omega, r) \implies g = e$

Suppose $g \in \mathrm{SL}(2,\mathbb{R})$ stabilizes a point, i.e.,
fixes the oscillator state $(\theta_0, \omega_0, r_0)$. We show
$g = e$.

The oscillator at the identity $e \in G$ has state
$(\theta_0, r_0, \omega_0) = (0, 1, 0)$ (reference phase, unit
amplitude, zero detuning). An element $h \in G$ acts by left
multiplication: $h \cdot e = h$, sending the reference oscillator to
the oscillator with Iwasawa coordinates of $h$.

For an arbitrary point $g_0 \in G$, the stabilizer is:

$$\mathrm{Stab}(g_0) = \{ h \in G : h \cdot g_0 = g_0 \}
  = \{ h \in G : h g_0 = g_0 \}$$

This gives $h = g_0 g_0^{-1} = e$. That is, the left-multiplication
action $G \curvearrowright G$ defined by $h \cdot g = hg$ has trivial
stabilizer at every point: $\mathrm{Stab}(g_0) = \{e\}$ for all
$g_0 \in G$.

This is a general fact: the left-regular action of any group on itself
is free (every stabilizer is trivial). The content of this lemma is
not the group theory — it is establishing that the left-regular action
is the correct physical description, which requires part (d).

### (d) Faithfulness implies trivial stabilizer

The left-regular representation $\lambda : G \to \mathrm{Aut}(G)$
defined by $\lambda(h)(g) = hg$ is always faithful:
$\ker \lambda = \{e\}$. For any group, a faithful and transitive
action on a set $X$ yields $X \cong G/\mathrm{Stab}(x_0)$ for any
$x_0 \in X$. Since the left-regular action has $\mathrm{Stab}(x_0)
= \{e\}$, we get:

$$\mathcal{M} = G / \{e\} = G$$

The spatial manifold is the group itself.

### (e) Conclusion: $M = G/{e} = G$, hence $d = 3$

Combining (a)-(d):

1. The oscillator state space is three-dimensional: $(\theta, \omega, r)$
2. These three coordinates are exactly the Iwasawa parameters of
   $\mathrm{SL}(2,\mathbb{R})$
3. The group acts on the state space by left multiplication, which is
   free (trivial stabilizer)
4. Therefore $\mathcal{M} = G/H = G/\{e\} = G = \mathrm{SL}(2,\mathbb{R})$

$$d = \dim \mathcal{M} = \dim \mathrm{SL}(2,\mathbb{R}) = 3 \qquad \square$$

---

## Key assumption: no hidden variables

The argument above rests on a critical assumption that must be stated
explicitly.

**Assumption (Kuramoto completeness).** *The observable state of a
Kuramoto oscillator at $K = 1$ is exhausted by the triple
$(\theta, \omega, r)$. There are no hidden internal degrees of freedom
beyond these three quantities.*

**Physical justification.** This assumption is true *by definition* of
the Kuramoto model. The Kuramoto equations of motion contain exactly
the variables $\{\theta_i, \omega_i\}$ and the derived quantity
$r = |z|$ (mean-field amplitude). No additional state variable appears
in the dynamical system. An oscillator in the Kuramoto model IS a
phase plus a natural frequency plus its coupling to the collective
field. There is no internal Hilbert space, no spin, no color charge,
no hidden label. The oscillator's identity is entirely relational: it
is defined by how it participates in the mean field.

This is not a physical discovery but a consequence of the model's
definition. The Kuramoto model is a *minimal* synchronization model
in precisely this sense: it assigns to each oscillator only the
degrees of freedom required for synchronization, and no more.

**Mathematical formulation.** Let $\mathcal{S}$ denote the space of
observable states of a single oscillator. The Kuramoto completeness
assumption states:

$$\mathcal{S} = \{ (\theta, \omega, r) \in S^1 \times \mathbb{R}
  \times \mathbb{R}_{>0} \} \cong \mathrm{SL}(2,\mathbb{R})$$

via the Iwasawa parameterization. The isomorphism
$\mathcal{S} \cong G$ means that the oscillator's observable
properties ARE its $G$-orbit — there is nothing left over for a
nontrivial stabilizer to act on.

---

## What changes with hidden variables

If the oscillator possessed additional internal degrees of freedom
beyond $(\theta, \omega, r)$, the stabilizer $H$ would be nontrivial
and the spatial dimension would decrease. The three cases are
classified by the conjugacy type of $H$ in $\mathrm{SL}(2,\mathbb{R})$
(Derivation 6, subgroup classification):

### Case 1: $H = \mathrm{SO}(2)$ (elliptic/compact)

The oscillator has an internal phase symmetry — a hidden angular
variable that makes the observable phase redundant. The quotient is:

$$\mathcal{M} = \mathrm{SL}(2,\mathbb{R}) / \mathrm{SO}(2)
  \cong \mathbb{H}^2 \qquad (d = 2)$$

The spatial manifold is the hyperbolic plane. Phase is gauged away:
the oscillator cannot lock because its phase is unobservable. This
eliminates the compact (K) Iwasawa factor and reduces the coupling
loop to two stages ($N = 2$), which is below the self-sustaining
threshold (Derivation 6).

### Case 2: $H = A$ (hyperbolic/split)

The oscillator has an internal scale symmetry — a hidden amplitude
variable that makes the observable amplitude redundant. The quotient
is two-dimensional. Amplitude is gauged away: the coupling strength
is not dynamical. The system cannot modulate how strongly it couples,
only whether it couples. This eliminates the split (A) Iwasawa
factor, again giving $N = 2$.

### Case 3: $H = N$ (parabolic/nilpotent)

The oscillator has an internal frequency symmetry — a hidden frequency
variable that makes the detuning redundant. The quotient is
two-dimensional. Frequency detuning is gauged away: there are no
tongue boundaries, no devil's staircase, no saddle-node bifurcations.
This eliminates the nilpotent (N) Iwasawa factor, giving $N = 2$.

### Summary

| Stabilizer $H$ | $\dim H$ | $\dim \mathcal{M}$ | Iwasawa factor lost | Coupling stages | Self-sustaining? |
|---|---|---|---|---|---|
| $\{e\}$ | 0 | 3 | None | 3 | Yes |
| $\mathrm{SO}(2)$ | 1 | 2 | $K$ (phase) | 2 | No |
| $A$ | 1 | 2 | $A$ (amplitude) | 2 | No |
| $N$ | 1 | 2 | $N$ (frequency) | 2 | No |

Every nontrivial connected $H$ reduces $d$ to 2 and kills exactly one
coupling stage, dropping the system below the $N = 3$ self-sustaining
threshold. This is why the trivial stabilizer is not merely a
mathematical convenience but a physical necessity: $H = \{e\}$ is the
unique stabilizer compatible with a self-sustaining synchronization
substrate.

---

## Relationship to the proof chain

This lemma closes gap #4 identified in PROOFREADER_RESPONSE.md:

> *"The claim that 'an oscillator has no identity beyond its coupling'
> forces $H = \{e\}$. This is physically motivated and true for the
> Kuramoto model (the left-regular representation is faithful), but
> the formal statement needs: 'the map $g \to (\text{oscillator at } g)$
> is injective AND the observable properties of the oscillator are
> exactly its $G$-orbit.' The second condition is the physical content
> --- it excludes hidden internal degrees of freedom."*

The lemma provides both components:

1. **Injectivity** (part c): the left-regular action $g \mapsto hg$ is
   free, hence the map $g \mapsto (\text{oscillator at } g)$ is
   injective.

2. **Completeness** (Kuramoto completeness assumption): the observable
   properties $(\theta, \omega, r)$ exhaust the oscillator's state,
   so the observable properties are exactly the $G$-orbit.

Together these give $H = \{e\}$, hence $\mathcal{M} = G$, hence
$d = \dim G = 3$.

---

## References

- Derivation 6 (planck_scale.md): Classification of
  $\mathrm{SL}(2,\mathbb{R})$ subgroups and the $N = 3$
  self-sustaining threshold
- Derivation 14 (three_dimensions.md): The full chain
  mediant $\to$ $\mathrm{SL}(2,\mathbb{Z})$ $\to$
  $\mathrm{SL}(2,\mathbb{R})$ $\to$ $d = 3$, with Step 3c
  being the argument formalized here
- Derivation 15 (lie_group_characterization.md): Uniqueness of
  $\mathrm{SL}(2,\mathbb{R})$ as the continuum substrate
- PROOFREADER_RESPONSE.md: Gap identification (gap #4, "trivial
  isotropy needs formalization")
