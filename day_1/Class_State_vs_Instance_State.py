class BankAccount:
    # Class State
    bank_name = "Global Bank"  
    interest_rate = 0.05

    def __init__(self,owner, balance):
        # Instance State
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

# Create two instances of BankAccount
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Accessing instance attributes
print(account1)  # Output: Account owner: Alice, Balance: 1000
print(account2)  # Output: Account owner: Bob, Balance: 500

# Accessing class attributes
print(account1.interest_rate)  # Output: 0.05
print(account2.interest_rate)  # Output: 0.05

# change the instance attribute
account1.balance= 1200
print(account1)  # Output: Account owner: Alice, Balance: 1200
print(account2)  # Output: Account owner: Bob, Balance: 500

# change the class attribute
BankAccount.interest_rate = 0.06
print(account1.interest_rate)  # Output: 0.06
print(account2.interest_rate)  # Output: 0.06