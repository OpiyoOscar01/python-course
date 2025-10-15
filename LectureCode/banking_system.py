# Simple Banking System

# Dictionary to store account info
accounts = {}

def create_account():
    account_name = input("Enter your account name: ")
    if account_name in accounts:
        print("Account already exists!")
        return
    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Balance cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    accounts[account_name] = {"balance": initial_balance, "transactions": [f"Account created with ${initial_balance:.2f}"]}
    print(f"Account '{account_name}' created successfully!")

def deposit():
    account_name = input("Enter your account name: ")
    if account_name not in accounts:
        print("Account does not exist!")
        return
    while True:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Deposit must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    accounts[account_name]["balance"] += amount
    accounts[account_name]["transactions"].append(f"Deposited ${amount:.2f}")
    print(f"${amount:.2f} deposited successfully!")

def withdraw():
    account_name = input("Enter your account name: ")
    if account_name not in accounts:
        print("Account does not exist!")
        return
    while True:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal must be positive. Try again.")
                continue
            if amount > accounts[account_name]["balance"]:
                print("Insufficient balance! Try a smaller amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    accounts[account_name]["balance"] -= amount
    accounts[account_name]["transactions"].append(f"Withdrew ${amount:.2f}")
    print(f"${amount:.2f} withdrawn successfully!")

def check_balance():
    account_name = input("Enter your account name: ")
    if account_name not in accounts:
        print("Account does not exist!")
        return
    balance = accounts[account_name]["balance"]
    print(f"Your current balance is: ${balance:.2f}")

def show_transactions():
    account_name = input("Enter your account name: ")
    if account_name not in accounts:
        print("Account does not exist!")
        return
    print(f"Transaction history for '{account_name}':")
    for t in accounts[account_name]["transactions"]:
        print(f"- {t}")

def main():
    print("Welcome to Simple Python Bank!")
    while True:
        print("\nSelect an option:")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Show transaction history")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            show_transactions()
        elif choice == "6":
            print("Thank you for using Simple Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the banking system
if __name__ == "__main__":
    main()
