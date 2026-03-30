"""
Mediant animations for the harmonics framework.

Five scenes derived from the Stern-Brocot traversal [0; 8, 1, 1, 3]:
    1. stairs   – continued-fraction staircase unfolding step by step
    2. triangle – mediants as triangle subdivisions that flip/overturn
    3. orbit    – the L/R path traced as a polar orbit around 13/19
    4. spiral   – spiraling mediants converging on 7/60
    5. rose     – Farey rose: |F_6| = 13 petals at the 13/19 ratio

Run:
    python animate_mediants.py              # all five, sequential
    python animate_mediants.py stairs       # one scene
    python animate_mediants.py spiral rose  # subset
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.collections import LineCollection

# ---------------------------------------------------------------------------
# Constants from MANIFEST.yml / the Facebook post
# ---------------------------------------------------------------------------
CF = [0, 8, 1, 1, 3]           # continued fraction [0; 8, 1, 1, 3]
DEPTH = sum(CF[1:])            # 13 = |F_6|
BUDGET = 19                    # |F_6| + q2*q3
OMEGA_LAMBDA = DEPTH / BUDGET  # 13/19 ≈ 0.6842

# Stern-Brocot path: L^8 R^1 L^1 R^3
PATH = "L" * 8 + "R" * 1 + "L" * 1 + "R" * 3  # 13 steps


def stern_brocot_walk():
    """Walk the Stern-Brocot tree for [0; 8, 1, 1, 3] = 7/60.

    Standard SB tree with boundaries 0/1 and 1/0 (infinity).
    L^8 R^1 L^1 R^3 lands at 7/60.
    """
    lo_p, lo_q = 0, 1   # 0/1
    hi_p, hi_q = 1, 0   # 1/0 = ∞
    yield 0, "S", (lo_p, lo_q)
    for i, ch in enumerate(PATH):
        med_p = lo_p + hi_p
        med_q = lo_q + hi_q
        if ch == "L":
            hi_p, hi_q = med_p, med_q
        else:
            lo_p, lo_q = med_p, med_q
        yield i + 1, ch, (med_p, med_q)


WALK = list(stern_brocot_walk())
# Final node should be (7, 60)
assert WALK[-1][2] == (7, 60), f"Expected (7,60), got {WALK[-1][2]}"


# ---------------------------------------------------------------------------
# 1. STAIRS – continued-fraction staircase
# ---------------------------------------------------------------------------
def animate_stairs(save=False):
    """Each partial quotient a_k becomes a horizontal or vertical run of a_k
    unit steps, alternating direction like a staircase unfolding."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Continued-Fraction Staircase  [0; 8, 1, 1, 3]", fontsize=13)
    ax.set_xlabel("step")
    ax.set_ylabel("height")
    ax.set_aspect("equal")

    # Pre-compute stair segments: alternate horizontal / vertical runs
    segments = []  # (x0,y0,x1,y1, color)
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(CF[1:])))
    x, y = 0.0, 0.0
    for k, a_k in enumerate(CF[1:]):
        horizontal = (k % 2 == 0)
        for _ in range(a_k):
            if horizontal:
                nx, ny = x + 1, y
            else:
                nx, ny = x, y + 1
            segments.append((x, y, nx, ny, colors[k]))
            x, y = nx, ny

    total = len(segments)
    ax.set_xlim(-0.5, max(s[2] for s in segments) + 1)
    ax.set_ylim(-0.5, max(s[3] for s in segments) + 1)

    lines = []
    label = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=11,
                    verticalalignment="top", fontfamily="monospace")

    def update(frame):
        # draw segments up to frame
        while len(lines) <= frame and frame < total:
            s = segments[frame]
            ln, = ax.plot([s[0], s[2]], [s[1], s[3]], lw=3, color=s[4])
            ax.plot(s[2], s[3], "o", color=s[4], ms=5)
            lines.append(ln)
        depth_so_far = frame + 1
        label.set_text(f"depth {depth_so_far}/{DEPTH}   budget {BUDGET}")
        return lines

    ani = animation.FuncAnimation(fig, update, frames=total,
                                  interval=300, repeat=False)
    if save:
        ani.save("stairs.gif", writer="pillow", fps=3)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 2. TRIANGLES – mediant subdivisions that overturn
