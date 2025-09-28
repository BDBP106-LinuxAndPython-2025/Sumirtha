#!/usr/bin
S=input("Enter string: ")
replaced=""
for i in range(len(S)):
    if S[i] == 'c':
        replaced+='d'
    else:
        replaced+=S[i]
print(replaced)