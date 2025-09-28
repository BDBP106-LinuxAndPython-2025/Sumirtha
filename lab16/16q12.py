#!/usr/bin
m1=int(input("enter matrices m1:"))
m2=int(input("enter matrices m2:"))
rows = len(m1)
cols = len(m1[0])
for i in range(rows):
    for j in range(cols):
        result[i][j] = m1[i][j] - m2[i][j]
        print(result[i][j])