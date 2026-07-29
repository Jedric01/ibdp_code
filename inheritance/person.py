class Person:

    # static variable
    q = 50

    def __init__(self, name, age, height, weight):
        self.__name = name
        self.age = age
        self.height = height
        self.weight = weight

    def sleep(self):
        print('Person is sleeping...')

    def exercise(self):
        print('Person is exercising...')

    def foo(self):
        print(self.q)

class Student(Person):

    def __init__(self, name, age, height, weight, student_id):
        super().__init__(name, age, height, weight)
        self.student_id = student_id

    # method overriding
    def sleep(self):
        print('going through bedtime routine..')
        super().sleep()

s1 = Student('jane', 20, 170, 60, 101)
s1.sleep()

s1.foo()

# private: attribute cannot be access anywhere, except the class in which it was defined
# protected: attrbiutes are accessible in all child classes, but not outside
# public: attribute is accesible anywhere