class Bank:
    account_list = []
    loanFacility = True
    is_BankRupt = False
    
    def __init__(self, name):
        self.name = name
        self.total_balance = 100000000
        self.total_loan = 0
        
    def create_account(self, name, email, phone, password, user_type):
        from account import Account
        user = Account(name, email, phone, password, user_type)
        self.account_list.append(user)
        
    def delete_account(self, account):
        for person in self.account_list:
            if person.account_no == account:
                self.account_list.remove(person)
                self.total_balance -= person.total_balance
    
    def show_users(self):
        for user in self.account_list:
            print(f"Name: {user.name} Account no. {user.account_no} Email: {user.email} Phone: {user.phone} User type: {user.user_type}")
    
    def show_total_balance(self):
        print(f"Total balance of the bank is = {self.total_balance} taka")
    
    def show_total_loan(self):
        print(f"Total loan on the bank is = {self.total_loan} taka.")
    
    def loan_on(self):
        print("Loan facility is set to ON.")
        self.loanFacility = True
    
    def loan_off(self):
        print("Loan facility is set to OFF.")
        self.loanFacility = False
    
    def declare_bankrupt(self):
        self.is_BankRupt = True