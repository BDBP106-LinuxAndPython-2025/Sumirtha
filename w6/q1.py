class Car:
    showroom = 'NewAge'

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @classmethod
    def change_showroom(cls, new_showroom):
        cls.showroom = new_showroom

    @staticmethod
    def show_intro_message():
        print("This Car class represents a vehicle with attributes.")

# (a)
toyota_camry = Car('Toyota', 'Camry', 2022, 'Red')
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
# (b)
ford_mustang = Car('Ford', 'Mustang', 2022, 'Black')
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)
print(ford_mustang.started)
print(ford_mustang.speed)
print(ford_mustang.max_speed)
# (c)
try:
    print(Car.make)
except AttributeError as e:
    print(e)
# (d)
print(Car.__dict__)
# (e)
Car.change_showroom('Premium Motors')
print(Car.__dict__)
# (f)
print(toyota_camry.__dict__)
# (g)
print(str(toyota_camry))
print(str(ford_mustang))
# (h)
Car.show_intro_message()