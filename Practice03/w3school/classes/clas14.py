class Car:
    wheels = 4  # class variable
    def __init__(self, color):
        self.color = color
car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, car1.wheels)
print(car2.color, car2.wheels)