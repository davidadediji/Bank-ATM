# register: email, firstname, lastname, password
# login: account no, password 

import random
import datetime


avaliable_balance = 150000
naira = "N"
database= {}
current_date = datetime.datetime.now()

def init():
    is_valid_option_selected = False
    print("Welcome to Quabbly Mortgage Bank")
    now = datetime.datetime.now()
    print(f"Today is {current_date}")
    print('== ===== ========== ======')
    while is_valid_option_selected == False:
        have_account = int(input("Do you have an account with us 1. Yes 2. No \n"))
    
        if have_account == 1:
            is_valid_option_selected = True
            login()
        elif have_account == 2:
            is_valid_option_selected = True
            register()
        else:
            is_valid_option_selected = False
            print("invalid option selected, try again later")
            
def login():
    is_login = True
    print ("login to your account")
    account_number_user = int(input("Enter your account number: \n"))
    password = input("Enter your password: \n")
    for account_number,user_details in database.items():
        if account_number == account_number_user and user_details[3] == password:
            bank_operations(user_details)
        else:
            print("invalid account or password")
                
def register():
    print("*****Register*****")
    email = input("What is your email? \n")
    firstname = input("What is your firstname? \n")
    lastname = input("What is your lastname? \n")
    password = input("create a new password: \n")
    
    account_number = generate_account_number()
    print ("This is your user details, do not reveal password to anyone")
    database[account_number] = [firstname, lastname, email, password]
    
    print("Your Account has been created")
    print("== ==== ====== ===== ===")
    print("Your Account number is %d" %account_number)
    print("Make sure you keep it safe") 
    print("== ==== ====== ===== ===")
    
    login()
    
def bank_operations(user_details):
    print("Welcome %s %s" %(user_details[0], user_details[1]))
    selected_option = int(input ("What would you like to do? (1) deposit (2) withdrawal (3) complaint (4) logout (5) Exit \n"))
    
    if selected_option == 1:
        deposit_operation(user_details)
    elif selected_option == 2:
        withdrawal_operation(user_details)
    elif selected_option == 3:
        complaint(user_details)
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected! Try again")
        bank_operations(user_details)
    
def deposit_operation(user_details):
    is_deposit_operation = False
    deposit_trasaction = int(input("select (1) to deposit your cash (2) to cancel or logout \n"))
    if deposit_trasaction == 1:
        deposit = int(input("How much do you want to deposit \n"))
        print ("Trasaction in progress------>")
        current = deposit + avaliable_balance
        is_deposit_operation = True
        print ("Transaction complete \n Your new balance is: %s%d" %(naira, current))
        another_transaction(user_details)        
    elif deposit_trasaction == 2:
        logout()
    else:
        print("Invalid option, please select the right option to proceed")
        deposit_operation(user_details)
            

def withdrawal_operation(user_details):
   
    withdrawal_transaction = int(input("Enter (1) to withdraw your cash (2) to cancel or logout \n"))
    if withdrawal_transaction == 1:
        withdraw =  int(input("How much would you like to withdraw? \n"))
        amount_after_withdrawal = avaliable_balance - withdraw
        print ("Trasaction in progress------>")
        print ("You have withdrawn %d, you have %d remaining in your account."%(withdraw, amount_after_withdrawal))
        print ("Trasaction completed")
        another_transaction(user_details)
    elif withdrawal_transaction == 2:
        logout()
    else:
        print("Invalid option selected, please select the right option to proceed")
        withdrawal_operation(user_details)
    
def complaint(user_details):
    make_complain = int(input("Enter (1) For Complaints or (2) to cancel or Logout \n"))
    if make_complain == 1:
        print("Do have any challenges with any of our operations or services")
        input('Please state your complains here \n')
        print('Your response has been received and you will be attended to shortly.... Please be patient with us \n')
        another_transaction(user_details)
    elif make_complain == 2:
        logout()
    else:
        print("invalid option selected, please choose the correct option to proceed")
        complaint(user_details)
        
def logout():
    login()
    
def another_transaction(user_details):
    print("Would you like to make another transaction")
    decision = int(input("select (1) Yes (2) No- I want to logout (3) exit\n"))
    if decision == 1:
        bank_operations(user_details)
    elif decision == 2:
        logout()
    elif decision == 3:
        exit()
    else:
        print("invalid option, select the right option to proceed")
        
def generate_account_number():
    return random.randrange(1111111111, 9999999999)


####ACTUAL BANKING OPERATIONS####
init()
