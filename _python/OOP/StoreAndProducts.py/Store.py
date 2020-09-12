from Product import Product
class Store:

    def __init__(self,name):
        self.name = name
        self.products = []
        
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        self.products.pop(id)
        #self.products[id].print_info()
        return self

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
            return self

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
        return self

    def print_inventories(self):
        print('Inventories:')
        for i in range(len(self.products)):
            self.products[i].print_info()
        return self
store1 = Store("toy's rus")

Toy = Product('Lego-Man', 100, 'Toy')
Milk = Product("Whole-Milk", 5, "Groceries")
Bread = Product("Wheat", 2, "Groceries")
Yogurt = Product("Chobbani", 3, "Groceries")
phone = Product("iphone", 1000, "Electronics")
# Using my method chaining
store1.add_product(Toy).add_product(Milk).add_product(Bread).add_product(Yogurt).sell_product(3).print_inventories().add_product(phone).print_inventories().inflation(10).print_inventories().set_clearance('Electronics', 15).print_inventories()
# store1.add_product(Milk)
# store1.add_product(Bread)
# store1.add_product(Yogurt)
# store1.sell_product(3)
# store1.add_product(phone)
# store1.print_inventories()
# store1.inflation(10)
# store1.print_inventories()
# store1.set_clearance('Electronics', 15)
# store1.print_inventories()
