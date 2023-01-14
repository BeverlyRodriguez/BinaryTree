print("\n\t\t\t\t\t\t********PROGRAMMED BY:******** ")
print("\t\t\t\t\t\t***BEVERLY ANN L. RODRIGUEZ***\n ")

# BINARY TREE ACTIVITY
# This program aims to test the COMPUTING SUM method.
# The list will contain numbers instead of letters. 


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # The value already exist.
    def add_child(self, data):
        if data == self.data:
            return

        
        #Goes to left subtree (if the data is < the value of current node)
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        #Goes to right subtree (if the data is > the value of current node)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
