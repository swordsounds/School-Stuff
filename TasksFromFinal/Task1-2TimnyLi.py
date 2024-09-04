
#Should look like 
#   1
#  / \
# 2   3
# 
tree = {'value': 1, 
        'left':{'value': 2},
        'right':{'value': 3}
        }

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    @property
    def print_binary_tree(self):
        print(self.data)
        if self.left:
            self.left.print_binary_tree
        if self.right:
            self.right.print_binary_tree

# for value in tree.values():
#     try:
#         for value in value.values():
#             print(value)
#     except:
#         print("int")


x = Node(tree)
x.print_binary_tree

#IM COOKED, WHAT IS A BINARY TREEEEEE