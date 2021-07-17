
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
    try:
        balance_in_checking = float(input("How much money do we have to work with? (Usually the money in your checking)\nAnswer in dollars and cents: "))
    except:
        print(bcolors.FAIL + 'ERROR. YOU MUST ENTER THE VALUE IN DOLLARS AND CENTS.' + bcolors.ENDC)
        print("Please run the program again.")
    try:
        accounts_to_pay = int(input("How many accounts do you have to pay today? "))
    except:
        print(bcolors.FAIL + 'ERROR. THIS VALUE MUST BE AN INTEGER' + bcolors.ENDC)
        print("Please run the program again.")

def dictionary_work():
    # calling the global variables
    global balance_in_checking
    global accounts_to_pay
    global length_counter
    global ticker
    # initiate the dictionary
    accounts_and_balances = {}
    # use length counter to create a length for the loop (1*n)
    num_of_accounts = accounts_to_pay*length_counter
    # start the summary string for csv file creation
    summary_string = "ACCOUNT, PAYMENT, FINAL BALANCE\n"

    for i in range(len(num_of_accounts)):
        ticker += 1
        names = str(input(f'Please name account {ticker} '))
        balances = float(input(f"Please enter the balance of {names}, in dollars and cents "))
        accounts_and_balances[names] = round(balances,2)

    sum_of_accounts = round(sum(accounts_and_balances.values()),2)
    print(bcolors.BOLD + "Okay, to recap, here's what your accounts look like:" + bcolors.ENDC)
    print(bcolors.BOLD + "-----------------------------------------------------" + bcolors.ENDC)
    for i,j in accounts_and_balances.items():
        print(bcolors.BOLD + f'{i}: {j}' + bcolors.ENDC)
    print(bcolors.BOLD + f'--------------------------\nTOTAL AMOUNT OWED: {sum_of_accounts}' + bcolors.ENDC)

    for i,j in accounts_and_balances.items():
        print('You owe: ' + bcolors.BOLD + f'${round(j,2)}' + bcolors.ENDC + ' on account: ' + bcolors.BOLD + f'{i}' + bcolors.ENDC)
        payment = float(input('How much would you like to pay? '))
        balance_in_checking -= payment
        minus = Calculator(j, payment)
        account_balance = minus.subtract()
        print(bcolors.OKBLUE + f'Your new checking balance will be: {round(balance_in_checking,2)}\nYour balance on account {i} will be: {account_balance}' + bcolors.ENDC)
        print("And we Continue...")
        summary_string += f'{i},{payment},{account_balance}\n'
    answr = input("Would you like to create a CSV file of account payments for your records? y/n: ")
    if answr == 'y' or answr == ' y':
        with open('payments.csv', 'w') as writer:
            writer.write(summary_string)
    if answr == 'n' or answr == ' n':
        pass