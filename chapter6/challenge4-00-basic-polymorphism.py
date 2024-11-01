## Let's dive into some geometry. We'll create a base class called Shape and derived classes
## Circle and Rectangle that will calculate their respective areas.

## we used the math.pi constant to accurately calculate the area of a circle. 
## This library is handy for tasks like trigonometry, logarithms, factorials, and more,
## enhancing Python's built-in arithmetic capabilities.
import math

# Base class
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Function to demonstrate polymorphism
def print_area(shape):
    print(f"The area of the {shape.name} is {shape.area()}")

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Demonstrating polymorphism
print_area(circle)    # Output: The area of the Circle is 78.53981633974483
print_area(rectangle) # Output: The area of the Rectangle is 24
