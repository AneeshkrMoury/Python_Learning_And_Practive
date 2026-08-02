# PracticeQuestion -1
'''
Safe Number Input
Ask the user for a number and print its double. Wrap it in try/except so that entering text prints  "Please enter a valid number" instead of crashing.'''

try:
    number = int(input("enter a number : "))
    print(number * 2)
except ValueError:
    print("please entere a valid number")


#PracticeQuestion -2 
'''Safe Division
Ask for two numbers and print the result of dividing them. Handle both ValueError (bad input) and ZeroDivisionError (dividing by zero) with clear messages.
'''
try:
    a = int(input("enter a number : "))
    b = int(input("enter b number : "))
    z = a / b
    print(z)
except ValueError:
    print("please enter a numerical value ....")
except ZeroDivisionError:
    print(" dividing by zero or is not possible ...")


try:
    a = int(input("enter a number : "))
    b = int(input("enter b number : "))
    z = a / b
    print(z)
except (ValueError , ZeroDivisionError) as e:
    print(e)


#practice question -3 
'''Safe List Access
Given items = [10, 20, 30]  ask the user for an index and print that item Catch  IndexError and print no item there if the index is out of range'''

try:
    items = [10, 20, 30]
    index_no = int(input("ender index number : "))
    print(f"item at index no {index_no} is -->> {items[index_no]} ")
except IndexError:
    print(f"No item at there")


#practice question -4
'''Safe Dictionary Lookup
Given a phone book dict, ask for a name and print the number. Catch KeyError and print "name not found".(compare with using .get from #14)'''


try:
    phone_book = {
        "Aneesh" : "8564759871",
        "Racikha" : "9785697852","Udhyam" : "3256849512"
    }
    name = input("enter name to get contact : ")
    print(f"{name} --> {phone_book[name]}")
except KeyError:
    print("Name not found...")


phone_book = {
        "Aneesh" : "8564759871",
        "Racikha" : "9785697852",
        "Udhyam" : "3256849512"
    }
name = input("enter name to get contact : ")
number = phone_book.get(name)
if number == None:
    print("Name not found")
else:
    print(f"{name} -->> {number}")


#practice problem --5
'''Always Say Goodbye
Write a try/except that converts user input to always prints 
int . Add a finally block that "Thanks for using the app!" whether or not there was an error.'''

try:
    int_value = int(input("enter a number : "))
    print(int_value)
except ValueError:
    print("enter a numerical value ....")
finally:
    print("Thanks for using the app!")

#practice problem --6
'''Keep Asking Until Valid
Using a while  loop with try/except, keep asking the user for a number until they enter a valid one, then print it. Invalid input should re-prompt, not crash'''


input_number = None
while not isinstance(input_number, int): 
''' this version is my original method i was trying to do but there was one issue i was using (while input_number is not int ) this was not working as its not write to compare data type thus i take some help from google i found that ther is a builtin function isinstance that we can use to check if a number belong to a specific data type '''
    try:
        input_number = int(input("enter a number : "))
        print("number -> ", input_number)
        break
    except ValueError:
        print("enter a numberical number  ...")


while True: # this one was i found wile reading about isinstance 
    try:
        input_number = int(input("enter a number : "))
        print("number -> ",input_number)
        break
    except ValueError:
        print("enter a numberical number  ...")


#practice problem --> 7
'''
Validate with raise
Write a function set_age(age) that raises a ValueError if the age is negative or over 150, otherwise returns it. Call it inside a try/except and print the caught message.
'''

def set_age(age):
    if age < 0 or age > 150:
        raise ValueError("age is negative or over 150")
    return age

try:
    age_v = int(input("enter age :"))
    print("ager -> ", set_age(age_v))
except ValueError as e:
    print("caight :" , e)



#practice problem --> 8
'''
Batch Divider with else
Loop over pairs [(10, 2), (5, 0), (9, 3)] For each, try to divide and print the result in an else block , catch ZeroDivisionError in except , and print"---" in finally after each pair 
'''

pairs  = [(10, 2), (5, 0), (9, 3)]
for p in pairs:
    try:
         divide_result = p[0] / p[1]
    except ZeroDivisionError as e:
         print(e)
    else:
        print(divide_result)
    finally:
         print("----")


#practice problem - 9
# Predict the Output
# Without running it, predict what prints, then verify:
        
def f():
    try:
        return "try" # second print
    finally:
        print("finally runs")  # first print

print(f())   

'''print call the fucntion "f()" --> now pointer move inside the function --> find try and try return ("Try") --> return value get passed to fucntion --> then pointer move finally as finally alway exceute after try it will print "finally runs" then- --> pointer get out of exception block ---> and print the return value passed to it from return "try" '''

#practice problem 10
'''
Custom Exception Bank
Create a custom exception InsufficientBalance  Write a withdraw(balance, amount) function that raises it when the amount exceeds the balance. Test both a successful and a failing withdrawal with try/except
'''
class InsufficientBalance(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalance("Not enough money!")
    return balance - amount

try:
    withdraw(100,500)
except InsufficientBalance as e:
    print(e)


try:
    print(withdraw(500,100))
except InsufficientBalance as e:
    print(e)


#practice problem --> 11
'''Log and Re-raise
Write a function that does a risky int() conversion. Catch the ValueError , print "Logging: bad input" , then re-raise it. In the calling code, catch the re-raised error and print "Handled at top level" .'''

def covert_int():
    try :
        n = int(input("enter a number : " ))
    except ValueError:
        print("Logging: bad input")
        raise 

try: 
    covert_int()
except :
    print("handled at top level")