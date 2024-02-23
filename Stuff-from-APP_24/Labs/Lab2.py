#Task 3: Implement traversals
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value) 
def preorder(node):
    if node:
        print(node.value) 
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value) 
        inorder(node.right)

#Task 1: Implment Binary Tree Node
class Node:
    #Initializes the nodes values alogn with each of its subtrees
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
# Function to insert in BST
    def insert(self, val):
        # if value is lesser than the value of the parent node
        if val < self.value:
            if self.left:
                # if need to move towards the left subtree
                self.left.insert(val)
            else:
                #Makes a new left subtree when parent Node is "full"
                self.left = Node(val)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.right:
                # if need to move towards the right subtree
                self.right.insert(val)
            else:
                # Makes new right subtree when parent Node is "full"
                self.right = Node(val) 
                return

# Creating root node
root = Node(3)

# Inserting values in BST
# Task 2: Build a Binary Tree
root.insert(1)
root.insert(4)
root.insert(2)

# Task 4: Insert values 5, 0
root.insert(5)
root.insert(0)

#Prints out the traversals
print("--Post Order--")
postorder(root)
print()
print("--Pre Order--")
preorder(root)
print()
print("--In Order--")
inorder(root)