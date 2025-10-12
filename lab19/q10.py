import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper
@measure_time
def population_growth(initial_population, growth_rate, iterations):
    population = initial_population
    for _ in range(iterations):
        population += population * growth_rate
    return population
final_population = population_growth(1000, 0.00002, 1000000)  # small growth rate
print("Final population:", round(final_population))
