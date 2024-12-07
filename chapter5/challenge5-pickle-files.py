import pickle  # Importing the pickle module for serializing and deserializing Python objects.

# Function to save data to a pickle file
def save_data_to_pickle(data, file_path):
    """
    Saves the given data to a pickle file.

    Args:
        data: The Python object to be serialized and saved.
        file_path: The path to the pickle file where data will be saved.
    """
    try:
        # Open the file in binary write mode and serialize the data using pickle
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)  # Serialize and write the data to the file.
        print(f"Data saved to {file_path}")  # Confirmation message on successful save.
    except Exception as e:
        # Handle any exception that occurs during the save process
        print(f"Error saving data to pickle file: {e}")

# Function to load data from a pickle file
def load_data_from_pickle(file_path):
    """
    Loads and returns data from a pickle file.

    Args:
        file_path: The path to the pickle file to be read.

    Returns:
        The deserialized Python object if successful, otherwise None.
    """
    try:
        # Open the file in binary read mode and deserialize the data using pickle
        with open(file_path, 'rb') as file:
            data = pickle.load(file)  # Read and deserialize the data.
        print(f"Data loaded from {file_path}")  # Confirmation message on successful load.
        return data  # Return the loaded data.
    except FileNotFoundError:
        # Handle the case where the specified file does not exist
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        # Handle any other exception that occurs during the load process
        print(f"Error loading data from pickle file: {e}")
        return None

# Entry point of the script
if __name__ == "__main__":
    # Example dictionary to be saved to a pickle file
    example_data = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Save the example data to a pickle file named 'example_data.pickle'
    save_data_to_pickle(example_data, 'example_data.pickle')

    # Load the data back from the pickle file
    loaded_data = load_data_from_pickle('example_data.pickle')

    # Display the loaded data if it was successfully retrieved
    if loaded_data:
        print("Loaded data:")
        print(loaded_data)
