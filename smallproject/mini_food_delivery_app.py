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
        self.discounts = 0
        self.dilivery_fess = 25

    def add_item(self , item):
        self.items.append(item)
        print(f"Added {item.name}")

    def Sub_total(self):
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

        dis_price = self.Sub_total() * self.discounts / 100

        print(f"-"*self.total_with)

        print ("Sub Total".ljust(self.item_width), str(self.Sub_total()).rjust(self.price_witdth))
        print(f"Discount ( {self.discounts}% )".ljust(self.item_width), str(dis_price).rjust(self.price_witdth))
        print("Dilivery Charge".ljust(self.item_width), str(self.dilivery_fess).rjust(self.price_witdth))
        print("Final Total".ljust(self.item_width), str(self.Sub_total() - dis_price + self.dilivery_fess).rjust(self.price_witdth))
        print(f"-"*self.total_with)

    # M3. Extend the food app: give Order a delivery fee and a apply_discount(percent)  method. Add a second restaurant and show orders can be built from either.
    def apply_discount(self, discount):
        self.discounts = discount



pizza = MenuItem("Pizz", 250)
coke = MenuItem("Coke", 60)
pasta = MenuItem("Pata", 80)
r = Restorant("PizzHut")
r.add_dish(pizza)
r.add_dish(coke)

a = order("Aneesh") # customer 

# r.show_menu() # check menu 
a.add_item(r.menu[0])  # add item 
a.add_item(r.menu[1])
a.apply_discount(25)
# print(f"Total: ${a.Sub_total()}") # check total
# a.remove_item(a.items[1])
a.show_bill()

r2 = Restorant("ItalioHut")
r2.add_dish(pizza)
r2.add_dish(coke)
r2.add_dish(pasta)

b = order("Ravi")
b.add_item(r2.menu[0])
b.add_item(r2.menu[1])
b.add_item(r2.menu[2])

b.show_bill()

