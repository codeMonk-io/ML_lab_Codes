def alphabeta(depth, node, alpha, beta, isMax, values):

    if depth == 3:
        return values[node]

    if isMax:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1,node * 2 + i, alpha, beta, False, values)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(
                depth + 1, node * 2 + i,alpha,beta,True,values
            )
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break

        return best
    
values = [3, 5, 2, 9, 12, 5, 23, 23]
result = alphabeta( 0 , 0,float('-inf'),float('inf'),True, values )
print("Optimal Value:", result)

#######################################################################

import matplotlib.pyplot as plt
import numpy as np

# Generate sample n-dimensional data
data = np.random.randn(100, 4)   # 100 samples, 4 features

# Create box plot
plt.boxplot(data)

# Labels for each feature
plt.xticks([1, 2, 3, 4], ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])

plt.title("Box Plot of N-Dimensional Data")
plt.xlabel("Features")
plt.ylabel("Values")

plt.show()