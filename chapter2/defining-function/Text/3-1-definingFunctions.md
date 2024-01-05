
# Defining Functions

## Introduction to Functions
A function is a named sequence of statements that performs a specific task. In Python, functions are used to organize and reuse code, making it more manageable and efficient. Functions can take inputs (parameters) and produce outputs (return values).

## 2. Defining a Function
To define a function in Python, you use the `def` keyword followed by the function name and a set of parentheses. Here's the basic syntax:

	def function_name(parameters):
	    # Function code
	    # ...
	    return result  # Optional

`def greet(name):
    return f"Hello, {name}!"

## 3. Function Parameters
Functions can accept parameters (inputs) that provide data for the function to work with. Parameters are defined within the parentheses of the function definition. You can have multiple parameters separated by commas.

	def add(x, y):
	    return x + y` 

## 4. Return Values

Functions can return values using the `return` statement. The `return` statement terminates the function and sends a value back to the caller.

	def square(x):
	    return x ** 2

## 5. Function Scope

Python uses a concept called "scope" to determine the visibility and lifetime of variables. Variables defined inside a function have local scope, while those defined outside functions have global scope.

	global_var = 10  # Global variable
	def func():
	    local_var = 5  # Local variable
	    return global_var + local_var

## 6. Lambda Functions

Lambda functions, also known as anonymous functions, are small, unnamed functions defined using the `lambda` keyword. They are often used for simple, one-line operations.

	square = lambda x: x ** 2
	# Use the lambda function
	result = square(5)
	print(result)  # Output: 25` 

## 7. Recursion

Recursion is a programming technique where a function calls itself to solve a problem. Recursive functions are useful for solving problems that can be broken down into smaller, similar sub-problems.

	def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

## 8. Decorators

Decorators are a powerful and advanced Python feature. They allow you to modify or enhance the behavior of functions or methods without changing their code.

	def my_decorator(func):
	    def wrapper():
	        print("Something is happening before the function is called.")
	        func()
	        print("Something is happening after the function is called.")
	    return wrapper

	@my_decorator
	def say_hello():
	    print("Hello!")

	say_hello()

# Python Function Argument Types

In Python, you can define functions with various types of function arguments. Function arguments allow you to pass data into a function. Here are the different types of function arguments in Python:

## Positional Arguments:

Positional arguments are the most common type of function arguments. They are passed to a function in the order in which they are defined in the function's parameter list.

	def greet(name, age):
	    print(f"Hello, {name}! You are {age} years old.")

	greet("Alice", 30)

## Keyword Arguments:

Keyword arguments allow you to pass arguments to a function by explicitly specifying the parameter name they correspond to.

	greet(age=25, name="Bob")

## Default Arguments:

Default arguments have predefined values in the function's parameter list. If an argument is not provided when calling the function, the default value is used.

	def greet(name, age=18):
	    print(f"Hello, {name}! You are {age} years old.")

	greet("Charlie")  # age defaults to 18

## Arbitrary Positional Arguments (args):

You can use the `*args` syntax to accept a variable number of positional arguments. These arguments are collected into a tuple within the function.

	def print_args(*args):
	    for arg in args:
	        print(arg)

	print_args(1, 2, 3)

## Arbitrary Keyword Arguments (kwargs):

You can use the `**kwargs` syntax to accept a variable number of keyword arguments. These arguments are collected into a dictionary within the function.

	def print_kwargs(**kwargs):
	    for key, value in kwargs.items():
	        print(f"{key}: {value}")

	print_kwargs(name="David", age=28, city="New York")

## Combining All Types:

You can combine positional arguments, default arguments, `*args`, and `**kwargs` in a single function definition.
	
	def complex_function(name, age=18, *args, **kwargs):
	    print(f"Name: {name}, Age: {age}")
	    print("Additional positional arguments:", args)
	    print("Additional keyword arguments:", kwargs)

	complex_function("Eve", 30, 1, 2, 3, city="London", country="UK")

