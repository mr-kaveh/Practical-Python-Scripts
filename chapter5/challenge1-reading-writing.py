# Python code to utilize files
# create 2 files as follows

## on a Linux machine run the following commands:
# touch input_data.txt output_data.txt
# echo "let's write something" > input_data.txt

## on a windows machine run the following commands on the command prompt:
# type nul > input_data.txt
# type nul > output_data.txt
# echo "let's write something" > input_data.txt


# Input file path
input_file_path = 'input_data.txt'

# Output file path
output_file_path = 'output_result.txt'

try:
    # Reading data from the input file
    with open(input_file_path, 'r') as input_file:
        data = input_file.read()

    # Performing some processing on the data (e.g., converting to uppercase)
    processed_data = data.upper()

    # Writing the processed data to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(processed_data)

    print("File processing successful. Check the output file for results.")

except FileNotFoundError:
    print(f"Error: Input file '{input_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
