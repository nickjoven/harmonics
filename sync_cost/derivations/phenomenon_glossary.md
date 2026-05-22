# Phenomenon glossary — dynamics first, names second

## What this file is

A pedagogical glossary, organized by **phenomenon** rather than by the
literature's eponymous tags. The framework's content is a set of
dynamics, not a set of named theorems; the dynamics work the same
whether or not you have heard them called the Stern-Brocot tree, the
Klein bottle, the Arnold tongue, or anything else.

The companion file `canonical_glossary.md` is the translation table
into standard physics / math vocabulary, and is the right reference
when you are trying to map framework writing onto a textbook. This
file is the right reference when you are trying to *commit the
dynamics to memory* — independent of which century someone first
named them.

Each entry has:

- a **description** of what the phenomenon is and what it does,
- **where it appears** in the framework,
- an *also called* tagline pointing to the literature name(s) for the
  same thing, included only as a wayfinding aid.

The descriptions are deliberately written so that you could give them
to someone with no exposure to the literature and have them recognize
the phenomenon when they next encounter it under any of its many
names.

---

## 1. Structures on the line of fractions

### Adjacent fractions and the simplest fraction between them

Two reduced fractions $a/b$ and $c/d$ are **adjacent** when
$|ad - bc| = 1$. Between any two adjacent fractions there is a unique
fraction with smaller denominator than any other rational in the open
interval between them, given by
$$\frac{a+c}{b+d}.$$
This combining operation preserves adjacency: the new fraction is
adjacent to each of its parents. Iterating from $\tfrac{0}{1}$ and
$\tfrac{1}{0}$ generates every positive rational exactly once,
arranged as a binary tree ordered by denominator.

The operation is forced by two requirements: (i) the combined
frequency must lie between the two parent frequencies (energy
conservation), and (ii) it must be the smallest-denominator rational
in that interval (the rational with the widest stability region under
coupling). No other binary combining rule satisfies both.

*Also called:* the **mediant** of $a/b$ and $c/d$; the **Stern-Brocot
tree** (or **Farey tree**); the **Farey sum**. Restricted to fractions
of denominator $\le n$, the listing is the **Farey sequence** $F_n$.

### Counting the new fractions added at each depth

The number of distinct reduced fractions in $[0,1]$ with denominator
$\le n$ is
$$|F_n| = 1 + \sum_{k=1}^{n} \varphi(k),$$
where $\varphi(k)$ counts the integers from $1$ to $k$ that share no
common factor with $k$ (i.e. the count of "units" mod $k$). The
framework uses $|F_6| = 13$ as the count of mode-locked rationals at
denominator depth $6$, and $|F_7| = 19$ as the total when the next
generation of unlocked modes is added.

*Also called:* $|F_n|$ is the **Farey count** at depth $n$;
$\varphi(k)$ is **Euler's totient function**.

### The invariant labeling of fraction-equivalence under the natural
moves on the rationals

Two configurations on the upper half-plane are equivalent under the
natural integer-coefficient fractional moves (see §3) if and only if
they assign the same value to a particular complex-analytic function
of the configuration. That function distinguishes equivalence classes
exactly, and so serves as a "fingerprint" for orbits.

*Also called:* the **$j$-invariant** of an elliptic curve / lattice.

---

## 2. Coupled oscillators and synchronization

### Mode-locking: integer-ratio synchronization of mismatched oscillators

Two oscillators with slightly different natural frequencies, weakly
coupled, will under certain conditions abandon their independent
rhythms and settle into an exact whole-number ratio $p:q$ of cycles.
As the coupling strength rises, the range of frequency mismatch over
which a given ratio $p:q$ remains locked widens out into a region.
The region's width grows with coupling and is broadest for the
smallest denominator $q$, narrower for larger $q$. The framework's
substrate is built from these locked rationals as its only stable
states.

*Also called:* **mode-locking**; the lock regions are called
**Arnold tongues**.

### Criticality: the coupling at which every rational locks

There is a critical coupling strength at which the union of lock
regions covers the entire frequency axis save for a set of measure
zero (only irrationals remain unlocked, and only on a fractal set).
At this critical strength, the graph of the locked-in frequency
ratio against detuning becomes a **staircase**: flat on every
rational interval, with rises concentrated on a Cantor-like set. The
framework treats this critical strength as a *limit*: it is where the
discrete substrate of locked rationals dissolves into a continuum,
and where general-relativistic geometry emerges from substrate
physics. The actual physical regime sits strictly below it.

