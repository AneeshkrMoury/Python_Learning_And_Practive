# Create a Book Record
# Create a named tuple Book with fields title author , year . Make one book and print a sentence using field names, like "Wings of Fire by Kalam (1999)"

from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year"])
b1 = Book("Wings of Fire", "Kalam", "1999")
print(f"{b1.title} by {b1.author} ({b1.year})")

# Using the same Use Book tuple, you have a row 
# ["Ignited Minds", "Kalam", 2002] ._make() to turn it into a Book, then print the author.

row = ["Ignited Minds", "Kalam", 2002]
b2 = Book._make(row)
print(f"{b2.title} by {b2.author} ({b2.year})")

# Point in 2D Create a named tuple Point with fields x and y . Make a point (3, 7) and print its coordinates using field names. Hint: Point = namedtuple("Point", ["x", "y"])

Points = namedtuple("Points", ["x", "y"])
p1 = Points(3, 7)
print(f"Cordinates = {p1.x}, {p1.y}")

# Give a Raise with _replace()
# Using your employee tuple, create a new record where the salary is increased by 5000 using _replace() . Print both the original and the updated record to prove the original didn't change.

Employee = namedtuple("Employee", ['id', 'Name', 'salary'])
e1 = Employee(1,"Aneesh", 20200)
e2 = e1._replace(salary = e1.salary + 5000)

print(e1,'\n',e2)

# Print the Field Names 

print(Employee._fields)

# Rows to Records
# You have a list of rows: rows = [["Amit", 21, 8.5], ["Neha", 20, 9.1], ["Ravi", 22, 7.8]] Create a Student named tuple (name , age , Tricky , gpa ) Loop over the rows, use _make() to convert each into a Student, and print each student's name and gpa.

rows = [["Amit", 21, 8.5], ["Neha", 20, 9.1], ["Ravi", 22, 7.8]]
Student = namedtuple("Student", ["name", "age", "gpa"])
for i in range(len(rows)):
    s1 = Student._make(rows[i]) 
    print(f"Student named -> {s1.name} got {s1.gpa} gpa")
