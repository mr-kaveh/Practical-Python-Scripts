# Caching and memoization are techniques used to store the results of
# expensive function calls and return the cached result when the same 
# inputs occur again. Python dictionaries are often employed for this purpose. 
# Here's a simple example demonstrating caching and memoization using a dictionary:

# Function for expensive computation (e.g., Fibonacci sequence)
def fibonacci(n, memo={}):
    # Check if the result is already in the memo dictionary
    if n in memo:
        return memo[n]

    # Base cases
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        # Recursive calculation with memoization
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    # Cache the result in the memo dictionary
    memo[n] = result
    return result

# Example usage:
n = 10

# Calculate Fibonacci number for n with memoization
result = fibonacci(n)

print(f"The Fibonacci number for {n} is: {result}")
