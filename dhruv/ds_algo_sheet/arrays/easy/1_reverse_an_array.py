"""Reverse an Array
   Explanation: Use two pointers to swap from ends inward.
   Example: [1,2,3,4,5] → [5,4,3,2,1]
   """

def reverse(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1

arr = [1,2,3,4,5]
reverse(arr)
print(arr)