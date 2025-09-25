"""Implement Selection Sort
   Explanation: Select the minimum each pass and place at front.
   Example: [64,25,12,22,11] → [11,12,22,25,64]
   """
import math

# TC: O(n^2), SC: O(1)
def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(selection_sort([5, 1, 4, 2, 8]))
print(selection_sort([3]))
