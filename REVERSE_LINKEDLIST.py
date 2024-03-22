class Node:
  """
  Represents a node in a linked list.
  """
  def __init__(self, data):
    self.data = data
    self.next = None

def reverse_linked_list(head):
  """
  Reverses a singly linked list.

  Args:
      head: The head node of the linked list.

  Returns:
      The head node of the reversed linked list.
  """
  prev = None
  current = head
  while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  return prev

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Print the original list
current = head
while current:
  print(current.data, end=" -> ")
  current = current.next

print("None")

# Reverse the list
reversed_head = reverse_linked_list(head)

# Print the reversed list
current = reversed_head
while current:
  print(current.data, end=" -> ")
  current = current.next

print("None")