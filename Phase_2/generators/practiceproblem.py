'''
Practice Problem -> 1
S1. Write a generator  count_up_to(limit) using yield the produces 1 upto limit loop over it and print each value 
'''

def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1


obj = count_up_to(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem -> 2
S2. Open a text file and print only the lines containing "ERROR", reading one line at a time (no readlines() ).
'''
def errorofile(filename):
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if "ERROR" in line:
                yield line

obj = errorofile("que.txt")
print(next(obj))
print(next(obj))

'''
Practice Problem -> 3
S1. Write a generator  count_up_to(limit) using yield the produces 1 upto limit loop over it and print each value 
'''

def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1


obj = count_up_to(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem -> 4
S2. Open a text file and print only the lines containing "ERROR", reading one line at a time (no readlines() ).
'''
def errorofile(filename):
    with open(filename, "r") as file:
        while True:
            if not line:
                break
                
            line = file.readline()
            if "ERROR" in line:
                yield line

obj = errorofile("que.txt")
print(next(obj))
print(next(obj))

'''
Practice Problem 3-> B1. Write a generator even_numbers(n) that yields the first 
n even numbers
'''
def even_num(n):
    en = 2
    for i in range(n):
        yield en
        en +=2

obj = even_num(3)
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem ->4
B2. Rewrite [x*x for x in range(10)] as a generator expression and pull the first three values with next()
'''
obj = (x*x for x in range(10))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem -5
B3. Write a generator countdown(n) that yields n down to 1, then the string "Done".
'''
def countdown(n):
    for i in range(n):
        yield n-i
        
    yield "Done"

obj = countdown(3)
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem -> 6
M1. Write a generator fibonacci(n) that yields the first n  Fibonacci numbers no list, yield each as you go.
'''
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b

obj = fibonacci(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

'''
Practice Problem 7-> 
M2. Write a generator that reads a large file and yields only lines longer than 80 characters. Explain in a comment why this saves memory

explanation -> it never load complete file in memory instead it load the one line at a time and only return it when needed due the memory usees are almost constant reagrdless of the file size 
'''
def readfile(filename):
    with open(filename, "r") as file:
        for line in file:
            if len(line.strip()) > 80:
                yield line

obj = readfile("que.txt")
print(next(obj))

'''
Practice Problem ->8
I1. What is the difference between return and yield ? What single thing makes a function a generator?

ANS->return kill the function  after returning imidiatly but yield pause the funciton  and keep it alive ;
when a function use yield instead of print or return then it become a generator 
'''

'''
Practice Problem -> 9
2. Why does a generator use less memory than a list for large data? Give a scenario where a list crashes but a generator doesn't.

ANS-> generator only load one data at a time to work with it and that make it moemory use almost constant and less but list impoert complete data at onnce thus it use more meory 

in the case of where we may try to storelarge data in list let consider storing 1b numbers in list will crash it as it will try to store them at once in memory 
while generator store one value at a time thus it does not crashes 
'''

'''
Practice Problem -> 10
I3. When would you choose a generator expression over a list comprehension — and when would a list actually be the better choice?

ANS-> i would prefer generator expression when i will be working with very large data set or unknow sequence like reading a huge file line by line as generator read one by one it will perfect to get first point where our condition meet to evaluate instead of getting all at once 

i will use list like where i need to know the length or need to get multiple result value at once and for indexing 
'''
