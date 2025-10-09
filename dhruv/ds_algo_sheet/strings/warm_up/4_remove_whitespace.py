"""
Remove Whitespace
Explanation: Filter out space characters.
Example: 'a b c' → 'abc'
"""

def remove_whitespace(s):
    ans = []
    for i in s:
        if i != ' ':
            ans.append(i)
    return ''.join(ans)

print(remove_whitespace('a b c  '))