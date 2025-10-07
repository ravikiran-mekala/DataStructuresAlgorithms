"""
Balanced Parentheses
   Explanation: Stack to match brackets.
   Example: {[()]} → valid
"""


def is_balanced_parenthesis(s) -> bool:
    hm = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    st = []
    for i in s:
        if i not in hm:
            st.append(i)
        else:
            if not st or st[-1] != hm[i]:
                return False
            st.pop()
    return len(st) == 0
