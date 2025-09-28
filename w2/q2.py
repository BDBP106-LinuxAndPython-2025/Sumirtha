#!/usr/bin
D = int(input("Enter Decimal Number D: "))
if D == 0:
    print("Binary representation is: 0")
else:
    binary = ""
    while D > 0:
        remainder = D % 2
        binary = str(remainder) + binary
        D= D// 2

    print(f"Binary representation is: {binary}")
