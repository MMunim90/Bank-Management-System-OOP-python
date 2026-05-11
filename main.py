from bank import Bank
from account import Account
from time import sleep
import random

print("\n\t---Welcome to Pocket Vari Bank---\n")
bank = Bank("Pocket Vari")

def logged_in_as_user():
    print(f"Welcome {user.name} to Pocket Vari Bank. Your Account number is, {user.account_no}.")
    while True:
        print("________________________________________")
        print("| Press 1 for Check Balance.           |")
        print("| Press 2 for Deposit Money.           |")
        print("| Press 3 for Withdraw Money.          |")
        print("| Press 4 for Take Loan.               |")
        print("| Press 5 for Transaction History.     |")
        print("| Press 6 for Profile Details.         |")
        print("| Press 7 for Logout.                  |")
        print("|______________________________________|")
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            user.show_balance()
        elif choice == 2:
            amount = int(input("Enter the amount you want to deposit : "))
            user.deposit(amount, bank)
        elif choice == 3:
            amount = int(input("Enter the amount you want to withdraw : "))
            user.withdraw(amount, bank)
        elif choice == 4:
            amount = int(input("Enter the amount you want to take loan : "))
            user.take_loan(amount, bank)
        elif choice == 5:
            user.show_transaction_history()
        elif choice == 6:
            user.profile_details()
        elif choice == 7:
            print("Logging out...")
            sleep(random.randint(2, 3))
            break
        else:
            print("Invalid Choice.")

def logged_in_as_admin():
    print(f"Welcome {user.name} to Pocket Vari Bank. Your Administrative Account number is, {user.account_no}.")
    while True:
        print("_________________________________________")
        print("| Press 1 for Create an user account.   |")
        print("| Press 2 for Delete an user account.   |")
        print("| Press 3 for Show all users.           |")
        print("| Press 4 for Show total bank balance.  |")
        print("| Press 5 for Show total loan amount.   |")
        print("| Press 6 for Turn on loan.             |")
        print("| Press 7 for Turn off loan.            |")
        print("| Press 8 for Declare Bankrupt.         |")
        print("| Press 9 for Logout.                   |")
        print("|_______________________________________|")
        
        choice = int(input("Enter your choice : "))
        if choice == 1:
            name = input("Enter name : ")
            email = input("Enter email : ")
            phone = input("Enter phone no : ")
            password = input("Enter password : ")
            bank.create_account(name, email, phone, password, "user")
        elif choice == 2:
            account = int(input("Enter the account number you want to delete : "))
            conf = input("\nTo delete this account, type \"CONFIRM\" : ")
            if conf == 'CONFIRM':
                bank.delete_account(account)
                print("Account deleted.")
            else:
                print("Text didn't match.")
        elif choice == 3:
            bank.show_users()
        elif choice == 4:
            bank.show_total_balance()
        elif choice == 5:
            bank.show_total_loan()
        elif choice == 6:
            bank.loan_on()
        elif choice == 7:
            bank.loan_off()
        elif choice == 8:
            bankrupt = input("\nTo declare bank as bankrupt, type \"BANKRUPT\" : ")
            if bankrupt == 'BANKRUPT':
                bank.declare_bankrupt()
                print("Bank is declared as Bankrupt.")
            else:
                print("Text didn't match.")
        elif choice == 9:
            print("Logging out...")
            sleep(random.randint(2, 3))
            break
        else:
            print("Invalid Choice.")

while True:
    op = input("Register/Login/Exit (r/l/e) : ")
    if op == 'r':
        user_type = input("User/Admin (u/a) : ")
        
        if user_type == 'a' or user_type == 'u':
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            phone = input("Enter your phone no : ")
            password = input("Enter a strong password : ")
            
            if user_type == 'u':
                user = Account(name, email, phone, password, "user")
                print(f"Welcome {name} to Pocket Vari Bank. Your Account number is, {user.account_no}.")
                bank.account_list.append(user)
            elif user_type == 'a':
                user = Account(name, email, phone, password, "admin")
                print(f"Welcome {name} to Pocket Vari Bank. Your Administrative Account number is, {user.account_no}.")
                bank.account_list.append(user)
        else:
            print("Wrong Input! Try again.")
            
            
    elif op == 'l':
        user_type = input("User/Admin (u/a) : ")
        
        if user_type == 'a' or user_type == 'u':
            email = input("Enter your email : ")
            password = input("Password : ")
            
            for user in bank.account_list:
                if user.email == email:
                    if user.password == password:
                        if user_type == 'a':
                            print("Processing...")
                            sleep(random.randint(3, 5))
                            logged_in_as_admin()
                        else:
                            print("Please wait...")
                            sleep(random.randint(3, 5))
                            logged_in_as_user()
                    else:
                        print("Sorry, Password didn't match. Try again.")
                else:
                    print("Sorry, email didn't match. Try again.")
        else:
            print("Wrong Input! Try again.")
                
    elif op == 'e':
        print("Shutting down...")
        sleep(random.randint(2, 3))
        break
    
    else:
        print("Wrong Input! Try again.")