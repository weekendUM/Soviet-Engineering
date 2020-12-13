class item:
    name = 'blank'
    price = 0

    def __init__(self, name, price):
        print("constructor for item class called...")
        self.name = name
        self.price = price

    def __hash__(self):
        print("hashing item...")
        return str(name + str(price)).__hash__()

class cart():
    items = {}
    
    def append(self, new_item : str, amount = 1):
        print("adding item...")
        self.items[new_item] = amount

    def __getitem__(self, item_name : str):
        print("showing item...")
        return self.items[item_name]

cart1 = cart()
cart1.append("suc", 3)
cart1.append("mere", 5)
cart1.append("paine")

print(cart1["mere"])