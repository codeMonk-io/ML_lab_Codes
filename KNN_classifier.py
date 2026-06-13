import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("glass.csv")

# Features and Target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 70-30 Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Distance Metrics
metrics = {
    "Euclidean": "euclidean",
    "Manhattan": "manhattan"
}

# K value
k = 3

for metric_name, metric in metrics.items():

    model = KNeighborsClassifier(
        n_neighbors=k,
        metric=metric
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print(
        f"{metric_name} Distance (K={k}) Accuracy = {acc*100:.2f}%"
    )