# In this assignment you will write a recursive function that determines whether or not a string is
# a palindrome.
    # • The empty string is a palindrome, as is any string containing only one character
    # • Any longer string is a palindrome if its first and last characters
# match, and if the string formed by removing the first and last characters is also
# a palindrome.

# Write a main program that reads a string from the user. Use your recursive function
# to determine whether or not the string is a palindrome. Then display an appropriate
# message for the user

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    
    def preorder(node):
        if node:
            print(node.value)
            node.left.preorder()
            node.right.preorder()
    def insert_node(self, val):
        if val < self.value:
            if self.left:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right:
                self.right = Node(val)
            else:
                self.right.insert(val)

root = input("Enter a string: ")