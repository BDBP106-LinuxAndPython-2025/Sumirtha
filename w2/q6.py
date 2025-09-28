#!/usr/bin/python3
S=input("Enter String S:")
freq=0
freq_char=''
for char in S:
    count = 0
    for c in S:
        if c == char:
           count+=1
    if count>freq:
        freq=count
        freq_char=char
        print("The highest frequency character is:", freq_char)
