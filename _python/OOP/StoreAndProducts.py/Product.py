
class Product:
    def __init__(self, name=" ", price=0, category=" "):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            change = self.price * percent_change/100
            self.price = self.price + change
        else:
            self.price = self.price
            change = self.price * percent_change/100
            self.price = self.price - change

    def print_info(self):
        print(f"Product Name: {self.name} : Category: {self.category} : Price: ${self.price}")
        


# Toy1 = Product('Lego-Man', 100, 'Lego')









