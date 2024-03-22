
class Node:
  """
  Represents a node in a doubly linked list.
  """
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  """
  Represents a doubly linked list.
  """
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_beginning(self, data):
    """
    Inserts a new node at the beginning of the list.
    """
    new_node = Node(data)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def traverse(self):
    """
    Traverses the list and prints the data of each node.
    """
    current = self.head
    while current:
      print(current.data, end=" <-> ")
      current = current.next
    print("None")

# Example usage
my_list = DoublyLinkedList()
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)

my_list.traverse()