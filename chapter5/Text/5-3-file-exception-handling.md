# Handling File Exceptions
File operations are common in Python, whether you're reading from or writing to files. However, files can be elusive – they might not exist, have permission issues, or encounter unexpected errors. To ensure your Python scripts handle these situations gracefully, it's essential to incorporate robust file exception handling.

## The Basics of File Exception Handling:

Python provides a built-in `open()` function for file operations. When dealing with files, exceptions related to file I/O typically fall under the `FileNotFoundError` or `PermissionError` categories. To handle these exceptions, you can use a `try-except` block.

	try:
	    with open('example.txt', 'r') as file:
	        content = file.read()
	    print(f"File content: {content}")
	except FileNotFoundError:
	    print("File not found.")
	except PermissionError:
	    print("Permission error. Check file permissions.")
	except Exception as e:
	    print(f"An unexpected error occurred: {e}")

In this example:

-   A `try` block attempts to open a file ('example.txt') for reading.
-   If the file is found, its content is read.
-   If the file is not found, a `FileNotFoundError` is caught and a relevant message is displayed.
-   If there's a permission issue, a `PermissionError` is caught.
-   The generic `Exception` block catches any other unexpected errors.

## Handling Multiple Exceptions:

You can handle multiple exceptions in a single `except` block or have separate blocks for each exception type.

	try:
	    with open('example.txt', 'r') as file:
	        content = file.read()
	    print(f"File content: {content}")
	except (FileNotFoundError, PermissionError) as e:
	    print(f"An error occurred: {e}")
	except Exception as e:
	    print(f"An unexpected error occurred: {e}")

This code uses a tuple to catch either a `FileNotFoundError` or `PermissionError`. It then falls back to a generic exception block for any other unexpected errors.

## Using the `finally` Block:

The `finally` block is useful for code that must be executed regardless of whether an exception occurred. For example, closing a file should always happen, even if an error occurs.

	try:
	    with open('example.txt', 'r') as file:
	        content = file.read()
	    print(f"File content: {content}")
	except FileNotFoundError:
	    print("File not found.")
	except PermissionError:
	    print("Permission error. Check file permissions.")
	except Exception as e:
	    print(f"An unexpected error occurred: {e}")
	finally:
	    print("Closing file.")
	    file.close()

In this example, the `finally` block ensures the file is closed, regardless of whether an exception was caught.
