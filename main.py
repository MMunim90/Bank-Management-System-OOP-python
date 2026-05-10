from bank import Bank
from account import Account

print("\n\t-----Welcome to Pocket Vari Bank-----\n")
bank = Bank("Pocket Vari")

while True:
    op = input("Register/Login (r/l) : ")
    if op == 'r':
        user_type = input("User/Admin (u/a) : ")
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        phone = input("Enter your phone no : ")
        password = input("Enter a strong password : ")
        
        if user_type == 'u':
            user = Account(name, email, phone, password, "user")
            print(f"Welcome {name} to Pocket Vari Bank. Your Account number is, {user.account_no}")