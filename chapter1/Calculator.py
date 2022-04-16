# Defining and Initializing the Variables
x, y = 0, 0
#2 print("X is of Type: ", type(x),"Y is of Type: ", type(y))
# Prompting the User to enter 2 integers
x ,y = input('please enter two integers [example 2,3] : ').split(',')
#2 print("After input X is of Type: ", type(x),"After input Y is of Type: ", type(y))
# Explicitly Converting input into integers 
x = int(x)
y = int(y)
# Printing the Results
print(f"First Input: {x} , Second Input: {y}, sum: {x+y}, subtraction: {x-y}, multiplication: {x*y}, division: {x/y}")

#3 z = input("please enter two more numbers [example 2,3] : ")
#3 print("Z is of Type: ", type(z))