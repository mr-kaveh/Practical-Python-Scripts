
-   **Class Definition**: The `BankAccount` class has two attributes: `owner` and `__balance`. The `__balance` attribute is private, denoted by the double underscores. This means it cannot be accessed directly from outside the class.
    
-   **Constructor (**`__init__` **method)**: Initializes the `owner` and `__balance` attributes. The `balance` parameter has a default value of 0.
    
-   **Public Methods**:
    
    -   `deposit`: Adds a specified amount to the balance if it is positive.
        
    -   `withdraw`: Deducts a specified amount from the balance if it is positive and less than or equal to the current balance.
        
    -   `get_balance`: Returns the current balance.
        
-   **Testing the Class**:
    
    -   **Instance Creation**: We create a `BankAccount` instance for "Alice" with an initial balance of 100.
        
    -   **Accessing Public Attributes**: We print the account owner's name.
        
    -   **Using Methods**: We use the `deposit` and `withdraw` methods to modify the balance and print the final balance using the `get_balance` method.
        
    -   **Direct Access**: Attempting to directly access the `__balance` attribute will raise an `AttributeError`, demonstrating encapsulation.
