
from src.colors import bcolors

class LetsMakeDictionaries:
    
    def __init__(self, arr1, arr2):
        self.l1 = arr1
        self.l2 = arr2
        
    def make_it_happen_boss(self):
        new_dict = dict(zip(self.l1, self.l2))
        return new_dict

    def easy_street(self):
        return self.l1 - self.l2
            
    def excel_is_for_nerds(self):
        start_it = f'ACCOUNT  |  BALANCE\n'
        start_it += '-----------------\n'
        start_it += f'CHECKING:  {self.l1}\n'
        for i, j in self.l2.items():
            start_it += f'{i}:  {j}\n'
        with open('Whatever dumb name.txt', 'w') as writer:
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
    v1 = LetsMakeDictionaries(names, balance)
    solution = v1.make_it_happen_boss()
    return solution

def accounts_and_min_payments(balance_dictionary):
    min_payment = []
    names = []
    for i in balance_dictionary:
        payment = float(input(f'What is the minimum payment for {i}: '))
        min_payment.append(payment)
        names.append(i)
    v1 = LetsMakeDictionaries(names, min_payment)
    solution = v1.make_it_happen_boss()
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
        print(f'For account {i}, you have a balance of {v1[i]}, and a minimum payment of {j}.')
        payments = float(input('How much would you like to pay today? '))
        checking -= payments
        payment.append(payments)
    ticker = 0
    final_list_of_destiny = []
    for i, j in v1.items():
        val1 = LetsMakeDictionaries(j, payment[ticker])
        val2 = val1.easy_street()
        final_list_of_destiny.append(val2)
        ticker += 1
    second_final_list_of_destiny = []
    for i in v1:
        second_final_list_of_destiny.append(i)
    val3 = LetsMakeDictionaries(second_final_list_of_destiny, final_list_of_destiny)
    dictionary_of_destiny = val3.make_it_happen_boss()
    ran_out_of_names = LetsMakeDictionaries(checking, dictionary_of_destiny)
    solution_of_destiny = ran_out_of_names.excel_is_for_nerds()