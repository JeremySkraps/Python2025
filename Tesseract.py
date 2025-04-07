import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the 4D vertices of a tesseract (16 points)
def get_tesseract_vertices():
    # A tesseract has 16 vertices in 4D space
    vertices = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                for w in [-1, 1]:
                    vertices.append([x, y, z, w])
    return np.array(vertices)

# Project 4D to 3D using a simple perspective projection
def project_4d_to_3d(vertices, w_dist=2.0):
    projected = []
    for vertex in vertices:
        x, y, z, w = vertex
        # Perspective projection: scale by distance from w-plane
        factor = 1 / (w_dist - w)
        proj_x = x * factor
        proj_y = y * factor
        proj_z = z * factor
        projected.append([proj_x, proj_y, proj_z])
    return np.array(projected)

# Define edges of the tesseract (32 edges)
def get_tesseract_edges():
    edges = []
    vertices = get_tesseract_vertices()
    for i, v1 in enumerate(vertices):
        for j, v2 in enumerate(vertices):
            if i < j:
                # Two vertices are connected if they differ in exactly one coordinate
                diff = np.abs(v1 - v2)
                if np.sum(diff > 0) == 1:  # Only one dimension differs
                    edges.append((i, j))
    return edges

# Rotation function in 3D space
def rotate_3d(points, angle_xy, angle_yz):
    # Rotation in XY plane
    rot_xy = np.array([
        [np.cos(angle_xy), -np.sin(angle_xy), 0],
        [np.sin(angle_xy), np.cos(angle_xy), 0],
        [0, 0, 1]
    ])
    # Rotation in YZ plane
    rot_yz = np.array([
        [1, 0, 0],
        [0, np.cos(angle_yz), -np.sin(angle_yz)],
        [0, np.sin(angle_yz), np.cos(angle_yz)]
    ])
    return points.dot(rot_xy).dot(rot_yz)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])

# Initial data
vertices_4d = get_tesseract_vertices()
vertices_3d = project_4d_to_3d(vertices_4d)
edges = get_tesseract_edges()

# Plot edges
lines = []
for edge in edges:
    line, = ax.plot(
        [vertices_3d[edge[0], 0], vertices_3d[edge[1], 0]],
        [vertices_3d[edge[0], 1], vertices_3d[edge[1], 1]],
        [vertices_3d[edge[0], 2], vertices_3d[edge[1], 2]],
        'b-'
    )
    lines.append(line)

# Set limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Projection of a Rotating Tesseract')

# Animation function
def update(frame):
    angle_xy = frame * 0.02  # Rotation speed in XY plane
    angle_yz = frame * 0.01  # Rotation speed in YZ plane
    rotated = rotate_3d(vertices_3d, angle_xy, angle_yz)
    for i, edge in enumerate(edges):
        lines[i].set_data_3d(
            [rotated[edge[0], 0], rotated[edge[1], 0]],
            [rotated[edge[0], 1], rotated[edge[1], 1]],
            [rotated[edge[0], 2], rotated[edge[1], 2]]
        )
    return lines

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=360, interval=50, blit=False
)

plt.show()