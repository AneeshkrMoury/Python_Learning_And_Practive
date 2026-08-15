
# Practice problem - 1
'''
B1. Model a Playlist that holds many Song objects (title, duration). Add add_song() and a total_duration() method 
'''

'''
Noun in the problem        Big enough to be a class?       Becomes
Song                       hold song title and duration    yes
playlist                   create a playlist of songs      yes
add song                   just add songs                  no
total duration             just add duration               no
''' 

class Song:
    def __init__(self, song, duration):
        self.song = song
        self.duration = duration

    def __repr__(self): 
        return f"{self.song} ({self.duration}s)"


class Playlist:
    def __init__(self, p_list_name):
        self.name = p_list_name
        self.song_list = []

    def add_song(self, name):
        self.song_list.append(name)
        print(f"Added {abc.song} to {self.name}") 

    def total_duration(self):
        return sum(song.duration for song in self.song_list)


abc = Song("Jiya Jyae na" , 30)
deg = Song("Tum Bin" , 30)


mysongs = Playlist("MySongs")
mysongs.add_song(abc)
mysongs.add_song(deg)

print(mysongs.song_list)

print(mysongs.total_duration(),"s")


#Practice problem 2
'''
B2. Model a classroom  that holds many students objects (name, marks). Add a method that prints the class topper


Noun in the problem        Big enough to be a class?              Becomes
students                   hold name and marks                    yes 
classroom                  holds stundets obj and print topper    yes
topper                     method to check topeer                 No
'''

class Students: 
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

        print("added", self.name)


class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students_details = []

    def add_student(self, s_name):
        self.students_details.append(s_name)

    def topper(self):
        t_name = None
        mark = 0
        t_marks = 0
        for std in self.students_details:
            marks = sum(std.marks)
            if marks > t_marks:
                t_marks = marks
                t_name = std.name
                mark = std.marks

        print(f"Topper -> {t_name}, \nOptained Marks -> {mark}, \nTotal Marks -> {t_marks}/300")


aneesh = Students("Aneesh" , [78, 92, 85])
monu = Students("Monu" , [64, 88, 91])
archana = Students("Archana" , [89, 73, 95])

d_4 = Classroom("4_D")

d_4.add_student(aneesh)
d_4.add_student(monu)
d_4.add_student(archana)

d_4.topper()


#practice problem - 3
'''
B3. For the food app, add a  show_bill() method to Order that prints each item with its price, then the total at the bottom.
'''

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):  # repare method to correct priniting problem of order list itmes present in order items
        return f"{self.name} (${self.price})"



class Restorant:
    def __init__(self, name):
        self.nameme = name
        self.menu = []   

    def add_dish(self, item):
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            print(f"{item.name} -${item.price}")


class order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self , item):
        self.items.append(item)
        print(f"Added {item.name}")

    def total(self):
        return sum(item.price for item in self.items)
    
    def remove_item(self, item):
        self.items.remove(item)
        print(f"{item} removed from order of {self.customer}")

    def show_bill(self):
        self.item_width = 25
        self.price_witdth = 12
        self.total_with = 37

        print(f"="*self.total_with)
        print("INVOICE / RECEPIT".center(self.total_with, " "))

        for item in self.items:
            dish_name = (item.name).ljust(self.item_width)
            dish_price = str(item.price).rjust(self.price_witdth)
            print(dish_name, dish_price)

        print(f"-"*self.total_with)
        print ("Total".ljust(self.item_width),str(self.total()).rjust(self.price_witdth))
        print(f"-"*self.total_with)



pizza = MenuItem("Pizz", 250)
coke = MenuItem("Coke", 60)

r = Restorant("PizzHut")
r.add_dish(pizza)
r.add_dish(coke)


a = order("Aneesh") # customer 

r.show_menu() # check menu 

a.add_item(r.menu[0])  # add item 
a.add_item(r.menu[1])

print(f"Total: ${a.total()}") # check total

