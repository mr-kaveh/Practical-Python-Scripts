import math

# Basic arithmetic operations
x = 4
y = 3

# Addition
result_add = x + y

# Subtraction
result_sub = x - y

# Multiplication
result_mul = x * y

# Division
result_div = x / y

# Exponentiation
result_pow = math.pow(x, y)

# Trigonometric functions
angle_degrees = 45

# Sine
sin_result = math.sin(math.radians(angle_degrees))

# Cosine
cos_result = math.cos(math.radians(angle_degrees))

# Tangent
tan_result = math.tan(math.radians(angle_degrees))

# Logarithmic functions
logarithm_base = 10

# Logarithm base 10
log10_result = math.log10(x)

# Natural logarithm (base e)
log_result = math.log(x)

# Constants
pi_value = math.pi
euler_constant = math.e

# Print the results
print("Basic Arithmetic Operations:")
print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")
print(f"Exponentiation: {result_pow}")

print("\nTrigonometric Functions:")
print(f"Sine({angle_degrees} degrees): {sin_result}")
print(f"Cosine({angle_degrees} degrees): {cos_result}")
print(f"Tangent({angle_degrees} degrees): {tan_result}")

print("\nLogarithmic Functions:")
print(f"Log base 10 of {x}: {log10_result}")
print(f"Natural logarithm of {x}: {log_result}")

print("\nConstants:")
print(f"Pi (π): {pi_value}")
print(f"Euler's Constant (e): {euler_constant}")
