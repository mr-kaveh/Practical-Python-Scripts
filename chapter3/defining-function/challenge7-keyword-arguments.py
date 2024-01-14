# here's a Python code example that utilizes keyword arguments 
# to calculate the area of different geometric shapes

def calculate_area(shape="rectangle", **kwargs):
    """
    Calculate the area of different geometric shapes.

    :param shape: The geometric shape (default is "rectangle").
    :param kwargs: Keyword arguments for shape-specific parameters.
    :return: The calculated area.
    """
    if shape == "rectangle":
        length = kwargs.get("length", 1)
        width = kwargs.get("width", 1)
        area = length * width
    elif shape == "circle":
        radius = kwargs.get("radius", 1)
        area = 3.14159 * radius ** 2
    elif shape == "triangle":
        base = kwargs.get("base", 1)
        height = kwargs.get("height", 1)
        area = 0.5 * base * height
    else:
        area = 0

    return area

# Calculate the area of a rectangle using keyword arguments
rectangle_area = calculate_area(shape="rectangle", length=5, width=3)
print(f"Rectangle Area: {rectangle_area}")

# Calculate the area of a circle using keyword arguments
circle_area = calculate_area(shape="circle", radius=2)
print(f"Circle Area: {circle_area}")

# Calculate the area of a triangle using keyword arguments
triangle_area = calculate_area(shape="triangle", base=4, height=6)
print(f"Triangle Area: {triangle_area}")
