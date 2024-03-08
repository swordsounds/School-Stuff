def main():
    # Defined a base class "Vehicle" with the following attributes
    class Vehicle:
        #Created an __init__ method inside the class to initialize the attributes
        def __init__(self, make, model, year, speed=0.0):
            self.make = make
            self.model = model
            self.year = year
            self.speed = speed

        # Method called brake that will decrease the speed of the vehicle
        def brake(self, value):
            self.speed -= value
            return self.speed
        # Method called brake that will increase the speed of the vehicle
        def speed_up(self, value):
            self.speed += value
            return self.speed
        def show(self):
            print(f" The {self.model} model {self.year} {self.make}")
    # Created subclass "Car" that inherits from "Vehicle"
    class Car(Vehicle):
        def __init__(self, *args, speed=0.0, fuel_level=0.0):
            super().__init__(*args, speed)
            # Attribute fuel_level (float)
            self.fuel_level = fuel_level
        # Displays information/attributes
        def show(self):
            print("----------")
            print(f" The {self.model} model {self.year} {self.make}" 
                  f" has the speed of {self.speed} Km/h. And has {self.fuel_level} L of fuel")
            print("----------")
        # Method refuel to simulate refueling.
        def refuel(self, value):
            if self.fuel_level + value < 40:
                self.fuel_level += value
            else:
                self.fuel_level = 40
    # Created subclass "Bicycle" that inherits from "Vehicle"
    class Bicycle(Vehicle):
        def __init__(self, *args, speed=0.0, pedal_cadence=0):
            super().__init__(*args, speed)
            # Attribute pedal_cadence (integer)
            self.pedal_cadence = pedal_cadence
        # Displays information/attributes 
        def show(self):
            print("----------")
            print(f"The {self.model} model {self.year} {self.make}" 
                  f" has the pedal cadence of {self.pedal_cadence} RPM.")
            print("----------")
        
        # Method change_cadence to adjust the pedaling speed.
        def change_cadence(self, pedal_cadence):
            self.pedal_cadence = pedal_cadence
            return self.pedal_cadence
    #Created instances of the "Car" and "Bicycle"
    b = Bicycle("Bike", "Generic", 2024)
    c = Car("Toyota", "Corolla", 1997)

    b.change_cadence(10)
    b.change_cadence(100)

    c.speed_up(100)
    c.brake(20)

    #Calls the refuel method
    c.refuel(10.1)
    c.refuel(40)

    # Calls the show method of each subclass
    b.show()
    c.show()

    b = Vehicle("Bike", "Generic", 2024)
    c = Vehicle("Toyota", "Corolla", 1997)
    b.show()
    c.show()


# Runs main function if the module is the main module
if __name__ == "__main__":
    main()
