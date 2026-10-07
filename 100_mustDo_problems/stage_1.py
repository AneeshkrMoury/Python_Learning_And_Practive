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
