from datetime import datetime as dt


class BankAccount:
    def __init__(self, username, password, currentbalance):
        self.u = username
        self.p = password
        self.cb = currentbalance
        with open(f"{username}.txt", "w") as file:
            file.write("\n")

    def deposit(self, dep):
        flag = True
        a = 0
        while flag:
            a += 1
            b = self.authenticate()
            try:
                assert a < 3
            except:
                print("Too many wrong attempts!!")
                flag = False
                continue
            if b:
                flag = False
                self.cb += dep
                with open(f"{self.u}.txt", "a") as file:
                    file.write(
                        f"{dt.now()} The amount of Rupees {dep} has been added Current balance :  {self.cb} \n")

    def withdraw(self, wd):
        flag = True
        a = 0
        while flag:
            a += 1
            b = self.authenticate()
            try:
                assert a < 3
            except:
                print("Too many wrong attempts!!")
                flag = False
                continue
            if b:
                flag = False
                if wd <= self.cb:
                    self.cb -= wd
                    with open(f"{self.u}.txt", "a") as file:
                        file.write(
                            f"{dt.now()} The amount of Rupees {wd} has been debited Current balance : {self.cb} \n")
                else:
                    print("Low balance!! Cannot be debited at this time!")

    def authenticate(self):
        sp = input("Provide your secret password: ")
        if sp == self.p:
            return True
        else:
            return False

    def bankStatement(self):
        flag = True
        a = 0
        while flag:
            a += 1
            b = self.authenticate()
            try:
                assert a < 3
            except:
                print("Too many wrong attempts!!")
                flag = False
                continue
            if b:
                flag = False
                print(f"Hey {self.u}! Your Transaction History:")
                with open(f"{self.u}.txt") as file:
                    lines = file.readlines()
                    for line in lines:
                        print(line.strip())


print("Welcome to the Bank of IIIT-D")
username = input("Enter Name: ")
password = input("Enter Password: ")
currentbalance = float(input("Starting balance for your account: "))
wish = "Y"
obj = BankAccount(username, password, currentbalance)
while wish == "Y":
    print("Select Your Option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Bank Statement")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        dep = float(input("Provide the amount to be deposited: "))
        obj.deposit(dep)
        wish = input("Do you wish to continue? Y/N : ")
    if choice == 2:
        wd = float(input("Provide the amount to be withdrawn: "))
        obj.withdraw(wd)
        wish = input("Do you wish to continue? Y/N : ")
    if choice == 3:
        obj.bankStatement()
        wish = input("Do you wish to continue? Y/N : ")
