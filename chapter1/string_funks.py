# Define a string
my_string = "Hello, Python!"

# Access individual characters in the string
first_char = my_string[0]  # Access the first character 'H'
last_char = my_string[-1]  # Access the last character '!'

# String slicing
substring = my_string[7:13]  # Extract 'Python' from the string

# String concatenation
new_string = my_string + " Welcome!"  # Concatenate two strings

# String length
length = len(my_string)  # Get the length of the string

# String repetition
repeated_string = my_string * 3  # Repeat the string 3 times

# String methods
uppercase_string = my_string.upper()  # Convert to uppercase
lowercase_string = my_string.lower()  # Convert to lowercase
title_case_string = my_string.title()  # Convert to title case

# String formatting using f-strings (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."

# String splitting
sentence = "This is a sample sentence."
words = sentence.split()  # Split the sentence into words
# Output: ['This', 'is', 'a', 'sample', 'sentence.']

# Joining strings
word_list = ["Python", "is", "fun"]
joined_string = " ".join(word_list)  # Join words into a single string
# Output: 'Python is fun'

# Checking for substring
contains_python = "Python" in my_string  # Check if 'Python' is in the string

# String replacement
replaced_string = my_string.replace("Python", "JavaScript")  # Replace 'Python' with 'JavaScript'

# String formatting using placeholders
formatted_str = "Hello, {}. Today is {}.".format("Alice", "Monday")

# Printing the results
print("Original String:", my_string)
print("First Character:", first_char)
print("Last Character:", last_char)
print("Substring:", substring)
print("Concatenated String:", new_string)
print("String Length:", length)
print("Repeated String:", repeated_string)
print("Uppercase String:", uppercase_string)
print("Lowercase String:", lowercase_string)
print("Title Case String:", title_case_string)
print("Formatted String:", formatted_string)
print("Split Sentence:", words)
print("Joined Words:", joined_string)
print("Contains 'Python':", contains_python)
print("Replaced String:", replaced_string)
print("Formatted String (Placeholders):", formatted_str)
