items = [1, 2, 2, 3, 4, 4, 4, 5, 9, 9]
duplicate = []

for i in items:
    count = 0
    for j in items:
        if i == j:
            count = count+1   

    if count > 1 and i not in duplicate :
        duplicate.append(i)

print(duplicate)


# Find the Largest Number (without max())
# Given nums = [23, 67, 12, 89, 45] , find the biggest number without using
# max() .
# Uses: loop · if · comparison · "best so far" pattern

Given_nums = [23, 67, 12, 89, 45]
largest_num = Given_nums[0]
for ele in Given_nums:
    if ele > largest_num:
        largest_num = ele

# print(f"largest number from the given number list is : {largest_num}")

# Prime Number Check
# Take a number from the user. Print whether it is prime (divisible only by 1 and itself).
# Uses: input · loop · if · break · modulo

num = int(input("Enter A number to check prime number : "))

i = 1
count = 0
if num < 2:
    print(f"{num} is not a prime") 
else:
    while i <= num:
        if num % i == 0 :
            count = count+1

        i = i + 1

    if count > 2 :
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number (divisible only by 1 and itself)")


# Count Duplicates in a List
# Given items = [1, 2, 2, 3, 4, 4, 4, 5] , find all numbers that appear more
# than once. Expected output: [2, 4]
# Uses: nested loop · list · membership (in)

items = [1, 2, 2, 3, 4, 4, 4, 5, 5]
dup = []
for i in items:
    count = 0
    for j in items:
        if i == j :
            count = count + 1

    if count >= 2 and i not in dup:
        dup.append(i)

print(dup)

# Find the Smallest Number (without min())
# Given nums = [34, 12, 78, 5, 60] , find the smallest number without using
# min() .

nums = [34, 12, 78, 5, 60]
smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i

# print(f"smallest number from the nums list -> {nums} \n smallest == {smallest}")

# Count Primes in a Range
# Print all prime numbers between 1 and 50, and count how many there are.
# Hint: Reuse your prime-check logic inside another loop. Combine a loop, the break trick, and an
# accumulator.

starting_num = int(input("starting number : "))
ending_num = int(input("ending number : "))

if starting_num < 1 or ending_num < 1 : 
    print("range number should be greather then poistive ")
else:
    print(f"Prime numbers between {starting_num} and {ending_num} ==>>", end=" ")
    for i in range(starting_num,ending_num+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count = count + 1

        if count == 2 :
            print(i, end=",")       
            

    
# Remove Duplicates (keep unique only)
# Given items = [1, 2, 2, 3, 4, 4, 4, 5] , build a new list with each number
# appearing only once. Expected: [1, 2, 3, 4, 5]
# Hint: Loop the list, append to a new list only if it's not in it already.

items = [1, 2, 2, 3, 4, 4, 4, 5]
non_duplicate_items = []
for i in items:
    if i not in non_duplicate_items :
        non_duplicate_items.append(i)

print(non_duplicate_items)

# Second Largest Number
# Given nums = [23, 67, 12, 89, 45] , find the second largest number without
# sorting and without max() . Answer: 67.
# Hint: Track two variables — largest and second_largest — and update both as you loop.

Given_nums = [23, 67, 12, 89, 45]
largest = Given_nums[0]
second_largest = Given_nums[-1]

for ele in Given_nums:
    if ele > largest:
        largest = ele
for ele in Given_nums:
    if ele < largest and ele > second_largest:
        second_largest = ele

print("Second largest number in the list is : ", second_largest)


# Most Frequent Number
# Given items = [3, 1, 3, 2, 3, 1, 2, 3] , find the number that appears the most times. Answer: 3 (appears 4 times).
# Hint: Combine the duplicate-counting nested loop with the "best so far" pattern to track the highest count.

Given_items = [3, 1, 3, 2, 3, 1, 2, 3, 5]
item = []
appearance = []  

for i in Given_items:
    count = 0
    for j in Given_items:
        if i == j:
            count = count+1
    
    if i not in item:
        item.append(i)
        appearance.append(count) 

most_appear_item = 0
most_appear_count = 0
for i in range(len(appearance)):
    if appearance[i] > most_appear_count:
        most_appear_count = appearance[i]
        most_appear_item = item[i]

print(f"most appeard item is -> {most_appear_item}\nnumber of item appearance -> {most_appear_count}" )
print(item, appearance)
