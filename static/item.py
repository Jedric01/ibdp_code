class Item:
    # static variables - belong to the class, shared by all instances
    count = 0

    # static method - belongs to the class
    def getStore():
        print('using static method to getStore.')

    # attributes (instance variables - belong to an instance) and behaviours (instance methods)
    def __init__(self, name, price, brand):
        # instance variables
        self.name = name
        self.price = price
        self.brand = brand

        self.id = Item.count 
        Item.count += 1

    # instance method
    def checkPrice(self):
        print('checking price....')

Item.getStore()

item_a = Item('Toothpaste', 20, 'colgate')
item_b = Item('Toothpaste', 40, 'sendodyne')
item_c = Item('Bread', 30, 'A1-Bakery')
item_d = Item('Chips', 10, 'Lays')

print(item_a.count)

item_a.getStore()

print(item_a.id)
print(item_b.id)
print(item_c.id)
print(item_d.id)