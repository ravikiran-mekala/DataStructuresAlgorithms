"""Implement Insertion Sort
   Explanation: Insert each element into the sorted prefix.
   Example: [12,11,13,5,6] → [5,6,11,12,13]
   """

def insertion_sort(arr):
    for current_card in range(1, len(arr)):
        card_value = arr[current_card]

        checking_position = current_card - 1

        # assuming all the elements before current_card are already sorted.
        # start with one element as sorted.
        while checking_position >= 0 and arr[checking_position] > card_value:
            arr[checking_position + 1] = arr[checking_position] # shifting to the right
            checking_position = checking_position - 1
        
        arr[checking_position + 1] = card_value
    
    return arr

print(insertion_sort([5, 1, 4, 2, 8]))
print(insertion_sort([3]))
