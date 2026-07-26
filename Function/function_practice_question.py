# practice problem 01
# Greet with a Default Write a function greet(name, msg="welcome") that prints a greeting  Call it once with just a name, and once with both a name and a custom message

def greet (name, msg="welcome"):
    print("My name is ",name, msg)

# greet("Aneesh")


# ProbleNumber 02
# Rectangle Area
# Write a function area(length, width) that returns the area (not prints). Call it,store the result in a variable, and print it.


def area(length, width):
    rectangle_area = length*width
    return rectangle_area

# l = int(input("Enter length of rectange :"))
# w = int(input("Enter width of rectange :"))

# result = area(l,w)
# print(result)

#ProblemNumber -> 3
# Is Even?
# Write a function is_even(n) that returns True if n is even, else Easy False . Test it with a few numbers.

def is_even(n):
    if n%2 == 0 and n != 0:
        return True
    else:
        return False

# number_to_Check = int(input("Enter a Number to check even :"))
# print(is_even(number_to_Check))

#ProblemNumber -> 4
# Simple Interest
# Write a function interest(principal, rate, years) that returns the simple
# interest (P * R * T / 100). Give rate a default of 5 and call once using the default and once overriding it 
def simple_interest(principal,years, rate=5, ):
    interest = principal * rate  * years / 100
    return(interest)

# print(simple_interest(principal=100000,years=5))
# print(simple_interest(principal=100000,years=5, rate = 2.5))

#ProblemNumber -> 5
# Greatest of Three
# Write a function biggest(a, b, c) that returns the largest of three numbers —without using max().

def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# print(biggest(78,66,85))

#ProblemNumber -> 6
# Grade from Marks
# Write a function grade(marks) that returns "A", "B", "C", or "Fail" based on themarks (your own cutoffs). Test it with a few values.

def grade(marks):
    if marks > 80:
        return "A"
    else:
        if marks > 60 and marks <= 80:
            return "B"
        else :
            if marks > 30 and marks <= 60:
                return "C"
            else:
                return "Fail"

# print (grade(40))

#ProblemNumber -> 7
# Temperature Converter
# Write a function convert(temp, to="F") if to is "F" it returns
# Celsius→Fahrenheit; if "C" it returns Fahrenheit→Celsius. Use a default argument and return the result. Test both directions

def convert(temp, to="F"):
    if to == "F":
        temp_in_fahrenhei = temp * 9/5 + 32 
        reault = f"C → F{temp_in_fahrenhei}"
        return reault
    else:
        temp_in_Celsius = (temp - 32) * 5/9
        result =  f"F → C : {temp_in_Celsius}"
        return result

print(convert(256, "C"))
