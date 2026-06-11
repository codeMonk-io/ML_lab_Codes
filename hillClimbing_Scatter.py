# Hill Climbing Algorithm Example
# Problem: Minimize f(x) = (x - 3)^2

import random

# Objective function
def cost(x):
    return (x - 3) ** 2

# Start with a random value
current = random.randint(-10, 10)

while True:
    # Generate neighbors
    left = current - 1
    right = current + 1

    # Choose the better neighbor
    if cost(left) < cost(current):
        current = left
    elif cost(right) < cost(current):
        current = right
    else:
        # No better neighbor found
        break

print("Best Solution (x):", current)
print("Minimum Cost:", cost(current))

#####################################################################

import matplotlib.pyplot as plt
import numpy as np

# Generate sample n-dimensional data
data = np.random.randn(100, 4)   # 100 samples, 4 features

# Select two features for visualization
x = data[:, 0]   # Feature 1
y = data[:, 1]   # Feature 2

# Create scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.title("Scatter Plot (Feature1 vs Feature2)")

# Display plot
plt.show()