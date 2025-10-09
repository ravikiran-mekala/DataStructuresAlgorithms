"""Check Palindrome
   Explanation: Compare from both ends.
   Example: racecar → true
"""

def check_palin(s):
    return s == s[::-1]

print(check_palin("abba"))