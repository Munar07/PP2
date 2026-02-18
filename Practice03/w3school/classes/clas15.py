class Student:
    school = "XYZ School"  # class variable
    def __init__(self, name):
        self.name = name
s1 = Student("Alice")
s2 = Student("Bob")
print(s1.name, s1.school)
print(s2.name, s2.school)