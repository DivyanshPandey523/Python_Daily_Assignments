# Python Functions
# This file contains selected beginner-friendly examples of Python functions.

# Program 1: Demonstrating built-in functions
numbers = [10, 20, 30, 40, 50]

print("Total elements:", len(numbers))
print("Sum of numbers:", sum(numbers))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
print("Data type:", type(numbers))


# Program 2: Creating and calling a simple function
def greet():
    print("Welcome to Python Functions!")


greet()


# Program 3: Using parameters and arguments
def add_numbers(a, b):
    total = a + b
    print("Sum =", total)


add_numbers(10, 20)
