class X():
    def __init__(self) -> None:
        self.__thing = "AAH"
        self._thin = "AAA"
x = X()
print(x.__thing, x._thin)