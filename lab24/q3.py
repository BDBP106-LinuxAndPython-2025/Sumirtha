import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original array:")
print(arr)
# Reverse rows (flip vertically)
reversed_rows = arr[::-1]
print("\nReversed rows:")
print(reversed_rows)
# Reverse columns (flip horizontally)
reversed_cols = arr[:, ::-1]
print("\nReversed columns:")
print(reversed_cols)