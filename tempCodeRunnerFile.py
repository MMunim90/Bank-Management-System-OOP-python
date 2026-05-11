name = input("Enter your name : ")
        password = input("Password : ")
        
        for user in bank.account_list:
            if user.name == name:
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
                print("Sorry, Name didn't match. Try again.")