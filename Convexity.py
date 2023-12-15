import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define your cost function f(x, y) here (e.g., f(x, y) = x^2 + y^2)
# convexity
def cost_function(x, y):
    return x ** 2 + y ** 2


# Define the domain of interest for x and y
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_values, y_values)

# Calculate the corresponding function values
Z = cost_function(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the cost function surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Choose two points (x1, y1) and (x2, y2)
x1, y1 = -2, -2
x2, y2 = 2, 2

# Calculate function values at (x1, y1) and (x2, y2)
z1 = cost_function(x1, y1)
z2 = cost_function(x2, y2)


# Define the tangent plane equation
def tangent_plane(x, y):
    return z1 + (x - x1) * (z2 - z1) / (x2 - x1) + (y - y1) * (z2 - z1) / (y2 - y1)


# Plot the tangent plane
ax.plot_surface(X, Y, tangent_plane(X, Y), alpha=0.5, color='r')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.show()
