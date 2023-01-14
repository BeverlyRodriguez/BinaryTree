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
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # Pre Order Traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # Finding Maximum Element
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # Finding Minimum Element
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    # Delete Method (For Exercise 2)
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    # Calculating Sum
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    
# Build Tree where 'elements' are the input.
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [50, 30, 10, 25, 20, 100, 80, 75, 65]
    numbers_tree = build_tree(numbers)

    
    # Printing Statements for Exercise 1
    print("\n\t\t\t\t>>>>>>>>>>>>>>>>>>>>>>>>> EXERCISE 1 <<<<<<<<<<<<<<<<<<<<<<<<<\n")
    print("\t\t\t\t\t\t\t LIST OF NUMBERS: \n\t\t\t\t\t     ", numbers)
    print("\n\n\t\t\t\tTOTAL SUM:\t\t", numbers_tree.calculate_sum())
    print("\t\t\t\tMAXIMUM NUMBER:\t\t",numbers_tree.find_max())
    print("\t\t\t\tMINIMUM NUMBER:\t\t",numbers_tree.find_min())
    print("\t\t\t\tIN ORDER TRAVERSAL:\t", numbers_tree.in_order_traversal())
    print("\t\t\t\tPRE ORFER TRAVERSAL:\t", numbers_tree.pre_order_traversal())
    print("\t\t\t\tPOST ORDER TRAVERSAL:\t", numbers_tree.post_order_traversal())

        
    print("\n\t\t\t\t>>SEARCH<<    IS THERE A NUMBER '20' ON THE LIST? \t", numbers_tree.search(20))
    print("\t\t\t\t>>SEARCH<<    IS THERE A NUMBER '50' ON THE LIST? \t", numbers_tree.search(50))
    print("\t\t\t\t>>SEARCH<<    IS THERE A NUMBERS '120' ON THE LIST? \t", numbers_tree.search(120))



    # Printing Statements for Exercise 2
    print("\n\t\t\t\t>>>>>>>>>>>>>>>>>>>>>>>>> EXERCISE 2 <<<<<<<<<<<<<<<<<<<<<<<<<\n")
    numbers_tree.delete(10)
    print("\t\t\t\tIN ORDER TRAVERSAL AFTER DELETING '10':\t", numbers_tree.in_order_traversal())
    numbers_tree.delete(20)
    print("\t\t\t\tIN ORDER TRAVERSAL AFTER DELETING '20':\t", numbers_tree.in_order_traversal())



    
