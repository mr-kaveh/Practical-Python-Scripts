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
## 2. Floating-Point (float)
A float is a data type used to represent real numbers, both rational and irrational, with a decimal point. Floats can also represent numbers in scientific notation, such as 1.23e-4, which stands for 0.000123. Unlike integers, which can only represent whole numbers, floats offer a much broader range of numeric values, including fractions and non-integer values.

Here's how you can declare a float variable in Python:

	my_float = 3.14

In this example, my_float is assigned the float value 3.14. Python's dynamic typing system allows variables to be reassigned with different values and types, providing great flexibility in coding.
### Float Arithmetic
Python supports a wide range of arithmetic operations for float numbers, including addition, subtraction, multiplication, division, and exponentiation. These operations are intuitive and closely resemble standard mathematical notation:

	a = 5.0
	b = 2.0
	# Addition
	sum_result = a + b # sum_result = 7.0
	# Subtraction
	difference = a - b # difference = 3.0
	# Multiplication
	product = a * b # product = 10.0
	# Division
	quotient = a / b # quotient = 2.5
	# Exponentiation
	power = a ** b # power = 25.0
Float arithmetic in Python is highly precise, allowing you to perform complex calculations with ease. However, it's crucial to be aware of potential pitfalls related to floating-point precision.

### Floating-Point Precision
Float numbers in Python, like in most programming languages, are stored as binary fractions, which can lead to precision issues when dealing with some decimal values. For example:

	result = 0.1 + 0.1 + 0.1
	print(result) # Output: 0.30000000000000004
In this case, the expected result of 0.3 is not precisely represented due to the inherent limitations of binary floating-point representation. To mitigate such issues, it's common practice to round float values when necessary:

	result = round(0.1 + 0.1 + 0.1, 2)
	print(result) # Output: 0.3
This rounding technique helps achieve the desired level of precision in floating-point calculations.
### Introducing Complex Numbers

In the realm of mathematics, complex numbers are an extension of the real numbers. While real numbers represent quantities that exist on a single number line, complex numbers encompass a broader spectrum, incorporating both real and imaginary components. The imaginary unit, represented as i or j, is the square root of -1. In Python, complex numbers are constructed using the format a + bj, where a and b are real numbers.

Here's how you can declare a complex number in Python:

	my_complex = 3 + 2j

In this example, my_complex is assigned the complex number 3 + 2j, where 3 is the real part, and 2 is the imaginary part. Python's support for complex numbers allows it to tackle a wide range of mathematical problems, including those in engineering, physics, and signal processing.

### Arithmetic Operations with Complex Numbers

Python's complex data type supports a plethora of arithmetic operations, enabling you to perform complex mathematical computations with ease. These operations include addition, subtraction, multiplication, division, modulus, and exponentiation, just as with real and float numbers. Let's explore some of these operations using complex numbers:

	a = 3 + 2j
	b = 1 - 1j
	# Addition
	sum_result = a + b # sum_result = (4 + 1j)
	# Subtraction
	difference = a - b # difference = (2 + 3j)
	# Multiplication
	product = a * b # product = (5 - 1j)
	# Division
	quotient = a / b # quotient = (2.5 + 2.5j)
	# Modulus (magnitude)
	magnitude_a = abs(a) # magnitude_a = 3.605551275463989

These operations facilitate complex number manipulation, making Python an excellent choice for scientific and engineering computations.

### Complex Conjugate

In complex number mathematics, the complex conjugate of a number a + bj is a - bj, where the sign of the imaginary part is flipped. Python provides a built-in function, conjugate(), to compute the complex conjugate of a complex number:

	a = 3 + 2j
	# Compute the complex conjugate
	conjugate_a = a.conjugate() # conjugate_a = (3 - 2j)

The complex conjugate is useful in various applications, particularly in signal processing and solving complex equations.

### Polar Representation

Complex numbers can also be represented in polar form, which expresses a complex number as a magnitude (r) and an angle (θ or phi) in radians. Python's cmath module provides functions to convert between rectangular and polar representations:

	import cmath
	z = 1 + 1j
	# Convert to polar form
	r, phi = cmath.polar(z) # r = 1.4142135623730951 (magnitude), phi = 0.7853981633974483 (angle in radians)
	# Convert back to rectangular form
	z_from_polar = cmath.rect(r, phi) # z_from_polar = (1+1j)

Polar representation is particularly useful for dealing with complex number multiplication and division.

### Decimal Numbers

  In Python, the built-in float type represents real numbers using the IEEE 754 floating-point standard. While floating-point numbers offer a broad range of values and are suitable for most applications, they exhibit limitations when it comes to precision. These limitations often lead to rounding errors and inaccuracies, which can be problematic in scenarios requiring high precision, such as financial calculations, scientific simulations, and certain engineering tasks.

