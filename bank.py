class Bank:
    account_list = []
    loanFacility = True
    
    def __init__(self, name):
        self.name = name
        self.total_balance = 100000000
        self.total_loan = 0
        
    def create_account(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        
    def delete_account(self, account):
        pass
    
    def show_users(self):
        pass
    
    def show_total_balance(self):
        print(f"Total balance of the bank is = {self.total_balance} taka")
    
    def show_total_loan(self):
        pass
    
    def loan_on(self):
        pass
    
    def loan_off(self):
        pass
    
    def declare_bankrupt():
        pass