# ---------------------------------------------------------------------------
def animate_triangle(save=False):
    """Each mediant (a+c)/(b+d) splits an interval [a/b, c/d].
    Show as a triangle whose apex is the mediant, flipping L/R."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_title("Mediant Triangles Overturning", fontsize=13)
    ax.set_xlim(-0.05, 0.25)
    ax.set_ylim(-0.3, 1.1)
    ax.set_xlabel("value on number line")
    ax.set_ylabel("depth (inverted)")
    ax.invert_yaxis()

    patches = []
    texts = []
    colors_lr = {"L": "#3b82f6", "R": "#ef4444"}

    # Build triangle data from the pre-computed WALK
    triangle_data = []
    lo_p, lo_q = 0, 1
    hi_p, hi_q = 1, 0
    for i, ch in enumerate(PATH):
        med_p = lo_p + hi_p
        med_q = lo_q + hi_q
        left_val = lo_p / lo_q if lo_q != 0 else 0
        right_val = hi_p / hi_q if hi_q != 0 else 1.2
        med_val = med_p / med_q
        depth_y = i / DEPTH
        triangle_data.append((left_val, right_val, med_val, depth_y, ch,
                              f"{med_p}/{med_q}"))
        if ch == "L":
            hi_p, hi_q = med_p, med_q
        else:
            lo_p, lo_q = med_p, med_q

    def update(frame):
        if frame < len(triangle_data):
            lv, rv, mv, dy, ch, lbl = triangle_data[frame]
            # clamp for visibility
            lv_c = max(lv, -0.02)
            rv_c = min(rv, 0.25)
            color = colors_lr.get(ch, "#888")
            tri = Polygon(
                [[lv_c, dy - 0.02], [rv_c, dy - 0.02], [mv, dy + 0.05]],
                closed=True, alpha=0.5, fc=color, ec="k", lw=1.2
            )
            ax.add_patch(tri)
            patches.append(tri)
            t = ax.text(mv, dy + 0.07, lbl, ha="center", fontsize=8,
                        fontweight="bold")
            texts.append(t)
        return patches + texts

    ani = animation.FuncAnimation(fig, update, frames=len(triangle_data),
                                  interval=500, repeat=False)
    if save:
        ani.save("triangles.gif", writer="pillow", fps=2)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 3. ORBIT – L/R path as a polar orbit
# ---------------------------------------------------------------------------
def animate_orbit(save=False):
    """Each L step curves left, each R step curves right, spiraling toward
    the target fraction 7/60. The orbit's angular budget is 2π × 13/19."""
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
    ax.set_title("Stern-Brocot Orbit\nL⁸R¹L¹R³  →  7/60", fontsize=13, pad=20)
    ax.set_ylim(0, 1.2)

    theta_step = (2 * math.pi * OMEGA_LAMBDA) / DEPTH
    thetas = [0.0]
    radii = [1.0]

    for i, ch in enumerate(PATH):
        direction = -1 if ch == "L" else 1
        thetas.append(thetas[-1] + direction * theta_step)
        radii.append(radii[-1] * 0.93)  # spiral inward

    line, = ax.plot([], [], "o-", color="#8b5cf6", lw=2, ms=4)
    dot, = ax.plot([], [], "o", color="#ef4444", ms=10, zorder=5)
    label = ax.text(0, 0, "", transform=ax.transAxes, fontsize=11)

    def update(frame):
        n = frame + 1
        line.set_data(thetas[:n], radii[:n])
        dot.set_data([thetas[frame]], [radii[frame]])
        step_info = WALK[min(frame, len(WALK) - 1)]
        p, q = step_info[2]
        label.set_text(f"  {p}/{q}")
        return line, dot, label

    ani = animation.FuncAnimation(fig, update, frames=len(thetas),
                                  interval=400, repeat=False)
    if save:
        ani.save("orbit.gif", writer="pillow", fps=3)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 4. SPIRAL – spiraling mediants converging on 7/60
