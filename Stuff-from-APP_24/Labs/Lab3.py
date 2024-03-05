# Lab: Creating a Vehicle Hierarchy
# Objective: Create a Python class hierarchy representing different types of vehicles with shared
# attributes and methods.
# Instructions:
# 3) Define a base class "Vehicle" with the following attributes:
# • make (string): The make of the vehicle (e.g., "Toyota", "Ford").
# • model (string): The model of the vehicle (e.g., "Corolla", "F-150").
# • year (integer): The year the vehicle was manufactured
# • speed (float): The current speed of the vehicle.
# 4) Create an __init__ method inside the class to initialize the attributes when a new vehicle object
# is created.
# 5) Define a method called brake that will decrease the speed of the vehicle.
# 6) Create two subclasses: "Car" and "Bicycle", inheriting from the "Vehicle" class.
# • Each subclass should have its unique attributes and methods:
# o For the "Car" class, add an attribute fuel_level (float) and a method refuel to
# simulate refueling.
# o For the "Bicycle" class, add an attribute pedal_cadence (integer) and a method
# change_cadence to adjust the pedaling speed.
# 7) Create instances of the "Car" and "Bicycle" classes and use their methods to simulate actions.
# 8) Run the program and observe the output.

class Vehicle():
    def __init__(self, brand=None, type=None):
        self.brand = brand 
        self.type = type

    def brake(self):
        pass

class Car(Vehicle):
    def __init__(self, brand=None, type=None):
        super().__init__(brand, type)
        self.fuel_level = 100
        self.refuel = 10

    def brake(self):
        self.fuel_level -= 10
        if self.fuel_level <= 0:
            self.fuel_level = 0
            self.refuel = 10
            print("Braking")
            
class Bicycle(Vehicle):
    def __init__(self, brand=None, type=None):
        super().__init__(brand, type)
        self.pedal_cadence = 10
        self.change_cadence = 1
        self.speed = 0
