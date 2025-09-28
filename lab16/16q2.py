#!/usr/bin/python3
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = 1
for _ in range(power):
    result *= base
print(f"{base}^{power} =", result)
