"""Evaluate Postfix (RPN)
   Explanation: Stack-based evaluation.
   Example: 23+ → 5
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        def add(x, y): return x+y
        def sub(x, y): return x-y
        def div(x, y): return int(x/y)
        def mul(x, y): return x*y
        ops = {
            "+": add, "-": sub, "/": div, "*": mul
        }
        for i in tokens:
            if i not in ops:
                st.append(int(i))
            else:
                y = st.pop()
                x = st.pop()
                st.append(ops[i](x, y))
        return int(st[0])
