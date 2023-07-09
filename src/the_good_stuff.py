
from src.colors import bcolors

class LetsWork:
    
    def __init__(self, arr1, arr2, extra):
        self.l1 = arr1
        self.l2 = arr2
        self.ex = extra
        
    def making_dicts(self):
        new_dict = dict(zip(self.l1, self.l2))
        return new_dict

    def easy_street(self):
        return self.l1 - self.l2
            
    def excel_is_for_nerds(self):
        start_it = f'ACCOUNT,PAYMENT,BALANCE\n'
        start_it += '-----------------\n'
        start_it += f'CHECKING, N/A, {self.l1}\n'
        ticker = 0
        for i, j in self.l2.items():
            start_it += f'{i}, {self.ex[ticker]},{j}\n'
            ticker += 1
        with open('payments.csv', 'w') as writer:
            writer.write(start_it)
        
    
def accounts_and_balances():
    while True:
        try:
            num_of_accounts = int(input('How many accounts do you have to pay? '))
            break
        except:
            print('INVALID INPUT!!!')
     
    names = []
    balance = []
    for i in range(num_of_accounts):
        n = input(f'Please input the name of account {i + 1}: ')
        names.append(n)
    for i in names:
        balances = float(input(f'What is the balance of {i}? '))
        balance.append(balances)
    v1 = LetsWork(names, balance, None)
    solution = v1.making_dicts()
    return solution

def accounts_and_min_payments(balance_dictionary):
    min_payment = []
    names = []
    for i in balance_dictionary:
        payment = float(input(f'What is the minimum payment for {i}: '))
        min_payment.append(payment)
        names.append(i)
    v1 = LetsWork(names, min_payment, None)
    solution = v1.making_dicts()
    return solution

def let_us_pay(v1, v2):
    while True:
        try:
            checking = float(input('How much money do we have to work with? '))
            break
        except:
            print(bcolors.FAIL + 'YOU HAVE FAILED A SIMPLE TASK, PAY ATTENTION AND INPUT DOLLARS AND CENTS!!' + bcolors.ENDC)
    
    payment = []
    for i, j in v2.items():
        print(f'For account ' + bcolors.BOLD + f'{i},' + bcolors.ENDC + 'you have a balance of ' + bcolors.BOLD + f'{v1[i]}, ' + bcolors.ENDC + 'and a minimum payment of ' + bcolors.BOLD + f'{j}.' + bcolors.ENDC)
        payments = float(input('How much would you like to pay today? '))
        checking -= payments
        payment.append(payments)
    ticker = 0
    final_list_of_destiny = []
    for i, j in v1.items():
        val1 = LetsWork(j, payment[ticker], None)
        val2 = val1.easy_street()
        final_list_of_destiny.append(val2)
        ticker += 1
    second_final_list_of_destiny = []
    for i in v1:
        second_final_list_of_destiny.append(i)
    val3 = LetsWork(second_final_list_of_destiny, final_list_of_destiny, None)
    dictionary_of_destiny = val3.making_dicts()
    solution_of_destiny = LetsWork(checking, dictionary_of_destiny, payment)
    solution_of_destiny.excel_is_for_nerds()