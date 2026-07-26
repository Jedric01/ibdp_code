class Vehicle:

    # special method - constructor
    def __init__(self, num_of_wheels, brand, mileage, owner):
        self.__num_of_wheels = num_of_wheels
        self.__brand = brand
        self.__mileage = mileage
        self.__owner = owner

        self.__read_db()

    def acclerate(self): 
        print('aceelerating...')

    def brake(self):
        print('braking...')

    def get_owner(self, password):
        if password == '1234':
            return self.__owner
        print('Sorry, wrong password!')


    def get_num_of_wheels(self):
        return self.__num_of_wheels

    def set_num_of_wheels(self, wheels):
        if wheels < 0: 
            print('Sorry, number of wheels must be a positive number')
        else:
            self.__num_of_wheels = wheels
            print("Successfully changed the number of wheels!")

    def get_brand(self):
        return self.__brand 

    def set_brand(self, brand):
        self.__brand = brand

    def get_mileage(self):
        return self.__brand 
    
    def set_mileage(self, mileage):
        self.__mileage = mileage

    def __read_db(self):
        print('Readding DAtabase and senstive information')
    

ev1 = Vehicle(4, 'tesla', 200, 'Jane')
ev2 = Vehicle(4, 'rivian', 250, 'John')

owner = ev2.get_owner('12345')
ev1.set_num_of_wheels(5)

print(ev1.get_num_of_wheels())


