# Defining/Initializing Variables
usr_input = input("please enter something to calculate: ") # Getting the input from the user

print(3 + 5)

try:
    print(usr_input)
except ValueError:
    print('Input error!')