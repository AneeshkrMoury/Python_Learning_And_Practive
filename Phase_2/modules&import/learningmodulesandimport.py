#package -> when a conatiner have multiple modules we call it a pacakge and to create a package we need to create "__init__.py" file inside the packege folder other wise it will be just a folder 


__name__ == __main__

# every module we create get a __name__ by default and it's value is __main__ ,"when we directly run this module file " if module runs indirectly then its __name__ will be the file name 
if __name__ == "__main__":
    print("direct excetution of learnmodule")
else:
    print("indirect excetution of learnmodule from different file")

# relatvie vs absulute import

import calculator   # -- does not work if pagakage and module are not in same location 

import my_app.calculator as calc  # this is absulute import where complete module with package 
print(calc.add(8,5))


from .calculator import add  #when we import using .modulename it is relative import , relative import used within same file of package  runs out side of package "python -m my_app.main"
print("sum = ", add(5,8))


#importing methond

x = int(input("enter the value of x : "))
y = int(input("enter the value of y : "))

# first method 
import calculator
print(f"Sum of {x} and {y} is {calculator.add(x,y)}")

# second method
import calculator as calc
print(f"Product of {x} and {y} is {calc.prod(x,y)}")

#3rd method
from calculator import add,prod
print(f"Sum of {x} and {y} is {add(x,y)}")
print(f"Product of {x} and {y} is {prod(x,y)}")


#predefined module 

import math

print(math.sqrt(9))
print(math.pi)

import learnmodule
print("hello")
