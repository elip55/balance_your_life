
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
    
    def __init__(self, arr1, arr2, extra):
        self.l1 = arr1
        self.l2 = arr2
        self.ex = extra
        
    def making_dicts(self):
        new_dict = dict(zip(self.l1, self.l2))
        return new_dict

    def easy_street(self): # bad name, this just subracts lol
        return self.l1 - self.l2
            
    def excel_is_for_nerds(self): # where l1 is None, l2 is the csv_dict, and extra is checking
        csv_string = f'ACCOUNT,PAYMENT,BALANCE\n'
        for i,j in self.l2.items():
            csv_string += f'{i},{j[0]},{j[1]}\n'
        csv_string += f'CHECKING, N/A, {self.ex}'
        with open('payments.csv', 'w') as writer:
            writer.write(csv_string)


def gather_data(): # gather accounts, balances, and min payment due
    accounts = []
    balances = []
    min_payments_due = []

    ticker2 = 0
    while True:
        try:
            num_of_accounts = int(input("How many accounts do you have to pay today? "))
            break
        except:
            print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
            ticker2 += 1
            if ticker2 > 3:
                print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                exit()
    for i in range(num_of_accounts):
        names = input(f"Please input the name of account {i+1}: ")
        accounts.append(names)
    for i in accounts:
        balance = float(input('Please input the ' + bcolors.OKBLUE + 'TOTAL AMOUNT YOU OWE ' + bcolors.ENDC + f'on account: {i} '))
        min_payment = float(input('Please input the ' + bcolors.FAIL + 'MINIMUM PAYMENT DUE ' + bcolors.ENDC + f'on account: {i} '))
        balances.append(balance)
        min_payments_due.append(min_payment)
    arrays = BalanceLife(balances, min_payments_due, None)
    balances_min_dict = arrays.making_dicts()
    
    return accounts, balances_min_dict


def let_us_pay(checking, account_names, balance_min_dict): # bring names, balances_min_dict from previous function
    t1 = 0
    payment = []
    for i, j in balance_min_dict.items(): # get payment info
        print(f'For account ' + bcolors.BOLD + f'{account_names[t1]},' + bcolors.ENDC + 'you have a balance of ' + bcolors.OKBLUE + f'{i}, ' + bcolors.ENDC + 'and a minimum payment of ' + bcolors.FAIL + f'{j}.' + bcolors.ENDC)
        t1 += 1
        payments = float(input('How much would you like to pay today? '))
        checking -= payments
        payment.append(payments)
    ticker = 0
    subtracted_totals = []
    for i, j in balance_min_dict.items(): # now subtract the payment from account balance
        val1 = BalanceLife(i, payment[ticker], None)
        val2 = val1.easy_street()
        subtracted_totals.append(val2)
        ticker += 1
    csv_dict = {}
    ticker2 = 0
    for i in account_names: # make a csv dict to write the csv file easily
        csv_dict[i] = [payment[ticker2], subtracted_totals[ticker2]]
        ticker2 += 1
    f = BalanceLife(None, csv_dict, checking)
    f.excel_is_for_nerds()

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

names, balances = gather_data()
let_us_pay(checking, names, balances)
