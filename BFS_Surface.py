import heapq

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

def best_first_search(start, goal):
    pq = []                     # priority queue
    visited = set()
    heapq.heappush(pq, (h[start], start))

    while pq:
        heuristic, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print("Visited:", node)

        if node == goal:
            print("Goal Found!")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor))

    print("Goal Not Found")

# Driver code
best_first_search('A', 'G')

#######################################################################
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate sample n-dimensional data
data = np.random.randn(100, 4)   # 100 samples, 4 features

# Select three features for visualization
x = data[:, 0]    # Feature 1
y = data[:, 1]    # Feature 2
z = data[:, 2]    # Feature 3

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D surface plot
ax.plot_trisurf(x, y, z, cmap='viridis')

# Add labels and title
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")
ax.set_title("3D Surface Plot")

# Display plot
plt.show()