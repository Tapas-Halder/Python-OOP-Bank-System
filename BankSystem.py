"""
A simple command-line based Bank Management System built using Python and Object-Oriented Programming (OOP) concepts.
🔹 Features
Check account balance
Deposit money
Withdraw money
Multiple bank accounts using dictionary
Uses encapsulation (private balance)
"""

#class and methods of bank
class bank():  
    def __init__(self,__balance):
        self.__balance = __balance

    def balance(self):
        print("your balance : ",self.__balance)
    
    def deposit(self,deposit):
        self.deposit = deposit
        self.__balance += self.deposit
        print("deposit : ",self.deposit)

    def withdraw(self,withdraw):
        self.withdraw = withdraw
        self.__balance -= self.withdraw
        print("withdraw : ",self.withdraw)

#bank accounts ID 
account = {
    1:bank(5000),
    2:bank(7000),
    3:bank(12000),
}

#input bank account id
id = int(input("enter your bank account id : "))

#transfer data in my veriable
my = account[id]

#system loop run
while(1):
    print("1.balance " \
    "2.deposit " \
    "3.withdraw " \
    "4.exit ")

    n = int(input("enter 1 to 4 as your choise : "))

    if n == 1:
        my.balance()
    elif n == 2:
        a = int(input("enter amount : "))
        my.deposit(a)
    elif n == 3:
        a = int(input("enter amount : "))
        my.withdraw(a)
    else:
        break



