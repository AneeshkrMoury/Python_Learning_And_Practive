#  without function 

# name = "Aneesh"
# age = 16
# profession = "Student"

# print("Name is ",name)
# print("age is ",age)
# print("profession is ",profession)

# name = "Raja"
# age = 16
# profession = "Hacker"

# print("Name is ",name)
# print("age is ",age)
# print("profession is ",profession)


#with function
#function -  is named logic which we can reuse fuction works when we call it 

def intro(name,age,profession):
    print("Name is ",name)
    print("age is ",age)
    print("profession is ",profession)

intro("Aneesh",25,"student")
print("++++++++++++++++++++++++")
intro("Raju",15,"Hacker")

# function is a reusable , named logic , we write it once and give it a name and call whenever we need it 
#advantage is no repetition, fix bugs in one place , readable (a good name explains itself ) and testable

# how we create a function using def keyword then give it a name and paramenter in side the braacket 
def greet(n):
    print('hello how are you?', n)
# executing function by calling its name with parameter if required 
greet("aneesh")

def add(a,b): # we we careate fuction values are called as formal paramenter or orguments or paramenter
    print("sum is",a+b)

 # when we pass real values known as actual parameter or actual argument 
add(30,10)

def prod(a,b):
    z = a*b
    return z

print(prod(10,20))

#function type

#1 -> no return type and no parameter
def greet():
    print('hello how are you?')

greet() #calling

#2 -> with paramenter but no return 
def parameter(a,b):
    print(a+b)

parameter(10,96) #calling


#3 -> no parameter but return
def calc():
    a = 10
    b = 20
    return a/b

# print(calc()) #calling

# 4 -> with return and with parameter

def prod(a,b,c):
    z = a*b*c 
    return z

# print("prodcut is :", prod(2,3,9)) #calling

#keyword argument-give paramneter with parameter keyword 
def intro(name, age):
    print("My name is ", name)
    print("My age is ", age)

# intro(age=85, name= "ravi" )

#default argument -> when we forget to give a parameter it will use pre assigned value inplace of giving error 

def intro(name, age, msg="welcome"):
    print("My name is ", name)
    print("My age is ", age)
    print(msg)

intro("aneesh",15)
