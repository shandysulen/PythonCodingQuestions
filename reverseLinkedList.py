import LinkedList

#Initialize linked list
ll = LinkedList.LinkedList()
ll.pushToFront(5)
ll.pushToFront(4)
ll.pushToFront(3)
ll.pushToFront(2)
ll.pushToFront(1)

#Print original linked list
print "Original Linked List: "
ll.printList()

#Reverse the linked list
ll.reverse()

#Print reversed linked list
print "Reversed Linked List: "
ll.printList()
