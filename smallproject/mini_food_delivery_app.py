# Mini Food delivery app

# a restaurant has a menu of dishes . a customer builds an order by adding dishes and we show the running total

'''
Noun in the problem        Big enough to be a class?       Becomes
a dish (name+price)        yes — it has its own data       class MenuItem
a restaurant (name+menu)   yes — it holds many dishes      class Restaurant
an order (items + total)   yes — it has state & actions     class Order



New rule of thumb: if a noun has its own data and behavior, make it a class. Three real "things" → three classes. That decision is the
core design skill of this video

'''

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_dish(self, item):
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            print(f"{item.name} - ${item.price}")

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name}")

    def total(self):
        return sum(item.price for item in self.items)

pizza = MenuItem("Pizz", 250)
coke = MenuItem("Coke", 60)

r = Restaurant("PizzHut")
r.add_dish(pizza)
r.add_dish(coke)

a = order("Aneesh")
a.add_item(r.menu[0])
a.add_item(r.menu[1])
print(f"Total: ${a.total()}")
