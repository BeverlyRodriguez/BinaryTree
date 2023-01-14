print("\n\t\t ********PROGRAMMED BY:******** ")
print("\t\t ***BEVERLY ANN L. RODRIGUEZ***\n ")

# BINARY TREE ACTIVITY
# Creating a demo using the letters in your fullname as the content of the binary tree.


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist