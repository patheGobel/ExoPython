"""
OOP Exercise 5: Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
    
Expected Output:

Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18    
"""
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def affiche(self):
        return f"Color: {Vehicle.color}, Vehicle name: {self.name}, Speed:{self.max_speed}, Mileage: {self.mileage}"
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

modelx = Bus ("School Volvo", 180, 12)
modely = Vehicle("Audi Q5", 240, 18)
print(f"{modelx.affiche()}\n{modely.affiche()}")
