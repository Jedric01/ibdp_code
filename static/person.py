class Person:
    # static variables - belong to the class, shared by all instances
    name = ''

    # attributes (instance variables - belong to an instance) and behaviours (instance methods)
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

p1 = Person('Jane',28, 175)
p2 = Person('John', 25, 150)

print(p1.name)
