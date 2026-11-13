# Logic Practice
# A few questions to improve basic problem-solving skills.

# 1. Check whether a number is prime
number = 17
is_prime = True

if number <= 1:
    is_prime = False
else:
    for value in range(2, number):
        if number % value == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# 2. Print the Fibonacci series
first = 0
second = 1

for count in range(7):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number

print()


# 3. Check whether a number is an Armstrong number
number = 153
original_number = number
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** 3
    number = number // 10

if total == original_number:
    print(original_number, "is an Armstrong number")
else:
    print(original_number, "is not an Armstrong number")


# 4. Make a simple calculator
first_number = 12
second_number = 4
operator = "*"

if operator == "+":
    print("Answer:", first_number + second_number)
elif operator == "-":
    print("Answer:", first_number - second_number)
elif operator == "*":
    print("Answer:", first_number * second_number)
elif operator == "/":
    if second_number != 0:
        print("Answer:", first_number / second_number)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 5. Find the largest digit in a number
number = 5832
largest_digit = 0

while number > 0:
    digit = number % 10

    if digit > largest_digit:
        largest_digit = digit

    number = number // 10

print("Largest digit:", largest_digit)
