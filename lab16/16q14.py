L = input("Enter list of numbers separated by space: ").split()
L = [int(num) for num in L]
element = int(input("Enter the element to remove: "))
result = []
for num in L:
    if num != element:
        result.append(num)
print("List after removing all occurrences:", result)