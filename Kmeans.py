from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()
X = iris.data

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

# Train model
kmeans.fit(X)

# Cluster assigned to each data point
labels = kmeans.labels_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)

########################################################
import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("dataset.csv")

# Select only numerical columns
X = data.select_dtypes(include=['number'])

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

# Train model
kmeans.fit(X)

# Cluster assigned to each row
labels = kmeans.labels_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)
