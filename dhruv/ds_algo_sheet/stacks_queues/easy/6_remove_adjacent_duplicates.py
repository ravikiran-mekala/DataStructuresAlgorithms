"""Remove Adjacent Duplicates
   Explanation: Pop matching neighbors.
   Example: abbaca → ca
"""

def remove_adjacent_dups(s):
    st = []
    for i in s:
        if st and st[-1] == i:
            st.pop()
        else:
            st.append(i)
    
    return ''.join(st)


s = "abbaca"
print(remove_adjacent_dups(s))
