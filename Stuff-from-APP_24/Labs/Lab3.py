
# Instructions:
# 3) Define a base class "Vehicle" with the following attributes:
# • make (string): The make of the vehicle (e.g., "Toyota", "Ford").
# • model (string): The model of the vehicle (e.g., "Corolla", "F-150").
# • year (integer): The year the vehicle was manufactured
# • speed (float): The current speed of the vehicle.
# 4) Create an __init__ method inside the class to initialize the attributes

# 5) Define a method called brake that will decrease the speed of the vehicle.
# 6) Create two subclasses: "Car" and "Bicycle", inheriting from the "Vehicle" class.
# • Each subclass should have its unique attributes and methods:
# o For the "Car" class, add an attribute fuel_level (float) and a method refuel to
# simulate refueling.
# o For the "Bicycle" class, add an attribute pedal_cadence (integer) and a method
# change_cadence to adjust the pedaling speed.
# 7) Create instances of the "Car" and "Bicycle" classes and use their methods to simulate actions.
# 8) Run the program and observe the output.

def main():
    class Vehicle:
        def __init__(self, make, model, year, speed):
            self.make = make
            self.model = model
            self.year = year
            self.speed = speed

        def brake(self, value):
            self.speed -= value
            print(self.speed)

        def speed_up(self, value):
            self.speed += value
            print(self.speed)

        def show(self):
            print(self.make, self.model, self.year, self.speed)

    class Car(Vehicle):
        def __init__(self, *args, speed=0.0, fuel_level=0.0):
            super().__init__(*args, speed)
            self.fuel_level = fuel_level

        def refuel(self, value):
            self.fuel_level += value
            print(self.fuel_level)

    class Bicycle(Vehicle):
        def __init__(self, *args, speed=0.0, pedal_cadence=0):
            super().__init__(*args, speed)
            self.pedal_cadence = pedal_cadence

        def change_cadence(self, pedal_cadence):
            self.speed = pedal_cadence

    b = Bicycle("Bike", "Generic", 2024)
    c = Car("Toyota", "Corolla", 1997)

    b.change_cadence(1)

    c.speed_up(10)
    c.brake(5)

    c.refuel(1.1)
    c.refuel(1.9)



if __name__ == "__main__":
    main()
