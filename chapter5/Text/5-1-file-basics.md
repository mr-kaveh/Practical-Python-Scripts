
## File Basics

Before diving into the intricacies of file handling in Python, it's crucial to understand the basic operations: opening, reading, writing, and closing files.

### Opening a File

In Python, the `open()` function is used to open a file. It takes two arguments - the file path and the mode. Modes can be 'r' for reading, 'w' for writing (creating a new file or overwriting an existing one), 'a' for appending, and 'b' for binary mode. Let's look at an example:

	# Opening a file in read mode
	file_path = "example.txt"
	file = open(file_path, 'r')

### Reading from a File

Once a file is opened, you can read its contents using various methods. The `read()` method reads the entire file, while `readline()` reads a single line. Alternatively, you can use `readlines()` to read all lines into a list.

	# Reading the entire file
	content = file.read()

	# Reading a single line
	line = file.readline()

	# Reading all lines into a list
	lines = file.readlines()

### Writing to a File

To write to a file, open it in 'w' or 'a' mode and use the `write()` method.

	# Opening a file in write mode
	file = open("output.txt", 'w')

	# Writing to the file
	file.write("Hello, this is a sample text.")

	# Closing the file
	file.close()

### Closing a File

It's crucial to close a file after performing operations on it using the `close()` method. This ensures that the resources associated with the file are properly released.

	# Closing the file
	file.close()

## Context Managers and the `with` Statement

Python supports the `with` statement, which provides a clean and efficient way to handle files. The `with` statement creates a context manager that automatically takes care of opening and closing the file.

	# Using the with statement
	file_path = "example.txt"
	with open(file_path, 'r') as file:
	    content = file.read()
	    # File is automatically closed when exiting the block

This approach is not only more concise but also ensures that the file is properly closed, even if an exception occurs within the block.

## File Object Attributes

File objects in Python have several useful attributes that provide information about the file. Some of the commonly used attributes include:

-   `name`: Returns the name of the file.
-   `mode`: Returns the access mode with which the file was opened.
-   `closed`: Returns `True` if the file is closed.

		file_path = "example.txt"
		with open(file_path, 'r') as file:
		    print("File Name:", file.name)
		    print("Access Mode:", file.mode)
		    print("Is Closed:", file.closed)

## Working with Different File Formats

Python supports various file formats, and specialized modules are available for handling them.

### CSV Files

The `csv` module simplifies reading from and writing to CSV (Comma-Separated Values) files.

	import csv

	# Reading from a CSV file
	with open('data.csv', 'r') as csvfile:
	    reader = csv.reader(csvfile)
	    for row in reader:
	        print(row)

	# Writing to a CSV file
	data = [['Name', 'Age', 'City'], ['John', 25, 'New York'], ['Alice', 30, 'San Francisco']]
	with open('output.csv', 'w', newline='') as csvfile:
	    writer = csv.writer(csvfile)
	    writer.writerows(data)

### JSON Files

The `json` module allows working with JSON (JavaScript Object Notation) files.

	import json

	# Reading from a JSON file
	with open('data.json', 'r') as jsonfile:
	    data = json.load(jsonfile)
	    print(data)

	# Writing to a JSON file
	data = {'name': 'John', 'age': 25, 'city': 'New York'}
	with open('output.json', 'w') as jsonfile:
	    json.dump(data, jsonfile)

### Pickle Files

The `pickle` module is used for serializing and deserializing Python objects. It's particularly useful when working with complex data structures.

	import pickle

	# Writing to a pickle file
	data = {'name': 'John', 'age': 25, 'city': 'New York'}
	with open('output.pkl', 'wb') as picklefile:
	    pickle.dump(data, picklefile)

	# Reading from a pickle file
	with open('output.pkl', 'rb') as picklefile:
	    loaded_data = pickle.load(picklefile)
	    print(loaded_data)

## File Navigation and Directory Operations

Python's `os` module provides functions for working with the operating system, allowing you to navigate directories, check file properties, and perform various file-related operations.

### Listing Files in a Directory

The `os.listdir()` function returns a list of files in a specified directory.

	import os

	# Listing files in the current directory
	files = os.listdir('.')
	print(files)

### Checking File Properties

The `os.path` module provides functions to check various properties of a file.

	import os

	file_path = 'example.txt'

	# Checking if a file exists
	exists = os.path.exists(file_path)
	print(f"File exists: {exists}")

	# Getting the size of a file
	size = os.path.getsize(file_path)
	print(f"File size: {size} bytes")

	# Getting the last modification time
	modification_time = os.path.getmtime(file_path)
	print(f"Last modified: {modification_time}")

### Creating and Deleting Directories

You can use `os.mkdir()` to create a new directory and `os.rmdir()` to remove an empty directory.

	import os

	# Creating a new directory
	new_directory = 'new_folder'
	os.mkdir(new_directory)

	# Removing a directory
	os.rmdir(new_directory) 

### Handling Exceptions

When working with files, it's essential to anticipate and handle potential errors, such as file not found or insufficient permissions. This is done using exception handling.

	file_path = 'nonexistent_file.txt'

	try:
	    with open(file_path, 'r') as file:
	        content = file.read()
	        print(content)
	except FileNotFoundError:
	    print(f"File not found: {file_path}")
	except Exception as e:
	    print(f"An error occurred: {e}")

By handling exceptions gracefully, your program can respond appropriately to unexpected situations, improving robustness and user experience.
