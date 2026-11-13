# Python Basics
# Starting with some simple Python examples.

# Printing a message
print("Hello, Python!")

# Storing values in variables
name = "Divyansh"
age = 21
height = 5.10

print("Name:", name)
print("Age:", age)
print("Height:", height)

# Checking the data types
print(type(name))
print(type(age))
print(type(height))

# Taking input from the user
user_name = input("Enter your name: ")
print("Welcome", user_name)

# Converting input into a number
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# Basic arithmetic operations
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)

# Comparing two values
print("Are both numbers equal?", first_number == second_number)
print("Is first number greater?", first_number > second_number)

# Working with a string
message = "I am learning Python"

print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Number of characters:", len(message))

# Checking whether an item is present in a list
subjects = ["Python", "Maths", "English"]
print("Python" in subjects)
