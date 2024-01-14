# Define a function to generate a Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1  # Initialize the first two numbers in the sequence

    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b  # Calculate the next number in the sequence

    return fibonacci_sequence

# Prompt the user for the number of terms in the sequence
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Call the function to generate the Fibonacci sequence
fib_sequence = generate_fibonacci(num_terms)

# Display the generated sequence
print(f"The first {num_terms} terms of the Fibonacci sequence are:")
print(fib_sequence)
