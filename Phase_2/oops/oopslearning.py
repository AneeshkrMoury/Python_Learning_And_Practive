a = 10
b = 20
def add(a,b):
    return a+b
def prod(a, b):
    return a*b


#objected oriented programming
'''
2 concept of objected oriented programming 
class -> 
object ->
class is a blueprint or prototype that define cetain type of objects  
'''
class calculator:
    pass # tells interpretur that we are not doing anything right now 

x = calculator() #-> object of class 
y = calculator() # -> object of class we can create any numbers of class

# global varibale -> any thing in a class that is accessible by anyone in a class is a global variable 
# local variable  ->
# method          ->a function inside a class is a
# construtor      ->



class calculator:
    name = "Calculation"  # class varibale or atribute it will be same for very object and method 

    def __init__(self, x , y):  # constrator run as soon as object is created

        self.a = x # instance variable or atribute 
        self.b = y
        # print("object created")

    def add(self): # method  we need to call after creating object to un method 

        print(f"sum = {self.a + self.b}")

    def prod(self): # method 
        print(f"product = {self.a * self.b}")

    def area(self, r): # here r is local variable 
        pi = 3.1414    # pi is local variable can not used by other method 
        return pi * r * r


ob = calculator(10,20)
# ob.add()
# ob.prod()

ob1 = calculator(30,40)
ob1.add()
ob1.prod()

ob3 = calculator(5,3)
print(ob3.area(5.4))
print(ob1.name)
print(ob.a , ob.b)

print(ob1.a , ob.b)
ob.a = 15
print(ob.a)
print(ob1.a)
print(calculator.name)
calculator.name = "again calculation"
print(ob.name)
print(ob1.name)
