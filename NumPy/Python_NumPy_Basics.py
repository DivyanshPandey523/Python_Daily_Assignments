# NumPy Basics
# NumPy helps us work with arrays and do calculations easily.
# If NumPy is not installed, run: pip install numpy

import numpy as np

# Creating a simple array
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)

# Checking the type and dimensions of an array
print("Type:", type(numbers))
print("Number of dimensions:", numbers.ndim)
print("Shape:", numbers.shape)

# Accessing values from an array
print("First value:", numbers[0])
print("Last value:", numbers[-1])

# Creating another array
marks = np.array([65, 70, 85, 90, 75])
print("Marks:", marks)

# Basic calculations on arrays
print("Addition:", numbers + marks)
print("Subtraction:", marks - numbers)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 10)

# Finding some useful values
print("Total:", np.sum(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))

# Joining two arrays
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
combined_array = np.concatenate((first_array, second_array))
print("Combined array:", combined_array)

# Making a 2D array (rows and columns)
table = np.array([[10, 20, 30], [40, 50, 60]])
print("2D array:")
print(table)
print("Value from first row and second column:", table[0, 1])
