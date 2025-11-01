import numpy as np

large_array = np.array([[1e10, 1.5e8, 2.3e9],
                        [5e11, 7.8e7, 9.2e10],
                        [3.4e9, 6.1e8, 1.2e11]])

print("Default (with scientific notation):")
print(large_array)
# Suppress scientific notation
np.set_printoptions(suppress=True)
print("\nWith suppressed scientific notation:")
print(large_array)
np.set_printoptions(suppress=True, precision=2, linewidth=100)
print("\nWith suppression, 2 decimals, and custom line width:")
print(large_array)

np.set_printoptions(edgeitems=3, infstr='inf', linewidth=75,
                    nanstr='nan', precision=8, suppress=False)