These different types of function arguments provide flexibility in how you can call and use functions in Python, making your code more versatile and adaptable to various scenarios.

## 4.8.1. Default Argument Values

In Python, when defining a function, you can provide default argument values for some or all of the function's parameters. Default argument values allow you to specify a default value for a parameter, so if the caller doesn't provide a value for that parameter, the default value is used instead.

Here's the syntax for defining a function with default argument values:


	def function_name(parameter1=default_value1, parameter2=default_value2,...):
    # Function code` 

-   `function_name`: The name of the function.
-   `parameter1, parameter2, etc.`: The parameters that the function accepts.
-   `default_value1, default_value2, etc.`: The default values assigned to the parameters. If the caller doesn't provide a value for a parameter, these default values will be used.

Here are some key points to understand about default argument values in Python:

-   Default Values are Optional: If a caller provides a value for a parameter, that value will be used, even if a default value is specified in the function definition. Default values are only used when the caller doesn't provide a value for the parameter.
    
-   Default Values Should Be Immutable: When specifying default values, it's a good practice to use immutable data types like numbers, strings, or tuples. Avoid using mutable types like lists or dictionaries, as they can lead to unexpected behavior due to sharing the same object across multiple function calls.
    
-   Default Values Are Evaluated Once: The default values are evaluated when the function is defined, not each time the function is called. This means if you use mutable objects as default values, changes to those objects persist across function calls.
    
-   Default Values in Order: When defining a function with multiple parameters, parameters with default values should come after parameters without default values. This is because arguments are passed by position, and you can't omit a parameter with a default value and specify one that comes after it.
    

Here's an example of a function with default argument values:

	def greet(name, greeting="Hello"):
	    print(f"{greeting}, {name}!")
		
	# Call the function with and without providing the greeting parameter
	greet("Alice")  # Uses the default greeting
	greet("Bob", "Hi")  # Overrides the default greeting

In this example, the `greet` function has a default value of "Hello" for the `greeting` parameter. You can call the function with or without specifying the greeting, and it will use the default value if not provided.

Default argument values are a useful feature in Python, making functions more flexible and user-friendly by allowing callers to provide only the necessary arguments while still having the option to override defaults when needed.

## Keyword Arguments

In Python, keyword arguments are a way to pass arguments to a function using parameter names or keywords, which makes the code more readable and allows you to provide arguments in a different order from the function's parameter list. Keyword arguments are also known as named arguments.

To use keyword arguments in a function call, you specify the parameter name followed by a colon (:) and the value you want to assign to that parameter. Here's the basic syntax:

	function_name(param_name1=value1, param_name2=value2, ...)

Here are some key points to understand about keyword arguments:

-   Order Independence: When using keyword arguments, you can provide the arguments in any order you like, as long as you specify the parameter names. This can be particularly useful for functions with a large number of parameters, as it makes the code more self-explanatory.
    
-   Readability: Keyword arguments improve the readability of function calls, especially when the function has many parameters with similar data types. They help make the code more self-documenting.
    
-   Default Values: Keyword arguments can be used to override default parameter values set in the function definition. If you only want to change one or a few arguments, you can use keyword arguments without specifying the rest.
    

Here's an example of a function call using keyword arguments:

	def greet(name, greeting="Hello", punctuation="!"):
	    full_greeting = f"{greeting}, {name}{punctuation}"
	    return full_greeting

	# Call the function using keyword arguments
	result = greet(name="Alice", greeting="Hi", punctuation=".")
	print(result)

In this example, we use keyword arguments to call the `greet` function. We specify the values for the `name`, `greeting`, and `punctuation` parameters using their names. This allows us to change the greeting and punctuation while keeping the default "name" parameter.

Keyword arguments are a powerful and flexible feature in Python that contributes to code clarity and allows you to tailor function calls to specific needs without relying on the order of parameters in the function's definition.

## Keyword-only Arguments

