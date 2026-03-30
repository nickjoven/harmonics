"""
Genesis animation: from zero information to the Klein bottle.

Stages:
    0. Void          – black, no information
    1. Binary        – a single bit flickers: 0 / 1
    2. Plane          – x,y axes emerge from the bit
    3. Pong           – two oscillators, a ball between them
    4. Fixed point    – ball converges, oscillators decelerate
    5. Vortex         – when motion threatens zero, a spiral ignites
    6. Twin trees     – vortex settles into two inverted Stern-Brocot
                        trees joined at a half-twist node (Klein neck)

Run:
    python animate_genesis.py              # play + save genesis.gif
    python animate_genesis.py --no-save    # play only
"""

import sys
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch, Circle, Arc
from matplotlib.collections import LineCollection

# ---------------------------------------------------------------------------
# Timing (frames)
# ---------------------------------------------------------------------------
FPS = 30
STAGE_FRAMES = [
    45,   # 0  void           1.5s
    50,   # 1  binary         1.7s
    50,   # 2  plane          1.7s
    90,   # 3  pong           3.0s
    70,   # 4  fixed point    2.3s
    80,   # 5  vortex         2.7s
    90,   # 6  twin trees     3.0s
]
TOTAL = sum(STAGE_FRAMES)
STAGE_STARTS = []
_s = 0
for n in STAGE_FRAMES:
    STAGE_STARTS.append(_s)
    _s += n

def stage_of(frame):
    for i in range(len(STAGE_STARTS) - 1, -1, -1):
        if frame >= STAGE_STARTS[i]:
            return i, (frame - STAGE_STARTS[i]) / STAGE_FRAMES[i]
    return 0, 0.0

# ---------------------------------------------------------------------------
# Stern-Brocot helpers
# ---------------------------------------------------------------------------
def sb_tree_with_edges(max_depth=4):
    """Build Stern-Brocot tree nodes and parent-child edges."""
    # Each node: (numerator, denominator, depth, left_bound_n, left_bound_d,
    #             right_bound_n, right_bound_d)
    nodes = []   # (n, d, depth, index)
    edges = []   # (parent_idx, child_idx)

    def build(a_n, a_d, b_n, b_d, depth, parent_idx):
        if depth > max_depth:
            return
        m_n = a_n + b_n
        m_d = a_d + b_d
        idx = len(nodes)
        nodes.append((m_n, m_d, depth))
        if parent_idx is not None:
            edges.append((parent_idx, idx))
        # Left child: between a and m
        build(a_n, a_d, m_n, m_d, depth + 1, idx)
        # Right child: between m and b
        build(m_n, m_d, b_n, b_d, depth + 1, idx)

    build(0, 1, 1, 0, 1, None)
    xs = np.array([n[0] / n[1] for n in nodes])
    depths = np.array([n[2] for n in nodes])
    return xs, depths, edges

# ---------------------------------------------------------------------------
# Easing
# ---------------------------------------------------------------------------
def ease_in_out(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)

def ease_out(t):
    t = np.clip(t, 0, 1)
    return 1 - (1 - t) ** 3

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6), facecolor="black")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.0, 1.0)
ax.set_aspect("equal")
ax.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Persistent artists
txt_center = ax.text(0, 0, "", color="white", fontsize=28,
                     ha="center", va="center", fontfamily="monospace")
txt_small = ax.text(0, -0.15, "", color="gray", fontsize=11,
                    ha="center", va="center", fontfamily="monospace")

# Pong elements
paddle_l = plt.Rectangle((-1.05, -0.15), 0.04, 0.3, color="cyan", visible=False)
paddle_r = plt.Rectangle((1.01, -0.15), 0.04, 0.3, color="magenta", visible=False)
ball = plt.Circle((0, 0), 0.03, color="white", visible=False)
ax.add_patch(paddle_l)
ax.add_patch(paddle_r)
ax.add_patch(ball)

# Axis lines (for stage 2)
xaxis_line, = ax.plot([], [], color="white", lw=0.8, alpha=0)
yaxis_line, = ax.plot([], [], color="white", lw=0.8, alpha=0)

# Vortex line
vortex_line, = ax.plot([], [], color="cyan", lw=1.2, alpha=0)

