L=int(input("Enter List: "))
L=L.split
even_numbers = []
for num in L:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers in the list:", even_numbers)
