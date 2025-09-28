#!/usr/bin
S= input("Enter the string: ")
A= "c"
for i in range(len(S)):
    if S[i] == A:
        occurance_index = i
        print(f"The first occurrence is at: {[i]}")
        break

