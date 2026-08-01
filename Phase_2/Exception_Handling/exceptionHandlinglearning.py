# error types -> 1- synatx error -> program writing error 
#                2- runtime error -> program accuars during the execution of proghra, appearn when a program is running we also call exception to runtime error to handle these error we do exception handling 
#                3- logical error -> error due to logic such as we have to divide 2 number but inplace of program add this is logic error
'''
Excepection Handling -> when something goes wrong , python raise an exception and if we do not handle it - the whole program crashes 

age = int(input("Enter age: ")) # user types "abc"
print("Next year:", age + 1)
ValueError: invalid literal for int() with base 10: 'abc'
program crashes — nothing after this runs

The goal: catch the problem, show a friendly message, and keep the program running. That's the difference between a fragile script and reliable software.

'''
#method to handle expection

#try expect 
try:
    a = int(input("enter number "))
    b = int(input("enter number "))
    z = a / b
    print(z)
except ZeroDivisionError:
    print("you just entered O...error here")
except ValueError:
    print("please enter a valid number ... error generated")

print("hellow")
print("hellow again")

'''
2. Common Built-in Exceptions
----------------------------------------------------------------
Exception            ->  Happens when…
ValueError           ->  Right type, wrong value — int("abc")
TypeError            ->  Wrong type — "2" + 2
KeyError             ->  Missing dict key — d["nope"]
IndexError           ->  List index out of range — lst[99]
ZeroDivisionError    ->  Dividing by zero — 5 / 0
FileNotFoundError    ->  Opening a file that doesn't exist
-----------------------------------------------------------------
'''

l1 = [5,6,7,8,9]

try :
    print(l1[5])
except IndexError as e:
    print(e)



try:
    a = int(input("enter number "))
    b = int(input("enter number "))
    z = a / b
    print(z)
except (ZeroDivisionError, ValueError) as e:
    print(e)

print("hellow")
print("hellow again")



# 4. else and finally
# else runs only if NO exception happened. finally runs ALWAYS — error or not.
try:
    x = int(input("Number: "))
except ValueError:
    print("Not a number")
else:
    print("You entered", x) # only if try succeeded
finally:
    print("Done checking.") # always runs


'''
------------------------------------------------
Block          Runs when
try Always —   holds the risky code
except         Only if a matching error occurs
else           Only if NO error occurs
finally Always cleanup (close files, etc.)
------------------------------------------------
'''


# 5. raise — Triggering Your Own Errors
# Sometimes YOU want to signal a problem. raise throws an exception on purpose.
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    set_age(-5)
except ValueError as e:
    print(e) # Caught: Age cannot be negative


# Re-raising
# Catch an error, do something (like log it), then pass it up with a bare raise . refuse to handle error and complete program get crashed 
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    print(set_age(-5))
except ValueError as e:
    print(e) # Caught: Age cannot be negative
    raise

print("lolololo")
