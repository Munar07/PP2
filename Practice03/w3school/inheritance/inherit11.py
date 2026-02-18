class Person:
    def greet(self):
        print("Hello")
class Student(Person):
    def greet(self):
        print("Hi, I am a student")
s = Student()
s.greet() 