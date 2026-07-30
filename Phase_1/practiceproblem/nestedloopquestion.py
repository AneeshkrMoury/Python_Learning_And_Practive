#problem solving 

# wap for sqaure pattern 

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# wap for a increasing trangle 
for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()


# wap for a decreasing trangle 

for i in range(1,5):
    for j in range(5-i):
        print("*", end=" ")
    print()


# number trangle 
for i in range(1,5):
    for j in range(1,i+1):
        print(j , end=" ")
    print()

#break example 

lists = [5,6,7,5,8,4,2,5,5,44,99,87,74]

for ele in range (len(lists)):
    if lists[ele] == 99:
        print (99, "found at", ele )
        break

    
#contineue example 

for ele in range (len(lists)):
    if lists[ele] % 2 == 0:
        continue
    print (lists[ele] , end=" ")


# Basic
# B1. Print numbers 1–5 using nested loops.
for i in range(1,6):
    for j in range (1,2):
        print(i, end =" ")


# B2. Print a 4×6 rectangle of stars.
for i in range(4):
    for j in range(6):
        print("*", end = " ")
    print()


# B3. Print multiplication tables from 1–5.
for i in range(1,11):
    for j in range(1,6):
        print(f"{j} * {i} = {i*j}", end= "  | ")
    print()

# Moderate

# M1. Diamond-like half pattern.
for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")# in my original method i was not using the space after * due to that instead of dimond it was a right shifted trangle after trying multiple time i got to the point to print perfec half dimond i will need to use odd number of stars but i was not satisifed yet so i took help from google and found that if i use space after * it will look like adimond pattern 
    print()


for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")#odd places one 
    print()


# M2. Floyd's Triangle.
sums = 1
for i in range(4):
    sums = sums + i
    for j in range(i+1):
        print(sums+j, end=" ")
    print()


# M3. Print A, AB, ABC, ABCD, ABCDE.
import string as str


for i in range(1,6):
    for j in str.ascii_uppercase[:i]:
        print(j,end=" ")
    print()  # i am not sure if i have to print like exact given in question or in pattern like trangle so i am goona do both this one prints in trangle pattern 

for i in range(1,6):
    for j in str.ascii_uppercase[:i]:
        print(j,end="")
    print(end=",")# its print exactly like given in question 


# Break and continue. Print a 5×5 grid skipping the centre i am not sure if it saying to skip just the exat middle point in the 5x5 grid or middle point of each line of 5x5 grid

mid = 5 // 2 # mid of odd number
for i in range(5):
    for j in range(5):
        if i==mid and j==mid:
            print(" ", end="")    # this version prints a space at exact mid position of grid of 5*5 it can  work with any same type of add square grid
            continue
        print("*", end="")
    print()


mid = 5 // 2 # mid of odd number
for i in range(5):
    for j in range(5):
        if j==mid:
            print(" ", end="")    # this version print space  at mid position of each row 
            continue
        print("*", end="")
    print()


# Challenge
# C1. 1 / 22 / 333 / 4444 / 55555 i am considering that i have to print in pattern like trangle 
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

# C2. Right aligned star triangle.
for i in range(1,5):   
    for j in range(4-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

# C3. Multiplication tables 1–10.
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

    print()


# C4. Print all prime numbers from 1–100 using nested loops
for i in range(1,101):
    if i == 1 :
        continue

    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")
