# class Node, working on  version 1
class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

  def printname(self):
    print(self.data, self.left, self.right)

class BinaryTreeSearch:
   def __init__(self, root):
     self.root = root
#Use the Node class to create an object, and then execute the printname method:
x = Node(10, None, None)
x.printname()