import math
def population_growth(initial,rate, time):
    def exponential_growth():
        No=initial
        for i in range(time):
            return initial*math.exp(rate*time)
    population=exponential_growth()
print(population_growth(1000,0.5,10))