#!/usr/bin/python3
N=int(input("Enter Natural Number:"))
if N>0:
    Result=N*(N+1)*(2*N+1)/6
    print(f"The result is: {Result}")
else:
    print("Error! Enter Natural Number")