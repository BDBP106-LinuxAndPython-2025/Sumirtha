def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nextPrime(n):
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1
try:
    user_input = int(input("Enter an integer: "))
    prime = nextPrime(user_input)
    print(f"The first prime number larger than {user_input} is {prime}.")
except ValueError:
    print("Please enter a valid integer.")
