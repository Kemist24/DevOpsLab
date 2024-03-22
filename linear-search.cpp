#include <iostream>

int linearSearch(int arr[], int n, int x) {
  """
  Searches for an element x in the array arr of size n.

  Args:
      arr: The array to be searched.
      n: The size of the array.
      x: The element to be searched.

  Returns:
      The index of x in arr if found, -1 otherwise.
  """
  for (int i = 0; i < n; i++) {
    if (arr[i] == x) {
      return i;
    }
  }
  return -1;
}

int main() {
  int arr[] = {2, 3, 4, 10, 40};
  int n = sizeof(arr) / sizeof(arr[0]);
  int x = 10;

  int result = linearSearch(arr, n, x);

  if (result == -1) {
    std::cout << "Element is not present in array" << std::endl;
  } else {
    std::cout << "Element is present at index " << result << std::endl;
  }

  return 0;
}
