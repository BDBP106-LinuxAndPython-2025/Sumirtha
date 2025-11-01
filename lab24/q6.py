import numpy as np
matrix = np.random.rand(3, 3) * 100
print("Default printing:")
print(matrix)

np.set_printoptions(precision=3)
print("\nWith 3 decimal places:")
print(matrix)

np.set_printoptions(precision=3, suppress=True)
print("\nWith 3 decimals and suppression:")
print(matrix)