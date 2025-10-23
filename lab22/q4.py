import functools
def track_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        log_message = f"Function '{func.__name__}' called {wrapper.call_count} time(s)\n"
        with open("function_calls.log", "a") as log_file:
            log_file.write(log_message)
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
@track_calls
def greet(name):
    return (f"Hello, {name}!"
@track_calls)
def add(a, b):
    return a + b
print(greet("Alice"))
print(greet("Bob"))
print(add(3, 4))
print(add(10, 20))