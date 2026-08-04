class Animal:

    # attributes
    # constructor
    def __init__(self, name, height, weight, species):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__species = species

        # print('Animal constructor')

    def eat(self):
        print('eating...')

    def rest(self): 
        print('resting...')

    # getter methods - accesors
    def getName(self, password):
        if password == '123':
            return self.__name
        else:
            print('wrong password')

    # setter methods - mutators
    def setName(self, name):
        if (len(name) < 5):
            print('sorry length of name must be >= 5')
        else:
            self.__name = name
            print('sucessfully set a new name')

class fourLegged:

    def walk(self):
        print('walking using four legs')


class Bird(Animal):

    # constructor
    def __init__(self, name, height, weight, species, max_flying_height):
        super().__init__(name, height, weight, species)
        self.max_flying_height = max_flying_height
        # print('Bird Constructor')

    def eat(self):
        print('eating birdfood...')

class Dog(Animal):
     # constructor
    def __init__(self, name, height, weight, species, breed):
        super().__init__(name, height, weight, species)
        self.breed = breed
        # print('Dog Constructor')

    # method overriding
    def eat(self):
        super().eat()
        print('eating dogfood...')

# swan: type => Bird, Bird inherits from Animal, therefore all attributes, methods in Animal are inherited by Bird
swan = Bird('swan1', 40, 30, 'swan', 200)
dog_a = Dog('dog_a', 40, 30, 'dog', 'husky')

print(swan.getName('123'))

swan.setName('swan123')

print(swan.getName('123'))

# swan.eat()
# dog_a.eat()

