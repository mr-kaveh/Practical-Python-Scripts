# For Loop
When it comes to Python, the "for" loop is a powerful and versatile construct that allows you to perform repetitive tasks with ease. Whether you're iterating over a sequence of items, performing calculations, or interacting with data structures, the "for" loop is your trusty companion. In this article, we will explore the ins and outs of Python's "for" loop, including its syntax, common use cases, and best practices.

### 2-2-1. The Anatomy of a For Loop
The basic syntax of a "for" loop in Python is straightforward:

	for item in iterable:
		Code to be executed for each item

Here's a breakdown of the key components:

-   for: This keyword signals the start of a "for" loop.
    
-   item: This variable represents the current item being processed during each iteration.
    
-   in: This keyword separates the item variable from the iterable.
    
-   iterable: An iterable is a sequence of items (e.g., a list, tuple, string, or range) over which the loop iterates.

### 2-2-2. Iterating Over Sequences
One of the most common uses of "for" loops is to iterate over sequences of data. Let's start with a simple example, iterating over a list of numbers:

	numbers = [1, 2, 3, 4, 5]
	for num in numbers:
		print(num)

In this example, the loop iterates through each element in the numbers list, and *num* takes on the value of each element during each iteration. The result is that the numbers are printed one by one.

### 2-2-3. Iterating Over a Range

Python's range() function is often used in "for" loops to generate a sequence of numbers. The range() function creates a range object representing a sequence of numbers, and you can iterate over it:

	for i in range(5):
		print(i)

This code prints numbers from 0 to 4. The range(5) creates a sequence of numbers from 0 to 4, and the loop iterates through them.

### 2-2-4. Nested For Loops

You can also nest "for" loops within each other to work with multidimensional data. For instance, you can use nested loops to iterate over elements in a 2D list:

	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	for row in matrix:
		for element in row:
			print(element)

This code prints each element in the 2D matrix, going row by row.

### 2-2-5. Modifying Lists with For Loops

For loops can be used to modify lists, create new lists, or filter elements. For instance, let's double each element in a list:

	numbers = [1, 2, 3, 4, 5]
	doubled_numbers = []
	for num in numbers:
		doubled_numbers.append(num * 2)
		
	print(doubled_numbers)

  
In this example, we use a "for" loop to iterate through the numbers list, double each element, and append it to a new list, doubled_numbers.

#### 2-2-5-1. The enumerate() Function

Sometimes, you may want both the value and the index of an element while iterating. Python's enumerate() function comes to the rescue:

	fruits = ["apple", "banana", "cherry"]
	for index, fruit in enumerate(fruits):
		print(f"Index {index}: {fruit}")

This code prints the index and the corresponding fruit, making it easy to work with both the position and value of each element in the list.

### 2-2-6. Looping with a Condition: The break and continue Statements

In some cases, you might need to break out of a loop prematurely or skip an iteration. Python provides the break and continue statements for this purpose. Here's how they work:

**break**: This statement exits the loop entirely when a certain condition is met. For example:
    
	numbers = [1, 2, 3, 4, 5]
	for num in numbers:
		if num == 3:
			break
		print(num)

In this code, when num becomes 3, the break statement is executed, and the loop terminates.

**continue**: The continue statement skips the current iteration and proceeds to the next one. For example:

	numbers = [1, 2, 3, 4, 5]
	for num in numbers:
		if num == 3:
			continue
		print(num)

In this code, when num is 3, the continue statement is executed, skipping the print statement, and the loop continues with the next iteration.
