S = input("Enter a string: ")
index = 0
while index < len(S) and S[index] == ' ':
    index += 1
result = ""
for i in range(index, len(S)):
    result += S[i]
print("String after trimming leading spaces:", result)
