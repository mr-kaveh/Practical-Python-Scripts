# Input prompt
name = input("please enter your name: ")

# Start of Input Evaluation 
if(name.lower() == 'karl'):
    print(f'you have one new message {name.capitalize()}') # if it is Karl
else:
    print(f'you have no new messege(s) {name.capitalize()}') # otherwise

