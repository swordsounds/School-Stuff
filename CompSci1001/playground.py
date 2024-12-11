class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__pointer = None

    def set_node(self, node):
        self.__pointer = node
    def get_node(self):
        return self.__pointer
    
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def set_head(self, node):
        self.__head = node
    def get_head(self):
        return self.__head
    
    def set_size(self, value):
        self.__size = value
    def get_size(self):
        return self.__size

    def search(self, value):
        current = self.__head

        while current != None:
            if current.get_data() == value:
                return True
            current = current.get_node()
        return False

    def add(self, value):
        temp = Node(value)
        temp.set_node(self.__head)
        self.__head = temp
        self.__size += 1
    
    def append(self, value):
        temp = Node(value)
        current = self.__head

        while current.get_node() != None:
            current = current.get_node()
        
        current.set_node(temp)

    def print_list(self):
        current = self.__head

        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_node()

def main():
    with open("README.md") as f:
        print(f.read())

    x = LinkedList()
    try:
        x.add(1)
        x.append(2)
        print(x.search(3))
        x.print_list()
    except Exeption as e:
        print(e)

main()