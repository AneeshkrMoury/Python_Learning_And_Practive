# Practive Problem -> 1
# Sum and Average Together
# write a function stats(nums) that returns BOTH the sum and the average as a tuple. Call it and unpack the result into two variables in one line, then print them

def stats(nums):
    return sum(nums), sum(nums) / len(nums)

sum_v, avg_v = stats([25,69,86,73,89])
print(f"sum of the list : {sum_v} \navg of the list : {avg_v}")


# Practive Problem -> 2
# Documented Area Function
# Write a function area(length, width)  that returns the area, with a docstring explaining what it does. Then print its docstring using area.__doc__ .

def area(length, width):
    ''' area function return the are of a rectangle'''
    return length * width

print(f" area : {area(15,30)}\n {area.__doc__}")


# Practive Problem -> 3
# Divide with Remainder
# Write a function divide(a, b) that returns BOTH the quotient and the remainder as a tuple. Unpack and print them for divide(17, 5) --> expected 3 and 2 

def divide(a, b):
    return a // b, a % b

quotient , remainder = divide(15, 2)
print (f"quotient : {quotient}\nremainder : {remainder}")


# Practive Problem -> 4
# Scope Detective
# Write code with a global x = global and a function that creates a local x = "local" and  and prints it. Outside the function, print x too In a comment, explain why the two prints differ.

x = "global"
def fun(x):
    x = "local" 
    print(x)

fun(x) # when we call our function fun it looks inside the function first there it got the x = local variable after that print fuction so it print local when we call fun function as based on LEGB rule function start from inside the function first 

print(x) # as x = "gloabal" and it can be used directly inside the print function and the function does not affect the vlaue outside of it unless it called and value changes inside it this here print will direclty return the global 



# Practive Problem -> 5
# Trace the LEGB Ladder
# Recreate the nested outer/inner example. Run it, then delete the local x , run again; then delete the enclosing x , run again. Note in comments which value prints each time and why.

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "loal"
        print(x)
    inner()

outer()
#python move to outer function now insdie outer find the innder call and inside inner call imediately find the x = local thus  print local its inner scope 

def outer():
    x = "enclosing"
    def inner():
        # x = "loal"
        print(x)
    inner()

outer()
# here local scope is empty thus it move to enclosing scope and find the value of x there then it prints that 

def outer():
    #x = "enclosing"
    def inner():
        # x = "loal"
        print(x)
    inner()

outer()
#as both local and enclosing scope are commneted out now the python will climb to the global scope and print x value as global 



# Practive Problem -> 6
# Min, Max and Average
# Write a function summary(nums) that returns the minimum, maximum, AND
# average — three values as a tuple. Add a docstring. Unpack all three and print them.

def summary(nums):
    """Return minimum, maximum and average."""
    return min(nums), max(nums), sum(nums) / len(nums)

min_v, max_v, avg_v = summary([65,98,75,15,23])
print(f"max element of lsit : {max_v} \nmin element of lsit : {min_v} \naverage value  of lsit : {avg_v}")



# Practive Problem -> 6 
# Your Own Math Module
# Create a file mymath.py with two functions: add(a, b) and is_prime(n) . In a second file main.py , import them and use both. (Prime logic is from #11.2.)

from mymath import add,is_prime
print(add(7,8))
print("given number is prime :",is_prime(476473))
