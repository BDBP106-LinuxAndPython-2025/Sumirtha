L = input("Enter list of words separated by space: ").split()
k = input("Enter the character k: ")
result = []
for word in L:
    if len(word) > 0 and word[0] == k:
        result.append(word)
print(f"Words starting with '{k}':", result)