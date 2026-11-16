
# Bank Account System using OOP

class BankAccount:

    # Constructor
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")

    # Check balance
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Display account details
    def display_details(self):
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Create account
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, initial_balance)

# Menu
while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_details()

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
