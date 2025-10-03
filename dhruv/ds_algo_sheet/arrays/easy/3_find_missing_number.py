"""Find Missing Number in 0..n
   Explanation: Use XOR or sum difference.
   Example: [3,0,1] → 2
"""


def sum_difference(arr):
    min_num = min(arr)
    max_num = max(arr)
    return sum(list(range(min_num, max_num+1))) - sum(arr)


print(sum_difference([3, 0, 1]))


def xor_solution(arr):
    xor_all = 0
    N = len(arr)
    for i in range(0, N+1):
        xor_all ^= i

    for i in arr:
        xor_all ^= i

    return xor_all

print(xor_solution([3, 0, 1]))
