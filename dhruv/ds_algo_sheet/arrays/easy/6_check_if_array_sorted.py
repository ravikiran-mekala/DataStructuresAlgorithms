"""Check if Array is Sorted
    Explanation: Ensure non-decreasing order across neighbors.
   Example: [1,2,3,4,5] → true
"""


def check_if_sorted(arr):
    N = len(arr)
    for i, j in zip(range(N), range(1, N)):
        if arr[i] > arr[j]:
            return False
    return True


print(check_if_sorted([1, 2, 3, 4, 5]))
print(check_if_sorted([1, 2, 4, 4, 5]))
print(check_if_sorted([1, 2, 10, 4, 5]))
