class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    pass
s = Student()
s.greet()