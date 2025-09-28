L = input("Enter list of numbers separated by space: ")
L = [int(num) for num in L]
duplicates = []
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] == L[j] and L[i] not in duplicates:
            duplicates.append(L[i])
print("Duplicate elements in the list:", duplicates)