This is where the decimal module comes to the rescue. Python's decimal module provides a specialized data type called Decimal, designed for precise decimal arithmetic. Unlike floats, which use binary representation, decimals store numbers in base-10, the same way humans do, making them ideal for applications where exact decimal representation is paramount.

### Introduction to the Decimal Module

To work with decimal numbers in Python, you need to import the decimal module. Here's how you can declare a decimal number:

	from decimal import Decimal
	my_decimal = Decimal('3.14')

In this example, my_decimal is assigned the Decimal object representing the decimal value 3.14. You can also create decimal numbers from floats, integers, or strings, ensuring the desired level of precision:

	# Creating a Decimal from a float
	decimal_from_float = Decimal(3.14)
	# Creating a Decimal from an integer
	decimal_from_int = Decimal(42)
	# Creating a Decimal from a string
	decimal_from_string = Decimal('123.4567890123456789012345678')

### Precise Arithmetic with Decimal Numbers

One of the standout features of the Decimal data type is its support for precise arithmetic operations. The decimal module provides a wide range of mathematical operations, including addition, subtraction, multiplication, division, and more, that adhere to the exact decimal representation:

	from decimal import Decimal
	a = Decimal('0.1')
	b = Decimal('0.2')
	# Addition
	sum_result = a + b # sum_result = Decimal('0.3')
	# Subtraction
	difference = a - b # difference = Decimal('-0.1')
	# Multiplication
	product = a * b # product = Decimal('0.02')
	# Division
	quotient = a / b # quotient = Decimal('0.5')

The precise results obtained with decimal arithmetic are invaluable in scenarios where rounding errors would be unacceptable.

### Controlling Precision

The decimal module allows you to control the precision (number of decimal places) and rounding behavior of your calculations. You can set the precision using the getcontext().prec attribute and specify the rounding mode using getcontext().rounding. For example:
	
	from decimal import Decimal, getcontext, ROUND_HALF_UP
	getcontext().prec = 10 # Set precision to 10 decimal places
	getcontext().rounding = ROUND_HALF_UP # Set rounding mode to "half up"

These settings ensure that your decimal calculations adhere to specific precision requirements.
  
### Rational Numbers

Rational numbers, often referred to as fractions, are an essential part of mathematics and everyday life. They represent values that can be expressed as the quotient of two integers—a numerator and a denominator. Unlike floating-point numbers, which can result in rounding errors, rational numbers allow for precise representation of fractions, making them indispensable in various fields, including mathematics, engineering, and finance.

Python's fractions module provides developers with the Fraction class, allowing them to work with rational numbers seamlessly.

### Introduction to the Fractions Module

To use rational numbers in Python, you need to import the fractions module. Here's how you can declare a rational number:
	
	from fractions import Fraction
	my_fraction = Fraction(3, 4)

In this example, my_fraction is assigned the Fraction object representing the fraction 3/4. The Fraction class automatically reduces fractions to their simplest form by dividing both the numerator and denominator by their greatest common divisor (GCD).
You can also create fractions from floats, integers, or strings, ensuring the desired level of precision:

	# Creating a Fraction from a float
	fraction_from_float = Fraction(0.25)
	# Creating a Fraction from an integer
	fraction_from_int = Fraction(5)
	# Creating a Fraction from a string
	fraction_from_string = Fraction('1/3')

### Fraction Arithmetic

One of the prominent features of the Fraction data type is its support for precise arithmetic operations. The fractions module provides a wide range of mathematical operations, including addition, subtraction, multiplication, division, and more, that adhere to the exact fractional representation:

	from fractions import Fraction
	a = Fraction(1, 2)
	b = Fraction(1, 4)
	# Addition
	sum_result = a + b # sum_result = Fraction(3, 4)
	# Subtraction
	difference = a - b # difference = Fraction(1, 4)
	# Multiplication
	product = a * b # product = Fraction(1, 8)
	# Division
	quotient = a / b # quotient = Fraction(2, 1)

The precise results obtained with rational arithmetic are invaluable in scenarios where rounding errors would be unacceptable.

### Fraction Limitations and Approximations

While rational numbers provide precise fractional representations, it's important to note that not all values can be exactly represented as fractions. For instance, irrational numbers like the square root of 2 or transcendental numbers like pi cannot be expressed exactly as fractions. In such cases, the Fraction class provides a way to approximate these values:

	from fractions import Fraction
	import math
	# Approximating pi as a fraction
	pi_fraction = Fraction(math.pi)

This approach allows you to obtain rational approximations of irrational or transcendental numbers.
