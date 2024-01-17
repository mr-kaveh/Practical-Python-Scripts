## utilize python tuples to keep immutable data

# Define a tuple to store person information (immutable data)
person_info = ("John", 25, "Male", "Engineer")

# Display the initial person information
print("Initial Person Information:")
print("Name:", person_info[0])
print("Age:", person_info[1])
print("Gender:", person_info[2])
print("Occupation:", person_info[3])

# Attempt to modify the tuple (this will result in an error)
# Uncomment the next line to see the error
# person_info[1] = 26

# Display the person information after attempting modification
print("\nPerson Information after Attempted Modification:")
print("Name:", person_info[0])
print("Age:", person_info[1])
print("Gender:", person_info[2])
print("Occupation:", person_info[3])