*Also called:* **$K = 1$ critical coupling**; the staircase is the
**devil's staircase** of the standard circle map.

### Exponential separation rate of nearby trajectories

For a dynamical system, the average exponential rate at which two
trajectories starting infinitesimally close to one another grow
apart in time. A positive rate signals chaos / sensitivity to
initial conditions; a zero rate signals neutral or quasi-periodic
behaviour; a negative rate signals attraction onto a limit set. The
framework computes this rate on the substrate's unlocked sector
analytically and obtains the closed form
$$\lambda_{\text{unlock}}(K=1) = \frac{4G - \pi \ln 2}{\pi}
  \approx 0.473096,$$
where $G \approx 0.915966$ is the constant in §6 below.

*Also called:* the **Lyapunov exponent** (or **Lyapunov rate**) of
the unlocked sector.

### The threshold acceleration below which mode-locking partially
decouples

In ordinary regimes, mode-locking is essentially complete: a test
mode tracks its source as if rigidly coupled. Below a particular
acceleration scale, the lock weakens. The unlocked fraction of the
coupling carries a smaller-than-Newtonian response to the curvature
source, and rotation curves in that regime appear flatter than
Newton predicts. The crossover is smooth, not a sharp on/off. The
framework derives the threshold from the cosmological constant via
$$a_0 = \frac{c H_0}{2\pi} \approx 1.04 \times 10^{-10}~\text{m/s}^2.$$

*Also called:* the **MOND acceleration scale** $a_0$ (after the
phenomenological theory that first identified the empirical
crossover in galactic rotation curves).

### The universal one-parameter form for a pair of fixed points
appearing or disappearing

As a single control parameter is varied, the simplest way a
dynamical system can create or destroy fixed points is for two of
them — one stable, one unstable — to collide and annihilate.
Locally, every smooth one-parameter such event looks like
$$\dot{x} = \mu + x^2,$$
or equivalently $x^2 + \mu = 0$ at equilibrium. This parabola is
the local "weather pattern" of every codimension-1
appearance/disappearance of fixed-point pairs in any smooth system.
The framework uses this normal form to anchor its sector-specific
coupling parabolas.

*Also called:* **saddle-node bifurcation**; **fold catastrophe**
(Thom 1972).

---

## 3. Topology of the phase space

### A coordinate that returns to its start after one trip

A one-dimensional configuration space where the coordinate is
identified modulo a full period — the simplest closed one-dimensional
loop. Every continuous map of this loop into itself has a well-defined
integer "winding number" counting how many times its image runs
around. Whole-number winding is what makes integer charge possible:
once you have a closed loop as a phase space, any covering map
quantises the cover degree as an integer.

*Also called:* the **circle** $S^1$; $\mathbb{R}/\mathbb{Z}$; the
**unit circle group** $U(1)$.

### A surface with no consistent "outward" side

A two-dimensional surface that closes onto itself but cannot be
oriented: walking around certain closed paths on the surface returns
you to your start, mirror-reversed. It cannot be embedded in ordinary
three-dimensional space without self-intersection. The framework
selects this surface as the unique mode topology compatible with its
self-consistency requirements; on it, a parity filter admits exactly
four surviving zero-point modes, against the $\sim 10^{183}$ that the
ordinary "wraps cleanly in all directions" surface would admit.

*Also called:* the **Klein bottle**. The cleanly-orientable
alternative is a **torus**.

### A surface with finitely many boundary degeneration points

When the natural fractional moves on the rationals are restricted to
preserve divisibility mod $N$ (see §3), the resulting quotient
surface has a small finite collection of "cusps" — points where the
geometry pinches off and ordinary measure breaks down. For a
square-free integer $N$, the number of cusps equals the number of
divisors of $N$. For $N = 6$, the four cusps are
$\{\infty,\,1/2,\,1/3,\,0\}$. The framework's symmetric Klein-singlet
boundary mode inhabits Cusp $1/2$.

*Also called:* the **cusps of the modular curve** $X_0(N)$.

---

## 4. Symmetry and group action

### Integer-coefficient fractional moves on the line of rationals

