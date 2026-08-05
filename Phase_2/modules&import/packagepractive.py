#practice problem
'''
Your First Module
Create a module mymath.py with Add an add(a, b) and multiply(a, b) . In main.py ,  import and use both. Try both import mymath and import mymath and
'''

import mymath
print(mymath.add(45,56))
print(mymath.multiply(45,56))

from mymath import add,multiply
print(add(45,56))
print(multiply(45,56))

#practice problem 2
'''
The main Guard
add and if __name__ == "__main__" block to my math.py that tests your function confirm the test runs when you run mymath,py directly but not when you impot it into main.py
'''
def add(a,b):
    return a+b

def multiply(a, b):
    return a*b


if __name__ == "__main__":
    print("--- Testing function ---")
    print(add(85,96))
    print(multiply(85,96))  #when running directly mymath.py file testing run other wise not 

#practice question 3 
'''Random Dice
Use the random modules to  simulate rolling a dice 5 times and print each result'''

import random as rdm

for i in range(5):
    rooling_result = rdm.randint(1,6)
    print(f"rooling a dice got -> {rooling_result}")


# practice problem 4
'''Today's Date 
Use the datetime module to print today's date and the current year separately.'''

import datetime as dt
print(dt.date.today(), dt.date.today().year)
print(dt.datetime.now())

#practice problem 5
"""
Import with Alias 
Create a module  greetings.py with hello(name) function. Import it into a another file using an alias and call it
"""

'''
def add(a,b):
    return a+b
def multiply(a, b):
    return a*b
if __name__ == "__main__":
    print("--- Testing function ---")
    print(add(85,96))
    print(multiply(85,96))
def greeting(name):
    return(f"welcom {name}")
'''
# as i already have serval files i will use one of old one in this as welll 
from mymath import greeting 
print(greeting("Alice"))



#practice problem 6
'''Build a Package
Create a package folder utils/with an __init__.py , a strings.py module (witha shout(text) function ) that uppercase text and a number .py modules with an is_even(n) function , import and use both from a main.py outside the folder '''

'''
def shout(text):
    return(text.upper())

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
'''
from util.strings import shout, is_even

print(shout("my name is aneesh"))
print(is_even(5473187254))

#practice problem - 7
'''Save & Load JSON
Using the json module, save a dictionary of student data to a file, then load it back and print it. (Combines #14 dicts + #19 files + json.)'''

import json
student = {
    "Name" : "Aneesh",
    "age" : 18,
    "field" : "IT", 
}
with open("strings.json", "w") as f:
    json.dump(student, f)
with open("strings.json", "r") as f:
    data = json.load(f)
    print(data)

#practice problem -8
'''Password Generator
Use randome to generate a random 8-character password from letters and digits. Bonus: let the user choose the length'''
import random,string
passward = ""
passward_chr = string.ascii_letters + string.digits + string.punctuation
for i in range(10):
    passward = passward + random.choice(passward_chr)
print("passward : ",passward)
