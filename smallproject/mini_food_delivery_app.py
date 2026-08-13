# Mini Food delivery app 
# a restaurant has a menu of dishes . a custome builds an ordr by adding dishes and we show the running total




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

    def __repr__(self):  # repare method to correct priniting problem of order list itmes present in order items
        return f"{self.name} (${self.price})"



class Restorant:
    def __init__(self, name):
        self.anme = name
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


pizza = MenuItem("Pizz", 250)  # add menuitems
coke = MenuItem("Coke", 60)

r = Restorant("PizzHut")   #add restorant 
r.add_dish(pizza) # add items 
r.add_dish(coke)


a = order("Aneesh") # customer 

r.show_menu() # check menu 

a.add_item(r.menu[0])  # add item 
a.add_item(r.menu[1])

print(f"Total: ${a.total()}") # check total

a.remove_item(a.items[1])

print(a.items)
