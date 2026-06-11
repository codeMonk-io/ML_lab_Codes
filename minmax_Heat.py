def minimax(depth, node, isMax, values):

    # Leaf node reached
    if depth == 3:
        return values[node]

    if isMax:
        left = minimax(depth + 1, node * 2, False, values)
        right = minimax(depth + 1, node * 2 + 1, False, values)

        return max(left, right)

    else:
        left = minimax(depth + 1, node * 2, True, values)
        right = minimax(depth + 1, node * 2 + 1, True, values)

        return min(left, right)


values = [3, 5, 2, 9, 12, 5, 23, 23]

result = minimax(0, 0, True, values)

print("Optimal Value:", result)
########################################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate data
data = np.random.randn(100, 4)

# Convert to DataFrame
df = pd.DataFrame(data,
                  columns=['Feature1', 'Feature2',
                           'Feature3', 'Feature4'])

# Plot heatmap
sns.heatmap(df.corr(), annot=True)

plt.title('Correlation Heatmap')
plt.show()