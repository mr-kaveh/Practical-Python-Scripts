import math

# 1. Calculate the area of a circle given its radius.
radius = 5
circle_area = math.pi * math.pow(radius, 2)
print(f"Area of a circle with radius {radius} is {circle_area:.2f}")

# 2. Calculate the area of a triangle using Heron's formula.
a = 7
b = 8
c = 9
s = (a + b + c) / 2
triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of a triangle with sides {a}, {b}, and {c} is {triangle_area:.2f}")

# 3. Calculate the factorial of a number using a recursive function.
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

factorial_number = 6
factorial_result = factorial_recursive(factorial_number)
print(f"Factorial of {factorial_number} is {factorial_result}")

# 4. Generate Fibonacci sequence up to a certain number of terms.
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

fibonacci_terms = 10
fib_sequence = fibonacci_sequence(fibonacci_terms)
print(f"Fibonacci sequence of {fibonacci_terms} terms: {fib_sequence}")

# 5. Calculate the square root using the Babylonian method.
def babylonian_sqrt(number, guess=1.0, tolerance=1e-6):
    while True:
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

number_for_sqrt = 20
sqrt_result = babylonian_sqrt(number_for_sqrt)
print(f"Square root of {number_for_sqrt} is approximately {sqrt_result:.6f}")

# 6. Calculate the natural logarithm (base e) of a number.
logarithm_number = 2.0
natural_log = math.log(logarithm_number)
print(f"Natural logarithm of {logarithm_number} is approximately {natural_log:.6f}")

# 7. Generate a list of prime numbers up to a specified limit.
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % prime != 0 for prime in primes)
        if is_prime:
            primes.append(num)
    return primes

prime_limit = 50
prime_numbers = generate_primes(prime_limit)
print(f"Prime numbers up to {prime_limit}: {prime_numbers}")

# 8. Calculate the sine and cosine values for a range of angles.
angle_step = 15
print(f"Angle (degrees)\tSine\t\tCosine")
for angle_degrees in range(0, 360, angle_step):
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    print(f"{angle_degrees}\t\t{sin_value:.4f}\t\t{cos_value:.4f}")

# 9. Calculate the area under a curve using the trapezoidal rule.
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

def example_function(x):
    return x**2  # Replace with your own function

a_integral = 0
b_integral = 4
n_intervals = 100
area_under_curve = trapezoidal_rule(example_function, a_integral, b_integral, n_intervals)
print(f"Approximate area under the curve: {area_under_curve:.4f}")

# 10. Calculate the greatest common divisor (GCD) of two numbers.
num1 = 36
num2 = 48
gcd = math.gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {gcd}")

# 11. Calculate the exponential value of a number.
exponential_base = 2.0
exponential_power = 3.0
exponential_result = math.pow(exponential_base, exponential_power)
print(f"{exponential_base} raised to the power of {exponential_power} is {exponential_result}")

# 12. Calculate the hyperbolic sine and cosine.
hyperbolic_x = 2.0
sinh_value = math.sinh(hyperbolic_x)
cosh_value = math.cosh(hyperbolic_x)
print(f"Hyperbolic sine of {hyperbolic_x} is {sinh_value:.4f}")
print(f"Hyperbolic cosine of {hyperbolic_x} is {cosh_value:.4f}")

# 13. Calculate the gamma function of a number.
gamma_number = 5.0
gamma_result = math.gamma(gamma_number)
print(f"Gamma function of {gamma_number} is {gamma_result:.4f}")

# 14. Calculate the error function (Erf) of a number.
erf_number = 0.5
erf_result = math.erf(erf_number)
print(f"Error function (Erf) of {erf_number} is {erf_result:.4f}")

# 15. Generate a list of random numbers between 0 and 1.
import random
random_numbers = [random.random() for _ in range(10)]
print(f"Random numbers between 0 and 1: {random_numbers}")

# 16. Calculate the power of 10 using the pow() function.
power_of_ten = math.pow(10, 3)
print(f"10 raised to the power of 3 is {power_of_ten}")

# 17. Calculate the least common multiple (LCM) of two numbers.
lcm_num1 = 12
lcm_num2 = 18
lcm = lcm_num1 * lcm_num2 // math.gcd(lcm_num1, lcm_num2)
print(f"LCM of {lcm_num1} and {lcm_num2} is {lcm}")

# 18. Calculate the absolute value of a number.
negative_number = -7
absolute_value = abs(negative_number)
print(f"Absolute value of {negative_number} is {absolute_value}")

# 19. Round a floating-point number to a specified number of decimal places.
float_number = 3.141592653589793
rounded_float = round(float_number, 2)
print(f"Rounded value of {float_number} to 2 decimal places is {rounded_float}")