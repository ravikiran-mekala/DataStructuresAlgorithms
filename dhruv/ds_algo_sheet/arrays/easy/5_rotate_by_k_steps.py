"""Rotate Array by k Steps
   Explanation: Reversal trick or modular index write.
   Example: [1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]
"""


def _cycle_replace(arr, k, visited, idx):
    # You can also use an empty array and do it instead of in-place
    N = len(arr)
    current_value = arr[idx]
    while idx not in visited:
        visited.add(idx)
        next_idx = (idx + k) % N
        next_value = arr[next_idx]
        arr[next_idx] = current_value
        idx = next_idx
        current_value = next_value


def rotate_by_k(arr, k):
    N = len(arr)
    if N == 0:
        return arr
    k %= N  # Important to remove any useless rotations.
    if k == 0:
        return arr

    visited = set()
    for i in range(N):
        if i not in visited:
            _cycle_replace(arr, k, visited, i)
    return arr


print(rotate_by_k([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_by_k([1, 2, 3, 4], 2))
