#lambda function -> we use lambda keyword to create lambda fuction also known as anonymous function that you can define without a name, it can only contain one expresion 

sqr = lambda n:n*n
# print(sqr(3))

#when we have jsut a number lsit we can sort using builtin function sort 
# stud = [34,55,6,78,2]
# stud.sort()
# print(stud)
# stud.sort(reverse=True)
# print(stud)

student = [("a",85), ("n",92), ("r",78), ("l",25)]
student.sort(key=lambda s:s[1]) # sort will call the lambda 4 times and in each call s= ()first tuple inside of lsit and s[1] = will be the 1 st index value of tuple 
'''
("a",85), --> 85 
("n",92), --> 92
("r",78), --> 78
("l",25)  --> 25

now sort will sort using these value thus lsit will be sorted based on vlaue 
[("l",25), ("r",78) , ("n",92), ("a",85)] and this shows one of best use of lmbda function
'''
# print(student)


#highorder function : a function in which we can pass another function are said to be high order function 

def add(a,b):  # here this add is a normal function we will pass 2 normal value when we call it 
    return a+b

add(4,5)

nums = [3,4,3,5,3]

#map(function, collection ) -> map is a fucntion in which we can pass another function or collection as paramenter 
# map working --
# 1-> call function for each element of collection, and the return value of function will be sotred by map in an object know as map object 
#  

sqr = list(map(lambda n: n**2, nums))# [9,16,9,25,9]
# print(sqr)


#filter(function,collection ) - filter return boolean value true or false and filter call the collection the number of itmes times and store the true alue 

evens = list(filter(lambda x:x%2==0 , nums))
# print(evens)


from functools import reduce

#reduce(function , collection )
nus = [3,4,3,5,3]
prod = reduce(lambda a,b:a*b, nus) #  on first call will assign first 2 value of lsit a=2 and b = 4
# then store the value [6] now in next time when lambda will be call it will take a = stored value [6] and b = nus[2] 3 and store the result [18] similary will keep repeating untill all itmes are called 
# print(prod)


number = [-3,5,-1,8,-7,0,4,5]

p_number = list(filter(lambda n: n >= 0, number ))
print(p_number)