The set of transformations
$$z \mapsto \frac{az + b}{cz + d}$$
with integer entries and $ad - bc = \pm 1$, with matrices identified
up to overall sign. Generated by two basic moves: shift by an
integer, $z \mapsto z + 1$, and inversion-through-zero,
$z \mapsto -1/z$. Acting on the rationals, this group rearranges
them by best-approximation moves and is generated by the mediant
operation. Acting on the upper half plane, it tiles it with
fundamental domains whose vertices are arranged by the structure of
the rationals.

*Also called:* the **modular group**; $\mathrm{PSL}(2, \mathbb{Z})$;
$\mathrm{SL}(2, \mathbb{Z})$ before quotienting by sign. Its
continuum closure $\mathrm{SL}(2, \mathbb{R})$ is three-dimensional,
which is the framework's derivation of spatial $d = 3$.

### Subgroup of fractional moves preserving divisibility mod $N$

Restrict the integer-coefficient fractional moves to those whose
lower-left entry is divisible by $N$. The result preserves
residues mod $N$. For $N = 6 = 2 \cdot 3$, this is the natural
subgroup compatible with the substrate's two basic mode-counts
$q_2 = 2$ and $q_3 = 3$. It can also be obtained as the
intersection of the analogous subgroups for $N = 2$ and $N = 3$
separately.

*Also called:* the **Hecke congruence subgroup of level $N$**,
written $\Gamma_0(N)$.

### Cyclic structure modulo $n$

The integers $\{0, 1, \dots, n-1\}$ with addition mod $n$. For $n$
that factors as a product of pairwise coprime numbers, the
structure splits cleanly into the independent product of its
factor pieces. Mod 6, for instance, knowing a residue is the same as
knowing the parity (mod 2) **and** the third-rotation (mod 3)
separately. The framework's basic mode lattice is exactly this six-
element structure.

*Also called:* $\mathbb{Z}_n$ or $\mathbb{Z}/n\mathbb{Z}$; the
cleanly-factoring decomposition is the **Chinese remainder theorem**.

### Parity-flip symmetry: each mode is either fixed or sign-flipped

A single order-2 transformation (an "involution"; doing it twice is
the identity) sends each mode either to itself with sign $+1$ or to
itself with sign $-1$. The two kinds of mode are the **symmetric**
and the **antisymmetric** modes. In the framework, the symmetric
modes carry electromagnetic coupling and the antisymmetric ones do
not, which distinguishes ordinary from dark matter as a matter of
group representation rather than as a matter of postulated extra
fields.

*Also called:* a **$\mathbb{Z}_2$ character decomposition** /
**Klein-antipodal involution**; the eigenvalue is the
**Klein monodromy** $\pm 1$.

### Six-fold permutation symmetry of four points on a line

Four points on a line, under the natural fractional moves, have one
independent ratio between them — the **cross-ratio**. Permuting the
four points permutes the six possible expressions for this single
ratio:
$$\lambda,\;\; 1 - \lambda,\;\; \tfrac{1}{\lambda},\;\;
  \tfrac{1}{1 - \lambda},\;\; \tfrac{\lambda}{\lambda - 1},\;\;
  \tfrac{\lambda - 1}{\lambda}.$$
The six form one orbit under a symmetric group of size six. This is
the symmetry that organises the framework's three candidate boundary
weights as a single orbit and pins down which of them is realised.

*Also called:* the **anharmonic group**; $S_3$ acting on
$\mathbb{P}^1$; the cross-ratio symmetry.

### Continuous group of point-by-point transformations on fields

A continuous group whose action can vary smoothly from point to
point in spacetime. Specifying which continuous group, and which
representations the matter fields lie in, fixes the inventory of
force carriers and the rules for how they couple. The Standard
Model's choice — three independent components combined as
$\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ — is an
input. The framework derives this combination from the substrate's
six-element mode lattice and its two basic mode-counts $q_2$, $q_3$.

*Also called:* the **gauge group**. Its three pieces are the colour
(strong-force) group $\mathrm{SU}(3)$, the weak-isospin group
$\mathrm{SU}(2)$, and the hypercharge group $\mathrm{U}(1)$.

---

## 5. Bifurcations and regime distinctions

### Coupling strength as the principal control parameter

