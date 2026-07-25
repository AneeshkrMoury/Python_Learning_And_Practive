#practice question 

# Student Profile CRUD
# Create a dict student with name and age . Then: add a course key, update the age, safely read a missing email key with .get() , and delete the course. print the dict after each step.



Student ={
    "Name":"Aneesh",
    "age":16,  
}

Student["course"] = "Python"
print(Student)

Student["age"] = 20
print(Student)

print(Student.get("email"))

# del Student["course"]  # or we can use pop to show what is deleted as well like below 
# print(f"Delted from student record -->>  {Student.pop("course")}")
# print(Student)

# Print a Price List
# Given prices = {"pen": 10, "book": 50, "bag": 200} , loop over it with .items() and print each line as "pen costs 10".

prices = {"pen": 10, "book": 50, "bag": 200}
for item,price in prices.items(): # .itmes covert the dic key and value into a tuple pair ex prices.items  --> [('pen',10), ('book', 50), ('bag', 200)]
    print(f"{item} costs {price} ")


# Phone Book
# Build a phone book dict with 3 name → number entries. Ask the user for a name and print the number using .get() so a missing name prints 
# "Not found" instead of crashing.

Phone_Book = {
    "Aneesh": 7394077767,
    "Rahul": 9876543210,
    "Neha": 9123456789,
}

Name = input("Enter person name to get number : ")
# Name = Name.title()
print(f"{Name} ->>> {Phone_Book.get(Name.title(),'Not found')}")

# Total & Highest
# Given marks = {"math": 90, "sci": 85, "eng": 78} , use looping to print the total marks and the subject with the highest marks.

marks = {"math": 90, "sci": 85, "eng": 78}
total_marks = 0 
Highest_mark = 0
Highest_mark_subject = ""

for subject,mark in marks.items():
    total_marks = total_marks + mark
    if Highest_mark < mark:
        Highest_mark = mark
        Highest_mark_subject = subject

print(f"total marks  -->> {total_marks} \nHighest marks subject -->>{Highest_mark_subject} \nHighest Mark -->> {Highest_mark}")

# Nested Student Records
# Create a nested dict of 3 students, each with 
# name and gpa . Loop over it and print each student's name and gpa. Then print the name of the student with the highest gpa


Student = {
    1: {"name": "Aneesh",
       "gpa" : 9.0
    },

    2: {"name" : "Rahul",
       "gpa" : 7.6
    },
    3: {"name": "Neha",
        "gpa" : 8.4
    }
}
highest_gpa_StudentName = ""
highest_gpa = 0
for ns,s in Student.items():
    # print(ns,"\n",s)
    s_details = s
    print("Name : ",s_details["name"], " and GPA : ", s_details["gpa"])
    
    if s_details["gpa"] > highest_gpa : 
        highest_gpa = s_details["gpa"]
        highest_gpa_StudentName = s_details["name"]

print(f"student named -> '{highest_gpa_StudentName}' got the highest GPA -> {highest_gpa} ")



# Count Letters with defaultdict
# Take a word from the user. Use defaultdict(int) to count how many times each letter appears, and print the result.

from collections import defaultdict

word = input("Enter a word : ")

count = defaultdict(int)
for ch in word:
    count[ch] = count[ch]+1

print(dict(count))

# Word Frequency with Counter
# Take a sentence from the user. Split it into words and use Counter to find the 3 most common words. Print them with their counts

from collections import Counter
#counter counts how many times a itmes appear in a lsit , tuple , or any other type of collection 
sentence = input("enter a sentence : ")
print(Counter(sentence.split()).most_common(3)) # .most_common(3) find the most comman number upto give numebr enter in it like 3 here 

     

