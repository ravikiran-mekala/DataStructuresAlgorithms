"""Implement Quick Sort
   Explanation: Partition around a pivot and recurse on partitions.
   Example: [10,7,8,9,1,5] → [1,5,7,8,9,10]
"""


def arrange_around_pivot(arr, lo, hi):
    pivot = arr[hi]
    i = lo-1
    for j in range(lo, hi+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i

# TC: O(n^2), SC: O(1)


def quick_sort(arr, lo, hi):
    if lo >= hi:
        return
    pvt_idx = arrange_around_pivot(arr, lo, hi)
    quick_sort(arr, lo, pvt_idx-1)
    quick_sort(arr, pvt_idx+1, hi)


def quick_sort_main(arr):
    if len(arr) == 1:
        return
    quick_sort(arr, 0, len(arr)-1)


print("Testing Quick Sort")

arr1 = [5, 1, 4, 2, 8]
quick_sort_main(arr1)
print(arr1)

arr2 = [3]
quick_sort_main(arr2)
print(arr2)