A single non-negative number $K$ that measures the strength of
coupling between an oscillator and its neighbours. The standard
circle map is
$$\theta_{n+1} = \theta_n + \Omega - \frac{K}{2\pi}\sin(2\pi \theta_n).$$
At $K = 0$, every oscillator runs at its own pace and rationals have
measure zero. At $K = 1$, every rational is locked. Above $K = 1$
trajectories begin to overlap and the map is no longer a
homeomorphism. The framework's matter sector operates at
$K_\star \approx 0.86$, comfortably below criticality.

*Also called:* the **standard circle-map coupling**. The framework
uses $K_\star$ for its matter operating point, $K = 1$ for the
critical (continuum) limit, and $K_0 \sim 3$ for a separate
nucleation threshold; these three coupling regimes are distinct from
the synchronisation-onset coupling $K_c$ of disordered
many-oscillator models, with which the framework's $K_\star$ should
not be confused.

### The continuum limit: where general relativity emerges

At the critical coupling $K = 1$, the rationals densify into the
reals, the Stern-Brocot tree dissolves into a continuum, and the
substrate's combinatorial structure becomes invisible. Smooth
manifold geometry is recovered at this limit, and Einstein's field
equations are the natural equations of motion. The framework treats
this as a *limit point* — useful for matching to general
relativity — not as the actual physical regime.

### The subcritical regime: where the substrate is discrete

For $K < 1$, gaps remain between the lock regions: there exist
detunings on which no locked rational is reached. The substrate
remains discrete, and quantum mechanics emerges as the small-$\varepsilon$
limit of substrate dynamics in this regime. This is the
framework's actual physical regime.

---

## 6. Selected special numbers

### A number from an alternating sum of reciprocal odd squares

$$G = \sum_{n = 0}^{\infty} \frac{(-1)^n}{(2n+1)^2}
   \approx 0.915966.$$
It arises whenever one integrates $\ln|1 + K\cos\theta|$ over half a
period at unit coupling. The framework's analytic Lyapunov rate
$\lambda_{\text{unlock}}(K=1) = (4G - \pi \ln 2)/\pi$ inherits this
constant from such an integral.

*Also called:* **Catalan's constant**.

### A sequence in which each term is the sum of the previous two

Starts $1, 1, 2, 3, 5, 8, 13, 21, \dots$. Successive ratios approach
the golden ratio. The framework uses these as labels for shift
operations on its mediant tree and as the source of its
golden-ratio-winding identification for the scalar spectral tilt
$n_s$.

*Also called:* the **Fibonacci numbers**.

### The identity expressing the unit-circle constraint

$$\sin^2\theta + \cos^2\theta = 1.$$
A direct consequence of parametrising the unit circle by
$(\cos\theta, \sin\theta)$. The framework treats this as a
*definitional primitive* — it carries no derivation content; it is
the algebraic form of the circle topology.

*Also called:* the **Pythagorean identity**.

---

## 7. Cosmological and particle-physics observables

These entries describe the observables the framework predicts, in
phenomenon-first language. The named-after-people tags are kept as
*also-called* taglines so that the framework's predictions are
matchable to the literature.

### The cosmic expansion rate today

The proportionality constant between the recession speed of a
distant source and its present distance from us. Has units of
inverse time. The substrate's prediction of the absolute value sits
on the framework's open-questions list (it requires an anchor); the
substrate predicts the dimensionless ratios involving it, not the
scale itself.

*Also called:* the **Hubble constant** $H_0$.

### The energy density of empty space

A constant energy density that pervades the vacuum, with units of
GeV$^4$ in natural units, measured at roughly $10^{-47}$~GeV$^4$.
Naïvely estimating it by summing zero-point oscillations on a
torus topology up to a quantum-gravitational cutoff gives roughly
$10^{74}$~GeV$^4$ — an excess of $10^{121}$. On the framework's
selected non-orientable surface, a parity filter admits exactly
four surviving zero-point modes; the corresponding vacuum energy is
of order $10^{-47}$~GeV$^4$ without fine-tuning.

*Also called:* the **cosmological constant** $\Lambda$, **vacuum
energy**, **dark energy density**.

### The fraction of the universe's energy density in component $X$

Density of component $X$ divided by the critical density required
for spatial flatness. The three principal cases are dark-energy
$\Omega_\Lambda$, dark-matter $\Omega_{\text{DM}}$, baryon
$\Omega_b$. The substrate predicts the three as the rational
partition $13 : 5 : 1$ (denominator $19 = |F_7|$) at single-weight
closure; the two-component closure refines this to $181 : 70 : 13$
(denominator $264$).

