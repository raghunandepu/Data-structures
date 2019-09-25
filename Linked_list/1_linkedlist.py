class Node():
  def __init__(self, data):
    self.data = data
    self.nextNode = None
    
class LinkedList():
  def __init__(self):
    self.head = None
    self.size = 0
   
  # O(1) 
  # Insert at begining
  def insertStart(self, data):
    self.size = self.size + 1
    newNode = Node(data)
    if not self.head:
      self.head = newNode
    else:
      newNode.nextNode = self.head
      self.head = newNode
      
  
  # Remove node
  def remove(self, data):
    if self.head is None:
      return
    self.size = self.size -1
    
    currentNode = self.head
    previousNode = None
      
    while currentNode.data != data:
      previousNode = currentNode
      currentNode = currentNode.nextNode
      
    if previousNode is None:
      self.head = currentNode.nextNode
    else:
      previousNode.nextNode = currentNode.nextNode
      
      
    
  # O(1)
  def size1(self):
    return self.size
  
  # O(N) --> not good
  def size2(self):
    actualNode = self.head
    size=0
    
    while actualNode is not None:
      size+=1
      actualNode = actualNode.nextNode
      
    return size
  
  # Insert at middle
  def insertMid(self, data, previousNode):
    self.size = self.size + 1
    newNode = Node(data)
    
    actualNode = self.head
    while actualNode.data != previousNode:
      actualNode = actualNode.nextNode
    
    newNode.nextNode = actualNode.nextNode
    actualNode.nextNode = newNode
    
  # Insert at end
  # O(N)
  def insertEnd(self, data):
    self.size = self.size + 1
    newNode = Node(data)
    actualNode = self.head
    while actualNode.nextNode is not None:
      actualNode = actualNode.nextNode
      
    actualNode.nextNode = newNode
   
  # Traversal
  def traversalList(self):
    actualNode = self.head
    while actualNode is not None:
      print ("%d" % actualNode.data)
      actualNode = actualNode.nextNode
     
# Test 
linkedlist = LinkedList()
linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)
linkedlist.insertMid(55,31)

linkedlist.traversalList()
print ("Size of linked list is:", linkedlist.size1())

print ("Removing items...")
linkedlist.remove(31)
linkedlist.remove(122)
linkedlist.remove(3)
linkedlist.remove(12)
print ("Size of linked list is:", linkedlist.size1())

