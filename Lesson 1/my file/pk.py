# Let's generate a short Jarvis-style pulsating "arc reactor" animation as a GIF.
# It will be saved at /mnt/data/jarvis_pulse.gif for download.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Figure setup
fig, ax = plt.subplots(figsize=(4.8, 4.8), dpi=100)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# Static elements (outer ring)
outer_ring = plt.Circle((0, 0), 1.0, fill=False, linewidth=3, alpha=0.6)
inner_ring = plt.Circle((0, 0), 0.25, fill=False, linewidth=2, alpha=0.7)
glow_ring = plt.Circle((0, 0), 0.6, fill=False, linewidth=8, alpha=0.15)

ax.add_patch(outer_ring)
ax.add_patch(inner_ring)
ax.add_patch(glow_ring)

# Dynamic elements
num_spokes = 12
spokes = []
for i in range(num_spokes):
    # Each spoke is a line from r0 to r1 at angle theta
    line, = ax.plot([], [], linewidth=2, alpha=0.85)
    spokes.append(line)

# Rotating triangles (energy shards)
num_shards = 6
shards = []
for i in range(num_shards):
    tri, = ax.plot([], [], linewidth=1.5, alpha=0.9)
    shards.append(tri)

# Pulsing dots around the ring
num_dots = 40
dots_theta = np.linspace(0, 2*np.pi, num_dots, endpoint=False)
dot_scat = ax.scatter(np.cos(dots_theta)*0.9, np.sin(dots_theta)*0.9, s=10, alpha=0.7)

# Central glow
central_glow = plt.Circle((0, 0), 0.28, color='#7ffcff', alpha=0.25)
ax.add_patch(central_glow)

# Color palette (Jarvis-style cyan/teal/white)
COLORS = ['#9ffcff', '#7ffcff', '#5feaff', '#e6ffff']

def init():
    for i, line in enumerate(spokes):
        line.set_data([], [])
        line.set_color(COLORS[i % len(COLORS)])
    for i, tri in enumerate(shards):
        tri.set_data([], [])
        tri.set_color(COLORS[(i+1) % len(COLORS)])
    outer_ring.set_edgecolor('#bffaff')
    inner_ring.set_edgecolor('#dfffff')
    glow_ring.set_edgecolor('#7ffcff')
    return spokes + shards + [outer_ring, inner_ring, glow_ring]

def make_triangle(center, r0, r1, theta, width_angle):
    # Create a thin triangular shard
    p0 = np.array([r0*np.cos(theta), r0*np.sin(theta)])
    p1 = np.array([r1*np.cos(theta - width_angle/2), r1*np.sin(theta - width_angle/2)])
    p2 = np.array([r1*np.cos(theta + width_angle/2), r1*np.sin(theta + width_angle/2)])
    xs = [p0[0], p1[0], p2[0], p0[0]]
    ys = [p0[1], p1[1], p2[1], p0[1]]
    return xs, ys

def update(frame):
    t = frame / 60.0  # seconds if 60 fps
    # Pulse radii
    pulse = 0.6 + 0.05*np.sin(2*np.pi*t*1.2)
    glow_ring.set_linewidth(8 + 4*np.sin(2*np.pi*t*1.2))
    glow_ring.set_alpha(0.12 + 0.08*(1+np.sin(2*np.pi*t*1.2))/2)
    central_glow.set_radius(0.26 + 0.03*np.sin(2*np.pi*t*1.2))

    # Rotate spokes
    for i, line in enumerate(spokes):
        theta = 2*np.pi*(i/num_spokes) + 2*np.pi*t*0.4
        r0, r1 = 0.32, 0.95
        x = [r0*np.cos(theta), r1*np.cos(theta)]
        y = [r0*np.sin(theta), r1*np.sin(theta)]
        line.set_data(x, y)
        line.set_alpha(0.6 + 0.4*(0.5+0.5*np.sin(2*np.pi*t*1.2 + i)))
    
    # Energy shards rotate at a different speed
    for i, tri in enumerate(shards):
        theta = 2*np.pi*(i/num_shards) - 2*np.pi*t*0.25
        xs, ys = make_triangle((0,0), 0.35, pulse, theta, width_angle=0.2)
        tri.set_data(xs, ys)
        tri.set_alpha(0.6 + 0.3*(0.5+0.5*np.sin(2*np.pi*t + i)))
    
    # Dots shimmer
    sizes = 12 + 6*np.sin(dots_theta*3 + 2*np.pi*t*2)
    alphas = 0.4 + 0.4*(0.5+0.5*np.sin(dots_theta*2 + 2*np.pi*t*1.5))
    dot_scat.set_sizes(sizes)
    dot_scat.set_alpha(None)  # needed to pass array-like alpha in newer matplotlib
    try:
        # Newer versions allow setting alpha per point via "_alpha" private attr is not reliable;
        # We'll modulate overall alpha instead.
        dot_scat.set_alpha(0.55 + 0.25*np.sin(2*np.pi*t*1.5))
    except Exception:
        pass

    return spokes + shards + [glow_ring, central_glow]

# Create the animation
frames = 240  # ~4 seconds at 60 fps
anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

# Save as GIF
output_path = "/mnt/data/jarvis_pulse.gif"
writer = PillowWriter(fps=30)
anim.save(output_path, writer=writer)

plt.close(fig)

output_path
