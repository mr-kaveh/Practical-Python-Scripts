##  Encapsulation is a fundamental concept in object-oriented programming that 
##  restricts access to the internal state of an object and allows modification through public methods.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

# Testing the BankAccount class
account = BankAccount("Alice", 100)
print(f"Account owner: {account.owner}")

# Try accessing the private attribute directly (will raise an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

# Use public methods to interact with the balance
account.deposit(50)        # Output: Deposited 50. New balance is 150.
account.withdraw(20)       # Output: Withdrew 20. New balance is 130.
print(f"Final balance: {account.get_balance()}")  # Output: Final balance: 130
