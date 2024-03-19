# You're building a system for a new startup that's
# all about optimizing productivity through caffeine.
# However, if someone tries to log less than 2 cups
# of coffee, confront them with a
# NotEnoughCaffeineError. This startup runs on
# coffee, after all.

def main():
    class Monitor:
        #Initial attributes of cups
        def __init__(self, cups):
            self.cups = cups
        #Method to detemine the output
        def caffiene(self):
            if self.cups < 2:
                #raises a custum expectyion when the input is less than 2
                raise Exception("NotEnoughCaffeineError")
            else:
                return "Success"

    #Initializes an objct of Monitor
    m = Monitor(int(input("Please enter cups of joe: ")))
    #Prints the values that would be returned depending on the cups of coffee
    print(m.caffiene())

#Runs the main function is the name of this module is "main"
if __name__ == "__main__":
    main()