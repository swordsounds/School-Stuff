def postorder(node):
    if node:
        postorder(node.leftChild)
        postorder(node.rightChild)
        print(node.data) 
def preorder(node):
    if node:
        print(node.data) 
        preorder(node.leftChild)
        preorder(node.rightChild)
def inorder(node):
    if node:
        inorder(node.leftChild)
        print(node.data) 
        inorder(node.rightChild)


class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def __repr__(self):
         return str(self.data)
# Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

# Creating root node
root = Node(3)
# Inserting values in BST
root.insert(1)
root.insert(4)
root.insert(2)
root.insert(5)

# printing BST
# root.PrintTree()

postorder(root)
print()
preorder(root)
print()
inorder(root)