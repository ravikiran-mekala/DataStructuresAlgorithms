"""
Reverse a String
   Explanation: Two-pointer swap of characters.
   Example: hello → olleh
"""

def reverse_string(s):
    chars = list(s)
    l, r = 0, len(chars) - 1

    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1
    
    return ''.join(chars)

ans = reverse_string("hello")
print(ans)
