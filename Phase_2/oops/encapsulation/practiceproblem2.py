'''
Practice Problem -1
S1. Give a Book class __str__ (friendly) and __repr__ (precise). Print a book, and show what __repr__ returns.
'''
class book:
    def __init__(self, book_name):
        self.book_name = book_name

    def __str__(self):
        return f"class Book created with book called : {self.book_name}"

    def __repr__(self):
        return f"reparing .....{self.book_name} "

b1 = book("Aladeen")
print(b1)

# when we use both str and repr dunder method in a class then both a valid for the print and if both are preset then str will always get executed but if some how str get curropted or failed to work then repr metod work as a recovery option for str 

'''
Practice Problem -> 2
S2. Build a Money class with __add__ and __str__ so Money(100) + Money(50) prints $150
'''
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount}"

print(Money(100) + Money(50))


'''
Practice Problem -> 3
B1. Add __str__ to a Person class so print(person) shows "Name: X, Age: Y".
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

obj = Person("Aneesh", "21")
print(obj)

'''
prctice problem 4 ->
B2. Write a Playlist class with a list of songs and a __len__ returning the number of songs.
'''
class Playlist:
    def __init__(self):
        self.songs = ["chal chiyan chal chiyan chiyan", "rang de basanti"]

    def __len__(self):
        return len(self.songs)

obj = Playlist()
print(len(obj))

'''
Practice Problem -> 5
B3. Give a Point class __eq__ so two points with the same x and y are equal. Prove it prints True.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

print(Point(5,8) == Point(5,8))

'''
practice problem -6
M1. Build a Vector class with __add__ so Vector(1,2) + Vector(3,4) returns Vector(4,6) . Add __str__ to
print it nicely.
'''
class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector((self.x + other.x),(self.y + other.y))

    def __str__(self):
        return f"{self.x},{self.y}"

print(Vector(1,2) + Vector(3,4))

'''
Practice Problem -> 7
M2. Give a Temperature class __eq__ (compare by value) and __lt__ so you can use < to sort a list of temperatures.
Hint: __lt__ lets sorted() work on your objects
'''
class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def __eq__(self, other):
        return self.temp == other.temp

    def __lt__(self, other):
        return self.temp < other.temp

    def __str__(self):
        return f"{self.temp}"

    def __repr__(self):
        return f"{self.temp}"

Temperature_list = [Temperature(45), Temperature(23), Temperature(25), Temperature(46)]

for i in range(len(Temperature_list)):
    for j in range(len(Temperature_list)):
        if Temperature_list[i] < Temperature_list[j] :
            Temperature_list[i] , Temperature_list[j] = Temperature_list[j], Temperature_list[i]

print(Temperature_list)
sorted(Temperature_list) # simple built in method


'''
Practice Pronlem -> 8 
M3. Build a Money class supporting both __add__ and __sub__ , plus __eq__ . Test all three operators.
'''
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
            return self.amount - other.amount

    def __eq__(self, other):
            return self.amount == other.amount
    
    def __str__(self):
            return self.amount

print(Money(20) + Money(60))
print(Money(80) - Money(60))
print(Money(20) == Money(60)) 

'''
Practice Problem -> 9
I1. What's the difference between __str__ and __repr__ ? When is each used, and which should you define if you
write only one?

Ans -> 
__str__  → "How should a normal user see this object?"
__repr__ → "How should a developer see this object?" "__repr__ = developer/debug representation 🧑‍💻"
"__str__ is for humans, __repr__ is for developers and containers."

'''

'''
Practice Problem -> 10
I2. What is operator overloading? Give an example where overloading + is a good idea and one where it would be
confusing.

Ans -> operator overloading mean defining how a operator should behave in class and operator overloading is good to use when we require to work with 2 object of a class and its confusing to use when we do not rquire to work with multiple  object of a class 
example->
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return f"${self.amount + other.amount}"

    def __str__(self):
        return self.amount
'''

'''
Practice Problem-> 11
I3. What does __slots__ do, when does it actually help, and what flexibility do you give up by using it?

Ans -> lets conisder a real world case when you are asked to prepare for a class for student but u have not told how many studnets will be there in that case u make need to consider for large space so everyone can fit , but if u have been told that there will be 5 student u then u just created space for 5 student this makes your work easy for managing space similarly __slot__ works in python class

__slots__ used It defines which instance attributes are allowed. and make it faster for python to work as it already know how much space it require and how many values will be comming 

ex :
class add:
    __slots__ = ["x", "y"]
    def __init__(self, x, y)
       self.x = x
       self.y = y
'''
