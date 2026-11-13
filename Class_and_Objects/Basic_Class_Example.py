# Classes and Objects in Python
# A class is like a blueprint. An object is made using that blueprint.


# Program 1: Creating a simple Student class
class Student:
    def introduce(self):
        print("Hello! My name is Rahul.")
        print("I am learning Python.")


# Creating an object of the Student class
student1 = Student()
student1.introduce()


# Program 2: Using a constructor (__init__)
class StudentDetails:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_details(self):
        print("Name:", self.name)
        print("Course:", self.course)


student2 = StudentDetails("Aman", "MCA")
student2.show_details()


# Program 3: A simple Rectangle class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


rectangle1 = Rectangle(10, 5)
print("Area of rectangle:", rectangle1.calculate_area())
