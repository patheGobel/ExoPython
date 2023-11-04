"""
OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

if isinstance(School_bus, Vehicle):
    print("School_bus est une instance de Vehicle.")
else:
    print("School n'est pas une instance de Vehicle.")