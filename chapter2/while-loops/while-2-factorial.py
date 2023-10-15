# Get input from the user
num = int(input("Enter a positive integer: "))

# Initialize variables
factorial = 1
i = 1

# Check if the input is a positive integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate the factorial using a while loop
    while i <= num:
        factorial *= i
        i += 1
    
    # Display the result
    print(f"The factorial of {num} is {factorial}")
