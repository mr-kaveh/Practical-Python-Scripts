class SimpleDatabase:
    def __init__(self):
        self.database = {}

    def add_record(self, record_id, data):
        """
        Add a record to the database.

        Parameters:
        - record_id: Unique identifier for the record.
        - data: Dictionary representing the data associated with the record.
        """
        self.database[record_id] = data

    def get_record(self, record_id):
        """
        Retrieve a record from the database.

        Parameters:
        - record_id: Unique identifier for the record.

        Returns:
        - Dictionary representing the data associated with the record.
        """
        return self.database.get(record_id)

    def update_record(self, record_id, new_data):
        """
        Update a record in the database.

        Parameters:
        - record_id: Unique identifier for the record.
        - new_data: Dictionary representing the updated data for the record.
        """
        if record_id in self.database:
            self.database[record_id].update(new_data)
        else:
            print(f"Record with ID {record_id} not found.")

    def delete_record(self, record_id):
        """
        Delete a record from the database.

        Parameters:
        - record_id: Unique identifier for the record.
        """
        if record_id in self.database:
            del self.database[record_id]
        else:
            print(f"Record with ID {record_id} not found.")

# Example usage:
database = SimpleDatabase()

# Add records to the database
database.add_record(1, {'name': 'John', 'age': 25, 'city': 'New York'})
database.add_record(2, {'name': 'Alice', 'age': 30, 'city': 'San Francisco'})

# Retrieve and print a record
record = database.get_record(1)
print("Record 1:", record)

# Update a record
database.update_record(1, {'age': 26, 'city': 'Los Angeles'})
record_after_update = database.get_record(1)
print("Record 1 after update:", record_after_update)

# Delete a record
database.delete_record(2)
record_after_delete = database.get_record(2)
print("Record 2 after deletion:", record_after_delete)
