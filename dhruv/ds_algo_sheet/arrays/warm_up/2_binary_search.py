""" Implement Binary Search
   Explanation: Halve a sorted array repeatedly to locate the target.
   Example: [1,3,5,7,9], target=5 → index=2
"""

# TC: O(log N), SC: O(1)
def find_index_bs(arr, target):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print(find_index_bs([4,2,7,1,9], 7))
print(find_index_bs([4,2,7,1,9], 0))
print(find_index_bs([5], 5))