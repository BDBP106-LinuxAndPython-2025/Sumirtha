import numpy as np
import pandas as pd

# (i) Create 1D array from 0 to 9
arr = np.arange(10)
print("(i):", arr)

# (ii) Create boolean array 3x3
bool_arr = np.array([[True, False, True], [False, True, False], [True, False, True]])
print("\n(ii):\n", bool_arr)


# (iii) Prime numbers from 1 to 50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


arr = np.arange(1, 51)
primes = arr[[is_prime(x) for x in arr]]
print("\n(iii):", primes)

# (iv) 1D array with 20 random elements, reshape to 4x5
arr_1d = np.random.randint(0, 100, 20)
print("\n(iv) 1D array:", arr_1d)
arr_2d = arr_1d.reshape(4, 5)
print("4x5 array:\n", arr_2d)

# (v) Stack arrays horizontally
a = np.arange(10)
b = np.ones(10, dtype=int)
print("\n(v) a:", a)
print("b:", b)
stacked = np.hstack((a, b))
print("Stacked:", stacked)

# (vi) Intersection of arrays
a = np.arange(1, 101)
primes_list = []
num = 2
while len(primes_list) < 100:
    if is_prime(num):
        primes_list.append(num)
    num += 1
b = np.array(primes_list)
print("\n(vi) a:", a)
print("b:", b)
intersection = np.intersect1d(a, b)
print("Intersection:", intersection)

# (vii) Set difference a - b
difference = np.setdiff1d(a, b)
print("\n(vii) a - b:", difference)

# (viii) Indices of common elements
common_indices = np.where(np.isin(a, b))[0]
print("\n(viii) Indices:", common_indices)

# (ix) Elements > 5 and < 20
filtered = a[(a > 5) & (a < 20)]
print("\n(ix) Filtered:", filtered)