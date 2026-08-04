class A:

    p = 5

    # method overloading
    def hello(self, x):
        print(x)

    def hello(self, x, y):
        print(x, y)
        print('in 2nd method')

    def foo(self):
        # here, python will pick the variable p that is most specific to the instance that is calling this method
        x = self.p * 2
        print(x + 5)

class B(A):
    p = 10

    def hello(self, x):
        print("in B's hello")

b = B()

b.foo()

