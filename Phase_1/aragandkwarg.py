#args -> we use * to create args in front of any parameter 

def add(*args): # when we use * infront of parameter then we can provide any number of paraenter in the function and it stoe them in them form of tuple
# this is also called as args 
    return args,sum(args)
print(add(5,4,3))
print(add(5,4,3,8,9,10))



#kwargs

def intro(name,age,prof):
    print(f"my name is : {name}\nmy age is : {age}\nmy professon is : {prof}")

intro("aneesh",14, "software developer")
# in above method if we missplace the order then value wll be assigned to non related parameter to avoid this we can use keyname method assigh parameter with there key name 
intro(age = 14, name = "aneesh", prof = "software developer") 

intro(age = 14, name = "aneesh", prof = "software developer", place = "khaga")# sometimes we may need to enter a new parameter that is not present in original function to avoid this issue we can use kwargs 

def intro(**kwargs): #kwargs -> know as key word argument it sotres in the form of dictionaries 
    # we use double * to create kwargs 
    for value in kwargs.values():
        print(value)

intro(age = 14, name = "aneesh", prof = "software developer", place = "khaga")


def f(a,b):
    print(a+b)

f(32) #-> when we only pass one argument we get error say missing argument to avoid this we can use default argument 

def t(name,msg="welcome"): # we provide a default argument value to argument during creating it
    print(name)
    print(msg)

t("Aneesh")

def demo(a, b=10, *args, **kwargs):
    print(f"{a}\n{b}\n{args}\n{kwargs}")

demo(1,2,3,45,56, x=85, y=56)


#unpacking

def add(a,b,c):
    return a+b+c

nums = [11,12,13] # we need to pass the values of lsit in function 


print(add(nums[0],nums[1],nums[2])) #first method to do it but to make it more easy we use spread method *listname 
print(add(*nums)) #-> here *nums will spread the lsit * here is also know as spread opertaor not args if inside function as paramenter then work as args 

info = {'a':12,'b':20,'c':30}
print(add(**info))
# similary we use ** when we have to pass values from dictionaries to function 