In Python, keyword-only arguments are function parameters that can only be passed by specifying their names in a function call. They are defined using the `*` symbol in a function definition, indicating that all parameters following it must be passed as keyword arguments. Keyword-only arguments are useful when you want to make it explicit that certain parameters should not be passed positionally and should be provided as keyword arguments for clarity and to prevent potential confusion.

Here's how you define keyword-only arguments in a function:


	def function_name(param1, param2, *, keyword_param1, keyword_param2):
	    # Function code

In this definition:

-   `param1` and `param2` are regular positional parameters.
-   `*` acts as a separator, indicating that all parameters following it must be passed as keyword arguments.
-   `keyword_param1` and `keyword_param2` are keyword-only arguments.

Key points to understand about keyword-only arguments:

-   Clarity: Keyword-only arguments make it clear which parameters need to be passed as keyword arguments. This can improve the readability of function calls and reduce the risk of misinterpretation.
    
-   Enforcing Keyword Arguments: By using keyword-only arguments, you enforce that certain parameters must be passed as keyword arguments. This can be particularly useful for functions with many parameters, some of which should not be passed positionally.
    
-   Positional and Default Arguments: You can have a combination of regular positional parameters, default arguments (with or without keyword-only arguments), and keyword-only arguments in a function definition.
    

Here's an example of a function using keyword-only arguments:

	def divide(dividend, divisor, *, verbose=False):
    if divisor == 0:
        return "Error: Division by zero"
    result = dividend / divisor
    if verbose:
        return f"{dividend} / {divisor} = {result}"
    return result
	# Using keyword-only argument 'verbose'
	result = divide(10, 2, verbose=True)
	print(result)

In this example, the `divide` function takes `dividend` and `divisor` as positional parameters and a keyword-only argument `verbose`. The `verbose` argument must be provided as a keyword argument. When `verbose=True`, it provides additional details about the division.

To call this function, you must use keyword syntax for the `verbose` argument to make it clear that it's being passed as a keyword-only argument.

Keyword-only arguments in Python help improve code clarity and enforce how certain parameters are passed, making the intention of the function call more explicit.

## Lambda Functions

Python is a versatile and powerful programming language that offers a wide array of features to developers. One such feature is the lambda function, also known as an anonymous function. Lambda functions provide a concise and expressive way to create small, inline functions. In this article, we will explore what lambda functions are, how to use them, and their practical applications.

### What Are Lambda Functions?

A lambda function is a small, unnamed function that can have any number of arguments, but can only have one expression. These functions are also known as anonymous functions because they don't require a formal `def` statement to define them. Instead, they are typically defined using the `lambda` keyword.

The basic syntax of a lambda function is as follows:

	lambda arguments: expression

Here, `arguments` are the input parameters, and `expression` is the operation that the function will perform on these arguments. Lambda functions are concise and often used when you need a simple function for a short period and don't want to define a full function using `def`.

### Using Lambda Functions

Lambda functions are most commonly used in the following scenarios:

1.  **Inline Functions** Lambda functions are perfect for situations where you need a quick, one-off function, especially when passing functions as arguments to other functions, like in the `map`, `filter`, or `sorted` functions.
    
		numbers = [1, 2, 3, 4, 5]
	    squared = list(map(lambda x: x ** 2, numbers))
	    # Output: [1, 4, 9, 16, 25]` 
    
2.  **Short, Simple Functions** When the function logic is straightforward and concise, using a lambda function can make the code more readable and less cluttered.
    
		add = lambda a, b: a + b
	    result = add(3, 5)
	    # Output: 8` 
    
3.  **Sort and Filter** Lambda functions are commonly used with the `sorted` and `filter` functions to customize sorting or filtering operations.

		points = [(1, 2), (3, 1), (0, 4)]
		sorted_points = sorted(points, key=lambda point: point[1])
		# Output: [(3, 1), (1, 2), (0, 4)]

		even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
		# Output: [2, 4]
