# Problem solving Practice 

# question 1 ->
# Print numbers from 1 to 50
# ->MUILTIPLES OF 3 -> print "Fizz"
# ->Multiples of 5 -> print "Buzz"
# -> Multiples of 5 and 3 print "FizzBuzz"
# -> other wise print number 

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

# #Question 2 ->
# Given marks -[85,90,72,60,95] find the total and the average of all marks using a loop (not sum() function)

marks = [85,90,72,60,95]
total = 0
for ele in marks :
    total = total + ele

print(f"Total marks -> {total} \nAverage marks -> {total / len(marks)}")


#Question no 3
#given nums = [23, 67, 12, 89, 45] find the biggest num without using max function 

nums = [23, 67, 12, 89, 45]
biggest_num = nums[0]
for ele in nums:
    if biggest_num < ele:
        biggest_num = ele

print (f"Biggest num -> {biggest_num}")



#Question no -> 4
# Take a number input and check if its a prime or not 
number = int(input("enter a number: "))


if number <= 1 :
    print(f"{number} is not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else: 
        print(f"{number} is prime")


is_prime = True
if number <= 1 :
    is_prime = False
i = 2
while i*i <= number:
    if number % i == 0:
        is_prime  = False
        break
    i += 1 
if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")



# question no 5
# give items = [1,2,2,3,4,4,4,5] find all numbers that apear more then once expected output [2,4]
#dirst method 
items = [1,2,2,3,4,4,4,5]
dublicate_items = []
for i in items:
    itme_count = 0
    for j in items:
        if i == j:
            itme_count += 1

    if itme_count > 1 and i not in dublicate_items:
        dublicate_items.append(i)

print(dublicate_items)

#second method  right now i am not able to perfectly define what difference but this one timecomplexity is lower then first one that much i undrestand 
for i in items:
    itme_count = 0
    for j in range(i + 1, len(items)):
        if i == j:
            itme_count += 1

    if itme_count > 0 and i not in dublicate_items:
        dublicate_items.append(i)

print(dublicate_items)
