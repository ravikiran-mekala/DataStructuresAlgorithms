"""Move All Zeros to End
   Explanation: Stable two-pointer compaction of non-zeros.
   Example: [0,1,0,3,12] → [1,3,12,0,0]

Here the pointers are not starting from the ends but in the same direction (0->N)
"""


def move_zeros_to_end(arr):
    write = 0
    N = len(arr)
    for i in range(N):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1
    while write < N:
        arr[write] = 0
        write += 1


arr = [0, 1, 0, 3, 12]
move_zeros_to_end(arr)
print(arr)

arr = [0, 0, 0, 0, 0]
move_zeros_to_end(arr)
print(arr)
