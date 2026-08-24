class Prodcut:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"
    
#inital product on cart 
a = Prodcut("A", 50)
b = Prodcut("B", 40)
c = Prodcut("C", 55)
d = Prodcut("D", 30)
e = Prodcut("E", 25)

class Cart():
    def __init__(self):
        self.product = [a,b,c,d,e]

    def add_prodcut(self, prod):
        self.product.append(prod)
        print(f"Product addition successful .....")

    def remove_product(self, prod):
        if prod in self.product:
            self.product.remove(prod)
            print(f"item removal successful ....")
        else:
            print(f"{prod} not present in Product list")
    def total(self):
        total = 0
        for i in self.product:
            total = total + i.price
        print(total)

    def length(self):
        print(len(self.product))

    def show(self):
        ls = []
        for i in self.product:
            ls.append(i.name)
        print(ls)

p1 = Prodcut("P1", 59)
p2 = Prodcut("P2", 54)

cart1= Cart()
cart1.add_prodcut(p1)
cart1.add_prodcut(p2)
cart1.length()
cart1.total()
cart1.show()
cart1.remove_product(c)
