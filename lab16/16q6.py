S = input("Enter a string: ")
result = ""
index = 0
for char in S:
    if index % 2 == 0:
        result += char
    index += 1
print("Alternate characters:", result)