*Also called:* the **density-fraction parameters** $\Omega_X$.

### The mixing angle between the electroweak gauge bosons

The angle that diagonalises the two electroweak gauge bosons into
the observed photon and Z. Equivalently, the fraction
$\sin^2\theta_W$ of the gauge structure carried by the hypercharge
component. Measured at $\approx 0.2312$. The substrate's only
admitted value is $8/35 \approx 0.2286$.

*Also called:* the **Weinberg mixing angle**, **weak mixing angle**.

### The departure of the primordial power spectrum from
scale-invariance

The exponent $n_s$ measuring how the amplitude of curvature
fluctuations imprinted on the cosmic microwave background varies
with scale. A value of $1$ means perfect scale-invariance; the
observed value $0.9649 \pm 0.0042$ shows a slight tilt to redder
scales. The substrate's value, set by the self-similarity of the
mediant tree at the golden-ratio winding, is $0.963$–$0.966$.

*Also called:* the **scalar spectral tilt** $n_s$.

### The ratio of the strong-force coupling to the weak-isospin
coupling

At the Z-boson energy scale and after the standard
energy-scale-tracking procedure, the strong-force coupling is
roughly $3.05$ times the weak-isospin coupling. The substrate's
bare ratio is $q_3^3 / q_2^3 = 27/8 = 3.375$.

*Also called:* $\alpha_s / \alpha_2$; the **strong-to-weak coupling
ratio**.

### The energy scale at which gravitational and quantum effects
become comparable

The energy at which the Compton wavelength of a quantum becomes
comparable to its Schwarzschild radius. Roughly $10^{19}$~GeV; the
corresponding length is roughly $10^{-35}$~m. Used as the natural
cutoff for naïve estimates of the vacuum energy.

*Also called:* the **Planck mass**, **Planck length**, **Planck
scale**.

### The relic radiation from the recombination epoch

The thermal photon bath left over from the time at which the
universe first became transparent. Carries imprinted variations in
temperature and polarisation that record the universe's matter and
geometry. Its temperature-fluctuation spectrum is the principal
empirical anchor for the framework's $n_s$ and amplitude
predictions.

*Also called:* the **cosmic microwave background**, **CMB**.

### The functional whose stationary paths give the equations of
motion

A single scalar quantity built from the fields and their
derivatives; varying the action over field configurations and
demanding stationarity gives the equations of motion. The Standard
Model is specified by its Lagrangian: a small list of terms
encoding the gauge group, the matter content, and the couplings.
Whose values those couplings take is exactly the question the
framework addresses.

*Also called:* the **Lagrangian** / **action** / **principle of
stationary action**.

### The axiomatic framing of relativistic quantum field theory

A formalisation in which quantum fields are operator-valued
distributions on spacetime, with three structural requirements:
covariance under the symmetries of flat spacetime, commutativity of
operators at spacelike-separated points, and positive energy. Under
this framing the Lagrangian's parameters are inputs to be measured,
not outputs to be derived; the framework relaxes that
research-program choice without contradicting the framing itself.

*Also called:* the **Wightman axioms**.

---

## 8. How to use this glossary

The intended workflow is:

1. **Reading framework docs.** When a literature name appears, use
   the *also-called* tagline to find the entry, then read the
   description to recover the dynamics.
2. **Reading textbooks against the framework.** Use this glossary's
   description in reverse: identify the dynamics the textbook is
   describing, then look up which framework entry it corresponds to.
3. **Reasoning about the framework.** Forget the names entirely. The
   framework's content is in the descriptions; the names are
   wayfinding.

The `canonical_glossary.md` translation table is the right reference
when the goal is to publish or to argue with a physicist who reads in
the literature's vocabulary. This file is the right reference when
the goal is to think clearly.

---

## Status

Phenomenon glossary v0.1. ~40 entries across 8 sections. Intended
to be readable end-to-end in ~30 minutes by someone with general
mathematical literacy and no exposure to the specific literature.

Maintenance: update whenever a phenomenon enters or leaves the
framework's working vocabulary. New entries should lead with the
dynamics; the literature name belongs in the *also-called* line.
