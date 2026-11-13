# Lists and Comprehensions
# A list can store multiple values in one variable.

# Creating a list
fruits = ["apple", "banana", "mango", "orange"]
print("Fruits:", fruits)

# Accessing list items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding and removing items
fruits.append("grapes")
print("After adding:", fruits)

fruits.remove("banana")
print("After removing:", fruits)

# Updating an item
fruits[1] = "watermelon"
print("Updated list:", fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)


# A simple list comprehension
numbers = [1, 2, 3, 4, 5, 6]
squares = [number * number for number in numbers]
print("Squares:", squares)

# Getting only even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

# Converting names to uppercase
names = ["rahul", "aman", "priya"]
upper_names = [name.upper() for name in names]
print("Names in uppercase:", upper_names)


# A tuple stores values that we do not want to change
colors = ("black", "white", "blue")
print("Tuple:", colors)
print("First color:", colors[0])


# A set stores unique values
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print("Unique values:", unique_numbers)


# A dictionary stores data in key-value pairs
student = {
    "name": "Aman",
    "age": 20,
    "marks": 82
}

print("Student name:", student["name"])
print("Student marks:", student["marks"])
