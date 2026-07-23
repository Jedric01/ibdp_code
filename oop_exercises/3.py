class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
a = Rectangle(10, 5)
b = Rectangle(15, 5)

x = a.area()
# print(a.perimeter())

print(x)


