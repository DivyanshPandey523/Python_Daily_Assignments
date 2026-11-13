# Daily Python Practice
# Some small questions for daily practice.

# 1. Swap two numbers
first_number = 10
second_number = 20

first_number, second_number = second_number, first_number
print("After swapping:", first_number, second_number)


# 2. Find the largest of three numbers
a = 15
b = 28
c = 21

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


# 3. Find the sum of digits of a number
number = 1234
total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits:", total)


# 4. Reverse a string
word = "python"
reversed_word = word[::-1]
print("Reversed word:", reversed_word)


# 5. Check whether a word is a palindrome
word = "madam"

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# 6. Count vowels in a word
word = "education"
vowel_count = 0

for letter in word:
    if letter in "aeiou":
        vowel_count = vowel_count + 1

print("Number of vowels:", vowel_count)


# 7. Find factorial of a number
number = 5
factorial = 1

for value in range(1, number + 1):
    factorial = factorial * value

print("Factorial:", factorial)
