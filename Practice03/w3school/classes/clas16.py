class Book:
    category = "Fiction"
    def __init__(self, title):
        self.title = title
b1 = Book("Book A")
b2 = Book("Book B")
print(b1.title, b1.category)
print(b2.title, b2.category)