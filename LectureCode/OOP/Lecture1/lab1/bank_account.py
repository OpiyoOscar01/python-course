class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# Using the class
acc = BankAccount("Alice", 100)
acc.deposit(50)   # Deposited $50. New balance: $150
acc.withdraw(70)  # Withdrew $70. New balance: $80
