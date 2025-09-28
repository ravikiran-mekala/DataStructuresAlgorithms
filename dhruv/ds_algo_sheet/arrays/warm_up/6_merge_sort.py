"""Implement Merge Sort
   Explanation: Divide, sort halves, and merge (O(n log n)).
   Example: [38,27,43,3,9,82,10] → [3,9,10,27,38,43,82]
"""


def merge(arr, lo, mid, hi):
    """
    Corrected merge function using temporary arrays to avoid data corruption
    This is the standard approach for merge sort
    """
    # Create temporary arrays for left and right subarrays
    left = arr[lo:mid + 1]    # Elements from lo to mid
    right = arr[mid + 1:hi + 1]  # Elements from mid+1 to hi

    # Pointers for left array, right array, and main array
    i = j = 0  # Start of left and right arrays
    k = lo     # Start position in main array

    # Merge the temporary arrays back into arr[lo..hi]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left[], if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right[], if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, lo, hi):
    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid+1, hi)
        merge(arr, lo, mid, hi)

# Wrapper function for easier use

# TC: O(n logn), SC: O(n)
def merge_sort_easy(arr):
    """Easy-to-use wrapper that doesn't require lo and hi parameters"""
    if len(arr) <= 1:
        return arr
    merge_sort(arr, 0, len(arr) - 1)
    return arr


# Test cases
print("=== Testing Corrected Merge Sort ===")

arr1 = [5, 1, 4, 2, 8]
print(f"Before: {arr1}")
merge_sort(arr1, 0, len(arr1) - 1)
print(f"After:  {arr1}")

arr2 = [3]
print(f"\nSingle element - Before: {arr2}")
merge_sort(arr2, 0, 0)
print(f"Single element - After:  {arr2}")

# More test cases
arr3 = [38, 27, 43, 3, 9, 82, 10]
print(f"\nLarger array - Before: {arr3}")
merge_sort_easy(arr3)
print(f"Larger array - After:  {arr3}")

arr4 = [5, 4, 3, 2, 1]
print(f"\nReverse sorted - Before: {arr4}")
merge_sort_easy(arr4)
print(f"Reverse sorted - After:  {arr4}")
