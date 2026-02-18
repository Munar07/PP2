class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def greet(self):
        super().greet()
        print("I am a student")
s = Student()
s.greet()