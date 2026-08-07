#practice Question -1
'''S1. Build a Student class with name and marks. Add a method has_passed() that returns True if marks ≥ 40.'''

class Student :
    def __init__(self, name, marks ):
        self.name = name
        self.marks = marks

    def has_passed(self):
        if self.marks >= 40:
            return True
        
ob = Student("Aneesh" , 54)
print(ob.has_passed())


#practice problem 2 
'''S2. Create a Rectangle class with width and height. Add methods area() and perimeter().'''

class Rectangle:
    def __init__(self , width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
ob = Rectangle(12,45)
print(ob.area())

#practice problem 3 -> 
'''B1. Make a Car class with attributes brand and speed. Add a method show() that prints them nicely.'''

class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"car model is {self.brand} and its speed is {self.speed}")

ob = car("THOR", 300)
ob.show()


#practice question  - 4
'''Create a Book class with title and author. Instantiate 3 books and print all their titles using a loop'''

class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

books = {"Ramayan" : "Tulisdas",
         "Mahabhrat" : "Vedvyas",
         "LOOK khata" : "Aneesh"
        }

for aut , tit in books.items():
    ob = book(title=tit , author=aut)
    print(ob.title)


practice question 5 ->
'''
Write a Counter class that starts at 0 and has an increment() method. Create one object and increment it 5 times, then print the count
'''
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count  + 1
        
ob = Counter()
ob.increment()
ob.increment()
ob.increment()
ob.increment()
ob.increment()
print(ob.count)

#practice problem - 6
'''M1. Extend the BankAccount class: add a class attribute total_accounts that increases by 1 every time a new
account is created. Print it after making 3 accounts'''


class BankAccount:
    total_account = 0
    def __init__(self):
        BankAccount.total_account += 1
        

    def deposit(self):
        pass

    def widtdraw(self):
        pass


ob = BankAccount()
ob1 = BankAccount()
ob2 = BankAccount()
print(BankAccount.total_account)


#practice problem 7
'''

M2. Create a Temperature class storing celsius. Add a @staticmethod called c_to_f(c) that converts Celsius to
Fahrenheit, and an instance method fahrenheit() that uses it.

'''
class Temperature:
    def __init__(self, c):
        self.c = c

    @staticmethod
    def c_to_f(c):
        f = (c * 1.8) + 32
        return f

    def fahrenheit(self):
        fahrenheit = self.c_to_f(self.c)
        return fahrenheit


ob = Temperature(47)
print(ob.fahrenheit())

#practice question 8
'''
M3. Build a Playlist class holding a list of songs. Add add_song(), remove_song(), and total() methods
'''
class playlist:

    def __init__(self):
        self.songs = ["blinding lights", "as it was", "levitating", "watermaelon sugar", "flowers"]
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(song, "song added to list.....")
        else:
            print(song, "song is present in list....")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(song , "song removed")
        else:
            print(song , "song is already not in list....")

    def total(self):
        return len(self.songs)

ob = playlist()
print(ob.total())

ob1 = playlist()
ob1.add_song("tere bina na lage jiya")
print(ob1.total())
ob1.remove_song("tere bina na lage jiya")
print(ob1.total())


#practice problem - 9
'''I1. Add a @classmethod called from_string() to a Person class that builds an object from a string like "Rajeev-30"
(name-age). This is the "alternate constructor" pattern'''

class person:
    def __init__(self, Name, age):
        self.Name = Name
        self.age = age

    @classmethod
    def from_String(cls, data):
        Name,age  = data.split("-")
        age = int(age)
        return cls(Name,age)

p = person.from_String("aneesh-75")
print(p.Name , p.age)


#practice proble -10
'''I2. Explain in code the difference between changing a class attribute via the class (Dog.species = ...) vs via aninstance (d1.species = ...). Show what happens to d2 in each case.'''

class Dog:
    species = "________"      # class attribute
    def __init__(self, name):
        self.name = name

d1 = Dog("Tommy")
d2 = Dog("Rocky")

-------- Case 1 --------
Change class attribute using the class

Dog.species = "________"
print(d1.species)
print(d2.species)


-------- Case 2 --------
Create fresh objects
d1 = Dog("Tommy")
d2 = Dog("Rocky")

Change attribute using one instance
d1.species = "________"   #It creates (or overrides) an instance attribute for that object only.

print(d1.species)
print(d2.species)

#practice problem - 11
'''
I3. Design a Stack class (LIFO) using a list internally, with push(), pop(), peek(), and is_empty(). Handle popping from an empty stack gracefully
'''
class stack:

    def __init__(self):
        self.internal_list = []

    def push(self, item):
        self.internal_list.append(item)
        print("item added")

    def poped(self):

        if self.is_empty() == True:
            return("no data present")

        r = f"{self.internal_list.pop()} ....item removed"
        return r

    def peek(self):

        if self.is_empty() == True:
            return("no data present")

        return self.internal_list[-1]

    def is_empty(self):
        if len(self.internal_list) == 0:
            return  True
        return False


ob = stack()
ob.push(3513)
print(ob.peek())
print(ob.poped())
print(ob.is_empty())

