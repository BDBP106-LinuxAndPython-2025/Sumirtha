N = int(input("Enter a number: "))
if N <= 1:
    print(f"{N} is not a prime number.")
elif N <= 3:
    print(f"{N} is a prime number.")
elif N % 2 == 0 or N % 3 == 0:
    print(f"{N} is not a prime number.")
else:
    i = 5
    is_prime = True
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            is_prime = False
            break
            i += 6
        if is_prime:
            print(f"{N} is a prime number.")
        else:
            print(f"{N} is not a prime number.")