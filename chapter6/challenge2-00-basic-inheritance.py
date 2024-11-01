##  python code to use object oriented inheritence in monitoring network ports
#
#
##  Level: basic

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "I don't know what to say."

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return "Woof! Woof!"

# Creating an instance of Animal
animal = Animal("Generic Animal")
print(animal.name)  # Output: Generic Animal
print(animal.speak())  # Output: I don't know what to say.

# Creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.speak())  # Output: Woof! Woof!
