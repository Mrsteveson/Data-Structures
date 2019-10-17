import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
"""If smaller go left
if bigger or equal go right
Does not have to be balanced?
Negative numbers are not 
allowed?
Not sure how it handles chars
When deleting, smaller child
becomes parent
Deleting root, replace with largest node on left side
Root starts as first node and stays unless deleted"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # Go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Base case, if no nodes just return
        if node == None:
            return
        # Start left to go lowest to highest value
        if node.left != None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right != None:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use a queue for breadth first
        bft = Queue()
        bft.enqueue(node)
        # Create a loop to iterate through nodes
        # If nodes exist, loop.
        while bft.size > 0:
            node = bft.dequeue()
            # Print the value we are taking out
            print(node.value)
            if node.left != None:
                bft.enqueue(node.left)
            if node.right != None:
                bft.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Use a stack for depth first
        dft = Stack()
        dft.push(node)
        # While something exists, we traverse
        while dft.len() > 0:
            node = dft.pop()
            # Print the value we are taking out
            print(node.value)
            if node.left:
                dft.push(node.left)
            if node.right:
                dft.push(node.right)
            


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
