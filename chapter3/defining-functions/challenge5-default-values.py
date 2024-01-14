def calculate_rectangle_area(length=5, width=3):
    """
    Calculate the area of a rectangle.

    :param length: Length of the rectangle (default is 5).
    :param width: Width of the rectangle (default is 3).
    :return: The area of the rectangle.
    """
    area = length * width
    return area

# Call the function with default values
default_area = calculate_rectangle_area()
print(f"Default Rectangle Area: {default_area}")

# Call the function with custom values
custom_area = calculate_rectangle_area(8, 4)
print(f"Custom Rectangle Area: {custom_area}")
