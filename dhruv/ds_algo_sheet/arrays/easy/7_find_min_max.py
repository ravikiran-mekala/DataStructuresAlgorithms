"""Find Min and Max
   Explanation: Linear scan updating running min/max.
   Example: [5,7,2,9,1] → (1,9)
"""
import math
def find_min_max(arr):
    min_nm, max_nm = math.inf, -math.inf
    for i in arr:
        min_nm = min(min_nm, i)
        max_nm = max(max_nm, i)
    return min_nm, max_nm

print(find_min_max([5,7,2,9,1]))