# ---------------------------------------------------------------------------
def animate_spiral(save=False):
    """Plot successive mediants on the number line, connected by arcs that
    spiral inward toward the convergent 7/60."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Spiraling Mediants  →  7/60 = 0.11̄6̄", fontsize=13)
    ax.set_xlabel("value")
    ax.set_ylabel("arc height (depth)")

    vals = [w[2][0] / w[2][1] for w in WALK]
    target = 7 / 60

    ax.axvline(target, color="#ef4444", ls="--", alpha=0.5, label="7/60")
    ax.set_xlim(min(vals) - 0.02, max(vals) + 0.05)
    ax.set_ylim(-0.5, DEPTH + 1)

    arcs = []
    dots = []
    annotations = []

    def update(frame):
        if frame < len(vals):
            v = vals[frame]
            d = frame
            dot, = ax.plot(v, d, "o", color="#3b82f6", ms=8, zorder=5)
            dots.append(dot)
            p, q = WALK[frame][2]
            ann = ax.annotate(f"{p}/{q}", (v, d), textcoords="offset points",
                              xytext=(8, 4), fontsize=8)
            annotations.append(ann)

            if frame > 0:
                v_prev = vals[frame - 1]
                d_prev = frame - 1
                mid_x = (v_prev + v) / 2
                mid_y = (d_prev + d) / 2 + 0.3
                arc_x = np.linspace(v_prev, v, 30)
                t_param = np.linspace(0, 1, 30)
                arc_y = d_prev + (d - d_prev) * t_param + \
                    0.4 * np.sin(np.pi * t_param)
                ln, = ax.plot(arc_x, arc_y, "-", color="#8b5cf6", alpha=0.6,
                              lw=1.5)
                arcs.append(ln)
        return dots + arcs + annotations

    ani = animation.FuncAnimation(fig, update, frames=len(vals),
                                  interval=400, repeat=False)
    if save:
        ani.save("spiral.gif", writer="pillow", fps=3)
    ax.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# 5. ROSE – Farey rose with |F_6| = 13 petals
# ---------------------------------------------------------------------------
def animate_rose(save=False):
    """A polar rose r = cos(13θ/19) with 13 petals, colored by the
    Stern-Brocot path. Each petal blooms one at a time."""
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
    ax.set_title(f"|F₆| = {DEPTH} petals,  Ω_Λ = {DEPTH}/{BUDGET}",
                 fontsize=13, pad=20)
    ax.set_ylim(0, 1.15)

    # Rose curve: r = cos(k*theta) where k = 13 gives 13 petals (k odd)
    n_petals = DEPTH
    full_theta = np.linspace(0, 2 * np.pi, 2000)
    full_r = np.abs(np.cos(n_petals * full_theta / 2))

    # Color map: 13 segments from the path
    cmap = plt.cm.plasma

    line, = ax.plot([], [], lw=2, color="#8b5cf6")
    fills = []

    frames_per_petal = 8
    total_frames = n_petals * frames_per_petal

    def update(frame):
        petal = frame // frames_per_petal
        sub = frame % frames_per_petal + 1
        frac = sub / frames_per_petal

        # draw up to current petal
        end_idx = int((petal + frac) / n_petals * len(full_theta))
        end_idx = min(end_idx, len(full_theta))
        line.set_data(full_theta[:end_idx], full_r[:end_idx])
        line.set_color(cmap(petal / n_petals))

        # fill completed petals
        if sub == frames_per_petal and petal < n_petals:
            start_idx = int(petal / n_petals * len(full_theta))
            seg_theta = full_theta[start_idx:end_idx]
            seg_r = full_r[start_idx:end_idx]
            color = cmap(petal / n_petals)
            fill = ax.fill_between(seg_theta, 0, seg_r, alpha=0.3, color=color)
            fills.append(fill)

        return [line] + fills

    ani = animation.FuncAnimation(fig, update, frames=total_frames,
                                  interval=80, repeat=False)
    if save:
        ani.save("rose.gif", writer="pillow", fps=12)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
SCENES = {
    "stairs": animate_stairs,
    "triangle": animate_triangle,
    "orbit": animate_orbit,
    "spiral": animate_spiral,
    "rose": animate_rose,
}

if __name__ == "__main__":
    requested = sys.argv[1:] if len(sys.argv) > 1 else list(SCENES.keys())
    save = "--save" in requested
    requested = [r for r in requested if r != "--save"]
    for name in requested:
        if name in SCENES:
            print(f"▶ {name}")
            SCENES[name](save=save)
        else:
            print(f"Unknown scene: {name}. Choose from: {list(SCENES.keys())}")
