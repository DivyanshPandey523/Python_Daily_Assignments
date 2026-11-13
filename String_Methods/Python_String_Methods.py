# String Methods
# Python has many useful methods for working with text.

message = "Hello Python"

# Changing the case of a string
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title case:", message.title())

# Checking the length of a string
print("Length:", len(message))

# Finding and counting characters
print("Position of Python:", message.find("Python"))
print("Count of l:", message.count("l"))

# Checking the beginning and ending of a string
print("Starts with Hello:", message.startswith("Hello"))
print("Ends with Python:", message.endswith("Python"))

# Replacing a word
new_message = message.replace("Python", "World")
print("After replacement:", new_message)

# Splitting a sentence into a list
sentence = "I like cricket and music"
words = sentence.split()
print("Words:", words)

# Joining words to make a sentence
joined_words = " ".join(words)
print("Joined sentence:", joined_words)

# Removing extra spaces from the beginning and end
name = "  Divyansh  "
print("Name:", name.strip())

# Checking the type of characters in a string
word = "Python123"
print("Only letters:", word.isalpha())
print("Only digits:", word.isdigit())
print("Letters and digits:", word.isalnum())
