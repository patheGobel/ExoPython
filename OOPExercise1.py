"""OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""
class Vehicle():
    def __init__(self, max_speed, mileage) -> None:
        self.max_speed=max_speed
        self.mileage=mileage
        
modeLx = Vehicle(300,18)
print(modeLx.max_speed,modeLx.mileage)