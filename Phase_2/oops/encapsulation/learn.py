'''
encapsulation -> means keeping an object's data safe inside it, and controlling how the outside world touches it. Not every attribute should be freely editable — a bank balance shouldn't be set to -9999 by anyone

binding code and data in single unit 

'''
class Abc:
    def __init__(self, name):
        self.name = name
        self.__name1 = "Aneehs"

a = Abc("Anni")
print(a.name)
print(a.__name1__)  # should not work

#python do not provide strick implemention of encapsulation 
'''
self.name  -> public
self._name -> protected 
self.__name -> private
'''

#example
class Account1:
    def __init__(self):
        # instance variable 
        self.owner = "Aneesh"   # public
        self._bank = "UBOI"     # protected
        self.__balance = 1000   # private

obj = Account()
print(obj.owner)
print(obj._bank)
print(obj.__balance)


"""
@property — clean getters & setters
So how do you let people read a private value safely, and write it only with rules? The @property decorator lets a method act like an
attribute — clean syntax, full control.
"""

class Account:
    def __init__(self):
        # instance variable 
        self.owner = "Aneesh"   # public
        self._bank = "UBOI"     # protected
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("amount can not be negative")
        else:
            self.__balance = amount

    '''these 2 also work but not correct way to access private varibale and perform action to it '''
    def balance(self):
            return self.__balance
    
    def submit(self, amount):
        self.__balance = self.__balance + amount


a = Account()
a.__balance = 500  # incorrect will not work as classified as private variable

print(a.balance)
a.balance = 2000
print(a.balance)

'''
dunder methods : ->  Dunder ("double underscore")
methods — also called magic methods — let your objects work with Python's built-in features like printing, len() , == , and + . You've already used one: __init__

|----------------------------------------------------------------------------|
|Dunder      |   Runs when you...                                            |
|----------------------------------------------------------------------------|
|__init__    |   create the object (you know this one)                       |
|__str__     |   use print(obj) — a friendly, readable form                  |
|__repr__    |   inspect the object in the shell / debugger — a precise form |
|__len__     |   call len(obj)                                               | 
|__eq__      |   compare with ==                                             |
|__add__     |   use + between objects                                       |
| __mul__    |   *  multiply                                                 |
|__truediv__ |   / divide                                                    |
| __lt__     |   < less then                                                 |
| __gt__     |   > greater then                                              |
|----------------------------------------------------------------------------|


'''
class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"hellow my name is {self.name} and my age is {self.age}")
    def performance(self, marks):
        if marks>60:
            print(f"{self.name} is good in STUD")
        else:
            print(f"{self.name} is not good at study")

    def __str__(self): # __str__() this is a dender method for print
        return f"objected ceated with name {self.name}"

    def __repr__(self): # __str__() this is a dender method for print
        return f"{self.name} here , i am from REPR"
    def __len__(self):
        return len(self.name)

s1 = Student("Aneesh", 18)
print(len(s1))  #__len__()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other): # point1 == point2
        return self.x == other.x and self.y == other.y
    
print(Point(1, 2) == Point(1, 2)) # True — same values
print(Point(1, 2) == Point(9, 9)) # False



'''
__slots__ — a performance boost
By default every object stores its attributes in a hidden dictionary ( __dict__ ), which is flexible but uses memory. __slots__ tells
Python the exact attributes a class will have — saving memory and speeding up access when you create many objects.

'''

class Point:
    __slots__ = ["x", "y"] # only these two attributes allowed
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
p.x = 10 # fine
p.z = 5 # AttributeError — not in __slots__
