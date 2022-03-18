from datetime import datetime


class BankAccount:
    interest_rate = 0.04

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = float(amount)
        self.transactions = []
        self.transactions.append(f"{datetime.now()}*****  Initial deposit   *** {self.balance}")

    def deposit(self, amount):
        self.balance += float(amount)
        self.transactions.append(f"{datetime.now()} Deposited Amount: {amount}")

    def roi(self):
        self.balance += self.balance * BankAccount.interest_rate

    def withdraw(self, amount):
        if amount <= self.balance:
            return amount
        else:
            return f"cannot withdraw {amount} from {self.balance}"

    def statement(self):
        for line in self.transactions:
            print(line)
        print(f"Total Account Balance: {self.balance}")


p1 = BankAccount("Srini", "vasulu", 3000)









