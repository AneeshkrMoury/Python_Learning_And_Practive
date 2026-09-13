#Part 1
'''
S1. Write a closure multiplier(factor) that returns a function multiplying its input by factor . Build double and
triple from it.
'''
def multiplier(factor):
    def multiplying(n):#it sould take number be like take 2 if we want to double our number or 3 if need triple 
        return n*factor

    return multiplying

#lets try to call it 
onj = multiplier(5) # now here onj hold multiplying function so when we call it we need to pass a value 

print(onj(2)) #double 
print(onj(3)) # triple

'''
S2. Write a my_decorator that prints "Before" and "After" around any function, using *args, **kwargs , returning
the result, and with @functools.wraps . Test it on add(a, b) .
'''
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Before")
        res = f(*args, **kwargs)
        print("after")
        return res
    return wrapper

@my_decorator
def add(a,b):
    return a+b

print(add(7,2))
'''
B1. Store the built-in-style function greet in a variable f without calling it, then call it through f . Show the
difference between greet and greet() .
'''
def greet():
    return "hii"

f = greet # when function is passed it is like refernce of function it know where the function is and can point to it 
print(f) # thus printing it return address of greet 
obj =f() # now we pass f like a function it call the grret function and then greet peform its action and return is store in to f that is obj now 
print(obj) # so printing obj now returns hii 

'''
B2. Write an outer() that defines and returns an inner() . Call it and then call the returned function.
'''
def outer():
    print("its outer here")
    def inner():
        return "hii i am inner"
    return inner

obj = outer() #lets see what we get here obj = inner
print(obj()) # so now when we call obj its like calling inner() that return hii i am inner 

'''
B3. Write a decorator that prints "Start" before and "End" after a no-argument function.
'''
def my_decorator(f):
    @wraps(f)
    def wrapper():
        print("start")
        res = f()
        print("end")
        return res
    return wrapper
@my_decorator
def no_argument():
    return 'i am no argument function'

print(no_argument())

'''
M1. Write a logger decorator that prints the function's name and the arguments it was called with each time.
Hint: use func.__name__ and the *args / **kwargs values.
'''
def longer_decorator(func):
    @wraps(func)
    def wrapper(*arsg, **kwargs):
        print(f"function name: {func.__name__} ")
        print("args value :", *arsg)
        print("args value :", {**kwargs})
        res = func(*arsg, **kwargs)
        return res
    return wrapper

@longer_decorator
def randomfun(a,b):
    return f"{a} and {b} are friends "

print(randomfun("ankit", "ranjen"))

'''
M2. Show that @my_decorator is the same as f = my_decorator(f) by writing both forms and confirming identical
output.
'''
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return wrapper

@my_decorator  # we got 9 from this @
def add(a,b):
    return a+b

add= my_decorator(add) # 9 from this as well so both are same 
print(add(4,5))


'''
M3. Take a decorator without @functools.wraps , print the decorated function's __name__ , then add @wraps and
print it again. Explain the difference.
'''
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return wrapper

@my_decorator
def add(a,b):
    return a+b
# using used code becuse we just have to test name

print(add.__name__) # when we have @wraps -> output add ad the function name 
print(add.__name__) # without @wraps -> output is wrapper 
# this is due to decorator because we we decorate a function it lose its orignality but if we use @wraps then the orginality is function can remain original to return its name on checking name 

'''
I1. What does it mean that functions are "first-class objects" in Python? Give two things you can do with a function
because of it.

ANS -> first class object is like any other data type we can use the function as well like a data type we can pass it to a variable it can return a return it can be sordet as object in list , tuple dict etc , 
2 things that we do ->
we can pass to variable as other data type 
it can return a return
we can pass function to function as variable 
'''

'''
I2. What is a closure, and why does a decorator depend on one? What does the wrapper "remember"?
Ans -> not not 100% sure but i thing clousers are function inside function like nexted function and inner function can remeber the outer function varibale even after the outer function executed 

and decorator are basiclly in use becuase of closure as they cuse clouse propertly to pass a function as vatible into inner function that is warpper and it remeber it even after outer function executed
wrapper function remeber the varible of outer function / decorater
'''
'''
I3. What does the @ syntax actually do under the hood, and why do we use *args, **kwargs plus
@functools.wraps in the wrapper?

Ans -> i never really looked about @ but i thinks its use to override something like when we do @my_decoratoer it covert it into a decorator variable jsut  guessing , leave it , 
we use *args and **kwrags because as a decorater it jsut take a function as a varible but we nver know what will be varible of this funtons thus we use *args as it can store any number of single vale and **kwargs to store any number of pair value those are in form of key value pair 
'''