# Tree scatter + lines
tree_scatter_up = ax.scatter([], [], s=40, c="cyan", alpha=0, zorder=5)
tree_scatter_dn = ax.scatter([], [], s=40, c="magenta", alpha=0, zorder=5)
tree_lines_up, = ax.plot([], [], color="cyan", lw=1.2, alpha=0)
tree_lines_dn, = ax.plot([], [], color="magenta", lw=1.2, alpha=0)
twist_line, = ax.plot([], [], color="yellow", lw=2.5, alpha=0)
twist_dot = plt.Circle((0, 0), 0.04, color="yellow", visible=False, zorder=10)
ax.add_patch(twist_dot)

# Pre-compute tree — clip to rational range (0,1) to avoid infinity edges
TX_raw, TD_raw, TEDGES_raw = sb_tree_with_edges(4)
# Filter out nodes where fraction > 5 (near 1/0 boundary)
keep = TX_raw < 5.0
keep_idx = np.where(keep)[0]
idx_map = {old: new for new, old in enumerate(keep_idx)}
TX = TX_raw[keep]
TD = TD_raw[keep]
TEDGES = [(idx_map[p], idx_map[c]) for p, c in TEDGES_raw
          if p in idx_map and c in idx_map]

# Normalize: map (0, max) → (-0.85, 0.85)
tx_max = max(TX.max(), 1.0)
tx_norm = (TX / tx_max - 0.5) * 1.7
ty_up = -TD * 0.17 + 0.82     # upper tree: root at top, grows down
ty_dn = TD * 0.17 - 0.82      # lower tree: root at bottom, grows up

# Ball trail (afterimage)
TRAIL_LEN = 12
ball_trail = []  # list of (x, y) recent positions
trail_dots = [plt.Circle((0, 0), 0.02, color="white", alpha=0, visible=False)
              for _ in range(TRAIL_LEN)]
for dot in trail_dots:
    ax.add_patch(dot)

# Spiral point markers (for Stage 4)
N_SPIRAL_MARKERS = 20
spiral_markers = ax.scatter([], [], s=30, c="white", alpha=0, zorder=6)

# Ball physics state
ball_state = {"x": 0.0, "y": 0.0, "vx": 0.03, "vy": 0.018,
              "converging": False, "conv_start": 0}

def reset_ball():
    ball_state["x"] = 0.0
    ball_state["y"] = 0.0
    ball_state["vx"] = 0.03
    ball_state["vy"] = 0.018
    ball_state["converging"] = False
    ball_trail.clear()

