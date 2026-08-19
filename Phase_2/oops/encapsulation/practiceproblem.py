'''
Practice Problem 1 ->

M1. Give a Product class a private __price . The setter must reject prices below 0 and print a message; the getter returns the price formatted as $price .
'''

class Product:
    def __init__(self):
        self.__price = 0

    @property
    def price(self):
        return f"${self.__price}"
    
    @price.setter
    def price(self, rate):
        if rate >= 0:
            self.__price = rate 
        else: 
            print("price can not be less then 0")     

apple = Product()
apple.price = 90
print(apple.price)


'''
Practice Problem 2 ->
M2. Add a computed property full_name to a Person class that joins first and last — no setter, calculated
each time.
'''

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

obj = Person("Aneesh", "Mourya")
print(f"Full Name: {obj.fullName}")

'''
Practice Problem -3
M3. Build a BankAccount where __balance is private, balance is a read-only property, and money changes only through deposit() and withdraw() methods (withdraw blocks overdraw).
'''
class BankAccount:
    def __init__(self,name):
        print("==== 0 Balance Account Created ====")
        print()
        self.name = name
        self.__balance = 0

    @property
    def balance(self):
        return f"Current Balance: {self.__balance}"

    def deposit(self, ammount):
        if ammount > 0:
            self.__balance = self.__balance + ammount
            print(f"Deposit completed....")
        else:
            print("Amount entered should be grater then 0 for deposit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"withdrwal completed....")
        else:
            print(f"amount enterd for withdrow should be less the balance and greatehr then 0")

aneesh = BankAccount("Aneesh Kumar Mourya")
aneesh.deposit(10000)
aneesh.withdraw(8541)
print(aneesh.balance)

'''
Practice Problem -> 4
B1. Make a Student class with a private __marks . Add a @property getter, and a setter that only allows 0 - 100 (reject anything else).
'''
class Student:
    def __init__(self, sname):
        self.sname= sname
        self.__marks = 0

    @property
    def marks(self):
        return f"Marks: {self.__marks}"

    @marks.setter
    def marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print(f"Marks should be between 0-100")

anni = Student("Aneesh")
anni.marks = 545
anni.marks = 45
print(anni.marks)

'''
Practice Problem 5 ->
B2. Give a Person class a private __age with a getter and a setter that rejects negative ages.
'''
class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def age(self):
        return f"Age: {self.__age}"

    @age.setter
    def age(self , p_age):
        if p_age > 0:
            self.__age = p_age
        else:
            print("age can not be negative")

obj = Person("Anni")
obj.age = 45
print(obj.age)


'''
Practice Problem -> 6
B3. Make a Circle with a read-only radius property (getter, no setter). Confirm reading works and setting raises an
error.
'''
class Circle:
    def __init__(self):
        self.__radious = 8

    @property
    def radious(self):
        return f"Radious: {self.__radious}"

obc = Circle()
print(obc.radious) 
obc.radious = 45 # throw attribute error taht object has no setter 

'''
Practie Problem -> 7
I1. What is encapsulation, and what's the real difference between _protected and __private in Python?

Ans -> encapsulation is the process of binding code and data togeather as single unit 
encapsulation help in keeping object data safe inside it and contral how it should be accessed and edited It's also controlling how that internal state is accessed or modified.
'''

'''
Practive Problem -> 8
I2. Why use @property instead of a plain get_x() / set_x() method pair? What do you gain?

Ans -> @property is a decorator in python that help to create clean getter and setters and this lets a method act as a atribute 
'''

'''
Practice Problem -> 
I3. How do you make a property read-only, and when would a computed property be better than storing the value?

Ans -> when we create only property method of an object then its work as read only an 

when we need to drive something from pre stored objected and it can change if pre stored value changes then computed property is better then storing value 
'''
