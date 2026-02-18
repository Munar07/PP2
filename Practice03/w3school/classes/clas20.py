class Circle:
    def __init__(self, radius):
        self.radius = radius
c = Circle(10)
c.radius = 15  # изменение
print(c.radius)
del c.radius