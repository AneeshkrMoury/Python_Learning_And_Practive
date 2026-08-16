#inheritance -> a new class (the child) automatically get all the data and methods of an existing class (the parent) — then add or change what it needs. Write shared code once in the parent; every child gets it free.
# "is-a" -> employee is a person 

# inheritance can be done in many ways 
'''
1 -> single inheritance: one parent, one child
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)  # call parent class constrator or if chield class do not have any constrcator then parent class constractor is called direcctly 
        self.bread = bread

    def bark(self):
        print(f"{self.name} says woof")

    def show_bread(self):
        print(f"bread is {self.bread} ")

    #Method Overriding -> If a child defines a method with the same name as the parent's, the child's version wins(get called). This is overriding — the child replaces the inherited behavior with its own.
    
    def eat(self):
            print(f"Dog is eating and her name is {self.name}")
    
# a = Dog("leo", "vodaphone dog")
# a.eat()
# a.show_bread()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} earns ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def show(self):
        super().show() #if we have to call parent class method in chield then we use super().methodname() , super() — call the parent's version too
        print(f"Mnages a team of {self.team}")


# e = Employee("Aneesh", 50213)
# e.show()
# m = Manager("rakhi", 65000, 5)
# m.show()


#Multiple inheritance -> A class can inherit from more than one parent — list them all in the parentheses. It then gets methods from every parent.


class Camera:
    def click(self): 
        print("Photo taken")

class Phone:
    def call(self): 
        print("Calling...")

class Smartphone(Camera, Phone): # two parents
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print(f"model is {self.model}")


s = Smartphone("One+")
# s.show_model()
# s.click() # Photo taken (from Camera)
# s.call() # Calling... (from Phone)

'''
MRO (Method Resolution Order) is the rule Python follows to decide which parent to check first when a method exists in more than
one. It searches left to right, as listed. You can see the exact order:

left -- to --- right
'''
# print(Smartphone.__mro__)


'''

isinstance() and issubclass() Two built-ins to check relationships at runtime:
|=============================================================================================================================================|
| Function                  |  Question it answers                                             |  Example → result                            |
| isinstance (obj, Class)   |   Is this object an instance  of the class (or a child of it)?   |   isinstance (m,Employee)→ True              |
| issubclass(A, B)          |  Is class A a child of class B?                                  |  issubclass(Manager, Employee) → True        |
|=============================================================================================================================================|

'''

print(isinstance(s, Camera))
print(issubclass(Smartphone, Camera))
print(issubclass( Camera, Smartphone))
