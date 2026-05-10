import random
from bank import Bank

class Account:
    def __init__(self, name, email, phone, password, user_type):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type
        self.account_no = self.generate_account_no()
        self.total_balance = 0
        self.loan_count = 0
        self.transaction_history = []
        
    def generate_account_no(self):
        account_no = random.randint(100000, 199999)
        return account_no
    
    def deposit(self, amount, bank):
        self.total_balance += amount
        bank.total_balance += amount
        print(f"Deposit {amount} taka Successfully!!!")
        print(f"Current balance is = {self.total_balance} taka")
        self.transaction_history.append(f"Deposited {amount} taka.")
    
    def withdraw():
        pass
    
    def show_balance(self):
        print(f"Your total balance is = {self.total_balance} taka")
    
    def show_transaction_history():
        pass
        
    def take_loan():
        pass
    
    def delete_account(self):
        pass
    
    