# Task 1: Implement a Binary Tree Node
#   • Define a Node class with three attributes: val, left, and right.
#   • Initialize the node with a value, and set left and right children to None.
# Task 2: Build a Binary Tree
    # Using the Node class from Task 1, create the following binary tree:
    #  3
    # / \
    # 1 4
    #  \
    #   2
# Task 3: Implement Preorder, Inorder, and Postorder Traversals
    # Write functions for preorder, inorder, and postorder traversals of the binary tree.
    # Each function should print the values of the nodes in the order defined by the type of traversal.
# Task 4: Implement Insertion
    # Write a function to insert new nodes into the binary tree. For simplicity, insert nodes to ensure the tree
    # remains a binary search tree (BST). In a BST, for every node, all values in the left subtree are less than
    # the node’s value, and all values in the right subtree are greater.
    # Insert the following values into your binary tree: 5, 0. Test your tree by performing an inorder traversal
    # to print the values in ascending order.

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert_node(self, val):
        if val < self.value:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    
    def preorder(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
            

root = Node(3)

