import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("titanic.csv")

# Keep useful columns
data = data[['Pclass', 'Sex', 'Age', 'Fare', 'Survived']]

# Handle missing values
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Convert Male/Female to 0/1
data['Sex'] = data['Sex'].map({
    'male': 0,
    'female': 1
})

X = data.drop('Survived', axis=1)
y = data['Survived']

# ---------- 90-10 ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("90-10 Accuracy:", accuracy_score(y_test, y_pred) * 100)
