class Shape:
    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return self.side * self.side
    def __init__(self, side):
        self.side = side
sq = Square(5)
print(sq.area()) 