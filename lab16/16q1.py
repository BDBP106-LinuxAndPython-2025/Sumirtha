#!/usr/bin/python3
B = input("Enter a binary number: ")
decimal = 0
for i in range(len(B)):
    bit = int(B[-(i+1)])
    decimal += bit * (2 ** i)
print("Decimal number is:", decimal)
