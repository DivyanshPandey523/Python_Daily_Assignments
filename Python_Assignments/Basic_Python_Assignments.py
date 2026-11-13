# Basic Python Assignments
# Simple questions for beginners to practise Python.


# Question 1: Check whether a number is even or odd
number = 12

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")


# Question 2: Find the largest of three numbers
first_number = 25
second_number = 40
third_number = 15

if first_number >= second_number and first_number >= third_number:
    largest_number = first_number
elif second_number >= first_number and second_number >= third_number:
    largest_number = second_number
else:
    largest_number = third_number

print("Largest number:", largest_number)


# Question 3: Print the multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Question 4: Find the sum of numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total)


# Question 5: Find the factorial of a number
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is", factorial)
