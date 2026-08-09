# practice problem -1 
''' Give a Dog class a class attribute count that goes up by 1 with every new dog. Add a @classmethod how_many() that prints the total. Create 3 dogs and call it.'''

class Dog:
    count = 0
    def __init__(self):
        Dog.count = Dog.count + 1

    @classmethod
    def how_many(cls):
        print(f"Total Dog = {cls.count}")


ob1 = Dog()
ob2 = Dog()
ob3 = Dog()

Dog.how_many()

#practice question -02
"""
Add a @classmethod from_string() to a Person class so Person.from_string("Rajeev-30") returns a
Person with name "Rajeev" and age 30 (an alternate constructor)
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod 
    def from_string(cls, data):
        name , age = data.split("-")
        age = int(age)
        return cls(name, age)

ob = Person.from_string("Aneesh-21")
print(ob.name, ob.age)


#practice problem - 3
'''
Build a Temperature class with a @staticmethod c_to_f(c) and an instance method fahrenheit() that reuses it. Test both.
'''
class Temperature:
    def __init__(self , c):
        self.c = c

    @staticmethod 
    def c_to_f(c):
        return c * 1.8 + 32

    def fahrenheit(self):
        f = self.c_to_f(self.c)
        return f


ob = Temperature(45)
print(ob.fahrenheit())


#practice problem 4-
'''
B1. Create a Circle class with a @staticmethod area(r) that returns π·r². Call it without creating any object.
'''

class Circle:
    def __init__(self, r):
        self.r = r

    @staticmethod
    def area(r):
        return 3.14 * r * r

# print(Circle.area(5))

#practice problem - 5
'''B2. Add a class attribute college = "SHEAT" to a Student class and a @classmethod show_college() that prints it.
Call it on the class'''

class Student:
    collage = "SHEAT"
    def __init__(self):
        pass

    @classmethod 
    def show_college(cls):
        print(cls.collage)

Student.show_college()

#practice problem - 6
'''
 Write a MathUtils class with two static methods: add(a, b) and multiply(a, b). Use them without making an object.
'''
class MathUtils:
    def __init__(self,a ,b):
        self.a = a
        self.b = b

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def multiply(a,b):
        return a*b

print(MathUtils.multiply(8,9))
m = MathUtils.multiply(5,89)
print(m)

#practice problem 7 
'''M1. Give BankAccount a class attribute total_accounts that increments in __init__, and a @classmethod count()
to report it. Make 3 accounts and print the count.'''

class BankAccount:
    total_account = 0
    def __init__(self):
        BankAccount.total_account += 1

    @classmethod 
    def count(cls):
        return cls.total_account

ob = BankAccount()
ob1 = BankAccount()
ob2 = BankAccount()

print(BankAccount.count())

#practice problem 8
'''M2. Add a @classmethod from_csv_line() to a Product class that parses "Pen,10,50" (name, price, qty) into a
Product object'''

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    @classmethod 
    def from_csv_line(cls, data ):
        name,price,qty = data.split(",")
        price = int(price)
        qty = int(qty)

        return cls(name,price,qty)

ob = Product.from_csv_line("Pen,10,50")
print(ob.name, ob.price, ob.qty)


#practice problem -> 9 
'''
M3. Create a Validator class with a @staticmethod is_valid_email(email) that returns True if the string contains "@" and ".". Test it on 3 strings
'''
class Validator:

    @staticmethod 
    def is_valid_email(email):
        if "@" in email and "." in email:
            return True
        return False

ob = Validator.is_valid_email("aneeshk@gmail.com")
print(ob)
ob1 = Validator.is_valid_email("aneeshkgmail.com")
print(ob1)
ob2 = Validator.is_valid_email("aneesh")
print(ob2)


#practice problem - 11
'''Explain, with code, why an alternate constructor uses cls(...) instead of the hard-coded class name. Show what breaks if a subclass calls the hard-coded version.'''

class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    @classmethod 
    def from_csv_line(cls, data ):
        name,price,qty = data.split(",")
        price = int(price)
        qty = int(qty)

        return cls(name,price,qty)    #with this result is Pen 10 50 


    @classmethod 
    def from_csv_line(Product, data ):
        name,price,qty = data.split(",")
        price = int(price)
        qty = int(qty)

        return Product(name,price,qty)  #with this result is Pen 10 50 

ob = Product.from_csv_line("Pen,10,50")
print(ob.name, ob.price, ob.qty)

'''as the both give same code so right now i do not have much iedea about right now but i know that much that we cls to avoid some kind of conflit related to object'''


# practice problem - 11

'''I2. When would you choose a @staticmethod over a module-level plain function? Give one code example arguing each
side'''
# Ans -> i think ill use static function when i need to do some consistance work like converting from c to f or like doing independent task does does not require to intract much and also we use staticmethod when we do not want somehting that can intracte with object directly  it mostly time used where we have to do something fixed or a static operation it is based on my current understanding 

# also similarly we use classmethod where we need something for whole class like when we want to intract with class we use class method its result pass to class to like give instuction or change something or pass class values something like this 


#practice problem 12 ->
'''
I3. Build a Date class taking day, month, year. Add two alternate constructors: from_string("25-07-2026") and today() (use the datetime module). Both must return a Date object via cls
'''

import datetime as dt

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data):
        day, month, year = data.split("-")
        return cls(day, month, year)

    @classmethod
    def today(cls):
        t = dt.date.today()

        return cls(t.day, t.month, t.year)


ob = Date.from_string("5-08-26")
print(ob.day, ob.month, ob.year )
ob1 = Date.today()
print(ob1.day, ob1.month, ob1.year)
