L = input("Enter list of numbers separated by space: ").split()
L = [int(num) for num in L]
k = int(input("Enter the value of k: "))
result = []
for item in L:
    count = 0
    for elem in L:
        if elem == item:
            count += 1
    if count > k and item not in result:
        result.append(item)
print(f"Elements occurring more than {k} times:", result)
