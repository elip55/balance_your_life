
# color options
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

ticker = 0
counter = '1'
accounts_and_balances = {}

balance_in_checking = float(input("How much money do we have to work with? (Usually the money in your checking)\nAnswer in dollars and cents: "))
accounts_to_pay = int(input("How many accounts do you have to pay today? "))
num_of_accounts = accounts_to_pay*counter

for i in range(len(num_of_accounts)):
    ticker += 1
    names = str(input(f'Please name account {ticker} '))
    balances = float(input(f"Please enter the balance of {names}, in dollars and cents "))
    accounts_and_balances[names] = balances

for i,j in accounts_and_balances.items():
    payment = float(input(f"You owe {j} on account {i}. How much do you want to pay?\nEnter your answer in dollars and cents: "))
    balance_in_checking -= round(payment, 2)
    account_balance = round(j - payment,2)
    print(bcolors.OKBLUE + f'Your new checking balance is: {balance_in_checking}\nYour balance on account {i} is: {account_balance}' + bcolors.ENDC)
    print("And we Continue...")

print("Thank you for using Eli Pachecos " + bcolors.HEADER + "BALANCE YOUR LIFE" + bcolors.ENDC + " program\nPlease use again next month!")