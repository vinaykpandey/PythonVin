"""
A simple approach is to do linear search, i.e

Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
"""
# linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def linear_search(arr, n, e):
    for i in range(0, n):
        if (arr[i] == e):
            return i
    return -1


# Driver Code
l = [2, 3, 4, 10, 40]
e = 10
n = len(l)
result = linear_search(l, n, e)
if result == -1:
    print("Element is not present in list")
else:
    print("Element is present at index: ", result)
