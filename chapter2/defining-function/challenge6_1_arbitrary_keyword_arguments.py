def display_items(*items):
    for item in items:
        print(item)

# Call the function with different numbers of positional arguments
display_items("Apple", "Banana", "Cherry")
display_items("Dog", "Cat")
display_items(1, 2, 3, 4, 5)
