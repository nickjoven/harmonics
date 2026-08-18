# Module 0 — History and naming

Read this after working through `README.md` and `engine.py`. The three
shapes are old, and the names that go with them are older than most of
mathematics. Below, each shape is named, dated, and connected to where
it reappears in this curriculum.

## The right angle

The right angle is among the oldest mathematical objects; perpendicular
construction was central to surveying and architecture across multiple
ancient civilizations. The 3-4-5 right triangle (3² + 4² = 5²) was
used by builders long before its proof. Euclid's *Elements* (c. 300 BCE),
Book I Definition 10, gives the formal geometric definition: "When a
straight line set up on a straight line makes the adjacent angles
equal to one another, each of the equal angles is right."

Euclid's definition is intrinsic — it does not refer to motion or
force. The physical reading of 90° as "the angle at which a push does
no work" emerged with analytical mechanics in the 18th and 19th
centuries, and was crystallized in the modern dot-product formulation
in the vector calculus of Gibbs and Heaviside in the late 19th
century.

Today *orthogonal* is used in three contexts — geometric (perpendicular
lines), physical (forces that do no work on each other), and abstract
(vectors with zero inner product in any inner product space). All
three are the same concept seen at different levels of abstraction.

In this curriculum, orthogonality reappears in Module 1 as the
coordinate change that decouples two interacting pendula (the *normal
modes*), and in Module 5 as the structure that distinguishes one phase
direction from another when the joint state of two oscillators is
quotiented by physical symmetries.

## The parabola

The parabola was studied as a conic section by the ancient Greeks.
Apollonius of Perga (c. 200 BCE) introduced the names *ellipse*,
*parabola*, and *hyperbola* in his *Conics*, classifying them by how
a plane could cut a cone. The word *parabola* comes from the Greek
*parabolē* ("comparison," "application").

The physical reading — that the parabola is the trajectory of a
projectile under uniform gravity — was established by Galileo in his
*Dialogues Concerning Two New Sciences* (1638). The orbital
interpretation — that the parabola is the boundary case between
elliptical (bound) and hyperbolic (unbound) trajectories — followed
from Newton's gravitational mechanics in the *Principia* (1687).

In this framework's later modules, the parabola has a second life:
the curve y = x² is the *EML primitive* (`eml(x, y) = exp(x) − ln(y)`),
one of the two universal generators of the framework's continuous
mathematics. The role planted here (boundary between bound and
unbound) is the same role it plays in the framework's bifurcation
analysis: the parabola is the *local shape* near every saddle-node
bifurcation, the boundary between "two states exist" and "no states
exist." Modules 2 and 7 will both lean on this.

## The square

The square is among the oldest geometric shapes in human use. Its
unique mathematical status among regular polygons rests on two
classical results:

1. **Only three regular polygons tile the plane.** The triangle
   (N = 3, interior angle 60°), the square (N = 4, interior angle 90°),
   and the hexagon (N = 6, interior angle 120°). The proof is short:
   a tiling at a vertex requires the interior angle (N − 2)·180/N to
   divide 360° evenly. Only those three values of N work; the
   pentagon (108°) fails, and so does every regular polygon with seven
   or more sides.

2. **Among these three, the square is the only one whose rotational
   order is divisible by four.** The half-turn and quarter-turn are
   symmetries of the square lattice; the triangle and hexagon admit
   thirds and sixths but no order divisible by four. Finer binary
   refinement (eighth-turn and beyond) is not available as rotation —
   the crystallographic restriction below caps lattice rotation at
   order 4 — but is available as scale: dyadic subdivision of the
   square cell.

The seventeen wallpaper groups (the complete classification of
two-dimensional crystallographic symmetries) were enumerated by
E. S. Fedorov in 1891 and independently by George Pólya in 1924.
Three of the seventeen — p4, p4m, and p4g — are built on the square
lattice with four-fold rotational symmetry; they are the only
crystallographic plane groups that admit it.

In this framework, the square's bisectability — quarter-turn
rotation plus dyadic subdivision in scale — anchors every later use
of binary structure: the
two-children-per-node form of the Stern-Brocot tree (introduced in
Module 4), the 2-adic mode-counting of the substrate, and the Catalan
forcing that distinguishes 2 from larger primitive integers (Module
6).

## What you now have

Three shapes in *role form*, not just picture form:

- **90°** is the angle of decoupling.
- **The parabola** is the boundary between bound and unbound.
- **The square** is the simplest tile with binary rotational
  structure.

These are not the only roles each shape can play, but they are the
roles the curriculum will use. Module 1 begins with the simplest
physical system — two pendula on a shared support — in which all
three roles arrive together: orthogonality as the normal-mode
decomposition, the parabola as the boundary between locking and
drifting, and the square's binary structure as the appearance of the
first integer mode counts.
