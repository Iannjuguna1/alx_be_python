# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account with a default or provided balance
        self.__account_balance = initial_balance

    def deposit(self, amount):
        # Add the deposit amount to the current balance
        self.__account_balance += amount

    def withdraw(self, amount):
        # Check if sufficient balance is available
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Display the current account balance
        print(f"Current Balance: ${self.__account_balance}")

