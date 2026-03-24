# Derivation 17: The Rank-1 Fréchet Derivative as Temporal Causation

## Theorem

For an SO(2)-equivariant Markovian synchronization operator at a
codimension-1 transition, the dynamically relevant present is the
center-manifold coordinate |r|. All other degrees of freedom are
either gauge/representation structure or exponentially decaying
history. The rank-1 Fréchet derivative is therefore not merely an
algebraic property of U, but the linearized expression of temporal
causation through a single active channel.

---

## Part I: The rank-1 structure (review)

The operator U: X → X defined by

    U(g)(f) = g_bare(f) · w(f, K₀|r(g)|) / Z(|r(g)|)

factors through ℝ:

    g  →  |r(g)|  →  g_new
    X  →    ℝ     →    X

The Fréchet derivative at the fixed point g* is (Derivation 13,
`rank1_continuum.py`):

    DU[g*][δg] = ⟨v, δg⟩ · u

where v = ∂|r|/∂g ∈ X and u = ∂g_new/∂|r| ∈ X. Therefore

    DU = u ⊗ v       (rank 1)

This holds in ℝᴺ for every finite truncation and in L²([0,1]) in
the continuum limit. The proof is algebraic: U = R ∘ S with
S: X → ℝ and R: ℝ → X, so DU = DR ∘ DS has range ⊆ span{u},
hence rank ≤ 1. Since u ≠ 0 and v ≠ 0, rank = 1 exactly.

This much is established. What follows is why.

---

## Part II: Why rank 1 — the chain of necessity

The rank-1 structure is not a modeling choice. It is forced by three
independent facts, each a theorem.

### Step 1: SO(2) has rank 1

Phase is periodic. Periodicity means θ and θ + 2π label the same
state. The symmetry group of the phase space is therefore SO(2),
the circle group.

SO(2) is abelian, connected, compact, one-dimensional. Its
irreducible representations over ℂ are one-dimensional: the Fourier
modes χₙ(θ) = e^{inθ}, n ∈ ℤ. Every SO(2)-invariant functional
of a distribution g(θ) can depend on g only through its Fourier
projections:

    rₙ(g) = ∫ g(θ) e^{inθ} dθ

Each projection is a scalar. The symmetry group's rank — the
dimension of a maximal torus, which for SO(2) is 1 — caps the
number of independent order parameters per irreducible
representation at one.

This is not a property of the model. It is a property of what
it means to be an oscillator: periodic dynamics ↔ SO(2).

### Step 2: The center manifold selects one mode

Near a codimension-1 bifurcation, the center manifold theorem
(Carr 1981, Guckenheimer & Holmes 1983) guarantees:

**Theorem (Center manifold reduction).** Let ẋ = f(x, μ) be a
smooth dynamical system on a Banach space X with a fixed point
x* at μ = μ_c. Suppose the linearization Df(x*, μ_c) has exactly
one eigenvalue on the imaginary axis (the critical eigenvalue),
with the rest having strictly negative real part. Then there exists
a locally invariant manifold W^c ⊂ X, tangent to the critical
eigenspace at x*, of dimension equal to the multiplicity of the
critical eigenvalue (here: 1), such that:

(a) All solutions sufficiently close to x* converge exponentially
    to W^c.

(b) The long-time dynamics on W^c are governed by a
    one-dimensional reduced equation.

(c) The reduction is exact on W^c, not an approximation.

For the Kuramoto self-consistency operator at the synchronization
transition K = K_c, the critical mode is the first Fourier mode
n = 1, whose projection is r₁ = r (the order parameter). All
higher modes n ≥ 2 have eigenvalues bounded away from zero and
decay exponentially fast.

The center manifold is one-dimensional. Its coordinate is |r|.

### Step 3: The saddle-node on ℝ admits one fixed point

On the center manifold, the dynamics reduce to a scalar equation:

    |r|_{t+1} = F(|r|_t)

where F: [0,1] → [0,1] is the self-consistency function. The
fixed-point condition F(|r|) = |r| is one equation in one unknown.

