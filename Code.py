class StockItem:
    stock_category = "Car accessories"

    def __init__(self, stock_code, quantity, price):
        self.stock_code = stock_code
        self.quantity = quantity
        self.price = price

    def get_stock_name(self):
        return "Navigation System"

    def get_stock_description(self):
        return "Unknown Stock Name"

    def increase_stock(self, amount):
        if amount < 1 or self.quantity + amount > 100:
            print("Error: Invalid stock level.")
        else:
            self.quantity += amount

    def sell_stock(self, amount):
        if amount < 1:
            print("Error: Invalid stock amount.")
        elif amount > self.quantity:
            return False
        else:
            self.quantity -= amount
            return True

    def get_price_with_vat(self):
        vat_rate = 0.175
        return self.price * (1 + vat_rate)

    def __str__(self):
        return (f"Stock Category: {self.stock_category}\n"
                f"Stock Type: {self.get_stock_name()}\n"
                f"Description: {self.get_stock_description()}\n"
                f"StockCode: {self.stock_code}\n"
                f"PriceWithoutVAT: {self.price}\n"
                f"PriceWithVAT: {self.get_price_with_vat():.2f}\n"
                f"Total unit in stock: {self.quantity}\n")


item = StockItem("W101", 10, 99.99)

print("Printing item stock information:")
print(item)
item.increase_stock(15)
print("Increasing 10 more units")
print("Printing item stock information:")
print(item)
result = item.sell_stock(2)
if result:
    print("Sold 2 units")
else:
    print("Error: Not enough stock.")
print("Printing item stock information:")
print(item)
item.price = 100.99
print("Set new price 100.99 per unit")
print("Printing item stock information:")
print(item)

# Task 2:

class NavSys(StockItem):
    def __init__(self, stock_code, quantity, price, navsys_brand):
        super().__init__(stock_code, quantity, price)
        self.__navsys_brand = navsys_brand

    def get_stock_name(self):
        return "Navigation system"

    def get_stock_description(self):
        return "Unknown Stock Name"

    def __str__(self):
        return super().__str__() + f"Brand: {self.__navsys_brand}\n"

item = NavSys("W101", 10, 99.99, "Unknown Stock Name")
print("Printing item stock information:")
print(item)
item.increase_stock(10)
print("Increasing 10 more units")
print("Printing item stock information:")
print(item)
result = item.sell_stock(2)
if result:
    print("Sold 2 units")
else:
    print("Error: Not enough stock.")
