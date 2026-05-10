from bank import Bank
from account import Account

print("\n\t-----Welcome to Pocket Vari Bank-----\n")
bank = Bank("Pocket Vari")

def logged_in_as_user():
    print(f"Welcome {user.name} to Pocket Vari Bank. ")

def logged_in_as_admin():
    pass

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
            bank.account_list.append(user)
        elif user_type == 'a':
            user = Account(name, email, phone, password, "admin")
            print(f"Welcome {name} to Pocket Vari Bank. Your Administrative Account number is, {user.account_no}")
            bank.account_list.append(user)
        else:
            print("Wrong Input! Try again.")
            
            
    elif op == 'l':
        user_type = input("User/Admin (u/a) : ")
        name = input("Enter your name : ")
        password = input("Password : ")
        
        for user in bank.account_list:
            if user.name == name:
                if user.password == password:
                    if user_type == 'a':
                        logged_in_as_admin()
                    else:
                        logged_in_as_user()
                else:
                    print("Sorry, Password didn't match. Try again.")
            else:
                print("Sorry, Name didn't match. Try again.")
    
    else:
        print("Wrong Input! Try again.")