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
    
    def set_size(self, value):
        self.__size = value
    def get_size(self):
        return self.__size
    
    def set_head(self, node):
        self.__head = node
    def get_head(self):
        return self.__head

    def append(self, value):
        temp = Node(value)
        current = self.__head

        while current.get_node() != None:
            current = current.get_node()
        current.set_node(temp)

    def add(self, value):
        temp = Node(value)
        temp.set_node(self.__head)
        self.__head = temp
        self.__size += 1

    def print_list(self):
        current = self.__head

        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_node()

def main():
    x = LinkedList()
    x.add(1)
    x.add(2)
    x.append(3)
    x.append(4)
    x.print_list()

main()