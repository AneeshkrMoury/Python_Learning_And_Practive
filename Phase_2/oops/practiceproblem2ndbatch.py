# practice problem -1 
''' Give a Dog class a class attribute count that goes up by 1 with every new dog. Add a @classmethod how_many() that prints the total. Create 3 dogs and call it.'''

class Dog:
    count = 0
    def __init__(self):
        Dog.count = Dog.count + 1

    @classmethod
    def how_many(cls):
        print(f"Total Dog = {cls.count}")


ob1 = Dog()
ob2 = Dog()
ob3 = Dog()

Dog.how_many()
