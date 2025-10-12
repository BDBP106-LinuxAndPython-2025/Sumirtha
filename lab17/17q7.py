import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a, b, c = 3, 4, 5
area = triangle_area(a, b, c)
print(f"Area of triangle with sides {a}, {b}, {c} is: {area}")
