

class BalanceException(Exception):
    def __init__(self,withdrawnamount, msg="Insufficient Balance"):
        self.msg = msg
        self.withdrawnamount = withdrawnamount
        super().__init__(self.msg)


def check_balance(amount):
    balance = 10000
    if amount > balance:
        raise BalanceException(amount)

try:
    check_balance(11000)
except BalanceException as be:
    print("exception raised")
    print(be)





