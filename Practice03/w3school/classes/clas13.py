class Dog:
    species = "Canine"  # class variable
    def __init__(self, name):
        self.name = name  # instance variable
d1 = Dog("Rex")
d2 = Dog("Buddy")
print(d1.name, d1.species)
print(d2.name, d2.species)