import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@measure_time
def sample_function():
    print("Function is running...")
    time.sleep(2)
    print("Function has finished!")
sample_function()