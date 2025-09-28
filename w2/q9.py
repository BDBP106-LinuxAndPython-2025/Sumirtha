#!/usr/bin
L=(input("Enter list"))
L=L.split()
L=[int(i) for i in L]
min_val = L[0]
max_val = L[0]
for numbers in L:
    if min_val < numbers:
        min_val = numbers
    elif max_val < numbers:
        max_val = numbers
print(min_val)
print(max_val)