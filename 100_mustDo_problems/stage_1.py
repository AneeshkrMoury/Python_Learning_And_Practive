'''
Stage 1: Logic & Basic Thinking 
'''

#1. Print numbers from 1 to N. 
n = int(input("Enter Stooping Number: "))
for i in range(1,n+1):
    print(i)

#2 Print all even numbers between 1 and N.
n = int(input("Enter Stooping Number: ")) 
for i in range(2, n+1, 2): # sortcut way by starting from 2 and then printing every second number 
    print(i)

for i in range(1,n+1):
    if i % 2 == 0:
        print(i)

i = 1
while i != n+1:
    if i % 2 == 0:
        print(i)

    i+= 1

#3. Find the sum of numbers from 1 to N. 
n = int(input("Enter Stooping Number: ")) 
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f"sum: {sum}")

#4. Find the sum of all even numbers from 1 to N. 
n = int(input("Enter Stooping Number: ")) 
sum = 0 

for i in range(2, n+1, 2):
    sum = sum + i

print(f"sum: {sum}")

for i in range(1,n+1):
    if i % 2 == 0:
        sum = sum + i

print(f"sum: {sum}")

# 5. Count how many digits are present in an integer.
digit = int(input("enter digit:"))
# built in way
s = str(digit) # we can cover the digit into string then use the len function to count the length of string 
print(len(s))

#cutome way 
count = 0
for d in str(digit):
    count = count + 1
print(count)

#6. Find the sum of the digits of an integer. 
digit = int(input("enter digit:"))
digit_sum = 0
for d in str(digit):
    digit_sum = digit_sum + int(d)

print(digit_sum)

# 7. Reverse an integer. 
digit = int(input("enter digit:"))

d = str(digit)
print(d[::-1]) # making the steps negative 1 print in reversre prder its built in method 
revers = ''


#custom method 
while digit>0:
    r = digit % 10
    # revers.append(r) # append do not work with int or str
    revers = revers + str(r)
    digit = digit // 10
    

print(revers)


'''
100 Must-Do Problem-Solving Questions 
Stage 1: Logic & Basic Thinking Part 2
'''

'''
Problem No - 8 - 15
'''

'''
8. Check whether an integer is a palindrome. 
Example: 
121 → Palindrome 
123 → Not Palindrome
'''
number = int(input("enter a number: "))

# using build in function
n = str(number)
res = n[::-1]
if n == res:
    print(True)
else:
    print(False)

#cutome function
def is_palindrome(num):
    n = str(num)
    revs = ""
    while num > 0:
        remainder = num % 10
        revs = revs + str(remainder)
        num = num // 10

    if n == revs:
        return f"{n} is a Palindrom"

    return f"{n} is not a Palindrom"

print(is_palindrome(4523254))


'''
9. Find the largest of three numbers without using max(). 
'''
def max_num(n1, n2, n3): # ignoring the case where all 3 are equals for this question 
    if n1>n2 and n1> n3:
        return f"max = {n1}"
    elif n2 > n1 and n2>n3:
        return f"max = {n2}"
    else:
        return f"max = {n3}"

print(max_num(45,36,-99))

''' 
10 Find the smallest of three numbers without using min(). 
'''
def min_num(n1, n2, n3): # ignoring the case where all 3 are equals for this question 
    if n1<n2 and n1< n3:
        return f"min = {n1}"
    elif n2 < n1 and n2 < n3:
        return f"min = {n2}"
    else:
        return f"min = {n3}"

print(min_num(45,36,-99))

'''
11  Check whether a number is positive, negative, or zero.
'''
def num_type(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(num_type(54))

'''
12  Check whether a number is divisible by both 3 and 5. 
'''
def check_division(num):
    if num%5 == 0 and num%3 == 0:
        return f"{num} is Divisble by both 5 and 3"

    return f"{num} is not Divisble by both 5 and 3"

print(check_division(8715))

'''
13  Calculate the power of a number using a loop, without using **. 
Example: 2^5 → 32 
'''
def power_calc(num , power):
    result = 1
    for i in range(1, power+1):
        result = result * num

    return f"{num}^{power} -> {result}"

print(power_calc(5, 2))

'''
14  Find the average of N numbers without using sum(). 
'''
def avg(n): # does not work for - negatvie input 
    sum = 0
    for i in range(1,n+1):
        sum = sum + i

    return f"Average of {n} numbers -> {sum / n}"

print(avg(-1000))

'''
15. Print the multiplication table of a given number. 
'''
def table(n):
    for i in range(1,10+1):
        print(f"{n}*{i} = {n*i}")

table(17)
