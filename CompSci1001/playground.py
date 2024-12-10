class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None
    
    def get_data(self):
        return self.__data
    def set_data(self, new_data):
        self.__data = new_data
    def get_next(self):
        return self.__next
    
    def set_next(self, new_next):
        self.__next = new_next
    
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0
    
    def add(self, newdata):
        temp = Node(newdata)
        temp.set_next(self.__head)
        self.__head = temp
        self.__size += 1
    
    def print_list(self):
        print("List of nodes:")

        current = self.__head
        while current != None:
            print(current.get_data())
            current = current.get_next()
    
    def search(self, value):

        current = self.__head
        
        while current != None:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False
    
    def remove(self, value):

        current = self.__head
        previous = None
        found = False

        while current != None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if found:
            if previous == None:
                self.__head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.__size -= 1
    
    def append(self, value):
        temp = Node(value)

        if self.is_empty():
            self.__head = temp
        
        else:
            current = self.__head
            while current.get_next() != None:
                current = current.get_next()

            current.set_next(temp)
        
        self.__size += 1
    
    def insert(self, value, index):
        if index <= 0:
            self.add(value)
        elif index >= self.__size:
            self.append(value)
        else:
            current = self.__head
            for i in range(0, index-1):
                current = current.get_next()
            
            temp = Node(value)
            temp.set_next(current.get_next())
            current.set_next(temp)
            self.__size += 1

    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size = size
    def get_head(self):
        return self.__head
    def set_head(self, node):
         self.__head = node
def main():

	ll = LinkedList()
	ll.append(78)
	ll.append(66)
	ll.append(502)
	ll.append(4)
	ll.print_list()

main()