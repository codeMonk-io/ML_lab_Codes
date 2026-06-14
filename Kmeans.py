from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X)
labels = kmeans.labels_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)
