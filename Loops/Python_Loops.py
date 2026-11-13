# Loops in Python
# Loops help us repeat a task without writing the same code again and again.

# Using a for loop
for number in range(1, 6):
    print(number)


# Printing a multiplication table
table_number = 5

for number in range(1, 11):
    print(table_number, "x", number, "=", table_number * number)


# Adding numbers using a for loop
total = 0

for number in range(1, 6):
    total = total + number

print("Total:", total)


# Using a while loop
count = 1

while count <= 5:
    print("Count:", count)
    count = count + 1


# Printing even numbers
for number in range(2, 11, 2):
    print(number)


# Using break to stop a loop
for number in range(1, 10):
    if number == 5:
        break
    print(number)


# Using continue to skip one value
for number in range(1, 6):
    if number == 3:
        continue
    print(number)


# Looping through a list
fruits = ["apple", "mango", "orange"]

for fruit in fruits:
    print("I like", fruit)
