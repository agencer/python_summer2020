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
    ##  The simplest complexity with two attributes: 
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
    ##  It only takes 2 attributes:
    ##  Least complex.
    def __init__(self, _value = None):
        self.head = _value
        self.length = 0  # This is an empty list to append node values in an order. 


    ##  length(self): Returns the length of the list
    ##  Only one step, the most efficient.
    def length(self):
        return self.length            #   showing the length

    ##  addNode(self, new_value): Takes a number and adds it to the end of the list
    ##  This function is the most efficient one except for the print message at the end.
    ##  Total of n moves. 
    def addNode(self, new_value):
        new_node = Node(_value = new_value)
        lastest_node = self.head
        if self.head == None:
            self.head = new_node
        else:
            while lastest_node.next != None:
                lastest_node = lastest_node.next
            lastest_node.next = new_node
        self.length += 1
        print(new_value, "is linked to the end of linkedList.")

    ##  addNodeAfter(self, new_value, after_node): Takes a number and adds it after the after_node
    ##  This function is the most efficient one.
    ##  Total of n moves. 
    def addNodeAfter(self, new_value, after_node):
        new_node = Node(_value = new_value, _next = after_node.next)
        after_node.next = new_node
        self.length += 1

    ##  addNodeBefore(self, new_value, before_node): Takes a value and adds before the before_node
    ##  This function is the most efficient one.
    ##  Total of n moves.
    def addNodeBefore(self, new_value, before_node):
        new_node = Node(_value = new_value, _next = before_node)
        lastest_node = self.head
        while lastest_node.next != before_node:
            lastest_node = lastest_node.next
        lastest_node.next = new_node 
        self.length += 1          

    ##  removeNode(self, node_to_remove): Removes a node from the list
    ##  This function is the most efficient one.
    ##  Total of n moves.
    def removeNode(self, node_to_remove):
        lastest_node = self.head
        while lastest_node.next != node_to_remove:
            lastest_node = lastest_node.next
        lastest_node.next = node_to_remove.next  
        self.length -= 1

    ##  removeNodesByValue(self, value): Takes a value, removes all nodes with that value
    ##  This function is the most efficient one.
    ##  Total of n moves.
    def removeNodesByValue(self, value):
        lastest_node = self.head
        while (lastest_node.next).value != value:
            lastest_node = lastest_node.next
        lastest_node.next = lastest_node.next.next  
        self.length -= 1

    ##  reverse(self): Reverses the order of the linked list

    ##   __str(self)__: Displays the list in some reasonable way   
    def __str__(self):          #   Displays both head node and whole string of node values.
        if self.head == None:   
            return "None (PS. The linkedList is empty)."    #   If linkedList is empty, this message pops out. 
        else:
            print_me = ""
            lastest_node = self.head
            while lastest_node.next != None:
                print_me += str(lastest_node.value) + "  ->  "
                lastest_node = lastest_node.next
            print_me += str(lastest_node.value)       #    THis creates the string list of all node values by order.
            self.print = print_me
            return f"Head = {self.head.value}, \nTail = {lastest_node.value}, \nTotal list = {print_me}."


##
##
##
##  Let's try our class:
my_linkedlist = LinkedList()
print(my_linkedlist)
my_linkedlist.length

##
##
##
##  So far so good! Now let's use the addNote class method:
my_linkedlist.addNode(42)   #   I mean, that's the magical number.
print(my_linkedlist)
my_linkedlist.addNode(24)   #   The symmetry of a magic must be still magical
my_linkedlist.addNode(66)   #   The sum of two magic must be still magicalprint(my_linkedlist)
print(my_linkedlist)
my_linkedlist.addNode(77)   #   Add another number divisible by 11
my_linkedlist.addNode(88)
print(my_linkedlist)
print(my_linkedlist.head, my_linkedlist.head.next, my_linkedlist.head.next.next, my_linkedlist.head.next.next.next, my_linkedlist.head.next.next.next.next, my_linkedlist.head.next.next.next.next.next)
my_linkedlist.length        #   Five elements, yes!

##
##
##
##  Let's add 76 and 78 before and after the node that includes 77: 
print(my_linkedlist.head.next.next.next)        ##  This node is 77.
node_77 = my_linkedlist.head.next.next.next     ##  Let's create a copy. 
node_77                                         ##  This node is 77.

my_linkedlist.addNodeAfter(78, node_77)         ##  Let's add 78 after 77.
print(my_linkedlist)                            ##  Yes, yes, yes

my_linkedlist.addNodeBefore(76, node_77)        ##  Let's add 76 before 77.
print(my_linkedlist)                            ##  Yes, yes, yes
my_linkedlist.length                            ##  Seven elements, yes!

##
##
##  
##  let's check the removeNode function. Let's get rid of node_77:
my_linkedlist.removeNode(node_77)        ##  Let's add 76 before 77.
print(my_linkedlist)                            ##  Yes, yes, yes
my_linkedlist.length                            ##  Six elements, yes!

##  Now 76 and 78 are extra. Let's check the removeNodesByValue function. Let's get rid of 76 and 78:
my_linkedlist.removeNodesByValue(76)            ##  Let's remove value 76.
my_linkedlist.removeNodesByValue(78)            ##  Let's remove value 78.
print(my_linkedlist)                            ##  Yes, yes, yes
