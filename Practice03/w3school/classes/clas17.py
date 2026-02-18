class Person:
    def __init__(self, name):
        self.name = name
p = Person("Alice")
p.name = "Bob"  # изменение
print(p.name)