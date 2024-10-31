from periodictable import *

'''
---INSTRUCTIONS--

pip install periodictable

NOTE: Do this in the powershell terminal, also get python or a text editor to run.

''' 

def menu():
    print("\n1. Find Volume")
    print("2. Find Mass\n")

def volume_finder(density=None, mass=None):
    volume = mass/density
    return volume

def mass_finder(density=None, volume=None):
    mass = density * volume
    return mass

def main():
    menu()
    while True:
        try:
            stdin = int(input("Enter elemental number: "))
            
            name = elements[stdin].name
            density = elements[stdin].density
            print("\nElement: %s \nDensity %.3f g/cm^3\n" % (name, density))

            operator = str(input("Enter what to do (1 or 2): "))

            if operator == "1":
                value = float(input("Enter Mass (g): "))
                vol = volume_finder(density=density, mass=value)
                print("\n%s Vol: %.2f mL\n" %(name[0].upper()+name[1:],vol))

            elif operator == "2":
                value = float(input("Enter Volume (mL): "))
                mass = mass_finder(density=density, volume=value)
                print("\n%s Mass: %.2f g\n" %(name[0].upper()+name[1:], mass))

        except Exception as e:
            print("Input Valid input: %s" %e)
            quit('Bye Bye!')

if __name__ == "__main__":
    main()