# ---------------------------------------------------------------------------
# Frame update
# ---------------------------------------------------------------------------
def update(frame):
    stage, t = stage_of(frame)
    te = ease_in_out(t)
    to = ease_out(t)

    # --- defaults: hide everything ---
    txt_center.set_text("")
    txt_small.set_text("")
    paddle_l.set_visible(False)
    paddle_r.set_visible(False)
    ball.set_visible(False)
    xaxis_line.set_alpha(0)
    yaxis_line.set_alpha(0)
    vortex_line.set_alpha(0)
    tree_scatter_up.set_alpha(0)
    tree_scatter_dn.set_alpha(0)
    tree_lines_up.set_alpha(0)
    tree_lines_dn.set_alpha(0)
    twist_line.set_alpha(0)
    twist_dot.set_visible(False)
    for dot in trail_dots:
        dot.set_visible(False)
        dot.set_alpha(0)
    spiral_markers.set_alpha(0)
    spiral_markers.set_offsets(np.empty((0, 2)))
    fig.set_facecolor("black")
    ax.set_facecolor("black")

    # ===================== STAGE 0: VOID =====================
    if stage == 0:
        # Pure black. Maybe a faint pulse near the end.
        if t > 0.7:
            alpha = (t - 0.7) / 0.3
            txt_center.set_text("∅")
            txt_center.set_alpha(alpha * 0.3)

    # ===================== STAGE 1: BINARY =====================
    elif stage == 1:
        local_frame = frame - STAGE_STARTS[1]
        # Flicker between 0 and 1, increasing frequency
        freq = 2 + t * 20
        val = int(math.sin(freq * t * math.pi * 2) > 0)
        txt_center.set_text(str(val))
        txt_center.set_fontsize(40 + t * 30)
        txt_center.set_alpha(0.5 + 0.5 * abs(math.sin(freq * t * math.pi)))
        txt_center.set_color("white")
        if t > 0.8:
            txt_small.set_text("one bit")
            txt_small.set_alpha((t - 0.8) / 0.2)

    # ===================== STAGE 2: PLANE =====================
    elif stage == 2:
        extent = to * 1.1
        xaxis_line.set_data([-extent, extent], [0, 0])
        xaxis_line.set_alpha(to)
        yaxis_line.set_data([0, 0], [-extent, extent])
        yaxis_line.set_alpha(to)

        if t > 0.3:
            txt_center.set_text("+")
            txt_center.set_fontsize(20)
            txt_center.set_alpha((t - 0.3) / 0.7 * 0.5)
            txt_center.set_position((0.02, 0.02))

        if t > 0.5:
            a2 = (t - 0.5) / 0.5
            txt_small.set_text("x , y")
            txt_small.set_alpha(a2 * 0.7)
            txt_small.set_position((0.35, -0.35))

        # Reset for next stage
        if t > 0.95:
            reset_ball()

    # ===================== STAGE 3: PONG =====================
    elif stage == 3:
        # Keep axes faintly
        xaxis_line.set_data([-1.1, 1.1], [0, 0])
        xaxis_line.set_alpha(0.15)
        yaxis_line.set_data([0, 0], [-1.1, 1.1])
        yaxis_line.set_alpha(0.15)

        # Coupling: paddles drift inward as t grows, oscillation dampens
        coupling = ease_in_out(t)  # 0 → 1 over the stage
        pad_wall = 1.05 - coupling * 0.45  # paddles: 1.05 → 0.60
        bounce_wall = pad_wall - 0.10

        paddle_l.set_visible(True)
        paddle_r.set_visible(True)
        paddle_l.set_x(-pad_wall)
        paddle_r.set_x(pad_wall - 0.04)

        # Ball bouncing with dampened velocity
        bx, by = ball_state["x"], ball_state["y"]
        vx, vy = ball_state["vx"], ball_state["vy"]

        # Dampen horizontal oscillation as coupling increases
        speed_scale = 1.0 - 0.6 * coupling
        bx += vx * speed_scale
        by += vy * speed_scale

        # Bounce off paddles (walls close in)
        if bx < -bounce_wall:
            vx = abs(vx)
            bx = -bounce_wall
        if bx > bounce_wall:
            vx = -abs(vx)
            bx = bounce_wall
        # Bounce off top/bottom
        if abs(by) > 0.85:
            vy = -vy
            by = np.clip(by, -0.85, 0.85)

        ball_state["x"] = bx
        ball_state["y"] = by
        ball_state["vx"] = vx
        ball_state["vy"] = vy

        ball.center = (bx, by)
        ball.set_visible(True)

        # Afterimage trail
        ball_trail.append((bx, by))
        if len(ball_trail) > TRAIL_LEN:
            ball_trail.pop(0)
        for i, dot in enumerate(trail_dots):
            if i < len(ball_trail):
                tx_, ty_ = ball_trail[i]
                age = (i + 1) / len(ball_trail)  # 0..1, newest = 1
                dot.center = (tx_, ty_)
                dot.set_radius(0.015 + 0.01 * age)
                dot.set_alpha(age * 0.35 * (0.5 + 0.5 * coupling))
                dot.set_visible(True)
                # Trail colour shifts toward yellow as coupling grows
                r_c = coupling
                dot.set_color((1.0, 1.0, 1.0 - 0.6 * r_c))

        # Paddles track ball y (noise decreases with coupling)
        noise = np.random.normal(0, 0.02 * (1 - 0.8 * coupling))
        paddle_l.set_y(by - 0.15 + noise)
        paddle_r.set_y(by - 0.15 + noise)

        # Label: exchange count → "maximum coupling"
        if t > 0.3 and t < 0.75:
            txt_small.set_text(f"exchange {int(t * 12)}")
            txt_small.set_alpha(0.3)
            txt_small.set_position((0, 0.92))
        elif t >= 0.75:
            mc_alpha = ease_in_out((t - 0.75) / 0.25)
            txt_small.set_text("maximum coupling")
            txt_small.set_alpha(mc_alpha * 0.7)
            txt_small.set_position((0, 0.92))

    # ===================== STAGE 4: FIXED POINT =====================
    elif stage == 4:
        xaxis_line.set_data([-1.1, 1.1], [0, 0])
        xaxis_line.set_alpha(0.1)
        yaxis_line.set_data([0, 0], [-1.1, 1.1])
        yaxis_line.set_alpha(0.1)

        paddle_l.set_visible(True)
        paddle_r.set_visible(True)

        # Ball spirals inward toward origin (fixed point)
        decay = math.exp(-3.0 * t)
        angle = t * 12 * math.pi
        r = 0.8 * decay
        bx = r * math.cos(angle)
        by = r * math.sin(angle)

        ball.center = (bx, by)
        ball.set_visible(True)

        # Dramatized spiral markers: spacing inversely proportional to
        # number of completed turns.  Few turns → wide gaps; many → dense.
        n_turns = t * 6  # total turns so far (0→6)
        if n_turns < 0.3:
            n_marks = 2
        else:
            n_marks = min(N_SPIRAL_MARKERS, max(3, int(n_turns * 3.5)))
        # Non-uniform parameterisation: cube-root bunches points toward
        # the outer (early) part of the spiral when n_marks is low,
        # spreading them dramatically.  As n_marks grows, the effect
        # is diluted and the spacing becomes denser overall.
        u = np.linspace(0, 1, n_marks)
        spread = 1.0 / (1.0 + n_turns)       # 1 → ~0.14
        tau = u ** (1.0 - 0.6 * spread)       # exponent: ~0.4 (early) → ~0.9 (late)
        mk_t = tau * t                        # map to stage-local time
        mk_decay = np.exp(-3.0 * mk_t)
        mk_angle = mk_t * 12 * math.pi
        mk_r = 0.8 * mk_decay
        mk_x = mk_r * np.cos(mk_angle)
        mk_y = mk_r * np.sin(mk_angle)
        spiral_markers.set_offsets(np.column_stack([mk_x, mk_y]))
        # Size: larger when sparse, smaller when dense
        mk_size = max(15, 55 - n_marks * 2)
        spiral_markers.set_sizes(np.full(n_marks, mk_size))
        spiral_markers.set_facecolor("white")
        spiral_markers.set_alpha(min(1.0, 0.3 + te * 0.7))

        # Paddles drift toward center
        pad_x = 1.01 - t * 0.5
        paddle_l.set_x(-pad_x - 0.04)
        paddle_r.set_x(pad_x)
        paddle_l.set_y(by - 0.15)
        paddle_r.set_y(by - 0.15)

        # Fade paddles
        paddle_l.set_alpha(1 - t * 0.8)
        paddle_r.set_alpha(1 - t * 0.8)

        # Label
        txt_center.set_text("x = f(x)")
        txt_center.set_fontsize(18)
        txt_center.set_alpha(te * 0.6)
        txt_center.set_position((0, 0.85))
        txt_center.set_color("yellow")

        if t > 0.7:
            # Threaten stasis
            txt_small.set_text("Δ → 0")
            txt_small.set_alpha((t - 0.7) / 0.3)
            txt_small.set_position((0, -0.85))
            ball.set_color("red" if int(t * 40) % 2 == 0 else "white")

    # ===================== STAGE 5: VORTEX =====================
    elif stage == 5:
        # Spiral vortex expands from origin — double arm
        n_pts = 400
        max_turns = 3 + t * 6
        theta = np.linspace(0, max_turns * 2 * math.pi, n_pts)
        r = np.linspace(0.02, to * 1.05, n_pts)

        # Arm 1
        x1 = r * np.cos(theta + frame * 0.08)
        y1 = r * np.sin(theta + frame * 0.08)
        vortex_line.set_data(x1, y1)
        vortex_line.set_linewidth(1.5 + t * 1.5)
        vortex_line.set_alpha(min(1.0, 0.3 + to * 0.7))

        # Color shifts cyan → yellow
        if t < 0.5:
            vortex_line.set_color("cyan")
        else:
            frac = (t - 0.5) / 0.5
            vortex_line.set_color((frac, 1.0, 1.0 - frac * 0.5))

        # Draw second arm via the other plot object
        x2 = r * np.cos(theta + math.pi + frame * 0.08)
        y2 = r * np.sin(theta + math.pi + frame * 0.08)
        tree_lines_up.set_data(x2, y2)
        tree_lines_up.set_color("magenta")
        tree_lines_up.set_linewidth(1.5 + t * 1.5)
        tree_lines_up.set_alpha(min(1.0, 0.3 + to * 0.7))

        # Ball at center, pulsing
        ball.set_visible(True)
        pulse = 0.03 + 0.03 * abs(math.sin(t * 10 * math.pi))
        ball.set_radius(pulse)
        ball.center = (0, 0)
        ball.set_color("white")

        if t > 0.5:
            txt_small.set_text("information cannot stop")
            txt_small.set_alpha((t - 0.5) / 0.5 * 0.8)
            txt_small.set_position((0, -0.92))

    # ===================== STAGE 6: TWIN TREES =====================
    elif stage == 6:
        # Fade in two Stern-Brocot trees, one normal (up), one inverted (down)
        # connected by a half-twist at origin

        n_total = len(tx_norm)
        n_show = max(1, int(n_total * ease_out(t * 1.3)))
        n_show = min(n_show, n_total)

        # Upper tree (cyan) – normal orientation
        tree_scatter_up.set_offsets(np.column_stack([tx_norm[:n_show],
                                                      ty_up[:n_show]]))
        tree_scatter_up.set_alpha(min(1.0, te * 1.2))

        # Lower tree (magenta) – inverted
        tree_scatter_dn.set_offsets(np.column_stack([tx_norm[:n_show],
                                                      ty_dn[:n_show]]))
        tree_scatter_dn.set_alpha(min(1.0, te * 1.2))

        # Draw proper parent-child edges
        segs_x_up, segs_y_up = [], []
        segs_x_dn, segs_y_dn = [], []
        for p_idx, c_idx in TEDGES:
            if c_idx < n_show and p_idx < n_show:
                segs_x_up.extend([tx_norm[p_idx], tx_norm[c_idx], np.nan])
                segs_y_up.extend([ty_up[p_idx], ty_up[c_idx], np.nan])
                segs_x_dn.extend([tx_norm[p_idx], tx_norm[c_idx], np.nan])
                segs_y_dn.extend([ty_dn[p_idx], ty_dn[c_idx], np.nan])

        tree_lines_up.set_data(segs_x_up, segs_y_up)
        tree_lines_up.set_color("cyan")
        tree_lines_up.set_linewidth(1.2)
        tree_lines_up.set_alpha(min(1.0, te * 0.8))
        tree_lines_dn.set_data(segs_x_dn, segs_y_dn)
        tree_lines_dn.set_color("magenta")
        tree_lines_dn.set_linewidth(1.2)
        tree_lines_dn.set_alpha(min(1.0, te * 0.8))

        # Half-twist connection — figure-8 linking the two trees
        if t > 0.25:
            twist_t = (t - 0.25) / 0.75
            twist_te = ease_in_out(twist_t)

            # Lissajous figure-8
            theta_tw = np.linspace(-math.pi, math.pi, 120)
            tw_x = 0.2 * np.sin(2 * theta_tw) * twist_te
            tw_y = 0.35 * np.sin(theta_tw) * twist_te
            twist_line.set_data(tw_x, tw_y)
            twist_line.set_alpha(twist_te)
            twist_line.set_linewidth(2.5)

            twist_dot.center = (0, 0)
            twist_dot.set_radius(0.05)
            twist_dot.set_visible(True)
            twist_dot.set_alpha(twist_te)

        # Labels
        if t > 0.4:
            la = ease_in_out((t - 0.4) / 0.6)
            txt_center.set_text("13 / 19")
            txt_center.set_fontsize(24)
            txt_center.set_alpha(la * 0.95)
            txt_center.set_position((0, 0))
            txt_center.set_color("yellow")

            txt_small.set_text("K²  —  the loop that cannot close")
            txt_small.set_alpha(la * 0.7)
            txt_small.set_position((0, -0.95))

    return (txt_center, txt_small, paddle_l, paddle_r, ball,
            xaxis_line, yaxis_line, vortex_line,
            tree_scatter_up, tree_scatter_dn,
            tree_lines_up, tree_lines_dn,
            twist_line, twist_dot, spiral_markers,
            *trail_dots)


# ---------------------------------------------------------------------------
# Build and save
# ---------------------------------------------------------------------------
ani = animation.FuncAnimation(fig, update, frames=TOTAL,
                              interval=1000 // FPS, blit=False)

save = "--no-save" not in sys.argv
if save:
    print(f"Rendering genesis.gif  ({TOTAL} frames, {TOTAL / FPS:.1f}s) ...")
    ani.save("genesis.gif", writer="pillow", fps=FPS,
             savefig_kwargs={"facecolor": "black"})
    print("Done → genesis.gif")
else:
    plt.show()
