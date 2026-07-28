#Practice Problem -> 1
# Sum Any Numbers
# Write a function total(*args) that returns the sum of however many numbers are passed. Test it with 2 numbers, 5 numbers, and none.

def sums(*nums):
    return (sum(nums))

print(sums(4,5))
print(sums(2,3,4,5,6))
print(sums())


#Practice Problem -> 2
# Print a Profile
# Write a function profile(**kwargs) that prints every key-value pair passed to it as "key: value" . Call it with a few named arguments.

def profile(**kwargs):
    for item,value in kwargs.items():
        print(f"{item} : {value}")
profile(Name="Aneesh",Age = 25,prof= "student")



#Practice Problem -> 3
# Multiply Everything 
# Write a function multiply(*args) that returns the product of all numbers passed multiply(2, 3, 4)  → 24.

def prod(*nums):
    product = 1
    for n in nums:
        product = product * n 

    return(product)

print(prod(8,9,7,1,5,6,10,13))


#Practice Problem -> 4
# Count the Arguments Write a function how_many(*args) that returns how many arguments were passed.Test with different counts.

def how_many(*args):
    return len(args)

print(how_many(1,1,1,1,1,1,1,1,1))
print(how_many(1,1,1))
print(how_many())



#Practice Problem -> 5
# Greeting with kwargs
# Write a function describe(**kwargs)  that prints "name is Amit", "age is 21" etc., for whatever keyword arguments are passed

def describe(**kwargs):
    for key,value in kwargs.items():
        return(f"{key} is {value}")

print(describe(Name="Aneesh", age = 14 , prof = "student"))

#Practice Problem -> 6
# Max of Many
# Write a function biggest(*args) that returns the largest number passed without using max(). Handle the empty case by returning None

def biggest(*args):
    maxm = args[0]
    # for elm in range(len(args)):
    if len(args) == 0:
        return(None)
    else:   
        for elm in args:
            if maxm < elm:
                maxm = elm

    return(max)

print(biggest(85,96,35,75,64,28,58,68))


#Practice Problem -> 7
# Spread a List
# Write a function add3(a, b, c)  that returns the sum of three numbers. Then,given a list nums = [4, 5, 6]  call add3 by unpacking the list with *;

def add(a, b, c):
    return (a + b + c)

nums = [4, 5, 6]
print(add(*nums))


#Practice Problem -> 7
# Order Summary 
# Write a function order(customer, *items, **details)  Print the customer name,the list of items, and any extra details (like discount=10 )  Call it with a name, several items, and a couple of keyword details.

def order(customer, *items, **details):
    print(f"customer name : {customer}\nlist of itmes : {items}\nadditional details : {details}")

order(
    "Aneesh",
    "Biscut",
    "Namkeen",
    "Sugar",
    "Banana",
    Biscut="2% Discount",
    Banana="10% Discount over 24 piece purchase"
)
