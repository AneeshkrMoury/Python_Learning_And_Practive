'''
Practice Problem - 1

S1. Build the Employee → Manager hierarchy: parent 
super().__init__() and overrides Employee with  show( ) child manager that uses super().__init__() and overrides show().show() inside.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} salary is : {self.salary}")

class Manger(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def show(self):
        super().show()
        print(f"{self.name} lead team {self.team}")


emp = Manger("ravi", 542158, "rockstar")
emp.show()


'''
Practice Problem -> 2
Make an Animal parent with speak(), and childeren Dog and cat the each override speak() .Prove isinstance (dog, animal) is True 
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} can speak ")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} yelling woof.. woof... woof...")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} saying meow meow meow....")

ob1 = Animal("mikee")
ob1.speak()

ob2 = Dog("GalaxyDestroyer")
ob2.speak()

ob3 = Cat("kitty")
ob3.speak()

print(isinstance(ob2, Animal))
print(isinstance(ob3, Animal))
print(isinstance(ob3, Dog))


'''
Practice Problem 3 -> 
B1. Create a Vehicle parent (start() ) a Car child that adds honk() . Show the Car can do both.
'''

class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"starting......... {self.name}")

class Car(Vehicle):

    def honk(self):
        print(f"{self.name} is honking.... pooo pooo pooo pooo...")

obj = Car('Testoreta')
obj.start()
obj.honk()


'''
Practice Problem -> 4
B2. Give Shape a method area() that returns 0, then override it in Circle and Square children with real formulas
'''
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Circule(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return f" area of circule with {self.radius} : {3 * 3.14 * self.radius * self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return f" area of circule with {self.side} : {self.side * self.side}"

obj1 = Circule(54)
print(obj1.area())
obj2 = Square(48)
print(obj2.area())

'''
Practice Problem -> 5
use super().__init__(): a Person parent stores name; a  Teacher childs adds subject by caling super first
'''
class Perosn:
    def __init__(self, name):
        self.name = name

class Teacher(Perosn):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subjet = subject
    def show(self):
        print(f"{self.name} teaches {self.subjet}")

obj = Teacher("aneesh", "computer science")
obj.show()
        

'''
Practice Problem - 6
M1.Extend Employee→ Manager -> ceo (third level), each levels show() call super.show() and add one line 
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} salary is : {self.salary}")

class Manger(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def show(self):
        super().show()
        print(f"{self.name} lead team {self.team}")

class CEO(Manger):
    def __init__(self, name, salary, team, company):
        super().__init__(name, salary, team)
        self.company = company

    def show(self):
        super().show()
        print(f"{self.name} is CEO of {self.company}")


obj = CEO("Aneesh", 454412, "None2everyone")
obj.show()
    
'''
Practice Question 7
Build a smartphone(camera , Phone) wiht multiple inheritance Prine smartphone__mro__
'''
class Camera:
    def __init__(self):
        pass
    def click(self):
        print("Photo Captured...")

class Phone:
    def __init__(self):
        pass
    def caling(self):
        print("Calling..........")

class SmartPhone(Camera, Phone):
    def __init__(self):
        pass

smp = SmartPhone()
smp.click(), smp.caling()

print(SmartPhone.__mro__)  # MRO is: The order Python follows when searching for methods and attributes through an inheritance hierarchy
#SmartPhone --> Camera ---> Phone

'''
Practice Problem - 8
M3. Add a bonus () method to Employee. override it in manager to give a buigger bonus , using the parents bonus as the base via super()
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} salary is : {self.salary}")

    def bonus(self):
        return self.salary * 15 / 100

class Manger(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def show(self):
        super().show()
        print(f"{self.name} lead team {self.team}")

    def bonus(self):
            return super().bonus()* 1.5
    

class CEO(Manger):
    def __init__(self, name, salary, team, company):
        super().__init__(name, salary, team)
        self.company = company

    def show(self):
        super().show()
        print(f"{self.name} is CEO of {self.company}")

    def bonus(self):
        return super().bonus() * 2


obj = CEO("Aneesh", 454412, "rocksolid", "None2everyone")
obj.show()
print(obj.bonus())

'''
Practice Problem - 9
What's the difference between inheritance ("is-a") and composit       ("has-a")? Give one example of each and when you'd choose which.

Ans: in inheritance we use is-a represent class relationship like manager is a employee , teacher is a person this show that the manger is also employee and teacher is also a perosne , and has-a ompoist used when a object hold an another object like in order hold restorant objected for to get menu item and menu item and object of menu class that hold menu item name and price 
'''

'''
Practice Problem -10
What does super do, and why is calling super().__init__() in a child's constructor 

Ans: ssuper() is used to access methods of the next class in the inheritance hierarchy according to Python's MRO. In a child class, super().__init__() calls the next class's constructor so the parent can initialize the attributes that belong to it. This allows the child to reuse the parent's initialization instead of duplicating the code.
'''

'''
Practice Problem - 11
What is MRO? In class C(A, B) if both A and B define  which one does C use, and how would you confirm it?

Ans: MRO refer to method resultaion Order it isused by python to decide the order of class calling. it move from left to right 

solution -> C(A, B) 
we have 3 class C , A , B  Written in order called 
both a and b have run 
class C call run -> pyhton use MRO to find method run()
                    1->  look in to class C run() not fund move to next class
                    2 -> check class A found run() excute it finsihes the calling
'''
