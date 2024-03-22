def insertion_sort(arr):
  """
  Sorts an array in ascending order using insertion sort.

  Args:
      arr: The array to be sorted.
  """
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # Move elements of arr[0..i-1], that are greater than key, to one position ahead
    # of their current position
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
