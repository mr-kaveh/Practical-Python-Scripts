
## Introduction to Object Oriented Programming
Python, a versatile and widely used programming language, supports various programming paradigms. One of the most popular and powerful paradigms in Python is Object-Oriented Programming (OOP). OOP allows developers to structure their code in a way that mirrors the real-world entities and their interactions, making it easier to design, implement, and maintain complex systems. In this comprehensive guide, we'll delve into the fundamentals of Python OOP, covering key concepts, principles, and practical examples.

### Basics of Object-Oriented Programming
1. **Classes and Objects**

At the core of Python OOP is the concept of classes and objects. A class is a blueprint or a template for creating objects, which are instances of that class. Objects encapsulate data (attributes) and behavior (methods) within a single unit, promoting code reusability and modularity.

		class Dog:
		    def __init__(self, name, age):
		        self.name = name
		        self.age = age

	    def bark(self):
	        print(f"{self.name} says Woof!")

		# Creating an object of the Dog class
		my_dog = Dog("Buddy", 3)

		# Accessing attributes and calling methods
		print(my_dog.name)  # Output: Buddy
		my_dog.bark()       # Output: Buddy says Woof!

2. **Inheritance**

Inheritance allows a class (subclass or derived class) to inherit attributes and methods from another class (base class or parent class). This promotes code reuse and establishes a hierarchy of classes.

		class Animal:
		    def __init__(self, species):
		        self.species = species

		    def make_sound(self):
		        pass

		class Cat(Animal):
		    def make_sound(self):
		        print("Meow!")

		class Dog(Animal):
		    def make_sound(self):
		        print("Woof!")

		my_cat = Cat("Felis catus")
		my_dog = Dog("Canis lupus familiaris")

		my_cat.make_sound()  # Output: Meow!
		my_dog.make_sound()  # Output: Woof!

3. **Encapsulation**
   
Encapsulation involves bundling data and methods that operate on the data within a single unit (class). Access to the internal details is controlled, often using access modifiers like public, private, and protected.

		class BankAccount:
		    def __init__(self, balance):
		        self._balance = balance  # Protected attribute

		    def deposit(self, amount):
		        self._balance += amount

		    def withdraw(self, amount):
		        if amount <= self._balance:
		            self._balance -= amount
		        else:
		            print("Insufficient funds.")

		# Creating a BankAccount object
		account = BankAccount(1000)

		# Accessing and modifying balance
		account.deposit(500)
		account.withdraw(200)
		print(account._balance)  # Output: 1300
### Advanced Concepts
1. **Polymorphism**
   
Polymorphism allows objects of different classes to be treated as objects of a common base class. This promotes flexibility and extensibility in the code.

		class Shape:
		    def area(self):
		        pass

		class Circle(Shape):
		    def __init__(self, radius):
		        self.radius = radius

		    def area(self):
		        return 3.14 * self.radius**2

		class Square(Shape):
		    def __init__(self, side):
		        self.side = side

		    def area(self):
		        return self.side**2

		# Using polymorphism
		shapes = [Circle(5), Square(4)]
		for shape in shapes:
		    print(f"Area: {shape.area()}")
2. **Composition**
   
Composition involves creating complex objects by combining simpler objects. It allows for better code organization and flexibility compared to using inheritance alone.

		class Engine:
		    def start(self):
		        print("Engine started")

		class Car:
		    def __init__(self):
		        self.engine = Engine()

		    def start(self):
		        print("Car starting...")
		        self.engine.start()

		my_car = Car()
		my_car.start()  # Output: Car starting... Engine started
3. **Abstraction**

Abstraction involves hiding the complex implementation details and exposing only the essential features of an object. This simplifies the usage of the object and reduces complexity.

		from abc import ABC, abstractmethod

		class Shape(ABC):
		    @abstractmethod
		    def area(self):
		        pass

		class Circle(Shape):
		    def __init__(self, radius):
		        self.radius = radius

		    def area(self):
		        return 3.14 * self.radius**2
