# You're building a system for a new startup that's
# all about optimizing productivity through caffeine.
# However, if someone tries to log less than 2 cups
# of coffee, confront them with a
# NotEnoughCaffeineError. This startup runs on
# coffee, after all.

#Creates a custum exception
class CustomException(Exception):
    pass

#function to handle the input
def get_coffee(n):
    #Raises custom exception when cups are less than 2
    if n < 2:
        raise CustomException("NOT ENOUGH CAFFEIENE!")
    else:
        #prints if cups are greater than 2
        print("GREAT SUCCESS")

def main():
    #try and except to catch the custom exception and prints its
    try:
        get_coffee(int(input("Enter number: ")))
    except CustomException as e:
        print(f"Custom exception: {e}")


#Runs the main function is the name of this module is "main"
if __name__ == "__main__":
    main()