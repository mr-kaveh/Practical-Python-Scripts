#  Documentation Strings
Python is known for its simplicity, readability, and ease of use, making it a popular choice for both beginners and experienced programmers.
One of the key features that contributes to its user-friendliness is the concept of documentation strings, often referred to as "docstrings."
Docstrings are a valuable tool for creating clear and concise documentation for your Python code,
helping others (and your future self) understand how your code works, its purpose, and how to use it effectively.

## What Are Docstrings?

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition in Python.
These strings serve as documentation for the respective code element and provide information about its purpose, parameters, return values, and usage.
They are enclosed in triple-quotes (either single or double) and are typically placed immediately below the element's definition.

Here's a simple example of a function with a docstring:

> def greet(name):
>    """
>    This function takes a name as an argument and prints a greeting message.
>    
>    :param name: The name of the person to greet.
>    :type name: str
>    """
>    print(f"Hello, {name}!")
