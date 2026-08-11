#state -> if a variable change with action and require maintance then it is called a state 

'''A Bank Account
Track a balance. Support deposit and withdraw. Don't allow withdrawing more than the balance.'''


def deposit(balance, amount):
    return balance + amount
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
        return balance # unchanged
    return balance - amount

the balance floats around loose in a variable

balance = 0

balance = deposit(balance, 1000) # must catch the return...
balance = withdraw(balance, 300) # ...every single time
print(balance) # 700

'''
⚠ WHAT'S UNCOMFORTABLE HERE
The data is separated from the actions. balance lives in one place; the functions that change it live somewhere else. They're only connected by you remembering to wire them.

You must catch the return every time. Forget one balance = ... and your balance silently goes stale. Nothing warns you. Nothing protects the data. Anyone can write balance = -5000 directly. The rules only live inside the functions, not around the data.

Two accounts = double the juggling. Now you need balance1 and balance2 as loose variables, and you must pass the right one to the right call. Ten accounts? Chaos
'''

class Account:
    def __init__(self, balance,name):
        self.balance = balance 
        self.name = name
        print(f"{name} account created with balance {balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} deposited \nnew balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds!")
        else:
            self.balance = self.balance - amount
            print(f"Remaning balance is {self.balance}")


obj = Account(10000, "aneesh")
obj.deposit(5000)
obj.deposit(3000)

# now here balance is state as based on this hold class is maintaned 


'''
What the class fixed — point by point
✔ EVERY PAIN POINT, SOLVED
Data + actions together. balance and the methods that change it
live in the same object. No drifting apart. No catching returns. acc.deposit(1000) updates the object's own balance directly. Nothing to remember.

The data is protected. The only way to change the balance is through deposit / withdraw — the rules travel with the data.

Many accounts, zero juggling. a = BankAccount() and b = BankAccount() — each keeps its own balance
automatically. Ten accounts is just ten objects.
