# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning of the linked list
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert a node at a specific position in the linked list
    def insertAtIndex(self, data, position):
        new_node = Node(data)
        current_node = self.head
        count = 0

        # Traverse to the desired position
        while current_node and count < position - 1:
            current_node = current_node.next
            count += 1

        # Insert the new node
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node

    # Insert a node at the end of the linked list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Create an instance of LinkedList
linked_list = LinkedList()

# Take input from the user to add elements to the linked list
n = int(input("Enter the number of elements: "))
for _ in range(n):
    value = int(input("Enter a value: "))
    linked_list.insertAtEnd(value)

# Print the linked list
print("Linked List:")
linked_list.printLL()