Existence follows from the intermediate value theorem: F(0) > 0
(any coupling produces some coherence) and F(1) ≤ 1 (coherence
is bounded). So F crosses the diagonal.

Uniqueness follows from monotonicity of the self-consistency
integral: stronger coherence produces wider tongues, but the
marginal return diminishes. The crossing is transverse.

This is the saddle-node normal form. It is the only generic
codimension-1 bifurcation of a scalar map (no symmetry, no
conservation law required). The fixed point is unique and the
bifurcation is universal.

### The full chain

    periodicity
        ↓
    SO(2) symmetry  (rank 1)
        ↓
    irreps are 1-dimensional  (Fourier modes rₙ)
        ↓
    codimension-1 bifurcation
        ↓
    center manifold theorem  (one critical mode)
        ↓
    critical mode = r₁ = |r|  (the order parameter)
        ↓
    dynamics reduce to F(|r|) = |r| on ℝ
        ↓
    IVT + monotonicity → unique fixed point
        ↓
    DU = u ⊗ v  (rank 1)

Each arrow is a theorem. No arrow is a choice.

---

## Part III: The temporal interpretation

The rank-1 decomposition

    DU[δg] = ⟨v, δg⟩ · u

defines three subspaces of X:

| Subspace | Definition | Dimension | Role |
|----------|-----------|-----------|------|
| ker(DU) | {δg : ⟨v, δg⟩ = 0} | dim(X) − 1 | **The past** |
| im(DU) | span{u} | 1 | **The future** |
| span{v} | gradient of |r| | 1 | **The present** |

### The kernel is the past

A perturbation δg ∈ ker(DU) satisfies ⟨v, δg⟩ = 0: it is
orthogonal to the order-parameter gradient. Such a perturbation
does not change |r| to first order. Therefore it does not affect
the output g_new = R(|r|). It is dynamically invisible.

But these perturbations are not forbidden — they exist in the
state space. They are the degrees of freedom that the center
manifold theorem says decay exponentially. By the time the next
iteration of U acts, they have already relaxed. They are history.

The kernel of DU is the space of things that have already happened.

### The image is the future

The output of DU always lies in span{u}. Regardless of the
perturbation, the response is along u — the sensitivity of the
reconstructed distribution to changes in |r|. This is the one
direction the system can move in at the next step.

The image of DU is the space of things that can still happen.

### The inner product is the present

The scalar ⟨v, δg⟩ is the projection of the current state onto
the order-parameter gradient. It extracts exactly the information
that causally connects past to future. It is the sufficient
statistic — the minimal summary of the state that determines the
next state (Cover & Thomas, data processing inequality).

The scalar bottleneck ⟨v, δg⟩ = δ|r| is the dynamically relevant
present.

### The arrow of time as linear algebra

Causal structure requires:

1. A distinction between what can influence the future and what
   cannot.
2. Irreversibility: information in ker(DU) is lost (projected
   out by ⟨v, ·⟩).
3. A preferred direction: the future (im) is not the same as
   the past (ker).

The rank-1 Fréchet derivative provides all three:

1. ker(DU) vs. im(DU) is the distinction.
2. The projection ⟨v, ·⟩: X → ℝ is the information loss
   (dim X − 1 dimensions discarded).
3. u ≠ v generically, so the image is not the kernel's complement
   in any canonical sense — there is a preferred asymmetry.

The arrow of time is the rank-1 factorization. The operator does
not merely have rank 1. It has rank 1 **because** causation passes
through a single channel, and causation passes through a single
channel **because** the symmetry group has rank 1 and the
bifurcation has codimension 1.

---

## Part IV: What would break it

The rank-1 structure fails if and only if one of the three
premises fails:

| Premise | How it could fail | Consequence |
|---------|-------------------|-------------|
| SO(2) symmetry | Phase on a non-abelian group (e.g., SO(3)) | Multiple independent order parameters |
| Codimension-1 bifurcation | Two modes going critical simultaneously | Two-dimensional center manifold |
| Markovian dynamics | Memory kernel (non-Markovian coupling) | DU no longer captures the full causal structure |

