class Book:
    def __init__(self, title, author, edition):
        self.__title = title
        self.__author = author
        self.__edition = edition

    def get_info(self):
        return self.__title, self.__author
    
    # @property
    # def get_edition(self): 
    #     return self.__edition

    # @get_edition.setter
    @property
    def get_edition(self):
        if self.__edition <= 0:
            raise InvalidEditionError('Invalid edition')
        else:
            return self.__edition


class InvalidEditionError(Exception):
    pass

if __name__ == "__main__":
    try:
        b = Book("Book", "Idk Man", -3)
        b.get_edition
    except InvalidEditionError as e:
        print(f"Invalid Edition Error: {e}")