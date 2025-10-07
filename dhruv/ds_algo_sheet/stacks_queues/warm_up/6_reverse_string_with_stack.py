"""Reverse String with Stack

"""

def reverse_string_with_st(s):
    st = []
    for i in s:
        st.append(i)
    
    ans = []
    for _ in range(len(st)):
        ans.append(st.pop())
    
    return ''.join(ans)
