# Perceptron Function
def perceptron(x1, x2, w1, w2, threshold):
    
    net = x1*w1 + x2*w2

    if net >= threshold:
        return 1
    else:
        return 0


# Input combinations
inputs = [
    (0,0),
    (0,1),
    (1,0),
    (1,1)
]

print("AND Gate")
for x1, x2 in inputs:
    output = perceptron(x1, x2,
                        w1=1,
                        w2=1,
                        threshold=2)

    print(x1, x2, "->", output)

print("\nOR Gate")
for x1, x2 in inputs:
    output = perceptron(x1, x2,
                        w1=1,
                        w2=1,
                        threshold=1)

    print(x1, x2, "->", output)