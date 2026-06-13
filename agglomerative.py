from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

# Use first two features for plotting
X = iris.data[:, :2]

# Single Linkage
single = AgglomerativeClustering(
    n_clusters=3,
    linkage='single'
)
labels_single = single.fit_predict(X)

# Complete Linkage
complete = AgglomerativeClustering(
    n_clusters=3,
    linkage='complete'
)
labels_complete = complete.fit_predict(X)

# Plot Single Linkage
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels_single
)
plt.title("Single Linkage")

# Plot Complete Linkage
plt.subplot(1, 2, 2)
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels_complete
)
plt.title("Complete Linkage")

plt.show()

#load iris and features
# single linkage
# single predict

# complete linkage
# complete predict

# figure

# subplot
# scatter