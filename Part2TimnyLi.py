class Book:
    def __init__(self, title, author, edition):
        self.__title = title
        self.__author = author
        self.__edition = edition

    def get_info(self):
        return self.__title, self.__author
    
    @property
    def get_edition(self):
        return self.__edition

if __name__ == "__main__":
    #created an instance of Book
    b= Book("The Lord of the Rings", "Idk Man", "3rd Edition")
    #accessed private attribute with getter
    print(b.get_info())
    #accessed private attribute with getter
    print(b.get_edition)