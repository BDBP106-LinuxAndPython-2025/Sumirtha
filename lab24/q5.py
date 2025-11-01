import numpy as np

def max_of_arrays(a, b):
    """Returns a new array with maximum of respective elements"""
    return np.maximum(a, b)
# Example
a = np.array([1, 2])
b = np.array([0, 5])
c = max_of_arrays(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")