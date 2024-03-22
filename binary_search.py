def binary_search(data, target):
  """
  This function implements a binary search algorithm.

  Args:
      data: A sorted list of numbers to search through.
      target: The number to search for.

  Returns:
      The index of the target number in the list if found, otherwise -1.
  """

  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2

    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

# Example usage (assuming the data list is already sorted)
data = [1, 5, 8, 9, 12]
target = 8

result = binary_search(data, target)

if result != -1:
  print(f"The target number {target} was found at index {result}")
else:
  print(f"The target number {target} was not found in the list")
