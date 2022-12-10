n = int(input("Please Enter Fibonacci range: ")) # Reads the input and converts it to INTEGER
a, b = 0, 1
while a < n: # While loops until this condition is true
    print(a, end=' ')
    a, b = b, a+b
print()