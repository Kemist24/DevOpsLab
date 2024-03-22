def linear_search(data, target):
  """
  This function implements a linear search algorithm.

  Args:
      data: A list of numbers to search through.
      target: The number to search for.

  Returns:
      The index of the target number in the list if found, otherwise -1.
  """

  for i, num in enumerate(data):
    if num == target:
      return i

  return -1

# Example usage
data = [1, 5, 8, 9, 2]
target = 8

result = linear_search(data, target)

if result != -1:
  print(f"The target number {target} was found at index {result}")
else:
  print(f"The target number {target} was not found in the list")
