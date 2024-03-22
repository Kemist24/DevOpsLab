# def binary(arr,low,high,key):
#     mid=(low+high)//2
#     if(arr[mid]==key):
#         print("element found at",mid+1)
#     elif(arr[mid]<key):
#         return binary(arr,mid+1,high,key)
#     elif(arr[mid]>key):
#         return binary(arr,low,mid-1,key)
#     else:
#         print("element not founf")

# arr=[1,2,3,4,5,6,7]
# key=1
# n=len(arr)-1
# binary(arr,0,n,key)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input("enter the no. you want to search"))
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at  {result+1}")
else:
    print("Element not found")
