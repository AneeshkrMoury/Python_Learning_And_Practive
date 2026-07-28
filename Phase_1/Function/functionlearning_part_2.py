#function second part

#fuction are of 2 types 1-> user define defined by user , 2-> build in function predefiend we jsut call them 

def f1(name): # f1 is a user defined function 
    for e in name :
        print(e)

def min_max(num):
    #max and min here are built in function 
    max_v = max(num)
    min_v = min(num)
    return max_v,min_v

m1 , m2 = min_max([1,2,3,4,5])
print(f"max values of list :  {m1}\nmin value of list : {m2}")

#practice problem 
# define a method to return sum and avg of list 
def sum_avg(l):
    return sum(l), sum(l)/len(l)

sum_v , avg_v = sum_avg([1,2,3,4,5])
print(f"sum of list :  {sum_v}\navg value of list : {avg_v}")


#variables are of 2 types in function global and local 
# loacl_variable -->> if a variable is inside a function then it will be only used inside that function and no where else 
# global variable  -->> when a variable defined outside of any function then its known as global variable and it can be used anywhere in that program 

# scope  --> scops tells where a variable can be used inside in a program 

# Letter  |  Scope         |    Meaning
# L       |  Local         |    Inside the current function
# E       |  Enclosing     |    Inside an outer function (if nested)
# G       |  Global        |    Top level of the file
# B       |  Built-in      |    Python's own names ( prints. len ....)



#docstring --> A docstring is a string right under the def line that explains what the function does It's how professionals document code

def average(marks):
    """Return the average of a list of marks."""
    return sum(marks) / len(marks)
    # read it back anytime
print(average.__doc__)    # Return the average of a list of marks.
help(average)             # shows the docstring to   

# Good habit: One line saying what it does. For bigger functions, also mention the arguments and what it returns. Future-you will thank present-you.
print(max.__doc__)

# Using a Function from Another File 
# Once a function is reusable, you'll want it across files. Put functions in one file and import them into another.

# ---------- mymath.py ---------
def add(a, b):
  return a + b
def average(nums):
    return sum(nums) / len(nums)

# # ---------- main.py ---------
import mymath
print(mymath.add(3, 5))   # 8          
print(mymath.average([10, 20]))   # 15.0 

 # or import specific functions directly
from mymath import add
print(add(2, 2))  #4

# Key idea: Both files must be in the same folder. The file name (math.py) becomes the module name (mymath ) -- no .py when importing. This is exactly how big projects stay organized
