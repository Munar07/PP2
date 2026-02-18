class Vehicle:
    def move(self):
        print("Moving")
class Car(Vehicle):
    pass
c = Car()
c.move()