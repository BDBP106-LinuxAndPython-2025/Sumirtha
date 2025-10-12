import math
angles_deg = (0, 30, 45, 60, 90)
sine_cosine_list = list(map(lambda angle: (round(math.sin(math.radians(angle)), 4),
                                           round(math.cos(math.radians(angle)), 4)),
                            angles_deg))
print("List of (sin, cos) tuples:", sine_cosine_list)