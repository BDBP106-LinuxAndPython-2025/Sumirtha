def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = 10
fib = fibonacci(n)
even_fib = list(filter(lambda x: x % 2 == 0, fib))
print("Fibonacci series:", fib)
print("Even Fibonacci numbers:", even_fib)