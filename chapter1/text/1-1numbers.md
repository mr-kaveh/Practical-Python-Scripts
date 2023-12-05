# Numbers

Numbers are a fundamental data type in Python, and they play a crucial role in virtually every aspect of programming and data manipulation.
Python provides several types of numbers, each serving different purposes and use cases. 
In this comprehensive introduction, we will explore the various numeric data types in Python, how to perform arithmetic operations, and some common use cases for each type.

## 1.Integer

Integers, represented by the int data type, are whole numbers without a decimal point. They can be positive or negative, 
and Python allows you to perform a wide range of arithmetic operations on them.

	  x = 5
	  y = -10
	  result = x + y  # Addition
	  print(result)  # Output: -5

### Arithmetic Operations with int
Python provides a variety of arithmetic operations that can be performed on int objects. These operations include addition (+), subtraction (-), multiplication (*), division (/), modulus (%), and exponentiation (**). Let's see some examples:

	a = 10
	b = 5
	# Addition
	sum_result = a + b # sum_result = 15
	# Subtraction
	difference = a - b # difference = 5
	# Multiplication
	product = a * b # product = 50
	# Division
	quotient = a / b # quotient = 2.0
	# Modulus (remainder)
	remainder = a % b # remainder = 0
	# Exponentiation
	power = a ** b # power = 100000

These operations allow you to perform basic arithmetic calculations with ease. Python's syntax is intuitive, making it a popular choice for mathematical and scientific computing.
### Type Conversion
Sometimes, you might need to convert an int to other data types like float or str. Python provides built-in functions for such type conversions:

	my_int = 42
	# Convert int to float
	my_float = float(my_int) # my_float is now 42.0
	# Convert int to string
	my_str = str(my_int) # my_str is now "42"
These conversions are handy when you need to work with mixed data types or format integers as strings for display purposes.
