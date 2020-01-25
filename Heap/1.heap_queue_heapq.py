# Reference: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# Python code to demonstrate working of heapify(), heappush(),heappop(), # heappushpop() and heapreplce()

import heapq

#initializing list
list1 = [5, 7, 9, 1, 3]

#using heapify to covert list into heap
heapq.heapify(list1)

# printing created heap
print("The created heap is : ", end="")
print(list(list1))

# using heappush() to push elements into heap and pushes 4
heapq.heappush(list1, 4)
# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(list1))


# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print (heapq.heappop(list1))

# using heappushpop() to push and pop items simultaneously 
# pops 2 
print ("The popped item using heappushpop() is : ",end="") 
print (heapq.heappushpop(list1, 2))

# using heapreplace() to push and pop items simultaneously 
# pops 3 
print ("The popped item using heapreplace() is : ",end="") 
print (heapq.heapreplace(list1, 6))

# Python code to demonstrate working of  
# nlargest() and nsmallest()

# initalizing the list
list2 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(list2)
print ("The modified list after heap: ",list2, end="")

# using nlargest to print 3 largest numbers 
# prints 10, 9 and 8 
print("The 3 largest numbers in list are : ",end="") 
print(heapq.nlargest(3, list2))

# using nsmallest to print 3 smallest numbers 
# prints 1, 3 and 4 
print("The 3 smallest numbers in list are : ",end="") 
print(heapq.nsmallest(3, list2))