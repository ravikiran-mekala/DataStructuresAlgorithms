"""Implement Bubble Sort
   Explanation: Swap adjacent out-of-order elements repeatedly.
   Example: [5,1,4,2,8] → [1,2,4,5,8]
"""

# TC: O(n^2), SC: O(1)
def bubble_sort(arr):
    swapped = True
    for _ in range(len(arr)):
        if not swapped:
            break
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr


print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([3]))