a.remove_item(a.items[1])

a.show_bill()


# practice problem  - 4
'''
M1. Library. Build three classes: book  (title, available), Member (name, borrowed list), and library (holds book and memebrs ) with a borrow(member, book) method that checks availability and updates both objects.

Noun in the problem        Big enough to be a class?              Becomes
book                        hold title and book status              yes 
member                                                              yes
library                                                             yes
'''

class Book:
    def __init__(self, title, available):
        self.title = title
        self.available = available

    def __repr__(self):
            return f"{self.title} {self.available}"


class Member:
    def __init__(self, name, barrowed_list=None):
        self.name = name
        self.barrowed_list = barrowed_list if barrowed_list is not None else []

    def __repr__(self):
        return f"{self.name} {self.barrowed_list}"


class library:
    def __init__(self, books, members):
        self.books = books
        self.members = members

    def borrow(self, member, book):

        if member in self.members:
            print(f"welcom to library {member.name}")
            if book in self.books and book.available == True:
                print("requested book issued....")
                book.available = False
                member.barrowed_list.append(book.title)
            else:
                print(f"requested book is issued to another member come back in few days")
        else:
            print(f"to issue book you need to become memeber first")




geeta = Book("geeta", True)
nolife = Book("nolife", True)

aneesh = Member("Aneesh", ["lostword", "YourName"])
ane = Member("Ane")

members = [aneesh , ane]
books = [geeta , nolife]

city_library = library(books, members)
city_library.borrow(aneesh, geeta)
city_library.borrow(ane, geeta)
city_library.borrow("aness", geeta)

#practice question -5 
'''
M2. Quiz app. A Question (text, answer) and a Quiz that holds many Questions and has a run() method that asks each and scores the user.

Noun in the problem        Big enough to be a class?              Becomes
question                   hold question and its answer           yes
quiz                       hold the question and run method       yes 


--> question class used to create an object with test and answer --> the quiz class hold many question object and use run  method to ask those question and asaign score for each correct answer and maybe we can add another method that will the score at the end or include it in run method

'''
class Question :
    def __init__(self, text, answer ):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def run(self):
        print("----Welcome to Common Knowledge Quiz----")
        
        score = 0
        for index,ques in self.questions:
            print()
            print(f"Question No -> {index + 1}")
            print(ques.text)
            ans = float(input("enter answer using numerical value --> "))

            print()
            if ans == ques.answer:
                score +=1
                print(f"Correct answer...! \nYour score = {score}")
            else:
                print(f"incorrect answer...! \nYour score = {score}")

        print()
        print("=" * 25)
        print(f"Quiz Complete \nFinal Score : {score} / {len(self.questions)} ")

q1 = Question("total plantes in our solar system", 9)
q2 = Question("how many wonders do we have in world", 7)
q3 = Question("how many bones human body have", 207)
q4 = Question("what is the value of pi", 3.14)
q5 = Question("how many colors are present in rainbow", 7)

ques = [q1,q2,q3,q4,q5]

obj = Quiz(ques)
obj.run()

#Question Number 7
'''
I1. What is composition (the "has-a" relationship)? Give an example of an object that holds other objects and explain why that's useful
Ans-> Composition = one object/class contains other objects and uses them to do its job.

'''
#Question no - 8
'''
12 Inthe food app, why is total() amethod on order and noton Nenurtes or Restaurant ? Explain responsibility” in your answer
Ans -> Order should have total() because calculating the total is the responsibility of an order. The Order object contains the items that were ordered, so it has the data needed to calculate the total. MenuItem is responsible for its own price, while Restaurant is responsible for its menu, not a customer's order.
'''
#Question no -9
'''
When you have several related classes, how do you decide what belongs in each? Give one sign a class is doing too much
Ans -> Related classes should each have their own clear responsibility. Put the data and methods that belong to that responsibility in that class. One sign that a class is doing too much is when it has several unrelated responsibilities or methods.
'''
