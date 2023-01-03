
from src.colors import bcolors
from src.calculator import Calculator

# initiate the global variables as floats and integers
balance_in_checking = float
accounts_to_pay = int 
# initiate a length counter for the amount of accounts
length_counter = '1'
# initiate a counter for account(s) 1 - n
ticker = 0

def questions():
    global balance_in_checking
    global accounts_to_pay
    while True:
        try:
            balance_in_checking = float(input("How much money do we have to work with? (Usually the money in your checking)\nAnswer in dollars and cents: "))
            break
        except:
            print(bcolors.FAIL + 'ERROR. YOU MUST ENTER THE VALUE IN DOLLARS AND CENTS!' + bcolors.ENDC)
    while True:
        try:
            accounts_to_pay = int(input("How many accounts do you have to pay today? "))
            break
        except:
            print(bcolors.FAIL + 'ERROR. YOU MUST ENTER AN INTEGER!' + bcolors.ENDC)

def dictionary_work():
    # calling the global variables
    global balance_in_checking
    global accounts_to_pay
    global length_counter
    global ticker
    # initiate the dictionaries
    accounts_and_balances = {}
    accounts_min_payments = {}
    # use length counter to create a length for the loop (1*n)
    num_of_accounts = accounts_to_pay*length_counter
    # start the summary string for csv file creation
    summary_string = "ACCOUNT, PAYMENT, FINAL BALANCE\n"

    for i in range(len(num_of_accounts)):
        ticker += 1
        names = str(input(f'Please name account {ticker} '))
        while True:
            try:
                balances = float(input(f"Please enter the " + bcolors.BOLD + "balance" + bcolors.ENDC +  f" of " + bcolors.BOLD + f'{names}' + bcolors.ENDC + " in dollars and cents: "))
                break
            except:
                print(bcolors.FAIL + "INVALID INPUT." + bcolors.ENDC)
        while True:
            try:
                min_payment = float(input(f"What is the " + bcolors.BOLD + "minimum amount owed" + bcolors.ENDC + f" on account: " + bcolors.BOLD +  f'{names} ' + bcolors.ENDC))
                break
            except:
                print(bcolors.FAIL + "INVALID INPUT." + bcolors.ENDC)
        
        accounts_and_balances[names] = balances
        accounts_min_payments[names] = min_payment

    sum_of_accounts = round(sum(accounts_and_balances.values()),2)
    sum_of_min_payments = round(sum(accounts_min_payments.values()))
    sub1 = Calculator(balance_in_checking, sum_of_accounts)
    if_payed_in_full = sub1.subtract()
    sub2 = Calculator(balance_in_checking, sum_of_min_payments)
    if_payed_min = sub2.subtract()
    print(bcolors.BOLD + "Okay, to recap, here's what your accounts look like:" + bcolors.ENDC)
    print(bcolors.BOLD + "-----------------------------------------------------" + bcolors.ENDC)
    for i,j in accounts_and_balances.items():
        print(bcolors.BOLD + f'{i}: {j}' + bcolors.ENDC)
    for i, j in accounts_min_payments.items():
        print(bcolors.BOLD + f'{i} | min payment: {j}' + bcolors.ENDC)
    print(bcolors.BOLD + f'--------------------------\nTOTAL AMOUNT OWED: {sum_of_accounts}' + bcolors.ENDC)
    print(bcolors.BOLD + f'TOTAL AMOUNT OF MIN PAYMENTS: {sum_of_min_payments}\n' + bcolors.ENDC)
    print('If you payed the total amount, your account would have a final balance of: ' + bcolors.BOLD + f'{if_payed_in_full}' + bcolors.ENDC)
    print('If you payed ' + bcolors.BOLD + 'ONLY ' + bcolors.ENDC + 'The minimum amount, your account would have a final balance of: ' + bcolors.BOLD + f'{if_payed_min}' + bcolors.ENDC)
    for i,j in accounts_and_balances.items():
        print('You owe: ' + bcolors.BOLD + f'${round(j,2)}' + bcolors.ENDC + ' on account: ' + bcolors.BOLD + f'{i}' + bcolors.ENDC)
        while True:
            try:
                payment = float(input('How much would you like to pay? '))
                break
            except: 
                print(bcolors.FAIL + "INVALID INPUT!" + bcolors.ENDC)
        balance_in_checking -= payment
        sub3 = Calculator(j, payment)
        account_balance = sub3.subtract()
        print(bcolors.OKBLUE + f'Your new checking balance will be: {round(balance_in_checking,2)}\nYour balance on account {i} will be: {account_balance}' + bcolors.ENDC)
        print("And we Continue...")
        summary_string += f'{i},{payment},{account_balance}\n'
    summary_string += f'Checking, -, {balance_in_checking}'
    answr = input("Would you like to create a CSV file of account payments for your records? y/n: ")
    if answr == 'y' or answr == ' y':
        with open('payments.csv', 'w') as writer:
            writer.write(summary_string)
    if answr == 'n' or answr == ' n':
        pass