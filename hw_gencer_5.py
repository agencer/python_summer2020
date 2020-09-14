###############################################################
########################	HOMEWORK	#######################	
###############################################################

##
##
##
##
##	Author: Alper Sukru Gencer
##	Start Date: September 13, 2020
##	End Date: 	September 18. 2020
##
##
##
##


################################
####	QUESTIONS
################################

##  This homework is meant to guide you through implementing a data structure. For this 
##      homework you will be implementing a linked list. Note that this is a very common 
##      problem and you will be able to find the solutions readily on the internet. Try 
##      not to.
##
####    Singly Linked List
##
##	A Singly Linked List is a list comprised of many nodes. Each node contains some data, 
##      in our case just an integer, and a pointer to the next node in the list. The first 
##      node in the list is known as the head node. The last node in the graph has a 
##      pointer to a null next item. Represented graphically, a Singly Linked List looks 
##      like this (note that the head has value 5 and the tail has value 2):
##
##  Here is the image
##
##	Your assignment is to implement a LinkedList class with the following interface:
##
##	• __init__(self, value): Takes a number and sets it as the value at the head of the List
##  • length(self): Returns the length of the list
##  • addNode(self, new_value): Takes a number and adds it to the end of the list
##  • addNodeAfter(self, new_value, after_node): Takes a number and adds it after the after_node
##  • addNodeBefore(self, new_value, before_node): Takes a value and adds before the before_node
##  • removeNode(self, node_to_remove): Removes a node from the list
##  • removeNodesByValue(self, value): Takes a value, removes all nodes with that value
##  • reverse(self): Reverses the order of the linked list
##  • __str(self)__: Displays the list in some reasonable way
##  • hasCycle(self): Bonus: Returns true if this linked list has a cycle. This is non-trivial
##
##
##	For each of the above methods, figure out what the computation complexity of your 
##      implementation is and state whether or not you think that is the best possible 
##      complexity class. Make sure that your implementation is correct and robust to bad 
##      inputs.
##
##  You are free to define whatever private helper functions/classes/etc. that you need, 
##      but make sure that your implementation has the above public facing interface. 
##      You may NOT use any other data structures to implement this. That means no Lists, 
##      Arrays, Tuples, etc. You should use the following as the starter definition for a 
##
##      Node class:
##
#   class Node:
#       def __init__(self, _value=None, _next=None):
#           self.value = _value
#           self.next = _next
#       def __str__(self):
#           return str(self.value)




################################
####	SOLUTION:
################################


##
##
##
##  Starting:

class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)


##
##
##
##  Let's create a "my_node" object with Node class:

my_node = Node(80)
print(my_node)



##
##
##
##  Let's create a LinkedList class with the following interface:

class LinkedList:
    
    ##  __init__(self, value): Takes a number and sets it as the value at the head of the List
    def __init__(self, _value = None):
        self.head = _value
        self.list = []

    ##  Here I defined a helpful and comprehensive function called "addition":
    def addition(self, _new_value, _after_node, _before_node):
        new_node = Node(_new_value)
        lastest_node = self.head
        counter = 1
        if (_after_node == None) and (_before_node == None):
            if self.head == None:
                self.head = new_node
            else:
                while lastest_node.next != None:
                    lastest_node = lastest_node.next
                lastest_node.next = new_node
            self.list.append(_new_value)
        elif _after_node != None:
            while lastest_node.next != _after_node:
                lastest_node = lastest_node.next
                counter += 1
            lastest_node = lastest_node.next
            lastest_node.next = new_node
            counter += 1
            self.list.insert(counter, _new_value)            
        else:
            while lastest_node.next != _before_node:
                lastest_node = lastest_node.next
                counter += 1         
            lastest_node.next = new_node
            counter -= 1
            self.list.insert(counter, _new_value)            


    ##  addNode(self, new_value): Takes a number and adds it to the end of the list
    def addNode(self, new_value):
        self.addition(_new_value = new_value, _after_node = None, _before_node = None)

    ##  addNodeAfter(self, new_value, after_node): Takes a number and adds it after the after_node
    def addNodeAfter(self, new_value, after_node):
        self.addition(_new_value = new_value, _after_node = after_node, _before_node = None)
    
    ##  addNodeBefore(self, new_value, before_node): Takes a value and adds before the before_node
    def addNodeBefore(self, new_value, before_node):
        self.addition(_new_value = new_value, _after_node = None, _before_node = before_node)

    ##   __str(self)__: Displays the list in some reasonable way   
    def __str__(self):
        return f"Head = {self.head}, \nTotal list = {self.list}"


##
##
##
##  Let's try our class:

my_linkedlist = LinkedList()
print(my_linkedlist)

##
##
##
##  So far so good! Now let's use the addNote class method:

my_linkedlist.addNode(42)   #   I mean, that's the magical number.
print(my_linkedlist)

my_linkedlist.addNode(24)   #   The symmetry of a magic must be still magical
print(my_linkedlist)

my_linkedlist.addNode(66)   #   The sum of two magic must be still magical
print(my_linkedlist)

my_linkedlist.addNode(67)   #   +=1
print(my_linkedlist)

my_linkedlist.addNode(68)   #   +=1
print(my_linkedlist)

##
##
##
##  addNodeAfter(self, new_value, after_node): Takes a number and adds it after the after_node

my_linkedlist.addNodeAfter(33, 24)   #   I mean, that's the average of two magical numbers.
print(my_linkedlist)


##
##
##


##
##
##


##
##
##


##  • length(self): Returns the length of the list
##  • removeNode(self, node_to_remove): Removes a node from the list
##  • removeNodesByValue(self, value): Takes a value, removes all nodes with that value
##  • reverse(self): Reverses the order of the linked list
##  • hasCycle(self): Bonus: Returns true if this linked list has a cycle. This is non-trivial
