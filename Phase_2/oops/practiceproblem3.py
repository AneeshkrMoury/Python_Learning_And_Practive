# practice problem - 1

# B1. Write a Counter class with count = 0 , an increment() method, and a reset() method. The count is the state — it lives in the object.

class counter:
    
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0


ob1 = counter()
ob1.increment()
print(ob1.count)
ob2 = counter()
ob2.increment()
ob2.increment()
ob2.increment()
print(ob2.count)
ob2.reset()
print(ob2.count)

#practice problem 2
'''
. Add a balance check method to your BankAccount: show() that prints the current balance nicely. Create two accounts and prove they hold separate balances.
'''

class BankAccount:

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

    def balance_check(self):
        print(f"Account holder name -> {self.name} \nCurrent Balance -> {self.balance}")


aneesh = BankAccount(10000, "Aneesh")
urmila = BankAccount(5025, "Urmila")
aneesh.balance_check()
urmila.balance_check()


# Practice Problem -> 03

'''
Take any one-shot problem (e.g. "add two numbers") and argue in a comment why it does NOT need a class. Recognising when NOT to use OOP is a real skill.
'''

# add function 
def add(a, b ):
    return a + b  #--> in fucntion way its sort and easy to do 
print(98,86)

#CLASS WAY
class cal:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b  

ob1 = cal(54,56)
print(ob1.add)  # same problem increase the complexity 

# A class bundles related state and the operations that work on that state.

#practice problem - 4
'''
M1. Shopping Cart. First write it with functions ( add_item(cart, item) , total(cart) passing a list around). Then refactor into a Cart class holding its own items. Feel the difference.
'''
#using function
def add_item(cart,item):
    return cart.append(item)

def total(cart):
    return sum(cart)

cart = []
add_item(cart, 10)
add_item(cart, 12)
add_item(cart, 5)
add_item(cart, 24)

print(total(cart))


#using class
class Cart:
    def __init__(self):
        self.items_list = []

    def add_item(self, itme):
        self.items_list.append(itme)

    def total(self):
        return sum(self.items_list)

aneesh = Cart()
aneesh.add_item(250)
aneesh.add_item(15)
aneesh.add_item(254)
aneesh.add_item(68)

print(aneesh.total())

# class makes it super easy to handle states and calling same multiple block of code 


#practice problem -6
'''M3. Give BankAccount an owner name (set in __init__ ) and a transaction count that goes up on every deposit/ withdraw. Two new pieces of state, living in the object.'''

class BankAccount:

    def __init__(self, balance,owner_name):
        self.balance = balance 
        self.owner_name = owner_name
        print(f"{owner_name} account created with balance {self.balance}")

        self.transaction_cout = 0


    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transaction_cout +=1
        print(f"{amount} deposited \nnew balance {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds!")
        else:
            self.balance = self.balance - amount
            self.transaction_cout +=1
            print(f"{amount} withdraw \nRemaning balance is {self.balance}")

    def balance_check(self):
        print(f"Account holder name -> {self.owner_name} \nCurrent Balance -> {self.balance}")


aneesh = BankAccount(10000, "Aneesh")
aneesh.deposit(24)
aneesh.withdraw(653)
print(aneesh.transaction_cout)
aneesh.balance_check()


#practice problem - 7
'''
I1. What does "state" mean in programming, and why is it the main signal that a problem might suit a class rather than plain functions?

ANS -->> object that require monitorning when it changes consider we have a order object that changes every time when customer order something or when new cutome come and order also when customer add something it changes or it custome remove something it change as it the value is changing and require monitoring for handling customers here thus this object is  state 

State = information belonging to an object that can change over time.


its also confirm that the promple require a class as thing like we have to keep seprate every cart for each customer and also maintain security that no one else then the custome can access his cart and do action while its action is performing the object state also be maintained 

'''

# Practice Problem -8

"""
I2. In the functions version we passed balance into every call and caught the return. Explain exactly what problem the
class version removes, and how.

Ans --> in function we have to pass balance evry time while depositng or withdrowing also need to catch the balance each time 
and data can be modified ddireclty when we sue function 
create it complex to create multiple account

while on the other hand class solve all these problems provide security for data accessing , make it easy to create multiple obj , no need to catch balance value 

"""

# practice problem - 9
'''
I3. Give one example of a problem that should stay as functions (no class), and one that clearly calls for a class. What's the deciding factor?

Ans -> simple and mathmetical fucntion like add stay as function while a real like problem like handling a shoping cart stays in class 
'''

