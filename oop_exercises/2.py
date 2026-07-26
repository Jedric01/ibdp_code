class Vehicle:

    # method - constructor
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def accelerate(self):
        print("accelearating...")

    

# variables (attributes) vs functions (behaviours)

bicycle = Vehicle(5,  10)
car = Vehicle(120, 20000)

bicycle.accelerate()
