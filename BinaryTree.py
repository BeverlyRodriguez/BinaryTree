print("\n\t\t ********PROGRAMMED BY:******** ")
print("\t\t ***BEVERLY ANN L. RODRIGUEZ***\n ")

# BINARY TREE ACTIVITY
# Creating a demo using the letters in your fullname as the content of the binary tree.


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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # In-order traversal
    # Returning list of elements in specific order.
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    # Post Order Traversal
    # 

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


# Build Tree where 'elements' are the input.
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    name = ["B", "E", "V", "E", "R", "L", "Y", "A", "N", "N",
            "L", "R", "O", "D", "R", "I", "G", "U", "E", "B"]
    name_tree = build_tree(name)

    # Printing Statements
    print 

