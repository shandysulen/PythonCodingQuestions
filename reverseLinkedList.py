#Represents the Node class to be used in a LinkedList
class Node:

    #Function to initialize a node object
    def __init__(self, val):
        self.val = val
        self.next = None

#Represents the LinkedList class consisting of Node objects
class LinkedList:

    #Function to initialize a LinkedList
    def __init__(self):
        self.head = None

    #New function to insert new node at head of LinkedList
    def pushToFront(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    #Prints the LinkedList
    def printList(self):
        current = self.head
        while(current != None):
            print current.val, "\n"
            current = current.next

    #Function to reverse the LinkedList
    #Time complexity: O(n)
    #Space complexity: O(1)
    def reverse(self):
        prev = None
        current = self.head
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
