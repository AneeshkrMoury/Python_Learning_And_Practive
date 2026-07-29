#Practice Problem - 1
# Keep the Positives
# Given nums = [-3, 5, -1, 8, 0, -7, 2] , use filter() with a lambda to keep only the positive numbers.

number = [-3, 5, -1, 8, 0, -7, 2]

p_number = list(filter(lambda n: n > 0, number ))
print(p_number)


#Practice Problem - 2
# Double Every Number
# Given nums = [1, 2, 3, 4, 5] , use map() with a lambda to build a list where every number is doubled.


nums = [1, 2, 3, 4, 5]
print(list(map(lambda n:n*2, nums)))


#Practice Problem - 3
# Cube with Lambda
# Write a lambda cube that returns the cube of a number. Test it on 2, 3, and 5.

cube = lambda x : x**3
x = int(input("enter a numebr : "))
print(cube(x))


#Practice Problem - 4
# Uppercase All
# Given words = ["python", "lambda", "map"] , use map() to build a list of the words in UPPERCASE.

words = ["python", "lambda", "map"]

print(list(map(lambda x:x.upper(), words)))

#Practice Problem - 5
# Filter the Odds
# Given numbers 1 to 20, use filter() to keep only the odd numbers.

# print(list(filter(lambda n: n%2!=0, range(1,21))))

#Practice Problem - 6
# Sum with reduce
# Using reduce() , find the sum of all numbers in [5, 10, 15, 20]. Then modify it to find the maximum instead.

from functools import reduce

nums = [5, 10, 15, 20]
print(reduce(lambda a,b:a+b , nums))
print(reduce(lambda a,b: a if a > b else b , nums))



#Practice Problem - 7
# Sort by Last Letter
# Given names = ["Amit", "Neha", "Ravi", "Sara"] , sort them by their last letter using sorted() with a lambda key.

names = ["Amit", "Neha", "Ravi", "Sara"]
print(list(sorted(names, key=lambda n:n[-1])))


#Practice Problem - 8
# Clean the Prices
# Given raw = ["$100", "$250", "$99"] , use map() to strip the $ and convert each to an integer. Then use filter() to keep only prices above 100.

raw = ["$100", "$250", "$99"]
print(list(filter(lambda p: p > 100, map(lambda n: int(n.replace("$","")) , raw))))


#Practice Problem - 9
# map vs comprehension
# Write the same task — squaring only the even numbers from 1 to 10 — TWO
# ways: once using map + filter , and once using a list comprehension. In a comment, say which you find more readable and why.

sqrofeven = [i ** 2 for i in range(1,11) if i % 2 == 0 ]
print (sqrofeven)

print(list(map(lambda i: i**2, list(filter(lambda n: n%2==0, range(1,11) )))))

#Practice Problem - 10
# Longest Word with reduce
# Given a list of words, use reduce() to find the longest word — without max() . ["hi", "python", "lambda", "ok"] → "python" .

words = ["hi", "python", "lambda", "ok"]
print(reduce(lambda w1,w2: w1 if len(w1) >= len(w2) else w2 , words)) # but doing this there is problem when same size word appear it only return the last one if just use > if we use >= then first one


#Practice Problem - 11
# Predict the Output
# Without running it, predict what this prints, then verify:
nums = [1, 2, 3, 4, 5]
r = list(map(lambda x: x * 2, filter(lambda x: x > 2, nums)))
print(r)

#my answer ->  filter(lambda x: x > 2, nums)  this will return values greater then 2 so here it will be (3,4,)
# (map(lambda x: x * 2, filter(lambda x: x > 2, nums))) now repalcing the above value here but i am not sure if we can directly use without converting into lsit for now considering we can use so now what we got -->(map(lambda x: x * 2, [3,4,5]))  ---> it will do the square of all elements thus it will become 
# (9,16,25)  -->  we put these values in place of complete map function --> list(9,16,25) ---> [9,16,25]  this is our output 
