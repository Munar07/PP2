class Vehicle:
    def start(self):
        print("Vehicle starting")
class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine starting")
c = Car()
c.start()