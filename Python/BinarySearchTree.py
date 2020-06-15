class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# checkval method to compare the value with nodes
    def checkval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" Not Found"
            return self.left.checkval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" Not Found"
            return self.right.checkval(val)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(10)
root.insert(5)
root.insert(12)
root.insert(7)
print(root.checkval(7))
print(root.checkval(13))
