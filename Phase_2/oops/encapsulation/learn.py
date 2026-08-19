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
