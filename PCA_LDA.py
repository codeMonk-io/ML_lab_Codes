#PCA
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

# Reduce to 2 dimensions
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.title("PCA on Iris Dataset")

plt.show()


#LDA
from sklearn.datasets import load_iris
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

lda = LinearDiscriminantAnalysis(n_components=2)

X_lda = lda.fit_transform(X, y)

plt.scatter(
    X_lda[:, 0],
    X_lda[:, 1],
    c=y
)

plt.xlabel("LD1")
plt.ylabel("LD2")
plt.title("LDA on Iris Dataset")

plt.show()