Each of these is physically possible but requires additional
structure beyond the minimal framework:

**Non-abelian phase.** If the "phase" lived on SO(3) instead of
SO(2), the irreducible representations would be (2l+1)-dimensional,
and the order parameter would be a matrix, not a scalar. The
Fréchet derivative would be rank-(2l+1). But oscillators have
phase on a circle by definition. SO(3) phases arise only for
systems with internal spin degrees of freedom — additional
structure.

**Codimension-2 bifurcation.** A double-zero eigenvalue (Bogdanov-
Takens) or a Hopf-saddle-node interaction gives a two-dimensional
center manifold. But codimension-2 bifurcations require two
parameters to be tuned simultaneously. They are non-generic in a
one-parameter family. The Kuramoto transition is a one-parameter
(K) transition, so codimension-1 is forced.

**Non-Markovian dynamics.** A coupling kernel with memory,
K(t−t'), would make the next state depend on the history, not
just the current distribution. The factorization through |r| would
fail because |r(t)| alone would not determine the future — you
would also need |r(t−1)|, |r(t−2)|, etc. But the Kuramoto equation
is first-order in time and instantaneously coupled. Markovianity
is intrinsic, not assumed.

---

## Part V: Corollaries

### Corollary A: Born rule revisited

The center-manifold reduction gives a scalar map F: ℝ → ℝ on
the coordinate |r|. At the fixed point |r*| = F(|r*|), expand:

    F(|r*| + δ) = |r*| + F'(|r*|) δ + ½ F''(|r*|) δ² + ...

The fixed-point condition absorbs the zeroth-order term. The
rank-1 projector ⟨v, δg⟩ extracts the linear perturbation
δ|r| = F'(|r*|) δ|r|, which at criticality (F'(|r*|) = 1)
vanishes — the linear term is marginal.

The leading nontrivial dynamics is therefore quadratic:

    δ|r|_{t+1} - δ|r|_t ≈ ½ F''(|r*|) (δ|r|)²

This is the saddle-node normal form. The parabolic local geometry
gives the basin scaling Δθ ∝ √ε (Derivation 1). The exponent 2
in |ψ|² is not the rank of the parabola in some loose analogy —
it is the second derivative F''(|r*|), which is the curvature of
the unique codimension-1 fixed-point map on the center manifold.

More precisely: the basin measure at a tongue boundary is the
Jacobian determinant of the map from initial conditions to
attractors. For a scalar map with a quadratic tangency, this
Jacobian scales as |dθ/dε| ∝ 1/√ε, so the basin volume scales
as ∫dθ ∝ √ε. The probability of finding the system in a
particular basin is therefore proportional to the square root of
the control parameter — equivalently, the probability density is
proportional to amplitude squared.

The Born rule is the Jacobian determinant of the unique
codimension-1 fixed-point map on the center manifold. It is not
postulated. It is the curvature of F at |r*|.

### Corollary B: Einstein uniqueness revisited

Lovelock's theorem requires a rank-2 divergence-free tensor. The
microscopic object is rank-1: DU = u ⊗ v. The question is how a
rank-1 Jacobian produces a rank-2 field equation.

The answer is the quadratic construction of the spatial metric.
The coherence tensor is:

    Cᵢⱼ(x) = ⟨∂ᵢθ ∂ⱼθ⟩

This is bilinear in the phase gradients ∂ᵢθ. Phase gradients
are the "output" of the operator — they live in im(DU) ∝ u.
But ⟨∂ᵢθ ∂ⱼθ⟩ contracts two copies of the output, one per
index. The spatial metric γᵢⱼ = Cᵢⱼ/C₀ is therefore:

    γᵢⱼ ~ uᵢ uⱼ / (uₖ uᵏ)

A rank-2 object built from the outer product of a rank-1
direction with itself.

