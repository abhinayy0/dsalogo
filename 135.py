# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

# Function to initialize head
    def __init__(self):
        self.head = None
# def hello():
# Function to reverse the linked list
# Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

# Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverse(self):
        # if self.head is None:
        #     return None
        
        prev, curr = None, self.head

        while curr:
            print(curr.data)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr.next = nxt
        self.head = prev
        


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

