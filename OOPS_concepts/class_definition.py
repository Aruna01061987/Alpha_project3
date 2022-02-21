
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     def display(self):
#         return f"your name is {self.fname} {self.lname} and your pay is {self.pay}"
#
#
# emp1 = Employee("steve", "jobs", 1000)
#
# emp2 = Employee("steve", "henry", 9000)
#
# print(emp1.display())
# print(emp2.display())



"""creating bank account class"""


class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"************** Initial Amount Deposited: {balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount
        self.transactions.append(f"Amount withdrawn {amount}")
        return f"Please collect the cash {amount}"

    def transfer(self, to_account, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds")
        to_account.deposit(amount)
        self.balance -= amount
        self.transactions.append(f"Amount transferred {amount}")

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print("*" * 20)


c1 = BankAccount("Bhavana", 3000)

c2 = BankAccount("Hethvik", 3000)













































