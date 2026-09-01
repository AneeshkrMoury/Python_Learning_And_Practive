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



