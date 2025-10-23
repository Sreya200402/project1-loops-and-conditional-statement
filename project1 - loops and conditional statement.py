#project1 - using loops and conditional statements
#console based ATM
users = {'62433570421': ['Reena', 3000, 1234],
         '62433570422': ['John', 10000, 9087],
         '62433570423': ['Alex', 4000, 1122],
         '62433570424': ['Micheal', 1000, 9988],
         '62433570425': ['Lilly', 2000, 3366]
         }

print('************WELCOME TO ATM*************')
print() #prints in new line or an empty line

acc_no = input('Please enter your account number : ')

if acc_no in users:
    
    correct_pin = users[acc_no][2]  # users is a dictinary , [acc_no] is a list from users , [2] is the index of list
    #user[acc_no] will describe the list in dictionary

    # Run loop for 3 attempts
    for attempt in range(3):
        pin = int(input("Enter your PIN: "))
        if pin == correct_pin:
            active = True
            print(f"\nWelcome {users[acc_no][0]}!")
            print("Login successful ")
            print()
            # Continue with ATM operations here
            break
        else:
            active = False
            print("Incorrect PIN.")
            if attempt < 2:  # only show attempts left if not last try
                print(f"You have {2 - attempt} attempt(s) left.")
    else:
        # This 'else' executes only if loop finishes without break
        print("Invalid password . Timeout! Please try again later.")
        
    transactions = [] #for storing transactions


    while active:
        print('Please choose your task: ')
        print(' 1.WITHDRAW')
        print(' 2.DEPOSIT')
        print(' 3.BALANCE ENQUIRY')
        print(' 4.PIN CHANGE')
        print(' 5.MINI STATEMENT')
        print(' 6.EXIT')
        Choice = int(input('Enter your choice number:'))
        
        
        if Choice == 1:
            amount = int(input("Enter the amount : "))
            if amount <= users[acc_no][1]:
                u_pin = int(input("please enter your pin:"))
                if u_pin == users[acc_no][2]:
                        users[acc_no][1] -= amount #updating dictionary
                        tra = f"{amount} withdrwan"
                        transactions.append(tra)
                        print(f"Withdraw successful.Remaining amount:{users[acc_no][1]}")
            else:
                print("Insufficient amount!!!")
                
                
        elif Choice == 2:
            amount = int(input("Enter the amount:"))
            if amount > 0 :
                users[acc_no][1] += amount
                tra = f"{amount} deposited"
                transactions.append(tra)
                print(f"Deposit Succefull!!.balance:{users[acc_no][1]}")
            else:
                print("Invalid amount")
                
                
        elif Choice == 3:
            balance = users[acc_no][1]
            print(f"Current balance : {balance}")
            
            
        elif Choice == 4:
            old_pin = int(input("Enter the old pin: "))
            if old_pin == users[acc_no][2]:
                          new_pin = int(input("Enter the new pin :"))
                          confirm_pin = int(input("Again enter the New Pin for CONFIRMATION:"))
                          if new_pin == confirm_pin :
                                   users[acc_no][2] = new_pin
                                   print("New_pin is generated successfull!!")
                          else:
                              print("Pin does not match!!")

            else:
                print("Wrong pin")
                
                                          
        elif Choice == 5:
            print("**************MINI STATEMENT******************")
            print(f"Account Holder = {users[acc_no][0]}")
            print(f"Account_no = {acc_no}")
            if len(transactions) <= 3:
                mini_stat = transactions[::-1]
            else:
                mini_stat = transaction[-1:-4:-1]
            for i in mini_stat:
                print(i)
                print()

                
        elif Choice == 6:
            print('**********THANK YOU*************')
            break
        else:
            print('INVALID CHOICE')

else:
    print("Account does not exist")


    
    
    
