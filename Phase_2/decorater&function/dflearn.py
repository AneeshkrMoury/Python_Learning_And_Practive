def greet(name):
    """This function greets people"""
    return f"hey {name}"

print(greet.__name__)
print(greet.__doc__)


# calling it 
print(greet("aneesh"))

# we can store function in object as well 
f=greet
print(f("anni"))
# using this we can pass a function as parameter 
def intro(func,n):
    print(func(n))

# intro(greet,"aneesh")


# a function can return return
def calc():
    def sqr(x):
        return x * x
    return sqr

sq = calc()
print(sq(5))


print(input.__doc__)

print(greet.__doc__)

'''a function is first class object '''

#Closures -> a function that remembers varibales from the function that created it even after that outer function has finished "this memeory make decorators pwerful"

# inner function remember outer function variable 
def multi(f):
    def multiply(number):
        return number * f
    return multiply

double = multi(2)
print(double(5))
