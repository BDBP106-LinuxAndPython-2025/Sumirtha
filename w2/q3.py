#!/usr/bin/python3
D=int(input("Enter Decimal Number D:"))
B=0
while D > 0:
    if D % 2 == 1:
        B += 1
    D = D // 2
print("The number of 1's in binary representation is:", B)

