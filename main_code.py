
from gather_data import v,j
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


def payments(checking,list1,list2):
    payments = []
    account_payment_balance = {}
    checking_balance = checking
    for i in range(len(list1)-1):
        print(f'For account:' + bcolors.BOLD + f'{list1[i+1]}\n' + bcolors.ENDC + 'You have a balance of: ' + bcolors.BOLD + f'{list2[0][i+1]}\n' + bcolors.ENDC + 'And a minimum payment of: ' + bcolors.FAIL + f'{list2[1][i+1]}.' + bcolors.ENDC)
        ticker = 0
        while True:
            try:
                payment = float(input('How much would you like to pay today? '))
                checking_balance = checking_balance - round(payment, 2)
                break
            except:
                print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
                ticker += 1
                if ticker > 3:
                    print(bcolors.FAIL + 'YOU MUST BE CONFUSED, PLEASE RUN THIS PROGRAM AGAIN!' + bcolors.ENDC)
                    exit()
        new_balance = list2[0][i+1] - payment
        checking_balance = round(checking_balance,2)
        print(bcolors.BOLD + f'\nYour checking balance is now: {checking_balance}\n' + bcolors.ENDC)
        payments.append(payment)
        account_payment_balance[list1[i+1]] = [payment, round(new_balance, 2)]
    
    u = round(sum(payments), 2)
    checking = round((checking - u),2)
    f = BalanceLife(account_payment_balance, checking)
    f.excel_is_for_nerds()

checking = j[0][0]
payments(checking,v,j)
