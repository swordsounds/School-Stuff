# You're building a system for a new startup that's
# all about optimizing productivity through caffeine.
# However, if someone tries to log less than 2 cups
# of coffee, confront them with a
# NotEnoughCaffeineError. This startup runs on
# coffee, after all.

def main():
    class Monitor:
        def __init__(self, cups):
            self.cups = cups

        def caffiene(self):
            if self.cups < 2:
                raise Exception("NotEnoughCaffeineError")
            else:
                return "Success"


    m = Monitor(int(input("Please enter cups of joe: ")))
    print(m.caffiene())

if __name__ == "__main__":
    main()