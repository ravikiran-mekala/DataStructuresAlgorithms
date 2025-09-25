"""Implement Linear Search
   Explanation: Scan array sequentially to find target.
   Example: [4,2,7,1,9], target=7 → index=2
"""
# TC: O(N), SC: O(1)
def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

print(find_index([4,2,7,1,9], 7))
print(find_index([4,2,7,1,9], 0))