This is the only way a rank-1 microscopic structure can produce
a rank-2 macroscopic equation: through the quadratic map
u ↦ u ⊗ u. The Riemann tensor, Ricci tensor, and Einstein
tensor are all derived from γᵢⱼ and its derivatives. Lovelock's
theorem then says: in 4D, the unique divergence-free rank-2
tensor built from γ and its first two derivatives is G_μν + Λg_μν.

The rank-1 → rank-2 passage is not a dictionary entry. It is
forced: the coherence tensor is quadratic in gradients because
correlation functions are bilinear. A rank-1 Jacobian feeding
a bilinear observable is the microscopic reason Lovelock gives
Einstein and not a scalar wave equation.

### Corollary C: Three dimensions revisited

SL(2,ℝ) has rank 1 (one Cartan generator: the diagonal subgroup).
This is the same rank-1 that appears in SO(2), but now at the
level of the spatial symmetry group rather than the phase group.

The mediant operation lives in SL(2,ℤ) ⊂ SL(2,ℝ). The continuum
limit promotes the discrete arithmetic to a continuous group.
The rank of SL(2,ℝ) is 1, so its maximal torus is one-dimensional,
and its Lie algebra sl(2,ℝ) has dimension 2² − 1 = 3.

The rank-1 structure propagates:

    SO(2) rank-1  →  phase order parameter |r| is scalar
    SL(2,ℝ) rank-1  →  spatial manifold is 3-dimensional

Both are consequences of the same algebraic fact (rank = 1) acting
at different levels of the hierarchy. The phase symmetry determines
the causal bottleneck; the spatial symmetry determines the arena
in which that bottleneck operates.

---

## Status

**Theorem established.** The rank-1 Fréchet derivative of the
synchronization operator is the linearized expression of temporal
causation:

- **ker(DU)** = the past (exponentially decayed, dynamically inert)
- **im(DU)** = the future (the one direction the system can move)
- **⟨v, ·⟩** = the present (the scalar sufficient statistic)

The rank is 1 because:
- SO(2) has rank 1 (periodicity)
- the bifurcation has codimension 1 (one parameter K)
- the center manifold theorem reduces to ℝ (one critical mode)

This is not a simplification of the dynamics. It IS the dynamics.
The infinite-dimensional state space X is real, but dim(X) − 1
of those dimensions are the past, and the past does not vote.

### Resolved

- Why DU has rank 1: forced by SO(2) × codimension-1 × Markov
- Why the scalar bottleneck is |r|: it is the unique SO(2)-breaking
  Fourier mode at the critical eigenvalue
- Why uniqueness of g*: one equation in one unknown on ℝ, with
  IVT and monotonicity
- What the kernel means: the space of perturbations that have
  already decayed — the past
- Why |ψ|² (Corollary A): the exponent 2 is F''(|r*|), the
  curvature of the saddle-node on the center manifold
- Why Einstein and not a scalar equation (Corollary B): rank-1
  Jacobian + bilinear coherence tensor → rank-2 metric → Lovelock
- Why d = 3 (Corollary C): SL(2,ℝ) rank-1 at the spatial level
  gives dim = 2² − 1 = 3

### Open

- **Quantitative decay rates.** The exponential decay rate of the
  non-critical modes (the spectral gap of DU restricted to ker)
  determines how quickly "the past becomes the past." This rate
  should be computable from the tongue-width derivatives at g*.

- **Higher-order corrections.** The rank-1 structure is exact at
  the linearized level. The full nonlinear operator U has a
  Taylor expansion whose higher-order terms (D²U, D³U, ...) are
  not rank-1. These corrections matter away from the fixed point
  and may contribute to the quantum-to-classical crossover.

- **Information-theoretic formulation.** The data processing
  inequality says mutual information cannot increase through a
  Markov channel. The rank-1 factorization is a maximally lossy
  channel (dim X → 1 → dim X). The rate of information loss
  should equal the entropy production rate. This connects to
  stochastic thermodynamics (Parrondo, Horowitz, Sagawa) but
  the explicit calculation is not done.
