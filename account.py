import random
from bank import Bank
from datetime import datetime
class Account:
    def __init__(self, name, email, phone, password, user_type):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type
        self.account_no = self.generate_account_no(user_type)
        self.total_balance = 0
        self.loan_count = 0
        self.transaction_history = []
        
    def generate_account_no(self, user_type):
        if user_type == 'user':
            account_no = random.randint(100000, 199999)
            return account_no
        elif user_type == 'admin':
            account_no = random.randint(1000, 1999)
            return account_no
    
    def deposit(self, amount, bank):
        self.total_balance += amount
        bank.total_balance += amount
        print(f"\nDeposit {amount} taka Successfully!!!")
        print(f"Your current balance is = {self.total_balance} taka")
        self.transaction_history.append(f"Deposited {amount} taka at {datetime.now()}")
    
    def withdraw(self, amount, bank):
        if self.total_balance >= amount:
            self.total_balance -= amount
            bank.total_balance -= amount
            print(f"\nWithdraw {amount} taka Successfully!!!")
            print(f"Your current balance is = {self.total_balance} taka")
            self.transaction_history.append(f"Withdrawal {amount} taka at {datetime.now()}")
        else:
            print("Not sufficient balance.")
    
    def show_balance(self):
        print(f"Your current total balance is = {self.total_balance} taka")
    
    def show_transaction_history(self):
        print("\n\t -- Transaction History --")
        if len(self.transaction_history) == 0:
            print("No Transaction History Found")
        else:
            for history in self.transaction_history:
                print(history)
        
    def take_loan(self, amount, bank):
        if bank.loanFacility:
            if bank.total_balance > amount:
                if self.loan_count < 2:
                    self.total_balance += amount
                    bank.total_balance -= amount
                    bank.total_loan += amount
                    self.loan_count += 1
                    print(f"Congrats! You have taken a loan of {amount} taka. Your current balance is {self.total_balance} taka.")
                    self.transaction_history.append(f"Taken loan of {amount} taka at {datetime.now()}")
                else:
                    print("\nSorry. You have reached your loan taken limit. You can't take loan more than twice.")
            else:
                print("Sorry. The bank doesn't have enough money to provide loan.")
        else:
            print("Sorry. Taking loan facility is currently unavailable on our bank.")
            
    def profile_details(self):
        print("\n\t -- About --\n")
        print(f"User type: {self.user_type}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Account number: {self.account_no}")
        print(f"Password: {self.password}")
    