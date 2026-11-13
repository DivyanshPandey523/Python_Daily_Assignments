# Generators and Iterators in Python
# These examples show how Python can give us values one by one.


# Program 1: Creating an iterator from a list
numbers = [10, 20, 30]
number_iterator = iter(numbers)

print("First value:", next(number_iterator))
print("Second value:", next(number_iterator))
print("Third value:", next(number_iterator))


# Program 2: Creating a simple generator
def show_numbers():
    yield 1
    yield 2
    yield 3


for number in show_numbers():
    print(number)


# Program 3: Generator for even numbers
def even_numbers(limit):
    number = 2

    while number <= limit:
        yield number
        number = number + 2


print("Even numbers:")
for value in even_numbers(10):
    print(value)
