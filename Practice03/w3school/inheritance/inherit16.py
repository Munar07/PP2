class Engine:
    def start(self):
        print("Engine starting")
class GPS:
    def start(self):
        print("GPS starting")
class Car(Engine, GPS):
    pass
car = Car()
car.start() 