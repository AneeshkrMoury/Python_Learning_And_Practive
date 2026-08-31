#generators -> generator is another form of iterator 
'''
l1 =[1,2,3,4]# iterable 
li = iter(l1) #iterator get power of next that rememebr the postion 
print(next(li))#generator is sorter way to create these iterator 
'''


#generators -> generator is another form of iterator 

# normally 
def nums():
    return 5 # stop after this 
    return 4
    return 3

a = nums()
print(a)

# as a generator 
def nums(): 
    yield 5 # now it is a generator when we use yield 
    yield 4
    yield 3  

a = nums()
print(a) # return reference as knows what to return but do not return value 
print(next(a)) # now with next return item
print(next(a))
print(next(a))

# a function when become generator now it know what to return but do not save them in memory and yield pouse the function and keep it alavie but return kill the fucntion 
