# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
    def __init__(self, balance, account_no, full_name, account_type):
        self.balance = balance
        self.account_no = account_no
        self.full_name = full_name
        self.account_type = account_type

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
        print("\n New Balance=", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
        print("\n New Balance=", self.balance)

    def display(self):
        print("\n Acoount Holder=", self.full_name)
        print("\n Acoount Number=", self.account_no)
        print("\n Net Available Balance=", self.balance)


s = Customer(5000, '01992309913', 'ABC XYZ', 'savings')

s.deposit()
s.withdraw()
s.display()
