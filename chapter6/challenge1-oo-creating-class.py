# Let's create a simple example with two classes
# one representing a Person and another representing a Car. 
# Each class will have attributes and methods to demonstrate the basics of creating classes in Python.

class Person:
    def __init__(self, name, age): # Class Constructor 
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Car:
    def __init__(self, make, model, year): # Class Constructor
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
            self.is_running = True
        else:
            print("The engine is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")
            self.is_running = False
        else:
            print("The engine is already stopped.")

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Calling methods on Person instances
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
person2.greet()  # Output: Hello, my name is Bob and I am 25 years old.

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model S", 2023)

# Calling methods on Car instances
car1.start_engine()  # Output: The 2022 Toyota Camry's engine is now running.
car2.start_engine()  # Output: The 2023 Tesla Model S's engine is now running.
car1.stop_engine()   # Output: The 2022 Toyota Camry's engine is now stopped.
car2.stop_engine()   # Output: The 2023 Tesla Model S's engine is now stopped.
