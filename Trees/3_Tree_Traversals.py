# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

# Python program to for tree traversals 
  
# A class that represents an individual node in a 
# Binary Tree 

class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

# A function to do inorder tree traversal
def printInorder(root):
  if root:
    # First recurrence on left child 
    printInorder(root.left)
    # then print the data of node
    print(root.val, end =" ")
    # now recurrence on right child
    printInorder(root.right)
    
# A function to do postorder tree traversal 
def printPostorder(root):
  if root:
    
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val, end =" ")
    
def printPreorder(root):
  if root:
    print(root.val, end =" ")
    printPreorder(root.left)
    printPreorder(root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Preorder traversal of binary tree is: ", end ="")
printPreorder(root)
print("\n")

print ("Inorder traversal of binary tree is: ", end ="")
printInorder(root)
print("\n")

print ("Postorder traversal of binary tree is: ", end ="")
printPostorder(root)
print("")
    