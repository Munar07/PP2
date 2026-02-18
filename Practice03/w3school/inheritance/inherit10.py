class Vehicle:
    def move(self):
        print("Moving")
class Car(Vehicle):
    def move(self):
        print("Car is moving")
c = Car()
c.move() 