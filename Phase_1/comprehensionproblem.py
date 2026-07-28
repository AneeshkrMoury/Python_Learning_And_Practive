# Word Length Lookup
# Given words = ["python", "set", "tuple", "list"] , use a dictionary comprehension to build {word: length} and print it

words = ["python", "set", "tuple", "list"]

wordsLenDict = {w:len(w) for w in words}
print(wordsLenDict)

# Unique Lengths
# Given 
# names = ["Ravi", "Amit", "Sara", "Neha", "Ram"] , use a set comprehension to build the set of all distinct name lengths.
names = ["Ravi", "Amit", "Sara", "Neha", "Ram"]
unique_length = {len(name) for name in names}
print(unique_length)

# Squares List
# Use a list comprehension to build the squares of numbers 1 to 10. Then make a
# second version that keeps only the even squares.

print(f"Square of Numbers between 1 - 10 :\n{[i*i for i in range(1,11)]}")
print(f"Square of Even Numbers between 1 - 10 :\n{[i*i for i in range(1,11) if i%2 == 0]}")

# Cube Lookup Table
# Use a dictionary comprehension to build {n: n*n*n} (cubes) for numbers 1 to 6 Then look up and print the cube of 4

cube_dict = {i : i*i*i for i in range(7)}
print(f"Cube of numbres between 1 to 6 : {cube_dict}")
print(f"Checking the cube of 4 : {cube_dict[4]}")

# Take a word from the user. Use a set comprehension to collect all the unique vowels that appear in it. Example: "varanasi" -> {'a', 'i'} 

word = input("Enter a word : ")
unique_vowel = {ch for ch in word if ch in "aeiou"}
print(unique_vowel)

# Price with Tax
# Given prices = {"pen": 10, "book": 50, "bag": 200} , use a dictionary
# comprehension to build a new dict where every price is increased by 18% tax
prices = {"pen": 10, "book": 50, "bag": 200}
PricewithTax = {item: price * 1.18 for item, price in prices.items()}
print(f"New prices with 18% tax {PricewithTax}")

# Word Frequency
# Take a sentence from the user. Using a dictionary comprehension over the unique words, build {word: count} showing how many times each word appears.
# Example: "a b a c b a" → {'a': 3, 'b': 2, 'c': 1} 

sentence  = input("Enter a sentence : ")
word = sentence.split(" ")
# print(word)
word_frequency = {w: word.count(w) for w in set(word)}
print(word_frequency)
