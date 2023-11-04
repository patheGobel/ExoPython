"""OOP Exercise 6: Class Inheritance
Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is 
Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become 
the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class 
in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

Expected Output:
Total Bus fare is: 5500.0

Données :

Créez une classe enfant Bus qui hérite de la classe Vehicle. La tarification par défaut de tout véhicule est la capacité d'assise * 100. 
Si le véhicule est une instance de Bus, nous devons ajouter un supplément de 10 % sur le tarif complet en tant que frais d'entretien. 
Ainsi, le tarif total pour une instance de bus deviendra le montant final = tarif total + 10 % du tarif total.

Remarque : La capacité d'assise du bus est de 50. Donc, le montant final du tarif devrait être de 5500. 
Vous devez substituer la méthode fare() de la classe Vehicle dans la classe Bus.

Utilisez le code suivant pour votre classe parent Vehicle. Nous devons accéder à la classe parent depuis l'intérieur d'une méthode de la 
classe enfant.

Sortie attendue :
Le tarif total du bus est de 5500,0.
"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        tarifTotal = super().fare()
        return  tarifTotal+tarifTotal*0.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())