

from src.the_good_stuff import accounts_and_balances, accounts_and_min_payments, let_us_pay
from src.colors import bcolors

# calling functions from src
v1 = accounts_and_balances()
v2 = accounts_and_min_payments(v1)
v3 = let_us_pay(v1, v2)