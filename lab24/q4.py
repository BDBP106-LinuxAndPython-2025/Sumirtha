import numpy as np
matrix = np.random.randint(0, 10, size=(3, 3))
print("Original matrix:")
print(matrix)
# Swap first and second columns
matrix[:, [0, 1]] = matrix[:, [1, 0]]
print("\nAfter swapping columns 0 and 1:")
print(matrix)