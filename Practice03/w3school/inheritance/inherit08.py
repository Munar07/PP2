class Shape:
    def info(self):
        print("This is a shape")
class Circle(Shape):
    def info(self):
        super().info()
        print("This is a circle")
c = Circle()
c.info()