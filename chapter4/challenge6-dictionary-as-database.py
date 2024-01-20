# use dictioneries as database
#
# Function to initialize an empty database
def initialize_database():
    return {}

# Function to add a record to the database
def add_record(database, record_id, data):
    """
    Add a record to the database.

    Parameters:
    - database: Dictionary representing the database.
    - record_id: Unique identifier for the record.
    - data: Dictionary representing the data associated with the record.
    """
    database[record_id] = data

# Function to retrieve a record from the database
def get_record(database, record_id):
    """
    Retrieve a record from the database.

    Parameters:
    - database: Dictionary representing the database.
    - record_id: Unique identifier for the record.

    Returns:
    - Dictionary representing the data associated with the record.
    """
    return database.get(record_id)

# Function to update a record in the database
def update_record(database, record_id, new_data):
    """
    Update a record in the database.

    Parameters:
    - database: Dictionary representing the database.
    - record_id: Unique identifier for the record.
    - new_data: Dictionary representing the updated data for the record.
    """
    if record_id in database:
        database[record_id].update(new_data)
    else:
        print(f"Record with ID {record_id} not found.")

# Function to delete a record from the database
def delete_record(database, record_id):
    """
    Delete a record from the database.

    Parameters:
    - database: Dictionary representing the database.
    - record_id: Unique identifier for the record.
    """
    if record_id in database:
        del database[record_id]
    else:
        print(f"Record with ID {record_id} not found.")

# Example usage:
database = initialize_database()

# Add records to the database
add_record(database, 1, {'name': 'John', 'age': 25, 'city': 'New York'})
add_record(database, 2, {'name': 'Alice', 'age': 30, 'city': 'San Francisco'})

# Retrieve and print a record
record = get_record(database, 1)
print("Record 1:", record)

# Update a record
update_record(database, 1, {'age': 26, 'city': 'Los Angeles'})
record_after_update = get_record(database, 1)
print("Record 1 after update:", record_after_update)

# Delete a record
delete_record(database, 2)
record_after_delete = get_record(database, 2)
print("Record 2 after deletion:", record_after_delete)
