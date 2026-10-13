'''
100 Must-Do Problem-Solving Questions 
Stage 2: Logic & Basic Thinking Part 2  question no 21 - 25
'''
'''
21 -> Print all Armstrong numbers within a given range. 
153 → 1³ + 5³ + 3³ = 153 
count digit - 3 then power of digit 
'''

def ArmstrongNumberChecker(start, end):
    arms_num = []
    for i in range(start, end+1):
        number = str(i) # coverting number into string for checking len and then extracting each digit 
        number_len = len(number)
        digit_power = []
        for d in number:
            d_power = int(d) ** number_len # d is a string converting back to int
            digit_power.append(d_power)

        if int(number) == sum(digit_power):
            arms_num.append(number)

    return arms_num
print(ArmstrongNumberChecker(1, 500))

'''
22 Generate the first N Fibonacci numbers

IS IT LIKE 5! = 5 * 4 * 3 * 2 * 1 sorry its factorial 

febo is like 0 ,1 , then 3rd is the sum of last 2 number = 1 , 2, 3, 5, 8,13
'''

def Fibonacci_numbers(n):
    i = 0
    j = 1
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        series = []
        k = 0
        while k != n: # i am using idexing 1 starting at 1 for first febo. number
            series.append(i)
            i , j = j , i+j # shifting i to j and j to next position i + j 
            k = k+1

    return series

print(Fibonacci_numbers(2))

'''
23 Find the GCD of two numbers without using math.gcd()
 gcd is like gratest common divior 
'''
# its kinda like largest number that can divide both and its also the factor of both im goona try some logic into it lets see if it goona work 

def gcd(n ,m):
    limit = 0 
    if n>m:
        limit = abs(m) # using smallest number as stoping point 
    else:
        limit = abs(n)

    if n==0 and m == 0:
        return 0
    elif n == 0:
        return m
    elif m == 0:
        return m
    else:    
        res_gcd = [] # getting those number can divide both
        for i in range (1,limit+1):
            if n%i == 0 and m%i == 0:
                res_gcd.append(i)
        return max(res_gcd)
    
print(gcd(0,0))
print(gcd(0,27))
print(gcd(-12, 18))
print(gcd(25, 25))
print(gcd(17, 19))

'''
24- Find the Nth Fibonacci number using iteration.
'''
def Fibonacci_numbers(n):
    i = 0
    j = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        series = []
        k = 0
        while k != n: # i am using idexing 1 starting at 1 for first febo. number
            series.append(i)
            i , j = j , i+j # shifting i to j and j to next position i + j 
            k = k+1

    return series[-1]

print(Fibonacci_numbers(10))  # for this we have to find a specific point feb number so i using old finding thill nth position and the returning last indes feb 

'''
25 - Find the LCM of two numbers using your own logic.
'''
from math import prod
def lcm(n, m):
    stopping_point = 0
    if n > m :
        stopping_point = n
    else:
        stopping_point = m
    if n == 0 or m == 0:
        return 0
    else:
        common_factor = []
        for i in range(2, stopping_point+1):
            while True:
                if n%i == 0 and m%i == 0:
                    common_factor.append(i)
                    n = n/i
                    m = m/i
                elif n%i == 0:
                    common_factor.append(i)
                    n = n/i
                elif m%i == 0:
                    common_factor.append(i)
                    m = m/i
                else:
                    break
        return prod(common_factor)
print(lcm(1,6))
