# Example 1: Using lambda functions to perform simple operations
add = lambda x, y: x + y
multiply = lambda x, y: x * y

result1 = add(5, 3)
result2 = multiply(4, 6)

print("Result of addition:", result1)
print("Result of multiplication:", result2)

# Example 2: Using lambda functions for sorting
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 28},
]

# Sort students by age using a lambda function
students.sort(key=lambda student: student["age"])
print("Students sorted by age:", students)

# Example 3: Using lambda functions with built-in functions
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# Filter even numbers using a lambda function with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Calculate the sum of numbers using a lambda function with reduce
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)
