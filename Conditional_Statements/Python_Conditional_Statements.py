# Conditional Statements
# We use conditions when we want our program to make a decision.

# Checking whether a number is positive, negative or zero
number = 12

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Checking whether a number is even or odd
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Finding the grade using marks
marks = 76

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Fail")


# Checking whether a person is eligible to vote
age = 19

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")


# A simple nested if example
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Please bring your ID")
else:
    print("You are not old enough")


# Checking a student's result
student_marks = 68

if student_marks >= 40:
    print("Pass")
    if student_marks >= 60:
        print("Good work!")
else:
    print("Fail")


# Checking stock in a shop
quantity = 0

if quantity == 0:
    print("Out of stock")
elif quantity <= 5:
    print("Low stock")
else:
    print("Stock available")
