class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

account1 = BankAccount(1000)
account2 = BankAccount(500)
total= account1 + account2
print(total)  # Output: 1500