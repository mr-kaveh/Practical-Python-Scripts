ur_age = input('How Old Are You: ')

ur_age = int(ur_age)

if ( ur_age >= 1 and ur_age < 5 ):
    print('Hello, tiny little Human')
elif ( ur_age >= 5 and ur_age < 13 ):
    print('Hello, little one')
elif ( ur_age >= 13 and ur_age <= 18 ):
    print('Hello, teenager Human')
elif ( ur_age > 18 and ur_age < 29 ):
    print('Hello, young beautiful Human')
elif ( ur_age >= 30 and ur_age < 41 ):
    print('Time to level up your life')
elif ( ur_age >= 41 and ur_age < 60 ):
    print('Wisdom is a vertue, embrace your time')
else:
    print('learn to be a child again, it is all about enjoying your life')