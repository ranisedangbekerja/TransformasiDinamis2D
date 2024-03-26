#  ________________________________________________________________
# |Rani Nirmala Prakoso (22/493982/TK/54153)                       |
# |Tugas Individu: Implementasi Transformasi 2D                    |
# |________________________________________________________________|

import matplotlib.pyplot as plt
import numpy as np

def plot_shape(vertices, label):
    vertices_closed = np.vstack([vertices, vertices[0]])
    plt.plot(vertices_closed[:, 0], vertices_closed[:, 1], label=label)

def translate(vertices, dx, dy):
    translation_matrix = np.array([[1, 0, dx],
                                   [0, 1, dy],
                                   [0, 0, 1]])
    return np.dot(vertices, translation_matrix.T)

def rotate(vertices, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    return np.dot(vertices, rotation_matrix.T)

# Collect shape vertices from user
vertices_input = input("Enter the shape's vertices (format 'x1,y1 x2,y2 ...'): ")
shape_vertices = [list(map(float, vertex.split(','))) + [1] for vertex in vertices_input.split()]

# Collect translation parameters from user
dx, dy = map(float, input("Enter translation distances dx, dy (format 'dx dy'): ").split())

# Collect rotation angle from user
angle = float(input("Enter the rotation angle in degrees: "))

# Convert list of vertices into a numpy array
square_vertices = np.array(shape_vertices)

# Apply transformations
translated_square = translate(square_vertices, dx, dy)
rotated_square = rotate(translated_square, angle)

# Plotting
plt.figure()
plot_shape(square_vertices, "Original Square")
plot_shape(translated_square, "Translated Square")
plot_shape(rotated_square, "Rotated Square")

plt.title("Simulasi Transformasi Geometri pada bidang 2D oleh Rani Nirmala Prakoso")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.legend()
plt.show()
