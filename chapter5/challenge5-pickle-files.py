import pickle

def save_data_to_pickle(data, file_path):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to pickle file: {e}")

def load_data_from_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        print(f"Data loaded from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data from pickle file: {e}")
        return None

if __name__ == "__main__":
    # Example data to save
    example_data = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Save data to pickle file
    save_data_to_pickle(example_data, 'example_data.pickle')

    # Load data from pickle file
    loaded_data = load_data_from_pickle('example_data.pickle')

    # Display loaded data
    if loaded_data:
        print("Loaded data:")
        print(loaded_data)
