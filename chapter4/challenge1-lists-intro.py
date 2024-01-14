# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", numbers)

# Add an element to the end of the list
numbers.append(6)
print("List after appending 6:", numbers)

# Accessing elements by index
print("Element at index 2:", numbers[2])

# Modifying an element by index
numbers[3] = 10
print("List after modifying element at index 3:", numbers)

# Removing an element by value
numbers.remove(4)
print("List after removing 4:", numbers)

# Iterating through the list
print("Iterating through the list:")
for num in numbers:
    print(num)

# Finding the length of the list
list_length = len(numbers)
print("Length of the list:", list_length)

# Sorting the list
numbers.sort()
print("Sorted list:", numbers)
