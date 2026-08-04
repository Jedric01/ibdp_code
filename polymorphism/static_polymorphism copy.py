class A:

    # method overloading
    def hello(self, x):
        print(x)

    def hello(self, x, y):
        print(x, y)
        print('in 2nd method')


a = A()

a.hello(5)

