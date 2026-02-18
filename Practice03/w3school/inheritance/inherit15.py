class Father:
    def hobby(self):
        print("Fishing")
class Mother:
    def hobby(self):
        print("Painting")
class Child(Father, Mother):
    def hobby(self):
        print("Playing")
c = Child()
c.hobby()