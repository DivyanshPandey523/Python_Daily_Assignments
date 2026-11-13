# Python Functions
# Practising a few basic examples of functions.

# Question 1: Use some built-in functions in Python.

numbers = [10, 20, 30, 40, 50]

print("Total items:", len(numbers))
print("Sum of numbers:", sum(numbers))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# Output:
# Total items: 5
# Sum of numbers: 150
# Largest number: 50
# Smallest number: 10


# Question 2: Create a simple function to display a message.

def greet():
    print("Welcome to Python Functions!")


greet()

# Output:
# Welcome to Python Functions!


# Question 3: Create a function to add two numbers using arguments.

def add_numbers(a, b):
    total = a + b
    print("Sum =", total)


add_numbers(10, 20)

# Output:
# Sum = 30


# Question 4: Create a function that returns the sum of two numbers.

def calculate_sum(a, b):
    total = a + b
    return total


result = calculate_sum(15, 25)
print("The sum is:", result)

# Output:
# The sum is: 40


# Question 5: Create a function to check whether a number is even or odd.

def check_number(number):
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")


check_number(12)
check_number(7)

# Output:
# 12 is an even number
# 7 is an odd number


# Question 6: Create a function with a default argument.

def student_details(name, course="MCA"):
    print("Name:", name)
    print("Course:", course)


student_details("Aman")
student_details("Rohit", "BCA")

# Output:
# Name: Aman
# Course: MCA
# Name: Rohit
# Course: BCA
