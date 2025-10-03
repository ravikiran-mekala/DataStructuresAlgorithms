"""Find second largest distinct element in an array.
   Approach: Track max and second max in one pass.
   Example: [2,3,1,5,4] → 4. If no second distinct, return None.
"""


def find_second_largest(arr):
    first_mx = float('-inf')
    second_mx = float('-inf')
    for value in arr:
        if value > first_mx:
            second_mx = first_mx
            first_mx = value
        elif value != first_mx and value > second_mx:
            second_mx = value
    return None if second_mx == float('-inf') else second_mx


print(find_second_largest([2, 3, 1, 5, 4]))
