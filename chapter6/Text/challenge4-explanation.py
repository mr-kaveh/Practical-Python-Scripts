1.  **Base Class (**`Shape`**)**: This class has an `__init__` method to initialize the name attribute and an abstract `area` method.
    
2.  **Derived Classes (**`Circle` **and** `Rectangle`**)**: Each class inherits from `Shape` and provides its own implementation of the `area` method.
    
3.  **Mathematical Calculations**:
    
    -   `Circle` uses the formula πr2\pi r^2 to calculate the area.
        
    -   `Rectangle` uses the formula width×height\text{width} \times \text{height} to calculate the area.
        
4.  **Polymorphism**: The function `print_area` demonstrates polymorphism by accepting a `Shape` object and calling its `area` method. The actual method called depends on the type of the object passed (either `Circle` or `Rectangle`).
    

This example combines object-oriented programming with some basic mathematical calculations.
