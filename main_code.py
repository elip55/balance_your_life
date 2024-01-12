
# color and bold options
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'


class BalanceLife:
    
    def __init__(self, the_real_slim_shady, extra):
        self.l1 = the_real_slim_shady
        self.ex = extra
        
    def excel_is_for_nerds(self):
        csv_string = f'ACCOUNT,PAYMENT,BALANCE\n'
        for i,j in self.l1.items():
            csv_string += f'{i},{j[0]},{j[1]}\n'
        csv_string += f'CHECKING, N/A, {self.ex}'
        with open('payments.csv', 'w') as writer:
            writer.write(csv_string)

def checking_n_num_accounts():
    ticker = 0
    while True:
        try:
            checking = float(input('How much money do we have to work with? '))
            break
        except:
            print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
            ticker += 1
            if ticker > 3:
                print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                exit()
    ticker2 = 0
    while True:
        try:
            num_accounts = int(input('How many accounts do we have to pay today? '))
            break
        except:
            print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
            ticker2 += 1
            if ticker2 > 3:
                print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                exit()
    return checking, num_accounts


def gather_data(v): # gather account names, balances, and min payment due
    account_names = []
    accounts_balances_min = {}
    for i in range(v):
        ticker = 0
        while True:
            try:
                account_name = input(f'Please input the name of account {i+1}: ')
                break
            except:
                print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
                ticker += 1
                if ticker > 3:
                    print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                    exit()
        account_names.append(account_name)
    
    for i in account_names:
        ticker2 = 0
        while True:
            try:
                balance = float(input(f'Please input the balance of account: {i} '))
                break
            except:
                print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
                ticker2 += 1
                if ticker2 > 3:
                    print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                    exit()
        ticker3 = 0
        while True:
            try:
                minimum_payment = float(input(f'Please input the minimum amount owed of account: {i} '))
                break
            except:
                print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
                ticker3 += 1
                if ticker3 > 3:
                    print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                    exit()
        
        accounts_balances_min[i] = [balance, minimum_payment]

    return accounts_balances_min


def payments(checking, alldict):
    payments = []
    account_payment_balance = {}
    for i,j in alldict.items():
        print(f'For account:' + bcolors.BOLD + f'{i}\n' + bcolors.ENDC + 'You have a balance of: ' + bcolors.BOLD + f'{j[0]}\n' + bcolors.ENDC + 'And a minimum payment of: ' + bcolors.BOLD + f'{j[1]}.' + bcolors.ENDC)
        ticker = 0
        while True:
            try:
                payment = float(input('How much would you like to pay today? '))
                break
            except:
                print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
                ticker += 1
                if ticker > 3:
                    print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                    exit()
        new_balance = j[0] - payment

        payments.append(payment)
        account_payment_balance[i] = [payment, round(new_balance, 2)]
    
    u = round(sum(payments), 2)
    checking = checking - u

    f = BalanceLife(account_payment_balance, checking)
    f.excel_is_for_nerds()

l,v = checking_n_num_accounts() # l = checking, v = num of accounts
all_dict = gather_data(v) # returns dictionary
payments(l,all_dict)
